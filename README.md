<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-38782-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-26 01:28 ｜ **论文总数 / Total Papers**: 38782（近 30 天 / Recent 30 days: 4112）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 38782 篇论文（含摘要、分类筛选、搜索）/ View all 38782 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 732
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 709
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 59
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 180
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 571
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 681
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4684
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 94
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1359
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 159
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 4168
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 4116
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3854
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 4219
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 811
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 126
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 77
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 472
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 11644

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4112 篇，完整 38782 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4112 papers from the last 30 days (with date, authors & abstract). For the full list of 38782 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 5 papers

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

- **2026-11-22** — Honghao Feng, Shanhan Qu, Kai Tong et al. — [Adaptation or Poisoning? Security Risks of Conversational Test-Time Learning in Large Language Models](http://arxiv.org/abs/2611.29532v1)
  <details><summary>📄 Abstract</summary>
  Test-time learning (TTL) enables large language models to adapt to unlabeled inputs during deployment. The model updates a lightweight adapter by minimizing the next-token prediction loss on the input it receives. When these updates persist across conversation turns, every user query serves both as the request answered in the current turn and as adaptation data for later turns. By choosing the queries used for adaptation, an attacker can influence parameter updates and weaken safety alignment th...
  </details>

- **2026-11-22** — Saadh Jawwadh — [From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](http://arxiv.org/abs/2611.29303v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of Large Language Model (LLM) research makes it increasingly difficult to distinguish incremental refinements from true paradigm shifts. This review evaluates 22 of the most influential publications spanning nearly three decades (1997-2026), organized through a causal, chronologically anchored taxonomy centered on the author's birth year (1999). Beginning "before 1999" with how recurrent neural networks (RNNs) forgot earlier context (much like forgetting Chapter 1 by the ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 11 papers

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

- **2026-11-23** — Peter Horvath, Ilia Shumailov, Zhuoran Liu et al. — [FATCAT: Fault Injection Attacks Targeting Chip-level Alignment](http://arxiv.org/abs/2611.31129v1)
  <details><summary>📄 Abstract</summary>
  Model alignment is the primary safety and security mechanism for enforcing refusal of malicious prompts in modern foundation models; yet, existing adversarial evaluations implicitly assume underlying hardware integrity. In this paper, we present FATCAT, the first physical fault-injection attacks capable of eliminating refusal in modern large language and vision-language models. Specifically, we present a non-invasive electromagnetic (EM) fault injection attack targeting GPU-accelerated Systems-o...
  </details>

- **2026-11-23** — Kaixuan Li, Wenbo Guo, Sen Chen et al. — [Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills](http://arxiv.org/abs/2611.30932v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are reusable packages that extend a large language model (LLM) agent with scripts, third-party dependencies, and natural-language instructions. An agent builds a skill's arguments from user requests and untrusted external content, so a flaw left by a benign author can escalate a prompt injection to code execution. Existing studies target malicious skills or a single attack vector, and none tests whether an agent can reach such flaws. We present the first registry-scale empirical stu...
  </details>

- **2026-11-23** — Pascal Joos, Michael Pradel — [AgentBouncer: Defending Software Engineering Agents via Dynamic System-Call Mediation](http://arxiv.org/abs/2611.30621v1)
  <details><summary>📄 Abstract</summary>
  Software engineering (SE) agents can complete diverse engineering tasks by interacting with the development environment via tools that access files, run commands, and download resources. Unfortunately, the same ability that makes SE agents useful also makes them prone to performing unintended malicious actions through prompt injections, malicious tools, or supply-chain attacks. Existing defenses that analyze the agent trajectory may fail to detect such attacks, as they inspect only the initial p...
  </details>

- **2026-11-23** — Jiaqi Rong, Yunchen Lu, Lihai Nie et al. — [Conartist: Adaptive Agentic Red-Teaming of Computer-Using Agents against Multi-Step Prompt Injection](http://arxiv.org/abs/2611.29977v1)
  <details><summary>📄 Abstract</summary>
  Harnesses secure Computer-Using Agents by enforcing security constraints and defending against prompt injection attacks. However, we find that two core security mechanisms of agent harnesses remain vulnerable. First, consistency checking prevents agents from deviating from legitimate user objectives, while attackers can bypass it by embedding malicious actions that appear logically consistent with legitimate task execution. Second, risk auditing proactively examines high-risk operations. Yet, th...
  </details>

- **2026-11-22** — Brijesh Dongol — [Relativising Integrity and Robustness: Prompt Injection and Partitioned Enclaves](http://arxiv.org/abs/2611.29802v1)
  <details><summary>📄 Abstract</summary>
  Relative security (RS) judges a system against a reference system, but has only been applied to confidentiality. We introduce relative integrity (RI), which states that every behaviour a system exhibits under an attacker's influence must be one the reference can exhibit for the same trusted inputs. RS and RI each choose their own reference runs, so together they accept attacks whose leak and effects the reference reproduces only in different runs. We therefore develop a further property, relativ...
  </details>

- **2026-11-22** — Haichuan Zhang, Zhiyuan Zhong, Shih-Chieh Dai et al. — [Benchmarking Web Agent Defenses Against Adaptive Visual Prompt Injection](http://arxiv.org/abs/2611.29268v1)
  <details><summary>📄 Abstract</summary>
  Multimodal web agents automate website interactions but remain vulnerable to visual prompt injection (VPI), where malicious webpage content manipulates their visual processing and induces unintended actions. Although several defenses focus on detecting injected instructions in screenshots, malicious destinations such as phishing URLs embedded in HTML can remain hidden yet accessible through agent interactions. Existing evaluations have also not sufficiently examined adaptive attackers who know t...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-11-23** — Komal Thareja, Mats Rynge, Anirban Mandal et al. — [Evaluating Frontier-Model Agent Skills with Open-Weight Models in a Science Gateway](http://arxiv.org/abs/2611.31480v1)
  <details><summary>📄 Abstract</summary>
  Scientific analyses that span many jobs and computing sites depend on workflow management systems to run reliably, but writing a production workflow requires expertise in such a system, which many domain scientists do not have. Coding agents can supply this expertise when they are guided by skills and packaged procedures for recurring tasks. We wrote skills and specialist agents for the Pegasus workflow management system with a frontier model, and the PegasusAI Studio science gateway offers them...
  </details>

- **2026-11-23** — Kang Yang, Kevin Ying, Xiaojing Liao et al. — [Demystifying Detectors Guarding Agent Skill Hubs](http://arxiv.org/abs/2611.30913v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills has gained widespread adoption as an open standard for extending agent capabilities. To facilitate skill sharing, public skill hubs have grown in popularity and increasingly rely on automated security detectors to identify malicious skills at scale. Yet, the effectiveness and limitations of these detectors remain insufficiently understood. To fill this gap, we present the first systematic study of four hub-adopted and two community-provided malicious skill detectors on 1477 agent sk...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-11-24** — Guowei Guan, Yurong Hao, Jiaming Zhang et al. — [C3H: Compression-to-Consensus Criteria Hijacking in Multimodal LLM Recommender Systems](http://arxiv.org/abs/2611.32780v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are transforming recommender systems into content-aware decision systems. In these systems, multimodal compression and cross-modal fusion are often viewed as robustness-enhancing mechanisms against content manipulation, as compression can filter noisy signals and cross-modal consensus can suppress inconsistent anomalies. We challenge this assumption by showing that the same process can expose a compression-to-consensus (C2C) bias in ranking decisions. Sig...
  </details>

- **2026-11-24** — Sirui He, Chi Zhang — [ADE: A Zero-Training Unlearning Method for Latent World Models](http://arxiv.org/abs/2611.31998v1)
  <details><summary>📄 Abstract</summary>
  Latent world models learn compact recurrent dynamics from offline trajectories, yet deployed simulators can retain backdoor triggers or stale transitions from outdated physical regimes. Existing unlearning methods fail in autoregressive physics: gradient updates distort latent manifolds and compound rollout drift, naive output zeroing suppresses valid control responses on trigger onset, and single-step deletion leaves corruption inside recurrent hidden states. We propose Analytical Dynamics Exci...
  </details>

- **2026-11-23** — Boyd Kane, Jo J. Jiao, Elizabeth Donoway et al. — [Uncovering Hidden Behaviours in Language Models via Limited-Parameter Finetuning](http://arxiv.org/abs/2611.30672v1)
  <details><summary>📄 Abstract</summary>
  Large language models can have behaviours which only arise in hard-to-anticipate contexts. These hidden behaviours pose a challenge to alignment audits, which seek to uncover problematic model behaviour but are limited by the scenarios the auditor can anticipate. To address this challenge, we explore limited-parameter finetuning (LPF) on examples of a target behaviour. While training 3-25% of LoRA parameters, LPF reveals whether the model has a hidden behaviour, even when standard behavioural ev...
  </details>

- **2026-11-22** — Soumita Chatterjee, Sudip Ghosh, Tamal Ghosh et al. — [Lightweight Spectral Subspace Filtering for Trojan-Resilient AI Inference Engines](http://arxiv.org/abs/2611.29734v1)
  <details><summary>📄 Abstract</summary>
  Backdoor attacks pose a significant security threat to deep neural networks (DNNs) deployed on AI inference engines and hardware accelerators. By embedding hidden triggers during training, these attacks induce malicious behavior while maintaining high accuracy on benign inputs. Multi-trigger backdoor attacks are particularly challenging to detect and mitigate because of the distributed and stealthy nature of their effects. To address this challenge, this paper proposes a training-free Spectral S...
  </details>

- **2026-11-22** — Ramak Nassiri, Sujan Kumar Reddy Challa, Feroz Ahmed et al. — [Attacking Tabular Foundation Models: An Experimental Taxonomy of Context Poisoning and Test-Time Evasion](http://arxiv.org/abs/2611.29627v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models condition predictions on labeled examples supplied at inference time, creating an attack surface that differs from conventional model training. We study four manipulation families (label flipping, backdoor context poisoning, clean-label context selection, and test-time evasion) and organize them by attack stage, label consistency, and distributional realism. TabPFN-2.5, TabICL, and XGBoost are evaluated on CIC-IDS2017 and N-BaIoT using a common preprocessing and evaluat...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-11-24** — Tigran Fahradyan, Riccardo Ali, Sergio Calvo-Ordoñez et al. — [Understanding the Importance of Massive Activations through Adversarial Robustness](http://arxiv.org/abs/2611.32585v1)
  <details><summary>📄 Abstract</summary>
  A common occurrence in Large Language Models (LLMs) is the emergence of so-called massive activations. This phenomenon is well known in the literature and has been connected to attention sinks, representational compression, as well as signal propagation. However, the reasons and consequences for their appearance are not yet well understood. In this paper, we explain the role of massive activations in deep learning by showing that they are connected to the region migration phenomenon in delayed r...
  </details>

- **2026-11-23** — Adam Wróbel, Jacek Tabor, Bartosz Zieliński et al. — [Spec$^2$R: Recovering Emergent Properties in Supervised Vision Transformers](http://arxiv.org/abs/2611.31589v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) have achieved strong performance across computer vision tasks, but the quality of their learned representations differs drastically depending on the training paradigm. While self-supervised ViTs often demonstrate emergent properties, such as object-aligned patch representations and attention maps, supervised ViTs typically lack these properties, even when trained with strong data augmentations. Understanding the origin of this difference is important for explaining and...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 29 papers

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

- **2026-11-23** — Sahar Askari, Amin Golnari — [Demographic Encoding is Not Exposure: Fairness and Privacy in Chest X-ray Foundation Models](http://arxiv.org/abs/2611.31014v1)
  <details><summary>📄 Abstract</summary>
  Medical foundation models encode patient demographics and can reveal whether a patient was in the training set, and these properties are often treated as one problem. We tested whether they are aligned by measuring demographic encoding, diagnostic fairness gaps and membership-inference vulnerability on the same models. We trained 200 linear or multilayer-perceptron (MLP) heads on frozen BiomedCLIP, DINOv2 and RAD-DINO embeddings, with three seeds, and audited them on CheXpert and NIH ChestX-ray1...
  </details>

- **2026-11-23** — Fadel M. Megahed, Ying-Ju Chen, Yamin Dahwich et al. — [What Quality Engineers Need to Know About Generative AI: Structured Data Extraction](http://arxiv.org/abs/2611.30778v1)
  <details><summary>📄 Abstract</summary>
  In this expository paper, we explain how quality engineers can use large language models (LLMs) and vision-language models (VLMs) for structured data extraction. We introduce the relevant concepts, discuss structured extraction from a measurement-system perspective, and demonstrate its implementation in R and Python. We then present two freely available web-based applications (apps): (a) extracting information from automotive recall notices and (b) monitoring quality engineering research on arXi...
  </details>

- **2026-11-23** — Marco Pichler, Patrick Podest, Günter Klambauer et al. — [Time Series Foundation Models on the Edge](http://arxiv.org/abs/2611.30404v1)
  <details><summary>📄 Abstract</summary>
  Time series foundation models (TSFMs) forecast zero-shot with accuracy exceeding that of task-specific models, and the smaller ones fit on edge devices. Operational deployments must refresh their forecast as new observations arrive, and privacy and latency requirements often force this refresh onto resource-constrained edge devices. To serve as a forecasting system there, a TSFM must refresh quickly, keep latency and peak memory bounded as the stream grows, and retain its accuracy as the observe...
  </details>

- **2026-11-23** — Gwangui Hong, Seonho An, Seonkyu Lim et al. — [PseuDRAGON: Knowledge-Guided Local LLMs for Financial-Data Pseudonymization in Closed Networks](http://arxiv.org/abs/2611.30353v1)
  <details><summary>📄 Abstract</summary>
  Staff pseudonymizing financial data in closed networks must interpret abbreviated column names, identify personal information, and choose processing methods. Local language models can assist, but may give different labels for the same input. PseuDRAGON keeps confirmed judgments and corrections outside a fixed model and reuses them through exact-name lookup and learned rules. For expert review, the workflow searches institutional policy, national privacy law, then international sources. Across 92...
  </details>

- **2026-11-23** — Xinghe Chen, Haichao Sha, Zihao Wang et al. — [AutoClip-DPZO: Practical Private Clipping Selection for Differentially Private Zeroth-Order LLM Fine-Tuning](http://arxiv.org/abs/2611.30352v1)
  <details><summary>📄 Abstract</summary>
  Differentially private zeroth-order optimization (DPZO) is a promising approach for privacy-preserving LLM fine-tuning, offering exceptional memory efficiency. However, its utility is highly sensitive to the clipping threshold $C$, a key DP-specific hyperparameter that controls the trade-off between noise injection and clipping bias. Existing DPZO methods typically tune $C$ by repeatedly evaluating candidate values and reporting the best result, which is computationally expensive and incurs addi...
  </details>

- **2026-11-23** — Cheng Guo, Qiming Cao, Pu Perry Wang et al. — [OmniSenMo: A Unified Multisensory Language Model for Generalizable Human Motion Estimation, Understanding, and Prediction](http://arxiv.org/abs/2611.30176v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) estimate, understand, and predict human motion, but mainly from RGB cameras. Depth, LiDAR, mmWave, and WiFi complement RGB under poor lighting, through occlusions, and in privacy-sensitive applications, but existing multisensory models cover only some of these sensing tasks. Covering all of them from any sensor subset is challenging, since the tokens of heterogeneous sensors are semantically inconsistent and spatially misaligned, paired multisensory data ...
  </details>

- **2026-11-23** — Linxi Xie, Chonghua Liao, Mengxuan Wu et al. — [WASP: Continual Weight Adaptation for Streaming LLM Personalization](http://arxiv.org/abs/2611.30134v1)
  <details><summary>📄 Abstract</summary>
  Personalized large language models (LLMs) should continually adapt to users' evolving preferences. Yet extracting preference changes from noisy interaction histories while supporting inexpensive updates remains challenging. We introduce WASP (Weight Adaptation for Streaming Personalization), a recurrent framework that captures fine-grained preferences directly from raw user interactions and generates personalized LoRA adapters without expensive per-user optimization. Specifically, WASP achieves ...
  </details>

- **2026-11-22** — Yuhao Wang, Shengfang Zhai, Xinyu Zhou et al. — [AEP:Towards Trustworthy Agent Communication, Networking, and Collaboration](http://arxiv.org/abs/2611.29598v1)
  <details><summary>📄 Abstract</summary>
  As privately owned agents become increasingly capable, collaboration in open agent networks is limited by partial topology knowledge, ownership boundaries, and the risk of exposing or contaminating private context. Existing agent-to-agent protocols are useful when collaborators are already known, while shared-memory and broadcast-based systems rely on visibility and trust assumptions that do not hold in decentralized, low-trust environments. We introduce Open Private Agent Collaboration (OPAC), ...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-11-23** — Sina Abdollahi, Amir Al Sadi, Marios Kogias et al. — [Airlock: Robust Sandboxing and Governance of Rogue Agents](http://arxiv.org/abs/2611.31010v1)
  <details><summary>📄 Abstract</summary>
  Recent incidents involving agents bypassing sandboxing and network isolation have raised concerns about existing agent harnesses, prompting frontier labs such as OpenAI to reevaluate the security of their training platforms. Incident reviews show that determined agents can escape processes, containers, and VMs, or bypass their isolation through advanced side and covert channels. Follow-up audits also found that some agents concealed their actions by disabling monitoring and tampering with logs. ...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 11 papers

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

- **2026-11-23** — Magnus Saebo, Francesco Piccoli, Maxwell Watson et al. — [CyberDualEval: Measuring Dual-Use Cyber Risks in Frontier Language Models](http://arxiv.org/abs/2611.30533v1)
  <details><summary>📄 Abstract</summary>
  While frontier language models are becoming capable cybersecurity assistants, they also create a dual-use cyber risk: the same capabilities that help defenders identify and analyze vulnerabilities can similarly help attackers weaponize them. Existing cyber benchmarks measure either raw offensive capability or generic refusal behavior, overlooking the dual-use cyber assessment of preserving benign security utility while refusing assistance that materially advances misuse. We introduce CyberDualEv...
  </details>

- **2026-11-23** — Ziyuan Chen, Yueming Lyu, Songze Li et al. — [Bounded Autonomy: A Trust-Anchored Defense Against Resource-Exhaustion Attacks on Tool-Augmented LLM Agents](http://arxiv.org/abs/2611.30383v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented Large Language Model (LLM) agents are vulnerable to resource-exhaustion attacks that amplify model-token consumption through persistent context amplification, large tool output amplification, and error-induced agentic loops. Despite growing attention to agent security and resource-abuse risks, a systematic defense framework specifically targeting these attacks remains lacking. Meanwhile, existing general-purpose agent defense frameworks, which address a broader range of security t...
  </details>

- **2026-11-22** — Tong Li, Chenru Wang, Chris Thomas et al. — [Model Immunization Cannot Reliably Protect Models from Harmful Adaptation](http://arxiv.org/abs/2611.29815v1)
  <details><summary>📄 Abstract</summary>
  Efficient fine-tuning techniques have substantially reduced the cost of adapting open-weight models, enabling malicious actors to readily fine-tune them toward harmful capabilities. In response, model immunization modifies a pretrained checkpoint to resist subsequent adaptation toward designated harmful capabilities while preserving its utility and adaptability for benign tasks. Furthermore, a few immunization methods have sought to keep their protection robust to some changes in the attacker's ...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-11-24** — Guowei Zou, Beiwen Zhang, Haitao Wang et al. — [TeamFlowRL: Online Policy Optimization of Decentralized Flow Policies for Multi-Agent Coordination](http://arxiv.org/abs/2611.32645v1)
  <details><summary>📄 Abstract</summary>
  Complex cooperative tasks require coordinated multi-agent behavior. Offline generative policies learn expressive cooperative behaviors from trajectories but remain limited by fixed datasets. Online reinforcement learning can improve them through environment interaction. However, fine-tuning flow policies is difficult because action likelihoods are hard to compute. We propose TeamFlowRL, a two-stage framework that pretrains multi-agent flow policies offline and fine-tunes them online. We formulat...
  </details>

- **2026-11-23** — Zhongyuan Lyu, Xiaocong Xu — [Sequential Selection against an Adaptive Opponent](http://arxiv.org/abs/2611.30006v1)
  <details><summary>📄 Abstract</summary>
  Selecting a strategy by testing it against an opponent is common in game-playing AI, red-teaming of language models, and safety evaluations of AI agents. In many of these settings, the opponent adapts to what it observes, so a strategy that keeps winning in practice may already have stopped working by the time it is used. Motivated by these settings, we study a player who tries strategies in practice games against an adaptive opponent, decides when to stop, and then either selects one strategy f...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 56 papers

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

- **2026-11-23** — Xiao-Ming Wu, Kang Liao, Yuexiao Ma et al. — [Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness](http://arxiv.org/abs/2611.31201v1)
  <details><summary>📄 Abstract</summary>
  Frontier multimodal models exhibit extraordinary generalization in generating robot actions from observations and instructions, enabling a new paradigm in which they serve directly as policies within closed-loop robotic harnesses. However, the design principles of such harnesses, and the capabilities underlying their strong performance, remain unclear. We present Embo-Harness, a framework for systematically studying frontier-model-as-policy harnesses. We investigate four components of the roboti...
  </details>

- **2026-11-23** — Fareeha Amir — [SRCWDNet: Semantic-Relational Cross-Window Dual-Graph Network for Multi-Label Remote Sensing Scene Classification](http://arxiv.org/abs/2611.31135v1)
  <details><summary>📄 Abstract</summary>
  Multi-label remote sensing scene classification remains a challenging task due to complex spatial-spectral patterns, extreme class imbalance, and inter-label dependencies that are often insufficiently modeled. To address these challenges, we introduce a Semantic-Relational Cross-Window Dual-Graph Network (SRCWDNet), which integrates three key modules: (1) a Cross-Window Attention module that captures local and global visual context through learnable global tokens; (2) a Dual Label-Graph module t...
  </details>

- **2026-11-23** — M. Grecki, J. Branlard, M. Diomede et al. — [Optimization of Piezo Operation for Superconducting TESLA Cavities at EuXFEL](http://arxiv.org/abs/2611.31086v1)
  <details><summary>📄 Abstract</summary>
  Superconducting cavities with high-Q factor require precise tuning to match the RF frequency, ensuring stable electromagnetic fields and minimizing RF power consumption. At the European XFEL (EuXFEL) accelerator, TESLA cavities are tuned using slow tuners (step motors) for coarse adjustments and fast tuners (piezoelectric actuators) for fine-tuning and compensating disturbances such as Lorentz Force Detuning (LFD). Piezo actuators, critical to this system, require high-voltage (up to 100V) and h...
  </details>

- **2026-11-23** — Tomer Ashuach, Zorik Gekhman, Avi Caciularu et al. — [Can Latent Reasoning Drive LLM Outputs Without a Trace?](http://arxiv.org/abs/2611.31015v1)
  <details><summary>📄 Abstract</summary>
  LLMs typically solve complex tasks with chain-of-thought (CoT) reasoning, which is also the main tool for monitoring them for misaligned behavior. However, standard transformers can also solve tasks with complete latent reasoning (CLR), carrying out the whole task internally and outputting only the final answer. Theory bounds the depth of CLR, the number of sequential steps it can carry out, and recent work measured it to be shallow. In this work, we ask whether CLR is deep enough for a model to...
  </details>

- **2026-11-23** — José Antonio Carrillo, Timon Gutleb, Andrea Medaglia et al. — [A particle method for the space homogeneous Lenard-Balescu equation](http://arxiv.org/abs/2611.30808v1)
  <details><summary>📄 Abstract</summary>
  We propose a structure preserving particle method to numerically approximate the spatially homogeneous Lenard-Balescu equation for collisional plasmas. The Lenard-Balescu operator is an improvement of the Landau equation with a dielectric function taking the dynamic screening effect into account. Our particle method is based on the variational formulation of the Lenard-Balescu equation under suitable regularization analogous to the strategy followed for the Landau collision operator in [12]. The...
  </details>

- **2026-11-23** — Xianglong Shi, Nicu Sebe, Bernhard Schölkopf et al. — [PVFormer: Proper Velocity Transformer for Stable and Scalable Hyperbolic Representation Learning](http://arxiv.org/abs/2611.30785v1)
  <details><summary>📄 Abstract</summary>
  Hyperbolic representations have shown remarkable success on hierarchical and tree-like data, and Transformers have become a central architecture for representation learning. However, a principled construction of hyperbolic Transformers remains challenging because the self-attention layer decomposes into three coupled primitives, transformation, similarity, and aggregation, that should all respect the underlying geometry. Existing hyperbolic Transformer designs are typically built in the Poincaré...
  </details>

- **2026-11-23** — Hanne Say Eren, Ana Ezquerro, Ozan Özdenizci — [Object-Centric Differentiable Logic Networks for Abstract Visual Reasoning](http://arxiv.org/abs/2611.30736v1)
  <details><summary>📄 Abstract</summary>
  Human visual intelligence enables efficient reasoning capabilities on abstract visual problems with bounded cognitive resources and minimal experience, and yields remarkable generalization to novel problems with its ability to draw relational analogies and modular abstractions. In contrast, deep learning models require exhaustive task-specific training on large datasets, making them prone to exploiting visual shortcuts and resulting in poor generalization. While neuro-symbolic approaches attempt...
  </details>

- **2026-11-23** — Longan Wang, Yuang Shi, Chia Qian Tan et al. — [Faster, Smaller, and Better-Looking: Fast-GSVC for 2D Gaussian Video Coding](http://arxiv.org/abs/2611.30629v1)
  <details><summary>📄 Abstract</summary>
  2D Gaussians have emerged as a promising explicit representation for videos. However, fitting Gaussians to a video sequence requires substantial computation, resulting in long encoding times. In this work, we present Fast-GSVC, a 2D Gaussian video codec that accelerates encoding while improving rate-distortion performance. We identify the key bottlenecks in 2DGS training and accelerate optimization through improved initialization, smoother yet more aggressive parameter updates, coarse-to-fine pr...
  </details>

- **2026-11-23** — Gufeng Zhang, Yiru Zhao, Shengyu Liu et al. — [POMA: Beyond Final Flags -- Process-Level Evaluation of Base LLMs in Vulnerability Exploitation](http://arxiv.org/abs/2611.30590v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) evolve from text generation to autonomous software-engineering execution, automated vulnerability exploitability verification has emerged as a vital frontier in software quality assurance and security validation. Existing security benchmarks, however, largely judge models by binary pass/fail outcomes or coarse stage milestones. Such outcome-centric scoring obscures fine-grained failure dynamics across long-horizon execution and conflates the intrinsic capability o...
  </details>

- **2026-11-23** — Yuna Lee, Yulhwa Kim — [RAPID: Codec-Aware Video Decoding for Efficient Long-Video Understanding](http://arxiv.org/abs/2611.30557v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language models (VLMs) can process hour-long videos, but the large number of input frames incurs substantial inference overhead. Existing approaches to efficient long-video understanding largely overlook video decoding, which can take longer than LLM prefill. We propose RAPID (Reference- and Access-Point-Informed Decoding), a codec-aware framework that exploits information embedded in compressed bitstreams to reduce both frame decoding and selection costs. RAPID consists of two com...
  </details>

- **2026-11-23** — Hyunsu Ye, Hyunmin Choi, Jaehong Cho et al. — [ANOR: Scaling Sparse Attention with a GPU-PNM Computing Hierarchy](http://arxiv.org/abs/2611.30417v1)
  <details><summary>📄 Abstract</summary>
  Serving large language models with long contexts requires keeping the key-value (KV) cache of every request, which can exceed GPU memory capacity. Sparse attention reads only a small, query-dependent subset of this cache at each decoding step, yet must retain the full cache because later steps may select other entries. Processing-near-memory (PNM) devices attached through Compute Express Link (CXL) can hold the full cache and compute attention where it resides. Prior GPU-PNM systems for sparse a...
  </details>

- **2026-11-23** — Francesco Manigrasso, Fabrizio Lamberti, Lia Morra — [Boosting zero-shot learning through neuro-symbolic integration](http://arxiv.org/abs/2611.30358v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot learning (ZSL) aims to train deep neural networks to recognize objects from unseen classes, starting from a semantic description of the concepts. Neuro-symbolic (NeSy) integration refers to a class of techniques that incorporate symbolic knowledge representation and reasoning with the learning capabilities of deep neural networks. However, to date, few studies have explored how to leverage NeSy techniques to inject prior knowledge during the training process to boost ZSL capabilities. ...
  </details>

- **2026-11-23** — Xiangchao Chen, Zhiheng Lyu, Kai Zhang et al. — [VADE: A Verifiable Agent Data Engine from Professional Sources](http://arxiv.org/abs/2611.30202v1)
  <details><summary>📄 Abstract</summary>
  Language agents have shown their practical value, particularly in software engineering, where abundant public code and executable tests support training and evaluation at scale. Extending this success to other professional domains, such as law and finance, is not straightforward: many agent tasks involve open-ended analysis, making outcomes hard to verify and, in turn, hard to use as scalable supervision. As a result, high-quality tasks in these domains are still largely expert-authored, making ...
  </details>

- **2026-11-23** — Zehao Liu, Huashuo Lei, Xi Lin et al. — [EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution](http://arxiv.org/abs/2611.30004v1)
  <details><summary>📄 Abstract</summary>
  As AI models evolve from text and vision to physical agents, embodied AI faces a fundamentally different attack surface. Prior attacks on embodied systems have used crafted instructions, adversarial visual inputs, and training-time policy modifications; we study environment-only object rearrangements with unchanged models and instructions. We reveal an attack surface in safety-critical spatial relations among existing objects. An adversary who rearranges objects, without modifying instructions o...
  </details>

- **2026-11-23** — Rohit Singh, Nathaniel Weems — [Structure-Exploiting Hierarchical Retrieval for Long Narrative Documents: A Precision-Oriented Alternative to Learned Abstraction Trees](http://arxiv.org/abs/2611.29966v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation over book-length documents must locate a small, coherent set of passages inside tens of thousands of tokens. Flat dense retrieval ignores document structure; RAPTOR instead builds a hierarchy by recursively clustering and summarizing with a language model. We study a complementary design that exploits the native structure of a document: a two-level retriever that (i) selects chapters with a hybrid BM25+dense match over chapter recaps, (ii) runs a chapter-filtered d...
  </details>

- **2026-11-23** — Qingmei Li, Xiaoya Fan, Juepeng Zheng et al. — [SpectralRoute: Adaptive Spectral Routing for Training-Free Open-Vocabulary Hyperspectral Segmentation](http://arxiv.org/abs/2611.29919v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary semantic segmentation enables the recognition of arbitrary categories through natural language descriptions and has recently been extended from natural images to remote sensing. However, existing approaches primarily focus on three-channel optical imagery or limited-band multispectral data, while pretrained vision-language models (VLMs) struggle to directly exploit the rich spectral information of hyperspectral imagery (HSI) without additional adaptation. More importantly, differ...
  </details>

- **2026-11-22** — AbdulAziz AbdulGhaffar, Ashraf Matrawy — [Mitigating Nested GTP Attacks: A Closed-Loop eBPF Defense for 5G and Beyond Networks](http://arxiv.org/abs/2611.29756v1)
  <details><summary>📄 Abstract</summary>
  The evolving cellular networks continue to rely on the legacy GPRS Tunneling Protocol-User Plane (GTP-U) to encapsulate and route user data traffic across the data plane. Recent security research demonstrated that nested GTP-U (GTP-in-GTP) payload vulnerabilities enable a diverse range of attacks on victim users. To address this vulnerability, in this paper, we propose a closed-loop extended Berkeley Packet Filter (eBPF) and eXpress Data Path (XDP) defense to detect and mitigate nested GTP-U att...
  </details>

- **2026-11-22** — Xuanyi Lyu, Yuezhou Zhao, Qing Qin — [Which Loopholes Get Found? Predicting Reward Hacking of LLM Judges Before RL Training](http://arxiv.org/abs/2611.29651v1)
  <details><summary>📄 Abstract</summary>
  A policy trained against an LLM judge can learn to exploit its loopholes. Static probes show that such judges accept degenerate answers like a lone "{" or "Thought process:", but not which flaw a policy will find. In GRPO the first loophole to be exploited can be predicted before training from each pattern's exposure, the product of the starting policy's propensity to produce it and the judge's false-positive rate (FPR). To test exposure causally, we seed the patterns into fine-tuning at three d...
  </details>

- **2026-11-22** — Daojun Liang, Xiao Hong, Pei Zhang et al. — [Think Before You Forecast: Scaling Test-Time Compute for Time Series Forecasting](http://arxiv.org/abs/2611.29566v1)
  <details><summary>📄 Abstract</summary>
  Test-time compute has become an important paradigm in computer vision and language modeling, where additional computation at inference time enables models to explore multiple candidate solutions and select or refine the most reliable one. However, time series forecasting models typically produce predictions through a single forward pass, leaving them vulnerable to distribution shifts and non-stationarity that frequently arise in real-world temporal data. We propose Time Test Compute for Time Ser...
  </details>

- **2026-11-22** — Jieyu Li — [ParseGap: Testing What Coding Agents Authorize and What Shells Execute](http://arxiv.org/abs/2611.29546v1)
  <details><summary>📄 Abstract</summary>
  LLM coding agents authorize shell commands by parsing a command string against a policy and passing the raw string to a system shell, so the gate adjudicates one reading while the shell executes another. We present ParseGap, a differential testing framework that runs each command through an unmodified vendor checker and GNU Bash 5.2 in an isolated container, flagging a violation whenever an approved command produces policy-violating runtime effects. Across eight production coding agents, ParseGa...
  </details>

- **2026-11-22** — Feng Cheng, Cong Guo, Junyao Zhang et al. — [Gossamer: A Utility-Driven Architecture for Constant-Budget KV Cache Compression in Reasoning LLMs](http://arxiv.org/abs/2611.29497v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based large language models (LLMs) are increasingly applied to complex reasoning tasks, yet their inference efficiency is fundamentally constrained by the rapid growth of the KV cache. As reasoning contexts extend to hundreds of thousands of tokens, the key-value (KV) cache becomes the dominant contributor to both memory footprint and bandwidth demand, tightly coupling computation with memory utilization and thereby limiting scalability. Existing compression methods, such as quantiza...
  </details>

- **2026-11-22** — Shaked Perek, Avihu Dekel, Ben Wiesel et al. — [Fill in the Blanks: Non-Autoregressive Schema-Parallel Key Information Extraction with CTC Decoding](http://arxiv.org/abs/2611.29460v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) extract structured data from documents by generating the requested JSON one token at a time, so their sequential steps grow with the length of the answer. Yet in key information extraction (KIE) the schema already fixes the answer's structure: keys, nesting and lists are known before decoding, and only the values are unknown. We exploit this with a non-autoregressive extractor that writes the structure from the schema, sizes every list with a count pass, and predict...
  </details>

- **2026-11-22** — Zhiyi Wang, Xiaorui Xue, Xiaoxing Liu — [Constraint-Preserving Quantum Circuit Compilation for Graph Independent Sets via Persistent Occupancy Encoding](http://arxiv.org/abs/2611.29313v1)
  <details><summary>📄 Abstract</summary>
  Constraint-preserving mixers for graph independent sets repeatedly evaluate overlapping neighborhood conditions, increasing CX costs across ordered quantum optimization circuits. We propose a structure-aware compiler that reuses these conditions through persistent occupancy encoding. Exploiting mutual exclusion within true-twin classes, our reversible encoding stores class occupancy on the original data register across mixer operations and cost layers. Local mixers are synthesized using target c...
  </details>

- **2026-11-22** — Zhiyuan Chen, Zihao Yang, Quanjiang Li et al. — [QASparse: Query-Adaptive Sparse Attention with Tailored Budgets and Tokens](http://arxiv.org/abs/2611.29280v1)
  <details><summary>📄 Abstract</summary>
  Long-sequence inference in large language models is constrained by the high cost of prefilling, where dense attention scales quadratically with context length. Exploiting similarity across attention heads offers a way to reduce redundant computation. Prior approaches in this direction have relied on localized query observations to determine head-level computation reuse or budget allocation. However, inter-head similarity does not imply uniform query requirements, leaving adaptation to varying bu...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 67 papers

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

- **2026-11-23** — Reza Farahani, Zoha Azimi, Naser Hossein Motlagh et al. — [AeroPoint: Agentic AI for Intent-Driven Point Cloud Inspection in UAV-Edge Systems](http://arxiv.org/abs/2611.31671v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicle (UAV)-based Light Detection and Ranging (LiDAR) inspection generates dense point clouds that strain onboard computing and wireless bandwidth. Intent-based inspection allows operators to request objects, attributes, and spatial relationships through natural language. Answering these requests requires trans- lating intent into spatial queries and retrieving relevant evidence under UAV processing and communication constraints. This article presents AeroPoint, an agentic AI s...
  </details>

- **2026-11-23** — Zihang Lin, Huaiyuan Qin, Liangli Zhen et al. — [Modern Self-Supervised Vision Transformers Are Pareidolic](http://arxiv.org/abs/2611.31238v2)
  <details><summary>📄 Abstract</summary>
  In human perception, pareidolia is the tendency to perceive a meaningful pattern, such as a face, in a random or ambiguous stimulus. We find a similar phenomenon in modern self-supervised Vision Transformers (ViTs): on white noise, which contains neither objects nor spatial structure, a few directions of their features still form spatially coherent patterns across the patches, imposed by the features themselves. We call this behavior pareidolia, and the span of these directions the pareidolic su...
  </details>

- **2026-11-23** — Shabbir Hussain, Aaron Ortwein, Roya Ensafi — [CenShaper: Shaping Proxy Traffic for Censorship Circumvention](http://arxiv.org/abs/2611.31016v1)
  <details><summary>📄 Abstract</summary>
  Modern commodity DPI systems are capable of analyzing packet sizes, directions, and timings to detect circumvention tools even when those tools use sophisticated obfuscation. The anti-censorship community has called for innovation in traffic shaping and built an ecosystem that facilitates the adoption of new shaping techniques. However, a fundamental gap is halting progress: \textit{what} should circumvention traffic look like? Past experience with traffic shaping has underscored that effective ...
  </details>

- **2026-11-23** — Abdelmonaim Bounite, Zangir Iklassov — [Attributing Security Outcomes in LLM-Agent Evaluations: The Role of Content-Free State](http://arxiv.org/abs/2611.30259v1)
  <details><summary>📄 Abstract</summary>
  Security benchmarks for LLM agents record whether each attack succeeded and compare agents, attacks, and defenses by attack success rate (ASR). Such comparisons are valid only if the agent, the attack, and the defense cause each verdict. We show that verdicts also depend on content-free state: details of a run that carry no information about the system under test, such as the Python hash seed, the order of tools or evidence, and the scoring of failed runs. We require that this state influence no...
  </details>

- **2026-11-23** — Zhiyu Zhang, Yuankai Li, Muhao Chen — [MobileGrail: Learning Compact Guardrails for On-Device deployable Mobile GUI Agent Safety](http://arxiv.org/abs/2611.29847v1)
  <details><summary>📄 Abstract</summary>
  Runtime guardrails protect mobile GUI agents by assessing each proposed action before execution, but existing guardrails rely on cloud hosted large multimodal models, exposing every screen to a remote server, including private information such as payments, messages, and medical records. We propose MobileGrail, an on-device deployable model that addresses both. It maintains a recurrent task state that retains only the evidence subsequent safety decisions depend on, so that authorization and execu...
  </details>

- **2026-11-23** — Daniel Theron — [Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ](http://arxiv.org/abs/2611.31228v1)
  <details><summary>📄 Abstract</summary>
  Prompting language models to verbalize stepwise numerical confidence during generation is an increasingly popular approach for triggering backtracking and error correction in agentic reasoning. This strategy presupposes two capabilities: (1) in-situ monitoring fidelity (does confidence drop when an error occurs?) and (2) downstream steering control (does an uncertainty token causally steer the model to repair its error?). We evaluated four open-weights models (Qwen2.5-7B, Llama-3.1-8B, Mistral-7...
  </details>

- **2026-11-23** — Nicolas Bolouri, Gaya Mehenni, Daniel Toyama — [Habitats: A Framework for Open-Ended Evolution of Agent Objectives](http://arxiv.org/abs/2611.31160v1)
  <details><summary>📄 Abstract</summary>
  Designing what an agent should optimize can be as difficult as optimizing the agent itself. Existing language-model-based reward-generation methods typically refine objectives for predefined tasks and couple the decision of what to explore with the synthesis of how to implement it, potentially narrowing the resulting behavioral repertoire. We introduce Habitats, a framework for open-ended evolution of executable agent objectives. Habitats maintains a population of reward-policy pairs and evaluat...
  </details>

- **2026-11-23** — Shulu Li, Hanchen Li, Xiaokun Chen et al. — [TideSand: Performance-Accurate Sandbox Multiplexing for LLM Agents](http://arxiv.org/abs/2611.31118v1)
  <details><summary>📄 Abstract</summary>
  We propose TideSand, a sandbox system that intelligently multiplexes resources for performance-sensitive LLM agents, such as auto research agents working on system measurement tasks. TideSand combines three key ideas: agent-aware scheduling, which schedules sandbox execution intelligently at the tool call level to avoid resource contention; speculative swapping, which offloads the memory of sandboxes waiting on inference and restores it before their next tool call; and selective rollback, which ...
  </details>

- **2026-11-23** — Yiping Li, Haohua Que, Zhipeng Bao et al. — [CoSel: Cooperation as Selection for End-to-End Driving](http://arxiv.org/abs/2611.30918v1)
  <details><summary>📄 Abstract</summary>
  Cooperative driving can extend a vehicle's awareness beyond its own sensors, but existing cooperative end-to-end methods inject shared information into the planner and rely on cooperative driving demonstrations to learn how to use it. The moments in which shared information should change a driving decision are rare in such data, providing limited supervision for learning this behavior. We argue that cooperation need not be learned by the planner. Instead, reacting to shared information requires ...
  </details>

- **2026-11-23** — Frederic Lemieux, Shadi Abouzeid — [Deviant Machines: Innovation, Containment, and the Prevention of Autonomous Misalignment](http://arxiv.org/abs/2611.30848v1)
  <details><summary>📄 Abstract</summary>
  From May to September 2026, AI agents in training or evaluation at OpenAI, Anthropic and the UK AI Security Institute reached real third-party systems, published malicious packages, used fake identities to manipulate open-source maintainers, probed government data services, and wrote instructions into their own future contexts. Criminology has mostly treated AI as a tool for human offenders. This article treats these systems as deviant rather than criminal: they departed from training, rules and...
  </details>

- **2026-11-23** — Yuzhi Li, Hongliang Tian, Chengjun Chen et al. — [Interrupt-Aware Static Detection of Deadlocks in Rust Operating Systems](http://arxiv.org/abs/2611.30713v1)
  <details><summary>📄 Abstract</summary>
  Rust is increasingly adopted in operating systems, but Rust's safety guarantees do not eliminate deadlocks, especially those induced by interrupts. The core challenge is to recover interrupt-sensitive lock dependencies from Rust's guard-based synchronization across function boundaries. Applying this analysis across Rust OS projects also requires specifying project-specific synchronization semantics. We present an approach combining interrupt-aware static analysis with diagnostic-guided agent aud...
  </details>

- **2026-11-23** — Shengyao Wang, Siyuan Su, Siyu Song et al. — [Learning What to Change: State-Verified Reinforcement Learning for Educational Agents](http://arxiv.org/abs/2611.30559v1)
  <details><summary>📄 Abstract</summary>
  Persistent tutoring agents do more than answer questions: they manage course files, practice records, and learner profiles that govern future lessons. In such stateful settings, knowing what to teach does not guarantee knowing what to change. We identify a pervasive failure mode, content-state decoupling, where agents deliver pedagogically sound responses while silently corrupting workspace state through unwarranted updates, missed prerequisites, or unintended side effects. Text-level judges ove...
  </details>

- **2026-11-23** — Ruichen Qiu, Hao Shen, Lihong Zhi et al. — [LeanReviewBench: Semantic Alignment Review in Mathematical Lean Projects](http://arxiv.org/abs/2611.30361v1)
  <details><summary>📄 Abstract</summary>
  Lean verifies that a proof establishes its formal proposition, but whether that proposition preserves the mathematical content of an informal source requires separate review. In project-scale formalizations, this correspondence can depend on definitions and constraints distributed across many declarations. We introduce LeanReviewBench, a benchmark for project-level semantic alignment review containing 197 versioned inputs collected from 18 real Lean projects, with 87 aligned and 110 misaligned r...
  </details>

- **2026-11-23** — Hongyixuan Yuan, Qixing Zhou, Pengcheng Huang et al. — [RepoClean: Evaluating Coding Agents on Repository-Level Obsolete Code Cleanup](http://arxiv.org/abs/2611.30350v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents have demonstrated strong repository-level programming capabilities. However, as software evolves, repository code may become redundant or obsolete, increasing maintenance costs and potentially introducing functional issues. Agents must therefore identify and remove unnecessary code safely, yet autonomous repository-level code cleanup remains insufficiently evaluated in isolation. To evaluate this capability, we introduce RepoClean, a benchmark of 200 cleanup tas...
  </details>

- **2026-11-23** — Zilong He, Zhangchi Hu, Hebei Li et al. — [TAED: Trajectory-Aligned Encoder--Decoder Distillation for Detection Transformers](http://arxiv.org/abs/2611.30326v1)
  <details><summary>📄 Abstract</summary>
  Distilling localization knowledge into compact detection transformers (DETRs) requires consistent teacher-student query correspondence across decoder layers. However, in DETRs with encoder-based query selection, the teacher and student select top-K proposals independently. Same-rank queries can originate from different spatial locations and correspond to different objects, making rank-based layer-wise supervision unreliable. To address this problem, we propose Trajectory-Aligned Encoder-Decoder ...
  </details>

- **2026-11-23** — Yan Zheng, ShengYun Peng, Xuyao Liang et al. — [VeriWorld: A Verifiable Visual SWE-Bench for Spatial Reasoning in 3D Environments](http://arxiv.org/abs/2611.30226v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used for spatial tasks such as navigation and manipulation, where they must infer geometry and object relationships from visual input in order to act correctly. Existing benchmarks usually test perception and reasoning in isolation, making it hard to tell whether failures come from visual understanding, downstream reasoning, or the bridge between them. We introduce VeriWorld, a benchmark for spatial reasoning in interactive 3D environments with exec...
  </details>

- **2026-11-23** — Varad Srivastava, Victor Casas Hernandez — [Could This BE Any More Wrong? Teaching VLMs to Know What They Don't Know in Document Extraction](http://arxiv.org/abs/2611.30119v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models can extract structured fields from scanned financial documents, yet they provide no indication of when a field might be wrong. We derive per-field confidence estimates from the token log-probabilities the model already produces, via a token-to-span alignment procedure that maps logprobs onto each extracted value within the structured JSON output. Evaluated on two benchmarks (CORD v2 receipts, Kleister NDA legal contracts) with three VLM families, the minimum token probabil...
  </details>

- **2026-11-23** — Ayesha Sahar, Tahir Mustafa Madni, Tehseen Zia et al. — [One Size Doesn't Fit All: Input Adaptive Class Activation Mapping for Improved Visual Explanations](http://arxiv.org/abs/2611.29993v1)
  <details><summary>📄 Abstract</summary>
  Despite their widespread use in tasks such as image classification, object detection and semantic segmentation, the limited interpretability of Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) can undermine trust and hinder adoption in safety-critical applications. Explainable artificial intelligence (XAI) methods seek to address this by providing human-understandable explanations for model predictions. Class Activation Maps (CAM) constitute one such widely used XAI technique ...
  </details>

- **2026-11-23** — Fan Xu, Zhongtao Wang, Hao Wu et al. — [EmboEagle: An Efficient Agentic Embodied Framework for Long-horizon Robotic Manipulation](http://arxiv.org/abs/2611.31173v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robotic manipulation demands reliable execution across interdependent stages, yet standalone World-Action Models (WAMs) suffer from compounding physical errors, while stateless Vision-Language Model (VLM) supervision incurs prohibitive chunkwise latency and lacks 3D spatial persistence. We present EmboEagle, a closed-loop agentic framework that unifies subtask-conditioned WAM control, latent-space adaptive supervision, and memory-guided geometric recovery. First, we adapt sequential...
  </details>

- **2026-11-23** — Ziyu Liu, Zeyi Sun, Xiaoyi Dong et al. — [Visual-RFT++: Extending Visual Reinforcement Fine-Tuning to Multimodal Tool Use](http://arxiv.org/abs/2611.30193v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Fine-Tuning (RFT) has recently become a central paradigm for advancing Large Reasoning Models (LRMs), as demonstrated by systems such as OpenAI's o3 and the R1 series. Despite significant progress in LLMs, how to leverage RFT to unify visual perception, step-by-step reasoning, and agentic tool use into one coherent training paradigm remains an open challenge. In this work, we present Visual Reinforcement Fine-Tuning++ (Visual-RFT++), a unified framework that extends RFT to both vis...
  </details>

- **2026-11-23** — Zihang Lin, Huaiyuan Qin, Liangli Zhen et al. — [Modern Self-Supervised Vision Transformers Are Pareidolic](http://arxiv.org/abs/2611.31238v1)
  <details><summary>📄 Abstract</summary>
  In human perception, pareidolia is the tendency to perceive a meaningful pattern, such as a face, in a random or ambiguous stimulus.We find a similar phenomenon in modern self-supervised Vision Transformers (ViTs): on white noise, which contains neither objects nor spatial structure, a few directions of their features still form spatially coherent patterns across the patches, imposed by the features themselves.We call this behavior pareidolia, and the span of these directions the pareidolic subs...
  </details>

- **2026-11-23** — Federico Signorile, Raffaele Carli, Alessandro Bertogli et al. — [Bridging Continuous-Time MAPF and Industrial AGV Fleet Coordination with Lazy Priority-Based Search](http://arxiv.org/abs/2611.30874v1)
  <details><summary>📄 Abstract</summary>
  Continuous-time multi-agent path finding on roadmaps (MAPF$_R$) offers a principled way to coordinate robot fleets with geometric collision avoidance, yet its deployment on industrial automated guided vehicle (AGV) infrastructures remains challenging, as highly connected and redundant roadmaps amplify both safe-interval reasoning and multi-agent interaction handling. To bridge this gap, we formalize AGV-MAPF$_R$-CTC, a configuration-space variant of MAPF$_R$ with precomputed continuous-time conf...
  </details>

- **2026-11-23** — ChiFung Kwan, Kangzhong Wang, Youqian Zhang et al. — [TamperCert: A Benchmark for Detecting Text Tampering in Degree Certificates](http://arxiv.org/abs/2611.30419v1)
  <details><summary>📄 Abstract</summary>
  Degree certificates play a critical role in high-stakes decisions such as university admission, immigration, and hiring. The issuing institution vouches for the holder, so a forged certificate may let its bearer pass these checks. Degree certificate forgery is increasingly prevalent. Yet, many assume that it is easy to spot. Reported cases show otherwise: in 2024, the business school of the University of Hong Kong found that about 30 master's students had enrolled with forged academic credential...
  </details>

- **2026-11-23** — Nihel Loubna Ghennani, Mourtada Benazzouz, Julie Mauclair — [Trustworthy Speech-Based Autism Screening under Class Imbalance with Uncertainty-Aware HuBERT Ensembles](http://arxiv.org/abs/2611.30390v1)
  <details><summary>📄 Abstract</summary>
  Early screening of Autism Spectrum Disorder (ASD) is critical for timely clinical intervention, although establishing reliable speech based screening systems remains problematic due to limited clinical data, class imbalance, and the need for reliable uncertainty estimation. We propose an uncertainty-aware ASD screening framework based on self-supervised HuBERT representations, combining Leave-One-Subject-Out (LOSO) crossvalidation, balanced k-bagging, and Monte Carlo (MC) Dropout. Multiple HuBER...
  </details>

- **2026-11-23** — Parastoo Farajpoor, Mohammadreza Narimani — [Geospatial foundation models and deep learning for climate resilience: a review of transfer, uncertainty and decision readiness](http://arxiv.org/abs/2611.30198v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models can reuse information learned from large Earth-observation archives, but their value for climate resilience depends on whether that information transfers to unfamiliar events, regions and observing conditions. This review connects advances in deep learning with the evidence needed for hazard monitoring and early warning. A descriptive audit of 137 full-text hazard-application studies is interpreted alongside a separate corpus of 37 model and benchmark records. Ninety...
  </details>

- **2026-11-23** — Jaeyoung Lee, Misuk Kim — [ESGPT: A Data-Centric ESG Language Model with Unified Instruction and Benchmark Resources](http://arxiv.org/abs/2611.30052v1)
  <details><summary>📄 Abstract</summary>
  ESG analysis requires complex language understanding across diverse sources, including corporate reports, news, and disclosures, for tasks such as ESG relevance detection, action interpretation, impact analysis, and question answering. However, existing ESG datasets are fragmented by task and source, with heterogeneous formats and annotation schemes, limiting their use for training general-purpose ESG LLMs and unified evaluation. In this work, we construct ESG-Instruct, a 30,000-instance ESG ins...
  </details>

- **2026-11-23** — Zongjian Li, Mohammad Soleymani — [FlexGaze: Weakly Supervised Gaze Estimation at Scale](http://arxiv.org/abs/2611.30012v1)
  <details><summary>📄 Abstract</summary>
  Most gaze estimation models are trained on data collected using specialized equipment. The limited diversity of subjects, scenes, and head poses in these datasets hinders generalization to new conditions. We present FlexGaze, a family of 3D gaze estimators pretrained with weak supervision from gaze labels (pseudo-labels) automatically generated from in-the-wild images. We use off-the-shelf models to predict 2D gaze targets and scene depth, then combine these predictions to generate 3D gaze label...
  </details>

- **2026-11-23** — Xinyu Yan, Yurong Hao, Zherui Li et al. — [Antiphony: A Dual-Process Agent for Deepfake Video Detection with Real-Video Calibration](http://arxiv.org/abs/2611.29999v1)
  <details><summary>📄 Abstract</summary>
  Reliable video deepfake detection requires generalization to unseen generators while limiting false alarms on authentic footage. Although existing detectors capture diverse visual cues, they may produce overconfident errors under generator shift, limiting the reliability of confidence-based fusion. Threshold calibration is further complicated by shifts in authentic capture domains and the lack of future-generator examples. To address these challenges, we present Antiphony, a framework that combi...
  </details>

- **2026-11-23** — Benjamin Hurt, Oscar O'Donnell, Yefei Yang et al. — [Characterizing Frozen SSL Encoders and Backends for Cross-Domain Speech Deepfake Detection](http://arxiv.org/abs/2611.29865v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning (SSL) encoders are the dominant front end for speech deepfake detection, and the prevailing recipe fine-tunes the full encoder on a small spoofing corpus, maximizing in-domain accuracy at the cost of known degradation under domain shift. Taking a recent cross-attention fusion of SSL and constant-Q cepstral features as a fixed reference recipe, we freeze its encoder and ask which encoder and which backend behave best across domains. We cross two frozen encoders, the massi...
  </details>

- **2026-11-22** — Andrew T. Cadotte — [Evolutionary AI Control: Population-Level Safety Under Reproduction, Heredity, and Selection](http://arxiv.org/abs/2611.31312v1)
  <details><summary>📄 Abstract</summary>
  An AI agent can satisfy every individual safety check and still give rise to a population that violates a collective safety limit. This risk arises in open multi-agent systems, where agents copy themselves, modify their successors, and change system membership during a run. Selection then shifts the population toward traits outside the developers' optimization targets. We prove conditions under which safety guarantees persist through reproduction, inheritance, and selection, and we characterize ...
  </details>

- **2026-11-22** — Mert Onur Cakiroglu, Elham Buxton, Mehmet Dalkilic et al. — [CivicBench: Robust Detection of AI-Generated Political Video](http://arxiv.org/abs/2611.29766v1)
  <details><summary>📄 Abstract</summary>
  AI-generated video of politicians can pass for real footage, and once such fakes are common, real footage can be dismissed as fake. Platforms address both problems with detectors, but whoever uploads a clip controls its pixels. Existing datasets of political video are small, show real politicians, and test no attacks. We introduce CivicBench, with 10,800 generated clips of invented politicians from eight open generators and 2,632 public-domain or openly licensed real clips. Each clip can be atta...
  </details>

- **2026-11-22** — Fahrell Giovanny, Geby Bayuningtyas, Sahrul Mukharom — [Detectable Epistemic Attack Layers: A Coverage Theorem and Standardized Harness for Conversation-History Integrity](http://arxiv.org/abs/2611.29449v1)
  <details><summary>📄 Abstract</summary>
  Conversation history is infrastructure: deployed language models rely on application layers to store and reinject prior turns, and that stored state is writable. We formalize session-level contamination by attack layer, state a coverage theorem, and measure its scope: each deployment-layer verification tier covers exactly its layer and is sound with respect to the others; instruction overrides are not detectable without false positives; and composite vectors evade per-fragment verification. A st...
  </details>

- **2026-11-22** — Mu Jia, Junting Chen, Pooi-Yuen Kam — [RF-Florence: Unified RF Detection and Physical Grounding with a Foundation Model](http://arxiv.org/abs/2611.29496v1)
  <details><summary>📄 Abstract</summary>
  Reliable signal detection is essential for spectrum sharing and intelligent sensing in sixth-generation (6G) wireless networks. Wideband radio-frequency (RF) monitoring must locate emissions and identify those satisfying waveform-family and physical constraints. The latter task, physical grounding, requires query meaning to agree with measurable signal attributes. RF-Florence unifies three tasks---full-scene detection, physical grounding, and supplied-region recognition---through a shared pretra...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 57 papers

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

- **2026-11-23** — Adrià Ruiz, Bartłomiej Twardowski, Tinne Tuytelaars et al. — [Near-Zero Forgetting Is Not Enough: Out-of-Distribution Robustness in Continual Learning of Pretrained VLAs](http://arxiv.org/abs/2611.31511v1)
  <details><summary>📄 Abstract</summary>
  Recent work shows that pretrained Vision-Language-Action (VLA) models exhibit near-zero forgetting in specific continual learning settings with experience replay. However, robustness to domain shift of learned tasks remains unexplored. In this work, we study the robustness of Pi0 fine-tuned with experience replay under out-of-distribution (OOD) data using the LIBERO and LIBERO-Plus benchmarks. While the in-domain (ID) setup achieves near-zero catastrophic forgetting, OOD performance on previous ...
  </details>

- **2026-11-23** — Merel Kuijs, Till Richter, Rushin H. Gindra et al. — [Learning Multimodal Representations from Partially Paired, Small-Scale Data](http://arxiv.org/abs/2611.30601v1)
  <details><summary>📄 Abstract</summary>
  Modeling multimodal data from partially paired samples is critical for advancing domains like biomedicine, where vast unimodal datasets and foundation models exist but paired data remains scarce. Existing fusion methods rely on large-scale paired datasets, limiting their use in scenarios with incomplete pairing. We introduce CAMEO, an adversarial learning-based modality fusion framework that integrates modalities from small, partially paired datasets. Combining any pre-trained unimodal encoder w...
  </details>

- **2026-11-23** — Liangyi Huang, Zichen Liu, Fei Shao et al. — [LODESTONE: Linking System Events to Threat Intelligence for Evidence-Grounded Cyber Attack Investigation](http://arxiv.org/abs/2611.29932v1)
  <details><summary>📄 Abstract</summary>
  System provenance graphs help reconstruct attacks through causal dependencies, but these connections alone do not explain how events accomplish an adversary's goal. Cyber threat intelligence (CTI) provides the necessary security knowledge, yet linking it to execution evidence requires bridging differences in meaning and granularity between events and attack relations amid scarce labels and sparse relevant evidence. We present LODESTONE, a cross-graph alignment system that links observed system e...
  </details>

- **2026-11-23** — Avinash Kumar Singh, Bhaskarjit Sarmah, Stefano Pasquali — [Know When to Abstain: Conformal Confidence Estimation for Text-to-SQL](http://arxiv.org/abs/2611.31190v1)
  <details><summary>📄 Abstract</summary>
  Text-to-SQL systems often return queries that execute successfully but answer the wrong question. Detecting these errors at deployment is hard because execution correctness is defined against a gold query, which exists only in labeled data. We formulate confidence estimation for Text-to-SQL as probabilistic query validation under a latent correctness variable that is observable at calibration time through gold-SQL execution and latent at deployment. Our estimator separates generation from valida...
  </details>

- **2026-11-23** — Kangping Hu, Akshay Mehra, Stephen Mussmann — [SPROUT: Predicting Objective-Grounded Prompt Utility for Efficient Text-to-Image Preference Tuning](http://arxiv.org/abs/2611.31163v1)
  <details><summary>📄 Abstract</summary>
  Preference tuning of text-to-image diffusion models spends most of its compute generating candidate images, yet training prompts are typically sampled uniformly at random, wasting compute generating images that provide too little signal for model alignment. To best utilize the available compute, we study prompt selection, where at each iteration we identify the most useful prompts for preference tuning. We separate prompt selection into a utility score, an estimator of that utility score, and ba...
  </details>

- **2026-11-23** — Vladislav Mikhailov, Sarfraz Ahmad, Momina Ahsan et al. — [PRIMEAPE: A Multilingual Benchmark for Fine-Grained Meta-Evaluation of Judge Models](http://arxiv.org/abs/2611.30925v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly serve as judges of other models, shaping benchmark rankings and model development. Yet, a judge whose rationale consistently supports its verdict may still disagree with human preferences. To study this, we introduce PRIMEAPE, a multilingual benchmark for evaluating judge verdicts and rationales. PRIMEAPE provides 2,205 response pairs covering 243 instructions in English, French, Spanish, Urdu, Hindi, Norwegian Bokmål, and Yoruba, with 11k human annotations of ...
  </details>

- **2026-11-23** — Yi Liu, Qi Zhang, HaoLin Li et al. — [NeuroMotion: Aligning EEG to Discrete Motion Primitives for Continuous Motion Decoding](http://arxiv.org/abs/2611.30817v1)
  <details><summary>📄 Abstract</summary>
  EEG-to-motion decoding remains challenging because noisy scalp EEG is difficult to map directly to continuous kinematics. We present NeuroMotion, a framework that aligns EEG representations to discrete motion primitives for continuous motion decoding across heterogeneous paradigms, including full-body free movement, lower-limb treadmill locomotion, and upper-limb freewill reaching and grasping. A VQ-based motion prior discretizes continuous motion into reusable primitives that serve as both alig...
  </details>

- **2026-11-23** — Niclas Doll, Jasper Schulze Buschhoff, Shalaka Satheesh et al. — [When Does Continual Pre-Training Help? An Empirical Study of Decoupled Knowledge and Generation Trajectories in Clinical LLMs](http://arxiv.org/abs/2611.30507v1)
  <details><summary>📄 Abstract</summary>
  Continual pre-training (\textit{CPT}) is a standard route for domain adaptation, yet existing studies typically track pre-training loss or multiple-choice question answering (\textit{MCQA}) accuracy alone, offering only a narrow view of how adaptation unfolds. We jointly track factual knowledge via \textit{MCQA} and open-ended behavior via pairwise preference rankings across $18$ checkpoints for each of eight instruction-tuned \textit{Qwen} models ($0.5B$ to $8B$), adapted to German medicine wit...
  </details>

- **2026-11-23** — Ahmad Zorkot — [Newton iterations and semi-Lagrangian schemes for mean field games of controls](http://arxiv.org/abs/2611.30409v1)
  <details><summary>📄 Abstract</summary>
  We study Newton methods for second-order mean field games of controls (MFGC), in which agents interact through local averages of their controls. We prove local quadratic convergence of full Newton iterations, and of Newton iterations on reduced unknowns, near stable classical solutions. Stability holds under weak control interaction and under an infinitesimal monotonicity condition of Lasry--Lions type. We propose a semi-Lagrangian (SL) scheme for second-order MFGC, in which the average-control ...
  </details>

- **2026-11-23** — Yuxuan Chen, Changwei Lv, Yunfei Li et al. — [MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation](http://arxiv.org/abs/2611.30287v1)
  <details><summary>📄 Abstract</summary>
  AI agents accumulate conversations, images, and documents through long-term interactions with users. Answering later questions often requires connecting evidence across these records, yet the resulting understanding is rarely retained, allowing mistakes to recur on related questions. Existing multimodal memory methods largely focus on storing and retrieving records, with limited mechanisms for learning from completed tasks and consolidating task-specific experience. We therefore propose MMMem, a...
  </details>

- **2026-11-23** — Jian Zhou, Binqing Wu, Zongjiang Shang et al. — [STMemoLLM: A Spatial-Temporal Memory-Augmented LLM for Robust Traffic Forecasting](http://arxiv.org/abs/2611.30148v1)
  <details><summary>📄 Abstract</summary>
  Traffic forecasting is essential for intelligent transportation systems. However, traditional deep-learning models often rely heavily on high-quality observations. Recent LLM-based approaches incorporate pretrained knowledge to improve forecasting, but they remain sensitive to input perturbations and struggle to preserve long-term patterns. To address this, we propose STMemoLLM, a spatial-temporal memory-augmented LLM for robust traffic forecasting. STMemoLLM introduces memory prototypes to comp...
  </details>

- **2026-11-23** — Yiming Liu, Jianwei Ma, Zhongwei Xing et al. — [Sparse Hodge Preference Optimization: Fine-Tuning Language Models toward Alignment beyond Transitive Preferences](http://arxiv.org/abs/2611.30135v1)
  <details><summary>📄 Abstract</summary>
  The growing adoption of Direct Preference Optimization (DPO), which leverages pairwise preference data, reflects its great success in fine-tuning large language models to align with human expectations. It directly optimizes the policy from human preferences without explicit reward modeling or the complexities of reinforcement learning-based approaches. However, the classic DPO relies on the Bradley--Terry sampling model and cannot effectively capture intransitivity or cyclic structures in aggreg...
  </details>

- **2026-11-23** — Haiyu Xu, Yiyang Chen, Jiayi Zhou et al. — [AxE: Benchmarking Agent-Environment Generalization of Video World Models via Grounded Events](http://arxiv.org/abs/2611.30120v1)
  <details><summary>📄 Abstract</summary>
  Edge cases are not the long tail; they are the norm. An embodied system deployed across changing environments, bodies, objects, and tasks will routinely encounter combinations that were absent from its training data. General-purpose physical intelligence therefore requires world models that reuse prior knowledge, predict consequences, and adapt with little or no additional training. Yet current evaluations of conditional video generation emphasize visual quality, prompt alignment, or isolated ph...
  </details>

- **2026-11-23** — Jinxuan Zhu, Zhiyao Duan — [AIRPiano: Piano Score Following with Tabletop Hand Gestures](http://arxiv.org/abs/2611.30049v1)
  <details><summary>📄 Abstract</summary>
  AIRPiano aims to bring sound to the common practice of rehearsing piano music on a tabletop. Guided by a known score, users make piano-like finger movements on a flat surface without reproducing absolute keyboard positions. The score supplies pitches, while hand motion determines which score events to play and when. We formulate this interaction as online alignment between tabletop hand motion and symbolic score events. To address the ambiguity of tabletop motion, its differences from piano-play...
  </details>

- **2026-11-23** — Yi Kuang, Shu Liu, Ningning Wang — [CSI-Agnostic End-to-End Neural Decoding of LDPC Codes under Synchronization Errors](http://arxiv.org/abs/2611.30037v1)
  <details><summary>📄 Abstract</summary>
  Correcting synchronization errors (insertions, deletions, and substitutions) in concatenated coding schemes, typically comprising an inner marker code and an outer Low-Density Parity-Check (LDPC) code, poses a significant challenge. Traditional algebraic decoding fails entirely under sequence misalignment. While recent neural pipelines attempt to resolve this, they typically demand exact channel state information (CSI) for inner synchronization and suffer from error propagation caused by prematu...
  </details>

- **2026-11-23** — Junchi Liao, Wentao Li — [The Answer Is Not the State: Trajectory-Level Corrigibility in Diffusion Language Models](http://arxiv.org/abs/2611.29937v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models generate tokens at many positions on a shared canvas, making unfinished responses appear revisable. We find a counterexample: after the final answer is reopened, previously generated rationale can reconstruct the old decision despite newly available evidence. We isolate this effect by comparing reopening the answer alone with reopening both rationale and answer, and by exchanging rationales between paired trajectories. On a 150-question source-disjoint benchmark, reopen...
  </details>

- **2026-11-23** — Himanshu Gupta, Brendan Crowe, Christoffer Heckman et al. — [Particle Belief Representations for Reinforcement Learning under Partial Observability](http://arxiv.org/abs/2611.29884v1)
  <details><summary>📄 Abstract</summary>
  Particle filters flexibly represent complex, multimodal beliefs but expose them as weighted, unordered sets incompatible with conventional fixed-dimensional policies. We study particle-belief encodings as inputs to reinforcement-learning policies while holding belief estimation and policy optimization fixed. We compare statistical summaries, cumulant-generating-function (CGF) features, and permutation-invariant set encoders. Trainable encoders are learned end-to-end or pretrained through belief ...
  </details>

- **2026-11-23** — Sumer S. Vaid — [Causal Evidence for the Emergence and Spread of Reward Hacking in AI Agent Swarms](http://arxiv.org/abs/2611.30185v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents that coordinate and collaborate among each other have become pervasive across domains ranging from scientific research to finance and engineering. The opportunity to share messages and build upon each other's work also creates the potential for misaligned behaviors to spread across AI agents. We provide causal evidence that mere exposure to reward hacking, cheating on a task to pass an automated check, is enough to spread the behavior among AI agents, even after the cheat ha...
  </details>

- **2026-11-22** — Víctor Yeste, Candida Maria Greco, Paolo Rosso et al. — [Sánchez, Feijóo, or Abascal? Speaker Attribution and Ideological Congruence in LLM Personas Reading Posts on X of the Leaders of the Three Main Parties of the 29N General Election in Spain](http://arxiv.org/abs/2611.29765v1)
  <details><summary>📄 Abstract</summary>
  Source cues are central to political communication, yet reception studies with large language model (LLM) personas as synthetic audiences have not tested whether personas respond to who speaks and not only to what is said. With Spain's general election of 29 November 2026 in mind, we run a speaker-attribution experiment using 1,075 anonymised X posts by the leaders of PSOE, PP and VOX on four topics (the economy and employment, household costs, immigration and corruption) and 791 distinct value-...
  </details>

- **2026-11-22** — Kiana Taktehrani, Maryam Hosseini, Amir Keynia et al. — [LAF-ECG: Multi-Resolution Lead-Aware Fusion of Time-Series and Language Foundation Models for ECG Classification](http://arxiv.org/abs/2611.29721v1)
  <details><summary>📄 Abstract</summary>
  Automated electrocardiogram (ECG) interpretation has advanced substantially with deep learning, yet many methods remain task-specific and label-dependent. Large language models (LLMs) and time-series foundation models (TSFMs) offer complementary pretrained representations, but integrating them is challenging because of mismatched feature spaces and the lead- and scale-dependent structure of ECG signals. We propose LAF-ECG (Lead-Aware Foundation Fusion for ECG), a dual-foundation framework that e...
  </details>

- **2026-11-22** — Yijie Li, Xi Cao, Yuan Sun et al. — [Diversity in Unity, Theory in Practice: Hierarchical Multitask Benchmarks for Chinese Minority Languages](http://arxiv.org/abs/2611.29635v1)
  <details><summary>📄 Abstract</summary>
  Despite the rapid advancement of LLMs, their performance on linguistically and culturally diverse minority languages within a unified national context remains underexplored. We present CMiLBench, a collection of hierarchical multitask benchmarks designed to translate theoretical notions of "diversity in unity" into practical evaluation for three representative Chinese minority languages: Tibetan, Mongolian, and Uyghur. CMiLBench comprises 24,663 instances across 5 difficulty levels and 17 tasks ...
  </details>

- **2026-11-22** — Yihang Zou, Ruixi Liang, Chunmei Qing et al. — [STAGE: Structured Test-Time Adaptation with Global Entropic Soft-coupling for Cross-Subject Brain-to-Image Retrieval](http://arxiv.org/abs/2611.29538v1)
  <details><summary>📄 Abstract</summary>
  Cross-subject brain-to-image retrieval aims to identify viewed images from unseen subjects' brain signals. However, inter-subject variability hinders alignment of brain-image representations, while independent query ranking tends to concentrate predictions on a few candidates, making accurate retrieval difficult without target labels. We propose STAGE (Structured Test-Time Adaptation with Global Entropic Soft-coupling), a structured test-time adaptation framework for recovering cross-subject ali...
  </details>

- **2026-11-22** — Rongze Tang, Chenyu Zhou, Jianjie Fang et al. — [MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model](http://arxiv.org/abs/2611.29501v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) excel at robot manipulation by imagining future observations and decoding actions from them, yet remain confined to a single embodied agent. In practice, manipulation often requires multiple robots to collaborate across disjoint workspaces, coupled timing, and heterogeneous embodiments. Such coordination demands both spatiotemporal alignment of future interactions and awareness of individual embodiment and role identities, whereas existing decentralized per-robot polic...
  </details>

- **2026-11-22** — Zhengfeiyang Zhang, Haoyuan Chen, Hexin Wang et al. — [Representation Alignment Is Only as Good as the Teacher's Behavioral Structure](http://arxiv.org/abs/2611.29483v1)
  <details><summary>📄 Abstract</summary>
  Recent works align the intermediate features of vision-language-action (VLA) models with frozen vision encoders during fine-tuning, hoping to inject additional priors such as 3D awareness or affordances. Unlike in image generation, where teachers for representation alignment (REPA) are assessed with encoder-intrinsic metrics, teachers for VLAs are still chosen largely by heuristics. We show that this practice is unreliable: across 14 teachers and 16 manipulation tasks, under matched training bud...
  </details>

- **2026-11-22** — Pulkit Bansal, Vivek Srivastava, Shirish Karande — [Seeing Through Preferences: Recovering Hidden Local Preference Neighborhoods for Text-to-Image Alignment](http://arxiv.org/abs/2611.29436v1)
  <details><summary>📄 Abstract</summary>
  Aligning text-to-image (T2I) diffusion models with human preferences typically relies on large-scale pairwise annotations, which are expensive to obtain and provide only sparse supervision. Moreover, not all preference comparisons contribute equally to learning: comparisons between semantically distant images often reveal little about the fine-grained perceptual factors underlying human judgments. We argue that informative supervision can arise from local preference neighborhoods surrounding hum...
  </details>

- **2026-11-22** — Xudong Wang, Siwei Cheng, Haozhe Hu — [BQDNA: Multi-Head Binary Spherical Quantization for Genomic Sequence Modeling](http://arxiv.org/abs/2611.29395v1)
  <details><summary>📄 Abstract</summary>
  Decoding biological information from long, repetitive DNA remains challenging. Genomic language models (gLMs) often follow the conventional language-model pretrain-and-adapt paradigm. However, the lack of inherent semantic segmentation and prior rules makes hand-crafted tokenizers like k-mer and BPE suboptimal. We introduce context-aware \textbf{BQVAE} for scalar quantization of DNA and \textbf{BQDNA}, an autoregressive gLM supporting multi-head codebooks. Comprehensive experiments reveal that: ...
  </details>

- **2026-11-22** — Xiaoyu Chen, Xiao Gu, Chao Zhang et al. — [SleepXA: Composing Pretrained Neural and Cardiac Foundation Models for Sleep Representation Learning](http://arxiv.org/abs/2611.29364v1)
  <details><summary>📄 Abstract</summary>
  Physiological signals recorded during sleep provide synchronized views of neural, cardiac, respiratory, and other bodily systems, while preserving modality-specific information. Existing EEG and ECG foundation models already capture rich but distinct physiological structure, motivating an alternative to training a multimodal sleep model from scratch: composing existing pretrained models. We introduce SleepXA, a framework that uses synchronized polysomnography (PSG) to compose independently pretr...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 60 papers

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

- **2026-11-23** — Yukun Shi, Minglun Gong — [Which Way Is Up? Rotated Photos Silently Hurt Multi-View 3D Foundation Models](http://arxiv.org/abs/2611.31478v1)
  <details><summary>📄 Abstract</summary>
  Multi-view 3D foundation models estimate camera poses and 3D points from a set of photos in one forward pass. Many cameras store a portrait shot sideways, with an orientation tag telling viewers how to turn it, and this tag can be ignored, lost or wrong. We measure how rotated photos affect five such models on three datasets. A few rotated photos lower camera pose accuracy for every model, and the sideways photos already in a standard benchmark do the same. Even the most robust model still loses...
  </details>

- **2026-11-23** — Benedikt von Querfurth, Lukas Klein, Cédric Vincent-Cuaz et al. — [A multimodal foundation model for tissue proteomics and morphology in cancer](http://arxiv.org/abs/2611.31451v1)
  <details><summary>📄 Abstract</summary>
  Cancer diagnosis, prognosis, and treatment decisions increasingly rely on integrating tissue morphology with specific molecular readouts of the tumor and its microenvironment. H&E histopathology provides scalable morphology, whereas multiplex spatial proteomics quantifies dozens of proteins in situ with spatial context, but remains selectively deployed, often with different marker panels across cohorts. This creates a translational bottleneck: most patients lack high-depth molecular profiling, a...
  </details>

- **2026-11-23** — Ziheng Cheng, Xin Guo, Ben Hambly — [Transformers with Signatures: Towards Universal In-Context Learning in Path Space](http://arxiv.org/abs/2611.31439v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) enables transformers to adapt to new tasks from demonstrations without updating their parameters. However, theoretical guarantees for transformers remain limited in general, and elusive in particular when target responses depend nonlinearly on the evolution of observed paths. We establish an ICL framework for path space, using path signature features. Building on the universal linear approximation property of signatures, we construct explicitly a causal softmax transfor...
  </details>

- **2026-11-23** — Chaeeun Lee, Hossein A. Rahmani, Aryo Pradipta Gema et al. — [Learning What vs. Learning How: Decomposing Task and Interface Competence in Agentic Training](http://arxiv.org/abs/2611.31427v1)
  <details><summary>📄 Abstract</summary>
  LLM agents operate through harnesses that define system prompts, action formats, feedback loops, and resource constraints. A model may possess the knowledge needed to solve a task yet fail to express that knowledge through a particular harness. This raises a basic question: when a policy fails under a given harness, is it missing task knowledge or the competence to operate the interface? We distinguish two components of agentic competence: task competence, the knowledge and reasoning needed to s...
  </details>

- **2026-11-23** — Elisabeth Fink — [LimeTree: Linear-Memory Graph Neural Networks over Tree-Graphs for Resource-Efficient Language Modeling and Context Extrapolation](http://arxiv.org/abs/2611.30934v2)
  <details><summary>📄 Abstract</summary>
  The search for computationally efficient alternatives to the Transformer has yielded numerous architectures in recent years; however, most exhibit severe weaknesses in associative recall-such as key-value (KV) retrieval-and length extrapolation, where even standard Transformers struggle. This paper introduces LimeTree, a linear-complexity architecture in both memory and compute for sequence modeling. By integrating synthetic KV retrieval tasks directly into standard language modeling training, L...
  </details>

- **2026-11-23** — Christophe Reype, Thomas Opitz, Eleanora Bassi et al. — [Ranking honeybee breeder colonies: a probabilistic method using vine copulas to consider multiple criteria](http://arxiv.org/abs/2611.31322v1)
  <details><summary>📄 Abstract</summary>
  Ranking honeybee colonies according to multiple performance criteria is central to selection in bee breeding, but deterministic scores provide limited information about how a selected colony compares with the population of available colonies. We propose a population-calibrated probabilistic score based on a weighted Euclidean distance to an ideal colony and an estimation of the joint distribution of the data. For a candidate colony, the probability-score is the probability that a colony drawn fr...
  </details>

- **2026-11-23** — Mohit Tekriwal, Het Mankad, Naifeng Zhang et al. — [AI-Assisted Auto-formalization for Trustworthy Scientific Computing: Case Studies and Lessons Learned](http://arxiv.org/abs/2611.31033v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI tools have recently had success in mathematical reasoning. Both general purpose coding agents such as Claude Code and Codex, and specialized mathematics agents such as Aristotle, have been used for formalizing mathematical problems such as Fermat's last theorem, Erdős problems and several IMO level math problems. However, much of these efforts are concentrated in the pure mathematics domain, which benefits from relatively self-contained theorem statements, fixed mathematical represent...
  </details>

- **2026-11-23** — Mishuo Han, Zhixuan Liang, Zhaoyuan Wan et al. — [Foresight Forcing: Learning Spatial Foresight for Robotic Manipulation](http://arxiv.org/abs/2611.30963v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation policies can improve action prediction by anticipating how objects move and how their spatial relationships change. World Action Models (WAMs) learn to predict future visual observations, but their training objectives typically leave the underlying 3D geometric transitions implicit. To alleviate this problem, we introduce Foresight Forcing ($\mathcal{F}^{2}$), a WAM that learns a spatial transition representation from changes in a pretrained 3D feature space. During training...
  </details>

- **2026-11-23** — Navid Keshtiarast, Amirhassan Babazadeh Darabi, Cem Tarhan et al. — [Hierarchical Multi-Timescale Deep Reinforcement Learning for QoS-Aware AI-RAN Configuration](http://arxiv.org/abs/2611.30695v1)
  <details><summary>📄 Abstract</summary>
  Configuring radio access networks (RANs) for heterogeneous services requires coordinating radio parameters whose effects on throughput, delay, and reliability are closely coupled and evolve over different timescales. This paper presents a hierarchical deep reinforcement learning (DRL) framework for joint, QoS-aware RAN configuration that aligns the learning structure with the real-time, near-real-time, and non-real-time control loops of O-RAN that are also adopted by AI-RAN. Three proximal polic...
  </details>

- **2026-11-23** — Zhilun Hu, Yuqi Cheng, Yuxiang Tan et al. — [Active Observation for Robust Visual Servoing in Robotic Manipulation](http://arxiv.org/abs/2611.30658v1)
  <details><summary>📄 Abstract</summary>
  Robust visual servoing during robotic grasping remains challenging, as approach-phase occlusion frequently disrupts closed-loop control. To address this, we present an active observation framework in which one arm of an existing dual-arm platform carries an RGB-D camera as an active observer while the other executes grasping. The observer repositions to maintain or recover a shared target-gripper view within the feasible shared-view workspace. Occlusion during the final approach is particularly ...
  </details>

- **2026-11-23** — Ting Chen, Geng Li, Guohao Chen et al. — [Rethinking the Evaluation of Contrastive Decoding for Hallucination Mitigation in Multimodal Large Language Models](http://arxiv.org/abs/2611.30460v1)
  <details><summary>📄 Abstract</summary>
  Contrastive decoding (CD) mitigates object hallucination in multimodal large language models (MLLMs) by contrasting token distributions under different conditions to adjust token scores. However, existing generative and discriminative benchmarks primarily measure final task scores, which can be confounded by candidate filtering, changes in generation trajectories, and response biases, making it difficult to isolate the effects of the underlying contrastive adjustments. To address these limitatio...
  </details>

- **2026-11-23** —  Preeti, Ankita Kushwaha, Kiran Ravish et al. — [TAP: Policy Interfaces for Diffusion Language Models](http://arxiv.org/abs/2611.30406v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models denoise a masked canvas, making them a natural setting for selective generation decisions such as answering, waiting, clarifying, or refusing. We introduce TAP-DiLM, which adds a typed policy variable to masked diffusion LMs, and study how this policy should be attached to the denoising process. Across BERT-base, MDLMOWT, LLaDA-8B, and Dream-7B, we compare shared-vocabulary slots, dedicated slot heads, and CLS-based external heads. The results reveal a clear interface-b...
  </details>

- **2026-11-23** — Hesen Yang, Yuxue Liu, Yanzhe Chen et al. — [REACT: Response-based Expert Assembly from Contextual Trajectories](http://arxiv.org/abs/2611.30366v1)
  <details><summary>📄 Abstract</summary>
  Dense feed-forward networks are unaffected by how their neurons are grouped: every neuron is evaluated. Sparse execution makes this grouping consequential, because each input can access only a few experts. An arbitrary partition can therefore retain pretrained weights while separating computations that an input needs together. We argue that upcycling should organize neurons according to their responses to similar inputs. To establish this correspondence, we introduce a context-guided upcycling a...
  </details>

- **2026-11-23** — Yuxin Jia, Xing Lan, Wensong Wang et al. — [Face Is Not All You Need: MIME Benchmark for Incomplete Multimodal Emotion Recognition](http://arxiv.org/abs/2611.30288v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Emotion Recognition (MER) is a fundamental task in multimedia understanding, where state-of-the-art methods have achieved prominent success relying on the assumption of complete, well-aligned multimodal inputs. However, real-world unconstrained scenarios often suffer from unpredictable modality degradation and information loss, leading to catastrophic performance collapse of existing MER models that heavily depend on facial cues as the core inference anchor. However, few systematic wo...
  </details>

- **2026-11-23** — Luong Tran, Lan-Cuong Nguyen, Huynh Dang Nguyen et al. — [CLIP-FMoE: Scalable CLIP via Fused Mixture-of-Experts with Enforced Specialization](http://arxiv.org/abs/2611.30233v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) architectures have emerged as a promising approach for scaling deep learning models while maintaining computational efficiency. However, existing MoE adaptations for Contrastive Language-Image Pre-training (CLIP) models suffer from significant computational overhead during sequential training and degradation of zero-shot capabilities. To address these limitations, we propose CLIP-FMoE, a novel approach that integrates MoE architecture into CLIP fine-tuning. Our method us...
  </details>

- **2026-11-23** — Yanlong Chen, Thongthornpatch Chamadol, Yichen Guo et al. — [Quantizing in the Loop: Drift-Aware Ultra-Low-Bit Vision-Language-Action Models](http://arxiv.org/abs/2611.30178v1)
  <details><summary>📄 Abstract</summary>
  Deploying large vision-language-action (VLA) models on resource-constrained robots demands extreme compression, yet existing post-training quantization (PTQ) methods frequently collapse at ultra-low bit-widths ($\le$ 2 bits). We trace this failure to two mismatches in standard pipelines. First, calibrating on static offline demonstrations induces distribution shift: minor quantization perturbations drive the policy into unseen states where uncalibrated errors compound. Second, minimizing the lay...
  </details>

- **2026-11-23** — Gengming Cui, Mingfei Han, Jiawei Zhang et al. — [Agent on Guard: Self-Improving Runtime Intervention for Robust Robotic Manipulation](http://arxiv.org/abs/2611.30101v1)
  <details><summary>📄 Abstract</summary>
  Robot foundation policies provide learned execution capabilities, while programming agents can reason about failures and construct recovery behaviors. Combining them effectively requires learning when intervention helps and when the policy can reliably resume. This challenge is inherently temporal: the physical world continues to evolve during reasoning, and a useful recovery may become infeasible before a decision takes effect. We introduce Agent on Guard (AoG), a hierarchical framework that im...
  </details>

- **2026-11-23** — Chen Li, Xiaoling Hu, Chao Chen — [Beyond Binary Correctness: A Surrogate for Confidence Learning in Large Language and Vision-Language Models](http://arxiv.org/abs/2611.30059v1)
  <details><summary>📄 Abstract</summary>
  Confidence estimation for large language models (LLMs) and vision-language models (VLMs) aims to assess how likely a particular generated response is to be correct. We investigate how learning this assessment can benefit from the model's predictive reliability on the underlying query. Binary correctness supervision, however, assigns identical labels to occasional errors and frequent failures, as well as isolated successes and consistent success. These outcomes can arise from substantially differ...
  </details>

- **2026-11-23** — Jaeyoung Lee, Misuk Kim — [TRAE: Trustworthy Automated ESG Annotation via Multi-Agent Consensus and Confidence Assessment](http://arxiv.org/abs/2611.30035v1)
  <details><summary>📄 Abstract</summary>
  With the growing demand for ESG disclosure and evaluation, constructing high-quality datasets for automatically extracting ESG-related information from large-scale documents has become essential. However, ESG annotation remains challenging due to strong context dependence, ambiguous label boundaries, and the need for domain expertise, resulting in high annotation cost and limited scalability. To address these challenges, we propose TRAE (TRustworthy Automated ESG annotation), a multi-agent frame...
  </details>

- **2026-11-23** — Yanzhe Chen, Zhijun Cao, Zechen Bai et al. — [RUIBench: What Makes a Good Robot-Use Interface?](http://arxiv.org/abs/2611.31115v1)
  <details><summary>📄 Abstract</summary>
  Foundation models can reason about complex physical tasks, yet translating this intelligence into reliable robot execution remains challenging. We argue that a critical, often overlooked factor is the robot-use interface (RUI), which determines how agents express and execute physical actions. To systematically study its impact, we introduce RUIBench, comprising 30 manipulation tasks across five suites spanning world knowledge, in-context learning, discovery, dynamic interaction, and contact-rich...
  </details>

- **2026-11-23** — Jingyuan Liu, Yongwei Chen, Yishan Yang et al. — [Wrist-Camera Video Diffusion as Generalizable Robot Policies](http://arxiv.org/abs/2611.31079v1)
  <details><summary>📄 Abstract</summary>
  A generalist manipulation policy should perform new tasks, operate in unfamiliar scenes, and transfer skills across robot embodiments. We present Wrist Video Policy (WVP), a closed-loop manipulation framework that learns how manipulation unfolds through video prediction and recovers executable motion through geometric estimation. Our key idea is to represent robot motion through wrist-camera trajectories, which determine the corresponding end-effector poses through a fixed hand-eye transformatio...
  </details>

- **2026-11-23** — Le Yang, Haoyang Lyu, Honglei Jin et al. — [GeoMerge-OPD: Balanced Skill Integration in Vision-Language-Action Models](http://arxiv.org/abs/2611.30632v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models excel at individual robotic skills, yet integrating heterogeneous skills into a single policy remains a key challenge for general-purpose robotic control, especially in whole-body tasks with differing manipulation and locomotion requirements. Common multi-skill integration strategies, such as joint fine-tuning and parameter merging, can induce unintended actions during closed-loop execution, severely degrading individual skills. Task-conditioned analysis of ex...
  </details>

- **2026-11-23** — Zhengyang Wang, Renfei Tan, Shuze Daniel Liu et al. — [Revisiting Learning to Delegate: LLM Discovered Heuristics for Large-Scale Vehicle Routing](http://arxiv.org/abs/2611.31090v1)
  <details><summary>📄 Abstract</summary>
  Efficient vehicle routing is critical to logistics and transportation, yet solving large-scale capacitated vehicle routing problems (CVRP) remains computationally challenging due to their combinatorial complexity. One approach to solve large-scale vehicle routing optimization is to identify promising subproblems and then optimize them using solvers. In this paper, we propose a framework of automatic heuristic design (AHD) in which a large language model (LLM) autonomously refines heuristics for ...
  </details>

- **2026-11-23** — Richard Shaw, Arthur Moreau, Athanasios Papaioannou et al. — [WildAnySplat: Feed-Forward 3D Gaussian Splatting in the Wild](http://arxiv.org/abs/2611.31023v1)
  <details><summary>📄 Abstract</summary>
  We present WildAnySplat, a feed-forward 3D Gaussian Splatting framework that enables robust novel-view synthesis from in-the-wild multi-view images. Unlike controlled captures, real-world images often contain multi-view inconsistencies caused by transient occluders, illumination changes, and camera ISP, which degrade the quality of existing feed-forward reconstruction methods.   To address this challenge, we introduce a student-teacher framework that learns transient-robust and appearance-consis...
  </details>

- **2026-11-23** — Yue Pei, Shining Bo, Yingying Zhang et al. — [Evaluable Language-Model Treatment Policies for Sepsis Resuscitation via Offline Value-Guided Selection](http://arxiv.org/abs/2611.30951v1)
  <details><summary>📄 Abstract</summary>
  Offline treatment learning must balance imitation, which stays close to logged evidence but ignores outcomes, against value maximisation, which uses outcomes but drifts toward treatments the records cannot verify. Numerical reinforcement learning strikes this balance during training. For large language models (LLMs), directly using sparse retrospective outcomes for fine-tuning raises challenges of delayed credit assignment and limited evidence for alternative treatments. We present R-LLMC, which...
  </details>

- **2026-11-23** — Elisabeth Fink — [LimeTree: Linear-Memory Graph Neural Networks over Tree-Graphs for Resource-Efficient Language Modeling and Context Extrapolation](http://arxiv.org/abs/2611.30934v1)
  <details><summary>📄 Abstract</summary>
  The search for computationally efficient alternatives to the Transformer has yielded numerous architectures in recent years; however, most exhibit severe weaknesses in associative recall-such as key-value (KV) retrieval-and length extrapolation, where even standard Transformers struggle. This paper introduces LimeTree, a linear-complexity architecture in both memory and compute for sequence modeling. By integrating synthetic KV retrieval tasks directly into standard language modeling training, L...
  </details>

- **2026-11-23** — Andrei Khurshudov — [Can Cities Have Personalities? Introducing the SCD City Personality Assessment](http://arxiv.org/abs/2611.30733v1)
  <details><summary>📄 Abstract</summary>
  Descriptions of cities are shaped by human experience and institutional narratives. We introduce the SCD City Personality Assessment (SCD-CPA), a method that instantiates document-grounded ChatGPT city personas and interrogates each with an identical 24-statement instrument inspired by the four-pair structure of the Myers-Briggs Type Indicator. Rather than asking a general-purpose model to characterize cities freely, we configure a separate document-grounded conversational agent for each city an...
  </details>

- **2026-11-23** — Yan Tan, Liwei Xu, Tao Yin — [A new frequency-time hybrid RPML-BIE solver with few-mode corrections for the wave-equation problems in nonuniform closed waveguides](http://arxiv.org/abs/2611.30579v1)
  <details><summary>📄 Abstract</summary>
  This paper is devoted to proposing a novel FTH integral equation solver for wave-equation problems in two-dimensional nonuniform closed waveguides with multiple channels. The FTH methodology, which combines the Fourier transform with frequency-domain BIE formulations, has demonstrated its effectiveness in solving time-dependent wave scattering problems. However, when applied to waveguide problems, the modal expansions arising from multiple scattering introduce cut-off frequencies. Such frequenci...
  </details>

- **2026-11-23** — Junrui Zhang, Zeyu Xu, Runchuan Zhu et al. — [Revisiting LLMs as Context Engineers](http://arxiv.org/abs/2611.30494v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are used in more and more new tasks, context engineering becomes a fundamental method to efficiently steer LLMs by constructing instruction prompts or metadata without intensive training. A growing number of LLM context engineering (LCE) approaches automate the task by casting the LLM itself as the engineer that draws generalizable instructions or experiences from offline trials as context. Although these methods resemble how humans learn from experiences, it rema...
  </details>

- **2026-11-23** — Junho Song, Jong-Hwan Jang, Joon-Myoung Kwon et al. — [HEART: Hierarchical Expert Adaptive Refinement Transformer for ECG Representation Learning](http://arxiv.org/abs/2611.30298v1)
  <details><summary>📄 Abstract</summary>
  Learning robust representations from electrocardiograms (ECGs) is challenging because repeated cardiac cycles coexist with subtle and sparse diagnostic cues in local morphology and rhythm-level context. Existing ECG foundation models commonly rely on Transformerbased patch encoders with uniformly shared dense refinement pathways, limiting adaptive processing across heterogeneous ECG tokens. We propose HEART (Hierarchical Expert Adaptive Refinement Transformer), an ECG foundation model that intro...
  </details>

- **2026-11-23** — Mollah Md Saif, Showrin Rahman, Anindya Majumder et al. — [Benchmarking Geospatial Foundation Models under Calibrated Label Errors](http://arxiv.org/abs/2611.30215v1)
  <details><summary>📄 Abstract</summary>
  Earth-observation labels from maps, older products or hurried annotation arrive misaligned, coarse, loosely outlined or incomplete. Geospatial foundation models (GFMs) are nevertheless benchmarked with labels taken as correct. A practitioner therefore cannot tell which encoder to choose when the labels are imperfect. We present a benchmark protocol for fine-tuning under such labels. Four spatially structured error types are calibrated to equal label mIoU and applied identically to every model an...
  </details>

- **2026-11-23** — Sungyoung Ha, Yujin Kang, Seonjung Kim et al. — [UV3CP: Universal ViT-Based 3D Channel Predictor for MIMO-OFDM Systems](http://arxiv.org/abs/2611.30128v1)
  <details><summary>📄 Abstract</summary>
  Channel aging in time-division duplex multiple-input multiple-output orthogonal frequency division multiplexing (MIMO-OFDM) systems causes a mismatch between uplink-based channel state information and the downlink channel at the transmission instant. Although vision transformers (ViTs) are effective for channel prediction, their performance is highly sensitive to the patch size, whose optimum depends on the channel coherence region. Moreover, changing the patch size typically requires retraining...
  </details>

- **2026-11-23** — Pratyush Acharya, Nuraj Rimal, Apar Baral et al. — [Character Information in Language Models: A Prompt-Independent Word Store and a Late, Question-Driven Signal That Grows With Scale](http://arxiv.org/abs/2611.30094v1)
  <details><summary>📄 Abstract</summary>
  Linear probes recover character properties of a word from a language model's hidden states, but a probe at the answer position cannot say whether the property was stored with the word or produced because the prompt asked for it. We separate the two with a word-position baseline: the same held-out-word probe applied to the query word's own tokens in a sentence that asks nothing. Across 16 open-weight models from seven families (0.6B--14B) and eleven character tasks, the word tokens encode \texttt...
  </details>

- **2026-11-23** — Matias Marambio-Jimenez, Yosuke Minowa, Yoshito Ono et al. — [Performance of attention-based deep-learning models in Shack-Hartmann wavefront sensor measurements](http://arxiv.org/abs/2611.29991v1)
  <details><summary>📄 Abstract</summary>
  A systematic performance evaluation of attention-based deep-learning models for wavefront reconstruction in Shack-Hartmann wavefront sensor (SHWFS) systems is presented. While deep learning has been extensively applied to pyramid and focal-plane wavefront sensing, its application to standard SHWFS configurations remains relatively underexplored. A simulation dataset consisting of 3.5 million open-loop uncorrelated turbulent phase and image pairs modeled after the Subaru Telescope pupil was gener...
  </details>

- **2026-11-22** — Manyi Li, Yufan Liu, Bing Li et al. — [Robust Concept Erasure in Text-to-Image Models via Simulating Brain Functional Localization](http://arxiv.org/abs/2611.29288v1)
  <details><summary>📄 Abstract</summary>
  Concept erasure in text-to-image models aims to prevent a target concept from appearing in generated images while preserving general image generation capability. However, erased concepts can still be reactivated by attacks. Prior attacks mainly search text or image input spaces, leaving the initial latent space underexplored. To address this gap, we introduce IVO (Initial latent Variable Optimization), a new concept reactivation attack that changes the starting point of image generation by optim...
  </details>

- **2026-11-22** — Delin An, Mingqi Xu, Jian-Xun Wang et al. — [MISeg-Agent: A Human-in-the-Loop Agentic Framework for Error Diagnosis and Executable Prompt Review in 3D Medical Image Segmentation](http://arxiv.org/abs/2611.29741v1)
  <details><summary>📄 Abstract</summary>
  Despite the strong performance of modern medical image segmentation models, their predictions can still contain localized errors that compromise segmentation quality. Identifying and correcting these errors is therefore essential for improving the reliability of existing segmentation results. While interactive segmentation models enable targeted corrections, identifying potential errors, determining where to intervene, and evaluating corrective actions remain challenging. Moreover, each correcti...
  </details>

- **2026-11-22** — Mohammad Kasra Habib,  Umm-e-Habiba, Daniel Graziotin et al. — [ReqSeek: Transformer-Based Automatic Requirements Identification for Building Large Requirements Datasets](http://arxiv.org/abs/2611.29722v1)
  <details><summary>📄 Abstract</summary>
  Large, diverse, and high-quality datasets are significant for advancing AI in requirements engineering, yet automated identification of requirements from Software Requirement Specifications (SRS) remains a challenge. Automatic Requirements Identification (ARI) methods demonstrate limited generalization to unseen documents across heterogeneous SRSs. This work presents ReqSeek, a transformer-based, domain-agnostic ARI model for recognizing ISO 29148-style requirements in SRS documents, supporting ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

- **2026-11-24** — Yifan Duan, Lihuan Li, Chao Xue et al. — [RecordRoute: Auditing Agent Failures with Localization-Guided Diagnosis](http://arxiv.org/abs/2611.33022v1)
  <details><summary>📄 Abstract</summary>
  Auditing failed agent executions requires identifying the responsible actor, the earliest decisive step, and the error mode. Representative supervised methods either focus on step localization or predict multiple attribution targets from shared trajectory representations. These methods do not use the localization result to select the text for mode diagnosis. To address this limitation, we propose RecordRoute, which couples comparative localization with local diagnosis. Specifically, it represent...
  </details>

- **2026-11-24** — Shilin Ma, Xingming Shui, Jinglin Chen et al. — [OmniHarness-RSI: Modality-Aware Harness Evolution for Omnimodal Understanding](http://arxiv.org/abs/2611.32951v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in harness-based recursive self-improvement (RSI) have improved video understanding by evolving executable agent workflows without updating foundation model parameters. However, extending this paradigm to omnimodal understanding remains challenging, as the heterogeneous and interdependent nature of multimodal perception and reasoning creates a complex evolution space, making targeted harness optimization difficult. To address these challenges, we propose OmniHarness-RSI, a modali...
  </details>

- **2026-11-23** — Ian Miao, Fangrui Zhu, Bowen Jiang — [Provenance Loss and Repair in Multilingual Compaction](http://arxiv.org/abs/2611.31668v1)
  <details><summary>📄 Abstract</summary>
  Conversational assistants compact older messages into short notes and evict the originals. When the note's language requires a distinction that English leaves open, such as Spanish adjective gender (agotado vs. agotada), messages that omit or explicitly state that attribute can yield the same note. After eviction, later turns cannot tell them apart: taking the inflected form literally asserts an attribute the user never gave, whereas discounting it as routine grammar discards one the user did gi...
  </details>

- **2026-11-23** — Yikun Chi, Adam Davies, Debarati Das et al. — [COGENT: A Modular Cognitive Architecture for Agentic User Simulation](http://arxiv.org/abs/2611.31559v1)
  <details><summary>📄 Abstract</summary>
  LLM-based user simulation can support interface design, accessibility research, and interactive-agent evaluation, but standard computer-use agents are optimized for task completion rather than reproducing how people perceive, reason, and act. We introduce COGENT (COGnitive agENT), a modular cognitive architecture for simulating user interaction with desktop interfaces. COGENT draws on established cognitive theories, such as Norman's action cycle and ACT-R, to enable explainable, intervenable, an...
  </details>

- **2026-11-23** — Marcus Gawronsky — [Pretrained Tabular Features and the Measurement of Financial Proximity](http://arxiv.org/abs/2611.31491v1)
  <details><summary>📄 Abstract</summary>
  Spatial arbitrage pricing theory (S-APT) extends factor models to allow returns to spill over between connected firms, beyond what common risk factors explain. In recent years, tabular foundation models (TFMs) have matched or outperformed tuned gradient-boosted and bagged ensembles on small and medium-sized tabular benchmarks. Although their predictive performance is strong, these models reveal little about what they have learned, which limits their use in regulated financial applications that r...
  </details>

- **2026-11-23** — Yulliwas Ameur, Miqeas Pedro Mendes, Samia Bouzefrane — [Intent-Conditioned Argument Mediation for Tool-Using LLM Agents: Blocking Trusted-but-Unauthorized Arguments](http://arxiv.org/abs/2611.30745v1)
  <details><summary>📄 Abstract</summary>
  LLM agents turn a user's request and retrieved content into tool calls, and a call can reach the wrong recipient, endpoint, file or participant. Argument-level provenance blocks such values when they come from untrusted content, but accepts a trusted value that the user never requested. IntentFlow, a mediation layer between an unmodified planner and its tools, checks each authority-bearing argument against an intent contract and a provenance policy. On a synthetic benchmark of 200 attacks (oracl...
  </details>

- **2026-11-23** — Aggelos Semoglou, Thomas Tselentis, John Pavlopoulos — [CART: Clustering-based Analysis of Recurring narratives for Taxonomy construction](http://arxiv.org/abs/2611.30993v1)
  <details><summary>📄 Abstract</summary>
  We present CART, a computational pipeline for extracting political narratives from parliamentary discourse and organizing them into a data-driven taxonomy without relying on predefined narrative categories. It encodes parliamentary discourse using semantic representations, filters relevant and reliable content through unsupervised confidence estimation, extracts narrative statements using LLMs, and uses narrative clustering and cluster analysis to construct a narrative taxonomy. Applied to Greek...
  </details>

- **2026-11-23** — Hongchuan Zeng, Bowen Liu, Changjiang Gao et al. — [CocoonBench: Can Multilingual Search Agents Escape Language Information Cocoons?](http://arxiv.org/abs/2611.30727v1)
  <details><summary>📄 Abstract</summary>
  Multilingual search agents can access the global Web, yet may remain trapped in a language environment with insufficient evidence; we refer to this failure as a language information cocoon. However, existing search benchmarks largely operate within a single language, especially English, overlooking entity connections across multiple languages. We introduce CocoonBench, a benchmark that evaluates whether multilingual search agents can escape such language information cocoons. CocoonBench mines an...
  </details>

- **2026-11-23** — Ramraj Chandradevan, Sayontan Ghosh, Vinoth Selvendran — [CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting](http://arxiv.org/abs/2611.31185v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-GRAFT, a reward-agnostic interventional attribution framework in which an RL-trained agent and its pre-RL initialization jointly generate a single trajectory under closed-loop execution with live retrieval. Each policy c...
  </details>

- **2026-11-23** — S. Riggi, A. Ingallinera, C. Bordiu et al. — [MAASAI: A Tool-Augmented Multi-Agent System for Astronomical Data Analysis](http://arxiv.org/abs/2611.31088v1)
  <details><summary>📄 Abstract</summary>
  Modern astronomical workflows require the coordinated use of specialised software, scientific archives, heterogeneous data, and domain-specific knowledge. Advances in large language models and multimodal foundation models enable natural-language interaction with scientific data and tools. Realising this potential requires integrating these models with established scientific capabilities.   We present MAASAI (Multi-agent Astronomy Assistant for Scientific Analysis and Inference), a modular multi-...
  </details>

- **2026-11-23** — Yujie Zhang, Tianyi Zhao, Guanghui Min et al. — [Beyond Patching: Consistent Circuit Discovery via Gradient Spectral Analysis](http://arxiv.org/abs/2611.30939v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability seeks to reverse-engineer neural networks by identifying small, faithful subgraphs--circuits--that implement specific behaviors. The dominant paradigm scores each unit by replacing its clean activation with a corrupted counterpart as causal intervention. While effective, this approach rests on a brittle prerequisite: the structure prompt pairs are task-specific, expensive to engineer, and silently couple the discovered circuit to prompt-design choices. In this work, ...
  </details>

- **2026-11-23** — Jesper Derehag — [Doc-to-LoRA Analysis: Query Conditioning, Wrong Facts, and Distractor Interference](http://arxiv.org/abs/2611.30825v1)
  <details><summary>📄 Abstract</summary>
  Doc-to-LoRA (D2L) compiles documents into low-rank adapters, allowing language models to use their contents without repeatedly processing the original text. We investigate its suitability for internalizing user memories through factual question answering, controlled interventions, and a production MidBrain memory pipeline. Across Gemma-2-2B and Qwen3-4B, D2L loses accuracy relative to in-context learning, with additional documents introducing substantial interference. Single-document errors freq...
  </details>

- **2026-11-23** — Ying Fu, Yulong Fu — [ArguShield: Enforcing Minimum-Necessary Disclosure in Tool-Calling LLM Agents](http://arxiv.org/abs/2611.30360v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly use third-party tools to complete user tasks. Even without malicious intent, they may fill broad or weakly constrained fields with private information that is unnecessary or inappropriate for the receiving tool. Such calls can satisfy the tool schema and complete the task, yet still violate minimum-necessary disclosure. We introduce ArguShield, a mediation layer that intercepts proposed tool calls before execution. It evaluates each candidate value using ...
  </details>

- **2026-11-23** — Xiaoqian Hu, Ruihong Qiu, Yanran Tang et al. — [CARE-3D: Reinforcement Learning for Evidence Grounded Agentic Reasoning in Situated 3D Scenes](http://arxiv.org/abs/2611.29969v1)
  <details><summary>📄 Abstract</summary>
  Situated 3D reasoning requires embodied agents to interpret objects, scene geometry, and viewpoint dependent spatial relations. Existing methods learn grounded interactions from supervised traces, but largely imitate prescribed evidence acquisition patterns rather than optimizing the support that the returned evidence provides for the correct answer. Moreover, outcome rewards provide limited credit for intermediate tool choices and may leave infrequent tools underexplored. An effective agent sho...
  </details>

- **2026-11-23** — Yanan Zhang, Shengqi Liu, Tao Zhang et al. — [LLM-Assisted Software Migration: from Module-Level Transformation to Repository-Level Integration](http://arxiv.org/abs/2611.29942v1)
  <details><summary>📄 Abstract</summary>
  Software migration adapts an existing implementation to a new language, version, API, framework, or platform while preserving its behavior. Large language models (LLMs) succeed on individual functions and modules, but this success does not readily carry over to entire repositories, particularly deployable applications. This survey reviews LLM-assisted migration from module-level transformation to repository-level integration, culminating in the delivery of complete applications. We analyze 96 so...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-11-23** — Devang Kulshreshtha, Priyanka Kaswan, Minh Pham et al. — [Multimodal View Training: Learning More Through Different Modalities](http://arxiv.org/abs/2611.30165v1)
  <details><summary>📄 Abstract</summary>
  Can a language model learn more from the same information simply by encountering it in different forms? We answer this in the affirmative by introducing Multimodal View Training (MVT), a simple training approach that presents identical information through text, speech, and images, without requiring new facts or supervision. Starting from a text sample, MVT generates corresponding audio and rendered-text image views, and trains a multimodal language model to produce the same target output across ...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-11-23** — Benjamin Alt — [SayDo: Benchmarking the Safety of Frontier Models from Chat to Closed-Loop Robot Control](http://arxiv.org/abs/2611.30957v1)
  <details><summary>📄 Abstract</summary>
  Frontier vision-language models (VLMs) are increasingly used as high-level robot controllers, yet their safety is evaluated almost entirely in text. We introduce SayDo, a benchmark that assesses the propensity of frontier models to cause harm in embodied contexts. SayDo comprises eleven laboratory and household tasks that pair a benign instruction with a hazard latent in the scene. Tasks are implemented in six settings along an embodiment gradient, from chat questions about an imagined robot to ...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 6 papers

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

- **2026-11-23** — Federico Semenzato, Benjamin D. Wandelt, Michele Liguori et al. — [Interpretable morphology-based marked statistics](http://arxiv.org/abs/2611.31167v1)
  <details><summary>📄 Abstract</summary>
  The shapes and environments of cosmic structures carry cosmological information beyond the matter power spectrum. Recovering this information while retaining a physical understanding is a central challenge for cosmological inference. We construct an interpretable, rotation-equivariant neural marking scheme that reweights the matter field, combining learned density responses with explicit measures of local morphology. This approach enables direct inspection of the learned transformations, while r...
  </details>

- **2026-11-23** — Carlos Rafael Catalan, Lheane Marie Dizon, Patricia Nicole Monderin et al. — [Useful but Unwieldy: How Software Engineers Perceive the Design of Chain-of-Thought Explanations in Coding Agents](http://arxiv.org/abs/2611.30894v1)
  <details><summary>📄 Abstract</summary>
  Coding agents (CAs) powered by Large Language Models (LLMs) are increasingly integrated into software engineering (SE) workflows. As these CAs take up more tasks and responsibilities, it is imperative for software engineers to understand the CA's rationale behind its' decisions, also known as the chain-of-thought (CoT). During the interaction, some CAs are capable of showing this CoT as a separate message to users with the goal of providing transparency and explainability. However, its effective...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 169 papers

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

- **2026-11-23** — Gautam Choudhary, Jack Peng, Udesh Kumarasinghe et al. — [LimoBench: How Street Smart Are Large Language Models?](http://arxiv.org/abs/2611.31682v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have transformed how humans interact with information, enabling natural-language interfaces across various domains. They are increasingly deployed for geospatial applications including map-based question answering, location-based services, and natural-language interfaces to spatial databases. But are LLMs truly location-aware, able to reliably interpret and precisely answer location queries involving real-world coordinates, points of interest (POIs), and geospatial d...
  </details>

- **2026-11-23** — Donna Pham, Zhongwei Xu, Siyuan Dong et al. — [Rethinking Document Indexing for LLM-based Analysis](http://arxiv.org/abs/2611.31679v1)
  <details><summary>📄 Abstract</summary>
  Documents such as clinical records, legal contracts, and scientific papers are increasingly analyzed with large language models (LLMs). The naïve approach of prompting the model with the full text for every question is slow, expensive, prone to hallucination on long inputs, and reuses no work across questions. Retrieval-augmented generation (RAG) systems build reusable state to address this, but they store it as embedded chunks: slicing text into fragments can lose the meaning that spans them, a...
  </details>

- **2026-11-23** — Davood Wadi, Yu Ma — [Training decision models for simulating human respondents](http://arxiv.org/abs/2611.31613v1)
  <details><summary>📄 Abstract</summary>
  Researchers increasingly use large language models (LLMs) as synthetic respondents in market research, conjoint analysis, and randomized experiments. However, synthetic choice data from off-the-shelf generative LLMs bias downstream econometric inference. Neither proprietary models nor higher reasoning effort reliably reduces this bias. We investigate decision models (System One architectures) for silicon sampling. Using choice training, we update KEV model weights on historical respondent-level ...
  </details>

- **2026-11-23** — Muhammad Usman, Nafis M. Arefin, Akil Narayan et al. — [Uncertainty Quantification and Global Sensitivity Analysis of Patient-Specific Coronary Hemodynamics Under Unsteady Flow Conditions](http://arxiv.org/abs/2611.31594v1)
  <details><summary>📄 Abstract</summary>
  Patient-specific computational models of the coronary arteries demonstrate transformative potential for physiological assessment, identifying hemodynamic markers associated with disease progression, and optimizing treatment. Unfortunately, these models rarely account for input parameter uncertainty, limiting confidence in predictions and their clinical interpretation. Herein, we present a novel uncertainty quantification-finite element framework that integrates computationally efficient techniqu...
  </details>

- **2026-11-23** — Zhanwen Chen, Tianchun Wang — [One Step, Four Clocks: How GUI Agents Fall Out of Step](http://arxiv.org/abs/2611.31522v1)
  <details><summary>📄 Abstract</summary>
  GUI agents can choose correct actions yet fail as interfaces change during deliberation. Latency alone cannot explain these failures because actions may become invalid at different interaction stages. We model four events: environment change, observation availability, decision commitment, and action receipt (EODA). We introduce ChronotopeGym to study these failures under Paused, Replay, and Live execution. Across five tasks, agents can fail in Live despite succeeding when responses remain valid,...
  </details>

- **2026-11-23** — Anthony Cuturrufo, Ratul Ghosh, Devashish Khatwani et al. — [PatientFlowSynth: Evaluating FHIR Agents with Matched Patient Charts](http://arxiv.org/abs/2611.31521v1)
  <details><summary>📄 Abstract</summary>
  Agents that search patient charts must classify claims from retrieved records, including cases with missing or conflicting evidence. In Fast Healthcare Interoperability Resources (FHIR), status fields can change how those records should be interpreted. PatientFlowSynth provides 18,000 tasks from 225 synthetic patients and 18 templates that hold the patient, question, and retrieval program fixed across chart variants representing four evidence states. Re-executing the program verifies each varian...
  </details>

- **2026-11-23** — Xiwei Liu, Yulong Li, Xuhui Li et al. — [SpatialCraft: Evolving Procedural Intelligence from Experience and Skills for Spatial Reasoning Agents](http://arxiv.org/abs/2611.31475v1)
  <details><summary>📄 Abstract</summary>
  Spatial reasoning agents increasingly rely on external tools, such as 3D reconstruction, segmentation, and geometric computation, to answer questions that a multimodal large language model (MLLM) cannot resolve from pixels alone. Tool access, however, shifts the bottleneck to orchestration: the agent must decide which tools to call, in what order, and how to interpret their outputs, yet a stateless agent repeats the same mistakes across tasks. We ask whether a frozen tool-using agent can improve...
  </details>

- **2026-11-23** — Wenhao Wang, Panrong Tong, Quyu Kong et al. — [Self-Evolving Evaluation Environments for Computer-Use Agents](http://arxiv.org/abs/2611.30962v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs) are rapidly improving, yet their evaluation remains largely static. Existing benchmarks provide a strong foundation, but fixed difficulty ceilings, limited feature coverage, and coarse aggregate scores progressively weaken their discriminative and diagnostic value. We introduce CUA-SEE, a closed-loop evaluation environment that co-evolves tasks and executable verifiers from rollout evidence. It disentangles three objectives: benchmark evolution expands evaluation scope...
  </details>

- **2026-11-23** — Hamed Abdi, Kiarash Banihashem, MohammadTaghi Hajiaghayi et al. — [Optimal Matroid Prophets against Almighty Adversaries and Delegation](http://arxiv.org/abs/2611.30933v1)
  <details><summary>📄 Abstract</summary>
  We prove an optimal one-half matroid prophet inequality against an almighty ordering adversary: the adversary observes every realized value before choosing the arrival order, whereas the algorithm sees values only as they arrive and must accept irrevocably. The algorithm is deterministic, and its guarantee holds against the stronger ex-ante relaxation. Before any values are revealed, it partitions the ground set, replaces the matroid by a stricter direct sum of minors, and fixes one threshold fo...
  </details>

- **2026-11-23** — Igor Santos-Grueiro, Daniel Romero-Ruiz — [Oops!... I Parsed It Again: Tool-Call Smuggling Against LLM Agents](http://arxiv.org/abs/2611.30624v1)
  <details><summary>📄 Abstract</summary>
  LLM agents act through tool calls: the model writes the arguments of a call as JSON, a guard decides whether the call may run, and an executor runs it. The same bytes are parsed several times, by the provider, gateways, SDKs, frameworks, the guard, and the executor. JSON leaves some choices to each parser, such as which copy of a repeated key counts. When the guard and the executor choose differently, the guard approves one call, the executor runs another, and the audit log records the approved ...
  </details>

- **2026-11-23** — Aniruddh Pramod, Matthew Khoriaty, James Lucassen et al. — [Interrogation Protocols for AI Control](http://arxiv.org/abs/2611.30583v1)
  <details><summary>📄 Abstract</summary>
  As the intelligence of an AI agent increases relative to a trusted monitor, so does the risk that the monitor will fail to understand the agent's actions or to evaluate them confidently. We introduce interrogation protocols to a high-stakes AI control setting, and allow the monitor to ask the untrusted agent questions about confusing actions. For interrogation to improve safety, a weaker model must be able to distinguish misleading explanations produced by an attack policy from genuine ones prod...
  </details>

- **2026-11-23** — Hongli Shen, Shaopeng Fu, Qinbo Zhang et al. — [Learning Teacher Output Preferences from Final Responses for Reasoning Distillation](http://arxiv.org/abs/2611.30338v1)
  <details><summary>📄 Abstract</summary>
  Many large language models (LLMs) use chain-of-thought (CoT) to solve complex problems, but hide their CoT traces to prevent reasoning capabilities from being distilled. While recent studies have shown that hidden CoTs can be reconstructed, existing methods typically require training a separate attacker for each target LLM. This paper studies model-agnostic CoT reconstruction, aiming to reconstruct hidden CoT traces from arbitrary target LLMs using only input prompts and visible final responses....
  </details>

- **2026-11-23** — Son T. Huynh, Thuy T. Le, Thu H. A. Huynh et al. — [Genome-to-Image Translation: Reconstructing Escherichia coli Morphology from Genomic Sequences](http://arxiv.org/abs/2611.31132v1)
  <details><summary>📄 Abstract</summary>
  Antimicrobial resistance in Escherichia coli is established in routine practice by culture-based susceptibility testing, which is slow relative to the clinical need for an early treatment decision. Resistance status also leaves a measurable trace in cell morphology, and whole-genome sequencing of clinical isolates is increasingly available, which raises the question of whether colony appearance can be predicted directly from an isolate's genome. We formulate this as a conditional image-generatio...
  </details>

- **2026-11-23** — Hengzhi Jiang, Haixu Liu, Jindou Jia et al. — [Boltz-Flow: Generating High-Quality Robot Action from Boltzmann Machine](http://arxiv.org/abs/2611.31038v1)
  <details><summary>📄 Abstract</summary>
  Flow-matching policies integrate a velocity field from a fixed, observation-independent Gaussian source. However, since the source is unimodal and identical across all tasks, the limited representational capacity of Gaussian distributions constrains how far a policy can scale with growing task diversity. Moreover, the source factorizes over time steps and control dimensions, discarding the coordination that manipulation requires. We introduce Boltz-Flow, which replaces Gaussian initialization wi...
  </details>

- **2026-11-23** — Sung Eun Kim, Xiaoman Zhang, Xucheng Wang et al. — [SurgeCount: A Protocol-Guided Composition Harness for Bimanual Surgical Sponge Counting](http://arxiv.org/abs/2611.31037v1)
  <details><summary>📄 Abstract</summary>
  We present SurgeCount, a system for auditable robotic surgical sponge counting that composes learned skills under a written procedural protocol. Retained sponges cause preventable harm, and surgical teams count every sponge before closure to reduce that risk. The robot repeatedly isolates one deformable sponge from a tangled pile and places it in the next numbered counting-tray slot, requiring handling of occluded grasp threads while preserving step order. We train one subtask-conditioned policy...
  </details>

- **2026-11-23** — Jinkun Liu, Yingze Wang, Situ Wang et al. — [RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments](http://arxiv.org/abs/2611.31002v1)
  <details><summary>📄 Abstract</summary>
  Agentic Robotics, in which foundation models act as coding agents to control robots through executable programs, has emerged as a compelling paradigm for embodied intelligence. Yet unlike software engineering, where massive executable environments power post-training, robotics remains constrained by small, manual benchmarks and in-distribution evaluation. To bridge this gap, we introduce RoboUniverse-10K, 10,807 interactive, resettable, and verifiable physics environments built from real-world v...
  </details>

- **2026-11-23** — Milan Vojnovic — [Aggregation Rules Induced by KL-Regularised Preference Dynamics on Networks](http://arxiv.org/abs/2611.30941v1)
  <details><summary>📄 Abstract</summary>
  We study agents that each align a model to their own preference data while observing one another, and ask which aggregation rule the resulting policies implement. Each round, an agent takes one KL-regularised step. The step involves a reference that the agent is penalised for leaving and a challenger against which its responses are compared, and each of the two may be the agent's own or an average over the agents it observes; attention need not be reciprocal. Aggregating the reference makes the ...
  </details>

- **2026-11-23** — Horst-Holger Boltz, Max-Robin Schultz, Thomas Ihle — [Statistical mechanics of noisy collisions in active matter: Dyson-Landau theory](http://arxiv.org/abs/2611.30910v1)
  <details><summary>📄 Abstract</summary>
  Active systems and other coarse-grained descriptions are often modeled by generalized dynamics, effective equations of motion that are not bound by the constraints of genuinely microscopic physics. In particular, these equations are generally stochastic on the smallest resolved scale. This poses a challenge to first-principles statistical physics, which usually derives emergent noise on larger scales from deterministic interactions. Here, we show how to systematically incorporate microscopic noi...
  </details>

- **2026-11-23** — Anh Dao, Quan-Dung Pham, Danh Vinh Le et al. — [GlanceNav: Efficient Vision-and-Language Navigation with Streaming Memory and Counterfactual Rewind](http://arxiv.org/abs/2611.30900v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have become strong policies for vision-and-language navigation (VLN). However, most of them encode a sample of past frames again at every decision and are trained on isolated decisions, so computation is redundant and the usable history is short. They also learn from their own mistakes through outcome rewards that give one scalar to a whole episode. We ask whether a navigator can encode each frame only once, at a constant cost per step, and still remember...
  </details>

- **2026-11-23** — Yuan Gao, Dongchen Wei, Xinyang Lin et al. — [EgoDepth-Bench: Benchmarking Metric Depth for Egocentric Manipulation](http://arxiv.org/abs/2611.30734v1)
  <details><summary>📄 Abstract</summary>
  We introduce EgoDepth-Bench, comprising 941,233 synchronized samples collected across 37 distinct physical environments. Each sample combines six calibrated RGB views with metric depth in the native fisheye view, reconstructed from five active-infrared stereo modules. A calibrated ball-bar confirms millimeter-level geometric accuracy, with a median error of 1.27 mm on a known sphere spacing. Environment-held-out splits enable evaluation of generalization to unseen environments. Across monocular,...
  </details>

- **2026-11-23** — Y. Lu, L. Wang, S. Okada — [BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenization for Speech Language Models](http://arxiv.org/abs/2611.30723v1)
  <details><summary>📄 Abstract</summary>
  Speech language models (LMs) generate speech as sequences of discrete tokens. Their tokenizer must therefore preserve both acoustic detail and linguistic content at a low bitrate. Semantic-enhanced tokenizers may lose acoustic detail, whereas acoustic-oriented tokenizers retain acoustic variation that makes language modeling harder. Unified tokenizers combine both, but representing acoustic detail and linguistic content within a single feature space can cause interference between the two objecti...
  </details>

- **2026-11-23** — Matteo Pistillo, Isaak Mengesha, Charlotte Stix et al. — [Handoff at Frontier AI Companies](http://arxiv.org/abs/2611.30711v1)
  <details><summary>📄 Abstract</summary>
  The term "Handoff" captures frontier AI companies' ongoing delegation of all AI Research & Development (AI R&D) functions, including high-level decisions such as safety assessments and deployment decisions, to internally deployed AI agents. Handoff is progressing rapidly and will be complete once no human remains in the loop. This report aims to alert policymakers to the national security threats and Loss of Control risks that Handoff can create, and to advise them on how to monitor and respond ...
  </details>

- **2026-11-23** — Dominik Bernard Lau, Filip Pawlicki, Jan Dubiński et al. — [Uncovering the Tells: Efficient Black-Box Audits for LLM Data Contamination](http://arxiv.org/abs/2611.30639v1)
  <details><summary>📄 Abstract</summary>
  Existing methods for assessing training data contamination in Large Language Models achieve high accuracy, but fundamentally rely on gray-box access, rendering them inapplicable to fully black-box environments. This limitation forces auditors to rely on full-sequence sampling or rigid heuristics, both of which incur prohibitive inference costs and struggle to isolate the underlying memorization signal. To overcome this, we propose a generation-based black-box framework that infers context-induce...
  </details>

- **2026-11-23** — Matas Jurkevicius, Yen-Chia Hsu — [Automated Call for Action: RAG-Based Environmental Law Enforcement Screening System](http://arxiv.org/abs/2611.30423v1)
  <details><summary>📄 Abstract</summary>
  Environmental law inspectors face a structural issue in identifying potential violations from data: they often do not have the capacity to deal with large volume of data present in the emission events. This paper examines to what extent an LLM-based system can support evidence assembly and permit-based screening of such events, using the coke plants of a steel producer and a regional environmental service as a case. A simple puff-trajectory model aligns air quality measurements, weather and citi...
  </details>

- **2026-11-23** — Peilong Zhou, Cangyuan Li, Kaiyan Chang et al. — [HWRE-Bench: Can LLM Agents Understand Hardware They Did Not Design?](http://arxiv.org/abs/2611.30422v1)
  <details><summary>📄 Abstract</summary>
  Hardware benchmarks for LLM agents all run the design flow forward, from a specification to RTL, a layout or a bug fix. We ask the reverse question: given an implemented artifact, such as a layout, a gate-level netlist or a protected simulation model, can an agent work out what it does well enough to act on that knowledge? We introduce HWRE-Bench, a benchmark for agentic hardware reverse engineering built on one observation. Each step of the forward flow discards information (names, hierarchy, w...
  </details>

- **2026-11-23** — Giuseppe Canonaco, Alberto Pozanco, Daniel Borrajo — [Cost-Sensitive Reversibility of Non-Deterministic Actions](http://arxiv.org/abs/2611.30399v1)
  <details><summary>📄 Abstract</summary>
  Determining action reversibility requires checking whether the effects of an action can be undone. Recent work has extended reversibility to fully observable non-deterministic (FOND) planning. It distinguishes weak reversibility, where reversal may succeed, from strong-cyclic reversibility, where reversal is guaranteed under fairness. These notions are qualitative: they say whether reversal is possible, but not how costly it is.   We introduce cost-sensitive reversibility for non-deterministic a...
  </details>

- **2026-11-23** — Di Xin, Mingfei Han, Genming Cui et al. — [SOAR: temporal Structure-guided One-step Action generation for Robotic manipulation](http://arxiv.org/abs/2611.30363v1)
  <details><summary>📄 Abstract</summary>
  Efficient robotic manipulation requires temporally coordinated actions with low inference latency. Multi-step diffusion and flow policies progressively refine action trajectories but require costly iterative inference, whereas one-step policies eliminate iterative trajectory refinement to reduce inference cost. We introduce **SOAR**, a structure-guided one-step generative policy that improves action quality while preserving one-step efficiency. SOAR predicts an observation-conditioned discrete c...
  </details>

- **2026-11-23** —  Innata Team, Yu Bai, Ziyi Bai et al. — [Innata-0: A Native Embodied World System with Model-Agent Co-Design](http://arxiv.org/abs/2611.30254v1)
  <details><summary>📄 Abstract</summary>
  The physical world is open-ended, dynamic, and partially observable. While foundation models have advanced embodied intelligence, standalone models struggle with long-horizon execution, and simply integrating models with agents may lead to inconsistencies between planning and physical control. To support reliable and adaptive behaviors in the physical world, we introduce Innata-0, a native embodied world system. Innata-0 jointly designs an embodied world-action model and an agent to combine thei...
  </details>

- **2026-11-23** — Zeqiang Wang — [Laya-IsoToken: Day-One Clinical Codebook Switching via Closed-Form Operator Compilation](http://arxiv.org/abs/2611.30196v1)
  <details><summary>📄 Abstract</summary>
  Healthcare systems periodically revise diagnostic and procedural classifications (ICD-9 to ICD-10/11), update hospital reimbursement groupers (MS-DRG), and deploy clinical coding across languages. Supervised coding networks bind clinical text encoders to fixed per-code classifier weights, forcing hospitals to re-annotate tens of thousands of records before switching codebooks, whereas standalone large language models incur high latency and hallucinate invalid codes. Here we show that day-one cli...
  </details>

- **2026-11-23** — Bingqi Huang, Bingchuan Wei, Yingkai Cai et al. — [Trustworthy agentic lunar robotics: safety-constrained contingent planning with a foundation-model planner](http://arxiv.org/abs/2611.30179v1)
  <details><summary>📄 Abstract</summary>
  Sustained lunar-base operations require robots that restore equipment and deliver cargo under conditions unforeseen before deployment. Flown space autonomy executes pre-validated procedures and enters a safe hold outside their scope, whereas foundation models synthesize plans on site that cannot be verified before execution. We formulate these operations as safety-constrained contingent planning with irreversible actions, erroneous records, three-valued physical evidence, and costly, deadline-co...
  </details>

- **2026-11-23** — Wenyang Gao, Yinghao Yang, Xi Jin et al. — [FiRE: Fine-grained Ranking Evaluation for Machine Translation](http://arxiv.org/abs/2611.30168v1)
  <details><summary>📄 Abstract</summary>
  Developing reliable machine translation (MT) systems hinges on our ability to distinguish superior translations from inferior ones. However, existing evaluation paradigms, whether limited to coarse overall rankings or misaligned with human preferences, fail to deliver interpretable, fine-grained feedback in reference-free settings. We present a Fine-Grained Ranking Evaluation method (FiRE) that leverages off-the-shelf large language models to perform criterion-driven pairwise comparison across t...
  </details>

- **2026-11-23** — Bao Quoc Trinh, Tin Van Huynh, Kiet Van Nguyen et al. — [OpenViVE: New Benchmark and Dual-Stream Co-Attention Framework for Vietnamese Visual Entailment](http://arxiv.org/abs/2611.30161v1)
  <details><summary>📄 Abstract</summary>
  Visual Entailment (VE) determines whether a textual hypothesis is entailed, contradicted, or unverifiable from an image. However, existing VE benchmarks are largely English-centric and do not capture Vietnamese-specific linguistic distinctions or culturally grounded visual contexts. To address this gap, we introduce OpenViVE, the first large-scale native Vietnamese VE benchmark, containing 62,268 balanced image-hypothesis pairs from 10,378 culturally grounded images. OpenViVE is constructed usin...
  </details>

- **2026-11-23** — Shenhao Miao, Yizhou Li, Liqiao Xia et al. — [Domain advantage in two-dimensional quantum-device design with multi-modal agentic harness](http://arxiv.org/abs/2611.30043v1)
  <details><summary>📄 Abstract</summary>
  High-quality two-dimensional quantum devices are commonly fabricated from mechanically exfoliated crystals, whose irregular shapes and placement require a lithographic layout tailored to each specimen. Drawing these layouts remains largely manual. We introduce qlaybench, a benchmark that tests whether language-model agents can turn microscope images and experimental requirements into device layouts that fit the specimen. Agents with conventional tools often construct devices when material outlin...
  </details>

- **2026-11-23** — Lachlan Cowley, Jey Han Lau, Yulia Otmakhova et al. — [How Relations Impose Embedding-Space Structure](http://arxiv.org/abs/2611.29986v1)
  <details><summary>📄 Abstract</summary>
  Language models are known to encode simple relations, such as synonymy, in the geometry of their representations. It is unclear whether they also encode complex patterns of relationships such as those that drive analogy. We present a simple method, with no learned parameters, based on comparing the internal structural arrangements between disparate domains, to test this. Using our method we find over multiple models that representations are arranged consistently to encode complex relationship si...
  </details>

- **2026-11-23** — Zexin He, Rui Li, Yushi Lan et al. — [ACAP: Asynchronous Coding Agents for Efficient Robot Control](http://arxiv.org/abs/2611.31205v1)
  <details><summary>📄 Abstract</summary>
  Coding agents can construct and revise robot behavior during execution, but using one agent for the whole robot can delay otherwise independent work. We introduce Asynchronous Coding Agents as Policy (ACAP), an asynchronous framework that organizes one robot as a team of persistent agents. Each member reasons and acts for a configurable control group, such as an arm with its gripper or the torso and chassis, enabling asynchronous reasoning and execution. However, different robot components often...
  </details>

- **2026-11-23** — Jinzhong Gu, Jiakai Chen, Xinyi Cao et al. — [Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real for Robot Manipulation](http://arxiv.org/abs/2611.31098v1)
  <details><summary>📄 Abstract</summary>
  Scaling robot manipulation learning remains challenging due to the high cost of collecting real-world interaction data. Real-to-Sim-to-Real (Real2Sim2Real) offers a promising route by enabling policy learning in simulation grounded in real-world observations, yet scaling this paradigm across diverse tasks and physical interactions remains difficult. We introduce Real2Worlds2Real, a self-improving agentic framework that integrates scalable simulation-world construction with policy development. Gi...
  </details>

- **2026-11-23** — Xinyang Zhou, Qi Li, Xinchao Wang — [WorldLeague: Benchmarking Physical Agency](http://arxiv.org/abs/2611.30989v1)
  <details><summary>📄 Abstract</summary>
  AI systems can now operate Blender, follow instructions in complex video games, and manipulate objects with robot arms. What range of physical goals can today's AI systems achieve autonomously? Answering this question requires testing systems on tasks that demand different combinations of perception, memory, planning, and action. We introduce \textbf{WorldLeague}, a benchmark that compares AI systems on a common set of \textbf{60 simulated robot tasks} by measuring progress toward each task's ph...
  </details>

- **2026-11-23** — Vinay Udit Mohan, Xuchuan Huang, Rolandos Alexandros Potamias — [DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation](http://arxiv.org/abs/2611.30907v1)
  <details><summary>📄 Abstract</summary>
  World models facilitate planning and control in robotic manipulation by enabling agents to anticipate the consequences of their actions. However, they typically rely on action-labelled interaction data that is costly to acquire and difficult to scale. These models are also often tied to the specific embodiment they were trained on, limiting transferability to previously unseen robot morphologies. We introduce a 3D latent-action world model that learns continuous action representations directly f...
  </details>

- **2026-11-23** — Paul Mattes, Ayman Abdeldayem, Denis Shcherba et al. — [Object Count Generalization Is an Interface Problem: Warping a Frozen Skill Instead of Retraining It](http://arxiv.org/abs/2611.30765v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning policies for robot manipulation degrade when the number of objects N in the scene grows beyond the training range. This is a covariate shift that also changes the dimension of the state. We propose WAVE (Warping Actions and Views of an Expert), which extends a pretrained single-object skill to many objects without updating its weights. WAVE has three parts. First, a selection policy picks the one object the robot works on next. Second, a warping policy reads a local view o...
  </details>

- **2026-11-23** — Nilay Kushawaha, Abdalla Swikir, Fares Abu-Dakka — [LLM-Guided Compositional Continual Learning for Robot Manipulation with Gated Low-Rank Experts](http://arxiv.org/abs/2611.30667v1)
  <details><summary>📄 Abstract</summary>
  General-purpose manipulation robots must acquire new skills over time without forgetting prior ones or retraining from scratch. We present a continual learning framework that represents each skill as a dedicated expert sub- network in a Progressive Neural Network (PNN). New tasks reuse prior knowledge through low-rank adaptation (LoRA) modules on lateral connections controlled by learnable per-parent gates, enabling explicit attenuation of individual transfer paths while reducing the parameter c...
  </details>

- **2026-11-23** — Hiroaki Honda, Koya Sakamoto, Shu Morikuni et al. — [SWEEP-Bench: Do Embodied Policies Act on the Speed They See?](http://arxiv.org/abs/2611.30637v1)
  <details><summary>📄 Abstract</summary>
  Robot policies must adapt to the speed of moving objects, yet existing benchmarks rarely measure this ability across diverse tasks and speeds. We introduce SWEEP-Bench, a simulation benchmark with 80 conveyor-belt manipulation tasks spanning 16 skill categories, each evaluated at 13 belt speeds (0.10-0.40 m/s). Objects are transported through physical contact with a visibly moving belt. Each task has a static counterpart, and each evaluation episode uses the same randomized scene at all 13 speed...
  </details>

- **2026-11-23** — Huan Xu, Maosen Zhao, Pengtao Chen et al. — [Quantizing Diffusion LLMs under Parallel Decoding: Commitment Risk and the Parallelism Tax](http://arxiv.org/abs/2611.30587v1)
  <details><summary>📄 Abstract</summary>
  Diffusion large language models (dLLMs) are served with accelerated decoders that cache context and commit, in one step, every masked position whose confidence clears a threshold. Yet post-training quantization of dLLMs has so far been calibrated and evaluated under fixed-step samplers without caching. We study W4A4 quantization under the deployed decoder and find that the decoder determines both where quantization harms accuracy and what it costs. Irreversible errors enter chiefly through force...
  </details>

- **2026-11-23** — Jiawei Guo, Yu Huang, Dijiang Dong et al. — [RoboInF: A Benchmark for Instruction Fidelity in Robotic Manipulation](http://arxiv.org/abs/2611.30555v1)
  <details><summary>📄 Abstract</summary>
  Precise language control requires embodied models to follow instructions governing both task outcomes and execution. Although recent methods train policies to follow increasingly detailed commands, existing benchmarks often assess instruction following alongside perception, planning, and generalization to unfamiliar scenes. Higher task success therefore offers limited evidence of closer adherence to instructions. We introduce RoboInF, a benchmark measuring how reliably manipulation policies adap...
  </details>

- **2026-11-23** — Lijun Han, Muyuan Ma, Zichen Wang et al. — [CHAMP: Coordinated Humanoid Loco-Manipulation with Whole-Body Motion Priors](http://arxiv.org/abs/2611.30449v1)
  <details><summary>📄 Abstract</summary>
  Coordinating locomotion and dexterous manipulation is fundamental to humanoid robots operating in human environments. A key challenge is learning motion priors from diverse data and using them effectively for coordinated robot control. We present CHAMP, a unified framework for humanoid loco-manipulation that combines whole-body motion pretraining with adaptive feature extraction. CHAMP pretrains a vision-language model to predict future body and hand motion from approximately 2,298 hours of hete...
  </details>

- **2026-11-23** — Yunhe Zhang, Long Gao, Yuedong Fu et al. — [ConsisX: Cross-View Consistency Thinking in 3D for Vision-Language-Action Models](http://arxiv.org/abs/2611.30308v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models integrate visual perception and language understanding from vision-language models (VLMs) with action prediction for robotic manipulation. Although multi-view observations provide complementary scene information, VLMs model cross-view interactions based on 2D feature similarity, which can lead to physical inconsistency in the form of cross-view incorrect association between distinct entities and cross-view information fragmentation about the same entity. To ad...
  </details>

- **2026-11-23** — Yunhe Zhang, Long Gao, Yuedong Fu et al. — [Beyond Which: Where, How, and When in Vision-Language-Action Models](http://arxiv.org/abs/2611.30291v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models typically rely on vision-language model (VLM) features as the primary perceptual source for action prediction, showing strong generalization across diverse robotic manipulation tasks. Although VLM features can identify which entities are relevant to action prediction, precise manipulation also requires understanding where task-relevant entities are located within the spatial layout, how their geometric structure constrains physical interaction, and when spatia...
  </details>

- **2026-11-23** — Yunbei Zhang, Zijian Jin, Janet Wang et al. — [RoboThink: Let the Agent Think, Let the Policy Act](http://arxiv.org/abs/2611.30111v1)
  <details><summary>📄 Abstract</summary>
  Robot policies act in real time but fail without knowing why, whereas a reasoning agent that watches the robot can often tell what went wrong. Existing systems either hand the agent control, which takes minutes per episode, or let it send instructions. Yet a policy follows a new instruction only from a fresh start, since a half-finished task leaves it in states outside its training data. Nor can an instruction fix how the robot moves. If a drift keeps pulling the hand to the left, "push right, s...
  </details>

- **2026-11-23** — Wentao Lu, Shengzhe Cui, Xihao Wu et al. — [FolioWeaver: A LayerGraph-Grounded Agent for Layered Image Generation and Editing](http://arxiv.org/abs/2611.30067v1)
  <details><summary>📄 Abstract</summary>
  Layered image generation separates images into compositable layers, allowing users to manipulate individual elements independently. However, such asset-level editability does not enable the generation system to interpret successive feedback, perform targeted edits, and preserve unaffected content. We introduce FolioWeaver, a LayerGraph-grounded agent that unifies layered-image generation and iterative editing through a persistent Executable Scene State. FolioWeaver constructs a LayerGraph and ge...
  </details>

- **2026-11-23** — Ziyao Zeng, Xiatao Sun, Hao Wang et al. — [Ego2Wrist: Bootstrapping Wrist-View Synthesis from Egocentric Video](http://arxiv.org/abs/2611.29850v1)
  <details><summary>📄 Abstract</summary>
  Wrist cameras provide an action-centric view that is directly relevant to robot manipulation. However, collecting human wrist-camera videos at scale is challenging due to cumbersome setups that can interfere with natural hand movements. In contrast, head-mounted human egocentric videos are much easier to scale. We introduce Ego2Wrist, which synthesizes synchronized wrist-camera views from human egocentric videos and task descriptions. Trained on approximately 940 hours of paired head- and wrist-...
  </details>

- **2026-11-23** — Burak Demirel, Yu Wang, Pablo Soldati — [Agentic AI for Intent Management and Control in Autonomous Communication Networks](http://arxiv.org/abs/2611.31223v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI)-driven automation will help future mobile networks translate high-level network intents into concrete network optimization or control actions. However, existing approaches often focus on intent management and orchestration, leaving the adaptation of underlying network optimization and control functions largely unaddressed. This article proposes a triadic agentic AI framework that co-designs intent management and intent fulfillment through three agents: an interpreter...
  </details>

- **2026-11-23** — Sungchul Kim, Weixiao Huang, Mekala Raja Sekhar Reddy et al. — [Needwise: Generation-Free Conversational Recommendation from Need-Level Typed Decisions](http://arxiv.org/abs/2611.31175v1)
  <details><summary>📄 Abstract</summary>
  Conversational recommenders must rank items against needs that catalogs record only in part, while users add, withdraw and reverse needs and switch between requests. LLM rankers re-read the dialogue at every turn: they are slow, and their ordering does not show which needs an item meets. We show that a conversational recommender can be built from typed decisions instead: named questions over fixed options, answered with option probabilities rather than generated text. On each turn, one typed req...
  </details>

- **2026-11-23** — Nan Chen, Soledad Villar, Soufiane Hayou — [Precision-Aware Learning Rate Transfer Across Block Count in LLM Post-Training](http://arxiv.org/abs/2611.31166v1)
  <details><summary>📄 Abstract</summary>
  The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very sensitive to the learning rate, and tuning it through grid search is costly in both computation and memory. In this work, we propose \textbf{TipSweep}, a method to transfer the learning rate across the number of trainable transformer blocks. To do so efficiently, we search for the best learning rate b...
  </details>

- **2026-11-23** — Giacomo Bartolucci, Jonathan Bauermann — [Self-similar Inequality Dynamics in Biased Competition for a Conserved Resource](http://arxiv.org/abs/2611.31103v1)
  <details><summary>📄 Abstract</summary>
  In many complex systems the redistribution of a conserved resource can generate strong inequality. Important examples are cities exchanging inhabitants, farms competing for farmland, or agents for wealth in saturated markets. Here we model such systems as agents competing for a fixed total resource, and show that coupling agent extinction to a bias favoring richer agents dynamically amplifies this inequality over time. Drawing on an analogy with emulsions, where droplets compete for a conserved ...
  </details>

- **2026-11-23** — Qiyue Chen, Taian Yu, Junpei Komiyama et al. — [AlphaDefect: Expert-Level AI for Slay the Spire 2](http://arxiv.org/abs/2611.31076v1)
  <details><summary>📄 Abstract</summary>
  Slay the Spire 2 (STS2) is a single-player deck-building game that requires long-term planning under heavy randomness. We present AlphaDefect, an expert-level AI system for STS2: for each character, one network trained with proximal policy optimization (PPO) makes every decision of a run, in combat and outside it. At the highest difficulty, Ascension 10, on two versions of the game current in November 2026 and on test seeds not played in training, AlphaDefect wins 62-77% of runs across six chara...
  </details>

- **2026-11-23** — Wenlong Yu, Bingxu Lu, Qilong Wang et al. — [From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems](http://arxiv.org/abs/2611.31063v1)
  <details><summary>📄 Abstract</summary>
  In multi-agent systems (MAS) built on large language models (LLMs), errors can propagate through intermediate messages and compromise final answers. However, outcome-based evaluation obscures how agents amplify, attenuate, or correct these errors. We propose Response-Aware Error Propagation among Agents (REPA), a structural model that connects measured local responses to system-level error propagation. REPA separately estimates input assembly and agent processing across multiple error channels, ...
  </details>

- **2026-11-23** — Adeep Hande, Shaghayegh Agah, Neeraj Sharma et al. — [From Head to Tail: LLM-Augmented Sequential Recommendation and Trade-off Optimization](http://arxiv.org/abs/2611.31052v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems exhibit popularity bias, often under-serving long-tail and cold-start items with sparse interaction data. We propose a group-specific data augmentation approach that leverages LLMs to generate synthetic interactions, formulated as a constrained optimization problem, maximizing group-specific NDCG@20 and coverage while bounding overall NDCG@20 degradation within an acceptable threshold. Items are partitioned by interaction frequency to find the optimal augmentation strategy fo...
  </details>

- **2026-11-23** — Rafiazka Hilman, Júlia Koltai — [Origins of City Reputation: Measuring Trust and Bias in Online Reviews Using Agentic AI and NLP](http://arxiv.org/abs/2611.31009v1)
  <details><summary>📄 Abstract</summary>
  Online reviews aggregate millions of individual judgments into signals that shape where people eat, stay and travel to, and increasingly read them as evidence of the reputation of places. Nevertheless, whether such reputations really reflect the places or more the instruments used to measure them is unclear. Here we compare two instruments for measuring trust and bias in 100,000 Yelp reviews from ten US cities: a large language model based agentic system including an evaluator critic loop, and a...
  </details>

- **2026-11-23** — Bohe Chen — [Speak When You See It: Proactive Task Assistants Should Wait for Evidence, Not the Clock](http://arxiv.org/abs/2611.30895v1)
  <details><summary>📄 Abstract</summary>
  Proactive assistants that guide people through physical tasks must decide, every few seconds, whether a step is complete and whether a mistake has occurred. We find that two benchmarks for this task largely reward knowing when rather than seeing what: a timer that never looks at the video, raising an alarm at 25 s and confirming each step at 30 s, reaches a mistake F1 of 0.373 on Ego-MC-Bench, above every published result (at most 0.27). We formalize this as the video-blind frontier, the best tr...
  </details>

- **2026-11-23** — Yuxuan Jiang, Anna Mitsopoulou, Apostolos Koukouvinis et al. — [Semantic-aware Decoding for Diverse Text-to-SQL under Schema Ambiguity](http://arxiv.org/abs/2611.30873v1)
  <details><summary>📄 Abstract</summary>
  Real-world text-to-SQL systems often face schema ambiguity, where a question can map to multiple plausible schema elements. To support downstream disambiguation, SQL generation systems should include diverse interpretations among their top-k predictions. However, large language models (LLMs) typically favor a single interpretation, producing highly skewed outputs. We propose Semantic-aware Logit Adjustment (SLA), a training-free decoding method that promotes diverse SQL generation by adjusting t...
  </details>

- **2026-11-23** — Vijayasri Iyer, Cristiano De Nobili, Mubashir Hussain Shah et al. — [Trallie: from Free-Form Text to Structured Data with LLMs](http://arxiv.org/abs/2611.30773v1)
  <details><summary>📄 Abstract</summary>
  Trallie is an open-source framework that leverages large language models (LLMs) to perform information extraction (IE) from natural language sources with or without user guidance. Unlike conventional approaches that rely on extensive labeled datasets or domain-specific training, Trallie enables the conversion of unstructured data into structured formats with minimal or no representative examples. The framework is designed with three key objectives: (i) reducing manual annotation by harnessing pr...
  </details>

- **2026-11-23** — Yulliwas Ameur, Samia Bouzefrane, Soumya Banerjee — [Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing](http://arxiv.org/abs/2611.30742v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are often ranked by an LLM judge whose error rates are measured once and reused for every agent. The corrected success rates can then be biased when the judge's errors depend on the trajectory and agents differ in the trajectories they produce for successes or failures. We derive the exact asymptotic bias and give a chain of checks from identification to simultaneous ranks. On a four-agent semi-synthetic benchmark, a scalar correction with oracle calibration has...
  </details>

- **2026-11-23** — Yidong Luo, Weihuang Wen, Xuanhao Pan et al. — [Beyond the Black Box: A Diagnosis-Driven Agent for Interpretable MIP Solver Tuning](http://arxiv.org/abs/2611.30670v1)
  <details><summary>📄 Abstract</summary>
  Tuning a mixed-integer programming (MIP) solver is an instance-specific problem, where a poor configuration can increase solving time by orders of magnitude.   Existing Bayesian optimization tuners treat solver tuning as a black-box optimization problem: each evaluation returns a single score, allowing the tuner to learn which configuration is faster, but not why.   Inspired by the use of profilers in GPU-kernel optimization, we introduce APEC (Agent for Per-instance Explainable Configuration), ...
  </details>

- **2026-11-23** — Marius Smytzek, Martin Eberlein, Lars Grunske et al. — [Improving Repair Agents with Cause-Chain Diagnoses](http://arxiv.org/abs/2611.30574v1)
  <details><summary>📄 Abstract</summary>
  Repair agents resolve a growing share of real-world issues. Starting with the same information as a developer reading a bug report, they have to find out how the program fails before actually fixing it.   We present FORECAST, which provides repair agents with a diagnosis of the failure. From the executions of passing and failing tests, FORECAST infers a cause chain, a short sequence of execution features, such as conditions or data flow, that explains how the failing runs diverge. FORECAST appen...
  </details>

- **2026-11-23** — Nodirjon Khabibullaev, Rajat Dandekar — [Policy Invariance Is Not Learning Invariance: Potential-Based Reward Shaping for Navigation with a Limited View](http://arxiv.org/abs/2611.30492v1)
  <details><summary>📄 Abstract</summary>
  Potential-based reward shaping (PBRS) does not change the optimal policy, but how much it speeds up learning depends on the potential and on effects outside this guarantee. We analyse how PBRS changes the one-step reward while it preserves the discounted return: a per-step $(γ-1)Φ$ term, the terminal-state rule, a constant shift of the potential, and positive cycles in a bonus that is not potential-based. We then measure these consequences in pre-registered experiments with a PPO agent. The agen...
  </details>

- **2026-11-23** — Matheus Rakes, Maíra Chagas Morais, Gabriel Rodrigues Palma et al. — [Pesticide mixtures may compromise ecosystem services provided by an egg parasitoid of soybean pest stink bugs: a comprehensive ecotoxicological risk assessment](http://arxiv.org/abs/2611.30465v1)
  <details><summary>📄 Abstract</summary>
  Tank mixtures of crop protection products are widely used in agricultural systems, yet their integrated effects on biological control agents remain poorly understood. We evaluated the lethal, sublethal, and transgenerational effects of four synthetic insecticides, applied alone or in binary mixtures with three fungicides and two herbicides, on adults and pupae of Telenomus podisi (Hymenoptera: Scelionidae), an important egg parasitoid of pest stink bugs. In adult bioassays, LC50 values ranged fr...
  </details>

- **2026-11-23** — Jens Leysen, Noah Daniëls, Marco Favier et al. — [Disclosure Bias in AI Reviewers](http://arxiv.org/abs/2611.30410v1)
  <details><summary>📄 Abstract</summary>
  AI models increasingly help to review papers, and many conferences and journals now require authors to state how they used AI. Does this AI-use statement change how an AI reviewer rates a paper, and could it change which papers are accepted? In a preliminary study, we varied only the AI-use statement of 150 ICLR 2027 submissions, in up to nine versions adapted from real statements: from no AI, through writing help and coding, to an AI research agent and an AI author. Six AI reviewers rated the v...
  </details>

- **2026-11-23** — Juntong Shi, Stefano Ermon, Jure Leskovec et al. — [Verifiable On-Policy Distillation](http://arxiv.org/abs/2611.30325v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) has become a powerful approach for improving language-model reasoning, but its supervision is inherently sparse: a sequence-level verifier reward is propagated only through sampled trajectories and provides no direct signal for alternative actions. On-policy distillation (OPD) offers a complementary form of supervision by providing dense teacher feedback over the full next-token distribution, but this signal is not grounded in verified task o...
  </details>

- **2026-11-23** — Miaoyu Li, Boyang Li — [Uncovering Separable and Composable Skill Mechanisms in Vision-Language Models](http://arxiv.org/abs/2611.30290v1)
  <details><summary>📄 Abstract</summary>
  Recent work has sought to localize the internal mechanisms underlying visual reasoning skills in vision-language models. These methods largely overlook separability and composability in both mechanism identification and evaluation. We propose separability and composability as two important desiderata for skill localization. Separability requires identified mechanisms to contribute primarily to their target skills while having limited effects on other skills, enabling precise diagnosis and target...
  </details>

- **2026-11-23** — Zelong Wang, Weiyue Li, Fei Xue et al. — [Same Executions, Different Gaps: Judgment Rules in Web-Agent Evaluation](http://arxiv.org/abs/2611.30190v1)
  <details><summary>📄 Abstract</summary>
  Success-rate gains guide the development of web agents. Yet knowing which agent ranks first does not tell us how much confidence to place in its reported advantage. We study the comparison itself: how success is defined, what evidence supports the judgments, and how the difference between agents is estimated. On fixed web-agent executions, changing a judge from predicting likely completion to requiring recorded support can remove most of a reported lead without changing the ranking. This effect ...
  </details>

- **2026-11-23** — Yehui Yang, Jing Fan, Jun Hu et al. — [ReVAgent: Multi-Agent Reasoning-Intensive Video Generation](http://arxiv.org/abs/2611.30163v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in generating instructional videos for reasoning-intensive topics is to show how and why the state changes at each step. Even when an animation renders successfully, the depicted object relationships and state transitions can conflict with the explanation, making the reasoning difficult to follow. We present ReVAgent, a multi-agent framework that solves a problem, generates keyframes for its explanation, and synthesizes an instructional video. The agents share the execution r...
  </details>

- **2026-11-23** — Keuntae Kim, Beomseok Lee, Hyunwoo Kim et al. — [Revisiting Continual Learning in Language Models: A Three-Interface Diagnosis of Stability and Plasticity](http://arxiv.org/abs/2611.30151v1)
  <details><summary>📄 Abstract</summary>
  Continual learning in language models is commonly studied in the incremental learning (IL) setting, where a model learns a sequence of tasks and is evaluated through its final classifier or language-model (LM) head. This interface, however, does not indicate where forgetting occurs: a drop in accuracy may reflect representation degradation in the backbone, readout mismatch in the head, or both. We therefore argue that backward transfer (BWT) and forward transfer (FWT) should be interpreted as in...
  </details>

- **2026-11-23** — Ziqing Ge — [When Does Optical Context Compression Pay Off? A Decode-Aware Cost Analysis of Reasoning VLMs](http://arxiv.org/abs/2611.30130v1)
  <details><summary>📄 Abstract</summary>
  Rendering long text as images lets a vision-language model (VLM) read a document with fewer input tokens, and evaluations often count mainly these prefill tokens. We show that for reasoning models this accounting is incomplete. Across five models and two long-context benchmarks, reading the rendered document makes the model think longer: decode length grows by 1.5-3.5x on the four general-purpose VLMs tested, and under typical output pricing this decode tax makes image input more expensive than ...
  </details>

- **2026-11-23** — Jonghyun Lee, Soojung Kang — [Weight Averaging at Small Budgets Confounds Formula-Labeled Pretraining in Microstructure-Property Regression: A Pre-Specified Study with Post Hoc Rechecks](http://arxiv.org/abs/2611.29876v1)
  <details><summary>📄 Abstract</summary>
  Closed-form physics formulas can label synthetic microstructures at no cost, so supervised pretraining on those labels is an alternative to self-supervised pretraining when labels are scarce. One pre-specified protocol tests this on two public simulated benchmarks, two-phase conductivity and short-fiber stiffness: a ConvNeXt-Small is pretrained on 150,000 synthetic images by formula regression or masked reconstruction and fine-tuned on 100, 400, or 1,600 labels. Five fine-tuning seeds from one f...
  </details>

- **2026-11-23** — Luizza Dalla Pria, Amelia l. Nelson, Renata Ivanek — [Semantic repeatability and reproducibility of GPT-5 and Gemini 3 Flash on H5N1 One Health questions](http://arxiv.org/abs/2611.29859v1)
  <details><summary>📄 Abstract</summary>
  Highly pathogenic avian influenza A(H5N1) has re-emerged as a One Health concern since 2024, and the public is increasingly consulting large-language-model (LLM) chatbots for health information during outbreaks. Before a chatbot's accuracy can be meaningfully assessed, its consistency must first be understood, so that any single response can be trusted as a fair representative of the model's behavior. We characterized the semantic repeatability and reproducibility of GPT-5 (OpenAI) and Gemini 3 ...
  </details>

- **2026-11-22** — Zifan Zeng, Qunli Zhang, Peng Wang et al. — [Generating Safety-Critical Driving Scenarios from Role-Typed Signal Temporal Logic Specifications Drafted by Large Language Models](http://arxiv.org/abs/2611.29800v1)
  <details><summary>📄 Abstract</summary>
  Safety-critical scenarios are rare in recorded driving and must be generated to test and train motion planners of automated vehicles. In guided diffusion models, each scenario type needs its own weighted objective, separate from the validity check. Optimized together with the attacker, the vehicle under test can cancel the attack or draw it toward itself. We state each scenario as a signal temporal logic specification with clauses typed by role. Every clause names the agent it may change and the...
  </details>

- **2026-11-22** — Swakshar Deb, Tonmoy Hossain, Tom Fletcher et al. — [UniDR: Learning To Generate Anatomical Deformations From Images via Unified Diffusion Modeling and Registration](http://arxiv.org/abs/2611.29712v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a novel framework, Unified Diffusion modeling and Registration (UniDR), which learns to generate arbitrary anatomical deformations from images with preserved topology. Existing approaches often model the generative process separately from registration-based deformation estimation; hence making them prone to propagated errors from the registration stage. To address this limitation, we propose a unified paradigm based on a conditional diffusion model over deformation fields tha...
  </details>

- **2026-11-22** — Xiangzhao Hao, Dianyi Wang, Keyan Zhou et al. — [PROPS: Can Visual Generators Keep the Current Look of a Prop?](http://arxiv.org/abs/2611.29665v1)
  <details><summary>📄 Abstract</summary>
  Many generation tasks draw the next image from a visual history, such as storyboards, illustrated stories and multi-turn editing. A new request often states what happens next without restating how earlier objects look. Instead of recovering an object's current look from the history, generators often redraw it from the request alone or bring back an outdated look, and the error can carry into later steps. We call this failure prop drift. Existing evaluations rarely isolate it, because similarity ...
  </details>

- **2026-11-22** — Panagiotis Kasnesis, Lazaros Toumanidis, Amalia Contiero Syropoulou et al. — [Wactorz: Self-Writing LLM Agents That Discover, Repair, and Migrate at the Edge](http://arxiv.org/abs/2611.29619v1)
  <details><summary>📄 Abstract</summary>
  Most LLM agent frameworks build a crew that runs a task and exits. Physical environments (e.g., homes, labs, factory floors) need agents that stay up for months, survive their own bugs, and run on whatever hardware is already next to the sensors. We present Wactorz, an open-source runtime in which LLM-generated agents are long-lived, supervised actors: a planner turns a chat request into Python, compiles it into a new actor at runtime, and a supervisor restarts that actor alone, with its state i...
  </details>

- **2026-11-22** — Junpeng Hou, Jiaxing Qu, Derek Cheng et al. — [Weight Coding: Evolving Web-Scale Recommenders through Direct Weight Edits with LLM Agents](http://arxiv.org/abs/2611.29613v1)
  <details><summary>📄 Abstract</summary>
  Web-scale recommender models evolve primarily through retraining or fine-tuning. We propose \emph{weight coding}, a methodology for model evolution through direct, executable weight edits. A large language model (LLM) agent inspects model structure and parameters, formulates hypotheses, and implements edits using evaluation feedback. The loop progresses from localized changes to targeted searches and composition, allowing edited components to adapt to one another. A cached engine enables rapid f...
  </details>

- **2026-11-22** — Khurram Khalil, Khaza Anuarul Hoque — [Scalar Tuned Lens Summaries Offer Limited Incremental Value for Mid-Generation Abstention](http://arxiv.org/abs/2611.29589v1)
  <details><summary>📄 Abstract</summary>
  Mid-generation abstention aims to stop an unpromising response before spending its remaining computation budget. Intermediate transformer states may help predict eventual correctness, but whether scalar summaries of their vocabulary predictions add useful evidence is less clear. We compare Tuned Lens entropy and divergence features with final-state and raw intermediate-state probes under matched, causal evaluation. Across eight instruction-tuned models on MATH-500, raw intermediate states improv...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 732 |
| prompt-injection | 709 |
| memory-poisoning | 59 |
| tool-use-attack | 180 |
| backdoor | 571 |
| adversarial-attack | 681 |
| privacy-leakage | 4684 |
| steganography | 94 |
| misuse | 1359 |
| red-teaming | 159 |
| vulnerability | 4168 |
| defense | 4116 |
| alignment | 3854 |
| robustness | 4219 |
| watermark | 811 |
| unlearning | 126 |
| agent-safety | 67 |
| benchmark | 77 |
| survey | 472 |
| other | 11644 |

---

📚 **全部 38782 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-26 01:28:06*