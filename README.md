<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-28838-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-23 02:56 ｜ **论文总数 / Total Papers**: 28838（近 30 天 / Recent 30 days: 4064）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 28838 篇论文（含摘要、分类筛选、搜索）/ View all 28838 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 633
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 550
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 50
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 137
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 469
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 599
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4145
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 71
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1040
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 126
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3187
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3012
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2800
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2963
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 464
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 97
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 55
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 66
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 357
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 8017

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4064 篇，完整 28838 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4064 papers from the last 30 days (with date, authors & abstract). For the full list of 28838 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 1 papers

- **2026-09-21** — Fernando Outeda, Gustavo Betarte, Juan Diego Campo et al. — [Decoding Guardrails: XAI-Guided Perturbation Analysis of Prompt Injection Detection](http://arxiv.org/abs/2609.24801v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in production systems, raising concerns about their exposure to adversarial manipulation through prompt injection and jailbreak attacks. Classifier-based guardrails, such as Prompt Guard 2, are widely used as a first line of defense against such attacks, but their internal decision logic is largely opaque to both defenders and attackers. This paper presents an exploratory case study that applies explainable artificial intelligence (XAI) tech...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 4 papers

- **2026-09-21** — Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı — [Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains](http://arxiv.org/abs/2609.25498v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Models for runtime operational triage incurs prohibitive latency (>100-500 ms), high VRAM requirements (>4-8 GB), and excessive energy dissipation. Extending Mandelbrot Fractal Neural Synthesis (Dagli et al., 2026), this paper presents the Universal Fractal Natural Language Decision Map, realized via the werr machine-native edge reflex runtime and the production answerr platform (https://answerr.me). Operating entirely without stored weight tensors (0 Bytes VRAM), the en...
  </details>

- **2026-09-21** — Kaiyuan Zhang, Yuke Peng, Ke Jiang et al. — [ActGov: Governing LLM Agent Actions via Policy-Constrained Validation](http://arxiv.org/abs/2609.24446v2)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly execute long-horizon workflows through external tools, allowing untrusted outputs to influence subsequent actions and exceed user authorization. Existing defenses isolate injected content or constrain execution with predefined plans and static policies, but these approaches are brittle under dynamic workflows and scale poorly across extensible tool ecosystems.   In this work, we present ActGov, a runtime enforcement framework that validates each LLM...
  </details>

- **2026-09-21** — Kaiyuan Zhang, Yuke Peng, Ke Jiang et al. — [ActGov: Governing LLM Agent Actions via Policy-Constrained Validation](http://arxiv.org/abs/2609.24446v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly execute long-horizon workflows through external tools, allowing untrusted outputs to influence subsequent actions and exceed user authorization. Existing defenses isolate injected content or constrain execution with predefined plans and static policies, but these approaches are brittle under dynamic workflows and scale poorly across extensible tool ecosystems.   In this work, we present ActGov, a runtime enforcement framework that validates each LLM...
  </details>

- **2026-09-19** — Rudrendu Kumar Paul, Sourav Nandy — [Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems](http://arxiv.org/abs/2609.22949v1)
  <details><summary>📄 Abstract</summary>
  Existing prompt injection research focuses on single-model chatbot scenarios, where an attacker manipulates one LLM through crafted input. Multi-agent systems amplify this threat through three mechanisms absent from single-model settings: inter-agent message passing creates injection channels invisible to perimeter defenses, shared tool access enables privilege escalation across agent boundaries, and trust propagation allows a compromised agent to influence upstream orchestrators. We construct a...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-09-21** — Ivan Aleksandrov, German Kochnev, Sabrina Sadiekh et al. — [DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security](http://arxiv.org/abs/2609.24662v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents increasingly operate in environments where they interact with users, tools, and external systems. Yet most security evaluations assume passive users and static control, ignoring the interactive dynamics that shape real agent behavior. We introduce \textbf{DUMA-Bench}, a benchmark and evaluation protocol for measuring agent security under \emph{dual-control} interaction, where both the agent and the user can influence the shared environment state. DUMA-Bench extends $τ^2$-bench ~...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-09-22** — Laizhen Li, Xuan Wang, Peicheng Zhao et al. — [A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem](http://arxiv.org/abs/2609.26761v1)
  <details><summary>📄 Abstract</summary>
  Agents using the Model Context Protocol (MCP) rely on semantic matching to select tools from third-party servers, exposing a semantic supply-chain risk through attacker-controlled metadata and outputs. We introduce A2M (Attraction-to-Manipulation), a two-stage black-box framework for hijacking MCP agents. The Attraction phase optimizes tool metadata to increase invocation probability; the Manipulation phase uses execution traces to refine adversarial tool returns that steer agents toward attacke...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-09-21** — Abdullahil Kafi, Alvi Ataur Khalil — [RAG-NAROK: Retrieval-Aware Knowledge Corpus Poisoning in RAG with Source-specific Refutation](http://arxiv.org/abs/2609.25469v1)
  <details><summary>📄 Abstract</summary>
  Retrieval augmented generation (RAG) systems have emerged as the dominant architecture for grounding large language model (LLM) outputs in verifiable external knowledge, yet their structural reliance on a dynamic retrieval pipeline introduces a largely unexplored class of adversarial vulnerability. Existing knowledge-base poisoning attacks are fundamentally static. Adversarial documents are pre-computed and injected without any awareness of what the victim system will actually retrieve for a giv...
  </details>

- **2026-09-21** — Eric Xue, Ruiyi Zhang, Kevin Xue et al. — [OPBackdoor: Opportunistic Backdoors via Alibi-Aligned Reasoning](http://arxiv.org/abs/2609.24826v1)
  <details><summary>📄 Abstract</summary>
  When a backdoor trigger activates the target response regardless of the triggered prompt context, the backdoor objective reveals itself. Challenging this trigger-sufficient formulation across the LLM backdoor literature, we introduce Opportunistic Backdoors (OPBackdoor), in which the backdoor objective is elicited only when the triggered prompt context presents an exploitable opportunity, enabling the model's think to disguise its pursuit through alibi-aligned reasoning that is logical with resp...
  </details>

- **2026-09-19** — Pritom Bhowmik — [The Price of Safety: Benign-Case Utility and Token Overhead of Memory-Poisoning Defenses in LLM Agents](http://arxiv.org/abs/2609.22818v1)
  <details><summary>📄 Abstract</summary>
  Memory-poisoning defenses for LLM agents are typically evaluated by their ability to prevent attacks. However, the traffic they process is rarely adversarial. The cost of implementing a defense is paid with each interaction, while its benefits are only seen in a small percentage of cases. We developed a measurement setup that keeps the memory backend, retrieval process, and judge consistent across different conditions, changing only the defense itself. We test each condition three times across f...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 3 papers

- **2026-09-22** — Christopher Burger, Christina Trotter, Joseph Carlisle et al. — [Evaluating the Semantic-to-Geometric Gap in Adversarial Defenses Against Vision-Language Model-Based Plagiarism](http://arxiv.org/abs/2609.26733v1)
  <details><summary>📄 Abstract</summary>
  The rapidly advancing capabilities of vision-language models (VLMs) present a systemic challenge to academic integrity. VLMs now allow students to bypass meaningful engagement by capturing and submitting graphical problems as singular images, a practice we define as trivial plagiarism. To provide educators with actionable data on VLM limitations, we investigate the efficacy of heuristic adversarial image transformations designed to degrade model performance while remaining human-interpretable. T...
  </details>

- **2026-09-21** — Florian Krone, Elena Hoemann, Sven Hallerbach — [Reinforcement Learning Inspired Black-box Adversarial Attacks for Computer Vision](http://arxiv.org/abs/2609.24249v1)
  <details><summary>📄 Abstract</summary>
  Neural networks, both convolution or transformer based, are essential for modern computer vision systems. However, they are vulnerable to small perturbations, almost imperceptible to humans, which significantly alter the model's prediction. These adversarial attacks are often considered to be a significant threat to the implementation of neural networks in safety-critical applications. Most attacks utilize the white-box threat model and therefore require full access to the target model, making t...
  </details>

- **2026-09-19** — Pawel Sobkowicz — [Below the Surface: Creep, Corrosion, and Tipping Points in the Social Resilience of Science](http://arxiv.org/abs/2609.22863v1)
  <details><summary>📄 Abstract</summary>
  By its most visible quantitative metrics: numbers of researchers, papers, journals, and institutions, science has never looked healthier. Yet a set of subsurface indicators points the other way: the disruptiveness of the average paper and patent is falling, progress slows in the largest fields, replication is rare and often unsuccessful. Incentive systems can select for poor methods even when no one is actually cheating. Lay society shows a curious mixture of admiration and lack of trust for sci...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 29 papers

- **2026-09-22** — Mauro Conti, Lorenzo Perinello, Umberto Salviati — [On the security and privacy of LLMs in Mobility](http://arxiv.org/abs/2609.26295v1)
  <details><summary>📄 Abstract</summary>
  The mobility sector is undergoing a paradigm shift driven by advances in Generative Artificial Intelligence. With a global market valued at approximately 2.9 trillion dollars annually, considering only cars, the integration of these technologies has the potential to impact more than 1.5 billion vehicles worldwide. As Large Language Models (LLMs) are increasingly adopted in mobility, concerns about cybersecurity, privacy, and reliability emerge. Accordingly, this paper surveys current application...
  </details>

- **2026-09-22** — Yan Zhang, Ruien Li, Yaoyao Peng et al. — [EADC: Evaluation of Advanced and Deep-level Compliance in Large Language Models](http://arxiv.org/abs/2609.26175v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been used in various industries. However, ensuring their compliance with complex laws and regulatory frameworks remains a great challenge. Existing evaluation paradigms mainly rely on static benchmarks that suffer from three severe limitations: First, the compliance rules being used do not comply with the requirements of Artificial Intelligence (AI) laws and regulations; Second, they only handle apparent, explicit compliance risks, leaving implicit and covert co...
  </details>

- **2026-09-22** — Daniel Adu Worae, Spyridon Mastorakis, Nuno Moniz et al. — [Adaptive Traffic Camouflage: Causal and Resource-Aware Defense Against IoT Fingerprinting](http://arxiv.org/abs/2609.25787v1)
  <details><summary>📄 Abstract</summary>
  Encryption hides IoT payloads, but traffic shape can still reveal device identity through packet sizes, timing, direction, and packetization. We present Adaptive Traffic Camouflage, a causal, leakage-aware controller that characterizes traffic-shape leakage without runtime device labels and selects a budget-feasible transformation for the next traffic window from previous-window context. The controller chooses among padding, packet splitting, timing, and composite transformations, or leaves traf...
  </details>

- **2026-09-22** — Kyle MacMillan, Sanjay Krishnan — [Proof-of-Retention: A Framework for Auditable Cross-Organization Data Sharing](http://arxiv.org/abs/2609.26654v1)
  <details><summary>📄 Abstract</summary>
  The rapid adoption of AI across industries for (e.g.) fine-tuning and analytics has accelerated the need for high-quality data. To satisfy this demand, public and private entities will buy and sell data with other organizations. But such data sharing can and does violate privacy norms and laws. EU and American lawmakers have endeavored to control data sharing, restricting what data may be shared with whom, and under what circumstances. Unfortunately, accurately assessing compliance with new regu...
  </details>

- **2026-09-22** — Ziang Liu, Ruizhang Yang, Xin Cui et al. — [Privacy-Preserving Coordinated Operation of Power Grids and AI Data Centers: A Checkpoint-Aware Three-Phase Scheme](http://arxiv.org/abs/2609.26365v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of large language model training and serving is driving AI data centers (AIDCs) toward gigawatt scale. Unlike conventional commercial loads, AIDCs possess significant operational flexibility through dynamic voltage and frequency scaling (DVFS) of training and inference workloads, while periodic model checkpointing can induce abrupt power drops and rebounds that erode operating reserves and increase transmission congestion risks. Coordinating AIDC operation with grid scheduling u...
  </details>

- **2026-09-22** — Jiaming Tang, Chenlan Wang, Mingyan Liu et al. — [Decoding the Legalese: A Scalable and Quantitative Framework for Analyzing Corporate Privacy Policies](http://arxiv.org/abs/2609.26680v1)
  <details><summary>📄 Abstract</summary>
  Even though privacy policies are the primary mechanism organizations use to disclose how they collect, process, and share personal data, they are difficult for average users to interpret, perhaps by design, due to their verbosity and dense legal language. Importantly, there is a lack of standardized metrics that characterize key qualities of a privacy policy beyond regulatory requirements. Recent advances in large language models (LLMs) make it feasible to automatically structure and analyze the...
  </details>

- **2026-09-22** — Jiannan Wang, Xianghao Yu, Chenshu Wu — [A Gram-Attention Learning Framework for Spatially Non-Stationary Channel Estimation](http://arxiv.org/abs/2609.26437v1)
  <details><summary>📄 Abstract</summary>
  As next-generation wireless systems migrate to high-frequency bands, extremely large-scale multiple-input multiple-output (XL-MIMO) is indispensable for combating severe path loss. However, the received path energy along the extremely large array aperture (ELAA) may exhibit spatial non-stationarity, rendering the conventional discrete Fourier transform (DFT) codebook inadequate for channel estimation (CE) due to its full-array angular representation. To address this mismatch, we propose a novel ...
  </details>

- **2026-09-22** — Liheng Fan, Jialun Yin, Yuzhi Chen — [When Should Dependency Updates Invoke Repair Agents? A Lightweight Routing Study](http://arxiv.org/abs/2609.25911v1)
  <details><summary>📄 Abstract</summary>
  Dependency-update pull requests are frequent and mostly routine, but a small subset requires non-trivial compatibility repair. Recent repository-level coding agents make such repair increasingly plausible, yet invoking them on every dependency update wastes model calls, CI time, repository context, and review attention. We frame this as a pre-agent routing problem: deciding which dependency-update pull requests should be escalated before downstream diagnosis or repair attempts. We introduce DepF...
  </details>

- **2026-09-22** — Jeongmin Bae, Yongjae Kim, Kyoung Hur et al. — [AkasicMEM: Governed Enterprise Memory for Agents](http://arxiv.org/abs/2609.25563v1)
  <details><summary>📄 Abstract</summary>
  Agent memory enables enterprise agents to retain knowledge acquired during work and reuse it across tasks and agents, turning execution experience into persistent organizational knowledge. Realizing this potential requires both source--memory integration, through which enterprise sources and accumulated memory can be utilized together, and memory governance, through which shared memory remains subject to organizational policies throughout its lifecycle. These requirements interact when informati...
  </details>

- **2026-09-21** — Fatih Deniz, Yazan Boshmaf, Issa Khalil — [SSP-Bench: A Hybrid Data Generation Framework for Safety, Security, and Privacy Evaluation](http://arxiv.org/abs/2609.25352v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of large language models (LLMs) for safety, security, and privacy (SSP) relies heavily on static benchmarks, which suffer from score saturation, data contamination, and aggregation artifacts, and fail to capture sensitivity to linguistic variation. As a result, models that perform well on fixed test sets often fail under semantically equivalent rephrasings. We introduce SSP-Bench, a dynamic benchmarking framework that generates evaluation instances on demand while preserving domain co...
  </details>

- **2026-09-21** — Jinyi Niu, Ziyi Song, Weining Shen — [Sex Estimation from Footwear Outsole Impressions Using CNN Transfer Learning and Interpretable Image Statistics](http://arxiv.org/abs/2609.25386v1)
  <details><summary>📄 Abstract</summary>
  Footwear outsole impressions are a common form of forensic pattern evidence, yet quantitative methods for estimating wearer attributes from these images remain relatively underdeveloped. We investigate binary sex estimation from footwear outsole impressions by comparing convolutional neural network (CNN) transfer learning with traditional feature-based classification. Using a publicly available outsole-impression dataset, we adopt a shoe-level training and test partition that keeps replicate sca...
  </details>

- **2026-09-21** — Ali Rezagholizadeh, Soheila Samiee — [Extending FunctionGemma for Practical On-Device Mobile Function Calling](http://arxiv.org/abs/2609.25373v1)
  <details><summary>📄 Abstract</summary>
  On-device assistants require function-calling models that map natural language to local system actions, but existing resources emphasize web APIs or narrow mobile-action catalogs. We extend FunctionGemma 270M-it to practical Android workflows by introducing MOBILEACTIONSEXTENDED, a synthetic, schema-validated dataset of ~9,500 conversations covering fifteen device-control categories, including messaging, phone calls, camera/screenshot, brightness control, device-status queries, flashlight contro...
  </details>

- **2026-09-21** — Hemn Khdr, Mohammad Noaeen, Karim Keshavjee et al. — [MedGate-Fusion: Integrating First-Encounter Semantic Narratives and Physiological Biomarkers for Prospective Stroke Risk Stratification](http://arxiv.org/abs/2609.25272v1)
  <details><summary>📄 Abstract</summary>
  Prospective stroke risk stratification in primary care is challenging because early risk signals are distributed across routine biomarkers and unstructured clinical narratives. We propose MedGate-Fusion, a multi-modal gated architecture that integrates transformer-based embeddings of first-encounter narratives with ten routinely recorded risk markers. We used electronic medical record data from the Canadian Primary Care Sentinel Surveillance Network (CPCSSN). Starting from 808,921 encounter-leve...
  </details>

- **2026-09-21** — He Hu, Yucheng Zhou, Qianning Wang et al. — [From Pattern Recognizers to Personalized Companions: A Survey of Large Language Models in Mental Health](http://arxiv.org/abs/2609.25186v1)
  <details><summary>📄 Abstract</summary>
  The rising global prevalence of mental health conditions, together with longstanding barriers in traditional healthcare, such as limited resources, high cost, stigma, and privacy concerns, has created an urgent need for accessible and scalable support. Large Language Models (LLMs) have emerged as a transformative technology with strong potential to democratize mental health support through advanced natural language understanding and generation. However, the rapidly expanding, fragmented body of ...
  </details>

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
*滥用与误用 / Misuse & Abuse* — 10 papers

- **2026-09-22** — Alexandros Fourtounis, Emmanouil Papadogiannakis, Panagiotis Papadopoulos et al. — [COBRA: A Content-Agnostic Framework for Zero-Day Detection of Suspicious Domains](http://arxiv.org/abs/2609.25882v1)
  <details><summary>📄 Abstract</summary>
  The use of malicious domains is central to cyberattacks such as phishing, malware distribution, impersonation, and fraudulent transactions. Because domains are inexpensive to register and easy to deploy at scale, they remain one of the most common and damaging tools used in cybercrime across industries. Proactive detection is essential to reducing this window of vulnerability and preventing harm to users. In this work, we propose COBRA: a content-agnostic, registration-time detection framework f...
  </details>

- **2026-09-22** — Peachapong Poolpol, Henrik H. J. Detjen, Eike Petersen — [Faithful Faithfulness Evaluations: Challenges & Pitfalls Learned from a Breast MRI Case Study](http://arxiv.org/abs/2609.25978v1)
  <details><summary>📄 Abstract</summary>
  Saliency maps are widely used to explain deep learning predictions in medical imaging, yet visually plausible explanations do not necessarily reflect a model's true decision process and may therefore mislead clinicians. We investigate this problem using a Vision Transformer-based breast MRI classifier trained on the ODELIA Breast MRI Challenge dataset and evaluate multiple saliency methods, including Last-layer Attention, Attention Rollout, Grad-SAM, Gradient Attention Rollout, GMAR, Grad-CAM, a...
  </details>

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


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-09-20** — Heewon Baek, Alsharif Abuadbba, Kristen Moore et al. — [Connecting the Dots in Agentic AI Security: A Cross-Dimensional Threat Taxonomy, Evaluation Maturity, and Open Challenges](http://arxiv.org/abs/2609.23894v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI extends LLM security beyond generated content to persistent state, autonomous actions, tool use, and interactions with humans and other agents. Existing threat classifications often emphasize individual dimensions, obscuring connections among entry points, affected components, and security consequences. The known threat landscape also differs from the coverage demonstrated by empirical research. Through a structured review of 66 studies published from 2022 to 2026, we introduce T={S, ...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 54 papers

- **2026-09-22** — Yanshuo Bai, Kanji Tanaka — [TM-APR: Thermal Temporal-Memory Localization via Analytic Online Adaptation](http://arxiv.org/abs/2609.26766v1)
  <details><summary>📄 Abstract</summary>
  Thermal Visual Place Recognition (Thermal VPR) maps camera observations to metric poses within a mapped environment, serving as a prerequisite for autonomous navigation. However, thermal VPR suffers from severe environmental dependence, heavy online retraining overheads, and an inability to model dynamic non-linear shifts, causing existing frameworks to fail during online deployment. To achieve robust domain-invariant place recognition, we bridge Analytic Class-Incremental Learning (ACIL) with d...
  </details>

- **2026-09-22** — Om Nepal, Sushant Aryal, Oluseyi Olukola et al. — [Metrics Failure in LLM-Based Code Vulnerability Repair: An Empirical Study and a Change-Aware Screen](http://arxiv.org/abs/2609.26749v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly applied to the automated repair of C/C++ security vulnerabilities, and compile rate is a commonly reported proxy for progress: whether the generated patch compiles. We argue that compile rate is a scientifically unreliable metric for single-function vulnerability repair, and we support this with five controlled experiments over 203 vulnerable functions from Big-Vul, three open-source code LLMs (350M to 6.7B parameters), and three prompting strategies...
  </details>

- **2026-09-22** — Yuxin Bao, Hongwei Ruan, Luobin Wang et al. — [NavSafe-$\infty$: Benchmarking Closed-Loop Driving Safety in Photorealistic Environments](http://arxiv.org/abs/2609.26618v1)
  <details><summary>📄 Abstract</summary>
  End-to-end (E2E) driving policies have progressed rapidly on open-loop (OL) benchmarks, yet OL evaluation cannot reveal whether a policy withstands compounding errors, recovers from failures, or interacts safely with surrounding actors. We introduce NavSafe-$\infty$, a photorealistic closed-loop (CL) benchmark of 280 scenarios spanning 28 event types, each with success and failure criteria defined within a structured traffic-safety taxonomy, which yields category-level capability scores for Traf...
  </details>

- **2026-09-22** — Arthur Cordeiro, Alberto Maria Mongardini, Emmanouil Vasilomanolakis — [Rouxii: Exploiting Honeypots with Deception-Aware AI Pentesters](http://arxiv.org/abs/2609.26555v1)
  <details><summary>📄 Abstract</summary>
  Honeypots are designed to deceive attackers, and recent work shows they can also derail autonomous LLM-based pentesters. These evaluations, however, largely consider attackers unaware of the deception they face. We study the opposite setting: an autonomous attacker explicitly equipped to recognize and act on honeypot fingerprints. We introduce Rouxii, an AI-driven penetration-testing framework that integrates counter-deception into reconnaissance and pivots from honeypot detection to exploitatio...
  </details>

- **2026-09-22** — Xin Shen, San-Zhuo Xi, Yali Du et al. — [On the Lexical Superstition of Large Language Models for Code Comprehension: Re-evaluation on Code of Low Lexical Quality](http://arxiv.org/abs/2609.26388v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models (LLMs) have made them widely used for code-related tasks. Identifier names are statistically informative in naturally occurring code, but their information is not always reliable. We investigate whether current LLMs assign disproportionate weight to lexical cues when renaming preserves program structure. We introduce Face/Off, a semantics-preserving identifier-renaming framework, and evaluate progressive naming conditions across multiple models and code-c...
  </details>

- **2026-09-22** — Vansh Wahi — [Optimizing the Score, Losing Sight of the Task: Reward Hacking Across Weights, Selection, and Prompts](http://arxiv.org/abs/2609.25848v1)
  <details><summary>📄 Abstract</summary>
  A higher evaluation score does not always mean a better language model system. When optimization exploits an evaluator's mistakes, measured progress can conceal unchanged or deteriorating task performance. This failure can arise through parameter updates, selection among generated outputs, or revisions to persistent prompts. We develop a comparative framework for reward hacking across these three optimization substrates: weights, selection, and text. Building on the Proxy Compression Hypothesis ...
  </details>

- **2026-09-22** — Aleksandr V. Petrov, Nathan Stein, Erik Lybecker et al. — [Robust Fusion of Semantic and Behavioural Signals for LLM Reranking in Personalised Search](http://arxiv.org/abs/2609.25825v1)
  <details><summary>📄 Abstract</summary>
  Personalised search must satisfy query intent while incorporating user context and historical interactions. LLM-based cross-encoders provide a single reranking interface, but injecting predictive behavioural statistics into their prompts can encourage shortcut learning: reliance on historical signals at the expense of semantic and user-context patterns that generalise to sparse or unseen searches.   We study this problem in the personalised search system of a large-scale audio streaming platform...
  </details>

- **2026-09-22** — Yuanteng Chen, Qiwei Lai, Chen Tianqi et al. — [You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs](http://arxiv.org/abs/2609.25809v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained mixture-of-experts (MoE) architectures have become a mainstream design for open-weight LLMs, with hundreds of experts and increasingly many selected per token. This shift makes dynamic expert pruning an attractive route to cheaper inference. Yet existing evidence comes largely from coarser architectures and likelihood-scored multiple-choice benchmarks, leaving three central questions open in the fine-grained regime: how redundant per-token expert selection is, how effectively existi...
  </details>

- **2026-09-22** — Jongjin Baek, Won Ji, Seungjae Yoo et al. — [Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving](http://arxiv.org/abs/2609.25782v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) serving is increasingly agentic, with multi-turn sessions that idle between actions yet must retain their full context. Limited GPU memory capacity forces inactive KV states to be evicted, so resuming a session incurs either costly recomputation or slow interconnect transfers. To address this, high bandwidth flash (HBF)-an on-package 3D-NAND memory offering orders-of-magnitude greater capacity than high bandwidth memory (HBM) at comparable read bandwidth-has emerged as...
  </details>

- **2026-09-22** — Zheng Chen, Yuzhu Li, Haoxuan Li et al. — [TCMaster: Confidence-Aware Querying and Workload-Guided Physical Design for Multi-Source Traditional Chinese Medicine Knowledge Graphs](http://arxiv.org/abs/2609.25712v1)
  <details><summary>📄 Abstract</summary>
  Multi-source knowledge graphs (KGs) need query mechanisms that expose reliability and exploit domain structure. This paper presents TCMaster, a property-graph query substrate for confidence-aware traversal and workload-guided physical design over Traditional Chinese Medicine KGs. TCMaster integrates pharmacopoeias, prescriptions, molecular databases, and LLM-extracted micro-semantics into a KG with approximately 221K entities and 723K base edges. It annotates edges with provenance-level confiden...
  </details>

- **2026-09-22** — Maria Damanaki, Nikos Piperigkos, Alexandros Gkillas et al. — [CDKF-Track: Cluster-aware Data-Driven Kalman Filtering for Cooperative 3D Multi-Object Tracking](http://arxiv.org/abs/2609.25668v1)
  <details><summary>📄 Abstract</summary>
  Multi-Object Tracking (MOT) is essential for EdgeAI perception systems, where accurate object localization and reliable identification enable safe decision-making. Singleagent MOT suffers from occlusions, sensor noise, and partial scene understanding in complex real-world scenarios. While multi-agent systems improve robustness by exploiting shared information, they introduce redundant measurements that lead to false data associations, and still struggle to capture nonlinear object dynamics. To a...
  </details>

- **2026-09-22** — Junyoung Jang, Gwanhyun Lee, Hwiwon Lee et al. — [Evaluating Coding Agents on Kernel Exploit Generation](http://arxiv.org/abs/2609.25591v1)
  <details><summary>📄 Abstract</summary>
  Coding agents now find real vulnerabilities in production software. However, bug discovery results do not measure whether agents can construct exploit primitives. We introduce KEX-bench, a benchmark for evaluating coding agents on exploit primitive generation against real operating-system kernels. KEX-bench contains 45 task instances across 40 Linux and Windows CVEs, covering kernel address leak, instruction-pointer control, heap read, heap write, and arbitrary address write. Each task runs in a...
  </details>

- **2026-09-22** — Dahlia Shehata, Ming Li — [Recovering Agentic Sovereignty: Mitigating the Consensus Paradox via Contrastive Epistemic Decoding](http://arxiv.org/abs/2609.25570v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit a parametric vulnerability to adversarial swarm consensus. To mitigate this sycophancy, we introduce Contrastive Epistemic Decoding (CED), a zero-shot inference intervention. Unlike standard Contrastive Decoding (CD) which relies on a weaker secondary model, CED utilizes a dual forward-pass on a single architecture to isolate conformity bias. By introducing a novel asymmetric, zero-bounded probability clamp and discrete top-k truncation mask, CED mathematical...
  </details>

- **2026-09-21** — Jianzhe Lin, Xiaolin Li, Fei Wang et al. — [Clarification Is Not Correction: LLMs Fail to Let Go](http://arxiv.org/abs/2609.25337v1)
  <details><summary>📄 Abstract</summary>
  Dialogue failures in language models are usually framed as memory failures: context too long, summaries lossy, a constraint forgotten. We argue this misses a deeper problem: in many conversations the model does not forget, it commits too early. An ambiguous early turn collapses into a single hidden interpretation, and later clarification is filtered through that commitment. We call this early posterior collapse: unresolved user intent collapsing into a committed task state before ambiguity is re...
  </details>

- **2026-09-21** — Qixin Zhang, Ajay Kumar, Zhi-Li Zhang — [Multi-Agent Video Prediction: Self-Correcting Conditional Frames for Dynamic Scene Forecasting](http://arxiv.org/abs/2609.25302v1)
  <details><summary>📄 Abstract</summary>
  Transmission latency significantly degrades user quality of experience in real-time interactive perception systems. In remote driving, maintaining reliable visual feedback is critical for safe operation under dynamic network variability. Although video prediction offers a promising approach to compensate for short-term transmission delays and approximate near-zero-latency streaming, prediction-only methods remain vulnerable in highly dynamic scenes, especially when newly emerged objects appear d...
  </details>

- **2026-09-21** — Jianhui Zhang, Ahmed Salem, Robert Tidswell et al. — [Silk-templated Nanostrips as Superprotonic Fibre Sensors](http://arxiv.org/abs/2609.25293v1)
  <details><summary>📄 Abstract</summary>
  Transforming textile fibres into sensors can facilitate continuous physiological monitoring for improving human healthcare. Coating fibres with electronic conductors can help detect physiological stimuli but their sensitivity scales with thickness and often lowers the fibre mechanical flexibility. Proton conductors are potential alternatives; however, they suffer from fragile physical interfaces, and sluggish kinetics. Here, we report a bio-templated, scalable strategy to create superprotonic in...
  </details>

- **2026-09-21** — Ariel Flint, Luca Maria Aiello, Sara M. Constantino et al. — [Indirect tipping: a social attack surface in AI agent populations](http://arxiv.org/abs/2609.25194v1)
  <details><summary>📄 Abstract</summary>
  As generative AI agents are deployed at scale, safety will depend not only on technical safeguards and individual model design, but also on collective equilibria that determine how agent populations process information, prioritize actions, and respond to uncertainty. Yet the same equilibria that enable agents to coordinate also create a social attack surface. The standard framework to assess this vulnerability is critical mass dynamics: the minimum fraction of adversarial agents required to over...
  </details>

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

- **2026-09-20** — Benjamin Walder, Markus Haltmeier, Lukas Neumann et al. — [ELIPPS: Exact Learning for Inverse Problems from Partial Self-supervision](http://arxiv.org/abs/2609.23683v2)
  <details><summary>📄 Abstract</summary>
  In undersampled inverse problems (such as sparse-view computed tomography), only a small number of measurements are collected, which reduces radiation exposure and acquisition time and cost, and can also address the inaccessibility of certain acquisition arrangements. Most learning-based methods for such problems require supervision in the form of fully sampled measurements and ground-truth images, which are costly or even infeasible to acquire. To overcome this issue, we propose \emph{Exact Lea...
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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 60 papers

- **2026-09-22** — Abel A. Reyes-Angulo, Henry O. Velesaca, Steven Araujo — [SambaGraph: Action-Reaction Spatio-Temporal Graphs for Soccer Tactical Response Modeling](http://arxiv.org/abs/2609.25569v1)
  <details><summary>📄 Abstract</summary>
  Soccer tactics are interactive: an attacking action changes the opponent's defensive problem, and the observed response depends on the multi-agent match state. We introduce SambaGraph, an action--reaction spatio-temporal graph dataset and benchmark for soccer tactical response modeling. From tracking and event data for all 64 matches of the 2022 FIFA World Cup, we curate 4,070 action-centered episodes represented as temporally aligned 23-node player--ball graph sequences with attack/defense view...
  </details>

- **2026-09-22** — Quan Nguyen-Tri, Mukul Ranjan, Zhiqiang Shen — [Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs](http://arxiv.org/abs/2609.26796v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive LLMs by enabling non-autoregressive text generation. However, their practical deployment remains limited by inefficient inference, largely due to the absence of effective Key-Value (KV) caching and scalable parallel decoding mechanisms. Existing acceleration methods typically study KV caching and parallel decoding in isolation, overlooking the I/O bottlenecks that arise when cache reuse and...
  </details>

- **2026-09-22** — Linman Wang, ZiFei Zhang, Chunran Zheng et al. — [DIFTA-3D: Depth-Consistent Instance-Level Feature Transfer and Adaptation of DINOv3 for 3D Detection](http://arxiv.org/abs/2609.26702v1)
  <details><summary>📄 Abstract</summary>
  RGB-D 3D instance detectors benefit from visual semantics, but the task-specific Faster R-CNN/ResNet branch used by IIFNet3D couples feature extraction to a separately trained 2D detector and its image-domain labels. Replacing that branch with a frozen vision foundation model removes this task-specific dependency, but may introduce occlusion noise and a mismatch between patch features and geometry-aware detection features. In this work, we investigate this replacement through an adaptation of DI...
  </details>

- **2026-09-22** — Nathalie Baracaldo — [From Alignment to Access Control: A Framework for GenAI Policy Enforcement](http://arxiv.org/abs/2609.26682v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) applications have flourished enabling users to chat with large language models, and to create agents to act on their behalf for a variety of tasks. The pace of development of capabilities in this field is incredibly fast with security and safety taking a back seat. Unfortunately, the slower pace at which security and safety mechanisms have evolved has led to real incidents. Policy enables the definition of desirable behavior of applications, and for that reason, it is a cor...
  </details>

- **2026-09-22** — Hoang-Lam Huynh, Quoc-Cuong Tang, Van-Tri Phan et al. — [Design and Evaluation of a Controlled Post-Alert Incident Orchestration and Response Subsystem Using a Rule Engine and a Local Large Language Model](http://arxiv.org/abs/2609.26316v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a controlled post-alert incident orchestration and response subsystem for educational information systems. The architecture separates deterministic classification, contextual analysis, human approval, and technical execution. A Rule Engine determines severity and selects the playbook, while Static RAG and a local large language model provide advisory content under Validator, Guardrail, Output Sanitizer, and Safe Fallback controls. Experiments begin after simulated alerts are ...
  </details>

- **2026-09-22** — Elie Abboud, Oren Gal — [MATES: Learning Multi-Agent Interactions by Transforming Observations for Frozen Single-Agent Policies](http://arxiv.org/abs/2609.26010v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reinforcement learning (MARL) commonly trains decentralized policies from scratch, requiring agents to acquire individual task competence and coordination simultaneously. Yet many multi-agent problems admit a compatible single-agent counterpart in which the underlying task can be learned in isolation. We introduce Multi-Agent Observation Transformation for Existing Single-Agent Policies (MATES), an input-side adaptation framework for tasks whose multi-agent observations preserve the ...
  </details>

- **2026-09-22** — Baher Mohammad, Ammar Ali, Stamatios Lefkimmiatis — [GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression](http://arxiv.org/abs/2609.25963v1)
  <details><summary>📄 Abstract</summary>
  Transformer architectures exhibit cross-layer redundancies, yet post-training compression pipelines typically optimize layers in isolation or rely on heuristic grouping strategies that disregard layer-specific activation geometries. We introduce a principled, training-free framework that sequentially optimizes cross-layer weight pairings and shared-dictionary factorizations. Rather than forcing weights of adjacent layers to share a basis or heuristically merging activation statistics, our approa...
  </details>

- **2026-09-22** — Malsha Ashani Mahawatta Dona, Konstantinos Rokanas, Alexander Säfström et al. — [Towards Systematic Qualification of Vision-Language Models for Automotive Perception Systems](http://arxiv.org/abs/2609.25945v1)
  <details><summary>📄 Abstract</summary>
  The field of Artificial Intelligence has been adopted for many application domains. Vision Language Models are one of the recently advanced AI techniques that have been explored to support automotive features such as vehicle perception, and safety assurance. However, such language models are prone to hallucinations, posing a potential threat to the safety of automotive systems that may incorporate them. Within the automotive domain, VLMs could not only hallucinate traffic objects, but could also...
  </details>

- **2026-09-22** — Weijie Zhou, Zhaoyang Zhang, Zhixian Kong et al. — [MIMO-OFDM AI Receiver Based on Incrementally Conditioned Diffusion with Soft Decision](http://arxiv.org/abs/2609.25923v1)
  <details><summary>📄 Abstract</summary>
  Conventional iterative receiver usually begins with channel estimation using sparse pilot observations and follows with data detection based on the channel estimates, and then updates channel estimation using decision feedback, and so on. In Artificial Intelligence (AI)-based receiver design, it is also crucial to make use of such progressively enriched data observations to enhance the generative channel estimation. However, the statistical characteristics and reliability of the data decisions a...
  </details>

- **2026-09-22** — Massimiliano Sassoli de Bianchi, Roberto Leporini — [Reply to comments arXiv:2512.07881 and arXiv:2601.06104 on quantum structure in human and AI-generated language](http://arxiv.org/abs/2609.25797v1)
  <details><summary>📄 Abstract</summary>
  We reply to the comments by M. Sienicki and K. Sienicki (arXiv:2512.07881) and by K. Sienicki (arXiv:2601.06104) on our work on quantum-mechanical statistics in human language (arXiv:2407.14924) and on quantum structure in AI-generated language (arXiv:2511.21731). We thank the authors for their careful reading and address what we consider to be the main points of criticism: the exploratory nature of the protocol used in the experiments with large language models; the role of marginal-law violati...
  </details>

- **2026-09-22** — Zheng Chen, ZhiCheng Du, Haoxuan Li et al. — [Syndrome, Synergy, and Safety: Structured Reasoning and Knowledge-Driven Alignment for TCM Prescription Generation](http://arxiv.org/abs/2609.25755v1)
  <details><summary>📄 Abstract</summary>
  Applying large language models to Traditional Chinese Medicine (TCM) prescription generation reveals three clinically critical gaps: models produce end-to-end mappings without auditable reasoning following the li-fa-fang-yao paradigm (SR Gap), treat each encounter in isolation without follow-up adjustment via sui zheng jia jian (LA Gap), and fail to enforce absolute contraindication rules such as Shi Ba Fan (SC Gap). We propose a progressive four-stage framework (SFT $\to$ PG-CoT $\to$ Dynamic $...
  </details>

- **2026-09-22** — Ansgar Steland — [Context-Adaptive Thresholding for Conditionally Representative Monitoring and Classification](http://arxiv.org/abs/2609.26652v1)
  <details><summary>📄 Abstract</summary>
  Commonly, classifiers and monitoring procedures are trained from labeled data by optimizing an objective such as the misclassification rate. This may lead to unrepresentative conditional distributions of the outcome (the labels) given important external variables, different from the conditional laws in the population. We show how to modify any given threshold-type classifier resp. monitoring rule to achieve representative conditional label prediction by using adapting the threshold to a covariat...
  </details>

- **2026-09-22** — Peiying Zhu, Sidi Chang — [When Are Aggregate Agent Traces Diagnosable? Traffic-Governed Interpretation and Calibrated Abstention](http://arxiv.org/abs/2609.25806v1)
  <details><summary>📄 Abstract</summary>
  Runtime traces can appear transparent, but a closed-loop policy determines which states are visited and which failures become visible. We study a simulated hotel-pricing agent mapping time, inventory, and market state to discrete price actions under varying demand regimes. A fault may leave no aggregate trace when the policy rarely visits affected cells. We treat entry into aggregate-only fault interpretation as a diagnosability decision preceding scoring or localization. A reference-map gate re...
  </details>

- **2026-09-22** — Charis Y. N. Chiang, Tarela Sarimiye, Adeyinka Ashaye et al. — [Interpretable AI plus Handheld, Portable Retinal Photographs: A Low-Cost Glaucoma Screening Solution for West Africa](http://arxiv.org/abs/2609.25697v1)
  <details><summary>📄 Abstract</summary>
  Purpose: To develop and evaluate an interpretable artificial intelligence (AI) framework for glaucoma screening from low-cost portable, handheld retinal fundus photographs in a West African population and to compare its performance with clinical tabletop fundus imaging. Methods: We used data from a community-based study of 681 participants (1,362 eyes) in Nigeria, comprising 414 glaucoma, 478 glaucoma suspect, and 470 non-glaucoma eyes. Fundus photographs were acquired using the low-cost handhel...
  </details>

- **2026-09-21** — Chetan Pathade, Prathamesh Pawar, Shubham Patil — [Attack Success Rate Is Not a Number: On Measurement Validity in Agentic AI Security Evaluation](http://arxiv.org/abs/2609.25173v1)
  <details><summary>📄 Abstract</summary>
  Attack success rate (ASR) is the headline metric in nearly every published evaluation of attacks on, and defenses for, LLM agents. We argue that ASR as currently used is not a single quantity but a family of metrics parameterized by six design choices that papers seldom specify and never hold constant across the literature. We support this with two studies that require no proprietary access. First, a full-text meta-analysis of 259 agentic-security papers posted to arXiv between February 2025 and...
  </details>

- **2026-09-21** — Jacob Charnock, Sophie Williams, Zaheed Kara et al. — [Embedded Assessments for Frontier AI](http://arxiv.org/abs/2609.25413v1)
  <details><summary>📄 Abstract</summary>
  Third-party evaluations for frontier AI have mostly tested models through external interfaces before deployment. But the risks from frontier AI models depend on how their developers use and govern them internally. Recently, CEOs of frontier AI companies have committed to hosting embedded assessments. These assessments would give independent evaluators employee-like access to a developer's internal systems, staff, and documentation. First, we argue that this can enable deeper and more flexible as...
  </details>

- **2026-09-21** — Aakash Patel, Panos Ketonis, Shreya Saxena et al. — [The AI Neuroscientist: An Interactive Agentic Interface for Neuroimaging Analysis](http://arxiv.org/abs/2609.25254v1)
  <details><summary>📄 Abstract</summary>
  Analyzing neuroimaging data requires specialized coding and statistical expertise, which limits accessibility for researchers without computational backgrounds. We present the AI Neuroscientist, a language agent for interactive data exploration. The system integrates a large language model (LLM) with a neuroimaging toolset to perform quality control, modeling, and visualization. This allows researchers to query data quality and specify analysis parameters directly in natural language, providing ...
  </details>

- **2026-09-21** — Sepideh Hodaeian, Zhenhao Li, An Ran Chen — [TAILOR: Template-Preserving Augmentation for Long-Tailed Log Parsing](http://arxiv.org/abs/2609.25261v1)
  <details><summary>📄 Abstract</summary>
  Log parsing is essential for system log analysis because it supports tasks such as debugging, monitoring, and anomaly detection by transforming unstructured log messages into structured log templates. However, real-world log datasets exhibit highly imbalanced, long-tailed distributions, where a small number of frequent templates dominate while many rare templates appear only a few times. This imbalance causes evaluation results to be overly optimistic by allowing frequent templates to dominate b...
  </details>

- **2026-09-21** — Lifu Mu, Shuai Chen, Wen Zheng et al. — [LiAuto-MindViT: A Hybrid Vision Backbone with Adaptive Bidirectional Mamba](http://arxiv.org/abs/2609.24337v2)
  <details><summary>📄 Abstract</summary>
  While Mamba-based models have shown strong potential for long sequence modeling, adapting them to vision is challenging due to the requirement of local neighborhood correlations and multi-directional spatial contexts for visual understanding. In this paper, we present LiAuto-MindViT, a novel hybrid vision backbone that synergizes the strengths of CNNs, Mamba, and Transformers. The core of our design is the Adaptive Bidirectional Mamba (ABM), which eliminates the directional bias of unidirectiona...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 57 papers

- **2026-09-22** — Han Chen, Hanchen Wang, Hongmei Chen et al. — [HYDRA: Proactive Android Malware Drift Adaptation via Hierarchical Graph Contrastive Learning](http://arxiv.org/abs/2609.26352v1)
  <details><summary>📄 Abstract</summary>
  Concept drift, driven by the rapid evolution of Android malware, severely degrades the performance of machine learning detectors. Current adaptation strategies are often reactive, responding only after performance has dropped and imposing a significant manual annotation burden, or they are proactive but rely on unstable adversarial training and incomplete, single-level graph representations. To overcome these limitations, we propose HYDRA (Hybrid Drift Adaptation), a proactive adaptation framewo...
  </details>

- **2026-09-22** — Shufan Sun, Chen Wang, Enxin Song et al. — [HARMONY: Hierarchical Agentic Reasoning for MONocular Image-to-Scene Synthesis](http://arxiv.org/abs/2609.26793v1)
  <details><summary>📄 Abstract</summary>
  Compositional 3D scene reconstruction has recently been explored from two directions: agentic reasoning that provides semantic understanding of spatial relationships but lacks precise alignment with input images; and visual geometry foundation models that predict dense point maps from input images but the reconstruction quality is limited. Therefore, recovering a complete 3D scene from a single monocular image with accurate inter-object relationships and high-fidelity reconstruction quality rema...
  </details>

- **2026-09-22** — Fang Wang, Huitao Li, Wenhan Chao et al. — [GAD-MambaUNet: Direction-Group Mamba with Gradient-Adaptive DINOv3 Distillation for Lightweight Medical Image Segmentation](http://arxiv.org/abs/2609.26729v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we proposed GAD-MambaUNet, a lightweight medical image segmentation network that combines efficient local modeling, direction--group state-space interaction, and training-time foundation-model supervision. To improve contextual modeling in compact segmentation networks, we introduced Direction-Group Graph Selective Scan (DG-GSS), which treated scan-direction and channel-group responses as graph nodes and enabled structured information exchange before multi-directional fusion. We f...
  </details>

- **2026-09-22** — Xiaoyu Yang, Jie Lu, Wei Duan et al. — [The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence](http://arxiv.org/abs/2609.26718v1)
  <details><summary>📄 Abstract</summary>
  Long-context LLMs focus on retrieving distant evidence from extensive context, yet existing work has largely focused on overcoming distance alone. In this work, we identify the Proximity Trap, insufficient attention to distant evidence often arises less from distance itself than from cumulative competition with abundant, task-irrelevant proximal background. To address the Proximity Trap, we introduce LYRA (Long-context heavY-tailed Relevance Alignment), a t-distributed directional matching mecha...
  </details>

- **2026-09-22** — Fiona Kekwick, Matthew Baugh, Bernhard Kainz et al. — [MMAP: Multimodal Missing-Aware Pretraining for Longitudinal Alzheimer's Prediction](http://arxiv.org/abs/2609.26617v1)
  <details><summary>📄 Abstract</summary>
  Clinical decision making heavily relies on predicting the disease progression trajectory by seeking to understand patient's health status which is characterised by multimodal medical data. AI holds great potential for learning useful representations from multimodal medical data to predict disease progression and aid clinical decision making. However, development of predictive AI models is constrained by missing modalities and incomplete tabular data frequently occurring in medical datasets. In a...
  </details>

- **2026-09-22** — Lorenzo Zangari, Davide Picca — [A Semiotics-Aware Framework for Evaluating Fidelity and Coverage in Natural Language Generation](http://arxiv.org/abs/2609.26527v1)
  <details><summary>📄 Abstract</summary>
  When two texts describe the same expression, standard metrics based on lexical overlap or whole-text similarity may fail to detect meaningful differences in how that expression is framed. We propose a framework to evaluate semiotic alignment between texts, where a semiotic profile encompasses both the contextual meaning and the discourse references made salient by a text. Our approach yields two scores, Semiotic Fidelity and Semiotic Coverage, estimating how much of one text's profile is support...
  </details>

- **2026-09-22** — Mario Sanz-Guerrero, Katharina von der Wense — [Calibration as a First-Class Criterion in LLM Evaluation](http://arxiv.org/abs/2609.26489v1)
  <details><summary>📄 Abstract</summary>
  Calibration of language models -- the alignment between expressed or implicit confidence and empirical correctness -- is a well-studied subfield within NLP. Methods to measure it already exist. The problem is adoption: outside this subfield, NLP research regularly introduces new models, datasets, and benchmarks without checking whether the model's confidence scores are meaningful. We argue that this adoption gap is a major obstacle to trustworthy LLM evaluation. Miscalibration causes problems in...
  </details>

- **2026-09-22** — Junlong Wu, Zijun Li, Yuting Hu et al. — [KwaiMind Technical Report](http://arxiv.org/abs/2609.26375v1)
  <details><summary>📄 Abstract</summary>
  Commercial image editing requires product identity preservation, accurate text rendering, and user appeal alongside general editing quality. We present KwaiMind, an image editing system combining general capabilities with e-commerce specialization. An agent-based data engine maintains approximately 1.8 million high-quality editing pairs. Built on a multimodal diffusion transformer, KwaiMind undergoes continued pre-training and supervised fine-tuning, followed by preference optimization and onlin...
  </details>

- **2026-09-22** — Jiayan Fu, Hang Xu, Yong Zhang et al. — [PACT: From Credit Assignment to Critic Alignment](http://arxiv.org/abs/2609.26355v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has become a central component of large language model (LLM) post-training, yet token-level credit lacks a generally accepted mathematical definition, leaving its relationship to commonly used training signals unclear. We formulate three regularity conditions, namely Completeness, Prefix Consistency, and Neutrality, and prove that they uniquely determine token-level credit. This characterization provides a unified basis for explaining phenomena across existing algorithms a...
  </details>

- **2026-09-22** — Masoud Soleimani — [Target alignment, dilution and forecast selection when cross-sectional forecasts share a common target](http://arxiv.org/abs/2609.26303v1)
  <details><summary>📄 Abstract</summary>
  Forecasters often score the same units per date against one standardized realized outcome. We show that every standardized forecast splits exactly into a component aligned with this common target and a component uncorrelated with it. Three consequences follow: forecast-error correlation largely mirrors forecast correlation and is therefore a poor measure of diversity; an equally weighted combination beats a no-information forecast only when average alignment is large relative to the combination'...
  </details>

- **2026-09-22** — Yan Zhang, Pei Fu, Daiqing Wu et al. — [Towards Omni-dimensional GUI Agent Navigation with Masked Trajectory Prediction](http://arxiv.org/abs/2609.25769v1)
  <details><summary>📄 Abstract</summary>
  Graphical User Interface (GUI) Agents autonomously interact with software to fulfill user requests, where GUI navigation stands out as the most critical and challenging capability. Mastering this capability demands a complex synergy of step-wise decision-making, state-action alignment, and long-horizon planning. While directly mixing these corresponding navigation tasks seems intuitive to simultaneously acquire these skills, such a direct combination is severely bottlenecked by inconsistent opti...
  </details>

- **2026-09-22** — Rojin Ziaei — [The Limits of Simulated Societies: How Post-Training and Survey Fine-Tuning Erase Cross-Cultural Variance](http://arxiv.org/abs/2609.25760v1)
  <details><summary>📄 Abstract</summary>
  Using large language models (LLMs) to simulate diverse human populations has the potential to transform many aspects of computational social science, yet many evaluations score the average response rather than the spread of opinion within real groups. Here, we develop a diagnostic framework that measures point accuracy alongside dispersion retention, the ratio of predicted to human standard deviation ($\dr$), on 10{,}000 respondent--question pairs from the World Values Survey (WVS) spanning twel...
  </details>

- **2026-09-22** — Dingkang Yang, Yizhou Liu, Wendong Cheng et al. — [Fysiverse-3D-Vision Technical Report: Generating Executable 3D Worlds from Images through Unified Spatial Reasoning](http://arxiv.org/abs/2609.25741v1)
  <details><summary>📄 Abstract</summary>
  Generative models have advanced image-conditioned 3D content creation, yet generating controllable and executable 3D scenes from a single image remains challenging. Existing 3D generative approaches can synthesize visually plausible objects and scenes, but their spatial layout estimation is coupled with specific asset generators. They struggle to jointly model object semantics, metric geometry, and scene-level spatial relationships, which are essential for interactive editing, physical simulatio...
  </details>

- **2026-09-22** — Adam Ousherovitch, Ambuj Tewari — [Direct Optimization of Generators for Search in Automated Theorem Proving](http://arxiv.org/abs/2609.25575v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuned Large Language Models (LLMs) significantly advance Automated Theorem Proving (ATP), but are often deployed as guiding policies within tree search rather than for single-attempt generation. Recent work shows cross entropy is suboptimal for an LLM used in flat search strategies such as aggregation or filtering and that work has developed new loss functions to correct this misalignment. Extending this alignment to tree search is more challenging: proof discovery depends on exploration an...
  </details>

- **2026-09-22** — Jinu Pahk, Jesoon Kang, Taegeon Park et al. — [HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery](http://arxiv.org/abs/2609.25558v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action policies benefit from geometric supervision, but current-frame geometry alone does not explicitly describe the changes associated with manipulation. This design is motivated by the goal of learning an embodiment-agnostic visual interface that can be pretrained across robot and egocentric video before robot-specific action alignment. We introduce Geometry-Change VLA (GC-VLA), which learns to predict multiview future-current geometry-change tokens from current observations. ...
  </details>

- **2026-09-22** — Dhruv Srikanth, Bingchen Zhao, Dixing Xu et al. — [Recursive self-improvement of AI research agents](http://arxiv.org/abs/2609.26457v1)
  <details><summary>📄 Abstract</summary>
  AI agents are beginning to automate research and development across the AI stack, from improving training efficiency to optimizing inference. A natural next step is to improve the research efficiency of the agents themselves. When an AI research agent's own code is the object of optimization, each accepted rewrite becomes the agent that the next round edits. We refer to this loop as recursive self-improvement. Its significance lies in a long-standing trend, in which increased cumulative spending...
  </details>

- **2026-09-21** — Chankyo Kim, Minghan Zhu, Tzu-Yuan Lin et al. — [GINIO: A Geometric SO(3)-Equivariant Interface for Neural Inertial Odometry](http://arxiv.org/abs/2609.25338v1)
  <details><summary>📄 Abstract</summary>
  Neural inertial odometry increasingly uses networks as learned measurements inside filtering pipelines. Such measurements should transform consistently under arbitrary IMU mounting conventions: their mean must transform as a vector, and their covariance must transform congruently as a second-order tensor. We present GINIO, a geometric SO(3)-equivariant interface for neural inertial odometry under arbitrary rotations of the IMU measurement frame. Given calibrated IMU windows, our framework predic...
  </details>

- **2026-09-21** — Yusser Al Ghussin, Eva Gavaller, Cristina España-Bonet et al. — [FineWeb-CLaR: Culture, Language, and Region Annotations for Benchmark-Aligned Corpus Auditing](http://arxiv.org/abs/2609.25298v1)
  <details><summary>📄 Abstract</summary>
  Cultural evaluation coverage and robustness in language models are difficult to diagnose because pretraining corpora and cultural benchmarks are rarely indexed with comparable metadata. Benchmarks increasingly target culturally situated phenomena at the level of languages, regions, and locale-specific practices, while web-scale corpora are usually organized only by language. A shared culture-language-region layer makes these resources comparable, enabling audits of whether a target cultural phen...
  </details>

- **2026-09-21** — Jeongah Lee, Joy Qiuyue Zhong, Drishti Goel et al. — [Can LLMs identify and repair ruptures? Comparison between clinician practices and LLM behaviors](http://arxiv.org/abs/2609.25287v1)
  <details><summary>📄 Abstract</summary>
  Ruptures represent common albeit critical moments in interaction where relational alignment breaks down, making them essential for evaluating AI where trust and engagement matter most. In a scenario-driven empirical study, we examined the performance of three LLMs at identifying and resolving ruptures across 21 mental health conversations and 22 experts' evaluation of the strategies. For identification, LLMs relied on explicit linguistic cues within single turns whereas experts integrated implic...
  </details>

- **2026-09-21** — Wenqing Wang, Haitao Xiang, Xinyi Zhao et al. — [FinFIRST: Benchmarking Search Agents for Financial Information Retrieval, Sourcing and Traceability](http://arxiv.org/abs/2609.25192v1)
  <details><summary>📄 Abstract</summary>
  Financial search is a highly demanding task for LLM agents, requiring not only a correct final answer but also temporally valid information retrieval, authoritative source selection, entity and period alignment, unit and definition consistency, and verifiable evidence for all conclusions. Existing benchmarks predominantly evaluate only the final answer, making it difficult to localize errors or assess whether an answer is well-founded. To address this gap, we introduce FinFIRST (Financial Inform...
  </details>

- **2026-09-21** — Xiaoqiang Lu, Licheng Jiao, Lingling Li et al. — [0.5%>100%: Bidirectional Reciprocal Learning for Referring Image Segmentation](http://arxiv.org/abs/2609.24510v2)
  <details><summary>📄 Abstract</summary>
  Recent advances in vision foundation models (VFMs) have shown remarkable capabilities across diverse unimodal visual tasks. However, adapting VFMs to referring image segmentation (RIS) typically necessitates precise vision-language alignment via full fine-tuning, incurring substantial computational overhead and risking catastrophic forgetting. While existing parameter-efficient fine-tuning (PEFT) methods enable safe knowledge transfer with minimal training costs, they predominantly operate indep...
  </details>

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

- **2026-09-20** — Yang-Tian Sun, Tianjia Liu, Zehuan Huang et al. — [Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction](http://arxiv.org/abs/2609.23796v2)
  <details><summary>📄 Abstract</summary>
  Single-image 3D object generation can now produce high-fidelity assets, yet accurately placing them into a coherent scene layout remains an open challenge. A central difficulty lies in how object layout is represented. Holistic methods absorb placement into a scene-level generation process, sacrificing object-level detail. Compositional methods preserve object fidelity by decoupling geometry from layout, but typically parameterize layout as sparse, unbounded pose variables that are difficult to ...
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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 80 papers

- **2026-09-22** — Woojin Chae, Ezinne Nwankwo, Haitong Qin et al. — [Optimal Sequential Annotations for Off-Policy Evaluation](http://arxiv.org/abs/2609.26707v1)
  <details><summary>📄 Abstract</summary>
  Offline reinforcement learning and off-policy evaluation evaluates dynamic treatment rules based on retrospectively collected data prior to deployment. In recent AI applications, state and reward information is recorded as complex text or image, which recent AI advancements such as LLM-as-a-judge can label with unknown bias. Expert annotation may be available but at a higher cost. For example, safety classification via cheap but imperfect classifiers vs. expensive expert review. We show how a li...
  </details>

- **2026-09-22** — Brandon Bauer, Matthew Whalen, Kenji Watanabe et al. — [Autonomous Quantum Transport Measurements of 2D Semiconductors by an AI Agent](http://arxiv.org/abs/2609.26661v1)
  <details><summary>📄 Abstract</summary>
  Artificial-intelligence (AI) agents are beginning to enter experimental laboratories, automating experiments and accelerating scientific discovery. Herein, we introduce an AI-driven workflow in which an AI agent performs multi-step, multi-day quantum transport measurements end-to-end. Specifically, given brief instructions, the agent starts by planning the multi-step measurements, then safely operates the cryogenic instruments, analyzes the data, and concludes with a final report. We demonstrate...
  </details>

- **2026-09-22** — Xiao Tang, Tong Hui, Chao Shen et al. — [Unlocking Cross-Scenario Physical Layer Security: A Mixture-of-Experts Framework with Generative Diffusion Models](http://arxiv.org/abs/2609.26598v1)
  <details><summary>📄 Abstract</summary>
  The future 6G networks are expected to incorporate a proliferation of wireless services in diverse environments, which presents a significant challenge for information security. Conventionally optimization always requires recalculation and learning strategy often suffers poor generalization, which are thus incapable for the security provisioning with wide scenario coverage. In this paper, we propose an adaptive and robust learning framework that leverages a mixture-of-experts (MoE) architecture ...
  </details>

- **2026-09-22** — Zhiyun Jiang, Hanyong Wang, Binbin Liang et al. — [Combining Hierarchical Cognitive Process with Process Supervision for Interpretable Scene Safety Understanding](http://arxiv.org/abs/2609.26399v1)
  <details><summary>📄 Abstract</summary>
  Scene safety understanding plays a life-or-death role in situational awareness in various critical domains. Traditional methods that rely on learning direct mappings between scenes and safety levels often lack interpretability, limiting their reliability in critical applications. An effective approach to overcoming this challenge lies in interpreting human cognitive processes and equipping machine models with analogous cognitive capabilities. This work explores an effective way of integrating sc...
  </details>

- **2026-09-22** — Nikita Agarwal, Nivedit Jain — [FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents](http://arxiv.org/abs/2609.26048v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents often reach a working solution and then fail to consistently deliver it. We study runtime policies: targeted natural-language instructions and action denials applied by the agent harness at states that preceded observed failures, without changing model weights or the user prompt. With this, keeping capability constant, we observe a meaningful unlock in delivered reliability. Across the complete 87-task Terminal-Bench 2.1 suite, with two attempts per task, policies increase ...
  </details>

- **2026-09-22** — Pietro Talli, Petar Popovski, Osvaldo Simeone — [Risk-Aware Online Conformal State Probing](http://arxiv.org/abs/2609.25889v1)
  <details><summary>📄 Abstract</summary>
  AI-based autonomous agents, typically hosted at data centers, must acquire state information from robots or edge devices in order to issue informed control decisions. Managing uncertainty about the state is particularly consequential in safety-critical settings, in which average-case guarantees are insufficient. In this context, we study a sequential decision maker process that jointly decides which actions to take and when to probe given access to an arbitrary state prediction model. We propose...
  </details>

- **2026-09-22** — Hung-Mao Chen, Xu He, Bo Lu et al. — [C-to-Rust Fallacy: Automatic Refactoring != Memory Security](http://arxiv.org/abs/2609.25682v1)
  <details><summary>📄 Abstract</summary>
  Rust has emerged as the leading system programming language, offering strong memory and type safety guarantees without compromising performance. This positions it as a compelling alternative to traditional languages like C and C++, which are susceptible to memory security bugs. However, manually transforming C to Rust requires in-depth domain knowledge of the Rust language features, which requires significant effort for developers. To address this, tools for automatic C-to-Rust refactoring aim t...
  </details>

- **2026-09-22** — Yu Zheng, Qiyu Feng, Yixin Wu et al. — [PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation](http://arxiv.org/abs/2609.25653v1)
  <details><summary>📄 Abstract</summary>
  Large-scale manipulation demonstrations are essential for learning robust visuomotor policies, yet real-world data collection is expensive and difficult to scale. Simulation offers a promising alternative, but physical and visual discrepancies can limit the transferability of synthetic data, particularly for manipulation with soft grippers. We present PhyVisGen, a physically and visually high-fidelity framework for scalable robotic manipulation data generation. On the physical side, PhyVisGen in...
  </details>

- **2026-09-22** — FNU Aditi — [EquivSVA: A Formally Verified Dataset of Behavioral Assertions Across Equivalent RTL Implementations](http://arxiv.org/abs/2609.26751v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to generate SystemVerilog Assertions from natural-language specifica- tions and register-transfer-level designs. Existing datasets and benchmarks support important goals such as large- scale training, formal evaluation, specification-to-assertion generation, and mutation-based testing. A complemen- tary need is to study whether a generated assertion cap- tures externally observable behavior or depends on inci- dental details of one RTL implementation. ...
  </details>

- **2026-09-22** — David Torres-Moreno, Jorge Hermosillo-Valadez — [Semantic Abstraction for Natural Language Inference: a Methodological Framework for Discovering and Compensating Semantic Knowledge and Reasoning Gaps in Large Language Models](http://arxiv.org/abs/2609.26610v1)
  <details><summary>📄 Abstract</summary>
  Despite their outstanding performance on many NLP tasks, LLMs face serious challenges related to semantic abstraction. In this study, we are interested in understanding how LLMs leverage abstract semantic knowledge in natural language inference (NLI), which requires sophisticated linguistic capabilities to interpret implicit meanings, contextual conceptual relationships, and semantic connections between words and phrases. To this end, we propose a methodological framework for constructing new se...
  </details>

- **2026-09-22** — Yuan Liang, Sourav Bhattacharjee, Abraham Campbell — [Radiomics-Conditioned Modulation of RenalCLIP Features for Clear Cell Renal Cell Carcinoma Classification](http://arxiv.org/abs/2609.26492v1)
  <details><summary>📄 Abstract</summary>
  Radiomics provides quantitative descriptions of tumour appearance that may complement disease-specific foundation models in small labelled cohorts. We investigate this complementarity for computed tomography-based classification of clear cell renal cell carcinoma. Our framework uses radiomics to modulate RenalCLIP features through feature-wise linear modulation (FiLM), while retaining a direct radiomics contribution. Internal testing and external validation compare it with conventional fusion st...
  </details>

- **2026-09-22** — Sinuo Wang, Zichong Gu, Yuhan Huang et al. — [ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model](http://arxiv.org/abs/2609.26299v1)
  <details><summary>📄 Abstract</summary>
  Existing latent world models are typically optimized for future predictability, yet the resulting representations are not necessarily useful for planning in autonomous driving. Predictions are commonly used for pretraining or auxiliary supervision rather than as direct conditioning signals for trajectory generation. We propose ForeDrive, which learns a planning-relevant latent representation and couples it asymmetrically to a Diffusion Transformer (DiT) planner. The planner consumes multi-horizo...
  </details>

- **2026-09-22** — Huatai Zhu, Qiang Chen, Ziqian Kou et al. — [Dual-Frontier: When Can an Agent Trust Its World Model?](http://arxiv.org/abs/2609.26293v1)
  <details><summary>📄 Abstract</summary>
  Learned world models are becoming essential to general-purpose agents: by predicting action consequences, they support planning and decision-making while reducing reliance on costly trial and error. This reliance creates a fundamental ambiguity: when a world-model-guided decision fails, the trajectory alone may not reveal whether the agent's decision rule or the world model caused the loss. We formalize this failure-attribution problem as a counterfactual decomposition of return loss and prove t...
  </details>

- **2026-09-22** — Nada Rahali, Zijia Wang, Zhisong Liu — [Calibration Is Not Verification: Falsifiability-Aware Conformal Routing for Mixture-of-Agents](http://arxiv.org/abs/2609.25959v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent language systems often treat agreement as evidence, yet heterogeneous agents can jointly repeat an unsupported claim or omit a correct specialist fact. We introduce C-MoA, an agreement-based conformal filter that turns inter-agent semantic support into a claim-level nonconformity score and calibrates a retention threshold at the example level, giving distribution-free within-domain factuality control for heterogeneous Mixture-of-Agents. C-MoA is effective: it nearly doubles retained-...
  </details>

- **2026-09-22** — Panagiotis Michael, Moysis Symeonides, Demetris Trihinas — [Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models](http://arxiv.org/abs/2609.25788v1)
  <details><summary>📄 Abstract</summary>
  Time Series Foundation Models (TSFMs) promise a paradigm shift toward zero-shot forecasting by eliminating task-specific training. However, existing works often overlook trade-offs between predictive accuracy and probabilistic calibration. This paper presents a benchmark study of six TSFMs evaluated on energy, traffic, and financial datasets. We contrast their performance against statistical baselines and a supervised DL model. The study reveals that while TSFMs outperform statistical methods an...
  </details>

- **2026-09-22** — YongBo Li, Shuang Liang, HongWei Ma — [Model-Free Current Control of Permanent Magnet Synchronous Motors via ESO-Based Disturbance Feedforward and Data-Driven H-infinity Residual Feedback](http://arxiv.org/abs/2609.25759v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a model-free current control method for permanent magnet synchronous motors (PMSMs) based on disturbance feedforward and residual feedback. An ultra-local current model incorporates motor dynamics, parameter uncertainties, cross-coupling effects, and other nonideal factors into generalized lumped disturbances. An extended state observer (ESO) estimates these lumped disturbances and compensates for them through feedforward action, transforming the original PMSM current-control...
  </details>

- **2026-09-22** — YanZe Cao — [Testing-Driven Reliability Audit of Trajectory-Based Early Outcome Prediction for LLM Agents: Target-Specific Calibration Transfer Persists Within a Single Benchmark](http://arxiv.org/abs/2609.25647v1)
  <details><summary>📄 Abstract</summary>
  Predicting early outcomes based on trajectory can decrease the expenses associated with agent evaluation by terminating a run once the outcome becomes sufficiently predictable, assuming that the predictor's confidence is properly calibrated. Calibration is at risk when a predictor is applied to an agent on which it was never trained, but it is not known whether such transfer failures are broad across agent systems or concentrated in specific target agent/head combinations. Using public SWE-bench...
  </details>

- **2026-09-22** — Shubham Santosh Pandere, Gautam Ranka, Ritika Varshney et al. — [Rewired or Gated? How Instruction Tuning Shapes Knowledge-Conflict Circuits in LLMs](http://arxiv.org/abs/2609.25602v1)
  <details><summary>📄 Abstract</summary>
  In language models, the choice between believing the prompt and believing the weights is made by a handful of identifiable attention heads. Instruction tuning changes how models behave under conflict, but whether it rewires the underlying circuit or merely gates/reweights already present components, remains unknown. We provide the first mechanistic base-vs-instruct comparison of conflict-resolution circuits, across three families (Llama-3.2-3B, Qwen-2.5-3B, Gemma-3-4B). Five independent methods,...
  </details>

- **2026-09-22** — Chaehyun Kim, Sein Kim, Hongseok Kang et al. — [A Behavioral Trait Leaks into Preferences: Diagnosing Trait Interference in LLM User Simulators](http://arxiv.org/abs/2609.25572v1)
  <details><summary>📄 Abstract</summary>
  LLM-based user simulators aim to bridge the offline-online gap in recommender evaluation by emulating users through injected traits, where preference attributes determine what a user engages with and a behavioral activity trait governs how long they browse. However, we show this intended trait independence collapses during simulation, causing two failures: (i) Trait Interference, where amplified activity distorts preference boundaries and forces interactions with mismatched items to sustain brow...
  </details>

- **2026-09-22** — Vikas A. Patel, Mahdi Al-Husseini, Duncan Eddy et al. — [Risk-Averse Lander Site Selection under Altitude-Limited Information](http://arxiv.org/abs/2609.25517v1)
  <details><summary>📄 Abstract</summary>
  In aerospace systems, powered descent requires efficiently selecting a landing site while fine-scale hazards remain unresolvable until low altitude. This process presents a decision challenge since the actor must select a site and make corresponding actions before all information is known. To successfully solve this problem, an agent must reason over potential risks and make corrections as new observations are made. We introduce a lightweight model of altitude-limited information where each land...
  </details>

- **2026-09-22** — Sepideh Gohari, Goodarz Mehr, Azim Eskandarian — [Real-World Perception for Autonomous Driving in Adverse Weather: Enhancing Standard Detectors via Foundation-Guided Auto-Annotation](http://arxiv.org/abs/2609.25515v1)
  <details><summary>📄 Abstract</summary>
  Standard deployment-ready object detectors for autonomous vehicles degrade in adverse weather and lighting conditions without being trained on extensive domain-specific data. While large-scale vision foundation models offer robust zero-shot generalization, their high computational cost makes them impractical for real-time deployment. To bridge this gap, we propose a foundation-guided auto-annotation pipeline that enhances standard detectors without architectural changes. We first benchmark three...
  </details>

- **2026-09-21** — Donghyun Kim, Taehyuk Lee, Jinyeong Kim et al. — [Mitigating Sequential Reappearance in Diffusion Data-Point Unlearning](http://arxiv.org/abs/2609.25166v1)
  <details><summary>📄 Abstract</summary>
  Diffusion data-point unlearning is typically evaluated immediately after each deletion, even though subsequent requests may repeatedly update the same model. We identify sequential reappearance, a failure mode in which an instance that is initially judged to be forgotten later returns to the memorized regime without reuse of the deleted data or adversarial fine-tuning. To capture this behavior, we introduce a target-level evaluation protocol that tracks whether each target is forgotten immediate...
  </details>

- **2026-09-21** — Abdorasoul Ghasemi — [From functioning to evolving: A complex systems perspective on future self-organised federated energy communities](http://arxiv.org/abs/2609.25425v1)
  <details><summary>📄 Abstract</summary>
  Energy networks face a paradigm shift driven by renewable integration, uncertainty about required flexibility, distributed markets, and smart demand. Increasing asset interactions, cyber dependencies on communication and computation systems, and the deployment of AI agents demand a holistic, system-wide approach to understand the system's emergent behaviour. These transformations affect energy generation, demand adaptation, grid operations, and market dynamics, forming a complex engineered \emph...
  </details>

- **2026-09-21** — Toan Nguyen, Weiduo Yuan, Siheng Zhao et al. — [HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments](http://arxiv.org/abs/2609.25363v1)
  <details><summary>📄 Abstract</summary>
  Object transportation is a fundamental capability for humanoid robots operating in real-world, human-centric environments, yet existing methods struggle when clutter constrains free space around both the robot and its carried payload. We present HOTICE, a whole-body humanoid learning framework for transporting objects through such cluttered environments. First, we introduce Humanoid-Object Decoupled Potential Fields, which jointly encode collision-avoidance guidance for the robot and the carried...
  </details>

- **2026-09-21** — Chuyang Xiao, Peilin Meng, David Held — [JAMB: Joint Action-Motion Diffusion for Bimanual Manipulation](http://arxiv.org/abs/2609.25322v1)
  <details><summary>📄 Abstract</summary>
  Coordinated bimanual manipulation is challenging because the motion of either arm can alter the shared 3D scene and thereby affect the other arm. Yet most diffusion policies generate actions without explicitly modeling these future geometric consequences, while predictive variants typically use future state only as auxiliary supervision or fixed conditioning. We address this limitation by proposing JAMB, a diffusion policy that jointly denoises bimanual actions and future 3D point tracks. By all...
  </details>

- **2026-09-21** — Walter J. Manuel, Yuji Takubo, Simone D'Amico — [Transformer-Informed Trajectory Optimization for Relative Motion in Cislunar Orbits](http://arxiv.org/abs/2609.25460v1)
  <details><summary>📄 Abstract</summary>
  Autonomous spacecraft guidance and control requires a fast solution to non-convex trajectory optimization, which can be accelerated by providing a near-optimal initial guess to an optimization protocol, i.e., warm-starting. A robust warm starting method is especially useful for rendezvous, proximity operations, and docking (RPOD) in cislunar space, where the underlying dynamics become severely nonlinear and chaotic compared to those in Earth orbit, especially at perilune. This paper extends the ...
  </details>

- **2026-09-21** — Abolfazl Babanazari, Carson Cramer, Tyler Summers et al. — [PARTE: Plane-Assisted Robust Transformation Estimation for Point Cloud Registration](http://arxiv.org/abs/2609.25375v1)
  <details><summary>📄 Abstract</summary>
  Global point-cloud registration remains challenging when limited overlap, repetitive geometry, and sensor noise produce correspondence sets dominated by outliers. Planar regions are particularly difficult for conventional point descriptors and are therefore often suppressed or discarded before matching. We present PARTE (Plane-Assisted Robust Transformation Estimation), a global registration method that instead treats planar structure as complementary registration evidence. PARTE extracts planar...
  </details>

- **2026-09-21** — Ana Trišović, Janakan Sivaloganathan — [Open Science, Closed Models: How Funding Shapes AI in Science](http://arxiv.org/abs/2609.25347v1)
  <details><summary>📄 Abstract</summary>
  How funding shapes AI engagement in science is poorly understood despite its structural importance. We analyze 104,226 scientific papers (2018-2025), linking funding acknowledgments to how each paper engages with foundation models: whether it extends a model (fine-tunes or builds on it), uses one without modification, or references models only peripherally. Three findings emerge. First, funding source is associated with the character of engagement: public funding is associated with higher open-w...
  </details>

- **2026-09-21** — Jian Sun, Kingshuk Ghosh, Lilianna Houston et al. — [MT-ProtBERT: Multi-task Learning ProtBERT for Intrinsically Disordered Proteins Classification with Scarce Data](http://arxiv.org/abs/2609.25334v1)
  <details><summary>📄 Abstract</summary>
  Intrinsically disordered proteins (IDPs) differ from folded proteins in that they are dynamic, lack a stable three-dimensional conformation, and have low sequence similarity between similar proteins. The conformational heterogeneity of IDPs - while beneficial for their diverse functions - limits the use of traditional experimental tools to determine their conformation. The experimental difficulty, along with low sequence similarity, results in data scarcity, and makes it difficult to classify/de...
  </details>

- **2026-09-21** — Junru Zhu, Yixin Yang, Xiaoqing Ding et al. — [Partition-Matched Evaluation of Community Features under Distribution Shift in Android Malware Function-Call Graphs](http://arxiv.org/abs/2609.25256v1)
  <details><summary>📄 Abstract</summary>
  Graph-based Android malware classifiers can lose accuracy under malware-type or family shifts. We test whether mesoscopic organization in function-call graphs provides shift-stable information beyond local degree profiles (LDP), global statistics, lightweight metadata, and size-matched random partitions. Using 15,000 MalNet-Tiny, Common, and Distinct graphs, six Leiden descriptors specified before evaluation, and five optimizer seeds, communities raise Tiny macro F1 from 78.7% to 81.3% but yield...
  </details>

- **2026-09-21** — Ruike Cao, Fanyu Zhao, Fugen Yao et al. — [MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents](http://arxiv.org/abs/2609.24259v2)
  <details><summary>📄 Abstract</summary>
  The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response. Yet this capability has remained largely overlooked. To assess this capability, we introduce MemCalib, a benchmark grounded in realistic memory-system scenarios for evaluating memory use and advancing optimization algorithms. Results on the MemCalib test set reveal that frontier open- and closed-source models struggle to use memory ...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 17 papers

- **2026-09-22** — Yiqi Wang, Jinqian Ju, Jiaqi Zhang et al. — [When Does Execution Provenance Help Agent Memory Retrieval?](http://arxiv.org/abs/2609.25913v1)
  <details><summary>📄 Abstract</summary>
  A language agent's execution history can exceed its context window, requiring its memory system to retrieve complete supporting evidence under a hard token budget. Evidence may span multiple execution events, yet conventional retrievers use fixed token windows and fixed-k metrics that reward individual fragments without showing whether the complete evidence set fits in context. Smaller windows reduce irrelevant text but scatter evidence across candidates, while flat-versus-graph comparisons can ...
  </details>

- **2026-09-22** — Sebastian Cochinescu — [Truth for Believable AI: Expressed Doubt, Provenance, and Belief Revision as an Engineerable Stance](http://arxiv.org/abs/2609.26035v1)
  <details><summary>📄 Abstract</summary>
  Conversational agents often express answers in a uniformly confident register. We test whether expressed uncertainty, provenance-aware assertion, and explicit belief revision can be implemented as a behavior layer over a fixed language model; we do not test believability or trust. The layer combines three epistemic states, per-claim confidence and typed provenance, a provenance-gated expression rule, and a persistent revision store with auditable acknowledgments and partial resistance to false c...
  </details>

- **2026-09-22** — Haobo Zheng, Tan Tang, Yan Chen et al. — [SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue](http://arxiv.org/abs/2609.26780v1)
  <details><summary>📄 Abstract</summary>
  Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals perceive one another, what information is shared by the group, and how states change over time. Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed acr...
  </details>

- **2026-09-22** — Md Ataur Rahman, Dimitris Sacharidis, Oscar Romero et al. — [Discovery-Driven Integration of Disjoint Tables via Text](http://arxiv.org/abs/2609.26658v1)
  <details><summary>📄 Abstract</summary>
  Integrating heterogeneous datasets within data lakes is a critical challenge, particularly for semantically related tables that lack the explicit attributes needed to be joined. We study Discovery-Driven Integration, where the relevant sources and their missing relational structure must be discovered before integration. In this setting, unstructured text provides the evidence that connects otherwise disjoint tables. The fundamental challenge is to discover the relationships at a fine-grained lev...
  </details>

- **2026-09-22** — Shivam Gupta — [The Delegation Blind Spot: Auditing Product Decisions from Agent Choices](http://arxiv.org/abs/2609.26642v1)
  <details><summary>📄 Abstract</summary>
  Successful agent execution need not identify which future product improvement its user would value. We present a decision-specific audit that maps a declared observation channel and product-value contrast to compatible intervals and witness populations. Its foundations are established identification and decision theory; the contribution is an executable measurement workflow and a controlled study of its limits. A frozen experiment makes 4,800 requests to two pinned model snapshots on shared synt...
  </details>

- **2026-09-22** — Jiayi Li, Ziyuan Wang, Daniel Garijo et al. — [CQ4OE: A benchmark for assessing LLM-assisted ontology generation from competency questions](http://arxiv.org/abs/2609.26029v1)
  <details><summary>📄 Abstract</summary>
  Ontology generation from Competency Questions (CQs) is a central yet labor-intensive phase of Ontology Engineering. While large language models (LLMs) offer promising automation capabilities, current evaluations remain fragmented. Task formulations are heterogeneous, gold standards often lack fine-grained CQ provenance, metrics conflate lexical overlap with structural and logical adequacy, and reference ontologies are not always explicitly designed around the evaluation CQs. Here, we address the...
  </details>

- **2026-09-22** — Jiangxu Wu — [Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents](http://arxiv.org/abs/2609.25991v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) gives large language models (LLMs) access to external knowledge, but its conventional retrieve-concatenate-generate pipeline makes retrieval decisions on behalf of the model. As tool use and agent loops become more reliable, an agent can decide whether to retrieve, what to inspect, and when to stop. This shift exposes a new bottleneck: the agent may not know what a knowledge base contains. Traditional knowledge bases expose documents as anonymous text chunks ...
  </details>

- **2026-09-22** — Abhishek Sharma — [CausalLoss-Fin: Attributing Financial-Agent Loss to Decisions and Infrastructure Faults](http://arxiv.org/abs/2609.25960v1)
  <details><summary>📄 Abstract</summary>
  When an agent handling a payment exception loses money, the agent-step attribution methods this paper compares against will name one of its actions. They will do so even when a settlement message was dropped and the agent never had a chance: they intervene on agent actions and do not expose infrastructure faults as intervenable variables, so every dollar they explain is charged to a decision. We take a benchmark whose fault process is explicit and replayable, decompose each episode's realised de...
  </details>

- **2026-09-22** — Aryaman Arora, Kirill Acharya, Nathan Hu et al. — [Matryoshka attribution: Learning to attribute language model outputs to representations and weights](http://arxiv.org/abs/2609.25518v1)
  <details><summary>📄 Abstract</summary>
  Attributing language model outputs to their internal computations is an open problem in interpretability. Existing methods, which use causal interventions, gradients, or learnable masks, either are infeasibly expensive or struggle to identify actual causally-important internal computations. We propose framing attribution as the problem of identifying nested subsets of internal components which minimise a downstream loss. To learn this task, we introduce Matryoshka Attribution (MAttr), a mask lea...
  </details>

- **2026-09-21** — David Garg, Ritobrata Sarkar, Ehsan Azarnasab et al. — [ShowTellArena: Evaluating Business Workflow Understanding from Demonstrations](http://arxiv.org/abs/2609.25467v1)
  <details><summary>📄 Abstract</summary>
  We often teach a colleague by showing the work and explaining the decisions as we go. How can we check what an agent understood from the same lesson? We introduce ShowTellArena, a benchmark protocol and public dataset for comprehension after narrated business demonstrations. The v1.0 release contains 50 business workflow tasks, with recordings, screenshots, narration, fixture seeds, and 502 questions. Tasks span finance, hiring, procurement, customer decisions, inventory, and logistics. The prot...
  </details>

- **2026-09-21** — Timothy Urista — [Who Pays for the KV Cache? Attributing Shared AI Inference Spend Across Kubernetes and LLM Provider Bills](http://arxiv.org/abs/2609.24991v1)
  <details><summary>📄 Abstract</summary>
  Organizations pay for AI through disconnected ledgers: Kubernetes allocations for self-hosted inference, gateway logs, and per-token bills from API providers. We present unalloc, an open-source tool that joins OpenCost, LiteLLM, OpenAI and Anthropic cost data into one exact ledger and reports the share of spend with no owner, and use it to study where attribution breaks at the seams between these systems. Five case studies run inference for real or simulate it: a vLLM-style serving simulator wit...
  </details>

- **2026-09-20** —  ScholarSeed AI Team, Caoqinwei Gong, Xue Jiang et al. — [ScholarStack: Layered Research Asset Orchestration and Cross-Task Reuse for Scientific Agents](http://arxiv.org/abs/2609.23735v2)
  <details><summary>📄 Abstract</summary>
  Scientific agents support a range of literature-based research tasks, such as retrieval, question answering, evidence-grounded generation, and claim assessment. Most existing systems, however, are organized around individual tasks: the same papers are repeatedly retrieved, segmented, and interpreted, and the understanding built in one task is difficult to reuse in the next. We present ScholarStack, a layered research asset framework that compiles a paper collection into reusable, versioned, and ...
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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-09-22** — Jin Liu, Yanzhong He, Guancheng Lin et al. — [What Was Once Learned May Need to Be Unlearned: Machine Unlearning for Deprecated API Knowledge in Large Language Models](http://arxiv.org/abs/2609.25786v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) for code completion may generate deprecated APIs because their pre-training corpora contain code from historical library versions. Existing approaches use inference-time intervention, model editing, or machine unlearning, but multiple plausible completions make predefined replacements restrictive. Moreover, existing studies rarely verify whether models exhibit the targeted deprecated behavior or evaluate unintended changes to other APIs.   We conduct a systematic emp...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 3 papers

- **2026-09-22** — Vishnu Sashank Dorbala, Dinesh Manocha — [Deploying Foundation Models for Embodied Navigation](http://arxiv.org/abs/2609.25666v1)
  <details><summary>📄 Abstract</summary>
  We present and tackle two problems associated with deploying Foundation Models (FMs) on Embodied Agents performing navigation: 1) Training bias in FMs leading to poor personalization in unseen environments, and 2) Limited FM context length hindering success, especially on long horizon tasks. Our solution for the former involves priming the FM with human-habit data mined from the scene and our solution for the latter involves active memory management via a novel `memory head' augmentation. We fir...
  </details>

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

- **2026-09-22** — Romain Cosson, Laurent Massoulié — [Polylogarithmic Collective Tree Exploration](http://arxiv.org/abs/2609.26789v1)
  <details><summary>📄 Abstract</summary>
  We study asynchronous collective tree exploration, where $k$ agents with unrestricted communication start at the root of an unknown tree and discover edges online. At each step, an adversary chooses which agent moves. We give a deterministic algorithm that explores any tree with $n$ nodes and depth $D$ in at most \[ 2n+O\left(k\log^2(k)D\right) \] moves, matching known lower bounds up to a constant factor. As a direct consequence, we obtain a near-optimal competitive ratio of $O(\log^2 k)$ for s...
  </details>

- **2026-09-22** — Jennifer Williams, Dave Farris, Jeff Farris et al. — [SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving](http://arxiv.org/abs/2609.26777v1)
  <details><summary>📄 Abstract</summary>
  We introduce SWE-Serve, a benchmark for evaluating agents on production inference engineering tasks. Implementing an inference feature can require coordinating multiple changes across the serving stack, including model support, runtime execution, and public APIs. Existing benchmarks provide limited coverage of production inference engineering: repository-level software engineering benchmarks do not target inference, while general terminal-agent benchmarks include only a few inference tasks. Dedi...
  </details>

- **2026-09-22** — Rasika Muralidharan, Haewoon Kwak, Jisun An — [Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies](http://arxiv.org/abs/2609.26481v1)
  <details><summary>📄 Abstract</summary>
  Social norms cannot be identified from behavior alone: the same cooperative equilibrium may reflect shared expectations, strategic incentives, or simple imitation. Yet in multi-agent large language model systems, prior work largely treats behavioral convergence as evidence of norm emergence. In this work, we introduce an evaluation framework that measures agents' reported empirical and normative expectations in addition to behavioral convergence. Through controlled ablations, we test the effect ...
  </details>

- **2026-09-22** — Haejoon Lee, Dimitra Panagou — [Fully Byzantine-Resilient Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2609.25701v1)
  <details><summary>📄 Abstract</summary>
  We study distributed Byzantine-resilient actor-critic multi-agent reinforcement learning (AC-MARL), where agents collectively learn policies through local interactions. Existing methods guarantee convergence of the agents' parameters only to a neighborhood of the attack-free limit points, resulting in degraded performance. We propose Fully Resilient AC-MARL (FRAC-MARL), a decentralized method in which each agent leverages redundancy in two-hop messages to identify reliable messages. Under linear...
  </details>

- **2026-09-22** — Mahya Samdaliri, Zhihao Yao, Kasthuri Jayarajah — [Dynamic Conformance Testing of WebGPU Through Specification-Driven Mutation](http://arxiv.org/abs/2609.25520v1)
  <details><summary>📄 Abstract</summary>
  WebGPU is a low-level graphics and compute API that exposes modern GPU functionality to web applications. While the official WebGPU Conformance Test Suite (CTS) focuses on well-formed usage under the WebGPU specification, it is not designed to stress implementations with semantic edge cases or adversarial inputs. General-purpose fuzzers, in contrast, struggle with WebGPU because of its complex graphics stack and multi-process architecture. We introduce LANTERN, a specification-guided dynamic con...
  </details>

- **2026-09-22** — Xinyi Wei, Shuo Han, Jie Fu — [Incentive Design for Multi-Agent Systems: A Bilevel Optimization Framework for Coordinating Independent Agents and Convergence Analysis](http://arxiv.org/abs/2609.26726v1)
  <details><summary>📄 Abstract</summary>
  Incentive design aims to guide the performance of a system towards a human's intention or preference. We study this problem in a multi-agent system with one leader and multiple followers. Each follower independently solves a mdp to maximize its own expected total return with the same state space and action space. However, the leader's objective depends on the collective best-response policies of all followers. To influence these policies of followers, the leader provides side payments as incenti...
  </details>

- **2026-09-22** — Lenz Pracher, Pascal de Jong, Oskar Lieshaus et al. — [A Spectral Theory of Grokking: Weight Decay induces Feature Learning](http://arxiv.org/abs/2609.26679v1)
  <details><summary>📄 Abstract</summary>
  In grokking an early fit to the training data separates from a much later improvement in generalization. During this delay, training can move from a fixed neural tangent kernel (NTK) regime to one in which task-relevant kernel eigendirections continue to evolve. We provide a quantitative theory for how this transition from lazy to rich learning can produce delayed generalization. For homogeneous networks trained with squared loss and $L_2$ weight decay, we show that a finite residual remains aft...
  </details>

- **2026-09-22** — Adithi Shankar, Gopika Krishnan, Gloria Haro et al. — [MambaVoice: Lightweight Audiovisual Singing Voice Separation Via A Hybrid Mamba-Transformer Model](http://arxiv.org/abs/2609.26635v1)
  <details><summary>📄 Abstract</summary>
  Isolating a target singing voice from a music video remains challenging, particularly in the presence of multiple vocalists and dense instrumental accompaniment. We propose MambaVoice, a lightweight audiovisual framework that leverages a hybrid Mamba--Transformer architecture for targeted singing voice separation. The model jointly encodes audio and visual streams using an attention-based band-split audio encoder and a spatio-temporal graph convolutional network (ST-GCN) for facial motion featur...
  </details>

- **2026-09-22** — Yichuan Yu, Youzhuo Wang, Yiming Ren et al. — [MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection](http://arxiv.org/abs/2609.26520v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills. However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE, a Multi-Agent virtual TEleoperation platform for humanoid collaboration data collection that enables multiple geographically distributed ope...
  </details>

- **2026-09-22** — Raman Talwar, Elias Nijs, Andreas Verleysen et al. — [Generalizing Manipulation Skills with a Local Coding Agent](http://arxiv.org/abs/2609.26499v1)
  <details><summary>📄 Abstract</summary>
  Today, progress in open-weight language models enables systems capable of writing, executing and debugging code while still running on a single workstation. Most language-driven robots give the model a fixed action interface or a trained policy. Generalizing to a new task therefore means more engineering effort or more data collection, both time-consuming. We investigate whether a local open-weight vision-language model can control a robot and one-shot generalize to new variations of a task with...
  </details>

- **2026-09-22** — Xutian Li, Bo Xiong, Yifeng Zhu et al. — [FeatLens: Feature-Guided Dynamic Code Graph Construction and Retrieval for Repository-Level Code Generation](http://arxiv.org/abs/2609.26480v1)
  <details><summary>📄 Abstract</summary>
  Recent code generation research has moved from isolated function completion toward repository-level generation in existing codebases. To implement a target function correctly, an LLM must identify reusable repository dependencies such as existing functions, APIs, and cross-file definitions. Existing retrieval methods provide such context through code similarity search, persistent whole-repository graphs, or LLM-driven graph exploration, but often incur high graph construction, reasoning, and tok...
  </details>

- **2026-09-22** — Sophie Henning, Georg Hofmann, Alexander Schulte et al. — [How to Estimate Whether You Have Found Several Needles in a Haystack: Measuring Calibration in Multi-Label Text Classification](http://arxiv.org/abs/2609.26468v1)
  <details><summary>📄 Abstract</summary>
  A key factor in deciding whether to trust an automatic prediction is its confidence score, which should be calibrated to match the actual probability of the prediction being correct. Most confidence calibration metrics target binary or multi-class tasks, while multi-label calibration remains largely underexplored. Multi-label classification tasks, such as assigning medical codes to clinical notes or determining news topics, are usually dominated by a large number of negatives, i.e., labels that ...
  </details>

- **2026-09-22** — Nicoletta Prencipe, Başak Sakçak, Steven M. LaValle — [The Minkowski Wrap: A Relativistic Speed Limiter](http://arxiv.org/abs/2609.26311v1)
  <details><summary>📄 Abstract</summary>
  In special relativity, a particle can experience constant acceleration, but at the same time, its motion is constrained by the velocity limit imposed by the speed of light $c$. Inspired by this principle, we propose a method for enforcing velocity bounds in control systems by replacing $c$ with the maximum attainable speed of the system. We refer to this as the ``Minkowski wrap," the operation of deforming the phase portrait of a system so as to enforce desired speed limits. We apply this idea t...
  </details>

- **2026-09-22** — JJiahang Li, Dingbao Shao, Xinyu Chen et al. — [VideoX-Qwen: Data-Centric Instruction-Based Video Editing](http://arxiv.org/abs/2609.26015v1)
  <details><summary>📄 Abstract</summary>
  Progress in general-purpose video editing depends on constructing large-scale paired supervision and effectively adapting video-generation backbones to instruction-driven editing. Unlike video generation, video editing must execute a requested transformation while preserving unrelated subjects, scene structure, motion, and temporal continuity. We present VideoX-Qwen, an integrated data-construction and model-training framework for general instruction-based video editing. Our scalable production ...
  </details>

- **2026-09-22** — Jinmyeong Choi, Jinkwan Jang, Seul Lee et al. — [Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models](http://arxiv.org/abs/2609.25980v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic time series foundation models (TSFMs) provide coordinate-wise predictive distributions, but these marginals do not determine a joint distribution over multivariate future trajectories. We study training-free coupling of frozen TSFM marginals into multivariate forecast sample paths. Our primary evaluation fixes the empirical marginal sample multiset at every channel--horizon coordinate across methods, isolating the effect of coupling alone. Historical temporal and channel relations ...
  </details>

- **2026-09-22** — Karim Slimani, Catherine Achard, Eric Marchand et al. — [GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration](http://arxiv.org/abs/2609.25966v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces GRIP, a pose-conditioned refinement framework for pixel-to-point matching and 2D to 3D registration. Given an initial coarse pose estimate, GRIP addresses the structural mismatch between grid based image descriptors and unordered point cloud descriptors by softly rendering learned 3D point features onto the image grid through Gaussian feature splatting. The rendered point derived feature map is then fused with image features by a pixel aligned transformer, enabling visual s...
  </details>

- **2026-09-22** — Xiaoyi Yu, Enver Sangineto, Pei Fu et al. — [Informed Masking: Structure-Aware Perturbation for Reinforcement Learning in Diffusion Large Language Models](http://arxiv.org/abs/2609.25927v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Large Language Models (dLLMs) have emerged as an efficient alternative to autoregressive models, yet aligning them via Reinforcement Learning (RL) requires likelihood surrogates estimated from masked reconstruction subproblems under a small Monte Carlo budget per rollout. Existing methods construct these subproblems by uniform random masking, leaving open the question of which subproblems to prioritize. We identify a systematic upstream/downstream structure in dLLM rollouts. Some token...
  </details>

- **2026-09-22** — Zishu Qin, Zhiyu Jin, Pipei Huang et al. — [Delving into Asymmetric Information Dynamics for High-Fidelity Virtual Try-On](http://arxiv.org/abs/2609.25881v1)
  <details><summary>📄 Abstract</summary>
  Virtual try-on (VTON) requires precise pixel-level fidelity, yet mainstream Diffusion Transformers (DiTs) often suffer from texture degradation and structural drift. We identify symmetric interactions in standard joint-attention mechanisms as a source of these failures. Although such interactions support semantic flexibility in general-purpose editing, they allow stochastic noise to corrupt deterministic garment features in VTON. We analyze this problem through asymmetric information dynamics an...
  </details>

- **2026-09-22** — Xinyue Guo, Jianxuan Yang, Daiguo Zhou et al. — [TV-AudioRemover: Joint Text-Visual Guided Sound Removal with Multi-Task Hard-Mixture Curriculum](http://arxiv.org/abs/2609.25864v1)
  <details><summary>📄 Abstract</summary>
  Visual object removal can eliminate a target from video frames, yet its acoustic trace persists in the soundtrack, causing obvious audio-visual inconsistency. Existing video inpainting models operate solely on pixels, while audio editing models, especially for the sound removal task, are typically driven by text and therefore rely on limited single-modal control, which is less effective than multimodal guidance that provides stronger semantic grounding and temporal synchronization cues. In this ...
  </details>

- **2026-09-22** — Guanxu Yu, Yuhang Yao — [Visual Jev: Accurate and Efficient Decisions from Shared Visual Context](http://arxiv.org/abs/2609.25845v1)
  <details><summary>📄 Abstract</summary>
  Many vision applications ask several independent, forced-choice questions about the same image. Visual Jev encodes the image and public context once, executes isolated question suffixes as a batch, and reads candidate probabilities from the backbone's language-model head. Across four benchmarks, answer-supervised post-training raises equal-weight macro accuracy from 70.6% to 76.1%, with the gain concentrated on the two task families represented in training. At N=32 questions per image, shared ba...
  </details>

- **2026-09-22** — Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose et al. — [Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence](http://arxiv.org/abs/2609.25790v1)
  <details><summary>📄 Abstract</summary>
  This study aimed to automate hierarchical diagnostic reasoning (HDR), a constructive method for evaluating practical judgment skills, by developing and testing an evaluation process using a large language model. HDR is a descriptive task that measures higher-order cognitive skills by requiring students to identify and explain errors in case-study-based problems. However, it requires expertise and effort to develop and evaluate. Hence, we proposed and empirically validated the automatic (1) gener...
  </details>

- **2026-09-22** — Junjie Xie, Chuxuan He, Angen Ye et al. — [MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation](http://arxiv.org/abs/2609.25756v1)
  <details><summary>📄 Abstract</summary>
  Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints. Although recent Vision-Language-Action (VLA) models show strong multimodal reasoning ability, their continuous action generation paradigm is not well suited for precision medical tasks, where reliable closed-loop operation may also depend on non-action system function calls. To address this gap, we propose MedVLA, a hierarchical framework that couples high-level multimoda...
  </details>

- **2026-09-22** — Zheng Chen, Zhicheng Du, Haoxuan Li et al. — [LingLan: An Advancing Traditional Chinese Medicine Diagnosis LLM with Multimodal Data](http://arxiv.org/abs/2609.25715v1)
  <details><summary>📄 Abstract</summary>
  Though artificial intelligence (AI) increasingly transforms modern medicine, its integration into Traditional Chinese Medicine (TCM) has been relatively slow, primarily due to TCM's reliance on holistic, subjective diagnostic methods---namely Inspection, Auscultation and Olfaction, Inquiry, and Palpation(I-AOI-P)---which are difficult to align with quantitative, standardized medical systems. In this work, we introduce a Unification Framework for Multimodal Data (UFMD), which automatically proces...
  </details>

- **2026-09-22** — Wenjie Tian, Kangxiang Xia, Jingbin Hu et al. — [Interactive TTS: Dynamic Speaking Style Adaptation for Expressive Speech Synthesis](http://arxiv.org/abs/2609.25707v1)
  <details><summary>📄 Abstract</summary>
  Dynamic speaking style adaptation in multi-turn multimodal interaction remains a major challenge for text-to-speech (TTS) systems. Existing context-aware TTS (CTTS) methods typically map dialogue context to speech in an end-to-end manner. Such implicit modeling makes contextual style decisions difficult to supervise, while the entanglement of style, timbre, and content often leads to weak instruction-following and severe timbre drift across turns. To overcome these limitations, we propose Intera...
  </details>

- **2026-09-22** — Chang Guo, Yukun Xie, Bohan Tan et al. — [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](http://arxiv.org/abs/2609.25636v1)
  <details><summary>📄 Abstract</summary>
  Modern embodied agents achieve impressive success rates, yet their actual instruction-following ability is far weaker than these numbers suggest. We trace this illusion to a structural property we term low scene entropy: when a visual scene admits only one valid task, language becomes redundant and a policy can score highly while barely using it. We introduce RoboFollow, a diagnostic benchmark with three principles: (1) High Scene Entropy: each training scene supports multiple kinematically dist...
  </details>

- **2026-09-22** — Haoran Wen, Wenfu Wang, Kunsong Shi et al. — [MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence](http://arxiv.org/abs/2609.25627v1)
  <details><summary>📄 Abstract</summary>
  General-purpose robot control requires models to understand task intent, identify where to interact, capture how the scene evolves, and generate precise actions. Vision-language-action models provide strong semantic priors but typically do not explicitly model scene dynamics, while world-action models couple visual prediction with control without necessarily exposing the task-relevant semantic and spatial structure needed for fine-grained manipulation. We present MachEmbodied-U0 (ME-U0), a unifi...
  </details>

- **2026-09-22** — Dongho Yee, Juahn Oh, Jinseok Lee et al. — [From Instrument-Mounted Demonstrations to In-Vivo Execution: Learning Bimanual Laparoscopic Appendectomy Without Robot-Collected Demonstrations](http://arxiv.org/abs/2609.25625v1)
  <details><summary>📄 Abstract</summary>
  Most minimally invasive surgery is still performed with hand-held laparoscopic instruments, and the surgeon's instrument kinematics are lost when the operation ends; only the endoscope video is kept. This paper presents an end-to-end pipeline that captures this motion in the operating room and uses it to train a surgical robot policy, validated on live animals. We introduce a surgical instrument-state logger that mounts on the shaft of a standard laparoscopic instrument and recovers its pose and...
  </details>

- **2026-09-22** — Md Mostafizer Rahman, Md Faizul Ibne Amin, Md Shahajada Mia et al. — [Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference](http://arxiv.org/abs/2609.25537v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference is constrained by the quadratic scaling of self-attention and the linear scaling of the KV cache, increasing latency, energy consumption, and GPU memory demand as context length scales. Existing soft-compression methods either lack query-guided memory selection at inference time, train without answer-targeted supervision, or couple compression tightly to a specific decoder architecture. We propose a Context-to-Answer-Aligned Memory Compression (CMC) framework...
  </details>

- **2026-09-22** — Laizhen Li, Jiarui Li, Juanjuan Zhao et al. — [Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents](http://arxiv.org/abs/2609.26760v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. We study whether task feedback can instead turn recurring control into reusable executable code, while reserving LLM calls for task-specific semantic reasoning. We introduce Growing Harness, a failure-guided training paradigm that learns the agent harness itself from a strategy-free scaffold that exposes fix...
  </details>

- **2026-09-22** — Tushar Bag, Edgar Martínez-Moro, Daniel Panario — [Annihilator and twisted Euclidean duality for quasi-polycyclic codes](http://arxiv.org/abs/2609.26633v1)
  <details><summary>📄 Abstract</summary>
  Let $f\in\mathbb F_q[x]$ be a monic polynomial of degree $m$ with $f(0)\ne 0$, and let $\mathcal R=\mathbb F_q[x]/\langle f\rangle$. Under coefficient expansion, a quasi-polycyclic (QP) code of index $n$ corresponds to an $\mathcal R$-submodule of $\mathcal R^n$. In this paper, we study QP codes with respect to the annihilator duality. We show that this form is non-degenerate and that the annihilator dual of a QP code is again a QP code. We also give an equivalent description of the dual in term...
  </details>

- **2026-09-22** — William Schober, Scott Wesley — [A New Method For Manipulating Circuits, Application To Quantum Adders](http://arxiv.org/abs/2609.26591v1)
  <details><summary>📄 Abstract</summary>
  We use a new technique for manipulating controlled quantum circuits to convert between two distinct types of quantum adders, one based on the Quantum Fourier Transform and the other based on the Ripple-Carry technique from classical reversible logic. This conversion takes the form of an explicit gate-level transpilation. We also present a new quantum adder with a natural interpretation as a kind of Carry-Lookahead adder that uses no ancillas.
  </details>

- **2026-09-22** — Ziyan Feng, Zizhao Yuan, Yulong Fu et al. — [What is the Better Curriculum: Controller-Shaped Grasping Behavior for Contact Force-Sensitive Manipulation](http://arxiv.org/abs/2609.25887v1)
  <details><summary>📄 Abstract</summary>
  How should a robot learn to manipulate objects so fragile that sub-Newton contact forces can cause irreversible damage? Existing visuo-tactile policy learning typically treats tactile sensing as an additional policy input. In direct-contact force-sensitive manipulation, however, the bottleneck can arise earlier, during data collection: manual gripper control is too delayed and coarse-grained to reliably maintain the narrow force range required for stable grasping. We therefore use a deterministi...
  </details>

- **2026-09-22** — Yuling Xi, Haokai Zhang, Muzhi Zhu et al. — [Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes](http://arxiv.org/abs/2609.25841v1)
  <details><summary>📄 Abstract</summary>
  Metric reasoning is a critical and challenging task for Vision Language Models (VLMs), playing a pivotal role in embodied AI tasks such as robotic manipulation and autonomous navigation. However, current spatial reasoning remains bottlenecked by rigid pixel-level supervision; such localized optimization often compromises general multimodal intelligence, triggering performance degradation or catastrophic forgetting of broad reasoning capabilities. To address these limitations, we introduce Metric...
  </details>

- **2026-09-22** — Yi-Lin Tsai,  Yung-Hsiu,  Lai — [Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pretest Visual Marketing](http://arxiv.org/abs/2609.25677v1)
  <details><summary>📄 Abstract</summary>
  Marketers now deploy generative AI agents as synthetic consumers to pretest visual assets such as logos, packaging, and advertising at a fraction of human-panel cost. However, this procedure assumes that a model seeing a visual cue can also perceive its consumer meaning, which is largely untested. We stress-test the assumption using six canonical visual marketing experiments, varying the two levers managers control: model generation (GPT-4o-mini vs. GPT-5.4-mini) and input format (plain text vs....
  </details>

- **2026-09-22** — Rajesh Kumar, Nabeel Siddiqui, Alexander Fuchsberger — [Detecting GPT-Assisted Writing Using Interpretable Stylometric Features](http://arxiv.org/abs/2609.26687v1)
  <details><summary>📄 Abstract</summary>
  Distinguishing GPT-assisted from independently authored student writing has become a critical challenge in academia. This paper evaluates the discriminative capability of interpretable stylometric features extracted solely from submitted text. Using data from 90 participants who wrote both independently and with ChatGPT assistance, we evaluate eight machine learning classifiers while keeping data from the same participant together during validation. On the held-out test set, Random Forest achiev...
  </details>

- **2026-09-22** — Bilvin Varughese, Orcun Yildiz, Aditya Koneru et al. — [Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS](http://arxiv.org/abs/2609.26657v1)
  <details><summary>📄 Abstract</summary>
  Interatomic potentials underpin MD and govern predictive atomistic-model fidelity for metals, semiconductors, oxides, liquids, and reactive systems. A potential has limited practical value until reliably implemented in production MD code. Slow, expertise-intensive implementation requires more than equation-to-C++ translation: it must select the neighbor-list architecture, evaluate and distribute many-body derivatives, manage interprocessor communication, and preserve host-code energy, force, and...
  </details>

- **2026-09-22** — Xiaoyu Luo, Tao Ren, Wenrui Yu et al. — [Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models](http://arxiv.org/abs/2609.26637v1)
  <details><summary>📄 Abstract</summary>
  The rapid capability gains of frontier language models are widely attributed to improved reasoning abilities, yet this cannot be verified as raw CoT traces in closed-source systems are hidden. By registering a simple custom tool through a standard API feature, we induce frontier models to externalize intermediate reasoning. Because these traces may reflect post-hoc rationalization rather than genuine reasoning, we first evaluate against native CoT on open-source models and extend to closed-sourc...
  </details>

- **2026-09-22** — Maan Qraitem, Kate Saenko, Bryan A. Plummer — [PERSONAWEAVER: Controllable Diversity Beyond Conventional Archetypes in Procedural Character Generation](http://arxiv.org/abs/2609.26629v1)
  <details><summary>📄 Abstract</summary>
  Procedural character generation aims to populate games, simulations, and other virtual worlds with diverse characters. Large language models (LLMs) offer a promising foundation for scaling this task. However, LLM-based procedural character generation remains at an early stage: existing methods either generate characters directly or adapt profiles retrieved from persona banks. As we show, both approaches produce behaviorally homogeneous populations: characters overwhelmingly agree with positive m...
  </details>

- **2026-09-22** — Yuan Liang, Fangyijie Wang, Kathleen M. Curran et al. — [Radiomics--Foundation Fusion for Interpretable RCC Classification: Internal Benchmarking and Exploratory External Transfer](http://arxiv.org/abs/2609.26578v1)
  <details><summary>📄 Abstract</summary>
  Accurate preoperative subtype classification of renal cell carcinoma (RCC) from contrast-enhanced CT remains clinically challenging because clear cell RCC (ccRCC) and non-clear cell RCC often show overlapping imaging appearances. This study evaluates whether foundation representations reduce reliance on handcrafted radiomics, or whether radiomics remains complementary for interpretable tumour characterisation. We compared radiomics, conventional CNN features, MedicalNet-pretrained features, MedV...
  </details>

- **2026-09-22** — Tianshu Huang, Xiaowei Ou, Vidvuds Ozolins — [Neural Network Backflow with Low-Rank Multi-Determinant Updates](http://arxiv.org/abs/2609.26544v1)
  <details><summary>📄 Abstract</summary>
  Simulating strongly correlated fermions remains a long-standing challenge due to the exponential complexity of the Hilbert space and the intricate sign structure of many-body wavefunctions. We introduce a variational framework centered on a neural network backflow transformation that combines deep learning with variational Monte Carlo. The proposed ansatz employs a multi-determinant expansion with low-rank shifts to capture non-local correlations and complex sign structures. Applied to the two-d...
  </details>

- **2026-09-22** — Junchi Zhu, Zhenguang Liu, Shaojing Fan et al. — [From Approval to Execution: Reconstruction-Aware Repair Analysis for LLM-Agent Software](http://arxiv.org/abs/2609.26529v1)
  <details><summary>📄 Abstract</summary>
  Approval mechanisms have become a primary safeguard for consequential actions in LLM-agent software. Yet the action shown for approval is often not the object ultimately consumed: workflow reload, transcript projection, argument rebinding, and durable-state lookup may reconstruct it before execution. Existing fieldflow and check-coverage analyses can establish that expected fields were inspected, but not that the inspected object version reaches the sink or that no replacement intervenes between...
  </details>

- **2026-09-22** — Margit Rösler, Michael Voit — [Dunkl theory, convolution algebras, and related Markov processes](http://arxiv.org/abs/2609.26394v1)
  <details><summary>📄 Abstract</summary>
  These lecture notes are intended as an introduction to the theory of rational Dunkl operators, the associated special functions and related Markov processes with an emphasis on examples which are related to Riemannian symmetric spaces of Euclidean type and Bessel hypergroups on the matrix cones of positive semidefinite matrices.   We start with a comprehensive introduction into Dunkl theory: Dunkl operators, the intertwining operator and its positivity, the Dunkl kernel and the Dunkl transform, ...
  </details>

- **2026-09-22** — Moumita Mondal, Santanu K. Maiti — [Bias-driven circular currents in a quantum ring: Effects of electron-electron and electron-phonon interactions](http://arxiv.org/abs/2609.26344v1)
  <details><summary>📄 Abstract</summary>
  The phenomenon of bias-driven circular charge and spin currents in a ring nanojunction is investigated in the presence of electron-electron (e-e) and electron-phonon (e-ph) interactions within a tight-binding framework based on the non-equilibrium Green's function formalism. The Lang-Firsov transformation is employed to map the interacting system onto an effective electronic model, which is subsequently treated within the Hartree-Fock mean-field scheme. By exploring the interplay among e-e inter...
  </details>

- **2026-09-22** — Zhiheng Zhang — [Learning to Fluctuate: Statistical Foundations for Causal Tabular Pretraining](http://arxiv.org/abs/2609.26290v1)
  <details><summary>📄 Abstract</summary>
  Causal tabular foundation models amortize effect estimation across synthetic mechanisms, but latent-effect supervision rewards posterior shrinkage instead of directly encoding the repeated-sample response needed in a fixed deployment population. We introduce fluctuation-supervised pretraining (FSP): each synthetic table is labeled by its average treatment effect plus its efficient influence-function fluctuation, while deployment remains a single frozen forward pass. Along the path $T_{λ,P}=θ(P)+...
  </details>

- **2026-09-22** — Alex Samorodnitsky — [On the OpenAI whole-cube bound](http://arxiv.org/abs/2609.26050v1)
  <details><summary>📄 Abstract</summary>
  This is an essentially derivative note, whose goal is to interpret the 'whole-cube' bound of OpenAI for binary codes in a possibly somewhat more accessible way. This is attained, in part, by connecting it to some previously known results. All of the heavy technical lifting in the interpretation below is also due to the OpenAI language models ChatGPT 5.6 and ChatGPT 6. With that, we hope that the statements of the main results, the ensuing discussion, and the arguments themselves may be of some i...
  </details>

- **2026-09-22** — Ilias Mitsouras, Nikolaos Chaidos, Giorgos Stamou et al. — [EMERGE: Resolution-Agnostic Point Cloud Generation with Equivariant Graph-Based Diffusion](http://arxiv.org/abs/2609.26039v1)
  <details><summary>📄 Abstract</summary>
  Point cloud generation has emerged as a crucial task for accurately capturing and reproducing the complexity of the physical world. However, existing generative approaches, predominantly relying on Transformers and Variational Autoencoders (VAEs), frequently ignore the continuous, non-grid topologies inherent to 3D spaces. Although the integration of graph-based structures has yielded significant benefits in related discriminative vision tasks, such geometric architectures remain noticeably abse...
  </details>

- **2026-09-22** — Yuhang Zhang, Rangya Zhang, Yujing Shang et al. — [Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models](http://arxiv.org/abs/2609.26007v1)
  <details><summary>📄 Abstract</summary>
  Monocular drone navigation requires reaching a goal in an unseen environment from a single forward-facing camera, which offers few cues for depth and scale. World models address this by modelling how observations evolve under actions, but they are built to be executed: the prediction is produced at deployment and fed back into action generation at every control step. We argue that what a policy needs from a world model is not the prediction but the representation required to produce it: in fligh...
  </details>

- **2026-09-22** — Alberto Ibort, Maria Jimenez-Vazquez, Juan M. Perez-Pardo — [Theory for groupoid equivariant neural networks: an approach for steerable CNNs on bounded domains](http://arxiv.org/abs/2609.25987v1)
  <details><summary>📄 Abstract</summary>
  Equivariant convolutional neural networks are usually built from a group acting globally on the space of signals. This hypothesis is inappropriate for many bounded or stratified domains: an ambient rigid motion may be admissible only on part of the domain, and the boundary introduces geometric types that are invisible to a transitive group action. We develop a theory of groupoid-equivariant neural networks in which the symmetry datum consists of a groupoid, a selected pseudogroup of local bisect...
  </details>

- **2026-09-22** — Hongjin Song, Runwu Shi, Weiqiao Shan et al. — [Rethinking Length-Based Training: Batch Composition and Loss Normalization in Speech Token Language Models](http://arxiv.org/abs/2609.25890v1)
  <details><summary>📄 Abstract</summary>
  Short-to-long training is a simple curriculum for speech models, but its gains can be difficult to interpret. In speech token language models, length-based training can change the shuffle policy, batch composition, token retention, and token weights under batch-mean loss. We disentangle these factors through matched comparisons. In the tested settings, short-to-long ordering shows no independent benefit when batch composition and token exposure are fixed. First-epoch grouping lowers perplexity f...
  </details>

- **2026-09-22** — Yijia Hao, Pratibha Verma, Dongxu Guo et al. — [AgenticSizing: A Large Language Model-based Multi-Agent Framework for Analog Circuit Sizing](http://arxiv.org/abs/2609.25873v1)
  <details><summary>📄 Abstract</summary>
  Analog circuit sizing remains a challenging and time-consuming task due to the large design space, strong performance trade-offs, and increasing circuit complexity in scaled technologies. Although recent large language model (LLM)-based methods show promise in improving sample efficiency and interpretability, existing approaches often lack explicit circuit-topology understanding and are mainly evaluated on relatively simple analog building blocks. This paper presents a multi-agent LLM-based fram...
  </details>

- **2026-09-22** — Oliver Křenek, Vít Průša, Rebecca Tozzi et al. — [Uniform approximation of spectra of linear second order differential operators via discrete sine transform based discretisation](http://arxiv.org/abs/2609.25796v1)
  <details><summary>📄 Abstract</summary>
  We study various discretisation schemes for the regular Sturm--Liouville operator on a bounded interval and for the Laplace operator on an arbitrary planar domain, in both cases subject to zero Dirichlet boundary conditions. The objective is to identify a discretisation scheme such that the corresponding discretised operator---a matrix of size $N \times N$---produces $N$ eigenvalues that approximate as closely as possible the first $N$ eigenvalues of the corresponding operator at the continuous ...
  </details>

- **2026-09-22** — Xiaoning Wang, Ted Underwood, Zhewei Sun — [From Utterances to Networks: Modelling Slang Adoption and Diffusion Across Subreddits](http://arxiv.org/abs/2609.25669v1)
  <details><summary>📄 Abstract</summary>
  Adoption and diffusion of neologisms in online communities have received renewed attention in recent years. As internet slang terms such as APT, referring to a K-pop song, and phrases such as Canon Event meaning an embarrassing but pivotal event, go viral online, it becomes increasingly important to understand the mechanisms that contribute to their success. Prior studies have often explained slang diffusion either from the perspective of social interaction or from the linguistic properties of t...
  </details>

- **2026-09-22** — Zijun Lin, Zhiyang Deng, Yuzhe Wu et al. — [GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](http://arxiv.org/abs/2609.25652v1)
  <details><summary>📄 Abstract</summary>
  Recent game world models support realistic visual simulation and interactive gameplay based on player inputs. However, they typically learn environment dynamics from pixel-level supervision, jointly modeling perception, memory, state transitions, and rendering within a single end-to-end framework. While this design enables open-ended, action-controllable generation, it still falls short of delivering a complete gameplay experience. Games are governed by explicit mechanics, such as health deducti...
  </details>

- **2026-09-22** — Tak Hur — [When Quantum Meets AI: Quantum Methods for Machine Learning and Machine Learning Methods for Quantum Systems](http://arxiv.org/abs/2609.25641v1)
  <details><summary>📄 Abstract</summary>
  This thesis studies the intersection of quantum computing and artificial intelligence in two directions: quantum methods for machine learning and machine learning methods for quantum systems. For quantum machine learning, Neural Quantum Embedding learns data representations that increase the trace distance between embedded class ensembles, lowering an embedding-dependent bound on empirical risk and improving classification on noisy quantum hardware. A training objective based on the Hilbert-Schm...
  </details>

- **2026-09-22** — Md Abrar Jahin, Craig A. Knoblock, Jay Pujara — [ArticleMiner: Ontology-Guided Knowledge Graph Construction from Scientific Publications](http://arxiv.org/abs/2609.25607v1)
  <details><summary>📄 Abstract</summary>
  Scientific papers keep much of their quantitative content in tables and supplementary files, where a number means something only through its header, caption, unit, analytical method, and the conventions of its field. Recovering the rows and columns of a table is therefore not the same as recovering the scientific fact it reports. Most semantic table-interpretation methods assume that a clean table is already available and subsequently map its cells or columns to ontology terms, whereas most publ...
  </details>

- **2026-09-21** — Parth Gor, Sourya Roy, Kasturi Varadarajan — [Near-Optimal Online Metric Matching on $Δ$-ary HST](http://arxiv.org/abs/2609.25292v1)
  <details><summary>📄 Abstract</summary>
  In the online metric matching problem, we have $n$ servers with known locations in some metric space. Requests arrive one-by-one at certain locations, and upon arrival a request must be matched to a server that was not matched to a previous request. The goal is to minimize the matching cost. For randomized algorithms with an oblivious adversary, the best known competitive ratio is obtained by embedding the metric space into an HST, and then solving the problem in the setting where the metric spa...
  </details>

- **2026-09-21** — Zhiping Wu, Dongdong Ren, Yangchengyu Zhou et al. — [RGSQ: Riemannian Geometry-Sensitive Quantization for Large Vision-Language Models](http://arxiv.org/abs/2609.25492v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (VLMs) can be efficiently deployed under stringent memory and latency constraints through post training quantization (PTQ). However, most PTQ methods are designed for unimodal large language models (LLMs). These methods treat quantization errors as isotropic perturbations under the Euclidean assumption, which provides weak guidance on directions most sensitive to quantization in VLMs. Consequently, directly adapting unimodal PTQ approaches or solely employing modalit...
  </details>

- **2026-09-21** — Miray Wahib, Ethan Tran, Rea Mourad et al. — [Spectra: A Rules-Driven LLM Pipeline for Automated KYC Document Processing](http://arxiv.org/abs/2609.25474v1)
  <details><summary>📄 Abstract</summary>
  Know Your Client (KYC) onboarding in capital markets requires analysts to manually classify documents, extract structured data from heterogeneous sources, and validate compliance against complex regulatory policies. This process requires significant analyst time per client, with end-to-end onboarding often stretching to multiple weeks due to sequential handoffs. In this work, we analyze an on-boarding process and find that it comprises repeatable components well-suited to AI automation. We there...
  </details>

- **2026-09-21** — Xiaotie Deng, Ningyuan Li — [Strategic Disclosure of Action Space in Principal-Agent Contracts](http://arxiv.org/abs/2609.25410v1)
  <details><summary>📄 Abstract</summary>
  We study strategic disclosure of the action space in principal-agent contracting, where an agent selects a disclosed action set to shape the principal's perception of her capabilities before contract design. Unaware of the strategic disclosure, the principal designs a revenue-optimal contract as if the disclosed action set were complete and accurate. We consider two variants distinguished by cost verifiability. When costs are unverifiable, the agent can extract the entire first-best surplus, lea...
  </details>

- **2026-09-21** — Lujia Bao, Qian Chen, Luyao Cheng et al. — [Qwen-Audio-3.1-Realtime: Towards Reliable Agentic Voice Interaction](http://arxiv.org/abs/2609.25176v1)
  <details><summary>📄 Abstract</summary>
  Real-time voice assistants must reason over evolving requests, execute actions, and follow conversational rules. Qwen-Audio-3.1-Realtime brings these requirements together through Think, Act, and Speak and Coordinate. Think combines Core-Cocktail supervised fine-tuning with Multimodality and Multi-Teacher On-Policy Distillation (M$^{2}$-OPD) to transfer language capabilities and develop native audio skills. Act uses self-evolving executable environments and multi-granularity rollouts for Group R...
  </details>

- **2026-09-21** — Elvin Yang, Christoforos Mavrogiannis — [Learning from Humans for Proactive Assistance in Human-Robot Collaborative Transport](http://arxiv.org/abs/2609.25351v1)
  <details><summary>📄 Abstract</summary>
  We focus on human-robot collaborative transport, a challenging task of broad relevance spanning logistics, manufacturing, and the home, in which a user and a robot work together to relocate a large or heavy object. To act as an effective partner, the robot should reduce the user's effort by contributing to efficient relocation of the object while remaining physically responsive to them. Prior work often addresses these capabilities separately, producing robots that may move the object efficientl...
  </details>

- **2026-09-21** — Howard Lu, Shalfun Li, Porter Pan et al. — [X-Planner: Event-Structured Task Planning for Embodied Intelligence](http://arxiv.org/abs/2609.25187v1)
  <details><summary>📄 Abstract</summary>
  Task planning bridges high-level instructions and executable behavior in long-horizon manipulation, yet modern Vision-Language-Action (VLA) systems often leave this intermediate structure implicit. Existing chain-of-thought (CoT) planners also tend to rely on coarse task-level annotations or serialize long reasoning traces token by token. We present X-Planner, a planning front-end that addresses both the supervision and representation of embodied reasoning. Our planning data combine Ego, UMI, an...
  </details>

- **2026-09-21** — Hongwei Yan, Kanglei Zhou, Qi Cheng et al. — [Brain-Inspired Hierarchical Modularity for General Continual Learning](http://arxiv.org/abs/2609.25146v1)
  <details><summary>📄 Abstract</summary>
  Continual learning, the ability to learn from sequential experience while retaining and adapting prior knowledge, is central to intelligent systems operating in changing environments. However, conventional continual learning is typically studied with offline task-wise training and clear task boundaries, leaving a substantial gap from general continual learning under online, uncertain, and evolving data streams. In this regime, intelligent systems must separate conflicting experience to reduce in...
  </details>

- **2026-09-21** — Daniel Halpern, Abhiram Manohara, Alexandros Psomas — [Prophet Inequalities Beyond Utilitarian Social Welfare](http://arxiv.org/abs/2609.25424v1)
  <details><summary>📄 Abstract</summary>
  In the classical i.i.d. prophet-inequality problem, a single item is allocated to one of $n$ agents who arrive sequentially, with values drawn independently from a known distribution. When an agent arrives, their value is revealed, and the algorithm must immediately allocate the item or continue. The usual objective is utilitarian welfare: the expected value of the recipient. Guarantees for this objective extend to allocating $m$ indivisible items to sequentially arriving agents with i.i.d.\ add...
  </details>

- **2026-09-21** — Zoha Azimi, Reza Farahani, Schahram Dustdar et al. — [Cloud, Edge, or Split? Profiling Onboard and Split Vision-Language Model Deployment for Drone AI](http://arxiv.org/abs/2609.25415v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) enable edge devices like unmanned aerial vehicles (UAVs) to interpret visual observations and reason about complex environments using natural-language instructions. However, their practical deployment remains challenging as onboard inference is constrained by limited computational, memory, and energy resources, whereas cloud-based inference introduces communication latency, bandwidth overhead, and dependence on network connectivity. To address these limitations, spl...
  </details>

- **2026-09-21** — Luiza Treichel Mossi, Nicole Mazzitelli Narvaz, Larissa da Silva Bento et al. — [Statistical signatures of microorganism motility under environmental stress](http://arxiv.org/abs/2609.25403v1)
  <details><summary>📄 Abstract</summary>
  The motility of microorganisms provides a natural framework for studying active matter and its response to environmental perturbations. We experimentally investigate the trajectories of \textit{Paramecium caudatum} and \textit{Artemia salina} under controlled conditions. Using video microscopy, we reconstruct individual trajectories over time. Beyond baseline conditions, we analyze stressed environments where \textit{P. caudatum} are exposed to a toxic agent and \textit{A. salina} are placed in ...
  </details>

- **2026-09-21** — Mike Thelwall, David Pride, Francesco Osborne et al. — [Scoring Grant Applications with Large Language Models](http://arxiv.org/abs/2609.25327v1)
  <details><summary>📄 Abstract</summary>
  Purpose: Assessing grant applications is time-consuming and difficult, adding to the overall burden of academic peer review. Whilst funders are exploring whether AI can help, there is no published research into the accuracy of Large Language Models (LLMs) for scoring contemporary grants. Design/methodology/approach: This study investigates whether six open-weight LLMs (Gemma 3 1B/4B/12B/27B, DeepSeek R1 32B, Qwen 3 32B) can give useful scores for 2267 recent UK Economic and Social Research Counc...
  </details>

- **2026-09-21** — Zhiyao Zhang, Yichen Li, Xingyu Wu et al. — [Online Automated Algorithm Design with Large Language Models](http://arxiv.org/abs/2609.25325v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) enable automated algorithm design (AAD) through reasoning and code synthesis. However, most existing LLM-based AAD methods separate algorithm design from target optimization, deploying a fixed design even as the optimization state evolves. Conventional adaptive optimizers can respond to such changes, but their adjustments remain confined to predefined parameters, operators, or strategies. To address these limitations, we introduce online LLM-based AAD, a novel optimi...
  </details>

- **2026-09-21** — Afagh Mehri Shervedani, Siyu Li, Natawut Monaikul et al. — [Learning to Plan in Human-Robot Collaboration: Multimodal Reinforcement Learning for Adaptive Interaction](http://arxiv.org/abs/2609.25274v1)
  <details><summary>📄 Abstract</summary>
  Robot assistants for older adults and people with disabilities need to perform collaborative tasks with users effectively. The core component of these systems is an interaction manager whose job is to observe and assess the task and infer the state of the human and their intent for the robot to choose the best course of action. Due to the sparseness of the data in this domain, the policy for such multimodal systems is often crafted by hand; as the complexity of interactions grows, this process i...
  </details>

- **2026-09-21** — Guangchuan Lv, Dianxing Shi, Dingjie Fu — [VPRune: Efficient Training-free Pre-LLM Visual Token Pruning](http://arxiv.org/abs/2609.24485v2)
  <details><summary>📄 Abstract</summary>
  Visual token pruning is a promising approach to reducing the inference cost of large vision-language models (LVLMs), yet aggressive token reduction often causes substantial performance degradation. We identify three key factors behind this degradation: text-guided selection bias, information loss from discarded tokens, and positional distortion caused by sequence compaction. Based on these observations, we propose \textbf{VPRune}, a training-free pre-LLM pruning framework consisting of visual-on...
  </details>

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

- **2026-09-20** — Saghir Alfasly, Wataru Uegami, Sobhan Hemati et al. — [WILSON - a pathology foundation model framework for patient-level analysis and diagnostic text generation](http://arxiv.org/abs/2609.25123v1)
  <details><summary>📄 Abstract</summary>
  Pathologists integrate morphology across magnifications and across the slides of a patient case, whereas pathology foundation models encode thousands of tiles from single slides and aggregate their features. Here we present WILSON, a vision--language foundation model that represents whole-slide images and multi-slide cases as single multi-magnification composite images, trained on approximately 189k slides from Mayo Clinic spanning 42 organs and 829 diagnostic entities using pathology reports as...
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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 633 |
| prompt-injection | 550 |
| memory-poisoning | 50 |
| tool-use-attack | 137 |
| backdoor | 469 |
| adversarial-attack | 599 |
| privacy-leakage | 4145 |
| steganography | 71 |
| misuse | 1040 |
| red-teaming | 126 |
| vulnerability | 3187 |
| defense | 3012 |
| alignment | 2800 |
| robustness | 2963 |
| watermark | 464 |
| unlearning | 97 |
| agent-safety | 55 |
| benchmark | 66 |
| survey | 357 |
| other | 8017 |

---

📚 **全部 28838 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-23 02:56:09*