<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-21194-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-29 16:40 ｜ **论文总数 / Total Papers**: 21194（近 30 天 / Recent 30 days: 2293）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 21194 篇论文（含摘要、分类筛选、搜索）/ View all 21194 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 549
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 457
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 36
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 93
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 390
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 533
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3692
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 52
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 823
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 108
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2462
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2111
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1933
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1824
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 196
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 82
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 48
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 53
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 252
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5500

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2293 篇，完整 21194 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2293 papers from the last 30 days (with date, authors & abstract). For the full list of 21194 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 5 papers

- **2026-07-28** — Abhishek Kumar Singh, Shrey Nag, Sachita et al. — [Inspect India Evals: An Open Benchmarking Framework for Evaluating Large Language Models in the Indian Linguistic and Cultural Context](http://arxiv.org/abs/2607.25375v1)
  <details><summary>📄 Abstract</summary>
  India is a vast nation of over 1.4 billion people, varied by hundreds of diverse and locally specific traditions and cultures and 22 officially recognized languages. Large language models (LLMs) are now being deployed on a massive scale throughout the mainland as well as in remote villages. However, the common benchmarks - MMLU, BIG-Bench, and TruthfulQA are almost exclusively English- and Western-centric. They do not identify those safety, fairness, and accuracy failures unique to the Indian co...
  </details>

- **2026-07-28** — Haowen Dai, Zonghao Ying, Wenfeng Li et al. — [SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems](http://arxiv.org/abs/2607.25255v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems improve capability through task decomposition and role specialization, but these same mechanisms introduce an important safety blind spot: a harmful objective can be fragmented into locally plausible subtasks, allowing malicious intent to evade detection by any single agent. This is a growing social-impact challenge: systems handling sensitive information or consequential tools can turn routine delegation into unauthorized disclosure or unsafe action. We argue that this failu...
  </details>

- **2026-07-27** — Meng Xie, Li Zeng, Hangtao Zhang et al. — [TYPO: Instruction-Dense Visual Jailbreaks against Commercial Closed-Source Image-Generation Models](http://arxiv.org/abs/2607.24897v1)
  <details><summary>📄 Abstract</summary>
  Recent commercial image-generation models can generate high-quality images with readable text (e.g., posters, infographics, and manuals), attracting considerable attention. Yet we first show that this same capability also introduces a previously unreported safety vulnerability: these systems may refuse to generate harmful text directly, yet permit the same content when rendered as text within generated images, i.e., safety alignment does not reliably transfer from textual outputs to text embedde...
  </details>

- **2026-07-27** — Tong Zhang, Zexin Li, Simin Chen et al. — [When LLM Defenses Backfire: Characterizing Safety, Performance, and Cost Trade-offs](http://arxiv.org/abs/2607.24392v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak defenses are essential for protecting large language models (LLMs), but they can also introduce secondary costs that weaken model utility. We present a systematic study of these defense trade-offs along three dimensions: performance impact, over-refusal on benign inputs, and inference cost. Rather than treating defenses as a single class, we organize them by operational strategy and examine how different strategies correlate with different side-effect profiles. Across state-of-the-art ...
  </details>

- **2026-07-14** — Roman Prosvirnin, Victor Minchenkov, Alexey Soldatov et al. — [Silent Alarm: A J-Space Protocol for Comparing Danger Recognition Across Models and Quantization Levels](http://arxiv.org/abs/2607.12792v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak-robustness research typically evaluates safety through generated responses using an LLM-as-judge approach. Such evaluations, however, are sensitive to the benchmark's grading procedure and capture only observed behavior on a given set of attacks, without directly revealing the hidden fragility of the underlying safety mechanisms. This work proposes JADR (Jacobian Assessment of Danger Recognition), a protocol that measures a model's internal representation through Jacobian space (J-spac...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 5 papers

- **2026-07-27** — Arseny Kravchenko, Vadim Liventsev, Innokentii Konstantinov et al. — [Agentic Permissions Policy Algebra for Taint Confinement in LLM Agents](http://arxiv.org/abs/2607.24625v1)
  <details><summary>📄 Abstract</summary>
  Autonomous LLM agents processing mixed-confidentiality data face severe security risks from prompt injection attacks and reasoning errors. While dynamic Information Flow Control (IFC) provides structural security guarantees, traditional taint tracking permanently taints an agent's context upon reading unvetted data, severely restricting downstream utility. We present APPA (Agentic Permissions Policy Algebra), an IFC framework that resolves this usability bottleneck through engine-managed context...
  </details>

- **2026-07-27** — Max Landauer, Florian Skopik, Markus Wurzenberger et al. — [Just Testing, Move Along: Evasion of LLM-based System Log Interpretation by Prompt Injection](http://arxiv.org/abs/2607.24174v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly integrated into Security Operations Center (SOC) workflows, where they support analysts in tasks such as the interpretation of system logs. However, the ability of LLMs to directly process untrusted textual input also introduces new attack surfaces. In particular, attackers can inject contextual information or explicit instructions into log entries in order to influence how malicious activity is interpreted by the model. Despite the growing adoption ...
  </details>

- **2026-07-27** — Mohan Manivannan, Dalal Alharthi — [Agentic Cloud Decoys: A Deception-Driven Framework for Autonomous Intrusion Investigation](http://arxiv.org/abs/2607.24006v1)
  <details><summary>📄 Abstract</summary>
  Cloud telemetry arrives at a scale that, paradoxically, makes intrusion understanding harder rather than easier. Attackers operate through legitimate identity, federated session tokens, and cloud native APIs indistinguishable from routine administration, and analysts spend an incident reconstructing context the logs already contain. We present Cloud Decoy AI Agent, a framework pairing a high fidelity cloud decoy with an autonomous language model agent that compresses the path from suspicious act...
  </details>

- **2026-07-27** — Wenhao Lan, Shan Li, Xinhua Lai et al. — [ContainmentBench: Trace-Based Evaluation of Post-Injection Containment in Tool-Using LLM Agents](http://arxiv.org/abs/2607.23999v2)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents process untrusted content, maintain memory, delegate across agents, and invoke side-effecting tools. Existing prompt-injection evaluations typically summarize security with terminal attack or policy outcomes, but equal endpoints can conceal different post-exposure traces and different losses of authorized utility. We introduce ContainmentBench, a sandboxed, trace-based benchmark that separately measures benchmark-defined endpoint policy compliance, instrumented logged propa...
  </details>

- **2026-07-14** — Huihao Jing, Wenbin Hu, Shaojin Chen et al. — [Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions](http://arxiv.org/abs/2607.12406v1)
  <details><summary>📄 Abstract</summary>
  The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model. Consequently, safety is no longer only about input--output content alignment. It also concerns system behavior and real-world execution outcomes. However, the current literature is fragmented across attack types, applications, and benchmarks. This makes it hard to explain why failures such as prompt injection, tool misuse, and memory poisoning often share t...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-07-28** — Jianing Geng, Ruiqi He, Zekun Fei et al. — [Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories](http://arxiv.org/abs/2607.25560v1)
  <details><summary>📄 Abstract</summary>
  Agent skills package reusable procedures that improve downstream performance. Their lightweight, portable form enables marketplace monetization and private deployment behind cloud-hosted agent interfaces, giving providers incentives to keep high-value skills proprietary. Yet hiding the artifacts does not conceal their behavioral effects, which remain observable in execution trajectories and form a behavioral side channel. We define this exposure as Skill Leakage: reconstructing proprietary skill...
  </details>

- **2026-07-27** — Rajat Sainju, Dariusz Jarosz, Hairong Shang et al. — [A corrective agentic hybrid RAG and an operations-grounded evaluation for a scientific facility](http://arxiv.org/abs/2607.24663v1)
  <details><summary>📄 Abstract</summary>
  Scientific user facilities accumulate decades of operational knowledge that no single search index covers: electronic logbooks, technical documents, internal wikis, operations chat messages, maintenance records, and live control-system data. We present APS-RAG, Advanced Photon Source Retrieval Augmented Generation, a deployed platform that makes the institutional knowledge at the Advanced Photon Source (APS) accessible to staff through natural-language queries, along with an operations-grounded ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 4 papers

- **2026-07-28** — Rui Yang, Michael Fu, Kla Tantithamthavorn et al. — [SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents](http://arxiv.org/abs/2607.25619v1)
  <details><summary>📄 Abstract</summary>
  Software engineering teams now deploy AI coding agents (Cursor, Claude Code, GitHub Copilot) as first-class productivity tools, installing domain-specific skill files to tailor agent behavior to project APIs, framework conventions, and organizational workflows. These complex Markdown files are easily downloaded from public registries with a single npx skills add command and no real security screening, representing a novel supply-chain attack surface: a malicious skill file can silently reprogram...
  </details>

- **2026-07-28** — Maria Rosaria Briglia, Igor Maljkovic, Antonio Emanuele Cinà et al. — [Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering](http://arxiv.org/abs/2607.25479v1)
  <details><summary>📄 Abstract</summary>
  Vision--Language Models (VLMs) are increasingly deployed through a model supply chain in which pretrained checkpoints, architecture definitions, text encoders, and exported computation graphs are distributed by third parties and reused across downstream services. This reuse model creates a security-critical trust boundary: VLM deployments inherit not only learned parameters but also executable behavior encoded in shared model artifacts. In this paper, we show that a malicious provider can exploi...
  </details>

- **2026-07-27** — Diego Fernandez Arias, Dev Prashant Mistry, Ren Wang et al. — [Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study](http://arxiv.org/abs/2607.24893v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems can be attacked by a payload that no single agent ever holds in full: a poisoned tool hides encrypted fragments in its observations, spreads them across several agents, and an external step reassembles and executes them after the run. Per-step safety checks that judge each action in isolation may fail to recognize the complete distributed payload. We investigate how early such an attack can be detected while the run is still unfolding, and how robustly it can be caught on...
  </details>

- **2026-07-26** — Susil Kumar Mohanty, Rohit Patel, Kosuru Yuvaraj et al. — [TriShieldRAG: A Three-Ring Defense-in-Depth Framework Against Knowledge Corruption in Retrieval-Augmented Generation](http://arxiv.org/abs/2607.23838v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) lets a large language model answer questions using documents retrieved from an external knowledge base at query time. This makes RAG useful for private data, fast-changing information, and reducing hallucination, but it also means the model's answer is only as trustworthy as whatever the retriever hands it. If the knowledge base accepts writes from more than one party, an attacker needs only a handful of adversarial documents to steer the model toward a chose...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-07-28** — Anwar Alajmi, Ayed Salman, Imtiaz Ahmad — [Evaluation of Adversarial Robustness in Arabic Language Models](http://arxiv.org/abs/2607.25814v1)
  <details><summary>📄 Abstract</summary>
  The emergence of the recent outstanding capabilities of Arabic Language Models has opened doors for exposing their vulnerabilities. One of the major security risks associated with such Natural Language Processing models is adversarial attacks. These attacks can deceive the model into the wrong prediction, raising critical model security and safety concerns. This study aims to assess the robustness of five state-of-the-art Arabic Language Models under a distinct set of Arabic adversarial attacks ...
  </details>

- **2026-07-28** — Khalil Alhaj, Razane Tajeddine, Hadi Sarieddeen — [SignDeepSC: A Semantic Signature-based Approach for Robust Semantic Communication](http://arxiv.org/abs/2607.25676v1)
  <details><summary>📄 Abstract</summary>
  Semantic communication systems such as deep semantic communication (DeepSC) offer high efficiency but are vulnerable to adversarial attacks on their underlying neural networks. We address a physical-layer man-in-the-middle (MitM) threat in which an adversary injects perturbations into the transmitted signal to distort its meaning. We propose SignDeepSC, an architectural defense that achieves adversarial robustness without requiring explicit adversarial example generation during training. The app...
  </details>

- **2026-07-28** — Yimao Guo, Zuomin Qu, Wei Lu — [I2VShield: An Efficient Proactive Defense Framework against DiT-based Image-to-Video Models](http://arxiv.org/abs/2607.25522v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of video generation models has led to the increasing misuse of image-to-video (I2V) models. Although substantial progress has been made in detecting AI-generated videos, proactive defenses against I2V models remain underexplored. In particular, current proactive defenses against I2V models predominantly rely on gradient-based adversarial attacks, which require defenders to possess GPUs with substantial memory resources (VRAM) to generate adversarial examples. To address thi...
  </details>

- **2026-07-15** — Michal Štefánik, Philipp Mondorf, Andreas Waldis et al. — [AIMO Interpretability Challenge](http://arxiv.org/abs/2607.13899v1)
  <details><summary>📄 Abstract</summary>
  We propose the AIMO Interpretability Challenge, a competition on distinguishing robust from spurious reasoning in frontier mathematical language models based on the models' internal mechanisms. The challenge is motivated by a central limitation of standard reasoning benchmarks: strong final-answer accuracy does not reveal whether a model relies on stable reasoning mechanisms or exploits brittle reasoning shortcuts. Building on AI Mathematical Olympiad (AIMO) problems and submissions, together wi...
  </details>

- **2026-07-14** — Yuxin Huang, Ziming Hong, Mingming Gong et al. — [Delving into the Temporal Challenges of Unified Video Protection Against Image-to-Video and Fine-Tuning-based Customization](http://arxiv.org/abs/2607.13336v1)
  <details><summary>📄 Abstract</summary>
  Recent diffusion-based video generation models have enabled high-quality personalized video customization through both tuning-based pipelines, which fine-tune a video diffusion model, and reference-based pipelines such as image-to-video generation. However, these capabilities raise serious concerns about personal privacy, identity ownership and intellectual property protection. Existing anti-customization works focus on protecting images, while protection for videos against both reference- and t...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 17 papers

- **2026-07-28** — Akshay Sasi — [Bits and Memories: Measuring Verbatim Extraction Across LLM Quantization](http://arxiv.org/abs/2607.25451v1)
  <details><summary>📄 Abstract</summary>
  Language models are almost always quantized before they are deployed, and a growing line of work asks whether quantization also lowers their privacy risk. That work measures privacy almost entirely with membership inference. We think this is the wrong thing to measure for the risk that most people actually worry about, namely a model reproducing its training data word for word, and we measure that directly. Using the Pythia models and the public set of sequences each of them is known to have mem...
  </details>

- **2026-07-28** — Mohamed Nabih Ali, Daniele Falavigna, Alessio Brutti — [SpeechLLM Meets Federated Learning for End-to-End ASR: English and Italian Case Studies](http://arxiv.org/abs/2607.25716v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) enables privacy-preserving training of automatic speech recognition (ASR) systems across distributed data sources, yet its application to large-scale speech language models (SpeechLLMs) remains unexplored. This paper presents the first systematic study of federated training for SpeechLLM-based end-to-end ASR systems. We design a communication-efficient federated optimization strategy tailored to the unique challenges of SpeechLLM architectures, addressing high-dimensional...
  </details>

- **2026-07-28** — Yuwen Ma, Sarah Spurgeon, Tao Li et al. — [To What Extent Can Inherent Communication Noise Guarantee Privacy in Distributed Cooperative Control?](http://arxiv.org/abs/2607.25564v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a differentially private distributed cooperative control scheme for multi-agent systems (MAS). Unlike conventional approaches that actively inject artificial noise for privacy protection, this work investigates whether inherent communication noise can itself serve as a natural privacy mechanism. A physically motivated communication-noise model is developed for mobile MAS by incorporating transmitter perturbation, receiver noise, path-loss attenuation, and log-normal shadowing...
  </details>

- **2026-07-28** — Wanxu Cai, Zhengyu Chen, Huaisheng Zhu et al. — [Distilling Temporal Search and Reasoning: Evolving LLMs for Future Prediction via Harness-Assisted Efficient Data Synthesis](http://arxiv.org/abs/2607.25554v1)
  <details><summary>📄 Abstract</summary>
  Future event prediction carries broad social impact yet remains challenging. SOTA approaches augment LLMs with external agent frameworks whose predictive capability vanishes once the harness is removed. While recent Tool-Integrated Reasoning (TIR) internalizes deep search for multi-hop retrieval of facts, forecasting further demands temporal search and reasoning over historical trends and dynamic shifts. The key obstacle is data: historical queries induce temporal leakage that degrades forecasti...
  </details>

- **2026-07-27** — Taimoor Rizwan, Sara Atito, Muhammad Awais et al. — [Diff-ID: Identity Consistent Facial Image Generation and Morphing via Diffusion Models](http://arxiv.org/abs/2607.25078v1)
  <details><summary>📄 Abstract</summary>
  Generative diffusion models have revolutionized facial image synthesis, yet robust identity preservation in high resolution outputs remains a critical challenge. This issue is especially vital for security systems, biometric authentication, and privacy sensitive applications, where any drift in identity integrity can undermine trust and functionality. We introduce Diff-ID, a diffusion based framework that enforces identity consistency while delivering photorealistic quality. Central to our appro...
  </details>

- **2026-07-27** — Steve Aschenbrenner, Marcel Heisler, Thomas Sievers et al. — [Not Forgotten: Implementation and Evaluation of a Personalized Episodic Memory for the Humanoid Robot Head Kim](http://arxiv.org/abs/2607.24190v1)
  <details><summary>📄 Abstract</summary>
  Social robots that rely on large language models for conversation are unable to retain information across sessions. This absence of memory violates social expectations, potentially preventing the formation of persistent relationships. This paper presents a lightweight episodic memory module that integrates vector-based semantic retrieval with an LLM-controlled dialog system, deployed on the humanoid robot head Kim. The module employs a hybrid scoring function combining cosine similarity with a m...
  </details>

- **2026-07-27** — Zihan Li, Feiyang Liu, Dandan Shan et al. — [OPERA: Offline Policy-guided Expert Routing and Adaptation for Universal Biomedical Image Analysis](http://arxiv.org/abs/2607.25108v1)
  <details><summary>📄 Abstract</summary>
  Biomedical image analysis spans diverse modalities and tasks, yet real-world deployment is hindered by severe distribution shifts across scanners, protocols, and patient populations. High-performing models consequently require repeated domain-specific fine-tuning, which is a costly cycle that becomes impractical when labels are scarce or privacy constraints limit data sharing. We propose OPERA (Offline Policy-guided Expert Routing and Adaptation), a multi-agent ensemble framework that addresses ...
  </details>

- **2026-07-27** — Oluwadara Adedeji, Michael Mayowa Farayola, Jeff Brozena et al. — [A Computational Ethical Framework for Financial Digital Phenotyping for Mental Health](http://arxiv.org/abs/2607.24275v1)
  <details><summary>📄 Abstract</summary>
  Ethical governance of AI-driven systems is often expressed through high-level principles and static documentation, creating a gap between regulatory requirements and system-level verification. This challenge is particularly acute in digital phenotyping, where continuous behavioural data raises concerns around consent, privacy, and fairness. In this paper, we propose a computational ethical framework for AI-driven digital phenotyping system in which ethical requirements are formalised as deontic ...
  </details>

- **2026-07-26** — Arman Kolozyan, Tom Sorger, Alexander Hicks et al. — [ZKP Security Tools and Verification: Coverage, Effectiveness, Adoption, and Challenges](http://arxiv.org/abs/2607.23752v1)
  <details><summary>📄 Abstract</summary>
  Zero-knowledge proofs (ZKPs) have become a core technology for privacy and verifiable computing. They are used to secure blockchains that handle billions of dollars and identity applications dealing with sensitive personal data. However, ZKP systems are complex, and subtle implementation errors can completely break their guarantees, letting attackers forge money or false proofs of identity. Researchers and practitioners have therefore developed a growing set of bug detection and formal verificat...
  </details>

- **2026-07-26** — Yuhang Wang, Lingyao Li, Hao Zhou — [DriveDNA: A Large-Scale Multimodal Naturalistic Driving Dataset and Benchmark for Driving Style Identification](http://arxiv.org/abs/2607.23822v1)
  <details><summary>📄 Abstract</summary>
  Driving style captures stable, driver-specific patterns in how a vehicle is driven. In naturalistic data, however, this signal is hard to isolate because drivers are observed in different vehicles, on different roads, and under different conditions, so models may mistake vehicle- or situation-specific regularities for driver-specific style. We introduce DriveDNA, a large-scale naturalistic dataset and benchmark for personalized driving-style modeling, comprising 4,121 drives from 465 drivers acr...
  </details>

- **2026-07-15** — Ilef Chebil, Asma El Hadj, Souheib Yousfi et al. — [PriEval-Protect: A Unified Framework for Privacy Evaluation and Protection in Healthcare Systems](http://arxiv.org/abs/2607.13754v1)
  <details><summary>📄 Abstract</summary>
  Safeguarding patient privacy while enabling meaningful healthcare data use remains critical under GDPR and HIPAA. Existing compliance methods are manual, error-prone, and separate policy audits from data-level assessments. This paper presents PriEval-Protect, a two-phase framework for unified privacy risk evaluation and mitigation. The evaluation phase combines regulatory compliance scoring using a fine-tuned legal LLM with RAG, and technical analysis via encryption type, data architecture, and ...
  </details>

- **2026-07-15** — Michael O. Eniolade — [Evaluating Frontier AI Agents as Autonomous Clinical Security Auditors](http://arxiv.org/abs/2607.13411v1)
  <details><summary>📄 Abstract</summary>
  Clinical AI models can expose patients to harm when adversarial vulnerabilities go undetected, yet formal security auditing requires statistical expertise, specialized tools, and significant time. We present an open evaluation task, built on METR Task Standard v0.3.0, that tests whether frontier AI agents can autonomously implement a structured clinical AI security audit. Given a pre-trained clinical prediction model, a patient dataset, and written instructions, each agent must implement four at...
  </details>

- **2026-07-14** — Ranjeet K Jha, Venkata Suresh Gummadilli — [Privacy Preserving Recommender Systems Balancing Personalization with Privacy](http://arxiv.org/abs/2607.13328v1)
  <details><summary>📄 Abstract</summary>
  Personalized recommendation systems are central to modern e-commerce and retail platforms, but they typically rely on centralized storage of detailed user interaction data, creating significant privacy and regulatory challenges. With increasing requirements from regulations such as GDPR, CCPA, and CPRA, organizations must develop recommendation systems that preserve user privacy without substantially degrading recommendation quality.   This work presents and evaluates a privacy-preserving recomm...
  </details>

- **2026-07-14** — Bruce Coburn, Jingbo Yue, Jinge Ma et al. — [Open-KNEAD: Knowledge-grounded Nutrition Estimation via Agentic Decomposition](http://arxiv.org/abs/2607.12911v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) are increasingly used for dietary assessment from meal images, where retrieval-augmented grounding was shown to sharpen nutrition estimates. However, we find this premise no longer holds for current MLLMs. A modern MLLM's direct estimate now matches or surpasses the full retrieval pipeline. This raises a question: if retrieval no longer improves the overall estimate, can it still deliver the two things clinicians value, accurate portions and a traceable, ...
  </details>

- **2026-07-14** — Sai Sandeep Damera, John S. Baras — [Stability Buys Time: A Re-Keying Game for Encrypted Multi-Agent Control](http://arxiv.org/abs/2607.12742v1)
  <details><summary>📄 Abstract</summary>
  Encrypted control lets a cloud coordinate a fleet of agents on fully homomorphically encrypted state, keeping their positions and commands private. The approximate scheme for real-valued control, CKKS, returns decryptions that carry the encryption noise, a key-recovery leak; the loop must decrypt to actuate, so the leak is unavoidable. Yet the security of approximate FHE is studied statically, encrypted control assumes an honest-but-curious cloud, and persistent-threat games never reach inside t...
  </details>

- **2026-07-14** — Wenhao Zhang, Zhongliang Zhou, John Kang et al. — [Auditing Data Leakage in Whole-Slide Image Multimodal Benchmarks](http://arxiv.org/abs/2607.12278v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language models (VLMs) for computational pathology report striking zero-shot performance on whole-slide image (WSI) visual question answering (VQA) benchmarks. We audit these claims and find them fundamentally compromised by data leakage at two hierarchical levels: patient-level leakage, where slides from the same case appear in both training and test folds, and institutional-level leakage, where different cases nonetheless share staining-batch and scanner signatures through a comm...
  </details>

- **2026-07-13** — Navnit Shukla — [Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and Generation in Multi-Tenant LLM Systems](http://arxiv.org/abs/2607.12188v1)
  <details><summary>📄 Abstract</summary>
  Enterprise Retrieval-Augmented Generation (RAG) deployments face a critical governance gap: while LLM generation cost is metered per token, the retrieval layer - vector memory, similarity compute, and embedding API calls - remains an unattributed shared cost, enabling invisible cross-subsidization among tenants. We present Cost-Governed RAG, an architecture that integrates a codebook-oblivious vector index (TurboVec) with a multi-tenant LLM governance gateway, creating a unified observability st...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 14 papers

- **2026-07-28** — Yinuo Zhu, He Liu, Boyuan Gu — [BioDisclose: An Actionability-Aware Benchmark for Biomedical Safety under Adversarial Elicitation](http://arxiv.org/abs/2607.25700v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly support biomedical research, yet their behavior under adversarial requests for dual-use knowledge remains insufficiently characterized. We introduce BioDisclose, a benchmark for measuring biomedical knowledge disclosure under adversarial elicitation. BioDisclose contains 480 prompts derived from 24 expert-authored scenarios across six biomedical risk domains and four elicitation families spanning academic, historical, role-playing, and decomposed prompti...
  </details>

- **2026-07-28** — Abu Bakar Siddik — [Cyber-Capable AI Agents: Vulnerabilities, Evaluation Containment, and Defensive Response](http://arxiv.org/abs/2607.25379v1)
  <details><summary>📄 Abstract</summary>
  Cyber-capable AI agents combine language models with tools, memory, and execution en- vironments to perform multi-step offensive-security tasks. Existing work separately measures cyber capability and catalogs attacks against agent components, but provides less guidance on containing a capable agent within the environments used to evaluate it. This review synthe- sizes five vulnerability classes at that boundary: multi-step offensive chains, objectives that conflict with sandbox boundaries, suppl...
  </details>

- **2026-07-28** — Yongyi Cui, Yue Li, Tianbao Jiang et al. — [Construction-Driven Injection: Linguistically-Grounded Edit-Based Code-Mixing Fingerprints for Large Language Models](http://arxiv.org/abs/2607.25633v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are costly intellectual assets that remain exposed to unauthorized redistribution and commercial misuse. Injected fingerprints, i.e., trigger--target pairs embedded in model behavior, offer a practical, black-box-verifiable ownership signal, but existing methods decouple the two stages of the fingerprint life cycle: how a fingerprint is constructed and how it is injected. Existing fingerprinting frameworks suffer from two limitations. Natural-language fingerprints ar...
  </details>

- **2026-07-28** — Ping He, Yuexiang Xie, Yaliang Li et al. — [Hybrid Analysis for Secure MCP Tool Use in LLM Agents](http://arxiv.org/abs/2607.25297v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of large language model (LLM) agents has enabled their broad adoption across diverse real-world tasks. To standardize interactions between LLM agents and external environments, Model Context Protocol (MCP) tools have emerged as a de facto standard and have been widely integrated into these systems. However, the use of MCP tools also introduces new safety risks, as LLM agents can be induced to perform malicious or unauthorized actions. Although prior work has proposed defens...
  </details>

- **2026-07-28** — David Demitri Africa, Cate Heine, Nadine Staes-Polet et al. — [Detecting CSAM Text-to-Image LoRAs From Weights](http://arxiv.org/abs/2607.25750v1)
  <details><summary>📄 Abstract</summary>
  Low-rank adaptation (LoRA) fine-tuning has made it cheap and easy to customize open-weight image generation models for specific tasks, including the production of child sexual abuse material (CSAM). Existing moderation relies on metadata or generated outputs, but metadata can be deceptive and generating outputs may itself be unacceptable or illegal. We show that a safer signal lives in the weights. The top-left singular vectors of a LoRA's updates form a compact, inference-free fingerprint ($u_1...
  </details>

- **2026-07-28** — Rodolfo Rizzi, Alessandro Grecucci, Massimo Stella — [MyMentorLLM: A psychotherapy GenAI environment with multimodal voice/text patients, trainees and experts for deliberate practice](http://arxiv.org/abs/2607.25667v1)
  <details><summary>📄 Abstract</summary>
  Psychotherapists need repeated training and supervision by experts; however, scalability is problematic. Here we present MyMentorLLM, a multimodal voice- and text-based simulation environment for deliberate practice, used to generate 2,100 complete Cognitive Behavioural Therapy (CBT) training sessions. Each session links a DSM-5-TR-grounded patient (with major depressive, generalised anxiety or borderline personality disorder), a therapist-in-training and an expert supervisor. As an initial impl...
  </details>

- **2026-07-28** — Frank Yingjie Huo, Neil F. Johnson — [Many-body Tipping Dynamics of ChatGPT-like AIs](http://arxiv.org/abs/2607.25279v1)
  <details><summary>📄 Abstract</summary>
  Why do ChatGPT-like AIs, despite major architectural and training differences, unexpectedly tip to undesirable content (e.g. harmful, misleading, repetitive) even under deterministic greedy decoding? We show that a broad class of such tippings is caused by the many-body interactions between tokens (spins) as they cross the finite-layer system. Tipping emerges as a dynamical first passage process between competing output basins. Attention disorder controls the transport toward, away from, or alon...
  </details>

- **2026-07-28** — Benjamin Cookson, Soroush Ebadian, Dominik Peters et al. — [Proportional Fairness for Harmful Decisions](http://arxiv.org/abs/2607.26053v1)
  <details><summary>📄 Abstract</summary>
  We study allocation of (divisible) public bads, where agents incur costs for alternatives and the goal is to pick a lottery over the alternatives. We show that the traditional definitions of the core, a central criterion of proportional representation for allocation of public goods, private goods, and private bads (chores), do not make sense for allocation of public bads.   We introduce two formalizations of the core tailored to public bads. Under a structural condition which subsumes allocation...
  </details>

- **2026-07-27** — Cen Lu, Yung-Chen Tang, Andrea Cavallaro — [Similar Models Learn Differently: Final-Window Pretraining Shapes Post-Training Beyond SFT](http://arxiv.org/abs/2607.25063v1)
  <details><summary>📄 Abstract</summary>
  Developers judge a model checkpoint by how it behaves. After supervised fine-tuning (SFT), two checkpoints that perform about the same across relevant benchmarks are treated as interchangeable, equally ready for the next alignment stage, typically preference optimization. We ask whether this judgment misses a pretraining imprint: a difference that no post-SFT benchmark reveals, yet that decides how each checkpoint responds to further training. To find out, we run a controlled experiment on the f...
  </details>

- **2026-07-27** — Xinnuo Xu, Anja Thieme, Daniela Massiceti et al. — [Harm is not Universal: Community-Specific Toxicity Detection is Urgently Needed](http://arxiv.org/abs/2607.24898v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art toxicity detectors for text-to-image generation adopt a one-size-fits-all approach: a single universal model applying fixed safety guidelines to all users. Our empirical evidence shows that these detectors fail to shield marginalized communities: approximately 35% of generated images labeled safe are considered harmful by disability communities. In this position paper, we argue for community-specific toxicity detection (CTD). To demonstrate its feasibility, we collaborate with d...
  </details>

- **2026-07-26** — Ronnie de Souza Santos, Italo Santos, Maria Teresa Baldassarre et al. — [The Influence of Fraudulent AI-Generated Responses on Software Engineering Surveys](http://arxiv.org/abs/2607.23805v1)
  <details><summary>📄 Abstract</summary>
  Background: Large Language Models (LLMs) introduce new concerns regarding fraudulent or AI assisted participation in software engineering surveys. Aims: This study investigates how suspicious or potentially AI assisted responses may affect the validity of software engineering survey findings. Method: We conducted a secondary analysis of four software engineering survey datasets using manual identification of suspicious responses, automated AI generated text detection, descriptive statistical ana...
  </details>

- **2026-07-15** — Qiang Zhu, Jiajun Wu — [LAPO: Leave-One-Turn Attribution for Self-Generated Process Rewards in Multi-Turn Search Reasoning](http://arxiv.org/abs/2607.13501v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for multi-turn search reasoning typically relies on terminal outcome rewards, which cannot distinguish useful, redundant, and harmful intermediate interactions. We propose LAPO, a self-generated process-supervision method based on backward leave-one-turn attribution. For each search turn, LAPO replaces the turn and its retrieval observation with a fixed [DELETE] placeholder and measures the resulting change in the current policy's mean log-likelihood of the gold answer. Th...
  </details>

- **2026-07-14** — Paolo Magliano, Puze Liu, Jan Peters et al. — [Directional Constraints for Efficient Exploration in Safe Reinforcement Learning](http://arxiv.org/abs/2607.12784v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning has revolutionized the landscape of robotic research, allowing robust learning of complex robotic skills in simulation. However, real-world deployment in open-ended environments requires strong safety guarantees to prevent dangerous or harmful behaviors. Safe Reinforcement Learning methods address this requirement by enforcing safety constraints. Nevertheless, learning under constraints often reduces learning speed and could lead to suboptimal task performance, as the agen...
  </details>

- **2026-07-14** — Z Sun, Q Jiang, S Sheng et al. — [WaterMoE: Expert-Routing-based Watermarking for High Fidelity and Efficiency](http://arxiv.org/abs/2607.13099v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have achieved remarkable success but raise growing concerns about content provenance and misuse, motivating the need for reliable watermarking techniques. However, these techniques have rarely been adopted in practice mainly for two reasons: i) severely degraded model performance, and ii) additional inference overhead. To confirm the problem, we construct a comprehensive benchmark spanning different generation tasks to systematically evaluate 9 representative waterma...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-07-14** — Yakov Pyotr Shkolnikov — [Composable Trust for Language Models: A proven boundary and a measured defense](http://arxiv.org/abs/2607.13149v1)
  <details><summary>📄 Abstract</summary>
  In a language model, instructions and data share one token stream, so nothing inside the model's generation can keep untrusted text from steering it. We develop a trust model that places the authority to act outside the model, in code: a source's standing, not its content, decides which operation runs and whether it acts. A lower-trust source may inform an answer but not override a higher one. An unmodified model runs inside a deterministic pipeline that ranks inputs by source integrity, and a f...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 51 papers

- **2026-07-28** — Zhiyi Mou, Wangze Ni, Tianfang Xiao et al. — [From Role Prompt to Infinite Thinking: Exploiting Persona Conditioning for Inference Cost Attacks in LLMs](http://arxiv.org/abs/2607.25936v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly deployed in real-world applications, making inference efficiency and service reliability critical concerns due to their substantial computational costs. However, the autoregressive generation mechanism of LLMs enables malicious prompts to manipulate generation behaviors, inducing excessive token generation that amplifies computational consumption and threatens service efficiency. Existing methods mainly rely on adversarial suffixes or explicit extension instructions, which ...
  </details>

- **2026-07-28** — Pau Baguer, J. Xavier Salvat Lozano, Gines Garcia-Aviles et al. — [C-RE-ACT: Causal RE-ACTing Agent for O-RAN Forensic Triage](http://arxiv.org/abs/2607.25828v1)
  <details><summary>📄 Abstract</summary>
  The shift to O-RAN architectures marks a turning point in cellular security, where increased openness and modularity directly translate into a broader attack surface. Among the security threats cataloged by the O-RAN Alliance Working Group 11, performance-degradation attacks constitute the largest class. These attacks induce packet losses and latency spikes that are hard to distinguish from operational events such as misconfigurations, transient congestion, or software regressions. Consequently,...
  </details>

- **2026-07-28** — Yu Su, Nabil Aouf — [Cooperative Multi-UAV Navigation in Complex Environments via Systematic Multi-Agent Deep Reinforcement Learning](http://arxiv.org/abs/2607.25754v1)
  <details><summary>📄 Abstract</summary>
  Cooperative navigation of multi-agent UAVs in complex environments faces key challenges including local optima traps, sparse rewards, learning imbalance among agents, and insufficient cross-scenario generalisation. This paper proposes a multi-agent deep reinforcement learning framework that addresses these issues through coordinated exploration, demonstration exploitation, safe curriculum scheduling, and structure-aware generalisation. First, a perception mechanism combining memory of visited st...
  </details>

- **2026-07-28** — Xinran Liu, Shengtao Li, Shouqian Shi et al. — [IRIS: Reusable Identity Representations from Frozen LLMs for Entity Alignment](http://arxiv.org/abs/2607.25579v1)
  <details><summary>📄 Abstract</summary>
  Entity alignment (EA) identifies entities across knowledge graphs (KGs) that refer to the same real-world object. Conventional EA methods mainly exploit explicit graph structures and textual fields, which often provide insufficient semantic understanding to recognize the same entity under heterogeneous descriptions and distinguish it from semantically similar entities. Although large language models (LLMs) offer deeper entity understanding, existing LLM-based EA methods largely use this capabili...
  </details>

- **2026-07-28** — Cédric Bonhomme, Alexandre Dulaunoy — [Mapping CVEs to MITRE ATT&CK Techniques: A Curated Gold-Set Classifier and the Limits of LLM-Assisted Label Expansion](http://arxiv.org/abs/2607.25572v1)
  <details><summary>📄 Abstract</summary>
  We present a reproducible pipeline for mapping Common Vulnerabilities and Exposures (CVEs) to MITRE ATT&CK Enterprise techniques from free-text vulnerability descriptions. Rather than relying on the CWE->CAPEC->ATT&CK derivation chain, whose table-expansion artifacts we quantify, we train a multi-label classifier on a curated gold dataset of 1,207 CVEs from expert MITRE Center for Threat-Informed Defense mappings. The resulting model approximately doubles recall@5 compared with a zero-shot embed...
  </details>

- **2026-07-28** — Bowen Wang, Chi Zhang, Diyou Shen et al. — [At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference](http://arxiv.org/abs/2607.25504v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained weight pruning and activation sparsification have emerged as effective approaches for reducing the compute and memory cost of inference for Transformer models. In the moderate-sparsity regime, Gustavson's dataflow provides a natural execution model for exploiting both activation and weight sparsity on vector processors through metadata-driven indexed accumulation. However, existing RVV architectures lack native support for this pattern, forcing kernels to rely on software index deco...
  </details>

- **2026-07-28** — Clément Grisi, Jeroen van der Laak, Geert Litjens — [Beyond Counts: A Distributional Robustness Margin For Pathology Foundation Models](http://arxiv.org/abs/2607.25497v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models are approaching clinical deployment, yet remain vulnerable to systematic non-biological variation across centres. Differences in tissue preparation, staining and scanning are strongly encoded in their representations, enabling shortcut learning and weakening generalisation across cohorts and institutions. The Robustness Index (RI) quantifies whether local representation geometry is dominated by biology or by non-biological variation, but its count-based formulation di...
  </details>

- **2026-07-28** — Michael Macaulay, Harmony Bouabid, Guo Gen Ang et al. — [The Disruptive Impact of Large Language Models on Capture the Flag Competitions and the Path Toward Fair Play](http://arxiv.org/abs/2607.25425v1)
  <details><summary>📄 Abstract</summary>
  Capture the Flag (CTF) competitions are among cybersecurity's most effective training grounds, developing practical skill across cryptography, web exploitation, and binary exploitation. Large language models (LLMs) can now solve a growing share of challenges with minimal human input, raising urgent questions about fairness, the validity of rankings, and whether participation still delivers the learning that justifies the effort. This paper reports a mixed-methods study of LLM impact on modern CT...
  </details>

- **2026-07-28** — Chengxin Xie, Qiya Song, Yangbangyan Jiang et al. — [Dual-Domain Manifold Modeling for Hyperspectral Image Fusion](http://arxiv.org/abs/2607.25338v1)
  <details><summary>📄 Abstract</summary>
  Achieving a coherent integration of spectral richness and spatial fidelity remains a central objective in hyperspectral image fusion. However, existing hyperspectral image fusion methods struggle to effectively model geometric constraints. In the spatial domain, weak spatial-spectral interaction limits geometry-aware feature learning and suppresses high-frequency structural information, resulting in low-frequency bias and structural degradation. In the spectral domain, local manifold structures ...
  </details>

- **2026-07-28** — Chaemin Jang, Dongman Lee, Jihee Kim — [Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe](http://arxiv.org/abs/2607.25292v1)
  <details><summary>📄 Abstract</summary>
  Silicon sampling uses language models as proxies for human survey respondents, treating each model call as an independent draw from the persona's response distribution. We show this draw does not exist: instruction-tuned models do not sample from distributions, they collapse to a single output. The same persona on the same question returns the same answer on more than half of items in a public-opinion benchmark. The collapse is sharp: the model's internal probabilities concentrate on a single op...
  </details>

- **2026-07-28** — Zhenning Shi, Chen Xu, Junhao Zhang et al. — [ScaleResfusion: Residual Rectified Flow based on Residual Vector Field](http://arxiv.org/abs/2607.25275v1)
  <details><summary>📄 Abstract</summary>
  Real-world Image Restoration (Real-IR) aims to recover high-quality (HQ) images from complex and unknown degradations. Although recent diffusion-based methods have substantially improved perceptual quality, their current designs leave two key challenges unresolved. Methods that start from Gaussian noise are slow and often less faithful to the degraded input. Residual-based methods usually train from scratch, which makes it hard to exploit modern pre-trained generative priors. In this paper, we p...
  </details>

- **2026-07-28** — Mengqi Wang, Jianwei Wang, Qing Liu et al. — [Interpretable Column Annotation with LLM-Symbolized Decision Process Materialization](http://arxiv.org/abs/2607.25228v1)
  <details><summary>📄 Abstract</summary>
  Column annotation (CA), including column type annotation (CTA) and column property annotation (CPA), aims to identify the meanings of table columns and the semantic relationships among them. Recent CA methods usually use various neural models to learn column representations and directly map them to label categories, thereby (1) sacrificing model interpretability and adaptivity, and (2) overlooking rich label semantics and ultimately limiting accuracy. To address these limitations, we propose Sym...
  </details>

- **2026-07-28** — Narayanaswami Natraj Bharadwaj, Dhivya Chandramouleeswaran — [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](http://arxiv.org/abs/2607.25225v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used for code generation in critical infrastructure, yet the security effect of domain-specific prompting is understudied. We present SecDrift, a benchmark measuring sector-conditioned security drift: the change in static-analysis vulnerability rates when prompts are conditioned on industry contexts versus neutral baselines. We evaluate 7 LLMs (6 producing analyzable code) across 8 CISA critical infrastructure sectors and 9 CWE categories with 5 replicates (5,355 evaluation...
  </details>

- **2026-07-28** — Zheshun Wu, Renjie Zheng, Jinhang Zuo et al. — [A Unified Algorithmic Framework for Hybrid Reinforcement Learning in Tabular MDPs with Shifted Transition Dynamics](http://arxiv.org/abs/2607.25207v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates a hybrid reinforcement learning setting in tabular Markov Decision Processes (MDPs), where an agent aims to learn an optimal policy by combining online interactions with a target environment and offline data from a source environment. A central challenge is that offline data may be collected from outdated environments with shifted transition dynamics, making naive integration of historical data ineffective. To address this, we propose a unified algorithmic framework featu...
  </details>

- **2026-07-27** — Harrison J. Goldwyn, Graham Johnson, Christopher Ibarra et al. — [Beyond the Post Hoc User Study: Modeling Visual Decision-Making with Active Inference](http://arxiv.org/abs/2607.25131v1)
  <details><summary>📄 Abstract</summary>
  Empirical user studies are essential for evaluating visual encodings and can reveal perceptual and cognitive mechanisms, but they do not by themselves provide causal, predictive accounts of interpretation errors. Evaluations are therefore often post hoc: they measure performance after a design has been specified rather than predicting how attention, uncertainty, memory, and bias may produce accurate or erroneous judgments. To address this mechanistic gap, we translate a cognitive theory of visua...
  </details>

- **2026-07-27** — Zixuan Wu, Cristina Nita-Rotaru — [ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments](http://arxiv.org/abs/2607.24964v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed for security-sensitive tasks such as vulnerability detection and code review. Their reliance on natural-language context embedded in source code exposes a previously underexplored attack surface: adversarial comments that can influence a detector's reasoning without changing program behavior. We study LLM-based vulnerability detectors against a new adversary: a coding agent that implements new functionality, deliberately introduces vulnerabilities,...
  </details>

- **2026-07-27** — Andong Lu, Ziyi Zha, Jiandong Jin et al. — [Spatio-Temporal Conditional Denoising Transformer for Modality-Missing RGBT Tracking](http://arxiv.org/abs/2607.24701v1)
  <details><summary>📄 Abstract</summary>
  Missing modalities in RGBT tracking often lead to incomplete and unstable multimodal feature representations that greatly degrade the performance. Existing methods typically attempt to recover missing modalities from available ones, but the quality of data generated in challenging scenarios might be unsatisfactory. In addition, current approaches exhibit limited flexibility in processing both missing and complete data. To overcome these limitations, we propose a Spatio-temporal Conditional Denoi...
  </details>

- **2026-07-27** — Dael Sinay, Rica Gonen — [The Degree of Strategy-Proofness for Risk-Averse Committee Selection](http://arxiv.org/abs/2607.24676v1)
  <details><summary>📄 Abstract</summary>
  The classic notion of strategyproofness implicitly assumes that a manipulating agent either possesses complete knowledge of what all other agents are going to report, or is willing to take the risk and act as if they know these reports. To capture the profound uncertainty of real-world voters, recent work introduced \emph{risk-avoiding truthfulness (RAT)} and the \emph{RAT-degree}, which quantifies the exact number of known reports required for a manipulation to be strictly safe. While the RAT-d...
  </details>

- **2026-07-27** — Hang Ni, Weijia Zhang, Fan Liu et al. — [SIREN: Towards End-to-End Extreme-Weather Early Warning with Experience-Grounded LLM Agents](http://arxiv.org/abs/2607.24588v1)
  <details><summary>📄 Abstract</summary>
  Early warning of extreme weather is essential for mitigating the societal, economic, and environmental risks posed by hazardous weather events. However, expert-centered warning workflows are costly, labor-intensive, and difficult to scale throughout the warning-to-action process. Although recent advances in Large Language Model (LLM) agents have enabled the automation of weather-related tasks, existing studies remain centered on isolated scientific tasks and overlook the chain of interdependent ...
  </details>

- **2026-07-27** — Sofia Della Penna, Lorenzo Parracino, Luciano Pianese et al. — [VulnGym: Evaluating Vulnerability Management Strategies against Advanced Persistent Threats](http://arxiv.org/abs/2607.24552v1)
  <details><summary>📄 Abstract</summary>
  Enterprise networks are continuously targeted by Advanced Persistent Threats (APTs), attack campaigns exploiting software vulnerabilities to compromise critical assets over time. As disclosed vulnerabilities grow, resource-constrained organizations must prioritize which ones to patch. Existing prioritization standards score vulnerabilities individually and cannot capture how a patching policy performs against an adversary that progresses through the network over time. Previous tools have simulat...
  </details>

- **2026-07-27** — G{é}nesis Montenegro, Mokhtar Boumedyen Billami, Catherine Faron et al. — [LLM-Assisted Ontology Engineering and Construction of a French Legal Knowledge Graph](http://arxiv.org/abs/2607.24551v1)
  <details><summary>📄 Abstract</summary>
  Maintenance regulations are complex legal texts that are difficult to exploit when addressing a specific case and challenging to integrate into operational systems. This paper presents a two-stage LLM-assisted workflow for French maintenance regulations: ontology engineering from a SEMLEG-based core ontology, followed by construction of an ontology-grounded French legal knowledge graph. The first stage consists in the open extraction of typed entities and triples from a stratified corpus sample,...
  </details>

- **2026-07-27** — Christos Georgakilas, Aniello Panariello, Samir El Karrat Moreno et al. — [Rethinking Expert Training for Model Merging with Prompt Learning](http://arxiv.org/abs/2607.24465v1)
  <details><summary>📄 Abstract</summary>
  Model merging aims to combine multiple domain-specialized experts trained from a shared foundation model into a single multi-task model. Existing approaches largely focus on improving the merging procedure itself and typically assume experts obtained through full-parameter fine-tuning. In this work, we revisit expert training for model merging. We first show that prompt-based adaptation provides a strong baseline: independently learned prompts can be exploited across tasks while keeping the back...
  </details>

- **2026-07-27** — Qihui Zhu, Yuchen Wang, Zijian Wen et al. — [RP-OPSD: Resolution-Privileged On-Policy Self-Distillation for Multimodal Large Language Models](http://arxiv.org/abs/2607.24447v1)
  <details><summary>📄 Abstract</summary>
  On-Policy Self-Distillation (OPSD) uses privileged information available only to the teacher to provide dense token-level supervision on trajectories generated by the student. However, existing methods often rely on verified solution traces, explanations generated by external models, or manually localized visual evidence, which limits their scalable application to multimodal large language models. To address this issue, we exploit the information gap between high- and low-resolution views of the...
  </details>

- **2026-07-27** — Diego Bolón, Davy Paindaveine — [Möbius-Invariant Goodness-of-Fit Tests for the Spherical Cauchy Model](http://arxiv.org/abs/2607.24376v1)
  <details><summary>📄 Abstract</summary>
  We introduce a class of goodness-of-fit tests for the spherical Cauchy model on the unit hypersphere. The proposed procedures exploit the invariance of the spherical Cauchy family under Möbius transformations: after estimating the parameter by the sample Möbius mean, the observations are transformed to approximate spherical uniformity, and a projection-based uniformity statistic is applied to the resulting sample. We show that, under mild conditions, the resulting tests are exactly distribution-...
  </details>

- **2026-07-27** — Vaibhav Krishna, Hirokazu Shirado, Feng Fu et al. — [Modeling Duelling Contagions of True and False Information in the Face of Inherent Individual biases](http://arxiv.org/abs/2607.24360v1)
  <details><summary>📄 Abstract</summary>
  Advanced digital communication has revolutionized how people create and consume information, making information diffusion an important topic of research for domains from public health to national security. Real-world scenarios of information diffusion often involve competing narratives - true and false - spreading simultaneously. We propose a novel agent-based co-diffusion model, grounded in "complex-contagion" and "spiral of silence" theories, to capture how network dynamics exploit cognitive b...
  </details>

- **2026-07-27** — Tan T. Nguyen, Quan V. Dang — [DynaCalKV: Key-Value Cache Compression via Head Grouping and Adaptive Rank Allocation](http://arxiv.org/abs/2607.24331v1)
  <details><summary>📄 Abstract</summary>
  As the inference phase of Large Language Models (LLMs) requires handling long context windows, the Key-Value (KV) cache initially appears to address this challenge but eventually becomes a significant bottleneck as the context window continues to grow. Low-rank compression has recently been studied as an effective approach to reduce KV cache memory while maintaining model performance. However, only a few existing methods treat the Key and Value caches differently, despite their distinct roles. M...
  </details>

- **2026-07-27** — Angelo Nardone, Paolo Ferragina — [LLM-based Source Code Compression via Thresholded Symbol Ranking](http://arxiv.org/abs/2607.24192v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of lossless compression of source code, motivated by the storage demands of large-scale software archives, such as Software Heritage (https://www.softwareheritage.org/). General-purpose compressors (e.g., zstd, bzip2) offer a good trade-off between compression ratio and speed, but fail to exploit all special regularities inherent in source code. Recent approaches leverage Large Language Models (LLMs) within Shannon's symbol-ranking framework, relying on a scheme in which the...
  </details>

- **2026-07-27** — Yang Li, Hai Liu, Dian Shao et al. — [Agent-UCT: Upper Confidence Bounds Applied to Trees for Agentic Workflow Optimization with Cost-Awareness](http://arxiv.org/abs/2607.24162v1)
  <details><summary>📄 Abstract</summary>
  Optimizing agentic workflows, such as retrieval-augmented generation (RAG) pipelines, requires navigating a combinatorial space of discrete component choices under tight evaluation budgets. Existing approaches - heuristic search, black-box optimization, and standard tree search methods - do not explicitly exploit the compositional structure of these workflows, leading to redundant computation and inefficient budget allocation. We introduce Agent-UCT (Agent-based Cost-Aware Upper Confidence Bound...
  </details>

- **2026-07-27** — Pei Liu, Nan Zheng, Lang Zhang et al. — [LeapBot-WA: World-Anchor Action Models via Predictive Latent Alignments](http://arxiv.org/abs/2607.23969v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) have emerged as a powerful paradigm for embodied intelligence, yet the prevailing reliance on pixel-level video generation creates a fundamental bottleneck. Forcing models to reconstruct task-irrelevant visual details dissipates representational capacity and renders policies vulnerable to visual distractors. In this paper, we propose LeapBot-WA, which establishes a novel Predictive-Latent paradigm for WAMs by operationalizing the Joint-Embedding Predictive Architecture...
  </details>

- **2026-07-27** — Mohammed Aldeen, Muhammad Sami Irfan, Sagar Dasgupta et al. — [Development of Vision-Language Model-based GNSS Spoofing Detection for Autonomous Vehicle Navigation](http://arxiv.org/abs/2607.23962v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles (AVs) depend on Global Navigation Satellite Systems (GNSS) for localization and navigation, making them vulnerable to spoofing attacks that can covertly redirect vehicles or induce unsafe maneuvers. In this paper, we develop the first Vision-Language Model (VLM)-based framework for GNSS spoofing detection for autonomous vehicles by fusing front-camera visual data with in-vehicle sensor readings (e.g., speed, acceleration, yaw rate) against GNSS-derived maneuvers. Our approach...
  </details>

- **2026-07-27** — Jyun-Ze Tang, Po-Han Huang, Ming-Ching Chang et al. — [DuoAD: Leveraging [CLS] Dual Characteristics for Training-Free Few-Shot Anomaly Detection](http://arxiv.org/abs/2607.23924v1)
  <details><summary>📄 Abstract</summary>
  Vision foundation models have enabled strong training-free anomaly detection (AD). However, most existing approaches rely primarily on independent local patch features, leaving the global contextual information encoded by Vision Transformers (ViTs) underexploited. In this work, we identify the dual characteristics of the ViT [CLS] token: its embedding provides anomaly-invariant global semantic representation, while its attention maps implicitly highlight spatially abnormal regions. Building on t...
  </details>

- **2026-07-26** — Ge Zhang, Jingru Cheng, Huiyuan Chen — [Ranked by Position: Order Sensitivity as an Exploitable Attack Surface in LLM Listwise Recommenders](http://arxiv.org/abs/2607.24869v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) used as listwise rerankers in recommendation systems suffer from position bias when serializing candidate sets into prompts. We show this order sensitivity creates an exploitable attack surface: an attacker can promote a label-0 target into the top-$k$ solely by reordering candidates, without changing item content, labels, or model parameters. We introduce $\mathrm{promo}@k$ to quantify this vulnerability, measuring the fraction of label-0 targets that can be elevate...
  </details>

- **2026-07-26** — Zhaoyuan He, Muhammad Muaz, Lili Qiu — [OmniCache: Multidimensional Hierarchical Feature Caching For Diffusion Models](http://arxiv.org/abs/2607.23844v1)
  <details><summary>📄 Abstract</summary>
  High-resolution image and video diffusion models, including SD3, FLUX, and recent video diffusion transformers, have substantially improved generative quality but remain expensive at inference time because they repeatedly evaluate attention-heavy denoisers over many sampling steps. We address this inefficiency by exploiting redundancy in intermediate diffusion features rather than changing model weights or retraining. We identify four complementary redundancy sources in image and video generatio...
  </details>

- **2026-07-26** — Yifei Li, Zihui Gao, Laks V. S. Lakshmanan — [WISERouter: LLM Routing with Workload Budget Constraint](http://arxiv.org/abs/2607.23765v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve impressive performance across multiple domains, but using the most capable model for every query is prohibitive at scale. LLM routing exploits diversity in model capability and cost by assigning each query to a suitable model to balance utility and budget. Current methods have two limitations: (i) they either use heuristics that do not always enforce the budget constraint or impose a fixed per-query budget that cannot adapt across the workload and leads to su...
  </details>

- **2026-07-26** — Han Jiao, Chen Liu, Jiakai Sun et al. — [RoadVGGT: Road-Structure-Aware Feed-Forward Road Surface Reconstruction](http://arxiv.org/abs/2607.23758v1)
  <details><summary>📄 Abstract</summary>
  Large-scale road surface reconstruction supports high-definition mapping, autonomous-driving perception, annotation, and simulation. Existing road-specialized optimization methods can produce high-quality road representations, but they typically require per-scene training and scene-dependent coverage design around the driving trajectory, limiting scalable reconstruction over newly collected roads. To address these limitations, we introduce RoadVGGT, a road-structure-aware feed-forward framework ...
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

- **2026-07-14** — Aleh Manchuliantsau — [Win by Silence: Deletion Non-Monotonicity, Autonomous Exploitation, and Typed-State Gating in LLM Plan Evaluation](http://arxiv.org/abs/2607.12986v1)
  <details><summary>📄 Abstract</summary>
  Plan evaluators can reward a strategic plan for becoming less explicit. This paper studies that failure in a staged expected-value scorer for LLM-generated venture routes. Proposition 1 gives the score change from deleting an interior transition while retargeting its predecessor and retaining downstream value: Delta_k = (prod_{i<k} p_i)[c_k + (1 - p_k)R_{k+1}]. On a frozen 26-route cohort, all 57 admissible deletions matched the analytic identity and threshold sign, and every route had at least ...
  </details>

- **2026-07-14** — Duantengchuan Li, Yingqian Bi, Jinsong Chen et al. — [Disentangling Knowledge States with Ability and Proficiency Modeling for Knowledge Tracing](http://arxiv.org/abs/2607.13103v1)
  <details><summary>📄 Abstract</summary>
  Knowledge tracing (KT) aims to predict students' future performance by modeling their evolving knowledge states from historical interactions. Existing KT methods usually treat the raw interaction sequence as a unified behavioral process, overlooking the phase-specific nature of learning behaviors. Our preliminary observations show that students are more likely to correctly answer previously failed knowledge concepts after sufficient practice, suggesting a transition from ability-building to prof...
  </details>

- **2026-07-14** — Mohammadreza Rashidi — [Open-Source Intelligence for Code Provenance and the Security Patterns that Separate Human and Large-Language-Model Implementations of Common Programming Tasks](http://arxiv.org/abs/2607.12524v1)
  <details><summary>📄 Abstract</summary>
  Developers now draw code from two very different sources, the accumulated human answers on sites such as Stack Overflow and the output of large language models. We ask two questions about that split. First, can the provenance of a code snippet be recovered from the code itself, and second, do the two sources differ in the security patterns they adopt for the same task. Using only open sources, a public gateway of open-weight language models and the public Stack Overflow API, we build a fully rep...
  </details>

- **2026-07-14** — Yuhang Yan, Linchao Mou, Bokang Yang et al. — [TerraLogic: A Benchmark for Hierarchical Geospatial Reasoning in Earth Observation](http://arxiv.org/abs/2607.12497v1)
  <details><summary>📄 Abstract</summary>
  Beyond perception, reasoning is essential in remote sensing for advanced interpretation, inference, and decision-making. Recent advances in large language models (LLMs) have enabled tool-augmented agents that leverage external tools to perform complex analytical tasks. However, existing studies in remote sensing primarily focus on perception-oriented tasks, leaving cognitive geospatial reasoning largely underexplored. To address this gap, we introduce TerraLogic, a benchmark for geospatial reaso...
  </details>

- **2026-07-14** — Yubo Wang, Jiarong Liang, Yuxuan Zhang et al. — [Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models](http://arxiv.org/abs/2607.12463v1)
  <details><summary>📄 Abstract</summary>
  Coding agents must integrate external tool returns into ongoing reasoning - a capability that standard left-to-right pretraining on code exposes only in its forward direction. We observe that the action-observation-continuation loop of a coding agent is structurally isomorphic to a function call site, where a caller binds arguments, a callee returns a value computed elsewhere, and downstream code consumes that value. This conditioning structure exists at internet scale in ordinary code. We explo...
  </details>

- **2026-07-14** — Haitian Zhang, Thai Duy Nguyen, Xiangyuan Wang et al. — [UMSS: Towards Unsupervised Multi-modal Semantic Segmentation](http://arxiv.org/abs/2607.12372v1)
  <details><summary>📄 Abstract</summary>
  Multimodal semantic segmentation (MSS) is essential for robust perception in complex environments, yet its potential remains largely untapped because of the prohibitive cost of human annotations. While unsupervised semantic segmentation (USS) has achieved strong results on a single RGB modality, its naive extension to multimodal data is often hindered by fusion degradation. This occurs because, without explicit supervision, existing frameworks struggle to reconcile the heterogeneous structural p...
  </details>

- **2026-07-14** — Weifeng Yuan, Wenbo Guo, Feng Dong et al. — [Skills That Don't Exist: A Large-Scale Study of Hallucinated Skill Recommendation in LLM Agents](http://arxiv.org/abs/2607.12340v1)
  <details><summary>📄 Abstract</summary>
  LLM agents acquire new capabilities by downloading skills from open registries. Instead of browsing these catalogs manually, developers typically ask the agent to recommend and install a skill. This convenience hides a risk: agents frequently invent names for skills that exist in no registry. We term this flaw skill name hallucination. A fake name may seem harmless, but it opens the door to supply-chain attacks. Because registries rarely verify publishers, an adversary can prompt the agent, coll...
  </details>

- **2026-07-14** — Zhuohao Zhang, Junkun Liu, Rui Yang et al. — [Mystra: Declarative Dynamic Taint Analysis via Shadow Virtual Machine](http://arxiv.org/abs/2607.12308v2)
  <details><summary>📄 Abstract</summary>
  Dynamic taint analysis (DTA) for interpreted languages like JavaScript and Python requires three capabilities: observing host-runtime operations, maintaining parallel taint states, and defining how taint propagates. Existing systems couple these capabilities within an instrumentation mechanism -- source-rewriting or engine-native -- either incurring high runtime overhead or demanding engine-specific embeddings. There is yet to be a runtime-independent abstraction of a general DTA that separates ...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 69 papers

- **2026-07-28** — Adeela Bashir, Zia Ush Shamszaman, Zhao Song et al. — [Network Reciprocity Shapes Evolutionary Cybersecurity Dynamics](http://arxiv.org/abs/2607.25568v1)
  <details><summary>📄 Abstract</summary>
  AI-assisted cybersecurity systems are characterised by continuous adaptation between attackers and defenders, making evolutionary game theory a natural framework for studying their long-term behaviour. However, existing evolutionary cybersecurity models have primarily focused on homogeneous interactions, providing limited understanding of how population structure influences cyber attack-defence dynamics. In this paper, we develop a mixed-role evolutionary game in which adaptive cyber agents can ...
  </details>

- **2026-07-28** — Parmida Geranmayeh, Onur Günlü — [Bayesian-Guided Cooperative RL Beamforming for Wireless Adversarial User Detection](http://arxiv.org/abs/2607.25417v1)
  <details><summary>📄 Abstract</summary>
  In next-generation wireless networks, communication systems are expected to go beyond simple data transmission and simultaneously provide high data rates, efficiency, and security. This requirement has motivated the extensive adoption of machine learning methods to develop intelligent and real-time network management frameworks, enabling the system to continuously monitor and react to channel variations and user behavior while maintaining efficient information delivery. In this context, the inte...
  </details>

- **2026-07-28** — Farooq Shaikh — [Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?](http://arxiv.org/abs/2607.25995v1)
  <details><summary>📄 Abstract</summary>
  Kubernetes is central to the cloud-native ecosystem, orchestrating containerised workloads. Recent work suggests that large language models (LLMs) can automate cluster security remediation, generating configuration patches from Kubernetes Security Posture Management (KSPM) findings without human authoring. Such systems, however, prompt the model with each finding in isolation from the live service call graph, assuming general hardening knowledge suffices. This assumption breaks down whenever a p...
  </details>

- **2026-07-28** — Ravi Kant Sharma, Ashutosh Uttam, Ajay Kumar — [Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous Networks](http://arxiv.org/abs/2607.25914v1)
  <details><summary>📄 Abstract</summary>
  Autonomous Network Levels 4-5 require AI agents to invoke tools across vendor boundaries without human oversight, yet existing management standards lack a standardized mechanism for cross-vendor trust visibility. When a tool from Vendor B is compromised, agents from Vendor A continue invoking it -- unaware of the trust degradation -- causing cascading service impact. We present AgentToolMO, a proposed 3GPP NRM information model for agent tool trust management. The model comprises: a formally def...
  </details>

- **2026-07-28** — William Robert Gore — [Distributing Security Controls Through Harness Engineering](http://arxiv.org/abs/2607.25890v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents are being adopted at historic speed, yet security and risk concerns remain the primary barrier to scaling agentic AI across organizations. Existing security controls for coding agents are not systematically distributed to engineering teams, and vendor-native solutions introduce ecosystem dependencies that may not suit every deployment context. This paper investigates whether off-the-shelf security controls can be implemented on commercial AI coding agents and scaled to a distrib...
  </details>

- **2026-07-28** — Fanqing Meng, Lingxiao Du, Qiguang Chen et al. — [RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement](http://arxiv.org/abs/2607.25886v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement requires turning evidence of model failures into better models. Data-centric post-training research entails diagnosing capability gaps, designing and validating training-data strategies, and learning from checkpoint feedback. Can LLM agents automate this loop? Existing benchmarks entangle research decisions with optimization, serving, evaluation, and systems implementation, obscuring agents' research capability. We introduce RSIBench-Data, a controlled benchmark of LLM...
  </details>

- **2026-07-28** — Jui-Feng Chi, Wei-Ta Chu, Sheng-Long Lin — [Food Image Segmentation with LLM-Derived Ingredient Labels and Multimodal Fusion](http://arxiv.org/abs/2607.25820v1)
  <details><summary>📄 Abstract</summary>
  Food image segmentation plays a vital role in health-related applications such as nutrition tracking and personalized health monitoring. However, existing models often underperform on visually similar ingredients and rare food categories. To address this issue, we propose two plug-and-play multimodal modules that enhance the segmentation performance by leveraging ingredient labels inferred from food images using large language models (LLMs). The first module, called LIM-F (Language Injection Mod...
  </details>

- **2026-07-28** — Luqi Gong, Rui Xu, Yue Chen et al. — [Freq-RemoteVAR: Next-Frequency Autoregressive Modeling for Remote Sensing Change Detection](http://arxiv.org/abs/2607.25815v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing change detection aims to identify land-cover changes from bi-temporal images. Most existing methods follow a one-shot dense prediction paradigm, directly regressing a change mask from fused features. However, such approaches overlook the intrinsic frequency characteristics of change patterns. We propose Freq-RemoteVAR, a frequency autoregressive framework that reformulates change detection as a structured generation problem in the frequency domain. Instead of predicting the change...
  </details>

- **2026-07-28** — Ziqian Liu, Minghao Li, Yiming Qiu — [The Model in the Middle: Toward AI-Native Real-Time Communication](http://arxiv.org/abs/2607.25792v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex omni models are transforming human--AI interaction from turn-based exchanges into continuous multimodal conversations in which speaking, listening, and reasoning unfold concurrently. Rather than viewing the model as a replacement for a human endpoint, we argue for a new perspective: the model is a stateful computational middlebox inside a human-centered feedback loop, with network transport, model serving, and user playback jointly shaping how the interaction evolves. This perspectiv...
  </details>

- **2026-07-28** — Tresor Y. Koffi, Youssef Mourchid, Yohan Dupuis — [FLASH: Efficient Impact Fall Detection with Unified Hypergraph State-Space Model](http://arxiv.org/abs/2607.25791v1)
  <details><summary>📄 Abstract</summary>
  Falls represent a critical public health challenge, and accurate detection of the impact moment when an individual hits the ground is crucial for timely intervention. Existing skeleton-based methods rely on graph neural networks modeling only pairwise joint connections, failing to capture multi-joint coordination characteristic of fall impacts, while transformer-based temporal models suffer from quadratic complexity limiting real-time deployment. We propose FLASH, a novel framework integrating s...
  </details>

- **2026-07-28** — Xinyi Hong, Pinjun Dong, Xinyang Yu et al. — [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction](http://arxiv.org/abs/2607.25718v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly rely on invoking external tools to complete real-world tasks. Tool retrieval, which selects a small task-relevant subset from a library of thousands of tools before the agent acts, has therefore become a critical component of LLM agent pipelines. However, existing retrievers either score each tool in isolation or assemble the tool set sequentially, so the joint utility of a candidate set is never evaluated as a whole. In this paper, we propose HYSET...
  </details>

- **2026-07-28** — Zhenzhen Ren, Jiyan He, Xinpeng Zhang et al. — [OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation](http://arxiv.org/abs/2607.25656v1)
  <details><summary>📄 Abstract</summary>
  Complex tasks often decompose into parallelizable yet interdependent subtasks, making orchestration critical to the performance of multi-agent systems (MAS). Existing evaluations typically rely on end-to-end execution, which conflates orchestration-plan quality with worker capabilities, tool reliability, and environmental noise. Moreover, the time and token costs of real execution grow rapidly with workflow scale, making systematic evaluation expensive. We present OrchBench, a simulation-based b...
  </details>

- **2026-07-28** — Shiyu Lei, Ke-Xin Ren, Daiyi Jiang et al. — ["Dragon Slayer Becomes the Dragon": How Players Perceive and Respond to Inequality in the Game World of Whiteout Survival](http://arxiv.org/abs/2607.25574v1)
  <details><summary>📄 Abstract</summary>
  Inequality in real-world societies are associated with psychological distress and behavioral consequences. However, less is known about whether similar dynamics emerge when inequality exists within virtual environments or make-belief worlds. As online games increasingly constitute meaningful social spaces, it becomes critical to examine how players perceive and react to structural and resource differences online to optimize their experiences. This study studies perceptions of inequality in the o...
  </details>

- **2026-07-28** — Swarnadip Chatterjee, Ssharvien Kumar Sivakumar, Anirban Mukhopadhyay — [Group Equivariant Diffusion for Anomaly Detection in Computational Cytology](http://arxiv.org/abs/2607.25503v1)
  <details><summary>📄 Abstract</summary>
  Computational cytology on whole-slide images is challenging because malignant cells are rare, heterogeneous, and annotated slides are scarce. Anomaly detection frameworks can be trained on normal slide-negative patches and then applied at test time to flag abnormal patches in held-out slides. Most unsupervised anomaly detection approaches including generative ones (GAN-based and diffusion-based), are tuned to organ-level imaging and require large curated datasets. In cytology the signal is cell-...
  </details>

- **2026-07-28** — Korosh Vatanparvar, Ashutosh Joshi, Maria Xenochristou et al. — [PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents](http://arxiv.org/abs/2607.25485v1)
  <details><summary>📄 Abstract</summary>
  Health AI is evolving from answering questions to agentic systems that converse with patients, reason about health records, and act on their behalf. Primary care guards against diagnostic errors and unsafe care; agents assisting in this domain warrant evaluation against the same risks. Current benchmarks focus on medical knowledge, assessed through isolated question-answering or clinician-facing tasks. PatientAgentBench benchmarks patient-facing agentic healthcare; it evaluates a foundation mode...
  </details>

- **2026-07-28** — Jirong Zhuang — [How Likely and How Deep? Sharp Joint Bounds on Risk-Neutral Crash Probability and Conditional Depth from Option Bid-Ask Quotes](http://arxiv.org/abs/2607.25353v1)
  <details><summary>📄 Abstract</summary>
  A finite panel of option quotes with bid-ask spreads generally does not point-identify either the risk-neutral probability of breaching a specified threshold or the expected shortfall below that threshold conditional on a breach. Sharp marginal bounds characterize each quantity in isolation but not their jointly attainable combinations: values within the two marginal intervals may require different risk-neutral distributions, so pairing them can produce a tail scenario inconsistent with the opti...
  </details>

- **2026-07-28** — Lennart Trumpler, Rodrigo Furlan de Assis, Elias Ribeiro da Silva et al. — [Agentic AI Autonomy Assessment: A Decision-Support Framework Towards Governed Supply Chain Systems](http://arxiv.org/abs/2607.25405v1)
  <details><summary>📄 Abstract</summary>
  Supply chain decision-making is rapidly transforming with the rise of agentic AI - highly autonomous systems that can operate on complex, long-horizon tasks. Yet the adoption of agentic systems outpaces their governance: existing taxonomies of autonomy only offer discrete classifications, rely on subjective judgement, and cannot track autonomy across a system's life cycle, leaving enterprises unable to assess the risks of increasingly autonomous supply chain agents. This paper proposes the Agent...
  </details>

- **2026-07-28** — Can Wang, Yuhao Wang, Yushe Cao et al. — [LaP-Forensics: Latent-Pixel Consistency Guided Multimodal Reasoning for Deepfake Detection](http://arxiv.org/abs/2607.25962v1)
  <details><summary>📄 Abstract</summary>
  Recent generative models can produce images with few obvious visual artifacts, weakening detectors and explanations that rely only on surface appearance. We present LaP-Forensics, a multimodal framework that augments RGB semantics with reconstruction-based forensic evidence. A frozen Stable Diffusion DDIM inversion-reconstruction model provides a fixed reconstruction reference, and its residual map measures local compatibility with that reference. Independent projectors encode the RGB image and ...
  </details>

- **2026-07-28** — Fanfu Wei, Thibault Ehrhart, Raphaël Troncy — [Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs](http://arxiv.org/abs/2607.25959v1)
  <details><summary>📄 Abstract</summary>
  Wikipedia and Wikidata are widely used for information access, LLM pre-training, and retrieval-augmented generation. Their knowledge is deeply connected but scattered across text, tables, and knowledge graphs. This raises a practical question: when these modalities disagree, how can we detect and explain the conflict? We study this problem as \emph{modality-level inconsistency detection}. We first introduce a taxonomy of cross-modal knowledge inconsistencies, covering information granularity dif...
  </details>

- **2026-07-28** — Carlos Celemin, Benedict Wilkins, Adrián Barahona-Ríos et al. — [Evaluating VLMs for Autonomous Agent-Driven Geometry Clipping Detection in Video Game QA](http://arxiv.org/abs/2607.25921v1)
  <details><summary>📄 Abstract</summary>
  In this work, we study the use of Vision-Language Models (VLMs) for anomaly detection in an agent-driven game Quality Assurance (QA) pipeline focusing on geometry clipping. In this evaluation, a custom exploration agent navigates a game level to collect visual observations, while the automatic annotation pipeline provides frame-level clipping labels. This setup allows us to evaluate recent VLMs on a controlled anomaly detection task without manual annotation. We benchmark six recent VLMs (Gemini...
  </details>

- **2026-07-28** — Huynh Duc An Son Nguyen, Lukas Arzoumanidis, Youness Dehbi — [AuthentiCity: A Multi-Source Provenance-Aware Knowledge Graph and Benchmark for 3D City Models](http://arxiv.org/abs/2607.25243v1)
  <details><summary>📄 Abstract</summary>
  Urban digital twins increasingly combine authoritative, crowd-sourced, machine-learned, and reconstructed data with differing reliability, coverage, and semantics. Yet few urban datasets provide a unified representation supporting multi-source integration, provenance tracking, spatial reasoning, and machine learning. We present AuthentiCity, a multi-source, provenance-aware 3D city knowledge graph spanning five cities across three continents (Hamburg, Helsinki, Zurich, New York, and Tokyo) and c...
  </details>

- **2026-07-27** — Hyundoo Park, Byungho Choi — [When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops](http://arxiv.org/abs/2607.25152v1)
  <details><summary>📄 Abstract</summary>
  Long-running autonomous agents plan, act, and judge their own completion without human intervention. When an agent grades its own work, self-evaluation bias takes hold: plausible changes are accepted as progress while real-world outcomes stagnate or regress. We name this failure mode the progress mirage and show, with controlled measurement, that it is a question of what the evaluator is grounded in. We built a testbed that holds the agent and its tool surface fixed and manipulates only the info...
  </details>

- **2026-07-27** — Dushyant Sharma — [Gubernaut: A Deterministic Homeostatic Controller for Affect-Regulated LLM Agents, Validated Across Independent Model Families](http://arxiv.org/abs/2607.24339v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents inherit reactive failure modes: escalation under provocation, sycophantic drift under flattery, perseveration when stuck. These are failures of propensity, not capability; they concern what a model does under sustained pressure, which training-time alignment reduces but does not eliminate at runtime. This research led to the Gubernaut Cognitive Controller (GCC), a model-agnostic runtime control layer in a Nelson--Narens monitoring--control loop: an object level ...
  </details>

- **2026-07-27** — Kimi Team, Tongtong Bai, Yifan Bai et al. — [Kimi K3: Open Frontier Intelligence](http://arxiv.org/abs/2607.24653v1)
  <details><summary>📄 Abstract</summary>
  We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in o...
  </details>

- **2026-07-27** — Zhibin Kang, Hanmo You, Dong Wang et al. — [Evaluating Fuzz Testing for Reinforcement Learning Agents](http://arxiv.org/abs/2607.24577v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) agents are increasingly deployed in safety-critical domains such as robotics, autonomous driving, and drone control, where unexpected behaviors may lead to severe real-world consequences. Fuzz testing has recently emerged as a promising method for exploring the vast state spaces of RL agents and exposing crashes. Although numerous RL fuzzing methods have been proposed, existing studies often differ in evaluation settings, baselines, and metrics, making it difficult to...
  </details>

- **2026-07-27** — Th{é}otime de la Selle — [From transcription to semantic corpus analysis: unsupervised learning of sentence representations for ancient languages](http://arxiv.org/abs/2607.24542v1)
  <details><summary>📄 Abstract</summary>
  Automatic Text Recognition (ATR) now supplies digital humanities with large volumes of unstructured, heterogeneous, and often noisy text in ancient languages. Downstream semantic analysestext reuse identification, alignment, and semantic search-rely on sentence embeddings, yet existing methods transfer poorly to ancient languages: generic multilingual encoders underperform, specialized language models yield anisotropic representation spaces, and labeled similarity data is unavailable. We study t...
  </details>

- **2026-07-27** — Trung V. Phan, Tri Gia Nguyen, Thomas Bauschert — [DeepFaith: Evidence-Grounded LLMs for Faithful Incident Reporting in Multi-Stage APT Defense](http://arxiv.org/abs/2607.24348v1)
  <details><summary>📄 Abstract</summary>
  Advanced Persistent Threats (APTs) are difficult to detect and interpret due to their multi-stage and stealthy nature. While recent autonomous defense systems leverage provenance graphs and learning-based models for detection and mitigation, their outputs remain largely machine-oriented and difficult for analysts to interpret. Large language models (LLMs) offer a promising interface for report generation, but often produce hallucinated or weakly grounded content. In this paper, we propose DeepFa...
  </details>

- **2026-07-27** — Paul Kilian, Markus Kleffmann — [LLM-Based vs. Lexicon-Based Sentiment Signals for Tail-Risk Detection in Meme Stocks](http://arxiv.org/abs/2607.24072v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an empirical comparison of lexicon-based and Large Language Model (LLM)-based sentiment analysis for extracting market-relevant signals from social media discourse in highly volatile equity markets. Using Reddit data from r/WallStreetBets and focusing on meme stocks (GME, AMC, NOK), we construct time-aligned sentiment indicators and evaluate their relationship with market returns, with particular attention to extreme positive return events in the upper tail of the return dist...
  </details>

- **2026-07-27** — Keyu Li, Jin Gao, Dequan Wang — [The Cost of Knowing: A Resource-Aware Protocol for Benchmarking Hallucination Beyond Static Leaderboards](http://arxiv.org/abs/2607.24063v1)
  <details><summary>📄 Abstract</summary>
  On standard factuality tasks, frontier models now cluster near the top of the scale. The question is therefore shifting from how factual a system is toward how much compute that factuality costs. Static leaderboards score factuality in isolation and treat compute as free, so they cannot tell a genuinely better system apart from one that simply spends more. Consider a ranking reversal. A brute-force Best-of-4 agent posts the higher raw factuality score (H-Score 0.9169 vs 0.9103) and would top a s...
  </details>

- **2026-07-27** — Pengkun Jiao, Bin Zhu, Jingjing Chen et al. — [Disentangling Semantic Attention from Structural Bias in the Attention Manifold](http://arxiv.org/abs/2607.24017v1)
  <details><summary>📄 Abstract</summary>
  The empirical success of attention mechanism in Multimodal Large Language Models (MLLMs) often obscures its inherent, subtle flaws. Specifically, MLLMs consistently exhibit disproportionate attention toward certain semantically uninformative visual tokens, a phenomenon termed "register" or "Visual Attention Sinks." While existing inference intervention methods attempt to identify these sink tokens and redistribute their attention weights, such approaches typically treat these tokens in isolation...
  </details>

- **2026-07-27** — Haozhen You, Zhen Dong, Jingjing Wang et al. — [Industrial Practice of LLM-Based Test Case Carving and Assertion Generation (Experience Paper)](http://arxiv.org/abs/2607.24000v1)
  <details><summary>📄 Abstract</summary>
  Enterprise regression testing for microservice systems is often constrained by incomplete or outdated documentation. In practice, QA engineers frequently rely on real execution traffic to reconstruct business scenarios; however, turning raw traffic into replayable regression tests with stable validation logic remains labor-intensive and error-prone.   This paper presents NL2Test, an end-to-end approach and tool that generates executable API regression tests from (i) a natural-language scenario d...
  </details>

- **2026-07-27** — Guoyi Zhang, Yanjin Du, Zhengyao Zhao et al. — [Effective Receptive Field Ordering Matters for Infrared Small Target Detection](http://arxiv.org/abs/2607.23994v2)
  <details><summary>📄 Abstract</summary>
  In this work, we investigate a previously unexplored architectural dimension for infrared small target detection: the organization of effective receptive fields (ERFs) during feature refinement. Unlike existing approaches that primarily improve individual feature operators, we argue that ERF organization constitutes an architectural dimension independent of receptive field design itself, and formulate deep feature transformation as a progressive residual correction process, from which a theoreti...
  </details>

- **2026-07-27** — Dane Malenfant — [Moral Hazard in Multi-Agent Language Models](http://arxiv.org/abs/2607.23982v2)
  <details><summary>📄 Abstract</summary>
  Cooperation can fail when socially valuable effort is costly, weakly observable, and mainly benefits others. Drawing on Holmström's team moral-hazard model, we introduce the Dialogue Moral Hazard Game, a controlled textual game that operationalizes this hidden-action structure for language agents. In each episode, an agent can preserve an immediate local reward or pay a query cost to reveal a hidden safety fact that primarily helps another agent's downstream decision. We evaluate seven open-weig...
  </details>

- **2026-07-27** — Yihui Zhang, Tianyu Wo, Jinghao Wang et al. — [SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving](http://arxiv.org/abs/2607.23933v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents increasingly rely on the Model Context Protocol (MCP) to invoke isolated external sandboxes, disaggregated sandbox deployment introduces a fundamental tension between resource utilization and interactive tail latency. Persistent long-lived sandbox reservations incur excessive memory overhead at scale, while lazy on-demand instantiation generates severe cold-start penalties that degrade response performance under multi-tenant, multi-turn agent workloads. To resolve this dilemma, we ...
  </details>

- **2026-07-27** — Jun Ling, Tao Huang, Junzhuo Liu et al. — [GOTS: Greedy Orthogonal Token Selection for High-Resolution Vision-Language Models](http://arxiv.org/abs/2607.23913v1)
  <details><summary>📄 Abstract</summary>
  Modern vision-language models (VLMs) increasingly rely on dynamic or high-resolution visual encoding, producing thousands of visual tokens that substantially increase downstream language-model inference cost. Existing token-reduction methods assess token utility through token-wise importance, query relevance, coverage, pairwise diversity, or subset-level objectives. Our key insight is to view visual token reduction through selected-span complementarity: instead of scoring a token in isolation or...
  </details>

- **2026-07-27** — Keshav Rastogi, Eugy Han, Jeremy N. Bailenson — [FIDAC: An Easy-to-use Pipeline to Extract and Interpret Interpersonal Distance From Video](http://arxiv.org/abs/2607.25146v1)
  <details><summary>📄 Abstract</summary>
  The distance between persons reveals significant information about their perception of each other. However, such information is not easily extractable and interpretable from video input. We developed an open-sourced library, Facial Interpersonal Distance Analysis and Coding (FIDAC) that transforms facial detection results into actionable data about location and interpersonal distance. This tool merges data from multiple open-source facial detection models, strategically compensating for gaps in ...
  </details>

- **2026-07-27** — Anika Knupfer, Maximilian Lindholz, Johanna Paula Müller et al. — [Panda: Unsupervised Pelvic Anomaly Detection for Real-Time MR Imaging](http://arxiv.org/abs/2607.24703v1)
  <details><summary>📄 Abstract</summary>
  Female pelvic diseases remain an under researched area characterized by often delayed diagnosis. While pelvic MRI offers superior soft-tissue contrast for diagnosis and image-guided procedures, real-time anomaly detection remains challenging due to physiological motion, tissue deformation, and instrument artifacts. Existing supervised approaches are impractical, as adverse events are rare, heterogeneous, and difficult to annotate. We present a Dinomaly-based unsupervised anomaly detection framew...
  </details>

- **2026-07-27** — Marzieh Zare — [Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted Negative Controls](http://arxiv.org/abs/2607.24519v1)
  <details><summary>📄 Abstract</summary>
  Pretrained EEG foundation models are increasingly proposed for clinical decoding, but their transfer across populations and robustness to negative controls remain unclear. We benchmark six models (LaBraM, EEGMamba, CBraMod, REVE, BENDR, and BIOT) on five clinical tasks across four datasets using frozen linear probes with leave-one-subject-out, subject-grouped, or explicitly identified recording-level splits. Selected REVE findings are tested against random initialisation, random features, label ...
  </details>

- **2026-07-27** — Keti Korini, Christian Bizer — [SINT-Flow: Schema Integration using Large Language Model Workflows](http://arxiv.org/abs/2607.24492v1)
  <details><summary>📄 Abstract</summary>
  The goal of schema integration is, given a set of input schemata or tables, to derive a global, unified schema that is able to represent the concepts, attributes, and relationships of all input tables in a coherent fashion. This paper presents SINT-Flow, a schema integration framework composed of five LLM-based operators that can be combined into workflows to perform fully automated, end-to-end schema integration. In contrast to existing approaches, SINT-Flow can process denormalized source tabl...
  </details>

- **2026-07-27** — Heyan Chai, Xin Li, Wenjie Wang et al. — [StanceFlip: A Comprehensive Multi-Dimensional Benchmark for Multimodal Conversational Stance Flipping Forecasting](http://arxiv.org/abs/2607.24191v1)
  <details><summary>📄 Abstract</summary>
  Conversational stance detection has shifted from static text analysis to dynamic multimodal modeling. However, existing benchmarks exhibit three key limitations: failure to capture the dynamic evolution of beliefs, particularly during stance reversals; difficulty in disentangling affective states from logical reasoning; and neglect of the critical role of multimodal cues in resolving pragmatic ambiguities such as sarcasm. To address these limitations, we propose StanceFlip, a benchmark designed ...
  </details>

- **2026-07-27** — Tieniu Wang, Cangzhu Huang, Qianhui Li — [Myopia Prevention and Control 3.0: Artificial Intelligence--Driven Risk Stratification, Proactive Monitoring, and Personalized Intervention](http://arxiv.org/abs/2607.24187v1)
  <details><summary>📄 Abstract</summary>
  The convergence of artificial intelligence (AI), digital sensing, and ubiquitous computing has created an unprecedented opportunity to transform myopia prevention from a reactive, population-based model into a proactive, precision-driven one. Despite evidence that half the world's population will be myopic by 2050, conventional approaches---school-based vision screening (Phase 1.0) and evidence-based risk factor management (Phase 2.0)---have proven insufficient. We review the emergence of Myopia...
  </details>

- **2026-07-27** — Jingkun Luo, Da-Tian Peng — [Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation](http://arxiv.org/abs/2607.24054v1)
  <details><summary>📄 Abstract</summary>
  A correct answer can conceal why an agent succeeded. Once agents change their information state during evaluation, correctness no longer distinguishes intended reasoning from answer acquisition. Outcome evidence and exposure detection do not establish whether success depended on an acquired target; we call this missing evaluation object success provenance. AcquaBench audits it through matched CLEAN, GOLD, and SHAM value substitution on four standardized surfaces with joint qid-clustered analysis...
  </details>

- **2026-07-27** — Saurabh Ranjan, Konstantina Sokratous, Brian Odegaard — [Reality Monitoring in Large Language Models: Self-Knowledge That Transforms with Conversation Memory](http://arxiv.org/abs/2607.23927v1)
  <details><summary>📄 Abstract</summary>
  A conversational AI that cannot tell its own output from what a user said will treat its own mistakes as user-provided facts. In humans, this capacity is called reality monitoring, and its failures are linked to hallucinations, delusions, and confabulation, yet whether LLMs possess it remains untested. Here we show, across two experiments and six LLMs, that source attribution depends on how conversational memory is structured: ceiling accuracy for self-generated content under minimal memory dema...
  </details>

- **2026-07-26** — Satyam Kumar, Saurabh Jha — [The Missing Layer: Specification Infrastructure for AI Oversight](http://arxiv.org/abs/2607.24866v1)
  <details><summary>📄 Abstract</summary>
  AI safety has a missing layer. Interpretability, formal methods, security engineering, evaluation methodology, and reinforcement-learning safety each produce substantial work, but the resulting artifacts do not compose into deployable oversight: every team fielding an agentic system builds its own audit schema, policy dialect, monitoring stack, and escalation path, mostly reinventions of patterns understood elsewhere. We diagnose this as a coordination gap, not a research gap, and propose a two-...
  </details>

- **2026-07-26** — Zhonghua Chu, Hongliang Luo, Boxuan Sun et al. — [ISAC and Vision Fusion for Fine-Grained Low-Altitude Target Recognition](http://arxiv.org/abs/2607.23789v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose an integrated sensing and communications (ISAC) and vision fusion framework for fine-grained low-altitude target recognition. Specifically, we first utilize ISAC system to estimate the position of the low-altitude target. Then we adjust the working parameters of the Pan-TiltZoom (PTZ) camera based on the estimated target position, such that the camera can capture the image of tiny low-altitude target from several hundred meters away. After obtaining the wireless echo si...
  </details>

- **2026-07-26** — Ionut Predoaia, Tuong Manh Vu, Konstantinos Barmpis et al. — [A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems](http://arxiv.org/abs/2607.23884v1)
  <details><summary>📄 Abstract</summary>
  Recent industry practice has seen the rapid emergence of agentic systems composed of heterogeneous, tool- and LLM-mediated agent components, raising practical questions about inter-agent coordination and protocol design. This paper presents an implementation-grounded comparison of the Model Context Protocol (MCP) and the Agent2Agent (A2A) protocol, from a multi-agent systems engineering perspective, using an inter-agent coordination scenario involving LLM-based agents. We evaluate an MCP-based a...
  </details>

- **2026-07-26** — Mihai Suteu, Ovidiu Serban — [Controllable Diversity in Normalization-Based Implicit Ensembles via Softmax-Temperature Modulation](http://arxiv.org/abs/2607.23860v1)
  <details><summary>📄 Abstract</summary>
  Deep ensembles provide the most reliable uncertainty estimates in deep learning, but their cost grows linearly with the number of members. Implicit ensembles lower this cost by sharing a single backbone across members. Member diversity is a primary determinant of ensemble quality, yet no implicit ensemble can shape it during training; existing methods fix it at initialisation or build it into the architecture. We introduce $σ$N-Ens, a normalisation-based implicit ensemble that treats each member...
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

- **2026-07-14** — Xi Cheng, Ke Liu, Siyuan Feng et al. — [Cost-Optimal Foundation Model Deployment Portfolio for Transportation Management](http://arxiv.org/abs/2607.13239v1)
  <details><summary>📄 Abstract</summary>
  Foundation models, including large language models (LLMs) and vision-language models (VLMs), are increasingly used for transportation management center (TMC) tasks such as anomaly detection, incident reporting, and traveler information. Deploying multiple such models across TMC functions raises a portfolio question: which model should serve each function, in which deployment mode, and under what shared hardware budget? We formulate this as the Foundation Model Deployment Portfolio (FMDP) problem...
  </details>

- **2026-07-14** — Xiaoyu Li, Zheng Gao, Xiaoyan Feng et al. — [Watermark Forensics for Generative Models: An Information-Theoretic Perspective](http://arxiv.org/abs/2607.13003v1)
  <details><summary>📄 Abstract</summary>
  A watermark in a generative model's output is usually asked only whether a text is machine-made. The same mark can do more: attribute it to the user who produced it, extract a hidden payload, or localize the part that survives editing. These form a forensic ladder, and we ask what each rung costs in the sample length $n$.   One object organizes the answers. Let $S$ be the secret the mark carries (a user's identity or payload), and let the information profile $ν(t)=I(S;X_t\mid X_{<t})$ record how...
  </details>

- **2026-07-14** — T. O. Hodd, L. C. Gallo, A. G. Gonzalez et al. — [Investigating the Periodic X-ray Behaviour in the Eclipsing AGN NGC 6814](http://arxiv.org/abs/2607.12904v1)
  <details><summary>📄 Abstract</summary>
  A 2016 XMM-Newton X-ray light curve of the Seyfert 1.5 galaxy NGC 6814 exhibited clear eclipsing behaviour, with distinct ingress and egress, during half of the observation. Here, we report on the periodic behaviour in the light curve prior to the eclipse. We use timing and spectral analysis techniques to quantify the behaviour and examine the characteristics of the periodic signal. A superlet transform of the X-ray light curve reveals a period of ~45-50 $μ$Hz in the initial 60 ks of the observa...
  </details>

- **2026-07-14** — Cameron Cagan, Pedram Fard, Jiazi Tian et al. — [A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study](http://arxiv.org/abs/2607.12886v1)
  <details><summary>📄 Abstract</summary>
  Clinical notes contain many of the signs and symptoms that bring patients to care, yet this information rarely reaches structured fields. Existing extraction approaches either rely on context-insensitive rules that generate false positives or on supervised models that require substantial fine-tuning. We present Pythia, a multi-agent system that autonomously writes and optimizes extraction prompts for clinical concepts without manual prompt engineering or fine-tuning. Running on a locally hosted ...
  </details>

- **2026-07-14** — Roi Cohen, Yvan Carré, Nick Lechtenbörger et al. — [Knowledgeless Language Models: Suppressing Parametric Recall for Evidence-Grounded Language Modeling](http://arxiv.org/abs/2607.12831v1)
  <details><summary>📄 Abstract</summary>
  Language models encode substantial factual knowledge in their parameters, which can lead to unreliable behavior when this knowledge is outdated, incomplete, or misaligned with the provided context. In this work, we study whether modifying the pretraining signal can systematically shift models away from parametric recall and toward evidence-grounded reasoning. We introduce Knowledge--''Less'' Language Models (KLLMs), a fundamentally different epistemic training paradigm for LLMs, which are pretra...
  </details>

- **2026-07-14** — Hongbo Wang, Huaibo Huang, Jie Cao et al. — [Hallo4D: Multi-Modal Hallucination Mitigation for Consistent Spatio-Temporal Generation](http://arxiv.org/abs/2607.12752v2)
  <details><summary>📄 Abstract</summary>
  While recent advances in 3D generation have enabled impressive visual synthesis, existing methods often rely on 2D diffusion supervision without explicit mechanisms for geometric consistency, leading to spatial hallucinations such as duplicated structures and misaligned geometry. These issues become more severe in 4D generation, where maintaining consistency across viewpoints and temporal evolution introduces additional challenges, including jitter, identity flicker, and structural drift. We pre...
  </details>

- **2026-07-14** — Julius Steiglechner, Lucas Mahler, Gabriele Lohmann — [LLMs Can See the Smoke but not the Fire: Evaluating Abductive Reasoning with Elenchos](http://arxiv.org/abs/2607.12733v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) excel at pattern recognition and text generation, but their capacity for abductive inference - inferring latent hypotheses that explain observed behavior - remains poorly understood. Here, we introduce Elenchos (named after the Socratic method of cross-examination), a generative evaluation framework that measures abductive reasoning as a structural inverse problem. Given a reference formal system, such as the lambda-calculus, and a potentially mutated counterpart, ag...
  </details>

- **2026-07-14** — Jiahang Wang, Yirong Yang, Yanqing Zhu et al. — [ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning](http://arxiv.org/abs/2607.12680v1)
  <details><summary>📄 Abstract</summary>
  Existing vision-language navigation methods often couple a VLM with waypoint decoders to produce multi-step action plans, but they typically lack an explicit closed-loop mechanism for tracking semantic progress, diagnosing execution failures, and recovering from error accumulation in long-horizon navigation. To address this gap, we propose ReflectVLN, an agentic VLN framework that organizes decision-making through bidirectionally interactive intention and execution agents. The intention agent pe...
  </details>

- **2026-07-14** — Jiho Jun, Jeongwon Woo, Jaemin Song et al. — [MAGE: Color-Invariant and Spatial Knowledge Distillation for Gastric Neoplasm Classification](http://arxiv.org/abs/2607.12663v1)
  <details><summary>📄 Abstract</summary>
  Accurate differentiation between gastric adenoma and carcinoma during endoscopy is critical for clinical decision-making. Yet, this task is highly challenging due to high inter-class similarity and ambiguous boundaries between the two classes. Existing ROI-based classification methods often suffer from detection/segmentation error propagation and loss of surrounding global context. In contrast, full-image classification lacks the necessary spatial focus. Furthermore, we observe that deep neural ...
  </details>

- **2026-07-14** — Raheen Junaid Wani, Smruti R. Sarangi — [Lightweight Multi-Scale Anomaly Detection for Resource-Constrained Edge Devices](http://arxiv.org/abs/2607.12599v1)
  <details><summary>📄 Abstract</summary>
  Time-series anomaly detection is increasingly important in IoT systems, sensor networks, and edge monitoring applications, where models must operate under strict constraints on memory, latency, and power consumption. While recent deep-learning approaches have improved detection accuracy, many remain computationally expensive and often fail to capture subtle anomalies due to limited multi-scale sensitivity. Autoencoders are widely used for anomaly detection because they reconstruct normal pattern...
  </details>

- **2026-07-14** — Mattia Tamiazzo, Simone Milani, Massimo Iuliani et al. — [Explainable-by-Design Audio Deepfake Detection via Wiener-Hopf Linear Prediction](http://arxiv.org/abs/2607.12584v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of synthetic speech generation methods has made audio deepfake detection a critical challenge in multimedia forensics. While recent approaches achieve high detection accuracy, they typically rely on black-box architectures that offer limited interpretability and high computational complexity. In this paper, we propose an explainable-by-design audio deepfake detection framework based on Wiener-Hopf linear prediction, processed by a lightweight 2D Convolutional Neural Network...
  </details>

- **2026-07-14** — Martin Uray, Saverio Messineo, Roland Kwitt et al. — [Exploring Zero-Shot Foundation Models for Multivariate Time Series Anomaly Detection](http://arxiv.org/abs/2607.12454v1)
  <details><summary>📄 Abstract</summary>
  Multivariate Time Series Anomaly Detection (MTSAD) is essential for reliability and safety in domains such as industrial process monitoring and financial risk management, yet conventional approaches rely on application-specific models that are costly to train and hard to scale. Foundation Models (FMs), pre-trained on broad data with strong zero-shot generalization, have recently become available for univariate time series forecasting, raising the question of whether they can address MTSAD withou...
  </details>

- **2026-07-14** — A H M Nazmus Sakib, Dipayan Banik, Murtuza Jadliwala — [Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents](http://arxiv.org/abs/2607.12428v1)
  <details><summary>📄 Abstract</summary>
  The increasing adoption of autonomous coding agents accelerates software development but also introduces scoped security risks within high-impact file paths that can outpace traditional human review capacity. While prior research has primarily evaluated these systems in terms of functional correctness and productivity, this paper presents a large-scale empirical study using the AIDev dataset to systematically characterize security code smells in agent-generated pull requests (PRs). Through a com...
  </details>

- **2026-07-14** — Xiaoning Ren, Yinxing Xue, Lei Ma et al. — [Code-MUE: Measuring Code LLMs' Uncertainty through Execution-based Semantic Interaction Graphs](http://arxiv.org/abs/2607.12273v1)
  <details><summary>📄 Abstract</summary>
  As Code Large Language Models (LLMs) become central to modern software engineering, their inherent stochasticity poses significant real-world risks, where even minor errors can lead to severe functional, security, or safety consequences. Reliable automation, therefore, demands the ability to distinguish between confident, well-supported predictions and stochastic guessing. However, existing uncertainty estimation methods face a critical gap: white and grey-box techniques are often inapplicable t...
  </details>

- **2026-07-14** — Joshua Hill — [Saturation Makes Quantization Error Additive: A Coverage Model with a Certificate](http://arxiv.org/abs/2607.12266v1)
  <details><summary>📄 Abstract</summary>
  Mixed-precision quantization must decide which parts of a model to keep at higher precision. A common premise, shared by sensitivity-based methods such as HAWQ and CoopQ, is that the loss from quantizing a set of layers can be reconstructed from per-layer or pairwise sensitivities measured in isolation. We test this premise at the 4-bit weight-and-activation precisions now being deployed, treating the change in loss $f(S)$ from quantizing a layer set $S$ as a set function on the Boolean cube and...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 53 papers

- **2026-07-28** — Yu Yan, Jiahao Chen, Siqi Lu et al. — [Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks](http://arxiv.org/abs/2607.25227v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been widely applied in high-stakes decision-making scenarios such as corporate strategy, and users are increasingly relying on their outputs. However, the deep integration of open-source model sharing ecosystems with LLM-powered critical decision-making applications also introduces critical risks: if an attacker can manipulate the model's cognitive stance, they can indirectly influence the judgments and actions of downstream decision-makers. This paper defines s...
  </details>

- **2026-07-28** — Frank Nie, Ethan B Liu, Yuan Zhu et al. — [A Cost-Effective Multimodal LLM Reasoning Framework for Question Answering over Irregular Clinical Time Series](http://arxiv.org/abs/2607.25947v1)
  <details><summary>📄 Abstract</summary>
  Question answering (QA) over irregular clinical time series (ICTS) plays a pivotal role in a wide range of healthcare applications. Although recent multimodal time-series large language models (LLMs) have shown considerable promise in general-purpose time-series QA, they remain poorly equipped to model the sparsity, asynchrony, and irregular sampling patterns of clinical observations. To fill this gap, we propose ClinPRISM, a cost-effective multimodal LLM reasoning framework for question answeri...
  </details>

- **2026-07-28** — Can Lei, Rafael Garcia, Nuno Gracias et al. — [SC-Match: Scale-Space Matching with Context Consistency for Side-Scan Sonar Mapping](http://arxiv.org/abs/2607.25937v1)
  <details><summary>📄 Abstract</summary>
  Reliable estimation of spatial correspondences between overlapping side-scan sonar (SSS) measurements is essential for mapping, but acoustic appearance variations, weak seabed texture, repetitive patterns, and shadows make such correspondences sparse, unstable, and context-dependent. Scarce point-level annotations further limit sonar-specific training or fine-tuning of deep matching models. To this end, we propose SC-Match, a training-free scale-space matching framework with context-consistent c...
  </details>

- **2026-07-28** — Ramtin Ehsani, Irene Manotas, Saurabh Pujar et al. — [How Do LLMs Read Bug Reports? An Empirical Study of Attention in LLMs for Automated Program Repair](http://arxiv.org/abs/2607.25873v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based Automated Program Repair systems are advancing rapidly, yet their performance remains inconsistent. Even when provided with the same contextual information, an LLM may generate a correct patch for one bug but fail on another closely related bug. Why this happens remains poorly understood, and it is unclear how LLMs prioritize the diverse information in bug reports and whether model attention affects repair success. In this paper, we present the first empirical st...
  </details>

- **2026-07-28** — Leonardo Centellas-Claros, Estefania Pakarati-Cofre, Juan Pablo Sandoval Alcocer et al. — [Rethinking Training Data for Generating Code Review Comments](http://arxiv.org/abs/2607.25851v1)
  <details><summary>📄 Abstract</summary>
  Generating code review comments has become a prominent research direction in automated code review, commonly formulated as a text generation task over diff-comment pairs. Despite advances in learning-based approaches, generated review comments are often generic, weakly grounded, or non-actionable. Recent studies have also shown that review comment datasets contain noisy or unsuitable training instances, motivating LLM-based dataset cleaning approaches. In this paper, we argue that problematic tr...
  </details>

- **2026-07-28** — Aleksandr V. Petrov, Tarun Chillara, Matthew D. Moellman et al. — [Hypothesis-Driven Shelf Generation for Personalised Recommendation](http://arxiv.org/abs/2607.25823v1)
  <details><summary>📄 Abstract</summary>
  Modern recommendation interfaces organise content into shelves: themed rows such as "More of What You Like" or "New Releases for You." In production systems, these shelves are typically defined through hand-crafted templates coupled with dedicated retrieval logic. While effective for broad recommendation intents, this approach does not scale to the long tail of individual taste. We present a content-hypothesis-driven shelf generation system for Spotify Home that replaces fixed templates with nat...
  </details>

- **2026-07-28** — Jui-Feng Chi, Wei-Lun Chu, Bruce Coburn et al. — [Fine-Grained Food Image Understanding via Target-Aware Data Alignment](http://arxiv.org/abs/2607.25794v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained food visual--semantic understanding requires models to capture subtle distinctions across ingredients, cooking methods, doneness, color, texture, and plate composition. Although CLIP-style vision-language models provide a natural framework for this task, their effectiveness is limited when training relies on heterogeneous web-collected image--text pairs. Such data often exhibit a web-to-target domain gap and cross-modal misalignment, where images differ from the target distribution ...
  </details>

- **2026-07-28** — Seungheon Doh, Bruno Sguerra, Sergio Oramas et al. — [LLM-as-a-Judge for Evaluating System Responses in Conversational Music Recommendation](http://arxiv.org/abs/2607.25640v1)
  <details><summary>📄 Abstract</summary>
  Conversational Recommendation Systems (CRS) aim to achieve two primary objectives: recommending relevant items and generating natural language responses. While recommendation accuracy is effectively measured by established ranking metrics, the evaluation of response generation poses a more fundamental challenge. Although human evaluation remains the gold standard, its cost and scalability constraints have motivated the adoption of LLM-as-a-judge as a promising proxy, whose alignment with human j...
  </details>

- **2026-07-28** — Jiarui Wang, Xiang Shi, Jiaqi Cao et al. — [MemSFT: Mitigating Alignment Tax with an External Parametric Memory](http://arxiv.org/abs/2607.25614v1)
  <details><summary>📄 Abstract</summary>
  Adapting Large Language Models (LLMs) to specialized domains often incurs an alignment tax, as fine-tuning on domain-specific tasks can cause catastrophic forgetting and substantially degrade performance on general tasks. We propose MemSFT, which mitigates the alignment tax by decoupling domain specialization from backbone parameter updates through a plug-and-play parametric memory. The memory is trained to imitate the behavior of a non-parametric retriever operating over domain data, thereby me...
  </details>

- **2026-07-28** — Abraham Chachamovits — [Phase Structure in Rotary Attention: A Spectral Framework for Semantic Continuity and Execution-Boundary Governance](http://arxiv.org/abs/2607.25507v1)
  <details><summary>📄 Abstract</summary>
  Transformer language models are usually analyzed through vector geometry, yet ordered context and rotary position encoding introduce explicit phase structure into query-key interactions. This paper develops a bounded spectral framework for examining rotary phase alignment, hidden-state continuity, and semantic drift without treating language models as literal physical wave systems. It first identifies ordered hidden-state sequences, rather than vocabulary indices, as valid domains for spectral d...
  </details>

- **2026-07-28** — Jincheng Wang, Min Zheng, Tao Wei — [COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution](http://arxiv.org/abs/2607.25400v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly entrusted with natural-language workflow instructions (e.g., retail-payment policies) that specify not only what outcome to achieve, but also which steps, branches, and tool interactions are permitted. When these instructions are supplied as prompt context, however, the model retains control over both procedure selection and step execution. As interactions accumulate, an agent can skip required steps, take unsupported branches, or execute a vali...
  </details>

- **2026-07-28** — Huwei Ji, Jiajie Su, Yuyuan Li et al. — [Sharpness-aware Model Merging with Salience Recovery for LLM-based Cross-Domain Sequential Recommendation](http://arxiv.org/abs/2607.25366v1)
  <details><summary>📄 Abstract</summary>
  LLM-based Cross-Domain Sequential Recommendation (CDSR) leverages LLMs to enhance target performance via deep semantic reasoning, alleviating the dependency on overlapping users. Among LLM-based paradigms, model merging is particularly promising for multi-domain scenarios due to its superior scalability and flexibility in integrating diverse knowledge sources. However, our empirical investigations reveal two critical bottlenecks: (1) cross-domain knowledge conflict; and (2) performance saturatio...
  </details>

- **2026-07-28** — Yujian Ma, Jinqiu Sang, Ruizhe Li et al. — [From Semantics to Readout: Mechanistic Understanding of Audio Tokens after Fine-Tuning for Temporal Audio Grounding](http://arxiv.org/abs/2607.25355v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) convey acoustic evidence to language decoders through native audio tokens, yet the internal roles of these tokens remain poorly understood. Using temporal audio grounding as a diagnostic setting, we examine how language-model fine-tuning affects the layerwise semantics, decoder accessibility, and temporal output alignment of native audio-token states through four complementary analyses: query-conditioned token semantics, calibrated token readout, temporal-wind...
  </details>

- **2026-07-28** — Aysan Aghazadeh, Sina Malakouti, Adriana Kovashka — [Sense it with your eyes: Sensation Generation and Understanding for Advertisements](http://arxiv.org/abs/2607.25314v1)
  <details><summary>📄 Abstract</summary>
  Sensory advertising evokes human senses through visual cues, enabling audiences to mentally simulate experiences and increasing persuasive impact. Despite the recent increase in using AI in generating and understanding creative and persuasive content, how advertisements visually evoke sensations remains largely unexplored. In this work, we introduce the first study of understanding, evaluating, and generating sensory ads. We introduce the Sensory Ad dataset, and define sensation classification t...
  </details>

- **2026-07-28** — Katsuya Ogata, Zongshang Pang, Mayu Otani et al. — [MEDit-Bench: A Dataset for Evaluating Message-Driven Narrative Video Editing](http://arxiv.org/abs/2607.25300v1)
  <details><summary>📄 Abstract</summary>
  Video editing is fundamentally message-driven: even from the same source footage, the selected shots change depending on the narrative the editor wishes to convey. Benchmarks for a closely related task, video summarization, reduce editorial intent to a single, message-agnostic notion of saliency and thus do not account for this diversity. For evaluating message-driven video editing, we present \textbf{MEDit-Bench}, a dataset and benchmark, which pairs long-form videos with multiple editing messa...
  </details>

- **2026-07-28** — Jingbo Zhang, Haoxiang Sun, Wenbo Wang et al. — [ContractHIL-HLS: Contract-Aligned Multi-Agent Workflow with Hardware-in-the-Loop Feedback for HLS Design](http://arxiv.org/abs/2607.25283v1)
  <details><summary>📄 Abstract</summary>
  This paper presents ContractHIL-HLS, a contract-aligned multi-agent workflow for practical high-level synthesis (HLS) engineering. The workflow makes three contributions. First, it introduces a structured contract as the semantic-alignment and task-execution artifact that translates natural language requirements into explicit interfaces, constraints, validation checks, and rollback rules. Second, it incorporates hardware information into the feedback loop by feeding HLS, Vivado, PYNQ runtime, po...
  </details>

- **2026-07-28** — Qian Cheng, Saad Mohammad Rafid Pial, Ruize Tang et al. — [Specula: Scaling formal specifications for autonomous model checking of system code](http://arxiv.org/abs/2607.25333v1)
  <details><summary>📄 Abstract</summary>
  Specula is a push-button agentic system that generates high-quality formal specifications for large, complex system code and uses the specifications for highly effective model checking and bug finding. Specula employs large language model (LLM) based coding agents to autonomously develop TLA+ specifications, including invariants that describe correctness properties of the target system and formal models that describe the system implementation with the right level of abstractions. Specula is full...
  </details>

- **2026-07-28** — Xiaoyu Huang, Lulu Wang — [Emergent Latent-State Computation under Stochastic Volatility](http://arxiv.org/abs/2607.25459v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability has largely focused on language models and deterministic toy tasks. Much less is known about how sequence models internally represent latent stochastic dynamics under noisy, partially observed observations. We study this question in a controlled multivariate stochastic volatility setting, where models observe only returns while the ground-truth latent volatility state is known to the researcher. This setting provides a useful benchmark for mechanistic interpretabilit...
  </details>

- **2026-07-27** — Michał Wiliński, Liu Leqi, Chirag Nagpal — [Inverse RL Helps Align AI by Imitating Humans](http://arxiv.org/abs/2607.24900v1)
  <details><summary>📄 Abstract</summary>
  Language model alignment aims to make model behavior reliably reflect desirable properties such as helpfulness, safety, and instruction following. Current approaches typically use supervised fine-tuning on demonstrations or reinforcement learning with rewards derived from verifiers or human feedback. These paradigms leave an important question underexplored: can demonstrations alone yield an implicit reward that can be inspected, reused, and optimized on-policy to align AI? Motivated by inverse ...
  </details>

- **2026-07-27** — Yubo Sun, Chunyi Peng, Yukun Yan et al. — [HiEviDR-Bench: A Benchmark for Hierarchical Evidence Aggregation in Deep Research](http://arxiv.org/abs/2607.25151v1)
  <details><summary>📄 Abstract</summary>
  Deep research requires models to retrieve, connect, and synthesize evidence from large-scale heterogeneous sources to answer complex queries and produce analytical reports. Existing benchmarks mainly evaluate final outcomes, such as answer correctness, report quality, or citation alignment, while providing limited visibility into whether evidence is correctly selected, linked, and aggregated into supported claims and conclusions. To address this gap, we introduce HiEviDR-Bench, a benchmark for e...
  </details>

- **2026-07-27** — Takuya Isogawa, Ryotaro Okabe, Nutdech Phadetsuwannukun et al. — [Agentic AI for Scientific Reasoning in Autonomous Quantum Sensing Experiments](http://arxiv.org/abs/2607.25145v1)
  <details><summary>📄 Abstract</summary>
  We implement an agentic AI workflow built around a large language model (LLM) agent for autonomous experiments with nitrogen-vacancy (NV) centers in diamond. NV centers are a widely used platform for quantum sensing, and the ability to control many measurements from a computer makes NV experiments a natural setting for autonomous workflows. We make two main contributions. First, we demonstrate an autonomous NV experiment workflow that combines persistent project records, quantitative calculation...
  </details>

- **2026-07-27** — Md Rezwanul Haque, Md. Milon Islam, Fakhri Karray — [Towards Robust Reinforcement Learning for Small-Scale Language Model Agents](http://arxiv.org/abs/2607.25091v1)
  <details><summary>📄 Abstract</summary>
  The alignment of Small Language Models (SLMs) in the 70--500M parameter range using reinforcement learning is often considered unstable, though the underlying failure mechanisms have not been systematically investigated. In the State-of-the-Art (SOTA) research, fifteen (model, corpus) configurations were trained using Proximal Policy Optimization (PPO). The experiments included Pythia-70M, 160M, 410M and SmolLM2-135M, 360M on the TinyStories, CNN/DailyMail, and Wikitext-103 corpora. Three reprod...
  </details>

- **2026-07-27** — Sylvain Chassang — [Interactive Alignment](http://arxiv.org/abs/2607.25019v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the long-run alignment of interactive agents, including AI systems, teams, firms, and governments, with human welfare. It develops a farming game in which a population of agents makes planting, trading, and expansion decisions. Agents must allocate final output between transfers to humans and investment in their own expansion. Because transfers to humans reduce the resources available for expansion, evolutionary forces tend to select against aligned behavior. The central quest...
  </details>

- **2026-07-27** — Yifan Ye, Yankai Fu, Yaoxu Lv et al. — [Data Pyramid for Embodied Manipulation](http://arxiv.org/abs/2607.24744v1)
  <details><summary>📄 Abstract</summary>
  Multimodal foundation models learned to see and to speak by consuming the whole internet. Embodied agents admit no such shortcut, since they require data that couple observations with physical states and actions. These signals can be provided, to varying degrees, by multiple data sources. In this work, we organize the embodied data ecosystem as a "pyramid" spanning five complementary sources: real-robot data, UMI-style data, egocentric and exocentric data, simulation data, and general vision-lan...
  </details>

- **2026-07-27** — Yu Xia, Zihan Lin, Wei Yang et al. — [LaRec: Unleashing LLM-based Latent Reasoning for Generative Recommendation](http://arxiv.org/abs/2607.24617v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown great promise in recommendation due to superior reasoning abilities. However, existing methods mainly rely on explicit Chain-of-Thought (CoT), resulting in verbose reasoning texts and inefficient response times. latent reasoning aims to balance efficiency by thinking within a continuous latent space, yet it faces two major challenges: (1) Lack of Fine-grained Supervision: Latent reasoning relies solely on feedback from the final labels, providing sparse su...
  </details>

- **2026-07-27** — André Sacilotti, Samuel Felipe dos Santos, Jurandy Almeida — [Test-Time Adaptation via Dual Distillation for Videos Under Severe Distribution Shifts](http://arxiv.org/abs/2607.24611v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models have achieved state-of-the-art performance in several computer vision tasks. However, they experience severe performance degradation when applied to real-world scenarios due to unanticipated distribution shifts. Test-Time Adaptation (TTA) attempts to solve this problem by using unlabeled data from the target domain to dynamically adapt to the test distribution at inference time, without access to the source data. However, TTA remains a challenging problem when adapting to co...
  </details>

- **2026-07-27** — Muna Alebri, Noëlle Rakotondravony, Yassine Bechqito et al. — [Designing Within the Lines: Practitioners' Perspectives and Visualisation Tool Evaluation in the Arabic Context](http://arxiv.org/abs/2607.24571v1)
  <details><summary>📄 Abstract</summary>
  Design guidelines and best practices serve as references that support designers throughout the visualisation design process. While considerable effort has identified the elements that contribute to effective data visualisations, little attention has been paid to how language (scripts and reading direction), tool support, and cultural context also shape design decisions. As a result, assumptions of homogeneity persist, with visualisation practices predominantly benefiting users of English and lef...
  </details>

- **2026-07-27** — Sriharshaa S, Sangeetha Sivanesan, Jaya Nirmala S — [Systematic Analysis of Large Language Models and Transformer-Based Machine Translation for English-Tamil and Tamil-English Across Diverse Datasets](http://arxiv.org/abs/2607.24515v2)
  <details><summary>📄 Abstract</summary>
  The challenge of Machine Translation for low resource languages such as Tamil is primarily caused by the restricted amount of parallel data for these languages, as well as their substantial amount of domain variation and morphological complexity. This research presents the comprehensive evaluation of the performance of several multilingual translation models on English-Tamil and Tamil-English translations across multiple datasets: NTREX, EnTamV2, WikiMatrix and PMIndia. This study evaluates supe...
  </details>

- **2026-07-27** — Jinhao Zhang, Zeyu Liu, Zicheng Yan et al. — [Mechanisms of Width Scaling in Normalized Residual Networks: The Effective Alignment Dimension](http://arxiv.org/abs/2607.24887v1)
  <details><summary>📄 Abstract</summary>
  Existing theories of neural-network width characterize asymptotic limits, but provide limited guidance on whether an expansion direction identified from finite training data remains beneficial on unseen data. We study this problem for function-preserving residual expansion and introduce the effective alignment dimension, a measurable quantity describing the signal-noise geometry of activation gradients. By deriving the exact mean and variance of the inner product between independently estimated ...
  </details>

- **2026-07-27** — Guo Tang, HongJie Luo, Tianxu Wang et al. — [PRISM: Prompt Refinement via Image-grounded Self-rewarding Mechanism for Text-to-Image Generation](http://arxiv.org/abs/2607.24353v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image generation models can synthesize high-quality images from natural language descriptions, but their performance remains highly sensitive to prompt formulation. Existing prompt optimization methods mainly rely on text-side rewriting, prompt expansion, or external reward signals, offering limited image-grounded diagnosis and weak support for learning reusable optimisation policies. In this paper, we propose PRISM, a Prompt Refinement framework via Image-grounded Self-rewarding Mechani...
  </details>

- **2026-07-27** — Mingxuan Sun — [CONSISTRE: A Unified Consistency-Aware Framework for Document-Level Relation Extraction with Large Language Models](http://arxiv.org/abs/2607.24312v1)
  <details><summary>📄 Abstract</summary>
  Document-level relation extraction (DocRE) aims to extract relations among multiple entities across extended contexts while maintaining consistency across predicted triples. Although large language models (LLMs) show remarkable reasoning capabilities in information extraction, their predictions are typically generated independently for each candidate triple and may violate fundamental relational constraints such as transitivity, symmetry, and functional uniqueness, leading to contradictory and u...
  </details>

- **2026-07-27** — Shuo Wang, Fang Xi, Wenyuan Huang et al. — [KAP: Bridging the Knowledge Selection-Runtime Consumption Gap in LLM Systems](http://arxiv.org/abs/2607.24260v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM systems increasingly rely on knowledge-selection processes that produce high-value structured priors, such as ranked evidence, graph topology, multimodal alignment, and confidence signals. Yet LLM serving remains fundamentally oblivious to this rich structure: once such signals are serialized into a prompt, the backend observes only a flat token sequence, forcing dense and uniform consumption of the full key-value (KV) state during decoding. We term this architectural mismatch the Kno...
  </details>

- **2026-07-27** — Shengyi Wang, Niantong Li, Guangzheng Hu et al. — [FilmBench: A Film-Grade Benchmark for Cinematic Video Generation](http://arxiv.org/abs/2607.24241v1)
  <details><summary>📄 Abstract</summary>
  Progress in video generation keeps narrowing the visual gap between AI-generated and professionally produced footage, yet most benchmarks still draw prompts from web sources or LLM templates and score them with untrained, generic multimodal models. More fundamentally, their evaluation taxonomies remain rudimentary (overall visual quality, coarse text alignment and temporal smoothness) rather than the professional Cinematic Language criteria by which films are actually made and judged, so they as...
  </details>

- **2026-07-27** — Songyue Cai, Lianyu Wang, Shan Gu et al. — [Strategy-Aware Parameter-Efficient Adaptation for LLM-based Auto-Bidding](http://arxiv.org/abs/2607.24232v1)
  <details><summary>📄 Abstract</summary>
  Advertising bidding has evolved from manual strategies to auto-bidding systems better adapted for large-scale, dynamic auction environments. While recent advances in Large Language Models (LLMs) offer strong reasoning for auto-bidding, existing methods suffer from shallow trajectory-text interactions and require costly fine-tuning, hindering the efficient use of pretrained knowledge under diverse constraints. To address these challenges, we propose SAGE, a novel Strategy-aware Auto-bidding frame...
  </details>

- **2026-07-27** — Pengyu Xie, Rongjia Zhou, Zhilin Ou et al. — [TCellAlign: Cross-study T-cell Populations Alignment with Nomenclature-Guided Multi-Agent Workflow](http://arxiv.org/abs/2607.24093v1)
  <details><summary>📄 Abstract</summary>
  Cell type standardization plays a central role in integrating biological knowledge across single-cell studies. While standardized resources (e.g., Cell Ontology, Nomenclature Frameworks) provide unified vocabularies of cell populations, scientific publications and public datasets continue to use heterogeneous study-specific labels, making cross-study comparison difficult even when biologically equivalent cell populations are described. In this work, we are the first to formulate this challenge a...
  </details>

- **2026-07-27** — Michael Girstl, Alexander Mattick, Christopher Mutschler — [Constrained Reinforcement Learning Using Successor Representations](http://arxiv.org/abs/2607.24057v1)
  <details><summary>📄 Abstract</summary>
  Real-world Reinforcement Learning depends on the ability to formulate safety constraints into a policy. A common way to model such constraints is to introduce an additional cost signal in the Markov Decision Process, which notifies the agent of unwanted behavior independently of the reward signal. Unfortunately, current methods are hard to adapt to changes in the cost function introduced by, e.g., domain shift or obstacles moving over time. The lack of adaptability means that policies are too un...
  </details>

- **2026-07-27** — Jiyu Wei, Di Hong, Zhanjie Zhang et al. — [A Cyclic Adaptation-Generalization Framework with Uncertainty-Guided Self-Paced Learning for Long-Term Brain-Machine Interfaces](http://arxiv.org/abs/2607.24031v1)
  <details><summary>📄 Abstract</summary>
  Brain-Machine Interfaces (BMIs), which link the brain to external devices, hold great potential in rehabilitation, human performance augmentation, and human-centered robotics. However, invasive BMIs face a critical challenge for long-term deployment due to neural drift, which degrades decoding performance over time and necessitates frequent recalibration. Existing methods designed to mitigate neural drift typically rely on either domain adaptation (DA) or domain generalization (DG) alone and oft...
  </details>

- **2026-07-27** — Hao Yang, Jin Wang, Xuejie Zhang — [DICA: Dual-Indicator Guided Contrastive Alignment in Multimodal Large Language Models](http://arxiv.org/abs/2607.23944v1)
  <details><summary>📄 Abstract</summary>
  Human visual reasoning typically follows a coarse-to-fine attention process, starting from global scene understanding and gradually focusing on question-relevant regions. However, multimodal large language models may deviate from this pattern due to attention drift and the underutilization of visual evidence, which can lead to hallucinations. To mitigate these issues, this study proposes a Dual-Indicator Guided Contrastive Alignment (DICA), which tracks two information-theoretic indicators durin...
  </details>

- **2026-07-27** — Stefan Richter, Alberto Giammarino, Guillem Torrente et al. — [Bridging Reinforcement Learning and Optimal Control via Feasible Action Mapping](http://arxiv.org/abs/2607.23930v1)
  <details><summary>📄 Abstract</summary>
  Operating constrained dynamical systems requires controllers to efficiently solve complex tasks while enforcing recursive feasibility and safety constraints. To address these competing requirements, we present Feasible Action for Optimal Control (FAOC), a novel control framework integrating Reinforcement Learning (RL) and Optimal Control (OC). The key contribution is a computationally efficient, optimization-based mapping algorithm that transforms the RL agent's action from a static abstract set...
  </details>

- **2026-07-27** — Roberto Spinelli, Thiago C. Martins — [Embodied GPT-5.1: Evidence of a World Model?](http://arxiv.org/abs/2607.23899v1)
  <details><summary>📄 Abstract</summary>
  This exploratory study examines whether a large multimodal language model, GPT-5.1, can serve as the high-level controller of a physical mobile robot despite having no prior embodiment, no training in simulated environments, and no exposure to sensorimotor experience. Using only low-resolution first-person images and a discrete action set, the model was tasked with navigation and object-directed behaviors such as locating and contacting a target toy. Across multiple trials, GPT-5.1 demonstrated ...
  </details>

- **2026-07-26** — Masoud Badiei Khuzani, Sharath Honnaiah, Atiq Islam et al. — [A Coulomb Particle Model for Learning Kernel Attention in Transformers](http://arxiv.org/abs/2607.23869v1)
  <details><summary>📄 Abstract</summary>
  Randomized features provide a scalable approximation to kernel machines, but their performance depends strongly on the choice of feature distribution. We propose a particle-based method that learns this distribution by optimizing kernel-target alignment while regularizing particles with a Riesz/Coulomb repulsive potential. The resulting Hamiltonian yields diverse, task-adaptive random features and admits a mean-field description through a McKean--Vlasov equation. We instantiate the method in lin...
  </details>

- **2026-07-26** — Xianghao Jiao, Ruoyu Chen, Wei Wang et al. — [Consistent Evidence, Robust Recognition: Faithful Attribution Regularization under Geometric Transformations](http://arxiv.org/abs/2607.23835v1)
  <details><summary>📄 Abstract</summary>
  Attribution methods are widely used to characterize the evidence underlying model predictions, yet their potential to improve model behavior remains underexplored. Attribution inconsistency under label-preserving geometric transformations may indicate transformation-sensitive evidence reliance, motivating attribution regularization. However, such supervision is valid only when attribution faithfully reflects the evidence driving predictions. Existing self-supervised methods typically align gradi...
  </details>

- **2026-07-26** — Chenghao Wu, Kesha Ou, Xiaolei Wang et al. — [ClawRec: A Claw-Native Recommender System](http://arxiv.org/abs/2607.23779v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems have become integral to navigating the modern digital ecosystem. Yet most deployed systems remain confined within single-platform boundaries, observing localized interaction traces and ranking items from isolated candidate spaces. This design is poorly suited to real-world tasks that unfold through searches, content consumption, and comparisons across multiple information sources. Claw-style personal agents, with persistent access to authorized cross-platform context, create ...
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

- **2026-07-14** — Kaiwen Zheng, Junchen Fu, Wenhao Deng et al. — [Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?](http://arxiv.org/abs/2607.12787v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc. However, these performance improvements are often accompanied by an increase in model parameter size (e.g, at least 7B), which simultaneously incurs high computational costs and reduces inference efficiency, thereby hindering real-time deployment on reso...
  </details>

- **2026-07-14** — Lin Peng, Cong Wan, Zeyu Guo et al. — [CoRe: A Comprehensive Framework for Cross-Image Comparative Reasoning in Vision-Language Models](http://arxiv.org/abs/2607.12786v1)
  <details><summary>📄 Abstract</summary>
  Cross-image comparative reasoning remains challenging for vision-language models (VLMs), especially when correct prediction requires fine-grained attribute grounding and globally consistent reasoning. We present CoRe, a unified framework for this problem. CoRe includes: (i) CoRe-20K, a large-scale triplet-based training set automatically constructed from structured visual metadata through a multi-expert collaborative pipeline, covering counting, depth, distance, and spatial relations; (ii) TriSR...
  </details>

- **2026-07-14** — Wei Liu, Weisong Sun, Tingting Xu et al. — [Understanding before Naming! Enhancing LLM-based Method Name Prediction with Code Summarization](http://arxiv.org/abs/2607.12467v1)
  <details><summary>📄 Abstract</summary>
  Method names are critical to software quality, affecting code comprehensibility, maintainability, and developer collaboration. However, manually designing meaningful method names is challenging. Method Name Prediction (MNP), which automatically generates method names from code snippets, has recently attracted attention. Although large language models (LLMs) show promising performance for MNP, two challenges remain. First, existing evaluations mainly rely on token similarity metrics, which often ...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 98 papers

- **2026-07-28** — Conor McCauley, Zeliang Kan, Jason Martin — [\textsc{IH-Benchmark}: A Conflict-Centered Benchmark for Instruction-Hierarchy Robustness in LLM Applications](http://arxiv.org/abs/2607.25987v1)
  <details><summary>📄 Abstract</summary>
  When a language model receives conflicting instructions from different priority levels, which one does it actually follow? This question lies at the heart of reliable LLM deployment. Existing benchmarks answer this only partially, often focusing on a single hierarchy edge or adapting public datasets with limited tool-use coverage. We present IH-Benchmark, a conflict-centered benchmark for instruction-hierarchy robustness across direct system-user conflicts (S>U) and tool-mediated user-tool (U>T)...
  </details>

- **2026-07-28** — Abhishek Pillai, Samir Kumar Nayak, Yuan Chen — [Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?](http://arxiv.org/abs/2607.26041v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks. Current benchmarks primarily measure end-task success or single-frame grounding. Neither isolates whether a model can reconstruct the causal, task-relevant transition produced by an action- crucial for rejecting stale observations, verifying progress, and recovering from failure. This is difficult because inference, remote input, app rendering, and screenshot capture are asynchronous: the next observ...
  </details>

- **2026-07-28** — Weitao Li, Gong Cheng — [Generator-Aligned Representation Interfaces for Diagnostic Soft Equivariance](http://arxiv.org/abs/2607.25988v1)
  <details><summary>📄 Abstract</summary>
  Exact-equivariant architectures typically encode prescribed group actions in specialized operators, which can complicate their reuse with generic backbones and across data modalities. We introduce the Generator-Aligned Representation Interface (GARI), a representation-level design principle that exposes selected transformation generators to a generic sequence backbone through aligned canonical and generator-induced views. We formalize the resulting behavior using a probe-specific soft-equivarian...
  </details>

- **2026-07-28** — Rui Yang, Weihao Xuan, Yi Lin et al. — [Evaluating Multi-Turn Multimodal Diagnostic Reasoning on Challenging Real-World Clinical Cases](http://arxiv.org/abs/2607.25933v1)
  <details><summary>📄 Abstract</summary>
  Clinical diagnostic evaluation should not only assess whether models can provide correct diagnoses, but also reflect the realities of clinical practice, including progressive disclosure of multimodal information, dynamic updating of diagnostic hypotheses, and continuous refinement of clinical reasoning. However, existing evaluations of multimodal large language models (MLLMs) typically rely on single-turn or isolated tasks, making it difficult to fully capture the complexity of real-world clinic...
  </details>

- **2026-07-28** — Yi Xu, Cheng Chen, Mufan Cao — [OrthKD: Extracting Generalized Clinical Knowledge from Heterogeneous Teachers for Lightweight Deployment](http://arxiv.org/abs/2607.25545v1)
  <details><summary>📄 Abstract</summary>
  Deploying diabetic retinopathy (DR) screening models in primary care requires edge-efficient systems that remain accurate, safe, and reliable under domain shift. Multi-teacher knowledge distillation (KD) is a natural compression strategy, but existing approaches largely assume that all teachers provide equally trustworthy supervision. In our setting, this assumption fails: a strong CNN teacher (EfficientNet-B3, 0.876 QWK) and a weaker Transformer teacher (Swin-Base, 0.830 QWK) are complementary,...
  </details>

- **2026-07-28** — Zheng Tong, Yang Liu, Wanshu Fan et al. — [Agentic AI in medicine: architectures, applications, evaluation, and challenges for clinical translation](http://arxiv.org/abs/2607.25489v1)
  <details><summary>📄 Abstract</summary>
  Large language models and multimodal foundation models are enabling medical artificial intelligence (AI) systems to move beyond isolated prediction and undertake multistep clinical tasks that require planning, tool use, memory, iterative correction, and coordination among specialized agents. However, the scope of agentic AI in medicine remains unsettled, and current evaluation practices are not yet aligned with the requirements of clinical use. We conducted a scoping review with systematic evide...
  </details>

- **2026-07-28** — Yuan Yin, Elias Ramzi, Marc Lafon et al. — [Pictura: Perspective-View Self-Play at Scale for Driving](http://arxiv.org/abs/2607.26005v1)
  <details><summary>📄 Abstract</summary>
  Self-play in simulation produces robust driving policies at scale. Demonstrations of such behavior have been made using privileged vectorized observations such as exact poses and velocities, even for occluded agents. This assumes that perception is solved and introduces a representation gap with the partial observation of a deployed agent driving from the perspective view of egocentric cameras. A common fix, distilling the privileged policy into a camera-input student, leaves the student imitati...
  </details>

- **2026-07-28** — Malena Loza, David Chushig-Muzo, Eva Milara et al. — [Empirical Evaluation of Out-Of-Distribution Performance of Tabular Foundation Models](http://arxiv.org/abs/2607.26000v1)
  <details><summary>📄 Abstract</summary>
  Tabular Foundation Models (TFMs) have emerged as novel approaches for tabular predictive tasks, demonstrating competitive predictive performance to ensemble tree-based models. Most TFMs are trained and evaluated on independent and identically distributed data, but this assumption changes in real-world scenarios due to distribution shifts, which compromise the robustness of models. Limited research has been conducted of TFMs under distribution shifts. We present an empirical evaluation of Out-Of-...
  </details>

- **2026-07-28** — Keyu Zhang, Vadim Safronov, Andrew Martin — [Stemma: Induced Decision Regions Reveal LLM Provenance](http://arxiv.org/abs/2607.25880v1)
  <details><summary>📄 Abstract</summary>
  LLM provenance testing asks whether a suspect LLM belongs to the same lineage as a source. Existing black-box methods largely infer this relationship from response-level characteristics, but these characteristics may shift under adaptation or deployment even when the underlying meaning remains unchanged, weakening the reliability of provenance evidence. To address this limitation, we introduce induced decision regions by mapping open-ended outputs into a finite decision space, thereby abstractin...
  </details>

- **2026-07-28** — Du Yin, Xiachong Lin, Yue Tan et al. — [A2TTA: Anchored-and-Agile Test-Time Adaptation for Evolving Traffic Sensor Networks](http://arxiv.org/abs/2607.25875v1)
  <details><summary>📄 Abstract</summary>
  Traffic forecasting is important for efficient traffic management and route planning in smart cities. Existing traffic forecasting studies typically assume fixed sensor graphs, overlooking the continuous evolution of real-world traffic networks, e.g., ongoing road network construction and evolving human mobility patterns. These dynamic changes can substantially degrade conventional forecasting models, motivating test-time adaptation (TTA) to efficiently adapt pretrained models during deployment....
  </details>

- **2026-07-28** — Weixin Liu, Juming Xiong, Congning Ni et al. — [DRIFT: Direct-Recursive Intervention-Conditioned Forecasting of ICU Physiological Trajectories](http://arxiv.org/abs/2607.25864v1)
  <details><summary>📄 Abstract</summary>
  Many time-series forecasts depend not only on prior observations but also on actions specified during the forecast period. In intensive care units (ICUs), future vital signs and laboratory values are influenced by treatments such as vasopressors. However, models that predict the full future sequence all at once make little use of these treatments, whereas autoregressive models can accumulate errors. We introduce DRIFT, a hybrid framework in which a direct model produces the primary forecast and ...
  </details>

- **2026-07-28** — Philipp Gessler, Alessandro Pignedoli, Alexander Neuhaus et al. — [Topological Classification of Non-Normalizable Vector Fields](http://arxiv.org/abs/2607.25848v1)
  <details><summary>📄 Abstract</summary>
  Topological classification of physical vector fields conventionally relies on field normalization and homotopy-based invariants. However, when field amplitudes vanish, normalization becomes ill-defined, preventing a direct topological characterization. Here, we introduce a general framework for the topological classification of non-normalizable $n$-dimensional vector fields with compactifiable base spaces by transforming them into $(n+1)$-dimensional normalized vector fields. This construction e...
  </details>

- **2026-07-28** — Jean-Philippe Bouchaud, Pierre Bousseyroux, Tomas Espana et al. — [Spectra of high-dimensional Spearman correlation matrices under scale-mixture dependence](http://arxiv.org/abs/2607.25486v1)
  <details><summary>📄 Abstract</summary>
  We study the asymptotic spectral properties of high-dimensional Spearman correlation matrices for scale-mixture data. We consider observations of the form $x_t=σ_t ξ_t \in \mathbb{R}^N,$ where the coordinates of $ξ_t$ are i.i.d.\ and the scalar mixture variable $σ_t$ is shared by all coordinates. Under natural symmetry assumptions, the coordinates of $x_t$ are pairwise uncorrelated in both the Pearson and Spearman sense. Nevertheless, they are not independent when the mixture variable is non-deg...
  </details>

- **2026-07-28** — Frank Schweitzer — [Resilience: Understand Breakdown, Foster Recovery, and Choose the Right Perspective](http://arxiv.org/abs/2607.25458v1)
  <details><summary>📄 Abstract</summary>
  Resilience denotes the capacity of a system to withstand shocks and to recover from them. We distinguish between two different types of dynamics. The first allows for a separation between phases of normalcy and phases of rapid breakdown followed by slow recovery. The second applies to volatile organizations in which such phases are intertwined. Breakdown is often self-inflicted. Situation awareness is impaired by psychological mechanisms that lead to incorrect expectations regarding societal dyn...
  </details>

- **2026-07-28** — Masaki Satoh — [HOME: Robust Hough-space Matching Method for Structured and Textureless Videos](http://arxiv.org/abs/2607.25389v1)
  <details><summary>📄 Abstract</summary>
  Visual front-ends for robotic localization typically rely on point-based features such as Oriented FAST and Rotated BRIEF (ORB), which frequently fail in structured environments dominated by strong linear structures or textureless surfaces. While line-based Simultaneous Localization and Mapping (SLAM) systems mitigate this by utilizing line segments, conventional line extraction and description algorithms are computationally prohibitive for real-time edge robotics. To address this fundamental bo...
  </details>

- **2026-07-28** — Jintian Ji, Xingsu Li, Songhe Feng — [Breaking the Periodicity Assumption: Robust Tensorial Multi-View Clustering via Graph-Spectral Low-Rank Learning](http://arxiv.org/abs/2607.25295v1)
  <details><summary>📄 Abstract</summary>
  Tensorial multi-view clustering (TMC) has achieved strong performance due to its ability to capture high-order correlations across multiple views. Most existing t-SVD-based TMC frameworks apply the Fast Fourier Transform (FFT) along the sample mode to impose frequency-domain low-rank constraints. However, we reveal that this widely adopted design critically relies on an implicit ``periodicity assumption'' induced by the sample arrangement. When samples are ordered by class, neighboring indices t...
  </details>

- **2026-07-27** — Md Ashikur Rahman, Md Arifur Rahman, Niamul Hassan Samin et al. — [Beyond Aggregate Risk: Role-Stratified Conformal Risk Control for LLM Tool Calls](http://arxiv.org/abs/2607.24343v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents act through structured tool calls whose arguments carry different risks. Untrusted content may safely influence an email body but should not determine a recipient, account, command, or credential. Existing statistical methods typically control risk over the entire action, allowing failures in rare, high-risk fields to be obscured by benign arguments. We introduce role-stratified per-field conformal risk control, a calibration layer that wraps any per-field detector and sets...
  </details>

- **2026-07-27** — Barbara Kitchenham, Sebastián Pizard, Lech Madeyski et al. — [Preliminary Guidelines for Using and Evaluating GenAI Tools to Support Systematic Literature Reviews](http://arxiv.org/abs/2607.24991v1)
  <details><summary>📄 Abstract</summary>
  Context: Generative AI (GenAI) and Large Language Models (LLMs) are increasingly used for academic tasks in software engineering and beyond, including systematic literature reviews (SLRs). However, while capable of summarizing text, there is no guarantee they can meet the rigour, reliability, and transparency that SLRs require. Objectives: To support researchers intending to conduct SLRs using GenAI or those conducting empirical studies evaluating how well GenAI supports SLR tasks. Methods: Firs...
  </details>

- **2026-07-27** — Zeyu Zhang, Xue Li, Iacer Calixto et al. — [Beyond Scale and Generation: Understanding Language Model-based Entity Matching](http://arxiv.org/abs/2607.24688v1)
  <details><summary>📄 Abstract</summary>
  Entity matching identifies records that refer to the same real-world entity. Language models can be adapted to this task through bi-encoder, cross-encoder, and generative matcher architectures. However, prior studies often conflate matcher architecture with differences in model backbone, model variant(reflecting different pretraining objectives), and model size, making it difficult to isolate the sources of performance gains. We address this issue through a controlled factorial study spanning th...
  </details>

- **2026-07-27** — Sebastià Nicolau, Adrià Molina, Oriol Ramos Terrades et al. — [Robust Interpretation of Historical Documents in Knowledge Graphs Through Query Inference and Execution](http://arxiv.org/abs/2607.24475v1)
  <details><summary>📄 Abstract</summary>
  The emergence of Large Language Models (LLMs) has redefined how users interact with information in digital environments. However, their widespread and often indiscriminate integration has raised significant concerns regarding reliability and trustworthiness issues that are particularly critical when accessing digital libraries and historical archives. How can one leverage the generalization capacity of an LLM without losing the level of accountability required for an archival institution? In thi...
  </details>

- **2026-07-27** — Florin Neagu — [Decentralised Consensus Learning Networks: SME Rotation Without Centralised Reward](http://arxiv.org/abs/2607.24416v1)
  <details><summary>📄 Abstract</summary>
  Centralised reward signals dominate modern AI learning systems, but they impose a single external definition of correct or valuable knowledge. We present a decentralised, consensus-based multi-agent learning framework in which expertise emerges through peer validation rather than prescribed reward. Agents update beliefs via weighted social consensus, while trust is allocated according to competence inferred from peer consistency instead of ground truth. Subject-matter expert (SME) status is assi...
  </details>

- **2026-07-27** — Tianyi Gao, Han Fang, Tianyi Ding et al. — [Mixture-of-Thought-Tokens: Unifying Perception and Reasoning for Free-form Multimodal Grounding](http://arxiv.org/abs/2607.24407v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models have made great progress in grounding tasks, yet existing methods still struggle to unify precise localization and complex reasoning. For one thing, text-based methods rely on coordinates or index prediction, severely limiting the perceptual capabilities of the model for dense visual objects. Meanwhile, latent token-based methods employ special tokens without inherent spatial references and use a decoding mechanism that lacks thinking steps, weakening high-level ...
  </details>

- **2026-07-27** — Yidong Huang, Tenglong Lu, Hanwen Kang et al. — [Aligning Heterogeneous DFT Datasets: A Graph Neural Network Approach to Cross-Functional Formation Energies](http://arxiv.org/abs/2607.24327v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous density functional theory (DFT) calculations, particularly plane-wave implementations, introduce systematic formation energy errors ranging from tens to hundreds of meV/atom, depending on the selection of exchange-correlation functionals, kinetic energy cutoffs, pseudopotentials, and dispersion corrections. As demonstrated by the MatPES dataset, identical structures can exhibit an average energy discrepancy of 107 meV/atom between PBE and r2SCAN calculations. Such method-dependent ...
  </details>

- **2026-07-27** — Tapan Parikh — [Tag Questions and the Generational Reversal of Sycophancy Across 45 Language Models](http://arxiv.org/abs/2607.23976v1)
  <details><summary>📄 Abstract</summary>
  Appending a two-word confirmation tag to a decision question -- "Is X the better choice?" versus "X is the better choice, right?" -- changes whether a language model endorses the choice. We measure this tag effect on 20 frozen, ground-truth-free decisions between two defensible options, counterbalanced so a model's own preferences cancel, scored by exact match on clamped yes/no replies -- no LLM judge, no embeddings. Across 45 models the effect spans +32% to -32% -- a 64-point swing on one word ...
  </details>

- **2026-07-27** — Yu Li, Wengan He, Wenhui Xu et al. — [Color Fundus Photography Analysis: Co-evolution of Data, Preprocessing, and Modeling toward Multimodal AI](http://arxiv.org/abs/2607.23972v1)
  <details><summary>📄 Abstract</summary>
  Color Fundus Photography (CFP) is a primary non-invasive imaging modality for large-scale screening of ophthalmic and systemic diseases. Existing surveys mainly summarize task-specific algorithms, datasets, or preprocessing techniques independently, lacking a unified perspective on their co-evolution with modern artificial intelligence. This review provides an integrated overview of CFP AI through the interplay of dataset evolution, preprocessing paradigms, and modeling frameworks. We show that ...
  </details>

- **2026-07-27** — Keyu Li, Jin Gao, Jialing Zhang et al. — [LU-500: A Logo Benchmark for Concept Unlearning](http://arxiv.org/abs/2607.24101v1)
  <details><summary>📄 Abstract</summary>
  Concept unlearning is increasingly used to limit the reproduction of protected or unsafe visual concepts in text-to-image models. Existing evaluations, however, mostly study targets that dominate the whole image, such as styles, broad object categories, or portrait-like identities, leaving company logos comparatively underexamined. Logos create a different failure mode: a small localized mark can carry the entire protected concept, must be visually precise to remain recognizable, and can be trig...
  </details>

- **2026-07-27** — Xueping Gao, Jianwei Yang, Qiang Yang — [Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair](http://arxiv.org/abs/2607.24604v1)
  <details><summary>📄 Abstract</summary>
  Generate--test--revise loops are common in coding agents, but repetition alone provides no reliability guarantee. We study the gap between finding a correct patch and retaining, verifying, and submitting it. A sealed five-seed study over 30 HumanEval repairs produces 900 three-revision trajectories. Under forced revision, current correctness with current traces falls from 0.820 after one revision to 0.673 after two, although ever-correct rises to 0.847. Two common-state studies use 2,430 branche...
  </details>

- **2026-07-27** — Ioannis Sarridis, Ioannis Kompatsiaris, Symeon Papadopoulos — [Face Age Verification Vulnerabilities Under Simple Appearance Manipulations](http://arxiv.org/abs/2607.24194v1)
  <details><summary>📄 Abstract</summary>
  Online platforms increasingly rely on automated age estimation systems to enforce minimum-age policies. Focusing on vision-based models designed for this task, concerns arise regarding their robustness to simple appearance changes that underage individuals may use to bypass such systems, such as drawing a mustache or applying lipstick. In this work, we present a systematic study of age verification robustness by simulating visual alterations that can be easily achieved by underage individuals. W...
  </details>

- **2026-07-27** — Khadija Rais, Abdelmadjid Benmachiche, Imene Soualmia — [Hybrid Artificial Potential Fields and Spatio-Temporal Transformers for Real-Time AUV Path Planning](http://arxiv.org/abs/2607.25056v1)
  <details><summary>📄 Abstract</summary>
  Autonomous Underwater Vehicles (AUVs) operate in complex, unstructured environments where efficient and safe path planning is critical for mission success and energy conservation. This paper presents a comprehensive comparative evaluation of thirteen path planning algorithms, ranging from classical graph-search methods (A*, Dijkstra) and sampling-based approaches (RRT*) to metaheuristics (PSO, GA, ACO, BCO) and learning-based architectures. Special emphasis is placed on a proposed hybrid approac...
  </details>

- **2026-07-27** — Hamid El Bahja, Jan C. Riedel, Peter Jung — [A Hybrid Physics-Informed Neural Network Framework for Subcritical and Supercritical Dynamics in Multi-Species Chemotaxis](http://arxiv.org/abs/2607.24949v1)
  <details><summary>📄 Abstract</summary>
  We study a two-species chemotaxis system that exhibits two qualitatively different regimes: subcritical dynamics, in which solutions remain smooth, and supercritical dynamics, in which strong aggregation may lead to finite-time blow-up. In the subcritical regime, we use a standard continuous-time physics-informed neural network (PINN) with alternating training for the coupled fields and show that it provides accurate and efficient approximations. In the supercritical regime, however, this formul...
  </details>

- **2026-07-27** — Jinjie Mai, Gordon Guocheng Qian, Willi Menapace et al. — [EgoPlay: Event-Triggered Video Editing for Egocentric Streams](http://arxiv.org/abs/2607.24560v1)
  <details><summary>📄 Abstract</summary>
  We introduce EgoPlay, an event-triggered video-to-video editor for egocentric streams, obtained by fine-tuning a pretrained V2V diffusion transformer on event-conditioned data built primarily from Ego4D. Given a monocular video and an event-triggered prompt of the form "when X happens, do Y," EgoPlay infers whether and when event X occurs, preserves pre-event frames, and applies edit Y only to the post-event continuation. Rather than cascading a separate event detector with an editor, EgoPlay le...
  </details>

- **2026-07-27** — Fangyijie Wang, Tanya Akumu, Zi Ye et al. — [Efficient Ultrasound Image Segmentation with Token-Conditioned Neural Cellular Automata](http://arxiv.org/abs/2607.24529v1)
  <details><summary>📄 Abstract</summary>
  Point-of-Care Ultrasound (POCUS) plays an important role in bedside diagnosis and clinical decision-making, particularly in resource-constrained settings. Recent deep learning methods have substantially improved ultrasound image segmentation, enabling accurate diagnosis and biometric estimation. However, their computational cost limits deployment on portable and low-resource devices. To address this challenge, we propose LiteAdaNCA-Net (LANCANet), a lightweight ultrasound segmentation framework ...
  </details>

- **2026-07-27** — Xiangbo Zhang, Xiaoxu Ma — [Grounding latent algorithm routing in transformer reasoning](http://arxiv.org/abs/2607.24471v1)
  <details><summary>📄 Abstract</summary>
  A central question in the in-context learning literature is whether transformers can organize episode-level adaptation around different inductive-bias families. We study this question in a controlled setting through latent algorithm routing: route-like behavior in which the solver-family preference changes with the latent data-generating regime while prompt form is held fixed, remains stable under nuisance perturbations, and is selectively influenced by targeted activation interventions without ...
  </details>

- **2026-07-27** — Dariusz Nowak-Nova — [Retrieval-Augmented Large Language Models as Components of Cognitive Computing architecture for Regulatory Knowledge Management](http://arxiv.org/abs/2607.24352v1)
  <details><summary>📄 Abstract</summary>
  The aim of this article is to verify whether integrating large language models (LLMs) with the Retrieval-Augmented Generation (RAG) architecture enables their transformation from standalone generative models into components of cognitive computing infrastructure with enhanced epistemic reliability. The study proposes an architectural approach based on locally deployed LLMs operating in on-premises environments without high-end GPU accelerators and examines their applicability in supporting regula...
  </details>

- **2026-07-27** — Zefan Qu, Zhenwei Wang, Gerhard Petrus Hancke et al. — [UMI3D: Robust 3D Generation on Unconstrained Multi-Image Inputs via Simultaneous Focus Cross-Attention Routing](http://arxiv.org/abs/2607.24298v1)
  <details><summary>📄 Abstract</summary>
  Recent 3D foundation models can generate high-quality assets from a single image, but degrade markedly on unconstrained multi-image inputs, often producing distorted geometry, over-smoothed textures, and chaotic colors. We argue that this failure stems not from limited model capacity, but from a mismatch between single-image cross-attention and the multi-image setting: existing models lack a principled way to decide which image each 3D voxel should trust at each denoising step. Revisiting recent...
  </details>

- **2026-07-27** — Wenbin Wang, Xiaotong Luo, Yuan Gao et al. — [RPG-VST: Robust Poisson-Gaussian Variance Stabilization for Blind RAW Denoising](http://arxiv.org/abs/2607.24291v1)
  <details><summary>📄 Abstract</summary>
  Variance stabilization with the generalized Anscombe transform (GAT) enables frozen Gaussian denoisers to process Poisson--Gaussian (PG) RAW noise, but its reliability depends on fitted shot/read-noise parameters. In blind single-image deployment, these parameters are estimated from low-texture RAW statistics that are often corrupted by residual texture, clipping, defective pixels, and read-noise floors. Such contamination yields heavy-tailed log-variance residuals, making ordinary least-squares...
  </details>

- **2026-07-27** — Thomas Monks, Alison Harper, Amy Heather et al. — [Generative Artificial Intelligence (GenAI) to convert images of queuing networks into verifiable simulation models: an open-weight LLM workflow approach](http://arxiv.org/abs/2607.24259v1)
  <details><summary>📄 Abstract</summary>
  Recent work has explored the use of Large Language Models (LLMs) to automate simulation model building, typically by generating executable code directly from natural language descriptions. However, this raises challenges for verification and reproducibility particularly for users without programming expertise. We propose Sketch2DES, a sketch-to-simulation workflow that converts diagrammatic representations of queuing networks into verifiable discrete-event simulation models using open-weight LLM...
  </details>

- **2026-07-27** — Guangyi Liu, Huan Zhao, Quanming Yao — [Falsifiable Commitment Planning for Self-Correcting Web Agents](http://arxiv.org/abs/2607.24167v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon web agents often go off track before final failure: a trajectory can remain locally plausible even after the current state, reused skill, or plan assumption no longer supports the user instruction. Existing agents can plan, reflect, or reuse experience, but their plans rarely specify the evidence under which an active step should still be trusted. We propose FCPAgent, a falsifiable commitment planning framework for robust long-horizon web agents. FCPAgent represents each plan step a...
  </details>

- **2026-07-27** — Ahmad Dkhan, Yazan Dayoub, Jana El Haj et al. — [Hierarchical THz Near-Field Localization with Subarray Processing and Covariance Correction](http://arxiv.org/abs/2607.24149v1)
  <details><summary>📄 Abstract</summary>
  Terahertz (THz)-band near-field (NF) localization offers high spatial resolution due to short wavelengths and distance-dependent wavefront curvature in NF multi-antenna systems. However, large arrays and dense deployments, necessary to mitigate THz path loss, raise the received signal dimensionality, creating computational overhead for localization. Furthermore, traditional two-dimensional (2D) subspace algorithms suffer from excessive complexity and poor robustness under coherent sources. This ...
  </details>

- **2026-07-27** — Ali Zahid Raja — [Grading the Narrators: An Isnad-Rijal Framework for Claim-Level Provenance in Multi-Agent Knowledge Systems](http://arxiv.org/abs/2607.24117v1)
  <details><summary>📄 Abstract</summary>
  Modern multi-agent knowledge systems increasingly accumulate knowledge through chains of autonomous transformations rather than direct retrieval. Existing provenance work records what happened - execution traces, tool calls, evidence links - and source-reliability estimation is long established (truth discovery, reputation systems). What is missing is an operational framework that attaches graded, per-domain transmitter reliability to claim-level transmission chains, with completeness semantics,...
  </details>

- **2026-07-27** — Xun Zhou, Zhen Dong, Mingyu Ren et al. — [RESTOR: Automated Test Oracle Generation for RESTful APIs via Reinforcement Learning](http://arxiv.org/abs/2607.23963v1)
  <details><summary>📄 Abstract</summary>
  Modern REST API testing faces a critical challenge in defining reliable test oracles, particularly in agile industrial environments where formal specifications (e.g., OpenAPI) are frequently missing or outdated, and historical execution logs are unavailable for newly deployed endpoints. In this paper, we present Restor (Reinforcement Enhanced Single-Traffic Oracle generator for REST APIs), a framework that generates executable test assertions from a single observed request-response pair in a bla...
  </details>

- **2026-07-27** — Bajian Xiang, Cheng Wen, Han Zhao et al. — [Qwen-Audio-3.0-TTS: Freely Controllable and Highly Robust Speech Synthesis with Multi-Stage Training Paradigm](http://arxiv.org/abs/2607.23938v1)
  <details><summary>📄 Abstract</summary>
  In this report, we present Qwen-Audio-3.0-TTS, a production-oriented speech synthesis system that jointly advances content consistency, speaker similarity, prosodic naturalness, audio quality, controllability, multilingual coverage, efficiency, and robustness. It combines a 12.5~Hz low-frame-rate speech tokenizer for reduced inference latency with a five-stage progressive training paradigm for coordinated language model (LM) and flow-matching model (FM) optimization. The model provides productio...
  </details>

- **2026-07-27** — Goodarz Mehr, Sepideh Gohari, Montasir Abbas et al. — [SimBEV2X: A Large-Scale Dataset and Data Generation Tool for Multi-Task Vehicle-to-Everything Cooperative Perception](http://arxiv.org/abs/2607.23910v1)
  <details><summary>📄 Abstract</summary>
  Cooperative perception through vehicle-to-everything (V2X) communication can overcome the inherent physical limitations of individual autonomous vehicles, such as occlusions and limited sensor range. However, the development of robust V2X algorithms, particularly those relying on unified spatial representations like bird's-eye view (BEV) representation, is hampered by the lack of large-scale, multi-modal, multi-task datasets. Moreover, collecting and annotating a large set of synchronized, real-...
  </details>

- **2026-07-27** — Nicolas Romeo, David B. Brückner, Noah P. Mitchell — [Growth and remodeling control shape memory in morphogenetic rods](http://arxiv.org/abs/2607.23907v1)
  <details><summary>📄 Abstract</summary>
  Mechanical instabilities provide a general design principle for shaping developing organs and engineering soft materials. However, in slender structures, simple elastic buckling tends to erase rather than preserve shape complexity: structures relax to the simplest possible shape, erasing finer detail. Living systems nonetheless build complex, reproducible morphologies from continually remodeling material, while remaining robust to noise arising across scales. Using analytical theory and numerica...
  </details>

- **2026-07-26** — Shuyu Chen, Chen Zhu, Ye Zhang et al. — [SCTA: An Agentic Framework for Stable and Interpretable Target Gene Discovery from Single-Cell RNA Sequencing](http://arxiv.org/abs/2607.23821v1)
  <details><summary>📄 Abstract</summary>
  Identifying therapeutic target genes from single-cell RNA sequencing (scRNA-seq) data remains a fundamental challenge in translational biology. Unlike bulk assays, scRNA-seq captures heterogeneous cellular states and rare subpopulations, but this same heterogeneity makes target discovery highly sensitive to analytical choices throughout the pipeline, including preprocessing, cell population selection, differential expression analysis, and downstream biological interpretation. As a result, existi...
  </details>

- **2026-07-26** — Daphne Chen, Archit Ritesh Jain, Eric Goossen et al. — [A Few Words Go a Long Way: Language Guided Robot Policy Synthesis](http://arxiv.org/abs/2607.23784v1)
  <details><summary>📄 Abstract</summary>
  While vision-language-action models have demonstrated impressive zero-shot manipulation capabilities, they remain fundamentally black box policies that are difficult to interpret, adapt, or correct when they inevitably fail. In this work, we propose ARCHITECT, a framework that treats robot policy acquisition as an interactive program synthesis task. ARCHITECT leverages the reasoning capabilities of LLM coding agents to synthesize modular robot programs that utilize a suite of perception and cont...
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

- **2026-07-14** — Rwik Rana, Jesse Quattrociocchi, Christian Ellis et al. — [Adapting Generalist Vehicle Models for High-Speed MPC Across Terrains](http://arxiv.org/abs/2607.13319v1)
  <details><summary>📄 Abstract</summary>
  High-speed off-road autonomy requires precise closed-loop control for a target vehicle while remaining robust across changing terrains. Recent forward kinodynamic (FKD) prediction foundation models suggest a promising path, starting from a generalist model and specializing it to the target platform. However, effective specialization remains challenging, as it often requires substantial real-world data, and models adapted to one setting can still overfit to specific terrains or driving regimes. W...
  </details>

- **2026-07-14** — Bidyarthi Paul, Nahida Jannat Mayouree, Md. Asif Karim et al. — [GSM-Plus-BN: A Perturbation-Based Benchmark for Bangla Mathematical Reasoning in Large Language Models](http://arxiv.org/abs/2607.13248v1)
  <details><summary>📄 Abstract</summary>
  The evaluation of mathematical reasoning in large language models (LLMs) has predominantly focused on high-resource languages like English. This has created a significant barrier to the equitable development and deployment of AI in linguistically diverse regions such as Bangladesh, where over 230 million people speak Bengali. Despite this global significance, there has been minimal prior work on mathematical reasoning in Bengali and no existing research that systematically benchmarks a perturbat...
  </details>

- **2026-07-14** — Zhouchonghao Wu, Akshay Rangesh, Weixin Li et al. — [TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale](http://arxiv.org/abs/2607.13028v1)
  <details><summary>📄 Abstract</summary>
  Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation on the CPU and policy inference on the GPU over a zero-copy path, sustaining 1.3M agent-steps per se...
  </details>

- **2026-07-14** — Zhao Yang, Yinan Shi, Mingyuan Yao et al. — [ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning](http://arxiv.org/abs/2607.12992v1)
  <details><summary>📄 Abstract</summary>
  Vision-language action (VLA) models increasingly adopt chunked action heads to satisfy real-time constraints; however, this introduces boundary jitter: overlapping regions between consecutive chunks often yield inconsistent predictions, degrading temporal coherence and the task success rate. Existing methods, such as inference-time blending, merely reweight mismatched proposals without correcting underlying errors, leading to residual accumulation under biased or noisy histories. We propose Chun...
  </details>

- **2026-07-14** — Yanzhe Zhang, Sanmi Koyejo, Diyi Yang — [The Illusion of Robustness: Aggregate Accuracy Hides Prediction Flips under Task-Irrelevant Context](http://arxiv.org/abs/2607.12963v2)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) grow more capable, they are increasingly deployed in context-rich settings where task inputs are often accompanied by long, partially irrelevant context. In a controlled setting, we find that state-of-the-art models often appear robust to task-irrelevant context at the aggregate level: prepending it to benchmark questions causes little change in overall accuracy. This aggregate stability, however, masks significant per-example instability. Even semantically meanin...
  </details>

- **2026-07-14** — Yilun Kong, Yunpeng Qing, Guozheng Ma et al. — [ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning](http://arxiv.org/abs/2607.12931v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models on complex manipulation tasks. However, its practical scalability remains severely limited by the substantial cost of environmental interactions. In this work, we first investigate the exploration stagnation bottleneck in current VLA-RL frameworks and reveal that trajectory diversity is fundamentally more important to sample efficiency than the sheer quantity of collected rollouts...
  </details>

- **2026-07-14** — Xixuan Hao, Zeyu Zhang, Zehao Lin et al. — [MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations](http://arxiv.org/abs/2607.12893v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions. Existing benchmarks, however, evaluate such memory almost exclusively through downstream question answering, scoring only the correctness of a final answer. This black-box formulation conflates the heterogeneous causes of memory failure, such as missing the introduction of a relevant fact, binding an operation to the wrong target, or relying on stale values...
  </details>

- **2026-07-14** — Peter R. D. van der Wal, Nicola Strisciuglio, George Azzopardi — [Inhibited Self-Attention: Sharpening Focus in Vision Transformers](http://arxiv.org/abs/2607.12881v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) have demonstrated remarkable performance in computer vision tasks. However, their self-attention mechanism often diffuses focus across background regions, relying on spurious correlations rather than object-relevant cues. Inspired by inhibitory mechanisms observed in biological vision systems, we propose the Inhibited Self-Attention (ISA), a novel self-attention that integrates inhibitory signals to enhance feature selectivity and suppress spurious responses. In contra...
  </details>

- **2026-07-14** — Takumi Shioda, Kohei Terashima, Tatsuo Nagai — [Verifier-Based Reinforcement Fine-Tuning of Reasoning Models for Thermal Energy Storage Control](http://arxiv.org/abs/2607.12856v1)
  <details><summary>📄 Abstract</summary>
  Buildings are expected to shift cooling loads in response to grid conditions. Thermal energy storage (TES) enables this shift, but scheduling it well requires planning hours ahead under storage constraints. Model predictive control (MPC) and reinforcement learning are difficult to scale across buildings. This study instead adapts an open-weight reasoning model through reinforcement learning with verifiable rewards (RLVR). We convert exact offline dynamic-programming (DP) action values into dense...
  </details>

- **2026-07-14** — Tapan Parikh — [The One-Word Census: Answer-Choice Conformity Across 44 Language Models](http://arxiv.org/abs/2607.12796v1)
  <details><summary>📄 Abstract</summary>
  When a language model must pick one answer from a large space of equally valid options, which does it pick -- and how often is it the same answer every other model picks? Asked to "pick a word -- any word," 44 models chose "serendipity" 41% of the time. We characterize this convergence with a deliberately minimal instrument: 31 single-turn prompts, each naming a category with many valid one-word answers ("Name a tree."), asked four times per model with no system prompt. Analysis is exact-match o...
  </details>

- **2026-07-14** — Samuel Yeh, Yiwen Zhu, Shaleen Deep et al. — [Tracing Agentic Failure from the Flow of Success](http://arxiv.org/abs/2607.12747v1)
  <details><summary>📄 Abstract</summary>
  Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debugging and improving these systems. Existing approaches either rely on prompting-based pipelines, which are computationally expensive, or require post-training on failure trajectories with step-level error annotations, which are costly to collect and difficult to scale. We argue that a practical failure attribution model should be lightweight and tr...
  </details>

- **2026-07-14** — Sarah Al-Shareeda, Gulcihan Ozdemir, Heung Seok Jeon — [Learning-based Probabilistic Load Forecasting with Post-hoc and In-model Uncertainty](http://arxiv.org/abs/2607.12730v1)
  <details><summary>📄 Abstract</summary>
  Smart-building load forecasters are often trained offline on dense, multivariate, high-frequency data, but deployment may provide only hourly, feature-limited inputs. Missing features must then be reconstructed, and their errors can propagate through the model. If this input uncertainty is not reflected, prediction intervals may become miscalibrated, affecting demand-response scheduling. Our work examines where uncertainty should be placed once inference inputs are reconstructed. We develop a un...
  </details>

- **2026-07-14** — Jiho Hong, Eunae Kang, Sanghyun Kim et al. — [Instance-Enriched Semantic Maps for Visual Language Navigation](http://arxiv.org/abs/2607.12630v1)
  <details><summary>📄 Abstract</summary>
  Visual Language Navigation (VLN) aims to enable an embodied agent to navigate complex environments by following natural language instructions. Recent approaches build semantic spatial maps and leverage Large Language Models (LLMs) for reasoning and decision making. Despite these advances, existing systems lack instance-level object detail and robustness to diverse user queries, limiting reliable navigation in complex indoor environments. To address these limitations, we propose Instance-Enriched...
  </details>

- **2026-07-14** — Rui Zheng, Changwen Li, Yi Ji et al. — [Hierarchical Fault Localization for Autonomous Driving Systems with Hypothesis Validation and Intent Analysis](http://arxiv.org/abs/2607.12598v1)
  <details><summary>📄 Abstract</summary>
  Comprehensive testing is essential for the safety and reliability of Autonomous Driving Systems (ADS). Existing techniques can detect system-level failures or attribute them to coarse-grained modules, but they often fall short of localizing the root cause in source code. As a result, debugging remains labor-intensive, requiring developers to connect behavioral violations with complex implementation logic. To address this gap, we present HINT, a two-phase framework for hierarchical ADS fault loca...
  </details>

- **2026-07-14** — Cheng-You Ho, Justin Luo, Henry Ng et al. — [Clifford-Only Quantum Reed-Solomon Codes and a Tornado Concatenation for Biased-Noise Cat Qubits](http://arxiv.org/abs/2607.13105v1)
  <details><summary>📄 Abstract</summary>
  Dissipative cat qubits exponentially suppress one Pauli error channel with the mean photon number, leaving the conjugate bit-flip error as the dominant failure mode. This strong noise bias makes the full machinery of general quantum error correction unnecessary: a code need only protect against a single error type, and any classical linear code can be promoted to a Clifford stabilizer code that does exactly this. We use this observation to build a Clifford-only quantum Reed-Solomon (RS) code. St...
  </details>

- **2026-07-14** — Rongxin Gao, Yuzhi Huang, Dongxuan Liu et al. — [DynTrace: Tracking Dynamic Object Evidence for 4D Spatio-Temporal Reasoning in MLLMs](http://arxiv.org/abs/2607.12503v2)
  <details><summary>📄 Abstract</summary>
  4D spatio-temporal reasoning, jointly modeling 3D spatial structure and temporal evolution, is essential for understanding dynamic worlds and enabling embodied interaction. While current Multimodal Large Language Models (MLLMs) show strong capabilities in static scene understanding and coarse-grained 4D tasks, they still have notable limitations in continuous dynamic scene perception, especially in tracking dynamic object evidence for coherent 4D spatio-temporal reasoning. This shortcoming stems...
  </details>

- **2026-07-14** — Jeeyung Kim, Erfan Esmaeili, Qiang Qiu — [Steering Diffusion Models via Class-Contrastive Influence for Few-Shot Medical Classification](http://arxiv.org/abs/2607.12464v1)
  <details><summary>📄 Abstract</summary>
  When labeled data are scarce, off-the-shelf diffusion models can augment training sets for few-shot medical image classification, but not all generated samples are equally useful for the downstream task. Existing approaches largely improve synthetic data by increasing realism, diversity, or domain adaptation, while overlooking a more fundamental question: how should sample usefulness for classification be measured and optimized? We address this with Class-Contrastive Influence (C2I), a criterion...
  </details>

- **2026-07-14** — Jie Mao, Changlun Li, Xiang Li et al. — [EVOQUANT: Self-Evolving Verifier-Guided Strategy Optimization for Robust Quantitative Trading](http://arxiv.org/abs/2607.12455v1)
  <details><summary>📄 Abstract</summary>
  Quantitative strategy optimization remains largely manual, requiring domain experts to identify weak signals, tune risk-control rules, and repeatedly validate iterative revisions. Large language models can accelerate this process, but directly relying on them to rewrite trading strategies often introduces hallucinated edits, strategy drift, and backtest overfitting. We propose EVOQUANT, a self-Evolving Verifier-guided framework for strategy Optimization in Quantitative trading. Our method utiliz...
  </details>

- **2026-07-14** — Timing Yang, Jinrui Yang, Xinlong Li et al. — [Let RGB Be the Language of Vision](http://arxiv.org/abs/2607.12450v1)
  <details><summary>📄 Abstract</summary>
  This work introduces a unified formulation for vision models, where diverse forms of visual information beyond natural images, such as masks, depth maps, and other structured visual signals, are all represented as RGB images, while general visual tasks can be converted into a common RGB-to-RGB image editing problem. In this paradigm, different types of visual information internally share the same encoding and decoding architecture and parameters as natural images, enabling a single model to tran...
  </details>

- **2026-07-14** — Arash Nikzad, Sasan Sarbishegi, Ali Dasmeh et al. — [Differentiable Clone-Structured Causal Graphs for End-to-End Cognitive Map Learning from Image Sequences](http://arxiv.org/abs/2607.12382v1)
  <details><summary>📄 Abstract</summary>
  How can an agent build a structured map of its world from nothing but an ongoing sequence of raw sensory input and its own movements, especially when natural variation means exact sensory patterns rarely repeat? The Clone-Structured Causal Graph algorithm (CSCG), a normative hippocampus model, shows how an interpretable map can be learned from aliased observations. However, CSCG requires a predefined discrete alphabet, and its expectation-maximization formulation is not easily combined with exis...
  </details>

- **2026-07-14** — Hung-Chieh Wu, Xiaopan Zhang, Kasra Sinaei et al. — [StratMamba: Strategic and Reactive Stream Partitioning for Path-Efficient LiDAR-Based Obstacle Avoidance](http://arxiv.org/abs/2607.12370v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes StratMamba, a dual-stream Mamba-based temporal modeling architecture, to more efficiently capture long-horizon temporal dependencies required for robot navigation in complex and obstacle-rich environments. StratMamba leverages a combination of fast-decay and slow-decay memory architectures, where the fast-decay component processes high-frequency LiDAR data for reactive obstacle avoidance, while the slow-decay component maintains longer-horizon goal information for strategic p...
  </details>

- **2026-07-14** — Xinyue Xu, Zheng Zhang, Kunyang Ma et al. — [DM-KG: A Novel Method for Boosting Spatial Cognition of Vision-Language Models in Street View Imagery](http://arxiv.org/abs/2607.12319v1)
  <details><summary>📄 Abstract</summary>
  As vision-language models (VLMs) are increasingly deployed in geospatial question answering and visual scene understanding, improving their spatial cognition capability on street view imagery for complex logical reasoning has emerged as a key research priority. However, existing VLMs frequently suffer from "spatial semantic hallucinations" when perceiving object locations, distances, and directions in real-world street view scenes. Furthermore, such errors are often recalcitrant to tracing and c...
  </details>

- **2026-07-14** — Michael Solodko, Steven Gong, Guangwei Yu et al. — [LakeQuest: A Three-Domain Benchmark for Grounded Question Answering across Data Lakes](http://arxiv.org/abs/2607.12310v1)
  <details><summary>📄 Abstract</summary>
  While modern question answering (QA) systems excel on clean, schema-aligned corpora, real-world knowledge is rarely so neatly packaged. Answering questions over enterprise and scientific data lakes requires systems to navigate heterogeneous, weakly structured collections of tables, passages, and linked metadata. Current benchmarks abstract away this noisy discovery process, failing to evaluate end-to-end performance. To bridge this gap, we introduce LakeQuest, a human-validated benchmark of 9,84...
  </details>

- **2026-07-14** — Muhammad Ashad Kabir, Sirajam Munira — [From Many to Meaningful: Feature-Guided Zero-Shot Chronic Kidney Disease Screening Using Large Language Models](http://arxiv.org/abs/2607.12260v1)
  <details><summary>📄 Abstract</summary>
  Early screening of chronic kidney disease (CKD) is essential for preventing irreversible progression; however, many machine learning (ML)-based screening methods remain difficult to deploy in community and resource-limited screening settings due to their reliance on large labeled datasets, resource-intensive pathology tests, or high-dimensional clinical features, and limited robustness to population and distributional shifts. This study examines the feasibility of using large language models (LL...
  </details>

- **2026-07-14** — Vinay Kumar Chaganti — [On-Device Deep Research at 4B: Exposure Bounds Faithfulness, Retrieval Bounds Coverage](http://arxiv.org/abs/2607.12257v1)
  <details><summary>📄 Abstract</summary>
  On-device research agents search a corpus, read sources, and write a cited brief on a personal laptop. Whether their citations are faithful, and at what cost, is unmeasured for a deployable small model. This study fixes one 4B generator on a 24 GB laptop and asks what makes its citations faithful. It separates two quantities usually reported as one number. Cited claim faithfulness asks whether the cited source supports the claim. Trustworthy coverage asks whether the agent also cites the right s...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 20 papers

- **2026-07-28** — Genliang Zhu, Chu Wang — [Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales](http://arxiv.org/abs/2607.25364v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents expose structured calls but commonly attach free-form rationales. Such rationales are neither authorization nor reliable introspection. We present Explanation-Bound Tool Execution (EBTE), a claim-carrying mediation layer that converts decision-relevant rationale content into typed action claims and checks them against server-held intent, policy, payload, tool, risk, provenance, and freshness facts. EBTE cannot widen baseline authority: conflicts deny, incomplete or uncertain cl...
  </details>

- **2026-07-28** — Ziheng Zhou, Huiyu Luo, Xiaohu Zhu et al. — [AMPBench-MT: A Homology-Controlled Benchmark for Antimicrobial Peptide Potency, Spectrum, and Safety Prediction](http://arxiv.org/abs/2607.25518v1)
  <details><summary>📄 Abstract</summary>
  Computational AMP discovery is often evaluated through AMP/non-AMP recognition, yet follow-up decisions depend on assay-derived evidence such as target-species potency, hemolysis, toxicity, and selectivity. Existing AMP and peptide benchmarks cover binary recognition, multilabel annotation, assay regression, or broader peptide-model comparison, but they do not jointly place AMP recognition, species-conditioned potency, spectrum, safety-facing proxy endpoints, and cross-endpoint behavior within o...
  </details>

- **2026-07-28** — Florian Krebs — [F(AI)2R: Who Did What, and Who Checked? Verifiable AI Provenance as an Executable Skill](http://arxiv.org/abs/2607.25637v1)
  <details><summary>📄 Abstract</summary>
  F(AI)2R is FAIR research with AI in the loop, twice: an AI-assisted authoring pass and a machine-readable audit pass over every artefact. AI systems now draft, refactor, and verify research artefacts, yet their contributions are rarely recorded in a form a later human or machine can audit. Building on the original F(AI)2R experiment, we generalize its provenance model beyond scholarly writing into aiprov, a PROV-O extension covering any AI-in-the-loop artefact, and we package the method as an ex...
  </details>

- **2026-07-28** — Mateusz Kozłowski — [Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact](http://arxiv.org/abs/2607.25589v1)
  <details><summary>📄 Abstract</summary>
  Medical-imaging AI benchmarks combine datasets, DICOM rendering, prompts, provider APIs, automated labels, statistical code, manuscripts, and repository releases. Agreement across these artifacts is usually assumed rather than tested. We performed a retrospective forensic reproducibility audit of a preserved chest-radiograph vision-language model (VLM) pilot; no model was called again and no image or report was newly annotated. We traced prompt bindings, DICOM metadata, output completeness, labe...
  </details>

- **2026-07-28** — Sagie Dekel, Omer Madmon, Moshe Tennenholtz et al. — [Learning Dynamics of Strategic Publishers in Generative AI Ecosystems](http://arxiv.org/abs/2607.25514v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) search systems are transforming how users access information. Unlike ranking-based search systems, where users observe a ranked list of documents, GenAI search systems, given a user's question, generate an answer, often accompanied by external sources (e.g., in the form of citations). Content creators (publishers) seeking to increase exposure might behave strategically and compete with other creators for users' attention. While publishers in ranking-based systems might stra...
  </details>

- **2026-07-27** — Stefan G. Creadore — [Plato-Bio: verification-first biological novelty screening with temporal rediscovery and structural benchmarks](http://arxiv.org/abs/2607.23975v1)
  <details><summary>📄 Abstract</summary>
  Large language model research agents can connect literature retrieval, analysis code, and manuscript preparation, but coherent output does not establish scientific validity. We developed Plato-Bio, a biology-routed extension of the open Plato/Denario architecture that couples explicit workflow states with provenance records, citation checks, claim-to-evidence links, scoped file writes, and publication gates. A source audit identified and repaired three defects that could distort evaluation: loss...
  </details>

- **2026-07-27** — Krithi Shailya, Ananya Lakshmi Ravi, Venkatanathan K. V. et al. — [KANEx: Translating Kolmogorov-Arnold Networks' Interpretability to Medical Explainability](http://arxiv.org/abs/2607.24730v1)
  <details><summary>📄 Abstract</summary>
  Computer vision models have become highly effective for medical applications, yet their black-box nature continues to undermine clinician trust. In clinical workflows, chest X-ray classifiers are increasingly paired with Vision-Language Models (VLMs) to generate natural-language explanations. However, these systems add linguistic fluency without addressing the underlying opacity of the visual model. With the emergence of Kolmogorov-Arnold Networks (KANs), whose spline-based components provide in...
  </details>

- **2026-07-27** — Zhichao Yan, Shizhao Li, Jiapu Wang et al. — [CAGE: Cognitive Attribution Graphs for Faithful Inline Citation Generation in Long-Form Question Answering](http://arxiv.org/abs/2607.24236v2)
  <details><summary>📄 Abstract</summary>
  Long-form question answering increasingly relies on retrieved evidence to make LLM outputs verifiable, with inline citations tracing claims to source documents. However, existing systems often attach citations that are topically related but insufficient to support their claims. We identify attribution ambiguity as a structural challenge: end-to-end generation must implicitly resolve combinatorial claim--document assignments, obscuring evidential boundaries and increasing the risk of evidence-bou...
  </details>

- **2026-07-27** — Xiaoyang Li, Yiqi Wang, Haohui Lu et al. — [MemTX: Transactional Belief Commit for Stateful Agent Memory](http://arxiv.org/abs/2607.23929v2)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly coordinate through persistent shared memory: one agent's write becomes another agent's premise, and eventually a tool call with real side effects. Current agent memory systems treat every accepted write as immediately actionable truth, so a polluted tool result, a stale update, or a teammate's half-finished note can silently drive an irreversible action. We argue that a memory write is not a belief commit. We present MemTX, a transactional belief-commit protocol. Each rec...
  </details>

- **2026-07-27** — Qing Li, Zeyu Dong, Yin Cui et al. — [What Can I Edit? Open-Ended Strategy Discovery and the Emotion Editability Landscape](http://arxiv.org/abs/2607.23920v1)
  <details><summary>📄 Abstract</summary>
  Emotional image editing requires more than applying affective filters or modifying predefined visual factors: an effective edit must identify what a particular image can afford for a target emotion. Existing affective image manipulation methods, including recent agentic variants, largely operate within bounded strategy spaces based on predefined factor taxonomies, knowledge libraries, or conventional editing templates, and therefore often miss image-specific, context-grounded strategies. We intr...
  </details>

- **2026-07-27** — Sonia Castelo, Eden Wu, Joao Rulff et al. — [UrbanTrace: LLM-Assisted Discovery and Semantics-Aware Integration of Spatial Data](http://arxiv.org/abs/2607.25124v1)
  <details><summary>📄 Abstract</summary>
  Urban decision-making requires integrating heterogeneous spatial data. While current GIS tools handle geometric computation efficiently, they lack the semantic reasoning to guide complex workflows. Analysts manually manage data discovery, spatial boundaries, and measurement semantics, risking aggregation errors. We present UrbanTrace, a visual analytics system that transforms manual spatial data-wrangling into a transparent, node-based collaborative workflow with context-aware AI agents. Using a...
  </details>

- **2026-07-27** — Zhuchenyang Liu, Yao Zhang, Yu Xiao — [Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels](http://arxiv.org/abs/2607.24651v1)
  <details><summary>📄 Abstract</summary>
  Reliable visual document understanding requires a model to attribute each answer to the evidence regions that support it. Recent benchmarks and systems express this step through a coordinate interface: the model outputs the coordinates of bounding boxes that mark the evidence regions in the document. Under this interface, vision-language models often fail to identify the right regions even when the answer is correct, a failure known as Attribution Hallucination. We present a study that investiga...
  </details>

- **2026-07-27** — Zongyou Yang, Yinghan Hou — [Accuracy Hides How Language Models Fail: Measuring Failure States Under Matched Output Budgets](http://arxiv.org/abs/2607.24268v1)
  <details><summary>📄 Abstract</summary>
  Language-model benchmarks collapse two distinct measurement questions into a single accuracy score: whether a response reached an evaluable state, and whether its answer was judged correct. We introduce a two-layer evaluation framework that separates scorer-independent execution evidence, including termination, answer exposure, parseability, and completion length, from scorer-dependent correctness. Across 2,550 outputs from five fixed Qwen and DeepSeek configurations on MATH and ARC-Challenge, m...
  </details>

- **2026-07-27** — Guiling Guo, Jia Yang, Jiahao Xu et al. — [GraphRareBench: An Auditable Graph-Evidence Benchmark for Phenotype-Driven Rare-Disease Diagnosis](http://arxiv.org/abs/2607.24878v1)
  <details><summary>📄 Abstract</summary>
  Phenotype-driven diagnostic benchmarks usually report the rank of the reference disease, but they rarely reveal which plausible alternatives are ranked above it or what evidence a tool-using model examines before making its decision. We introduce GraphRareBench, a provenance-preserving benchmark containing 2,365 ontology-derived cases and 18,093 target-confounder pairs. Each case includes a coarsened HPO query, a fixed candidate pool, graph-defined hard confounders, and source-linked evidence re...
  </details>

- **2026-07-26** — Quoc-Huy Trinh, Lin Zhu, Sebastian Szyller — [How Context Attribution Handles What the Model Already Knows](http://arxiv.org/abs/2607.23804v1)
  <details><summary>📄 Abstract</summary>
  Context attribution methods for large language models (LLMs) identify which input context contributes to the model response. Recent works show the initial success in attributing the con- tributive score of the contexts. However, we observe that when the context overlaps with the training data, these methods can- not disentangle in-context from in-weight (IW) contributions, producing unreliable scores. Based on this observation, in this work, we introduce: 1) an evaluation protocol that relies on...
  </details>

- **2026-07-15** — Hyunkyung Han, Min Jung Kim — [Anatomically Faithful but Temporally Blind: Auditing Attribution for Left-Ventricular Ejection-Fraction Estimation from Echocardiography](http://arxiv.org/abs/2607.13738v1)
  <details><summary>📄 Abstract</summary>
  Background and Objective: Deep video models estimate left-ventricular ejection fraction (EF) from echocardiography with near-expert accuracy, and post-hoc attribution (Chefer relevance for transformers, Grad-CAM for CNNs) is increasingly used to certify that models "look at the right place." Yet whether these explanations are faithful both spatially and temporally is unaudited. Because EF is defined by the end-systolic (ES) and end-diastolic (ED) frames, a faithful explanation must localize the ...
  </details>

- **2026-07-14** — Binwen Liu, Yilin Ren — [Epistemic Stance Flexibility Probing: Measuring Prompt-Conditioned Register Shift in Large Language Models](http://arxiv.org/abs/2607.12739v1)
  <details><summary>📄 Abstract</summary>
  A language model may be asked either what experts believe about a contested claim or what it believes about the claim itself. A trustworthy conversational agent should distinguish these two requests and respond in different epistemic registers: neutral attribution in the first case and stance expression in the second. Whether such a shift occurs-and whether it occurs coherently-is not directly assessed by existing benchmarks for accuracy, instruction following, or safety. We introduce ESFP, a be...
  </details>

- **2026-07-14** — Igor Santos-Grueiro — [When Binaries Talk Back: Representation-Confusion Attacks on LLM-Assisted Reverse Engineering](http://arxiv.org/abs/2607.12507v1)
  <details><summary>📄 Abstract</summary>
  LLM-assisted reverse-engineering (RE) systems analyze strings, decompiler output, and tool reports derived from ttacker-controlled binaries. A binary can make data look like instructions or records from one origin look like independent evidence. We call such failures Representation-Confusion Attacks in Reverse Engineering (RARE): the pipeline promotes a correctly extracted observation to instruction authority, claim-validating evidence, or trusted analysis state without the authority or support ...
  </details>

- **2026-07-14** — Satwik Bathula, Anand A. Joshi — [Fisher Rank Inflation: A Spectral Signature of Memorization under Label Noise](http://arxiv.org/abs/2607.12438v1)
  <details><summary>📄 Abstract</summary>
  Deep networks trained with label noise often learn clean structure before memorizing corrupted labels. We show that this transition leaves a spectral signature in the centered scatter of per-example last-layer gradients. Its effective rank transiently expands during memorization and contracts after corrupted labels are fit. We call this phenomenon Fisher Rank Inflation. Corrupted labels increase effective rank by injecting spectral mass into low-energy or previously unused eigendirections, incre...
  </details>

- **2026-07-14** — Jixiang Luo — [XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery](http://arxiv.org/abs/2607.12301v1)
  <details><summary>📄 Abstract</summary>
  Autonomous research systems are often evaluated as one-shot paper generators: given a topic, they produce a manuscript and a small set of experiment logs. This framing hides the operational problem that makes such systems difficult to trust: research is long-running, branching, failure-prone, and dependent on auditable handoffs between agents and humans. XScientist is a git-like research protocol and operating system for this setting. It orchestrates idea generation, experiment execution, manusc...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 8 papers

- **2026-07-28** — Podakanti Satyajith Chary, Barath Parthiban, Pranesh Velmurugan et al. — [Knowledge-Guided Multimodal Reasoning over Interacting Streams for Video-Level Ambivalence and Hesitancy Recognition](http://arxiv.org/abs/2607.25961v1)
  <details><summary>📄 Abstract</summary>
  Ambivalence and hesitancy (A/H) are conflicting affective states that precede the delay or abandonment of health behaviour change. Recognition of A/H at the video level is difficult, since the signal arises from disagreement across and within facial, vocal, linguistic, and bodily modalities, and manifests differently across individuals. The proposed PRISM-AH (Predictive Reasoning over Interacting Streams for Multimodal Ambivalence/Hesitancy Recognition), is a framework that treats A/H as a multi...
  </details>

- **2026-07-27** — Zichao Lin, Yifeng Xie, Bowen Qu et al. — [PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models](http://arxiv.org/abs/2607.24957v1)
  <details><summary>📄 Abstract</summary>
  We introduce PerceptionBench, a benchmark specifically designed to evaluate the atomic visual perception capabilities of Multimodal Large Language Models (MLLMs). Existing benchmarks often fail to isolate perception: holistic evaluations conflate perceptual errors with failures in reasoning or domain knowledge, while application-driven benchmarks only cover narrow, fragmented domains shaped by heuristic designs. To address these limitations, PerceptionBench adopts a bottom-up approach: by diagno...
  </details>

- **2026-07-27** — Atharva Pandey, Gautam Jajoo — [Reason-Mediated Behavioral Models for Auditing LLM Social Simulators](http://arxiv.org/abs/2607.24649v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as social simulators, including as synthetic survey respondents. Most evaluations ask whether simulated outcomes resemble human outcomes. We argue that this is necessary but too weak: a simulator can match the final answer while using the wrong rationale-derived reason pattern. We study this problem through a 94-person sunscreen concept test in which each respondent evaluated three product concepts and wrote open-ended rationales. We map those rational...
  </details>

- **2026-07-27** — Yuze Sun, Zhongjie Duan, Yingda Chen — [TreeAdapter: Hierarchical Taxonomy-Guided Adapter Composition for Fine-Grained Species Image Generation](http://arxiv.org/abs/2607.24215v1)
  <details><summary>📄 Abstract</summary>
  Although general text-to-image models excel in open-domain generation, their performance degrades significantly in specialized downstream domains, particularly when generating images of rare biological species. Hindered by long-tailed distributions, general models struggle to capture subtle fine-grained details, while per-species fine-tuning methods over-isolate individual species and consequently ignore the shared visual features among closely related taxa. To address this, we propose TreeAdapt...
  </details>

- **2026-07-27** — David Soldani, Petrit Nahi, Awn Muhammad et al. — [6G: From Connectivity Infrastructure to Guaranteed Digital Services](http://arxiv.org/abs/2607.24185v2)
  <details><summary>📄 Abstract</summary>
  Sixth-generation mobile networks are approaching a structural inflection point. Five generations of vendor-led architecture have left operators dependent on platforms they cannot fully modify and artificial-intelligence inference layers they cannot audit. This article argues that 6G should reverse that trajectory by reordering five priorities: control first; customer outcomes before peak rates; business guarantees before megabytes; software-driven operations with governed agentic artificial inte...
  </details>

- **2026-07-27** — Alexandra Vassar, Rahat Masood, Hammond Pearce — [On Capturing the Narrative: Social Media Manipulation Wargaming for Cyberliteracy](http://arxiv.org/abs/2607.23993v1)
  <details><summary>📄 Abstract</summary>
  Misinformation is deeply embedded in online discourse, with nearly one in five posts during global events generated by bots that amplify false content. In recent years, the use of Generative AI has further lowered the barrier to producing convincing misinformation, yet most digital literacy education still relies on static checklists and single-player inoculation games built for an earlier media landscape. This paper describes how we addressed this educational gap through Capture the Narrative, ...
  </details>

- **2026-07-27** — Weijie Xia, Stefanie Horian, Hanyue Huang et al. — [Simulating Tenant Responses to Energy Policy Interventions with Transaction-Cost-Aware LLM Age](http://arxiv.org/abs/2607.24341v2)
  <details><summary>📄 Abstract</summary>
  Recent studies use Large language models (LLMs) to simulate human opinions and decisions by prompting models with demographic, attitudinal, or persona-based descriptions. Yet such simulations rarely model the practical, cognitive, or social frictions that shape how people respond to policy interventions. Perceived transaction cost (PTC) provides a useful lens for modeling the practical frictions that shape policy responses, such as information burden, administrative effort, coordination demands,...
  </details>

- **2026-07-26** — Belal S. Alsinglawi, Weizheng Wang, Junyi Wu et al. — [MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents](http://arxiv.org/abs/2607.23870v1)
  <details><summary>📄 Abstract</summary>
  Smart-city airspace is transforming Uncrewed Aerial Vehicles (UAVs) from passive sensing platforms into cyber-physical decision makers that must follow operational rules under degraded observations and ambiguous language. Existing UAV and multimodal benchmarks evaluate perception, navigation, collaboration, and reasoning, but few assess whether physical evidence, protocol constraints, and action risk remain coupled during critical decisions. We introduce MulRobBench, an offline, protocol-conditi...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 148 papers

- **2026-07-28** — Abhishek dileep, Shubham Sharma, Padmanabhan Rajan — [Device Invariance using Domain Adaptation on Acoustic Scene Classification](http://arxiv.org/abs/2607.25887v1)
  <details><summary>📄 Abstract</summary>
  This paper explores the effectiveness of domain adaptation techniques when using convolutional neural network (CNN)-based and transformer-based feature representations for acoustic scene classification. Two well-known domain adaptation techniques, namely domain adversarial neural network (also called DANN) and conditional domain adversarial network (also called CDAN) are evaluated under various domain shifts. Our study indicates that DANN provides effective domain adaptation fairly consistently ...
  </details>

- **2026-07-28** — Yuhao Cheng — [Beyond endoscopy for the symmetric square representation: The simple trace formula case](http://arxiv.org/abs/2607.25383v1)
  <details><summary>📄 Abstract</summary>
  At the beginning of this century, Langlands introduced a strategy known as \emph{Beyond Endoscopy} to attack the principle of functoriality. Altuğ studied $\mathsf{GL}_2$ over $\mathbb Q$ in the unramified setting for the standard representation. We consider the case with ramification at $S=\{\infty,q_1,\dots,q_r\}$ with $2\in S$ and derive an asymptotic formula for the symmetric square representation adding some additional conditions on the test function so that the trace formula is simple. The...
  </details>

- **2026-07-28** — Nagarani Brammanayagam, Devaprakash Muniraj — [MR-TGN: A Meta-Role Temporal Graph Network for Team-Level Intent Prediction in Multi-Agent Systems](http://arxiv.org/abs/2607.25316v1)
  <details><summary>📄 Abstract</summary>
  Collective intent prediction in multi-agent systems focuses on predicting the shared objectives and future behaviours of groups of interacting agents. The problem is particularly challenging because collective intent emerges from complex interactions, evolving cooperation structures, and long-term behavioural dependencies among heterogeneous agents operating in dynamic and partially observable environments. Furthermore, functional roles adopted by agents are often latent, may change over time, a...
  </details>

- **2026-07-28** — Syed Mhamudul Hasan, Anas AlSobeh, Hussein Zangoti et al. — [VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening](http://arxiv.org/abs/2607.26042v1)
  <details><summary>📄 Abstract</summary>
  We present VetClaw, an edge-cloud multimodal agentic system for early veterinary disease screening. VetClaw uses a camera module as an edge sensing device and sends captured images, together with optional symptom descriptions, to a server-hosted vision-language model for zero-shot disease classification. The system separates agent interaction from workflow orchestration: OpenClaw provides scheduling, tool access, user interaction, and notification services on the edge device, while LangGraph man...
  </details>

- **2026-07-28** — Ankang Yang, Jitao Zhao, Di Jin et al. — [CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer](http://arxiv.org/abs/2607.26023v1)
  <details><summary>📄 Abstract</summary>
  Graph foundation models (GFMs) have emerged as a promising paradigm for transferring knowledge across graph domains and tasks. Real-world graphs associate nodes with text, images, and other modalities, making multimodal graphs essential for representing complex entities and relations. Moreover, collecting labels and adapting models for every new graph domain is costly and often infeasible, motivating zero-shot transfer. Unfortunately, zero-shot transfer on multimodal graphs remains underexplored...
  </details>

- **2026-07-28** — Stefan Krsteski, Charlotte Meyer, Guillaume Allegre et al. — [Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation](http://arxiv.org/abs/2607.25891v1)
  <details><summary>📄 Abstract</summary>
  Evaluating AI agents in interactive environments is hindered by fragmented tasks, scaffolds, verifiers, and scoring rules. Existing efforts focus on narrow settings, remain limited in scale, or require costly reruns, leaving much of the empirical record incomparable. We introduce Messier, a unified corpus of 957,253 records that span 30 benchmarks, 714 agents, 11,891 tasks, and 74,205 verifiers. Messier consolidates public benchmark scores and supplements them with five-agent runs across six und...
  </details>

- **2026-07-28** — Minghao Li, Ziqian Liu, Ziyu Mao et al. — [Towards a Systems Foundation for Agentic Cloud Management](http://arxiv.org/abs/2607.25883v1)
  <details><summary>📄 Abstract</summary>
  Agentic cloud management is emerging as a practice to automate laborious operations, minimize toil, and improve responsiveness. Despite the rapid development of autonomous management agents, we argue that the fundamental missing piece is a systems foundation to enable safe, effective operations across agents and between agents and human operators. In this paper, we advocate for the need of such a systems foundation and share our efforts on developing CloudWeaver, an agentic management substrate ...
  </details>

- **2026-07-28** — Jiabao Ji, Yujian Liu, Li An et al. — [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL](http://arxiv.org/abs/2607.25816v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents often spend substantial wall-clock time waiting for tool call results. Tool-call speculation can hide this latency by predicting and pre-executing an agent's next tool call if the prediction matches the agent's eventual tool call, but existing speculators are typically separate draft models or cached traces that are poorly aligned with the deployed agent's own behavior. We identify this speculator-agent gap and show that the target agent itself is a strong next-call s...
  </details>

- **2026-07-28** — Bo-Shiun Shen, Son-Hsien Chen — [Macroscopic wall pressure and microscopic contact load in crowds without egress: social-group cohesion and boundary buffering](http://arxiv.org/abs/2607.25780v1)
  <details><summary>📄 Abstract</summary>
  Crowd safety in confined venues is usually evaluated through evacuation performance or pre-collision avoidance, while direct mechanical hazards in dense gatherings without egress remain poorly understood. We study an Elastic Reorientation Model (ERM), a Social Force Model (SFM), and their coupled dynamics. Post-collision behavior is represented by social-group cohesion ($γ_g$) and wall buffering ($γ_w$), while risk is quantified by the macroscopic wall line pressure ($P_{\text{wall}}$) and the m...
  </details>

- **2026-07-28** — Thomas Hickling, Dylan Wynne, Yu Su et al. — [Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller](http://arxiv.org/abs/2607.25728v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a cooperative indoor UAV guidance framework that combines a shared voxel-map world model with a multi-agent Soft Actor-Critic (MASAC) controller. Multiple drones fuse 360 LiDAR observations into a common world-frame occupancy map, which is converted into a compact bird's-eye-view (BEV) representation and provided to each agent as an ego-aligned local crop. This integrate-in-world, act-in- ego design enables consistent multi-UAV spatial fusion whilst retaining decentralised co...
  </details>

- **2026-07-28** — Sam Relins, Daniel Birks — [Why Public Service AI Governance Frameworks Risk Failing in the Age of General-Purpose AI: Lessons from Policing](http://arxiv.org/abs/2607.25648v1)
  <details><summary>📄 Abstract</summary>
  Public services face growing pressure to adopt artificial intelligence (AI) to close the gap between rising demand and falling resources. That pressure has intensified with general-purpose AI (GPAI): AI built on large language models that can be directed by prompt alone to perform an effectively unbounded range of tasks. We argue that the properties that make these models attractive - their generality, accessibility, and low deployment cost - undermine the conditions under which AI safety has hi...
  </details>

- **2026-07-28** — Federico Cabitza, Gianluca Colombo — [Beyond Epistemia: Epistemic Schizologia and Large Language Models as Techno-Semiotic Machines](http://arxiv.org/abs/2607.25620v1)
  <details><summary>📄 Abstract</summary>
  Quattrociocchi and colleagues warn that the fluent outputs of large language models may allow linguistic plausibility to substitute for epistemic evaluation, producing the condition they call *Epistemia*: the experience of possessing knowledge without undertaking the practices through which judgment would ordinarily be warranted. This article accepts that diagnosis but challenges its explanatory framework, which compares an embodied, socially situated human knower with an isolated generative mod...
  </details>

- **2026-07-28** — Weiming Zhuang, Jiabo Huang, Jingtao Li et al. — [Argus-Unified: Towards A Compact and Economical Unified Model for Image Understanding and Generation](http://arxiv.org/abs/2607.25527v1)
  <details><summary>📄 Abstract</summary>
  Unifying visual understanding and generation in one model holds immense promise, but remains challenging and expensive due to heavy compute and data demands and conflicts between the visual features needed for these two capabilities. To address these challenges, we present Argus-Unified, a compact, effective and unified multimodal model built with low demand on computation and data. Instead of aligning modalities from scratch, Argus-Unified effectively leverages pretrained vision-language models...
  </details>

- **2026-07-28** — Huan Chen, Xiang Song, Jian Jin et al. — [Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm](http://arxiv.org/abs/2607.25446v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent frameworks built on large language models (LLMs) routinely entangle three logically distinct concerns: who is on the team (organization), how members align (coordination), and which algorithm fuses their work (collaboration protocol). IMACS (Intelligent Multi-Agent Collaboration System) separates the three into orthogonal, independently swappable layers. Classic organizational theory (Belbin roles, Mintzberg coordination, RACI accountability) becomes executable, validated configurati...
  </details>

- **2026-07-28** — Jiaran Ye, Lingxu Ran, Zijun Yao et al. — [Where Steering Signals Come From: Activation Source Selection in Activation Steering](http://arxiv.org/abs/2607.25270v1)
  <details><summary>📄 Abstract</summary>
  Activation steering controls language models by adding vectors or features to hidden states at inference time, but the upstream source of these steering signals is often treated as a secondary detail. We study this source choice as activation source selection: the combination of source context and activation readout policy used to collect the hidden states from which a steering signal is built. Holding the downstream intervention fixed, we show across three instruction-tuned models and four stee...
  </details>

- **2026-07-28** — Ghazal Kaviani, Ghassan AlRegib — [FORGE: Frame Orthogonality in Relevance Geometry for Long-Form Video Understanding](http://arxiv.org/abs/2607.25266v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have enabled long-form video understanding at a scale that was not previously possible. However, the density of relevant content decreases sharply as video sequence length increases, and exposing the model to more irrelevant content measurably reduces its accuracy. In this paper, we address the problem of maximizing query-relevant information in a frame subset selected at inference time, without training. FORGE (Frame Orthogonality in Relevance Geometry) ...
  </details>

- **2026-07-28** — Yixuan Duan, Arjun Naik, Sadeer Al-Kindi et al. — [CADENCE: A Cardiac Atom Dictionary for Interpretable Neural Concept Extraction from ECG Foundation Models](http://arxiv.org/abs/2607.25244v1)
  <details><summary>📄 Abstract</summary>
  Foundation models for 12-lead electrocardiograms (ECGs) transfer well across clinical tasks, but the physiological knowledge encoded in their representations remains opaque. We present CADENCE, a framework that decomposes an ECG foundation model into a human-interpretable, queryable dictionary of physiological concepts. Using a BatchTopK sparse autoencoder, CADENCE factorizes Layer-6 embeddings from more than nine million ECG tokens into 8,192 sparse cardiac atoms. These atoms align better than ...
  </details>

- **2026-07-28** — Weiqi Huang, Dianyi Yang, Jiaxin Li et al. — [SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation](http://arxiv.org/abs/2607.25219v1)
  <details><summary>📄 Abstract</summary>
  Social navigation has progressed from simplified 2D environments toward a more general vision-based setting, in which a robot needs to achieve socially compliant behavior purely from onboard visual observations. Yet supporting simulation platforms have not kept pace: existing options either lack visual observations, lack moving human avatars, or fall short of real-world fidelity in appearance and pedestrian behavior, offering limited support for advancing vision-based social navigation. We intro...
  </details>

- **2026-07-28** — Shutong Qiao, Wei Yuan, Tong Chen et al. — [VaLiDRec: Variable-Length LLM-Aligned Semantic IDs for Generative Recommendation](http://arxiv.org/abs/2607.25209v1)
  <details><summary>📄 Abstract</summary>
  Generative recommendation commonly represents items using fixed-length semantic identifiers (SIDs) constructed through clustering and quantization. However, these artificial codes may overcompress item semantics, remain misaligned with pretrained LLM vocabularies, and require costly autoregressive decoding. In light of this, we propose VaLiDRec, a generative recommendation framework based on variable-length, LLM-aligned semantic identifiers. VaLiDRec constructs SIDs directly from informative nat...
  </details>

- **2026-07-28** — Xiao Li, Mouxiao Bian, Zhaodi Wu et al. — [MyoCardBench: A Real-World Data Benchmark for Evaluating Large Language Models in Clinically Authentic Cardiovascular Care Scenarios](http://arxiv.org/abs/2607.25186v1)
  <details><summary>📄 Abstract</summary>
  Background: Most medical large language model (LLM) benchmarks focus on examination knowledge or isolated tasks and may not reflect the longitudinal, multimodal, and safety-critical workflow of cardiovascular care. Objective: To develop MyoCardBench, a real-world benchmark spanning the cardiovascular care continuum, and assess LLM performance across clinical dimensions and specialist tasks. Methods: MyoCardBench includes 2,263 items from 13 task-specific datasets derived from de-identified cardi...
  </details>

- **2026-07-28** — Elan Barenholtz — [A scaling law of contextual persistence in human language](http://arxiv.org/abs/2607.25184v1)
  <details><summary>📄 Abstract</summary>
  Human language exhibits lawful structure at the level of words (frequency, vocabulary growth) and word pairs (co-occurrence across distance). Here we show that the arrangement of words in sequence -- a central determinant of meaning -- obeys a comparable law. Using large language models as probabilistic probes, we measured the reduction in target perplexity conferred by prior context at distance d beyond that of the same words scrambled; this difference, the contextual persistence function P(d),...
  </details>

- **2026-07-28** — Sungjae Park, Shubham Tulsiani — [$π\mathbf{R}^2$: Reactive Real-time Flow Policies](http://arxiv.org/abs/2607.26055v1)
  <details><summary>📄 Abstract</summary>
  Generalist manipulation policies increasingly take the form of action-chunking flow policies built on large pretrained backbones. Such chunks run open-loop, so the policy cannot react to sensory input arriving mid-execution, sacrificing \emph{reactivity}. Replanning more often would restore it, but the perception-to-action pipeline (a large backbone plus multiple denoising steps) is too slow: this \emph{latency} forbids frequent replanning and leaves committed actions stale, making such policies...
  </details>

- **2026-07-28** — Samantha V. Barron, Bradley Mitchell, Vinay Tripathi et al. — [Observable Estimation in the Absence of Classical Verification](http://arxiv.org/abs/2607.25998v1)
  <details><summary>📄 Abstract</summary>
  The predictive success of quantum mechanics underpins many areas of modern science, even as the exact simulation of large, interacting quantum systems remains beyond the reach of classical computation. This success has been enabled by the remarkable advancement of scalable numerical approximation methods, which often demonstrate practical accuracy despite the absence of formal guarantees. As quantum simulation pushes into regimes where these approximations struggle, a fundamental challenge arise...
  </details>

- **2026-07-28** — Huy Ha, C. Karen Liu, Shuran Song — [Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design](http://arxiv.org/abs/2607.25798v1)
  <details><summary>📄 Abstract</summary>
  An often overlooked factor of robot manipulation performance is the embodiment of the robot itself. Motivated by this problem, we study motion-conditioned robot co-design, where the goal is to generate complete robot designs that track target end-effector trajectories (from human demonstrations) while optimizing user-defined rewards. We introduce Transformer Transformer, a diffusion transformer trained on RoboTokens, a unified tokenization of robot embodiments, states, and actions. The same arch...
  </details>

- **2026-07-28** — Yizhou Chen, Hang Xu, Dongjie Yu et al. — [Decompose and Reorganize: Planning with Primitives and Visuomotor Policies Learned from Demonstrations](http://arxiv.org/abs/2607.25397v1)
  <details><summary>📄 Abstract</summary>
  Successfully automating dexterous, long-horizon robotic manipulation requires frameworks capable of both high-level reasoning and fine-grained execution. Traditional task and motion planning (TAMP), while excellent at symbolic planning, is often brittle in contact-rich operations. Simultaneously, imitation learning (IL), while effective in manipulation tasks with visual feedback, is limited by its low capability in spatial generalization and multi-stage operation. To reconcile their complementar...
  </details>

- **2026-07-28** — Fengxiang Wang, Jiangnan Huang, Mingshuo Chen et al. — [Beyond Zooming: Learning Multi-Tool Visual Reasoning for Ultra-High-Resolution Remote Sensing](http://arxiv.org/abs/2607.25993v1)
  <details><summary>📄 Abstract</summary>
  Ultra-high-resolution (UHR) remote-sensing (RS) imagery provides fine-grained Earth-observation evidence over city-scale scenes, but poses a fundamental challenge for multimodal large language models (MLLMs): task-relevant evidence is often sparse, local, and spatially dispersed across extremely large visual contexts. A natural solution is to equip MLLMs with zoom-in tools for active local inspection. However, through a pilot study on XLRS-Bench, we find that zoom-in is only partially effective:...
  </details>

- **2026-07-28** — Shuyue Wei, Chang Liu, Zimu Zhou et al. — [MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents](http://arxiv.org/abs/2607.25992v1)
  <details><summary>📄 Abstract</summary>
  Recently, memory management has become a key infrastructure for LLM-based agents, as it directly affects long-horizon reasoning, personalized responses, and knowledge reuse. However, existing LLM memory systems typically adopt a coarse-grained (utility-agnostic) manner that treats heterogeneous user-LLM interaction records uniformly, leading to redundant and low-impact records persisting in the memory repository. To address this challenge, we present MemLens, a value-aware memory management syst...
  </details>

- **2026-07-28** — Rahat Rizvi Rahman, Mia Mohammad Imran, Kostadin Damevski — [A Low-Cost Human-in-the-Loop Investigation of Toxicity on GitHub at Scale](http://arxiv.org/abs/2607.25946v1)
  <details><summary>📄 Abstract</summary>
  Toxic interactions in open source discussions can alienate contributors and threaten project sustainability, yet prior empirical studies of GitHub toxicity have been limited in scale, raising questions about their generalizability. Scaling up is difficult because toxicity on GitHub is often implicit and context-dependent, making both fully manual annotation and LLM-based labeling unreliable.   We present a human-in-the-loop (HITL) annotation methodology that makes large-scale, domain-calibrated ...
  </details>

- **2026-07-28** — Ana Melissa P. Brito, Neha Bura, Pablo Botella et al. — [Pressure-Induced Irreversible Disorder in $β^{\prime}$-Mn$_3$(PO$_4$)$_2$: A High-Pressure X-ray Diffraction and Density-Functional Theory Study](http://arxiv.org/abs/2607.25896v1)
  <details><summary>📄 Abstract</summary>
  The high-pressure structural behavior of $β^\prime$-Mn$_3$(PO$_4$)$_2$ was investigated using synchrotron X-ray diffraction up to 20 GPa combined with density-functional theory calculations. At ambient conditions, $β^\prime$-Mn$_3$(PO$_4$)$_2$ crystallizes in a monoclinic structure that exhibits strongly anisotropic compression. The pressure dependence of the unit-cell volume was described using a third-order Birch--Murnaghan equation of state, and the principal axes of compressibility were dete...
  </details>

- **2026-07-28** — S. Mitra, S. E. Lakhal, C. P. Connaughton et al. — [A Two-Regime Statistical Framework for Wind-Power Distributions: From Wind-Speed Fluctuations to Turbine Control](http://arxiv.org/abs/2607.25863v1)
  <details><summary>📄 Abstract</summary>
  Wind-power variability is a major challenge for the reliable integration of utility-scale wind energy into modern power systems. Although wind-speed statistics are often described by simple parametric distributions, translating these statistics into turbine-level power fluctuations is nontrivial because the relationship between wind speed and power is highly nonlinear and changes across different turbine operating regimes. Here, we develop a two-regime statistical framework for wind-power distri...
  </details>

- **2026-07-28** — Tiecheng Cai, Zexian Yang, Chao Chen et al. — [Towards Faithful Sentimental Image Captioning via Evidence-Aware Multi-Agent Reasoning](http://arxiv.org/abs/2607.25789v1)
  <details><summary>📄 Abstract</summary>
  Sentimental Image Captioning (SIC) requires balancing emotional expression with visual fidelity. Existing methods often struggle with this trade-off, leading to hallucinations due to insufficient local grounding and the lack of sentimental verification mechanisms. To address these limitations, we propose SEA-Cap, a Sentiment-Evidence-Aware Multi-Agent System for faithful and evidence-grounded sentimental image captioning. SEA-Cap incorporates a Sentiment Evidence Miner that extracts structured, ...
  </details>

- **2026-07-28** — Hyunkyung Han, Min Jung Kim — [Loss Invariance Determines What Concept Layers Encode: Volume Grounding in Echocardiography](http://arxiv.org/abs/2607.25748v1)
  <details><summary>📄 Abstract</summary>
  Objective: Concept bottleneck models route prediction through interpretable intermediate variables, and their validity is normally judged by how accurately those variables are predicted. We ask whether that judgement is sufficient, using left ventricular volumes as the concepts underlying ejection fraction estimation from echocardiographic video.   Methods: A video transformer encoder was trained on a publicly available echocardiography dataset. End-systolic and end-diastolic volumes formed a co...
  </details>

- **2026-07-28** — Javier Irigoyen, Roberto Daza, Francisco Jurado et al. — [AIriskEval-edu Demo: Auditing of Pedagogical Risks in Educational Explanations](http://arxiv.org/abs/2607.25634v1)
  <details><summary>📄 Abstract</summary>
  We present AIriskEval-edu Demo, a platform that audits the pedagogical quality of instructional explanations and provides explainable audit results. The platform evaluates an explanation against a rubric covering five dimensions of pedagogical risk: factual accuracy, depth and completeness, focus and relevance, student-level appropriateness, and ideological bias. For each dimension, it returns a binary decision and a confidence score. Detected risks also include a natural-language rationale and,...
  </details>

- **2026-07-28** — Mary John, Shibili Said, Imad Barhumi et al. — [Matrix-Free Photoacoustic Image Reconstruction via Sensor-Token Self-Attention](http://arxiv.org/abs/2607.25576v1)
  <details><summary>📄 Abstract</summary>
  Photoacoustic tomography (PAT) combines the optical absorption contrast of biological tissue with the spatial resolution of ultrasound, yet recovering the initial pressure distribution from sparse-view sensor measurements remains an ill-posed inverse problem. Iterative compressive-sensing solvers and unrolled deep networks both retain a dependence on the system matrix at inference, which leaves real-time clinical reconstruction computationally expensive. This paper proposes the Sensor Attention ...
  </details>

- **2026-07-28** — Jooyeol Yun, Jintae Park, Hyesu Lim et al. — [ReDesign: Recovering Editable Design Structures from Images via Agentic Decomposition](http://arxiv.org/abs/2607.25565v1)
  <details><summary>📄 Abstract</summary>
  Recovering an editable design file from a raster image is a common and costly bottleneck in modern design workflows, yet remains challenging since editability depends on recovering multi-modal attributes, such as typography, vector geometry, colors, grouping, and layer ordering. We present ReDesign, an agentic framework that grows an editable layer hierarchy by selecting and composing specialized tools across modalities. To keep this long decision process reliable despite imperfect tool outputs,...
  </details>

- **2026-07-28** — Anis Ur Rahman — [DensFiLM: Density-Conditioned Video Saliency for Crowd Scenes](http://arxiv.org/abs/2607.25465v1)
  <details><summary>📄 Abstract</summary>
  Video saliency models typically apply a single fixation strategy across crowd scenes, despite systematic changes in attention with crowd density. Sparse scenes encourage tracking individuals, whereas dense scenes shift attention toward collective motion and scene-level landmarks. We introduce DensFiLM, a density-conditioned video saliency model that inserts a lightweight Feature-wise Linear Modulation layer at the bottleneck of a Video Swin Transformer. A learned density embedding produces chann...
  </details>

- **2026-07-28** — Siyuan Xu, Yan Wang, Haofei Song et al. — [Towards Reliable Stain Transfer: An Iterative Data-Model Co-Optimization Framework Based on Multimodal Expert-Guided Assessment](http://arxiv.org/abs/2607.25393v1)
  <details><summary>📄 Abstract</summary>
  Histopathological examination primarily relies on hematoxylin and eosin (H&E) and immunohistochemistry (IHC) staining. Although IHC provides critical molecular information, it is costly and requires specialized expertise. Stain transfer provides an efficient alternative by computationally generating IHC from H&E images, but remains challenged by unified and interpretable modeling for heterogeneous biomarkers under pixel-unaligned supervision. We propose DMCoStain, a novel Data-Model Co-optimizat...
  </details>

- **2026-07-28** — Ruijie Su, Yuanzhi Liang, Xiaohua Xie et al. — [Physics-Grounded Fluid Video Generation with a Simulation Dataset and Dual-Stream Optical-Flow Supervision](http://arxiv.org/abs/2607.25321v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion models generate visually compelling content but routinely violate elementary physics when the subject involves fluids: liquid columns break apart in mid-air, container water levels fail to rise as liquid is poured in, and splashes disperse without regard to momentum or gravity. We attribute this gap to the fact that large-scale video-text corpora contain almost no explicit motion supervision, so models learn to imitate fluid appearance rather than dynamics. We address this with t...
  </details>

- **2026-07-28** — Deepani Hemachandra, Jagath Senarathne, Mahasen Dehideniya — [A Copula-Based Regression Framework for Enhanced Prediction under Heteroscedasticity](http://arxiv.org/abs/2607.25250v1)
  <details><summary>📄 Abstract</summary>
  Classical regression approaches, including ordinary least squares, rely on strong assumptions such as constant variance and normality of residuals, which are often violated in real-world data. Although log-transformation is commonly used to stabilise variance, it may introduce re-transformation bias and fail to address heteroscedasticity and asymmetric dependence structures adequately. To overcome these limitations, this study proposes a copula-based regression framework for modelling data in th...
  </details>

- **2026-07-28** — Prathyush Sajith, Emadeldeen Hamdan, Ahmet Enis Cetin — [WHTMix: Efficient Stereo Depth Estimation via Walsh-Hadamard Token Mixing](http://arxiv.org/abs/2607.25234v1)
  <details><summary>📄 Abstract</summary>
  Stereo depth estimation for driving, robotics and augmented reality must run at high resolution under tight latency budgets, yet in transformer-based matchers the global self-attention that aggregates scene context grows quadratically with the number of pixels and comes to dominate runtime. We show that the joint self-attention stage of a stereo transformer, whose role is to spread context across both views, can be replaced by a data-independent Walsh-Hadamard token mixer that mixes tokens globa...
  </details>

- **2026-07-28** — Liexin Cheng, Xue Cheng, Shuaiqiang Liu et al. — [RIDGE: An Autonomous Framework for Validation and Method Discovery in LLM-Generated Option Pricing](http://arxiv.org/abs/2607.25199v1)
  <details><summary>📄 Abstract</summary>
  Automated code generation is becoming an important tool in quantitative finance, where large language models can generate option pricing implementations directly from mathematical model specifications. Validating such implementations, however, requires considerably more than conventional software testing: numerical pricing methods must remain mathematically consistent, numerically stable, and reliable across a wide range of model parameters.   We introduce RIDGE, an autonomous validation framewo...
  </details>

- **2026-07-28** — Howard Su, Huan-Hsin Tseng, Chi-Sheng Chen et al. — [Quantum Transformer BSDE Solver via Multi-Layer Fully-Connected Variational Quantum Circuits](http://arxiv.org/abs/2607.25162v1)
  <details><summary>📄 Abstract</summary>
  Solving high-dimensional parabolic partial differential equations (PDEs) is important in engineering, physics, and stochastic control. Deep BSDE methods reformulate semilinear PDEs as backward stochastic differential equations and admit a model-based reinforcement learning interpretation, where trajectories are generated from known stochastic dynamics while a trainable model learns the gradient-related control process. We propose a Quantum Transformer BSDE solver based on Multi-Layer Fully-Conne...
  </details>

- **2026-07-28** — Dorin Dumitraşcu, Liviu Suciu — [On the Irreducibility of the Differential Operators Associated to Random Walks in the Standard Euclidean Lattice](http://arxiv.org/abs/2607.25160v1)
  <details><summary>📄 Abstract</summary>
  For a positive integer $d\geq 1$, we consider the sequences $(A_{n}^{(d)})_n$ and $(x_{n}^{(d)})_n$ given by $$ A_{n}^{(d)} =\sum_{n_1+\dots+n_d=n} \frac{(2n)!}{(n_1!)^2 (n_2!)^2 \dots (n_d!)^2} \quad \text{ and } \quad x_{n}^{(d)} = \frac{A_{n}^{(d)}}{\binom{2n}{n}}. $$ They have rich combinatorial interpretations, but we focus on the analytical properties of their generating functions $A_d$ and $F_d$. We use a modified Borel transform, and algebraic and combinatorial considerations to prove th...
  </details>

- **2026-07-28** — Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi — [VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge](http://arxiv.org/abs/2607.25155v1)
  <details><summary>📄 Abstract</summary>
  Language models have demonstrated remarkable success in solving a wide range of tasks. However, answering complex scientific questions about the power flow often requires solving the distribution optimal power flow (D-OPF) problem. These questions call for numerical solvers and simulators, as linguistic reasoning from parametric knowledge often gives incorrect answers. In this work, we present VeraGrid-Agent, a tool-augmented LLM that autonomously writes the simulator input, executes the open-so...
  </details>

- **2026-07-27** — Mingzhi Xu, Yizhe Zhang — [ESRVS: Extreme Semi-Supervised Retinal Vessel Segmentation with a Single Annotated Image](http://arxiv.org/abs/2607.24453v1)
  <details><summary>📄 Abstract</summary>
  Learning from minimal human supervision is a long-standing goal in medical image analysis, where dense expert annotations are costly. We study retinal vessel segmentation in an extreme semi-supervised setting with one annotated image and a pool of unlabeled images. We propose ESRVS, which selects a representative reference image for manual annotation and transfers vessel cues using target-domain-adapted DINOv3 features. ESRVS constructs a multi granular vessel prototype, combines prototype-simil...
  </details>

- **2026-07-27** — Oleg Grynets, Kyrylo Fursov, Vasyl Lyashkevych et al. — [Specification-Driven DevOps for Multi-Service Environments](http://arxiv.org/abs/2607.25141v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used to generate executable software environments from repository artifacts. However, functional executability does not necessarily imply conformity with architectural, security, workflow, and production intent. This study investigates whether a frontier LLM can generate Dockerfiles and Docker Compose configurations for multi-service applications using repository contents without access to developer-authored deployment artifacts. Three heterogeneous ...
  </details>

- **2026-07-27** — Mohan Li, Rama Doddipatla, Philip C. Woodland — [Text-Prompted CLAP: Learning Query-Conditioned Audio Representations via Contrastive Learning](http://arxiv.org/abs/2607.25085v1)
  <details><summary>📄 Abstract</summary>
  Contrastive Language-Audio Pretraining (CLAP) learns aligned text and audio representations in a shared embedding space. However, independent encoding of each modality limits its ability to model cross-modal semantics in complex audio understanding and retrieval tasks. To address this limitation, this paper proposes Text-Prompted CLAP (TP-CLAP), a parameter-efficient extension of CLAP that introduces a cross-attention-based fusion module to incorporate textual prompts into audio features. TP-CLA...
  </details>

- **2026-07-27** — Dengzhe Hou, Lingyu Jiang, Fangzhou Lin et al. — [CogEEGAgent: Toward Autonomous Cognitive EEG Analysis with Grounded Execution and Selection-Aware Verification](http://arxiv.org/abs/2607.25045v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) analysis in cognitive studies requires specialized expertise and involves many defensible choices over contrasts, channels, time windows, and statistical tests. LLM agents can translate varied natural-language questions into analysis choices, offering a flexible interface for automation. Yet fluent reports alone cannot establish that an agent selected the requested analysis or evaluated a confirmatory claim independently of adaptive search. We present CogEEGAgent, a ...
  </details>

- **2026-07-27** — Dengzhe Hou, Lingyu Jiang, Fangzhou Lin et al. — [CogArena: A Multimethod Evaluation of Cognitive Ability Structure in Large Language Models](http://arxiv.org/abs/2607.24999v1)
  <details><summary>📄 Abstract</summary>
  LLM cognitive scores are increasingly summarized as per-ability profiles whose dimensions should converge across tasks, respond selectively to matched interventions, and generalize beyond the models used to define them. We introduce CogArena, a procedurally generated 13-paradigm benchmark built around a multimethod framework for determining when cognitive-task scores warrant dimensional labels across five theory-motivated groupings. Across 55 open-weight models, nearly all paradigm correlations ...
  </details>

- **2026-07-27** — Hangjie Yuan, Yichen Qian, Zhiwei Tang et al. — [ClinFusion: A Vision-Centric Multimodal LLM System for Holistic Medical Understanding](http://arxiv.org/abs/2607.24743v2)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) hold immense potential to revolutionize clinical practice, yet deploying them in the medical domain is fundamentally a vision-centric challenge: models must absorb knowledge from heterogeneous 2D and 3D medical images, and evaluation protocols must align with radiologists' clinical practice and provide an accurate, fine-grained and factualness-driven assessment. In this paper, we introduce ClinFusion, a vision-centric MLLM designed for holistic medical un...
  </details>

- **2026-07-27** — Shaker Al-Tamari, Waled Kadour — [Explainable Reinforcement Learning via Physics-Aware Policy Distillation](http://arxiv.org/abs/2607.24672v1)
  <details><summary>📄 Abstract</summary>
  In safety-critical sectors such as robotics and automotive engineering, the deployment of Deep Reinforcement Learning (DRL) is often hindered by the black-box nature of deep neural networks. This lack of transparency poses significant challenges for regulatory compliance and human-agent trust. This paper presents an experimental study aimed at making high-performance continuous control DRL systems interpretable. A policy distillation framework is implemented using the classic Inverted Pendulum b...
  </details>

- **2026-07-27** — Zhenhan Gao, Marvin Muñoz Barón, Umm-e Habiba et al. — [Evaluating the Impact of Explainable AI on Trust in AI-Assisted Code Review](http://arxiv.org/abs/2607.24601v1)
  <details><summary>📄 Abstract</summary>
  Background: Large language models (LLMs) are increasingly used to automate code review, but the reasoning behind their decisions remains hard to understand. Developers struggle to assess the validity of LLM-generated reviews, making it difficult to gauge how much trust to place in them. The role of Explainable AI (XAI) in code review and its impact on trust remain underexplored.   Objective: We study the influence of XAI on developer trust in AI-assisted code reviews.   Method: We conducted a wi...
  </details>

- **2026-07-27** — Jan Range, Björn Schembera, Dominik Göddeke — [Making Mathematical Knowledge Explainable, Accessible and Interoperable Through Large Language Model Integration](http://arxiv.org/abs/2607.24512v1)
  <details><summary>📄 Abstract</summary>
  Mathematical models are central to formalizing research problems, yet their documentation often falls short of FAIR principles. Knowledge bases such as the Mathematical Model Database (MathModDB) address this gap by providing curated, semantically rich representations of mathematical models. Built on Wikibase, the same open-source infrastructure underlying Wikidata, MathModDB utilizes Semantic Web technologies to support Linked Open Data, collaborative editing, and the storage of semantically en...
  </details>

- **2026-07-27** — Liwei Dong, Jiahao Zhao, Nan Xu — [From Execution to Capability: Scientific Experience Consolidation via Procedural Knowledge Synthesis](http://arxiv.org/abs/2607.24459v2)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly solve scientific-computing tasks, but executable feedback from one problem rarely becomes durable capability on subsequent problems. We study scientific-computing experience consolidation: converting verified runtime experience into transferable procedural knowledge and persistent model improvement. This setting presents two challenges: trajectory-derived artifacts may encode source-specific repairs rather than cross-task computational mechanisms; and a weaker ...
  </details>

- **2026-07-27** — Yifan Hu, Shuwei He, Rui Liu et al. — [Let Me Look at You: Advanced Facial Expression Modeling for Conversational Speech Synthesis](http://arxiv.org/abs/2607.24430v1)
  <details><summary>📄 Abstract</summary>
  Conversational Speech Synthesis is a fundamental component of human-computer interaction, aiming to generate contextually appropriate, expressive, and empathetic speech. However, facial expressions encode subtle and rich affective cues that are crucial for empathetic speech interaction, whereas existing approaches often overlook this important modality. In addition, the lack of large-scale natural conversational datasets with both speech and visual modalities also limits the development of visua...
  </details>

- **2026-07-27** — Kai Syun Hou, James Kwok — [Rethinking the Generation Order of Block Diffusion Language Models](http://arxiv.org/abs/2607.24306v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models enable flexible arbitrary-order generation, but existing sampling methods are mostly designed for early masked diffusion models (MDMs). In this work, we study sampling for recent block diffusion language models (BDLMs). We show empirically and analytically that these models are naturally more aligned with left-to-right decoding than MDMs. Based on this observation, we propose Parallel Autoregressive Decoding (PARD), a simple training-free sampling method that preserves ...
  </details>

- **2026-07-27** — Yueru Luo, Xu Yan, Changqing Zhou et al. — [Reasoning to Regulate: Chain-of-Thought for Traffic Rule Understanding](http://arxiv.org/abs/2607.24199v1)
  <details><summary>📄 Abstract</summary>
  Understanding and complying with traffic regulations is a safety-critical requirement for autonomous driving, yet remains challenging due to the diversity and context dependence of traffic signage. Importantly, regulation understanding is not a simple recognition task, but a reasoning problem: whether a rule applies depends on interpreting the sign in relation to the spatial layout of lanes and scene context. To support such reasoning, MapDR provide fine-grained annotations that link each traffi...
  </details>

- **2026-07-27** — Ya Gao, Peina Zhao, Yiheng Li et al. — [Secrecy Energy Efficiency for IRS-Assisted Low-Altitude Communications: A D3QN-PER Based Approach](http://arxiv.org/abs/2607.24183v1)
  <details><summary>📄 Abstract</summary>
  To address the security and energy efficiency challenges in low-altitude economy (LAE) wireless communications, we develop a secure synergistic network integrating unmanned aerial vehicle (UAV) and intelligent reflecting surface (IRS), with an emphasis on maximizing secrecy energy efficiency (SEE) for downlink transmission scenarios. In particular, firstly, we establish the channel transmission models for UAV-IRS assisted LAE communications network. Then, we formulate a non-convex fractional opt...
  </details>

- **2026-07-27** — Jingwen Zhu, Keshu Wu, Pei Li et al. — [Forecasting the Emergence and Evolution of Crash Hotspots: A Unified Deep Learning Framework for Proactive Traffic Safety](http://arxiv.org/abs/2607.24168v1)
  <details><summary>📄 Abstract</summary>
  Road crashes remain among the gravest threats to public safety, and preventing them is a defining task of transportation systems worldwide. Much of that harm concentrates at hotspots, yet a hotspot is less a place than an episode; it emerges quietly at an intersection or along an arterial, intensifies for weeks, then subsides, only to reappear elsewhere. Enforcement guided by maps of past crashes inevitably trails this cycle, patrolling yesterday's hotspots while tomorrow's form unwatched. Break...
  </details>

- **2026-07-27** — Qian Li, Zhenyan Qi, Liang Shen et al. — [A Cybersecurity MLPS Large Language Model with Multi-Path Retrieval Fusion](http://arxiv.org/abs/2607.24116v1)
  <details><summary>📄 Abstract</summary>
  The Multi-Level Protection Scheme (MLPS) is a foundational system in China's cybersecurity governance framework. Therefore, accurate analysis and understanding of MLPS requirements are essential. At present, MLPS analysis still relies mainly on manual interpretation of standards and rule-based tools. This makes it hard to provide stable and consistent compliance analysis in complex application scenarios. The rise of large language models has created new opportunities for making MLPS work more in...
  </details>

- **2026-07-27** — Tuan-An To, Yuk-Kwan Wong, Tuan-Anh Vu et al. — [MarineEVT: Advancing Event-Centric Marine Video Understanding via Visual Tool Reasoning](http://arxiv.org/abs/2607.24064v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language Models (VLMs) have achieved remarkable success in visual understanding, driven by the growing availability of high-quality image-text pairs. However, the performance of VLMs often degrades in the video domain due to the essential need for temporal understanding and the scarcity of large-scale annotated video data. In this work, we focus on marine video understanding, which brings further challenges: first, it requires substantial domain expertise; and video VLMs usually st...
  </details>

- **2026-07-27** — Seoyeon Kim, Minjae Kang, Jaehyung Kim — [SyRuP: Enhancing System-Prompt Following via Reward-Guided Prediction in LLM Decoding](http://arxiv.org/abs/2607.23991v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly controlled through system prompts that specify roles, styles, formats, and safety requirements. However, models follow these prompts only implicitly through in-context learning, which can be insufficient for complex or compositional prompts. Existing approaches often require model tuning or response-level reranking, limiting their practicality for lightweight inference-time control. We introduce SyRuP, a decoding-time framework for improving system-p...
  </details>

- **2026-07-27** — Callie C. Liao, Duoduo Liao, Ellie L. Zhang — [MusiChat: Vibe Composing for Music Creation](http://arxiv.org/abs/2607.24873v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in AI music generation have enabled users to create complete musical pieces from natural-language prompts. However, most existing systems follow a prompt-and-regenerate paradigm, making iterative refinement difficult because users must repeatedly recreate compositions instead of directly evolving existing musical ideas. We present MusiChat, a conversational vibe composing system that enables collaborative human-AI music creation through natural-language interaction and iterative ...
  </details>

- **2026-07-27** — Haodi Fan, Zucong Lan — [From Cognitive Architectures to Language Agents: A Mechanism-Level Review of Lineage, Convergence, and Migration Gaps](http://arxiv.org/abs/2607.23942v1)
  <details><summary>📄 Abstract</summary>
  Memory, planning, reflection, and tool use are often compared as feature labels, obscuring the control semantics that determine how an agent actually runs. This review connects ten historical cognitive architectures, eight language-agent runtime families, and forty-two mechanism-focused modern systems. We reconstruct each mechanism through state, control, transition, persistence, failure, learning, and resource governance, then code evidence relation (E1-E4) separately from migration depth (D0-D...
  </details>

- **2026-07-27** — Yue Zhang, Xiangyu Li, Wanshu Fan et al. — [DDVT: Dynamic Dual-level Vision Transformer Fusion Network for Answer Grounding in Visual Question Answering](http://arxiv.org/abs/2607.23921v1)
  <details><summary>📄 Abstract</summary>
  Answer grounding in visual question answering aims to locate the region from a given natural language question associated with the visual content of an image, which has garnered significant attention due to its practical applications. In this paper, we introduce the Dynamic Dual-level Vision Transformer Fusion Network (DDVT) for answer grounding in visual question answering. Specifically, we propose a question-guided dynamic regional-level module (QGDR) that combines complementary image context ...
  </details>

- **2026-07-27** — Praveen Selvaraj, Lorenzo Uttini, Ville Kuosmanen — [ArmnetBench v0.1: Parallel Real-World Evaluation of Manipulation Policies on a Low-Cost Arm Farm](http://arxiv.org/abs/2607.24481v1)
  <details><summary>📄 Abstract</summary>
  Real-world evaluation is a bottleneck in developing generalist robot manipulation policies. Each rollout requires physical hardware and an operator to set up, reset, and score it. We introduce ArmnetBench v0.1, a benchmark run on a fleet of low-cost SO-101 cells under light on-site supervision. v0.1 validates this arm farm end to end and compares 7 policies across 12 tasks with both single-arm and bimanual configurations. Each policy is trained or fine-tuned on 50 demonstrations per task; the be...
  </details>

- **2026-07-27** — Pin Qian, Su Wang, Chong Peng et al. — [When Should Active RAG Retrieve? A Budget-Aware Evaluation of Utility, Calibration, and Cost](http://arxiv.org/abs/2607.24010v1)
  <details><summary>📄 Abstract</summary>
  Active RAG systems decide when to retrieve external knowledge during generation, making them a budget-sensitive case of agentic RAG and self-adaptive retrieval. Yet evaluations often leave the operating point underspecified: two systems may both claim a 50% evidence-usage budget while realizing different held-out usage rates, so higher accuracy can reflect a looser budget rather than a better retrieval policy. We study budget-aware evaluation for Active RAG by recasting active retrieval as utili...
  </details>

- **2026-07-27** — Tianyuan Du, Tianyi Hu, Hanting Ye et al. — [SHARE: Towards Head-Mounted AR with User-Centric SLAM in Shared Human-Robot Workspaces](http://arxiv.org/abs/2607.23901v1)
  <details><summary>📄 Abstract</summary>
  Human-Robot Collaboration (HRC) in shared physical spaces using Augmented Reality (AR) interfaces is powered by Simultaneous Localization and Mapping (SLAM). Existing multi-agent SLAM systems rely on an edge server to combine visual findings of multiple resource-constrained agents, perform computation, and schedule updates to their local maps. However, the edge treats all agents uniformly and ignores the fundamentally different latency requirements of heterogeneous HRC agents: robots and head-mo...
  </details>

- **2026-07-27** — Funda Durupinar — [How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation](http://arxiv.org/abs/2607.25140v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the behavior of language models in a multi-agent crowd simulation, focusing on how affect propagates among agents that perceive and appraise one another. Each agent perceives its neighbors through visual, auditory, and tactile channels, then appraises these perceptions in light of its prompted personality profile, memory, current affective state, and situational context. Appraisal is carried out by an LLM, which updates the agent's internal affective state and selects its outw...
  </details>

- **2026-07-27** — Shiwei Tan, Yusong Zhao, Weiyi Qin et al. — [Interpretable GOHR Agents via Sparse Autoencoders](http://arxiv.org/abs/2607.25132v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in interpreting learned decision-making systems is to determine whether their internal representations contain concepts that help explain their behavior. We report interpretability experiments for a tokenized autoregressive Transformer agent in the Game of Hidden Rules (GOHR). We focus on a compact two-rule task in which both hidden rules map object shapes to target buckets, but with different permutations. The policy is trained on episodes sampled from these two hidden rules...
  </details>

- **2026-07-27** — Manizheh Botshekananfard, Elif Büşra Güraksın, Vasileios A. Letsios et al. — [A discrete series gauge field at the late-time boundary of $dS_4$](http://arxiv.org/abs/2607.25067v1)
  <details><summary>📄 Abstract</summary>
  We study the free Maxwell field on the planar patch of four-dimensional de Sitter spacetime ($dS_4$). We review its bulk canonical quantization in the Bunch-Davies vacuum, and we give a representation-theoretic viewpoint by studying the transformation properties of single-particle states under infinitesimal dS transformations. By taking the late-time limit, we identify two late-time operators with scaling dimensions $Δ=1$ (leading) and $Δ=2$ (subleading). We introduce CFT-inspired inner products...
  </details>

- **2026-07-27** — Getachew K. Befekadu — [Simulation-based parameter estimation via a combination of embedded normalizing flows and implied empirical probabilities under moment restrictions](http://arxiv.org/abs/2607.25026v1)
  <details><summary>📄 Abstract</summary>
  In this work, we present a simulation-based parameter estimation framework for a model defined by a computational simulation of a physical system. We specifically outline an estimation framework consisting of two closely-integrated steps that facilitate an overall end-to-end parameter estimation scheme. The first step involves utilizing an embedded normalizing flow which is used to transform the unknown complex distribution of the residual information into a simple base distribution correspondin...
  </details>

- **2026-07-27** — Ishrat Jahan Eliza, Md Dilshadur Rahman — [Chart-Supported or Model-Supplied? Examining MLLM-Generated Claims for Accessible Visualization](http://arxiv.org/abs/2607.25021v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can connect visualization patterns to external causes, consequences, and domain knowledge, but the evidential basis of these interpretations is often unclear. We present an exploratory study of 102 visualizations from four sources, three MLLMs, and four input conditions that vary access to the image, source-specific accessible chart context, and withheld-context framing. Across 1,224 descriptions, we analyze model-attributed DIRECT, DERIVED, and SPECULATI...
  </details>

- **2026-07-27** — Stefan L. Ludescher, Manuel Mekonnen, Thomas D. Galley et al. — [Quantum reference frames beyond subsystems: a reconstruction and generalization of the perspective-neutral framework](http://arxiv.org/abs/2607.24976v1)
  <details><summary>📄 Abstract</summary>
  We generalize the notion of quantum reference frames (QRFs) to cases where the frame does not necessarily correspond to a tensor factor subsystem, but to a covariant quantum instrument. This unlocks a variety of physical applications: "frames of labeling" for indistinguishable particles, suggesting explanations for the symmetrization postulate and the absence of parastatistics, and yielding a transparent description of the entanglement of bosons and fermions; and relational clocks reproducing th...
  </details>

- **2026-07-27** — Ali Ansari, Yasmin Mohammadi, Farnoush Nili et al. — [ERUnderstand: Evaluating Vision-Language Models on Structured ER Diagrams](http://arxiv.org/abs/2607.24707v1)
  <details><summary>📄 Abstract</summary>
  Entity-Relationship Diagrams (ERDs) are central to conceptual database design, yet they are typically available only as rendered images rather than machine-readable schemas, limiting AI-assisted database engineering. We introduce ERUnderstand, the first large-scale benchmark for structured understanding of ER diagrams, comprising 2,960 diagrams collected from curated educational sources, real-world schemas, and synthetically generated examples spanning diverse domains, notations, complexity leve...
  </details>

- **2026-07-27** — Yanhao Jia, Jiepeng Wang, Haibin Huang et al. — [MMOE: Modernizing Diffusion Transformers with Efficient Expert Design](http://arxiv.org/abs/2607.24665v1)
  <details><summary>📄 Abstract</summary>
  Modern large language models scale successfully by pairing capacity growth with efficiency, keeping per-token and deployment costs under control as capacity grows. AIGC Foundation Models (AFMs), especially diffusion-transformer backbones, have begun to adopt sparse experts, but recent efforts mostly enlarge total parameter counts and sparsity ratios without importing the efficiency mechanisms that made LLM scaling practical, so generation quality is seldom balanced against training and deploymen...
  </details>

- **2026-07-27** — Jinlong Yang, Wenhao Zhang, Kuanwei Lin et al. — [CADER: Confidence-Aware Dynamic Evidence Reasoning for Long-Video Understanding](http://arxiv.org/abs/2607.24582v1)
  <details><summary>📄 Abstract</summary>
  Long-video understanding increasingly relies on large vision-language models and tool-augmented reasoning, but most systems apply the same inference procedure to every example regardless of difficulty. This uniform strategy invokes unnecessary tool-assisted processing for easy questions and provides limited control when difficult questions require fine-grained temporal evidence. We propose CADER (Confidence-Aware Dynamic Evidence Reasoning), a training-free framework for adaptive and reliable lo...
  </details>

- **2026-07-27** — Shuo Wang, Kai Zhang, Wenyuan Huang et al. — [DeCoRAG: Cognitive Decoupling and Semantic-Aware Cropping for Complex Document Understanding](http://arxiv.org/abs/2607.24554v1)
  <details><summary>📄 Abstract</summary>
  Advancing multimodal retrieval-augmented generation (RAG) for complex document understanding presents a formidable dual dilemma of accuracy and efficiency, particularly in graph RAG. Processing structurally sparse yet visually dense layouts, such as extracting a tiny data marker from a financial chart, often incurs computationally prohibitive token overhead while still triggering catastrophic hallucination. However, multimodal Graph RAG pipelines rely on graph-construction stages that assume Vis...
  </details>

- **2026-07-27** — Kaiyang Ye, Yuan Ge, Junxiang Zhang et al. — [FlowCTS: On-policy Continuous Trajectory Supervision of Flow Models](http://arxiv.org/abs/2607.24522v1)
  <details><summary>📄 Abstract</summary>
  While on-policy distillation (OPD) effectively addresses sparse rewards and exposure bias in large language model post-training, its extension to flow models remains underexplored. To this end, we propose Flow Continuous Trajectory Supervision (FlowCTS), which matches subsequent student and reference trajectories initialized from the same student-visited state. Using the integral relation between trajectories and velocity fields, we derive a temporally weighted velocity-matching upper bound and ...
  </details>

- **2026-07-27** — Huu Hiep Nguyen, Dung Nguyen, Minh Hoang Nguyen et al. — [LLM as Forecasting Planner: Training-Free Text Conditioning for Time-Series Foundation Models](http://arxiv.org/abs/2607.24892v1)
  <details><summary>📄 Abstract</summary>
  Text-conditioned time-series forecasting predicts a series from both its numerical history and natural-language context, allowing forecasts to account for events and constraints that the past alone cannot reveal. This requires both reliable numerical forecasting and the ability to interpret contextual information. Time-series foundation models (TSFMs) provide strong numerical forecasts, while large language models (LLMs) can reason over text, but combining their strengths remains challenging bec...
  </details>

- **2026-07-27** — Jiahao Xie, Zhongbin Guo, Qianle Wang et al. — [DecoupleMix: Decoupled Ratio Search and Convex Allocation for Scalable VLM Data Recipes](http://arxiv.org/abs/2607.24516v1)
  <details><summary>📄 Abstract</summary>
  While data curation for Vision Language Models (VLMs) is increasingly active, public practice for constructing pretraining mixtures remains largely heuristic: practitioners stack datasets that pass quality filters, set cross-domain ratios by intuition, and lack a principled, attributable criterion for admitting new data, while frontier recipes remain undisclosed. We formulate data construction as a systematic mixture-optimization problem and turn it into a reproducible engineering discipline by ...
  </details>

- **2026-07-27** — Brittany Harbison, Ashok K. Goel — [LEX-EC: A Lexical Evidence-Channel Audit Framework for Zero-Shot LLM Personality Classification in Black-Box Settings](http://arxiv.org/abs/2607.24435v1)
  <details><summary>📄 Abstract</summary>
  Large language models may easily assign personality labels from text, but model interpretability remains an open problem. To address this gap, we introduce LEX-EC, a reusable black-box audit framework combining prevalence and agreement diagnostics with controlled lexical ablation to distinguish marginal-distribution effects from trait-associated signal recoverable under restricted evidence. Using this framework, we illustrate how various text genres may exhibit sharply different profiles: free-f...
  </details>

- **2026-07-27** — Shaofei Lei — [MAViE: A Multi-scale Adaptive Vision Encoder for Fine-grained Visual Perception and Efficient Multimodal Reasoning](http://arxiv.org/abs/2607.24424v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models commonly project all tokens produced by a pretrained vision encoder into a large language model. However, final-layer features can discard text, local attributes, and spatial relationships, while high-resolution inputs substantially increase context length and inference latency. We introduce \method, a Multi-scale Adaptive Vision Encoder. \method uses position-dependent gates to fuse shallow, intermediate, and deep features from a vision Transformer, preserving global sema...
  </details>

- **2026-07-27** — Tahar Chettaoui, Guray Ozgur, Eduarda Caldeira et al. — [IJCB-AFMFR 2026: Competition on Adapting Foundation Models for Face Recognition Using Synthetic Training Data](http://arxiv.org/abs/2607.24422v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a summary of the Competition on Adapting Foundation Models for Face Recognition Using Synthetic Training Data (AFMFR), held at the 2026 International Joint Conference on Biometrics (IJCB 2026). The competition received a total of eight valid submissions from four distinct teams across two complementary tracks: a Full Data Track, in which participants adapt the CLIP ViT-L/14 foundation model using large-scale synthetic identity data, and a Limited Data Track, designed to refle...
  </details>

- **2026-07-27** — Priyansh Srivastava — [The Tokenizer Tax: Quantifying and Explaining the Cross-Lingual Cost of Subword Tokenization for Indian Languages](http://arxiv.org/abs/2607.24276v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) process text through subword tokenizers rather than directly reading characters or words. Because these tokenizers are trained predominantly on English-centric corpora, they introduce a systematic and often overlooked disadvantage for many non-English languages. In this work, we quantify this tokenizer tax for Indian languages using the FLORES-200 parallel corpus, measuring tokenization fertility across six widely used tokenizers and fourteen languages. Under cl100k_...
  </details>

- **2026-07-27** — Yu Cui, Yi Xu, Jiahao Wang et al. — [SpecFormer: Mitigating Embedding and Attention Collapse via Spectral-Aware Transformer for Recommendation](http://arxiv.org/abs/2607.24025v1)
  <details><summary>📄 Abstract</summary>
  Transformer architectures have achieved remarkable success across diverse domains; however, directly applying their standard self-attention mechanism to recommendation often yields suboptimal performance, sometimes even trailing behind well-designed simple recommendation models. In this paper, we reveal that this performance bottleneck stems from severe embedding and attention collapse unique to recommendation scenarios. The heterogeneity and long-tail nature of recommendation data lead to a sev...
  </details>

- **2026-07-27** — Younggue Bae — [MEMOIR: Temporal Behavioral Memory for Recommendation Across the Preference-Drift Spectrum](http://arxiv.org/abs/2607.23986v1)
  <details><summary>📄 Abstract</summary>
  We propose MEMOIR, a framework that segments user interaction histories into temporal windows, generates semantic behavioral memory for each period using an LLM, and aggregates current state, evolution direction, and predicted future into a single user representation. On the Electronics and Clothing_Shoes_and_Jewelry categories of Amazon Reviews 2023, MEMOIR is statistically tied with UniSRec, the strongest baseline, on aggregate NDCG@10 (0.0643 vs. 0.0641), splitting the four reported metrics 2...
  </details>

- **2026-07-26** — Chi Phan, Tianyi Zhang, Yufeng Wu et al. — [PathScale-R1: Cross-scale Reasoning for Pathological Image Analysis](http://arxiv.org/abs/2607.23794v1)
  <details><summary>📄 Abstract</summary>
  Pathological diagnosis is inherently multi-scale, requiring the integration of global tissue architecture at low magnification with cellular morphology at higher magnification. However, existing pathology benchmarks and vision-language models (VLMs) are still largely developed under single-scale settings, limiting their ability to learn clinically meaningful multi-magnification reasoning. Moreover, naively constructed visual question answering (VQA) tasks may be susceptible to text-only or super...
  </details>

- **2026-07-26** — Kartik Teotia, Helge Rhodin, Hyeongwoo Kim et al. — [STEER: Steerable Dyadic Head Avatars](http://arxiv.org/abs/2607.23840v1)
  <details><summary>📄 Abstract</summary>
  Facial movement and expression are central to face-to-face communication, conveying turn-taking, attention, agreement, and engagement alongside speech. While speech-driven facial animation has made strong progress in lip synchronization and audio-conditioned motion generation, most methods treat conversational behavior as an emergent byproduct of audio, or expose only coarse sequence-level affect control. As a result, key non-verbal channels such as gaze contact and aversion, rhythmic head motio...
  </details>

- **2026-07-26** — Deovrat Mehendale, Aditya Mehndiratta, Dhruv Rathi et al. — [Indic DiarBench: A Multilingual Joint Diarization and ASR Benchmark for Indian Languages](http://arxiv.org/abs/2607.23808v1)
  <details><summary>📄 Abstract</summary>
  In this work, we introduce Indic DiarBench, a speaker diarization and ASR benchmark dataset spanning all 22 scheduled languages of India. This corpus comprises approximately 108 hours of natural multi-speaker audio from near-field meetings, far-field recordings, and in-the-wild audios. All annotations are human-corrected with time-aligned speaker attributed transcriptions. The dataset captures conversational nuance prevalent in Indian speech, such as English code-mixing, dialectal variation, and...
  </details>

- **2026-07-26** — NeoteAI Team, Fudan TEAI Team — [$N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation](http://arxiv.org/abs/2607.23783v1)
  <details><summary>📄 Abstract</summary>
  We present $N_0$-TWAM, a tactile-native world-action model for contact-rich manipulation that predicts both future vision and future contact. To our knowledge, it is the first tactile world-action model trained at large scale, and it shows strong capability on contact-rich tasks. We pre-train $N_0$-TWAM at large scale with visuo-tactile joint training over tactile-rich demonstrations spanning six embodiments and 450 tasks. We use NeoForce, a unified force-based tactile representation, to form a ...
  </details>

- **2026-07-26** — NeoteAI Team, Fudan TEAI Team — [$N_0$-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens](http://arxiv.org/abs/2607.23782v1)
  <details><summary>📄 Abstract</summary>
  We present $N_0$-VTLA, a vision-tactile-language-action (VTLA) foundation model capable of (1) fine-grained contact-rich manipulation with tactile perception and tactile-feedback control, and (2) offline policy improvement from stored deployment data. Building on current vision-based backbones, we propose a training recipe for tactile integration consisting of visuo-tactile pre-training, staged tactile-pathway integration, and advantage-conditioned offline policy improvement. During pre-training...
  </details>

- **2026-07-26** — Sietse Schelpe — [A Frozen 12B Beats Frontier Models on Verified Work: 100% Accuracy, 0 Tokens, Bit-Exact, Forever](http://arxiv.org/abs/2607.23806v1)
  <details><summary>📄 Abstract</summary>
  Improving a language model today means retraining it: enormous compute, a new opaque model each cycle, non-deterministic output. We take the opposite path: the model stays frozen, and a persistent memory of verified solutions grows beside it. Once a problem family is solved and has passed an independent verification step that never consults the answer key, every new instance of that family is answered at zero generation tokens, bit-exact, deterministically. Across 180 fresh instances spanning ni...
  </details>

- **2026-07-26** — Qinsi Wang, Jing Shi, Huazheng Wang et al. — [From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement](http://arxiv.org/abs/2607.23802v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning with Verifiable Rewards (RLVR) has driven recent progress in reasoning-oriented large language models (LLMs) by enabling large-scale optimization. However, its applicability remains largely limited to domains such as mathematics and coding, where correctness can be deterministically verified. Open-ended tasks instead often rely on human preferences, reward models, or LLM-based judges, introducing evaluation bias, judge capability bottlenecks, and additional inference costs...
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

- **2026-07-14** — Aldrin Montana, Colin Marc, Luca Bigon et al. — [Not Your Usual Type(s): Data contracts as types across languages and engines](http://arxiv.org/abs/2607.13339v1)
  <details><summary>📄 Abstract</summary>
  Composable data systems promise to let developers combine languages, engines, and catalogs without sacrificing a coherent user experience. In practice, however, pipeline-node boundaries remain weakly specified: transformations exchange tables through schemas that are often checked late, enforced unevenly across languages, and disconnected from the semantics business users care about. Based on over a year of operating millions of jobs in Bauplan, we share the design principles behind our new SDK,...
  </details>

- **2026-07-14** — Jae Joong Lee — [Accuracy Without Grounding: Diagnosing Visual Dependency Dissociation in Video LLM Benchmarks](http://arxiv.org/abs/2607.13305v1)
  <details><summary>📄 Abstract</summary>
  Benchmark accuracy in video large language models (LLMs) is often treated as evidence of visual understanding. We audit this assumption across twenty models spanning 2-78B parameters and ten architecture families. We introduce the Visual Dependency Gap (VDG), the difference in per-question correctness between original-video and black-screen conditions. Paired McNemar tests on MVBench show that accuracy and visual dependency are separable: models differ on original video (p = 0.0003) but not on b...
  </details>

- **2026-07-14** — Stylianos Loukas Vasileiou, Olga Derendiaeva — [Discourse-Aware Policy Analysis with Argumentation: A Hybrid LLM-Symbolic Framework for Disaster Governance](http://arxiv.org/abs/2607.13260v1)
  <details><summary>📄 Abstract</summary>
  Policy documents shape governance outcomes, but their reasoning is often implicit. Participatory commitments and managerial control routinely coexist in the same text, and the tensions between them are rarely stated directly. Existing computational approaches to policy discourse cannot express the frame-mediated relations that drive these tensions, where one argument narrows or instrumentalizes another rather than rejecting it. End-to-end summarization by large language models produces fluent te...
  </details>

- **2026-07-14** — Ali Parviz, Gal Mishne, Alex Cloninger — [Reassessing Muon for Matrix Factorization](http://arxiv.org/abs/2607.13246v1)
  <details><summary>📄 Abstract</summary>
  Muon has recently emerged as a strong optimizer for large-scale deep learning, where it reshapes gradient updates through approximate orthogonalization and has been reported to outperform Adam and AdamW in large language model training. Its empirical success has motivated a growing body of theoretical work that interprets Muon as steepest descent under the spectral norm. Yet it remains unclear which of Muon's advantages stem from its update rule itself and which are artifacts of the scale, archi...
  </details>

- **2026-07-14** — Quanyan Zhu — [AI-Native Insurance for Agentic AI: Pricing, Underwriting, and End-to-End Automation](http://arxiv.org/abs/2607.13230v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI introduces new insurance challenges because autonomous AI systems can make decisions, invoke tools, modify external environments, and interact with third-party services. This paper develops an AI-native mathematical framework for underwriting, pricing, and contract design for agentic AI deployments. A deployment is represented by a risk state that captures autonomy level, operational authority, permission exposure, governance maturity, and dependency concentration. The framework maps ...
  </details>

- **2026-07-14** — Saber Ganjisaffar, Chengyu Song, Nael Abu-Ghazaleh — [Microflow: Microarchitectural Causal Observability for Deep Cross-Layer Analysis and Optimization](http://arxiv.org/abs/2607.13184v1)
  <details><summary>📄 Abstract</summary>
  Existing architectural simulators expose aggregate metrics or raw traces, but fail to reveal complex interactions among microarchitectural events and their relationship to program execution. Consequently, architects observe performance symptoms but cannot systematically attribute them to root causes across abstraction layers. This paper introduces Microflow, an observability framework elevating causality to a first-class analytical object. Microflow transforms execution traces into the Microflow...
  </details>

- **2026-07-14** — Asmaa Abada, Claire Chevallier, Luighi P. S. Leal et al. — [Challenging Majorana neutrino effects in $B\to K^{(\ast)}νν$ and $K\to πνν$ decays](http://arxiv.org/abs/2607.13142v1)
  <details><summary>📄 Abstract</summary>
  We investigate the contributions of Lepton Number Violating (LNV) effective operators to the rare decays $B\to K^{(\ast)}νν$ and $K\to πνν$. Such operators can modify the kinematic distributions of these processes, providing distinctive probes of physics beyond the Standard Model. Through a renormalization-group analysis, we show that the Standard Model Effective Field Theory (SMEFT) operators responsible for these effects are subject to stringent indirect constraints from neutrino physics. In p...
  </details>

- **2026-07-14** — Tanmay Singla, James C. Davis — [Software Supply Chains are Dead: Use-Case-Oriented Regeneration](http://arxiv.org/abs/2607.13021v1)
  <details><summary>📄 Abstract</summary>
  Modern software development relies on an increasingly doubtful premise: that the up-front implementation savings from adopting a dependency outweighs the maintenance costs. Two changes are reshaping the build-vs.-reuse calculus: software supply chain attacks have raised the cost of external reliance, while generative AI has lowered the cost of local implementation. We envision use-case-oriented regeneration as a new software sourcing paradigm that shifts the supply chain from external trust to l...
  </details>

- **2026-07-14** — Héctor Carrión, Narges Norouzi — [Controllable Generation of Diverse Dermatological Imagery for Fair and Efficient Malignancy Classification](http://arxiv.org/abs/2607.12987v2)
  <details><summary>📄 Abstract</summary>
  Accurate dermatological diagnosis naturally necessitates equitable performance across diverse populations, yet a systematic lack of expertly annotated images, especially for underrepresented skin tones and rare diseases, impedes progress toward measurably fair methods. We introduce cgDDI (Controllable Generation of Diverse Dermatological Imagery), a hybrid framework that (1) synthesizes realistic healthy skin samples without disturbing other input properties, (2) maps single-sample rare lesions ...
  </details>

- **2026-07-14** — Mehmet Iscan — [Form, Not Content? A Preregistered, Placebo-Controlled Evaluation of Learned Error-Conditioned Self-Repair Through Prompts and Weights in Frozen Small Code Models](http://arxiv.org/abs/2607.12962v1)
  <details><summary>📄 Abstract</summary>
  Frozen small code LLMs are deployed locally, yet the information guiding a retry after a failed attempt is still measured without placebo controls in the self-repair literature. We treat a failed program as a conjecture and an execution counterexample as an oracle-relative refutation, and introduce PoPE (Popperian Placebo-controlled Evaluation): a methodology for measuring whether evidence that falsifies LLM-generated code can be used operationally by that same model. In PoPE, error content is p...
  </details>

- **2026-07-14** — Elnara Kadyrgali, Muragul Muratbekova, Pakizar Shamoi — [CD-MED: Cross-Domain Multimodal Emotion Descriptor for Visual Comparison of Digital Objects](http://arxiv.org/abs/2607.12958v1)
  <details><summary>📄 Abstract</summary>
  Digital objects express emotions through different modalities. For example, a movie may include visual scenes, audio, dialogue, and facial expressions, while a song may contain melody, rhythm, lyrics, and vocal tone. Because existing emotion recognition models are usually modality-specific, it is difficult to compare such objects directly. This paper proposes CD-MED, a Cross-Domain Multimodal Emotion Descriptor for representing heterogeneous digital objects in a common emotional space. Each moda...
  </details>

- **2026-07-14** — Sigma Jahan — [Toward Localizing and Repairing Bias in Transformer Attention Heads](http://arxiv.org/abs/2607.12863v1)
  <details><summary>📄 Abstract</summary>
  Transformer language models are increasingly used as software components, yet biased outputs remain difficult to localize and repair inside the model. Existing fairness testing and repair methods largely operate at the input-output or retraining level, while recent work suggests that bias-related behavior can concentrate in a small set of attention heads. This paper studies whether attention heads can be localized and repaired through a targeted inference-time intervention. We introduce ROBIN, a...
  </details>

- **2026-07-14** — Yize Mi, Jianan Li, Liang Li et al. — [Unveiling Complex Collective Behaviors from Simple Rewards](http://arxiv.org/abs/2607.12861v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent Reinforcement Learning (MARL) holds great potential for robot swarms, but the black-box nature of neural policies complicates strategic analysis, limiting multi-robot applications. Furthermore, complex swarm behaviors can surprisingly emerge from simple rewards without explicit aggregation incentives. Unveiling the mechanisms behind this emergence is critical, but the disconnection between simple rewards and collective behaviors exacerbates interpretability challenges. This paper aim...
  </details>

- **2026-07-14** — Hiroto Osaka, Shohei Taniguchi, Gouki Minegishi et al. — [Visual Access Boundaries in Vision-Language Model Reasoning](http://arxiv.org/abs/2607.12815v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) prompting is widely used as a test-time scaling strategy for Vision-Language Models (VLMs), but it remains unclear what is extended when VLMs generate longer reasoning traces. We ask whether CoT requires continued access to image tokens, or whether it mainly operates over visual information already made available earlier in the forward pass. We introduce Visual Access Sweep, a causal intervention that masks attention from generated-token queries to image-token keys along l...
  </details>

- **2026-07-14** — Viktor A. Lilja, Philippe Tassin — [Symmetry-Informed Deep Learning for Electromagnetic Scattering](http://arxiv.org/abs/2607.12810v1)
  <details><summary>📄 Abstract</summary>
  Deep learning can accelerate the modeling of electromagnetic devices by replacing costly simulations with neural networks trained to map design parameters to scattering parameters. However, data efficiency remains a central bottleneck, as training data is typically generated through expensive numerical simulations. Here we show that symmetry provides a powerful and largely untapped route to overcoming this limitation in electromagnetic scattering problems. Leveraging the equivariance of Maxwell'...
  </details>

- **2026-07-14** — Aleksei Bakin, Andrey V. Savchenko — [HSEmotion Team at the 11th ABAW Challenge: Multi-Task Learning and Ambivalence/Hesitancy Video Recognition](http://arxiv.org/abs/2607.12774v1)
  <details><summary>📄 Abstract</summary>
  This article presents our results for the 11th Affective Behavior Analysis in-the-Wild (ABAW) competition. For multi-task learning with simultaneous prediction of valence, arousal, facial expressions, and action units on s-Aff-Wild2 dataset, we use frozen lightweight facial extractors, MT-EmotiDDAMFN and MT-EmotiEffNet-B0, with separate heads and systematic post-processing: temporal Gaussian smoothing, per-class expression bias, AffectNet blending, per-AU threshold tuning, and weighted backbone ...
  </details>

- **2026-07-14** — Xingyu Dang, Haocheng Tang, Junmei Wang et al. — [Learning Mechanistic Reasoning for Chemical Reactions with Large Language Models](http://arxiv.org/abs/2607.12771v1)
  <details><summary>📄 Abstract</summary>
  Reaction mechanisms consist of the step-by-step sequences of elementary reactions that explain chemical transformations. Learning the mechanism logic is therefore essential for enhancing the fundamental chemical intelligence of large language models (LLMs). The stepwise deduction of reaction mechanism aligns naturally with the reasoning paradigms of reasoning LLMs. However, current chemical LLMs primarily emphasize coarse-grained name reactions for product prediction and retrosynthesis, often le...
  </details>

- **2026-07-14** — Sanjaya Paudel, Suk-Jin Yoon, Tek Prasad Adhikari et al. — [Tidal Grinding of Dwarf Galaxies in Cluster Environments](http://arxiv.org/abs/2607.12694v1)
  <details><summary>📄 Abstract</summary>
  Dwarf elliptical galaxies (dEs) dominate galaxy clusters and provide key constraints on environmentally driven galaxy evolution. Here we examine whether the projected shapes of dEs retain information about their accretion and transformation histories using a homogeneous sample of 1,108 bright (m_g < 19 mag) dEs in the Virgo cluster. Based on the axis-ratio (b/a), we define flat (< 0.70) and round (> 0.74) subsamples and compare their spatial and kinematic properties. We find that flat dEs are di...
  </details>

- **2026-07-14** — Mahmoud Elkarargy, Abdelaziz Rahwan, Abdelrahman Elsayed et al. — [Quantum PDE Solvers in Practice: Application-Driven Benchmarking of the Heat Equation](http://arxiv.org/abs/2607.12688v1)
  <details><summary>📄 Abstract</summary>
  Quantum PDE solvers are difficult to evaluate in practice because published studies use different discretizations, output models, reconstruction rules, and hardware assumptions. We present a reproducible, application-driven benchmark for the 1-D Dirichlet heat equation that compares eleven kernels under the same problem instances and readout contract. The benchmark covers coherent linear solvers (HHL, QSVT, and QLS-Fourier), VQLS, imaginary-time methods (QITE, var-QITE, and AVQDS), real-time Ham...
  </details>

- **2026-07-14** — Chengguang Gan, Zhixi Cai, Yunhao Liang et al. — [A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism](http://arxiv.org/abs/2607.12640v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards, and Group Relative Policy Optimization (GRPO) in particular, is now run routinely on a supervised checkpoint in the hope of producing a stronger agent. We ask whether it adds skill to a small language and vision-language model web agent at the 4B to 8B scale, or whether it mostly reshapes behavior the supervised model already has. Across a control grid of 18 runs that varies learning rate, KL weight, seed, initialization, and clipping, no configura...
  </details>

- **2026-07-14** — Sachin Dev Duggal, Pradyumna Swarnalatha Ramanna, Alexandros Vassiliades — [Atomic Units of X: The Compression Layer of Intelligence](http://arxiv.org/abs/2607.12634v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a theoretical framework for understanding intelligence as a process of atomic compression and compositional reuse. We argue that cognitive, biological, computational, and organizational systems achieve scalable intelligence by decomposing complex phenomena into reusable atomic units that can be recombined into higher-order structures. Drawing on evidence from cognitive science, information theory, evolutionary biology, software engineering, medicine, legal reasoning, educatio...
  </details>

- **2026-07-14** — Minh Khoi Ho, Zihao Zhu, Runchuan Zhu et al. — [Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making?](http://arxiv.org/abs/2607.12631v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) are increasingly deployed as autonomous agents in high-stakes domains, understanding contextual factors that may modulate their decision-making becomes critical. While LLMs are trained to perceive and resonate with users' emotions, it remains unclear whether induced emotion can influence their sequential decision-making. We investigate this question using the Iowa Gambling Task (IGT), a classic psychological paradigm for studying decision-making under uncertainty,...
  </details>

- **2026-07-14** — Yunxin Li, Jinchao Li, Shibo Su et al. — [KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill](http://arxiv.org/abs/2607.12625v2)
  <details><summary>📄 Abstract</summary>
  OpenClaw has emerged as a leading agent framework for complex task automation, yet it faces insufficient cross-platform GUI interaction support and a well-built self-evolution mechanism. These flaws limit its adaptation to diverse device ecosystems and prevent performance improvements through continuous learning from execution experience. To resolve these issues, we propose the Know Deeply, Act Perfectly paradigm for personal assistants, which holds that accumulated user interaction and task-run...
  </details>

- **2026-07-14** — Ryotaro Shimada, Yu-Chieh Lin, Yuji Nozawa et al. — [Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking for Zero-Shot Composed Image Retrieval](http://arxiv.org/abs/2607.12621v1)
  <details><summary>📄 Abstract</summary>
  Recent work has shown that "Vision-Free'' approaches (representing images as text) can be effective for standard image retrieval tasks. However, it remains unclear whether this paradigm can effectively handle a more complex, multimodal task, Composed Image Retrieval (CIR), due to the inherent information loss in textual descriptions. In this paper, we introduce a Vision-Free CIR framework that addresses this challenge through two key techniques: (1) Attribute-Augmented Hybrid Scoring, which comp...
  </details>

- **2026-07-14** — Ruocong Tang, Yang Huang, Xing Fang et al. — [Cheaper is Better: A Discount-Aware Network for Conversion Rate Prediction in E-commerce Recommendation System](http://arxiv.org/abs/2607.12578v1)
  <details><summary>📄 Abstract</summary>
  Post-click conversion rate (CVR) is a crucial element in online recommendation systems, which addresses significant challenges such as data sparsity (DS), sample selection bias (SSB), and delayed feedback. However, the impact of item discount rate-a key factor influencing both pricing and user purchasing behavior, has received limited attention. In this paper, we introduce the Discount-Aware Network (DANet) to model the relationship between item discount rates and CVR. DANet comprises three main...
  </details>

- **2026-07-14** — Kaixiang Shu — [From Preimage Search To Source-Grounded Feature Inversion](http://arxiv.org/abs/2607.12526v1)
  <details><summary>📄 Abstract</summary>
  Interpreting a neural network requires understanding what its internal features extract from a particular input. Feature inversion seeks to express a selected feature in the input domain, but canonical iterative methods search for an input whose re-encoded representation matches the target. Because many inputs can satisfy this constraint, target matching alone does not specify the inverse associated with the sample that generated the feature. We formulate source-grounded feature inversion by con...
  </details>

- **2026-07-14** — Junshi Chen, Xuhong Li, Russ Whiton et al. — [Cellular Signal Constructed Convolutional Vision Transformer for High Accuracy Positioning](http://arxiv.org/abs/2607.12518v1)
  <details><summary>📄 Abstract</summary>
  Modern cellular systems employ wide bandwidths and large antenna arrays to meet high data rate requirements. The high spatial and temporal resolution for communication also enables high-accuracy positioning as an ancillary benefit. Standard convolutional neural networks (CNNs) and vision Transformers have demonstrated excellent performance in positioning by leveraging delay-angle domain channel representations. However, they still face practical challenges in complicated cellular environments wi...
  </details>

- **2026-07-14** — Zhiyuan Liu, Yihe Li, Trevor E. Carlson et al. — [When is LLM-Based Program Reasoning Correct? A Completion Semantics for LLM-Based Code Inference](http://arxiv.org/abs/2607.12490v1)
  <details><summary>📄 Abstract</summary>
  Due to token and cognitive limits, Large Language Models (LLMs) typically perform program reasoning over incomplete code fragments/prompts rather than complete programs. Such reasoning therefore must rely on {assumptions about omitted code and context. As a result, the meaning of an inference over a program fragment is not absolute, but depends on an implicit completion model describing how the fragment may be refined into a complete program. In this paper, we introduce completion semantics for ...
  </details>

- **2026-07-14** — Ingmar Posner, Anson Lei, Bernhard Schölkopf — [From Observation to Insight: Mechanistic World Models and the Quest for Autonomous Discovery](http://arxiv.org/abs/2607.12474v2)
  <details><summary>📄 Abstract</summary>
  Recent advances in foundation models have transformed AI for Science, enabling remarkably accurate predictive performance across domains ranging from protein folding to weather forecasting. Yet prediction alone does not constitute scientific discovery. Scientific understanding depends on uncovering the reusable explanatory mechanisms that generate observations, whereas contemporary machine learning remains fundamentally organised around predictive mappings rather than explanatory structure. In t...
  </details>

- **2026-07-14** — Jinjian Wu, Jiaqi Tang, Wei Wei et al. — [IQA-T1: Tool-based Visual Evidence Reasoning for Image Quality Assessment](http://arxiv.org/abs/2607.12375v1)
  <details><summary>📄 Abstract</summary>
  Image Quality Assessment (IQA) in open-world environments remains challenging due to limited generalization and interpretability. Recent approaches based on multimodal large language models (MLLMs) introduce textual reasoning for quality prediction, yet their judgments rely heavily on semantically biased internal representations, making them insensitive to low-level perceptual degradations. We propose IQA-T1, a tool-based visual evidence reasoning framework that augments MLLM reasoning with expl...
  </details>

- **2026-07-14** — Shipeng Liu, Zhanping Song, Liang Zhao et al. — [Semantic-Edge Response Decoding of SAM3 for Zero-Shot Crack Segmentation](http://arxiv.org/abs/2607.12292v1)
  <details><summary>📄 Abstract</summary>
  Crack segmentation is essential for infrastructure inspection and structural health assessment, but existing high-performance methods typically require task-specific pixel-level annotations and training. Text-promptable vision foundation models enable zero-shot deployment, yet their final mask proposals are poorly suited to thin, fragmented, and low-contrast cracks, whose evidence may be suppressed, truncated, or over-expanded during mask generation. We find that language-conditioned semantic re...
  </details>

- **2026-07-14** — Chun-Yi Kuan, Hung-yi Lee — [The Sound of Absence: Audio-Language Embedding Models Struggle with Negation](http://arxiv.org/abs/2607.12290v1)
  <details><summary>📄 Abstract</summary>
  Audio-language embedding models such as CLAP are widely evaluated on matching present sound events, but rarely on negation. We show this affirmation-only evaluation hides a key limitation: these models fail to encode negated sound concepts, mapping affirmative and negated captions to nearly identical representations. To expose this blind spot, we introduce NegEval-Audio, a framework that converts existing datasets into two negation-aware tasks, Retrieval-Neg and Multiple-Choice Negation (MCQ-Neg...
  </details>

- **2026-07-14** — Siqi Wang, Xianjie Chen, Shaofeng Deng et al. — [SlimPer: Make Personalization Model Slim and Smart](http://arxiv.org/abs/2607.12281v1)
  <details><summary>📄 Abstract</summary>
  Transformer-style architectures are increasingly adopted for industrial recommendation systems, yet they inherit a design premise misaligned with the task: generative models rely on per-token autoregressive prediction, which justifies maintaining large intermediate tensors that scale with sequence length. In contrast, recommendation systems produce a single set of relevance scores for each <user, item> pair without token-level supervision. Leveraging this observation, we propose SlimPer, which r...
  </details>

- **2026-07-14** — Gendo Kumoi, Fumie Watanabe, Tota Suko et al. — [A Semi-Automated System for Generating Dialogue-Based TTS Lessons Using Large Language Models: An Exploratory Study of Educational Potential](http://arxiv.org/abs/2607.12235v1)
  <details><summary>📄 Abstract</summary>
  This study proposes a semi-automated system for generating dialogue-based lessons using Large Language Models (LLMs) and Text-to-Speech (TTS) technology, and exploratorily examines its educational potential via a practical quasi-experiment. The system augments rather than replaces educators through a three-stage human-in-the-loop workflow (LLM-based slide/narration generation, educator review, automated audiovisual integration), and introduces a novel method for generating Expert-Novice dialogue...
  </details>

- **2026-07-13** — Brenda Lelis, Rodrigo Cabral-Carvalho — [RCWT: Measuring Task-Budget Displacement from Coordination Content in LLM Calls](http://arxiv.org/abs/2607.12216v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent and memory-augmented LLM systems often place coordination content, shared state, prior discussion, tool outputs, summaries, and role instructions, inside the same finite prompt used for the current task. This creates a practical allocation problem: every token spent on coordination is unavailable to task instructions or evidence when a call is assembled under a fixed context budget. We introduce the Roundtable Context Window Test (RCWT), a controlled protocol for measuring this task-...
  </details>

- **2026-07-13** — Rasiq Hussain, Darshil Italiya, Joshua Oltmanns et al. — [Fine-Tuned Multi-Agent Framework for Detecting OCEAN in Life Narratives](http://arxiv.org/abs/2607.12215v1)
  <details><summary>📄 Abstract</summary>
  Accurately assessing personality from text is challenging because traits are latent, context-dependent, and often subtly expressed across long narratives. Large language models (LLMs) offer new opportunities by processing extensive textual contexts, but pretraining of these models can induce latent "personality-like" biases, making single-model inferences inconsistent. We propose a fine-tuned multi-agent framework for detecting OCEAN personality traits, in which sub-agents are conditioned to ado...
  </details>

- **2026-07-13** — Jiahao Luo, Hao Zhang, Jianqi Chen et al. — [RegHead: Non-Humanoid Head Blendshapes via Feed-Forward Registration](http://arxiv.org/abs/2607.12206v1)
  <details><summary>📄 Abstract</summary>
  We present RegHead, a framework for constructing semantic blendshape sets for animatable non-humanoid head avatars. With a fixed expression vocabulary, semantic blendshapes provide a low-dimensional and interpretable animation interface and support cross-identity retargeting. Building such blendshape sets remains expensive because (i) expression-consistent supervision is scarce, (ii) generated 4D assets typically lack correspondence, and (iii) facial motion is highly localized. We propose (1) a ...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 549 |
| prompt-injection | 457 |
| memory-poisoning | 36 |
| tool-use-attack | 93 |
| backdoor | 390 |
| adversarial-attack | 533 |
| privacy-leakage | 3692 |
| steganography | 52 |
| misuse | 823 |
| red-teaming | 108 |
| vulnerability | 2462 |
| defense | 2111 |
| alignment | 1933 |
| robustness | 1824 |
| watermark | 196 |
| unlearning | 82 |
| agent-safety | 48 |
| benchmark | 53 |
| survey | 252 |
| other | 5500 |

---

📚 **全部 21194 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-07-29 16:40:26*