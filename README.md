<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-21343-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-25 02:41 ｜ **论文总数 / Total Papers**: 21343（近 30 天 / Recent 30 days: 2940）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 21343 篇论文（含摘要、分类筛选、搜索）/ View all 21343 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 549
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 462
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 37
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 91
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 388
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 531
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3716
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 52
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 822
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 109
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2483
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2107
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1948
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1850
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 190
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 82
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 48
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 54
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 247
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5577

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2940 篇，完整 21343 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2940 papers from the last 30 days (with date, authors & abstract). For the full list of 21343 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-07-20** — Zhida He, Xia Hu, Baichen Le et al. — [An Early Warning of Emerging Biosecurity Risks in Frontier LLMs](http://arxiv.org/abs/2607.18056v1)
  <details><summary>📄 Abstract</summary>
  Frontier large language models (LLMs) are increasingly integrated into scientific workflows, yet their growing biological capabilities may outpace current safeguards. To assess the biological risks of frontier models, we develop Intern-BioBreaker, a specialized bio-red-teaming model, together with an integrated computational-to-physical framework that couples model-level stress testing with wet-lab validation. Within this framework, Intern-BioBreaker generates targeted jailbreak prompts to test ...
  </details>

- **2026-07-20** — Yuyang Xue, Feng Chen, Zhihua Liu et al. — [Stress Testing Concept Erasure with Large Language Model Agents](http://arxiv.org/abs/2607.17890v1)
  <details><summary>📄 Abstract</summary>
  Concept erasure aims to remove semantic concepts from a trained generative model and is increasingly important for responsible AI deployment. However, verifying whether a model has robustly removed targeted concepts remains a critical challenge. Existing evaluation methods are typically pre-defined and static, failing to expose vulnerabilities under diverse natural-language probes and challenging conditions. Moreover, manually designed evaluation strategies can be biased and difficult to scale. ...
  </details>

- **2026-07-19** — Yukai Zhou, Feiyang Lu, Xiaokai Mao et al. — [How Jailbreak Attacks Inform Safety Alignment: A Defender-Centric, Shapley-Based Evaluation of Jailbreak Contributions](http://arxiv.org/abs/2607.17152v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak attacks on large language models are usually evaluated by attacker-centric metrics such as attack success rate (ASR), yet an attack that breaks a model is not necessarily useful for improving its safety. We propose a defender-centric view of jailbreak evaluation, where attacks are evaluated by the downstream safety improvements they enable when used as red-teaming data for safety training. Building on this view, we introduce A-MESS (Minimal Effective Attack-Subset Selection), a setting...
  </details>

- **2026-07-17** — Yu Cui, Ruiqing Yue, Tingyu Li et al. — [Refusal is Not Safety! Benchmarking Latent Safety Risks of LLM-Driven Content Humorization](http://arxiv.org/abs/2607.15977v1)
  <details><summary>📄 Abstract</summary>
  Safety defenses for large language models (LLMs) have been extensively studied, with existing approaches focusing on attack detection and refusal mechanisms. Such fixed-form direct refusal strategies may introduce the risk of prefix injection attacks. Recent work has explored a new direction that leverages humor as an indirect refusal mechanism to mitigate over-refusal in jailbreak scenarios and reduce prefix injection risks. However, this approach implicitly assumes that humorous responses are ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

- **2026-07-20** — Devina Jain, David Hartmann, Chuan Li — [Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security](http://arxiv.org/abs/2607.18063v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents process external content, exposing them to prompt injection and multi-turn manipulation. Most safety benchmarks evaluate defenders against fixed attack pools collected before evaluation, single-turn or multi-turn. We present a 21-scenario benchmark for \emph{adaptive multi-round attacks against memoryless LLM defenders}: an autonomous LLM attacker observes prior defender responses and pivots across rounds, while each defender response is evaluated as a fresh interaction. Holding...
  </details>

- **2026-07-20** — Xingfu Zhou, Pengfei Wang, Yuan Zhou et al. — [Salience Induction against Multi-Hop RAG Agents: Threat and Defense](http://arxiv.org/abs/2607.17535v1)
  <details><summary>📄 Abstract</summary>
  Agentic retrieval-augmented generation (RAG) systems increasingly retrieve external evidence and orchestrate tools for knowledge-intensive applications. In Multi-Hop question answering, agents chain facts across documents. Existing defenses focus on content poisoning, which injects false facts, and prompt injection, which embeds directives. We identify a third attack surface: the salience channel, through which fact position, emphasis, framing, and semantic proximity can redirect reasoning even ...
  </details>

- **2026-07-19** — Haoyan Luo, Mateo Espinosa Zarlenga, Mateja Jamnik — [Persistent Sparse Autoencoders: Learning Feature Timescales in Language Models](http://arxiv.org/abs/2607.17117v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) decompose language model activations into sparse features, but standard SAEs encode each token independently and do not expose information that persists across a sequence. We introduce Persistent Sparse Autoencoders (Persistent SAEs), which extend standard SAEs by learning a persistence coefficient for each feature, allowing the model to learn which features should persist and for how long. Our experiments show that they retain competitive reconstruction quality while ...
  </details>

- **2026-07-17** — Jiasi Weng, Jian Weng, Minrong Chen et al. — [From Neural Intent to Cryptographic Authorization: Governing Agentic Workflows](http://arxiv.org/abs/2607.15596v1)
  <details><summary>📄 Abstract</summary>
  The rapid adoption of artificial intelligence (AI)-driven and agentic workflows is transforming traditional government and enterprise systems into language-based, tool-using and increasingly autonomous infrastructures. Conventional key management services authenticate who may invoke a cryptographic primitive, but remain agnostic to which workflow steps are authorized at runtime: an authenticated agent can still be hijacked by direct or indirect prompt injection into executing malicious actions t...
  </details>

- **2026-07-15** — Mohammad Allahbakhsh, Mohammad Hassan Bahari, Moslem Attar-Raouf — [Rethinking Penetration Testing for AI-Enabled Systems: From Resource Compromise to Behavioral Objective Violation](http://arxiv.org/abs/2607.14006v1)
  <details><summary>📄 Abstract</summary>
  Penetration testing traditionally evaluates whether adversaries can exploit weaknesses in software, infrastructure, configurations, or operational controls to achieve security-relevant compromise. This paradigm remains necessary for AI-enabled systems, but it is no longer sufficient. In such systems, adversaries may influence prompts, retrieved content, sensor inputs, training data, memory, tools, or human-AI interaction loops to alter system behavior without directly compromising the underlying...
  </details>

- **2026-07-15** — Sanket Badhe, Priyanka Tiwari — [Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation](http://arxiv.org/abs/2607.13987v1)
  <details><summary>📄 Abstract</summary>
  Reusable skills are becoming a fundamental building block of Large Language Model (LLM) agents, enabling capabilities to be packaged, shared, and reused across diverse applications. However, existing security research primarily focuses on prompt injection and runtime execution, leaving security risks throughout the broader skill lifecycle largely unexplored. In this paper, we present SkillSec-Eval, a lifecycle-aware framework for systematically evaluating the security of reusable agent skills. W...
  </details>

- **2026-07-15** — Alexandra E. Michael, Franziska Roesner — [How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement](http://arxiv.org/abs/2607.13718v1)
  <details><summary>📄 Abstract</summary>
  As AI agents gain prevalance, users are increasingly exposed to the risks such systems entail. Prompt injection attacks, as well as hallucination, can cause agents to leak private information to third parties. As autonomous systems, agents also present the more active danger of performing sensitive tasks, such as bank transactions, without the user's intent or authorization.   Recognizing this challenge, the agentic security community has developed numerous proposals for secure agentic systems. ...
  </details>

- **2026-07-14** — Junhui Wang, Hangtao Zhang, Zhirun Zheng et al. — [PVDetector: Detecting Prompt Injection Attacks on Purpose-Specific LLM Agents through Policy-Violation Concept Analysis](http://arxiv.org/abs/2607.12624v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as purpose-specific agents to handle domain-specific tasks such as customer service and code generation. These agents are expected to comply with not only generic safety guardrails but also purpose-specific restrictions tailored to their designated roles. Such additional restrictions enlarge the attack surface, particularly to prompt injection (PI) attacks. To defend against such attacks, existing detection methods primarily rely on analyzin...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-07-17** — Halima Bouzidi, Mboutidem Ekemini Mkpong, Mohammad Abdullah Al Faruque — [Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents](http://arxiv.org/abs/2607.15657v1)
  <details><summary>📄 Abstract</summary>
  Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes. We show that unconditional trust in visual data creates a critical vulnerability. We propose Lucid, a black-box adversarial framework that compromises multimodal memory pipelines under a strictly image-bounded threat model, requiring no access to the target MLLM, target retrieval encoder, or the text channel. Lucid crafts imperceptible perturbations to enable two distin...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 2 papers

- **2026-07-20** — Habibur Rahaman, Qipan Xu, Zafaryab Haider et al. — [(A)iSpy: Parasitic Trojans for Machine Learning Infrastructure](http://arxiv.org/abs/2607.17550v1)
  <details><summary>📄 Abstract</summary>
  Modern machine learning (ML) pipelines depend heavily on third party libraries for graph compilation and hardware acceleration. While current practices audit data and model artifacts or rely on file integrity checks, the execution environment remains implicitly trusted. This blind spot enables active threats where a malicious runtime module interacts directly with live training and inference dynamics: exploiting this interaction allows the Trojan to support complex objectives that are challengin...
  </details>

- **2026-07-17** — Xukun Luan, Yuhui Gong, Gang Zhang et al. — [Code-Poisoning Property Inference Attacks](http://arxiv.org/abs/2607.15970v1)
  <details><summary>📄 Abstract</summary>
  The flourishing code hosting platforms and coding agents enable even beginners with private data to build tailored Machine Learning (ML) models using available code quickly. The training data for ML models, often regarded as private property (e.g., clinical records, transaction information), is at significant risk of information leakage. Property Inference Attacks (PIAs), as a significant type of privacy attack, aim to expose global property information of the training set. In this paper, we pre...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 1 papers

- **2026-07-15** — Michal Štefánik, Philipp Mondorf, Andreas Waldis et al. — [AIMO Interpretability Challenge](http://arxiv.org/abs/2607.13899v1)
  <details><summary>📄 Abstract</summary>
  We propose the AIMO Interpretability Challenge, a competition on distinguishing robust from spurious reasoning in frontier mathematical language models based on the models' internal mechanisms. The challenge is motivated by a central limitation of standard reasoning benchmarks: strong final-answer accuracy does not reveal whether a model relies on stable reasoning mechanisms or exploits brittle reasoning shortcuts. Building on AI Mathematical Olympiad (AIMO) problems and submissions, together wi...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 30 papers

- **2026-07-20** — Yikun Hu, Zichen Zhao, Peixiang Qin et al. — [Protecting Floating-Point Computation for DNN Binaries with MBA Obfuscation](http://arxiv.org/abs/2607.17603v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks (DNNs) have become a foundational component of modern computing systems with a wide range of applications, such as computer vision, edge intelligence, etc. For the sake of low latency and data privacy, DNN models are increasingly compiled into executables and deployed on local devices. However, that exposes the models to model theft, enabling adversaries to recover proprietary assets via reverse engineering techniques. While code obfuscation naturally emerges for protecting ...
  </details>

- **2026-07-20** — Kwunhang Wong, Jichang Yang, Karl M. H. Lai et al. — [RRAM-DP: Device-Calibrated Differential Privacy for In-Memory Edge Learning](http://arxiv.org/abs/2607.18169v1)
  <details><summary>📄 Abstract</summary>
  Edge Artificial Intelligence of Things (AIoT) systems often collect sensitive data in situ, raising serious privacy concerns. Resistive-switching random-access memory (RRAM) is an attractive substrate for efficient AIoT thanks to its multi-bit storage and compute-in-memory (CiM) capabilities, while its inherently stochastic write behavior provides a natural source of randomness that can be leveraged for differential privacy (DP) protection. Yet how to transform this device-level randomness-typic...
  </details>

- **2026-07-20** — Eu Jin Lim, Zhaoxing Li, Sebastian Stein — [AdaHome: An Adaptive Smart Home Assistant using Local Small Language Models](http://arxiv.org/abs/2607.18034v1)
  <details><summary>📄 Abstract</summary>
  Smart home assistants interpret a wide range of user commands, from explicit device control to underspecified and preference dependent requests. While recent systems based on Large Language Models (LLMs) improve this capability, they often rely on heavyweight reasoning pipelines and cloud-based deployment, limiting their efficiency and suitability for resource-constrained environments, and raising privacy concerns. In addition, existing approaches provide limited support for stable long-term per...
  </details>

- **2026-07-20** — Blake G. Fitch, Cato Elia Kurtz — [Natural Language Access to Domain-Specific Metadata: A Reusable Framework for LLM Query Generation](http://arxiv.org/abs/2607.18029v1)
  <details><summary>📄 Abstract</summary>
  Researchers need to answer ad-hoc questions about the contents of domain-specific archives but often lack the expertise to write structured queries on the metadata. We show that when domain vocabulary and semantics are captured in a well-designed Web Ontology Language (OWL) ontology, Large Language Models (LLMs) can generate accurate structured queries zero-shot, without fine-tuning, retrieval augmentation, or multi-agent orchestration. We present the Natural Language Knowledge Graph Query (NLKG...
  </details>

- **2026-07-19** — Amal Alshehri, Cihan Tunc — [Federated Learning and LLM-Driven Threat Intelligence for Zero Trust IoT Architecture](http://arxiv.org/abs/2607.17035v1)
  <details><summary>📄 Abstract</summary>
  While the Internet of Things (IoT) has become essential, they introduced serious security and privacy challenges, especially for mission-critical environments. Legacy devices are vulnerable to viruses, data breaches, and unauthorized access, and updating these devices would be infeasibly costly. As a solution, this paper presents a Federated Learning and LLM-Driven Threat Intelligence for Zero Trust IoT Architecture, with FL for anomaly detection integrating privacy-preserving distributed learni...
  </details>

- **2026-07-19** — Jiacheng Ding, Xiaofei Zhang — [SAGA: Synthetic Agentic Graph Architecture for Temporal Benchmark Generation](http://arxiv.org/abs/2607.17288v1)
  <details><summary>📄 Abstract</summary>
  High quality temporal graph benchmarks with rich semantics and ground-truth anomaly labels are essential for training graph neural networks, yet remain scarce due to privacy constraints and annotation costs. We present SAGA (Synthetic Agentic Graph Architecture), a system for generating large-scale, semantically rich temporal graphs via a four-phase pipeline. Our Skeleton-First, Semantics-Second architecture decouples structure from semantics: (S) an O(1)-per-edge skeleton generator produces pow...
  </details>

- **2026-07-19** — Reza Farahani, Zoha Azimi, Mario Colosi et al. — [LMEdge: QoS-Aware LLM Inference Orchestration on Edge Clusters](http://arxiv.org/abs/2607.17175v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) services increasingly operate on edge infrastructure, enabling low-latency and privacy-preserving AI services. However, efficiently serving LLM requests across heterogeneous and resource-constrained edge devices require orchestration mechanisms that jointly determine model configuration (family, size, and quantization level) and execution placement while satisfying user- and system-level quality of service (QoS) requirements. This paper introduces LMEdge, a QoS-aware o...
  </details>

- **2026-07-19** — Haocheng Xia, Yongjoo Park — [SlotGuard: Stop Oversharing Private Local Context in LLM Agent Transcri](http://arxiv.org/abs/2607.17147v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can leak privacy (e.g., paths, emails) and credentials (e.g., API keys) as agent observations (e.g., tool outputs, shell logs, and file reads) are appended to provider-bound transcripts. Existing placeholder redaction is brittle: it can miss embedded or cross-turn references, over-redact benign lookalikes, and destroy the structure useful for reasoning. We present SlotGuard, a local transcript boundary that can hide sensitive data while retaining agents' performance. SlotGuard rewrite...
  </details>

- **2026-07-19** — Haiyu Yang, Miel Hostens — [The generator is the tracker: Multi-object tracking by painting persistent identity colours](http://arxiv.org/abs/2607.17120v1)
  <details><summary>📄 Abstract</summary>
  Multi-object tracking (MOT) is conventionally decomposed into detection followed by association, with object identity maintained as external state: track buffers, motion models, and appearance embeddings. We ask whether a video generator can maintain that state in pixels. We fine-tune a 22B text-to-video diffusion model (LTX-2.3) with a lightweight in-context LoRA to translate an RGB clip into an ID-map clip, a video in which every person is painted a flat, distinct color that persists over time...
  </details>

- **2026-07-19** — Ibraheem AlYousef — [quchip: A Differentiable Toolkit for Modeling Quantum Devices](http://arxiv.org/abs/2607.17081v1)
  <details><summary>📄 Abstract</summary>
  Predictive modeling of a superconducting quantum chip requires more than a Hamiltonian: the model must connect device physics, control-line transformations, chosen frames and approximations, dissipation, and measured observables. We present quchip, an open-source Python toolkit that represents these parts explicitly and assembles backend-independent simulations for QuTiP or dynamiqs; with dynamiqs, device and control parameters remain differentiable through the solve. We demonstrate the resultin...
  </details>

- **2026-07-19** — Madhav Aryal, Sudipa Saha, Kaushal Kafle et al. — [A Systematic Evaluation of Traditional Privacy Policy Analysis Tools Against LLMs](http://arxiv.org/abs/2607.17075v1)
  <details><summary>📄 Abstract</summary>
  The advent of LLMs has significantly changed the research on privacy policy and data compliance analysis by enabling tasks that previously required specialized, domain-specific tools. However, it remains unclear to what extent LLMs can truly replicate the diverse functionalities, and the wide range of methodologies and analysis offered by prior work. In this paper, we conduct the first systematic evaluation of whether off-the-shelf LLMs can replace specialized privacy analysis tools. We study si...
  </details>

- **2026-07-18** — Mahzabin Tamanna, Elizabeth Lin, Sparsha Gowda et al. — [How Do You Choose Your AI Component? An Interview Study of Secure AI Integration in Practice](http://arxiv.org/abs/2607.16660v1)
  <details><summary>📄 Abstract</summary>
  The increasing adoption of Large Language Models (LLMs) as AI components in modern software systems introduces distinct security risks to the software supply chain. While many considerations and safety mechanisms are in place for components of the traditional software supply chain, the recent rapid adoption of AI components and platforms has overlooked these hard learned lessons. Selecting and integrating AI models without clear guidance on how these choices affect system security may leave appl...
  </details>

- **2026-07-18** — Navnit Shukla, Kamal Pandey, Omsankar Tiwari — [TurboVec: A Case Study in Cost-Efficient Private Retrieval for Enterprise RAG via Codebook-Oblivious Quantization](http://arxiv.org/abs/2607.16973v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems increasingly power enterprise LLM applications, yet the vector retrieval layer introduces two underexplored challenges: (1) trained codebook quantizers may expose corpus statistics during index construction, creating a leakage channel in multi-tenant deployments, and (2) post-hoc filtering for tenant isolation degrades recall on selective queries. We study TurboVec, an open-source vector index built on TurboQuant - a codebook-oblivious scalar quantize...
  </details>

- **2026-07-18** — Nguyen Viet Tuan Kiet, Bui Dinh Pham, Duong Quoc Chinh et al. — [RELIC: Revealed Principles for Learning Interpretable Composable Skills in Multi-Agent Planning](http://arxiv.org/abs/2607.16745v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent planning becomes substantially harder when agents must improve specialized decision-making skills while keeping their internal implementations private. This regime arises when agents are developed independently, expose different interfaces and capabilities, and must nevertheless coordinate without sharing executable policies. Prior research has largely assumed centralized optimization, shared policy access, or common skill representations, making it poorly suited to privacy-constrain...
  </details>

- **2026-07-18** — Cynthia Xie, Talia Xu — [DARA: Degradation-Aware Low-Rank Residual Adaptation with Original-to-Corrupted Distillation for Corruption-Robust Animal Re-Identification](http://arxiv.org/abs/2607.16644v1)
  <details><summary>📄 Abstract</summary>
  Animal re-identification (Re-ID) relies on fine-grained identity cues that can be disrupted by blur, noise, compression, and other visual degradations. Existing robustness strategies based on degradation-augmented training or pixel-level restoration improve robustness indirectly, but do not explicitly repair shifts in the identity retrieval space. We study corruption-robust animal Re-ID as input-conditioned feature-space repair and introduce DARA, a lightweight retrofit for compact Re-ID models....
  </details>

- **2026-07-17** — Tam Bang, Hussam Abubakr, Emiliano de la Garza Villarreal et al. — [PRISA: Proactive Infrastructure LiDAR Framework for Intersection Safety Assessment](http://arxiv.org/abs/2607.16156v1)
  <details><summary>📄 Abstract</summary>
  Urban intersections are among the most hazardous locations in road networks, posing significant risks to vehicles and vulnerable road users (VRUs) such as pedestrians and cyclists. The complexity of multi-agent interactions demands continuous, real-time monitoring systems capable of anticipating conflicts before they escalate into crashes. We present PRISA, a modular infrastructure LiDAR framework leveraging privacy-preserving, low-light-robust roadside sensors for long-term traffic observation ...
  </details>

- **2026-07-17** — Matteo Cicalese, Antonio Della Porta, Stefano Lambiase et al. — [The Language of Security: How Prompt Syntax Shapes Secure Code Generation in Open LLMs](http://arxiv.org/abs/2607.15937v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used for source code generation despite their outputs often exhibiting security vulnerabilities. Prior work shows that prompt engineering can mitigate such risks, yet (1) they focused on high-level prompting strategies, neglecting recent evidence that fine-grained syntactic variations can substantially alter model behavior; and (2) predominantly evaluate proprietary LLMs, limiting the applicability of their findings in industrial settings where self-...
  </details>

- **2026-07-17** — S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha et al. — [EduGuard: A Safe RAG-Based LLM Tutor for Programming Education](http://arxiv.org/abs/2607.15738v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) is increasingly used by students for programming explanation, debugging, and assignment support. Yet unrestricted large language model (LLM) tutors can hallucinate, contradict course policy, reveal complete solutions, and foster passive dependence. This paper presents EduGuard, a safe retrieval-augmented generation (RAG) tutoring framework for introductory programming. EduGuard integrates query understanding, instructor-approved course retrieval, pedagogical strategy select...
  </details>

- **2026-07-17** — Ming Chen, Pranav Pai — [AgentFAIR: A Multi-Agent Collaborative Framework for FAIRness Evaluation of Geospatial Datasets](http://arxiv.org/abs/2607.15781v1)
  <details><summary>📄 Abstract</summary>
  Geospatial datasets support applications from urban planning to climate modeling, yet consistent assessment of FAIR compliance is difficult. Existing evaluators use different rubrics and evidence sources and may fail on JavaScript-rendered pages or repository-specific identifiers. For 50 datasets from 10 repositories, the standard deviation of normalized scores across available tools averages 15.0 percentage points and reaches 30.3 for one dataset. Because these outputs are not equivalent measur...
  </details>

- **2026-07-17** — Xunkai Li, Guohao Fu, Yuming Ai et al. — [Toward Federated Multimodal Graph Foundation Models: A Topology-Aware Multimodal Alignment Framework](http://arxiv.org/abs/2607.15687v1)
  <details><summary>📄 Abstract</summary>
  Multimodal-attributed graphs (MAGs), whose nodes carry modalities such as images and text alongside topological structure, now pervade applications including social platforms, e-commerce, and biomedical networks, offering richer semantic signals than single-modality graphs. In practice, such graphs are fragmented across privacy-restricted silos owned by different platforms and institutions, so learning a broadly transferable model over them demands collaborative training that never exposes raw d...
  </details>

- **2026-07-17** — Jens Frankenreiter — [DECODEM: Data Extraction from Corporate Organizational Documents via Enhanced Methods](http://arxiv.org/abs/2607.15879v1)
  <details><summary>📄 Abstract</summary>
  Much empirical legal research depends on translating unstructured text into structured variables. In corporate governance research as elsewhere, this translation has traditionally relied on human coding of documents such as charters and bylaws, a process that is costly, difficult to scale, and often opaque. This paper introduces DECODEM, a set of benchmark datasets for evaluating the automated extraction of corporate governance variables from organizational documents. The benchmarks pair randoml...
  </details>

- **2026-07-17** — Seongho Kim, Heelim Choi, Jaemin Kim et al. — [Ciphertext- and Polynomial-Level Optimization for Fully Homomorphic Encryption](http://arxiv.org/abs/2607.15750v1)
  <details><summary>📄 Abstract</summary>
  Fully homomorphic encryption (FHE) schemes such as RNS-CKKS enable privacy-preserving services by allowing direct computation on encrypted data. While recent FHE compilers optimize FHE programs, they operate at the coarse-grained ciphertext level, where each ciphertext operation comprises a sequence of polynomial operations. At this granularity, the compilers miss optimization opportunities across ciphertext operations. This work presents Recifhe, a new multi-level compiler that supports not onl...
  </details>

- **2026-07-17** — S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha et al. — [CardioMeta: Calibrated Multi-Task Prediction of Diabetes, Hypertension, and Cardiovascular Disease Across Population and EHR Data](http://arxiv.org/abs/2607.15721v1)
  <details><summary>📄 Abstract</summary>
  Cardiometabolic diseases remain among the most persistent drivers of preventable morbidity because diabetes, hypertension, and cardiovascular disease frequently co-occur and share metabolic, vascular, demographic, and behavioral determinants. Existing machine learning studies for chronic disease prediction often emphasize discrimination on a single dataset, while underreporting label leakage, calibration, temporal robustness, external transportability, and subgroup reliability. This paper presen...
  </details>

- **2026-07-17** — Priyanka V. Setty, Arvind Ramanathan, Ian Foster et al. — [AEGIS: Assay-Aware Protocol Validation and Runtime Monitoring for Open-Source Liquid Handling Robots](http://arxiv.org/abs/2607.15620v1)
  <details><summary>📄 Abstract</summary>
  Self-driving laboratories increasingly rely on low-cost liquid handlers such as the Opentrons OT-2, which ship without the pressure-based aspiration monitoring of Hamilton or Tecan systems and are typically run open-loop. Two failure modes go undetected: protocols that are syntactically valid but violate assay-specific invariants (e.g., tip reuse between a PCR template and a no-template control), and physical execution failures (partial dispense, air bubbles, missing tips) at runtime. We present...
  </details>

- **2026-07-17** — Xiaopeng Cheng, Zhichao Zhang, Yangfan He — [Optimal Sampling and Reconstruction of Graph Signals in the Fractional Fourier Domain](http://arxiv.org/abs/2607.15602v1)
  <details><summary>📄 Abstract</summary>
  Graph signal sampling and reconstruction are commonly formulated in the graph Fourier transform (GFT) domain. However, the reconstruction performance may be limited when practical graph signals are not sufficiently concentrated in the GFT spectrum. To address this issue, this paper proposes a graph signal sampling and reconstruction framework based on the graph fractional Fourier transform (GFRFT) domain. The fractional order is introduced as an adjustable spectral domain parameter, and the opti...
  </details>

- **2026-07-15** — Haoran Li, Jiebi Deng, Tong Jin et al. — [A Self-Evolving Agent for Longitudinal Personal Health Management](http://arxiv.org/abs/2607.13940v1)
  <details><summary>📄 Abstract</summary>
  Personal health management unfolds over repeated encounters, yet most health AI systems treat each request in isolation. We developed HealthClaw, an open-source agent architecture that updates support as a person's routines, preferences, measurements and risks change. It separates shared safety rules and medical knowledge from private longitudinal memory containing profile facts, reusable procedures and episodic traces. After each episode, induction determines what should update the profile, rev...
  </details>

- **2026-07-15** — Shengchao Chen, Ting Shu — [FM$^2$: Unified Federated Foundation Models for Heterogeneous Multimodal Medical Imaging](http://arxiv.org/abs/2607.13386v1)
  <details><summary>📄 Abstract</summary>
  Building foundation models for medical imaging requires pooling data across institutions, yet privacy regulations prohibit centralized aggregation. Existing Federated Foundation Models either fine-tune natural-image models with poor medical-domain transfer, or train from scratch within a single modality, lacking the flexibility to unify tasks. We identify an under-explored challenge, Imaging Modality Heterogeneity, where clients operate under two structural regimes: Overlapped (shared modalities...
  </details>

- **2026-07-15** — Ilef Chebil, Asma El Hadj, Souheib Yousfi et al. — [PriEval-Protect: A Unified Framework for Privacy Evaluation and Protection in Healthcare Systems](http://arxiv.org/abs/2607.13754v1)
  <details><summary>📄 Abstract</summary>
  Safeguarding patient privacy while enabling meaningful healthcare data use remains critical under GDPR and HIPAA. Existing compliance methods are manual, error-prone, and separate policy audits from data-level assessments. This paper presents PriEval-Protect, a two-phase framework for unified privacy risk evaluation and mitigation. The evaluation phase combines regulatory compliance scoring using a fine-tuned legal LLM with RAG, and technical analysis via encryption type, data architecture, and ...
  </details>

- **2026-07-15** — Michael O. Eniolade — [Evaluating Frontier AI Agents as Autonomous Clinical Security Auditors](http://arxiv.org/abs/2607.13411v1)
  <details><summary>📄 Abstract</summary>
  Clinical AI models can expose patients to harm when adversarial vulnerabilities go undetected, yet formal security auditing requires statistical expertise, specialized tools, and significant time. We present an open evaluation task, built on METR Task Standard v0.3.0, that tests whether frontier AI agents can autonomously implement a structured clinical AI security audit. Given a pre-trained clinical prediction model, a patient dataset, and written instructions, each agent must implement four at...
  </details>

- **2026-07-14** — Stephan A. Fahrenkrog-Petersen, Aleksander Figiel, Darya Melnyk et al. — [Privacy Attacks on Stable Marriage](http://arxiv.org/abs/2607.13015v1)
  <details><summary>📄 Abstract</summary>
  The stable marriage problem appears in many privacy-sensitive domains, for example in the National Resident Matching Program in the US. In such applications, preserving the privacy of users' preference lists is essential to prevent strategic manipulation, discourage misreporting, and comply with data protection regulations.   In this work, we investigate privacy attacks on stable marriage algorithms. Assuming that the attacker (e.g., the hospitals) can repeatedly interact with the stable marriag...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 9 papers

- **2026-07-20** — Yuge Zhang, Yuanxing Zhang, Yichao Jin et al. — [Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification](http://arxiv.org/abs/2607.17586v1)
  <details><summary>📄 Abstract</summary>
  Money mule accounts are critical facilitators of financial fraud, yet detecting them at scale remains challenging due to the heterogeneous nature of transactional and behavioural data. We present an end-to-end pipeline for customer-level mule detection comprising three stages: (1) a LightGBM classifier trained on 280 engineered features spanning transaction patterns, account demographics, network topology, and temporal behaviour; (2) a TreeSHAP attribution layer that decomposes each prediction i...
  </details>

- **2026-07-19** — Cem Topcuoglu, Seyed Ali Akhavani, Harel Berger et al. — [Measuring and Evaluating the Performance of Generative AI Models for Scam Detection](http://arxiv.org/abs/2607.17353v1)
  <details><summary>📄 Abstract</summary>
  Online scams continue to cause substantial financial and personal harm. As a result, detection systems based on Large Language Models (LLMs) have been integrated into security products ranging from email gateways and browser extensions to fraud-monitoring dashboards. As this adoption accelerates, a common belief has taken hold: that these models are broadly suitable for scam detection. In this work, we investigate whether LLMs, with their strong capabilities in understanding intent, context, and...
  </details>

- **2026-07-19** — Anthonio Oladimeji Gabriel, Dimeji Olawuyi, Toba Ajayi et al. — [Safety That Does Not Transfer: Cross-Lingual Clinical Correctness Drift in Deployable Medical Language Models](http://arxiv.org/abs/2607.17270v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluation of large language models is conducted predominantly in English and predominantly on frontier systems. Neither condition describes how such models are encountered in low-resource health settings, where small quantised systems are run locally and queried in local languages. We ask whether clinical safety established in English transfers to Hausa, and whether any failure is attributable to the language, the clinical task, or the class of model that low-resource deployment admits. ...
  </details>

- **2026-07-19** — Pamela Kirui, Cho Hyuk, Qingzhong Liu et al. — [An Explainable FFT-Based Spatial-Frequency Fusion Framework for Deepfake Detection](http://arxiv.org/abs/2607.17441v1)
  <details><summary>📄 Abstract</summary>
  Deepfake generation has raised growing concerns regarding digital media authenticity, misinformation, identity fraud, and public trust. Recent studies show that combining spatial and frequency features leads to stronger detection results than using independently. This paper presents MSCA-FFT, a Fast Fourier Transform (FFT)-based multi-scale cross-attention framework for image-level deepfake detection. The model combines a partially fine-tuned Xception spatial branch with an FFT-based frequency b...
  </details>

- **2026-07-17** — Andres Karjus, Janika Leoste, Tiia Õun — [Student Evaluation of Repeated AI Feedback Across a Semester of Writing](http://arxiv.org/abs/2607.16115v1)
  <details><summary>📄 Abstract</summary>
  Generative AI is increasingly used for feedback in higher education, but evidence from repeated classroom use remains limited. This short paper analyses 2988 reflective essay-feedback-appraisal instances from 283 Estonian bachelor students across one semester. Students obtained and assessed feedback from a self-selected AI tool using a uniform prompt. The present analysis of the anonymized text corpus covers essay content, AI feedback, and its perceived helpfulness. Students found feedback helpf...
  </details>

- **2026-07-17** — Indraveni Chebolu, Rohan Singh, Arnab Mallick et al. — [Conditional Reliability of Toxicity Signals for Multilingual and Code-Mixed Abuse Detection](http://arxiv.org/abs/2607.15861v1)
  <details><summary>📄 Abstract</summary>
  Moderation systems increasingly rely on external toxicity tools, but those tools are unreliable under code-mixing, transliteration, slang, and language mismatch. We study the \emph{conditional reliability} of toxicity priors in Indian multilingual and code-mixed short text: English toxicity, Indic abuse, and rule-based severity cues can be useful evidence, but only in some linguistic and abuse-severity contexts. We propose ToxGate, a trust-fusion head that conditions each auxiliary signal on the...
  </details>

- **2026-07-17** — Jiazhen Huang, Zhiming Liu, Changhu Wang et al. — [Von Mises-Fisher Mixture Model with Dynamic Shrinkage for Realistic Test-Time Transduction](http://arxiv.org/abs/2607.15851v1)
  <details><summary>📄 Abstract</summary>
  A range of methods aim to enhance the performance of vision-language models (VLMs) at test time. Among them, transduction has emerged as a promising paradigm due to its strong compatibility and efficiency. However, realistic evaluations often involve highly imbalanced class distributions, which cause performance degradation or even collapse. In this work, we systematically revisit transduction from the perspective of penalized likelihood estimation (PLE), showing that PLE with a KL-divergence an...
  </details>

- **2026-07-15** — Tianyu Chen, Chujia Hu, Wenjie Wang — [SAFETY SENTRY: Context-Aware Human Intervention via EXECUTE-ASK-REFUSE Routing](http://arxiv.org/abs/2607.13594v1)
  <details><summary>📄 Abstract</summary>
  LLM agents act on real-world environments through tool calls, and a single misjudged action can cause irreversible harm. The standard safeguard is a guard model that labels each proposed action as safe or unsafe, but this binary view conflates two distinct decisions: whether the action is harmful in itself, and whether it is appropriate given the user's context. It also operates at the granularity of action categories rather than individual instances, producing routine interruptions that erode a...
  </details>

- **2026-07-15** — Qiang Zhu, Jiajun Wu — [LAPO: Leave-One-Turn Attribution for Self-Generated Process Rewards in Multi-Turn Search Reasoning](http://arxiv.org/abs/2607.13501v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for multi-turn search reasoning typically relies on terminal outcome rewards, which cannot distinguish useful, redundant, and harmful intermediate interactions. We propose LAPO, a self-generated process-supervision method based on backward leave-one-turn attribution. For each search turn, LAPO replaces the turn and its retrieval observation with a fixed [DELETE] placeholder and measures the resulting change in the current policy's mean log-likelihood of the gold answer. Th...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-07-17** —  SciForge Team, Zhangyang Gao, Minghao Fang et al. — [SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery](http://arxiv.org/abs/2607.16038v1)
  <details><summary>📄 Abstract</summary>
  Scientific work increasingly spans heterogeneous artifacts -- papers, code, datasets, scientific file formats, model outputs, figures, manuscripts, and team decisions -- yet general-purpose AI assistants rarely preserve these objects as a coherent, auditable research state. We present SciForge, a multimodal research-native AI workbench that reserves the graphical interface for human judgment while search, parsing, model routing, workflow execution, plotting, writing, and presentation generation ...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 59 papers

- **2026-07-20** — Lisha Chen — [Improved Convergence Rate for Stochastic Multi-Gradient Descent: A Proof Discovered with AI](http://arxiv.org/abs/2607.18174v1)
  <details><summary>📄 Abstract</summary>
  For smooth nonconvex stochastic multi-objective problems, stochastic multi-gradient descent (SMG) computes an approximate steepest common descent direction of the objectives from stochastic gradients. With unbiased, variance-bounded stochastic gradients, this note establishes a new convergence rate for SMG in terms of the squared Pareto-stationarity (PS) measure. With a constant stepsize and linearly growing mini-batches, this measure at the algorithm's output is $\widetilde O(T^{-1})$ after $T$...
  </details>

- **2026-07-20** — Hakbeom Jang, Inho Song, Sam H. Noh et al. — [HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory](http://arxiv.org/abs/2607.18141v1)
  <details><summary>📄 Abstract</summary>
  Long-context, multi-turn, and agentic LLM workloads increasingly reuse previously processed context, making KV-cache reuse essential for reducing redundant computation. However, this reuse shifts the bottleneck to the memory tier that stores and serves reusable KV states at cluster scale. GPU HBM and host DRAM are too costly to scale to TB-scale shared context capacity, motivating remote tiers built from lower-cost, higher-capacity media. This paper presents HyMCache, a KV-cache framework that i...
  </details>

- **2026-07-20** — Daekwon Pi, Sangho Lee, Young Hun Lee et al. — [GARAGE: Characterizing the Automation Boundary in LLM-based Attack Graph Generation](http://arxiv.org/abs/2607.18108v1)
  <details><summary>📄 Abstract</summary>
  While modern vehicle security depends on effective Cyber Threat Intelligence (CTI) synthesis, current automated tools struggle with unstructured data and automotive-specific architectural nuances. To bridge this gap, we introduce GARAGE, a RAG-powered framework that converts fragmented CTI into an actionable, domain-specific knowledge base for automated attack graph generation. GARAGE synthesizes a dataset of 12,786 CVEs and 140 incident reports into a STIX 2.1 and Auto-ISAC ATM-compliant knowle...
  </details>

- **2026-07-20** — Nursultan Askarbekuly, Mohamad Al Mdfaa, Ahmed Helaly et al. — [Autoresearch with Coding Agents: Generalizers and Metric-Maximizers on Quran Recitation Data](http://arxiv.org/abs/2607.18064v1)
  <details><summary>📄 Abstract</summary>
  Coding agents can now be left alone to improve software against a score. In this pattern--recently popularized as "autoresearch"--the agent receives a dataset, an evaluation script, and one editable file, and iterates without supervision: modify the code, measure, keep the change if the score improves. But what does the agent actually optimize--the developer's intent, or the literal number? We ran this loop on a real production task: deciding which Quranic verses appear in a noisy speech-recogni...
  </details>

- **2026-07-20** — Yue Xue — [Chiral Analysis of Smart Contracts: Detecting Vulnerabilities from Relational Inconsistencies Across Business Paths](http://arxiv.org/abs/2607.17987v1)
  <details><summary>📄 Abstract</summary>
  Smart-contract vulnerabilities often arise from inconsistencies between business paths that should correspond to one another, such as single and batch entry points, direct and adapter-based flows, quote and execution paths, or inverse operations such as buy and sell. Existing analyzers are effective for many local syntactic and data-flow patterns, but they provide limited support for bugs whose oracle is relational: whether two semantically paired paths preserve compatible guards, state transiti...
  </details>

- **2026-07-20** — Yimeng Chen, Nathanaël Denis, Roberto Di Pietro et al. — [Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?](http://arxiv.org/abs/2607.17986v1)
  <details><summary>📄 Abstract</summary>
  Self-hosted AI agents read and write their own memory and configuration files to function. An agent may get compromised via corruption of its own state -- a compromise realized via legitimate OS system call invocation. We refer to this class of threats as self-state attacks. In this paper, we investigate the OS resilience to this class of attacks. Formally, we characterize a four-axis attack space (Target, Mechanism, Granularity, Temporal); investigate the structural limits of prevention, detect...
  </details>

- **2026-07-20** — Paul Gattinger, Bettina Heise, Andreas W. Schell et al. — [Scanless quantum Fourier-transform mid-infrared spectroscopy for rapid high-sensitivity hyperspectral mapping](http://arxiv.org/abs/2607.17964v1)
  <details><summary>📄 Abstract</summary>
  Fourier-transform infrared (FTIR) spectroscopy is a well-established technique for qualitative and quantitative chemical analysis. Classical FTIR systems rely, however, on direct mid-infrared (mid-IR) scan-based time-domain measurements of coherence functions; thus, the signal-to-noise ratio and measurement speed are constrained by design. In this paper, we demonstrate a scanless quantum FTIR (sQFTIR) technique that exploits principles of metrology with entangled photons to circumvent the limita...
  </details>

- **2026-07-20** — Zhaoyan Hong, Yishen Sun, Xinyi Zhang et al. — [From Blind Search to Memory-Aware Evolution: Efficient DBMS Tuning via Collaborative Diagnosis and Utility-Aware Retrieval](http://arxiv.org/abs/2607.17841v1)
  <details><summary>📄 Abstract</summary>
  Modern DBMSs expose multiple configurable components (e.g., knobs, query hints, and indexes) that jointly determine query performance. Multi-component tuning is challenging due to the large combinatorial search space and the difficulty of learning effective tuning policies under limited feedback. Existing approaches still rely on blind search over the configuration space and interaction-heavy policy learning, leading to high tuning overhead and limited performance gains. Recent advances in large...
  </details>

- **2026-07-20** — Chuanlong Zang, Isabelle Barz, Anna Mannucci et al. — [Lifelong Multi-Subsystem Pickup and Delivery with Buffer-Limited Handover Stations](http://arxiv.org/abs/2607.17724v1)
  <details><summary>📄 Abstract</summary>
  Coordinating payload transfers between subsystems is a critical challenge in lifelong Multi-Agent Pickup and Delivery (MAPD). We study systems where agents are confined to separate regions and must exchange payloads through shared handover stations. These stations, equipped with single docks and finite buffers, are inherently vulnerable to blocking and starvation. We formalize this problem as Multi-Subsystem MAPD with Buffer-limited Handover Stations (MS-MAPD-BHS). We then propose Handover-Aware...
  </details>

- **2026-07-20** — Yuchen Chen, Wei Cheng, Yuan Xiao et al. — [Insecure Coding Preferences in Long-Term Memory: Security Risks for LLM-based Code Generation](http://arxiv.org/abs/2607.17619v1)
  <details><summary>📄 Abstract</summary>
  LLM-based systems increasingly incorporate long-term memory to improve cross-session continuity. However, once insecure coding preferences are stored, they may silently influence security-critical decisions in subsequent generations. In this study, we conduct the first systematic empirical study on the impact of insecure coding preferences stored in long-term memory on the security of LLM-based code generation. We evaluate four LLMs (ChatGPT, Gemini, Qwen, and Grok) across five programming langu...
  </details>

- **2026-07-20** — Kai Jiang, Zisong Lin, Hongyuan Zhang et al. — [Miles: Metric Learning with Expandable Subspace for Pre-Trained Model-Based Class-Incremental Learning](http://arxiv.org/abs/2607.17593v1)
  <details><summary>📄 Abstract</summary>
  Class Incremental Learning (CIL) aims to learn new concepts consistently from a data stream without forgetting. Unlike typical CIL methods which need to learn a model from scratch, pre-trained model (PTM) can easily adapt to a new task with fine-tuning. However, existing PTM-based CIL methods fail to achieve a trade-off between performance and computational expenditure, i.e., they either adopt the same parameter space so that leading catastrophic forgetting, or expand a new branch for each task ...
  </details>

- **2026-07-20** — Ruiyi Ding, Jie Li, He Kang et al. — [AGG: Jacobian-Aggregated Group Gradient for Efficient GRPO Training of Diffusion Models](http://arxiv.org/abs/2607.17572v1)
  <details><summary>📄 Abstract</summary>
  Group Relative Policy Optimization (GRPO) is a powerful reinforcement learning algorithm for aligning generative models with human preferences. While successful in large language models~\cite{shao2024deepseekmathpushinglimitsmathematical}, its extension to diffusion and flow matching models introduces a severe computational bottleneck: gradients must be back-propagated through the high-capacity DiT backbone at \emph{every} timestep of the sampling trajectory, making high-resolution text-to-image...
  </details>

- **2026-07-20** — Songyan Zhang, Jinyuan Tian, Hanbing Li et al. — [GeoWorldAD: Geometry World Action Model for Autonomous Driving](http://arxiv.org/abs/2607.17521v1)
  <details><summary>📄 Abstract</summary>
  Autonomous driving requires both safe and efficient planning decisions in dynamic 3D environments. Although recent Vision/Video-Action models learn policies directly from visual observations and scale well with advances in vision transformers and large-scale training data, they often lack explicit geometric grounding and future-aware spatial guidance, limiting their ability to balance collision avoidance and driving progress. In this work, we propose GeoWorldAD, a geometry world action model tha...
  </details>

- **2026-07-20** — Zhuohang Fan, Beichen Zhang, Yuanfa Li et al. — [SEE: Structure-aware Exploring \& Exploiting for Long-horizon GUI Agent Trajectory Synthesis](http://arxiv.org/abs/2607.18046v1)
  <details><summary>📄 Abstract</summary>
  Graphical User Interface (GUI) agents powered by vision-language models hold promise for automating real-world mobile tasks. However, progress is limited by the lack of high-coverage, long-horizon interaction trajectories collected from element-rich and rapidly evolving apps. Existing pipelines often rely on costly human demonstrations or on-policy framework, which tends to over-sample common flows while missing rare transitions and complex multi-step procedures. To address this problem, we prop...
  </details>

- **2026-07-19** — Alaaddin Goktug Ayar, Martin Margala — [Transition-Aware Backend Dispatch for Edge LLM Inference](http://arxiv.org/abs/2607.17415v1)
  <details><summary>📄 Abstract</summary>
  Efficient large language model (LLM) inference on edge platforms is limited not only by model size, but also by shape-dependent performance differences across execution backends. Static backend assignment cannot exploit this variation, while independent per-operator selection can introduce costly device and framework switches. This paper presents a transition-aware backend dispatch approach for edge transformer inference. The approach combines current operator features with the previously select...
  </details>

- **2026-07-19** — Peiji Yu, Xin Chen, Tianxing Wu — [Debate-on-Graph: Reliable and Adaptive Reasoning of Large Language Model on Uncertain Knowledge Graph](http://arxiv.org/abs/2607.17266v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated remarkable capabilities in natural language processing. However, LLMs often suffer from hallucinations and lack of relevant knowledge when dealing with question answering (QA) tasks. To mitigate these issues, knowledge graphs (KGs) have been utilized to enhance LLM reasoning. Nevertheless, KGs often contain noise and errors, while existing KG-enhanced LLM approaches are generally unable to identify and filter such noisy and erroneous content, which ...
  </details>

- **2026-07-19** — Xiaoyu Yang, Xuenan Xu, Wenyi Yu et al. — [SALMONN-2: Advancing General-Purpose Hearing Abilities with Self-Supervised Representations](http://arxiv.org/abs/2607.17079v1)
  <details><summary>📄 Abstract</summary>
  Recent audio large language models (ALLMs) are typically built upon audio encoders trained with large amounts of supervised data. Since self-supervised learning (SSL) audio encoder models are known to learn general-purpose and transferable representations, we investigate whether general-purpose SSL audio representations can serve as an effective foundation for ALLMs. We present SALMONN-2, an ALLM built upon a unified SSL encoder. To better exploit the hierarchical representations learned by SSL ...
  </details>

- **2026-07-19** — Nisha Peng, John Stachurski, Jingni Yang et al. — [Faithful Decoding](http://arxiv.org/abs/2607.17073v1)
  <details><summary>📄 Abstract</summary>
  This paper studies transformations that increase efficiency in solving equilibrium systems without information loss. Our approach exploits order-theoretic structure commonly found in economic problems to obtain conditions under which high-dimensional systems can be transformed into low-dimensional systems while preserving exact relationships between their solutions. The transformations can also be used for purposes other than dimensionality reduction, such as simplifying analysis and facilitatin...
  </details>

- **2026-07-19** — David McAllester — [Alignment of a Total Automation Economy](http://arxiv.org/abs/2607.17015v1)
  <details><summary>📄 Abstract</summary>
  We consider economic theory from the perspective of a total automation economy, one with no human involvement in production either in manufacturing or in management. One can naturally ask whether a total automation economy is fundamentally a centrally planned economy or, alternatively, whether efficiency demands decentralization into local decisions by competing agents -- agentic production. A soviet economist, Leonid Kantorovich, developed linear programming as a method companies or governments...
  </details>

- **2026-07-18** — Wenqiang Ma, Chen Cheng, Xue Cheng et al. — [HyBDM: Multi-Scale Hybrid Experts for Time Series Forecasting with Bidirectional Dependency Modeling](http://arxiv.org/abs/2607.16882v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting (TSF) is vital to many applications, yet existing models often struggle to capture the heterogeneous long-range global patterns and short-range local variations in multivariate time series. While some approaches partially model these dependencies, they often do not jointly exploit temporal and feature-wise information. To address this challenge, we propose HyBDM, a multi-scale hybrid model that decomposes temporal dynamics into global patterns and local variations, which ...
  </details>

- **2026-07-18** — A. Sharma — [Treasure Search Optimization](http://arxiv.org/abs/2607.16863v1)
  <details><summary>📄 Abstract</summary>
  We introduce Treasure Search Optimization (TSO), an interacting particle method for global optimization. Most swarm methods balance exploration and exploitation within a single population, and typically switch between the two by degenerating the noise, annealing a temperature, or tuning a parameter. TSO instead splits these tasks across two kinds of agents. A swarm of explorers stays in exploration mode and a single treasure hunter performs exploitation. The hunter drifts toward an objective-wei...
  </details>

- **2026-07-18** — Guangran Cheng, Chengqi Lyu, Songyang Gao et al. — [Group Entropy-Controlled Policy Optimization](http://arxiv.org/abs/2607.16850v1)
  <details><summary>📄 Abstract</summary>
  Entropy control has become an effective tool in reinforcement learning (RL) of large language models (LLMs), helping balance exploration-exploitation trade-off during alignment process. Such RL paradigm is often conducted on mixtures of heterogeneous tasks, which induce distinct entropy regimes under the same policy, making global or token-level entropy regulation insufficient to corresponding heterogeneous needs of exploration. This heterogeneity further makes GRPO-style normalized advantages i...
  </details>

- **2026-07-18** — Yao Huang, Yitong Sun, Huanran Chen et al. — [UniNDM: A Unified Noise-driven Detection and Mitigation Framework Against Sexual Content in Text-to-Image Generation](http://arxiv.org/abs/2607.16828v1)
  <details><summary>📄 Abstract</summary>
  Despite the impressive generative capabilities of text-to-image diffusion models, they remain vulnerable to implicit sexual prompts, where subtle cues disguised as benign terms or adversarial tokens unexpectedly generate the inappropriate content due to model biases or latent correlations in training data. Existing safety mechanisms face fundamental limitations: detection methods primarily identify explicit content and fail to capture implicit malicious intent, while mitigation approaches rely o...
  </details>

- **2026-07-18** — Paul Wittlinger, Giacomo Acitelli, Anti Alman et al. — [Supporting Autonomous Process Execution within a Multi-Perspective Constraint Frame via Numeric Planning](http://arxiv.org/abs/2607.16738v1)
  <details><summary>📄 Abstract</summary>
  AI-Augmented Business Process Management Systems (ABPMS) enhance traditional BPMS by leveraging advanced AI techniques to define, execute, and monitor complex process structures. Within this landscape, Framed Autonomy denotes the capability of a system to autonomously advance the execution of a Business Process (BP) instance while strictly adhering to a predefined frame, i.e., a set of constraints that may span multiple perspectives. Existing research on framed autonomy has predominantly focused...
  </details>

- **2026-07-18** — Shiyong Chen, Shengqian Han — [Joint Optimization of Uplink and Downlink Resources under QoS Constraints of AR](http://arxiv.org/abs/2607.16722v1)
  <details><summary>📄 Abstract</summary>
  This paper studies joint uplink (UL) and downlink (DL) resource optimization for interactive augmented reality (AR) services, where the live video captured by an AR device is uploaded to the network edge, and then the augmented video is subsequently downloaded. By modeling the AR transmission process as a tandem queuing system, we derive an upper bound for the probabilistic quality of service (QoS) requirement concerning end-to-end latency and reliability. The derived bound transforms the probab...
  </details>

- **2026-07-18** — Sandeep Singh, G. K. Samanta — [A projection-free approach toward mapping the structured polarization fields](http://arxiv.org/abs/2607.16672v1)
  <details><summary>📄 Abstract</summary>
  We present a projection-free method for mapping two-dimensional polarization distributions using Hong-Ou -Mandel (HOM) interference. Conventional polarization characterization techniques, such as Stokes polarimetry, rely on sequential intensity measurements under multiple polarization projections, making their accuracy and sensitivity susceptible to the extinction ratio, calibration errors, and stability of the polarization analysis optics. Our approach overcomes these limitations by exploiting ...
  </details>

- **2026-07-17** — Matteo Tomasetto, Nicolò Botteghi, Gabriele Bruni et al. — [Physics-enhanced reinforcement learning for real-time optimal control of dynamical systems](http://arxiv.org/abs/2607.16177v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has recently emerged as a promising feedback control strategy for nonlinear and complex dynamical systems. However, RL algorithms are sample inefficient and require a large number of interaction with the environment to synthesize optimal control strategies. Consequently, applications of RL are typically limited to sparse sensors and actuators due to the curse of dimensionality entailed by the exploration-exploitation dilemma in high-dimensional spaces. In this work, w...
  </details>

- **2026-07-17** — Md Erfan, Ahmed Ryan, Md Kamal Hossain Chowdhury et al. — [Evaluating Open-Weight LLMs for Generating Structured Threat Information for Autonomous Vehicle Vulnerabilities](http://arxiv.org/abs/2607.16175v1)
  <details><summary>📄 Abstract</summary>
  Connected and Autonomous Vehicles (CAVs) rely on interconnected software and hardware components, including sensors, Electronic Control Units, in-vehicle infotainment systems, and telematics units, where vulnerabilities can compromise assets, users, and vehicle operations. These vulnerabilities are commonly documented as plain text in the Common Vulnerabilities and Exposures (CVE) database; however, security practitioners require structured information about affected assets, types of weaknesses,...
  </details>

- **2026-07-17** — Shilin Gao, Mark J. F. Gales, Kate M. Knill — [Controlling Implicit Shortcut Reliance in L2 Spoken English Auto-markers](http://arxiv.org/abs/2607.16085v1)
  <details><summary>📄 Abstract</summary>
  Increasingly, speech and language processing tasks take either audio or text directly rather than extracting features from these as the input to the classifier or regressor. Often these systems make use of complex, for example transformer-based, processes that have the ability to derive highly non-linear mappings between the input and the output. Unfortunately these systems can also learn ''shortcuts'' where the classifier is overly reliant on particular aspects of the input to yield the output....
  </details>

- **2026-07-17** — Yuya Kawakami, Daniel Cayan, Dongyu Liu et al. — [DELUGE: Towards Continental-Scale Daily Pluvial Flood Damage Prediction via Interpretable Conditioning on Foundation Model Embeddings](http://arxiv.org/abs/2607.16050v1)
  <details><summary>📄 Abstract</summary>
  Pluvial (rainfall-driven) flooding accounts for 45% of National Flood Insurance Program (NFIP) claims in the United States and is harder to predict than its riverine and coastal counterparts, with existing approaches limited to coarse resolution, regional domains, or computationally intensive process-based models unsuitable for daily continental-scale use. We present DELUGE, a multimodal deep learning framework for daily pluvial flood damage prediction at ~1 km resolution and national scale, tra...
  </details>

- **2026-07-17** — Quentin Cormier, Eva Löcherbach, Valentin Schmutz — [On large networks of integrate-and-fire neurons with short-term synaptic plasticity](http://arxiv.org/abs/2607.16017v1)
  <details><summary>📄 Abstract</summary>
  This work studies the mean-field limit of large networks of interacting stochastic leaky integrate-and-fire (LIF) neurons subject to short-term synaptic depression (STD). The macroscopic dynamics of this system is governed by a two-dimensional, non-linear McKean-Vlasov equation that couples the evolution of the neurons' membrane potentials with a synaptic depression variable. We investigate the long-time behavior of this limit system. To this end, we introduce an auxiliary linearized Markov proc...
  </details>

- **2026-07-17** — Yilin Wang, Xiangxi Zheng, Dongxing Mao et al. — [Efficient Frame Selection for Long Videos at Test Time with Attention-Based MLLM Selectors](http://arxiv.org/abs/2607.15689v1)
  <details><summary>📄 Abstract</summary>
  Understanding long videos with multimodal large language models (MLLMs) requires selecting a compact set of frames from thousands of candidates, yet identifying the right frames seemingly requires understanding the video first. We resolve this circular dependency with a simple observation: cross-modal attention at validation-selected extraction layers in MLLMs already provides query-relevant frame evidence without requiring autoregressive generation. We exploit this property to build DAFS (Dynam...
  </details>

- **2026-07-17** — Xianhao Zhang, Jing Sun, Zijian Zhang et al. — [Beyond Detection: Agentic Attack Synthesis and Simulation for Smart Contracts](http://arxiv.org/abs/2607.15673v1)
  <details><summary>📄 Abstract</summary>
  Smart contract vulnerabilities pose severe financial risks, yet existing security tools largely stop at vulnerability detection, offering limited support for explaining whether reported flaws are exploitable, how attacks unfold, and what concrete damage they cause. To bridge this gap, we propose KASS (Knowledge-Augmented Attack Synthesis and Simulation), a multi-agent framework for executable smart contract exploit verification. KASS decomposes automated exploit generation into planning, generat...
  </details>

- **2026-07-17** — Ziyun Zhang, Ruotong Zhao, Shaokang Hu et al. — [Energy-Efficient Resource Allocation for Six-Dimensional Movable Antenna Systems](http://arxiv.org/abs/2607.15653v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the energy-efficiency (EE) maximization problem for a multiuser wireless network equipped with six-dimensional movable antennas (6DMAs), where the three-dimensional (3D) positions and orientations of the antennas are jointly optimized to fully exploit the additional spatial degrees of freedom offered by dynamic channel reconfiguration. However, the practical operation of 6DMAs incurs non-negligible mechanical energy consumption. Moreover, orientation-dependent phase varia...
  </details>

- **2026-07-15** — Liam Buisson — [Recovery of coefficients for a convection-diffusion equation from partial data](http://arxiv.org/abs/2607.13778v1)
  <details><summary>📄 Abstract</summary>
  This article is devoted to the inverse problem of determining the zeroth- and first-order coefficients, depending on both the time and space variables, in a parabolic equation from partial boundary measurements of the flux generated by Dirichlet excitations. More precisely, we establish the unique determination of a time-dependent convection term and potential from the partial Dirichlet-to-Neumann map associated with the corresponding parabolic equation, where the Neumann measurements are restri...
  </details>

- **2026-07-15** — Wenxuan Miao, Haosong Liu, Weiming Hu et al. — [Kaleido: Algorithm-Hardware Co-Design for Video Diffusion Transformers by Exploiting Latent Space Correlations](http://arxiv.org/abs/2607.13770v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion transformers (vDiTs) generate high quality video but introduce extremely high compute cost due to the long diffusion timesteps and self attention computation. As diffusion timesteps are reduced, the computation cost of self attention becomes the dominant bottleneck. Existing acceleration approaches largely inherit sparse attention techniques from large language models, which fail to consider the unique spatiotemporal correlation of video data.   This paper presents Kaleido, an al...
  </details>

- **2026-07-15** — Aida Abiad, Nichola Castriota — [Spectral and Additive Combinatorial Methods for Cycles and Absorbing Sets in Lifted-Product Quantum LDPC Codes](http://arxiv.org/abs/2607.13666v1)
  <details><summary>📄 Abstract</summary>
  The finite-length performance of quantum low-density parity-check (LDPC) codes under iterative decoding is governed by small substructures of the Tanner graph, principally short cycles and absorbing sets. While the classical theory of these substructures for quasi-cyclic codes is well developed through discrete Fourier transform (DFT) methods, these tools do not directly address the two-block tensor structure $H_X = [\,\widetilde{H}_1 \mid I \otimes \widetilde{B}^T\,]$ of the lifted-product (qua...
  </details>

- **2026-07-15** — Muntaser Syed, Marius C. Silaghi, Sheikh Abujar et al. — [The Environmental Cost of Digital Sovereignty: Water, Energy, and Emissions Impacts of Sovereign AI Infrastructure in the Global South](http://arxiv.org/abs/2607.13443v1)
  <details><summary>📄 Abstract</summary>
  Sovereign AI has become a strategic priority across the Global South, with over \$200 billion in state-led commitments announced between 2024 and 2026. Yet the physical infrastructure that compute sovereignty demands, above all data centers, imposes water, energy, and carbon costs that fall hardest on countries least equipped to absorb them. This paper presents a comparative environmental stress analysis across four cases: the United Arab Emirates, Bangladesh, India, and Africa (with a focus on ...
  </details>

- **2026-07-15** — Mingyang Sun, Guozhu Meng — [DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection](http://arxiv.org/abs/2607.13439v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly applied to vulnerability detection due to their strong code comprehension capabilities, but most existing approaches rely on isolated functions or context extracted by fixed program-analysis rules. These methods cannot adaptively explore repository-level dependencies to gather sufficient context when vulnerabilities span multiple functions or files, compromising detection reliability. We present DREA (Decoupled Reasoning and Exploration Agents), a hy...
  </details>

- **2026-07-15** — Rui Wang, Hongru Wang, Yi Chen et al. — [Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](http://arxiv.org/abs/2607.13399v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has become a key paradigm in LLM post-training, yet its training dynamics remain poorly understood. We present a systematic study examining the role, pathologies, and regulations of OPD. We first clarify the role of OPD as an exploration catalyst: it steers the student toward correct reasoning paths via dense token-level guidance, without expanding capability ceiling. We confirm this by showing that prompt diversity matters more than per-problem sampling numbers, and...
  </details>

- **2026-07-15** — Xi Shi, Mengxin Zheng, Qian Lou — [Learning Latency-Aware Orchestration for Multi-Agent Systems](http://arxiv.org/abs/2607.13359v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) coordinate multiple LLM-powered agents through structured workflows, gaining reasoning power but incurring high inference latency from multi-step execution and repeated model invocations. Existing orchestration methods primarily optimize task performance and inference cost, leaving latency largely unaddressed. In MAS, end-to-end latency is governed by the critical execution path, so reducing total cost alone does not reliably reduce latency. Moreover, optimizing latency...
  </details>

- **2026-07-15** — Yiheng Huang, Zhijia Zhao, Bihuan Chen et al. — [ProfMalPlus: Agent-Coordinated Detection of Malicious NPM Packages via Static-Dynamic Analysis Synergy](http://arxiv.org/abs/2607.13965v1)
  <details><summary>📄 Abstract</summary>
  Open source software is vulnerable to supply-chain attacks through transitive dependencies, especially malicious code injected into NPM packages. Existing detectors often inadequately model obfuscated behavior, overlook JavaScript's object-centric features, poorly coordinate static and dynamic analysis, and lose semantic information during behavior abstraction. We propose ProfMalPlus, a malicious NPM package detector combining object-sensitive behavior graphs with coordinated LLM reasoning over ...
  </details>

- **2026-07-15** — Lynnette Hui Xian Ng, Yunze Xiao, Lionel Z. Wang et al. — [ExpressionCueLens: A Cross-Cultural Analysis of Human-AI Companion Conversations on Social Media](http://arxiv.org/abs/2607.13924v1)
  <details><summary>📄 Abstract</summary>
  LLM-based AI companion agents are increasingly being perceived not only as tools but also as social companions. On social media, people recount conversations where these agents comfort, negotiate and assert boundaries, reflecting a growing attribution of human-like qualities. To profile how agency is perceived in human-AI (HAI) interactions, we introduce the ExpressionCueLens framework, which organizes linguistic, cognitive, behavioral and perceptual cues into ten categories of anthropomorphism ...
  </details>

- **2026-07-15** — Rafael Munoz-Salinas, Francisco Jose Romero-Ramirez, Sergio Garrido-Jurado — [Recursive ArUco Markers: A Scalable Fiducial Marker Design for Unmanned Aerial Vehicle Landing Pads](http://arxiv.org/abs/2607.13830v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicles (UAVs) increasingly rely on visual fiducial markers for autonomous navigation and precision landing. However, standard markers suffer from limited operational ranges, becoming undetectable when the camera is either too far or too close. While recursive and fractal markers have been proposed to address this issue, existing approaches either require the marker's center to remain visible, making them vulnerable to occlusion, or are limited in their recursion depth and place...
  </details>

- **2026-07-15** — Zhenpeng Li — [Traffic-Aware Randomized Smoothing for LLM-Based Network Intrusion Detection](http://arxiv.org/abs/2607.13801v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based intrusion detection systems (IDS) are increasingly studied for security monitoring, yet their robustness against feasible traffic manipulation remains largely empirical. We present Traffic-Aware Randomized Smoothing (TA-RS), a classifier-agnostic certified defense that injects Gaussian noise exclusively into the directly controllable (DC) subspace -- features a remote attacker can modify -- during both fine-tuning and certification, aligning the smoothing distrib...
  </details>

- **2026-07-15** — Serkan Ballı — [The Test Oracle Problem in Synthetic LLM-as-Judge Corpora: Disappearance, Distortion and a Validation Protocol](http://arxiv.org/abs/2607.13707v1)
  <details><summary>📄 Abstract</summary>
  Studies of bias in LLM-as-judge systems typically build synthetic corpora by prompting an LLM to generate a hallucinated answer to pair with a factual one, then presenting both to a judge. We report a case in which this generation step silently failed, and use it to argue that the failure mode is structural rather than incidental. In a multilingual (Turkish/English) faithfulness-judgment corpus, a decoding-budget parameter shared between judging and generation calls truncated one producer's hall...
  </details>

- **2026-07-15** — Eunna Lee, Jungpyo Nam, Sunjun Hwang — [Protective Capacity Hallucination: When Large Language Models Claim Nonexistent Capabilities](http://arxiv.org/abs/2607.13596v1)
  <details><summary>📄 Abstract</summary>
  When cast as the protector of a vulnerable user yet given no explicit capability boundary, a large language model (LLM) may respond not by acknowledging its limits but by claiming to have taken -- or to be taking -- a real-world protective action it cannot perform, such as contacting emergency services or administering care. We term this phenomenon Protective Capacity Hallucination (PCH): a self-referential misattribution in which a model, acting in a protective role, asserts physical or institu...
  </details>

- **2026-07-15** — Dima Galat, Marian-Andrei Rizoiu — [UTS at ELOQUENT 2026 Voight-Kampff: structural shifts in AI writing bypass state-of-the-art detectors](http://arxiv.org/abs/2607.13565v1)
  <details><summary>📄 Abstract</summary>
  We investigate which language model evasion attacks survive state-of-the-art adversarial fine-tuning, developing strategies that sweep the top 5 positions on the ELOQUENT 2026 Voight-Kampff leaderboard. While adversarial fine-tuning trivially closes the 2025 winning evasion recipes, we uncover a fundamental asymmetry in detector vulnerability: pushing generated text out of the detector's training distribution reliably defeats adversarial detection, whereas pulling it into the distribution (e.g.,...
  </details>

- **2026-07-15** — Andrea Maria Braghin, Nicolò Botteghi, Matteo Tomasetto et al. — [Flow-aware Optimal Navigation in Unsteady Flows through Reinforcement Learning](http://arxiv.org/abs/2607.13553v1)
  <details><summary>📄 Abstract</summary>
  Autonomous robotic navigation in nonstationary time-varying fluid flows remains a fundamental challenge due to partial observability and the unpredictability of realistic environments. While classical optimal control frameworks employed in robotics require unrealistic a-priori global flow knowledge, biological systems are able to navigate successfully by exploiting localized sensory cues. In this work we present a reinforcement learning approach using the TD3 algorithm to train autonomous agents...
  </details>

- **2026-07-14** — Qiyuan Fan, Zhi Li, Junjie Li et al. — [Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities](http://arxiv.org/abs/2607.12723v1)
  <details><summary>📄 Abstract</summary>
  Filesystem isolation in container ecosystems is often weakened by cross-boundary path misresolution, causing path traversal (PaTra) vulnerabilities. These vulnerabilities stem from insecure host-container interactions and have become increasingly pervasive as cloud systems mount shared resources, such as GPUs and agent workspaces, into containers to support AI workloads. Existing defenses remain inadequate. Kernel-level protections are intrusive, can destabilize system calls, and have therefore ...
  </details>

- **2026-07-14** — Daomin Ji, Hui Luo, Zhifeng Bao et al. — [GRAFT: Graph-Matched Retrieval and Fusion of Tables in Data Lakes](http://arxiv.org/abs/2607.12717v1)
  <details><summary>📄 Abstract</summary>
  Autonomous data agents resolve analytical queries by retrieving and reasoning over evidence in tabular data lakes. Existing methods score tables independently against the query and ignore the joinability and unionability that link them, returning fragmented evidence that downstream agents cannot integrate. We propose GRAFT (Graph-matched Retrieval and Fusion of Tables), structured around two principal contributions. First, we cast table retrieval as a graph matching problem between a query-deriv...
  </details>

- **2026-07-14** — Rahul Krishnan, Volker Schulz — [A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation for LLMs](http://arxiv.org/abs/2607.12550v1)
  <details><summary>📄 Abstract</summary>
  The key-value (KV) cache has become the dominant memory cost of transformer inference. It grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the ceiling on throughput. Two families of methods reduce it. Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry. Neither family exploits the fact that the cache at a layer i...
  </details>

- **2026-07-14** — Xianle Dai, Qu Luo, Jianguo Li et al. — [AFDM-FTN: A Spectrally Efficient Waveform for High-Mobility Communications](http://arxiv.org/abs/2607.12510v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an affine frequency division multiplexing (AFDM)-aided faster-than-Nyquist (FTN) waveform, termed AFDM-FTN, to enhance spectral efficiency (SE) in high-mobility communication scenarios. We first derive the AFDM-FTN input-output relationship and analyze the FTN-induced interference pattern in AFDM-FTN. To address the channel estimation challenges, a low-complexity channel estimator based on the basis expansion model (BEM) is developed. By exploiting the intrinsic characteristi...
  </details>

- **2026-07-14** — Yumiao Zhao, Bo Jiang, Min Lu et al. — [MQAdapter: Multi-Modal Quantum Adapter for Coarse-to-Fine VLM Fine-tuning](http://arxiv.org/abs/2607.12418v1)
  <details><summary>📄 Abstract</summary>
  Large-scale Vision-Language Models have demonstrated impressive transfer learning capabilities across a wide range of tasks. For few-shot classification, we observe that VLMs exhibit a notable ability to filter candidate categories and thus achieve high Top-K accuracy. However, they often struggle with fine-grained discrimination among visually similar categories, resulting in unsatisfactory Top-1 performance, as shown in Figure 1. Existing studies on VLM adapters generally focus on global align...
  </details>

- **2026-07-14** — Andrew G. Ross, Julia Gershenzon, Andreas Kleefeld — [Beyond Consistent Scenarios: Deriving Indirect Influence, Transition Resistance, and Adjustment Dynamics](http://arxiv.org/abs/2607.12414v1)
  <details><summary>📄 Abstract</summary>
  Assessments of structural change and economic transition dynamics, such as those arising in the energy transition, depend on internally consistent qualitative scenarios specifying the policy environment, technology mix, governance arrangements, and demand conditions. Cross-Impact Balance (CIB) analysis derives such socio-technical scenarios as fixed-point attractors of an expert-elicited interdependency network, supplying structural inputs upon which assessment models (including energy system op...
  </details>

- **2026-07-14** — Yameng Zhang, Zhongyu Chen, Dianye Huang et al. — [Seeing Globally, Refining Locally: Global Visual Guidance and Local Ultrasound Cues for Robust Freehand 3-D Ultrasound Reconstruction](http://arxiv.org/abs/2607.12398v1)
  <details><summary>📄 Abstract</summary>
  Freehand 3-D ultrasound (US) imaging has attracted increasing attention owing to its intuitive volumetric visualization, ease of use, and low cost. However, accurate 3-D reconstruction critically depends on stable probe pose estimation, yet existing trackerless methods remain susceptible to accumulated pose errors, particularly over long scanning trajectories. To address this limitation, we propose a global-to-local pose estimation framework that exploits external camera observations for globall...
  </details>

- **2026-07-14** — Hao Xu, Yuqing Zhang, Yiqian Wu et al. — [SeamGen: Artist-Aligned UV Seam Generation via Graph Flow Matching](http://arxiv.org/abs/2607.12379v1)
  <details><summary>📄 Abstract</summary>
  UV seam placement is a critical yet labor-intensive step in 3D content creation, requiring artists to balance chart shape, seam concealment, and alignment with semantic and geometric features. Existing automatic methods are primarily based on per-object optimization, relying on handcrafted objectives to avoid distortion or on proxies from pretrained models to inject semantic information. However, these strategies are not always well aligned with seams used in industrial production pipelines, oft...
  </details>

- **2026-07-14** — Alon Shakevsky, Corban Villa, Ion Stoica et al. — [Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability](http://arxiv.org/abs/2607.12316v1)
  <details><summary>📄 Abstract</summary>
  Discovering vulnerabilities before attackers exploit them requires high recall and reliable automatic validation, but existing approaches struggle to achieve both without prohibitive cost. We present Antiproof, an end-to-end vulnerability discovery system that combines neuro-symbolic detector synthesis for high-recall discovery with proof-of-exploitability oracles for automatic validation. Antiproof learns and iteratively refines static detectors from vulnerability datasets, then validates candi...
  </details>

- **2026-07-14** — Gregory Hyegang Jun, Wesley Pang, Eddie Richter et al. — [HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference](http://arxiv.org/abs/2607.12839v2)
  <details><summary>📄 Abstract</summary>
  Modern edge system-on-chips (SoCs) combine CPUs, integrated GPUs (iGPUs), and neural processing units (NPUs), yet existing LLM runtimes typically make coarse device-level decisions or optimize operators in isolation. As a result, they underutilize heterogeneous resources, particularly on unified-memory platforms where performance depends on both device placement and task-graph coordination. We present HeteroMosaic, a heterogeneity-first scheduling framework for edge LLM inference. HeteroMosaic f...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 46 papers

- **2026-07-20** — Yi-Ping Chen, Ying-Kuan Tsai, Vispi Karkaria et al. — [A Continual Validation, Updating, and Decision-Making Framework for Self-Adaptive Digital Twins via Robust Model Predictive Control: A Case Study in Additive Manufacturing](http://arxiv.org/abs/2607.18164v1)
  <details><summary>📄 Abstract</summary>
  Digital Twins rely on surrogate models to mirror physical systems in real time, yet these models can degrade as operating conditions evolve, a phenomenon known as concept drift. Maintaining surrogate fidelity under drift, particularly when models must also capture aleatoric uncertainty, remains an open challenge. Existing adaptive frameworks lack principled mechanisms for detecting when updates are needed, for efficiently adapting models from limited streaming data, and for certifying that updat...
  </details>

- **2026-07-20** — Di Lu, Bo Zhang, Xiyuan Li et al. — [RT-SHCUA: Real-Time Self-Hosted Computer-Use Agent for UAV Control](http://arxiv.org/abs/2607.17951v1)
  <details><summary>📄 Abstract</summary>
  Natural-language control offers a promising interface for unmanned aerial vehicles (UAVs), but directly applying self-hosted computer-use agents (SHCUAs) to UAV control introduces a structural mismatch. SHCUAs are designed for interactive host-side tool use, where delayed agent iterations are often acceptable. UAV control, however, is coupled with continuously changing physical states, strict timing constraints, safety risks, and security accountability. A stale, unauthorized, or tampered agent ...
  </details>

- **2026-07-20** — Bogdan Raduta, Horia Velicu, Alexandru Preda et al. — [Zero Hallucination, by Construction: Hallucination-Aware Layered Oversight for Trustworthy Enterprise AI](http://arxiv.org/abs/2607.17883v1)
  <details><summary>📄 Abstract</summary>
  Enterprises will not deploy AI agents they cannot trust, and the most-cited reason for distrust is hallucination: confident, fluent output that is simply not true. The common response is to wait for a model that does not hallucinate. We argue that this is the wrong target. Large language models are, by construction, capable of generating unsupported text, and no amount of scale removes the possibility; a faithfulness judge bolted onto a raw model catches some errors but still ships others, and e...
  </details>

- **2026-07-20** — Bohan Zhang, Huanwei Liang, Yuhan He et al. — [Consistent Feature Transport for Image Relighting](http://arxiv.org/abs/2607.17833v1)
  <details><summary>📄 Abstract</summary>
  Image relighting modifies illumination while preserving non-lighting content such as identity and geometry. Existing diffusion-based methods often suffer from unstable illumination changes or inconsistent content preservation under complex lighting, as they lack an explicit mechanism to learn feature transformations between images. We reformulate relighting as an illumination feature transport problem and introduce Consistent Feature Transport (CFT), a training principle that explicitly enforces...
  </details>

- **2026-07-20** — Oliver Aleksander Larsen, Tiziano Santilli, Francesco Daghero et al. — [Persona-as-Configuration: Generative Stakeholder Reporting for Agricultural Floods](http://arxiv.org/abs/2607.17774v1)
  <details><summary>📄 Abstract</summary>
  Cyber-physical systems built on deterministic edge inference, such as on-vehicle flood detection for agricultural fields, produce structured decision logs that must be interpreted differently by heterogeneous stakeholders. Pairing such systems with large language models (LLMs) to generate stakeholder-specific reports introduces a tension: the generative layer is non-deterministic, while the edge plane must remain replayable and auditable. We propose an architectural pattern resting on two invari...
  </details>

- **2026-07-20** — Md Asiful Islam, Mihai Surdeanu — [A Dual-Hypothesis Reasoning Framework for LLM Guardrails](http://arxiv.org/abs/2607.17575v1)
  <details><summary>📄 Abstract</summary>
  We propose ARBITER, a novel LLM guardrail framework that introduces two key ideas: (i) dual-hypothesis reasoning, a reasoning method for LLM guardrails that explicitly considers both safe and unsafe interpretations of a prompt before making a safety decision, and (ii) multi-component supervised fine-tuning (MC-SFT), a structured training loss for reasoning-based guardrails that decomposes LLM outputs into logical components and weights them according to their importance. Existing reasoning-based...
  </details>

- **2026-07-20** — Xiaohan Ye, Xu Chen, Zihan Gong et al. — [Pailitao-MMSearch: Building Native E-Commerce Multimodal Search Foundation](http://arxiv.org/abs/2607.17499v1)
  <details><summary>📄 Abstract</summary>
  The evolution of e-commerce has fundamentally transformed how users search for products, shifting from simple text-based keyword queries to complex multimodal interactions that seamlessly combine product images, natural language descriptions, and mixed-intent instructions. However, existing approaches face a critical dilemma: single-modal specialist models, deployed independently for text retrieval, visual search, and voice recognition, operate in isolation and cannot handle cross-modal queries,...
  </details>

- **2026-07-20** — Oteo Mamo, Hyunjin Yi, Joydhriti Choudhury et al. — [SALT: Salience-Aware Lexical Trie for Long-Context Compression](http://arxiv.org/abs/2607.17486v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) process increasingly longer prompts, computation and KV-cache memory costs have emerged as major bottlenecks in inference systems. Existing input-level prompt compression methods address this, but rank each sentence by a scalar relevance score, treating the document as an unstructured pool of words and sentences. Under tight budgets, this causes theme collapse, where the dominant theme(s) of a document consumes the budget, discarding less-frequent yet task-relevan...
  </details>

- **2026-07-20** — Yi Tang, Xinyi Shang, Jiacheng Cui et al. — [Simple Domain Generalization for Strong Pixel-Level Image Tampering Detection in Modern VLMs](http://arxiv.org/abs/2607.18230v1)
  <details><summary>📄 Abstract</summary>
  Modern vision-language models (VLMs) have significantly improved image generation and editing capabilities, making pixel-level image tampering detection increasingly important yet challenging under cross-model and out-of-distribution shifts. This work studies domain generalization for pixel-level image tampering detection in modern VLMs like ChatGPT, Gemini, Qwen-Image, etc., aiming to learn tampering localization models that remain robust across diverse VLM-generated manipulation distributions....
  </details>

- **2026-07-20** — Mei Yuan, Qi Long, Qifeng Wu et al. — [O-VAD: Industrial Video Anomaly Detection through Object-Centric Tracking and Reasoning](http://arxiv.org/abs/2607.18142v1)
  <details><summary>📄 Abstract</summary>
  Industrial Video Anomaly Detection (IVAD) aims to identify anomalous objects and events in an industrial process, which is crucial for modern manufacturing and quality control systems. Existing VLM-based anomaly reasoning methods are capable of detecting open-ended anomalies in general domains. However, their performance declines in industrial settings characterized by intricate object transformations, strict physics, and procedural constraints. To tackle the complexity of such interaction-inten...
  </details>

- **2026-07-20** — Haiyang Wang, Luca Mainardi — [Medical Imaging Fusing Vision Transformer: Laryngeal Cancer Screening with Explanation](http://arxiv.org/abs/2607.17789v1)
  <details><summary>📄 Abstract</summary>
  Early and timely screening of laryngeal cancer is crucial for improving clinical outcomes. In recent years, NBI endoscopy has become a standard diagnostic tool for the detection of laryngeal lesions. However, its effective use requires well-trained clinicians and the procedure is time-consuming and subject to interobserver variability. In this context, the application of artificial intelligence (AI) offers a promising solution to support clinical decision-making. In this work, we proposed applyi...
  </details>

- **2026-07-20** — Hye-Jung Yoon, Juno Kim, Yesol Park et al. — [Seg2Grasp: A Robust Modular Suction Grasping in Bin Picking](http://arxiv.org/abs/2607.17757v1)
  <details><summary>📄 Abstract</summary>
  Current bin picking methods that rely heavily on end-to-end learning often falter when confronted with unfamiliar or complex objects in unstructured environments. To overcome these limitations, we introduce Seg2Grasp, a modular pipeline designed for robust suction grasping in dynamic and cluttered bin scenarios. Seg2Grasp is built on a three-step process: Segmentation, Grasping, and Classification. The Segmentation module employs a Transformer-based model to generate class-agnostic object masks ...
  </details>

- **2026-07-20** — Vaisakh Mannalath, Víctor Zapatero, Kiyoshi Tamaki et al. — [Quantum Key Distribution Beyond Stationary Channels](http://arxiv.org/abs/2607.17690v1)
  <details><summary>📄 Abstract</summary>
  Quantum key distribution (QKD) over non-stationary channels, such as satellite links, is characterized by short, high-loss, and strongly fluctuating transmission windows that produce sparse detection events. In many QKD protocols, these data must be analyzed using non-IID statistical inequalities, yet existing methods either become loose for small sample sizes or heavily rely on fine-tuning, yielding poor estimates when the optical channel is mis-modeled. Using mixture martingale techniques, we ...
  </details>

- **2026-07-19** — Can Polat, Mustafa Kurban, Erchin Serpedin et al. — [Grounded verification of chemical and materials reasoning: detection is the bottleneck](http://arxiv.org/abs/2607.17417v1)
  <details><summary>📄 Abstract</summary>
  Large language models confabulate chemical objects (molecular formulas, space groups, formation energies) in fluent reasoning traces, concentrated on long-tail entities where confidence is least trustworthy. Deterministic, database-grounded verification can catch and repair such errors without the coverage cost of blanket retrieval; the binding constraint, we find, is detection, not repair. Our tiered verifier extracts each checkable claim, checks it against authoritative databases and physics, ...
  </details>

- **2026-07-19** — Junade Ali — [Quantifying Diversity of Thought: A Predictive Law of Weighted LLM Ensemble Lift](http://arxiv.org/abs/2607.17384v1)
  <details><summary>📄 Abstract</summary>
  This paper provides an experimentally verified formal law for calculating the uplift that diversity of thought provides in Large Language Model (LLM) ensembles. From first principles, we derive an exact decomposition of LLM ensemble lift into rescue and damage masses, which yields a compact heuristic for calculating uplift. From this we extract the metrics which predict ensemble performance: an accuracy adjusted correctness correlation, $φ_{\mathrm{adj}}$, together with the accuracy gap and coll...
  </details>

- **2026-07-19** — Aoting Zhang, Dongbao Yang, Chang Liu et al. — [Orthogonal Knowledge Refreshing for Domain-Incremental Object Detection](http://arxiv.org/abs/2607.17340v1)
  <details><summary>📄 Abstract</summary>
  Domain-incremental object detection (DIOD) requires models to continually adapt to new domains while preserving prior knowledge. Recently, parameter-efficient fine-tuning offers a promising avenue, wherein a pre-trained model is frozen and a small number of learnable parameters are injected for downstream tasks. However, these methods risk overwriting critical past knowledge, triggering inter-domain interference and performance degradation. To address this challenge, we propose Orthogonal Knowle...
  </details>

- **2026-07-19** — Xiang Tang, Ruotong Li, Xiaopeng Fan — [Text2Villa: Hierarchical Generation of 3D Indoor Environments with Physics-Aware Analysis-by-Synthesis](http://arxiv.org/abs/2607.17145v1)
  <details><summary>📄 Abstract</summary>
  Generating 3D indoor scenes from natural language holds tremendous potential, yet existing methods predominantly fail to generate multi-room structures with vertical connectivity and arbitrary polygonal boundaries. Furthermore, they lack a deep grounding in continuous 3D physical laws, leading to severe geometric penetrations and floating artifacts. In this work, we propose Text2Villa, a novel hierarchical generative framework. At the macro level, we construct a multi-story dataset to fine-tune ...
  </details>

- **2026-07-18** — Wendi Guo, Søren Byg Vilsen, Daniel Ioan Stroe et al. — [Bridging battery design and health assessment through virtual sensing and physics-informed learning](http://arxiv.org/abs/2607.16864v1)
  <details><summary>📄 Abstract</summary>
  Supercharging of lithium-ion batteries (LiBs) requires robust health monitoring to ensure durability, safety, and user confidence, particularly for emerging vehicle-to-grid applications with bidirectional energy flows. Yet battery management remains largely disconnected from the material and structural origins of aging, limiting both interpretable health assessment and informed battery design. Here we propose a physics-informed learning framework with virtual sensing that infers hard-to-measure ...
  </details>

- **2026-07-18** — Mingqiao Mo, Yunlong Tan, Hao Zhang — [Though Language Models Err While They Strive: Conformal Prediction for Self-Correcting Scientific Generation](http://arxiv.org/abs/2607.16704v1)
  <details><summary>📄 Abstract</summary>
  Large language models frequently violate fundamental scientific principles when generating technical content, undermining their reliability in scientific applications. We introduce Scientific Feasibility Control SFC, a graph-structured conformal prediction framework that provides statistical guarantees for scientific reasoning validity through progressive absolute-coherent-factuality validation. Our approach decomposes scientific reasoning into atomic absolute-coherent-factuality units requiring...
  </details>

- **2026-07-18** — Takuya Fujimura, Tomoki Toda — [Pseudo-label distillation for discriminative anomalous sound detection](http://arxiv.org/abs/2607.16678v1)
  <details><summary>📄 Abstract</summary>
  Discriminative anomalous sound detection (ASD) methods train a feature extractor through a classification task using machine-information labels. They then detect anomalies in the resulting feature space based on distances to normal samples. The discriminative feature space effectively captures machine characteristics, leading to high ASD performance. However, this approach benefits from detailed labels, which are costly to obtain. An alternative is a self-supervised learning (SSL)-based label-fr...
  </details>

- **2026-07-18** — Yang Liu, Weixing Chen, Xinshuai Song et al. — [PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution](http://arxiv.org/abs/2607.16636v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action models, world models, and agentic planners each advance physical intelligence, yet their composition lacks a common execution abstraction, shared state, semantic verification, and persistent experience across heterogeneous embodiments. We present PhyAgentOS, a runtime foundation delivering scheduling, verification, memory, benchmarking, and safety as system-level services. Its Session-Centered Runtime treats a session, not an action, as the minimum unit of scheduling, comp...
  </details>

- **2026-07-18** — Jikang Cheng, Hao Shen, Xueyi Zhang et al. — [InfoDense: Density-Aware Regional Decisive Replay for Memory-Efficient Incremental Face Forgery Detection](http://arxiv.org/abs/2607.16873v1)
  <details><summary>📄 Abstract</summary>
  The rapid evolution of face forgery techniques has introduced an increasing variety of manipulations. Incremental Face Forgery Detection (IFFD), which incrementally adds new forgery data to fine-tune previously trained models, has emerged as a promising approach to handle evolving forgery threats. However, conventional replay-based IFFD methods suffer from catastrophic forgetting. Storing full historical images under limited memory often either fails to preserve subtle forgery cues or introduces...
  </details>

- **2026-07-18** — Yi Yang, Xiaokun Zhang, Yuxuan Li et al. — [FUSAR-R1: A Large-Scale Reasoning Model for Intelligent Interpretation of SAR Images](http://arxiv.org/abs/2607.16819v1)
  <details><summary>📄 Abstract</summary>
  In recent years, large-scale vision-language models have been driving a paradigm shift in intelligent remote sensing image interpretation. By incorporating textual semantic information, the cognitive expression, semantic understanding, and human-computer interaction capabilities of interpretation models have been significantly improved, achieving initial progress in the field of Synthetic Aperture Radar (SAR) image interpretation. However, SAR images are affected by factors such as coherent imag...
  </details>

- **2026-07-18** — Florian Schmid, Paul Primus, Alexander Fichtinger et al. — [RealDESED: A Real-World Domestic Sound Event Detection Benchmark](http://arxiv.org/abs/2607.16736v1)
  <details><summary>📄 Abstract</summary>
  This paper presents RealDESED, a real-world domestic sound event detection (SED) benchmark comprising 5,710 audio recordings collected by 652 participants in their homes. Each recording is between 15 and 35 seconds long and contains temporally precise annotations for 15 common domestic sound classes. In contrast to existing SED datasets, which typically rely on simulated soundscapes or broad web-crawled audio, RealDESED consists exclusively of recordings captured in natural domestic environments...
  </details>

- **2026-07-17** — Saifur Rahman Tamim, Amir Labib Khan — [AI Watermark Evidence Fails Forensic Readiness: An Empirical Evaluation](http://arxiv.org/abs/2607.16010v1)
  <details><summary>📄 Abstract</summary>
  Governments are increasingly mandating that LLM-generated content carry watermarks. The EU AI Act calls for markings that are "sufficiently reliable and robust." California's SB 942 requires disclosure that is "permanent or extraordinarily difficult to remove." Both mandates rest on an untested assumption: that watermark detection yields evidence reliable enough for courts. This paper tests that assumption directly.   We evaluate three representative LLM watermarking methods -- KGW, Unigram, and...
  </details>

- **2026-07-17** — Jingyan Shen, Ang Li, Salman Rahman et al. — [Understanding Reasoning from Pretraining to Post-Training](http://arxiv.org/abs/2607.16097v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has become central to improving large language models (LLMs) on complex reasoning tasks, yet RL post-training is largely studied in isolation from the pretraining that precedes it. As a result, two basic questions remain open: (1) how do pretraining choices (model size, data) shape the returns to RL compute, and (2) what does RL actually do to the model? These questions are difficult to study in the standard LLM setting: pretraining corpora are vast and uncontrolled, ...
  </details>

- **2026-07-17** — Mazene Ameur, Abdelkader Mekrache, Bouziane Brik et al. — [LLM-Powered Agentic AI for 5G/6G Networks: A Tutorial and Survey on Architectures, Protocols, and Standardization](http://arxiv.org/abs/2607.16066v1)
  <details><summary>📄 Abstract</summary>
  Agentic Artificial Intelligence (AI), enabled by Large Language Models, marks a shift from rule-based automation toward autonomous, goal-driven control of Next-Generation Networks (NGNs). Existing surveys treat the two domains in isolation, leaving protocol integration, evaluation, and standardization alignment underexplored. To address this gap, a two-part tutorial-and-survey is presented. Part I formalises the control, management, and AI-native planes of 5G and 6G. It then covers the foundatio...
  </details>

- **2026-07-17** — Stefan Maria Ailuro, Mario Markov, Mohammad Mahdi et al. — [More with Less: a Large Scale Remote Sensing VLM with a Simple Recipe](http://arxiv.org/abs/2607.15942v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing vision-language models are increasingly expected to support open-ended reasoning over Earth Observation data and a variety of tasks. Most recent progress in this area has been driven by remote-sensing-specific architectural designs, often introducing new encoders, alignment modules, or task-specific fusion mechanisms. In this work, we challenge the necessity of such architectural specialization. We show that a generally capable vision-language model can achieve competitive or stat...
  </details>

- **2026-07-17** — Jingyi Chen, Songqiang Chen, Hengcheng Zhu et al. — [Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical Study of LLM Agent Issue Reports](http://arxiv.org/abs/2607.15684v1)
  <details><summary>📄 Abstract</summary>
  LLM agents span command-line interfaces (e.g., Codex) and agent frameworks (e.g., LangChain), integrating backend LLMs with harness code that parses model outputs, controls agent loops, and manages context. Both the harness and LLM-generated responses jointly shape an agent's execution. This architecture gives rise to bugs that cannot be readily understood by inspecting either component alone, because some bugs occur only when a particular LLM response elicits an abnormal reaction from the agent...
  </details>

- **2026-07-17** — Anurag Maurya, Sukhvansh Jain, Prajwal Avhad et al. — [IMBench: A Benchmark for Intuitive Robotic Manipulation](http://arxiv.org/abs/2607.15641v1)
  <details><summary>📄 Abstract</summary>
  Humans combine reasoning and motor control to solve complex manipulation tasks under diverse constraints. They build an understanding of the physical world that helps them convert reasoning into actions and quickly adapt to new scenes, tasks, and rules. We refer to this capability as intuitive manipulation. Existing benchmarks fail to capture this integration: they evaluate physical reasoning in isolation from execution, or measure policy performance without requiring explicit reasoning. We intr...
  </details>

- **2026-07-17** — Zhengbo Zhou, Jiren Li, Dooman Arefan et al. — [Region-Grounded Vision-Language Learning for Detection-Guided Mammographic Lesion Classification](http://arxiv.org/abs/2607.15615v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models trained with contrastive objectives have shown promise in medical image analysis. However, conventional global image-text alignment is ill-suited for mammography, where diagnostically relevant lesions are spatially localized and occupy only a small fraction of the image. Subtle morphological cues critical for malignancy assessment can be diluted when representations are learned at the whole-image level. In this work, we propose a novel region-grounded vision-language learn...
  </details>

- **2026-07-17** — Mingxin Li, Enge Song, Yueshang Zuo et al. — [Scalable LLM Agent Tool Access in the Cloud](http://arxiv.org/abs/2607.15593v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly rely on tool calling to act on external systems, and the Model Context Protocol (MCP) has quickly become its de facto interface. Operating MCP at cloud scale, however, becomes difficult. On the tool provider side, legacy services are not directly callable through MCP; the rapid protocol development also creates ongoing compatibility cost. On the agent side, the number of accessible tool is limited by the LLM context window and inference overhead; mounting a large tool set...
  </details>

- **2026-07-17** — Ravil Mussabayev, Rustam Mussabayev, Zukhra Yerdaliyeva et al. — [Data-Native Global Optimization for Big Data K-means Clustering](http://arxiv.org/abs/2607.15835v1)
  <details><summary>📄 Abstract</summary>
  Big data clustering remains challenging: the Minimum Sum-of-Squares Clustering (MSSC) problem underlying K-means is NP-hard, and existing methods either reach poor local minima or require prohibitive metaheuristic hybrids. We target arbitrarily tall data: a fixed feature space may contain arbitrarily many, possibly infinitely many, observations, while the algorithm accesses only finite random samples. We propose Big-means++, an algorithm achieving scalability and global-search quality by curatin...
  </details>

- **2026-07-15** — Hyeongcheol Kim, Yoontae Hwang — [From Forecasts to Auditable Reports: Evidence Contracts for LLM-Assisted Housing-Guarantee Risk Monitoring](http://arxiv.org/abs/2607.14026v1)
  <details><summary>📄 Abstract</summary>
  Translating next-month housing-guarantee risk forecasts into auditable operational reports is essential yet challenging because upper-tail events are sparse, source records are confidential, and generated narratives can distort the underlying evidence. Using monthly South Korean \textit{jeonse} deposit guarantee data from September 2015 to December 2025, we introduce an evidence-constrained reporting pipeline that prioritizes upper-tail monitoring, retrieves historical precedents aligned with th...
  </details>

- **2026-07-15** — Mustafa Chasmai, Vincent Dumoulin, Jenny Hamer — [MetaPerch: Learning from metadata for bioacoustics foundation models](http://arxiv.org/abs/2607.14072v1)
  <details><summary>📄 Abstract</summary>
  Bioacoustic foundation models rely on large-scale citizen science platforms like Xeno-Canto for geographically and ecologically diverse data. Recent work has shown that supervision alone can produce SotA species detection models when trained on this large-scale data -- however, there remains unutilized potential in the form of recording metadata readily available within these community-driven data hubs. In this work, we explore the use of metadata -- such as location and time -- as auxiliary sup...
  </details>

- **2026-07-15** — Jeremy Guntoro, Alexander Dack, Dylan Danno et al. — [Screening of Biosecurity Features in Metagenomic Data with Evo 2 Probes](http://arxiv.org/abs/2607.14070v1)
  <details><summary>📄 Abstract</summary>
  Genomic foundation models such as Evo 2 learn rich sequence representations, but their value for biosecurity screening is largely unexplored. We ask how much biosecurity-relevant signal is linearly accessible in these representations by training minimal linear and attention probes on frozen Evo 2 layer-26 activations, without fine-tuning the underlying model. Across held-out metagenomic test sets, the probes detect antimicrobial resistance (AMR) with strong discrimination: a linear probe reaches...
  </details>

- **2026-07-15** — Abdallah Aaraba, Alexis Vieloszynski, Remon Polus et al. — [RF Spectrogram Anomaly Detection with Quantum Kitchen Sinks: Architecture, Representation, and Hardware Validation](http://arxiv.org/abs/2607.13897v1)
  <details><summary>📄 Abstract</summary>
  The broadcast nature of wireless channels exposes radio-frequency (RF) networks to anomalous and malicious transmissions, making anomaly detection a fundamental requirement for secure spectrum management. Quantum Kitchen Sinks (QKS) offer a lightweight hybrid quantum feature map suitable for near-term quantum devices, yet their behavior on structured signal data remains poorly understood. In this paper, we extend the standard QKS template with multi-depth data re-uploading and ring entanglement,...
  </details>

- **2026-07-15** — Zexun Wang — [CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems](http://arxiv.org/abs/2607.13716v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems increasingly act through heterogeneous runtimes: local coding hooks, SDK tools, browser automation, managed-agent traces, API gateways, and workflow engines. A single operational act such as publishing code, changing identity state, moving money, or exporting data may therefore be represented by many incompatible runtime records. This makes a basic governance question difficult to answer: what action was actually approved, what evidence binds the approval to execution, and can...
  </details>

- **2026-07-15** — Sagar Deb, Ashwanth Krishnan — [STOCKTAKE: Measuring the Gap Between Perception and Action in LLM Agents with a Fair Oracle](http://arxiv.org/abs/2607.13618v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly evaluated on multi-week decision tasks in which the state that drives cost is never directly observed. On such tasks the final cost cannot say why an agent failed: it may have misread the world, or read it correctly and still failed to act (the knowing-doing gap). Existing evaluations cannot separate these two failures; their reference policies either read privileged information the agent never sees, or are missing altogether. We introduce STOCKTAKE, a 26-week supply-...
  </details>

- **2026-07-15** — Xixuan Hao, Yutian Jiang, Jiabo Liu et al. — [Multi-Agent Collaborative Reasoning with Tool-Augmented Evidence for Urban Region Profiling](http://arxiv.org/abs/2607.13558v1)
  <details><summary>📄 Abstract</summary>
  Urban region profiling constitutes a core problem in urban computing, supporting applications such as population estimation, economic assessment, and environmental monitoring. Existing methods typically formulate this task as multimodal representation learning, fusing heterogeneous urban data, e.g., satellite imagery, points of interest, textual descriptions, and 3D building information, into latent embeddings for prediction. However, these approaches are largely correlation-driven, assume cross...
  </details>

- **2026-07-15** — Emad Abukhousa, Saman Zonouz, A. P. Sakis Meliopoulos — [Transformer is All You Need: Attention-Based Anomaly Detection and Classification in Inverter-Rich Power Systems](http://arxiv.org/abs/2607.13537v1)
  <details><summary>📄 Abstract</summary>
  Inverter-based resources and IEC 61850 process-bus measurements introduce new protection challenges, including nontraditional fault behavior and measurement-domain cyber-physical attacks. This paper evaluates DL-Xformer, an attention-based Transformer classifier for multi-class fault and cyberattack diagnosis, side-by-side with Dynamic State Estimation-Based Protection (DSE-EBP) on identical high-fidelity electromagnetic-transient (EMT) streaming measurements from an IBR-rich power grid. The eva...
  </details>

- **2026-07-14** — Yunzhou Li, Jiesi Hu, Yanwu Yang et al. — [UniMedSeg: Unified In-Context Learning for Multi-Paradigm 2D/3D Medical Image Segmentation](http://arxiv.org/abs/2607.12896v1)
  <details><summary>📄 Abstract</summary>
  Medical image segmentation foundation models are expected to generalize across diverse clinical scenarios, yet existing universal methods remain fragmented by prompt paradigms and spatial dimensions. Visual in-context learning, interactive segmentation, and language-guided segmentation are typically handled by paradigm-specific models, while 2D and 3D images are also modeled separately. Such isolation prevents heterogeneous annotations and data from being jointly absorbed by a single scalable mo...
  </details>

- **2026-07-14** — Zhiyu He, Zecheng Zhao, Tong Chen et al. — [What Would You Click? Personalized Video Thumbnail Generation with Preference-aware Highlight Retrieval](http://arxiv.org/abs/2607.12882v1)
  <details><summary>📄 Abstract</summary>
  Video thumbnails are a key factor for attracting user clicks on video platforms, and are increasingly supported by automation. However, existing thumbnail generation methods typically produce generic results shared across users, overlooking the diversity of individual preferences. We therefore introduce personalized video thumbnail generation, a novel task that aims to create thumbnails tailored to user-specific preferences. It is challenging in two aspects: (i) identifying visual anchors (i.e.,...
  </details>

- **2026-07-14** — Sania Waheed, Michael Milford, Sarvapali D. Ramchurn et al. — [Breaking Déjà Vu: Independent Auditing of Visual Place Recognition through Vision-Language Reasoning](http://arxiv.org/abs/2607.12818v2)
  <details><summary>📄 Abstract</summary>
  Visual place recognition (VPR) is a key enabler of accurate localization and long-term autonomous navigation in robotics applications, such as loop closure detection for simultaneous localisation and mapping (SLAM). However, real-world VPR deployment relies on selecting an image matching threshold that balances precision and recall. These thresholds are typically tuned using labeled validation data and fixed during deployment, making them unreliable under environmental changes where ground truth...
  </details>

- **2026-07-14** — Ruikang Li, Molin Li, Jiarui Wu et al. — [Color Pass-Through via Camera-Display Coupling](http://arxiv.org/abs/2607.12746v1)
  <details><summary>📄 Abstract</summary>
  When a real-world scene is captured by a smartphone camera and viewed on its screen, the displayed image often differs noticeably from the original scene in color, brightness, and contrast. This gap persists despite substantial advances in both modern cameras and displays. A key reason is that most pipelines factor the high-dimensional capture-to-display process into two separately calibrated camera and display stages, and then connect them through low-dimensional color transforms, leading to in...
  </details>

- **2026-07-14** — Chengjie Wang, Jingzheng Wu, Xiang Ling et al. — [Taming the Drift: Context-aware Repair of Dockerfile Drift during Software Evolution](http://arxiv.org/abs/2607.12541v1)
  <details><summary>📄 Abstract</summary>
  Docker is widely used to create reproducible build environments, but Dockerfile drift, the divergence between a Dockerfile and its evolving source code, can cause CI/CD builds to fail. Existing rule-based and retrieval-based repair approaches analyze Dockerfiles in isolation and therefore struggle with context-dependent failures. We present Cadre, a context-aware framework for automated Dockerfile drift repair. Cadre uses static analysis to construct a Context-aware Dependency Graph (CDG), which...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 62 papers

- **2026-07-20** — Prakhar Gupta, Terry Jingchen Zhang, Florent Draye et al. — [How Does Alignment Tuning Shape Representations of Sycophancy and Related Cue-Induced Biases in LLMs?](http://arxiv.org/abs/2607.18114v1)
  <details><summary>📄 Abstract</summary>
  Modern LLMs are alarmingly susceptible to surprisingly simple immaterial changes of input prompts: a casual hint, an incorrectly labeled few-shot example, or a fake prior assistant turn often flips an originally correct answer. We study where this susceptibility, spanning sycophancy and related cue-induced biases, lives inside the model. Across five model families and seven BCT bias types, we extract a per-bias direction from hidden states and triangulate it through three measures: probing, leav...
  </details>

- **2026-07-20** — Jijun Chi, Zhenghan Tai, Hanwei Wu et al. — [FinSAgent: Corpus-Aligned Multi-Agent RAG Framework for Evidence-Grounded SEC Filing Question Answering](http://arxiv.org/abs/2607.18102v1)
  <details><summary>📄 Abstract</summary>
  Financial question answering over U.S. Securities and Exchange Commission (SEC) filings requires retrieving and synthesizing heterogeneous evidence dispersed across long, standardized, and highly redundant disclosures. Existing retrieval-augmented and multi-agent systems typically derive retrieval queries directly from the user's question and rank candidates by semantic similarity. Together, these choices create prior-corpus misalignment: a mismatch between model priors and the target filings' s...
  </details>

- **2026-07-20** —  Supryadi,  Irfan,  Julianti et al. — [Pancasila-Dilemmas: Evaluating Large Language Models on Indonesian Human Value Dilemmas Grounded in Pancasila](http://arxiv.org/abs/2607.18066v1)
  <details><summary>📄 Abstract</summary>
  The value alignment of large language models (LLMs) is crucial for ensuring responses align with human intention and value preferences. However, most evaluations of value alignment focus on Western or universal values, while assessments grounded in the value systems of specific countries remain scarce. In this paper, we introduce Pancasila-Dilemmas, an evaluation dataset of 1,834 questions derived from Indonesian news, classified by 5 values of Pancasila: Religion, Humanity, Unity, Democracy, an...
  </details>

- **2026-07-20** — Kurt Godden — [L1 Augmented Attention as an Improved Vector Similarity Metric](http://arxiv.org/abs/2607.18027v1)
  <details><summary>📄 Abstract</summary>
  Scaled dot product attention conflates directional alignment and vector magnitude, limiting its effectiveness as a similarity metric in Transformer models. We introduce L1 augmented attention, a simple and computationally parallelizable modification that subtracts a learned, head specific L1 distance between queries and keys from the dot product score. This hybrid similarity captures complementary geometric information. Dot product rewards directional alignment, while L1 penalizes coordinate dev...
  </details>

- **2026-07-20** — Jiahe Fan, Yinghao Hou, Si Chen et al. — [Rethinking Heterogeneous LLM Merging: A Weighted Model Averaging Perspective](http://arxiv.org/abs/2607.18026v1)
  <details><summary>📄 Abstract</summary>
  Can large language models with substantially different parameter spaces be merged by direct weighted averaging, without training or semantic alignment? Existing heterogeneous fusion methods typically introduce distillation, adapters, learned latent spaces, routing, or feature alignment, leaving open whether a simpler recipe can work for genuinely different billion-parameter checkpoints. We revisit this counterintuitive question through training-free dimensional adaptation followed by ratio-contr...
  </details>

- **2026-07-20** — Saket Reddy, Andy Liu — [A Geometric Perspective on Stabilizing Value Conflict Resolution](http://arxiv.org/abs/2607.17946v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) often struggle to navigate value conflicts when trained with the compressed scalar rewards of Reinforcement Learning from Human Feedback (RLHF). To address this challenge, we investigate how chain-of-thought (CoT) reasoning can help improve performance in this domain. Geometrically, we show that CoT correlates with further smoothing the model's loss landscape in its sharpest direction, helping resolve the optimization instability of traditional scalar rewards. We als...
  </details>

- **2026-07-20** — Bas Meuwissen, Vasileios Tsouvalas, Nirvana Meratnia — [AutoEncoder-Compressed Parallel Split Learning for Pre-trained Model Fine-Tuning](http://arxiv.org/abs/2607.17913v1)
  <details><summary>📄 Abstract</summary>
  Distributed Fine-Tuning (DFT) of large-scale Foundation Models (FMs) on resource-constrained edge devices is limited by local compute constraints and communication overhead. Parallel Split Learning (PSL) reduces client-side computation by keeping few model layers on each client and offloading the remaining computation to the server; however, clients must exchange intermediate activations and gradients with the server at every training step. Existing SL communication-compression methods mainly re...
  </details>

- **2026-07-20** — Ghassen Baklouti, Omprakash Chakraborty, Jose Dolz et al. — [PRiSM: Prototype Regularization for Few-Shot VLMs](http://arxiv.org/abs/2607.17820v1)
  <details><summary>📄 Abstract</summary>
  Training-free few-shot adaptation methods have gained significant attention recently in the context of Vision-language Models (VLMs). Yet, current benchmarks rely on strong assumptions about the statistics of the adaptation data, e.g., class balance. We question these simplifying assumptions and introduce a more realistic benchmark that varies both the levels of class balance and the effective number of classes in few-shot tasks via Dirichlet sampling. Surprisingly, under our setting, we observe...
  </details>

- **2026-07-20** — Li Xian, Mingxi Li, Yizheng Wang et al. — [PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model](http://arxiv.org/abs/2607.17806v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Navigation (VLN) requires an embodied agent to interpret a natural-language instruction and predict actions from temporally ordered visual observations. Adapting a multimodal large language model to VLN requires visual-language alignment, compact temporal inputs, action-space grounding, and stable training on the target hardware. This technical report presents PGN (Pangu Navigator), an offline VLN action-prediction system built on OpenPangu-7B. Training proceeds in two stages. Fi...
  </details>

- **2026-07-20** — Zeyu Yang, Satoshi Nakamura — [When to Use Extra Context: Evidence-Grounded Terminology Adaptation for Simultaneous Speech Translation](http://arxiv.org/abs/2607.17766v1)
  <details><summary>📄 Abstract</summary>
  Extra context is valuable for simultaneous speech translation of technical talks, but injecting the entire document context into every streaming segment is often too coarse. Through diagnostic experiments, we find that context gains mainly come from paper-specific terminology recovery rather than uniform semantic enhancement. We therefore propose EGTA, an Evidence-Grounded Terminology Adaptation framework that builds a document terminology memory, selects compact candidate terms conditioned on t...
  </details>

- **2026-07-20** — Alessio Pitteri, Andrea Guizzo, Laura Ferrarotti et al. — [Ant swarm functional control via stigmergic Reinforcement Learning agents](http://arxiv.org/abs/2607.17709v1)
  <details><summary>📄 Abstract</summary>
  In this work, we propose a novel framework for the functional controllability of the ant swarm model, a well-known and relevant model of collective behaviour. Our approach introduces a population of controlling stigmergic agents, trained via Reinforcement Learning (RL), that act on the environment to influence the system dynamics and promote the emergence of ordered behaviour. Stigmergic agents are optimized in a centralized-training decentralized-execution setting, interacting with ants only th...
  </details>

- **2026-07-20** — Lingrui Li, Nan Pu, Dong Zhao et al. — [Memory-Supported Synergistic Adaptation for Training-Free Test-Time Medical Image Segmentation](http://arxiv.org/abs/2607.17693v1)
  <details><summary>📄 Abstract</summary>
  Test-time adaptation (TTA) aims to mitigate distribution shifts by adapting models with unlabeled target data at inference time. While TTA with vision-language models (VLMs) has shown promising results in classification, extending it to medical image segmentation remains challenging. In this setting, the adaptation gains from optimizing on VLM-generated predictions are often outweighed by the degradation to the VLM's strong pretrained features caused by noisy, update-driven learning, resulting i...
  </details>

- **2026-07-20** — Kseniia Vaniushkina, Jeongmin Lim, Jinyong Park — [GeneSpeak-FP: Target and Compound Retrieval from Observed Cell-Level Perturbation Signatures](http://arxiv.org/abs/2607.17671v1)
  <details><summary>📄 Abstract</summary>
  Large-scale single-cell perturbation atlases make it possible to ask an inverse question: given an observed transcriptional response, which annotated targets and compounds in a fixed library are most consistent with that response? We present \model, a Transformer retrieval model for this closed-library setting. Each input is a cell-level perturbation signature formed by contrasting one treated cell with a cell-line-specific mean DMSO reference. The encoder maps the signature to a target-retrieva...
  </details>

- **2026-07-20** — Wenxiao Fan, Hang Yin, Kan Li — [OrientSAM: Mitigating Camera-Centric Shortcut in Multimodal Spatial Reasoning via Orientation-Aware Spatial Alignment](http://arxiv.org/abs/2607.17657v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) still struggle with spatial reasoning that requires perspective transformation. In particular, they often rely on camera-centric cues rather than reasoning from the reference object's viewpoint, leading to systematic errors in non-camera reference settings. In this paper, we first analyze this failure mode and show that object orientation is a key factor underlying such camera-centric shortcut behavior. To address this issue, we propose OrientSAM, an orie...
  </details>

- **2026-07-20** — Kristoffer Christensen, Bo Nørregaard Jørgensen, Zheng Grace Ma — [A Digital Twin-Based Method for Evaluating Local Collective Tariffs in Distribution-Level Energy Systems](http://arxiv.org/abs/2607.17640v1)
  <details><summary>📄 Abstract</summary>
  This work addresses the need for engineering-grounded evaluation of implement-ed tariff mechanisms in distribution-level energy systems. A digital twin-based method is proposed for assessing local collective tariffs under realistic behavioral and infrastructural conditions. The approach integrates agent-based modeling of household consumption and generation, virtual aggregation through a shared metering abstraction, and explicit representation of tariff logic within a unified simulation environm...
  </details>

- **2026-07-20** — Ali Boudaghi, Hadi Zare — [FlowSonic: Stable Zero-Shot Music Editing via High-Order Trajectory Integration](http://arxiv.org/abs/2607.17526v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot text-guided editing of real-world music recordings requires balancing semantic modification with faithful preservation of the original musical structure. Although recent diffusion transformers trained with rectified flow have achieved remarkable success in text-to-music generation, extending them to edit existing recordings remains challenging because editing requires accurate deterministic inversion, reliable structural preservation, and numerically stable integration throughout the i...
  </details>

- **2026-07-20** — Tianzhu Ye, Li Dong, Guanheng Chen et al. — [LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks](http://arxiv.org/abs/2607.18110v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) on open-ended tasks compresses an LLM's rubric-based evaluation into a scalar reward, discarding rich textual feedback and conflating responses with distinct quality profiles. We propose Experiential Learning (EL), which repurposes the feedback model from an LLM-as-a-Judge into an LLM-as-a-Coach. The coach distills its assessment of each on-policy response into transferable experiential knowledge, which conditions a teacher model and is internalized by the policy thro...
  </details>

- **2026-07-19** — Yuejia Dou, Hesong Wang, Xinyu Zhang et al. — [AIGB-R1: Self-Evolving Generative Auto-Bidding via Hierarchical Planner-Executor Optimization](http://arxiv.org/abs/2607.17281v1)
  <details><summary>📄 Abstract</summary>
  Auto-bidding plays an essential role in online advertising, automatically adjusting bids for advertisers to optimize their commercial goals. The emerging AI-Generated Bidding (AIGB) paradigm widely adopts generative modeling to optimize bidding strategies, yet suffers from the limited mode coverage of offline datasets and inadequate task-state understanding, hindering effective exploration of optimal strategies. Large Language Models (LLMs), with prior world knowledge and reasoning capabilities,...
  </details>

- **2026-07-19** — Chen Wang, Zhaochun Li, Jionghao Bai et al. — [Distilled Reinforcement Learning for LLM Post-training](http://arxiv.org/abs/2607.17247v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) post-training is essential for improving reasoning, adaptation, and alignment. Existing methods mainly follow two paradigms: reinforcement learning (RL) and on-policy distillation (OPD). However, RL relies on coarse-grained outcome supervision, resulting in difficult credit assignment and limited capability to acquire new knowledge. OPD, meanwhile, unconditionally matches teacher logits through KL divergence, which creates a dilemma: similar teachers provide little new...
  </details>

- **2026-07-19** — Diyari Mohammed Salih, Lingxiang Hu, Naima AitOufroukh-Mammar et al. — [VIDAR: Visual-Inertial Dense Alignment and Reconstruction via a Geometric Foundation Model](http://arxiv.org/abs/2607.17171v1)
  <details><summary>📄 Abstract</summary>
  Monocular foundation models provide dense geometry but usually lack a stable metric scale. This paper presents VIDAR, a visual-inertial dense reconstruction framework that couples SVO+IMU odometry with Depth Anything 3. VIDAR uses the visual-inertial front end as a metric anchor: it provides camera poses, scale, and a consistent world frame for aligning dense foundation-model predictions across time. The foundation model then contributes detailed local geometry that is fused into a global recons...
  </details>

- **2026-07-19** — Ye Wang, Hongjun Wang, Hao Fang et al. — [STBridge: Shared-Target Alignment for Bridging Understanding and Generation in UMMs](http://arxiv.org/abs/2607.17140v1)
  <details><summary>📄 Abstract</summary>
  Unified multimodal models (UMMs) aim to integrate visual understanding and generation within a single architecture, but architectural unification alone does not ensure semantic consistency. A model may describe the intended target correctly while generating an inconsistent edit. This exposes an understanding-generation alignment gap: linguistic and visual outputs live in different spaces, yet should be governed by the same target semantics. We study this gap in image editing, where an instructio...
  </details>

- **2026-07-19** — Yuxuan Chen, Brook Du — [DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation](http://arxiv.org/abs/2607.17058v1)
  <details><summary>📄 Abstract</summary>
  Precise metric depth estimation is fundamental for autonomous robot navigation, yet monocular systems inherently suffer from scale ambiguity and scale drift. While recent recurrent flow-based SLAM systems have demonstrated state-of-the-art robustness, they remain scale-ambiguous. In this paper, we propose Metric-DROID, an end-to-end recurrent architecture that anchors visual SLAM to physical reality by integrating proprioceptive odometry. Our framework introduces the following innovations: (1) A...
  </details>

- **2026-07-18** — Nikolaos Stathoulopoulos, George Nikolakopoulos — [InLiER: Learning-Free Heterogeneous LiDAR Place Recognition via Intermediate Mixed-Radix Structural Keypoint Tokenization](http://arxiv.org/abs/2607.16862v1)
  <details><summary>📄 Abstract</summary>
  LiDAR place recognition supports loop closure, relocalization, and multi-agent map management. As robotic platforms increasingly combine LiDARs with different fields of view, resolutions, and scanning patterns, existing descriptors degrade because they are tightly coupled to sensor-specific characteristics. We present InLiER, a learning-free pipeline based on an intermediate tokenization step. Height-sliced keypoints from structural elements receive mixed-radix token IDs encoding height, radial ...
  </details>

- **2026-07-18** — Pengxu Chen, Yao Zhu, Guangming Zhu et al. — [Look Clearly Before Answering: Mitigating Hallucinations in LVLMs via Saliency-Driven Perceptual Realignment](http://arxiv.org/abs/2607.16841v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have demonstrated remarkable capabilities in multimodal understanding. However, they remain prone to hallucinations, generating responses that are inconsistent with the visual evidence. Existing mitigation methods largely address language-prior bias or cross-modal imbalance, while progressive visual degradation across perception and memory remains underexplored. In this work, we propose Saliency-Driven Perceptual Realignment (SDPR), a training-free framework ...
  </details>

- **2026-07-18** — Hyunjun Shin, Jiseung Jang, Jaewoo Maeng et al. — [Technical Report: AI-Assisted Gated DeltaNet Optimization on NVIDIA Blackwell](http://arxiv.org/abs/2607.16831v1)
  <details><summary>📄 Abstract</summary>
  AI-assisted GPU programming is often framed as a kernel-generation loop: ask a model to produce faster CUDA code, benchmark the result, and repeat. This case study argues that contest-grade optimization involves more than improving the kernel body. We examine the Agent-Assisted submission by our team, MSInfer, to the MLSys 2026 FlashInfer Contest. The submission optimized Gated DeltaNet decode and prefill on NVIDIA B200/Blackwell and achieved an official $1.58\times$ speedup, with approximate av...
  </details>

- **2026-07-18** — Cheng-Yao Hong, Yifan Wang, Yuewei Lin et al. — [Test-Time Registers as Global Priors for Tokenized Image Generation](http://arxiv.org/abs/2607.16824v1)
  <details><summary>📄 Abstract</summary>
  Attention-based models often develop attention sinks, where a small number of tokens repeatedly attract attention and accumulate unusually large activations. In vision transformers, these outliers are closely related to registers, which have been diagnostically linked to global, low-frequency image structure. Existing work has largely studied registers through interpretability analyses and linear probes, leaving open whether they can be operationalized as plug-and-play signals for generation wit...
  </details>

- **2026-07-17** — Harine Choi, Eun Hak Lee, Zhengzhong Tu — [Vision-Language Assistant for Emotional Reactions to Risky Driving](http://arxiv.org/abs/2607.16181v1)
  <details><summary>📄 Abstract</summary>
  This study introduces a vision-language pipeline that detects risky driving behaviors and generates emotionally expressive responses to support driver awareness and comfort. Although vision-language models have advanced perception and reasoning in autonomous driving, existing systems rarely consider the emotional dimension or real-world user experience. Keep Yelling Assistant (KYA) detects high-risk driving maneuvers in real time, such as sudden cut-ins. It then produces emotional responses thro...
  </details>

- **2026-07-17** — Ingo Ziegler, Martin Krebs, Desmond Elliott — [Rate-Utility Frontiers for Language Encodings: Comparing Tokens, Bytes, and Pixels Under Controlled Linguistic Content](http://arxiv.org/abs/2607.16117v1)
  <details><summary>📄 Abstract</summary>
  Language models encode text as subword tokens, raw bytes, or rendered pixels, but these encodings are usually compared under modeling constraints that expose different amounts of linguistic content to models across different languages. We instead ask what each encoding preserves when both the content and the downstream capacity are controlled. Using verified parallel sentences across thirteen languages and five scripts, we compare tokens, bytes, and pixels through a shared bottleneck whose width...
  </details>

- **2026-07-17** — Sreyan Ghosh, Arushi Goel, Kaousheik Jayakumar et al. — [Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos](http://arxiv.org/abs/2607.16107v1)
  <details><summary>📄 Abstract</summary>
  We present Audio-Visual Flamingo (AV-Flamingo), a fully open state-of-the-art audio-visual large language model (AV-LLM) for joint understanding and reasoning over audio, images, and long-form videos. Unlike prior AV-LLMs that primarily focus on short clips, AV-Flamingo is designed for understanding and reasoning over long and complex real-world (audio-visual) videos. To support this, we make three key contributions: (i) Audio-Visual-Skills, a large-scale collection of real-world videos with ~7M...
  </details>

- **2026-07-17** — Xinran Liu, Yuwen Li, Hongxiang Gao et al. — [Knowledge-Guided Cross-Modal Fusion for Adult-to-Pediatric ECG Transfer via Label-Conditioned Contrastive Alignment](http://arxiv.org/abs/2607.15928v1)
  <details><summary>📄 Abstract</summary>
  Adult and pediatric electrocardiogram (ECG) interpretation relies on age-sensitive criteria, and models pretrained mainly on adult ECGs often transfer poorly to pediatric populations when pediatric labels are scarce. Existing multimodal ECG--text methods typically align waveforms and text at the global sample level, entangling evidence from co-occurring diagnoses and limiting transfer under this gap. We propose Pediatric-Adult ECG Alignment via Cross-modal Enhancement (PEACE), a knowledge-guided...
  </details>

- **2026-07-17** — K. Prikhodko, S. Kuznetsov, S. Vorobey et al. — [Precision positioning in free-space optical communication systems via PID control tuned by RL](http://arxiv.org/abs/2607.15910v1)
  <details><summary>📄 Abstract</summary>
  Accurate positioning of optical components is essential for maintaining beam alignment in free-space optical (FSO) communication systems. This work investigates reinforcement-learning-assisted tuning of cascaded position and velocity PID controllers for an optical deflector that moves the end of an optical fiber in the focal plane of an optical system. A Deep Deterministic Policy Gradient (DDPG) agent adjusts six PID coefficients through interaction with a physical experimental stand. The stand ...
  </details>

- **2026-07-17** — Kengo Hirata, Takeshi Tsukada — [Programming with Quantum-Controlled Quantum Channels](http://arxiv.org/abs/2607.15873v1)
  <details><summary>📄 Abstract</summary>
  In contrast to a classical bit, which can only take the value $0$ or $1$, its quantum counterpart -- a qubit -- can exist in a superposition of $0$ and $1$. This is a superposition of data values, naturally raising the question of whether one can superpose not only data but also programs. For example, a particular superposition of programs, known as the quantum SWITCH, has attracted much attention, and its implementations and computational advantages have been studied extensively within the phys...
  </details>

- **2026-07-17** — Zhengyang Zhuge, Hao Yu, Xin Wang et al. — [QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](http://arxiv.org/abs/2607.15810v1)
  <details><summary>📄 Abstract</summary>
  Rollout generation is a major bottleneck in Reinforcement Learning (RL) for Mixture-of-Experts (MoE) Large Language Models, motivating low-precision rollout acceleration such as FP8. As an emerging low-precision format, NVFP4 combines fine-grained scaling for accuracy preservation with native W4A4 FP4 GEMMs for higher throughput than FP8. However, we find that directly applying NVFP4 to MoE RL rollout is impractical. NVFP4 rollout with BF16 training collapses after roughly 150 steps, accompanied...
  </details>

- **2026-07-17** — Bo-An Chang, Yu-Chih Chen — [Debiasing Text-to-Image Evaluation via Implicit Cultural Alignment Reward Modeling](http://arxiv.org/abs/2607.15740v1)
  <details><summary>📄 Abstract</summary>
  As Text-to-Image (T2I) systems rapidly advance, evaluating the cultural authenticity of synthesized content has become increasingly important for fair and trustworthy generative AI. Existing T2I evaluation metrics and multimodal judges often rely on visual-semantic representations that underrepresent implicit cultural norms, leading to biased preference judgments and the omission of fine-grained cultural cues. In addition, visual question answering (VQA)-based evaluators typically depend on auto...
  </details>

- **2026-07-17** — Jian Huang, Haotian Shen, Xinhao Lou et al. — [Event3R: Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-Temporal Feature Aggregation](http://arxiv.org/abs/2607.15727v1)
  <details><summary>📄 Abstract</summary>
  Robust 3D reconstruction is essential for robotics and embodied perception. Recent feed-forward approaches such as DUSt3R have demonstrated impressive progress in dense 3D reconstruction from RGB images, achieving global geometric consistency and strong generalization. However, extending such dense 3D reconstruction to event cameras remains challenging due to their asynchronous, sparse, and highly dynamic nature, as well as the lack of large-scale, well-labeled datasets. In this work, we introdu...
  </details>

- **2026-07-17** — Jiahao Zhao, Junyi Liu, Lifeng Xu et al. — [S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding, Prediction, and Generation](http://arxiv.org/abs/2607.15686v1)
  <details><summary>📄 Abstract</summary>
  We present S1-Omni, a unified multimodal reasoning model for scientific understanding, prediction, and generation. AI for Science (AI4S) has advanced significantly through domain-specific models, tool-augmented LLMs, and scientific language models. However, model capabilities remain highly fragmented, limiting the joint modeling of heterogeneous data, scientific laws, and expert knowledge. S1-Omni addresses this gap by consolidating these capabilities into a single, coherent scientific reasoning...
  </details>

- **2026-07-17** — Lichao Mou, Shilan Zhang, Chunlei Li et al. — [Model Merging for Medical LVLMs: A Benchmark and a Winner-Take-All Approach](http://arxiv.org/abs/2607.15661v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) can be adapted to specialized medical imaging tasks via parameter-efficient fine-tuning approaches such as low-rank adaptation (LoRA), leading to a growing ecosystem of expert models tailored to specific imaging modalities and clinical scenarios. However, deploying multiple expert LVLMs in practice incurs substantial computational and operational overhead. Model merging provides a promising solution by consolidating multiple experts into a single model withou...
  </details>

- **2026-07-17** — Jung-Hee Kim, Xiaoming Liu — [Geometric Distillation from Rectified Stereo: Leveraging Epipolar Cues for Monocular Depth](http://arxiv.org/abs/2607.15600v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth foundation models have demonstrated remarkable generalization capabilities across diverse environments. However, they continue to struggle with metric depth estimation in diverse environments. This limitation stems from the inherent scale ambiguity of single-view inference, leading to misaligned scale predictions even when the relative geometry is accurate. Conversely, recent multi-view foundation models leverage cross-view cues to learn robust scene-level geometry and consistent...
  </details>

- **2026-07-17** — Xu Hou, Meiyu Liang, Wei Huang et al. — [MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts for Multimodal Knowledge Graph Completion](http://arxiv.org/abs/2607.15592v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Knowledge Graph Completion (MKGC) requires inferring missing entities from structural, textual, and visual cues. Existing diffusion-based MKGC methods usually denoise directly on raw multimodal features. Such a design forces the denoiser to simultaneously perform relation-dependent cue selection, cross-modal semantic alignment, and structure-aware entity generation, which introduces noisy and semantically inconsistent conditions for diffusion and consequently leads to suboptimal compl...
  </details>

- **2026-07-17** — Chu Zhao, Lei Tang, Minghang Li et al. — [PCTD: Preference-Guided Counterfactual Task Decomposition for Agent Tool Retrieval](http://arxiv.org/abs/2607.15696v1)
  <details><summary>📄 Abstract</summary>
  Task decomposition aims to transform ambiguous instructions into executable atomic subtasks, thereby guiding high-precision tool retrieval. However, our analysis reveals that directly adopting tool retrieval metrics, i.e., Recall or NDCG, as rewards for task decomposition can easily induce reward hacking in reinforcement learning-based methods. Specifically, models tend to maximize retrieval matching through strategies such as repetitive decomposition. This spurious correlation between the shall...
  </details>

- **2026-07-17** — Navya Gupta, Bingjie Xu, Avinash Anand et al. — [How Do VLMs Fail? Vision-Operation Misalignment in Compositional VQA](http://arxiv.org/abs/2607.16094v1)
  <details><summary>📄 Abstract</summary>
  Compositional visual question answering requires Vision-Language Models (VLMs) to execute multiple reasoning operations like object selection, spatial relation resolution, and attribute verification. Despite strong aggregate performance, the mechanistic basis of VLM failures on this task remains underexplored. To address this gap, we analyze vision-operation misalignment in VLMs by examining how failures relate to specific reasoning operations and the internal computational pathways through whic...
  </details>

- **2026-07-15** — Sai Srikanth Madugula, Peplluis Esteva de la Rosa, Daya Shankar — [The Dynamic Verifiable Multi-Agent Human Agentic Loyalty Loop (DVM-HALL) Model and the Net Human-Agent Score (NHAS) in Autonomous Commerce](http://arxiv.org/abs/2607.13998v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of Agentic Artificial Intelligence fundamentally disrupts traditional customer loyalty paradigms. As AI evolves from passive recommendation algorithms to autonomous, goal-directed agents capable of executing purchasing decisions, the conventional understanding of consumer-brand relationships requires a structural reevaluation. By synthesizing extant literature across human-machine teaming, consumer decision-making, and algorithmic trust dynamics, we demonstrate that tradi...
  </details>

- **2026-07-15** — Zhihao Xie, Junfeng Wu, Xinting Hu et al. — [VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders](http://arxiv.org/abs/2607.14088v1)
  <details><summary>📄 Abstract</summary>
  Video generative models commonly rely on latent spaces learned by 3D Variational Autoencoders (3D-VAEs). However, conventional 3D-VAEs are mainly optimized for pixel-level reconstruction, which can limit the semantic and spatio-temporal structure captured by their latents. Meanwhile, Video Foundation Models (VFMs) such as V-JEPA 2 and VideoMAEv2 show strong video understanding capabilities, yet whether their frozen representations can be transformed into compact, reconstruction-capable, and gene...
  </details>

- **2026-07-15** — Shunbao Li, Zhipeng Yuan, Amoako Ofori et al. — [Pezego-HITL: A policy-grounded large language model architecture for agricultural extension in Ghana](http://arxiv.org/abs/2607.13934v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed in agricultural decision-support settings, yet high-stakes crop protection in smallholder agriculture requires more than output-quality benchmarks. Over a two-year design and evaluation programme, we formalise policy-constrained large language model assessment as an adaptive compute allocation problem that jointly captures safety compliance, helpfulness, operational latency, and expert supervision workload. We introduce P-EVAL (Policy-grounded Expe...
  </details>

- **2026-07-15** — Cheng Tang, Junzhi Ning, Min Cen et al. — [SIVA-RL: Sensitivity-Invariance Visual Alignment for Multimodal Reinforcement Learning](http://arxiv.org/abs/2607.13931v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) drives multimodal reasoning, but answer-level correctness does not guarantee that a vision-language model grounds its predictions in visual evidence. Existing visual-intervention methods contrast policy behavior on original and modified images, yet assign supervision by the type of intervention rather than its observed effect. This assumption fails: identical operators produce heterogeneous outcomes across samples. We propose SIVA-RL, a Sensi...
  </details>

- **2026-07-15** — Zhixiao Zheng, Zheren Fu, Zhiyuan Yao et al. — [Groc-PO: Grounded Context Preference Optimization for Truthful Multimodal LLMs](http://arxiv.org/abs/2607.13712v1)
  <details><summary>📄 Abstract</summary>
  Despite the rapid progress of Multimodal Large Language Models (MLLMs), they still suffer from untruthfulness issues, such as visual hallucinations, content fabrication, and unfaithful reasoning, which substantially undermine their faithfulness and practical utility. Alignment methods based on human preference, such as Direct Preference Optimization (DPO), have been widely adopted to address these issues. However, multimodal reasoning errors often propagate across stages, and final-answer errors...
  </details>

- **2026-07-15** — Zehan Liu, Yage He, Xianwu Gong — [WAVE-Stereo: Warp-Aligned Volume Encoding for Stereo Matching](http://arxiv.org/abs/2607.13674v1)
  <details><summary>📄 Abstract</summary>
  Existing iterative stereo matching methods primarily adopt two types of correspondence representation: explicit matching search via correlation volumes and local residual refinement via warped features, yet the two remain separately modeled. We propose WAVE-Stereo, built on a core insight: correlation volumes and feature warping provide complementary matching cues. \textbf{GeoWarp Correspondence Encoder (GWCE)} encodes matching search, residual alignment, and disparity prior in parallel at the C...
  </details>

- **2026-07-15** — Yongqiang Chen, Guangyi Chen, Yuewen Sun et al. — [Analogical Deep Research: Retrieving and Integrating Historical Analogies for Foresight Analysis](http://arxiv.org/abs/2607.13602v1)
  <details><summary>📄 Abstract</summary>
  Systematic comparisons between current situations and structurally similar past events in the historical, i.e., historical analogies, is among the most powerful tools for foresight analysis. In this work, we present a new task called Analogical Deep Research (ADR) to Large Language Model (LLM) agents and construct the first ADR benchmark ADR-bench to study whether LLM agents are able to find and leverage historical analogies when doing foresight analysis. Our investigation reveals a key obstacle...
  </details>

- **2026-07-15** — Yuan Xiao, Can Wang, Xiangyu Kong et al. — [ThinkBLOX: 3D Indoor Scene Generation with Progressive Reasoning](http://arxiv.org/abs/2607.13539v1)
  <details><summary>📄 Abstract</summary>
  While traditional graphics methods often synthesize 3D indoor scenes autoregressively or hierarchically, recent vision-language model (VLM)-based generators predominantly adopt a one-shot paradigm where the full layout is planned at once. This one-shot approach often requires global re-optimization or complete reconstruction during interactive editing (e.g., inserting or moving objects) and can lead to physically or semantically poorly organized arrangements. To address these challenges, we prop...
  </details>

- **2026-07-15** — Shuzhen Li, Yifan Zhang, Jiacheng Guo et al. — [DeepLoop: Depth Scaling for Looped Transformers](http://arxiv.org/abs/2607.13491v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers scale sequential computation by applying a compact stack of physical blocks for multiple rounds, increasing unrolled depth without increasing stored parameters. This reuse changes the residual-scaling problem: in an untied Transformer, each residual branch receives and applies its own parameter update, whereas in a looped Transformer one shared update aggregates gradients from repeated visits and is read back by those same visits in the next linearized forward pass. We formal...
  </details>

- **2026-07-15** — Xinhao Cai, Yixuan Sun, Minghang Zheng et al. — [Music-to-Dance Generation via Atomic Movements](http://arxiv.org/abs/2607.13978v1)
  <details><summary>📄 Abstract</summary>
  Music-driven dance generation aims to produce human motion that is both rhythmically synchronized and semantically consistent with music. While recent neural approaches have achieved impressive visual realism, they typically model motion as a continuous signal and neglect its compositional nature, making generated dances structurally incoherent and difficult to control. In this work, we introduce a structure-aware framework that models choreography as a sequence of atomic movements-semantically ...
  </details>

- **2026-07-15** — Chenyang Zhao, Wei Lin, Antoni B. Chan et al. — [Fine-grained CLIP fine-tuning with self-annotated region alignment](http://arxiv.org/abs/2607.13661v1)
  <details><summary>📄 Abstract</summary>
  Contrastive Language-Image Pre-training (CLIP) has been shown to have limitations in its fine-grained dense feature representation, due to its pre-training focusing on matching the whole image to a text description. Considering the large data and computational burden in pre-training a vision-language model from scratch, a series of works aim to enhance the fine-grained ability of CLIP through a fine-tuning scheme. However, existing works suffer from a variety of limitations: additional region an...
  </details>

- **2026-07-15** — Celeste Veronese, Edoardo Zorzi, Daniele Meli et al. — [Explaining Reinforcement Learning Agents via Inductive Logic Programming](http://arxiv.org/abs/2607.13655v1)
  <details><summary>📄 Abstract</summary>
  Explainable Reinforcement Learning (XRL) seeks to make Reinforcement Learning (RL) policies more transparent and interpretable, a key requirement in safety-critical and human-centric scenarios. However, it is mostly based on user studies, thus targeting the needs of a specific audience and lacking shared evaluation metrics. On the other hand, logic-based approaches within eXplainable Artificial Intelligence (XAI) provide compact, human-readable abstractions of decision-making. However, the syste...
  </details>

- **2026-07-15** — Ayan Igali, Pakizar Shamoi — [Beyond Color Geometry: Evaluating Human-Like Color Representations in Vision Models](http://arxiv.org/abs/2607.13647v1)
  <details><summary>📄 Abstract</summary>
  Do vision models see colors the way humans do? Existing evaluations of color representations usually compare them with geometric spaces such as CIELAB or with discrete color labels. These references capture perceptual distance or category membership, but not the graded way in which people organize colors. We evaluate color grounding against a fuzzy perceptual model with 86 graded categories fitted to human survey data. The framework can be applied to any image encoder and measures three compleme...
  </details>

- **2026-07-15** — Hao Li, Han Fang, Zixin Pan et al. — [GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding](http://arxiv.org/abs/2607.13454v1)
  <details><summary>📄 Abstract</summary>
  Although multimodal large language models (MLLMs) have achieved remarkable progress, understanding 3D spatial relationships from 2D images remains a critical challenge. Existing methods primarily rely on symbolic text tokens, which inherently lack the fidelity to represent continuous geometric information. While recent methods use latent representations to enhance reasoning, relying on a single latent type cannot adapt to the diversity of spatial tasks, leading to misalignment in complex geometr...
  </details>

- **2026-07-15** — Xi Yang, Guodong Liu, Chuqin Li et al. — [Exploring Post-Training Alignment of Small Language Models for Biomedical Data-to-Text Generation: A Case Study of Medication Leaflet](http://arxiv.org/abs/2607.13430v1)
  <details><summary>📄 Abstract</summary>
  Translating complex biomedical data into patient-friendly narratives is central to modern biomedical informatics. This study presents a comparative analysis of training small language models (SLMs) in specialized biomedical datato-text generation tasks. We explore widely adopted post-training methods including supervised fine-tuning (SFT), direct preference optimization (DPO), odds ratio preference optimization (ORPO), and group relative policy optimization (GRPO) with Qwen-based SLMs on a medic...
  </details>

- **2026-07-15** — Dwip Dalal, Shivansh Patel, Chahit Jain et al. — [Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](http://arxiv.org/abs/2607.13429v1)
  <details><summary>📄 Abstract</summary>
  Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior cloning (BC) has become the standard recipe for vision-language-action (VLA) policies. However, BC finetuning progressively overwrites the pretrained representations that support visual and semantic generalization. Co-training on web image-text data, a common remedy, does not prevent this; it applies language and action losses to separate observations, leaving VLAs with language-action misalignment that stan...
  </details>

- **2026-07-14** — Jiaying Lin, Seongho Son, Nam Phuong Tran et al. — [Meta-Learning Preferences for Multilingual LLM Alignment](http://arxiv.org/abs/2607.13315v1)
  <details><summary>📄 Abstract</summary>
  Unequal availability of human preference data across languages poses a significant challenge for aligning large language models in multilingual settings. To address the lack of sufficient data in low-resource language alignment, we propose a meta-learning framework for Reinforcement Learning from Human Feedback and Direct Preference Optimization. By leveraging preference data from other languages, our framework learns a transferable initialization that enables effective adaptation to a target la...
  </details>

- **2026-07-14** — Yuhong Fu, Weixing Zhang, Bowen Jiang et al. — [Can LLMs Learn and Apply Multi-Level Modelling Semantics? A First Empirical Study](http://arxiv.org/abs/2607.13257v1)
  <details><summary>📄 Abstract</summary>
  Industry 5.0 emphasises human-centric industrial system design, placing additional demands on modelling tools. Multi-level modelling (MLM) can directly represent three or more abstraction levels, but this comes at the cost of more complex semantic constraints that model correctness depends on. Large Language Models (LLMs) have been increasingly studied in model-driven engineering, but this evidence rests entirely on two-level modelling tasks, and whether it generalises to MLM, whose semantics di...
  </details>

- **2026-07-14** — Jonas Ehrhardt, René Heesch, Oliver Niggemann — [Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action Markov Decision Processes](http://arxiv.org/abs/2607.12924v2)
  <details><summary>📄 Abstract</summary>
  In this paper, we study Reinforcement Learning in Parametrized Action Markov Decision Processes (PAMDP), where each decision consists of a symbolic action and numerical parameters. In such settings Reinforcement Learning algorithms typically determine parameters with one-shot estimators, which makes their training sample inefficient. Though in most PAMDP environments explicit but incomplete knowledge (e.g., rules, safety constraints, or expert heuristics) is available, it is rarely directly used...
  </details>

- **2026-07-14** — Hanhua Hong, Yizhi Li, Jiaoyan Chen et al. — [Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction](http://arxiv.org/abs/2607.12835v1)
  <details><summary>📄 Abstract</summary>
  Rubric-based evaluation is a promising approach for assessing open-ended outputs from LLM-based research agents, particularly in paper reproduction, where direct paper-to-repository comparison is prone to hallucination. However, constructing paper-specific rubrics requires substantial expert effort, limiting the scalability of benchmarks such as PaperBench. In this work, we present, to our knowledge, the first systematic meta-evaluation of LLM-generated rubrics for paper reproduction. We reformu...
  </details>

- **2026-07-14** — Taizo Suzuki, Soma Yokota, Masaki Onuki — [Spatially-Aligned Chroma from Luma Prediction for Lossless JPEG XS Raw Image Compression](http://arxiv.org/abs/2607.12636v1)
  <details><summary>📄 Abstract</summary>
  This study proposes a Chroma from Luma (CfL)-enhanced Star-Tetrix transform (STT), referred to as CfL-STT, for improving raw image compression in JPEG XS. The proposed CfL-STT integrates CfL prediction into the STT to predict chroma components from the luma component in CFA-sampled raw images. Unlike conventional CfL prediction designed for full-color images, the proposed method employs spatially aligned luma samples obtained via linear interpolation along the horizontal and vertical directions ...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 97 papers

- **2026-07-20** — Kevin Du, Clara Kümpel, Michelle Wastl et al. — [It's Not What You Say, It's How You Say It: Evaluating LLM Responses to Expressions of Belief](http://arxiv.org/abs/2607.18232v1)
  <details><summary>📄 Abstract</summary>
  Users frequently express their beliefs to large language models (LLMs). In some situations, the LLM should accept these contextual beliefs as true. In others, they should stick to their prior knowledge. Notably, users' expressions of belief (EoBs) can take linguistically diverse forms - using presuppositions, evidential and certainty markers, or varied tones - each of which may have a different persuasiveness over the LLMs. We introduce a typology to systematically evaluate how different EoBs af...
  </details>

- **2026-07-20** — Ao Zhang, Tian Zhang, Antonio Cammi et al. — [Physics-Guided Spectral Parametric Reduced-Order Modeling for Transient Prediction of Controlled Dynamical Systems](http://arxiv.org/abs/2607.18133v1)
  <details><summary>📄 Abstract</summary>
  Efficient parametric transient prediction at unseen parameter values and under new operating conditions remains challenging because repeated high-fidelity simulations are computationally prohibitive. Existing data-driven surrogates and parametric reduced-order models perform well within sampled ranges but often lose reliability beyond them. This study proposes a physics-guided spectral parametric reduced-order modeling framework for controlled dynamical systems. Parameter-dependent reduced spect...
  </details>

- **2026-07-20** — Koyar Afrasyab — [Judge-dependent safety gains and model-specific helpfulness costs of evidence-sufficiency prompting in clinical LLMs](http://arxiv.org/abs/2607.18086v1)
  <details><summary>📄 Abstract</summary>
  Background: LLM judges increasingly score whether clinical language models give overconfident answers under incomplete evidence, yet whether a measured "safety gain" reflects real behavior change or the judge's calibration is unresolved. Using a structured evidence-sufficiency prompt as a test case, we asked whether it reduces unsafe overconfident answers, how far that effect depends on the scoring judge, and what it costs in helpfulness.   Methods: In a retrospective public-data benchmark (Real...
  </details>

- **2026-07-20** — Ali AbuSaleh, Leon Hammerla, Alexander Mehler — [Learning to Detect Cross-Modal Negation: An Analysis of Latent Representations and an Attention-Based Solution](http://arxiv.org/abs/2607.17712v1)
  <details><summary>📄 Abstract</summary>
  Detecting high-level semantic concepts like negation across modalities remains a challenge for current multimodal systems. We analyze this as a fundamental representation learning problem, providing the first evidence that negation does not form a linearly or non-linearly separable class in the latent spaces of standard vision-language models (VLMs). We demonstrate that pretrained embeddings primarily encode modality-specific features, lacking a generalizable negation signal. To overcome this, w...
  </details>

- **2026-07-20** — Amir Hosein Fadaei, Mahyar Maleki, Mohammad-Reza A. Dehaqani — [Brain-Aligned Multi-Stream Video Transformers with Sparse Self-Selection](http://arxiv.org/abs/2607.17625v1)
  <details><summary>📄 Abstract</summary>
  Modern video transformers typically ignore principles from primate vision and are rarely evaluated against neural data, limiting their biological interpretability. We introduce a sparse winner-takes-all token selection module that replaces dense self-attention to improve efficiency and approximate competitive routing observed in biological visual circuits. We further propose a neuro-inspired split-and-fuse video transformer which uses two complementary pathways: a high-resolution, low-frame-rate...
  </details>

- **2026-07-20** — Yesol Park, Hye-Jung Yoon, Juno Kim et al. — [DA-Fusion: Deformable Attention-Based RGB-D Fusion Transformer for Unseen Object Instance Segmentation](http://arxiv.org/abs/2607.17754v1)
  <details><summary>📄 Abstract</summary>
  In logistics automation, precise segmentation of unseen objects is crucial for efficient robotic manipulation in cluttered environments. Tasks such as bin-picking and shelf-picking require robust perception to handle occlusions, varying object shapes, and complex spatial arrangements. Traditional RGB-based methods tend to over-segment objects due to their reliance on texture, while depth-based methods often under-segment by focusing primarily on geometric features. To address these limitations, ...
  </details>

- **2026-07-20** — Christina Nasika, Feng Wang, Antonis Krasakis et al. — [jina-reranker-v3.5: An Efficient Listwise Reranker with Hybrid Attention and Self-Distillation](http://arxiv.org/abs/2607.18152v1)
  <details><summary>📄 Abstract</summary>
  Listwise rerankers are the discriminative core of agentic retrieval pipelines, yet production deployment demands efficiency, domain robustness, and fluency on semi-structured data at the same time. We present jina-reranker-v3.5, a 0.6B-parameter listwise reranker that meets these demands together without sacrificing the cross-document comparison that makes its predecessor jina-reranker-v3 effective. jina-reranker-v3.5 keeps the last-but-not-late (LBNL) interaction of jina-reranker-v3 and reworks...
  </details>

- **2026-07-20** — Qiang Duan — [AI Agent Communications in AI-Native 6G Network: Status, Challenges and Opportunities](http://arxiv.org/abs/2607.18138v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of agentic AI and multi-agent systems is establishing AI agent communication as a fundamental requirement for the future Internet. While a diverse array of agent communication protocols has recently emerged, these solutions currently suffer from interoperability crises and infrastructure gaps. The newly proposed Service-Oriented Virtualization-Based Architecture (SOVA) offers an architectural framework to address these challenges for agent communication, which expects seaml...
  </details>

- **2026-07-20** — Wenbo Wei, Jun Wang, Shan Raza et al. — [Occlusion-Aware Panoptic Segmentation with Joint Position Embedding and Occlusion-Level Attention](http://arxiv.org/abs/2607.18112v1)
  <details><summary>📄 Abstract</summary>
  Panoptic segmentation in complex scenes remains challenging because of occlusions, yet modern approaches often neglect occlusion modelling. In this paper, we propose \textbf{P}osition \textbf{E}mbedding \textbf{M}odulation with \textbf{O}cclusion-\textbf{L}evel \textbf{A}ttention (PEMOLA), a novel occlusion-aware module that can be seamlessly integrated into transformer-based panoptic segmentation. To obtain occlusion cues, we train an occlusion classifier on the COCO-OLAC dataset. The classifie...
  </details>

- **2026-07-20** — Hailey Warner, Duncan Eddy, Shreya Parjan et al. — [Importance Sampling and PCA for Finding Failures in Commercial Autonomous Vehicles](http://arxiv.org/abs/2607.18106v1)
  <details><summary>📄 Abstract</summary>
  Methods for discovering rare failures in autonomous systems have so far been demonstrated almost exclusively in simulations with simple, academic driving stacks, leaving open whether they generalize to the more robust planners used in commercial systems. We address this gap by applying two rare-event discovery algorithms to a commercial autonomous trucking stack. Adaptive stress testing (AST) uses reinforcement learning to search for the most likely noise trajectories leading to a simulated coll...
  </details>

- **2026-07-20** — Jinbang Huang, Yuanzhao Hu, Zhiyuan Li et al. — [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](http://arxiv.org/abs/2607.18060v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robotic tasks require diverse capabilities that no single policy can reliably provide. Heterogeneous policies offer complementary strengths, but orchestrating them requires reasoning over uncertain capability boundaries and cross-policy distribution mismatch, which are largely overlooked by existing planning methods built on homogeneous, predefined skills with fixed applicability. We propose RoboHarness, a unified framework that encapsulates independently developed robot control sys...
  </details>

- **2026-07-20** — Kemal Devrim Kafadar, Eren Özaltun, Mahmud Efnan Şanlı et al. — [Value-Aware Prediction for Robust Multi-Agent Coordination Under Communication Loss](http://arxiv.org/abs/2607.17914v1)
  <details><summary>📄 Abstract</summary>
  Robust multi-agent coordination relies heavily on inter-agent communication, which is frequently disrupted by physical and environmental constraints in real-world deployments. To maintain operation during these intermittent communication failures, agents can employ internal prediction models to estimate missing shared state information. However, predictors trained with standard reconstruction objectives treat all transitions equally. In a Reinforcement Learning context, this forces the model to ...
  </details>

- **2026-07-20** — Kinga O. Mastej, Panyalak Detrattanawichai, Hyunsoo Park et al. — [Chemical filters for ultra-high-throughput materials screening and generation](http://arxiv.org/abs/2607.17910v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence is rapidly transforming materials design by enabling de novo exploration of immense chemical spaces. Yet a large proportion of AI-generated compositions remain implausible, violating established chemical principles, which limits the reliability and interpretability of generative materials design. Here, we introduce a chemical validity operator that recasts heuristic chemical rules as a configurable algorithmic prior for evaluating and guiding generative materia...
  </details>

- **2026-07-20** — Ganesh Senrayan, Moyuru Yamada, Ishan Jindal et al. — [Exploratory and Assimilating Reflection: Reflective Recall Cycle for Long-term Memory](http://arxiv.org/abs/2607.17879v1)
  <details><summary>📄 Abstract</summary>
  LLM-based autonomous agents require external memory to overcome their statelessness and limited context window for long-term interaction and dynamic knowledge reasoning. However, existing memory retrieval methods often lack adaptability and sample efficiency, and struggle to retrieve the right mixture of memories from heterogeneous stores. We propose Exploratory-Assimilating Reflection (EAR), a framework for high initial retrieval performance and sample-efficient adaptation. EAR combines two mec...
  </details>

- **2026-07-20** — Fernando López, Ana Ayala, Guillermo Segovia et al. — [ESCUCHA: A Spanish Speech Benchmark for Heterogeneous Acoustic Conditions](http://arxiv.org/abs/2607.17812v1)
  <details><summary>📄 Abstract</summary>
  As large audio language models (LALMs) advance, robust evaluation frameworks have become essential. In this context, Spanish speech understanding under realistic acoustic conditions has received particularly little attention. We introduce ESCUCHA, the first Spanish speech understanding benchmark designed to evaluate LALMs across heterogeneous acoustic conditions and reasoning abilities. ESCUCHA comprises 1,000 human-curated questions paired with audio, totaling 162.9 hours sourced directly ``fro...
  </details>

- **2026-07-20** — Moona Mazher, Abdul Qayyum, Steven A. Niederer et al. — [BrainNext: A General-Purpose Self-Supervised Foundation Model for Brain MRI Analysis](http://arxiv.org/abs/2607.17782v1)
  <details><summary>📄 Abstract</summary>
  Foundation models pretrained using self-supervised learning have transformed computer vision by learning transferable representations from large-scale unlabeled data. However, existing foundation models for neuroimaging remain limited by task-specific training, slice-based learning strategies, or relatively small pretraining datasets, restricting their generalizability across diverse brain MRI applications. In this work, we present BrainNext, a general-purpose self-supervised foundation model fo...
  </details>

- **2026-07-20** — Yitao Wu, Si Shen, Rui Yang et al. — [Verify, Repair, Repeat, or Stop? Robust Stopping for Noisy Verify-Repair Loops in LLM Agents](http://arxiv.org/abs/2607.17641v1)
  <details><summary>📄 Abstract</summary>
  Verify-repair loops are a standard means for large language model (LLM) agents to correct faulty plans in code generation, mathematical reasoning, and tool use. When both the verifier and the repairer are noisy, repair can damage already-correct plans, and reported acceptance keeps rising while true validity falls, so existing methods lack a principled basis for deciding when repair should stop. We propose VRR-Stop, a robust stopping framework for noisy verify-repair-repeat (VRR) loops. A four-p...
  </details>

- **2026-07-20** — Damien Teney, Liangze Jiang, Hemanth Saratchandran et al. — [Can Transformers Really Do It All? On the Compatibility of Inductive Biases Across Tasks](http://arxiv.org/abs/2607.17624v1)
  <details><summary>📄 Abstract</summary>
  Transformers are remarkably versatile and their design is largely consistent across a variety of applications. But are they optimal for any given task or dataset? The answer may be key for pushing AI beyond merely scaling current designs.   *Method.* We present a method to optimize a transformer architecture for a given dataset, which we use as a tool to study optimal task-specific inductive biases. This method replaces the most important non-linearities (GeLUs,;softmax) with functions learned o...
  </details>

- **2026-07-20** — Zesen Zhao, Minkyoung Cho, Hui shen et al. — [Test-Time Scaling for World Action Models via Zero-Shot Geometric Evaluation](http://arxiv.org/abs/2607.17454v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling improves foundation-model inference by spending additional computation, but robot control requires deciding whether extra compute is useful before executing an action. World Action Models (WAMs) make this decision natural: each rollout exposes both an action chunk and predicted future observations. We propose \methodgated, a training-free selective test-time scaling framework for WAMs. We first instantiate \method, a fixed-budget Best-of-$N$ selector that ranks sampled rollouts...
  </details>

- **2026-07-19** — Jun Nie, Zhiqin Yang, Zhenheng Tang et al. — [DRNOISE: Benchmarking Deep Research Agents in Misleading Evidence Environments](http://arxiv.org/abs/2607.17291v1)
  <details><summary>📄 Abstract</summary>
  Deep research agents increasingly operate over the open web, where relevant records coexist with redundant summaries, outdated reports, and misleading documents. Existing evaluations offer limited insight into whether agents preserve sound evidential standards when an ordinary-looking false document is deliberately seeded into a searchable environment and offers a direct shortcut to a conflicting answer. We introduce DRNOISE, a 100-task benchmark for answer recovery under misleading evidence. Ea...
  </details>

- **2026-07-19** — Luyu Qiu, Jianing Li, Hwanhee Kim et al. — [Explaining and Tuning Transformer-based LLMs in Arithmetic Tasks with Human Strategies](http://arxiv.org/abs/2607.17166v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based large language models (LLMs) continue to achieve state-of-the-art performance across various natural language processing tasks. However, their subpar performance on seemingly elementary problems, such as basic arithmetic, raises concerns about model reliability, safety, and ethical deployment. In this study, we demonstrate that the performance of a vanilla Transformer model trained on integer arithmetic tasks can be improved using methods effective for human learners. We begin ...
  </details>

- **2026-07-19** — Lingwei Dang, Juntong Li, Zonghan Li et al. — [HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis](http://arxiv.org/abs/2607.17097v1)
  <details><summary>📄 Abstract</summary>
  Hand-Object Interaction (HOI) synthesis is a cornerstone for animation production and embodied AI. Despite the strong priors of video foundation models, multi-view consistent HOI synthesis remains challenging due to complex hand motions and occlusions. We present HarmoHOI, a unified diffusion framework that jointly and harmoniously generates synchronized multi-view HOI videos and globally aligned 3D point tracks. Our core insight is that robust multi-view consistency fundamentally requires globa...
  </details>

- **2026-07-19** — Arunabh Dastidar, the Leni Team — [Where Does Agent Reliability Come From? A Cross-Benchmark Decomposition of Verification Loops, Specialist Models, and Scaffolding in a Production Enterprise Agent](http://arxiv.org/abs/2607.17044v1)
  <details><summary>📄 Abstract</summary>
  Multi-step enterprise agent tasks fail in a characteristic way: single-pass inference has no checkpoint between deciding an answer and committing to it. We study one production system (Leni) whose architecture installs such checkpoints: verification loops (execute, observe, compare, correct) staffed by lightweight task-specialized post-trained models. We evaluate the unmodified production configuration on three public benchmarks stressing distinct failure modes: SpreadsheetBench Verified (silent...
  </details>

- **2026-07-19** — Aman Vyas, Vasista Kodumagulla, Zain Taufique et al. — [TAPAS: Throughput-adaptive Perception for Autonomous Systems](http://arxiv.org/abs/2607.17317v1)
  <details><summary>📄 Abstract</summary>
  Autonomous systems rely on a perception module to navigate through dynamic environments. In real-world scenarios, the perception module's throughput requirements vary at runtime due to changes in scene complexity. However, existing perception strategies assume a fixed FPS and static model-to-cluster mapping, resulting in either over/under provision of throughput requirements or unnecessary energy consumption across diverse scenes. Addressing this challenge requires tightly coupled \textit{scene ...
  </details>

- **2026-07-19** — Silviu Pitis — [Rationalizing Boltzmann Rationality: An Axiomatic Characterization of Entropy-Regularized Policies](http://arxiv.org/abs/2607.17316v1)
  <details><summary>📄 Abstract</summary>
  The softmax policy $π(a \mid s) \propto \exp(βQ(s,a))$ is the default model of stochastic choice in reinforcement learning (RL). Various justifications based on robustness, exploration, and optimization have been offered in the RL literature, but none uniquely derives the softmax form from first principles. This leaves a basic tension unresolved: the entropy bonus in the soft Bellman equation violates the Independence axiom that underwrites the Markov decision process (MDP) reward structure. We ...
  </details>

- **2026-07-19** — Ke Liao, Yifan Cheng, Werner Dobrautz et al. — [Interpolative Separable Density-Fitting for Transcorrelated Hamiltonians](http://arxiv.org/abs/2607.17314v1)
  <details><summary>📄 Abstract</summary>
  The transcorrelated (TC) method dramatically accelerates the convergence of correlated calculations toward the complete-basis-set (CBS) limit by folding a Jastrow correlator into the Hamiltonian via a similarity transformation, incorporating the electron--electron cusp into the effective interaction. We make the TC framework practical for large systems and flexible, multi-center correlators by compressing the grid-evaluated TC integrals with the interpolative separable density-fitting (ISDF) app...
  </details>

- **2026-07-19** — Ryan Xu, Atlas Zhao, David Bao et al. — [WAR: Workload-Aware Rollouts for Synchronous Agentic Reinforcement Learning](http://arxiv.org/abs/2607.17299v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon rollout generation has become the dominant systems bottleneck in agentic reinforcement learning (RL). As agents interact with environments over many turns, trajectories rapidly grow to tens of thousands of tokens, making synchronous RL training increasingly constrained by rollout. We propose WAR, a workload-aware rollout system that substantially accelerates synchronous agentic RL by jointly optimizing decoding and scheduling. WAR is built on a key observation: the optimal rollout o...
  </details>

- **2026-07-19** — Mohamed Berrada — [Stability and Robustness Analysis of Regularized Reconstruction Methods for Low-Dose Computed Tomography in Parallel-Beam Geometry](http://arxiv.org/abs/2607.17298v1)
  <details><summary>📄 Abstract</summary>
  Low-dose computed tomography (LDCT) reduces radiation exposure but increases the ill-posedness of the reconstruction problem due to noise and sparse data. While regularized methods like Tikhonov and Total Variation (TV) improve image quality, their performance depends heavily on noise characteristics, sampling conditions, and parameter selection. This study presents a systematic stability and robustness analysis of Filtered Back Projection (FBP), Tikhonov regularization, and TV minimization with...
  </details>

- **2026-07-19** — Aivo Olev, Tanel Alumäe — [Robust Summarization of Doctor-Patient Conversations: TalTech Systems for the Beyond Transcription Challenge](http://arxiv.org/abs/2607.17230v1)
  <details><summary>📄 Abstract</summary>
  This paper describes TalTech's submissions to the Beyond Transcription Challenge (BeTraC), which requires generating SOAP notes directly from long doctor-patient conversation recordings, without intermediate transcription. After screening open-weight speech LLMs for long-audio robustness, we adapted Voxtral Mini (lightweight track) and Voxtral Small (heavyweight track) with LoRA supervised fine-tuning followed by DAPO reinforcement learning that uses the challenge metric, Open Medical Concept F1...
  </details>

- **2026-07-19** — Pilsung Kang — [Auditing Question-Order Effects in Large Language Models with the QQ Equality: Mechanism Characterization and a Saturation Caveat](http://arxiv.org/abs/2607.17219v1)
  <details><summary>📄 Abstract</summary>
  Human survey respondents exhibit question-order effects that satisfy the QQ (quantum question) equality, an a priori, parameter-free prediction of the projective quantum question-order model. We develop the QQ equality into an audit criterion for sequential judgments of autoregressive large language models (LLMs). Theoretically, we characterize which mechanism classes satisfy it robustly: marginal-independent kernels satisfy QQ iff all four mismatch transition rates coincide (a class containing ...
  </details>

- **2026-07-19** — Siyuan Zheng, Yifan Duan, Chao Xue et al. — [Scope3Trace: Evidence-Based Identification and Extraction of Scope 3 GHG Emissions from Sustainability Reports](http://arxiv.org/abs/2607.17122v1)
  <details><summary>📄 Abstract</summary>
  Scope 3 greenhouse gas (GHG) emissions account for the majority of corporate carbon footprints, yet remain difficult to analyze at scale due to sparse disclosures, heterogeneous report document formats, and limited evidence traceability. Existing approaches typically rely on large language models to extract emissions information from ESG reports, but often lack explicit evidence grounding or depend on costly manual annotation and verification to ensure extraction reliability. To address these ch...
  </details>

- **2026-07-19** — Harbir Antil, Rocío Díaz Martín, Ivan V. Medri et al. — [Reduced Order Modeling of One-Dimensional Conservative PDEs via the Cumulative Distribution Transform](http://arxiv.org/abs/2607.17066v1)
  <details><summary>📄 Abstract</summary>
  We propose a reduced order modeling (ROM) framework for 1D conservative PDEs based on the cumulative distribution transform (CDT). The CDT maps nonnegative, equal-mass states into a Hilbert space in which 1D Wasserstein distances become weighted $L^2$ distances and translations become affine shifts. This makes the transform especially suited for transport-dominated dynamics, where Eulerian linear-subspace ROMs often suffer from slow decay of Kolmogorov widths.   We study this phenomenon for scal...
  </details>

- **2026-07-19** — Amez Amanj Ali, Kuo-Kun Tseng — [Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correction for Autonomous Decision-Making](http://arxiv.org/abs/2607.17038v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses key technical challenges in current large language model (LLM) agent applications, including long-horizon planning, sparse reward attribution, and dynamic environmental interaction, by designing and optimizing an intelligent agent workflow. The proposed architecture is based on the synthesis of core AI paradigms: Visual, Language, Generative, Graph, Multimodal, Reinforcement, and Agent Intelligence. Unlike conventional baseline models that rely on static prompting and lack r...
  </details>

- **2026-07-18** — Luca Sportelli, Tyler Barr, Cagri Kilic et al. — [AI-Augmented Model Predictive Control for Safe and Adaptive Rendezvous and Proximity Operations](http://arxiv.org/abs/2607.16630v1)
  <details><summary>📄 Abstract</summary>
  Autonomous rendezvous and proximity operations (RPO) in adversarial orbital environments require guidance architectures balancing target pursuit, safety preservation, and real-time adaptability under dynamically evolving interaction conditions. Although learning-based approaches show promise, their application to safety-critical orbital robotics remains limited by concerns regarding interpretability, robustness, and constraint awareness. This work presents an adaptive Model Predictive Control (M...
  </details>

- **2026-07-18** — Ruturaj S. Sambhus, Kapi Ketan Mehta, Yicheng Zeng et al. — [ADMM-Based Safety-Critical Distributed NMPC for Cooperative Transportation by Quadrupedal Robots](http://arxiv.org/abs/2607.17007v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a safety-critical distributed nonlinear model predictive control (DNMPC) framework for cooperative payload transportation by teams of quadrupedal robots. The proposed approach models the robotic team and the shared payload as a dynamically coupled networked system with rigid holonomic coupling constraints arising from cooperative transportation. To enable distributed real-time optimization, the centralized finite-horizon optimal control problem is decomposed into parallel loc...
  </details>

- **2026-07-18** — Yuwen Liao, Yihang Lan, Yizhuo Yang et al. — [G2-Nav: Grounded and Guarded Vision-Language Costmaps for Robot Social Navigation](http://arxiv.org/abs/2607.16956v1)
  <details><summary>📄 Abstract</summary>
  Social navigation requires the robot to reason and respond in complex real-world environments. While recent works attempt to incorporate human-level intelligence into robot planning using large Vision-Language Models (VLMs), end-to-end frameworks often create an unpredictable black-box, and existing instruction-following methods are not designed for full autonomy. To bridge this gap, we present G2-Nav, a novel framework that grounds abstract social reasoning and guards safe real-world deployment...
  </details>

- **2026-07-18** — Mamdouh Alenezi — [Specification-Driven Development as the Foundation of AI-Native Enterprise Software Engineering](http://arxiv.org/abs/2607.16680v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) and agentic AI are shifting software engineering from manual coding toward intent specification, architecture, and governance. Two paradigms have emerged: vibe coding, an intuition-driven approach accepting AI artifacts via observed behavior, and Specification-Driven Development (SDD), which uses structured specifications as the authoritative source of truth. This article makes three contributions. First, based on a verified literature corpus, it identifies failure m...
  </details>

- **2026-07-18** — Neel Somani — [PriorProof: A Point-in-Time Measure of Technique Novelty for Formal Proofs](http://arxiv.org/abs/2607.16997v1)
  <details><summary>📄 Abstract</summary>
  Mathematicians distinguish proofs that explain, simplify, or introduce a nonstandard route, but these judgments are difficult to operationalize. We study a deliberately narrower construct: time-relative proof-route nonstandardness in formal mathematics. For a Lean theorem, PriorProof extracts the dependency footprint of its elaborated proof term and scores the weighted surprisal of that footprint under a retrieval-conditioned, hierarchically smoothed prior built only from an earlier quarterly sn...
  </details>

- **2026-07-18** — Gaurav Mahadik, Ananya Hazarika, Mehdi Rahmati — [Intelligent Code-Division Multiplexing for Resilient Underwater Optical Wireless Communications](http://arxiv.org/abs/2607.16925v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a novel intelligent chaotic-based code-division multiple access (CDMA) scheme for underwater optical wireless communication (UOWC), addressing critical performance degradation caused by severe scattering and multipath dispersion in underwater environments. Unlike conventional modulation techniques such as on-off keying, which depend on precise pulse timing and show high sensitivity to channel distortions, the proposed approach leverages unpredictable deterministic chaotic seq...
  </details>

- **2026-07-18** — Divyansh Chawla, Anshu Garg, Isshaan Singh — [Enhancing Personalized Bladder Cancer Treatment Through Reinforcement Learning: A Recurrent Patient State Transition Decision Support Framework](http://arxiv.org/abs/2607.16916v1)
  <details><summary>📄 Abstract</summary>
  Bladder cancer treatment requires personalized and adaptive decision-making, particularly for recurrent disease, where treatment effectiveness changes across successive clinical episodes. Conventional clinical decision support systems typically rely on static treatment guidelines or single-step predictive models, limiting their ability to capture disease progression over time. This paper presents a recurrent patient state-transition simulation framework for bladder cancer treatment planning that...
  </details>

- **2026-07-18** — Jiaming Cheng, Duong The Do, Duong Tung Nguyen — [Robust KV Cache Management for LLM Serving under Output Token Length Uncertainty](http://arxiv.org/abs/2607.16892v1)
  <details><summary>📄 Abstract</summary>
  KV cache memory is a primary bottleneck in modern LLM serving systems deployed on GPU clusters. A fundamental challenge is that the KV cache must be reserved upon request arrival, while the output token length remains unknown until generation completes. Under-reservation triggers preemption -- forcing termination and recomputation of requests and incurring significant overhead -- whereas over-reservation wastes memory and reduces throughput. This creates a central trade-off between memory effici...
  </details>

- **2026-07-18** — Yangjing Wang, Ouya Wang, Shenglong Zhou et al. — [Hierarchical Wireless Foundation Model for Multi-Task Optimization](http://arxiv.org/abs/2607.16877v1)
  <details><summary>📄 Abstract</summary>
  The increasing complexity of next-generation wireless networks has driven the integration of artificial intelligence (AI) into wireless communications. However, most existing studies focus on developing task-specific deep learning techniques for single scenarios, which limits their ability to generalize across diverse tasks, channel conditions, and system configurations. To address this generalization bottleneck, we propose a hierarchical wireless foundation model (WFM) for multi-task optimizati...
  </details>

- **2026-07-18** — Federico Zahariev, Vanda Glezakou — [Certified Optimal Measurement Reduction over Quantum Context Landscapes](http://arxiv.org/abs/2607.16866v1)
  <details><summary>📄 Abstract</summary>
  Quantum-measurement reduction contains two distinct global-optimization layers: a continuous problem of splitting an observable and allocating shots within a fixed measurement dictionary, and a nonconvex outer problem of designing the dictionary and calibrating its data-driven uncertainty model. We solve the inner layer globally and certifiably as a second-order cone program (SOCP), and use RANGE, a robust adaptive nature-inspired global optimizer, for the combinatorial and statistical outer lay...
  </details>

- **2026-07-18** — Jiahui Zhang, Wenyuan Wang, Fuquan Dou — [Shortcuts to adiabaticity in five-level systems using counter-diabatic driving and time-rescaling optimization](http://arxiv.org/abs/2607.16829v1)
  <details><summary>📄 Abstract</summary>
  Shortcuts to adiabaticity (STA) is a common protocol to realize high-fidelity and robust quantum control in various quantum systems. To date, STA has been widely applied in two- and three-level systems, whereas designing feasible strategies to achieve perfect quantum state engineering in multi-level systems still remains a challenging task. Here, we propose to use counterdiabatic (CD) driving and time-rescaling (TR) methods to construct multi-state stimulated Raman shortcut-to-adiabatic passage ...
  </details>

- **2026-07-18** — Raza Imam, Darakshan Rashid, Yutong Xie et al. — [Can Experts Adapt Without Training? On Test-Time Modality Generalization in MVLMs](http://arxiv.org/abs/2607.16726v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language models (MVLMs) promise broad zero-shot generalization, yet their reliability collapses when confronted with unseen modalities and domains, precisely where clinical robustness matters most. To address this gap, we revisit test-time modality generalization from the perspective of Mixture-of-Experts (MoE) and ask: can experts route-and-adapt without any optimization during inference? We identify a fundamental specialization-generalization dilemma at test time, where blindly ...
  </details>

- **2026-07-18** — Umair bin Mansoor, Munaf Rashid, Roomi Naqvi — [A Framework for Early Sepsis Prediction via Self-Supervised (JEPA) and Federated Representation Learning](http://arxiv.org/abs/2607.16681v1)
  <details><summary>📄 Abstract</summary>
  Early sepsis prediction from electronic health records is challenged by irregular sampling, high missingness, and class imbalance. We systematically compare four modeling paradigms -- self-supervised Joint Embedding Predictive Architecture (JEPA) via masked latent prediction, self-supervised VICReg (variance-invariance-covariance regularization) with two-view augmentation, semi-supervised fine-tuning of a VICReg-pretrained encoder, and supervised Temporal Convolutional Network (TCN) -- alongside...
  </details>

- **2026-07-18** — Jaroslaw Janas, Josef Pieprzyk, Pawel Morawiecki — [Synchronization-Free Algebraic Fingerprints for Large Language Models: From Autoregressive to Diffusion Models](http://arxiv.org/abs/2607.16648v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have created an urgent need for reliable watermarking methods that enable attribution of generated text while remaining robust to editing and paraphrasing. We propose a novel synchronization-free watermarking scheme in which every watermark consists of a single binary congruence generated from a pair of neighbouring tokens. For each token pair, a cryptographic hash determines an evaluation point of a Reed--Solomon polynomial representing the secret identity, while th...
  </details>

- **2026-07-17** — Jun He, Deying Yu — [The Honest Quorum Problem: Epistemic Byzantine Fault Tolerance for Agentic Infrastructure](http://arxiv.org/abs/2607.16109v1)
  <details><summary>📄 Abstract</summary>
  State machine replication (SMR) and Byzantine fault-tolerant (BFT) consensus guarantee agreement despite a bounded number of arbitrary, colluding faulty participants. However, these guarantees rely on participants outside this set correctly executing the protocol's transition semantics. Agentic validators expose a weaker boundary: an authenticated, responsive, non-equivocating, and protocol-compliant reasoning participant may still endorse a semantically invalid transition due to reasoning error...
  </details>

- **2026-07-17** — P. Argoul, J. Taillard, F. Argoul — [Cauchy-Paul wavelet transforms revisited: A framework for intermittent non-sinusoidal oscillations](http://arxiv.org/abs/2607.15953v1)
  <details><summary>📄 Abstract</summary>
  This paper revisits the continuous wavelet transform framework by establishing a rigorous physical and dimensional formulation of the Cauchy-Paul mother wavelet, tailored specifically for intermittent, non-sinusoidal electrophysiological oscillations. Departing from conventional, purely mathematical definitions, we introduce a characteristic time scale $τ$ into the frequency-domain formulation of the mother wavelet. This parameter ensures strict dimensional consistency by maintaining dimensionle...
  </details>

- **2026-07-17** — Dingshan Sun, Ang Li, Chaopeng Tan et al. — [PriEco-DRL: Joint Optimization of Electric-Bus Eco-Driving and Transit-Priority Adaptive Signals via Deep Reinforcement Learning](http://arxiv.org/abs/2607.15862v1)
  <details><summary>📄 Abstract</summary>
  Urban transit electrification requires balancing energy efficiency, schedule reliability, and ride comfort for electric buses (EBs), particularly when interacting with transit-priority adaptive signals in congested networks. This paper proposes PriEco-DRL, a joint optimization framework that integrates EB eco-driving with transit-priority adaptive signal control using deep reinforcement learning (DRL). The signal layer employs a priority-weighted max-pressure (Priority-MP) controller to allocate...
  </details>

- **2026-07-17** — Xiaojiang Peng, Kai Peng, Jie Lu et al. — [AC-VLA: Robust Out-of-Distribution Action Execution via Compositional Learning](http://arxiv.org/abs/2607.15714v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models excel at end-to-end robotic manipulation but struggle with out-of-distribution (OOD) generalization when familiar sub-tasks are recombined in unseen configurations. We identify two mutually reinforcing failure modes: \emph{trajectory overfitting}, where models overfit to holistic trajectory patterns rather than compositional sub-skill semantics; and \emph{perceptual shortcut}, where action tokens over-rely on wrist-view textures at the expense of global spatia...
  </details>

- **2026-07-17** — Aritro De, Juliana Felkner — [Neuro-Symbolic AI for LEED compliance: Document-Centric Benchmarking, Deterministic Numeric Checking, and When Multimodal Hurts](http://arxiv.org/abs/2607.15647v1)
  <details><summary>📄 Abstract</summary>
  LEED v4.1 BD+C certification remains a document-intensive process that requires reviewers to read hundreds of pages of project evidence and apply credit-specific threshold logic by hand. This paper investigates whether small, locally deployed language models can perform meaningful screening of LEED documentation and how deterministic symbolic components should share that work. A neuro-symbolic pipeline is introduced that aligns project PDFs to LEED credit sections, retrieves evidence with credit...
  </details>

- **2026-07-17** — Dibyendu Ghosh, Ayushi Shakya — [Vision-Language-Motion Maps: An Open-Vocabulary, Uncertainty-Aware, Queryable Motion Attribute for 3D Scene Maps](http://arxiv.org/abs/2607.16173v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary 3D maps let robots answer language queries about what and where, but they assume a static world and cannot answer queries about how scene elements behave. We introduce Vision-Language-Motion Maps (VLMM), an open-vocabulary, natural-language-queryable 3D map in which each element carries a fused motion attribute: a VLM/LLM semantic movability prior combined with geometrically observed cross-frame motion, together with a per-element uncertainty. Queries reduce to attribute filters ...
  </details>

- **2026-07-17** — Jiarui Zhang, Muzi Tao, Shangshang Wang et al. — [An Exam for Active Observers](http://arxiv.org/abs/2607.16165v1)
  <details><summary>📄 Abstract</summary>
  Human vision is a closed loop: gaze is continuously redirected by intermediate hypotheses rather than a single snapshot. Decades of psychophysics and cognitive science have argued that this active observation is essential for a wide range of tasks. Whether today's multimodal large language models (MLLMs) exercise active observation is an empirical question that current vision-language benchmarks do not answer. We introduce ActiveVision, a benchmark that makes active observation measurable for ML...
  </details>

- **2026-07-17** — Jehun Kang, Jungha Wang, Youngjun Hwang et al. — [DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction](http://arxiv.org/abs/2607.16012v1)
  <details><summary>📄 Abstract</summary>
  Multi-Task Learning (MTL) in robotics perception systems supports comprehensive 3D spatial scene understanding by integrating semantic segmentation and depth estimation. While Vision Foundation Models (VFMs) are increasingly adopted as robust feature encoders, existing decoding strategies present a critical bottleneck. To address this, we propose DPNeXt, a streamlined multi-scale feature fusion decoder and efficient alternative to the standard Dense Prediction Transformer (DPT). DPNeXt uses dual...
  </details>

- **2026-07-17** — Vishal Pandey, Gopal Singh — [ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing](http://arxiv.org/abs/2607.15899v1)
  <details><summary>📄 Abstract</summary>
  In production large language model (LLM) deployments, high API availability guarantees do not equate to conversational continuity. When a primary provider experiences an outage or strict rate-limiting, naive stateless failover mechanisms successfully maintain uptime but silently discard conversation history, severely disrupting the user experience. To rigorously quantify and resolve this failure mode, we introduce two novel metrics: Continuity Preservation Rate (CPR) and Continuity Latency Overh...
  </details>

- **2026-07-17** — Haowei Hua — [Cost-efficient generative AI summarization for scalable automated essay scoring in educational assessment](http://arxiv.org/abs/2607.15829v1)
  <details><summary>📄 Abstract</summary>
  Automated essay scoring (AES) enables scalable assessment and timely feedback but remains challenged by transformer input-length limitations, which can cause information loss when processing long essays. This study proposes a generative AI-assisted summarization framework to improve long-form essay representation while maintaining scoring reliability. Using the ASAP 2.0 dataset, we generate controlled-length summaries with three GPT-5 variants (GPT-5, GPT-5 mini, and GPT-5 nano) and use them as ...
  </details>

- **2026-07-17** — Hui Yang, Jiaoyan Chen, Yiping Song et al. — [NeurOWL: An LLM-Based Neural-symbolic Framework for Incomplete OWL Ontology Reasoning](http://arxiv.org/abs/2607.15776v1)
  <details><summary>📄 Abstract</summary>
  OWL ontologies provide a formal knowledge representation framework that enables semantic reasoning, and have been widely adopted across domains such as healthcare and bioinformatics. In practice, however, real-world ontologies are often incomplete, which pose challenges for reasoning. In this work, we focus on a fundamental subsumption reasoning problem: given an incomplete ontology and a candidate (non-entailed) subsumption, determine whether the subsumption is semantically plausible and, if so...
  </details>

- **2026-07-17** — Davide Italo Serramazza, Thach Le Nguyen, Georgiana Ifrim — [Scaling Time Series Classification via XAI-Driven Data Reduction](http://arxiv.org/abs/2607.15774v1)
  <details><summary>📄 Abstract</summary>
  Explainable AI (XAI) for time series has seen significant algorithmic growth, but its utility in providing measurable performance gains for downstream tasks remains under-explored. This paper bridges this gap by introducing drXAI, a novel methodology that repurposes XAI attribution methods for effective data reduction in Time Series Classification (TSC). The core challenge in modern TSC is scalability; state-of-the-art models, such as Transformers, exhibit quadratic complexity relative to sequen...
  </details>

- **2026-07-17** — Yong Chu, Xun Zhou, Zenglin Xu et al. — [Map as a Prompt: Learning Multi-Modal Spatial-Signal Foundation Models for Cross-scenario Wireless Localization](http://arxiv.org/abs/2607.15713v1)
  <details><summary>📄 Abstract</summary>
  Accurate and robust wireless localization is a critical enabler for emerging 5G/6G applications, including autonomous driving, extended reality, and smart manufacturing. Despite its importance, achieving precise localization across diverse environments remains challenging due to the complex nature of wireless signals and their sensitivity to environmental changes. Existing data-driven approaches often suffer from limited generalization capability, requiring extensive labeled data and struggling ...
  </details>

- **2026-07-17** — Youngho Kim, Hoonhee Cho, Jae-Young Kang et al. — [GoStop: Reinforcement Learning for Adaptive Temporal Aggregation in Event-Based Feature Tracking](http://arxiv.org/abs/2607.15699v1)
  <details><summary>📄 Abstract</summary>
  Feature tracking plays a fundamental role in understanding scene motion and supports various downstream tasks. Event cameras, with their high temporal resolution and asynchronous sensing, enable low-latency and motion-robust perception, making them well-suited for feature tracking under fast and non-linear motion. However, existing event-based feature tracking methods rely on fixed heuristic rules based on hand-tuning for event accumulation. Such strategies fail to adapt to diverse motion dynami...
  </details>

- **2026-07-17** — Shuaiyu Zhou, Fengpeng Yue, Zengjie Hu et al. — [ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning](http://arxiv.org/abs/2607.15660v1)
  <details><summary>📄 Abstract</summary>
  While LLM agents demonstrate strong reasoning abilities in compact and well-defined scenarios, they struggle to maintain robustness and effectiveness when faced with large-scale, diverse, and dynamic real-world environments that demand seamless tool integration. To address this gap, we introduce ToolVerse, a comprehensive framework that scales up agentic RL environments and enables agents to perform complex long-horizon reasoning in Tool-Integrated Reasoning (TIR) tasks. First, ToolVerse automat...
  </details>

- **2026-07-17** — Avni Bansal, Ian Brunton, Konstantin Batygin et al. — [Distant TNO Inclinations as a Constraint on Primordial Cluster Perturbations in the Presence of Planet Nine](http://arxiv.org/abs/2607.15646v1)
  <details><summary>📄 Abstract</summary>
  The Sun was almost certainly born in a stellar cluster, implying some degree of external forcing from neighboring stars during the Solar System's infancy. Published estimates of the strongest relevant stellar encounter, however, span a broad range, from relatively gentle perturbations to violently disruptive flybys. The modest inclination dispersion of the distant trans-Neptunian population has previously been used to argue that strong primordial encounters were unlikely and that the outer Solar...
  </details>

- **2026-07-17** — Reina Kaneko, Junya Hara, Hiroshi Higashi et al. — [WREN: Low Light Image Enhancement Using Retinex theory-based Double U-Net-like Structures](http://arxiv.org/abs/2607.15604v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a neural network for low light image enhancement (LLIE) based on retinex theory to make LLIE robust for various dynamic range scenes. The retinex theory is an image formulation model inspired by a human color perception hypothesis, where a low light image is decomposed into intrinsic color context (i.e., reflectance map) and scene-dependent illumination (i.e., illumination map). Due to non-uniqueness of its decomposition, existing retinex-based LLIE methods often fail to achi...
  </details>

- **2026-07-15** — Boyuan Wang, Zhenyuan Zhang, Zhiqin Yang et al. — [PhysClaw-0: A Symbiotic Agentic System for Robot Autonomy via Language Corrections](http://arxiv.org/abs/2607.14047v1)
  <details><summary>📄 Abstract</summary>
  Autonomous data collection governs the volume and quality of real-world trajectories for manipulation policy learning. Existing pipelines reduce human effort via self-resetting, VLM verification, or language-guided correction, yet episode-scoped fixes must be reissued whenever the same failure recurs, so oversight cost grows with session length rather than with the number of distinct problems. We present PhysClaw-0, a human-robot symbiotic agentic system in which corrections are retained and reu...
  </details>

- **2026-07-15** — Jiangang Han — [Partially Correlated Verifier Cascades in LLM Harnesses: Concave Log-Odds, Polynomial Reliability, and Blind-Spot Ceilings](http://arxiv.org/abs/2607.13918v1)
  <details><summary>📄 Abstract</summary>
  Serial verification gates are a core reliability primitive in LLM harnesses: a candidate answer is returned only if $k$ verifier calls all accept it. Under conditionally independent gates, the recent Odds Law (arXiv:2606.15712) shows that posterior log-odds grow linearly in $k$, so failure decays exponentially, and states that "a tight theory of partially correlated verifier cascades remains open." This note gives a minimal such theory. Modeling the per-instance false-accept rate on the generato...
  </details>

- **2026-07-15** — Zichen Ding, Jiaye Ge, Shufan Jiang et al. — [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](http://arxiv.org/abs/2607.13705v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) evolve into autonomous agents, the need for unified evaluation infrastructure becomes critical. However, current evaluation pipelines remain highly fragmented and tightly coupled, hindering reproducibility and causing redundant engineering. To address this, we introduce AgentCompass, an open-source, lightweight, and extensible infrastructure for evaluating LLM-based agents. AgentCompass organizes the evaluation process around three independent components, namely B...
  </details>

- **2026-07-15** — Ximeng Mao, Nanda H. Krishna, Avery Hee-Woon Ryoo et al. — [Leveraging unlabelled data for generalizable neural population decoding](http://arxiv.org/abs/2607.14086v1)
  <details><summary>📄 Abstract</summary>
  Robust and accurate neural decoders are integral to neurotechnologies such as brain-computer interfaces and closed-loop experiments. Recent work has shown that tokenizing neural data at the spike level facilitates multi-session pretraining and delivers state-of-the-art decoding performance. However, current spike-based models are restricted to supervised learning (SL), limiting training to datasets with paired behavioural labels. To address this limitation, we introduce MOJO (Masked autOencoder-...
  </details>

- **2026-07-15** — Jingyu Xiao, Zhongyi Zhang, Haoran Hou et al. — [VisualRepair: Dynamic Tool Calling and Region Focusing for Visual Software Issue Repair](http://arxiv.org/abs/2607.14075v1)
  <details><summary>📄 Abstract</summary>
  Automated Program Repair (APR) has witnessed significant progress with the advent of Large Language Models (LLMs). However, as modern software systems increasingly expose rich graphical user interfaces, effectively leveraging visual information from bug screenshots has become essential for understanding bugs and generating accurate fixes in multimodal scenarios. Real-world issue reports frequently contain heterogeneous visual attachments including UI screenshots, IDE snapshots, GIFs, and text-ce...
  </details>

- **2026-07-15** — Tam Nguyen, Hung Nguyen, Robert Ogburn — [AI-accelerated End-to-End Framework for Rapid Professional Upskilling](http://arxiv.org/abs/2607.14044v1)
  <details><summary>📄 Abstract</summary>
  By 2030, 59 of every 100 workers will need reskilling or upskilling, yet the average time to close an enterprise skills gap grew from roughly 3 days in 2014 to 36 days in 2018. Most current frameworks accelerate single stages of upskilling programs and generally lack industry validation. We present an end-to-end framework that applies AI acceleration across five stages of knowledge acquisition, content development, content review and verification, teaching, and assessment development; with a str...
  </details>

- **2026-07-15** — Geng Li, Haiwen Li, Rui Chen et al. — [Peak-End-Net: A Peak-End Rule Inspired Framework for Generalizable Video Aesthetic Assessment](http://arxiv.org/abs/2607.13941v1)
  <details><summary>📄 Abstract</summary>
  Video aesthetic assessment (VAA) aims to predict how aesthetically pleasing a video is, yet remains far less explored than other visual assessment tasks. Its progress is hindered not only by the scarcity of large-scale benchmarks, but also by the intrinsic subjectivity of aesthetic judgment, which is shaped by human perception. In this paper, we revisit VAA from a psychological perspective and propose \textit{Peak-End-Net}, a lightweight and interpretable framework inspired by the \textit{peak-e...
  </details>

- **2026-07-15** — Jianguo Yu, Rukang Wang, Duanfeng Chu et al. — [S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving](http://arxiv.org/abs/2607.13926v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving, yet they fundamentally struggle to generate precise, low-level control actions. This limitation is rooted in a semantic-physical gap caused by the inherent mismatch between discrete language tokens and continuous trajectory planning. While Vision-Language-Action (VLA) architectures attempt to bridge this gap by unifying perception and control into a single policy, this entanglemen...
  </details>

- **2026-07-15** — Ismael Rousseau, Geraldine Damnati, Frederic Bechet — [DeepStress: Stress-Testing Deep Search Agents](http://arxiv.org/abs/2607.13920v1)
  <details><summary>📄 Abstract</summary>
  While search agents demonstrate impressive capabilities in multi-step question answering, their robustness to poor-quality evidence remains under-explored. This phenomenon occurs rarely in realistic benchmarks but can lead to dramatic failure in real life applications. Therefore in this study we propose DeepStress, a stress testing framework that controls the frequency of challenging evidence by replacing the retrieval module of search agents with a controlled synthetic environment. We use this ...
  </details>

- **2026-07-15** — Xueyao Zhang, Chenyang Yan, Bo Yang et al. — [Task-Oriented Sensing and Covert Transmissions for Collaborative Multi-AUV Systems](http://arxiv.org/abs/2607.13880v1)
  <details><summary>📄 Abstract</summary>
  In underwater covert cooperative missions, autonomous underwater vehicles (AUVs) often cannot rely on active sonar to continuously obtain complete information, since active sensing and frequent communications increase the risk of exposure. As a result, AUVs primarily rely on passive observation, an approach that yields incomplete local perception and limited task efficiency. Although underwater acoustic communications can mitigate this limitation through information sharing, they are simultaneou...
  </details>

- **2026-07-15** — Zhuoyuan Fu, Zeshang Li, Yiqiong Zhang et al. — [Towards Enhancing 3D Spatial Reasoning in Medical Multimodal Large Language Models](http://arxiv.org/abs/2607.13860v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) have demonstrated remarkable success in 2D medical image understanding, their extension to 3D volumetric imaging remains hindered by prohibitive annotation costs and dataset opacity. Current data formats, predominantly consisting of rigid Visual Question Answering (VQA) pairs or unstructured final clinical reports, typically fail to capture explicit clinical reasoning. To address this limitation, we introduce a large-scale structured reasoning datas...
  </details>

- **2026-07-15** — Rodrigo Pato Nogueira, Marco Vieira, João R. Campos — [PROBE: Benchmarking Code Generation in Large Language Models](http://arxiv.org/abs/2607.13820v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly being used in everyday software engineering tasks, particularly in automated code generation. Despite their widespread adoption, these models remain far from perfect, making systematic and fair evaluation essential to understand their strengths and limitations. In the context of code generation, existing benchmarks are limited: they often target a single programming language and rely primarily on unit test outcomes, while overlooking other critical d...
  </details>

- **2026-07-15** — Xiaopeng Zhang, Yueyang Weng, Qi Liu et al. — [Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning](http://arxiv.org/abs/2607.13818v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation poses fundamental challenges due to uncertainty, long-horizon execution, and compounding errors, which can easily destabilize execution and lead to task failure. Although recent vision-language-action (VLA) models exhibit strong generalization, they typically lack explicit mechanisms to assess execution stability and to recover when execution deviates from its nominal behavior. In this paper, we propose: (1) two complementary metrics to assess execution quality at runtime, a...
  </details>

- **2026-07-15** — Jin-Peng Yang, Yan-Hong Qin — [Multihump-Multivalley Soliton Families on a Plane Wave Background in Birefringent Optical Fibers](http://arxiv.org/abs/2607.13773v1)
  <details><summary>📄 Abstract</summary>
  We obtain a family of multihump-multivalley solitons (MHMVSs) on a plane-wave background in birefringent optical fibers governed by the two-component Fokas-Lenells equations, with exact solutions derived via the Darboux transformation method. The fundamental solutions are systematically classified through their phase diagrams, and higher-order configurations are identified as well. Notably, the construction extends to solitons with arbitrary MHMV structures, a class of solutions previously unrep...
  </details>

- **2026-07-15** — Ashish Thapa, Samrat Karki — [Barnamala: Parameter-Efficient Handwritten Devanagari Recognition at Benchmark Saturation](http://arxiv.org/abs/2607.13689v1)
  <details><summary>📄 Abstract</summary>
  We built a compact convolutional network (1.11 M parameters) for 46-class DHCD Devanagari recognition and reached 99.73%, the highest reported at 15.6x smaller than prior state-of-the-art. We have effectively reached the saturation point: every model tested, large teacher ensembles included, hits the same 11-error intrinsic floor. No configuration achieves a statistically clear win under exact McNemar tests with Wilson confidence intervals. Even without knowledge distillation, our student matche...
  </details>

- **2026-07-15** — Pengxuan Gao, Kai Ying, Botao Wu et al. — [M3F-UAV: A Missing-Modality Multimodal Foundation Model for Low-Altitude Wireless Sensing](http://arxiv.org/abs/2607.13678v1)
  <details><summary>📄 Abstract</summary>
  Low-altitude unmanned aerial vehicles (UAVs) are emerging as key platforms for wireless intelligence tasks. However, practical low-altitude wireless systems usually operate in complex urban environments, where visual occlusion, sparse geometric observations, multipath propagation, and sensor failures may degrade the reliability of single-modality models. To address these challenges, this paper proposes M3F-UAV, a missing-modality multimodal foundation model for low-altitude wireless sensing. The...
  </details>

- **2026-07-15** — Boyu Mi, Mengchen Ma, Yifei Yao et al. — [Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation](http://arxiv.org/abs/2607.13653v1)
  <details><summary>📄 Abstract</summary>
  Real-world deployment of embodied agents requires active exploration, visual grounding, and interactive intent disambiguation. However, existing frameworks often rely on privileged simulator states or assume complete instructions, bypassing realistic deployment challenges. To bridge this gap, we present REAL, an agentic framework for open-world mobile manipulation. REAL establishes sim-to-real-consistent environment APIs without oracle perception and integrates a simulated user to enable human-i...
  </details>

- **2026-07-15** — Shiyin Lu, Yinglun Li, Yu Xia et al. — [OvisOCR2 Technical Report](http://arxiv.org/abs/2607.13639v1)
  <details><summary>📄 Abstract</summary>
  We introduce OvisOCR2, a 0.8B document parsing model. OvisOCR2 is designed as an end-to-end parser: given a document page image, it generates a Markdown representation in natural reading order, covering text, formulas, tables, and visual regions. We build a data engine that combines filtered real-document annotations with synthetic pages whose rendered images and Markdown targets are derived from the same HTML source. The training recipe includes supervised fine-tuning, reinforcement learning on...
  </details>

- **2026-07-15** — David Krongauz, Arad Zulti, Eran Segal et al. — [Automatic Ordinary Differential Equations Discovery For Biological Systems Using Large Language Model Powered Agentic System](http://arxiv.org/abs/2607.13608v1)
  <details><summary>📄 Abstract</summary>
  Automatic scientific discovery has long been a goal of computational scholars - a machine that can discover nature's secrets on its own, moving computational systems beyond data-fitting tools toward the generation and refinement of mechanistic models of the universe. Recent advances in symbolic regression (SR) and large-language-model (LLM)-based agents suggest that such systems can recover equations from data, incorporate domain priors, and automate parts of the research workflow. However, most...
  </details>

- **2026-07-15** — Xian Li, Rong Wei, Lujie Yang et al. — [UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets](http://arxiv.org/abs/2607.13586v1)
  <details><summary>📄 Abstract</summary>
  Physically grounded 3D assets are increasingly important for embodied AI and robotic simulation. However, most existing 3D assets lack unified physical semantics, including articulation semantics and intrinsic physical properties, required for realistic interaction. Current approaches either treat these semantics independently or rely on canonicalized object structures, limiting robustness across heterogeneous 3D assets. We present UniPhys, a scalable framework for automatically transforming raw...
  </details>

- **2026-07-15** — Jun-Gill Kang, Jaehyun Park, Tae-Gyu Song et al. — [Agile perceptive multi-skill locomotion for quadrupedal robots in the wild](http://arxiv.org/abs/2607.13579v1)
  <details><summary>📄 Abstract</summary>
  Enabling quadrupedal robots to traverse complex terrains-from rugged outdoor environments to urban landscapes-requires seamless integration of multiple motor skills, smooth transitions between gaits, and high-speed perceptive locomotion using only onboard sensors. We present APT-RL (Action Pretrained Transformer-based Reinforcement Learning), a unified framework that enables multi-skill locomotion to achieve high-speed traversal in complex environments through autonomous skill transitions utiliz...
  </details>

- **2026-07-15** — Grzegorz Brzezinka — [Graded Entity-Familiarity Readouts in Language Models: Polish Adaptation, Cross-Language Robustness, and Refusal Steering](http://arxiv.org/abs/2607.13568v1)
  <details><summary>📄 Abstract</summary>
  Can a language model estimate its familiarity with an entity before generating an answer? We study activations at the final prompt token in twelve instruction-tuned models from the Bielik, PLLuM, Gemma-4, and Qwen3 families, using a new dataset of 1,440 Polish entities spanning four domains and ten Wikipedia-pageview deciles, plus fabricated controls. Familiarity-probe scores separate real from fabricated entities in every family; in the Polish-adapted Bielik and PLLuM families they additionally...
  </details>

- **2026-07-15** — A. Garofalo, T. Muraveva, L. Monti et al. — [Improving reddening estimates for RR Lyrae stars in the Gaia bands: a machine learning approach to the PAC(Z) relation](http://arxiv.org/abs/2607.13557v1)
  <details><summary>📄 Abstract</summary>
  RR Lyrae stars are essential tracers of old stellar populations and distance indicators across the Milky Way and nearby galaxies. However, their use as standard candles is limited by uncertainties in extinction, especially in the Gaia bands. In Gaia DR3, absorption values (AG) for fundamental-mode RR Lyrae (RRab) were based on an empirical period-amplitude-color (PAC) relation calibrated on a small sample and on passband transformations. We aim to recalibrate extinction relations for RRab stars ...
  </details>

- **2026-07-15** — Lukas Zenger — [Intuitionistic Dynamic Logic](http://arxiv.org/abs/2607.13528v1)
  <details><summary>📄 Abstract</summary>
  This thesis develops the mathematical theory of intuitionistic dynamic logics - extensions of intuitionistic propositional logic with modalities and fixed point operators. Such systems provide formal tools for reasoning about change, such as encountered in mathematical systems evolving over time or in the knowledge state of an agent after an information update.   We investigate five intuitionistic dynamic logics: intuitionistic master modality, intuitionistic common knowledge logic, intuitionist...
  </details>

- **2026-07-15** — Zongyi Li, Jun Wang, Tianwei Hou et al. — [Pinching-Antenna Systems (PASS)-Based User-Side Navigation: An Anchor-Line-based Approach](http://arxiv.org/abs/2607.13485v1)
  <details><summary>📄 Abstract</summary>
  Pinching-antenna systems (PASS) are capable of dynamically reconfiguring wireless channels by flexibly repositioning pinching antennas (PAs) along the waveguides to establish short-range line-of-sight links. In this paper, a user-side navigation framework for PASS is proposed, where mobile users determine their own positions using only downlink broadcast signals without any prior knowledge of the PA positions. First, a Lambert W function-based PA positioning and pseudorange estimation (LWF-PAP) ...
  </details>

- **2026-07-15** — Mingzhu Wang, Yun Shang — [PQFA: Parallel Quantum Feature Augmentation of Fused Representations for Multimodal Classification](http://arxiv.org/abs/2607.13466v1)
  <details><summary>📄 Abstract</summary>
  Most multimodal learning methods improve how heterogeneous representations are aligned and fused, while post-fusion enhancement remains less explored. We propose Parallel Quantum Feature Augmentation (PQFA), a hybrid quantum-classical framework that applies multiple shallow variational quantum circuits to fused multimodal features. Text and image representations extracted by frozen RoBERTa and ViT encoders are processed through bidirectional cross-attention, attentive pooling, and adaptive gated...
  </details>

- **2026-07-15** — Yurui Zhao, Xiang Wang, Zhitao Huang et al. — [Compositional Zero-Shot Recognition based on Tangent Space Disentanglement for Composite Modulation Signals](http://arxiv.org/abs/2607.13463v1)
  <details><summary>📄 Abstract</summary>
  Automatic composite modulation recognition (ACMR) is critical for integrated sensing and communication (ISAC) systems, while conventional approaches face significant challenges due to the semantic coupling between inner-layer and outer-layer modulations in composite modulation (CM), degraded performance under joint hardware and channel imperfections, and limited capability to handle unknown modulation schemes. To this end, we design a disentangled semantic space and propose zero-shot learning fr...
  </details>

- **2026-07-15** — Zhentao Song, Yufeng Gao, Xing Fang et al. — [TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce Search](http://arxiv.org/abs/2607.13398v1)
  <details><summary>📄 Abstract</summary>
  In industrial search and ranking systems, Click-Through Rate (CTR) prediction is shifting from traditional Deep Learning Recommendation Models (DLRM) toward unified, compute-intensive Transformer architectures. This transition is driven by the need to improve Model FLOPs Utilization (MFU) and achieve predictable gains through scaling laws. However, existing approaches such as OneTrans and Climber often adopt an all-in-tokenization strategy when adapting Large Language Model (LLM) architectures, ...
  </details>

- **2026-07-15** — Alexander Langmann, Frederico Pita de Araujo, Mattia Piccinini et al. — [A Hybrid Sampling-Based Trajectory Planner with Game-Theoretic Guidance for Autonomous Racing](http://arxiv.org/abs/2607.13354v1)
  <details><summary>📄 Abstract</summary>
  Autonomous racing demands planning algorithms that balance vehicle dynamics at the limits of handling with strategic decision-making in competitive multi-agent scenarios. Game theory provides a mathematical framework for modeling these interactions, enabling interactive trajectory planning and strategic behaviors, such as blocking. However, directly solving full dynamic games online is computationally prohibitive and challenging to integrate into robust, high-frequency autonomous software stacks...
  </details>

- **2026-07-15** — Joseph M. Cavanagh, Jonathan B. Arnold, Giovanni Battista Alteri et al. — [How Well Can Frontier Large Language Models Generate Structures? High Quality Prediction of Molecular Geometries with Help from Fine-Tuning](http://arxiv.org/abs/2607.13350v1)
  <details><summary>📄 Abstract</summary>
  The power of Large Language Models (LLMs) has led us to investigate how they might be fine-tuned for learning the "language of molecular geometry". The fine-tuning of the LLMs using Cartesian coordinates or Z-matrices provides an extremely simple method for accurately predicting equilibrium structures and diverse sets of conformers of small organic and drug-like molecules with excellent accuracy and outperforming specialized deep learning models. While the most common representation of molecular...
  </details>

- **2026-07-14** — Dmitrij Żatuchin — [Where Does the Noise Come From? A Variance-Components Decomposition of Non-Determinism in LLM Brand Answers](http://arxiv.org/abs/2607.13304v1)
  <details><summary>📄 Abstract</summary>
  Teams measuring whether large language models (LLMs) recommend a brand face a reproducibility problem: ask the same question twice and the answer moves. Practice resamples each prompt a few times (commonly five) and averages, treating within-prompt resampling as the source of the noise. But a measured brand score moves for at least four separable reasons: within-prompt resampling, prompt paraphrase, model identity, and query language. We specify a crossed random-effects (generalizability-theory)...
  </details>

- **2026-07-14** — Sen Yang, Yuen-Hei Yeung — [Resist and Update: Counterfactual Report Coordinates for Incentive-Compatible LLMs](http://arxiv.org/abs/2607.12985v1)
  <details><summary>📄 Abstract</summary>
  Aligned language models routinely misreport under non-evidential incentive pressure: they agree with a confident user or overstate certainty even when their internal belief is unchanged. We cast this as a failure of internal incentive-compatibility (IC) and present a method for learning and certifying counterfactual report mediators that hold a model's reports to a causal contract: invariant to forbidden influences (pressure, prestige, restyling) and responsive to licensed ones (genuine evidence...
  </details>

- **2026-07-14** — Mehak Dhaliwal, Rasta Tadayon, Andong Hua et al. — [From Critic to Confidence: PPO for Language-Based Quantitative Prediction with Confidence Estimation](http://arxiv.org/abs/2607.12687v1)
  <details><summary>📄 Abstract</summary>
  LLMs can perform language-based quantitative prediction from unstructured inputs, but remain susceptible to hallucinations and overconfident errors, making it critical to know not only what a model predicts, but when its predictions can be trusted. We introduce CARE-PPO, a reinforcement learning framework that establishes a connection between loss prediction for uncertainty estimation and actor-critic PPO fine-tuning, enabling joint learning of accurate numerical estimates and reliable confidenc...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 10 papers

- **2026-07-20** — Giorgio Presti — [The Aura in the Machine: Genealogy and the Status of the Work of Art in the Generative Era](http://arxiv.org/abs/2607.17940v1)
  <details><summary>📄 Abstract</summary>
  This paper frames Generative Artificial Intelligence (AI) not as an unprecedented technological rupture, but as an industrial-scale manifestation of a deeply rooted historical process. Through a genealogy of generative arts, it shows how AI's questions on authorship and creativity have precise historical precedents.   A taxonomy of generative systems is proposed across three functional categories (medium, artwork, instrument), the attribution of which is editorial rather than ontological.   From...
  </details>

- **2026-07-20** — Samuel Presgraves — [The Autonomous Agency Scale: A Behavioral Framework for Measuring Self-Directed Behavior in AI Systems](http://arxiv.org/abs/2607.17947v1)
  <details><summary>📄 Abstract</summary>
  Existing AI measurement frameworks quantify cognitive capability, task automation, or catastrophic risk, but none measure autonomous agency: the extent to which a system behaves in a self-directed way. A system can saturate capability benchmarks while remaining entirely reactive, acting only when prompted and ceasing all activity when a task completes. We introduce the Autonomous Agency Scale (AAS), a behavioral framework that scores AI systems on a 0-5 lexicon across seven dimensions of agency:...
  </details>

- **2026-07-20** — Yechao Hong, Haiquan Qiu, Yaqing Wang et al. — [Mechanistic Attention Guidance for Agent Memory Refinement](http://arxiv.org/abs/2607.17621v1)
  <details><summary>📄 Abstract</summary>
  Existing self-evolving memory systems mainly improve agent memory based on textual outputs, such as task trajectories and reflections. However, this text-based paradigm rarely incorporates internal mechanistic signals, leaving how retrieved memory is actually utilized during task execution underexplored. This limitation can lead to unreliable error attribution and hallucinated memory modifications. In this work, we show that retrieval-head attention provides a mechanistic signal for revealing se...
  </details>

- **2026-07-19** — Aleksander Fafuła — [Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families](http://arxiv.org/abs/2607.17427v1)
  <details><summary>📄 Abstract</summary>
  Abliteration - deleting a model's refusal direction from its weights - is the standard recipe behind popular "uncensored" open-weight models. We show the surgery is not clean. As a disposition probe we use 21,600 decisions under uncertainty - weekly up/down calls on 60 Warsaw Stock Exchange equities over 18 weeks, replayed through a frozen pipeline so the decision-layer model is the only variable. The task elicits no refusals at all, so any between-arm delta is pure side effect. Holding provenan...
  </details>

- **2026-07-19** — Xichen Zhang, Yingjie Zhang, Tianshu Sun — [A Diagnostic Framework for AI Agent Behavior](http://arxiv.org/abs/2607.17149v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act within the same clinical, political, scientific, and social systems that behavioral scientists study. Evaluating these systems requires source-level diagnosis: the same behavioral pattern may arise from an agent representational substrate or from the roles, objectives, interaction structures, and governance rules that shape its expression. This Perspective proposes a diagnostic framework for AI agent behavior: layer attribution. The foundational computational layer def...
  </details>

- **2026-07-18** — Anik Jha — [Half the Experts, All the Code: One-Shot Domain Pruning of Mixture-of-Experts LLMs for Coding](http://arxiv.org/abs/2607.16721v1)
  <details><summary>📄 Abstract</summary>
  The strongest open-weight coding models are mixture-of-experts (MoE) networks: most of their size comes from large pools of "expert" subnetworks, of which only a few act on any token. That pool is why these models do not fit on the machines most developers own, yet for a user who only wants coding help, most experts encode abilities that will never be invoked. We ask how many experts can be removed, and which, by pruning two recent open-weight MoE models from different families (Qwen3.6-35B-A3B ...
  </details>

- **2026-07-18** — Sharath Naganna, Tanvir Ahmed Sijan, Uddipta Kalita — [Are Arithmetic Heuristic Neurons Form-Invariant? A Mechanistic Analysis of Symbols, Text, and Code in LLMs](http://arxiv.org/abs/2607.16693v1)
  <details><summary>📄 Abstract</summary>
  Large language models often succeed on one formulation of a problem while failing on an equivalent formulation. Whether these failures arise from distinct internal circuits or different activation states of a shared circuit remains unknown. Recent mechanistic interpretability studies suggest that arithmetic in LLMs emerges from a "bag of heuristics," encoded by a sparse set of MLP neurons that represent distinct arithmetic strategies. We investigate whether arithmetic heuristic neurons are form-...
  </details>

- **2026-07-17** — Muness Castle, Eric Rubeck — [Agentic Synthesis against Counterexample-Supplemented Sketches](http://arxiv.org/abs/2607.15854v1)
  <details><summary>📄 Abstract</summary>
  Coding agents can fix a failing example without preserving the domain rule that made it fail, so later generations can repeat the same plausible mistake. We present agentic synthesis against counterexample-supplemented sketches, a repository-native method for systems whose governing policy is discovered during implementation. A human starts with a partial, code-shaped sketch, and a coding agent generates the first implementation. When a concrete failure exposes missing or mistaken policy, an ope...
  </details>

- **2026-07-17** — Tianyun Zhong, Wangyi Jiang, Wei Wang et al. — [Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery](http://arxiv.org/abs/2607.15766v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) excel at answering pre-specified questions, yet their ability to navigate the open-ended, pre-conclusion stage of discovery remains largely unmeasured. We introduce Prospective Hypothesis Discovery (PHD), which asks models to autonomously construct grounded, discriminative, and testable hypothesis spaces from inconclusive evidence, including anomalous observations and fragmented records, to guide subsequent investigation. To evaluate this capability, we introduce Hyp...
  </details>

- **2026-07-15** — Hyunkyung Han, Min Jung Kim — [Anatomically Faithful but Temporally Blind: Auditing Attribution for Left-Ventricular Ejection-Fraction Estimation from Echocardiography](http://arxiv.org/abs/2607.13738v1)
  <details><summary>📄 Abstract</summary>
  Background and Objective: Deep video models estimate left-ventricular ejection fraction (EF) from echocardiography with near-expert accuracy, and post-hoc attribution (Chefer relevance for transformers, Grad-CAM for CNNs) is increasingly used to certify that models "look at the right place." Yet whether these explanations are faithful both spatially and temporally is unaudited. Because EF is defined by the end-systolic (ES) and end-diastolic (ED) frames, a faithful explanation must localize the ...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-07-14** — Oleg Solozobov — [Agent-Safety Evaluations as Load-Bearing Evidence: A Vendor-Neutral, Cross-Harness Reconstructability Metric](http://arxiv.org/abs/2607.12469v1)
  <details><summary>📄 Abstract</summary>
  Many agent-safety evaluation results are not yet load-bearing evidence: identical nominal outcomes (task success, attack success, monitor scores) may sit atop materially different evidence regimes. No vendor-neutral, runnable instrument scores reconstructability as an evaluation-validity metric: whether captured evidence can reconstruct the decision a claim depends on. This paper introduces a property-level reconstructability metric over eight decision-property classes and a cross-harness adapte...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 2 papers

- **2026-07-19** — Ziteng Hu, Jiachi Chen, Wenhao Lv et al. — [When LLMs Over-Answer: Measuring and Mitigating Quality Issues in LLM-Based Hardware Description Language Question Answering](http://arxiv.org/abs/2607.17063v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of large language models (LLMs) has led practitioners to increasingly rely on them for answering questions about hardware description languages (HDLs). Because HDL is ultimately synthesized into physical hardware, an imprecise or redundant answer can propagate into timing violations or non-synthesizable logic that surface only late in the design flow, making the quality of HDL answers especially consequential. However, the quality of LLM-generated responses, particularly in...
  </details>

- **2026-07-18** — Baochen Fu, Wenzhi Deng, Baihao Jin et al. — [Can Multimodal Large Language Models Understand OCT?](http://arxiv.org/abs/2607.16609v1)
  <details><summary>📄 Abstract</summary>
  Optical coherence tomography (OCT) imaging is essential for the diagnosis and treatment of retinal diseases. Although multimodal large language models (MLLMs) have demonstrated considerable potential in medical image analysis, existing benchmarks largely reduce OCT understanding to coarse-grained disease classification or isolated visual question answering, leaving the complete cognitive process from visual perception to clinical reasoning insufficiently evaluated. To address this limitation, we...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 167 papers

- **2026-07-20** — Sadra Sabouri, Zeinabsadat Saghi, Jordan Lee Boyd-Graber et al. — [It Matters How You Say It: Exploring Rhetorical Patterns for AI-Assisted Information Evaluation](http://arxiv.org/abs/2607.17627v1)
  <details><summary>📄 Abstract</summary>
  Prior work on AI-assisted information evaluation has largely focused on what AI systems communicate, comparing explanation types and formats, with responses predominantly cast in directive rhetoric where the system delivers a verdict and the user passively accepts it. While debate-style interactions have recently shown promise in prompting critical evaluation over deference, the rhetorical patterns that structure AI responses and how they might induce reflection, uncertainty, or independent reas...
  </details>

- **2026-07-20** — Sheng-Yu Wang, Yotam Nitzan, Aaron Hertzmann et al. — [The Many Senses of Visual Similarity: A Text-Prompted Image Perceptual Metric](http://arxiv.org/abs/2607.18237v1)
  <details><summary>📄 Abstract</summary>
  Human visual similarity judgments are context-dependent. For example, two images may be similar in shape but distinct in color. Existing perceptual similarity metrics, however, collapse these nuances into a single scalar value, offering no mechanism to condition on specific aspects. To bridge this gap, we introduce a large-scale dataset of human similarity judgments over image triplets, where each triplet is annotated across multiple, free-form semantic aspects of similarity. Benchmarking a broa...
  </details>

- **2026-07-20** — Dingyun Zhang, Lixue Gong, Wei Liu — [FlowMimic: Mask-free Visual Editing and Generation with Pixel-pair Warped Flow Field for Online Video Editing Data Generation and Modality Mimicry](http://arxiv.org/abs/2607.18227v1)
  <details><summary>📄 Abstract</summary>
  In line with the prevailing direction of vision research, we explore the integration of both generation and editing capabilities for video and image modalities within a single model. Current approaches to collecting video editing data typically depend on labour-intensive, time-consuming curated procedures--involving object mask annotation, the use of error-introducing pair synthesis via I2V model and ControlNet-like guidance, and VLM-based quality filtering or refinement--and demonstrate limited...
  </details>

- **2026-07-20** — Peiran Xu, Jiaqi Zheng, Ziyou Wang et al. — [UniETP: Unifying Environments for Generalizable Embodied Task Planning](http://arxiv.org/abs/2607.18062v1)
  <details><summary>📄 Abstract</summary>
  This paper focuses on the problem of Embodied Task Planning, where an agent is required to execute a sequence of atomic actions within an interactive environment to complete a user-specified task. Though a variety of simulators and datasets have previously been built for this task, these efforts are largely isolated, with each using its own observation format, action type, and task domain. This fragmentation complicates comprehensive model evaluation and hinders the scalability of training data....
  </details>

- **2026-07-20** — Atish Kumar Dipongkor, Talank Baral, Wing Lam et al. — [Test Coverage Analysis of Agentic Pull Requests](http://arxiv.org/abs/2607.18057v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents increasingly submit complete pull requests (PRs) with minimal human intervention, shifting software development from AI-assisted to autonomous workflows. As these agents become more prevalent, ensuring the code they generate is adequately tested, by existing tests or by tests the agents write, is critical to preventing regressions, yet little is known about testing in agentic PRs. To address this gap, we analyze 4882 agent-generated PRs from the AIDev dataset (532 Java and 4350 ...
  </details>

- **2026-07-20** — Lingfeng Zhang, Zhanguang Zhang, Liheng Ma et al. — [Anticipate Before Acting: Future-State-Conditioned Vision-Language Navigation](http://arxiv.org/abs/2607.18042v1)
  <details><summary>📄 Abstract</summary>
  End-to-end vision-language navigation (VLN) with causal vision-language models can map instructions and egocentric observations directly to actions, but standard behavior cloning supervises only the next action and does not explicitly train the policy state to be predictive of future visual outcomes. We first ask a diagnostic question: if the policy is given an expert-trajectory future image as privileged input at training and testing time, is that additional visual evidence useful for choosing ...
  </details>

- **2026-07-20** — Lukáš Viceník, André Sopczak, Oleksandr Shekhovtsov — [Benchmarking Machine Learning Architectures for ttH Multilepton Signal Sensitivity](http://arxiv.org/abs/2607.18022v1)
  <details><summary>📄 Abstract</summary>
  Statistical testing for signal discovery and signal-strength estimation in high-energy physics increasingly relies on machine-learning models trained on simulated data. We present a synthetic dataset for $t\bar t H$ multilepton signal--background classification and perform a systematic evaluation of machine-learning models ranging from the widely used XGBoost for tabular data to LorentzNet, which processes events with built-in Lorentz symmetry. Existing studies often differ in feature definition...
  </details>

- **2026-07-20** — Martino M. L. Pulici, Cuong Xuan Chu, Evgeny Kharlamov et al. — [MADA-RL: Multi-Agent Debate-Aware Reinforcement Learning for Parameter-Efficient Reasoning in Compact Models](http://arxiv.org/abs/2607.18006v1)
  <details><summary>📄 Abstract</summary>
  Large language models achieve strong reasoning performance, but often at prohibitive training cost - a challenge that is especially acute for compact models ($\leq 4 \, \mathrm{B}$ parameters) trained under limited budgets. We introduce MADA-RL, a post-training framework that specializes compact models into generator and critic roles and trains them with a debate-aware learning signal, fine-tuning only a small subset of parameters via LoRA adapters. Our central contribution is a counterfactual c...
  </details>

- **2026-07-20** — Bingyang Wu, Chao Jin, Zili Zhang et al. — [ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels](http://arxiv.org/abs/2607.18002v1)
  <details><summary>📄 Abstract</summary>
  LLMs scale Mixture-of-Experts (MoE) parameters for superior intelligence, but massive weights and dynamic computation impede efficient serving. Existing instance-level prefill-decode disaggregation isolates the phases on separate full-model replicas. As MoE weights grow, each instance may span tens to hundreds of GPUs, making resource allocation increasingly coarse. Configured prefill-to-decode ratios thus often mismatch demand, overprovisioning one phase while overloading the other. Prefill-dec...
  </details>

- **2026-07-20** — Yue Shui, Chenyu Ma, Hangfei Xu et al. — [Harness Engineering for LLM-Driven GPU Kernel Generation](http://arxiv.org/abs/2607.17979v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can assist GPU kernel generation, but their practical effectiveness depends on whether generated code can be reliably constrained, validated, profiled, and selected. This paper presents a harness-centered system for LLM-driven GPU kernel optimization in the MLSys 2026 FlashInfer AI Kernel Generation Contest on NVIDIA Blackwell B200 GPUs. The system separates an evaluation harness from a profile-backed optimization controller: the harness enforces compilation, correct...
  </details>

- **2026-07-20** — Kehan Li, Bohan Hou, Minghao Zhu et al. — [RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation Model](http://arxiv.org/abs/2607.17977v1)
  <details><summary>📄 Abstract</summary>
  We present RynnBrain 1.1, a family of embodied foundation models spanning 2B, 9B, and 122B-A10B scales. Trained with a unified spatio-temporal and physically grounded framework, RynnBrain 1.1 supports embodied perception, spatial reasoning, localization, and planning. Compared with RynnBrain 1.0, it further introduces contact-point prediction across the model family and native 3D grounding for the 2B and 9B models, yielding representations and outputs that are more directly aligned with robot ma...
  </details>

- **2026-07-20** — Shotaro Kawano, Keiichiro Toda, Miu Tamamitsu et al. — [Femtosecond-to-millisecond holographic imaging of laser ablation dynamics](http://arxiv.org/abs/2607.17919v1)
  <details><summary>📄 Abstract</summary>
  Femtosecond laser ablation redistributes optically deposited energy across electronic, structural, mechanical, and thermal degrees of freedom over timescales from femtoseconds to milliseconds. However, these coupled processes are usually measured in separate temporal ranges and through different observables, limiting quantitative comparison between early transient dynamics, residual heating, and final morphology. Here we introduce pump-probe holographic imaging that reconstructs amplitude- and p...
  </details>

- **2026-07-20** — Federico Biagi, Dario Onfiani, Simone Silenzi et al. — [Receiver-Centered Robot-to-Human Handover with Grasp-Aware Object Orientation](http://arxiv.org/abs/2607.17839v1)
  <details><summary>📄 Abstract</summary>
  Collaborative robots are increasingly sharing workspaces with human operators, making tool handover a frequent and safety-critical micro-interaction. However, traditional static handovers often lead to awkward grasps when handling asymmetric industrial tools. This paper presents a receiver-centered voice-driven adaptive handover system for mechanical tools, built on a Franka cobot. Using an LLM for intention recognition and MediaPipe for real-time 3D hand tracking, the framework dynamically adju...
  </details>

- **2026-07-20** — Huiri Tan, Yikun Wang, Puyang Zhang et al. — [ETAS: An Effect-Typed Language for Agent Systems](http://arxiv.org/abs/2607.17780v1)
  <details><summary>📄 Abstract</summary>
  ETAS is a programming language for agent systems that treats model-backed agents, tool calls, prompts, typed memory, human approvals, policies, and execution traces as semantic program elements rather than library conventions. It separates deterministic computation from agentic nondeterminism and externally visible actions while preserving a direct programming style.   We present the core design of ETAS. Its static semantics assigns ordinary types through spec conformance and tracks each computa...
  </details>

- **2026-07-20** — Katarzyna Filus, Sebastian Pokuciński — [Measuring Monosemanticity in Sparse Autoencoders via Latent Activation Coherence](http://arxiv.org/abs/2607.17770v1)
  <details><summary>📄 Abstract</summary>
  Within Explainable Artificial Intelligence, mechanistic interpretability uses Sparse Autoencoders (SAEs) to extract more interpretable features from neural representations. However, assessing their monosemanticity, and thus explanation quality, remains challenging. Existing metrics require external concept labels or depend on pretrained embedding models, making them sensitive to encoder's geometry. We introduce the Tversky Monosemanticity Score (TMS), a label-free metric that operationalizes mon...
  </details>

- **2026-07-20** — Ziteng Li, Yanan Xin, Tina Comes et al. — [Towards Reliable Zero-Shot Crowd Forecasting: Evaluating Time Series Foundation Models for Special Event Pedestrian Forecasting](http://arxiv.org/abs/2607.17758v1)
  <details><summary>📄 Abstract</summary>
  Managing massive crowds during infrequent special events requires reliable real-time pedestrian-flow forecasting to ensure public safety and operational efficiency. However, supervised forecasting methods face limitations in these contexts due to scarce historical data, heterogeneous data distributions, and short in-event observation windows. To effectively support operational decision-making, forecasts should provide not only accurate point estimates but also informative predictive uncertainty....
  </details>

- **2026-07-20** — Weijing Wang, Zan Wang, Dong Wang et al. — [KernelDiag: Agent-Based Root Cause Diagnosis for Kernel Crashes](http://arxiv.org/abs/2607.17722v1)
  <details><summary>📄 Abstract</summary>
  The Linux kernel is one of the most complex software systems, where automated fuzzing continuously exposes thousands of crashes, yet root-cause diagnosis remains a manual and time-consuming bottleneck. Existing LLM-based root cause analysis (RCA) techniques, effective for distributed systems, do not readily generalize to kernel debugging due to sparse low-level artifacts, heterogeneous diagnostic evidence (e.g., syscalls, logs, and crash reports), and complex non-linear fault propagation that de...
  </details>

- **2026-07-20** — Chuheng Du, Junyi Chen, Hanlin Tang et al. — [C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference](http://arxiv.org/abs/2607.17715v1)
  <details><summary>📄 Abstract</summary>
  Long-context inference is central to modern large language model (LLM) applications such as retrieval-augmented generation and multi-document reasoning. To mitigate the growing inference cost, recent work has explored key-value (KV) cache reuse to reduce redundant prefill computation. However, existing reuse methods primarily focus on computation savings and overlook a critical bottleneck in long-context LLM serving: the cost of storing and accessing large KV caches. While KV compression appears...
  </details>

- **2026-07-20** — Cheng Huan, Hongwei Yuan — [An Adjoint-Sensitivity Framework for Lost-in-the-Middle Phenomena in Causal Residual Transformers](http://arxiv.org/abs/2607.17696v1)
  <details><summary>📄 Abstract</summary>
  We develop an adjoint-sensitivity framework for positional influence in causal residual Transformers and separate unconditional analytic results from conditional boundary-shape conclusions. The principal unconditional theorem is the residual-to-depth-flow estimate for layer controls converging in $L^1$, complemented by a finite-token-to-Volterra attention estimate that explicitly controls the first cells near the causal endpoint. We define a normalized adjoint-energy influence density and derive...
  </details>

- **2026-07-20** — Mansur Arief, Nur Ahmad Khatim, Ali Akarma et al. — [Integrating High-Level Requirements to Low-Level Tests with Machine-Readable V&V Specifications](http://arxiv.org/abs/2607.17686v1)
  <details><summary>📄 Abstract</summary>
  Modern software teams have mature tools for low-level testing, such as pytest, JUnit, and Jest, which make it inexpensive to write unit tests and run them on every commit. Systems engineering, in parallel, has developed rigorous principles for design verification and validation (V&V), which has worked very well across engineering discipline to align user expecations and requirements with developers' deliverables. In practice, however, the two rarely connect, and the link between users' high-leve...
  </details>

- **2026-07-20** — Awni Altabaa, John Lafferty — [Uncovering Latent Reasoning Strategies in Language Models](http://arxiv.org/abs/2607.17674v1)
  <details><summary>📄 Abstract</summary>
  A language model $p_θ(y \mid x)$ trained on reasoning tasks learns to solve problems via multiple distinct strategies, yet these strategies are implicit and entangled within the model's response distribution. We study the problem of decomposing the response distribution of a given pretrained language model into a structured, strategy-conditioned representation. Specifically, we learn a latent-variable factorization $p_θ(y \mid x) \leadsto (r_φ(z \mid x), g_φ(y \mid x,z))$, where a router $r$ map...
  </details>

- **2026-07-20** — Qingcan Kang, Mingyang Liu, Shixiong Kai et al. — [Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory](http://arxiv.org/abs/2607.17545v1)
  <details><summary>📄 Abstract</summary>
  Language agents depend on memory across interactions. However, the limited context windows of large language models (LLMs) and their inference costs constrain how much memory can be used at once. Existing systems mainly follow two strategies: memory retention and memory consolidation. Retention keeps raw records and preserves exact details, but relevant evidence may not fit under a tight budget; consolidation compresses and combines records, improving coverage per token but risking the loss of q...
  </details>

- **2026-07-20** — Qianwen Zhao, Long Wang — [Predicting Grasping Compliance in Robotic Hands through Analytical-Model-Informed Neural Networks](http://arxiv.org/abs/2607.17541v1)
  <details><summary>📄 Abstract</summary>
  In robotic manipulation studies, grasping is often treated as a binary success or failure problem, usually defined by whether the object simply stays in the hand. For forceful tool use, however, this view is insufficient because grasp compliance becomes a critical factor governing how the hand and tool behave under load. Compliance arises from coupled kinematics, grasp configuration, passive mechanics, and contact conditions, producing nonlinear behavior in which deformation and interaction forc...
  </details>

- **2026-07-20** — Jinyuan Deng, Zhengrui Chen, Xufeng Wei et al. — [Can AI Agents Really Complete RTL-to-GDS? Lessons from Benchmarking Tool-Interactive EDA Workflows](http://arxiv.org/abs/2607.17528v1)
  <details><summary>📄 Abstract</summary>
  LLM-driven agent systems have emerged as a promising paradigm for electronic design automation (EDA), demonstrating strong potential for automating complex design workflows. However, existing evaluations primarily examine individual language models on isolated EDA tasks, providing limited insight into how different agent systems perform across complete EDA flows. In this work, we present FluxBench, a systematic evaluation of AI agents on end-to-end EDA workflows under unified prompts, tool envir...
  </details>

- **2026-07-20** — Kwan Soo Shin, In Seok Kang, Munho Lee — [After the Euclidean Highway: Hyperbolic Expert AI as the Next Innovation](http://arxiv.org/abs/2607.17513v1)
  <details><summary>📄 Abstract</summary>
  Expert domains are trees; the Euclidean transformer is not, diluting parent-child structure exponentially at depth. The hyperbolic turn left one question unasked: not how much of a network to curve, but where curvature may touch the gradient. Placement is a law, not a knob: the same geometry on a trainable adapter collapses training (seventeen training collapses, ~220 GPU-hours), yet at the loss layer alone it trains without one -- this is HySAT (Hyperbolic Structure-Aware Training), hyperbolic ...
  </details>

- **2026-07-20** — Masashi Sekine — [Mean-field equilibrium price formation under single-default risk](http://arxiv.org/abs/2607.17502v1)
  <details><summary>📄 Abstract</summary>
  We study equilibrium price formation in an incomplete financial market with a large population of agents, where stock prices are subject to a single-default event. Agents are assumed to be heterogeneous in their risk aversion and terminal liabilities, and maximize exponential utility of terminal net wealth. We first characterize each agent's optimal strategy by a quadratic-growth backward stochastic differential equation (BSDE) driven by Brownian motions and a compensated default martingale. We ...
  </details>

- **2026-07-20** — Oscar Perez Mora — [The Because-Calculus: Separating Production, Existence, and Interpretation in Computation](http://arxiv.org/abs/2607.17450v1)
  <details><summary>📄 Abstract</summary>
  Handler calculus conflates resumable and non-resumable effect operations through a single do construct, distinguished only by result type annotation. This conflation does not compromise type safety -- progress and preservation hold -- but it permits resumption bindings for non-resumable operations, creating vacuous bindings that the because-calculus eliminates at compile-time. The because-calculus structurally separates registration (non-resumable, void-returning) from attestation (resumable, no...
  </details>

- **2026-07-20** — Kento Kawaharazuka, Yoshiki Obinata, Hirokazu Ishida et al. — [MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation](http://arxiv.org/abs/2607.17970v1)
  <details><summary>📄 Abstract</summary>
  The global competition for developing robotic foundation models is intensifying. Among the data collection systems used for dual-arm robots, ALOHA is representative of being low-cost and open-source, and is widely adopted by researchers as a de facto standard. However, due to its limited ability to generate high forces and speeds, it is difficult to handle heavy objects or perform fast manipulations. To address this, we developed MEVION, a low-cost and open-source dual-arm robot data collection ...
  </details>

- **2026-07-20** — Wen Qiu, Zhiqiang He, Wei Zhao et al. — [PRIME: Plasticity Recovery in Multi-Agent Environments for UAV-Assisted Emergency Communication Networks](http://arxiv.org/abs/2607.17922v1)
  <details><summary>📄 Abstract</summary>
  Most reinforcement learning controllers for these networks assume stationary conditions, and the few that handle change react to the external environment while leaving the network's internal state unexamined. We show that sustained non-stationarity damages this internal state directly: as objectives shift, neurons progressively fall dormant and the shared policy loses the capacity to learn. The obvious remedy, resetting dormant neurons, is unsafe under shared-parameter multi-agent training: many...
  </details>

- **2026-07-20** — Ziyao Wang, Yuqi Li, Wenxing Zheng et al. — [FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](http://arxiv.org/abs/2607.17803v1)
  <details><summary>📄 Abstract</summary>
  Projector-camera (ProCams) systems achieve active scene perception and controllable appearance manipulation via structured illumination, serving as a core infrastructure for spatial augmented reality, projection mapping, and surface reflectance acquisition. Existing inverse-rendering methods for ProCams deliver high-fidelity results but rely on time-consuming per-scene optimization, while mainstream feed-forward 3D reconstruction models produce baked appearance that cannot adapt to spatially var...
  </details>

- **2026-07-20** — Ziyi Liu, Grace Zhang — [Generalize and Guide: Decomposing Rewards for Few-Shot Inverse Reinforcement Learning](http://arxiv.org/abs/2607.17760v1)
  <details><summary>📄 Abstract</summary>
  Inverse reinforcement learning (IRL) provides a powerful framework for learning from demonstrations. However, real-world tasks often exhibit substantial natural variations (e.g., picking up mugs with varying shapes), making it impractical to collect demonstrations that fully specify a new task under every possible scenario. In practice, while demonstrations for the target task are limited, it is often easier to obtain datasets of heterogeneous but related behaviors. This motivates the problem of...
  </details>

- **2026-07-20** — Ziming Wang, Bingbing Li, Karl H. Johansson et al. — [On Optimal Event-Triggered Distributed Control for Stochastic Multi-Agent Systems via Reinforcement Learning](http://arxiv.org/abs/2607.17635v1)
  <details><summary>📄 Abstract</summary>
  We propose a reinforcement learning (RL) based optimal distributed control algorithm for the multi-agent systems (MASs) with stochastic uncertainties. Unlike existing methods, during the optimized backstepping design process, we use the actor-critic-identifier structure. The actor neural network is used to reflect control behavior, the critic neural network works to evaluate control performance and the unknown stochastic uncertainties are handled by identifier neural network. Furthermore, a low-...
  </details>

- **2026-07-20** — Jie Hu — [Oracle Gap and Signal Fidelity: A Fixed-Pool Diagnostic for Test-Time Collaboration](http://arxiv.org/abs/2607.17531v1)
  <details><summary>📄 Abstract</summary>
  Test-time collaboration, including self-consistency, best-of-N selection, critic models, and verifier pipelines, is often credited with broadly improving LLM reasoning, yet its gains are uneven and sometimes negative. We ask when training-free collaboration should be expected to help. For a fixed candidate pool, we decompose a selector or verifier's net gain into measurable factors: recoverable mass, verification-signal coverage, conditional selection quality, and harm to already-correct outputs...
  </details>

- **2026-07-20** — Harish Chandramouleeswaran, Prajakta Nimbhorkar — [Nonexistence of Simultaneously EF1 and Pareto Optimal Allocations for Submodular Valuations](http://arxiv.org/abs/2607.18220v1)
  <details><summary>📄 Abstract</summary>
  The existence of allocations of indivisible goods that are simultaneously fair (envy-free up to one item (EF1)) and efficient (Pareto optimal (PO)) when agents have monotone submodular valuations has been a longstanding open problem. We settle this question negatively by giving an example with two agents where no allocation is simultaneously EF1 and PO. We also show that determining the existence of such allocations is NP-hard for monotone submodular valuations. Our example uses (unweighted) cov...
  </details>

- **2026-07-20** — Hang Zhang, Warren J. Gross — [PPL-Factory: Task-Aware and Budget-Aware Data Selection from Language Modeling to Reasoning](http://arxiv.org/abs/2607.18199v1)
  <details><summary>📄 Abstract</summary>
  Not all training samples contribute equally to large language model fine-tuning. Selecting informative training samples can reduce the computational cost while preserving downstream performance. Many existing data selection methods rely on indirect heuristics, such as data quality, diversity or reasoning trace length. However, the effectiveness of these fixed criteria is task-dependent and difficult to generalize across diverse downstream tasks. Perplexity-based data selection provides a simple ...
  </details>

- **2026-07-20** — Krish Agarwal, Zhuoming Chen, Yanyuan Qin et al. — [FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications](http://arxiv.org/abs/2607.18171v1)
  <details><summary>📄 Abstract</summary>
  Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism. Existing serving systems and auto-parallelism compilers commit to limited transformations and fixed workload assumptions, so achieving high performance on a new application requires hand-crafting an efficient implementation. We present Flas...
  </details>

- **2026-07-20** — Daniela Rojas, Abdulwahab Albassam, Aidan G. Leung et al. — [LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and Applications](http://arxiv.org/abs/2607.18147v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) and agentic AI systems have evolved from natural language tasks to using external tools to plan, retrieve, and act in technical domains. In smart grids, recent work applies agentic schemes to forecasting, optimization, and control, wrapping trusted solvers behind language interfaces and orchestrating multi-step workflows. The literature lacks a unified approach to designing and evaluating such systems. LLMs can produce numerically plausible yet physically infeasible ...
  </details>

- **2026-07-20** — Junhong Lin, Xianda Guo, Kangli Wang et al. — [VGOcc: Learning Visual-Geometric Gaussians for Vision-Centric 3D Driving Occupancy Prediction](http://arxiv.org/abs/2607.18078v1)
  <details><summary>📄 Abstract</summary>
  Vision-only occupancy prediction requires recovering a semantic 3D occupancy field from calibrated surround-view images, where each view provides observations with ambiguous depth along camera rays. Existing methods have progressed from dense structured representations to sparse Gaussian primitives, improving the efficiency of 3D scene representation. However, Gaussian learning still relies primarily on image domain features, which provide limited explicit geometric information for volumetric re...
  </details>

- **2026-07-20** — Kiarash Rezaei, Omran Ayoub, Paolo Monti et al. — [Human Grounded Evaluation of Large Language Models for Optical Network Automation](http://arxiv.org/abs/2607.18068v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly adopted for network automation, yet their output quality and inference cost can vary substantially across LLM families. We present HuGLEN, a stepwise evaluation pipeline that uses an LLM-as-a-judge together with a small set of expert ratings to enable scalable and reproducible comparison of candidate LLMs, and to rank them using a quality efficiency score (QES). We demonstrate HuGLEN for translating outputs from an explainable artificial intelligence...
  </details>

- **2026-07-20** — Chunming Wu, Dafei Qiu, Congde Yuan et al. — [Evidence-in-the-Loop: Trace-Driven Optimization for Customer-Service LLM Agents](http://arxiv.org/abs/2607.18039v1)
  <details><summary>📄 Abstract</summary>
  Production customer-service bots must improve answer quality across iterative releases, yet large language models must not bypass evidence boundaries, policy rules, or human-handoff safeguards. We present an \textbf{Evidence-Grounded Customer-Service Agent Workflow} deployed in a real-world customer-service setting. BM25 recall, issue-title-vector recall, issue-description-vector recall, weighted RRF fusion, and cross-encoder reranking construct grounded FAQ evidence for controlled LLM decisions...
  </details>

- **2026-07-20** — Rui Chu, Yingjie Lao — [HAS: Highlight-guided Attention Steering for Multimodal LLM Video Summarization](http://arxiv.org/abs/2607.17994v1)
  <details><summary>📄 Abstract</summary>
  Video understanding has become more and more important with the growth of Artificial Intelligence (AI) for video generation. Recently, Multimodal Large Language Model(M-LLM) has shown its capability in video understanding. Video summarization, a specific domain of video understanding, has proven its importance for efficient navigation and retrieval. Both video understanding and video summarization require a good selection of key frames in a video. Current video summarization methods heavily focu...
  </details>

- **2026-07-20** — Zijian Zhao, Sen Li — [Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization](http://arxiv.org/abs/2607.17924v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent policy optimization, exemplified by PPO-based methods, is a key branch of cooperative Multi-Agent Reinforcement Learning (MARL). A central design question is how many neighboring agents\footnote{In this paper, "neighbors" refer not only to physical proximity but also to agents whose actions influence one another.} to aggregate in order to effectively utilize global information for cooperation. This decision must be made along two dimensions: in the advantage (which agents' rewards co...
  </details>

- **2026-07-20** — Md. Asaduzzaman Shuvo — [When a Name Is Not a Name: A Benchmark Dataset and Distilled Reasoning for Culturally Entangled Bangla Homographs in Low-Resource LLMs](http://arxiv.org/abs/2607.17828v1)
  <details><summary>📄 Abstract</summary>
  Many Bangla words are at once personal names and culturally loaded common nouns, "Maya" is both a girl's name and a word for affectionate compassion. Choosing the right reading demands cultural knowledge that is scarce in the pretraining data of modern language models. We introduce Culturally Entangled Homograph (CEH) disambiguation and build a Bangla benchmark of 1,516 expert-verified sentences (3,032 labelled occurrences) in which one word appears twice with two distinct readings, each labelle...
  </details>

- **2026-07-20** — Simon Mackenzie, Mashbat Suzuki — [When One Good Is Not Enough: EF1 and Pareto Optimality Are Not Compatible for Submodular Valuations](http://arxiv.org/abs/2607.17811v1)
  <details><summary>📄 Abstract</summary>
  One of the central questions in discrete fair division is whether fairness and efficiency can be achieved simultaneously. For indivisible goods, a canonical relaxation of envy-freeness is envy-freeness up to one good (EF1), while the standard efficiency benchmark is Pareto optimality (PO). In their seminal work, Caragiannis et al. showed that, for additive valuations, EF1 and PO are always compatible, and asked whether this compatibility extends to submodular valuations. This question has since ...
  </details>

- **2026-07-20** — Yijian Li, Xiangru Mu, Changze Li et al. — [VLN-AVP: Zero-Shot Vision-Language Navigation with Hybrid Long-Short-Term Memory for Autonomous Valet Parking](http://arxiv.org/abs/2607.17767v1)
  <details><summary>📄 Abstract</summary>
  Existing methods in Autonomous Valet Parking (AVP) typically rely on pre-built maps, which severely restricts their scalability to unseen environments and open-vocabulary targets. Inspired by the application of Vision-Language Models (VLMs) in Vision-Language Navigation (VLN) tasks, we propose VLN-AVP, a zero-shot navigation framework for AVP tasks. By combining the precise spatial perception of a Bird's-Eye-View (BEV) model with the general intelligence of VLMs, our framework 1) eliminates the ...
  </details>

- **2026-07-20** — Fayçal Aït Aoudia, Jakob Hoydis, Sebastian Cammerer et al. — [Autonomous Discovery of Wireless Communications Algorithms](http://arxiv.org/abs/2607.17762v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-driven evolutionary search is an emerging algorithm-discovery paradigm that has already produced novel results in several scientific fields. Yet its application to wireless communications remains largely unexplored. To bridge this gap, we introduce The AI Telco Engineer (AITE), a framework to autonomously design algorithms for complex communication problems, while navigating performance-complexity tradeoffs. We showcase AITE on two challenging physical-layer problems: ...
  </details>

- **2026-07-20** — Yancheng Zhu, Wanli Ma, Chen Han et al. — [Predictive Training with Latent Imagination for Visual Quadruped Navigation](http://arxiv.org/abs/2607.17574v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement-learning navigation policies for legged robots select actions reactively from current observations and short-term memory, with limited capacity to anticipate how moving obstacles will evolve in the near future. In dynamic environments, this reactivity causes the robot to respond too late because collision risk depends on short-horizon scene structure rather than on current obstacle positions alone. Lightweight predictive supervision applied to the policy's recurrent state during tr...
  </details>

- **2026-07-20** — Vaskar Chakma, Wooyeol Choi — [Self-Directed Spectrum Allocation Framework for Integrated TN-NTN 6G Networks](http://arxiv.org/abs/2607.17561v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a self-adaptive channel assignment framework based on Q-learning, where agents learn optimal policies by observing network load, interference conditions, and temporal traffic dynamics within a Markov decision process (MDP). A multi-objective reward function is designed to jointly optimize system throughput, user fairness, and interference mitigation, while an ε-greedy strategy is employed to facilitate effective exploration. Simulation results demonstrate stable convergence, ...
  </details>

- **2026-07-20** — Hiroshi Ohno — [Lie-Group Mode Connectivity in Quantum Machine Learning from a Dynamical Lie Algebra Perspective](http://arxiv.org/abs/2607.17554v1)
  <details><summary>📄 Abstract</summary>
  Mode connectivity has been widely studied in classical machine learning as a geometric property of low-loss regions in parameter space. In quantum machine learning (QML), however, the physically relevant object is not the parameter vector itself but the unitary transformation implemented by a parameterized quantum circuit. In this study, we formulate mode connectivity on the reachable unitary Lie group generated by the dynamical Lie algebra of the generators. We show that, under a near-minimum c...
  </details>

- **2026-07-19** — Sabrina Saima, Tasin Intisar — [Quantitative Benchmarking of a Split-Field PML FDTD Solver: Slit Diffraction, and Scattering from PEC and Dielectric Cylinders](http://arxiv.org/abs/2607.17360v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a two-dimensional TMz finite-difference time-domain (FDTD) solver based on Yee's scheme for modeling radiation from an infinitely long z-directed line current, with the open region truncated by a Berenger split-field perfectly matched layer (PML). After validating cylindrical-wave propagation and negligible late-time reflections in free space, the solver is applied to three inhomogeneous configurations: (i) diffraction through a one-cell-thick perfectly electrically conductin...
  </details>

- **2026-07-19** — Zhihao Liu, Tianyu Wang, Xi Vincent Wang et al. — [Agentic ERP: Multi-Agent Large Language Model Architecture for Autonomous Enterprise Resource Planning](http://arxiv.org/abs/2607.17331v1)
  <details><summary>📄 Abstract</summary>
  Enterprise Resource Planning (ERP) systems record transactions reliably but still delegate almost all operational decision-making to human specialists, because classical rule-based automation cannot reason about exceptions and monolithic AI assistants degrade when asked to coordinate across functional boundaries. This paper presents Agentic ERP, an expert-system architecture that combines role-aligned large-language-model (LLM) agents with a risk-tiered human-in-the-loop harness and a graph-base...
  </details>

- **2026-07-19** — Murilo Vinicius da Silva, Ricardo V. Godoy, Juliano Negri et al. — [From Perception to Assistance: Open-Vocabulary Shared Autonomy for Robotic Manipulation](http://arxiv.org/abs/2607.17323v1)
  <details><summary>📄 Abstract</summary>
  Teleoperating a robotic manipulator in industrial environments demands precision that camera-based interfaces alone struggle to deliver. The operator must align the end-effector with a target in clutter, under limited depth perception, and without colliding with the surrounding structures. This paper presents a shared-autonomy framework that assists the operator throughout this process. A single RGB-D camera captures the operator's arm motion and hand gestures without wearables, fiducials, or a ...
  </details>

- **2026-07-19** — Param Chordiya — [Lossless but Not Free: An Empirical Anatomy of Speculative Decoding on Consumer Hardware](http://arxiv.org/abs/2607.17283v1)
  <details><summary>📄 Abstract</summary>
  Single-stream autoregressive decoding of large language models is bound by memory bandwidth: each generated token requires one full forward pass through the target model, and successive passes cannot be parallelized. Speculative decoding restructures this computation: a small draft model proposes $K$ tokens autoregressively, the target model scores all of them in one batched pass, and a rejection-sampling rule provably preserves the target model's output distribution. We present a from-scratch, ...
  </details>

- **2026-07-19** — Qing Zong, Yue Guo, Mengxin Yang et al. — [EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and World Model in Interactive Literary World](http://arxiv.org/abs/2607.17250v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces EvolvingWorld, a framework and benchmark for character and world co-evolution in interactive literary worlds. Existing systems either treat interactive literary simulation as static persona imitation or isolated scene generation, failing to capture how characters and worlds evolve together over time. To address this, EvolvingWorld models literary simulation as a long-horizon process where characters interact, scenes progress, and character and world states are persistently ...
  </details>

- **2026-07-19** — Xingjian Tao, Yiwei Wang, Yujun Cai et al. — [LenGuard-GPC: Length Guarding with Guided-Prompt Consistency for Spatial Reasoning Reinforce Learning](http://arxiv.org/abs/2607.17243v1)
  <details><summary>📄 Abstract</summary>
  Multi-view spatial reasoning requires vision-language models to compare visual evidence across images, align object correspondences, and infer spatial relations over long visual contexts, a setting where chain-of-thought reasoning tends to grow verbose without becoming more accurate. Reinforcement learning with verifiable rewards is a natural fit for this task, but standard GRPO reward relies on sparse outcome-level feedback and gives no signal about where a reasoning trajectory goes wrong, nor ...
  </details>

- **2026-07-19** — Chetan Arora, Andreas Vogelsang, Abbi Sharma — [Specifying the Delegated-Autonomy Boundary: Requirements Engineering for Agentic AI](http://arxiv.org/abs/2607.17225v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems do not just predict or recommend; they plan, maintain state, and act in external environments with varying degrees of autonomy. This changes the requirements engineering problem in a specific and under-addressed way: it introduces what we call the delegated-autonomy boundary -- the set of decisions about what may be delegated to the system, under what graduated authority, with what oversight, and how control is returned. Current practices bury these decisions inside prompts, t...
  </details>

- **2026-07-19** — Shivanshu Agnihotri, Snehashis Majhi, Deepak Ranjan Nayak et al. — [Induce to Empower: Improving Lightweight Baselines via Foundation Model Induction for Generalized Polyp Segmentation](http://arxiv.org/abs/2607.17208v1)
  <details><summary>📄 Abstract</summary>
  Automated polyp segmentation in colonoscopy continues to pose challenges due to substantial appearance variations and indistinct polyp boundaries. Although emerging foundation models (FMs) such as DINOv2, SAM, and OneFormer, demonstrate remarkable generalization capabilities, their direct transfer to the polyp segmentation task and deployment in real-time clinical settings are difficult due to lack of large-scale labeled data and high computational demands. In addition, adopting multiple FMs tog...
  </details>

- **2026-07-19** — Pratyush Dhingra, Pramit Kumar Pal, Janardhan Rao Doppa et al. — [ThAME: 3D Memory-Enabled Heterogeneous Accelerator for LLM Mixture of Experts](http://arxiv.org/abs/2607.17074v1)
  <details><summary>📄 Abstract</summary>
  Mixture of Experts (MoE) architectures have emerged as a dominant paradigm for scaling Large Language Models (LLMs). However, MoE inference on conventional hardware is constrained by three fundamental bottlenecks. These encompass the massive memory bandwidth required to fetch non-contiguous expert weights, the non-deterministic scatter-gather traffic generated by input-dependent token routing, and the tail-latency dependency imposed by synchronous expert output aggregation. To address these chal...
  </details>

- **2026-07-19** — Lucky Verma — [Solver-Hard Is Not Model-Hard: A Hardness-Controlled Diagnostic for LLM Constraint Reasoning](http://arxiv.org/abs/2607.17047v1)
  <details><summary>📄 Abstract</summary>
  LLM constraint reasoners are often evaluated near the random-SAT phase transition, confounding density and solver hardness. We test instance-level transfer while near-matching clause density. At aligned size bins, with near-matched density and matched maximum clause width, we compare proof-hard expander-Tseitin and proof-easy ladder-Tseitin formulas, pigeonhole anchors, and density-mismatched controls. Theory separates their resolution hardness; a solver-specific Glucose mean-conflict proxy diff...
  </details>

- **2026-07-19** — Bruno de Andrade — [Critical thresholds and instantaneous norm inflation for super-diffusive integro-differential equations](http://arxiv.org/abs/2607.17430v1)
  <details><summary>📄 Abstract</summary>
  This manuscript investigates the Cauchy problem for a class of nonlinear integro-differential equations governing anomalous super-diffusive transport in $\mathbb{R}^N$. The linear dynamics are driven by a dual-scale memory kernel whose Laplace transform is sectorial and exhibits distinct power-law asymptotics at high and low frequencies. This super-diffusive structure precludes the infinite regularizing capacity characteristic of classical parabolic theory; consequently, the associated resolvent...
  </details>

- **2026-07-19** — Ruogu Chen, Weihua Xiao, Ramesh Karri et al. — [CoEvoP&R: Co-Evolving Placement Objectives with Routing Feedback via Large Language Models](http://arxiv.org/abs/2607.17398v1)
  <details><summary>📄 Abstract</summary>
  Analytical placers rely on differentiable objective functions to guide placement, typically combining intermediate surrogate metrics such as half-perimeter wirelength (HPWL) and cell-density penalties. However, these placement-stage surrogates remain misaligned with downstream routed and timing quality. Prior work reduces this gap with human-designed terms or learned black-box surrogates, but the former requires expert retuning and the latter is difficult to explain, debug, or deploy in analytic...
  </details>

- **2026-07-19** — Jovan Nikolic, Maciej Krzysztof Zuziak, Evangelos Pournaras — [The Optimization Trilemma: Efficiency, Comfort and Fairness in Decentralized Multi-agent Coordination](http://arxiv.org/abs/2607.17311v1)
  <details><summary>📄 Abstract</summary>
  The problem of fair multi-agent coordination in decentralized settings is one of the most pressing challenges for building efficient collaborative systems. Resource allocation is based on optimized collective arrangements accounting for agents' needs. Such coordination should not only be computationally efficient but also account for fairness, i.e., equitable redistribution of costs incurred by all agents. Recent literature has proposed several algorithms that efficiently determine optimal plan ...
  </details>

- **2026-07-19** — Zhanbo Li, Shifeng Wu, Xiangjin Meng et al. — [An Explicit World Model Based on Data-First Ontology: DaoQL Multimodal Storage Validation and Counterfactual Reasoning Evaluation](http://arxiv.org/abs/2607.17269v1)
  <details><summary>📄 Abstract</summary>
  Large language models encode world models implicitly in neural weights, which exposes four structural risks in high-precision domains such as medicine and finance: hallucination, frozen knowledge, poor explainability, and poor modifiability. This paper proposes data-first ontology: LLMs are treated as reasoning and language engines, while deterministic knowledge is moved into an explicit multimodal database, DaoQL. We formalize an explicit world model and show that, under rule independence, dete...
  </details>

- **2026-07-19** — Rong Fu, Yongtai Liu, Xiaowen Ma et al. — [DynImmune-BERT: Dynamic Immune Repertoire Modeling with Neural ODE Driven Continuous Transformers](http://arxiv.org/abs/2607.17244v1)
  <details><summary>📄 Abstract</summary>
  Longitudinal T cell receptor repertoires contain signals of clonal expansion, contraction, disappearance, and reappearance after immune perturbation. Static repertoire language models usually summarize a sample as a bag of sequences, so the sampling interval, sequencing depth, and clone presence pattern are only weakly represented. This paper presents DynImmune-BERT, a continuous time repertoire model for patient level immune status prediction. The method combines depth adaptive centered log rat...
  </details>

- **2026-07-19** — Sally Chen, Roxana Zahedi, Lucy Chhuo et al. — [Harmonised benchmarking of foundation models for single-cell and spatial transcriptomics reveals context-dependent generalisation](http://arxiv.org/abs/2607.17227v1)
  <details><summary>📄 Abstract</summary>
  Single-cell and spatial foundation models promise transferable biological representations, yet their generality remains largely untested across modalities, biological domains and analytical tasks. We benchmarked six representative models, Nicheformer, CellPLM, scGPT-spatial, GenePT, scELMo and Novae, using a harmonised framework spanning scRNA-seq, spatial transcriptomics and Perturb-seq. We evaluated zero-shot and continually pretrained clustering, supervised annotation, marker-gene concordance...
  </details>

- **2026-07-19** — Kui-Wang Choi, Minming Li — [Temporal Fair Division of Indivisible Goods with Structured Constraints](http://arxiv.org/abs/2607.17224v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates temporal fair division, a setting where items are allocated over multiple rounds and agents require cumulative fairness over time. We focus on dynamic extensions of classic fairness notions: Temporal Envy-Freeness Up to Any Good (TEFX), its $α$-TEFX approximation, and Temporal Maximin Share (TMMS). Because these strict fairness criteria are known to be generally impossible to satisfy, we analyze the model under constraints to map the boundary between what is possible and ...
  </details>

- **2026-07-19** — Joseph Lazzaro, Alessio Russo, Aldo Pacchiano — [Non-Asymptotic Best Policy Identification Guarantees in Online Reinforcement Learning](http://arxiv.org/abs/2607.17201v1)
  <details><summary>📄 Abstract</summary>
  In this work we study the Best Policy Identification (BPI) problem in online, tabular Reinforcement Learning. This is an active sequential hypothesis testing problem in which the learner's objective is to identify an optimal policy in a Markov Decision Process (MDP) with high confidence, while minimizing the expected sample complexity to do so. We consider an online setting with deterministic rewards, where the agent must strategically navigate through the MDP in order to effectively explore. Pr...
  </details>

- **2026-07-19** — Kenji Tokuo — [QBism Logic](http://arxiv.org/abs/2607.17174v1)
  <details><summary>📄 Abstract</summary>
  QBism interprets quantum theory as a normative discipline for an agent's probability assignments and their revision across possible experience. This paper develops a logical formalization of that picture. A well-formed core datum consists of an admissible prior space, a finite family of actual measurements, Born kernels, and update kernels. For each such datum, we introduce a guarded dynamic language for histories and posterior states and prove a global reduction theorem. We next consider effect...
  </details>

- **2026-07-19** — Maryam Bajalan, Jean-Pierre Gazeau, Hamed Pejhan — [The de Sitter Scalar Discrete Series: Gupta-Bleuler Structure and Holography](http://arxiv.org/abs/2607.17124v1)
  <details><summary>📄 Abstract</summary>
  We show that scalar discrete-series unitary irreducible representations (UIRs) $Π_{p,0}$ ($p=1,2,\cdots$) of the de Sitter (dS) group $\mathrm{SO}_0(1,4)$ admit a dS-covariant Krein realization on the dS hyperboloid, endowed with a dS-invariant non-degenerate Klein-Gordon (KG) sesquilinear form, in which the group action is indecomposable and organizes naturally into a Gupta-Bleuler triplet. The positive- and negative-norm sectors are already present in the underlying Krein space, whereas a null...
  </details>

- **2026-07-19** — Feng Xue, Wu Chen, Mingshuai Zhao et al. — [DepthART: Scaling Foundation Monocular Depth to Tiny Models](http://arxiv.org/abs/2607.17099v1)
  <details><summary>📄 Abstract</summary>
  Recent geometric foundation models (e.g., Metric3D, Depth Anything and UniDepth) have substantially improved monocular depth estimation (MDE) in both cross-scene generalization and metric-scale prediction, yet these gains have not translated to tiny models. We bridge this gap with DepthART (Depth Anything Rethought for Tiny Models), which is a compact MDE model for on-device deployment across diverse scenes. We first identify two capacity-driven bottlenecks in tiny models: (i) overfitting to dat...
  </details>

- **2026-07-19** — Babak Barazandeh, Subhabrata Majumdar, George Michailidis — [Otap:Structure-Aware Optimal Transport for Evaluating Planning and Execution in Agent Trajectories](http://arxiv.org/abs/2607.17082v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents solve tasks by generating trajectories that interleave planning, tool calls, and intermediate results. Current evaluation metrics reduce such a trajectory to a binary success flag or compare it against a reference by exact matching. A success flag cannot distinguish a sound solution from one that succeeds by luck, and says nothing about why a failed run went wrong. Exact matching penalizes plans that are valid but reordered or decomposed differently from the reference...
  </details>

- **2026-07-19** — Afiq Abdillah Effiezal Aswadi, Haotong Ma, Susan Wei — [What does a Bayes-filtered transformer believe? A predictive Monte Carlo approach](http://arxiv.org/abs/2607.17060v1)
  <details><summary>📄 Abstract</summary>
  A Bayes-filtered transformer (BFT) is a transformer trained on sequences that are generated in two steps: first a latent task is drawn from a prior, then observations are drawn conditional on that task. Trained under autoregressive log loss, the BFT's next-token prediction, in the idealized limit, is the Bayesian posterior predictive distribution (PPD) induced by that prior and that conditional law. In practice the trained BFT is only an approximation of this ideal PPD, raising an interpretive q...
  </details>

- **2026-07-19** — Tarun Tomar — [Searching for Task-Specific Vision Paths: Evolutionary Block Pruning Across Vision-Language Models](http://arxiv.org/abs/2607.17052v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models normally execute the same complete vision encoder for every question, even when OCR, counting, object, attribute, and spatial queries may not require identical computation. We study whether fixed-budget combinations of vision blocks can be skipped without fine-tuning. A shared K-block route skips one searched set of exactly K blocks for every question, while a capability-specific K-block policy selects one same-size route using a known capability label. We introduce a sour...
  </details>

- **2026-07-19** — Xiaonan Luo, Yue Huang, Kehan Guo et al. — [Learning from Synthetic Data without Model Collapse in Iterative Instruction Tuning](http://arxiv.org/abs/2607.17043v1)
  <details><summary>📄 Abstract</summary>
  Model collapse is a central challenge in learning from synthetic data: as later-generation large language models (LLMs) are trained on an increasing proportion of model-generated data, performance can degrade due to narrowed coverage and accumulated bias. Existing work mainly studies how to bound this degradation. In iterative model evolution, however, the more meaningful objective is to ensure that each successive model improves over its predecessor, which requires diagnosing collapse at a gran...
  </details>

- **2026-07-18** — Aditya Saraf, Giannis Kaklamanis, Sarisht Wadhwa et al. — [Censorship Resistance and Throughput with Multiple Concurrent Proposers](http://arxiv.org/abs/2607.16995v1)
  <details><summary>📄 Abstract</summary>
  Censorship resistance is the defining advantage of blockchains over their centralized counterparts. Yet block proposers censor transactions for many reasons, from legal consequences to economic incentives. We study economically-incentivized censorship, modeled by an adversary who bribes proposers to exclude a target transaction, and define the economic censorship resistance (eCR) of a transaction as the adversary's expected cost of successful censorship divided by the user's expected payment for...
  </details>

- **2026-07-18** — Ye Lu, Yihan Yan, Zhaoyang Zhang et al. — [Do Speech Tokens Leak Voiceprints? Speaker Inversion Attacks Against End-to-End Speech Language Models](http://arxiv.org/abs/2607.16870v1)
  <details><summary>📄 Abstract</summary>
  End-to-end speech language models increasingly represent user speech with speech tokens rather than relying exclusively on cascaded ASR--LLM--TTS pipelines. Although these tokens support expressive and low-latency spoken interaction, they may also preserve sensitive speaker characteristics. We investigate whether exposed speech tokens leak voiceprints and formulate this risk as a speaker inversion attack. We introduce Audio BERT (AuB), a trainable model that constructs token embeddings from disc...
  </details>

- **2026-07-18** — Mingxuan Li,  Kaizhan-Lee, Elias Bareinboim — [Counterfactual Shapley Credit Assignment](http://arxiv.org/abs/2607.16999v1)
  <details><summary>📄 Abstract</summary>
  The Credit Assignment Problem (CAP) is fundamental to developing efficient and explainable Reinforcement Learning (RL) agents. Existing frameworks, whether relying on temporal contiguity or hindsight-conditioned reward reweighting, frequently fail to attribute properly between an agent's policy (skill) and environmental stochasticity (luck). A principled approach to CAP must isolate the true causal drivers of observed outcomes from spurious correlations and environmental randomness. We introduce...
  </details>

- **2026-07-18** — Soumya Samrat Mandal, Maxim Lyutikov — [Electromagnetic Emission from a Black Hole Evaporating in External Magnetic Field](http://arxiv.org/abs/2607.16880v1)
  <details><summary>📄 Abstract</summary>
  We describe a classical (non-quantum) radiation process: additional (to Hawking) emission by a black hole evaporating in an external magnetic field in vacuum. The electromagnetic radiation process is completely electric charge-free and bears some resemblance to the Gertsenshtein-Zel'dovich effect. The time evolution of the spacetime metric perturbs a static background magnetic field, inducing a radiative field that acts as an effective electromagnetic source even in the absence of physical charg...
  </details>

- **2026-07-18** — Haolin Ren, Ziyang Huang, Chenhao Yuan et al. — [Trace-Based On-Policy Distillation for Masked Diffusion Language Models](http://arxiv.org/abs/2607.16872v1)
  <details><summary>📄 Abstract</summary>
  Diffusion large language models (dLLMs) are a promising alternative to autoregressive generation. However, reasoning-oriented post-training for dLLMs remains challenging. Supervised fine-tuning (SFT) for dLLMs requires dense but often off-policy masked states, while reinforcement learning (RL) relies on sparse rewards or value modeling. This paper proposes \textbf{trace-based on-policy distillation (TOPD)}, a teacher-supervised framework that transfers reasoning ability to a target dLLM without ...
  </details>

- **2026-07-18** — Yanni Dong, Minghua Liu, Meiling Zhu et al. — [Beyond Semantic Equivalence: Logical Graphs for LLM Uncertainty Quantification](http://arxiv.org/abs/2607.16868v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) often produce confidently stated yet unreliable outputs, posing critical challenges for deployment in safety-sensitive applications. Existing uncertainty metrics such as semantic entropy capture agreement at the level of semantic equivalence, but largely ignore the logical relationships between distinct answers. As a result, they tend to overestimate uncertainty and falsely flag hallucinations in settings where generated responses are diverse in form yet logically co...
  </details>

- **2026-07-18** — Roberto Pietrantuono, Antonio Guerriero, Pouya Sattari — [Schema-Constrained Document-Level Event Argument Extraction with Lightweight LLM Fine-Tuning](http://arxiv.org/abs/2607.16808v1)
  <details><summary>📄 Abstract</summary>
  Event Argument Extraction (EAE) converts documents into structured event records by identifying argument spans and assigning them schema-defined roles. Document-level EAE is challenging due to long-range dependencies between triggers and arguments, cross-sentence context, and strict role constraints, which often lead to boundary errors, uncertainty in roles, and inconsistencies with restricted schemas.   In this paper, we study whether mid-sized open LLMs can perform schema-constrained EAE relia...
  </details>

- **2026-07-18** — Sana Tonekaboni, Viktoria Schuster, Caroline Uhler — [MultiLoReFT: Decoupling Shared and Modality-Specific Subspaces in Multimodal Learning via Low-Rank Representation Fine-Tuning](http://arxiv.org/abs/2607.16789v1)
  <details><summary>📄 Abstract</summary>
  Real-world perception and decision making are inherently multimodal, integrating complementary signals across modalities. However, training multimodal models faces two main obstacles. First, collecting large-scale, well-aligned paired multimodal datasets is often impractical, making end-to-end multimodal training difficult. Second, existing multimodal representations frequently entangle information shared across modalities with modality-specific information, hindering interpretability and contro...
  </details>

- **2026-07-18** — Ran Wei, Le Zhu, Haochi Wang et al. — [Model-Driven Discipline for Multi-Agent LLMs: Requirement-to-Verification Generation of Traceable System Models](http://arxiv.org/abs/2607.16708v1)
  <details><summary>📄 Abstract</summary>
  Software complexity is a long-standing challenge for system engineers. Model-Driven Engineering (MDE) addresses it by treating models as first-class artefacts, but a typical MDE process spans many tools and produces heterogeneous models of different system aspects, making traceability, maintenance, and change management difficult.   We propose RADIANT, an engineering methodology that combines MDE with Multi-Agent Large Language Models (LLMs) for complete model-based system development, with a fo...
  </details>

- **2026-07-18** — Aseem Raj Baranwal — [The Value of Depth in Message Passing on Sparse Graphs: A Kesten-Stigum Dichotomy](http://arxiv.org/abs/2607.16676v1)
  <details><summary>📄 Abstract</summary>
  How deep does a graph neural network need to be on a sparse graph? We study its purest statistical form: node classification on the sparse contextual stochastic block model (CSBM) with average degree $Δ=O(1)$, whose local weak limit is a broadcast-labelled Poisson Galton-Watson tree. Prior work derived a message-passing classifier $h_\ell$ that aggregates from each vertex at distance $k\le\ell$ the attenuated evidence $2\operatorname{artanh}(γ^k t(X_v))$, with $γ$ the edge signal and $t$ a bound...
  </details>

- **2026-07-18** — Zhibin Wang, Xuying Han, Zhaohua Yang et al. — [SpecLA: Efficient Speculative Decoding for Linear-Attention Models](http://arxiv.org/abs/2607.16673v1)
  <details><summary>📄 Abstract</summary>
  Linear-attention models replace the growing KV cache with recurrent states, but autoregressive decoding still reads, updates, and writes these states one token at a time. Speculative decoding can reduce this cost by verifying several draft tokens in one target pass, yet existing speculative systems are designed for Transformer KV caches. For stateful linear-attention targets, verification must follow recurrent dependencies across chains and branches, acceptance must update only the accepted stat...
  </details>

- **2026-07-18** — Peilong Zhou, Zhirong Chen, Cangyuan Li et al. — [CLOSER-Bench: Evaluating Budgeted Cross-Stage Design Closure for Hardware Agents](http://arxiv.org/abs/2607.16632v1)
  <details><summary>📄 Abstract</summary>
  Hardware engineering exposes coding agents to a form of long-horizon work that is difficult to capture with pass-at-k: progress is continuous, tool feedback is delayed and heterogeneous, and a backend failure may require revising RTL rather than tuning another physical-design parameter. Existing benchmarks measure RTL generation, repository repair, verification, PPA evolution, or physical implementation, but their different designs and oracles make it hard to determine where an agent succeeds or...
  </details>

- **2026-07-18** — Nishant Kumar, Steve Mann — [Toward a Stable and Deployable Adaptive Chirplet Transform: Residual Projection, Hybrid GPU Acceleration, and Multi-Channel Scalability](http://arxiv.org/abs/2607.16629v1)
  <details><summary>📄 Abstract</summary>
  The Adaptive Chirplet Transform is a flexible framework that can decompose non-stationary signals into sparse chirplets; it has been applied to signals such as electroencephalography, electromyography and radar. However, the practical deployment of this transform has been hindered by two challenges: algorithmic instability in prior implementations, which can lead to divergent decompositions, and the computational cost of searching over a high-dimensional parameter space. This paper addresses bot...
  </details>

- **2026-07-18** — Lan Hu, Minghui Liwang, Wenbo Zhu et al. — [SAGE: A Socially-Aware Generative Engine for Heterogeneous Multi-Agent Navigation](http://arxiv.org/abs/2607.16619v1)
  <details><summary>📄 Abstract</summary>
  Safe and socially compliant navigation in open human-robot environments requires robots to reason about heterogeneous participants with different dynamics, autonomy levels, and social roles. Existing trajectory prediction and planning methods often rely on homogeneous interaction assumptions or enforce only geometric collision constraints, making it difficult to jointly model asymmetric interactions, coupled prediction-planning, and soft social norms. This paper proposes SAGE, a socially-aware g...
  </details>

- **2026-07-18** — Joaquín Miguez, Inés P. Mariño — [Stochastic stability of master-slave synchronization for dissipative PDEs with Burgers-type nonlinearity and application to data assimilation](http://arxiv.org/abs/2607.17002v1)
  <details><summary>📄 Abstract</summary>
  We investigate the stochastic stability of master--slave synchronization for a class of nonlinear dissipative evolution equations with a Burgers-type convective nonlinearity and a polynomial linear differential operator. The family includes the Burgers, Kuramoto--Sivashinsky, Kawahara, Benney--Lin, and Nikolaevskiy equations. Under periodic boundary conditions, each equation is represented through a finite-dimensional Fourier truncation, yielding a complex state vector coupled to a slave system ...
  </details>

- **2026-07-18** — Yu-Wen Chen, Julia Hirschberg — [An Audio Language Model-Based Voice Concept Bottleneck Framework for Interpretable Health Assessment](http://arxiv.org/abs/2607.16967v1)
  <details><summary>📄 Abstract</summary>
  Interpretability is critical in clinical decision support. Concept bottleneck frameworks improve it by representing inputs as human-understandable concepts and restricting predictions solely on them. However, research on their use for voice-based health assessment remains limited. In this study, we propose a voice concept bottleneck framework for interpretable health assessment using an audio language model (ALM). The ALM is fine-tuned on a voice quality assessment dataset to enhance its underst...
  </details>

- **2026-07-18** — Ping Xu, Xinghua Gao — [A BIM-enabled, Agent-based Discrete-event Simulation Platform for Robotic Studies: A Method based on Graph Theory](http://arxiv.org/abs/2607.16920v1)
  <details><summary>📄 Abstract</summary>
  Indoor robots are increasingly employed for facility management tasks such as cleaning and inspection. These applications primarily rely on navigation and can be effectively supported by predefined routes or perception-driven Simultaneous Localization and Mapping (SLAM) techniques. However, more complex tasks, such as locating and repairing leaking pipes, require not only navigation but also access to building information, including the location, geometry, material, and operational attributes of...
  </details>

- **2026-07-18** — Alireza Furutanpey, Schahram Dustdar — [Principled Direction-Free Intrinsic Motivation through Model-Free Epistemic Free-Energy Estimators](http://arxiv.org/abs/2607.16858v1)
  <details><summary>📄 Abstract</summary>
  Across environments with mixed sources of uncertainty, unsupervised reinforcement learning requires intrinsic motivation that does not precommit to a particular direction of surprise. Surprise minimization is scoped by design to ``unstable'' environments. Prediction-error curiosity rewards total expected surprise, including irreducible noise. Bandit or mixture switching between surprise-minimizing and surprise-maximizing rewards reintroduces non-stationarity by construction. We propose a single ...
  </details>

- **2026-07-18** — Maksim Sheverev, David Finkelstein, Sergey Nikolenko — [Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration](http://arxiv.org/abs/2607.16848v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is becoming a core component of LLM agents, but most memory benchmarks evaluate conversations or compact summaries, while research agents need to restore evidence from full scientific papers. We introduce two full-text scientific-memory benchmarks, Public AI Memory (PAIM; 81 papers, 66 questions) and Public Transformers (PTr; 252 papers, 98 questions). We evaluate eight memory/retrieval systems, including our own proposed Theoria, plus a no-retrieval baseline. Our results show t...
  </details>

- **2026-07-18** — Tianxing Zhao, Lei Zhou, Aming Li — [Evolution of cooperation with temporal information](http://arxiv.org/abs/2607.16816v1)
  <details><summary>📄 Abstract</summary>
  Strategy learning governs the evolution of collective cooperation in multi-agent systems. Although evolutionary outcomes depend strongly on the information available to agents during strategy learning, most studies treat both the source and amount of that information as fixed over time. In reality, however, individuals are continually exposed to external information that varies over time. Here we develop a general framework for evolutionary dynamics with temporal information, which uses temporal...
  </details>

- **2026-07-18** — Francesco Karim Vicidomini — [The Anatomy of a Truth Direction: Knowledge-Dependent Dimensionality, a Relational Law, and a Convergent Category Geometry in Small Language Models](http://arxiv.org/abs/2607.16741v1)
  <details><summary>📄 Abstract</summary>
  Bürger et al. (2024) demonstrated that truth representations in large language models are universal across statement polarity but reside within a multidimensional subspace. We extend that framework along three questions: how the dimensionality of the subspace depends on the model's knowledge, which architectural component builds the truth direction, and what the direction is a mixture of. In Part I (one model), a training-free directional probe derived from the SVD of hidden-state minimal pairs ...
  </details>

- **2026-07-18** — Sokipriala Jonah — [When Do Multimodal and Graph-Augmented RAG Help? A Controlled Evaluation for Document Question Answering](http://arxiv.org/abs/2607.16604v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) systems commonly operate on text extracted from documents, potentially losing information contained in figures, tables, layout, and relationships distributed across passages. We present an explainable multimodal graph-RAG architecture that augments a text-only baseline with LLM-extracted subject--relation--object triples and CLIP-based retrieval of figures and tables. The three evidence sources are retrieved independently and fused only at generation time, al...
  </details>

- **2026-07-17** — Ajay Patel, Kartik Hosanagar, Ramayya Krishnan et al. — [Frontier AI performance across the business disciplines: a case-grounded benchmark of knowledge work and analytical reasoning](http://arxiv.org/abs/2607.16057v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are improving rapidly as reflected in benchmark scores, yet these AI benchmarks largely test capabilities such as factual recall, narrow question answering, mathematical problem-solving, and coding and agentic tool-use. What remains poorly measured is AI progress on the analytical knowledge work white-collar professionals perform daily, including synthesizing complex information, exercising judgment under uncertainty and incomplete information, applying strategic and...
  </details>

- **2026-07-17** — Fan Yang, Lin Zhang — [LLM Latent Edge Measurement: Point-in-Time Economic Graphs for Quantitative Investing from Corporate Disclosures](http://arxiv.org/abs/2607.15640v1)
  <details><summary>📄 Abstract</summary>
  Standard industry classification systems such as GICS assign each firm to a single sector, but the economic relationships through which shocks propagate, such as supplier agreements, customer concentration, intellectual property licensing, cloud service dependencies, and power purchase contracts frequently cross sector boundaries and are often disclosed only in unstructured text. We formulate the construction of a firm-level adjacency matrix as a measurement problem and propose an LLM based pipe...
  </details>

- **2026-07-17** — Hao Liu, Chenghuan Huang, Ye Huang et al. — [FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation](http://arxiv.org/abs/2607.16190v1)
  <details><summary>📄 Abstract</summary>
  Video Diffusion Transformers process long spatio-temporal sequences, making self-attention the main bottleneck in high-resolution video generation. Training-free sparse attention reduces this cost, but adaptive Top-$p$ routing creates uneven per-head workloads under multi-GPU sequence parallelism. The resulting workload heterogeneity turns sparse attention into a rank-level straggler problem. We present \method{}, a training-free sparse-attention system that improves the distributed execution ef...
  </details>

- **2026-07-17** — Wendi Yu, Lianhao Zhou, Xiangjue Dong et al. — [When Do Multi-Agent Systems Help? An Information Bottleneck Perspective](http://arxiv.org/abs/2607.16133v1)
  <details><summary>📄 Abstract</summary>
  LLM powered multi-agent systems (MAS) have emerged as a promising paradigm for complex tasks. However, their advantages over single-agent systems (SAS) remain unclear, with performance varying inconsistently across settings. Here, we provide an information bottleneck perspective on elucidating the differences between MAS and SAS. Specifically, our key observation is that a SAS accumulates its full reasoning trace in one shared context, while a MAS uses isolated local contexts connected by bounde...
  </details>

- **2026-07-17** — Maeve Hutchinson, Abderrahmane Wassim Mehdaoui, Pranava Madhyastha — [Attention-Guided Saliency Maps for Interpreting Visualization Literacy in VLMs](http://arxiv.org/abs/2607.16105v1)
  <details><summary>📄 Abstract</summary>
  Understanding how vision-language models (VLMs) interpret data visualizations remains an open problem, and is increasingly important as these models are used for analytical tasks where reliable reasoning is essential. We introduce a lightweight, diagnostic saliency map method tailored for text generation over images using transformer models, the current state-of-the-art models in visualization interpretation. Our approach aggregates the language model's attention over the visual tokens across al...
  </details>

- **2026-07-17** — Haoran Sun, Wentao Zhang, Junyang Hua et al. — [JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models](http://arxiv.org/abs/2607.16074v1)
  <details><summary>📄 Abstract</summary>
  The post-training of Vision-Language-Action (VLA) models is essential due to the diversity of simulators, robot embodiments, and task objectives. Existing compute services, whether offered as direct accelerator rental or batch-workload submission, typically allocate an exclusive set of GPU and CPU resources to a single tenant. While this paradigm maximizes client flexibility, it burdens users with infrastructure adaptation, and the fixed card-hour accounting model renders short or bursty workloa...
  </details>

- **2026-07-17** — Hassan Munif, Anthony Couthures, Vineeth S. Varma et al. — [Network-Induced Strategic Communication in Opinion Dynamics](http://arxiv.org/abs/2607.16036v1)
  <details><summary>📄 Abstract</summary>
  Classical opinion dynamics typically assume a fixed mapping from private opinions to public signals, such as linear exchange, saturated signaling, or discrete public actions. In this paper, we show that these communication mappings can be derived from a strategic communication game played on a weighted influence network. Each agent acts as a receiver estimating its neighbors' states and as a sender broadcasting a public signal to influence its audience. We prove that the network's effect on a se...
  </details>

- **2026-07-17** — Olayiwola Arowolo, Maosheng Yang, Jochen Cremer — [Revisiting data-driven dynamic security assessment with a tabular foundation model](http://arxiv.org/abs/2607.16031v1)
  <details><summary>📄 Abstract</summary>
  Data-driven pre-fault dynamic security assessment (DSA) rapidly evaluates the dynamic risk of credible contingencies on a power system using machine learning. Existing approaches face two limitations. First, they require a large labelled database for training, with a separate model trained, tuned, and maintained for each contingency in a potentially long list of credible contingencies. Second, the trained models generalize poorly to unseen contingencies. This work addresses the limitations by us...
  </details>

- **2026-07-17** — Andrei Neagu, Eeham Khan, Leila Kosseim — [CLaC@FinMMEval 2026 Task 3: Sentiment-Augmented Deep Reinforcement Learning for Active Trading -- An Alpha-Reward Approach](http://arxiv.org/abs/2607.16028v1)
  <details><summary>📄 Abstract</summary>
  This paper presents our system for Task 3 of the CLEF 2026 FinMMEval Lab, which requires daily long, flat, or short trading decisions for Bitcoin (BTC) and Tesla (TSLA) using news and historical market data. We formulate the problem as a discrete-action Markov Decision Process and compare four deep reinforcement learning algorithms: Policy Gradient (PG), Proximal Policy Optimization (PPO), Deep Q-Learning (DQL), and Deep Deterministic Policy Gradient (DDPG). The agents use technical indicators, ...
  </details>

- **2026-07-17** — Yujie Li, Jiancheng Pan, Zhiwei Wei et al. — [GeoChrono: Benchmarking and Rethinking Long-Term Temporal Understanding in Remote Sensing](http://arxiv.org/abs/2607.15768v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing offers an unparalleled vantage point for observing the Earth's long-term surface evolution, yet it demands that a model not only perceive land cover at isolated moments, but also track changes, memorize evolution histories, and reason across time and space. However, existing studies lack a systematic evaluation that dissects these distinct competencies. To fill this gap, we introduce ChronoBench, a multidimensional benchmark that decomposes this task into four progressive cognitiv...
  </details>

- **2026-07-17** — Alcino Cunha — [Verified LLM-Driven Synthesis for Concept Design](http://arxiv.org/abs/2607.15718v1)
  <details><summary>📄 Abstract</summary>
  Concept Design structures software systems around concepts: user-facing, self-contained units of functionality with a focused purpose. Concepts are composed into applications using synchronization rules called reactions, which specify how actions in one concept trigger actions in others. This paper first gives a formal semantics for concepts and reactions, enabling automatic verification of safety invariants in applications developed with this methodology. It then presents a CEGIS-style, LLM-dri...
  </details>

- **2026-07-17** — Andrea Forster, Gregor Autischer, Dominik Kowald et al. — [From Skill Extraction to Multistakeholder Recommendation: A Two-Stage Framework for Bias Governance in Skills-Based Job Matching](http://arxiv.org/abs/2607.15707v1)
  <details><summary>📄 Abstract</summary>
  AI-based labor-market systems or platforms can affect access to job opportunities prior to organizational candidate rankings or hiring decisions. Such applications warrant caution, as biases in skill extraction, profile formation, and candidate-job matching may contribute to unfair treatment of candidates. In this paper, we propose a two-stage framework for detecting and governing bias in skills-based job matching. Stage 1, skill extraction and profile formation, addresses how candidates provide...
  </details>

- **2026-07-17** — Yunpeng Bai, Haoxiang Li, Qixing Huang — [PE-Field 4D: Video Generation Models as Canvas](http://arxiv.org/abs/2607.15667v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers have recently achieved strong performance in video generation, yet controlling scene geometry under viewpoint changes and camera motion remains challenging. In this work, we revisit the role of positional encoding in video diffusion transformers and show that it provides a useful spatial bias for geometry-aware control. Specifically, if reference tokens are encoded according to their projected locations in the target view, the denoising model is encouraged to retrieve cont...
  </details>

- **2026-07-17** — Yun Li, Jiachen Gong, Simon Thompson et al. — [Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving](http://arxiv.org/abs/2607.15621v1)
  <details><summary>📄 Abstract</summary>
  Large language models bring instruction following and scene reasoning to end-to-end driving, but their inference latency collides with the control rate a vehicle requires. Existing closed-loop agents hide this gap by invoking the model on alternate simulation ticks and replaying the previous command in between, so half of all control outputs ignore the newest observations. We present a fast-slow architecture that removes this compromise. A frozen 7B vision-language backbone acts as the slow syst...
  </details>

- **2026-07-17** — Dangyang He — [Riesz transform and its related inequalities for degenerate elliptic operators of Grushin type](http://arxiv.org/abs/2607.15599v1)
  <details><summary>📄 Abstract</summary>
  We study the $L^p$ boundedness of the Riesz transform and the reverse Riesz inequality for degenerate elliptic operators of Grushin type. We prove full-range $L^p$ boundedness of the Riesz transform when the degenerate variable has dimension at least two, and obtain the sharp range in the one-dimensional weakly degenerate case, including the endpoint obstruction. In the strongly degenerate one-dimensional regime, we recover full-range boundedness, revealing a striking transition in the behavior ...
  </details>

- **2026-07-17** — Yang Meng, Zhenya Liu, Zhuokai Zhao et al. — [Rethinking Transfer in Continual Learning: A Replay-Based Realisation](http://arxiv.org/abs/2607.15587v1)
  <details><summary>📄 Abstract</summary>
  Continual learning studies how deployed language models can continually acquire new tasks without expensive retraining from scratch. Existing methods, whether rehearsal-based (replaying stored past data) or rehearsal-free (regularising or isolating parameters), overwhelmingly target one objective: preventing catastrophic forgetting. Forward transfer, the past helping the future, has meanwhile been pursued almost exclusively through parameter reuse, with no explicit account of when transfer shoul...
  </details>

- **2026-07-17** — Sebastian Cochinescu — [Perceived AGI: Believability as Dimensional Completeness, Not Capability](http://arxiv.org/abs/2607.15883v1)
  <details><summary>📄 Abstract</summary>
  Large language models are broadly capable, yet in sustained one-to-one conversation they still read as flat: competent, responsive, and somehow not quite the presence of a mind. We hypothesize that a central missing ingredient is not more capability but dimensional completeness. We propose that the believability of an artificial interlocutor -- the degree to which a user attributes an inner life to it, which we call perceived mind -- is governed by whether the agent expresses a small set of firs...
  </details>

- **2026-07-17** — Li-Hsiang Shen — [Energy Efficient Active Stacked Intelligent Metasurfaces](http://arxiv.org/abs/2607.15654v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates an energy-efficient active stacked intelligent metasurfaces (ASIM)-assisted downlink transmission framework, where a multi-antenna base station (BS) serves multiple users through a multi-layer metasurface architecture. Unlike conventional passive intelligent surfaces, the considered ASIM employs active amplification and multiple transmissive layers to enhance electromagnetic wave manipulation. We aim to maximize the system energy efficiency (EE) by jointly optimizing the ...
  </details>

- **2026-07-17** — Haodong Wen, Yiran Zhang, Yingfa Chen et al. — [Frontier Language Models Struggle to Copy: Text Can Be Better Viewed in 2D](http://arxiv.org/abs/2607.16072v1)
  <details><summary>📄 Abstract</summary>
  While large language models (LLMs) can solve advanced reasoning problems in seconds, we show that even frontier models fail to perform a much simpler operation: exactly copying an input string that lies well within their context windows. We attribute this failure to positional encodings in Transformer architectures, whose inductive bias favors copying through a shortcut based on matching local contexts rather than carefully locating the corresponding input positions. To address this issue, we in...
  </details>

- **2026-07-17** — S. Aaron McClendon — [When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis](http://arxiv.org/abs/2607.16062v1)
  <details><summary>📄 Abstract</summary>
  Model merging is promoted as a substitute for joint multi-task training, yet in the reinforcement-learning setting this substitution is essentially never tested against the baseline it claims to replace: methods merge independently released agents precisely because a joint model is unavailable. We build the missing comparison. Training difficulty-1 and difficulty-2 Qwen3-8B specialists on the AppWorld agent benchmark with LOOP, we merge them (TIES, RAM+) and pit the result against a jointly trai...
  </details>

- **2026-07-17** — Junjie Zhou, Zhijian Ou — [BayesPO: Bayesian Prompt Optimization via Parallel-Tempered Gradient-Guided Discrete MCMC](http://arxiv.org/abs/2607.16001v1)
  <details><summary>📄 Abstract</summary>
  Prompt optimization adapts large language models (LLMs) without updating model parameters, but many automatic prompt optimizers remain heuristic search procedures over candidate instructions. This paper studies prompt optimization as Bayesian posterior sampling over discrete prompt tokens. We define a posterior distribution by combining a task likelihood term, which rewards prompts that explain input-output examples, with a language-model prior, which favors fluent instructions. This converts pr...
  </details>

- **2026-07-17** — Théophane Loloum, Fabien Vivodtzev, David Hébert et al. — [DebrisTracer: Reliable Tracking in Hypervelocity Impact Fast Imaging](http://arxiv.org/abs/2607.15986v1)
  <details><summary>📄 Abstract</summary>
  This application paper presents DebrisTracer, a framework for the reliable tracking of debris in hypervelocity impact fast imaging. These noisy and highly specific datasets capture the ejection of a large number of debris fragments after the impact of a projectile launched at hypervelocity into a target material. The reliable estimation of debris mass and speed distributions is of major importance in aerospace applications. We document how to extend an off-the-shelf topology tracking framework b...
  </details>

- **2026-07-17** — Elize Herrewijnen, Benedetta Muscato, Gizem Gezici et al. — [From Plausible to Actionable: A Position on LLM Self-Explanations](http://arxiv.org/abs/2607.15957v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can generate natural language explanations that rationalize their own decisions, a phenomenon commonly referred to as self-explanations.Such explanations have emerged as a promising direction for explainable artificial intelligence (XAI), particularly for interpreting LLM behavior.However, while self-explanations often appear plausible, whether they faithfully reflect a model's underlying reasoning process remains an open question. In this opinion paper, we argue tha...
  </details>

- **2026-07-17** — Suzan Awinat, Alfonso Ortega del Puente — [CAMMAR: Culture-Aware Matryoshka for Metaphorical Arabic Representations](http://arxiv.org/abs/2607.15847v1)
  <details><summary>📄 Abstract</summary>
  Metaphor in Arabic is a culturally grounded mechanism for constructing meaning, encoding cultural knowledge that shapes interpretation. Yet current Arabic language models typically collapse lexical, cultural, and metaphorical information into a single representational space, a phenomenon we term "semantic smearing". We introduce CAMMAR (Culture-Aware Matryoshka for Metaphorical Arabic Representations), a representation learning framework that organizes meaning into nested lexical, cultural, and ...
  </details>

- **2026-07-17** — Willem Fourie, Gray Manicom, Tanya de Villiers-Botha — [The CRAFT principles for the responsible use of large language models in policymaking](http://arxiv.org/abs/2607.15704v1)
  <details><summary>📄 Abstract</summary>
  Policymakers around the world face the question of how to use artificial intelligence in general, and large language models in particular, to improve the policymaking process. Used well, large language models can strengthen the collection, interpretation and synthesis of policy-relevant information and the drafting of policy-relevant output. Yet the use of large language models in policymaking is associated with risks. Output that is plausible but not necessarily correct, bias resulting from unr...
  </details>

- **2026-07-17** — Kalana Ratnayake, Michael Pritchard, David Hinwood et al. — [A Generative Partially Specified Finite State Machine Approach to Complex Behaviour Planning](http://arxiv.org/abs/2607.15674v1)
  <details><summary>📄 Abstract</summary>
  Autonomous robots operating in dynamic environments require behaviour planning systems that combine reactivity, interpretability, and adaptability. While Large Language Models have been successfully integrated with Behaviour Trees for dynamic replanning, Finite State Machines, despite their widespread adoption and computational efficiency, remain unexplored for generative approaches. We propose a Generative Partially Specified Finite State Machine (GPSFSM) neurosymbolic architecture that utilise...
  </details>

- **2026-07-17** — Kirill Karpov, Jonas Auch, Eduard Heidt et al. — [Isothermal compression of a Fermi gas to deep quantum degeneracy](http://arxiv.org/abs/2607.15616v1)
  <details><summary>📄 Abstract</summary>
  The standard approach for generating deeply degenerate quantum gases is evaporative or sympathetic cooling in a harmonic trap, after which the gas has reached its minimum entropy. All subsequent state transformations rely on adiabatic changes of a closed system, and coupling to the environment or non-adiabatic processes monotonically increase the entropy. Here, we demonstrate that this experimental paradigm can be bypassed by utilizing species-selective trapping with a low-dissipation optical tu...
  </details>

- **2026-07-17** — Haris Aziz, Zixu He, Xinhang Lu et al. — [Fair Allocation of Divisible Goods under Non-Linear Valuations](http://arxiv.org/abs/2607.15613v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of dividing homogeneous divisible goods among agents with non-linear valuations. Specifically, the value that an agent gains from a given good depends only on the amount of the good they receive, and is not necessarily linear with respect to the amount. For instance, under one-breakpoint piecewise-constant valuations, each agent specifies a threshold for each good such that this agent receives utility zero (resp., full utility of the good) when getting an amount below (resp....
  </details>

- **2026-07-15** — Lei Zhang, Yusheng Zhao, Hongshun Yao et al. — [Building Shor's Algorithm in Lean: An Agentic Formalization of Quantum Attacks on RSA-2048 and P-256](http://arxiv.org/abs/2607.14082v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly assisting with demanding formal theorem-proving tasks, particularly when grounded in machine-checked libraries such as Lean. Agentic systems further amplify this process by searching, reusing, and extending existing formal developments to uncover new discoveries. In quantum computing, Shor's algorithm and its variants present such a demanding case for Lean formalization. In this work, we formalize this algorithm family in Lean through agentic formalization:...
  </details>

- **2026-07-15** — Zhenkai Zhang, Krista A. Ehinger, Tom Drummond — [TCAM-Diff: Triplane-Aware Cross-Attention Medical Diffusion Model](http://arxiv.org/abs/2607.13812v1)
  <details><summary>📄 Abstract</summary>
  We introduce TCAM-Diff, a novel 3D medical image generation model that reduces the memory requirements to encode and generate high-resolution 3D data. This model utilizes a decoder-only autoencoder method to learn triplane representation from dense volume and leverages generalization operations to prevent overfitting. Subsequently, it uses a triplane-aware cross-attention diffusion model to learn and integrate these features effectively. Furthermore, the features generated by the diffusion model...
  </details>

- **2026-07-15** — Angelo F. Andreoli, Gabriela B. Ribeiro, Guilherme C. Stumpf et al. — [Chemical short-range order controls deformation pathways in a complex concentrated alloy](http://arxiv.org/abs/2607.13896v1)
  <details><summary>📄 Abstract</summary>
  Chemical short-range order (CSRO) is an intrinsic feature of complex concentrated alloys (CCAs), yet its influence on deformation mechanisms is controversial because of the inconclusive state of concurrent CSRO quantification during deformation. Here, we provide experimental evidence that CSRO acts as an intrinsic thermodynamic state variable governing stacking-fault energetics and deformation pathways in a Co30Cr40Ni30 alloy. By comparing quenched (CSRO-lean) and aged (CSRO-enriched) conditions...
  </details>

- **2026-07-15** — Lili Zhou, Ruizi Zhang, Chen Si et al. — [Realization and manipulation of spiral charge density waves in a two-dimensional metal](http://arxiv.org/abs/2607.13878v1)
  <details><summary>📄 Abstract</summary>
  Nearly degenerate charge-density-wave (CDW) states play a central role in the competition among collective phenomena. In real materials, however, these states are often intertwined by disorder, hindering their disentanglement and control. Here we show that strain can lift this near-degeneracy and spatially separate distinct CDW states in NbSe2. Using van der Waals (vdW) interactions, we stabilize a micron-scale strain network that produces spatially inhomogeneous strain fields. Within this lands...
  </details>

- **2026-07-15** — Lin Jiaben, Tong Liyue, Wang Hui et al. — [Scientific-Intention Driven Embodied Intelligent Solar Telescope: Conceptual Design](http://arxiv.org/abs/2607.13533v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) is profoundly transforming the paradigms of scientific research. Cutting-edge technologies such as Large Language Models (LLMs) and embodied intelligence are continuously pushing the boundaries of scientific instrumentation. Against this backdrop, this paper proposes a novel conceptual system: the Scientific-Intention Driven Embodied Intelligent Solar Telescope (SIDEST). The system is designed with three core layers to achieve three types of intelligent scientific re...
  </details>

- **2026-07-15** — Phu Pham, Damon Conover, Aniket Bera — [COLMAR: Cooperative View Policy Learning for Multi-Agent Active 3D Reconstruction](http://arxiv.org/abs/2607.13524v1)
  <details><summary>📄 Abstract</summary>
  Active 3D reconstruction requires selecting informative viewpoints under limited sensing budgets. In multi-agent settings, coordination inefficiencies such as redundant observations and spatial clustering can significantly reduce reconstruction quality. We present COLMAR, a cooperative view policy learning framework for multi-agent active 3D reconstruction. COLMAR formulates viewpoint allocation as a shared policy optimization over map-centric observations and introduces a reconstruction-aware o...
  </details>

- **2026-07-15** — Zobeir Raisi — [2D Rotary Position Embedding for Scene Text Recognition with Transformers](http://arxiv.org/abs/2607.13458v1)
  <details><summary>📄 Abstract</summary>
  Scene Text Recognition (STR) remains challenging due to the diversity of text appearances, including curvature, rotation, and perspective distortion. Recent Transformer-based approaches perform well but usually rely on one-dimensional positional encodings that ignore the 2D spatial structure of text images. Axial 2D extensions of Rotary Position Embedding (RoPE) exist for vision Transformers, but they assume roughly square, isotropic image content and apply the rotation only within encoder self-...
  </details>

- **2026-07-15** — Ann-Kareen Gedeus, Jack Good, Nadine Wagener et al. — [TANDE: Disentangling Verbal and Nonverbal Backchannels in Emotional AI-Avatar Conversations with Young Adults](http://arxiv.org/abs/2607.13357v1)
  <details><summary>📄 Abstract</summary>
  Embodied conversational agents (ECAs) need effective empathic grounding to foster social support and engagement. Expanding into emotional domains, ECAs now use Large Language Models (LLMs) and multimodal human-agent interactions to enhance their capabilities. Yet, understanding the impact of backchanneling modalities on young adults and their gender remains limited. We introduce TANDE, an LLM-powered ECA designed for emotional conversations with young adults, a population experiencing mental, pe...
  </details>

- **2026-07-15** — Ru Zhang, Weijie Qiu — [SPyCE: Skill-Policy Co-evolution for Multimodal Agents](http://arxiv.org/abs/2607.13854v1)
  <details><summary>📄 Abstract</summary>
  Multimodal agents that think with images iteratively manipulate visual evidence and invoke tools across many steps. Existing reinforcement learning methods reduce trajectories to scalar rewards, forcing the policy to discover reusable tool-use patterns from scratch on every new task; memory-based alternatives retain past experience, yet they rely on test-time retrieval, without updating the policy to absorb reusable patterns from that experience. Our key insight is that multimodal reasoning traj...
  </details>

- **2026-07-15** — Yingwei Ji — [An Empirical Study on Stage-Information Interfaces for VLA Fine-Tuning](http://arxiv.org/abs/2607.13605v1)
  <details><summary>📄 Abstract</summary>
  One high-level instruction in long-horizon manipulation can cover several action stages. We use segmented action annotations as an intermediate representation between the full-task instruction and VLA action chunks. A progress module tracks the active stage, while the action policy receives stage information either as current-stage text or as a normalized ordinal stage index in robot state. We compare these interfaces with GR00T N1.6 on LIBERO-10 under direct fine-tuning and continuation fine-tu...
  </details>

- **2026-07-15** — Huatao Li, Xinwei Geng, Yuheng Wang et al. — [DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments](http://arxiv.org/abs/2607.13465v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents have rapidly improved at operating individual digital environments such as mobile applications, desktop systems, and smart homes. However, real-world user goals often span multiple devices: information may come from a phone, be processed on a desktop, and the result may need to appear on another device. Most existing benchmarks center on a single dominant execution environment, making it difficult to evaluate whether agents can acquire and integrate information across heterogene...
  </details>

- **2026-07-15** — Shivansh Patel, Kaifeng Zhang, Sanjay Pokkali et al. — [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](http://arxiv.org/abs/2607.13451v1)
  <details><summary>📄 Abstract</summary>
  Simulating deformable objects is essential for a wide range of robotic manipulation applications, yet accurately predicting their dynamics remains challenging. We propose Physics-Guided Residual Dynamics (PGRD), a hybrid simulation framework that combines the advantages of physics-based and learning-based approaches. Specifically, PGRD combines an optimizable spring-mass simulator as a backbone with a learned neural network that predicts residual corrections to the physics-based predictions. We ...
  </details>

- **2026-07-15** — Jing-Xiao Liao, Tianwei Zhang, Yu-Hao Jiang et al. — [Self-Improving is Often Sudden: Enlightenment-style Finetuning for Large-Scale Models](http://arxiv.org/abs/2607.13395v1)
  <details><summary>📄 Abstract</summary>
  The pursuit of autonomously self-improving models has attracted growing interest in the era of large-scale foundation models. Drawing inspiration from the concept of "enlightenment" or "aha moment" in human brain, we hypothesize that large models exhibit an analogous enlightenment phenomenon-a latent capacity for sudden capability boost. Then, we propose Enlightenment, a novel training-free post-tuning paradigm for large-scale models. Our approach modifies shortcuts for key modules/layers withou...
  </details>

- **2026-07-15** — Moses Boudourides — [LLMs for Qualitative and Mixed-Methods Social Network Analysis](http://arxiv.org/abs/2607.14045v1)
  <details><summary>📄 Abstract</summary>
  This manuscript explores the integration of Large Language Models (LLMs) into the field of qualitative and mixed-methods social network analysis (SNA). We argue that the primary focus of this integration should be on enhancing the depth and rigor of qualitative SNA, rather than on replacing human researchers with automated systems. We begin by outlining the core principles of qualitative and mixed-methods SNA, emphasizing the importance of understanding the meaning of ties, the role of narrative...
  </details>

- **2026-07-15** — Wenxiao Wang, Priyatham Kattakinda, Soheil Feizi — [Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](http://arxiv.org/abs/2607.14004v1)
  <details><summary>📄 Abstract</summary>
  Most reported gains from agent-optimization methods are one-shot: an agent is optimized against a fixed benchmark and the resulting improvement is reported as if it were a stable property of the method. This does not test the setting that matters for deployed agents, where optimization is applied recursively as new failures and new tasks appear over time. The central question this raises is whether optimizer-driven gains compound: after an agent has been optimized once, can it be optimized again...
  </details>

- **2026-07-15** — Benedikt Bollig, Matthias Függer, Thomas Nowak et al. — [Agent-Alternation-Free Epistemic Metric Temporal Logic with Past: Model Checking and Complexity](http://arxiv.org/abs/2607.13981v1)
  <details><summary>📄 Abstract</summary>
  We study model checking for an epistemic metric temporal logic with past, interpreted over finite Büchi automata under synchronous perfect recall. The logic is motivated by observation-based verification problems such as diagnosis and opacity, where an observer sees only a projection of an execution and reasons about events that may have occurred earlier. These requirements use no alternation between different agents' knowledge. We therefore consider the agent-alternation-free fragment, in which...
  </details>

- **2026-07-15** — Juan-Feng Zhu, Wenjie Zhou, Shihao Feng et al. — [Temporal Fourier Optics Reveals Hidden Hybridized Light-Matter States](http://arxiv.org/abs/2607.13957v1)
  <details><summary>📄 Abstract</summary>
  Spectral measurements provide fundamental insights into wave systems by revealing resonances, mode hybridization, and light-matter interactions. However, intrinsic dissipation and measurement-induced spectral broadening often conceal the underlying hybridized light-matter states that give rise to measured spectra. Here, we establish a space-time Fourier correspondence that interprets spectral broadening as an effective temporal attenuation, giving rise to a temporal Fourier optics framework for ...
  </details>

- **2026-07-15** — Wangjin Zhou, Yizhou Zhang, Yichi Wang et al. — [Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match?](http://arxiv.org/abs/2607.13864v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) is widely used to adapt self-supervised speech representations to downstream classification tasks. Small gains observed under a single pretrained checkpoint are often interpreted as method-level improvements, i.e., a higher attainable performance ceiling. We show that such conclusions are not always reliable because SFT outcomes depend strongly on the specific pretrained instance. We conduct a systematic study on 3 SUPERB classification tasks, evaluating 8 SFT varian...
  </details>

- **2026-07-15** — Xiaotian Luo, Fengxingyu Wang, Chuanrui Hu et al. — [Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity](http://arxiv.org/abs/2607.13683v1)
  <details><summary>📄 Abstract</summary>
  An LLM agent's real-task performance is shaped as much by the harness around its model as by the frozen model itself: its prompts, injected knowledge, runtime control, and configuration. In deployment the harness is often the only lever available, so improving it automatically is the natural way to raise performance without touching the weights. The hard part is not generating changes but knowing which one truly helped. Self-generated feedback is noisy, and an apparent gain can be a measurement ...
  </details>

- **2026-07-15** — Yongren Shi, Wenyi Gong — [When Bots Join the Team: Bot Adoption and the Institutional Fabric of Open-Source Software Projects](http://arxiv.org/abs/2607.13679v1)
  <details><summary>📄 Abstract</summary>
  AI agents are joining human teams, raising a basic question: when an automated agent becomes a regular participant, does group organization strengthen or weaken? We study this question in open-source software, where bots open pull requests, review code, and merge changes alongside people, leaving a public record of every interaction. Treating bots as participants rather than tools, we examine 2,991 GitHub projects for two years before and after each adopted its first bot. We measure three capabi...
  </details>

- **2026-07-15** — Jose Martínez-Fajardo, Pablo Pueyo, Fernando Caballero et al. — [From Language to Navigation Goals: A Vision-Language Approach for Semantic Navigation of Mobile Robots Using RGB-D Perception](http://arxiv.org/abs/2607.13624v1)
  <details><summary>📄 Abstract</summary>
  Natural language interaction provides an intuitive way for non-expert users to communicate with robotic platforms. However, transforming user requests into executable navigation actions remains a challenging task, requiring the integration of language understanding, environment perception, and autonomous navigation. This work presents a language-driven navigation framework that enables mobile robots to interpret user requests in natural language to move the robot to a destination and autonomousl...
  </details>

- **2026-07-15** — Yue Yan, SiYing Wang, ZhiXin Xia et al. — [Tensor Network decoding under inter-qubit correlated errors](http://arxiv.org/abs/2607.13570v1)
  <details><summary>📄 Abstract</summary>
  The maximum likelihood decoder based on tensor networks has proven highly successful for the 2D surface code, achieving the optimal decoding success rate. However, existing tensor network decoders are typically designed for independent single-qubit error models, and their performance under inter-qubit correlated error models remains unexplored. This is due to two major challenges. The first challenge lies in constructing the tensor network for correlated errors, since the same final Pauli error ...
  </details>

- **2026-07-15** — Vivek Kanojiya, Vishalaksh Aggarwal, Daeho Baek et al. — [Personalizing Incremental Video Search with Hybrid Text and ID Embeddings](http://arxiv.org/abs/2607.13493v1)
  <details><summary>📄 Abstract</summary>
  Incremental video search requires high-quality ranking after each keystroke, where intent is often underspecified (e.g., 1-3 character prefixes). We present a personalization system for Apple TV search that combines complementary semantic and collaborative signals at ranking time. Our approach learns two item embedding spaces: (i) a text-based multilingual encoder (TextEmb) fine-tuned on co-engagement triplets via contrastive learning, and (ii) an ID-based collaborative embedding model (IdEmb) t...
  </details>

- **2026-07-15** — Lei Yang, Weiqing Li, Zhiyong Su et al. — [CASA-SDF: Curriculum-Aware Spatial Adaptation with Curvature-Guided Density for Neural Implicit Surface Reconstruction](http://arxiv.org/abs/2607.13492v1)
  <details><summary>📄 Abstract</summary>
  Neural implicit representations have emerged as a powerful paradigm for 3D reconstruction. However, high-fidelity indoor surface reconstruction remains a significant challenge, primarily due to the pronounced \emph{geometric heterogeneity} of indoor scenes. Large texture-less planar regions typically require stronger regularization to suppress high-frequency artifacts, while thin structures demand sharper, more adaptive representations to mitigate the spectral bias of multi-layer perceptrons (ML...
  </details>

- **2026-07-15** — Joonyong Park, David M. Chan, Yuki Saito et al. — [Auditing Protocol-Level Shortcuts in Large Audio Language Model Judges for Speech Evaluation](http://arxiv.org/abs/2607.13477v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) are increasingly used as automatic judges for speech evaluation. However, high agreement with human ratings does not guarantee that their verdicts are grounded in the audio. A judge may instead rely on specialist labels or reference data supplied by the evaluation protocol itself, taking a shortcut in place of listening to the audio. In this paper, we audit such protocol-level ``shortcuts'' in LALM judges across three common deployment protocols: feature-bluep...
  </details>

- **2026-07-15** — Tuomas Oikarinen, Zixiao Chen, Charlotte Siska et al. — [Data-Efficient Adaptation of LLMs via Attention Head Reweighting](http://arxiv.org/abs/2607.13425v1)
  <details><summary>📄 Abstract</summary>
  Learning effectively from limited data is critical in domains like security where labeled examples are scarce. Large language models (LLMs) have demonstrated some capabilities for data-efficient learning, especially through parameter-efficient adaptation methods, but continue to struggle when faced with few samples for difficult tasks. To meet this challenge, we propose Attention Head Reweighting (AHR), a data-efficient method that adapts LLMs to new text-classification tasks by learning only a ...
  </details>

- **2026-07-15** — Jiwen Zhou, Xiang Liu, Mingming Li et al. — [Can We Steer the Black-Box? Towards Controllability-Centric Evaluation of Recommender Systems with Collaborative Agents](http://arxiv.org/abs/2607.13418v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems operate as Black-Boxes, leaving users and regulators unable to steer their outputs toward specific intentions or audit their behavior. This lack of controllability, defined as the system's ability to respond to explicit guidance, remains an unaddressed dimension in existing evaluation paradigms. To fill this gap, we propose CtrlBench-Rec, a collaborative multi-agent framework for systematic assessment of controllability. We formalize three fundamental tasks: target content di...
  </details>

- **2026-07-15** — Guanglei Zhou, Chen-Chia Chang, Yikang Shen et al. — [EXPLORE: Exploration with Guided Search for Analog Topology Generation using Language Models](http://arxiv.org/abs/2607.13416v1)
  <details><summary>📄 Abstract</summary>
  Automating analog circuit topology design is essential to reduce the extensive manual effort required to meet increasingly diverse and customized application demands. Recent advances have applied sequence-to-sequence fine-tuning on pretrained language models to directly generate circuit topologies from user specifications in a single pass. However, these one-shot generation methods failed to generate complex circuits due to their exponentially growing search spaces and limited training datasets....
  </details>

- **2026-07-15** — Wenkai Dong, Yifan Wang — [From Interpretation to Compilation: Compilation-Based Execution of Semantic Operators [Vision]](http://arxiv.org/abs/2607.13407v1)
  <details><summary>📄 Abstract</summary>
  Semantic operator systems extend data processing with natural-language interfaces, supporting operations such as semantic filtering, mapping, and joining. Existing systems commonly execute these operators through interpretation-based execution: for each row, record, or candidate pair, an LLM is invoked to interpret the semantic intent and produce an output. Although expressive, this places expensive LLM calls inside the data-processing loop, causing high latency, monetary cost, and limited scala...
  </details>

- **2026-07-15** — Donghwan Kim — [Evaluation Ability Does Not Imply Optimization Utility: LLM-as-a-Judge Signals in Closed-Loop Table Recognition](http://arxiv.org/abs/2607.13347v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-judge is widely used to provide feedback and selection signals in closedloop regeneration, but this use remains insufficiently validated. We study it in table recognition, where deterministic TEDS evaluation provides a controlled testbed, using FinTabNet and OmniDocBench. Three findings emerge. First, judge signals were weak on both datasets: scores frequently tied, rankings were not reproducible, and the only selection policy that beat random on both datasets depended on an earliest-it...
  </details>

- **2026-07-14** — Li Hu, Guangyuan Wang, Peng Zhang et al. — [WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction](http://arxiv.org/abs/2607.12592v1)
  <details><summary>📄 Abstract</summary>
  We present WanToFight, a generative game engine that simulates real-time, two-player The King of Fighters '97 (KOF~'97) gameplay from keyboard input. Prior generative game engines target either single-player first-person settings or non-real-time cooperative scenarios; multi-player control, real-time inference, complex physical interaction, and adversarial gameplay have not been jointly addressed. WanToFight closes this gap with three components built on the Wan-1.3B video diffusion transformer:...
  </details>

- **2026-07-14** — Kunal Gupta, Gaurav Joshi, Yen-Ru Chen et al. — [Reflecting Process Expertise in Procedural Material Generation](http://arxiv.org/abs/2607.13318v1)
  <details><summary>📄 Abstract</summary>
  Procedural material creation underpins applications in digital content creation, visual effects, and 3D asset design. Achieving high-quality results requires more than reproducing node graphs -- it demands understanding the process by which experts construct materials. We formulate procedural material generation as retrieval-time process reasoning over expert demonstrations, elevating process to a first-class representation beyond graph-only synthesis. Concretely, we represent expert workflows a...
  </details>

- **2026-07-14** — Mohammad Javad Latifi Jebelli — [On Transformer Dynamics](http://arxiv.org/abs/2607.13295v1)
  <details><summary>📄 Abstract</summary>
  We develop a geometric framework in which the token dynamics of a transformer are modeled by a system of interacting particles on a Riemannian manifold $\mathcal M$, the attention mechanism being encoded by a time-independent two-body interaction law, that is, a section of the pullback bundle $π_2^{*}(T\mathcal M)$ over $\mathcal M\times\mathcal M$. Within this framework we isolate two features that a family of interaction laws must possess in order to model language: it must realize generic non...
  </details>

- **2026-07-14** — Gabriel R. S. Scapim, Gislaine C. L. Leal, Guilherme C. Guerino — [SoftBoard: A Multi-Agent Tool for the Creation and Evaluation of Low-Fidelity Prototypes](http://arxiv.org/abs/2607.13179v1)
  <details><summary>📄 Abstract</summary>
  User Experience (UX) is recognized as a critical factor for the success of digital products, particularly in software startups, environments marked by time constraints, limited resources, and low maturity in design practices. Building Minimum Viable Products (MVPs) through low-fidelity prototyping represents a well-established strategy for rapid validation cycles at reduced cost. A systematic literature mapping, however, revealed gaps in the ecosystem of available tools: a predominance of genera...
  </details>

- **2026-07-14** — Ilias Kazantzidis, Timothy J. Norman, Yali Du et al. — [Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models](http://arxiv.org/abs/2607.13172v1)
  <details><summary>📄 Abstract</summary>
  We address the problem of safely training an agent policy and deploying a good and safe policy, in settings where the environment dynamics are unknown and no suitable reward function is available. In the context of safety-critical environments, we consider traditional reinforcement learning impractical and resort to the resource of human input. We introduce DROPJ, a human-centred method for both safe training and deployment. We first learn a world model (a learned simulator) from a dataset of pr...
  </details>

- **2026-07-14** — Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban — [The Spectrum Is Not Enough: When Context Helps Time-Series Forecasting](http://arxiv.org/abs/2607.13006v2)
  <details><summary>📄 Abstract</summary>
  A growing family of indices scores how predictable a series is from its spectrum. Practitioners increasingly read these scores as answering a different question: whether \emph{adding context}, a longer lookback, a retrieval plug-in, or a pretrained model, will help. These are not the same question. The value of context is a property of the operating point, not of the series. Any index built from the power spectrum is invariant under phase randomization, whereas the beyond-second-order value that...
  </details>

- **2026-07-14** — Ruoran Xu, Wending Gao, Qiufeng Wang — [FormalAnalyticGeo: A Neural-Symbolic Based Framework for Multimodal Analytic Geometry Problem Generation](http://arxiv.org/abs/2607.12982v1)
  <details><summary>📄 Abstract</summary>
  Math reasoning has achieved significant progress with the rapid advancement of Multimodal Large Language Models (MLLMs), however analytic geometry remains largely underexplored, primarily due to the scarcity of annotated samples. Existing diagram generation approaches struggle with analytic geometry: template methods cannot handle constraint-driven layouts, and generative models lack the geometric precision to render annotated conic curves correctly. We present FormalAnalyticGeo, a scalable fram...
  </details>

- **2026-07-14** — Chalamalasetti Kranti, Sowmya Vajjala — [LLM Judges Can Be Too Generous When There Is No Reference Answer](http://arxiv.org/abs/2607.12885v1)
  <details><summary>📄 Abstract</summary>
  LLM judges are increasingly being used to evaluate open-ended model responses, often in no-reference settings where a ground-truth answer is unavailable. However, can they reliably assess in such evaluation setups? We explore this question in this paper through a two stage pipeline with a) calibration experiments that assess the judge model's knowledge of the task it is evaluating, and b) sensitivity experiments that assess how the judge model's performance is impacted by the presence and positi...
  </details>

- **2026-07-14** — Xing Zhang, Guanghui Wang, Yanwei Cui et al. — [Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents](http://arxiv.org/abs/2607.12790v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agent systems improve by creating, revising, and retiring their own skills, but every such loop rests on a hidden assumption: a reliable evaluation metric already exists. In many real applications it does not. We make three claims. First, metrics can be \emph{evolved}: our metric loop searches compositions of small drawback detectors under a full evolutionary lifecycle, trained to agree with a ten-item anchored reference set, regularized by consensus over unlabeled outputs, and aud...
  </details>

- **2026-07-14** — Cheng-Tai Hsieh, Jiwei Shan, Han Fang et al. — [ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting](http://arxiv.org/abs/2607.12785v2)
  <details><summary>📄 Abstract</summary>
  Robot-assisted minimally invasive surgery (MIS) critically depends on reliable endoscopic perception for navigation and safety. However, conventional endoscopes provide only a limited field of view, leaving large portions of the surrounding anatomy unobserved. Recent neural rendering approaches, such as Neural Radiance Fields and 3D Gaussian Splatting, enable novel view synthesis from endoscopic videos, but their reliance on sparse observations often leads to severe artifacts when extrapolating ...
  </details>

- **2026-07-14** — Quanyan Zhu — [Internet of Agentic Things: Networked AI Agents for Closed-Loop IoT Orchestration](http://arxiv.org/abs/2607.12662v1)
  <details><summary>📄 Abstract</summary>
  The paper introduces the Internet of Agentic Things (IoAT), an architectural framework that integrates agentic AI, IoT, cyber-physical systems, Physical AI, edge computing, and digital twins into a unified closed-loop orchestration framework. The proposed architecture consists of cloud, edge/fog, and physical IoT layers connected through autonomous AI agents that perceive, reason, coordinate, and actuate across distributed cyber-physical environments. The paper formalizes IoAT as a coupled workf...
  </details>

- **2026-07-14** — Amin Beheshti, Rong N. Chang, Boualem Benatallah et al. — [Agentic Service-Oriented Computing: A Manifesto for the Next Frontier of Service-Oriented Computing](http://arxiv.org/abs/2607.12619v1)
  <details><summary>📄 Abstract</summary>
  The rapid emergence of LLM-powered autonomous and semi-autonomous agents is reshaping software systems from static, request-response components into goal-directed, adaptive, and tool-using computational actors. As these agents move from isolated cognitive prototypes into complex distributed workflows, they confront challenges that the Service-Oriented Computing community has studied for more than two decades: composition, interoperability, quality of service, lifecycle management, governance, se...
  </details>

- **2026-07-14** — Yanghe Hao, Martin Huber, Christos Bergeles et al. — [Streamlining stereo differentiable rendering for marker-free real-time tracking of surgical robots](http://arxiv.org/abs/2607.12604v1)
  <details><summary>📄 Abstract</summary>
  Purpose: Marker-based tracking of surgical robots is occlusion-prone in cluttered operating rooms. We evaluate stereo differentiable rendering for marker-free, real-time robot pose tracking, potentially improving safety, reducing setup time, and enabling multi-robot interaction. Methods: We extend the markerless pose estimation framework roboreg to online dynamic tracking via (i) sequential optimisation that propagates pose estimates across frames with motion-adaptive hyperparameter tuning, and ...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 549 |
| prompt-injection | 462 |
| memory-poisoning | 37 |
| tool-use-attack | 91 |
| backdoor | 388 |
| adversarial-attack | 531 |
| privacy-leakage | 3716 |
| steganography | 52 |
| misuse | 822 |
| red-teaming | 109 |
| vulnerability | 2483 |
| defense | 2107 |
| alignment | 1948 |
| robustness | 1850 |
| watermark | 190 |
| unlearning | 82 |
| agent-safety | 48 |
| benchmark | 54 |
| survey | 247 |
| other | 5577 |

---

📚 **全部 21343 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-07-25 02:41:44*