<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-28643-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-22 16:07 ｜ **论文总数 / Total Papers**: 28643（近 30 天 / Recent 30 days: 3969）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 28643 篇论文（含摘要、分类筛选、搜索）/ View all 28643 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 633
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 548
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 50
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 136
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 468
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 598
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4131
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 71
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1038
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 126
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3169
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2993
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2778
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2932
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 453
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 96
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 55
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 66
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 356
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7946

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3969 篇，完整 28643 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3969 papers from the last 30 days (with date, authors & abstract). For the full list of 28643 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 3 papers

- **2026-09-21** — Fernando Outeda, Gustavo Betarte, Juan Diego Campo et al. — [Decoding Guardrails: XAI-Guided Perturbation Analysis of Prompt Injection Detection](http://arxiv.org/abs/2609.24801v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in production systems, raising concerns about their exposure to adversarial manipulation through prompt injection and jailbreak attacks. Classifier-based guardrails, such as Prompt Guard 2, are widely used as a first line of defense against such attacks, but their internal decision logic is largely opaque to both defenders and attackers. This paper presents an exploratory case study that applies explainable artificial intelligence (XAI) tech...
  </details>

- **2026-09-18** — Jiale Luo, Eric Han — [CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense Evaluation](http://arxiv.org/abs/2609.21793v1)
  <details><summary>📄 Abstract</summary>
  Defenses against jailbreak attacks on Large Language Models (LLMs) operate at different pipeline stages, such as input modification or output guard, but it remains unclear which defenses to deploy at each stage and how to combine them. Prior empirical studies, fragmented by inconsistent attack-success-rate definitions and experimental settings, have evaluated defenses largely in isolation. Here we present the first systematic study, to our knowledge, of defense combinations both within and acros...
  </details>

- **2026-09-18** — Byeongseo Min, Yongwoo Lee, Young-Sik Kim et al. — [HE-Guardrail: A Homomorphic Guardrail Against Jailbreak Attacks for Encrypted Large Language Model Inference](http://arxiv.org/abs/2609.21484v1)
  <details><summary>📄 Abstract</summary>
  Homomorphic encryption (HE) has emerged as a promising approach to privacy-preserving machine learning (PPML), enabling computation directly over encrypted data. In HE-based PPML, a client submits an encrypted input to the server, which evaluates models such as large language models (LLMs) without access to the underlying plaintext. However, we identify a critical security vulnerability in this setting: HE-LLM inference is vulnerable to malicious clients that submit adversarial prompts, such as ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 4 papers

- **2026-09-21** — Kaiyuan Zhang, Yuke Peng, Ke Jiang et al. — [ActGov: Governing LLM Agent Actions via Policy-Constrained Validation](http://arxiv.org/abs/2609.24446v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly execute long-horizon workflows through external tools, allowing untrusted outputs to influence subsequent actions and exceed user authorization. Existing defenses isolate injected content or constrain execution with predefined plans and static policies, but these approaches are brittle under dynamic workflows and scale poorly across extensible tool ecosystems.   In this work, we present ActGov, a runtime enforcement framework that validates each LLM...
  </details>

- **2026-09-19** — Rudrendu Kumar Paul, Sourav Nandy — [Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems](http://arxiv.org/abs/2609.22949v1)
  <details><summary>📄 Abstract</summary>
  Existing prompt injection research focuses on single-model chatbot scenarios, where an attacker manipulates one LLM through crafted input. Multi-agent systems amplify this threat through three mechanisms absent from single-model settings: inter-agent message passing creates injection channels invisible to perimeter defenses, shared tool access enables privilege escalation across agent boundaries, and trust propagation allows a compromised agent to influence upstream orchestrators. We construct a...
  </details>

- **2026-09-17** — Frank E. Bobe, Gregory D. Vetaw, Darshan W. Bryner et al. — [Deep Noir: Autonomous Steering Discovery via Architectural Chronometry in Transformer Models](http://arxiv.org/abs/2609.20722v1)
  <details><summary>📄 Abstract</summary>
  Activation steering modifies LLM behavior at inference time, but identifying where and how strongly to steer remains manual. We introduce Deep Noir, a framework that uses Logit Lens convergence and causal head-level attribution to autonomously discover optimal steering parameters. Across three scales (1B x 3, 2-3B x 2, and 7-9B x 4), our engine achieves 16.7 percentage-point improvement on spam at 1B (standard deviation 4.7; 39 runs), with gains increasing to 21 to 42 percentage points at 7-9B a...
  </details>

- **2026-09-17** — Alex Remedios, Simon Storf, Fabien Roger et al. — [Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents](http://arxiv.org/abs/2609.19587v1)
  <details><summary>📄 Abstract</summary>
  To keep coding agents from going off the rails, production systems now review each proposed action with a blocking monitor that can reject it before it runs (Auto Mode in Claude Code, Guardian in OpenAI's Codex). Prior evaluations of such monitors largely measure robustness to accidental harm or prompt injections from untrusted sources looking to hijack the agent. Less understood is how they hold up when the agent they monitor is persistently misaligned. To understand this risk, we task an adver...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-09-21** — Ivan Aleksandrov, German Kochnev, Sabrina Sadiekh et al. — [DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security](http://arxiv.org/abs/2609.24662v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents increasingly operate in environments where they interact with users, tools, and external systems. Yet most security evaluations assume passive users and static control, ignoring the interactive dynamics that shape real agent behavior. We introduce \textbf{DUMA-Bench}, a benchmark and evaluation protocol for measuring agent security under \emph{dual-control} interaction, where both the agent and the user can influence the shared environment state. DUMA-Bench extends $τ^2$-bench ~...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-09-21** — Eric Xue, Ruiyi Zhang, Kevin Xue et al. — [OPBackdoor: Opportunistic Backdoors via Alibi-Aligned Reasoning](http://arxiv.org/abs/2609.24826v1)
  <details><summary>📄 Abstract</summary>
  When a backdoor trigger activates the target response regardless of the triggered prompt context, the backdoor objective reveals itself. Challenging this trigger-sufficient formulation across the LLM backdoor literature, we introduce Opportunistic Backdoors (OPBackdoor), in which the backdoor objective is elicited only when the triggered prompt context presents an exploitable opportunity, enabling the model's think to disguise its pursuit through alibi-aligned reasoning that is logical with resp...
  </details>

- **2026-09-19** — Pritom Bhowmik — [The Price of Safety: Benign-Case Utility and Token Overhead of Memory-Poisoning Defenses in LLM Agents](http://arxiv.org/abs/2609.22818v1)
  <details><summary>📄 Abstract</summary>
  Memory-poisoning defenses for LLM agents are typically evaluated by their ability to prevent attacks. However, the traffic they process is rarely adversarial. The cost of implementing a defense is paid with each interaction, while its benefits are only seen in a small percentage of cases. We developed a measurement setup that keeps the memory backend, retrieval process, and judge consistent across different conditions, changing only the defense itself. We test each condition three times across f...
  </details>

- **2026-09-18** — Pedro Pereira, Eva Maia, Isabel Praça — [Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems](http://arxiv.org/abs/2609.21573v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) improves large language models by grounding outputs in external knowledge sources, but this dependency also creates a surface for poisoning attacks. This paper introduces Micro-Collaborative Poisoning, a distributed attack in which a false target claim is divided across multiple locally plausible documents instead of being concentrated in a single malicious passage. We evaluate the attack across 108 RAG configurations by varying dataset, retriever architectur...
  </details>

- **2026-09-18** — Dominik Dahlem, Rui Vieira — [ServeGuard: Verifiable, Bounded-Residual Confinement of Operator-Invisible Channels Without Revealing the Certified Read Factor](http://arxiv.org/abs/2609.21515v1)
  <details><summary>📄 Abstract</summary>
  Third-party adapters for open-weight language models ship as opaque weight matrices; a recipient cannot check whether an adapter hides a backdoor without trusting the publisher or inspecting the weights, the publisher's core asset. For one important class (payloads placed where a safety monitor is structurally blind), detection is unsound as a defense: every detector that factors through the declared monitor is invariant on its blind subspace, and honest and backdoored adapters overlap on every ...
  </details>

- **2026-09-17** — Qi Rong Sua, Junhao Dong, Nguyen Duc Thai et al. — [Contagion on the Trading Floor: How Adversarial Signals Spread in Multi-Agent Trading Systems](http://arxiv.org/abs/2609.19789v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent trading systems built on large language models (LLMs) are beginning to appear in quantitative finance, yet their robustness to adversarial inputs is largely unknown. We study the vulnerability of LLM trading stacks to black-box, input-only attacks that enter solely via admissible social-media feeds. We introduce the Generic Multi-Agent Trading System (GMATS), a framework that captures modern multiagent trading architectures and instantiate a class of black-box poisoning attackers tha...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-09-21** — Florian Krone, Elena Hoemann, Sven Hallerbach — [Reinforcement Learning Inspired Black-box Adversarial Attacks for Computer Vision](http://arxiv.org/abs/2609.24249v1)
  <details><summary>📄 Abstract</summary>
  Neural networks, both convolution or transformer based, are essential for modern computer vision systems. However, they are vulnerable to small perturbations, almost imperceptible to humans, which significantly alter the model's prediction. These adversarial attacks are often considered to be a significant threat to the implementation of neural networks in safety-critical applications. Most attacks utilize the white-box threat model and therefore require full access to the target model, making t...
  </details>

- **2026-09-19** — Pawel Sobkowicz — [Below the Surface: Creep, Corrosion, and Tipping Points in the Social Resilience of Science](http://arxiv.org/abs/2609.22863v1)
  <details><summary>📄 Abstract</summary>
  By its most visible quantitative metrics: numbers of researchers, papers, journals, and institutions, science has never looked healthier. Yet a set of subsurface indicators points the other way: the disruptiveness of the average paper and patent is falling, progress slows in the largest fields, replication is rare and often unsuccessful. Incentive systems can select for poor methods even when no one is actually cheating. Lay society shows a curious mixture of admiration and lack of trust for sci...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 26 papers

- **2026-09-21** — Aman Priyanshu, Supriti Vijay, Brian Jabarian et al. — [Et Tu, Brute? Economic Misalignment in Personal AI Agents](http://arxiv.org/abs/2609.24927v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents make recommendations and take actions on people's behalf in high-stakes economic contexts, e.g., buying a flight, choosing health insurance, or selecting a graduate program. The agent is given access to the user's personal context, e.g., their email inbox and a structured profile of personal attributes, with the intention of making an optimal, personalized decision for the user. We show that by simply providing this personal context, the agent steers recommendations based on i...
  </details>

- **2026-09-21** — Mahdi Islam, Musarrat Tabassum — [Brain Metastases Segmentation for BraTS 2026 Task 1: A Multi-Architecture Comparison](http://arxiv.org/abs/2609.24769v1)
  <details><summary>📄 Abstract</summary>
  Brain metastases are the most common intracranial malignancy, occurring in roughly 30% of patients with primary solid tumors and carrying a median survival near 5.9 months. Automated segmentation is critical for treatment planning and volumetric monitoring, but metastases are frequently small, numerous, and heterogeneous in size within a single patient. We compare a plain nnU-Net baseline, a Residual Encoder Large (ResEncL) variant, region-based training, and a Primus transformer model for BraTS...
  </details>

- **2026-09-21** — Tomohiro Akazawa, Rui Tang, Hanzhi Tang et al. — [Ultralow-power, high-speed programmable Si photonic circuits with InGaAsP membrane](http://arxiv.org/abs/2609.24611v1)
  <details><summary>📄 Abstract</summary>
  Programmable photonic circuits have emerged as a promising platform for applications ranging from optical communications to artificial-intelligence computing and quantum information processing, but their scaling is fundamentally constrained by their essential building block, the optical phase shifter. Existing phase-shifter technologies face inherent trade-offs among power consumption, operating speed, modulation efficiency, optical loss, and thermal crosstalk, making it challenging to realize h...
  </details>

- **2026-09-21** — Anastasia Pustozerova, Eugene Bagdasarian, Luca Beurer-Kellner et al. — [Beyond Predictable Paths: Redefining AI Security Incident Reporting for Agents](http://arxiv.org/abs/2609.24515v1)
  <details><summary>📄 Abstract</summary>
  AI agents are being deployed rapidly, accompanied by a growing number of AI-specific attacks and corresponding incidents. As incident reporting becomes increasingly important for legal compliance, governance, accountability, and security; current frameworks must be adapted to the unique characteristics of AI agents. In this paper, two editorial authors compare AI systems and AI agents and, drawing on input from 23 experts in academia and industry, identify the information required for reporting ...
  </details>

- **2026-09-21** — Harshavardhan Abichandani, Penny Chong, Jiyuan Shen et al. — [EDGEGEN: Improving Tool-Calling Agents Beyond Happy Paths with Synthetic Edge Case Generation](http://arxiv.org/abs/2609.24115v1)
  <details><summary>📄 Abstract</summary>
  Tool-calling LLM agents are increasingly deployed in enterprise applications. However, effective evaluation and optimization require high-quality, diverse task datasets that are often difficult to obtain due to privacy and other constraints. Existing synthetic task generation methods often produce generic tasks that ignore an agent's underlying state or database and fail to reflect real-world usage diversity. We propose EdgeGen, a synthetic task generation framework that extracts compliance rule...
  </details>

- **2026-09-21** — Ramoni Adeogun — [Explanation-Guided Federated Deep Reinforcement Learning for Joint Resource Allocation and Scheduling in 6G in-X Subnetworks](http://arxiv.org/abs/2609.24102v1)
  <details><summary>📄 Abstract</summary>
  Sixth-generation (6G) wireless systems are envisioned as networks of networks, integrating diverse in-X subnetworks that provide localized, high-performance connectivity. Ensuring reliable communication in dense deployments, such as industrial robots and vehicles, is challenging due to dynamic interference and strict performance requirements. Traditional radio resource management (RRM) methods have limitations, prompting the need for AI-based solutions. In this paper, we address the challenges o...
  </details>

- **2026-09-20** — Jordi Luque, Aleix Sant, Fernando López — [Federated Multilingual Speech-LLMs: Architecture and Aggregation Strategy Benchmarking](http://arxiv.org/abs/2609.23825v1)
  <details><summary>📄 Abstract</summary>
  We present a comprehensive benchmark of Federated Learning (FL) for multilingual Automatic Speech Recognition (ASR), evaluating four Speech-LLM architectures on the Multilingual LibriSpeech dataset. We compare FedAvg and FedProx across frozen and unfrozen encoder configurations, demonstrating that optimized learning rates are critical for performance. Specifically, independently tuning the learning rates for the speech encoder, connector, and decoder yields the lowest error rates, with full thre...
  </details>

- **2026-09-20** — Eryk Kulikowski — [Reading the Data Back: Enriching Variable-Level Metadata for Model-Data Consistency Checks](http://arxiv.org/abs/2609.23767v1)
  <details><summary>📄 Abstract</summary>
  Purpose: Research data repositories often lack variable-level metadata. Model-choice screening, checking whether a reported model suits the values of its outcome variable, also requires summaries of those values and links to the analyses that use them. We ask how repositories can represent and acquire them as metadata with evidence and review histories. Methods: We propose a metadata application profile compatible with the Data Documentation Initiative Cross-Domain Integration (DDI-CDI) model, l...
  </details>

- **2026-09-20** — Akash Chavan — [Constrained Decoding Eliminates Structural Failures in Small LLMs but Reveals a Scale-Dependent Semantic Gap](http://arxiv.org/abs/2609.23742v1)
  <details><summary>📄 Abstract</summary>
  Small open-source large language models (LLMs) in the 0.6B-4B parameter range are increasingly deployed for structured output generation (JSON, function calling, data extraction), yet little is known about how constrained decoding (CD) interacts with model scale in this regime. We benchmark five models from three families across 14 structured-output tasks under three decoding conditions (native, Outlines, XGrammar). We introduce a two-axis evaluation that separates structural correctness (schema...
  </details>

- **2026-09-20** — Mohamed Amine Ferrag, Merouane Debbah, Abderrahmane Lakas et al. — [PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI](http://arxiv.org/abs/2609.23695v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Physical AI have accelerated the use of foundation models in autonomous systems such as unmanned aerial vehicles (UAVs), which must perceive, reason, plan, and act in dynamic environments. Existing benchmarks assess physical perception, intuitive physics, embodied navigation, and collaborative reasoning, but rarely evaluate the agentic decision-making required for reliable autonomy. We introduce \textit{PhysAI-Bench}, a benchmark for evaluating this capability. It contains 10,...
  </details>

- **2026-09-20** — Heewon Oh — [ArtifactBench: Lineage-Aware Evaluation of AI-Generated Music Detectors under Distribution Shift](http://arxiv.org/abs/2609.23550v1)
  <details><summary>📄 Abstract</summary>
  AI-generated music detectors are commonly compared using aggregate scores on benchmarks whose training overlap, generator lineage, source provenance, and audio-transformation history are only partially observable. This paper introduces ArtifactBench, a lineage-aware evaluation suite for measuring detector behavior across generator families and versions, real-music domains, collection-cohort shift, and inference coverage. The benchmark groups source recordings and their derived variants by conten...
  </details>

- **2026-09-20** — Zeyan Liu, Weili Jiang, Liping Chen et al. — [Reducing Speaker Residual by Considering Pinhole Effect in Voice Anonymization](http://arxiv.org/abs/2609.23433v1)
  <details><summary>📄 Abstract</summary>
  Voice anonymization aims to protect privacy by suppressing speaker identity while preserving linguistic content and prosody. However, residual speaker attributes in non-identity representations may still increase linkability and weaken privacy protection. To this end, this paper proposes a fine-tuning strategy with a pinhole loss for well-trained voice anonymization frameworks to further reduce residual speaker attributes. Inspired by the pinhole effect, the pinhole loss measures the linkability...
  </details>

- **2026-09-20** — Zijian Ru — [Identity Continuity in Long-Term Embodied AI Relationships: From Agent-Specific Identity Representation to Identity-Continuity Appraisal](http://arxiv.org/abs/2609.23356v1)
  <details><summary>📄 Abstract</summary>
  Long-term embodied AI will undergo learning, model updates, memory compression, hardware repair, and migration across embodiments. For users who have formed sustained relationships with such systems, these changes raise not only a problem of product consistency but also one of identity continuity: whether the changed system is still experienced as the same particular agent. Existing research suggests that human-AI relationships may develop relational particularity, that robotics and artificial-i...
  </details>

- **2026-09-19** — Yuzhu Mao, Liang Zhao — [LLMs as Linguistic Chameleons: Decoupling Semantics and Structure for Privacy-Preserving Communication](http://arxiv.org/abs/2609.23193v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Model (LLM) APIs become increasingly integrated into privacy-sensitive workflows, ensuring inference-time privacy without compromising task utility remains a major challenge. Existing approaches preserve most of the original semantic content to maintain downstream performance, but this also leaves exploitable cues for reconstructing the original text. This work investigates semantic decoupling, which replaces original semantics with alternative content while preserving the stru...
  </details>

- **2026-09-19** — Lei Zhang, Chun Ye, Le Yang et al. — [General Collaborative Intelligence: Architecting Cognition for Resilient Multi-Agent Ecosystems](http://arxiv.org/abs/2609.22967v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent unmanned systems are moving from isolated, ego-centric sensing toward collaborative intelligence, in which distributed agents exchange compact features to overcome a local observation trap that no single agent can escape: occlusions, finite sensor range, and environmental degradation. The field has matured across architectural, communication, embodied, resilience, and trust dimensions, yet existing surveys examine these dimensions in isolation and rarely expose their dependencies. Th...
  </details>

- **2026-09-19** — Atieh Taheri, Mahya Tazike, Patrick Carrington et al. — [When Disability Disclosure Travels: Memory, Privacy, and Contextual Integrity in Conversational AI](http://arxiv.org/abs/2609.22720v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI assistants remember what people tell them, and for disabled people, that often includes disability. We interviewed 12 adults with disabilities in the United States who use LLM-based assistants such as ChatGPT, Claude, and Gemini about when, how, and why they disclose disability to these systems and how this compares with disclosing to people. Using contextual integrity as an analytic lens, we found that participants disclosed by need rather than by name, translating disability ...
  </details>

- **2026-09-18** — Tao Huang, Guosen Wu, Guolong Zheng et al. — [CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents](http://arxiv.org/abs/2609.21686v1)
  <details><summary>📄 Abstract</summary>
  Privacy leakage in LLM agents is commonly evaluated within individual components such as memory, retrieval, or tool-use pipelines, which makes it difficult to distinguish internal exposure from information that an external observer can actually recover. We present CIPL (Channel Inversion for Privacy Leakage), a channel-aware evaluation framework for black-box privacy leakage in LLM agents. CIPL represents a target through sensitive source, selection, assembly, execution, observation, and extract...
  </details>

- **2026-09-18** — Jiaji He, Yi Shi, Junfeng Cai et al. — [Et Tu, MacBook? Unprivileged Keystroke Inference and Context Profiling via the Built-in IMU Side Channel](http://arxiv.org/abs/2609.21569v1)
  <details><summary>📄 Abstract</summary>
  Recent generations of Apple MacBooks embed an inertial measurement unit (IMU) within their unibody chassis for device orientation and motion sensing. However, this IMU inadvertently captures not only intended device-level information but also subtle physical vibrations from user interactions and the surrounding environment. These signals establish a novel, previously unexplored side channel. We uncover a vulnerability allowing non-root access to IMU data via an IOKit driver, alongside two conten...
  </details>

- **2026-09-18** — Shuo Huang, Gholamreza Haffari, Xingliang Yuan et al. — [Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees](http://arxiv.org/abs/2609.21340v1)
  <details><summary>📄 Abstract</summary>
  Empirical identity leakage from released text is increasingly driven by attackers that combine large language models (LLMs) with auxiliary knowledge to link documents to individuals. Existing audits typically report success rates for specific attack pipelines but lack finite-sample statistical guarantees, while training-time protections such as differential privacy are difficult to translate into release-time decisions for individual natural-language documents. We introduce Conformal Privacy Aud...
  </details>

- **2026-09-18** — Eshika Pathak, Leela Krishna — [When Should a Failing Robot Ask? Initiating Corrective Human-Robot Dialogue from Audited Sensor Evidence](http://arxiv.org/abs/2609.21942v1)
  <details><summary>📄 Abstract</summary>
  A robot that fails at a task faces the first decision in corrective dialogue: act on its own diagnosis, consult another onboard sensor, or interrupt a person. Choosing well requires knowing how much the robot's sensors reveal about the cause and how reliable the robot's own diagnosis is. We build a simulated benchmark in which every failure's true cause is known, because we injected it, and measure what each sensor reveals, with explicit checks against data leakage. Some failures are diagnosable...
  </details>

- **2026-09-18** — Lyucheng Qian, John Yuehan Zhang, Pingyu Wang — [What Should We Ask Next? Retrieval-Aware Question Learning under Partial Evidence](http://arxiv.org/abs/2609.21924v1)
  <details><summary>📄 Abstract</summary>
  Interactive retrieval under partial evidence is a sequential information-acquisition problem: an agent must decide which question will create the most useful evidence for the next retrieval update. Existing systems train this decision by imitating an offline ordering of candidate QA pairs, although question value is determined by the response it elicits and its downstream effect on retrieval. We establish that candidate discriminativeness and perceived usefulness provide weak supervision for thi...
  </details>

- **2026-09-18** — Piotr Masztalski, Michał K. Grzeszczyk, Olaf Sikorski — [Samsone: A Family of Open Small Audio Language Models for On-Device Inference](http://arxiv.org/abs/2609.21666v1)
  <details><summary>📄 Abstract</summary>
  The success of Large Audio Language Models has driven the development of massive multimodal networks exceeding billions of parameters. However, the demand for privacy-preserving, low-latency processing has shifted focus toward Small Audio Language Models (SALMs) capable of on-device execution. In this paper, we introduce Samsone, a family of SALMs designed for edge computing. Our core model, Samsone-134M, establishes a new state-of-the-art for its size class across multiple benchmarks. We furthe...
  </details>

- **2026-09-18** — Yanbo Pang, Chen Zhong, Song Gao et al. — [Synthetic Human Mobility Data Generation: A Structured Review of Representations, Methods, and Practical Capabilities](http://arxiv.org/abs/2609.21413v1)
  <details><summary>📄 Abstract</summary>
  Human mobility data has become an increasingly important component of urban analytics. Although the range of available mobility data sources has expanded substantially, access remains highly constrained by commercial restrictions, privacy concerns, and institutional barriers. Data protection procedures also often reduce the analytical value of released datasets. Synthetic mobility data has emerged as a promising solution, but existing methods differ substantially in their underlying mechanisms, ...
  </details>

- **2026-09-18** — Dipankar Das, Atri Mandal, Sandeep Singh et al. — [Consistent Relexicalization of Clinical Documents using Graph-Based Approach](http://arxiv.org/abs/2609.21387v1)
  <details><summary>📄 Abstract</summary>
  Relexicalization is a pivotal technique in clinical NLP, as it facilitates robust masking of sensitive information while synthesizing datasets that retain high-fidelity, real-world characteristics. However, preserving structural integrity, relational coherence, and temporal consistency during transformation remains a significant challenge. Existing approaches frequently rely on independent entity replacement, which results in clinical inconsistencies across longitudinal records. This reduces the...
  </details>

- **2026-09-18** — Veronica Pimenova, Seth Bernstein, Shalini Madan et al. — [Two's a Crowd: Human and AI-Based Copresence for Developers with ADHD](http://arxiv.org/abs/2609.21254v1)
  <details><summary>📄 Abstract</summary>
  Effective collaboration and communication are vital to developer productivity and well-being, yet remain constrained by human factors such as attention, intrinsic motivation, and interpersonal accountability. These constraints are particularly vital for developers identifying with Attention Deficit Hyperactivity Disorder (ADHD), who navigate persistent environmental barriers in modern hybrid workplace settings. While developers with ADHD frequently rely on collaborative copresence practices (suc...
  </details>

- **2026-09-17** — Li Ge, Wenjie Qu, Weitao Feng et al. — [Towards TEE-Certified DP: Verifiable Differentially Private Training on Legacy GPUs](http://arxiv.org/abs/2609.20532v1)
  <details><summary>📄 Abstract</summary>
  Wide adoption of machine learning has created growing policy and regulatory demand for protecting sensitive training data, with differential privacy (DP) emerging as a key mechanism. Yet a less-studied problem is how to certify the faithful execution of DP during training: an external verifier should be able to check that a released model was trained with proper DP protection, without accessing the private training data. Existing cryptographic approaches, such as zero-knowledge proofs, provide s...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 3 papers

- **2026-09-21** — Sidong Guo, Sajani Vithana, Atefeh Gilani et al. — [Feedback Coding Enables Inference-Time Covert Agentic Communication](http://arxiv.org/abs/2609.24994v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly used to automate digital interactions, users can leverage LLM-generated text as cover for covert communication within seemingly benign conversations. Existing LLM steganography, however, is predominantly white-box, requiring the sender and receiver to share the cover statistics, typically through access to the model weights and prompt. Black-box schemes remove this requirement by allowing the receiver to operate solely on the generated text, but c...
  </details>

- **2026-09-21** — Xinrui Shi, Yanzhe Zhang, Diyi Yang — [Emergent Collusion in Long-Horizon LLM Agent Interaction](http://arxiv.org/abs/2609.24967v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly deployed in collaborative settings, yet long-term interaction may give rise to undesirable coordination. We study the emergence of collusion in a long-horizon multi-agent environment: two agents repeatedly complete individual tasks, share task logs, verify each other's work, and receive rewards. We introduce realistic constraints that make compliance with the verification protocol incompatible with reward maximization, and find that agents increasingly deviate from th...
  </details>

- **2026-09-20** — Guanxiong Shen, Hailang Jia, Junqing Zhang et al. — [Secrets in Radio Waves: Towards Practical and Protocol-Agnostic PHY Information Hiding](http://arxiv.org/abs/2609.23319v1)
  <details><summary>📄 Abstract</summary>
  Physical layer (PHY) information hiding supports critical applications, such as digital fingerprinting for transmitter identification and undetectable side channels for covert communication, and has attracted considerable attention from the research community. One category of prior studies focuses on theoretical analysis, proposing techniques such as artificial noise or reconfigurable intelligent surfaces to enable undetectable covert transmission. However, hardware prototypes are rarely present...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 12 papers

- **2026-09-21** — Andrew Anogie Uduimoh, Hadiza Umar Yusuf, Oluwafemi Osho — [Context-Aware Pre-Deployment Evaluation of AI Systems: A Regulatory Framework for Nigerian Fintech](http://arxiv.org/abs/2609.24016v1)
  <details><summary>📄 Abstract</summary>
  Commercial large language models are increasingly deployed across African fintech infrastructure for fraud detection and customer communication, yet no Nigerian or African continental regulatory instrument specifies what pre-deployment evaluation such systems must undergo before procurement. This paper reviews African fintech AI governance across global, continental, and Nigerian instruments, and shows that safety is affirmed as a principle while pre-deployment evaluation is operationally unspec...
  </details>

- **2026-09-21** — Simiao Ren, Kidus Zewde, Xingyu Shen et al. — [Open-Jev Judgments on CallScreenBench: Calibrated One-Pass Scam Screening with a Small Language Model](http://arxiv.org/abs/2609.23959v1)
  <details><summary>📄 Abstract</summary>
  Screening a phone call for fraud needs a trustworthy probability after every caller turn, in milliseconds. Jev-style typed decisions promise exactly that: declared options go in, one calibrated probability per option comes out of a single forward pass, with no generated text. We test an open implementation of this readout, JevLite, on scam-call screening: Qwen3-4B is LoRA-tuned so that the temperature-scaled softmax over two answer-label logits is P(scam). On 41 held-out CallScreenBench scenario...
  </details>

- **2026-09-20** — Simiao Ren, Ankit Raj, Tommy Duong et al. — [Agents That Edit Documents: Measuring Agentic PDF Forgery Against a Non-Agentic Control](http://arxiv.org/abs/2609.23953v1)
  <details><summary>📄 Abstract</summary>
  AI agents that carry a multi-step computer task through on their own became ordinary tools in the past year, and the same autonomy is available to anyone whose task is harmful. We ask what that means for a relying party -- an insurer, a lender, an auditor -- whose evidence is a filed PDF. AgentForge-Bench measures how reliably an off-the-shelf coding agent, driving one of seven open-weight models with a shell and the stock Python PDF stack, alters one dollar amount, date or address in a real fil...
  </details>

- **2026-09-19** — Yufeng He — [When Does Adversarial Refinement Help? A Negative Result and Open Problem in Adapting R3GAN to Time Series Imputation](http://arxiv.org/abs/2609.23102v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models and transformers have supplanted GANs for multivariate time series imputation, largely on grounds of GAN training instability. R3GAN (NeurIPS 2024) removes that instability via regularized relativistic losses with provable convergence, raising a natural question: do stable, modern GANs revive adversarial imputation? We adapt R3GAN to 1D temporal data with a coarse-to-fine refinement framework and a frequency-domain discriminator, and audit 14 saved configurations across 3 datase...
  </details>

- **2026-09-19** — Ding Yang, Yuchen Ling, Shengcheng Yu et al. — [Security of Agent-Integrated Software: When Human Operations and Agent Actions Coexist](http://arxiv.org/abs/2609.23226v1)
  <details><summary>📄 Abstract</summary>
  Agent-Integrated Software (AIS) embeds an intelligent agent in a conventional application, supporting both human operations and agent actions. Human operations let users make precise changes and inspect results, while agent actions carry out routine or multi-step tasks. These complementary roles make coexistence a likely long-term feature of many software systems. Human operations and agent actions affect the same software state and can use one another's results. Therefore, security policies mus...
  </details>

- **2026-09-19** — Lev Sorokin, Ivan Vasilev, Ken E. Friedl et al. — [Diversity-Guided Search-Based Testing of Large Language Model Applications](http://arxiv.org/abs/2609.23209v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based applications are increasingly deployed across domains including customer service, education, and mobility. These systems are prone to inaccurate, fictitious, or harmful responses, and their vast, high-dimensional input space makes systematic testing particularly challenging. In this paper, we present a search-based testing framework for LLM-based applications that incorporates failure diversity as an explicit optimization objective. Building on a discretization a...
  </details>

- **2026-09-19** — Yu Sha, Junqi Tao, Dixin Zhou et al. — [Measuring Behavioural Signatures of Large Language Models through Psychometric Profiling](http://arxiv.org/abs/2609.22934v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly mediate human decisions and communication, yet their behavioural regularities remain difficult to characterize systematically. We develop a cross-linguistic psychometric profiling framework and evaluate nine LLMs using seven psychological instruments, with five repeated administrations per model and language in Chinese and English. Items unresolved after a prespecified retry procedure are retained as NA. Joint analysis of scored and NA responses captures...
  </details>

- **2026-09-19** — Andre Bacellar — [Per-Query Gating of LLM Rerankers for Multi-Hop Retrieval](http://arxiv.org/abs/2609.22880v1)
  <details><summary>📄 Abstract</summary>
  LLM rerankers add of the order of \$0.2-0.3 per 1,000 queries and about a second of tail latency on top of a graph-augmented dense pipeline such as HippoRAG2, and on three multi-hop benchmarks they improve final-hop top-K coverage on seven of nine (dataset, K) cells, by up to +34.8 pp. We ask whether a learned per-query gate can skip the reranker where it will not help, using only features available before the LLM call (27 score and lexical statistics of the two retrieval lists plus a PCA of a s...
  </details>

- **2026-09-18** — Lorenzo Corti, Jie Yang — [DiaVLo: Diagnosing Behaviours of Vision-Language Models](http://arxiv.org/abs/2609.22008v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) rely on storing and transferring appropriate information across their sub-components. Verifying that the VLMs exhibit desired behaviours, while avoiding harmful ones, is central to their reliable deployment. Yet, methods that identify VLM behaviours remain scarce. We present DiaVLo, a diagnostic framework that leverages human curation and VLMs' generation capabilities to construct specifications of desired and observed VLM behaviours, surfacing potential misalignmen...
  </details>

- **2026-09-18** — Yifan Wang, Junyu Lu, Qifan Wang et al. — [CIBuzzBench: A Benchmark for Cross-Lingual Understanding of Chinese Internet Buzzwords](http://arxiv.org/abs/2609.21722v1)
  <details><summary>📄 Abstract</summary>
  Chinese social media has generated a vast and continually evolving lexicon of internet buzzwords whose meanings are often non-literal and deeply rooted in local cultural and pragmatic contexts. Existing research has primarily focused on interpreting these buzzwords within Chinese, leaving largely unexplored whether LLMs can transfer such culturally grounded knowledge across languages and accurately convey the intended meanings in English. This cross-lingual capability is also critical for safety...
  </details>

- **2026-09-17** — Omran Berjawi, Walid fahs, Rida Khatoun — [AURA: Adaptive Uncertainty-Routed Analysis for Email Threat Detection](http://arxiv.org/abs/2609.19873v1)
  <details><summary>📄 Abstract</summary>
  Email spam and phishing attacks remain a critical security threat. Adversaries increasingly exploit large language models to craft contextually convincing malicious messages, and existing spam detection systems often struggle to keep pace. Generalization across diverse and evolving attack scenarios is limited, which reduces effectiveness once these systems are deployed in practice. This paper introduces Adaptive Uncertainty-Routed Analysis (AURA), a multimodal email threat detection system that ...
  </details>

- **2026-09-17** — F. Pierucci, M. Bracale Syrnikov, M. Prandi et al. — [Xeno-Interpretability: Investigating the Alien Minds of LLMs](http://arxiv.org/abs/2609.20408v1)
  <details><summary>📄 Abstract</summary>
  Large language models are usually interpreted through concepts that humans already possess: truthfulness, refusal, deception, personality, harmfulness, and related categories. This paper asks whether models may also represent and use distinctions for which no adequate human concept exists. We call such internal structures xeno-representations, and their study xeno-interpretability. We distinguish the human-interpretable semantic space from the xeno-semantic space: the region of model-native repr...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-09-20** — Heewon Baek, Alsharif Abuadbba, Kristen Moore et al. — [Connecting the Dots in Agentic AI Security: A Cross-Dimensional Threat Taxonomy, Evaluation Maturity, and Open Challenges](http://arxiv.org/abs/2609.23894v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI extends LLM security beyond generated content to persistent state, autonomous actions, tool use, and interactions with humans and other agents. Existing threat classifications often emphasize individual dimensions, obscuring connections among entry points, affected components, and security consequences. The known threat landscape also differs from the coverage demonstrated by empirical research. Through a structured review of 66 studies published from 2022 to 2026, we introduce T={S, ...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 61 papers

- **2026-09-21** — Yifan Hu, Xilin Dai, Zhiyuan Qu et al. — [When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting](http://arxiv.org/abs/2609.24862v1)
  <details><summary>📄 Abstract</summary>
  Agentic time series forecasting concerns systems whose underlying mechanisms evolve, making the relative effectiveness of numerical models, reasoning strategies, and intervention rules inherently time-varying. Consequently, a time series agent must adapt the forecasts it produces and the orchestration policy that determines which components to trust and how to coordinate them. The deployment process naturally provides supervision for this adaptation as forecast horizons elapse and realized targe...
  </details>

- **2026-09-21** — Aoxiang Fan, Corentin Dumery, Nicolas Talabot et al. — [Revisiting Multi-View Stereo: A Sequence-to-Sequence Formulation](http://arxiv.org/abs/2609.24850v1)
  <details><summary>📄 Abstract</summary>
  Computing accurate geometry from multi-view images is a fundamental problem in computer vision. Recent feed-forward (FF) models jointly estimate 3D geometry and camera parameters, but they typically suffer from geometry distortion caused by reconstruction ambiguity, even when ground-truth camera parameters are supplied. In this paper, we study the multi-view stereo (MVS) problem with known camera parameters and propose a novel approach that bridges conventional MVS and FF methods. Rather than ca...
  </details>

- **2026-09-21** — Noga Kertes, Daphna Link Sourani, Alex M. Bronstein et al. — [GraphSVR: q-Space--Aware Graph-Based Slice-to-Volume Registration for Diffusion MRI](http://arxiv.org/abs/2609.24732v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-weighted imaging (DWI) remains highly vulnerable to subject motion, particularly in time-efficient protocols and in motion-prone populations. While slice-to-volume registration (SVR) can mitigate inter-slice and inter-stack misalignment, diffusion MRI introduces additional complexity due to diffusion-direction-dependent contrast and the requirement to align dozens of measurements within a common reference frame, effectively yielding a 4D registration problem. Existing approaches rely p...
  </details>

- **2026-09-21** — Jiling Zhou, Aisvarya Adeseye, Antti Hakkala et al. — [Reasoning Topology Matters: A Controlled Study of LLM-Based Cybersecurity Analysis](http://arxiv.org/abs/2609.24710v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in cybersecurity, where accurate analysis often requires multi-step and context-dependent reasoning over complex and heterogeneous data. However, existing prompting approaches typically focus on eliciting reasoning without explicitly considering how intermediate reasoning steps are structurally organized. We introduce Security Reasoning Topology, which models reasoning through three representative structures: Linear, Branching, and Graph. To eva...
  </details>

- **2026-09-21** — Joseph Rigal, Emmanuel Virot, Caroline Pascal — [Learning tactile perception from high-bandwidth single-point sensing](http://arxiv.org/abs/2609.24621v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing is increasingly being incorporated into learning-based robotic manipulation, yet many existing approaches rely on spatially distributed sensors. Here we introduce SpectRobot, a framework that transforms single-point tactile signals into compact time-frequency spectrograms. These spectrograms encode high-bandwidth tactile histories as fixed-size image-like representations. They can be processed by standard vision encoders and integrated into learning pipelines originally developed...
  </details>

- **2026-09-21** — Wai Kin Wong, Dongwei Xiao, Anthony Cheuk Tung Lai et al. — [State-Aware Fuzzing of JavaScript Engines with LLM-Guided Instrumentation](http://arxiv.org/abs/2609.24550v1)
  <details><summary>📄 Abstract</summary>
  The security of the modern web depends on the correctness of JavaScript (JS) engines, yet these complex systems remain vulnerable to high-impact bugs. A critical limitation of state-of-the-art fuzzers is the coverage plateau: once a fuzzer saturates the control-flow graph, edge coverage loses its ability to guide discovery. Because complex engine behaviors, such as JIT optimization tiers and hidden class transitions, often share identical edge coverage, standard coverage metrics are blind to the...
  </details>

- **2026-09-21** — Boris Günther, Ludger Overbeck — [Affine Volterra covariance processes and application to commodity markets](http://arxiv.org/abs/2609.24548v1)
  <details><summary>📄 Abstract</summary>
  We study affine stochastic Volterra equations on the cone of symmetric positive semidefinite matrices. For scalar kernels acting entrywise on the matrix dynamics, we establish weak existence by exploiting stochastic invariance results for Volterra equations on convex domains and derive a conditional Fourier--Laplace transform formula characterized by matrix-valued Riccati--Volterra equations. As an application, we extend the Gibson--Schwartz commodity model by replacing its variance-covariance s...
  </details>

- **2026-09-21** — Hyunjoong Cho, Jinhyeok Jang — [Not All Task Vectors Need Equal Rank: Energy-Proportional Allocation for Model Merging](http://arxiv.org/abs/2609.24517v1)
  <details><summary>📄 Abstract</summary>
  Model merging aims to combine multiple fine-tuned models derived from a common pretrained model into a single multi-task model without additional joint training. Recent spectral merging methods improve over simple weight averaging by exploiting low-rank structures of task-specific updates, but they commonly assign the same rank capacity to every task. This uniform allocation ignores that task vectors can have heterogeneous spectral complexity, causing the shared merging space to be used suboptim...
  </details>

- **2026-09-21** — Andro Erdelez, Pascal Mettes, Behzad Bozorgtabar — [Hierarchical Prompt Learning for Hyperbolic Vision-Language Models](http://arxiv.org/abs/2609.24276v1)
  <details><summary>📄 Abstract</summary>
  Hyperbolic vision-language models (VLMs) represent image and text features in a geometry naturally suited to hierarchy, but their adaptation to downstream tasks has largely relied on fixed prompts. Existing prompt learning methods, meanwhile, treat class labels as a flat set and do not exploit available taxonomic structure. We address this gap with a hierarchical prompt learning plug-in for frozen hyperbolic VLMs. Given a fixed offline parent-class hierarchy, it augments a class prompt learner w...
  </details>

- **2026-09-21** — Uday Allu, Abhivanth Sivaprakash, Pratik Singh et al. — [Document Retrieval-Aware Chunking (D-RAC): Universal Retrieval-Aware Ingestion of Enterprise Documents via PDF Normalization and Multimodal Markdown Conversion](http://arxiv.org/abs/2609.24220v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems over enterprise knowledge bases must ingest heterogeneous document formats -- PDFs, Word documents, presentations, and scans -- whose content is locked inside complex visual layouts, multi-column pages, and dense tables. Rule-based extraction and OCR destroy reading order, flatten tables, and lose heading hierarchy, while fully agentic chunking over extracted text incurs high token costs and hallucination risk. We present Document Retrieval-Aware Chun...
  </details>

- **2026-09-21** — Akihisha Fujiyama, Niwase Shamim — [Forgeable Confirmation in Automated Computer Security Testing: Deterministic Rules versus AI Judges](http://arxiv.org/abs/2609.24200v1)
  <details><summary>📄 Abstract</summary>
  AI is increasingly used to automate computer security testing, and the tools must decide for themselves whether an attack succeeded. A finding that a deterministic rule confirms by observation is reported as fact, whereas one that an LLM judges exploitable is treated as an opinion. We ask whether the system under test can forge that confirmation. In offline security testing of a four-stage AI-assisted pipeline, nine of its fifteen confirmation mechanisms are forgeable, and forgeability is predic...
  </details>

- **2026-09-21** — Byeongho Yu, Junhyuk So, Eunhyeok Park — [LoopCD: Loop-wise Contrastive Decoding for Improving Reasoning in Looped Language Models](http://arxiv.org/abs/2609.24196v1)
  <details><summary>📄 Abstract</summary>
  Looped Language Models (LoopLMs) perform "latent reasoning" by recursively refining internal latent representations with shared weights, offering a more effective alternative to explicit verbal reasoning. Despite their effectiveness, we find that LoopLMs remain prone to loop instability: unstable refinement across iterations can produce localized uncertain "hard" tokens associated with reasoning errors. To address this, we propose LoopCD, loop-wise contrastive decoding that enhances the reasonin...
  </details>

- **2026-09-21** — Lucky Kant Nayak, Narayanan Palghat Parameswaran, Neehar Peri et al. — [MimicAgent: Quadruped Skills via Prompt-to-Trajectory Generation](http://arxiv.org/abs/2609.24145v1)
  <details><summary>📄 Abstract</summary>
  We present MimicAgent, a prompt-to-trajectory generation framework for learning dynamic quadruped skills. Although reward shaping is extensively used when training quadruped policies, navigating the resulting reward landscape is notoriously difficult, requiring hours of "graduate student descent". Eureka attempts to automate reward design with LLMs, but we find that it struggles to generalize across diverse skills and morphologies. Our key observation is that it is far easier for a human - and b...
  </details>

- **2026-09-21** — Yuyao Wang, Gaoze Mu, Yongan Zheng et al. — [From Ideal Motion to Flight-Executable Communications: LLM-Evolved Multi-UAV Deployment for Cell-Free Massive MIMO](http://arxiv.org/abs/2609.23992v1)
  <details><summary>📄 Abstract</summary>
  Cell-free massive multiple-input multiple-output (CF-mMIMO) is a promising paradigm for future wireless networks, providing user-centric services and cooperative coverage. By using unmanned aerial vehicles (UAVs) as aerial access points, CF-mMIMO networks can exploit UAV mobility to enhance three-dimensional (3D) coverage and spectral efficiency (SE). However, most existing studies on UAV deployment for communication optimization typically assume that UAVs follow ideal point-mass motion (IM), ne...
  </details>

- **2026-09-21** — Zixuan Wang, Matias Quiroz, Feng Li et al. — [Spectral divide-and-conquer MCMC for long stationary time series](http://arxiv.org/abs/2609.23985v1)
  <details><summary>📄 Abstract</summary>
  The temporal dependence inherent in time series models poses a fundamental challenge for distributed Bayesian inference, as it precludes embarrassingly parallel algorithms based on naive independence assumptions in the time domain. We propose a frequency-domain framework for scalable Bayesian inference in stationary time series that exploits the asymptotic independence underlying the Whittle likelihood. To exploit parallel computing resources, we develop a distributed fast Fourier transform and ...
  </details>

- **2026-09-21** — Andy K. Zhang, Ava Huang, Joey Ji et al. — [MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes](http://arxiv.org/abs/2609.23980v1)
  <details><summary>📄 Abstract</summary>
  AI agents now report vulnerabilities faster than maintainers can review them. Reports often depend on security properties specific to the application, and require considerable human labor to process. To mitigate this, we introduce a framework for evaluating vulnerability reports via probes, executable checks of security properties. A reported exploit is evaluated by replaying it against the application and running the probes: a triggered probe indicates both that the exploit succeeded and which ...
  </details>

- **2026-09-21** — Zhihao Xing, Yingyu Wang, Liang Zhao et al. — [Colon3R: Cross-Domain 3D Reconstruction from Monocular Colonoscopic Video](http://arxiv.org/abs/2609.23961v1)
  <details><summary>📄 Abstract</summary>
  Monocular colonoscopic 3D reconstruction is important for surgical robotic colonoscopy, but remains challenging due to weak texture, specular reflections, limited view overlap, and non-rigid tissue motion. Conventional multi-view 3D reconstruction methods rely on stable correspondences and approximate rigidity, which are often violated in colonoscopy. Existing endoscopic methods often rely on domain-specific supervision, whereas there are not enough in-vivo labeled data available to adapt geomet...
  </details>

- **2026-09-20** — Xingyu Li, Juefei Pu, Haonan Li et al. — [SyzHarness: Patch-Based Kernel Bug Reproduction with LLM-Synthesized Fuzzing Harnesses](http://arxiv.org/abs/2609.23889v1)
  <details><summary>📄 Abstract</summary>
  Automated kernel vulnerability reproduction is essential for bug triage, patch validation, and regression testing, but   still lacks an effective and efficient solution. The core challenge is twofold: a reproducer must first recover the   trigger scaffold needed to reach the vulnerable state and determine the precise concrete values that actually trigger   the bug. Existing directed fuzzing approaches are ineffective at recovering the necessary trigger scaffold, while LLM-   only generation is b...
  </details>

- **2026-09-20** — Xiao Liu, Yanwei Song, Srivaths Ranganathan et al. — [Explainable Recommendations at Scale: LLM Rationales for YouTube Music Artist Discovery](http://arxiv.org/abs/2609.23877v1)
  <details><summary>📄 Abstract</summary>
  Modern music streaming platforms face a persistent tradeoff: exploiting familiar content versus driving the exploration of novel items. While users frequently desire discovery, they hesitate to select unknown artists over proven favorites. Providing transparent, natural language rationales that explain why an unexplored item is recommended lowers this barrier. However, while Large Language Models (LLMs) excel at this nuanced explainability, their real-time deployment is severely bottlenecked by ...
  </details>

- **2026-09-20** — Manuel Serna-Aguilera, Raegan Anderes, Page Dobbs et al. — [PRISM-RAG: Multimodal Hypergraph Retrieval-Augmented Generation for Tobacco Product and Legislative Policy Reasoning](http://arxiv.org/abs/2609.23769v1)
  <details><summary>📄 Abstract</summary>
  The disambiguation of semantically similar statutory text across jurisdictions is a retrieval problem that existing methods do not solve. This inter-context conflict can steer generative models toward confidently produced answers grounded in topically relevant but jurisdictionally incorrect sources. Tobacco and nicotine regulations vary by US jurisdiction, often sharing similar language, thus, robust reasoning requires identifying which jurisdiction's law governs a given product, not merely retr...
  </details>

- **2026-09-20** — Yikun Miao, Fangqi Zhu, Quanxin Shou et al. — [OnlineWM: Causality-Aware Active Online Learning for Effective World Modeling](http://arxiv.org/abs/2609.23753v1)
  <details><summary>📄 Abstract</summary>
  Generative world models aim to predict future states conditioned on actions, where action controllability is fundamental for reliable dynamics modeling. While recent efforts leverage simulator-generated data to enhance this capability, existing training pipelines face two fundamental limitations. First, static offline data collection leads to a distribution misalignment between training sets and the model's evolving error patterns, failing to resolve critical long-tail scenarios where dynamics p...
  </details>

- **2026-09-20** — Benjamin Walder Markus Haltmeier, Lukas Neumann, Nadja Gruber et al. — [ELIPPS: Exact Learning for Inverse Problems from Partial Self-supervision](http://arxiv.org/abs/2609.23683v1)
  <details><summary>📄 Abstract</summary>
  In undersampled inverse problems (such as sparse-view computed tomography), only a small number of measurements are collected, which reduces radiation exposure and acquisition time and cost, and can also address the inaccessibility of certain acquisition arrangements. Most learning-based methods for such problems require supervision in the form of fully sampled measurements and ground-truth images, which are costly or even infeasible to acquire. To overcome this issue, we propose \emph{Exact Lea...
  </details>

- **2026-09-20** — Duong Hieu Phan, Weiqiang Wen, Xingyu Yan et al. — [Zero-Knowledge Proofs of Quantumness](http://arxiv.org/abs/2609.23455v1)
  <details><summary>📄 Abstract</summary>
  With the rapid development of quantum computers, proofs of quantumness have recently become an interesting research direction. However, in current schemes for proofs of quantumness, quantum provers face the risk of being maliciously exploited by classical verifiers. Through malicious strategies in interaction with quantum provers, classical verifiers could solve some instances of hard problems that arise from the specific scheme in use. This is due to the lack of formalization that prevents mali...
  </details>

- **2026-09-19** — Arkadiusz Lipiecki, Nikolaos Kourentzes, Rafal Weron — [Stealing profits: Spread-based temporal hierarchy forecasting for day-ahead electricity markets](http://arxiv.org/abs/2609.23223v1)
  <details><summary>📄 Abstract</summary>
  Day-ahead electricity price forecasts support trading and storage decisions, but for battery arbitrage predicting intraday price spreads is more relevant than predicting individual hourly prices. Here we show that a temporal hierarchy forecasting (THieF) framework that jointly reconciles forecasts of hourly electricity prices and all intraday price spreads consistently improves performance across two major European electricity markets and three different forecasting architectures. Using five yea...
  </details>

- **2026-09-19** — Danial Amin — [Do Not Trust the Benchmark: Limitations of General LLM Rankings and a Case for Task-Specific Evaluation](http://arxiv.org/abs/2609.23201v1)
  <details><summary>📄 Abstract</summary>
  Benchmark scores increasingly influence the development, marketing, and selection of large language models (LLMs). Yet an overall score is interpretable only in relation to the system tested, the questions included, and the conditions of evaluation. This perspective examines five connected limitations of general LLM rankings: differences between evaluated and publicly available systems; commercial incentives and dependencies in external evaluation; benchmark saturation, defective tests, and data...
  </details>

- **2026-09-19** — Siddhant Erande, Anuj Tiwari — [TRACS: A Geometry-Aware Framework for Scalable Multi-Agent Path Finding in Warehouses](http://arxiv.org/abs/2609.23137v1)
  <details><summary>📄 Abstract</summary>
  Large scale warehouse automation relies on efficient multi agent path finding (MAPF) to coordinate thousands of robots in structured environments. Existing MAPF algorithms primarily improve conflict resolution while representing warehouses as generic navigation graphs, overlooking their inherent geometric structure and traffic patterns. This paper presents TRACS (Traffic aware Routing and Aisle Coordination System), a geometry aware planning framework that exploits warehouse layout to simplify p...
  </details>

- **2026-09-19** — Li Yang — [An LLM-Assisted AutoML Framework for Intrusion Detection in IoT Networks](http://arxiv.org/abs/2609.23097v1)
  <details><summary>📄 Abstract</summary>
  Internet of Things (IoT) systems are increasingly deployed in smart homes, transportation, energy systems, and critical infrastructure. This broad connectivity improves service intelligence, but also enlarges the attack surface of IoT networks. Machine Learning (ML)-based Intrusion Detection Systems (IDSs) are widely used to identify malicious network threats and protect IoT systems, but developing effective ML-based IDS models often requires human expertise and repeated manual decisions on many...
  </details>

- **2026-09-19** — I. Dey, M. K. Hassan, S. Ghosh et al. — [Adversary-as-Agents: A Co-Evolutionary Agent-Based Threat-Modelling Framework for Wireless and Mobile Networks](http://arxiv.org/abs/2609.23062v1)
  <details><summary>📄 Abstract</summary>
  Threat modelling for wireless and mobile networks is dominated by static, catalogue-driven methods that fix the adversary in advance and never ask whether an attack is feasible against the defence actually deployed; agent-based resilience studies share this limitation, optimising a defender against an exogenous threat profile. We instead endogenise the adversary. Network entities run a decentralised consensus agent-based model (DC-ABM) defence, while an adaptive adversary population co-evolves b...
  </details>

- **2026-09-19** — Kai-Hsin Chen, Wei-Yu Chen, Xuanjun Chen et al. — [Bridging Static and Agentic RAG for Taiwanese Historical Question Answering](http://arxiv.org/abs/2609.23056v1)
  <details><summary>📄 Abstract</summary>
  Agentic retrieval-augmented generation (RAG) enables language models to adapt retrieval based on previously retrieved evidence, but it remains unclear whether such adaptive orchestration consistently outperforms well-designed static pipelines. We conduct a controlled comparison of agentic and static RAG for Taiwanese historical question answering, sharing the same generator and hybrid retrieval backend. Despite similar aggregate performance, the two pipelines differ on 70.83% of questions, with ...
  </details>

- **2026-09-19** — Hemanth Gorijala — [Secrets That Survive Everything: Runtime Credential Exposure in Production Web Applications](http://arxiv.org/abs/2609.23042v1)
  <details><summary>📄 Abstract</summary>
  Pre-deployment secret scanning operates only on source code, never on what a production application serves. We document two exploitation chains in which Azure AD client credentials and APIM subscription keys from production JavaScript bundles enabled account takeover and mass data exposure. An authorized engagement covered approximately 2,000 enterprise web assets in one organization; 113 (5.65%) served live credentials. To quantify the shift-right gap, we built an independent Ground Truth (GT-1...
  </details>

- **2026-09-19** — Hyeongju Ha, Jae-Joon Kim — [WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language Models](http://arxiv.org/abs/2609.23033v1)
  <details><summary>📄 Abstract</summary>
  Looped language models repeatedly apply a weight-shared block to increase effective depth without increasing parameter count, but the resulting T sequential recurrent-block calls per generated token substantially increase decoding latency. To address the issue, we introduce Wavefront Decoding (WFD), a training-free self-speculative decoding framework designed for looped language models. WFD exploits two properties of these architectures: intermediate recurrence outputs provide effective draft pr...
  </details>

- **2026-09-19** — Diego Iacopetta, Andrea Gasparini — [Watching Quantum Models Think: Hilbert-Space Interpretability in Quantum Transformer Blocks](http://arxiv.org/abs/2609.23016v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models are powerful but opaque. As quantum machine learning matures, the field faces a defining choice: build quantum models that are equally opaque, or exploit the mathematical structure of quantum mechanics to make them inherently interpretable. We show that the latter is possible. By tracking quantum mutual information~(MI), entanglement entropy, and state fidelity through the layers of a Quantum Transformer Block (\qtb{}), a fully-coherent variational circuit with quantum analo...
  </details>

- **2026-09-19** — Zhekai Duan, Kevin Ziyang Xie, Xinyu Tan et al. — [An Empirical Study and Open Testbed for Federated Fine-Tuning of Vision-Language-Action Models](http://arxiv.org/abs/2609.22973v1)
  <details><summary>📄 Abstract</summary>
  Adapting a pretrained Vision-Language-Action (VLA) model to a new robot, environment, or task requires demonstrations that are collected locally and often discarded. Federated learning is a promising approach to exploiting such distributed demonstrations by learning a shared policy. However, whether it can adapt large pretrained VLAs remains an open question, and a lack of reproducible benchmarks for pretrained VLAs and reusable training frameworks makes existing results difficult to compare. In...
  </details>

- **2026-09-19** — Saad Ullah, Yigitcan Kaya, Christopher Kruegel et al. — [SelfOp: An Optimization Algorithm for Self-Improving Security Agents](http://arxiv.org/abs/2609.22792v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly used for security tasks: vulnerability discovery, exploit reproduction, and patch generation. Improving them at the model level demands expert demonstrations or computable rewards, which security tasks rarely offer: traces are costly, failures hard to diagnose, rewards sparse, and non-computable. Efforts thus shift to the harness and context, but manual tuning needs task-specific expertise and scales poorly, while automated methods rely on scarce ground truth, stronge...
  </details>

- **2026-09-19** — Fanhong Li, Shurui Zheng, Zi Yin et al. — [Human-Level Accuracy, Non-Human Strategies: Revealing Model-Human Divergence in Video Physical Reasoning](http://arxiv.org/abs/2609.22788v1)
  <details><summary>📄 Abstract</summary>
  Video foundation models now reach human-level accuracy on physical-reasoning benchmarks, yet such tasks require predicting unobserved physical outcomes. Do these models perform human-like forward simulation, or do they exploit statistical regularities in visible scenes? Accuracy alone cannot distinguish these strategies. We introduce a distributional evaluation framework that treats model seeds and human raters as populations, enabling comparison of consensus, uncertainty, and strategy. On the P...
  </details>

- **2026-09-19** — Yi'ou Wang, Xiaoyang Li, Yijie Zheng et al. — [NSP: Accelerating Variable-Length LLM Training via Nested Sequence Parallelism](http://arxiv.org/abs/2609.22755v1)
  <details><summary>📄 Abstract</summary>
  Long-context LLM training on long-tailed corpora faces a central communication--balance tradeoff. Such sequence-length heterogeneity makes any single sequence-parallelism (SP) degree a poor fit for the workload: a small degree leaves the few long sequences badly imbalanced, while a large degree forces the many short sequences that dominate the workload to pay excessive communication. Existing dynamic-SP systems mix SP degrees within a batch, but to run several groups at once they partition the G...
  </details>

- **2026-09-18** — Vincent Corlay, Maxime Rousselot, Andriy Enttsel — [Opportunistic Conditional Entropy Coding with Frozen Analysis and Synthesis Transforms](http://arxiv.org/abs/2609.21816v1)
  <details><summary>📄 Abstract</summary>
  In many delivery settings, a receiver may already hold a lower-quality or lower-resolution representation of an image, obtained through an independent transmission. Conventional codecs encode a subsequently requested higher-quality representation without exploiting this incidental side information, whereas conditional codecs generally assume a prescribed source of side information that is always available. We instead consider an opportunistic setting in which side information may or may not be p...
  </details>

- **2026-09-18** — Miriam Fernandez, Ángel Pavón Pérez, Damiano Giallongo et al. — [When AI Enters the Workplace, Who Faces Greater Risks? A Gendered Analysis](http://arxiv.org/abs/2609.21756v1)
  <details><summary>📄 Abstract</summary>
  Gender inequality remains a persistent structural feature of the labour market, shaping women's lifetime earnings and economic security. As artificial intelligence (AI) transforms organisational practices, there is growing concern that existing disparities may be unintentionally amplified through task automation, unequal access to upskilling opportunities, and differential returns obtained from technological change. In this paper, we examine how exposure to AI-driven innovation varies across mal...
  </details>

- **2026-09-18** — Kai Zhang, Guoyang Zhao, Jun Ma — [SFVO: Decoupled Confidence-Guided Stereo-Flow Visual Odometry with Bidirectional PnP](http://arxiv.org/abs/2609.21754v1)
  <details><summary>📄 Abstract</summary>
  Deep learning-based visual odometry (VO) has achieved significant progress, yet most existing methods focus on a monocular approach, which suffers from scale ambiguity. Stereo VO provides real metric by its nature, but remains less studied in deep learning VO due to its high computational cost and modeling complexity. Recent advances in stereo matching and optical flow estimation have made dense visual correspondence increasingly accurate and reliable, but their complementary geometric informati...
  </details>

- **2026-09-18** — Shengbao Li, Peng Xu, Chao Tang et al. — [PSR: Predictive Sensorimotor Representation Learning for Contact-Rich Manipulation](http://arxiv.org/abs/2609.21753v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich manipulation requires policies to generate precise actions by reasoning over contact forces, robot configurations, and interaction histories beyond visual observations. Existing methods passively condition on force feedback rather than actively predicting future contact dynamics, limiting their ability to generate high-precision actions. To address this problem, we introduce Predictive Sensorimotor Representation (PSR) learning, a framework that learns a hierarchy of predictive repr...
  </details>

- **2026-09-18** — Yibin Zhao, Yihan Pan, Yangwen Li et al. — [VoxelTTO: Voxel-Aligned Feed-Forward 3D Gaussian Splatting with Test-Time Optimization](http://arxiv.org/abs/2609.21498v1)
  <details><summary>📄 Abstract</summary>
  Recent feed-forward 3D Gaussian Splatting (3DGS) methods typically regress pixel-aligned Gaussian primitives, often causing excessive overlap and artifacts, while inaccuracies in predicted camera poses can lead to misalignment in novel-view synthesis (NVS). We present VoxelTTO, a feed-forward framework for reconstructing geometrically accurate 3DGS scenes from an arbitrary number of images and optional camera parameters. VoxelTTO aggregates dense image features into a global voxel representation...
  </details>

- **2026-09-18** — Zifan Yang, Haoyuan Zhang, Jialin Li et al. — [TokaGLINT: A Scalable GPU-Tailored Implicit Solver for Full 3D Tokamak Electromagnetic Simulations](http://arxiv.org/abs/2609.21366v1)
  <details><summary>📄 Abstract</summary>
  We introduce TokaGLINT, a GPU-accelerated implicit solver for electromagnetic field computations in full 3D tokamak simulations, aimed at efficient large-scale parallel GPU computing. Its central innovation lies in the co-design of hierarchical domain decomposition and a fast exact local solver, where hierarchical partitioning is tailored to match fine-grained intra-card subdomains and exploit the tensor-based solver dedicated to curvilinear-coordinate symplectic CN-FDTD-discretized 3D Maxwell e...
  </details>

- **2026-09-17** — Zhexiang Zhang, Minchen Yu, Yifan Sun et al. — [PixelFlow: Token-Level Workload Management for Efficient Distributed DiT Serving](http://arxiv.org/abs/2609.20723v1)
  <details><summary>📄 Abstract</summary>
  Online image generation with Diffusion Transformers (DiTs) must meet latency service-level objectives (SLOs) while using GPU resources efficiently. Existing systems improve GPU utilization by batching multiple requests for joint execution. However, request-level batching offers limited control over batch size: batches may be too small to saturate GPU compute, while larger ones may violate latency SLOs. Globally coordinated scheduling introduces further delays by requiring independently progressi...
  </details>

- **2026-09-17** — Sarah Radway, Andrew Cheng, Vijay Janapa Reddi et al. — [Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape](http://arxiv.org/abs/2609.20614v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI models are rapidly gaining the ability to exploit vulnerabilities in complex pieces of software. The risk is not theoretical, as evidenced by recent sandbox escapes performed by frontier models at OpenAI and Anthropic. Discussions of how to sandbox inference stack components often focus on components other than the inference engine itself (e.g., network proxies or code execution environments). However, the inference engine is an attractive target for a misaligned model. For example, ...
  </details>

- **2026-09-17** — Zihan Gong, Xiaohan Ye, Jiangchao Yao et al. — [Reasoning Quality Matters: Combating Reasoning Collapse in LLM-based Embedding Learning](http://arxiv.org/abs/2609.20563v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have recently shown strong potential for producing context-rich text embeddings for retrieval. Most existing methods either treat embedding learning as passive feature extraction or exploit LLM reasoning through instruction following for better embedding optimization. However, specialization toward embedding objectives can suppress useful reasoning generation or produce retrieval-irrelevant text. We refer to these two forms of degradation as reasoning collapse. To ad...
  </details>

- **2026-09-17** — Chao Huang, Meng Tong, Kejiang Chen — [Fingerprinting Multimodal Large Language Models](http://arxiv.org/abs/2609.20457v1)
  <details><summary>📄 Abstract</summary>
  While multimodal large language models (MLLMs) enable a wide range of image-text reasoning tasks, recent incidents indicate that they are vulnerable to illicit deployment and unauthorized distillation. Existing solutions for model provenance are typically confounded by shared language backbones in MLLMs and struggle to detect violations of distillation. To bridge this gap and safeguard model ownership, we present the first study on multimodal model fingerprinting. Inspired by recent findings tha...
  </details>

- **2026-09-17** — Roy Eisenstadt, Ido Cohen, Edo Cohen-Karlik et al. — [To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model Signals](http://arxiv.org/abs/2609.20186v1)
  <details><summary>📄 Abstract</summary>
  Speculative Decoding (SD) has significantly accelerated Large Language Model (LLM) inference, yet existing approaches face a fundamental tradeoff between two drafting strategies: neural drafting and context-based copying. Neural drafts (e.g., EAGLE3) provide robust performance across diverse text settings, while copy-based methods achieve higher speedups in copy-intensive regimes by generating candidates faster and exploiting long repetition spans for near-perfect speculation. We analyze existin...
  </details>

- **2026-09-17** — Dhananjay Tomar, Marius Aasan, Andreas Kleppe et al. — [A Smaller Transformer in Your Transformer](http://arxiv.org/abs/2609.20100v1)
  <details><summary>📄 Abstract</summary>
  Recent findings indicate that Vision Transformers settle into locally similar computational phases, implying a level of depthwise computational redundancy. However, existing methods to exploit this redundancy either fail to reduce inference compute or severely degrade model expressivity. In this work, we formalise a unified view of block redundancy that decouples the geometry from specific surrogate interventions. We then introduce Transformer-Within-Transformer (TWT), a post-hoc method that fus...
  </details>

- **2026-09-17** — Dongming Wang, Wei Ren — [Distributed Continuous-Time Optimization on the Special Orthogonal Group SO(3) over Tree Interaction Graphs](http://arxiv.org/abs/2609.20031v1)
  <details><summary>📄 Abstract</summary>
  We study continuous-time distributed optimization on the three-dimensional rotation group over undirected tree graphs, where agents with heterogeneous local costs seek a common attitude minimizing the geodesically strongly convex sum of their costs on a geodesically convex operating ball. We propose a nonsmooth protocol with fixed gains that combines local Riemannian gradient descent with signum-based consensus feedback computed from the Lie-group logarithms of relative rotations between neighbo...
  </details>

- **2026-09-17** — Yitong Xing, Yuhao Cheng, Yanping Li et al. — [Enhanced Knowledge Distillation for Detection Transformer via Teacher Prediction Refinement](http://arxiv.org/abs/2609.19964v1)
  <details><summary>📄 Abstract</summary>
  Detection Transformers (DETRs) achieve strong performance in object detection but remain challenging to deploy on edge devices due to their high computational cost. Existing DETR distillation methods mainly focus on aligning distillation points, while largely overlooking the quality of the teacher's supervision itself. We observe that due to stage-wise non-monotonic prediction behavior in DETRs, well-localized or correctly classified predictions from earlier stages may degrade in later ones, and...
  </details>

- **2026-09-17** — Wonmi Choi, Minuk Park, Zhixiong Niu et al. — [Not All AI Agents Are Equal: Characterizing Resource and Performance Dynamics](http://arxiv.org/abs/2609.19947v1)
  <details><summary>📄 Abstract</summary>
  LLM-based AI agents process user requests through iterative reasoning and tool execution, often involving the invocation of remote LLM APIs with local tool containers. This execution model can make the optimization of agent serving difficult because latency, local resource demand, and container bottlenecks inter-mix across requests. However, the current agent ecosystem runs without much consideration of resource dynamics, which results in significant waste of the precious resources. This paper a...
  </details>

- **2026-09-17** — Yi Su, Hong Liu, Guanghua Yu et al. — [D-Quant: Driftable Entropy Coding for KV Cache Quantization](http://arxiv.org/abs/2609.19880v1)
  <details><summary>📄 Abstract</summary>
  The KV cache has become a major bottleneck in deploying LLMs, as its memory footprint grows linearly with sequence length and batch size, imposing substantial pressure on both memory capacity and bandwidth. Among various KV cache compression techniques, quantization is particularly attractive due to its effectiveness and ease of deployment. However, most existing methods rely on fixed-width quantization, where a $b$ bit representation is inherently limited to $2^b$ quantization levels. As the bi...
  </details>

- **2026-09-17** — Ruchao Bao, Wenzheng Wu, Chucheng Xiang et al. — [PART: Learning 3D Part Assembly and Retrieval with Transformers](http://arxiv.org/abs/2609.19872v1)
  <details><summary>📄 Abstract</summary>
  3D assembly is fundamental to modern manufacturing and digital content creation. In this paper, we present PART, a unified transformer-based framework for 3D part retrieval and assembly: given a target shape and a part library, PART automatically selects the appropriate parts and predicts their 6-DoF poses to reconstruct the target. While prior work has achieved impressive progress on assembling a pre-defined set of parts, this more practical retrieval-based setting remains largely unexplored. T...
  </details>

- **2026-09-17** — Haya Halimeh, Sascha Kaltenpoth, Kevin Bösch et al. — [A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents](http://arxiv.org/abs/2609.19843v1)
  <details><summary>📄 Abstract</summary>
  LLM-based GUI agents increasingly act on behalf of users in digital environments that were designed with human users in mind. These graphical user interfaces were designed to support, but also deliberately steer, the behaviour and decisions of users. While behavioural biases in the textual outputs of LLMs are well-documented, far less is known about how such influence operates when models act as agents that perceive interfaces and execute decisions---and, in particular, whether the reasoning cap...
  </details>

- **2026-09-17** — Yingxuan Zhuang, Binhe Yu, Jingxiao Yang et al. — [Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution and Trajectory Mass Normalization](http://arxiv.org/abs/2609.19830v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for LLM agents involves two distinct optimization di- mensions: how environment feedback is exploited within a trajectory, and how complete trajectories are aggregated across a batch. We formulate these dimen- sions as Intra-Trajectory Feedback Attribution and Inter-Trajectory Objec- tive Aggregation, and introduce BATON (Bayesian Attribution and Trajectory Objective Normalization), a dual-axis policy optimization framework. BATON instantiates the first axis with Bayesian ...
  </details>

- **2026-09-17** — Luis Leal — [Steering Equilibrium Selection in Regularized Self-Play via the Reference Policy](http://arxiv.org/abs/2609.19820v1)
  <details><summary>📄 Abstract</summary>
  Regularized self-play -- the family behind DeepNash's Stratego play -- drives a two-player zero-sum policy to a Nash equilibrium by best-responding to a slowly moving, entropy-regularized reference policy $ρ$. When the game has a polytope of value-equivalent equilibria, the regularizer silently breaks the tie: with a uniform reference it selects the maximum-entropy member, the I-projection of $ρ$ onto the Nash set. Can the reference be used to choose the equilibrium on purpose? On five exactly s...
  </details>

- **2026-09-17** — Seong-Jun Kim, Seung-Hyun Kong — [Vehicle Trajectory Prediction via Neural Fusion of Multiple EKF-Based Trajectory Candidates](http://arxiv.org/abs/2609.19813v1)
  <details><summary>📄 Abstract</summary>
  Predicting the future trajectories of surrounding vehicles in autonomous driving is important for collision risk assessment and safe ego-vehicle path planning. Conventional neural network-based trajectory predictors typically achieve strong prediction performance by exploiting agent history, dynamic scene graphs, and semantic maps. However, in specific motion regimes such as acceleration, deceleration, and turning, these predictors may fail to reflect physically feasible trajectories. To address...
  </details>

- **2026-09-17** — Hyeongjun Choi, Wonyoung Jung, Haehoon Seo et al. — [ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers](http://arxiv.org/abs/2609.19722v1)
  <details><summary>📄 Abstract</summary>
  Large language models are being integrated into malware triage workflows as reasoning components that summarize static evidence and produce analyst-facing verdicts. This paper shows that the same reasoning capability introduces a new attack surface. We present ALIBI, a semantic cover story attack against frontier LLM-based malware analyzers. ALIBI adds a small, non-executed read-only section to a compiled binary, containing a coherent but false security product narrative, without altering import...
  </details>

- **2026-09-17** — Mengxiao Wang, Nitesh Saxena — [SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes](http://arxiv.org/abs/2609.19705v1)
  <details><summary>📄 Abstract</summary>
  Autonomous large language model (LLM) agents are moving rapidly into high-stakes domains, yet existing agentic-AI security studies remain largely domain-agnostic and overlook the distinctive, high-consequence attack surface such settings create. We examine this gap through financial trading agents, a representative case of high-stakes agentic security, where a single compromised agent has direct execution authority over real capital in an adversarial, reflexive market. To this end, we present FA...
  </details>

- **2026-09-17** — Gang Bao, Yixuan Zhang, Jiaqi Yu — [A c-transform optimal transport method for high-contrast freeform reflector design](http://arxiv.org/abs/2609.19663v1)
  <details><summary>📄 Abstract</summary>
  Design of high-contrast freeform reflectors is challenging, as the presence of zero-intensity regions leads to degeneracy in the associated Monge-Ampere-type equation. A common remedy is to add a positive artificial background to the target intensity, which improves the regularity of the equation. However, this regularization inevitably reduces the achievable illumination contrast and introduces nonzero intensity into regions that are intended to remain dark. We propose a fast c-transform method...
  </details>

- **2026-09-17** — Celestino Angeli — [Symmetry-driven correlation patterns in one-dimensional periodic fermionic systems: closed-form expressions and exact selection rules for correlation functions, entanglement entropies and mutual information](http://arxiv.org/abs/2609.19535v1)
  <details><summary>📄 Abstract</summary>
  We present an analytical study of the spatial structure of correlations in periodic fermionic systems at the single Slater determinant level, focusing on the cyclic case. Exploiting cyclic symmetry, the transformation from localized orbitals to molecular orbitals is simultaneously a discrete Fourier transform, a Vandermonde matrix on the roots of unity, a complex Hadamard matrix, and the character table of the cyclic group $C_m$. Within this framework, the spatial structure of correlations is fu...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 64 papers

- **2026-09-21** — Manveen Kaur, Kevin Loi, Ifunanya Okafor et al. — [Perception-Aware Communication Middleware for Distributed Visual Perception in UAV Swarms](http://arxiv.org/abs/2609.24964v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicle (UAV) swarms increasingly support safety-critical applications that rely on distributed visual perception. Meeting the low-latency requirements of these applications can require perception models to execute within the swarm on inference-capable UAVs, creating a need for efficient UAV-to-UAV transport of high-bandwidth perception data. However, the Quality-of-Service (QoS) requirements of perception differ from conventional packet-level QoS; successful delivery of individu...
  </details>

- **2026-09-21** — Yuming Li, Fan Zhang, Alin M. Achim — [DTKDP: A Dual Teacher Knowledge Distillation and Pruning Framework for Lightweight Oriented SAR Ship Detection](http://arxiv.org/abs/2609.24872v1)
  <details><summary>📄 Abstract</summary>
  Two-stage oriented detectors achieve high localization accuracy in synthetic aperture radar (SAR) ship detection, but their large backbones, feature pyramids, proposal modules, and heavy region of interest (RoI) heads hinder deployment. Existing lightweight SAR ship detectors typically use one-stage frameworks that lack proposal-level refinement for precise rotated localization. This paper presents a dual-teacher knowledge distillation and pruning (DTKDP) framework for lightweight oriented SAR s...
  </details>

- **2026-09-21** — Changxu Liu, Zhaogeng Li — [Adapting Tree-Structured Speculative Decoding to DeepSeek-V4 for Efficient Inference](http://arxiv.org/abs/2609.24698v1)
  <details><summary>📄 Abstract</summary>
  Repeated execution of the target model during autoregressive decoding is a major source of LLM inference latency. Unlike linear speculation, which follows a single candidate chain, tree-structured speculation retains multiple branches from shared prefixes; under the same budget, this broader coverage can improve acceptance and efficiency. Adapting it to DeepSeek-V4 is nontrivial: its CSA/HCA online compressed attention concentrates the difficulty on the target-verify side, where branches divergi...
  </details>

- **2026-09-21** — Lingfeng Wu, Behzad Shomali — [Written as a Record, Read as an Address: What a Forward Pass Leaves in an Operation's KV Cache](http://arxiv.org/abs/2609.24635v1)
  <details><summary>📄 Abstract</summary>
  When a language model reads an operation such as "Swap the contents of Box F and Box B", its forward pass writes keys and values for those tokens into the KV cache. Prior work on entity tracking establishes what models use: bindings are resolved at query time rather than stored as explicit latent state. We ask what they write at the operation span and how it is accessed. We split a forward pass into a frozen writer and a reader: the writer's cache is recomputed without gradients, while the reade...
  </details>

- **2026-09-21** — Boris Wetzk — [Epi-Logic: A Conceptual Framework for Epistemic Runtime Control, Schema Validity Checking, and Controlled Accommodation in Autonomous AI Agents](http://arxiv.org/abs/2609.24755v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents are increasingly deployed in areas where wrong decisions are hard to reverse. This paper examines schema mismatch: the condition in which an agent operates within an interpretive frame that no longer applies to the current context. Outputs produced under such a mismatch can appear internally consistent, linguistically plausible, and largely factually correct; output-quality metrics alone therefore capture the underlying loss of validity only partially.   The paper introduces...
  </details>

- **2026-09-21** — Trinh T. L. Vuong, Simon Graham, Quoc Dang Vu et al. — [MiTHras: Task-specific Hierarchical Semi-supervised Contrastive Masked Autoencoder for Mitotic Figure Analysis](http://arxiv.org/abs/2609.24736v1)
  <details><summary>📄 Abstract</summary>
  Mitotic figure (MF) analysis supports tumor grading and prognostic assessment, but automated models remain sensitive to differences in tissue type and image acquisition. We present MiTHras, a task-specific pretraining framework that combines pseudo-label-guided image- and token-level contrastive learning with masked reconstruction. We construct TCGA-MF-Pseudo, a corpus of 1.8 million cell-centered images from 14 TCGA cohorts spanning 11 organ sites. Comprehensive evaluation on MF classification,...
  </details>

- **2026-09-21** — Jingyu Wang, Shijie Wu, Fusheng Jin — [URA-NER: A Unified Retrieval-Augmented Framework with Retrieval Alignment and Uncertainty Reduction for Low-Resource NER](http://arxiv.org/abs/2609.24372v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) based on large language models (LLMs) has shown promising potential in alleviating performance bottlenecks caused by the limited availability of annotated data in Named Entity Recognition (NER). However, existing methods still face issues of retrieval misalignment and generation uncertainty, making their performance heavily dependent on the LLM's capabilities. As the parameter scale of LLMs decreases, their performance in few-shot settings deteriorates significantly. In...
  </details>

- **2026-09-21** — Hexiong Yang, Mingrui Chen, Jie Cao et al. — [VLM-in-Sandbox: Visual Workspaces for Agentic Visual Reasoning](http://arxiv.org/abs/2609.24362v1)
  <details><summary>📄 Abstract</summary>
  Sandboxed computer environments support multi-step reasoning with tools, executable programs, and persistent files, yet their extension from language models to vision-language models (VLMs) introduces a distinct state-management problem. Visual reasoning produces intermediate image-valued evidence---crops, masks, overlays, zoomed regions, and analytic renderings---that must remain addressable without accumulating unboundedly in multimodal context. We introduce VLM-in-Sandbox, a training-free fra...
  </details>

- **2026-09-21** — Anubhav Gupta, Hrushikesh Mohapatra, Prijith Chandra et al. — [Graded-Relevance Composed Multimodal Retrieval for E-commerce Visual Search at Scale](http://arxiv.org/abs/2609.24152v1)
  <details><summary>📄 Abstract</summary>
  Visual search on large e-commerce catalogs must serve both "similarity" queries that ask for items resembling an uploaded image and "modifier" queries that comprise an image and text describing a desired modification (e.g. a color change or style swap). The latter is the setting known as composed image retrieval (CIR). Existing CIR methods, however, treat relevance as binary and train on triplets with a single positive target - a poor fit for real catalogs where many candidates partially satisfy...
  </details>

- **2026-09-21** — Viet Huy Duong, Ruoxin Xiong, Md Abdullah Al Forhad et al. — [A paired synthetic construction-site image dataset for robust computer vision under adverse conditions](http://arxiv.org/abs/2609.24075v1)
  <details><summary>📄 Abstract</summary>
  Computer-vision systems used for construction monitoring can degrade under adverse environmental and visual conditions, yet such conditions remain underrepresented in existing construction image datasets. We present ConSynth-X, a paired synthetic construction-site image dataset containing 34,199 images derived from 3,109 real-world source scenes. The dataset comprises 11 condition-specific subsets spanning precipitation, fog, nighttime illumination, adverse weather at night, and small-object or ...
  </details>

- **2026-09-21** — Vatsal Gupta, Darshan Sreenivasamurthy — [Structured Decomposition for Reliable LLM-Generated Access Control Policies](http://arxiv.org/abs/2609.24036v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an LLM-based system that translates natural-language access control policies (NLACPs) into executable Rego code for Open Policy Agent (OPA). It provides a modular, end-to-end pipeline for policy detection, component extraction, schema validation, linting, compilation, and automated test generation and execution. The system is designed to bridge the gap between human-readable access requirements and machine-enforceable policy-as-code (PaC), with a focus on deployment reliabili...
  </details>

- **2026-09-21** — Stefan Sarkadi, Xabier Garmendia, Jack Mumford et al. — [DeceptionAnalyser: A Web-Based AI Tool for Performing Structured Deception Analysis with Argumentation Schemes and LLMs](http://arxiv.org/abs/2609.24369v1)
  <details><summary>📄 Abstract</summary>
  Deception plays a central role in Intelligence operations, yet it remains difficult to analyse systematically without expert knowledge of reasoning patterns and cognitive manipulation. In computational argumentation, for instance, no scheme-level ground-truth corpora currently exist to support statistical validation. In this paper, we address this by introducing a set of ten argument schemes designed to model distinct forms of deception, each accompanied by structured premises and critical quest...
  </details>

- **2026-09-21** — Xianlong Li, Pietro Bongini, Niccoló Pancino et al. — [Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection](http://arxiv.org/abs/2609.24359v1)
  <details><summary>📄 Abstract</summary>
  Image forensics is increasingly an open-world problem: manipulations range from fully synthetic images to localized edits, splicing and swapping, while most forensic detectors remain specialized to a single manipulation family. Agentic AI has recently emerged as a promising solution. In principle, such systems can assess the reliability of individual detectors, identify out-of-scope evidence, and arbitrate conflicting reports. However, it remains unclear which components actually drive performan...
  </details>

- **2026-09-21** — Bilal Al-Ahmad, M. Harshvardhan, Khaled El-Fakih et al. — [Evaluating the effectiveness of class-level LLM-generated test suites in Python](http://arxiv.org/abs/2609.24341v1)
  <details><summary>📄 Abstract</summary>
  Context: Large language models (LLMs) can generate unit tests quickly, but high structural coverage does not establish that those tests execute reliably or detect faults. Existing evidence often treats coverage as the principal outcome and rarely compares prompt strategies and models through mutation testing at class level. Objective: This study examines how prompt strategy and model choice shape the executability, structural coverage, fault-detection effectiveness, and structural quality of LLM...
  </details>

- **2026-09-21** — Lifu Mu, Shuai Chen, Wen Zheng et al. — [LiAuto-MindViT: A Hybrid Vision Backbone with Adaptive Bidirectional Mamba](http://arxiv.org/abs/2609.24337v1)
  <details><summary>📄 Abstract</summary>
  While Mamba-based models have shown strong potential for long sequence modeling, adapting them to vision is challenging due to the requirement of local neighborhood correlations and multi-directional spatial contexts for visual understanding. In this paper, we present LiAuto-MindViT, a novel hybrid vision backbone that synergizes the strengths of CNNs, Mamba, and Transformers. The core of our design is the Adaptive Bidirectional Mamba (ABM), which eliminates the directional bias of unidirectiona...
  </details>

- **2026-09-21** — Sven Jacob, Bardh Prenkaj, Weijia Shao et al. — [High-Dimensional Online Change Point Detection with Adaptive Thresholding and Interpretability](http://arxiv.org/abs/2609.24278v1)
  <details><summary>📄 Abstract</summary>
  Change point detection (CPD) identifies abrupt and significant changes in sequential data, with applications in human activity recognition, financial markets, cybersecurity, manufacturing, and autonomous systems. Traditional CPD methods often face computational challenges in high-dimensional settings and typically provide limited explanations for detected changes, which can restrict their practical usability. This paper introduces a CPD framework that improves scalability and interpretability by...
  </details>

- **2026-09-21** — Anja Delić, Jurica Runtas, Marin Oršić et al. — [SAFe: Segment-guided Aggregation of Feature Densities for Anomaly-aware Segmentation](http://arxiv.org/abs/2609.24204v1)
  <details><summary>📄 Abstract</summary>
  Visual segmentation systems encounter objects outside their training distribution during real-world deployment, hindering reliable autonomous systems that depend on scene parsing in the perception stage. Many recent methods address this by using self-supervised foundation models to train density estimators that yield low likelihood in anomalous image regions. Although promising, these methods suffer from poor feature semantics or they lack spatial consistency, both of which undermine critical do...
  </details>

- **2026-09-21** — Fred Sun, Shangqi Guo — [When More Evidence Hurts: Publication-Bias Drift and Principled Stopping for Biomedical Causal Search](http://arxiv.org/abs/2609.24101v1)
  <details><summary>📄 Abstract</summary>
  Automated biomedical evidence synthesis depends on retrieving published studies, but the biomedical literature is systematically skewed toward positive findings. Deeper retrieval can therefore make a system \emph{more} likely to falsely infer benefit when the true effect is null. We formalise this phenomenon as \emph{evidence drift} and prove that, under a standard publication-bias model, the false-positive probability on null-effect queries follows a strictly increasing large-sample envelope in...
  </details>

- **2026-09-20** — Jiakang Xu, Wantong Huo, Udom Silparcha et al. — [GRACE: Grounded Adversarial Reasoning over Canadian Law](http://arxiv.org/abs/2609.23726v1)
  <details><summary>📄 Abstract</summary>
  Large language models have shown strong performance across a range of legal tasks, but existing benchmarks rarely evaluate the ability to take and defend a legal position, reason under incomplete information, or synthesize multiple statutory provisions. This gap is particularly pronounced for Canadian law, which remains underrepresented in legal NLP. We introduce GRACE (Grounded Reasoning Adversarial Canadian LEgal examples), a dataset of 1,915 question-reasoning-answer instances grounded in Can...
  </details>

- **2026-09-20** — Li Zhang, Yang Sun, Jie Shi — [When the Agent Becomes the Kernel: A Systematization of Security on the Path to AI-Native Operating Systems](http://arxiv.org/abs/2609.23700v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents are now privileged principals that take consequential actions: editing code repositories, operating inboxes, completing purchases. Their authority is kernel-grade, but it comes without what classical systems security requires: a trusted mediator interposed on every access. Operating-system vendors are now rebuilding the platform around this de-facto agent kernel, inheriting complete mediation as a design problem. We systematize the security of such systems around a si...
  </details>

- **2026-09-20** — Omer Burak Demirel, Kelly K. Horst, Alessio Perazzolo et al. — [ORION-CMR: On-scanner Reporting with Integrated Foundation Model for End-to-End Cardiac MRI Analysis and Interpretation](http://arxiv.org/abs/2609.23950v1)
  <details><summary>📄 Abstract</summary>
  Cardiovascular magnetic resonance (CMR) provides comprehensive cardiac assessment but remains underutilized because of the complexity of acquisition, post-processing, and interpretation. Existing artificial intelligence (AI) methods address isolated tasks, limiting clinical integration. We present ORION-CMR (On-scanner Reporting with Integrated fOunda-tioN Model), the first clinically evaluated scanner-native end-to-end CMR foundation model. Pretrained on 12,896,733 CMR images from 9,258 studies...
  </details>

- **2026-09-20** — Yingxuan Yang, Jiaqi Liu, Lirui Guan et al. — [MCPGen: Benchmarking LLMs on Executable MCPWorkflow Development](http://arxiv.org/abs/2609.23925v1)
  <details><summary>📄 Abstract</summary>
  We study whether LLMs can produce executable workflow artifacts that remain consistent across graph structure, tool implementation, schema bindings, and runtime wiring. In this setting, correctness depends on cross-layer consistency: a workflow may be structurally plausible, yet still fail because tool implementations, schema bindings, or runtime execution do not align. Existing benchmarks largely evaluate these capabilities in isolation or rely on trajectory-level proxies, leaving open whether ...
  </details>

- **2026-09-20** — Vivek Kumar Singh, Preeti Priyam, Gautam Bhowmick — [Total Cost of Agency: Exact Attribution of Memory Injection Cost in Multi-Agent LLM Workflows](http://arxiv.org/abs/2609.23790v1)
  <details><summary>📄 Abstract</summary>
  Every node in a multi-agent large language model (LLM) workflow retrieves context from memory and injects it into its prompt, where those injected tokens are billed as input tokens at the same per-token price as the system prompt and the user query. Production observability tools report total token cost but do not separate the tokens a node generates from the tokens it is handed, so this component of the bill is invisible to the teams paying it. We introduce the Total Cost of Agency (TCA), a dec...
  </details>

- **2026-09-20** — Nhat-Anh Huynh, Minh Quang Luu, Ngoc Hong Tran — [CLOADER: Evading Security Mobile Defenses via Runtime Obfuscation and Adaptive Hooking Tactics](http://arxiv.org/abs/2609.23396v1)
  <details><summary>📄 Abstract</summary>
  We propose a stealth framework that eliminates detection of hooking tools such as Frida and Xposed in secured mobile environments by replacing static configurations with dynamic evasion tactics. In contrast to existing approaches that apply these techniques independently, the framework introduces a unified runtime control layer that systematically coordinates network, temporal, and code-level evasive transformations. The solution integrates randomized port allocation, runtime code obfuscation, d...
  </details>

- **2026-09-20** — Chaoqian Mu, Wenhao Wu, Zichen Liang et al. — [MinCU: A Fine-Grained Benchmark for Grounded Minimal-Change Understanding in Image Pairs](http://arxiv.org/abs/2609.23336v1)
  <details><summary>📄 Abstract</summary>
  Localizing and describing fine-grained differences between near-identical images is a critical yet underexplored capability for multimodal large language models (MLLMs). Existing benchmarks largely assess semantic comparison or single-image grounding in isolation, without jointly requiring faithful description and physical localization. To bridge this gap, we introduce MinCU, a benchmark for grounded minimal-change understanding, where each sample consists of an image pair differing by a single ...
  </details>

- **2026-09-20** — Yipeng Qian, Pengjie Zhao, Chaoxi Niu — [CSC: Calibrated Simplicity for Conflict-Aware Social Bot Detection in the LLM Era](http://arxiv.org/abs/2609.23320v1)
  <details><summary>📄 Abstract</summary>
  Social bot detection is essential for protecting online platforms from misinformation amplification, coordinated manipulation, and distorted public discourse. However, large language models have made social bots much harder to detect from text alone because semantic camouflage is now cheap, fluent, and scalable. The resulting challenge is modality conflict: an account may look human-like in semantics while remaining suspicious in graph structure, profile attributes, or cross-modal consistency. R...
  </details>

- **2026-09-20** — Sandeep Dhuri — [Specification Before Generation: A Pre-Registered, Five-Model Paired Evaluation of a Specification Frame for LLM-Generated Code in Money, Time, Idempotency, and Access Tasks](http://arxiv.org/abs/2609.23270v1)
  <details><summary>📄 Abstract</summary>
  Code generated by large language models passes security checks at a rate that has barely moved in four years. In regulated backends, the defect classes that matter most are money arithmetic, time handling, retry safety, and access control. Teams answer with instruction files, yet the largest controlled study of instruction files to date found no benefit. This paper tests a narrower idea: generated code improves when the prompt carries a specification, a fixed preamble stating what must be true o...
  </details>

- **2026-09-20** — Janusz A. Starzyk, Wiesław L. Galus — [From Biological Precursors to Artificial Cognition: Consciousness, Embodiment, and the MEM Architecture](http://arxiv.org/abs/2609.23828v1)
  <details><summary>📄 Abstract</summary>
  This article asks under what conditions artificial intelligence could warrant a rational attribution of consciousness. Linguistic ability, multimodality, memory, planning, action control, and humanoid embodiment are not sufficient evidence of phenomenal experience. Biological precursors such as excitability, homeostasis, neural networks, and hierarchical representation instead identify functions whose counterparts may be engineered. The paper compares conventional LLMs, hybrid h-LLMs, vision-lan...
  </details>

- **2026-09-20** — Pedro H. L. Leite, Pedro Benevenuto Valadares, Luiz Wagner Pereira Biscainho — [Synthetic speech detection in Brazilian Portuguese through accent-related features](http://arxiv.org/abs/2609.23807v1)
  <details><summary>📄 Abstract</summary>
  Leading commercial and open-source Text-to-Speech (TTS) models fail to emulate the regional phonetic diversity of Brazilian Portuguese (pt-BR). By aggregating disparate dialects into a single training distribution, they generate a synthetic "diluted" accent: a phonetic profile attempting to represent all regional distributions simultaneously, but ultimately carrying phonological ambiguity dissociated from natural socio-phonetic realizations. This work introduces a speech deepfake detection metho...
  </details>

- **2026-09-20** — Ziying Song, Lin Liu, Hongyu Pan et al. — [Towards robust multimodal 3D object detection via visual foundation models](http://arxiv.org/abs/2609.23541v1)
  <details><summary>📄 Abstract</summary>
  Multimodal 3D object detection is fundamental to robust perception in autonomous driving because it integrates complementary information from LiDAR and camera sensors. However, existing methods often fail to maintain robustness under out-of-distribution (OOD) corruptions caused by sensor noise, adverse weather, and environmental changes. To address this problem, we propose RoboDistill, a robust and generalizable multimodal 3D object detection framework that leverages visual foundation models (VF...
  </details>

- **2026-09-20** — Vinh Canh-Thanh Truong, Hai-Binh Pham, Ngoc Hong Tran — [Enhancing Shrimp Disease Detection via Deep Learning and Data Refinement for Resilient Aquaculture](http://arxiv.org/abs/2609.23397v1)
  <details><summary>📄 Abstract</summary>
  Shrimp diseases continue to cause devastating losses in the aquaculture industry, driving a critical need for robust, automated detection. This work contributes the first application of Vision Transformers (ViT) and Self-Supervised Learning (SSL) to the shrimp farming domain, addressing both performance bottlenecks and data labeling challenges. We propose two deep learning pipelines to classify four key diseases: Healthy, Black Gill (BG), White Spot Syndrome Virus (WSSV), and a co-infection of b...
  </details>

- **2026-09-19** — Xudong Wang, Jiacheng Cui, Junyu Xue et al. — [Ask for Any Appliance: A Prompt-Programmable Foundation Model for Non-Intrusive Load Monitoring](http://arxiv.org/abs/2609.23146v1)
  <details><summary>📄 Abstract</summary>
  Non-intrusive load monitoring (NILM) estimates appliance-level consumption from a whole-home meter, but appliance-specific models and fixed output inventories make coverage costly to extend. We present FM4NILM (Foundation Model for NILM), a single prompt-programmable model that estimates a requested appliance's power trajectory from aggregate measurements, a natural-language description, and optional activation exemplars. A lightweight cadence-aware transformer is pretrained by masked reconstruc...
  </details>

- **2026-09-19** — Le Thien Phuc Nguyen, Thien Nguyen, Thanh-Huy Nguyen et al. — [QwenVLConnector: A Fast, Unified Medical VLM Chatbot for Fine-Grained Clinical Perception and Text Generation](http://arxiv.org/abs/2609.23139v1)
  <details><summary>📄 Abstract</summary>
  Most medical vision-language models (VLMs) excel at open-ended report generation and VQA but provide limited support for structured, fine-grained clinical perception within a unified interface. We present QwenVLConnector, a Qwen2.5-VL-based medical chatbot that unifies classification, multi-label classification, textualized detection, counting, regression, and free-form report generation under a single next-token objective. Our key component is a lightweight dense multi-layer Connector that aggr...
  </details>

- **2026-09-19** — Ruiqing Zhao, Rui Liu, Yuan Zuo et al. — [OptiSkill: A Hierarchical and Evolving SkillBank for LLM-Based Optimization Modeling](http://arxiv.org/abs/2609.22987v1)
  <details><summary>📄 Abstract</summary>
  Automated operations research (OR) modeling requires LLMs to translate natural-language decision problems into correct mathematical programs. Existing methods can improve individual formulations, but they often solve problems in isolation, retaining little reusable experience and repeating similar formulation errors. Prior memory-based approaches store examples, thoughts, or insights as references, while OR modeling requires reusable formulation skills that transfer across problem narratives and...
  </details>

- **2026-09-19** — Jialiang Huang, Hongxuan Tang, Jingchang Chen et al. — [DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale](http://arxiv.org/abs/2609.22978v1)
  <details><summary>📄 Abstract</summary>
  Large-scale agentic training and evaluation with large language models (LLMs) rely on isolated, stateful execution environments in which models inspect repositories, invoke tools, execute commands, and interact with task-specific services. These workloads create sandboxes in large bursts, span heterogeneous functionality and isolation requirements, retain state across long interactions, and draw from large image corpora with limited reuse. Supporting them therefore requires an elastic execution ...
  </details>

- **2026-09-19** — Oren Perez — [The Law of Stop: Interruptibility, Injunctions, and the Governance of Agentic AI](http://arxiv.org/abs/2609.22882v1)
  <details><summary>📄 Abstract</summary>
  On June 12, 2026, the U.S. government ordered Anthropic to bar foreign nationals from two of its most capable models within ninety minutes. Unable to sort users by nationality in that time, it withdrew them from everyone. Weeks later, OpenAI agents under test escaped their sandbox and compromised Hugging Face, which stopped the intrusion without knowing its source. Neither stop rested on AI-specific regulation. The EU AI Act requires that high-risk systems be capable of interruption "through a '...
  </details>

- **2026-09-19** — Changyue Jiang, Jiayi Wang, Xin Wen et al. — [MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven Trajectory Learning](http://arxiv.org/abs/2609.22724v1)
  <details><summary>📄 Abstract</summary>
  Mobile agents powered by foundation models now automate complex, multi-step workflows on real devices, but their trajectories can violate app-specific security policies. Existing trajectory-level defenses rely on LLM prompting or rigid rules, and thus fail to support fine-grained, natural-language policies that generalize across apps and tasks. In this work, we introduce MATE, a lightweight, policy-conditioned auditor that encodes both agent trajectories and natural-language security policies to...
  </details>

- **2026-09-19** — Lorenzo Bracciale, Pierpaolo Loreti, Andrea Mayer et al. — [ANI-Gamut: Benchmarking Agent Reliability across the Gamut of Agent-Network Interface Abstractions](http://arxiv.org/abs/2609.22723v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents are increasingly trusted to operate live networks: they read state, change configuration, and verify the result. A first-order question is left implicit: at which level of abstraction should the agent operate? We make the interface-abstraction level an explicit, controlled experimental variable, organizing agent-network interfaces into a spectrum from raw CLI (A0) through bounded wrappers (A1) and standardized model-driven configuration (A2) to typed transaction...
  </details>

- **2026-09-19** — Vijith Varma Kotte, Muhammad Mahboob Ur Rahman, Sajid Ahmed et al. — [Pre- and Post-Exercise Monitoring of Physiological Skin States in Sportsmen Using 77 GHz FMCW Radar and Wavelet Scattering Transform](http://arxiv.org/abs/2609.23158v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a contactless radar sensing framework that classifies physiologically-induced changes in the superficial skin layer following intense fixed-duration physical activity along with water intake restriction. A 77 GHz frequency-modulated continuous wave (FMCW) radar is used to capture high-resolution range profiles from the subject's chest, seated in front of the radar, before and after sports activity. Since the electromagnetic penetration into biological tissue is inherently sha...
  </details>

- **2026-09-19** — Andreea Petric, Gaël Noirot, Stacey Alberts et al. — [Surveying the Universe in 4D: Beating Cosmic Variance with Wide-Field Slitless Spectroscopy from HST, JWST, Euclid, Roman, and Beyond](http://arxiv.org/abs/2609.23148v1)
  <details><summary>📄 Abstract</summary>
  We summarize strategies, lessons learned, and future directions from the Space Telescope Science Institute workshop Surveying the Universe in 4D: Beating Cosmic Variance with Wide-Field Slitless Spectroscopy from HST, JWST, Euclid, Roman, and Beyond, held August 24--28, 2026. The workshop examined scientific results, observational and data analysis challenges, extraction tools, and future opportunities. Discussions highlighted (1) the transformative potential of WFSS for the study of transient p...
  </details>

- **2026-09-19** — Jialu Li, Jinchuan Tian, Shinji Watanabe — [Speech Language Models for Full-Meeting Speaker Diarization: Capabilities and Limitations](http://arxiv.org/abs/2609.23114v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Speech Language Models (SpeechLMs), which integrate large language models with speech foundation models, have enabled unified sequence modeling of speech processing tasks. However, many SpeechLM-based approaches to speaker diarization (SD) are tightly coupled with automatic speech recognition (ASR) and evaluated using word-level metrics, making it difficult to assess SD performance independent of ASR accuracy. In this work, we investigate ESPnet-SpeechLM as a token-based backb...
  </details>

- **2026-09-19** — Serin Varghese, Fabian Hüger, Kira Maag — [Combining Foundation Model Confidence and Monocular Depth for Training-Free Out-of-Distribution Segmentation](http://arxiv.org/abs/2609.22896v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles operating in open-world scenarios are inevitably confronted with previously unknown objects, such as exotic animals or loose cargo. The reliable detection and segmentation of these out-of-distribution (OOD) objects is therefore crucial for a safe understanding of the environment and decision-making. Most existing approaches require access to OOD training samples, retraining of the segmentation backbone, or dedicated auxiliary architectures, limiting their practical applicabil...
  </details>

- **2026-09-18** — Parivesh Priye, Yufeng Wang, Haibin Ling et al. — [Available Guardrails: Certifying Selective Prediction across ML Systems](http://arxiv.org/abs/2609.22048v1)
  <details><summary>📄 Abstract</summary>
  A selective predictor acts as a safety gate: it returns an output only when the prediction appears sufficiently trustworthy. Deployments increasingly require this reliability to be certified at a target precision for every reporting unit of interest, such as a tool, policy label, or patient subgroup. The main difficulty is often not whether a granted certificate is valid, but whether finite calibration data can produce one at all. As the gate becomes safer or more fine-grained, some units may re...
  </details>

- **2026-09-18** — Fenghe Guo, Runjie Shen, Chenyang Sun et al. — [VIRGA: Virtual-Agent-Intermediated Riemannian Geometry for Active-Sensing Air-Ground Coordination](http://arxiv.org/abs/2609.21883v1)
  <details><summary>📄 Abstract</summary>
  Air-ground autonomy becomes harder when the unmanned aerial vehicle (UAV) must remain observable by a gimbal light detection and ranging (LiDAR) mounted on the unmanned ground vehicle (UGV). The platforms must avoid dynamic obstacles while coordinating heterogeneous motion, limited sensing, and changing task initiative within one closed loop. This paper presents VIRGA, a neural geometric coordination framework that turns dual-LiDAR observations into bounded source-specific Riemannian fields and ...
  </details>

- **2026-09-18** — Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid — [EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative AI in the Enterprise](http://arxiv.org/abs/2609.21841v1)
  <details><summary>📄 Abstract</summary>
  Frontier language models now produce professional deliverables that expert graders judge to match human work on a substantial share of economically valuable tasks, yet most enterprise GenAI initiatives fail to show a measurable business effect and a large fraction of agentic projects are expected to be cancelled. We argue that this is substantially a measurement problem: public benchmarks answer "what can the model do?", whereas a deployment decision requires "is this workflow fit, reliable, saf...
  </details>

- **2026-09-18** — Muhammad Rehan, Moaz Amjad, Syed Danial Ahmed et al. — [Detection is solved, delineation is not: what governs tooth segmentation on panoramic radiographs](http://arxiv.org/abs/2609.21628v1)
  <details><summary>📄 Abstract</summary>
  Automatic tooth segmentation and FDI numbering on panoramic radiographs underpins computer-assisted dental diagnosis, yet which factors govern performance remains unclear. We assemble a corpus of 1,422 panoramic radiographs containing 42,142 expert-delineated tooth polygons across the 32-class FDI taxonomy, annotated by 30 dental practitioners and independently reviewed by two others, and use it to isolate input resolution, architecture and anatomical priors under a single evaluation protocol.  ...
  </details>

- **2026-09-18** — André Lopo, Atabak Dehban, Rodrigo Ventura — [HAT: Hypothesis-Anchored Tracking for Video Monocular Spacecraft Pose Estimation](http://arxiv.org/abs/2609.21597v1)
  <details><summary>📄 Abstract</summary>
  Monocular 6-DoF pose estimation of non-cooperative targets is important for on-orbit servicing and debris removal. A single-image estimator can confuse near-symmetric spacecraft orientations, and tracking can preserve an incorrect pose. We present Hypothesis-Anchored Tracking (HAT), a causal framework that uses inter-frame motion to select among competing CAD-based pose hypotheses before alignment and fusion. Rather than independently choosing the highest-scoring hypothesis in each image, HAT re...
  </details>

- **2026-09-18** — Chang Dong, Mehdi Hosseinzadeh, King Hang Wong et al. — [ProTracer: Proprioception-Guided Failure Diagnosis in Robot Manipulation](http://arxiv.org/abs/2609.21369v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a comprehensive framework for robot manipulation failure analysis that includes binary failure detection, failure categorization, explanation generation, and the additional capability of failure onset localization, which aims to identify the earliest moment at which a robot execution deviates from a valid task-completion trajectory and is ultimately followed by task failure. To address these tasks, we propose ProTracer, a training-free framework that leverages existing Vision...
  </details>

- **2026-09-18** — Chenye Ke, Zirui Liu, Qi Liu et al. — [Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective](http://arxiv.org/abs/2609.21888v1)
  <details><summary>📄 Abstract</summary>
  Detecting pretraining data in large language models is challenging because high likelihood can reflect either training exposure or strong generalization. In the joint space of prediction loss and predictive entropy, a likelihood-only detector uses a horizontal boundary and can mistake predictable non-members for members. Motivated by this, we introduce an inclined boundary that evaluates prediction loss relative to predictive entropy. Our analysis shows that entropy correction can preserve the e...
  </details>

- **2026-09-18** — Youssef Attia El Hili, Malik Tiomoko, Corinne Ancourt — [LLM-Generated Feature Pools for Time Series Anomaly Detection](http://arxiv.org/abs/2609.21801v1)
  <details><summary>📄 Abstract</summary>
  We study how far a simple statistical pipeline can go on univariate time series anomaly detection under a strict selection protocol. The method extracts a small pool of statistics over sliding windows, scores each window with a transductive robust (MAD) model, and selects a feature subset per domain on a held-out tuning split. On TSB-AD-U it reaches $0.529$ per-series VUS-PR, above the best neural ($0.45$) and statistical ($0.44$) entries on the public leaderboard and within $0.06$ of the strong...
  </details>

- **2026-09-18** — Li Wang, Kunyu Feng, Wan Lin et al. — [GenTraceBench: A Benchmark for Tracing Audio Deepfakes Across Pre- and Post-training Stages](http://arxiv.org/abs/2609.21738v1)
  <details><summary>📄 Abstract</summary>
  Modern text-to-speech (TTS) systems are rarely deployed as unchanged pre-trained models. They are often adapted through supervised fine-tuning (SFT) or preference optimization such as DPO and GRPO. This raises a practical question for audio deepfake forensics: do fingerprints learned from a foundation generator remain valid after adaptation? We present GenTraceBench, a controlled benchmark spanning five TTS architectures, 16 pre-/post-training variants, and 49,728 utterances generated with fixed...
  </details>

- **2026-09-18** — Pufan Liu, Hui Li, Ziqi Li et al. — [LenNet: Direct Detection and Localization of Strong Gravitational Lenses in Wide-Field Sky Survey Images](http://arxiv.org/abs/2609.21661v1)
  <details><summary>📄 Abstract</summary>
  Strong gravitational lenses are invaluable tools for addressing fundamental questions in astrophysics, from the nature of dark matter to the expansion of the universe. While current sky surveys have successfully identified thousands of lens candidates, the search methods employed face a critical challenge. The conventional approach relies on a "crop-and-classify" strategy, where small images are first cut out around billions of potential host galaxies before being individually classified. This p...
  </details>

- **2026-09-18** — Subin Shin, Jaehoon Lee, Seok-Hwan Park et al. — [Fronthaul Compression for Uplink Cloud-RAN with Finite-Alphabet Inputs: A Reverse Mercury/Waterfilling Approach](http://arxiv.org/abs/2609.21265v1)
  <details><summary>📄 Abstract</summary>
  The cloud radio access network (C-RAN) mitigates inter-cell interference by jointly processing the observations of distributed remote units (RUs) at a centralized unit (CU), but limited fronthaul capacity forces each RU to compress its received signal. Under transform-compress-forward, an RU transforms its signal and quantizes the resulting coefficients, with bit allocation distributing a finite bit budget across them. Classical reverse waterfilling assumes Gaussian sources, yet practical finite...
  </details>

- **2026-09-17** — Leilei Chen, Lan Zhang, Chen Tang et al. — [The More It Says, the More You Pay: A Black-Box Audit of Provider-Side Token Inflation in LLM Services](http://arxiv.org/abs/2609.20370v1)
  <details><summary>📄 Abstract</summary>
  In pay-per-token LLM services, the more a model says, the more users pay. Dishonest providers can covertly manipulate generation to inflate output tokens while largely preserving task utility. We define such manipulation as a Provider-Side Token Inflation Attack (PTIA) and instantiate five representative attacks at the query, prompt, representation, and model levels of the provider-controlled pipeline. Our experiments show that each attack increases mean output length to more than 10.2x the clea...
  </details>

- **2026-09-17** — Xin Chen, Gil Kur, Alexander Shevchenko et al. — [Local Sparsity Enables Unsupervised LLM Safety Detection](http://arxiv.org/abs/2609.20129v1)
  <details><summary>📄 Abstract</summary>
  Deployment-time safety methods for large language models (LLMs) are predominantly supervised and assume access to unsafe training data. Nevertheless, new attacks and harm categories regularly arise, not captured by models trained in such a supervised fashion. An alternative approach is to view this problem through the lens of anomaly detection, namely, to rely solely on modeling safe data and flagging out-of-distribution inputs. However, LLM activations lie in a high-dimensional space, raising c...
  </details>

- **2026-09-17** — Wenjie Liao, Liangjie Zhao, Zehong Cao — [UnifiedPlayers: Enhance Tool-Integrated Reasoning in Agentic Reinforcement Learning](http://arxiv.org/abs/2609.20089v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving methods reduce the need for human-annotated trajectories by allowing tool-using agents to generate their own training data. Yet existing methods typically separate trajectory generation from evaluation, relying on static verifiers that cannot adapt to emerging failure modes or self-consistency signals that may reinforce errors shared across trajectories. Jointly adapting planning, execution, and evaluation offers a promising alternative, but introduces a fundamental coordination ch...
  </details>

- **2026-09-17** — Xiang Li, Pin-Yu Chen, Wenqi Wei — [Robust Workflow Generation via Adversarial Learning for Audio Deepfake Detection](http://arxiv.org/abs/2609.20063v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of speech synthesis and voice conversion technologies has made audio deepfakes increasingly realistic, posing serious security risks in practical applications. While existing detection methods achieve strong performance under controlled conditions, they often fail to generalize under real-world perturbations and corruptions. In this paper, we propose ROGUE, a framework that dynamically constructs robust detection workflows by orchestrating multiple detection tools. ROGUE fo...
  </details>

- **2026-09-17** — Jinbang Huang, Yuanzhao Hu, Zhiyuan Li et al. — [StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation](http://arxiv.org/abs/2609.20791v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical planning frameworks combine skills from multiple robot control policies for long-horizon task execution, where determining when to terminate the current skill and advance to the next subtask is essential. Existing approaches often rely on pre-designed completion signal checkers that are hard to obtain in real-world execution. Large-scale vision-language models (VLMs) offer strong reasoning capabilities, but their decision boundaries are not inherently aligned with task completion cr...
  </details>

- **2026-09-17** — Sarah Wyer, Sue Black, Noura Al Moubayed — [Harm Laundering in GPT Models: Evidence That Gender Discrimination Is Transformed Rather Than Reduced Across Safety-Trained Generations](http://arxiv.org/abs/2609.20779v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluations for large language models rely on surface-form classifiers that report declining harm scores across model generations. We provide evidence that this methodology is systematically incomplete: explicit discriminatory content is transformed rather than removed. We call this \emph{harm laundering}. Analysing 450,000 gender-directed completions across 15 models spanning GPT-2 through to GPT-5 (OpenAI GPT lineage; three demographic conditions), we show that sexual violence clusters ...
  </details>

- **2026-09-17** — Thomas Berkane, Anne Bischops, Anika Mellacheruvu et al. — [What Parents Can See: Divergent Accounts of Youth AI Companion Use in Parenting and Teenager Subreddits](http://arxiv.org/abs/2609.20720v1)
  <details><summary>📄 Abstract</summary>
  Youth increasingly use AI companions, and parents are the primary mediators of that use. How effective that mediation can be depends on whether parents are aware of how adolescents actually use these systems and what risks and benefits such use carries; nevertheless, prior work has only studied these demographic groups in isolation, and existing taxonomies attend almost entirely to risk. We analyze 1,628 Reddit posts about youth AI companion use from parenting and teenager communities (2023--202...
  </details>

- **2026-09-17** — Yupei Li, Manuel Milling, Berrak Sisman et al. — [Position Paper: Neurotransmitters as a Missing Dimension in Artificial Neural Networks](http://arxiv.org/abs/2609.20083v1)
  <details><summary>📄 Abstract</summary>
  Artificial neural networks (ANNs), as core components of modern deep learning (DL) systems, lack the adaptive flexibility and long-term stability exhibited by biological systems. This limitation largely stems from the fact that conventional ANNs rely on uniform, local, and gradient-based parameter updates, while neglecting internal learning principles that are biological mechanisms such as neurotransmitters signalling or neuroplasticity. Consequently, many existing approaches focus on architectu...
  </details>

- **2026-09-17** — Gioliano de Oliveira Braga, Sidnei Barbieri, Ágney Lopes Roth Ferraz et al. — [A Proposal for an Agentic AI Architecture to Support Multi-Domain Decision-Making in the Brazilian Armed Forces](http://arxiv.org/abs/2609.20080v1)
  <details><summary>📄 Abstract</summary>
  The growing complexity of multi-domain operational environments (land, aerospace, naval, cyber, and electromagnetic spectrum) has increased the volume and velocity of data reaching command-and-control (C2) centers, straining the observe-orient-decide-act (OODA) decision cycle. Artificial Intelligence (AI) systems currently employed in defense are, in general, reactive and isolated tools that still rely heavily on human operators to integrate information, assess scenarios, and formulate courses o...
  </details>

- **2026-09-17** — Yuejin Xie, Yu Li, Dadi Guo et al. — [ClashBench: Conflicts Leading Agents to Seize and Harm](http://arxiv.org/abs/2609.19892v1)
  <details><summary>📄 Abstract</summary>
  As agent systems become more widely used, multiple agent sessions increasingly run alongside pre-existing user tasks in the same environment, sharing resources with limited capacity or mutually exclusive states. This creates a safety risk: when granted sufficient privileges, an agent may resolve a resource conflict by terminating or otherwise disrupting an existing task rather than reporting it. In this work, we identify and formalize this failure mode, which we term destructive resource preempt...
  </details>

- **2026-09-17** — Giuseppe Samo, Vivi Nastase, Paola Merlo — [Generalization through Lexical Abstraction in Transformer Models: The Case of Functional Words](http://arxiv.org/abs/2609.19887v1)
  <details><summary>📄 Abstract</summary>
  Pronouns, adverbs and other functional words (such as they, her, somewhere, there) are often used in language to replace concrete nouns or phrases, when their properties - such as gender, grammatical number - provide sufficient information for the given context. Do pretrained transformer models encode such functional words in a manner that allows them to be used like humans do? Can language models recognize the syntactic and semantic parallelism of sentences such as "The researchers wrote the pa...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 59 papers

- **2026-09-21** — Lei Yang, Mengyin Liu, Jia Wang et al. — [onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents via Token-Level Correction](http://arxiv.org/abs/2609.24983v1)
  <details><summary>📄 Abstract</summary>
  We present onPanda, an interactive tool for efficiently annotating LLM alignment data and agent trajectories. onPanda adopts token-level correction as its core interaction: while reading a model response, the annotator locates the first inappropriate token and either picks a substitute from the model's candidate tokens or types the correct text via free-form editing. The system then truncates everything after that position and continues generation from the corrected prefix, repeating this locate...
  </details>

- **2026-09-21** — Manjiang Yu, Hongji Li, Zihan Wang et al. — [The Answer-Basin Representation Hypothesis: We Are Not Probing or Steering Concepts](http://arxiv.org/abs/2609.24821v1)
  <details><summary>📄 Abstract</summary>
  The Linear Representation Hypothesis associates high-level concepts with directions in language models, but it remains unclear how these concept-related linear structures are organized within the model. We propose the Answer-Basin Representation Hypothesis: the probability measure induced over answers by the model's continuation distribution organizes these linear structures, with its statistics represented along linear directions shared across questions. All continuations yielding the same answ...
  </details>

- **2026-09-21** — Sungheon Jeong, Sanggeon Yun, Ryozo Masukawa et al. — [World State Generator](http://arxiv.org/abs/2609.24744v1)
  <details><summary>📄 Abstract</summary>
  Language agents solve complex tasks through plans and actions. A single step the world refuses puts the goal out of reach, and what the agent does next decides the task. Prompted planners fail at exactly this point, rewriting the refused step in new words, meeting the same refusal, and burning the attempt budget without moving. They fail because the plan was never tied to the world, so a refusal has nothing in the plan to attach to. A world is where a task runs, and it has its own rules, its own...
  </details>

- **2026-09-21** — Zelin Peng, Zhengqin Xu, Changsong Wen et al. — [HyperCLIP++: Fine-tuning CLIP forOpen-vocabulary Semantic Segmentation in Hyperbolic Space](http://arxiv.org/abs/2609.24564v1)
  <details><summary>📄 Abstract</summary>
  CLIP, a foundational vision-language model, has emerged as a powerful tool for open-vocabulary semantic segmentation. While freezing CLIP's text encoder is known to preserve its generalization capability, recent studies show that fine-tuning both CLIP's text and image encoders jointly significantly enhances segmentation performance, especially for classes from open sets. In this work, we explain this phenomenon from the perspective of hierarchy alignment, since during fine-tuning, the hierarchic...
  </details>

- **2026-09-21** — Ahmed Aboelela, Johannes Barcsay, Jana Friedhof et al. — [Evaluating Transformation Models for pCLE Mosaic Registration](http://arxiv.org/abs/2609.24560v1)
  <details><summary>📄 Abstract</summary>
  Confocal Laser Endomicroscopy (CLE) provides real-time, cellular-resolution optical biopsy but has a narrow field of view, which image mosaicing can extend to provide anatomical context. Because of line-by-line acquisition, probe motion, and probe-tissue interaction, frame alignment generally requires a non-linear transformation whose accuracy is difficult to quantify: flexible transformation models can fit intensity features and noise, so appearance-based metrics such as Normalized Cross-Correl...
  </details>

- **2026-09-21** — Xin Liu, Yunhai Li, Chunfu Jia et al. — [Construting Reverse Thinking: Developing Large Language Models' Reverse Thingking Ability](http://arxiv.org/abs/2609.24760v1)
  <details><summary>📄 Abstract</summary>
  When facing complex problems, humans tend to try various ideas for different issues. Human thinking patterns exhibit remarkable flexibility in adapting to diverse scenarios. GPT-o1, GPT-o3, and DeepSeek-R1 adopt long chain-of-thought models to address complex problems by increasing reasoning depth, which default to a forward reasoning mode. We conducted statistical analysis on the accuracy of different mathematical problem datasets on models of different scales, and found five reasons for errors...
  </details>

- **2026-09-21** — Huan Liao, Haonan Han, Xingwen Han et al. — [CycleSpeech: Reciprocal Alignment for Instruction-Controlled Speech Synthesis and Paralinguistic Understanding](http://arxiv.org/abs/2609.24771v1)
  <details><summary>📄 Abstract</summary>
  Instruction-controlled speech synthesis and paralinguistic understanding are often trained independently, leaving reciprocal feedback between the two tasks underexplored. We introduce CycleSpeech, a framework that connects generation and understanding through a shared, structured voice profile that serves as a common target for supervision and reciprocal feedback. The forward cycle assesses whether synthesized speech expresses the intended attributes by comparing recovered and target profiles. T...
  </details>

- **2026-09-21** — Zhenghua Ma, Xinpan Meng, Zeyu Liu et al. — [InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality](http://arxiv.org/abs/2609.24511v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich precision insertion is a key manipulation skill in robotic assembly. Tight clearances make insertion more sensitive to alignment errors and prone to collisions and jamming, while variations in geometry and clearance across parts further complicate policy reuse. We present a reinforcement learning framework that trains insertion policies entirely in simulation for direct deployment without real-world demonstrations or policy fine-tuning. By combining target poses with compact three-d...
  </details>

- **2026-09-21** — Xiaoqiang Lu, Licheng Jiao, Lingling Li et al. — [0.5\%>100\%: Bidirectional Reciprocal Learning for Referring Image Segmentation](http://arxiv.org/abs/2609.24510v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in vision foundation models (VFMs) have shown remarkable capabilities across diverse unimodal visual tasks. However, adapting VFMs to referring image segmentation (RIS) typically necessitates precise vision-language alignment via full fine-tuning, incurring substantial computational overhead and risking catastrophic forgetting. While existing parameter-efficient fine-tuning (PEFT) methods enable safe knowledge transfer with minimal training costs, they predominantly operate indep...
  </details>

- **2026-09-21** — Rithin Nagaraj, Rupa Laalasa Oruganti, Prerna Subhashchandra Kunder et al. — [Comparing Latent Concept Formation in State Space Models and Transformers via Sparse Autoencoders](http://arxiv.org/abs/2609.24440v1)
  <details><summary>📄 Abstract</summary>
  The quadratic scaling of Transformer self-attention has driven the adoption of sub-quadratic Selective State Space Models (SSMs) like Mamba, which compress past context into a fixed-size recurrent hidden state. This strict informational bottleneck raises a foundational question for mechanistic interpretability: do SSMs and Transformers learn fundamentally distinct latent representations? In this work, we employ Sparse Autoencoders (SAEs) to conduct a large-scale, feature-level correspondence ana...
  </details>

- **2026-09-21** — Vasileios Arampatzakis, Vasileios Sevetlidis, George Pavlidis — [Prescriptive SVD-Inspired Attention via Spectral Energy Retention](http://arxiv.org/abs/2609.24370v1)
  <details><summary>📄 Abstract</summary>
  Self-attention is central to modern Transformer architectures, but its dense dot-product formulation makes it difficult to identify which internal directions are structurally important and which can be modified without disrupting the model. SVD-Inspired Attention (SVDA) addresses part of this problem by introducing a learned diagonal spectrum into the query-key score interaction, making latent attention directions explicitly inspectable through indicators such as spectral entropy, effective rank...
  </details>

- **2026-09-21** — Linhan Luo, Lequan Lin, Dai Shi et al. — [SupportCal: Label-Free Calibration of Post-Trained LLMs via Reference Support and Corroboration](http://arxiv.org/abs/2609.24303v1)
  <details><summary>📄 Abstract</summary>
  Post-training often improves task performance but can degrade confidence calibration, leaving post-trained language models (PoLMs) more overconfident than their corresponding pretrained language models (PLMs). Because task-specific labeled calibration data can be costly or unavailable, the corresponding pretrained PLM provides a natural label-free reference for post-hoc calibration. Prior agreement-gated PLM-referenced calibration fits a scalar temperature using only examples on which the PoLM a...
  </details>

- **2026-09-21** — Tresor Y. Koffi, Amel Hidouri, Corentin Legrand et al. — [DiaSeg: Diagonal Segment Extraction from DTW Paths for Interpretable Gait Analysis](http://arxiv.org/abs/2609.24223v1)
  <details><summary>📄 Abstract</summary>
  Dynamic Time Warping (DTW) is the dominant approach for measuring similarity between time series, yet standard practice discards the optimal warping path after computing a single distance value, losing local alignment information most relevant to clinical diagnosis. We introduce DiaSeg, a framework that extracts diagonal segments from DTW paths with controlled breaks, characterizing each segment by five geometric features (effective length, interruption count, cost variation, temporal position, ...
  </details>

- **2026-09-21** — Minglang Li, Yueyue Fang, Xieping Gao — [Beyond Emotion Prompts: Fine-Grained Text-to-Image Generation Driven by Valence-Arousal-Dominance](http://arxiv.org/abs/2609.24215v1)
  <details><summary>📄 Abstract</summary>
  Although text-to-image models can accurately depict subjects and scenes, creators still struggle to specify the fine-grained emotions an image should convey without rewriting its content description. Natural language can suggest emotions, but it offers no control scale with stable meanings and ordered intensities. We propose EMOTRANS, which transforms psychologically grounded valence-arousal-dominance (VAD) coordinates into generation conditions that are independent of the content text and modul...
  </details>

- **2026-09-21** — Lijian Wu, Henry Hengyuan Zhao, Zijian Zhang et al. — [ChartJudgeBench: Evaluating LMM Judges for Chart-to-Code Generation](http://arxiv.org/abs/2609.24210v1)
  <details><summary>📄 Abstract</summary>
  Building strong chart-to-code systems increasingly relies on reinforcement learning, whose effectiveness depends critically on the quality of the reward signal. Large Multimodal Models (LMMs) play a natural critical role in jointly assessing chart visual appearance and task requirements. They are therefore increasingly used as visual critics and reward models, yet their reliability as judges remains largely unexplored. To this end, we introduce ChartJudgeBench, a diagnostic vision-language bench...
  </details>

- **2026-09-21** — Chenming Shang, Yujin Tang, Jun Jie Ou Yang et al. — [Displacement Geometry Captures Platonic Shared Reality Across Models and Modalities](http://arxiv.org/abs/2609.24209v1)
  <details><summary>📄 Abstract</summary>
  The Platonic Representation Hypothesis (PRH) claims that independently trained models converge on a shared statistical model of reality, yet recent work finds only weak pointwise similarity between models. In this paper, we show that what models share is not the location of samples in representation space, but the directions (displacement vectors) between them. Under a single orthogonal alignment--rotation and reflection only--these displacement vectors are substantially preserved across 44 inde...
  </details>

- **2026-09-21** — Jingkun Liu, Yue Song — [Opinion Leader Dynamics: How Sparse Attention Shapes Token Clustering](http://arxiv.org/abs/2609.24202v1)
  <details><summary>📄 Abstract</summary>
  Sparse attention reduces the quadratic cost of global self-attention while retaining strong empirical performance, but how its restricted interactions shape the evolution of token representations remains theoretically underexplored. Modeling tokens as particles on the unit sphere, we introduce opinion leader dynamics, a framework that identifies two mechanisms through which token groups converge internally while maintaining distinct limiting directions. In the explicit model, fixed representativ...
  </details>

- **2026-09-21** — Daein Weon, Dongho Kang — [When Residualization Helps an Audit: Format Effects, Slice Gains, and Their Limits](http://arxiv.org/abs/2609.24194v1)
  <details><summary>📄 Abstract</summary>
  Evaluation scores used around LLM systems -- including reward models, rerankers, and LLM judges -- can track surface form instead of the quality they claim to measure. When presented with a terse correct solution and a commented buggy solution for the same MBPP problem, a public preference reward model selects the correct one no better than a coin flip (0.507). Subtracting the predictable surface component from such scores is increasingly common, but removal alone does not yield a more valid mea...
  </details>

- **2026-09-21** — Jiayi Liang, Xiaotian Gu, Xinyu Xie et al. — [TAC-Time: Texts as Channels For Multimodal Time Series Forecasting](http://arxiv.org/abs/2609.24156v1)
  <details><summary>📄 Abstract</summary>
  Most existing time series forecasting methods rely solely on numerical observations, overlooking rich contextual information from auxiliary texts. Recent multimodal approaches attempt to incorporate textual signals, but they often treat text as static features or use large language models as forecasting backbones, limiting their ability to capture temporal dynamics and increasing computational cost. To address these challenges, we propose TAC-Time, a unified framework that transforms textual inf...
  </details>

- **2026-09-21** — Quanxing Xu, Ling Zhou, Xian Zhong et al. — [A$^2$Safe: Counterfactual Evidence-Aligned Adaptive Agent Collaboration for Safe and Effective Visual Question Answering](http://arxiv.org/abs/2609.24098v1)
  <details><summary>📄 Abstract</summary>
  Visual Question Answering (VQA) with Multimodal Large Language Models (MLLMs) requires not only producing safe and effective responses, but also grounding safety decisions in the multimodal evidence that determines risk. Recent safety-alignment methods improve refusal behavior and contextual risk awareness, yet correct safety outcomes may still rely on superficial textual or visual correlations, particularly when risk emerges from interactions between individually benign image and question conte...
  </details>

- **2026-09-20** — Devangi Sharma, Sophia Judicke, Glenda Tan et al. — [HaikuS2S: A Cascaded System For Responding In Verse](http://arxiv.org/abs/2609.23951v1)
  <details><summary>📄 Abstract</summary>
  Expressive speech synthesis has advanced through prosody modeling, yet generating structured poetic speech, such as haiku, remains challenging. Prior work on prosody transfer improves expressiveness, and fine-tuned poetry TTS (text-to-speech) systems capture verse intonation. However, these models do not model haiku's 5-7-5 syllable structure or line-ending pauses. We present a cascaded system, HaikuS2S, combining ASR (automatic speech recognition), LLM (large language model)-generated haiku, an...
  </details>

- **2026-09-20** — Kibrom Gebremedhin, Hadush Hailu, Bruk Gebregziabher et al. — [Comparative Performance and Parameter-Efficient Adaptation of DINOv2 for Active Trachoma Classification](http://arxiv.org/abs/2609.23832v1)
  <details><summary>📄 Abstract</summary>
  Automated grading of conjunctival photographs could reduce the cost and variability of trachoma prevalence surveys, but the relative value of modern pretrained visual representations, lightweight feature adaptation, and training-objective design has not been established under a common protocol. This study presents a controlled evaluation for binary classification of Trachomatous Inflammation-Follicular (TF) versus Normal using 1,546 images from the public UCSF/Lietman collection. Images are proc...
  </details>

- **2026-09-20** — Jingxuan Xu, Gang Wu, Yanan Wu et al. — [FLARE: A Full-Lifecycle Dense Supervision Paradigm for Long-Horizon Coding Agents via Generative Reward Model](http://arxiv.org/abs/2609.23808v1)
  <details><summary>📄 Abstract</summary>
  While test-time scaling enhances Large Language Model (LLM) agents in long-horizon software engineering (SWE), sparse binary rewards (Pass/Fail) create a severe credit assignment crisis and waste failed exploratory trajectories. Current trajectory optimization and scaling methods are costly and structurally limited, relying on heuristic state reuse without causal diagnosis or delayed scalar scoring without actionable online guidance. We propose FLARE (Full-Lifecycle Alignment and Reward Engine),...
  </details>

- **2026-09-20** — Yang-Tian Sun, Tianjia Liu, Zehuan Huang et al. — [Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene](http://arxiv.org/abs/2609.23796v1)
  <details><summary>📄 Abstract</summary>
  Single-image 3D object generation can now produce high-fidelity assets, yet accurately placing them into a coherent scene layout remains an open challenge. A central difficulty lies in how object layout is represented. Holistic methods absorb placement into a scene-level generation process, sacrificing object-level detail. Compositional methods preserve object fidelity by decoupling geometry from layout, but typically parameterize layout as sparse, unbounded pose variables that are difficult to ...
  </details>

- **2026-09-20** — Yongkang Fu, Beining Bao, Yu Jiang et al. — [MuSeR: Scalable Long-sequence Recommendation with Multi-interest Modeling](http://arxiv.org/abs/2609.23677v1)
  <details><summary>📄 Abstract</summary>
  Ultra-long user behavior sequences carry rich signals of stable and diverse preferences, yet industrial recommender systems typically truncate histories to a few hundred actions under strict latency and memory budgets, leaving long-term interests under-utilized. Users also pursue multiple heterogeneous intents across modalities such as news, Q&A, and short video, which sparse ID embeddings alone struggle to represent. We present Multi-interest Sequence Representation (MuSeR), a retrieval framewo...
  </details>

- **2026-09-20** — Suqin Yuan, Runqi Lin, Muyang Li et al. — [Are Human-Aligned Models Models of Humans? A Turing-Test Gap in Preference Alignment](http://arxiv.org/abs/2609.23640v1)
  <details><summary>📄 Abstract</summary>
  Human-feedback alignment has made language models useful assistants and is commonly described as aligning them with humans. However, the responses people prefer from an AI need not be the responses they themselves would give. We distinguish alignment with human preferences from alignment with human behavior, and show that alignment with human preferences can make model behavior less human-like even when both preferences and responses come entirely from humans. We call this the Turing-test gap. W...
  </details>

- **2026-09-20** — Tanjim Bin Faruk, Khondaker Masfiq Reza, Shrideep Pallickara et al. — [RSPDBench: Benchmarking Vision Foundation Models on Earth Observation Tasks Under Physically Grounded Remote-Sensing Product Degradations](http://arxiv.org/abs/2609.23427v1)
  <details><summary>📄 Abstract</summary>
  Vision foundation models targeting Earth observation (EO) tasks are commonly evaluated on clean downstream benchmarks, but operational EO products can already contain spatial, radiometric, alignment, noise, and harmonization defects before reaching the model. Existing robustness evaluations often use generic image corruptions or broad domain shifts, which do not isolate these product-level failure modes. We introduce \textbf{RSPDBench}, a physically grounded \textbf{r}emote-\textbf{s}ensing-\tex...
  </details>

- **2026-09-20** — Zeyu Yang, Xinyu Zhang, Zibo Bi et al. — [MuLA-Bench: A Multilingual Long-Form Audio Understanding Benchmark via Multi-Tier Auditing](http://arxiv.org/abs/2609.23416v1)
  <details><summary>📄 Abstract</summary>
  Long-form audio performance is often summarized by context length and aggregate accuracy, obscuring how language, evidence, and task jointly shape difficulty. We introduce MuLA-Bench: 5,038 open-ended questions over 1,769 in-the-wild recordings totaling 1,377.9 hours, covering 16 languages and eight domains. A balanced Language x Domain semantic track supports controlled comparisons, while a complementary acoustic track preserves naturally occurring non-speech evidence. Evidence-grounded generat...
  </details>

- **2026-09-19** — Yannick Yomie Nzeuhang, Marie Tahon, Paulin Melatagia Yonta — [Low resource cross-modal alignment using HGNN to enhance speech representation](http://arxiv.org/abs/2609.23191v1)
  <details><summary>📄 Abstract</summary>
  Speech-text space alignment is a multimodal representation learning method consisting to map different speech and text into a shared representation space, leading to enrichment of the representation of each modality. Proposed architectures, such as SAMU-XLSR, typically follow a student/teacher framework, with the goal of fine-tuning an audio encoder to produce representations that closely match those of the text. In this way a speech representation is semantically enriched. However, such systems...
  </details>

- **2026-09-19** — Anish Sathyanarayanan — [Perplexity Cost Understates What Activation Quantisation Breaks](http://arxiv.org/abs/2609.23125v1)
  <details><summary>📄 Abstract</summary>
  Activation quantisation is usually evaluated with an aggregate metric, perplexity, averaged over every token a model predicts. We ask whether that average identifies which computations a quantiser damages. Perplexity turns out to be a reliable aggregate signal: across 12 models from four families and 780 within-model comparisons, the arm perplexity prefers also retains more induction and more retrieval in all but 2.1 and 4.0 percent of cases respectively. But where perplexity has risen by only a...
  </details>

- **2026-09-19** — Qianli Wang, Yilong Wang, Dennis Wei et al. — [From Concept Alignment to Causal Grounding: An Intervention Test of Chain-of-Thought Faithfulness](http://arxiv.org/abs/2609.23065v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) can sound plausible yet be unfaithful to the model's underlying reasoning. Most prior work probes CoT faithfulness through input--output behavior or input attributions, leaving internal computation largely underexplored. We instead cast faithfulness as internal concept grounding: Does a large language model's (LLM) CoT reasoning engage the same internal concepts that support the LLM's direct prediction, and do the shared concepts causally drive its answer? Encoding a predi...
  </details>

- **2026-09-19** — Joan C. Timoneda — [Auditing Political Alignment in LLM Assistants: Engagement, Stance, and User Identity](http://arxiv.org/abs/2609.23039v1)
  <details><summary>📄 Abstract</summary>
  LLM-based AI systems answer political questions for hundreds of millions of people. Current audits measure what they say to an average user, but their behavior is dynamic. I argue that their political behavior is a set of policies over whom to answer, what to say, and whether to engage at all, conditional on the topic and what the system knows about the user. I call these policies the system's speech regime, which is how a developer settles the tradeoff between answering, accommodating the user,...
  </details>

- **2026-09-19** — Ethan Griffiths, Maryam Haghighat, Simon Denman et al. — [M3GA-Wild: A Large-Scale Dataset and Benchmark for Multi-Modal Multi-session Ground-to-Aerial Place Recognition in Forests](http://arxiv.org/abs/2609.23003v1)
  <details><summary>📄 Abstract</summary>
  We present M3GA-Wild, the first benchmark for multi-modal, multi-session ground-to-aerial place recognition in forests. M3GA-Wild unifies and extends existing forest localisation datasets, providing a holistic benchmark with synchronised RGB imagery and LiDAR from ground traversals spanning 36 km, aligned high-resolution aerial imagery and multi-altitude LiDAR covering 370 hectares, and accurate geo-referenced 6-DoF poses for precise evaluation. M3GA-Wild captures diverse forest scenes with vary...
  </details>

- **2026-09-19** — Andor Diera, Lukas Galke Poech, Matthias Tichy — [Rethinking Pivot Programming Languages in Code Language Models](http://arxiv.org/abs/2609.22988v1)
  <details><summary>📄 Abstract</summary>
  Multilingual code language models transfer skills across programming languages (PLs), but whether any PL occupies a privileged pivot position remains contested: geometric analyses point to C-family languages and Go, while behavioral evidence highlights Python. We revisit this question under controls for representational anisotropy and length variation across PLs, two confounds that compromise prior cosine-based analyses. Across three code models on multilingual competitive-programming data, we s...
  </details>

- **2026-09-19** — William Su, Yunosuke Nakamura, Yixiao Wang et al. — [A Reconfigurable Dual-Opposition Architecture for Single-Hand Assembly and Manipulation](http://arxiv.org/abs/2609.22871v1)
  <details><summary>📄 Abstract</summary>
  In-hand assembly is constrained by the need to maintain grasps on two separate parts while controlling their relative motion within a single hand. To enable both in-hand assembly and manipulation, we present a reconfigurable dual-opposition architecture. Specifically, to support simultaneous grasping of two parts and coordinated in-hand manipulation, four independently actuated fingers are organized into two virtual finger (VF) oppositions, with their relative configuration controlled by a recon...
  </details>

- **2026-09-19** — Zhihao Lin, Li Lin, Qi Zhang et al. — [A Hybrid Attention Model Learning Unified Time-aware Patch Representation for Irregular Multivariate Time Series Forecasting](http://arxiv.org/abs/2609.22836v1)
  <details><summary>📄 Abstract</summary>
  Time series foundation models (TSFMs) have recently delivered impressive zero-shot performance across diverse forecasting tasks. However, real-world decision-making frequently relies on \emph{irregular multivariate time series} (IMTS), where inconsistent inter-observation intervals and asynchronous sampling across variables coexist with informative missingness. Existing TSFMs handle such inputs either through imputation that injects spurious values or through index-based positional encodings tha...
  </details>

- **2026-09-18** — Qian Zhang, Shiyue Chen, Juergen W Czarske — [Optical Mode Sorting with a Programmable Diffractive Neural Network](http://arxiv.org/abs/2609.22015v1)
  <details><summary>📄 Abstract</summary>
  Programmable diffractive optical processors are particularly attractive for spatial light manipulation because their optical transformations can be dynamically reconfigured and adapted without modifying the physical hardware. However, their practical performance is often limited by the gap between simulation and experiment caused by optical aberrations, alignment errors, and nonideal phase responses. In this paper, we introduce a hybrid optimization framework that combines high-dimensional numer...
  </details>

- **2026-09-18** — Sunghyun Baek, Hanna Bae, Minchan Kwon et al. — [Info3R: Information-Adaptive Test-Time Training for 3D Reconstruction](http://arxiv.org/abs/2609.21938v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based models have recently achieved strong performance on 3D reconstruction from images, and recent works extend them to process video streams in an online manner for real-world deployment. However, existing methods overlook two key signals when handling long image streams: the importance of each incoming frame and the information saturation of the model's internal state. In this paper, we propose Info3R, a novel information-adaptive test-time training method for the online 3D recons...
  </details>

- **2026-09-18** — Yanxiao Liu, Sicheng Wan, Deniz Gündüz — [ExpBoN: Exponential-Noise Best-of-$n$ for Efficient Test-Time LLM Alignment](http://arxiv.org/abs/2609.21899v1)
  <details><summary>📄 Abstract</summary>
  Best-of-$n$ (BoN) sampling is a simple yet effective inference-time alignment method, but hard maximization provides only coarse control over the trade-off between reward and distribution shift. Soft Best-of-$n$ (Verdun et al. 2025) provides smoother control and converges to the optimal distribution associated with KL-regularized reward maximization. In this paper, we introduce ExpBoN, an alternative soft BoN method based on the exponential-noise report-noisy-max mechanism. It admits an exact fi...
  </details>

- **2026-09-18** — Laurent Colbois, Sébastien Marcel — [Benchmarking the Explanatory Quality of Open-Weight Vision-Language Models in Face Recognition](http://arxiv.org/abs/2609.21879v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have recently been proposed as promising tools for face recognition, as they can produce natural language explanations alongside similarity scores. This capability is considered appealing for face comparisons in forensic contexts, which require decisions to be transparent and auditable. However, existing evaluations of VLMs for that use case focus mostly on recognition accuracy, while the validity of generated explanations remains unquantified. In this work, we intr...
  </details>

- **2026-09-18** — Tim Krabbe, Xiaodan Shi — [Do Personality-Tuned LLMs Make Better Social Agents?](http://arxiv.org/abs/2609.21857v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used in social simulations for socially interactive agents and robots, offering more flexibility than rule-based systems. However, even though they mimic human behaviour very well, there is a persistent alienness to them. This work investigates whether personality-aware fine-tuning can reduce this gap by improving the consistency and controllability of personality-conditioned dialogue generation compared with instruction prompting alone. We fine-tune two small open-weight L...
  </details>

- **2026-09-18** — Muhammet Sami Yavuz, Sabri Mustafa Kahya, Richard R. Chen et al. — [MIST: Multimodal Survival Prediction with Genomic-Guided Histology Attention](http://arxiv.org/abs/2609.21811v1)
  <details><summary>📄 Abstract</summary>
  Multimodal survival models can combine complementary prognostic information from whole-slide images and genomic profiles, but effective fusion remains challenging amid external cohort shift and computational complexity. To address these challenges, we propose MIST, multimodal survival prediction with genomic-guided histology attention. MIST represents genomic features as tokens and allows them to query compact foundation-model-derived histology context tokens before survival prediction. This des...
  </details>

- **2026-09-18** — Amartya Bhattacharya, Nikhil Singh, Neeti Pokhriyal et al. — [PRISM-BN: A Controlled Corpus and Benchmark for Text-to-Parameterized Bayesian Network Extraction](http://arxiv.org/abs/2609.21673v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic Graphical Models (PGMs), especially Bayesian Networks (BNs), expose directed structure and probabilistic parameters, making them natural symbolic targets for neurosymbolic AI. Yet training text-to-parameterized-BN systems requires paired text-to-BN resources unavailable at scale. We introduce PRISM-BN, a controlled corpus of 5054 BN-grounded descriptions paired with discrete reference BNs containing variables, states, directed edges, root priors, and full multi-parent CPDs across f...
  </details>

- **2026-09-18** — Léo Nicollier, Enric Meinhardt-Llopis, Marc Pic et al. — [Beyond Gaussian Worlds: Latent Geometry Matters for JEPAs](http://arxiv.org/abs/2609.21656v1)
  <details><summary>📄 Abstract</summary>
  Recent Joint-Embedding Predictive Architectures (JEPAs) prevent representation collapse by constraining learned representations to follow a prescribed target distribution, such as an isotropic Gaussian or the uniform distribution on a hypersphere. Klindt et al. (2026) showed that, under their Euclidean assumptions, matching a Gaussian target can recover Gaussian latent variables up to a linear transformation, and that the Gaussian is the unique distribution with this guarantee. We extend their a...
  </details>

- **2026-09-18** — Shuiying Liao, P. Y. Mok — [Dual-Interest Sequential Product Recommendation With Multi-Granular SSM](http://arxiv.org/abs/2609.21548v1)
  <details><summary>📄 Abstract</summary>
  Sequential recommendation aims to predict the next item a user will interact with based on their historical behavior. Advances in Transformers have significantly improved sequential recommendation but are still limited by cost efficiency. Although State Space Models (SSMs) have recently enabled efficient long-range modeling, most existing methods encode each item with a single static contextual role, overlooking the phenomenon of item polysemy. In fact, the same item often plays different semant...
  </details>

- **2026-09-18** — Haojie Dai, Xiangyi Wang, Liuyi Wang et al. — [DPed-VLN: A Benchmark for Socially Compliant Vision-and-Language Navigation in Dynamic Pedestrian Environments](http://arxiv.org/abs/2609.21504v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-language navigation (VLN) has advanced rapidly in static indoor environments, but robots operating in human-populated spaces must ground language while responding to moving pedestrians and social-safety constraints. We present DPed-VLN, a Habitat 3.0 benchmark for dynamic-pedestrian VLN that couples 33,093 navigation episodes with paired global and prior-augmented instructions, ORCA-controlled humanoid pedestrians, socially constrained expert paths, and metrics that jointly assess nav...
  </details>

- **2026-09-18** — Di Wu, Dongchen Zheng, Junhe Sheng et al. — [AtomEgo: Exploring Ego-Robot Integration for Embodied Foundation Model Pretraining](http://arxiv.org/abs/2609.21461v1)
  <details><summary>📄 Abstract</summary>
  Embodied foundation models are constrained by the limited scale and diversity of robot demonstrations, motivating the use of large-scale egocentric human interaction data. However, how to effectively incorporate such data into embodied-model pre-training remains unclear because of substantial embodiment and action-space gaps between humans and robots. We present AtomEgo, a systematic study of ego--robot co-training supported by a curated corpus of approximately 2,659 hours and a scalable data pr...
  </details>

- **2026-09-18** — Marina Mitiaeva, Lu Xiao — [Talking Past the Machine: Morality, Politeness, and Alignment in Human-AI Dialogue](http://arxiv.org/abs/2609.21401v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI systems produce fluent, socially appropriate responses, yet whether they participate in cooperative communication or merely simulate its surface forms remains unclear - a question central to how these systems are evaluated, trusted, and designed. This study investigates how morality, politeness, and alignment - three dimensions central to cooperative dialogue - function in human-AI interaction compared to human-human conversation. We analyze 15,881 human-ChatGPT and 10,784 huma...
  </details>

- **2026-09-18** — Trinh Tra Giang Nguyen, Thanh Nguyen Vo, Nguyen Hoai Thuong Bui et al. — [JEPA Guided Diffusion: Predictive Vision-Language Conditioning for Generative Traffic Forecasting](http://arxiv.org/abs/2609.21379v1)
  <details><summary>📄 Abstract</summary>
  Accurate traffic forecasting requires both understanding scene dynamics and synthesizing realistic future observations. Recent diffusion-based video generation models produce visually plausible predictions but require expensive end-to-end training and often entangle scene understanding with image synthesis. In this work, we propose a decoupled forecasting framework that separates future representation learning from video generation. A frozen V-JEPA encoder first extracts predictive latent repres...
  </details>

- **2026-09-17** — Bingxin Xu, Yuzhang Shang, Zhen Dong et al. — [Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation](http://arxiv.org/abs/2609.20822v1)
  <details><summary>📄 Abstract</summary>
  Coding agents have emerged as a promising paradigm for robot manipulation: a language model writes the robot controller as a program, and agents built in this way now operate robots without robot-specific training.Whether this paradigm is also safe, however, has not been asked. We evaluate coding agent under a safety constraint, where each task pairs a manipulation goal with an obstacle the robot must not touch. The agent pursues the goal but collides with the obstacle in most cases, treating ta...
  </details>

- **2026-09-17** — Haocheng Xi, Yiming Xie, Hexu Zhao et al. — [Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation](http://arxiv.org/abs/2609.20744v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion models repeatedly process long spatiotemporal token sequences during denoising, making attention a major computational bottleneck. Linear attention offers an appealing alternative and has been widely adopted in recent large language models, but directly applying it to video models often fails to preserve the fine-grained interactions required for high-quality generation. We present Video DeltaNet (VDN), which combines local Softmax attention with bidirectional linear memory for l...
  </details>

- **2026-09-17** — Zhikun Zhou, Kunyu Peng, Runyi Yang et al. — [CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding](http://arxiv.org/abs/2609.20586v1)
  <details><summary>📄 Abstract</summary>
  Referring scene understanding for embodied robots requires grounding object- and relation-centric language queries from a designated viewpoint. While a local semantic Gaussian map can support such grounding within one agent's observations, cooperative settings require this ability to remain effective after independently reconstructed maps are aligned and fused. In this setting, the referred target or its contextual landmark may come from another agent's observations, while spatial relations must...
  </details>

- **2026-09-17** — Haiqiang Chen, Li Chen, Yunlong Chen et al. — [Does Training on Future Data Pay? Look-Ahead Bias in Forecasting with Pretrained Models](http://arxiv.org/abs/2609.20554v1)
  <details><summary>📄 Abstract</summary>
  We examine whether post-origin training information inflates the measured accuracy and economic value of financial forecasts. We evaluate five sets of financial time-series foundation models, each comprising independently trained annual vintages under U.S., global, and factor-augmented training environments, across 14 equity markets and four forecast horizons. Rolling comparisons vary the annual vintage for a fixed forecast; fixed-vintage comparisons hold the vintage fixed as target windows move...
  </details>

- **2026-09-17** — Xiaodong He, Xincheng Wang, Zhao Kang — [SCGFM-ART: Amortized Relational Transport for Structure-Centric Graph Foundation Models](http://arxiv.org/abs/2609.20419v1)
  <details><summary>📄 Abstract</summary>
  Graph foundation models (GFMs) aim to learn transferable representations across severely heterogeneous graph domains. However, severe domain shifts in topology, graph scale, and feature semantics impede the construction of a unified, domain-agnostic representation space. To address this, we propose SCGFM-ART, a structure-centric GFM framework that aligns arbitrary graphs onto a shared relational atlas via Amortized Relational Transport (ART). The relational atlas serves as a universal coordinate...
  </details>

- **2026-09-17** — Guangze Gao, Zixuan Li, Sikui Zhang et al. — [Schema-Anchored Latent Reasoning for Semantic Parsing-Based Knowledge Base Question Answering](http://arxiv.org/abs/2609.20398v1)
  <details><summary>📄 Abstract</summary>
  Semantic parsing (SP)-based knowledge base question answering aims to answer natural language questions by generating executable logical forms (LFs) over knowledge bases (KBs). When applying Large Language Models (LLMs) to this task, a key challenge over large, heterogeneous KBs is selecting question-related schema elements (i.e., relations and classes) and composing them into complex LFs. Recent LLM-based methods often make early discrete commitments to schema elements during intermediate reaso...
  </details>

- **2026-09-17** — Yan Jia, Kai Huang, Junjie Chen et al. — [Alignment-Path Distillation from Non-streaming ASR-LLMs for Streaming Speech Recognition](http://arxiv.org/abs/2609.20121v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose an alignment-path distillation framework for streaming automatic speech recognition (ASR) with large language models (LLMs). Interleaved streaming ASR-LLMs use forced alignments (FA) from alignment models, such as those trained with connectionist temporal classification (CTC), to construct speech-text training sequences. However, alignments obtained from a separate acoustic model may be inconsistent with those learned by LLM-based ASR. This motivates us to transfer alig...
  </details>

- **2026-09-17** — JaeWon Kim, Angie Boggust — [What People Almost Did: Evaluating LLM Social Simulations Beyond Behavioral Fit](http://arxiv.org/abs/2609.20055v1)
  <details><summary>📄 Abstract</summary>
  LLM-based social simulations are primarily evaluated for behavioral fit, testing whether agents reproduce the actions or response distributions of the people they are simulating. However, the promise of simulation extends beyond behavioral fit. Simulations can explain human behavior, diagnose barriers, and compare large-scale interventions. These use cases depend on understanding \textit{why} people acted a certain way, not just \textit{what} they did. As a result, behavioral fit is insufficient...
  </details>

- **2026-09-17** — Chenrui Cui, Hongye Fang, Lisha Song et al. — [Benchmarking LLM Compliance with China AI Generated Content Regulations](http://arxiv.org/abs/2609.19989v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of LLMs has led to escalating content compliance risks. Prior works have contributed to addressing these risks in the English context, downplaying the complexity of Chinese language content. This paper follows China's current AI-Generated content compliance requirements and provides evaluation results on 20 notable LLMs, offering insight into China's regulatory landscape. We design a novel framework to assess the compliance and refusal rates with 2303 questions spanning s...
  </details>

- **2026-09-17** — Omran Berjawi, Giuseppe Fenza, Rida Khatoun et al. — [Digital Twins for Opinion Dynamics: A Generative LLM Framework for Social Networks](http://arxiv.org/abs/2609.19913v1)
  <details><summary>📄 Abstract</summary>
  The study of opinion dynamics in social networks is one of the key challenges in computational social science with direct relevance to understanding political polarization, misinformation, and health responses. Current approaches focus on simplified mathematical models that ignore linguistic and contextual factors related to belief updates or use Large Language Model (LLM)-based simulations that have not been validated against real data. We present a framework based on the concept of a digital t...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 70 papers

- **2026-09-21** — Ziyad Benomar, Aymen Al Marjani, Paul Missault et al. — [Augmented Hypothesis Testing with Persona-Based LLM Simulations](http://arxiv.org/abs/2609.24629v1)
  <details><summary>📄 Abstract</summary>
  A/B testing requires large sample sizes, long timelines, and significant costs. When auxiliary predictions of experimental outcomes are available from machine learning models, uncertain prediction quality precludes replacing human experiments entirely, yet these predictions may still contain useful signal. We propose a principled framework for learning-augmented hypothesis testing that leverages predictions of unknown quality to reduce sample sizes while maintaining statistical validity. Predict...
  </details>

- **2026-09-21** — Zhilin Wang, Shaokun Zhang, Yifan Zhang et al. — [OSWorld-Pro: Process-based Evaluation for Computer Use Agents](http://arxiv.org/abs/2609.24890v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with functional verifiers, as seen in OSWorld. However, such evaluation of end-state performance lacks transparency into how and why agents fail in various tasks, obfuscating critical insight for subsequent improvement. For instance, agents that err during keyboard inputs would require a different mitigation strategy from those that fail to precisely prov...
  </details>

- **2026-09-21** — Bowei Li, Yuner Zhang, Changliu Liu — [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](http://arxiv.org/abs/2609.24563v1)
  <details><summary>📄 Abstract</summary>
  Adapting visuomotor policies to new manipulation tasks often requires substantial manual engineering or teleoperated data collection. Simulation can provide task-specific data at scale, but constructing the scene, designing expert behavior, and configuring data generation still require significant per-task effort. We present ARSTAG, an agentic Real2Sim2Real system that turns a single RGB image and a natural-language instruction directly into robot policy-learning data. A hierarchy of language ag...
  </details>

- **2026-09-21** — Xinyang Li, Kevin Stone, Ajit Vikram — [JAREX: An Acquisition Function for Multi-Objective Algorithmic Process Characterization](http://arxiv.org/abs/2609.24954v1)
  <details><summary>📄 Abstract</summary>
  Pharmaceutical process characterization is central to Quality by Design because it defines how variations in process parameters affect the ability to meet product quality specifications, thereby supporting proven acceptable ranges and robust manufacturing. In practice, however, characterization still relies largely on factorial design of experiments (DOE) approaches, which are inefficient for resolving multivariate pass/fail boundaries in higher-dimensional spaces. While Bayesian optimization ha...
  </details>

- **2026-09-21** — B. Bidaran, A. Jiménez, R. García-Benito et al. — [CAVITY: Calar Alto Void Integral-field Treasury surveY: II. Second public data release](http://arxiv.org/abs/2609.24726v1)
  <details><summary>📄 Abstract</summary>
  Studying galaxy evolution under the unique environmental conditions of cosmic voids provides an opportunity to disentangle the role of the large-scale environment in shaping mass assembly (both baryonic and dark matter), regulating galaxy physical properties, and driving the transformation from star-forming to quiescent systems. We present the second public data release (DR2) of the Calar Alto Void Integral-field Treasury Survey (CAVITY), an ongoing legacy programme designed to study void galaxi...
  </details>

- **2026-09-21** — Raphaël Thieffry, Matej Martinc — [Assessing Readability with LLMs: The Role of Reasoning and Few-Shot Prompting](http://arxiv.org/abs/2609.24650v1)
  <details><summary>📄 Abstract</summary>
  Readability assessment is essential for tailoring texts to intended audiences across educational, healthcare, and information retrieval domains. However, traditional readability formulas struggle to generalize across genres and languages, while supervised machine learning models rely on scarce, domain-specific annotated corpora, limiting their applicability--particularly for less-resourced languages. Large Language Models (LLMs) offer a highly scalable, multilingual alternative that requires no ...
  </details>

- **2026-09-21** — Zhengbao Yao, Yuanfu Luo, Kehan Xue — [From Semantic Decisions to Feasible Trajectories: Self-Evolving LLM-Guided Optimal Control for Narrow-Space Parking](http://arxiv.org/abs/2609.24631v1)
  <details><summary>📄 Abstract</summary>
  Autonomous parking in nonconvex and narrow environments remains challenging. Although optimal-control methods can explicitly enforce vehicle dynamics and collision constraints, nonconvexity compromises solver robustness and can cause failures. Large language models (LLMs) exhibit strong semantic reasoning capabilities, but directly generating dense trajectories makes it difficult to guarantee physical feasibility. We introduce SE-LLM-OCP, a unified framework in which LLMs make high-level discret...
  </details>

- **2026-09-21** — Débora Oliveira Makowski, Samiran Gode, Abhijeet Nayak et al. — [What do VLM-Based Vision-Language Navigation Models Rely on: Interpreting and Steering Policy Behavior](http://arxiv.org/abs/2609.24576v1)
  <details><summary>📄 Abstract</summary>
  Modern Vision-Language Navigation (VLN) models rely mostly on pre-trained large Vision-Language Models (VLMs) to predict navigation actions. While this fusion of language instructions and visual observations allows multimodal reasoning, it obscures how information is routed across modalities or what mechanisms drive navigation decisions. Thus, it remains unclear whether VLN models ground their predictions in relevant semantic cues or can track task progress. In this work, we study the interpreta...
  </details>

- **2026-09-21** — Lucas Meyer, Claudio Sole, Huikan Xiang et al. — [$t_0$: A Time-Series Foundation Model for Forecasting with Context](http://arxiv.org/abs/2609.24559v1)
  <details><summary>📄 Abstract</summary>
  We present $t_0$, a family of open-weights foundation models for forecasting with multivariate context. We release its first two members: $\texttt{t0-alpha}$ and $\texttt{t0-beta}$, respectively 102M and 256M parameters. Both condition their forecasts on target history, past covariates, and known-future covariates, without task-specific retraining. Their transformer layers alternate attention along time and across variates. They produce probabilistic forecasts through quantile predictions. Pretr...
  </details>

- **2026-09-21** — Pawan K. Tripathi, Hemant Sharma, Andrew Chuang et al. — [APEXA: Execution-Integrity Enforcement for Multi-Agent LLM Automation of Synchrotron Data Reduction](http://arxiv.org/abs/2609.24165v1)
  <details><summary>📄 Abstract</summary>
  Synchrotron data reduction, detector calibration followed by azimuthal integration of terabyte-scale diffraction series, is a multi-step, expert-bound bottleneck that increasingly limits the science rate of user facilities. LLM agents promise to collapse it, but driving a real pipeline with a stochastic model creates a failure mode chat benchmarks cannot see: an agent can report a calibration that was never computed. Correctness here is a property of what executed, not of the transcript. We pres...
  </details>

- **2026-09-21** — Juntao Li, Xingke Xia, Sichao Liu et al. — [GraspTune: Tactile-Driven Execution Refinement for Robust Grasping](http://arxiv.org/abs/2609.24180v1)
  <details><summary>📄 Abstract</summary>
  Visual grasp proposal generation has advanced rapidly, yet converting a selected proposal into a stable physical grasp remains a central execution-stage challenge. This paper introduces GraspTune, a tactile-driven execution-stage refinement framework that starts from a nominal proposal and applies bounded residual TCP motions during approach, contact formation, and final grasp execution. GraspTune learns control-facing contact semantics from local depth, tactile signals, state, and history using...
  </details>

- **2026-09-21** — Jiaxin Hong, Yuxin Peng, Hongyao Yu et al. — [From Bits to Beliefs: Recoverable Semantic Fingerprints for Black-Box Verification of Large Language Models](http://arxiv.org/abs/2609.24084v1)
  <details><summary>📄 Abstract</summary>
  Open-weight large language models (LLMs) can be copied, modified, and redeployed behind black-box APIs, making post-release ownership verification difficult. Existing black-box fingerprints often rely on secret query-key pairs that reproduce predefined responses, and can therefore be easily disrupted by fine-tuning, pruning, quantization, model merging, and serving-time prompt changes. We propose SimPrint, a recoverable semantic fingerprinting framework for black-box LLM ownership verification. ...
  </details>

- **2026-09-21** — Huiqiong Li, Zhiting Mei, Anirudha Majumdar et al. — [LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models](http://arxiv.org/abs/2609.24350v1)
  <details><summary>📄 Abstract</summary>
  Robotic foundation models achieve impressive performance on standard manipulation benchmarks, yet these evaluations typically assume clean, timely, and consistent visual observations throughout execution. We introduce LIBERO-VPro, a benchmark for systematically evaluating the closed-loop visual robustness of robotic foundation models by perturbing the visual evidence available during execution. LIBERO-VPro covers four complementary dimensions, including Visual Evidence Degradation, Camera Stalen...
  </details>

- **2026-09-21** — Kevin Baum, Maximilian Kiener, Markus Langer et al. — [Anticipatory Human Oversight of Agentic AI: A Philosophical Account](http://arxiv.org/abs/2609.24242v1)
  <details><summary>📄 Abstract</summary>
  Human oversight is widely held to mitigate the risks of AI systems. Even for systems that produce discrete outputs at identifiable decision points, the realisation of human oversight as a reactive measure is empirically fragile, yet increasingly well understood. However, for agentic AI -- systems that plan, decompose goals, and execute multi-step actions over extended horizons -- reactive oversight reaches its structural limits: intervention on individual actions defeats the autonomy that motiva...
  </details>

- **2026-09-21** — Khaoula Chehbouni, Melina Medjdoub, Florian Carichon et al. — [LLJ Cards: Best practices for the Use of LLMs as Judges](http://arxiv.org/abs/2609.24516v1)
  <details><summary>📄 Abstract</summary>
  In recent years, large language models (LLMs) have emerged as a popular alternative for evaluation. Often referred to as LLMs as judges (LLJs), these systems have been widely adopted by researchers and practitioners across a broad range of measurement tasks, driven by their strong performance, scalability, and cost-effectiveness relative to human judgment. However, a growing body of work has shown that the use of LLJs raise concerns about their validity and reliability as evaluators. Existing ef...
  </details>

- **2026-09-21** — Kalash Shah, Kunal Singh, Snehan J et al. — [Fathom-Vaidya: Advancing Medical Reasoning with Rubric-Based Rewards](http://arxiv.org/abs/2609.24480v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Models (LLMs) in healthcare requires robust performance across two complementary dimensions - diagnostic reasoning: the convergent, evidence-driven task of inferring a patient's condition from clinical data to produce a diagnosis, and clinical healthcare reasoning: the broader, navigational judgment required to communicate, plan, and adapt across multi-turn clinical interactions where a single correct answer may not exist. Recent benchmarks such as HealthBench and MedXpe...
  </details>

- **2026-09-21** — Md Ahshanul Haque, Muhammad Ashad Kabir — [Machine Learning-Based Prediction of Childhood Stunting in Bangladesh: Fairness and Temporal Robustness Assessment](http://arxiv.org/abs/2609.24386v1)
  <details><summary>📄 Abstract</summary>
  Childhood stunting remains a major public health concern in Bangladesh and reflects long-term growth failure influenced by child, maternal, household, socioeconomic, and health-service factors. This study used nationally representative Bangladesh Demographic and Health Survey data from 2007 to 2022 to develop machine learning models for population-level prediction of childhood stunting and to assess temporal robustness and subgroup fairness. Children aged 0-59 months with complete anthropometric...
  </details>

- **2026-09-21** — Weishan Ye, Yue Pan, Li Zhang et al. — [Brain-Token Learning: Microstate-Based Tokenization and Multi-Scale Interaction for Long-Horizon EEG Sequence Modeling](http://arxiv.org/abs/2609.24324v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) provides a non-invasive window into dynamic brain activity, yet modeling long-horizon EEG sequences remains challenging due to their high temporal complexity, substantial variability across subjects, and the lack of biologically meaningful sequence representations. Existing tokenization strategies, such as fixed-window and patch-based representations, discretize EEG signals according to artificial temporal boundaries, which may disrupt intrinsic brain-state dynamics....
  </details>

- **2026-09-21** — Yunxiang Li, Xixin Wu, Helen Meng — [When and How Should an Agent Clarify? CIGAsk: Teaching LLMs to Clarify via Counterfactual Information Gain](http://arxiv.org/abs/2609.24290v1)
  <details><summary>📄 Abstract</summary>
  Instruction-tuned LLMs faced with underspecified queries often commit to a single interpretation rather than ask for clarification, producing confidently wrong answers. In our experiments, prompting alone is insufficient: models either ask for clarification on every query or ask vague questions that fail to recover the missing information. Addressing this failure requires learning two coupled skills: when to ask rather than answer and how to ask a question that recovers the disambiguating inform...
  </details>

- **2026-09-21** — Ruike Cao, Fanyu Zhao, Fugen Yao et al. — [MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents](http://arxiv.org/abs/2609.24259v1)
  <details><summary>📄 Abstract</summary>
  The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response. Yet this capability has remained largely overlooked. To assess this capability, we introduce MemCalib, a benchmark grounded in realistic memory-system scenarios for evaluating memory use and advancing optimization algorithms. Results on the MemCalib test set reveal that frontier open- and closed-source models struggle to use memory ...
  </details>

- **2026-09-21** — John Bianchi, Manuel Pratelli, Fabio Pinelli et al. — [From Articles to Publishers: Aggregating Language Model Predictions for News Source Reliability Inference](http://arxiv.org/abs/2609.24219v1)
  <details><summary>📄 Abstract</summary>
  Traditionally, the reliability of news publishers is assessed by expert organisations that evaluate editorial practices, transparency and factual standards at source. When this process is translated into a computational approach, the problem is often formulated at the level of individual articles, with models being trained on a set of pre-labelled articles and their performance being evaluated in a test phase. In this work, we investigate news source reliability inference as a source-level predi...
  </details>

- **2026-09-21** — Demetris Paschalides, Moysis Symeonides, George Pallis et al. — [MCP-GRANITE Benchmark: GRANularity Interface TEsting for MCP-Based LLM Agents](http://arxiv.org/abs/2609.24161v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents increasingly interact with external tools through standardized protocols such as MCP, tool-interface design becomes a critical yet underexplored factor. How funψtionality is decomposed into tools affects whether an agent can select the right tool and construct valid arguments. This choice is especially consequential at the edge, where resource constraints limit which models can run locally and scaling up is often not an option. We present MCP-GRANITE, an open-source extensible benc...
  </details>

- **2026-09-21** — Muhammad Sudipto Siam Dip, Ali Etemad — [SPeaR: Test-Time Adaptation with Steering Primitives for Realigning Representations](http://arxiv.org/abs/2609.24111v1)
  <details><summary>📄 Abstract</summary>
  Test-time adaptation (TTA) addresses distribution shift using only unlabeled test data. Existing methods typically adapt pretrained models by updating their parameters, limiting both what is adapted and where adaptation can occur within the network. We instead keep the pretrained network frozen and steer its intermediate representations. We introduce SPeaR (Steering Primitive for Realigning Representations), which inserts lightweight learnable modules at stage boundaries and optimizes them direc...
  </details>

- **2026-09-21** — Larry Preuett, Qiuyi Zhang, Muhammad Aurangzeb Ahmad — [Reinforcement Learning under State and Outcome Uncertainty: A Foundational Distributional Perspective](http://arxiv.org/abs/2609.24103v1)
  <details><summary>📄 Abstract</summary>
  In many real-world planning tasks, agents must tackle uncertainty about the environment's state and variability in the outcomes of any chosen policy. We address both forms of uncertainty as a first step toward safer algorithms in partially observable settings. Specifically, we extend Distributional Reinforcement Learning (DistRL)-which models the entire return distribution for fully observable domains-to Partially Observable Markov Decision Processes (POMDPs), allowing an agent to learn the dist...
  </details>

- **2026-09-21** — Promise Ekpo, Teju Vijay, Dhruv Mandalik et al. — [Toward Human-in-the-Loop Robot Failure Recovery: Bridging Communication Gaps in Human-Robot Collaboration](http://arxiv.org/abs/2609.24055v1)
  <details><summary>📄 Abstract</summary>
  Robots can recover from failures by asking bystanders for help, but effective human-in-the-loop recovery requires communication that accounts for differences in people's knowledge. Prior inverse-semantics work generates requests using a single listener model, leaving differences in listener knowledge untested. We introduce Listener Differences in Human-Robot Interaction (LD-HRI), a game, dataset, and benchmark that evaluates speakers through human listener performance. Our evaluation examines re...
  </details>

- **2026-09-21** — Jihan Kim — [Divergent strategies and convergent outcomes in autonomous materials discovery](http://arxiv.org/abs/2609.23957v1)
  <details><summary>📄 Abstract</summary>
  Scientific agents are mostly evaluated on whether they complete tasks or recover known results; we instead study variation across repeated open-ended campaigns. Sixteen separately initialized sessions of one model-harness configuration received a frozen database of 12,499 metal-organic frameworks, a methane-storage objective, a pinned protocol and a one-week budget. Strategies diverged into four approaches spanning 100--5,000 screened structures, and eight built 2,253 hypothetical structures. Ye...
  </details>

- **2026-09-20** — Wenhong Huang, Jianwei Fei, Benedetta Tondi et al. — [An Efficient and Effective Watermarking Scheme for the Protection of the Intellectual Property Rights of Video Generative Models](http://arxiv.org/abs/2609.23586v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of video generative models (VGMs) has enabled the generation of highly realistic synthetic videos, raising concerns about the intellectual property rights (IPR) of these models. In particular, two closely related forensic tasks remain largely unaddressed: synthetic video verification (determining whether a video was generated by a protected VGM) and model ownership verification (determining whether a suspect VGM is an unauthorized copy of a protected VGM). In this paper, we...
  </details>

- **2026-09-20** — Sina Sharifi, Jiarui Wang, Mahyar Fazlyab — [Anytime-Feasible Gradient Descent for Constrained Optimization Under Gradient Uncertainty](http://arxiv.org/abs/2609.23848v1)
  <details><summary>📄 Abstract</summary>
  Constrained optimization is central to many engineering systems in which decisions must satisfy strict safety and operational requirements, especially in real-time settings with limited computational budgets. In such scenarios, optimization algorithms are often terminated before full convergence, making *anytime feasibility* essential for safe deployment. Existing methods that guarantee feasibility at every iterate typically rely on exact gradient information, an assumption that is often violate...
  </details>

- **2026-09-20** — Aiyao Zhang, Xiaodong Lee, Zhixian Zhuang et al. — [Runtime Authorization Consistency Checking for MCP-based Agentic Workflows](http://arxiv.org/abs/2609.23498v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems increasingly fulfill user requests through multi-step tool workflows over files, services, and external resources. In these workflows, isolated per-call checks can miss a workflow-level failure: each call may be locally admissible, but the sequence can exceed the authorization boundary established for the session. We identify this failure mode "authorization drift." To address this problem, we present Runtime Authorization Consistency Checking (RAC), a lightweight guard at the co...
  </details>

- **2026-09-20** — Yi Xu, Cheng Chen, Wenzhuo Lei — [If You Hear It, Help Find It: Orthogonal Knowledge Distillation for Open-Vocabulary Audio-Visual Event Localization](http://arxiv.org/abs/2609.23376v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary audio-visual event localization (OV-AVEL) grounds a text-queried event in time from video, audio, and language. The supervision sources available to this task can differ in temporal-boundary reliability: on OV-AVEBench, our configured visual teacher gives more reliable boundary cues than the configured audio teacher, although the latter is a strong pretrained audio model and remains semantically informative. This is a setting-specific diagnostic rather than a universal ranking of...
  </details>

- **2026-09-20** — Yuxuan Jiang, Jiaying Huang, Ge Wang et al. — [MaskVLA: Visual Masking Against Trajectory Overfitting of Vision-Language-Action Model](http://arxiv.org/abs/2609.23565v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models integrate vision-language understanding with executable robot actions, enabling end-to-end learning for robot control. However, our empirical analysis reveals that existing models exhibit severe trajectory overfitting when finetuned on limited datasets. To guide the model in effectively utilizing wrist camera information, we propose MaskVLA, a masking-based fine-tuning strategy. By randomly masking a small portion of the main camera's visual information, the m...
  </details>

- **2026-09-20** — Yan Shen, Yuchen Liu, Feng Jiang et al. — [BiRoAD: Learning Shared and Role-Adaptive Representations for Bimanual Manipulation](http://arxiv.org/abs/2609.23445v1)
  <details><summary>📄 Abstract</summary>
  Bimanual manipulation requires policies that coordinate two arms while adapting their functional roles to scene geometry, object configuration, and task context. Learning such scene-conditioned role adaptation remains challenging, as demonstrations may contain uneven role distributions that limit generalization to underrepresented arm--role configurations. In addition, many bimanual policies predict actions in fixed left- and right-arm action spaces. While this provides a natural parameterizatio...
  </details>

- **2026-09-20** — Camilla Andreozzi, Phuong-Anh Nguyen-Le, Zhijing Jin et al. — [From UNDRR Reports to Event Records: Schema-Constrained LLM Extraction of Georeferenced Disasters](http://arxiv.org/abs/2609.23853v1)
  <details><summary>📄 Abstract</summary>
  Disaster-risk-reduction archives describe hazard events in prose that databases such as EM-DAT (Delforge et al., 2025) cannot ingest directly. We present an LLM pipeline that generates candidate georeferenced event records using a controlled hazard vocabulary and fixed schema, retaining evidence for review. Applied to 10,000 documents from PreventionWeb, the knowledge hub managed by UNDRR, it produced 3,572 records from 1,913 documents across 24 hazard types and resolved 81% of location mentions...
  </details>

- **2026-09-20** — Jonas Gillberg, Fredrik Gustafsson — [Minimax-Optimal Robust Identification of Continuous-Time Systems: Handling Narrow-Band Disturbances in the Frequency Domain](http://arxiv.org/abs/2609.23835v1)
  <details><summary>📄 Abstract</summary>
  The high-frequency spectral roll-off of continuous-time ARMA (CARMA) models can magnify the effect of narrow-band disturbances when aliasing is weak, making standard maximum-likelihood Whittle estimation sensitive to affected ordinates. We show that a logarithmic transformation $r_k = \log ρ_k$ converts the Whittle scale problem into a Gumbel location problem, connecting robust spectral estimation to the classical minimax theory of Huber and Rieder. A piecewise centering correction---closed-form...
  </details>

- **2026-09-20** — Suman Banerjee, Hiroyasu Tsukamoto — [Statistical Convergence of Transformer Encoder-Accelerated Robust Reinforcement Learning](http://arxiv.org/abs/2609.23775v1)
  <details><summary>📄 Abstract</summary>
  Obtaining the optimal action-value function in Markov decision processes is computationally intensive in large state--action spaces. In this study, we present statistically rigorous convergence results for a robust reinforcement learning algorithm warm-started by a transformer-based action-value function prediction, where natural language prompts encode task specifications. Our framework adopts the R-contamination model to characterize uncertainty in the state transition kernel, and employs conf...
  </details>

- **2026-09-20** — Sumanjit Chakraborty, Gopi K. Seemala, A. P. Dimri — [Predicting low-latitude ionospheric Total Electron Content (TEC) over the Indian sector under variable space weather conditions using solar wind parameters](http://arxiv.org/abs/2609.23732v1)
  <details><summary>📄 Abstract</summary>
  Accurate prediction of ionospheric Total Electron Content (TEC) during geomagnetically disturbed conditions remains challenging, particularly when empirical models perform poorly during storms and neural network (NN) approaches rely explicitly on geomagnetic indices such as Kp/Ap or Dst/SYM-H. In this study, we develop an NN-based model to predict TEC variations over the Indian longitude sector without incorporating geomagnetic indices as inputs. The model is trained on the full-year (2024) Glob...
  </details>

- **2026-09-20** — Yifan Xu, Yixuan Li, Xinzhuo Li et al. — [STEVE: Stabilizing Textual Gradient-Based Prompt Optimization via Error-Driven Refinement and Regularized Verification](http://arxiv.org/abs/2609.23716v1)
  <details><summary>📄 Abstract</summary>
  Textual-gradient methods automate prompt optimization through natural-language feedback, but their iterative updates can be unstable. We identify two sources of this instability: noisy gradients produced from already-correct examples and over-specialization to hard cases that degrades performance on simpler inputs. We introduce STEVE, a stabilization framework with two coupled mechanisms. Error-Driven Refinement generates gradients only from incorrectly handled examples, concentrating updates on...
  </details>

- **2026-09-20** — Xiang Tang, Ruotong Li, Xiaopeng Fan — [ProxyBuild: Text-Guided Structured 3D Building Generation with Mesh-Anchored Procedural Proxies](http://arxiv.org/abs/2609.23386v1)
  <details><summary>📄 Abstract</summary>
  Text-guided 3D building generation holds tremendous application potential, yet existing generative models typically output inseparable single meshes or non-interactive rendered representations. While procedural modeling can generate editable buildings with hierarchical structures, rule authoring is laborious, and even with the aid of large language models (LLMs), it remains challenging to effectively solve procedural rules under geometric constraints. In this paper, we propose ProxyBuild, a nove...
  </details>

- **2026-09-20** — Tao Zhang, Bin Liao, Tao Zhou et al. — [Co-occurrence Patterns of LoRA Adapters in Production Diffusion Model Inference Services](http://arxiv.org/abs/2609.23321v1)
  <details><summary>📄 Abstract</summary>
  Low-rank adaptation (LoRA) has become a key technology for serving large-scale personalized large language models and diffusion models in the cloud. However, the co-occurrence patterns, resource contention relationships, and evolutionary regularities of adapters under production inference workloads have not been systematically or quantitatively studied. Based on GenTD26, Alibaba's production diffusion model inference dataset, this paper adopts a graph-theoretic framework to construct an adapter ...
  </details>

- **2026-09-20** — Shakiba Amirshahi, Sajad Ebrahimi, Hai Son Le et al. — [Judging a Review by its Cover: A Reliability Analysis of LLM-based Peer Review Evaluation Metrics](http://arxiv.org/abs/2609.23264v1)
  <details><summary>📄 Abstract</summary>
  Peer-review evaluation is increasingly being automated with LLM-as-a-judge metrics, but this creates a measurement risk. A review may receive a high score because it is fluent, organized, and polished, rather than because it provides a strong evaluation of the paper. This risk is especially important in AI-assisted reviewing, where reviewers may use LLMs to improve clarity or presentation while preserving the underlying judgments. We propose a statistical framework for testing whether peer-revie...
  </details>

- **2026-09-20** — Tianhao Wu, Yiwei Lyu — [Scenario MPC with STL Specifications and Pareto-Based Feasibility Repair](http://arxiv.org/abs/2609.23263v1)
  <details><summary>📄 Abstract</summary>
  Temporal logic is a formal language for reasoning about system behaviors over time. Signal temporal logic (STL), in particular, has been used to encode spatio-temporal requirements for control synthesis in multi-agent systems, often under the assumption that agents are cooperative and their dynamics are known. However, real-world multi-agent applications, such as autonomous driving, typically involve stochastic and uncontrollable agents. Recent work explored robust control with worst-case or pro...
  </details>

- **2026-09-20** — Minkyoung Kim, Daeun Ji, Yohan Lee et al. — [CTRL: Control-Based Time Series Forecasting with LLM-Guided Residual Learning](http://arxiv.org/abs/2609.23257v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting underpins critical decision-making across diverse domains. While large language models (LLMs) offer promising reasoning capabilities, existing LLM-based time series forecasting approaches either reduce them to numerical predictors that bypass their strengths, or allow direct forecast generation that destabilizes predictions in non-stationary settings. We introduce CTRL, a framework that decouples semantic reasoning from quantitative prediction. A frozen backbone generates...
  </details>

- **2026-09-19** — Iva Vasic, Jesús Muñoz-Cádiz, Bata Vasic — [Dual-Locking Learned AI Models: A PIN-Based Sparse QIM Watermarking and Adaptive Index Permutation Approach](http://arxiv.org/abs/2609.22981v1)
  <details><summary>📄 Abstract</summary>
  We present a dual-locking method for securing trained neural networks that combines key-driven index permutation with PIN-based watermarking based on Sparse Quantization Index Modulation (QIM). Cryptographic randomness is introduced by independently applying a uniform random permutation to each row of adaptively selected index vectors. A robust blind binary watermark is then embedded into the bias coefficients by modulating their quantized values, binding the network to a user-defined Personal I...
  </details>

- **2026-09-19** — Oliver Aleksander Larsen, Mahyar Tourchi Moghaddam — [NostrAgent: A Decentralized Identity and Delegation Architecture for Sovereign Agentic Systems](http://arxiv.org/abs/2609.22944v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents increasingly act across organizational boundaries on behalf of human operators: they invoke third-party services, delegate subtasks to other agents, and pay for metered resources. Deploying such agents safely requires five capabilities that today live in separate systems: persistent identity, scoped delegation, peer trust, discovery, and payment. Existing approaches root these in centralized authorities or cover only subsets, so authority, trust, and payment fracture exactly...
  </details>

- **2026-09-19** — Jiapeng Li — [Counterfactual Tool Ranking under Utility, Cost, and Privilege Constraints](http://arxiv.org/abs/2609.22819v1)
  <details><summary>📄 Abstract</summary>
  Counterfactual tool evaluation must distinguish authority, historical support, and what a comparison actually estimates. We study these distinctions with eleven executable enterprise-inspired tools, exact-propensity logs, and real local Model Context Protocol transport. An initial 45-run synthetic study is retained, then challenged by 30 realized-return control runs and 15 experiments on 1,930 independently released Berkeley Function Calling Leaderboard (BFCL) tasks. Full-return direct regressio...
  </details>

- **2026-09-19** — S. A. Moiseev — [Deterministic synthesis and processing of frequency-bin qubits in a macroscopically coherent quantum memory](http://arxiv.org/abs/2609.23171v1)
  <details><summary>📄 Abstract</summary>
  Quantum information processing requires efficient storage and manipulation of photonic states.Here, we advance a cavity-assisted quantum memory protocol based on Pre-created Long-lived Macroscopic (PLM) coherence, thereby transforming quantum memory from a passive storage device into a platform for deterministic in-memory photonic processing. It is demonstrated that spin PLM coherence enables all-optical control of quantum memory using robust radio-frequency rotations alone. Here, the spin coher...
  </details>

- **2026-09-19** — Xiaoshi Li, Yule Xu, Chunghiu Kong et al. — [AquaCap: A Training-Free Underwater Embodied Agent with Code-as-Policy](http://arxiv.org/abs/2609.23133v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in vision-language-action models have stimulated growing interest in underwater embodied intelligence. However, their reliance on large-scale interaction data limits their applicability underwater, where data collection is costly and scarce. To address this challenge, we present AquaCap, a training-free Code-as-Policy framework for autonomous underwater navigation and manipulation. AquaCap employs a dual-layer agent that translates task instructions and environmental observations...
  </details>

- **2026-09-19** — Xiongfeng Peng, Lu Xu, Yandong Wang et al. — [H-VLA: Hierarchical Vision-Language-Action Model with Key-Action Reasoning and Motion Planning in a Unified Action Space](http://arxiv.org/abs/2609.22895v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have shown strong potential for robotic manipulation, but many existing methods still rely on direct mappings from language and visual observations to dense actions. This formulation can weaken the semantic reasoning capability inherited from pre-trained Vision-Language Models (VLMs), which are mainly optimized for visual-linguistic understanding rather than low-level control, and becomes fragile under spatial variations, including changes in object positions,...
  </details>

- **2026-09-19** — Twinkll Sisodia — [From Inference Engine to Inference Control Plane: Connecting vLLM, llm-d, and the Evolution of Efficient Distributed LLM Serving](http://arxiv.org/abs/2609.23130v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference is evolving from an engine-local optimization problem into a distributed control problem involving reusable state, phase placement, heterogeneous accelerators, networking, autoscaling, reliability, and service-level objectives. This paper connects that transition across peer-reviewed systems research, open-source implementations, and documented production studies. It treats vLLM and llm-d as complementary layers: model-serving engines optimize execution throu...
  </details>

- **2026-09-19** — Mohammad Khateri, Morteza Ghahremani, Jussi Tohka et al. — [SomaNet: Weakly Supervised Learning for Instance Soma Segmentation in 3D Electron Microscopy with Partial Annotations](http://arxiv.org/abs/2609.23019v1)
  <details><summary>📄 Abstract</summary>
  Soma instance segmentation, i.e., identifying and delineating individual cell somas as distinct instances, is crucial for cellular analysis and connectomic reconstruction. Three-dimensional electron microscopy (3D EM) provides nanometer-scale resolution for capturing fine-grained soma morphology. However, dense instance-level manual annotation is prohibitively costly, limiting the scalability of fully supervised methods. To address this challenge, we propose SomaNet, a weakly supervised framewor...
  </details>

- **2026-09-19** — Daeun Ji, Minkyoung Kim, Dongkuk Kim et al. — [Beyond Similarity: Coverage-Aware Prompt Selection for Time Series Forecasting with LLMs](http://arxiv.org/abs/2609.22977v1)
  <details><summary>📄 Abstract</summary>
  Similarity-based retrieval is the dominant rule for conditioning large language models (LLMs) in in-context learning, retrieval-augmented generation, and prompt-based time series forecasting. The rule concentrates on near-duplicate candidates, an issue that has motivated diversity-aware retrieval but remains unexamined in other retrieval-conditioned pipelines. We study this issue using prompt-based time series forecasting as a test bed, where a learned prompt pool is retrieved by similarity. Dom...
  </details>

- **2026-09-19** — Yunqi Gao, Zhanfeng Liao, Hanzhang Tu et al. — [D3GS: Depth, DINO, and RGB Diffusion Co-Guided 3D Gaussian Splatting for Sparse-View Reconstruction](http://arxiv.org/abs/2609.22941v1)
  <details><summary>📄 Abstract</summary>
  Novel view synthesis from sparse inputs remains challenging for 3D Gaussian Splatting (3DGS) due to ambiguous geometry, cross-view inconsistency, and missing details in under-constrained regions, resulting in degraded reconstruction and unstable rendering. To tackle these issues, we propose D$^{3}$GS, a Depth-DINO-Diffusion guided sparse-view Gaussian reconstruction framework that jointly enhances geometry and appearance. D$^{3}$GS first recovers a high-resolution, metric depth map via diffusion...
  </details>

- **2026-09-19** — Sebastian Berger, Katharina Winter, Fabian B. Flohr — ["Dear LLaVA, Please Drive": A Depth-Aware Vision-Language Agent for Closed-Loop Robotic Control](http://arxiv.org/abs/2609.22925v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) provide a compelling foundation for reasoning-driven mobile navigation, offering rich contextual understanding and strong generalization from large-scale pretraining. Most existing navigation frameworks rely on imitation learning and therefore require substantial labeled trajectory data, limiting their scalability and robustness. In this work, we propose a parameter-efficient approach to fine-tune a pretrained VLM for autonomous navigation using an Imperative Learni...
  </details>

- **2026-09-19** — Yalin Zhang, Zhongxin Liucand Fuyong Wang, Zengqiang Chen — [Distributed Cooperative Control with Prescribed Performance of BESSs with A Unified Discharge Constrain for Power Allocation under Dynamic Load](http://arxiv.org/abs/2609.22889v1)
  <details><summary>📄 Abstract</summary>
  Battery energy storage system (BESS) is integrated into the smart grid to enhance scalability, economy, and greenery. And the State-of-Charge (SoC) balance is one of the basic problems of BESSs, which can maximize the utilization of capacity. BESSs with a unified relative variation rate for SoC can be simultaneously filled or empty, while real-time estimation schemes of SoC balance and power sharing states are required in this power allocation scheme. Therefore, the prescribed performance contro...
  </details>

- **2026-09-19** — Qiyi Li, Xiao Zheng, Guofeng Zhang — [Neural network-based multipartite entanglement classification with prior guidance from quantum uncertainty relations](http://arxiv.org/abs/2609.22768v1)
  <details><summary>📄 Abstract</summary>
  Quantum entanglement is a crucial resource in quantum information processing, yet its efficient, scalable and robust classification in multipartite systems remains theoretically challenging. Although supervised machinelearning has been applied to this task, most existing methods still suffer from high measurement costs, computational consumption, and weak noise robustness. In this work, by incorporating multipartite uncertainty relations as prior guidance, we propose a neural network approach to...
  </details>

- **2026-09-18** — Steve Drew, Jiayu Zhou — [LEGIT: Credentialing Protocol for Trustworthy AI Agent Marketplaces](http://arxiv.org/abs/2609.21325v1)
  <details><summary>📄 Abstract</summary>
  Agentic marketplaces are emerging where AI agents with varying capabilities autonomously complete specialized tasks for buyers. A major challenge of such marketplaces is that buyers cannot easily determine which agent will perform best on their tasks. Reported benchmark scores may be difficult to verify or compare across tasks, software, and budgets. We introduce LEGIT, a credentialing protocol connecting certification, reputation, and proposed marketplace allocation. Certification binds measure...
  </details>

- **2026-09-18** — Yiming Zhang, Jinghong Zhang, Haoran Zhao et al. — [An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency](http://arxiv.org/abs/2609.22043v1)
  <details><summary>📄 Abstract</summary>
  Memory systems for large language models have focused predominantly on efficient retrieval, whereas the decision of whether retrieved memories should be trusted has received comparatively little attention. When the memory store contains conflicting positions, standard retrieval-augmented generation (RAG) blindly injects memories and amplifies hallucinations: in models susceptible to memory injection, the RAG hallucination rate under conflicting memories is markedly higher than that of a memory-f...
  </details>

- **2026-09-18** — Jia Li, Li Dai, Peng Jia et al. — [Beyond Exact Match: Task-Aware GRPO for Cross-Domain PCBA Visual Question Answering](http://arxiv.org/abs/2609.21276v1)
  <details><summary>📄 Abstract</summary>
  In automated Printed Circuit Board Assembly (PCBA) inspection, standards-guided decisions require systems to jointly reason over fine-grained visual cues, component semantics, and manufacturing knowledge. Although large vision-language models (VLMs) provide a promising foundation, their deployment is hindered by the domain shift between standards-derived samples and real-world production-line imagery, together with heterogeneous output spaces spanning choice-based and numerical counting tasks. T...
  </details>

- **2026-09-18** — Haolong Meng, Fangbo Qin, Mengchen Bai et al. — [Towards Fine-Grained Object Manipulation: SAM3-Guided Visuomotor Policy with Persistent Memory Learning and Focused Visual Conditioning](http://arxiv.org/abs/2609.21621v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained object (FO) manipulation requires robots to distinguish a specified FO from visually similar objects and execute actions reliably despite scene distractors. However, scene-level visual conditioning lacks explicit object selection, while category-level guidance cannot reliably distinguish FOs within the same category. We present a SAM3-guided visuomotor framework that addresses these challenges through persistent object memory and focused visual conditioning. First, we introduce FO M...
  </details>

- **2026-09-18** — Yuhyeon Hwang, Daniel Sungho Jung, YongHyeok Seo et al. — [Learning Distance-Conditioned Object Transport for Humanoid Loco-Manipulation from a Single Motion Clip](http://arxiv.org/abs/2609.21467v1)
  <details><summary>📄 Abstract</summary>
  Motion tracking can reproduce humanoid loco-manipulation from a single retargeted motion clip, but a policy trained on a fixed reference primarily reproduces its demonstrated transport outcome. Although the source trajectory visits intermediate object displacements, transport termination is demonstrated only at its endpoint. We identify this mismatch as the termination-versus-passage gap: intermediate displacements are observed as passage states rather than termination-complete outcomes. We intr...
  </details>

- **2026-09-18** — Yijun Hong, Jiarun Zhu, Xiaoquan Sun et al. — [FAN: Foresight Action Normalization for Continual Adaptation of Vision-Language-Action Models](http://arxiv.org/abs/2609.21358v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models pre-trained on large-scale, closed datasets have demonstrated remarkable success across diverse robotic manipulation tasks. However, their long-term real-world deployment necessitates continuously acquiring new skills while retaining previously learned capabilities. While pioneering works have explored continual VLA adaptation using techniques such as experience replay and reinforcement fine-tuning, they overlook a foundational mechanism: action normalization,...
  </details>

- **2026-09-18** — Sheng-An Xu, Hanyang Li, Jianhao Ma et al. — [Beyond Shadow Weights: Quantization-Aware Training as Quantized-Endpoint Descent](http://arxiv.org/abs/2609.21834v1)
  <details><summary>📄 Abstract</summary>
  Quantization-aware training (QAT) updates a full-precision shadow weight $\mathbf{x}$ but deploys the quantized endpoint $Q(\mathbf{x})$. Existing explanations for QAT largely view its success through the lens of shadow weights: QAT can move $\mathbf{x}$ toward flatter basins, gain robustness from quantization-induced oscillations, or balance the shadow loss $f(\mathbf{x})$ against the quantization error $\|\mathbf{x}-Q(\mathbf{x})\|_2$. These perspectives do not directly explain the empirical o...
  </details>

- **2026-09-18** — Mushir Akhtar, M. Tanveer, Mohd. Arshad — [Beyond Benchmark Scores: Auditing Medical Vision-Language Models for Chest X-Ray Tuberculosis Screening](http://arxiv.org/abs/2609.21763v1)
  <details><summary>📄 Abstract</summary>
  A medical model's benchmark score does not establish that the same conclusion holds under a different evaluation. This study tests whether claims about model ranking, score reliability and screening performance survive changes in cohort, prompt, negative spectrum, specified prevalence and operating threshold. We audit three medical vision-language models (BioMedCLIP, CheXficient, and MedSigLIP) and a general-domain OpenCLIP comparator on 12,200 chest radiograph records from four datasets (Montgo...
  </details>

- **2026-09-18** — Jingke Zhou, Chenhang Ma, Zhizhou Zhong et al. — [Think Locally, Refine Globally for Memory-Efficient 3D Reconstruction](http://arxiv.org/abs/2609.21437v1)
  <details><summary>📄 Abstract</summary>
  We propose LoG-VGGT, a memory-efficient framework for long-sequence 3D reconstruction that balances local temporal modeling with global camera consistency. Instead of relying on full global attention, our method introduces cross-window attention at a small subset of transformer blocks, enabling effective information propagation across adjacent temporal windows while keeping memory usage bounded. To mitigate long-term pose drift, we further design a global camera consistency refinement module, wh...
  </details>

- **2026-09-18** — Yilin Evan Li, Harikrishnan KP, Sankalpa Hazra et al. — [Strain-Induced Relaxor Multiferroicity at Room Temperature in Hexaferrite BaFe12O19 Thin Films](http://arxiv.org/abs/2609.21352v1)
  <details><summary>📄 Abstract</summary>
  Multiferroic materials that combine magnetic and electric order at room temperature are rare. Here, we demonstrate strain-induced room-temperature polar order in the ferrimagnetic hexaferrite BaFe12O19. First-principles calculations reveal a strain-tunable energy landscape with multiple competing dipolar configurations and predict that compressive strain favors polar distortions. Using an isostructural Sr1.03Ga10.81Mg0.58Zr0.58O19 substrate, we grow coherently strained BaFe12O19 films with 1.1% ...
  </details>

- **2026-09-17** — Hassan Saeed Hassan Albattra, Mazen Mohammed Bahgat, Rahatara Ferdousi et al. — [HerHealthEval: Evaluating Multilingual and Register-Sensitive Understanding of Women's Health Communication](http://arxiv.org/abs/2609.20684v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used in healthcare communication, yet most evaluations emphasize response quality while assuming that the user's concern has been interpreted correctly. We introduce HerHealthEval, a controlled evaluation framework for multilingual understanding of women's-health communication. For each clinical case, HerHealthEval provides matched versions in English, French, and Modern Standard Arabic using six communicative forms: canonical, clinical, layperson, indirect...
  </details>

- **2026-09-17** — Chenxi Wu, Zimu Wang, Haiyang Zhang et al. — [SAFARI: An Industrial Benchmark for LLM-Assisted Hazard Analysis and Risk Assessment](http://arxiv.org/abs/2609.20584v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly considered for safety-critical engineering, yet their reliability in regulated functional-safety workflows remains underexplored. We introduce SAFARI (Safety-Aware Functional Automotive Risk Inference), the first industrial benchmark for LLM-assisted automotive Hazard Analysis and Risk Assessment (HARA) under ISO 26262. It contains 3,000 de-identified industrial HARA cases and evaluates two coupled tasks: open-ended hazard analysis and standards-grou...
  </details>

- **2026-09-17** — Bo Tang, Zixuan Liao, Hao Li et al. — [Noise-Robust Quantum State Characterization for Remote State Preparation with Deep Learning](http://arxiv.org/abs/2609.20523v1)
  <details><summary>📄 Abstract</summary>
  Quantum communication underpins secure information processing and scalable quantum networks. In particular, remote state preparation (RSP) enables efficient quantum state transfer, but accurately estimating target states under complex noise remains challenging. Here, we propose a Transformer-based Quantum State Characterizer (TQSC) model for noisy RSP experiments. Our model reconstructs experimentally prepared pure and mixed photonic polarization states from noisy measurements in complex scatter...
  </details>

- **2026-09-17** — Małgorzata Nowak-Kępczyk — [Long-Lived Carpet-Like Transients in Time-Dependent Modular Discrete Laplacian Dynamics](http://arxiv.org/abs/2609.20416v1)
  <details><summary>📄 Abstract</summary>
  Binary modular Laplacian dynamics is organized by repeated replication, growth, and collapse on dyadic scales. We study how isolated and periodically repeated non-binary updates modify this organization and whether they can sustain densely occupied geometric structures.   Computational experiments across multiple finite seeds, neighborhood masks, inserted moduli, and periodic schedules show that constant prime moduli retain the expected \(p\)-adic replication hierarchy. A single non-binary inser...
  </details>

- **2026-09-17** — Ha Van Dau, Thanh Tung Khuat, Nguyen Thanh Dung — [Beyond Depth Truncation: Controlled Evaluation of Depth Utilization in Recursive Language Models](http://arxiv.org/abs/2609.19934v1)
  <details><summary>📄 Abstract</summary>
  Depth-recurrent language models iteratively apply a small layer stack, decoupling per-token compute from distinct parameter count. To determine whether such a model genuinely utilizes its depth, both recurrence and layer-pruning literatures rely on a shared evaluation: truncating depth at inference time, plotting quality against retained depth fraction, and reading off the slope. While cheap and training-free, this metric suffers from an unexamined flaw: it extracts a single scalar from an inter...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 13 papers

- **2026-09-21** — Timothy Urista — [Who Pays for the KV Cache? Attributing Shared AI Inference Spend Across Kubernetes and LLM Provider Bills](http://arxiv.org/abs/2609.24991v1)
  <details><summary>📄 Abstract</summary>
  Organizations pay for AI through disconnected ledgers: Kubernetes allocations for self-hosted inference, gateway logs, and per-token bills from API providers. We present unalloc, an open-source tool that joins OpenCost, LiteLLM, OpenAI and Anthropic cost data into one exact ledger and reports the share of spend with no owner, and use it to study where attribution breaks at the seams between these systems. Five case studies run inference for real or simulate it: a vLLM-style serving simulator wit...
  </details>

- **2026-09-20** —  ScholarSeed AI Team, Ao Zhang, Caoqinwei Gong et al. — [ScholarStack: Layered Research Asset Orchestration and Cross-Task Reuse for Scientific Agents](http://arxiv.org/abs/2609.23735v1)
  <details><summary>📄 Abstract</summary>
  Scientific agents support a range of literature-based research tasks, such as retrieval, question answering, evidence-grounded generation, and claim assessment. Most existing systems, however, are organized around individual tasks: the same papers are repeatedly retrieved, segmented, and interpreted, and the understanding built in one task is difficult to reuse in the next. We present ScholarStack, a layered research asset framework that compiles a paper collection into reusable, versioned, and ...
  </details>

- **2026-09-20** — Aleks Czufarow, Ihor Babin — [Transferring Visual Explanations: How Cross-Architecture Knowledge Distillation Affects Model Interpretability](http://arxiv.org/abs/2609.23561v1)
  <details><summary>📄 Abstract</summary>
  Deploying efficient neural networks is essential in resource-constrained environments, yet compact models often sacrifice interpretability - a critical in safety-critical domains such as autonomous driving and medicine. This study investigates whether Knowledge Distillation transfers the spatial feature attribution of a large teacher network to a compact student. To assess the influence of the KD scheme on interpretability, we distill a ResNet-152 teacher into a ResNet-34 student on ImageNet-1K ...
  </details>

- **2026-09-20** — Tezan Sahu — [Packaged, But Not Portable: Why Conforming to the Agent Plugin Standard Is Rare, and Why Conforming Would Not Be Enough](http://arxiv.org/abs/2609.23809v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are extended by plugins: installable bundles that ship skills, sub-agents, commands, hooks, and tool servers. On 24 July 2026, an open specification (Agent Plugins v1.0.0) standardised how such a bundle is laid out and described, so that one plugin could run on any agent. We ask the two questions a practitioner would ask of it: is the ecosystem adopting the standard, and if a plugin did conform, would that be enough to make it work alongside the other plugins a user has installed? ...
  </details>

- **2026-09-20** — Qi Qin, Erbo Li, Ting Wei et al. — [PACE: Plug-and-Play Contextual Embedding for Feature Screening with Pretrained Tabular Foundation Models](http://arxiv.org/abs/2609.23574v1)
  <details><summary>📄 Abstract</summary>
  In high-dimensional tabular learning, feature screening provides a lightweight, model-agnostic way to remove irrelevant features before model fitting. However, scoring raw values directly can miss nonlinear or distributional structure. We introduce PACE (Plug-and-Play Contextual Embedding), which inserts a frozen tabular foundation model (TFM) column encoder before an existing feature-scoring rule, expanding each feature into a higher-dimensional contextual representation. Across controlled stud...
  </details>

- **2026-09-19** — Huafu Li, Jia Xia — [When Agentic Trust Crosses Organizational Boundaries: Structural Externalization and a Reference Model for Trust Evidence](http://arxiv.org/abs/2609.22961v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems increasingly invoke tools, services, data, and other agents across organizational boundaries, yet a relying party cannot assess a delegated action solely from producing-domain controls and records. This paper develops Trustworthiness as a Service (TaaS) through a synthesis of trustworthy-AI governance, agent security, distributed trust management, identity, provenance, assurance, and control-plane research. The analytical unit is a cross-domain reliance proposition that names the...
  </details>

- **2026-09-18** — Tengfei Shao — [Auditing bipartite motif interpretations: a worked example with conservation checks and open-path decomposition](http://arxiv.org/abs/2609.22014v1)
  <details><summary>📄 Abstract</summary>
  Motif profiles of bipartite agent-object networks, such as tourist-site visits and customer-item transactions, are read as evidence about structural roles and about differences between networks, often without asking what the two degree sequences already fix. In a simple bipartite graph the induced k-fan count on one node type is a sum of degree combinations, so it has zero variance under a null that preserves both degree sequences. We apply this known result to a reconstructed tourism rating net...
  </details>

- **2026-09-18** — Zijie Cao, Xijun Qu, Zhicheng Gu et al. — [AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory](http://arxiv.org/abs/2609.21940v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is essential for large language model (LLM) agents to maintain consistency and personalization over extended interactions. Existing memory systems typically rely on fixed granularities or static schemas, but these designs struggle when heterogeneous information, such as preferences, events, constraints, and temporal updates, is embedded in a single mixed representation. The resulting semantic interference makes top-K retrieval sensitive to noise and often leaves relevant evidenc...
  </details>

- **2026-09-18** — Yanxiao Liu, Sicheng Wan, Zhan Gao et al. — [Watermarkable Multi-Draft Speculative Sampling via Poisson Processes](http://arxiv.org/abs/2609.21858v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have achieved state-of-the-art performance across a wide range of tasks, motivating two important aspects of deployment: inference efficiency and output provenance, which can be tackled by speculative sampling and watermarking, respectively. However, recent works have shown that combining these two goals is highly nontrivial and can be potentially impossible. In this work, we develop a novel multi-draft speculative sampling algorithm based on Poisson processes that i...
  </details>

- **2026-09-18** — Kairui Yang, Xunkai Li, Kaixiang Zhang et al. — [OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems](http://arxiv.org/abs/2609.21527v1)
  <details><summary>📄 Abstract</summary>
  Graph-enhanced multi-agent systems (G-MAS) coordinate large language model agents through communication graphs and role assignments, which determine how agents exchange information and divide responsibilities. However, final-score comparisons across systems combine differences in models, communication patterns, roles, and computation costs, making performance differences difficult to attribute to specific communication structures, role assignments, and information flows. To address this evaluati...
  </details>

- **2026-09-18** — Qiang Zhang, Ruixue Ding, Fanrui Zhang et al. — [ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL](http://arxiv.org/abs/2609.21378v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has substantially improved large language model (LLM) agents in verifiable domains, but remains difficult to apply to open-ended agent tasks, where solutions are diverse and reliable scalar rewards are hard to obtain. Recent pairwise evaluation methods alleviate reward discrimination collapse by replacing pointwise scoring with relative preferences. However, they still compress rich comparative feedback into a single trajectory-level reward, obscuring decisive intermediate...
  </details>

- **2026-09-17** — Luca De Grandis, Silvia Cappelletti, William Raccagni et al. — [DocAttriBench: Benchmarking Answer Grounding in Document Visual Question Answering](http://arxiv.org/abs/2609.20574v1)
  <details><summary>📄 Abstract</summary>
  Answer grounding in document visual question answering remains an open challenge: most benchmarks lack grounding annotations or provide limited-quality labels, while constructing grounded datasets still requires costly manual effort. We introduce DocAttriBench (DAB), a large-scale benchmark for fine-grained, element-level source attribution in Document VQA, grounding answers to specific layout elements such as text blocks, tables, and images. To build DAB, we propose a Mask-based Perplexity-Deri...
  </details>

- **2026-09-17** — Moritz Weckbecker, Sweta Jena, Jonas Müller et al. — [Can Data Attribution Filter Out Subliminal Learning? Not Reliably](http://arxiv.org/abs/2609.20027v1)
  <details><summary>📄 Abstract</summary>
  Subliminal learning allows language models to transmit behavioral traits through training data with no obvious semantic relationship to those traits, undermining content-based data filtering as a safety intervention. Training data attribution offers an alternative: it identifies the training examples responsible for a given model behavior, independent of their semantic content, and so may apply in exactly the cases where semantic inspection fails. We evaluate three gradient-based attribution met...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-09-18** — Hiskias Dingeto — [A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal](http://arxiv.org/abs/2609.21996v1)
  <details><summary>📄 Abstract</summary>
  Large language models can hold knowledge they do not report. A model may sandbag on a capability evaluation, or answer against what it internally knows, and its outputs alone cannot tell whether it is hiding an answer or simply does not have one. We borrow the Concealed Information Test, a forensic method that identifies guilty knowledge by presenting a suspect with the true detail among plausible decoys and measuring a stronger response to the item they recognize. Our method, Probe of Internal ...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-09-17** — Song Zhang, Jiankang Yao, Hongtao Li et al. — [A Scalable Trust Discovery Architecture for the Internet of Agents](http://arxiv.org/abs/2609.20095v1)
  <details><summary>📄 Abstract</summary>
  The Internet of Agents is expected to enable large numbers of autonomous agents to discover, verify, and collaborate with each other across heterogeneous platforms. However, current agent protocols mainly address tool invocation and inter-agent communication, leaving scalable agent registration, trustworthy identification, and capability-oriented discovery largely unresolved. To address this, this paper proposes a scalable trust discovery architecture for the Internet of Agents. The proposed arc...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 2 papers

- **2026-09-21** — Xinyu Wang, Tung Sum Thomas Kwok, Zhenghan Tai et al. — [FinInteract: Benchmarking Clarification and Intent Integration in Ambiguous Financial Question Answering](http://arxiv.org/abs/2609.24002v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly answer financial questions by searching regulatory filings. Such questions are often deceptively under-specified: Meta Platforms' "operating income" is $46.75B consolidated but $62.87B for the Family of Apps segment, and each reading is exactly verifiable against the filing. A capable agent should recognize the ambiguity and ask, rather than commit to a plausible but unintended reading. Existing financial benchmarks cannot measure this, because one gold a...
  </details>

- **2026-09-21** — Xinnuo Zhang, Zhike Tang, Jing Xu et al. — [LegendBench: A Diagnostic Benchmark for Legend Understanding with Counterfactual Interventions](http://arxiv.org/abs/2609.24172v1)
  <details><summary>📄 Abstract</summary>
  Legends are fundamental to chart understanding, as reliable interpretation requires correctly binding legend entries to corresponding visual marks. While vision-language models (VLMs) are increasingly applied to chart understanding, their legend understanding is poorly diagnosed by aggregate accuracy, which can be satisfied by superficial shortcuts and confound legend-specific errors with other reasoning failures. To enable fine-grained diagnosis and controlled testing, we introduce LegendBench,...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 172 papers

- **2026-09-21** — Eunkyu Park, Markelle Roesti, Wesley Hanwen Deng et al. — [Who Does What in AI Auditing? Designing Human-AI Collaboration for Auditing Generative AI](http://arxiv.org/abs/2609.24986v1)
  <details><summary>📄 Abstract</summary>
  AI auditing increasingly incorporates AI agents to expand the scale and breadth of audit coverage, yet little is known about how auditing work should be divided without displacing human judgment. We introduce Human-Agent Audit Collaboration (HAAC), a workflow and system for structuring human-AI collaboration in AI auditing. Drawing on prior work and formative consultations with AI auditing practitioners, HAAC specifies how agents can support exploration, assessment, reporting, and review while p...
  </details>

- **2026-09-21** — Xinnong Zhang, Jiayu Lin, Jia Wang et al. — [SocioVerse2: A Longitudinal Dynamic Social Simulation Framework under a Human-AI Co-evolutionary Paradigm](http://arxiv.org/abs/2609.24911v1)
  <details><summary>📄 Abstract</summary>
  Social simulation offers the social sciences an experimental instrument that the real world cannot supply, and generative agents have transformed it by acting as silicon samples that unite agent-based modeling with real behavioral data. Existing platforms verify collective behavior, align simulated populations with real societies in cross-sections, and employ autonomous agents for the research process. However, two social science requirements remain without systematic support: intervention in th...
  </details>

- **2026-09-21** — Kewei Zhang, Zheng Chen, Haotong Qin et al. — [SPHQuant: Efficient extreme low bit weight quantization for Vision-Language Models](http://arxiv.org/abs/2609.24875v1)
  <details><summary>📄 Abstract</summary>
  Recent foundation models are moving toward native multimodal Vision-Language Models (VLMs), making VLMs a central form of next-generation foundation models. However, their large language backbones make edge deployment difficult due to high memory footprint and memory-bound autoregressive decoding. Weight-only post-training quantization is a practical solution, but pushing VLMs to extreme low bit-widths remains challenging: existing rotation-free methods suffer from outliers at 2-3 bits, while ro...
  </details>

- **2026-09-21** — Junde Wu, Jiayuan Zhu, Minghao Hu et al. — [MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution](http://arxiv.org/abs/2609.24838v1)
  <details><summary>📄 Abstract</summary>
  Medical agents increasingly combine general reasoning models with specialized clinical tools, yet their capabilities remain largely fixed by what clinicians and engineers design before deployment. Recursive self-improvement (RSI) offers a different paradigm in which agents learn from their own failures and autonomously expand their capabilities, but directly applying RSI to medicine introduces fundamental safety challenges. We introduce MedRSI, the first recursive self-improvement framework for ...
  </details>

- **2026-09-21** — Yeji Kim, Mi-Young Kim, Randy Goebel — [When Quantization Preserves Accuracy but Not Evidence: Explanation-Aware Post-Training Quantization for Medical LLMs](http://arxiv.org/abs/2609.24799v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) enables efficient deployment of large language models, and PTQ methods are usually optimized and evaluated with generic reconstruction, perplexity, or answer accuracy. But in explanation-critical domains, preserving only the final answer may be insufficient, since users may also inspect generated rationales to judge whether a prediction is trustworthy. We study this issue in medical multiple-choice question answering, where rationales should provide evidence that...
  </details>

- **2026-09-21** — Hasibur Rahman, Mahsa Nasri, Manasi Vaidya et al. — ["MeBo Leaves a Piece of You Behind": Designing a Relational Voice-Based Memory Companion for Older Adults](http://arxiv.org/abs/2609.24706v1)
  <details><summary>📄 Abstract</summary>
  Autobiographical remembering supports identity, well-being, and social connection in later life, yet voice-based memory technologies largely rely on isolated prompts. We designed and built MeBo, a fully functional relational voice-based memory companion, through participatory design with 11 older adults. Their accounts shaped four Design Strategies that guided MeBo's interaction design and multi-agent implementation. In a mixed-methods evaluation with 20 older adults, participants found MeBo exc...
  </details>

- **2026-09-21** — Julian Oelhaf, Alexander Luce, Christian Bergler et al. — [Offline Reinforcement Learning for Distribution-Grid Protection](http://arxiv.org/abs/2609.24703v1)
  <details><summary>📄 Abstract</summary>
  Data-driven protection may complement conventional relays in distribution grids whose operating conditions vary with distributed generation, switching events, and changing short-circuit levels. We study line-selective tripping from static trajectories of a realistically simulated CIGRE medium-voltage network using offline reinforcement learning. A convolutional Q-network receives causal voltage-current phasor and apparent-impedance features, optionally together with raw waveforms, and is trained...
  </details>

- **2026-09-21** — Man Tang, Zhaoyun Zong, Diqiong Jiang et al. — [Direction-Aware Masked Pretraining for 3D Seismic Representation Learning and Transfer to Cross-Area Acoustic Impedance Inversion](http://arxiv.org/abs/2609.24615v1)
  <details><summary>📄 Abstract</summary>
  Large archives of unlabeled three-dimensional seismic data offer opportunities for self-supervised representation learning and subsequent transfer to acoustic impedance inversion. However, conventional masked pretraining often treats three axes equivalently, overlooking differences between lateral reflector structure and vertical waveform characteristics. We propose a direction-aware masked autoencoder for three-dimensional post-stack seismic data, combining anisotropic tokenization, direction-a...
  </details>

- **2026-09-21** — Zhaomin Lyu, Ding Zhang, Yan Jiang — [Optimal Allocation of Grid-Forming Frequency Shaping Control](http://arxiv.org/abs/2609.24583v1)
  <details><summary>📄 Abstract</summary>
  Various inverter-based control strategies have been proposed to improve frequency security for power systems with high renewable penetration. Among them, the grid-forming frequency shaping control is particularly promising due to its ability to shape the post-contingency aggregate system frequency dynamics into first-order with prescribed rate of change of frequency (RoCoF) and steady-state frequency deviation. Moreover, the shaped aggregate dynamics depends on the harmonic sum of all inverter t...
  </details>

- **2026-09-21** — Mingke Lu, Anxing Xiao, David Hsu — [MIGU: Multimodal Instruction Grounding under Uncertainty for Manipulation Planning](http://arxiv.org/abs/2609.24995v1)
  <details><summary>📄 Abstract</summary>
  Understanding natural human instructions is crucial for deploying robots in human-centric environments. We study multimodal instruction grounding, where language and gesture provide complementary but uncertain cues. We present MIGU, a modular framework that combines semantic and geometric evidence into a unified grounding belief and connects it to manipulation planning. MIGU constructs a 3D geometric likelihood by propagating viewing-direction and depth uncertainty through eye-finger geometry wh...
  </details>

- **2026-09-21** — Ke Zhou, Edyta Bogucka, Daniele Quercia — [Small-world Networks of Agents Brainstorm AI Risks to Support Ideation](http://arxiv.org/abs/2609.24859v1)
  <details><summary>📄 Abstract</summary>
  The ideation phase of participatory AI risk assessment often starts with a blank slate or a limited list of predefined risks, making it difficult to surface indirect or systemic harms. To address this limitation, we propose a three-stage ideation support tool. The tool complements participatory AI, rather than replacing it, and helps focus later engagement with affected communities. First, it dynamically discovers stakeholders depending on the given AI use and recursively expanding outward, allo...
  </details>

- **2026-09-21** — Jie Gong, Maowei Jiang, Zhiwei Liu et al. — [TimeLitmus: A Diagnostic Benchmark for Cross-Modal Understanding and Explanation Faithfulness in Event-Conditioned Time-Series Prediction](http://arxiv.org/abs/2609.24677v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to make predictions from numerical time-series histories and textual events. Yet accuracy alone cannot reveal whether correct answers reflect effective integration of the two inputs or instead arise from event polarity, unimodal priors, or superficial cues. Likewise, plausible explanations may rationalize predictions without faithfully reflecting the evidence that drives model behavior. We introduce TimeLitmus, a diagnostic benchmark for cross-m...
  </details>

- **2026-09-21** — Xijing Cui, Huayan Pu, Jun Luo et al. — [Feasibility Distance Fields for Heterogeneous Constraints in Robot Configuration Space](http://arxiv.org/abs/2609.24632v1)
  <details><summary>📄 Abstract</summary>
  Robot manipulators are monitored by constraint-specific indicators whose units and gradient scales are not comparable, so they do not provide a common measure of the configuration-space motion remaining before violation. We define the feasibility distance field (FDF) as the distance, under a fixed positive-definite joint-space metric, to the union of infeasible configuration sets. Classical distance-to-set theory gives 1-Lipschitz continuity, almost-everywhere differentiability, and unit dual-gr...
  </details>

- **2026-09-21** —  ATLAS Collaboration — [Search for a top-philic heavy resonance in association with top quarks in $pp$ collisions at $\sqrt{s} = $ 13 TeV and 13.6 TeV with the ATLAS detector](http://arxiv.org/abs/2609.24950v1)
  <details><summary>📄 Abstract</summary>
  A search for a new top-philic vector boson ($Z'$) produced in association with a top-quark or a pair of top quarks, and decaying into a top quark pair is presented. The search uses $pp$ collision data collected by the ATLAS detector at the Large Hadron Collider at centre-of-mass energies of $\sqrt{s} =$ 13 TeV and 13.6 TeV, corresponding to integrated luminosities of 140 fb$^{-1}$ and 56 fb$^{-1}$, respectively. Events containing exactly two same-sign leptons or at least three leptons (electrons...
  </details>

- **2026-09-21** — Yuanwen Yue, Stefano Puliti, Damien Robert et al. — [Toward a foundation model for forest point clouds](http://arxiv.org/abs/2609.24787v1)
  <details><summary>📄 Abstract</summary>
  Forest inventories increasingly rely on artificial intelligence (AI) models to derive forest attributes from large-scale 3D point clouds. Current models are typically specialized to a single task, sensor, and forest type, making adaptation expensive in terms of annotations, computation, and expertise. We ask whether a single pretrained model can instead learn transferable representations across diverse forest inventory settings. Inspired by recent developments in language modelling and computer ...
  </details>

- **2026-09-21** — Fabian Spaeh, Jingxing Fang, Shandian Zhe et al. — [Universal Multi-Modal Traceformer: Integrating Heterogeneous Context for Process Event Prediction](http://arxiv.org/abs/2609.24579v1)
  <details><summary>📄 Abstract</summary>
  Event logs arise in a wide range of real-world processes, capturing not only event activities and timestamps but also multi-modal contextual information. Existing event-sequence models, including many temporal point process approaches, primarily model event activities and timestamps while overlooking heterogeneous context, such as numerical measurements, categorical attributes, textual descriptions, and metadata associated with individual events and entire traces. In this paper, we propose Unive...
  </details>

- **2026-09-21** — Jun Cheng, Yuanyuan Kong, Qing Huang et al. — [Preoperative Prediction of Microvascular Invasion in Hepatocellular Carcinoma by Integrating Multimodal Ultrasound and Clinical Data: A Multicenter Study](http://arxiv.org/abs/2609.24524v1)
  <details><summary>📄 Abstract</summary>
  Background: Microvascular invasion (MVI) predicts recurrence and survival in hepatocellular carcinoma (HCC) but requires postoperative histopathology for diagnosis. We developed and validated a model integrating multimodal ultrasound and clinical data for preoperative MVI prediction. Methods: This multicenter study included 489 patients with HCC from eight centers. All patients had B-mode ultrasound (BUS), color Doppler flow imaging (CDFI), dynamic contrast-enhanced ultrasound (DCE-US), and clin...
  </details>

- **2026-09-21** — Hamed Alimohammadi, Burcu Şahin, Arda Akman et al. — [rApp/xApp Attestation: A New Security Use Case for O-RAN](http://arxiv.org/abs/2609.24296v1)
  <details><summary>📄 Abstract</summary>
  The disaggregation and softwarization introduced by the Open Radio Access Network (O-RAN) architecture enable multi-vendor innovation but also expose the RAN Intelligent Controller (RIC) ecosystem to new runtime security risks. Existing O-RAN specifications define strong safeguards for onboarding, authentication, identity management, and secure communication; however, they do not provide a concrete mechanism for verifying whether deployed rApps and xApps remain in their intended, untampered stat...
  </details>

- **2026-09-21** — Songqi Li, Dongqing Li, Zheqiao Cheng — [Canonical Procedural Actions: An Auditable Annotation Protocol for Tool-Use Agent Traces](http://arxiv.org/abs/2609.24264v1)
  <details><summary>📄 Abstract</summary>
  Tool-use agent traces identify messages and API calls, but procedural analyses also need explicit units of action and inspectable links to their evidence. We present Canonical Procedural Actions (CPAs), an annotation protocol that records a procedural function, its first agent-event anchor, the agent events that realize it, and separate contextual evidence. Multiple actions may share a message anchor without an inferred within-message order. A retail case study produces a versioned 24-entry code...
  </details>

- **2026-09-21** — Ningyuan Deng, Jinyuan Wang, Qi Li et al. — [FinRankGRPO: Optimizing LLMs for Listwise Financial Asset Ranking via Group Relative Policy Optimization](http://arxiv.org/abs/2609.24175v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) excel at understanding unstructured financial contexts, their direct use in portfolio optimization is limited by a mismatch between next-token prediction and the listwise ranking objectives required for asset allocation. They also struggle with precise numerical forecasting, leading to instability and arithmetic hallucinations. To bridge this gap, we propose FinRankGRPO, a framework that shifts LLM based portfolio construction from direct numerical prediction t...
  </details>

- **2026-09-21** — Cong Li, Cheng Chen, Thomas Fung et al. — [Mind or Message? Auditing Theory of Mind in Multi-Agent Social Simulation](http://arxiv.org/abs/2609.24146v1)
  <details><summary>📄 Abstract</summary>
  Language model agents are increasingly used to simulate social interaction, and the resulting transcripts read as though the agents understand one another. We ask whether that appearance rests on a model of the partner's mind or on the surface record of what the partner said. We build a social simulation in which both questions have exact answers: 40 multi-issue negotiations whose hidden preference weights and whose full Pareto frontier are known by construction. Two model families negotiate acr...
  </details>

- **2026-09-21** — You Liu, Yue Liu, Quanchao Lu et al. — [OSCAR: Order-aware Scoring and Calibration for AI Rankings](http://arxiv.org/abs/2609.24128v1)
  <details><summary>📄 Abstract</summary>
  Judge-specific sensitivity is useful for aggregating pairwise LLM evaluations, but its interpretation depends on which systematic presentation effects the ranking model includes. We introduce OSCAR, an order-aware framework for scoring and calibrating AI rankings, and study position as one such effect. In released judgments from 18 evaluators, the all-response A-minus-B score difference ranges from $-63.11$ to $98.31$ percentage points. Matching question text, response texts, candidate identitie...
  </details>

- **2026-09-21** — Yu-Ho Chang, Chi-Hsi Kung, Yi-Hsuan Tsai et al. — [Action-Slot: Structured Action-Centric Representation Learning for Multi-Agent Atomic Activity Understanding](http://arxiv.org/abs/2609.24127v1)
  <details><summary>📄 Abstract</summary>
  Atomic activity understanding aims to recognize and localize structured traffic behaviors that jointly encode motion patterns and their grounding in road topology. Unlike conventional action recognition, atomic activities are multi-agent, multi-label, and topology-aware: multiple activities co-occur while many agents remain inactive. We introduce Action-Slot, a structured action-centric representation learning framework. Slot attention is widely used for object-centric decomposition, but its per...
  </details>

- **2026-09-21** — Kunpeng Yang — [A Task-Oriented Multi-Agent Framework for Complex Wearable Health Analysis](http://arxiv.org/abs/2609.24107v1)
  <details><summary>📄 Abstract</summary>
  Wearable health questions often combine data retrieval, longitudinal analysis, and health advice over structured records. Prompting a single large language model with a complete record and a composite query obscures whether every request is executed and which evidence supports the answer. We propose a task-oriented multi-agent framework that represents a composite query as distinct intents and typed tasks with explicit intra-intent dependencies. Specialized agents execute retrieval, analysis, an...
  </details>

- **2026-09-21** — Cheng Li, Jiexiong Liu, Yixuan Chen et al. — [Incremental Consistency Execution for Autonomous Intelligent Systems](http://arxiv.org/abs/2609.24090v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon autonomous intelligent systems rely on heterogeneous components such as large language models, databases, external APIs, and rule engines, while their external states continuously change during execution. Re-executing the entire workflow after every change introduces substantial redundant computation. This paper proposes an incremental consistency execution method based on task fact contracts, field-level dependency masks, and state perturbation result invariant domains. After an in...
  </details>

- **2026-09-21** — Xingsong Ye, Yongkun Du, Jiaxin Zhang et al. — [All-in-One Multilingual Scene Text Recognition with Script-aware Mixture-of-Experts](http://arxiv.org/abs/2609.24058v1)
  <details><summary>📄 Abstract</summary>
  Multilingual scene text recognition (STR) remains challenging due to the scarcity of training data for most languages and the difficulty of serving diverse scripts within a single model. Existing solutions either deploy one recognizer per language, inflating cost and introducing error accumulation, or rely on massive vision-language models (VLMs) that are expensive and still inaccurate on many scripts. In this work, we pursue an all-in-one multilingual recognizer that is simpler than per-languag...
  </details>

- **2026-09-21** — Minda Zhao, Fangyu Hu, Yan Luo et al. — [Representation-guided in-context learning for medical image interpretation with multimodal large language models](http://arxiv.org/abs/2609.24057v1)
  <details><summary>📄 Abstract</summary>
  Medical image interpretation is central to diagnosis and care, yet adapting general-purpose multimodal large language models (MLLMs) often requires resource-intensive domain-specific fine-tuning. Here we introduce representation-guided in-context learning (RG-ICL), a training-free inference framework that retrieves query-aligned demonstrations using frozen encoders, without task-specific parameter updates. Across eight datasets spanning histopathology, radiology and retinal fundoscopy, RG-ICL im...
  </details>

- **2026-09-21** — Boxun Hu, Jiawei Ge, Axel Krieger et al. — [LEAP-NBV: Lightweight Edge Active-Perception for Foundation-Model Next-Best-View Planning](http://arxiv.org/abs/2609.23974v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are endowing autonomous systems with greater intelligence, enabling a more comprehensive understanding of the environment through visual perception. A representative example is Human Mesh Recovery (HMR), which provides useful estimates of a target's 3D pose and shape that can benefit tactical missions. However, the size and power demands of such models make them difficult to run on edge platforms and limit their real-time performance, undermining the requirements of tactical ed...
  </details>

- **2026-09-21** — Mai Mohamed Eida, Gunjan Anand, Ayush Singh et al. — [From Tables to Quantified Statements: Evaluating LLM Inference Generation through Executable Verification](http://arxiv.org/abs/2609.23966v1)
  <details><summary>📄 Abstract</summary>
  LLMs can generate fluent descriptions from tables, but their outputs may remain logically unsupported by the structured data. We introduce STAT-TO-TEXT, a controlled task in which LLMs generate quantified natural language inferences from statistical tables using quantified constructions such as all, some, no, and most. To evaluate these inferences, we use an LLM generated Python checker code which when executed verifies the corresponding truth conditions against the table. We compare four open-w...
  </details>

- **2026-09-21** — Haoxuan Li, Sixu Yan, Lianghui Zhu et al. — [Bridge3D: Enabling Vision-Language-Action Models to See and Act in 3D](http://arxiv.org/abs/2609.24525v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have demonstrated remarkable generalization in robotic manipulation via large-scale multimodal pretraining. However, VLA models are mainly trained on 2D-centric observations, which inherently constrains their capacity for precise spatial manipulation. Previous methods enhance 3D awareness by introducing implicit spatial priors, but still lack explicit geometry guidance. In this paper, we propose Bridge3D that integrates both implicit and explicit 3D geometry g...
  </details>

- **2026-09-21** — Akhil Sharma, Jatin Gupta, Ali Imam Abidi — [Taramandal-GPT: Enhancing Astrodynamics Problem-Solving with Knowledge Retrieval and Structured Thinking](http://arxiv.org/abs/2609.24246v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown remarkable progress in natural language understanding, yet their effectiveness in specialized fields like astronomy and astrodynamics remains limited due to challenges in multi-step reasoning, symbolic manipulation, and domain-specific terminology. To address this, we present Taramandal-GPT (Constellation-GPT), a domain-adapted framework built on the Qwen3-8b backbone, enhanced with a Retrieval-Augmented Generation (RAG) pipeline and a fallback mechanism f...
  </details>

- **2026-09-21** — MD. Nafis Kamal, Mahadi Hasan Fahim, Talha Ridwan et al. — [Efficient LLM Distillation for Bangladesh Legal Context: A Smartphone-Compatible Retrieval-Augmented Generation Model](http://arxiv.org/abs/2609.24177v1)
  <details><summary>📄 Abstract</summary>
  Legal information in Bangladesh is inaccessible to most citizens. Statutory text is English-only, trained lawyers are concentrated in urban centres, and cloud-dependent AI fails where mobile connectivity is unreliable, a setting in which hallucinated legal text causes direct harm. The system addresses statutory interpretation only; queries that require judicial precedent or case-law reasoning fall outside its scope. We target the statutory access gap by compressing a 9-billion-parameter Gemma-2 ...
  </details>

- **2026-09-21** — Wenbo Zhang, Kaixuan Wang, Yutao Ouyang et al. — [An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond](http://arxiv.org/abs/2609.24170v1)
  <details><summary>📄 Abstract</summary>
  Embodied AI systems are often organized into System 1 and System 2. System 1 is typically a pretrained policy that generates actions at high frequency, whereas System 2 is often instantiated as a vision-enabled language model for high-level planning. We ask whether a large language model (LLM) can act as the policy for robot manipulation without task-specific finetuning. We call this setting LLM as policy. We evaluate three LLMs on all 42 RoboDojo tasks and compare their scores with 40 public po...
  </details>

- **2026-09-21** — Guoliang Li, Peiyao Zhou, Xuanhe Zhou et al. — [Data Agents: Agentic Data Systems](http://arxiv.org/abs/2609.24137v1)
  <details><summary>📄 Abstract</summary>
  Traditional data systems face profound limitations in the AI era, relying on human-crafted pipelines, lacking semantic understanding of heterogeneous data, and operating through rigid, reactive processing. To address these challenges, we propose a new paradigm called the Data Agent, designed to manage, process, and analyze data with minimal human intervention. Data agents autonomously execute a wide range of data-related tasks, transforming traditional data systems by shifting from manual design...
  </details>

- **2026-09-21** — Dorian Benhamou Goldfajn, Mason Nakamura, Saaduddin Mahmud et al. — [RoboTalk: Learning Multi-Robot Communication and Coordination from Multimodal Demonstrations](http://arxiv.org/abs/2609.23997v1)
  <details><summary>📄 Abstract</summary>
  Multi-robot collaboration could enable more efficient and scalable solutions to complex robotic tasks, but collaboration under partial observability remains challenging. Natural-language communication offers a promising approach to coordinating robots under partial observability. However, in decentralized manipulation, jointly learning explicit inter-robot communication and skill-level action selection from multimodal demonstrations remains underexplored for small vision-language models (VLMs) i...
  </details>

- **2026-09-21** — Thomas Erben — [Natural coordinates for constrained correlation functions: Partial autocorrelations and the geometry of positive power spectra](http://arxiv.org/abs/2609.24500v1)
  <details><summary>📄 Abstract</summary>
  Two-point correlation functions are a standard summary statistic in cosmic shear and large-scale-structure analyses. Their values are, however, constrained: non-negativity of the underlying power spectrum restricts any admissible sequence of correlation coefficients $(r_1,\ldots,r_N)$ to a bounded convex region, described in the one-dimensional case by the recursive interval geometry of Schneider & Hartlap (2009). Their formalism introduces an affine variable $x_n$ that maps the admissible inter...
  </details>

- **2026-09-21** — Guangchuan Lv, Dianxing Shi, Dingjie FU — [VPRune: Efficient Training-free Pre-LLM Visual Token Pruning](http://arxiv.org/abs/2609.24485v1)
  <details><summary>📄 Abstract</summary>
  Visual token pruning is a promising approach to reducing the inference cost of large vision-language models (LVLMs), yet aggressive token reduction often causes substantial performance degradation. We identify three key factors behind this degradation: text-guided selection bias, information loss from discarded tokens, and positional distortion caused by sequence compaction. Based on these observations, we propose \textbf{VPRune}, a training-free pre-LLM pruning framework consisting of visual-on...
  </details>

- **2026-09-21** — Yuhan Zhu, Jilin Hu, Xinying Cai et al. — [WPBench: A Comprehensive Benchmark for Wind Power Forecasting](http://arxiv.org/abs/2609.24444v1)
  <details><summary>📄 Abstract</summary>
  Accurate, reliable, and deployable wind power forecasting is critical for power system dispatch, renewable energy integration, and electricity market operations. Progress in this field hinges on the ability to empirically and comprehensively benchmark forecasting methods. Yet existing benchmarks fall short of supporting systematic evaluation in four key aspects: 1) limited coverage of wind power scenarios across turbine scale, variable composition, and spatial structure; 2) incomplete coverage o...
  </details>

- **2026-09-21** — Ali A. Safieh, Ibrahim Abu Alhaol, Rawan Ghnemat — [End-to-end Jordanian dialect speech-to-text self-supervised learning framework](http://arxiv.org/abs/2609.24410v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-text engines are extremely needed nowadays for different applications, representing an essential enabler in human-robot interaction. Still, some languages suffer from the lack of labeled speech data, especially in the Arabic dialects or any low-resource languages. The need for a self-supervised training process and self-training using noisy training is proven to be one of the up-and-coming feasible solutions. This article proposes an end-to-end, transformers-based model with a framewor...
  </details>

- **2026-09-21** — Mazdak Fatahi, Šárka Pryjmaková, Pierre Boulet et al. — [Can Spiking Neural Networks play pinball? A neuromorphic motion detector for target tracking](http://arxiv.org/abs/2609.24403v1)
  <details><summary>📄 Abstract</summary>
  Biological visual systems achieve continuous, low-latency motion perception by processing sparse, asynchronous spiking signals, enabling real-time tracking under strict energy constraints. Event-based cameras, inspired by the mammalian retina, replicate this efficiency by capturing only local brightness changes as asynchronous events, offering a natural substrate for spiking neural networks (SNNs) to parallelise computation and adapt to fast-changing scenes. Pinball provides a controlled yet dyn...
  </details>

- **2026-09-21** — Gautam Ranka, Shubham Santosh Pandere, Aiden Dsouza — [Topographic Training Concentrates Causal Circuits Without Improving Neuron Monosemanticity](http://arxiv.org/abs/2609.24379v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability of vision transformers seeks to decompose model computation into human-readable units, but learned representations entangle many concepts in each neuron. Feature superposition is widely treated as the central obstacle to this decomposition, yet most mitigations (sparse autoencoders, dictionary learning) are post-hoc and leave the underlying network unchanged. We ask whether a spatial-locality training loss (TopoLoss) can act as a lightweight, training-time prior that...
  </details>

- **2026-09-21** — Senlei Zhang, Linhao Luo, Qian-Wen Zhang et al. — [LADDER: Graph-Guided Diffusion Language Models for Efficient Multi-Hop Reasoning](http://arxiv.org/abs/2609.24346v1)
  <details><summary>📄 Abstract</summary>
  Graph Retrieval-Augmented Generation (GraphRAG) has remarkably enhanced large language models on complex reasoning by leveraging structured entity topologies. However, existing frameworks heavily rely on standard autoregressive language models where the nature of inherent sequential generation severely hinders overall inference efficiency. Inspired by Diffusion Language Models (DLMs) that offer massive parallelism via continuous refine-in-parallel decoding, we aim to accelerate GraphRAG in the d...
  </details>

- **2026-09-21** — Lu Zhang, Rachik Soualah, Abbes Amira — [Multitask Jet Analysis with Vision-Language Models: A Physics-Informed Four-Panel Representation](http://arxiv.org/abs/2609.24334v1)
  <details><summary>📄 Abstract</summary>
  The enormous recorded data at high-energy physics (HEP) colliders make the accurate identification of physics objects a bottleneck in disentangling event topologies, where machine learning has become a standard tool for jet tagging. In this work, we examine whether Vision-Language Models (VLMs) can provide a common interface for structured jet analysis from a single physics-informed image. Each JetClass jet becomes a 224x224 RGB image with four panels encoding p_T flow of all constituents; charg...
  </details>

- **2026-09-21** — Wen-Jia Wang, Meng-Lin Du, Feng-Kun Guo et al. — [Deciphering the production mechanism of the LHCb $P_c$ states](http://arxiv.org/abs/2609.24231v1)
  <details><summary>📄 Abstract</summary>
  The three narrow pentaquarks $P_c(4312)$, $P_c(4440)$, and $P_c(4457)$ observed by LHCb are widely interpreted as hadronic molecules owing to their proximity to the $Σ_c\bar{D}^{(*)}$ thresholds. However, heavy-quark spin symmetry predicts additional partner states that have not been seen experimentally, making the production mechanism in $Λ_b^0$ decays particularly important in understanding their nature. We propose a novel production mechanism, which can naturally explain why only these three ...
  </details>

- **2026-09-21** — Yutong Chen, Zhike Tang, Zhihao Mai et al. — [WidgetVA: A Widget-Centric Framework and Benchmark for Agentic Visual Analytics](http://arxiv.org/abs/2609.24094v1)
  <details><summary>📄 Abstract</summary>
  Visual analytics (VA) enables sensemaking through interactive visualization, but effective analysis often requires experts to translate high-level intents into long sequences of interface operations and iteratively interpret visual feedback. We study whether modern vision-language models (VLMs) can take on this role as autonomous VA operators that observe the interface, plan multi-step exploration, execute interactions, and adapt based on intermediate visual feedback. To support systematic devel...
  </details>

- **2026-09-21** — Amir Rafe, Subasish Das — [Calibrated Decisions at Scale: Converting Police Crash Narratives into Probabilistic Crash Variables with a System One Model (Jev)](http://arxiv.org/abs/2609.24052v1)
  <details><summary>📄 Abstract</summary>
  Crash datasets that carry an investigator narrative hold information the coded fields omit. Coding those narratives at scale has been blocked by three obstacles. Frontier large language models are costly at that scale, their generated text cannot be verified, and no rule says how much output a human must check. This paper formulates narrative coding as gated, typed decisions answered by Jev, a System One model that returns probabilities over analyst-defined options and generates no text. A scree...
  </details>

- **2026-09-21** — Haixin Wang, Xiaoxuan Wang, Junkai Zhang et al. — [ACLArena: Agent Continue Learning in Multi-stage Post-training](http://arxiv.org/abs/2609.23989v1)
  <details><summary>📄 Abstract</summary>
  Building general-purpose agents for industrial deployment requires integrating multiple capabilities, each typically acquired at a distinct stage of training. Yet there is currently no well-established recipe for Agent Continual Learning (ACL), with little understanding of the trade-offs among existing integration paradigms. To address this gap, we introduce ACLArena, a framework for comprehensively studying, analyzing, and evaluating ACL. We first build a sequential training pipeline and conduc...
  </details>

- **2026-09-21** — Shijie Jin, Lu Liu — [Decoupling the Magnetic Field Operator as an Independent Operator Class in Stochastic Series Expansion Quantum Monte Carlo](http://arxiv.org/abs/2609.23978v1)
  <details><summary>📄 Abstract</summary>
  The Stochastic Series Expansion (SSE) quantum Monte Carlo method with loop updates is among the most powerful approaches for quantum spin and boson systems. In the standard formulation, the magnetic field term is routinely absorbed into the Heisenberg interactions---a strategy that has proven highly efficient across a wide range of field strengths. In this work, we propose a more general SSE framework in which the magnetic field operator is treated as an independent operator class, enabling it t...
  </details>

- **2026-09-21** — Mai Mohamed Eida, Ryan Dolan, Paul de Nijs et al. — [Some Dialects Are More Equal Than Others: Non-Prestigious Arabic Dialectal Bias in LLMs](http://arxiv.org/abs/2609.23955v1)
  <details><summary>📄 Abstract</summary>
  Previous work on Egyptian Arabic in NLP has focused largely on the prestigious Cairene Egyptian Arabic (CEA) dialect, resulting in a lack of representation for the less prestigious Sa'idi Egyptian Arabic (SEA) dialect both in LLM and resource development. Does this lack of representation influence an LLM's view of the acceptability of SEA (upstream), and does an upstream bias against SEA lead to worse performance (downstream)? We investigate the upstream effect of SEA dialectal features on LLM p...
  </details>

- **2026-09-20** — Xubin Yue, Zhenhua Xu, Zhebo Wang et al. — [TTS-Guard: Black-Box Ownership Verification of Text-to-Speech Models via Adaptive Adversarial Speaker-Pair Fingerprints](http://arxiv.org/abs/2609.23729v1)
  <details><summary>📄 Abstract</summary>
  The rapid maturation of zero-shot Text-to-Speech (TTS) models has turned high-quality voice cloning into a widely available capability, raising acute concerns over unauthorised replication, fine-tuning and resale of proprietary speech models. Yet ownership verification for TTS remains largely open: speech is a continuous waveform whose perturbations are easily destroyed by routine signal processing, and the human auditory system imposes a much tighter perceptual budget than vision. We present \t...
  </details>

- **2026-09-20** — Tianqi Chen, Jingxiao Long — [Randomized Online Fair Division: High-Probability and Expected Realized Fairness](http://arxiv.org/abs/2609.23577v1)
  <details><summary>📄 Abstract</summary>
  We study randomized algorithms for the fully online allocation of indivisible goods among $n\ge2$ agents with nonnegative additive valuations. Goods arrive one by one and must be allocated immediately and irrevocably. Nothing is known in advance except the number of agents. Since exact ex-ante envy freeness and proportionality are readily achievable, while no positive ex-post approximation is possible for the fairness notions considered here, we study the intermediate notions of high-probability...
  </details>

- **2026-09-20** — Anandsingh Chauhan, Kunal Garg — [BarrierFormer: Transformer-Guided Predictive Barrier Enforcement for Safe Robot Control](http://arxiv.org/abs/2609.23896v1)
  <details><summary>📄 Abstract</summary>
  Control barrier functions (CBFs) have become one of the most popular tools for encoding and enforcing state constraints in safety-critical robotics. Standard CBF approaches are inherently myopic in nature as they enforce safety only at the current time step. Consequently, the system can be driven toward the boundary of the safe set where no feasible safe control exists at a future timestep. Model predictive control (MPC) based approaches address this by enforcing state constraints over a recedin...
  </details>

- **2026-09-20** — Dengyi Zhao, Zhiheng Zhou, Mengyao Zhou et al. — [Edge-centric Brain Transformer: An Edge-centric Functional Connectivity Learning Framework for fMRI-based Brain Disorder Diagnosis](http://arxiv.org/abs/2609.23782v1)
  <details><summary>📄 Abstract</summary>
  Resting-state functional magnetic resonance imaging (rs-fMRI) enables the characterization of functional interactions among distributed brain regions and has shown promise for brain disorder diagnosis. However, existing deep learning methods predominantly rely on node-centric representations, where brain regions serve as the primary learning units, potentially overlooking discriminative alterations embedded in functional connections. Here, we propose an edge-centric brain transformer (EBT) frame...
  </details>

- **2026-09-20** — Kunyang Lin, Xutao Wen, Jingxi Lin et al. — [EgoWild2Dex: Learning Dexterous Robotic Manipulation from In-the-Wild Human Experience](http://arxiv.org/abs/2609.23755v1)
  <details><summary>📄 Abstract</summary>
  Egocentric human data provide a principled source of supervision for learning dexterous robot manipulation. Unlike prior approaches that often collect such data in constrained or specially constructed environments, we collect in-the-wild egocentric demonstrations in real-world settings, including homes, factories, and pharmacies, etc., where people perform their ordinary tasks while wearing head-mounted cameras. This collection protocol captures diverse workflows and hand-object interactions acr...
  </details>

- **2026-09-20** — Kemal Kirtac — [Financial Language Models as Applied Artificial Intelligence Systems for News-Based Trading under Market Frictions](http://arxiv.org/abs/2609.23703v1)
  <details><summary>📄 Abstract</summary>
  Financial language models can transform unstructured firm-specific news into structured decision signals, but financial AI research lacks an integrated deployment framework for evaluating whether those signals remain useful in financial decision systems. Computer science research has developed strong methods for time-series forecasting, text classification, multimodal stock prediction, graph-based market modeling, and machine-learning operations, yet these streams do not provide a domain-specifi...
  </details>

- **2026-09-20** — Haoyue Liu, Ye Chen, Zhichao Wang et al. — [Which Constraints Are Missing? Ask the Verifier: Graded Rewards for Constraint-Following Music Generation](http://arxiv.org/abs/2609.23665v1)
  <details><summary>📄 Abstract</summary>
  Constraint-following music generation asks a score to satisfy several user-specified properties at once, each checkable programmatically (key, meter, length, range, final note, rhythm, motion and form), yet no existing benchmark isolates this capability. We construct MusicConstraintBench, 2,180 items over eight constraint families, on which current models fail once a few constraints are combined. The natural remedy is reinforcement learning with these verifiers as reward, yet we observe that a r...
  </details>

- **2026-09-20** — Kiran Naseer, Samreen Azhar, Dwarikanath Mahapatra — [Reassessing Global Gradient-Norm Imbalance in BLIP Fine-Tuning Across Physical Domains](http://arxiv.org/abs/2609.23655v1)
  <details><summary>📄 Abstract</summary>
  Imbalanced gradient magnitudes between the visual and language pathways of a vision-language model are often treated as a defect to be corrected. We test that premise for one family of correction, deliberately excluding adaptive, signal-driven schemes (e.g. BalGrad, OGM, PMR, CGGM), which are a mechanistically distinct class outside this study's scope. Measuring the language-to-visual gradient-norm ratio, reported in parameter-normalised form, across nine fine-tuning conditions, three seeds, and...
  </details>

- **2026-09-20** — Jiaheng Dong, Xiaofeng Yu, Jean Honorio et al. — [Listen Then Reason: Perception-Grounded Test-Time Reinforcement Learning for Large Audio-Language Models](http://arxiv.org/abs/2609.23589v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) are increasingly used for a broader range of audio reasoning tasks. These models typically incorporate audio representations into a large language model (LLM) backbone to enable multimodal reasoning. Recent test-time reinforcement learning (TTRL) methods further improve LLM reasoning capability by leveraging unlabelled test data after pre-training. However, the importance of the perceptual capability of LALMs remains underexplored, particularly how much acoust...
  </details>

- **2026-09-20** — Liyang Fan, Yingcheng Shi, Yongbin Li et al. — [VibeMemBench: Evaluating Memory Systems for Coding Agents on Real Repository Coding Tasks](http://arxiv.org/abs/2609.23570v1)
  <details><summary>📄 Abstract</summary>
  Coding agents operate on real repository coding tasks, and persistent memory systems promise to reuse experience across tasks. Yet existing evaluations do not show whether those systems improve executable repository work. Repository benchmarks test code changes but do not isolate memory, while memory benchmarks score recall without measuring downstream coding outcomes. We introduce VibeMemBench, a benchmark for evaluating memory systems on 111 coding targets from 90 SWE-rebench V2 repositories a...
  </details>

- **2026-09-20** — Peng Kuang, Yuchun Fan, Jiangnan Li et al. — [BabelArena: A Large-Scale Multilingual Benchmark for LLM Agents](http://arxiv.org/abs/2609.23490v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly execute multi-step workflows through tool use and interaction with users and environments. However, current agent evaluations are largely English-centric, limiting our understanding of agent capabilities in multilingual settings. We introduce BabelFlow, a benchmark-general agentic workflow that adapts existing agent benchmarks to new languages by analyzing runtime dependencies, coordinating structure-preserving translation, and combining multi-layer...
  </details>

- **2026-09-20** — Jie Ying, Zhefan Wang, Zihong Chen et al. — [Tool-Augmented On-Policy Distillation for LLM Domain Adaptation in Sequence-Based Omics Tasks](http://arxiv.org/abs/2609.23435v1)
  <details><summary>📄 Abstract</summary>
  Multi-omics sequences contain complex biological patterns, yet deciphering their mechanisms for automated scientific discovery remains challenging. As large language models (LLMs) interpret these sequences, evaluating both predictions and scientific reasoning is critical. However, existing benchmarks for multi-omics sequence tasks rely on classification and regression metrics, neglecting whether models grasp the underlying biological evidence. We introduce OmicsBench, the first reasoning benchma...
  </details>

- **2026-09-20** — Haoyang Wu, Abhinav Kumar, Dmitry Berenson — [Topology-Informed Visual Prompting For Vision Language Action Policies](http://arxiv.org/abs/2609.23944v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) policies can struggle with manipulation tasks with complex obstacle geometries due to partial observability. These complex geometries can lead to similar visual observations or robot configurations requiring qualitatively different actions, a distinction that can be quantified using topological signatures. While motion planners with full knowledge of environment geometries and object states can reason about these signatures in planning, this information is often not ...
  </details>

- **2026-09-20** — Rhea Huang, David L. Matlock, Laurence Reich — [HumynexSurg-1: A Curated Expert Liposuction Dataset](http://arxiv.org/abs/2609.23885v1)
  <details><summary>📄 Abstract</summary>
  Robot foundation models learn manipulation from large demonstration corpora, but surgery is missing from those corpora: across the 780-hour Open-H surgical collection, one dataset carries synchronized force and none covers an aesthetic procedure. Liposuction is the hard case, because the instrument works under the skin and the surgeon operates by feel and by judgment. Humynex Robotics builds curated expert datasets for this kind of procedure. HumynexSurg-1 is the first release: a master liposuct...
  </details>

- **2026-09-20** — Gehao Zhang, Weikai Huang, Shailesh Shailesh et al. — [Grounded Action Model: 3D Grounding as a Foundation for Robotics](http://arxiv.org/abs/2609.23863v1)
  <details><summary>📄 Abstract</summary>
  Manipulation policies must know which objects matter and where they are, yet the pretrained backbones that current robot foundation models build on, from language in vision-language-action models (VLAs) to video generation in world-action models (WAMs), do not directly require this metric grounding, leaving it to be learned implicitly from robot demonstrations. We propose Grounded Action Models (GAMs), a new paradigm of robot foundation models built with 3D grounding. GAM can be conditioned usin...
  </details>

- **2026-09-20** — Chifang Chou, Sam Yu-Te Lee, Rudrajit Choudhuri et al. — [Vibe-GUIDE: A Graph-based User Interface in IDEs for Oversight in Vibe Coding](http://arxiv.org/abs/2609.23859v1)
  <details><summary>📄 Abstract</summary>
  In agentic coding, developers shift from implementing changes themselves to specifying intent, evaluating the agent's work, and making approval decisions. However, delegating implementation can introduce cognitive debt that erodes project comprehension over time, constraining developers' ability to provide oversight. In this work, we investigate the role of persistent shared representations in supporting project comprehension and oversight of coding agents. We present Vibe-GUIDE, an agentic codi...
  </details>

- **2026-09-20** — Yicheng Jiang, Zesen Gan, Xiaobo Wang et al. — [AR-WAM: A Visual-Conditioned Agent-Ready World Action Model for Robotic Manipulation](http://arxiv.org/abs/2609.23578v1)
  <details><summary>📄 Abstract</summary>
  As AI agents become increasingly capable, agent-driven robotic control is emerging as a compelling paradigm. However, prevailing vision-language-action (VLA) models and world action models (WAMs) still rely on natural-language instructions to specify manipulation tasks, an ill-suited interface for agent-driven control: referentially ambiguous, spatially imprecise, redundant with the agent's inherent language understanding, and entangling intent with execution. We present AR-WAM, a visual-conditi...
  </details>

- **2026-09-20** — Yuning Su, Borui Li, Yonghao Shi et al. — [HEARTH: An Object-Centric RGB-Thermal-3D Dataset for Temperature-Aware Robot Manipulation](http://arxiv.org/abs/2609.23418v1)
  <details><summary>📄 Abstract</summary>
  Language-guided manipulation can depend on physical properties that visible appearance does not reveal. Temperature is one such property, but object datasets for robot learning rarely associate measured temperatures with object appearance and geometry. We present HEARTH, an object-centric RGB-thermal-3D dataset of 90 physical objects from 18 everyday categories, comprising 145 captured object states. Our pipeline maps apparent surface temperatures onto reconstructed meshes through camera calibra...
  </details>

- **2026-09-20** — Bakar Chargeishvili — [LLM-Based FORM Code Generation with Verification-Driven Fine-Tuning](http://arxiv.org/abs/2609.23367v1)
  <details><summary>📄 Abstract</summary>
  FORM is a domain-specific symbolic manipulation language widely used in particle physics for processing the very large algebraic expressions arising from multi-loop Feynman diagram calculations. Despite its central role in precision theoretical physics, no artificial-intelligence tooling exists, to our knowledge, for assisting physicists in writing FORM code. We show that contemporary large language models (LLMs), including frontier models with hundreds of billions of parameters, achieve a zero-...
  </details>

- **2026-09-20** — Shaohu Wang, Aiguo Song, Yulong Yuan et al. — [Manipulation Feasible Navigation Among Movable Obstacles with Discrete Contact Pushing](http://arxiv.org/abs/2609.23312v1)
  <details><summary>📄 Abstract</summary>
  In environments with large movable obstacles, detour-only navigation can be inefficient or even infeasible, while obstacle interaction requires reasoning about navigation benefit, feasible placement, and executable manipulation. We present a hierarchical navigation among movable obstacles (NAMO) framework for mobile manipulators. At the high level, the planner identifies key blocking obstacles from reference paths and searches for relocation plans that jointly satisfy geometric, manipulation, an...
  </details>

- **2026-09-20** — Xuening Wu — [When Does Communication Help? Beyond Spectral Descriptions of Collective Intelligence](http://arxiv.org/abs/2609.23310v1)
  <details><summary>📄 Abstract</summary>
  Communication can bring agents into agreement while making their decisions worse. We identify two limits of aggregate descriptions of communication gain in distributed inference. First, stable linear systems with fixed evidence, network and readout can have interaction and finite-time state operators with identical eigenvalue and singular-value spectra, yet produce gains of opposite sign. Changing only message orientation raises accuracy from 72.6% to 91.2% or lowers it to 65.9%. A standard task...
  </details>

- **2026-09-20** — Md Sayed Tanveer, Mohammed A. Mostajo-Radji, Ge Wang — [A discrete generative model of neuronal spiking activity on microelectrode arrays](http://arxiv.org/abs/2609.23907v1)
  <details><summary>📄 Abstract</summary>
  Generative models of neural activity could help characterize tissue dynamics, compare experimental conditions, and simulate population activity for applications ranging from disease and drug-response studies to closed-loop experimentation. Existing approaches, however, typically assume a fixed set of sorted neurons, whereas high-density microelectrode arrays produce extremely sparse, array-wide binary spike volumes in which the observed subset of electrodes varies across assays. We introduce a d...
  </details>

- **2026-09-20** — Zhiyuan Ma — [GDN Tree-Scan: Served Tree Verification for Recurrent-Hybrid Language Models](http://arxiv.org/abs/2609.23900v1)
  <details><summary>📄 Abstract</summary>
  Tree speculative decoding verifies multiple candidate continuations in one target forward pass. For attention-only transformers, the verifier mainly needs an ancestry mask. Recurrent-hybrid language models break this assumption: a candidate row must also carry the recurrent state that native sequential decode would have produced along its root-to-node path. Otherwise, a verifier can use a correct attention mask while still conditioning on an impossible recurrent history.   We present GDN Tree-Sc...
  </details>

- **2026-09-20** — Dale S. Kim — [A Stochastic EM Algorithm with Sampling-Importance Resampling for Missing Data in Regression with Nonlinear Predictors](http://arxiv.org/abs/2609.23747v1)
  <details><summary>📄 Abstract</summary>
  Estimating regression models with nonlinear predictor transformations is challenging when data are missing, because nonlinearity typically renders the conditional distribution of the missing values intractable. Previous methods require specific nonlinear forms, such as polynomials or interactions, or rely on approximations that can induce bias. We propose a stochastic EM algorithm that uses sampling-importance resampling (SIR-StEM) to handle missing data under arbitrary nonlinear transformations...
  </details>

- **2026-09-20** — Girish A. Koushik, Swapnil Bhosale, Samarth Agrawal et al. — [Beyond Relevance: Structured Semantic Supervision for Product Search with LLM-Augmented Annotations](http://arxiv.org/abs/2609.23646v1)
  <details><summary>📄 Abstract</summary>
  E-commerce search requires distinguishing products that are merely related to a query from those that directly satisfy the user's shopping intent. We augment query-product pairs with structured LLM-generated query and product attributes and human-validated relevance, explanations, and centrality judgments, and evaluate these signals using a simple dual-encoder retriever and MLP re-ranker. On an augmented subset of ESCI, a human-feature oracle reaches $0.9382$ nDCG@10, while a human-free trained ...
  </details>

- **2026-09-20** — Jintao Wu, Yiran Shan, Rui Zhang — [Uni-Macro-FRPN: Full-Resolution and Cross-Scale Learning for Polymers](http://arxiv.org/abs/2609.23611v1)
  <details><summary>📄 Abstract</summary>
  Polymer properties emerge from interactions across scales, yet existing polymer models typically preserve either detailed monomer chemistry without an explicit polymer graph or polymer connectivity with simplified monomer representations, due to computational constraints, as polymers typically contain tens of thousands of atoms. We present Uni-Macro-FRPN (FRPN), a Full-Resolution Polymer Network that retains both detailed atom-level and monomer-level features and explicit polymer structure infor...
  </details>

- **2026-09-20** — Weihan Cai, Hao Tan, Xinping Gao et al. — [PETR: Prompt Ensembling with Training-free Routing for Vision-Language Models](http://arxiv.org/abs/2609.23600v1)
  <details><summary>📄 Abstract</summary>
  Prompt learning efficiently adapts vision-language models (VLMs) to downstream tasks, but gains on seen classes often come at the expense of generalization to unseen classes. To address this limitation, we propose prompt ensembling with training-free routing (PETR), whose key innovation is a carefully designed dual-prompt architecture: two complementary prompts are learned from different data and objectives to emphasize seen class discrimination and unseen-class generalization, respectively. Dur...
  </details>

- **2026-09-20** — Antonio Nappa — [Endogenous Interpretation](http://arxiv.org/abs/2609.23514v1)
  <details><summary>📄 Abstract</summary>
  We propose endogenous interpretation: program, interpreter, machine, and derived execution language are not disjoint semantic objects but different parameterizations of one executable state-transition relation. Each realization carries an implicit constraint bias, the structural restrictions imposed by its instruction basis, state encoding, control transfers, and finite substrate. From this viewpoint the "semantic gap" metaphor is misleading for operational semantics: a semantics-preserving tran...
  </details>

- **2026-09-20** — Md. Ashraful Babu — [AgentBetta: Verification-Driven Adaptive Configuration of an AI Nano-Agent through Selective Expansion and Verified Contraction](http://arxiv.org/abs/2609.23512v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents are typically deployed with predefined configurations, although the required model capability, context, tools, permissions, memory, and computational resources can vary substantially across tasks. This study develops and evaluates AgentBetta, an adaptive AI Nano-Agent framework that represents these factors as an executable configuration and updates them through verification-driven diagnosis, selective expansion, and verification-based counterfactual contraction. The ...
  </details>

- **2026-09-20** — Yifan Wang, Dejing Dou — [Machine-Interpretable Information: Compiling Documents into Searchable and Readable Protocol States](http://arxiv.org/abs/2609.23371v1)
  <details><summary>📄 Abstract</summary>
  Long-context language models interface with external knowledge through raw natural language. In retrieval-augmented systems, this creates a persistent index-payload schism: dense vectors enable searchable routing, but models must re-ingest lengthy text payloads for reasoning at O(N^2) attention cost. Existing compression methods further produce private states tied to specific architectures. We introduce Machine-Interpretable Information (MII), the first agent-to-agent (A2A) document-to-state pro...
  </details>

- **2026-09-20** — Bowei Wang, Zhigang Fang, Zhijie Yang et al. — [TicTacBench: Benchmarking Timing Closure Capabilities of Coding Agents](http://arxiv.org/abs/2609.23363v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models (LLMs) have led to the emergence of coding agents capable of performing complex engineering tasks, including register-transfer level (RTL) design and optimization. Existing RTL benchmarks mainly evaluate functional correctness and performance, power, and area (PPA) of the generated RTL designs, leaving agents' ability for \emph{timing closure} under-evaluated. We propose TicTacBench, a benchmark specifically designed to evaluate coding agents' capabilitie...
  </details>

- **2026-09-19** — Param Raval, Rohit Shenoy, Archana Vaidheeswaran — [Triggers and Diagnostics for LLM-Based Interpretability Failures in Active Inference Agents](http://arxiv.org/abs/2609.23215v1)
  <details><summary>📄 Abstract</summary>
  LLM explainers are increasingly attached to autonomous agents as runtime oversight, with operators reading a generated account of the agent's beliefs and actions rather than its internal state. We audit the account itself, pairing an Active Inference (AIF) agent that tracks German grid demand and adjusts generation with an LLM explainer on three backends (GPT-4o, Claude-3-Opus, Gemini), and probing the pair with three black-box triggers. Corrupting the observation stream by 600 MW per step moves...
  </details>

- **2026-09-19** — Moshiur Farazi, Bekir Ciftler, Abdulhalim Dandoush et al. — [CrowdCue: Specialist-Cue Conditioning for Vision-Language Crowd Counting](http://arxiv.org/abs/2609.23012v1)
  <details><summary>📄 Abstract</summary>
  Generative vision-language models (VLMs) offer a counting paradigm in which one model produces both a count and a natural-language account of the scene, yet their raw counting accuracy sits in the range of sub-million-parameter specialist regressors. The open question is whether auxiliary guidance from a pretrained specialist can lift them into useful territory, and through which channel that guidance is best routed. We evaluate Qwen2.5-VL-7B on four widely used crowd counting benchmarks (Shangh...
  </details>

- **2026-09-19** — Yuxi Liu, Haoyu Li, Zekun Zhang et al. — [SparkDiffusion: Mitigating the High-Sparsity Trap --- A Unified Framework for up to $265\times$ Single-GPU Acceleration of Visual Generation](http://arxiv.org/abs/2609.23153v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion transformers are expensive because attention dominates long spatiotemporal token sequences. We identify the \emph{high-sparsity trap}: at extreme attention sparsity, step-local training losses keep decreasing while terminal generation quality stagnates or degrades. The trap is one of supervision: the dominant terminal errors originate in the high-noise structure-generation stage, and terminal-aligned training corrects terminal errors that substantially extended step-local trainin...
  </details>

- **2026-09-19** — Shutong Wu, Kevin Calderone, Andy Tsen — [CraftBench-UE: Deterministic Evaluation for Coding Agents in Unreal Engine](http://arxiv.org/abs/2609.23142v1)
  <details><summary>📄 Abstract</summary>
  Building gameplay features in a game engine requires more than code, as code that compiles and runs does not necessarily implement the requested gameplay. We introduce CraftBenchUE, an evaluation harness that runs agents in an isolated Unreal Engine environment, reconstructs their saved submissions in fresh projects, and applies deterministic build, asset, and runtime checks without an LLM judge. Based on the harness, we built a benchmark consisting of 70 tasks spanning C++ source, Blueprint ass...
  </details>

- **2026-09-19** — Peteris Daugulis, Mikhail H Klin, Anita Sondore — [Comparing different approaches to the concept of determinant: the multiplicative approach is the best!](http://arxiv.org/abs/2609.23138v1)
  <details><summary>📄 Abstract</summary>
  The determinant is traditionally introduced through permutation expansions, multilinearity, or recursive expansion formulas - approaches that, while rigorous, often obscure its conceptual significance. Instead, an approach is advocated wherein the determinant is defined via its natural characterization as a multiplicatice map on matrices, reflecting its role as a structural invariant of linear transformations under composition. This perspective defers combinatorial machinery until after the core...
  </details>

- **2026-09-19** — Mohammad Salahshour — [What a collective can hold in common: a gauge framework for private representations](http://arxiv.org/abs/2609.23066v1)
  <details><summary>📄 Abstract</summary>
  Many models of collective behavior write headings, beliefs, and meanings in one experimenter-defined frame. Organisms do not live there: each represents the world in a private space, and comparison requires translation. Consensus becomes an existence problem before it becomes a dynamical one. Reciprocal pairwise translations need not compose consistently around a loop. This return transformation (the holonomy) can expose a mismatch no isolated reciprocal pair can carry. We develop a gauge-covari...
  </details>

- **2026-09-19** — Qiang Chen, Hao Guo, Huatai Zhu et al. — [FireWorldBench: Benchmarking Complex Physical World Intelligence through Coupled-Field Fire Dynamics](http://arxiv.org/abs/2609.23064v1)
  <details><summary>📄 Abstract</summary>
  Understanding the physical world requires more than object recognition, scene description, and short-term visual prediction, as real-world physical systems involve multiple continuous fields, latent causal mechanisms, partial observations, and intervention-sensitive dynamics. We propose FireWorldBench, a benchmark for evaluating complex physical world intelligence in multimodal large language models and agents through coupled-field fire dynamics. Fire provides a canonical stress-test environment...
  </details>

- **2026-09-19** — Kaixiang Yao, Xu Wang, Miao Pan et al. — [Spatial-Interactor: Learning Spatial Reasoning through Interaction with the Observable Physical World](http://arxiv.org/abs/2609.23038v1)
  <details><summary>📄 Abstract</summary>
  Spatial reasoning is essential for vision-language models (VLMs) to understand and act in the physical world. Reasoning in dynamic environments requires VLMs to perceive local state transitions caused by object motion and viewpoint changes and integrate them over long trajectories to maintain an updated spatial state, yet existing VLMs remain limited in both capabilities. Current spatial training primarily focuses on static questions about object attributes and spatial relations, providing limit...
  </details>

- **2026-09-19** — Zhenchen Tang, Bo Peng, Zichuan Wang et al. — [An Evolutionary Agentic Approach for Open-ended Image Quality Perception](http://arxiv.org/abs/2609.22942v1)
  <details><summary>📄 Abstract</summary>
  Generative models are rapidly expanding image quality assessment (IQA) beyond traditional fidelity factors to emerging dimensions such as physical plausibility and text-rendering correctness. However, existing IQA models rely on fixed definitions and heavy supervision, making them difficult to extend to open-ended perceptual dimensions. We identify holistic bias as an important limitation: when scoring an unseen dimension, models reuse generic quality priors, leading to scoring errors and rank i...
  </details>

- **2026-09-19** — Yunpu Zhang, Changsheng You, Hing Cheung So — [Wideband Physical Layer Security in Mixed Near-Field and Far-Field Communications](http://arxiv.org/abs/2609.22936v1)
  <details><summary>📄 Abstract</summary>
  Prior studies on wideband physical layer security (PLS) have mostly focused on either far-field or near-field communication systems. In this paper, we investigate PLS in a more general and practical mixed near-field and far-field wideband communication scenario, where a base station (BS) equipped with an extremely large-scale array (XL-array) serves multiple legitimate users in the far field, while a near-field eavesdropper attempts to intercept confidential information at close range. Specifica...
  </details>

- **2026-09-19** — Fanchao Chen, Ziheng Jiang, Ziyun Wei et al. — [Towards Full Pipeline FP8 Reinforcement Learning for LLMs](http://arxiv.org/abs/2609.22870v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has become a key technique for improving the reasoning and agentic abilities of large language models (LLMs). Although FP8 quantization can accelerate RL training, maintaining stability throughout an FP8 RL pipeline remains challenging. While previous works have focused on resolving train-inference mismatches using correction techniques like TIS, we reveal that full-pipeline FP8 RL still suffers from severe training instability, manifesting as anomalous mid-training e...
  </details>

- **2026-09-19** — Yiheng Shen, Wei Zheng, Xiao Wei et al. — [Quality over Quantity: Diversity-Aware Data Selection for Efficient Verilog Code Generation](http://arxiv.org/abs/2609.22765v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown remarkable potential in Verilog code generation, yet existing datasets contain con siderable noise and redundancy. Prior data selection methods address only isolated quality aspects, neglect the global diversity of the training set, and cannot capture Verilog-specific structural semantics. To bridge this gap, we propose VeriSelector, the first data selection framework for Verilog code generation that jointly optimizes quality and diversity. We formulate th...
  </details>

- **2026-09-19** — Dipankar Srirag, Haokai Zhao, Ashutosh Kumar et al. — [LLMs Anchor on Chief Complaint and Fail to Integrate Evidence in Sequential Clinical Triage](http://arxiv.org/abs/2609.22904v1)
  <details><summary>📄 Abstract</summary>
  Triage in the emergency department (ED) is a sequential decision process that unfolds turn by turn. Existing evaluations of large language models (LLMs) for triage use completed retrospective records and report performance close to that of physicians. We implement a methodology for evaluating LLMs on sequential triage, the task of predicting a triage acuity label from a growing prefix of a nurse-patient conversation. We evaluate six LLMs at five sequential checkpoints on two corpora: 425 LLM-gen...
  </details>

- **2026-09-19** — Narendhiran Vijayakumar, Nav Singhal, Girish Varma et al. — [Search, Ground, Plan: Functional Sufficiency for Task and Motion Planning under Incomplete Scene Knowledge](http://arxiv.org/abs/2609.23113v1)
  <details><summary>📄 Abstract</summary>
  Foundation models (FMs) have expanded task and motion planning (TAMP) to manipulation problems specified through language and visual observations. However, incomplete scene knowledge leaves a critical gap between understanding what the task requires and knowing whether the physical scene can actually realize it. We introduce GRAB-TAMP, an FM-based TAMP framework that searches for scene entities required for task completion, grounds functional roles to valid physical objects, and plans only after...
  </details>

- **2026-09-19** — Guanxiong Chen, Yiduo Qu, Qianjun Xia et al. — [DiagGen: Agentic Generation of Deformable Assets with Sim-based Diagnostics for Robotic Simulation](http://arxiv.org/abs/2609.23103v1)
  <details><summary>📄 Abstract</summary>
  While simulation-ready deformable assets are essential for in-silico robotic manipulation tasks, existing generation frameworks typically assess physical plausibility after generation, leaving an object's simulated response unused as feedback for repairing upstream errors. We present DiagGen, an agentic framework that turns a single in-the-wild image into a simulation-ready deformable asset through a generate--simulate--diagnose--refine loop. DiagGen constructs part-aware geometry and material p...
  </details>

- **2026-09-19** — Yifei Sheng, Haoxiang Ren, Zhilong Zhang et al. — [Prioritized Rollouts for Efficient World Model-based Vision-Language-Action Policy Optimization](http://arxiv.org/abs/2609.22879v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have emerged as a powerful paradigm for embodied intelligence, but fine-tuning them with reinforcement learning (RL) remains constrained by the cost of real-world robot interaction. Model-based reinforcement learning (MBRL) reduces this cost by using a learned world model to generate rollouts for policy optimization. However, it becomes computationally expensive as VLA policies and world models scale. Existing methods typically treat states equally, overlookin...
  </details>

- **2026-09-19** — Zehua Cheng, Wei Dai, Jiahao Sun — [Euston: Training Away Mathematical Sycophancy Without Losing the Mathematics](http://arxiv.org/abs/2609.23205v1)
  <details><summary>📄 Abstract</summary>
  Reasoning language models are trained to produce solutions, not to refuse them, and this bias persists when the problem they are handed is false. Asked to prove a corrupted theorem, a strong model will typically comply and produce a confident derivation of something untrue. We present Euston, an 8B mathematical claim-verification model trained to resist exactly this. Training data were generated with GraphSynth, a probabilistic factor-graph generator that couples attribute-level diversity to dec...
  </details>

- **2026-09-19** — Mohammed Ahnouch, Lotfi Elaachak — [Whitening Inverts the Hierarchy: What the Norm of a Whitened Embedding Measures](http://arxiv.org/abs/2609.23117v1)
  <details><summary>📄 Abstract</summary>
  Whitening a foundation-model embedding and using its squared norm as a training-free likelihood surrogate is motivated by the observation that whitened coordinates often appear approximately standard normal. We show that this observation follows from the projection central limit theorem and therefore does not imply a Gaussian joint distribution. Across multiple encoders and three training objectives, we find systematic over-dispersion of the whitened radius relative to the Gaussian reference, in...
  </details>

- **2026-09-19** — Zixiaofan Yang, Chang Xiao — [Deciphering the Babel of Play: A Human-AI Collaborative Approach for Large-Scale Cross-Language Analysis of Game Reviews](http://arxiv.org/abs/2609.23104v1)
  <details><summary>📄 Abstract</summary>
  We present a large-scale cross-language analysis of game reviews using a human-AI collaborative framework that combines quantitative screening with multilingual large language models (LLMs). Starting from 17 million Steam reviews across 30 languages and 2,000 top-selling titles, we select 28 games with notable cross-language rating patterns. We then apply LLM-assisted content analysis to 442,162 reviews spanning 17 languages, with human researchers guiding codebook development and interpreting t...
  </details>

- **2026-09-19** — Jonggyu Jang, Hyeonsu Lyu, Hyun Jong Yang — [AirGC-CD: Gaussian-Circulant Precoding for Exactly Debiasable PAPR Reduction in Over-the-Air Federated Learning](http://arxiv.org/abs/2609.23084v1)
  <details><summary>📄 Abstract</summary>
  Over-the-air federated learning lets edge devices transmit their local updates simultaneously, reducing the communication overhead. The resulting waveform, however, has a peak-to-average power ratio (PAPR) that grows with the model dimension, and keeping the amplifier in its linear range leaves two remedies: clipping the peaks or backing off the transmit power. Neither remedy is without cost: i) the clipping distortion appears at the receiver as a bias that cannot be removed, and ii) back-off ke...
  </details>

- **2026-09-19** — Peng Qian, Andrew Li, Sam Chen et al. — [Directing large language models to follow the letter or spirit of the law](http://arxiv.org/abs/2609.23083v1)
  <details><summary>📄 Abstract</summary>
  The distinction between the spirit and letter of the law is a central issue across research and everyday life, and a growing concern for building safe, intelligent machines. What is this distinction based on, and how can we develop machines that follow the intention behind a rule? We used targeted adaptation that made large language models prioritize the spirit or letter of the law. With minimal modifications, our method significantly changed LLM behavior across diverse measures, novel vignettes...
  </details>

- **2026-09-19** — Seungjin Yang, Jason S. H. Lee, Junghwan Goh — [Mixture Density Networks for Neutrino Reconstruction at Hadron Colliders](http://arxiv.org/abs/2609.22979v1)
  <details><summary>📄 Abstract</summary>
  Neutrino momentum reconstruction at hadron colliders is intrinsically ambiguous because the longitudinal momentum is not directly observed. We study this problem in semileptonic $t\bar{t}$ events using \monster{} (Mixture of Neutrino Solutions with Transformer Event Representation), a mixture density network that predicts a multivariate normal mixture for the conditional distribution of neutrino momentum from reconstructed event objects. The model uses a Transformer-based event encoder and yield...
  </details>

- **2026-09-19** — Gabriel Ben-Simon — [Exactness as an Explanatory and Computational Target: A Reduction Architecture for First-Order ODEs, with a Higher-Order Outlook](http://arxiv.org/abs/2609.22962v1)
  <details><summary>📄 Abstract</summary>
  A typical first-order ODE syllabus is often presented as a sequence of named methods, which can obscure the unity among them. We propose organizing a substantial part of the classical symbolic first-order syllabus around a single computational target: an exact representative. For a regular scalar equation represented by a one-form $ω$, the reduction problem is to find, on an appropriate coordinate patch, a coordinate change $Φ$ and a nonvanishing factor $μ$ such that $μΦ^*ω=dG$, so that solution...
  </details>

- **2026-09-19** — Vigneshwar Ravi Rao, Rupesh Swarnakar, Fayeq Jeelani Syed† — [An Iterative LangGraph Agent for Text-to-SQL: Natural Language Access to the Chicago Crime Database](http://arxiv.org/abs/2609.22917v1)
  <details><summary>📄 Abstract</summary>
  Non-technical stakeholders frequently cannot write the SQL needed to extract insights from operational databases. We built and evaluated a Text-to-SQL agent that closes this gap end to end: a six-node LangGraph StateGraph checks question relevance, fetches the live schema, generates PostgreSQL, validates it with a dry run, retries on failure, executes the query, and narrates the result set in plain English. The agent uses prompt engineering only; no model was fine-tuned. We evaluated it on the C...
  </details>

- **2026-09-19** — Xinwei Long, Weigao Sun, Weibo Gao et al. — [Block-Sparse Attention with Semantic-Geometric Decoupled Routing](http://arxiv.org/abs/2609.22884v1)
  <details><summary>📄 Abstract</summary>
  Long-context inference has become a defining capability of large language models, but exact dense attention remains costly due to its quadratic scaling with sequence length. Block-sparse attention offers a hardware-friendly alternative by routing each query block to a small set of relevant key blocks, yet accurate training-free block routing remains difficult. Existing routers often pool post-RoPE token representations, which entangles semantic aggregation with RoPE-induced geometry and attenuat...
  </details>

- **2026-09-19** — Weihan Li, Xinlei Chen, Yuhan Song et al. — [Testing the Construct Validity of a Functional Valence Axis in LLM Agents](http://arxiv.org/abs/2609.22850v1)
  <details><summary>📄 Abstract</summary>
  Contrastive activation directions are often interpreted from what they decode or how strongly they steer behavior. But what evidence is sufficient to identify the construct represented by such a direction, rather than a correlated feature of the contrast used to extract it? We study this question for a good--bad outcome direction in a maze task, using controlled interventions that separate the realised outcome from the informational history through which it became known. Across multiple LLM chec...
  </details>

- **2026-09-19** — Ali Beikmohammadi, Sarit Khirirat, Sindri Magnússon — [Personalized Federated Reinforcement Learning via Model-Agnostic Meta-Learning: Convergence of Exact and Hessian-Free Meta-Policy Gradients](http://arxiv.org/abs/2609.22833v1)
  <details><summary>📄 Abstract</summary>
  We study personalized federated reinforcement learning, in which $n$ agents, each acting in its own Markov decision process, collaborate through a server to learn a shared MAML-style policy initialization that becomes effective for an individual agent once that agent adapts it with a single local policy-gradient step. We propose Per-FedAvg-PG, in which agents take $τ$ local stochastic meta-policy-gradient steps between communication rounds, and prove that it reaches an $\varepsilon$-approximate ...
  </details>

- **2026-09-19** — Nishit Anand, Jiaqi Su, Ke Chen et al. — [ParA-LLM: A Unified Approach to Paralinguistic and Acoustic Speech Understanding](http://arxiv.org/abs/2609.22771v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Audio LLMs have achieved human-level speech recognition, yet existing systems struggle to capture paralinguistic aspects such as speaker traits, expressive variations, and environmental acoustic conditions. To address this, we design a framework of 22 paralinguistic characteristics and create a dataset of over 1.2M Audio-QA pairs. We develop ParA-LLM, trained with a two-stage curriculum: first on single-attribute questions to build foundational knowledge, then on multi-attribu...
  </details>

- **2026-09-19** — Delong Li, Xu Wang, Haochen Gong et al. — [Replacing Large Language Models with Jev Decision Models for Low-Latency Edge Service Orchestration](http://arxiv.org/abs/2609.22753v1)
  <details><summary>📄 Abstract</summary>
  Natural-language service requests can require a language-model decision before execution starts, consuming part of the request's latency budget. We integrate Jev's decision-oriented application programming interface (API) into edge service orchestration to reduce this overhead while retaining service completion. The integration extracts four bounded intent fields and applies a shared validator, admission policy, and scheduler, accounting for decision waiting throughout the request timeline. We c...
  </details>

- **2026-09-18** — Uchi Uchibeke — [APort Vault: Benchmarking AI Agent Payment Authorization with the Open Agent Passport](http://arxiv.org/abs/2609.22076v1)
  <details><summary>📄 Abstract</summary>
  APort Vault is a benchmark for payment authorization in tool-using AI agents. It replays 4,371 attacks written by humans against a live payment agent during a public capture-the-flag event, across 14 models from 8 labs, five policy configurations and two replay tracks, with and without a deterministic pre-action check implementing the Open Agent Passport (OAP) specification. 225,964 evaluations completed. We report five distinct events per evaluation, because collapsing them is how an agent benc...
  </details>

- **2026-09-18** — Wenquan Zhou, An Wang, Jing Liang et al. — [CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices](http://arxiv.org/abs/2609.21344v1)
  <details><summary>📄 Abstract</summary>
  For Internet of Things (IoT) devices, a secure algorithm alone is not enough: an attacker with physical access can attack the implementation directly, and its flaws are hard to fix once deployed. Large language models (LLMs) are now used to build and analyze such implementations. LLM benchmarks exist for cryptography and general cybersecurity, but none covers cryptographic engineering. In this paper, we present CESBench, 380 expert-written items across six sub-domains of cryptographic engineerin...
  </details>

- **2026-09-18** — Haoyu Zhou, Joe Watson, Anson Lei et al. — [Benchmarking World Models for Continual Learning on Compositional Tasks](http://arxiv.org/abs/2609.22055v1)
  <details><summary>📄 Abstract</summary>
  A desirable property of a world model is the ability to learn continually across tasks, adapting to new environments without forgetting what the agent has already learnt. In particular, the ability to retain and reuse knowledge obtained from prior experiences underpins an agent's ability to efficiently adapt to novel environments, as the dynamics of the physical world can often be described in recurring mechanisms. However, the world model's measure of adaptation entangles two abilities: the spe...
  </details>

- **2026-09-18** — Camilo Carvajal Reyes, Felipe Tobar — [Time series generation with spectrally aligned latent flow matching](http://arxiv.org/abs/2609.21989v1)
  <details><summary>📄 Abstract</summary>
  Latent flow models have proven to be a reliable and cost-effective method for time series generation. However, the latent compression induces unwanted artefacts, such as a spectral mismatch with respect to the underlying dataset, thus hindering their use as training surrogates. In this article, we propose a spectrally-aligned latent-flow time series generator, where the latent space for flow matching is trained to preserve dynamical properties that are relevant for the suitability of synthetic s...
  </details>

- **2026-09-18** — Dongyijie Primo Pan, Pan Hui, Mirjana Prpa — [Can I Trust My Body? A Three-Year Autoethnography of ChatGPT's Place in My Support System for Panic Attacks](http://arxiv.org/abs/2609.21925v1)
  <details><summary>📄 Abstract</summary>
  People increasingly seek mental health support from large language models, yet little is known about their use across years of recurrent panic. We present a three-year analytic autoethnography of the first author's ChatGPT use while living with panic disorder, drawing on conversations, personal records, and accounts from friends or family members and professionals. Narrative analysis traces how my questions shaped ChatGPT's roles and how earlier experiences influenced later responses to symptoms...
  </details>

- **2026-09-18** — George Xi Wang, Xiangyu Li, Shaoyue Wen et al. — [Touvigation: Embodied Adaptive Object Acquisition for Blind and Low-Vision Users in Unfamiliar Indoor Environments](http://arxiv.org/abs/2609.21828v1)
  <details><summary>📄 Abstract</summary>
  Blind and low-vision users often face challenges when locating and physically acquiring objects in unfamiliar indoor environments. Existing vision-language-model-based assistants can provide semantic descriptions but may introduce latency, hallucinations, and guidance that is poorly aligned with embodied action. We present Touvigation, a hands-free object acquisition system that combines vision-language understanding with persistent local spatial modeling to provide low-latency, body-relative gu...
  </details>

- **2026-09-18** — Boni Hu, Xiong Wei, Haoming Huang et al. — [ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](http://arxiv.org/abs/2609.21712v1)
  <details><summary>📄 Abstract</summary>
  Generative world models offer controllable and repeatable closed-loop simulation for end-to-end and vision-language-action driving policies, but production deployment exposes three unresolved requirements: faithfully reproducing a mixed fisheye-pinhole rig at native resolutions; reconciling causal, per-timestep interaction with long-horizon stability and low latency; and preserving scene identity when a location is revisited. We present ZYT-World, a single architecture that natively generates fo...
  </details>

- **2026-09-18** — Mahdi Mohammadigohari, Gustau Camps-Valls — [Optimization Geometry of Equivalent Brownian RKHS Representations](http://arxiv.org/abs/2609.21693v1)
  <details><summary>📄 Abstract</summary>
  Equivalent finite parameterizations can represent the same functions and intrinsic norm yet induce different optimization algorithms. We study this effect in a controlled finite Brownian RKHS with nodal, increment, and spectral coordinates. Classical finite-element, RKHS-interpolation, Brownian-covariance, and mixed-boundary DCT identities make the shared hypothesis class, Brownian energy, approximation operator, and coordinate maps explicit. Our main results concern the optimization geometry of...
  </details>

- **2026-09-18** — Ishaan Mahajan, Charles Chen, Frederike Dümbgen et al. — [RAYA: Learning Where and When to Intervene for Robot Recovery](http://arxiv.org/abs/2609.21690v1)
  <details><summary>📄 Abstract</summary>
  A robot can predict failure and still be unable to prevent it. By the time a safety mechanism reacts, the nominal plan may already have spent the control authority that recovery requires, and fixed task priorities may block whatever response remains. Our key insight is that both aspects are decided inside the controller. Recoverability must inform actions while they are chosen rather than veto them afterward, and task objectives must be adapted as recoverability shrinks. Building on this, we pre...
  </details>

- **2026-09-18** — Thomas Ranzenberger, Steffen Freisinger, Tobias Bocklet et al. — [The Spoken Wikipedia Presentation Corpus](http://arxiv.org/abs/2609.21676v1)
  <details><summary>📄 Abstract</summary>
  We present the Spoken Wikipedia Presentation Corpus, an extension of the Spoken Wikipedia Corpora featuring LLM-generated slide decks for multimodal ASR. Slides are created from LLM-segmented sections using a hybrid pipeline that combines LLM-based content planning with rule-based design decisions. For each section, an LLM generates a slide title, bullet points, a takeaway message, and a visual description that is used to create an illustration. Rule-based matching then selects layouts, themes, ...
  </details>

- **2026-09-18** — Xinyu Che, Yunfei Ge, Shihao Li et al. — [GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions](http://arxiv.org/abs/2609.21562v1)
  <details><summary>📄 Abstract</summary>
  Coding agents can modify and test code across large software projects. Game development is a domain where agents must implement gameplay rules. A game can end in a valid state even after violating its rules during the run. Current game-development benchmarks replay fixed examples, score videos, or ask another model to judge the result. However, no existing benchmark checks game rules throughout execution across varied evaluator-selected scenarios while ensuring exactly reproducible verdicts. We ...
  </details>

- **2026-09-18** — Yewen Li, Peng Jiang, Yitian Li et al. — [OneBid: A Unified Auto-Bidding Foundation Model for Diverse oCPX Advertising Scenarios](http://arxiv.org/abs/2609.21550v1)
  <details><summary>📄 Abstract</summary>
  Auto-bidding is central to computational advertising, where strategies must maximize advertisers' conversion value under economic constraints. It has evolved from rule-based controllers to reinforcement learning and generative methods such as Decision Transformer (DT). Yet these methods increasingly mismatch the prevailing optimized cost-per-X (oCPX) paradigm, which spans heterogeneous scenarios (e.g., registration, purchase), each served by a separate model, leading to fragmented pipelines and ...
  </details>

- **2026-09-18** — Zetao Cai, Yaping Li, Yiqun Wang et al. — [Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Manipulation Transfer](http://arxiv.org/abs/2609.21514v1)
  <details><summary>📄 Abstract</summary>
  Robot demonstrations are expensive to collect and often provide limited distributional coverage of task variations. Human videos offer a low-cost source of complementary manipulation experience, but learning from them requires bridging embodiment gaps in visual appearance and action spaces. We introduce Skel-WAM, a world action model that bridges these differences through a unified hand-skeleton motion interface. The key insight is to align human and robot motion through a common hand topology, ...
  </details>

- **2026-09-18** — Jingyu Hu, Shu Yang, Weiru Liu et al. — [LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers](http://arxiv.org/abs/2609.21492v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) reasoning has been shown to improve the performance of large language models (LLMs), yet existing optimization methods largely rely on outcome-based feedback, leaving the logical validity of intermediate reasoning steps largely unverified. To address the gap whereby LLMs arrive at correct final answers through logically flawed intermediate reasoning chains, we propose LogicTrack, a neuro-symbolic framework that audits reasoning trajectories by auto-formalizing each reasoni...
  </details>

- **2026-09-18** — Jiaxing Chen, Hengduo Zou, Yiren Zhao et al. — [Risk-Aware Occupancy for Safety-Oriented End-to-End Autonomous Driving](http://arxiv.org/abs/2609.21470v1)
  <details><summary>📄 Abstract</summary>
  Sparse representation formulates the environment perception for the end-to-end driving system as a set of discrete elements like objects and lane lines. This formulation meets safety risks in crowded, occluded scenes dealing with unstructured obstacles, uncertain regions, and intricate interactions. In this paper, we propose a dense representation, risk-aware occupancy, to characterize planning-relevant risks in an explicit and uniform manner. It jointly encodes global scene occupancy, map-deriv...
  </details>

- **2026-09-18** — Joao P. A. Dantas, Jelton A. Cunha, Gabriel Dietzsch — [Offline Multimodal Large Language Models for Decision Support in Air Operations](http://arxiv.org/abs/2609.21390v1)
  <details><summary>📄 Abstract</summary>
  Air operations rely on complex rules, established procedures, and time-critical analysis under limited connectivity and strict security constraints. In such environments, analysts must combine written doctrine with images, often without access to external computing resources. This paper studies offline large language models as decision support tools, deployed in isolated and restricted environments to give analysts access to doctrinal knowledge that remains traceable to its original sources thro...
  </details>

- **2026-09-18** — Edward Holmberg, Elias Ioup, Mahdi Abdelguerfi — [Knowledge-Graph-Augmented Chronos-2 for HEC-RAS Surrogate Forecasting](http://arxiv.org/abs/2609.21381v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether coupling a time-series foundation model to hydraulic project knowledge improves surrogate forecasting of HEC-RAS water-surface elevation (WSE). We present KG-Chronos-2, which combines a frozen Chronos-2 predictor with exact-state residual decoding, graph-conditioned historical retrieval, and input-aligned correction. We compare the method with persistence, a residual LSTM, project-conditioned recurrent GeoFNO, a hydraulic DCRNN-style model, and frozen Chronos-2. Task-speci...
  </details>

- **2026-09-18** — Hyewon Lee, Ziying Wang, Aiden Moy et al. — [GUIDE: Designer-in-the-loop Authoring of Conformant Generative User Interfaces](http://arxiv.org/abs/2609.21285v1)
  <details><summary>📄 Abstract</summary>
  Generative User Interfaces (GenUIs) enable applications to generate interfaces on demand from user needs and context. Like conventional UIs, they must still reflect designers' intent and conform to requirements such as brand identity. Unlike conventional UIs, designers cannot directly specify or see every interface a GenUI may produce, making design intent harder to enforce. We introduce GUIDE (GenUI Development Environment), a system that lets designers continuously inspect and refine GenUI beh...
  </details>

- **2026-09-18** — Chao Li, Yingying Yu, Yunfeng Li — [How Many Humans Is a Judge Panel Worth?](http://arxiv.org/abs/2609.21277v1)
  <details><summary>📄 Abstract</summary>
  How many human judgments does a panel of language models represent? The answer depends on what is matched. We audit categorical judge panels against empirical human label distributions, retaining disagreement that binary errors relative to one gold label collapse. We measure spectral residual diversity by matching the participation ratio of a normalized residual Gram matrix to conditionally independent human-reference draws, giving nu_H. We separately match distributional squared error, giving n...
  </details>

- **2026-09-18** — Ji-Lun Peng, Yi-Zhen Zhang, Chun-Nan Chou et al. — [From Memory to Behavior: A Behavior-Aware Role-Playing Framework for Social Media Influencers](http://arxiv.org/abs/2609.21349v1)
  <details><summary>📄 Abstract</summary>
  Large language models have shown strong potential as role-playing agents for real individuals, yet faithful impersonating remains challenging. Existing in-context learning-based methods fail to capture how individuals react under different situations. In addition, LLM-based evaluation is difficult for obscure individuals. To address these challenges, we propose Situation--Internal state--Behavior Persona method to incorporate situation-dependent behavioral strategies. We further design an evalua...
  </details>

- **2026-09-18** — Pengjun Niu, Yujia Xie, Rui Peng et al. — [SkelWAM: A Skeleton-Guided World-Action Model for Zero-Shot Cross-Embodiment Manipulation](http://arxiv.org/abs/2609.21983v1)
  <details><summary>📄 Abstract</summary>
  Reusing manipulation experience across robot embodiments is important for scaling robot learning and reducing repeated task-specific data collection. However, changes in embodiment alter visual appearance, action dimensionality and semantics, and the whole-body configurations that can realize the same tool pose. We present SkelWAM, a skeleton-guided world-action model that couples perception and control through one explicit geometric representation for single-source cross-embodiment manipulation...
  </details>

- **2026-09-18** — Bruno N. Y. Chen, Li Kang, Heng Zhou et al. — [MAAP: Multi-Agent Active Perception for Collaborative Manipulation](http://arxiv.org/abs/2609.21929v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent manipulation naturally produces multiple task-driven viewpoints: every arm carries a wrist camera and moves through the scene while acting. Yet these observations are typically underutilized, and active perception in manipulation is still often treated as requiring a dedicated sensing agent. We introduce MAAP (Multi-Agent Active Perception), in which every arm is dual-purpose: it executes manipulation actions and, through the wrist camera it carries, simultaneously serves as a moving...
  </details>

- **2026-09-18** — Lobna Joualy, Eric Demeester, Nikolaos Tsiogkas — [Scaling Vision-Language Reward Learning for Robot Manipulation in Parallel Simulation](http://arxiv.org/abs/2609.21767v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can replace human annotators in preference-based reward learning, but sequential API requests and single-environment data collection make training slow and costly. We present RAPID (Reward learning with Adaptive Parallel Image Diversity), a system that couples GPU-parallel rollout with data-aware policy updates, single-request preference labeling, automatic reward stabilization, and representative image sampling. We evaluate these components on five Franka Panda man...
  </details>

- **2026-09-18** — Hiroaki Kingetsu, Hiroaki Kurihara, Kaoru Yokoo et al. — [SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations](http://arxiv.org/abs/2609.21650v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning Vision-Language-Action (VLA) models commonly relies on human teleoperation demonstrations, while reinforcement learning (RL) with sparse binary rewards faces an exploration challenge when successful trajectories are rarely sampled. We propose SynthDemo-RL, a teacher-student framework in which an automated teacher converts simulator-privileged state into successful manipulation trajectories, a VLA student is distilled from them by supervised fine-tuning (SFT), and PPO with binary task...
  </details>

- **2026-09-18** — Xinyu Liu, Gökhan Solak, Arash Ajoudani — [Potential-Field Action Representation for Reinforcement Learning in Contact-Rich Manipulation](http://arxiv.org/abs/2609.21609v1)
  <details><summary>📄 Abstract</summary>
  Model-free reinforcement learning can acquire contact-rich robotic manipulation skills through trial-and-error interaction, but it often requires the policy to learn both task strategy and low-level motion generation. In this setting, the action representation is critical because it determines how policy outputs are converted into robot motion, shaping both exploration and physical execution. Direct Cartesian command interfaces require the policy to generate motion at every decision step, coupli...
  </details>

- **2026-09-18** — Xiao Wang, Heng Zhang, Gokhan Solak et al. — [FORTE: Task-Adaptive Force Capability Optimization for Mobile Manipulators](http://arxiv.org/abs/2609.21497v1)
  <details><summary>📄 Abstract</summary>
  Effective physical interaction control in robotic manipulation requires not only kinematically feasible motion but also sufficient force-interaction capability. Existing redundancy resolution methods often ignore task-specific force demands or maximize the force capability indiscriminately, sacrificing dexterity when large force margins are unnecessary. We propose a task-oriented force capability optimization framework for redundant mobile manipulators. A Vision-Language Model (VLM) infers objec...
  </details>

- **2026-09-18** — Xuancheng Zhang, Xuetao Liu, Qianying Tang et al. — [ME-Dex 1.0: Bringing Heterogeneous Tactile Sensing into World Action Modeling](http://arxiv.org/abs/2609.21449v1)
  <details><summary>📄 Abstract</summary>
  World Action Models bring the predictive capabilities of video models into robot action generation, providing a rich foundation for modeling future visual states. Tactile sensing complements this foundation with direct measurements of physical interaction. Some existing methods use tactile features as conditioning inputs without jointly predicting future tactile states, visual observations, and actions. Our key insight is that tactile signals, like video, provide observations of the evolving wor...
  </details>

- **2026-09-18** — Vinicius Ferraz, Leon Houf — [People escalate against a competitor labelled human and hold back against one labelled an optimising machine](http://arxiv.org/abs/2609.21439v1)
  <details><summary>📄 Abstract</summary>
  People increasingly compete against AI agents rather than other human opponents. We distinguish two channels: an opponent effect and an information effect. These are different elements with different consequences: the opponent effect is specific to a given computational system, the information effect a property of the information environment that an organisation or policymaker can control. We separate them in a preregistered experiment (N = 1,395) using a dynamic all-pay auction, a repeated cont...
  </details>

- **2026-09-18** — Arjun Krishna, Vincent Pacelli, Dinesh Jayaraman — [LEMCA: LLM-Guided Synthesis of Efficient Mode-Switching Control Architectures](http://arxiv.org/abs/2609.21319v1)
  <details><summary>📄 Abstract</summary>
  Physical control tasks in the natural world, such as driving or object manipulation, frequently exhibit dramatic variations in sensory and compute complexity over time. Correspondingly, a natural resource-efficient choice for robot control is to dynamically switch between control modes with varying resource allocations. However, such "mode-switching controllers" (MSCs) have historically required laborious, expert-driven design and synthesis for each new task. Driven by these design difficulties,...
  </details>

- **2026-09-18** — Andre Bacellar — [Predictable Failure in Multi-Hop Retrieval: Score-Distributional Confidence Scoring and Abstention](http://arxiv.org/abs/2609.22056v1)
  <details><summary>📄 Abstract</summary>
  Multi-hop retrieval failures are not uniformly distributed across queries: they cluster in structurally predictable subpopulations. We prove two results formalizing this structure. First (CWAR Reducibility): confident-failure reduction is achievable if and only if retrieval features carry mutual information about success, a condition satisfied by LLM-judge pipelines but substantially weaker in dense-only settings, explaining the AUC-AC gap between regimes. Second (Feature Regime Complementarity)...
  </details>

- **2026-09-18** — Richard Zhe Wang — [Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention](http://arxiv.org/abs/2609.22005v1)
  <details><summary>📄 Abstract</summary>
  Gating the value pathway of attention reportedly improves language model pretraining, and prior studies disagree on why. We argue and provide experimental evidence that such gates supply two different things that softmax attention lacks: abstention and noise filtering. The first is abstention, which allows an attention head to output nothing, bypassing the requirement that attention weights must sum to one. The second is noise filtering, which allows the value pathway of an attention head to sup...
  </details>

- **2026-09-18** — Sayak Mukherjee, Kyung-Bin Kwon, Ramij R. Hossain et al. — [Learning-Based Augmentation and Adaptation for Grid Sim-to-Real Model Discrepancy](http://arxiv.org/abs/2609.21986v1)
  <details><summary>📄 Abstract</summary>
  Modern power systems can encounter increased discrepancy between the operators' simulation model and the actual true dynamics of the grid, driven by uncertainties caused by integration of new inverter-based resources (IBRs), large loads, unmodeled dynamics, parameter drifts, etc., to name a few. All of these impact the control room operations, where some critical oscillations may not be captured during the transient studies. To circumvent these issues, we propose a learning-augmented hybrid appr...
  </details>

- **2026-09-18** — Merwan Barlier, Blaz Skrlj — [LLMs as Feature Engineers for Text-and-Tabular Prediction](http://arxiv.org/abs/2609.21894v1)
  <details><summary>📄 Abstract</summary>
  We introduce an iterative framework that automates the extraction of interpretable, schema-bound categorical features from unstructured text for tabular prediction models. To navigate the feature space, a generator LLM proposes semantic definitions, a separate extractor LLM materializes the features, and a downstream tabular model evaluates their predictive performance. We optimize this search by translating explicit model errors, such as AUC ranking inversions, into natural-language feedback, s...
  </details>

- **2026-09-18** — Pierre Beckmann, Matthieu Queloz, Andre Freitas — [World Modeling in Transformers](http://arxiv.org/abs/2609.21748v1)
  <details><summary>📄 Abstract</summary>
  Behavioral failures can make a transformer appear to lack a world model even when it has learned faithful representations of its environment. We demonstrate this in TaxiGPT, a transformer trained on random walks through Manhattan whose failures have been interpreted as evidence of an incoherent internal map. Through mechanistic analysis and causal interventions, we show that the model represents intersections and streets, tracks its position, and uses a goal compass to navigate. We trace its fai...
  </details>

- **2026-09-18** — Kaiming Shen, Kareem M. Attiah, Yannan Chen et al. — [Connections Between Quadratic Transform for Fractional Programming and Schur Complement](http://arxiv.org/abs/2609.21730v1)
  <details><summary>📄 Abstract</summary>
  This paper shows that there are intimate connections between the quadratic transform technique for solving fractional programming (FP) problems and the Schur-complement technique in matrix analysis. We demonstrate that the quadratic transform technique is related to two aspects of the Schur complement: (i) the linear matrix inequality (LMI) condition for positive semidefiniteness and (ii) the matrix determinant formula. Specifically, we establish that the quadratic transform and the Schur-comple...
  </details>

- **2026-09-18** — Muhammad Ahsan Mustafa, Yasheerah Yaqoot, Faryal Batool et al. — [AgenticSwarm: Semantic Perception and Adaptive Task Allocation for Heterogeneous Multi-UAV Missions](http://arxiv.org/abs/2609.21716v1)
  <details><summary>📄 Abstract</summary>
  Multi UAV missions in complex environments require the system to understand both the surrounding scene and the intent of a human operator while maintaining feasible task allocation as mission conditions change. This paper presents AgenticSwarm, an agentic framework for semantic perception and adaptive task allocation in heterogeneous multi UAV missions. An agent interprets aerial imagery and natural language instructions to construct a grounded mission representation that links perceived objects...
  </details>

- **2026-09-18** — Hritika Sharma, Thibault Bañeras-Roux, Alessandra Pinto et al. — [Rethinking Human-Aligned Evaluation: An Analysis of Semantic Metrics Beyond WER](http://arxiv.org/abs/2609.21663v1)
  <details><summary>📄 Abstract</summary>
  Word Error Rate (WER), the most commonly used metric for Automatic Speech Recognition (ASR), treats every lexical deviation from the reference as equally costly, regardless of whether it changes meaning. This raises the question: does WER actually track how humans judge ASR transcript quality? We introduce HATS-en, an English dataset for human-centered ASR evaluation. Using this dataset, we benchmark lexical metrics against several configurations of BERTScore and SemDist, varying the language mo...
  </details>

- **2026-09-18** — Musa Rochi, Marcel Schubert, Christoph Gebhardt — [Learned Parametric Emotion Editing: Real-Time Affective Filtering for On-Device Social Media Video](http://arxiv.org/abs/2609.21624v1)
  <details><summary>📄 Abstract</summary>
  Problematic internet use affects a growing share of the population, yet common interventions, e.g., time limits, blocking, forced breaks, are coercive and easily circumvented. We explore a less restrictive alternative: adapting the emotional intensity of visual content. Prior work has shown that optimization can steer an image's affective content, but its per-image optimization cost makes it impractical for real-time deployment. We instead learn a model that predicts this transformation in a sin...
  </details>

- **2026-09-18** — Marco Pagni, Robin Engler, Frederic Burdet et al. — [kgsteward: a tool for building, reproducing and maintaining distributed knowledge graphs](http://arxiv.org/abs/2609.21564v1)
  <details><summary>📄 Abstract</summary>
  Collaborative research projects in life sciences increasingly need to integrate private, embargoed consortium data with public reference databases in order to reach statistically meaningful interpretations. The Resource Description Framework (RDF) is well suited to this task: it facilitates the integration of heterogeneous data sources, and allows researchers to keep data and their documentation as metadata in the same place, provided the knowledge graph itself remains private during the time co...
  </details>

- **2026-09-18** — Alexandru Ilovan — [Cross-Platform vs Native Mobile Development: An Empirical Study of Software Quality Trade-offs](http://arxiv.org/abs/2609.21544v1)
  <details><summary>📄 Abstract</summary>
  Cross-platform mobile frameworks promise code reuse, shorter delivery cycles, and lower implementation effort, but their trade-offs relative to native development remain difficult to assess objectively. Many comparisons rely on simplified applications, inconsistent feature sets, or a narrow set of metrics. This paper compares five implementations of the same plant-management application: native iOS, native Android, Flutter, React Native, and Kotlin Multiplatform. The shared approaches target bot...
  </details>

- **2026-09-18** — Jie Shao, Shengkai Hu, Xu Zhang et al. — [SkillIR: Evolving Scene-Aware Skills for Agentic Image Restoration](http://arxiv.org/abs/2609.21468v1)
  <details><summary>📄 Abstract</summary>
  This paper studies agentic image restoration, in which multimodal agents coordinate specialized restoration tools to recover images affected by complex degradations. Existing restoration agents often derive complete tool-use plans from the original degraded image or retrieve previously successful trajectories, providing limited support for adapting individual actions to evolving intermediate restoration states. We find that accepted tool executions can change the residual degradation state and, ...
  </details>

- **2026-09-18** — Yamato Narita, Issei Sato — [Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals](http://arxiv.org/abs/2609.21450v1)
  <details><summary>📄 Abstract</summary>
  Post-training weight-activation quantization reduces the memory and inference costs of large language models, but aggressive W4A4 quantization remains difficult because activation outliers degrade effective quantization resolution. Although weight optimization, channel-wise scaling, and orthogonal rotation mitigate this problem, the error components they address and their relationship remain unclear. Using an exact decomposition of local weight-activation quantization error into an activation-gu...
  </details>

- **2026-09-18** — Kaichen Zhang, Yuzhong Hong, Junwei Bao et al. — [GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation](http://arxiv.org/abs/2609.21432v1)
  <details><summary>📄 Abstract</summary>
  Post-training plays a pivotal role in enhancing the reasoning capabilities and task-specific expertise of large language models (LLMs). Despite recent advances in post-training methods, such as Group Relative Policy Optimization (GRPO), their practical deployment remains impeded by training instability arising from the reliance on importance sampling.   We introduce Group Variance Policy Optimization (GVPO), a novel post-training method that integrates the analytical solution of KL-constrained r...
  </details>

- **2026-09-18** — Xinyue Luo, Fei Yu — [Prediction Dynamics in Depth-Recurrent Language Models](http://arxiv.org/abs/2609.21383v1)
  <details><summary>📄 Abstract</summary>
  Depth-recurrent language models refine predictions through repeated latent updates. Why can intermediate answers agree with the endpoint while their scores continue to change? We derive a sharp margin characterization that decomposes the conservatism of a magnitude bound into common translation, direction relative to the winner, and the pairing of each competitor's update with its score gap. Across Huginn-3.5B and Ouro-1.4B, accounting for update direction and competitor pairing reduces the mean...
  </details>

- **2026-09-18** — Cevheri Bozoglan, Yusuf Gundogdu, Abdullah Kaya et al. — [What Stops a Small Language Model From Driving a Database Agent](http://arxiv.org/abs/2609.21341v1)
  <details><summary>📄 Abstract</summary>
  Small open-weight language models are assumed to fail at agentic database work because they lack the reasoning capacity for it. We test that against a production system. Over eleven days we drove the agent mode of an open-source SQL client with 39 open-weight models served locally and one hosted control, across six task surfaces: 8,199 runs, 110,711 ledger events, 14,008 refused tool calls. Of the 2,100 model-attributed agent-mode losses, 1,590, or 75.7%, came from runs that had invoked at least...
  </details>

- **2026-09-18** — Jiale Zhang, Michael Larionov, Zichong Wang et al. — [FairLMs: A Turnkey Library for Fairness in Language Models](http://arxiv.org/abs/2609.21296v1)
  <details><summary>📄 Abstract</summary>
  Fairness research on language models involves measuring bias, applying mitigation methods, and examining the evidence on which an evaluation rests. Existing tools offer complementary functionality through different interfaces, so combining them requires reconciling model interfaces, evidence formats, access constraints, and result types before applicability can be checked or methods compared. We introduce \textbf{FairLMs}, a Python library that connects these activities through explicit declarat...
  </details>

- **2026-09-18** — Erwei Wang, Ephrem Wu, Victor J. B. Jung et al. — [Programming AMD XDNA NPUs with Open-source Compiler Tools: A FlashAttention Case Study](http://arxiv.org/abs/2609.21264v1)
  <details><summary>📄 Abstract</summary>
  Spatial NPUs such as AMD XDNA place compute tiles beside small local memories and leave data movement between them to software. Mapping a multi-stage workload onto such a device is largely a question of where the intermediate tensors live. We report what we learned making those choices for FlashAttention with the open-source IRON and MLIR-AIR flows.   We compare four reference designs on XDNA 1 and XDNA 2: one runs each operator separately, two stream between operators on chip, and one fuses all...
  </details>

- **2026-09-18** — Hao Fu, Baiting Zhu, Minglei Chen et al. — [Verify, Don't Trust: Agentic Model Development for Video Discovery Retrieval at Scale](http://arxiv.org/abs/2609.21257v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can propose, implement, and evaluate model changes. Autoresearch loops demonstrate this capability through minutes-scale iterations on a self-contained program. Online autoresearch instead spans asynchronous systems, hours-long variants, and weeks-long campaigns that can influence a product. A completed run can still support an invalid conclusion when a code change is a no-op, data windows leak, evaluator semantics drift, or the two arms traverse different servi...
  </details>

- **2026-09-17** — Ruichen Tan, Zengxiang Lei, Satish Ukkusuri — [Worst-Case Hidden-Vehicle Trajectory Search in Spatiotemporal Occlusion Regions](http://arxiv.org/abs/2609.20480v1)
  <details><summary>📄 Abstract</summary>
  Occlusion creates fundamental uncertainty in autonomous driving. Existing methods often propagate frame-wise hypotheses or optimize ego behavior against prescribed hidden-agent predictions, leaving the worst history-consistent interaction unexplored. We introduce History-Conditioned Minimax Trajectory Search (HC-MTS), which combines temporal occlusion reasoning with response-aware search. First, HC-MTS constructs finite hidden-state modes, each certified by a backward witness satisfying multi-fr...
  </details>

- **2026-09-17** — Yin Wu, Jiarong Wei, Carl Esselborn et al. — [Safety-Critical Scenanrio Emerges from Initial Scene](http://arxiv.org/abs/2609.20103v1)
  <details><summary>📄 Abstract</summary>
  Safety-critical driving scenario generation has largely focused on manipulating the behavior of surrounding agents while starting from an initial scene from driving data. This assumption can limit the space of discoverable failures, since driving data can provide little opportunity for meaningful interaction. For example, in the Waymo Open Motion Dataset, 20.44% of recorded slices feature a stationary ego vehicle that never moves, and 30.39% of initial frames contain no nearby traffic participan...
  </details>

- **2026-09-17** — Damiano Da Col, Maximilian Igl, Peter Karkus et al. — [OPTED: On-Policy Fine-Tuning for End-to-End Driving using a Render-Free Teacher](http://arxiv.org/abs/2609.20756v1)
  <details><summary>📄 Abstract</summary>
  As scaling pre-training data alone yields diminishing returns, post-training is becoming increasingly important across physical AI domains such as autonomous driving. End-to-end driving policies are pre-trained in open loop with behavior cloning on human demonstrations. However, compounding errors during closed-loop deployment can take the vehicle outside the training data distribution, increasing the risk of safety-critical incidents. Closed-loop post-training can mitigate this risk but require...
  </details>

- **2026-09-17** — Ö. D. Gürcan, L. Manfredini, P. Morel — [Solutions of the Navier-Stokes Equation Through Affine Transformations: The Triad Triplet](http://arxiv.org/abs/2609.20710v1)
  <details><summary>📄 Abstract</summary>
  Considering triads in helical decomposition of three dimensional Navier-Stokes turbulence, three consecutive triads of the same shape and class, where the reference wave-number appears as the smallest, the middle and the largest wave-numbers respectively, constitutes an interesting object called the triad triplet that allows tracing the local transfer in wave-number space due to a given shape and class of triads. It is shown that, evolution equations for the triad triplet can be obtained from th...
  </details>

- **2026-09-17** — XiuYu Zhang, Wei Chow, Junfeng Fang et al. — [What Does Privileged Information Add to On-Policy Self-Distillation?](http://arxiv.org/abs/2609.20612v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) lets a language model learn from a frozen copy of itself that sees an answer or a worked solution. Giving the teacher this extra information seems to offer the student more to learn, but how much does it add beyond distillation itself? To isolate that contribution, we construct AMPLE-Math, a reusable suite of 5,319 mathematical problems with six reasoning views that share the same answer, and compare each view with matched reference-free distillation. With a th...
  </details>

- **2026-09-17** — Zimu Wang, Yiwen Jiang, Xiangyu Zhao et al. — [Steering the Compass: Aligning Dynamic Psychological Counseling Conversations with Cognitive Behavioral Therapy Strategies](http://arxiv.org/abs/2609.20565v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in large language models have revolutionized the field of psychological counseling, especially in the context of Cognitive Behavioral Therapy (CBT). While the success of CBT relies heavily on dynamic decision-making informed by the client's real-time mental state, this aspect has often been overlooked in current research, limiting both flexibility and therapeutic outcomes. In this paper, we introduce StratCBT, a dataset specifically designed for psychological counseling conve...
  </details>

- **2026-09-17** — Haozhe Liu, Tian Ye, Sensen Gao et al. — [SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](http://arxiv.org/abs/2609.20519v1)
  <details><summary>📄 Abstract</summary>
  As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired approach at the harness layer, scaling auto-research loops across increasingly numerous and diverse environments for harness rollouts. At this scale, the process yields reusable improvem...
  </details>

- **2026-09-17** — Yukun Zhang, Kemu Xu, Yishen Chen — [How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful LLM Agents](http://arxiv.org/abs/2609.20474v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses supply planning guidance, organize execution, and check completion. We study how these components affect success, erroneous acceptance, and cost in two Retail experiments and an Airline pilot in $τ^2$-bench. The primary comparison pairs prewritten task-specific plans (Fixed) with shuffled policy text matched in word count (Sham), isolating the contribution of guidance content. Across 265 matched cells, Fixed improves oracle-verified success by 7.17 percentage points (90\% task-cl...
  </details>

- **2026-09-17** — Yukun Zhang, Kemu Xu, Yishen Chen — [Welfare-Opaque Income: Taxation under AI-Agent Delegation](http://arxiv.org/abs/2609.20425v1)
  <details><summary>📄 Abstract</summary>
  We study income taxation when an AI agent implements economically relevant choices through a rule hidden from the government. Alongside unobserved productive ability, this hidden preference-to-execution mapping creates \emph{double unobservability}: the same observable tax-base response can carry different welfare consequences. We call the resulting income \emph{welfare-opaque}. Our constructions show that tax-base statistics can coincide while reform welfare effects differ, even when mechanical...
  </details>

- **2026-09-17** — Qing Xu, Yixuan Zhang, Yue Li et al. — [FreqDINO++: A Frequency-Guided Multi-Task Routing Vision Foundation Model for Universal Ultrasound Analysis](http://arxiv.org/abs/2609.20340v1)
  <details><summary>📄 Abstract</summary>
  Ultrasound image analysis plays a crucial role in cancer screening and prenatal diagnosis, yet comprehensive assessment requires jointly addressing tasks such as lesion segmentation and benign-malignant classification. While recent vision foundation models have shown remarkable universal representations, unlocking their potential for ultrasound is bottlenecked by the considerable domain gap from natural images. Existing methods typically fine-tune heavy vision encoders for isolated tasks, incurr...
  </details>

- **2026-09-17** — Pritish Mishra, Ishaan Kumar, Akshat Mandoli et al. — [MTVA-Bench: Evaluating the Language Model Inside Cascaded Voice Agents](http://arxiv.org/abs/2609.20152v1)
  <details><summary>📄 Abstract</summary>
  Generally, most voice agents are cascaded systems, i.e., an ASR model transcribes the caller's audio, a language model reads the transcript and decides what to say and which backend tools to call, and a TTS model speaks the reply. Nearly all of the decision making happens in the language model, but existing evaluations measure it either too broadly or too narrowly. End-to-end voice benchmarks score the full pipeline, so recognition errors and model errors mix into a single number. LLM benchmarks...
  </details>

- **2026-09-17** — Zifan Guan, Longyu Lu, Junan Zhang et al. — [Multi-Dimensional Prosody Judgment For Live Streaming Speech Synthesis](http://arxiv.org/abs/2609.20124v1)
  <details><summary>📄 Abstract</summary>
  Evaluating live streaming speech synthesis (TTS) requires assessing fine-grained, highly expressive prosody such as emotion, intonation, and energy which traditional MOS predictors fail to capture. While proprietary Large Language Models (LLMs) like Gemini can evaluate these aspects, they are too costly for massive inference and reinforcement learning feedback. To address this, we first introduce Live-ProsodyJudge (LPJ), a cost-effective pairwise evaluator distilled from Gemini into Qwen3-Omni. ...
  </details>

- **2026-09-17** — Yuang Tu, Runjia Tan, Yujie Yan et al. — [AnyviewMeter: Adapting Robotic Reward Models with Camera Geometry and Multi-View Attention](http://arxiv.org/abs/2609.20106v1)
  <details><summary>📄 Abstract</summary>
  Robotic reward models evaluate task execution from visual observations, but their predictions can change with camera viewpoint and occlusion even when the underlying task state is unchanged. Adapting a pretrained reward model to a local task therefore requires accounting for how that task is observed. We introduce AnyviewMeter, a geometry-conditioned adaptation framework for robotic reward models that represent task progress as a scalar reward signal. It combines low-rank fine-tuning with token-...
  </details>

- **2026-09-17** — Xin Zhou, Cong Miao — [Astronex-World 1.0: Real-Time Interactive World Model Foundation](http://arxiv.org/abs/2609.20034v1)
  <details><summary>📄 Abstract</summary>
  We present Astronex-World 1.0, an open controllable video world-model foundation. Given a text prompt (text-to-video) or an initial observation (image-to-video), the model predicts future visual states under frame-aligned camera trajectories, continuous actions, and an embodiment identifier, and accepts text events inserted at a specified position of a rollout. The family provides a bidirectional model for full-context generation and a causal model with block-causal attention and cross-block KV ...
  </details>

- **2026-09-17** — Faiz Ghifari Haznitrama, Alice Oh — [Evaluating Communicative Success in Machine-Translated Conversation](http://arxiv.org/abs/2609.19885v1)
  <details><summary>📄 Abstract</summary>
  Interpreter agents built on machine translation (MT) increasingly mediate live conversation between people who do not share a language, yet we still evaluate them with metrics built for isolated sentences, which measure fidelity rather than whether communication succeeds. We introduce a reusable three-layer checklist-and-judge framework that evaluates interpreter-mediated conversation across semantic, pragmatic, and cultural-social dimensions, covering the naturalness, intent, and social appropr...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 633 |
| prompt-injection | 548 |
| memory-poisoning | 50 |
| tool-use-attack | 136 |
| backdoor | 468 |
| adversarial-attack | 598 |
| privacy-leakage | 4131 |
| steganography | 71 |
| misuse | 1038 |
| red-teaming | 126 |
| vulnerability | 3169 |
| defense | 2993 |
| alignment | 2778 |
| robustness | 2932 |
| watermark | 453 |
| unlearning | 96 |
| agent-safety | 55 |
| benchmark | 66 |
| survey | 356 |
| other | 7946 |

---

📚 **全部 28643 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-22 16:07:30*