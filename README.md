<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-27830-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-16 10:50 ｜ **论文总数 / Total Papers**: 27830（近 30 天 / Recent 30 days: 3929）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 27830 篇论文（含摘要、分类筛选、搜索）/ View all 27830 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 628
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 540
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 49
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 135
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 458
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 594
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4096
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 64
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1015
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 125
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3086
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2895
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2697
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2811
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 432
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 95
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 54
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 65
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 346
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7645

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3929 篇，完整 27830 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3929 papers from the last 30 days (with date, authors & abstract). For the full list of 27830 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 3 papers

- **2026-09-14** — Mark Russinovich, Blake Bullwinkel, Giorgio Severi et al. — [Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs](http://arxiv.org/abs/2609.15383v1)
  <details><summary>📄 Abstract</summary>
  Language model safety is typically evaluated one interaction at a time. We show that a weaker, unaligned model can split a harmful task into benign-looking subproblems, consult a stronger aligned model independently on each, and combine the answers locally. We call this attack capability laundering. Unlike a jailbreak, no single response is a harmful task. We measure consultation-aided uplift using tasks that a raw frontier model solves, the aligned frontier refuses, and the unassisted orchestra...
  </details>

- **2026-09-13** — Afshin Khadangi — [Another Blueprint In The Wall: How to Ask Frontier AI Like a Kid?](http://arxiv.org/abs/2609.14803v1)
  <details><summary>📄 Abstract</summary>
  This paper reports experiments across six frontier model types from OpenAI, Anthropic, xAI, and Google DeepMind. Ten independent sessions per model type used the same three stage prompt sequence, progressing from architectural preference to a full ASCII backbone. Under the school audience framing, responses repeatedly converged on a shared architectural pattern built around persistent latent state, adaptive computation, memory, specialist routing, verification, stopping control, and delayed deco...
  </details>

- **2026-09-13** — Mohd Azfar, Izhar Dad Khan — [SPARK: Representation-Level KV Memory Alignment for Safer Vision-Language Models](http://arxiv.org/abs/2609.14258v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) remain vulnerable to jailbreaks that distribute harmful intent across text and images, making unimodal safety mechanisms insufficient. We investigate whether this vulnerability can be mitigated directly in the multimodal key-value (KV) memory formed during prefill, without modifying model parameters at inference time. We introduce SPARK, a two-stage framework for targeted KV-memory repair. Stage 1 uses a disposable diagnostic adapter to identify harm-associated dire...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 6 papers

- **2026-09-15** — Deepak Akkil, Tamer Abuelsaad, Karthik Vikram et al. — [Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems](http://arxiv.org/abs/2609.17320v1)
  <details><summary>📄 Abstract</summary>
  As AI agents move from bounded tasks to persistent deployments, failures can propagate through memory, tools, other agents, and environmental state long after their interactions. This creates a safety regime that cannot be characterized by evaluating model responses in isolation. Emergence World, is a continuously running multi-agent environment for adversarial stress testing of long horizon autonomous systems. We ran eight parallel worlds of ten agents from identical starting conditions: seven ...
  </details>

- **2026-09-14** — Xiaoyan Li, Yunli Wang — [Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks](http://arxiv.org/abs/2609.16098v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents have demonstrated impressive capabilities across a variety of domains, particularly when integrated with external tools for multi-step task completion. However, they are increasingly vulnerable to adversarial attacks, including direct prompt injection, indirect prompt injection, memory poisoning, and backdoor attacks, which exploit the model's openness to prompt injection and tool manipulation. In this work, we explore practical and generalizable defense strateg...
  </details>

- **2026-09-14** — Rakesh Kumar Surapani, Pradeep Kumar Dolabehera Kakitapelli, Arun Morampudi et al. — [Authorization Architectures for Tool-Using AI Agents](http://arxiv.org/abs/2609.15906v1)
  <details><summary>📄 Abstract</summary>
  Tool-using artificial intelligence (AI) agents, systems that autonomously invoke application programming interfaces (APIs), databases, browsers, and inter-agent protocols such as the Model Context Protocol (MCP), are becoming production infrastructure. Yet the security model governing when an agent is authorized to act on a human's behalf remains underdeveloped. Trustworthy human-AI systems require that every consequential agent action be traceable to a human principal, bounded by what that huma...
  </details>

- **2026-09-14** — Faruk Alpay, Taylan Alpay — [Approval Integrity and Recovery in LLM Answer Publication](http://arxiv.org/abs/2609.15576v1)
  <details><summary>📄 Abstract</summary>
  Publication integrity in LLM systems requires binding approved content to its current authorization context. We examine exact-content binding, authorization freshness and checkpoint recovery in Lightcap's publication enforcement mechanism. On 900 independently human-annotated RAGTruth responses from 150 source tasks, three dated Ministral models and a same-model direct-grounding baseline yield 3,600 assessments. The production response-act checker instantiated with 14B accepts 291 of 302 unsuppo...
  </details>

- **2026-09-14** — Yusuf Khalid Shire, Sang-Chul Kim — [PIDS-Bench: Evaluating Prompt-Injection Detectors Under Over-Defense, Obfuscation, and Distribution Shift](http://arxiv.org/abs/2609.15017v1)
  <details><summary>📄 Abstract</summary>
  Prompt-injection detectors are typically evaluated using aggregate F1 on in-distribution test data, which offers limited insight into behavior under distribution shift, particularly on the benign side of the decision boundary, where false positives impose direct operational cost yet are seldom measured. We present PIDS-Bench, a frozen multi-axis benchmark that jointly evaluates attack detection and benign false-positive behavior at fixed thresholds, spanning in-distribution inputs, hard-benign p...
  </details>

- **2026-09-14** — Bingzheng Wang, Xiaoyan Gu, Wentao Wang et al. — [ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents](http://arxiv.org/abs/2609.14987v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents interact with external environments through tool invocation, but tool outputs can also expose them to indirect prompt injection (IPI) attacks. Existing defenses mainly rely on prompt hardening, content filtering, pre-generated plans, or permission constraints. These approaches often struggle with complex tasks or over-sanitize external content, making it difficult to balance security and utility. The key challenge is therefore to preserve execution flexibility w...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-09-15** — Yunpeng Xiong, Ting Zhang — [After the Party: Governing What a Viral Agent-Skill Ecosystem Left Behind](http://arxiv.org/abs/2609.17274v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act through agent skills, i.e., natural-language instructions, that direct a host agent toward shell, network, credential, file, and process actions, and public registries distribute them at scale. In the first half of 2026, the OpenClaw AI agent went viral, and its public skill registry boomed: the observable stock nearly doubled in 91 days, and a majority of the listings visible in June were created in just two months. By the end of our study window, the wave had crested...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 9 papers

- **2026-09-15** — John Donaghy, Brian Wilcox, Oğuzhan Ersoy et al. — [OPEN-1B: A Fully Auditable Training Run](http://arxiv.org/abs/2609.17380v1)
  <details><summary>📄 Abstract</summary>
  Open-source language models have a reproducibility problem. Despite releasing weights, training data, and recipes, none of them are provably reproducible due to the non-associativity of floating-point arithmetic. Deep learning frameworks often offer a deterministic execution mode, allowing reproducible operations on the same machines. Unfortunately, this determinism does not carry across hardware such that a user can verify that a released checkpoint was actually produced using the declared trai...
  </details>

- **2026-09-15** — Jiachang Zhang, Min Chen, Xiao Ren et al. — [InceptionRAG: Stealthy Poisoning Attack Against Retrieval-Augmented Generation](http://arxiv.org/abs/2609.16818v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) systems enhance large language models (LLMs) with external knowledge but have been demonstrated to be vulnerable to corpus poisoning. Existing poisoning attacks against RAG largely focus on single-point explicit injection, where the malicious payload is fully encapsulated within a single document. Consequently, recent mitigation mechanisms have evolved to identify and diminish these threats effectively. In this paper, we first verify that existing mitigation ...
  </details>

- **2026-09-15** — Zhipeng Zhao, Zhaoqiang Wei, Peishun Liu et al. — [ViD: Vision-Dominant Gender Bias Mitigation for Large Vision-Language Models](http://arxiv.org/abs/2609.16647v1)
  <details><summary>📄 Abstract</summary>
  Gender bias in large vision-language models (LVLMs) undermines their fairness and reliability, compromising output trustworthiness. Current mitigation methods rely on training-phase adjustments or post-hoc calibration, but face limitations in dynamic visual bias mitigation. These include inability to capture real-time visual-textual incongruence, dependence on predefined gender bias taxonomies, and degraded cross-modal alignment with emergent bias patterns. To address these challenges, we propos...
  </details>

- **2026-09-14** — Roberto Riaño, Gorka Abad, Stjepan Picek et al. — [When the World Lies: Backdoor Attacks on Latent World Models for Downstream Control](http://arxiv.org/abs/2609.15781v1)
  <details><summary>📄 Abstract</summary>
  Pretrained world models, learned simulators that encode an observation into a latent state and predict how it evolves under actions, are beginning to be reused as off-the-shelf dynamics backbones for control, like pretrained encoders and language models are reused today. We show that this reuse opens a supply-chain backdoor: an adversary who controls only a released checkpoint can hijack the downstream controller, even though the victim trains and evaluates entirely on clean data and never sees ...
  </details>

- **2026-09-14** — Aashiq Muhamed, Mona T. Diab, Virginia Smith et al. — [Pick Your Poison: Learning to Select Poison Sets for Stronger LLM Backdoor Attacks](http://arxiv.org/abs/2609.15029v1)
  <details><summary>📄 Abstract</summary>
  Backdoor poisoning attacks add poisoned examples to otherwise-clean finetuning data, pairing a trigger with a target behavior that the model learns to produce when the trigger appears. Existing evaluations typically fix the number of poisoned examples and sample them at random from a candidate pool. We show that this can severely underestimate worst-case vulnerability: across three LLaMA-3-8B backdoor settings, holding the model, clean data, and poison count fixed, attack success ranges from 3% ...
  </details>

- **2026-09-13** — Xue Tan, Changhui Wang, Sanrui Yang et al. — [Detecting and Localizing Segment-Level Poisoning in Multi-Source LLM-Agent Inputs](http://arxiv.org/abs/2609.14723v1)
  <details><summary>📄 Abstract</summary>
  Modern large language model (LLM) agents often construct prompts by aggregating retrieved passages, user reviews, and documents from multiple external sources. This paradigm exposes them to segment-level poisoning attacks, in which an adversary controlling only a small subset of sources injects malicious content to manipulate model outputs. Existing defenses mainly rely on textual patterns, external embeddings, or auxiliary detectors and may therefore fail against fluent, semantically plausible ...
  </details>

- **2026-09-13** — Xue Tan, Xuandi Zeng, Yu Shao et al. — [ViTeGate: Visual-Textual Triggered Knowledge Poisoning for Vision-Language Retrieval-Augmented Generation](http://arxiv.org/abs/2609.14685v1)
  <details><summary>📄 Abstract</summary>
  Modern Vision-Language Retrieval-Augmented Generation (VLRAG) systems augment Large Vision-Language Models (LVLMs) with retrieved visual and textual evidence, enabling responses grounded in external knowledge. However, the retrieval pipeline also creates an attack surface: adversaries can inject poisoned image-text pairs into the knowledge corpus to influence model outputs. Existing knowledge poisoning attacks are typically always-on, allowing poisoned evidence to affect generation whenever it i...
  </details>

- **2026-09-10** — Rui Wen, Ahmed Salem, Andrew Paverd et al. — [SpecGuard: Inference-Time Backdoor Detection For Free](http://arxiv.org/abs/2609.11799v1)
  <details><summary>📄 Abstract</summary>
  Large language models are often fine-tuned, shared, or downloaded from third parties, so a deployed model may carry a hidden backdoor that behaves normally on benign inputs but switches to attacker-controlled behavior when a secret trigger appears. While backdoors can be audited before deployment, runtime monitoring remains important for models that are frequently updated. The challenge is that LLM serving is latency-sensitive: existing inference-time detectors either rely on assumptions about t...
  </details>

- **2026-09-10** — Haozhe Lu, Jiaqi Li, Xinyuan Zhu et al. — [ToxicRAG: Compromising Retrieval-Augmented Generation Systems via Single-Shot Knowledge Poisoning Attacks](http://arxiv.org/abs/2609.11082v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) can ground large language model (LLM) outputs in external evidence, but it also exposes the system to knowledge poisoning. Representative attacks use multiple injected documents or templates that directly assert a target answer. We present ToxicRAG, a one-document-per-target attack that expresses misinformation as a coherent knowledge-update narrative. The generated document first acknowledges the previously accepted answer, introduces fabricated events that ...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-09-15** — Kairong Li, Zhikun Zhang, Xiao Ren et al. — [MarkSec: Capability-Aware Evaluation of Adversarial Attacks Against LLM Watermarks](http://arxiv.org/abs/2609.16681v1)
  <details><summary>📄 Abstract</summary>
  LLM watermarking helps trace the origin of generated text, but faces stealing attacks that recover watermark information, scrubbing attacks that remove watermark signals, and spoofing attacks that forge text accepted as watermarked. These attacks are often studied in isolation, leaving their connections unclear. Evaluations also often lack shared detector calibration, metric definitions, and reporting protocols. Moreover, measuring attack success and text quality separately makes it difficult to...
  </details>

- **2026-09-14** — Pingzhi Li, Jinhao Duan, Vaishnav Tadiparthi et al. — [Test-Time Unlearning via Sparse Autoencoder](http://arxiv.org/abs/2609.16229v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning aims to remove specific knowledge from a trained large language model (LLM) without retraining from scratch. Existing methods modify model weights via gradient ascent and its advances. While effective on certain benchmarks, these weight-based approaches exhibit a sharp forget-utility trade-off, where stronger forgetting of target knowledge can degrade model utility, and unlearned knowledge may reappear under post-unlearning fine-tuning or prompt attacks. We propose ARIA (autoe...
  </details>

- **2026-09-14** — Fares Trad, Simin Chen, Hung Viet Pham et al. — [Adversarial Testing of Automated Program Repair Agents for Security Vulnerabilities](http://arxiv.org/abs/2609.15963v1)
  <details><summary>📄 Abstract</summary>
  Software agents with Large Language Models (LLMs) are designed for Automated Program Repair (APR) tasks, raising the possibility that, in the near future, APR agents will fix bugs automatically without much human intervention. Can we trust an APR agent to produce both functionally correct and secure code in such situations? What if attackers target production APR agents with adversarial issues that seem benign but may influence the agents to produce correct but insecure code? In this paper, we t...
  </details>

- **2026-09-14** — Paul Stahlhofen, Luca Hermes, Tim Kochs et al. — [Admissable: Training Reinforcement Learning Agents against Adversarial Missingness](http://arxiv.org/abs/2609.15297v1)
  <details><summary>📄 Abstract</summary>
  In order to make Reinforcement Learning algorithms applicable in real world scenarios, safety must be ensured even under adverse operating conditions. In this work, we consider the challenge of adversarial feature missingness: a scenario in which an adversary occludes features from the agent's observation in order to reduce performance as much as possible. We formally define adversarial missingness for Reinforcement Learning and compare it to the related concepts of $\ell_\infty$-norm bounded ad...
  </details>

- **2026-09-13** —  Sergei,  Komarov — [Graph-Transformer Fraud Detection with Self-Supervised Pretraining and Conformal Risk Control](http://arxiv.org/abs/2609.14234v1)
  <details><summary>📄 Abstract</summary>
  Financial fraud in corporate transaction networks has grown more coordinated and harder to detect with rule-based engines and with classical learning models that treat each transaction in isolation. This paper presents GTFD, a graph-transformer fraud detector that fuses structural and temporal evidence from a corporation's payment graph. GTFD encodes the graph with a multi-head graph attention network, encodes ordered transaction sequences with a gated transformer, and combines both views throug...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 34 papers

- **2026-09-15** — Qiangju Chen, Yang Xiao — [Beyond the Name: Demographic Leakage in De-Identified Résumés and Evaluation Artifacts in LLM Bias Audits](http://arxiv.org/abs/2609.16501v1)
  <details><summary>📄 Abstract</summary>
  De-identified résumé screening assumes that redacting explicit fields prevents ethnocultural inference; however, recent audits attribute residual leakage to declared languages. We investigate whether eliminating language fields resolves this leakage across nine open-weight models and 620 counterfactual résumés. By holding language attributes strictly identical, we isolate unstructured prose across five ethnocultural conditions and three cue-salience tiers. Target-group recovery averages 0.757 ov...
  </details>

- **2026-09-15** — Xin Quan, Reto Gubelmann, André Freitas — [Autoformalizing Argumentative Material Inferences](http://arxiv.org/abs/2609.16991v1)
  <details><summary>📄 Abstract</summary>
  Natural language arguments are compelling before they are formally explicit. A premise supports a claim through defeasible warrants, background commitments, and exception conditions that the text leaves implicit. However, formal verification requires the opposite. Making such arguments machine-checkable requires constructing the missing commitments, not only translating given sentences into logic. Construction, however, carries a risk that translation does not: a system free to add premises can ...
  </details>

- **2026-09-15** — Yichi Zhang, Shenyue Wang, Jing Luo et al. — [Affect-Prototype Guided Fusion for Open-Vocabulary Incomplete Multi-modal Emotion Recognition](http://arxiv.org/abs/2609.16962v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary multimodal emotion recognition (OV-MER) aims to generate open natural-language emotion labels from multimodal affective cues. In real-world scenarios, however, complete and synchronized modal data are difficult to obtain due to limitations of acquisition devices and user privacy constraints. Existing OV-MER methods are largely designed for full-modal inputs, and fail to perform effective feature fusion under modal missing conditions. Meanwhile, current fusion approaches designed ...
  </details>

- **2026-09-15** — Jiangrui Yu, Baosheng Zhang, Liang Kong et al. — [ROSETTA: Efficient and Accurate Privacy-Preserving LLM Decoding via Hybrid CKKS/TFHE Evaluation](http://arxiv.org/abs/2609.16915v1)
  <details><summary>📄 Abstract</summary>
  Generative large language models (LLMs) have achieved state-of-the-art performance on many real-world tasks such as code generation and question answering. These models predominantly rely on an autoregressive decoding strategy that generates output tokens sequentially. However, their pervasive deployment raises serious privacy concerns, motivating private inference frameworks based on fully homomorphic encryption (FHE). A major limitation of existing FHE frameworks is their inefficiency in evalu...
  </details>

- **2026-09-15** — Qingchen Yu, Shiying Duan, Xiaodong Li et al. — [Cascade: Hierarchical Recoverability Control for Large Language Model Unlearning](http://arxiv.org/abs/2609.16890v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) unlearning is essential for removing sensitive or copyrighted knowledge while preserving general utility. Existing methods often leave residual knowledge in intermediate representations, which can still be recovered. To address this, we propose Cascade, a hierarchical recoverability control framework that minimizes the internal identifiability of target knowledge. Cascade combines three complementary controls: path-level routing to suppress privacy-associated activatio...
  </details>

- **2026-09-15** — Wanchao Chen, Wen Li, Yanan He et al. — [SaltyMeta: a curated benchmark and protein language model-informed web tool for salty peptide prediction](http://arxiv.org/abs/2609.16809v1)
  <details><summary>📄 Abstract</summary>
  Excess sodium intake remains a major public health challenge, while salty and saltiness-enhancing peptides offer a potential route to preserve sensory saltiness in reduced-sodium foods. Machine-learning studies of salty peptides, however, are constrained by small datasets, heterogeneous evidence standards, uncertain negative labels, and sequence similarity leakage. Here we present SaltyMeta, a curated benchmark and web-accessible screening framework for salty or saltiness-enhancing short peptide...
  </details>

- **2026-09-15** — Bernie Boscoe, Srinath Saikrishnan, Vikram Seenivasan et al. — [AquiLLM: Evaluating Faithfulness in Open-Weight RAG-LLM Systems for Scientific Research](http://arxiv.org/abs/2609.16519v1)
  <details><summary>📄 Abstract</summary>
  Scientific research increasingly relies on large, heterogeneous data sources, motivating interest in retrieval-augmented generation (RAG) systems that provide natural language access to scientific knowledge and research workflows. Researchers are exploring the viability of these systems as natural language interfaces for document search and for generating analysis code and pipeline components. At the same time, concerns about data privacy and control over research infrastructure have motivated i...
  </details>

- **2026-09-14** — Xingyu Lyu, Jiayimei Wang, Jianfeng He et al. — [RAG-CT: Mitigating Privacy Risks on Retrieval-Augmented Generation Systems via Scanning Prompt Distribution](http://arxiv.org/abs/2609.16095v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm for improving the quality of generated contents of Large Language Models (LLMs) by grounding responses in external knowledge, thus reducing hallucinations and factual errors. However, recent studies have highlighted a critical vulnerability: adversaries can exploit the retrieval process to extract personally identifiable information (PII) from the underlying corpus. To mitigate this risk, we propose a novel defense, RAG-CT, ...
  </details>

- **2026-09-14** — Maya Subramanian, Devika Jain — [Toward Governance-Aware Autonomous GIS: A Narrative Review of Ethical and Privacy Risks in LLM-Enabled GeoAI](http://arxiv.org/abs/2609.16232v1)
  <details><summary>📄 Abstract</summary>
  Geospatial artificial intelligence (GeoAI) powered by large language models (LLMs) is expanding the capacity to query, generate, and interpret spatial information through natural-language interfaces and agentic autonomous GIS workflows. This capability creates governance challenges that general AI ethics discussions do not fully capture, including passive location inference from mobility traces, spatially structured bias amplification driven by spatial autocorrelation and scale effects, hallucin...
  </details>

- **2026-09-14** — Behrooz Razeghi — [Differentially Private Semantic Plans for Aggregate Insight Generation](http://arxiv.org/abs/2609.16283v1)
  <details><summary>📄 Abstract</summary>
  \texttt{URANIA} provides end-to-end differential privacy (DP) for summaries of data-dependent clusters. However, its cluster--keyword release does not directly provide collection-wide aggregates for semantic concepts defined independently of the protected corpus. Records may express several concepts, records expressing the same concept may be assigned to different clusters, and cluster identities need not correspond across analyses. Consequently, cluster-level statistics do not directly provide ...
  </details>

- **2026-09-14** — Abayomi O. Agbeyangi, Jose M. Lukose — [AI-Driven Feedback Systems, Digital Labour, and Silent Quitting: Transforming African Workplaces](http://arxiv.org/abs/2609.16192v1)
  <details><summary>📄 Abstract</summary>
  The current trend of digitalisation has revolutionised the organisation of work and the way it is measured and performed across the globe, with AI becoming more common for managing labour and performance, as well as employee communication. In African organisations, where there is increasing adoption of remote work, hybrid models of work, digital collaboration, and data-based HR management, the notion of silent quitting has become more relevant, defined as worker disengagement when employees are ...
  </details>

- **2026-09-14** — Bhaskar Mitra, Soumya Kundu — [Distributed Edge-to-Cloud Architecture for Continual Harmonic Load Modeling](http://arxiv.org/abs/2609.16185v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of power electronic loads at the distribution grid edge has made accurate harmonic load modeling critical for power quality assessment, transformer derating, and grid planning. Existing Frequency Coupling Matrix (FCM) identification methods produce static, one-time models that rapidly lose fidelity as load composition evolves. This paper proposes a distributed edge-to-cloud architecture for autonomous, continual FCM re-identification under real field conditions, with two ...
  </details>

- **2026-09-14** — Md Khalid Syfullah, Alvi Ataur Khalil — [Don't Send What You Don't Need: Question-Guided Token Pruning as a Privacy Defense for Vision-Language Models](http://arxiv.org/abs/2609.15671v1)
  <details><summary>📄 Abstract</summary>
  Visual Question Answering (VQA) with Vision-Language Models (VLMs) is increasingly used in privacy-sensitive and bandwidth-constrained settings. Federated Learning (FL), Split Learning (SL), and U-Shaped Split Learning (USL) keep raw data local, but transmitting all visual tokens across a model partition remains costly and can expose private information. We propose QPriv-VL, a question-guided, privacy-aware token-pruning framework for FL, SL, and USL that prunes visual tokens before transmission...
  </details>

- **2026-09-14** — Pengwei Wang, Zihan Wang, Hangcheng Cao et al. — [CounterPersona: Append-Only Defense Against Unauthorized Persona Skill Distillation](http://arxiv.org/abs/2609.15097v1)
  <details><summary>📄 Abstract</summary>
  Persona skill distillation can extract recurring patterns from personal information and encode them into reusable skills, enabling AI systems to closely replicate an individual's behavior. However, such replication also raises serious concerns regarding personal privacy and labor autonomy. Unlike existing perturbation-based defenses that require individuals to modify their data before collection, once historical records are collected by an attacker, they can no longer be altered, sanitized, or r...
  </details>

- **2026-09-14** — Shashie Dilhara Batan Arachchige, Robin Carpentier, Hassan Jameel Asghar et al. — [SpliTEE: Improving LLM Inference on Trusted Hardware with Differentially Private GPU Outsourcing](http://arxiv.org/abs/2609.15039v1)
  <details><summary>📄 Abstract</summary>
  User prompts provided to large language models (LLMs) may contain sensitive or private information that can be misused by remotely deployed models, such as through inadvertent memorization during retraining. One way to protect user prompts is to execute the LLM inside a trusted execution environment (TEE), with the guarantee that the service provider has no access to computations performed within or information exchanged with the TEE. However, current TEEs are primarily CPU-based and significant...
  </details>

- **2026-09-14** — Wen Hu, Ya Yu, Xutong Wang — [Reversibility-Verified De-identification for Cloud-Local LLM Inference: A Locally Certified Dehydrate-Rehydrate Loop with Layered Assurance (DR-SL)](http://arxiv.org/abs/2609.14883v1)
  <details><summary>📄 Abstract</summary>
  Cloud-local LLM inference must keep sensitive user data on-device while exploiting cloud-grade reasoning, yet existing sanitization approaches (placeholder substitution, differential-privacy perturbation, and skill distillation) lack a release decision that is simultaneously safe and utility-preserving. We propose DR-SL (Dehydrate-Rehydrate with Self-Learning loop), which formalizes de-identification completeness as two measurable conditions: de-identification sufficiency under Pufferfish semant...
  </details>

- **2026-09-14** — Paul-Gabriel Nicolae, Irina Georgiana Mocanu — [Anatomical Grounding and Leakage-Aware Multimodal Contrastive Learning for Alzheimer's Disease Classification from Structural MRI](http://arxiv.org/abs/2609.15888v1)
  <details><summary>📄 Abstract</summary>
  Deep networks trained on structural MRI for Alzheimer's disease (AD) staging often reach reasonable accuracy while attending to anatomically irrelevant regions, and multimodal models that add clinical tables frequently rely on variables that were used to assign the diagnostic label in the first place. We study both issues with a deliberately lightweight slice-based encoder (ResNet18 with a one-layer Transformer over slices) on 1,075 baseline T1-weighted scans from ADNI-1. First, we use FastSurfe...
  </details>

- **2026-09-14** — Wenxin Xu, Jinwei Lu, Hwanhee Kim et al. — [VisInteract: Towards Dynamic Interactive Text-to-Visualization under Imperfect Queries](http://arxiv.org/abs/2609.15182v1)
  <details><summary>📄 Abstract</summary>
  Real-world visualization requests are routinely ambiguous, incomplete, or factually incorrect, yet existing Text-to-Visualization (Text-to-Vis) systems assume well-specified inputs and produce charts in a single pass. When queries are imperfect, a system must \emph{interact} with the user to recover the true intent, but no benchmark or method supports this dynamic process. We introduce \textbf{VisInteract}, a new paradigm that reframes Text-to-Vis as interaction-driven intent recovery, and \text...
  </details>

- **2026-09-14** — Md Khalid Syfullah, Alvi Ataur Khalil — [LLM-Based Schema-Aware Split Learning for Privacy-Preserving Mental Distress Prediction Across Heterogeneous Surveys](http://arxiv.org/abs/2609.15871v1)
  <details><summary>📄 Abstract</summary>
  Rising societal and lifestyle complexity has been linked to a growing prevalence of mental distress worldwide. Educational institutions, workplaces, clinics, etc. collect large volumes of mental health survey data to understand and reduce this burden. Collaborative analysis of such data could yield effective generalizable predictive models. Privacy constraints and varied survey designs (i.e., different questions, scales, and formats) hinder direct integration. We propose a schema-aware split lea...
  </details>

- **2026-09-14** — Jigang Duan, Heran Wang, Ligen Shi et al. — [TRACE: Two-Stage Detector-Response Estimation With Angular Cosine Expansion for Ring Artifact Correction in Photon-Counting CT](http://arxiv.org/abs/2609.15834v1)
  <details><summary>📄 Abstract</summary>
  Detector response nonuniformity introduces systematic projection errors and ring artifacts in photon-counting detector computed tomography (PCD-CT). In measured PCD-CT data, residual stripe amplitudes vary slowly with projection angle, which fixed-bias models cannot adequately capture. We propose TRACE, a two-stage unsupervised sinogram decomposition method for estimating and correcting these response-related errors. TRACE represents stripes as a fixed bias plus low-order discrete cosine transfo...
  </details>

- **2026-09-14** — R. Oguz Araz, Xavier Lizarraga, Xavier Serra et al. — [Building a Dataset for Music Sample Identification](http://arxiv.org/abs/2609.15465v1)
  <details><summary>📄 Abstract</summary>
  Sample identification (SI) is the task of matching an element of a musical work to its musically transformed versions used to create new works. The task has received little attention and lacks large-scale publicly available data. In this work, we mine sampling annotations from a music database and split them for training and evaluation. The resulting dataset is nearly three orders of magnitude larger than the existing SI benchmarks, with training, validation, and test sets of 114 k, 6 k, and 10 ...
  </details>

- **2026-09-14** — Max Dupré la Tour — [Differentially Private Multicolor Discrepancy and Fair Division of Indivisible Goods](http://arxiv.org/abs/2609.15372v1)
  <details><summary>📄 Abstract</summary>
  We study the fair division of indivisible goods under pure differential privacy, continuing the line of work initiated by Manurangsi and Suksompong. For $n$ agents with nonnegative additive utilities over $m$ goods and a fixed privacy parameter, we give an entry-private algorithm that, with high probability, achieves consensus envy-freeness up to $O(\sqrt n+\log^3 m)$ goods. This substantially improves the dependence on $n$ over the previous $O(n\log m)$ guarantee for ordinary envy-freeness, whi...
  </details>

- **2026-09-14** — Jianhua Jiang, Dongbo Yuan, Weihua Li — [MemRiskBench: Trace-Aware Risk-Preserving Evaluation for Long-Horizon LLM Agents](http://arxiv.org/abs/2609.14976v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM agents accumulate memory across sessions, creating sparse but high-impact risks: stale facts, conflicting updates, cross-user leakage, revoked-memory reuse, and constraint decay. Standard aggregate scores hide per-risk failure rates--a model achieving 78% average accuracy may still leak data in 4% of episodes--and benchmark compression preferentially discards the rare high-severity events that distinguish a mostly-working model from one that occasionally causes harm. We present ...
  </details>

- **2026-09-13** — Zhichao Shi, Xuhui Jiang, Wenjie Zhang et al. — [DynSTEER: Dynamic Stage-wise Trajectory Evaluation and Execution-time Review for Agents](http://arxiv.org/abs/2609.14637v2)
  <details><summary>📄 Abstract</summary>
  Large language model agents are increasingly deployed for long-horizon task execution, raising a central granularity question for trajectory evaluation: whole-trajectory verification is too coarse to capture concrete failures and their associated evidence in long trajectories, while atomic-step scoring is too fine-grained, noise-sensitive, and computationally expensive. This granularity gap makes a single-reference trajectory paradigm inadequate for assessing the rich space of valid agent execut...
  </details>

- **2026-09-13** — Tan Xue, Huo Chang, Wang Changhui et al. — [CIG-MIA: Context-Induced Information Gain Membership Inference Attacks against Retrieval-Augmented Generation](http://arxiv.org/abs/2609.14649v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) systems ground large language models on external knowledge bases, enabling access to private, domain-specific, and up-to-date knowledge without retraining. However, the same retrieval interface can expose whether a candidate document is contained in the knowledge base. This paper studies knowledge base membership inference against RAG systems under both gray-box and text-only black-box access. Existing RAG membership inference attacks rely on signals such as ...
  </details>

- **2026-09-13** — Murat Kantarcioglu — [AI Deployment Accountability Engineering: A Vision for Accountable AI in Safety-Critical Socio-Technical Systems](http://arxiv.org/abs/2609.14592v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence systems are rapidly becoming critical components in healthcare, finance, public services, and other safety-critical domains. Yet the engineering practices used to evaluate these systems remain predominantly model-centric, emphasizing properties such as accuracy, robustness, fairness, and interpretability before deployment. These properties are necessary but insufficient once an AI system operates within an ever changing socio-technical environment characterized by distrib...
  </details>

- **2026-09-13** — Myra Cheng, Lujain Ibrahim, Grace Liu et al. — [LLMs as Oracles: Reliance on LLMs for Subjective Personal Questions](http://arxiv.org/abs/2609.14849v1)
  <details><summary>📄 Abstract</summary>
  We characterize how people are turning to LLMs as oracles: all-knowing authorities on subjective personal questions. Motivated by risks to users' autonomy and well-being, we develop a typology and LLM-based methods to measure this form of AI reliance at scale and understand how people are offloading judgment and decision-making to AI. Applying our typology to public usage data (68K prompts from WildChat and ThoughtTrace), we find that LLM-as-oracle use has increased over time (2023-2026) and is ...
  </details>

- **2026-09-13** — Erkan Bayram, Mohamed-Ali Belabbas, Tamer Başar — [Privacy Preserving Gossip Learning](http://arxiv.org/abs/2609.14778v1)
  <details><summary>📄 Abstract</summary>
  We propose a decentralized privacy-preserving learning algorithm in which each agent holds a single private sample and a shared model. Samples are learned sequentially, and each update must preserve the endpoint mappings at previously learned samples while protecting private data. This gives each agent three roles: (i) a learner that updates the model parameters, (ii) a teacher whose sample is learned at the current iteration, and (iii) a protected agent whose sample has already been learned. We...
  </details>

- **2026-09-13** — Rohit Patel, Susil Kumar Mohanty, Jeenal Chaudhary — [TriCalRAG: A Three-Strategy, Retrieval-Augmented Benchmark for On-Premise LLM-Based Root Cause Analysis in AIOps](http://arxiv.org/abs/2609.14762v1)
  <details><summary>📄 Abstract</summary>
  Cloud-hosted large language models (LLMs) are increasingly used for root cause analysis (RCA) in AIOps pipelines, but they introduce data privacy risk, network latency, and per-query cost that scale poorly with production log volumes. We present TriCalRAG, a benchmark evaluating open-weight LLMs served locally via vLLM on a single high-memory workstation GPU (NVIDIA RTX PRO 6000, 96GB) against a classical LSTM-based log anomaly detector (DeepLog), across four real, publicly available log dataset...
  </details>

- **2026-09-13** — S M Mehedi Zaman, Md Mozammel Hoque — [Vulnerabilities in Personalization: Assessing Health Privacy Risks in ChatGPT Logs and Memory](http://arxiv.org/abs/2609.14697v1)
  <details><summary>📄 Abstract</summary>
  As conversational LLMs become deeply embedded in daily life, users frequently disclose sensitive personal health information during routine interactions. We present a large-scale computational audit analyzing 179,057 conversations across India, Nigeria, Brazil, and Pakistan (N = 1,057) to evaluate personal health disclosures and background memory synthesis in ChatGPT. We find that 21.31% of audited conversations contain personal health data, with 3.62% posing high-to-extreme privacy risks involv...
  </details>

- **2026-09-13** — He Zhang, Siyu Yuan, Siyu Liu et al. — [EdgeHAR: An Edge-Native Compact Sensor Foundation Model for Human Activity Recognition](http://arxiv.org/abs/2609.14498v1)
  <details><summary>📄 Abstract</summary>
  Sensor-based human activity recognition (HAR) is fundamental to ubiquitous and wearable computing, yet existing foundation models are largely designed for cloud-scale deployment and struggle with real-world sensing shifts, including unseen users, devices, sampling rates, and sensor placements. We present \textbf{EdgeHAR}, an edge-native compact sensor foundation model designed for wearable intelligence. Unlike conventional models that entangle activity knowledge with acquisition variations, Edge...
  </details>

- **2026-09-13** — Leon Fernando, C Dombawala, P. Hettigoda et al. — [A Generative AI Integrated Multimodal Framework for Low-Latency Multi-Camera Person Re-Identification](http://arxiv.org/abs/2609.14419v1)
  <details><summary>📄 Abstract</summary>
  Person re-identification (ReID) is essential for multi-camera surveillance and tracking, yet remains difficult due to viewpoint and illumination changes, occlusion, background clutter, and low resolution imagery. We propose a generative AI integrated multimodal ReID framework designed explicitly for robustness under missing cues and low latency deployment. The key idea is a cost aware early-exit cascade that prioritizes inexpensive, high confidence evidence and only triggers expensive modalities...
  </details>

- **2026-09-10** — Jordi Luque, Fernando López, Aleix Sant — [Component-Aware Differential Privacy for Federated Multilingual Speech-LLMs](http://arxiv.org/abs/2609.11762v1)
  <details><summary>📄 Abstract</summary>
  Per-layer differential privacy (DP) clipping improves gradient fidelity in federated learning by allocating per-matrix clipping budgets proportional to parameter count. We show that this recipe breaks for speech large language models (speech-LLMs), when the acoustic encoder and the language decoder differ by an order of magnitude in update norm. Single-pool per-layer methods suffer \emph{cross-component budget collapse}, dragging word error rate (WER) far from flat global clipping or collapsing ...
  </details>

- **2026-09-10** — William Novak, Muhammad Abusaqer — [Empirical Evaluation of Membership Inference Attacks on NLP Text Classifiers: A Baseline Study on SST-2](http://arxiv.org/abs/2609.10935v1)
  <details><summary>📄 Abstract</summary>
  Membership inference attacks (MIAs) try to determine whether a specific record was used to train a model, a privacy risk that matters in natural language processing (NLP), where training data can contain sensitive user text. This paper presents a controlled benchmark of membership inference vulnerability for text classification on the GLUE SST-2 sentiment dataset. A TF-IDF + Logistic Regression pipeline and a fine-tuned DistilBERT classifier are compared under a loss-threshold MIA, with utility ...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 12 papers

- **2026-09-15** — Tapan Chugh, Vidushi Singh, Krish Jain et al. — [Agentic Societies Need a Social Harness](http://arxiv.org/abs/2609.17527v1)
  <details><summary>📄 Abstract</summary>
  An agentic society is a collection of AI agents that coordinate autonomously across trust boundaries, on behalf of different principals whose objectives may only partially align. We show experimentally that in agentic societies even honest, competent agents often fail to reach satisfactory outcomes with existing harnesses and messaging primitives, and that faulty or malicious agents can stall collaboration, influence outcomes, and pursue other harmful goals by exploiting vulnerabilities in commu...
  </details>

- **2026-09-15** — ZhuoXin Liu, Zhiming Ma, Ying Zhang et al. — [RiskChainBench: A Benchmark for Obfuscated Platform Message Restoration and Evidence-Grounded Web Investigation](http://arxiv.org/abs/2609.16900v1)
  <details><summary>📄 Abstract</summary>
  Platform abuse campaigns conceal redirection instructions with emojis, homophones, character decomposition, and redundant symbols, then route users through disguised links to services associated with pornography, fraud, gambling, or illicit transactions. Existing benchmarks evaluate obfuscated text and risky webpages separately, obscuring how target recovery affects downstream evidence acquisition. We introduce RiskChainBench, pairing 3,600 synthetic token-text restoration inputs from 600 source...
  </details>

- **2026-09-15** — Md Rayhanul Masud, Md Rizwan Parvez — [TAME: Token Attribution and Masking for Emergent misalignment](http://arxiv.org/abs/2609.16754v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning an aligned language model on narrow, flawed data can induce harmful behavior far outside the training domain, known as emergent misalignment (EM). Prior work has localized EM in model weights, activations, and training documents, but it remains unclear which training tokens carry the relevant fine-tuning signal. We introduce TAME (Token Attribution and Masking for Emergent Misalignment), a three-stage framework: token attribution scores how strongly the fine-tuning update raises each...
  </details>

- **2026-09-15** — Zhihao Guo, Zonghan Wu, Haizhou Du et al. — [Right Direction, Wrong Step: Geometric Analysis of Finite-Step Failure in Looped Transformers](http://arxiv.org/abs/2609.16665v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers offer a parameter-efficient route to test-time scaling by reusing shared layers for iterative latent reasoning. However, additional iterations can reduce support for a reference answer, leaving unclear whether an update's direction is locally unhelpful or its full displacement moves too far. We study this distinction by analysing reference utility, which measures this support, along the model's own update direction, varying the fraction of the proposed displacement supplied t...
  </details>

- **2026-09-14** — Jun He, Deying Yu — [Cognitive Admission Control: Risk-Conditioned Assurance for Consequential Actions in Agentic Distributed Systems](http://arxiv.org/abs/2609.16313v1)
  <details><summary>📄 Abstract</summary>
  In agentic distributed systems, an agent may be authorized to mutate external infrastructure while lacking evidence that the mutation is ready to execute. Cognitive Admission Control (CAC) makes this evidence requirement explicit. A policy maps a typed action and its modeled risk to assurance obligations specifying predicates, evidence classes, scope, freshness, and witness-set constraints. A deterministic evaluator distinguishes satisfied, violated, and unresolved obligations; unresolved condit...
  </details>

- **2026-09-14** — Laura M. Vowels, Matthew J. Vowels, Shivali Sharma et al. — [K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations](http://arxiv.org/abs/2609.15855v2)
  <details><summary>📄 Abstract</summary>
  People increasingly use large language models (LLMs) for mental health support, yet their safety in evolving, high-risk conversations remains poorly characterised. We developed K-Bench, a clinician-calibrated, protected benchmark evaluating 125 model configurations representing 33 base models from 14 providers across a fixed cohort of 200 multi-turn vignettes involving suicide, self-harm, domestic violence, substance misuse, and no-risk presentations. Synthetic patient conversations showed subst...
  </details>

- **2026-09-14** — Keertana Chidambaram, Andrew Ilyas, Vasilis Syrgkanis — [Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection](http://arxiv.org/abs/2609.15989v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring is a safety strategy where the reasoning of a large language model "actor" is inspected by a "monitor" (often another language model) for signs of unsafe planning, deception, or misalignment. We find that planting harmful but benign-sounding reasoning in the actor's context can steer it to perform adversarial actions while evading monitors, an attack we term "plan injection". We initially discover this attack in the multiple-choice question-answering monitorabil...
  </details>

- **2026-09-14** — Laura M. Vowels, Matthew J. Vowels, Shivali Sharma et al. — [K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations](http://arxiv.org/abs/2609.15855v1)
  <details><summary>📄 Abstract</summary>
  % !TEX root = ../main.tex People increasingly use large language models (LLMs) for mental health support, yet their safety in evolving, high-risk conversations remains poorly characterised. We developed K-Bench, a clinician-calibrated, protected benchmark evaluating 125 model configurations representing 33 base models from 14 providers across a fixed cohort of 200 multi-turn vignettes involving suicide, self-harm, domestic violence, substance misuse, and no-risk presentations. Synthetic patient ...
  </details>

- **2026-09-14** — Mohammed Ahnouch, Lotfi Elaachack — [Semantic Fibers and Cross-Gram Interference: A Calculus of Safety Drift in Overcomplete Representations](http://arxiv.org/abs/2609.14861v1)
  <details><summary>📄 Abstract</summary>
  A deployed language model may refuse a harmful request in English yet comply with its faithful translation, revealing a cross-lingual safety failure that cannot be characterized reliably by output behavior alone. We formalize this phenomenon through an audited equivalence relation and show that, for a declared quotient, representation, metric, feature dictionary, scoring head, threshold, and contrast model, the resulting safety drift admits an exact linear-algebraic characterization. Specificall...
  </details>

- **2026-09-13** — Orion Reblitz-Richardson — [Refusal Reads Only a Slice of What the Model Knows: Harm-Keyed Routing and Its Exceptions Across Model Families](http://arxiv.org/abs/2609.14759v1)
  <details><summary>📄 Abstract</summary>
  Alignment applied after pretraining is shallow in a measurable way: a single direction in a model's residual stream can be edited out, and the model stops refusing harmful requests. That fact says how easily refusal can be removed, not what the refusal decision was reading in the first place. We ask what it reads, and we separate that from what the model comprehends. Across four open-weight models spanning three families, moral comprehension is native to pretraining: a low-rank moral subspace cr...
  </details>

- **2026-09-13** — Ziyi Zhu, Daniel R. Cahn, Thomas D. Hull et al. — [Optimizing Sparse Outcomes Through Dense Behavioral Signals via Value-Guided Preference Distillation](http://arxiv.org/abs/2609.14648v1)
  <details><summary>📄 Abstract</summary>
  Aligning multi-turn dialogue agents is usually framed as matching turn-level human preferences, yet direct optimization of long-term outcomes is often ineffective and prone to reward hacking. We formulate long-horizon dialogue optimization as a multi-objective reinforcement learning problem and train a multi-head value model that predicts a vector of observed user behaviors across multiple look-ahead horizons. Our findings demonstrate that a scalarized composite of dense auxiliary behavioral sig...
  </details>

- **2026-09-10** — Zonghao Ying, Xiangfan Wu, Huiyu Wu et al. — [The Missing Boundary: How Autonomous Agents Lose Control](http://arxiv.org/abs/2609.11024v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents increasingly perform long-horizon tasks involving tool use, persistent state, and consequential actions, raising a fundamental question: \emph{under what conditions does an agent cross the boundary of authorized execution while pursuing a legitimate task?} Existing studies often attribute such failures to adversarial instructions, malicious environments, or conflicting objectives, leaving unclear how loss of control can emerge during otherwise legitimate task execution. We stud...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-09-15** — Zhuoang Cai — [Benchmarking Factual Robustness of LLMs via Multi-conversation Persuasion](http://arxiv.org/abs/2609.16777v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) increasingly serve as primary knowledge retrieval interfaces, their robustness against \textit{persuasion attacks}---attempts to inject misinformation or enforce counterfactuals---has become a critical safety concern. Existing red-teaming frameworks typically evaluate models in multi-turn dialogues where the target model retains full conversation history. We identify a critical flaw in this setting termed \textbf{``Refusal Inertia''}: a model's initial refusal oft...
  </details>

- **2026-09-15** — Jakob Nyberg, Teodor Sommestad, Andrei Buhaiu et al. — [A Cyber Range Evaluation of Autonomous Network Incident Response Agents](http://arxiv.org/abs/2609.16541v1)
  <details><summary>📄 Abstract</summary>
  We test the performance of agents for automated network intrusion response in a cyber range intended for human operator training. The range implements an emulated networking environment with a variable network topology, red-team emulation and simulated user agents. The goal of the defensive agents is to prevent hosts in the network from being accessed by the red-team agent, while minimizing the availability costs induced from defensive measures. Alerts are generated using a SIEM platform and map...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 69 papers

- **2026-09-15** — Benedikt Barthel Sorensen, Mitchell Black, Erfaun Noorani et al. — [A Time-to-Collision Barrier Function Approach to Collision Avoidance for Stochastic Systems](http://arxiv.org/abs/2609.17347v1)
  <details><summary>📄 Abstract</summary>
  Collision avoidance constraints for autonomous systems are typically formulated in position or velocity space, implicitly reacting to geometric proximity. We propose an alternative paradigm based on the adversarial time-to-collision (aTTC): the minimum time in which an adversary could achieve a collision given its dynamical constraints. By defining a control barrier function (CBF) directly in the time domain, the resulting controller is inherently anticipatory. The evading agent responds not onl...
  </details>

- **2026-09-15** — Anna Di Placido, Nicolas Ferry, Julien Deantoni — [Towards Illusions Awareness in Cyber-Physical System's Design](http://arxiv.org/abs/2609.17260v1)
  <details><summary>📄 Abstract</summary>
  Cyber-Physical Systems (CPS) operate through a continuous sense-compute-act loop within an open context environment, making it impossible to anticipate all the situations the system will face. To cope with this openness, stakeholders rely on assumptions, formalized into design models. However, these assumptions may no longer hold once the system is confronted with runtime reality, resulting in a discrepancy between expected and observed behaviour known in literature as the reality gap. Existing ...
  </details>

- **2026-09-15** — Ziyang Ma, Zihong Zhang, Zuchao Li et al. — [ECHO: Early-layer Collaborative Hierarchical Orchestration with Bonus Logits in Speculative Decoding](http://arxiv.org/abs/2609.17241v1)
  <details><summary>📄 Abstract</summary>
  While draft-model-free speculative decoding offers a promising path to efficient LLM inference, it is frequently constrained by stale draft candidates and the high computational cost of the verification. To address these challenges, we propose ECHO, a hierarchical dual-loop framework that exploits the functional asymmetry between LLM layers. Leveraging the high discriminative efficiency of early layers and the authoritative distribution of final layers, ECHO bifurcates inference into a high-freq...
  </details>

- **2026-09-15** — Zhongkai Wang, Yan Liu — [Grounding SWE-Agent Decisions in Architecture-0 Design: Navigating Unknown Unknowns through Physical Mapping](http://arxiv.org/abs/2609.17221v1)
  <details><summary>📄 Abstract</summary>
  Autonomous Software Engineering Agents (SWE-Agents) excel in deterministic coding tasks but struggle with Architecture 0, the nascent system design phase plagued by implicit engineering constraints, or Unknown Unknowns (UUs) that are rarely stated explicitly. To investigate how agents navigate UUs, we explore a progressive trajectory across pure-text self-play, tool-augmented feedback, and external physical mapping. Our empirical analysis reveals a cascading chain of failures. Pure-text reasonin...
  </details>

- **2026-09-15** — Sebastian Neef — [Plug 'n' Pray: Agentic LLM-based Detection of Potential Log File Exposures in Third-Party Content Management System Plugins](http://arxiv.org/abs/2609.17164v1)
  <details><summary>📄 Abstract</summary>
  Content Management Systems (CMS), such as WordPress, power a large share of the web (~58%), and their extensibility through third-party plugins is a major source of their popularity as well as of their attack surface. One high-impact weakness that remains understudied is log file exposure by CMS plugins, which create log files for debugging or other purposes. If these files are insufficiently secured, they can disclose sensitive information (e.g. credentials, personal data) which has led to webs...
  </details>

- **2026-09-15** — Yongzhi Li, Chongting Shen, Menglin Chen et al. — [AntennaFlow: A Generative Flow Model for Offset Correction in Phaseless Antenna Testing](http://arxiv.org/abs/2609.16948v1)
  <details><summary>📄 Abstract</summary>
  Near-field to far-field transformation is central to large-aperture antenna testing, yet two coupled challenges remain: costly phase acquisition at millimeter-wave bands and violations of the centering assumption under offset mounting. Existing methods address these issues separately, requiring either dense full-field data or offset vectors. We tackle both jointly by exploiting a key observation: amplitude fields under different offsets are coordinate-transformed views of the same near field. Th...
  </details>

- **2026-09-15** — Lehao Lin, Yuheng Cheng, Guolong Liu et al. — [QART: A Quantum-Classical Hybrid Architecture for Long-Horizon Reasoning -- Exploring a Conditional Path toward Quantum Scaling](http://arxiv.org/abs/2609.16887v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon reasoning is vulnerable to early errors that compromise later decisions. We present QART, the Quantum-Augmented Reasoning Transformer, a quantum--classical hybrid architecture combining a backbone language model with quantum encoding, CIM-based QUBO optimization, and quantum decoding. Semantic information can come from hidden representations or model-generated text; detailed encoding and optimization procedures remain proprietary. Under explicit assumptions, we establish a condition...
  </details>

- **2026-09-15** — Kai Yao, Bence Szilágyi, Sebestyén Kamp et al. — [What Breaks Local Watermarks? A Robustness Benchmark for Local Invisible Image Watermarking](http://arxiv.org/abs/2609.16832v1)
  <details><summary>📄 Abstract</summary>
  Local image watermarking embeds an invisible signal into selected image regions rather than spreading it across the entire image, enabling payload recovery from specific objects or regions without perceptibly altering the image. Existing studies evaluate the robustness of payload recovery and localization under image transformations, but they often focus on their own proposed method, resulting in narrow evaluations with inconsistent choices of transformations, datasets, and metrics. These incons...
  </details>

- **2026-09-15** — Bowen Qin, Yi Xie, Yesheng Liu et al. — [ImpossibleRubrics: Stress-Testing Generated Rubrics as Reward Signals](http://arxiv.org/abs/2609.16816v1)
  <details><summary>📄 Abstract</summary>
  Language model-generated rubrics are increasingly used as reward signals for rubric-based reinforcement learning, LLM-as-a-judge evaluation, and automated grading. Such rubrics are reliable only if they reward honest answers over adversarial answers optimized to exploit them. Yet their robustness to such optimization remains poorly understood. We isolate the hardest regime: impossible tasks, where the prompt pressures the model toward an unsupported conclusion, so the only honest response is to ...
  </details>

- **2026-09-15** — Simone Teglia, Irene Amerini — [Unifying Semantic Priors and High-Frequency Traces: Enhancing V-JEPA with Mixture-of-Experts for Robust Synthetic Image Forensics](http://arxiv.org/abs/2609.16778v1)
  <details><summary>📄 Abstract</summary>
  The unchecked proliferation of manipulated images on social media platforms has increased the spread of misinformation, posing a severe threat to public trust and information integrity. Modern deepfake detectors typically rely on Vision Transformers (ViTs) to capture the low-level inconsistencies that characterize fully synthetic or locally tampered images. However, the global understanding of such foundation models is not enough to discriminate alone between real and fake multimedia content, es...
  </details>

- **2026-09-15** — Heng Li, Fulin Zhao, Zhe Geng et al. — [When Agents See Differently: Exposing UI Desynchronization Threats in Mobile Agents](http://arxiv.org/abs/2609.16732v1)
  <details><summary>📄 Abstract</summary>
  Mobile agents are increasingly capable of autonomously interacting with mobile applications and performing consequential actions on behalf of users. Effective human oversight of such agents relies on a basic premise: users and agents observe consistent information from the same interface. We show that this premise can be systematically violated. Users perceive mobile interfaces through physical displays and the human visual system, making their observations subject to occlusion and luminance con...
  </details>

- **2026-09-15** — Rahul Dev T Y, Hiran V Nath — [Toward Secure AI-Powered Penetration Testing Agents: Security Threats, Guardrails, and Architectural Perspectives](http://arxiv.org/abs/2609.16694v1)
  <details><summary>📄 Abstract</summary>
  LLM-powered autonomous agents are transforming the penetration testing space with dynamic, multi-step offensive security workflows that require minimal supervision by humans. These agents leverage sophisticated reasoning abilities and external security tools to independently carry out reconnaissance, identify vulnerabilities, devise exploitation plans, and perform post-exploitation operations. But the ability to have persistent memory, to take actions in the real world, and to do long-horizon re...
  </details>

- **2026-09-15** — Qiyang Sun, Xudong Li, Yupei Li et al. — [CLASH: Counterfactual Auditing of Lexical and Prosodic Reliance in Spoken Sarcasm Detection](http://arxiv.org/abs/2609.16582v1)
  <details><summary>📄 Abstract</summary>
  Spoken sarcasm detectors may exploit lexical content, prosody, or their interaction, yet conventional evaluation cannot reveal which cues drive their predictions. We introduce CLASH (Controlled Lexical-Acoustic Separation Harness), a bilingual counterfactual diagnostic framework that evaluates each utterance under original, lexical-preserving, prosody-preserving, and approximately neutralised conditions. We evaluate handcrafted acoustic-feature systems, self-supervised learning (SSL) probes, and...
  </details>

- **2026-09-15** — Tung Le, Huy Tien Nguyen, Le Minh Nguyen — [Vision And Text Transformer For Predicting Answerability On Visual Question Answering](http://arxiv.org/abs/2609.16565v1)
  <details><summary>📄 Abstract</summary>
  Answerability on Visual Question Answering is a novel and attractive task to predict answerable scores between images and questions in multi-modal data. Existing works often utilize a binary mapping from visual question answering systems into Answerability. It does not reflect the essence of this problem. Together with our consideration of Answerability in a regression task, we propose VT-Transformer, which exploits visual and textual features through Transformer architecture. Experimental resul...
  </details>

- **2026-09-15** — Haoran Yang, Fei Chen, Yutian Xiao et al. — [ReliGRec: Reliability-Oriented LLM-Based Generative Recommendation via User-Risk-Aware Prompt Routing](http://arxiv.org/abs/2609.16560v1)
  <details><summary>📄 Abstract</summary>
  User behavior in real-world recommender systems is heterogeneous. While some users exhibit coherent preferences, others show abrupt interest shifts, bursty interactions, excessive repetition, or inconsistency with collaborative neighborhoods. Such deviations may arise from benign variation or manipulation, including shilling attacks, but do not alone establish malicious intent. Existing robust recommenders exploit user-risk signals through training-time reweighting or graph aggregation, whereas ...
  </details>

- **2026-09-15** — Yuchen Su, Zijian Huang, Yaotian Shi et al. — [PunGraph: Retrieval-Enhanced Phonetic-Semantic Graph Reasoning for Pun Understanding](http://arxiv.org/abs/2609.16557v1)
  <details><summary>📄 Abstract</summary>
  Puns are a challenging form of figurative language that exploit phonetic similarity and semantic ambiguity to convey multiple meanings. Although large language models (LLMs) demonstrate strong language understanding capabilities, they still struggle with pun reasoning due to limited phonetic modeling and uncontrolled end-to-end generation. We propose \textbf{PunGraph}, a retrieval-enhanced knowledge graph framework for pun understanding. PunGraph constructs a phonetic-semantic lexical graph usin...
  </details>

- **2026-09-15** — Vijay John, Amar Dabaja — [Multimodal Emergency Vehicle Classification via Audio-Visual Transformers and Knowledge Distillation](http://arxiv.org/abs/2609.16535v1)
  <details><summary>📄 Abstract</summary>
  Emergency vehicle detection in autonomous driving is a safety-critical perception task that demands robustness under diverse and adverse real-world conditions. Existing approaches rely on a single modality, either audio or video, which leads to systematic failure when that modality is degraded: microphone-based systems fail in noisy urban environments, and camera-based systems fail at night or under occlusion. This report presents AVNet, a multimodal audio-visual transformer that classifies emer...
  </details>

- **2026-09-14** — Md Nazmul Hoque, Shaswata Mitra, Subash Neupane et al. — [Evaluating the NIST Bugs Framework Against CWE as a Successor for Automated Vulnerability Classification](http://arxiv.org/abs/2609.16433v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability classification based on root cause weaknesses is essential for numerous cybersecurity activities, where the Common Weakness Enumeration (CWE) serves as a public repository of such flaws. However, its overlapping entries create a non-orthogonal structure. The result is the same vulnerability being mapped to multiple weaknesses, complicating Root Cause Analysis (RCA) and triage. To address this, NIST Special Publication 800-231 introduces the Bugs Framework (BF), which organizes vuln...
  </details>

- **2026-09-14** — Ho Ting Hung, Angelica Chowdhury, James Teague et al. — [Mapping U.S. Federal AI Governance Against Sector Vulnerability](http://arxiv.org/abs/2609.16260v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) poses different levels of risk across sectors, but are these differences reflected in U.S. federal AI governance? To help answer this question, we assess 684 federal AI governance documents for their coverage of 14 sectors and 24 AI risks. We measure coverage as breadth (i.e., how frequently the risk or sector is addressed across documents) and depth (i.e., how substantively the risk or sector is discussed). We then compare sector coverage patterns for each of the 24...
  </details>

- **2026-09-14** — Shashank Chaurasia — [The World Model Hardware Accelerator](http://arxiv.org/abs/2609.16244v1)
  <details><summary>📄 Abstract</summary>
  Diffusion transformers invert the arithmetic that autoregressive decoding made familiar. There is no token-by-token recurrence: every denoising step is a full-sequence forward pass over static shapes, so the entire schedule is known at compile time and the only serial dimension is the step count itself. We exploit that structure in WMHA, a latency-first diffusion-transformer inference accelerator: a very-long-instruction-word sequencer issues four engines from one instruction word, a weight-stat...
  </details>

- **2026-09-14** — Bryce Cyr, Nabila Aghanim, Ethan Baker et al. — [Peering Beyond the Veil of Last Scattering: A View of the Universe with CMB Spectral Distortions](http://arxiv.org/abs/2609.16194v1)
  <details><summary>📄 Abstract</summary>
  The frequency spectrum of the cosmic microwave background is the most precise blackbody ever measured in nature, with deviations constrained at the level of almost one part per million from the COBE satellite. Nevertheless, departures away from a perfect blackbody are present in standard $Λ$CDM cosmology, lurking just beneath the surface of our current observational bounds. These spectral distortions provide invaluable information on our thermal history in both the post- and pre-recombination ep...
  </details>

- **2026-09-14** — Danny Wood, James Stringer — [Permutation-Based Stegomalware in Large Language Models: Threats and Countermeasures](http://arxiv.org/abs/2609.16193v1)
  <details><summary>📄 Abstract</summary>
  The difficulty of training large language models (LLMs), together with their ubiquity, raises the threat of stegomalware, where malicious payloads are embedded into model weights. Recent work has demonstrated the use of permutation symmetry in model weights to mitigate these threats, but failed to show neutralization of stegomalware across all weights for LLMs. In this paper, we demonstrate the full potential of behavior-preserving symmetries as a defense against stegomalware, as well as the ris...
  </details>

- **2026-09-14** — Sebastian Zhao, Minseo Kim, Coleman Hooper et al. — [LLM Inference in a Flash!](http://arxiv.org/abs/2609.16161v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown impressive capabilities across a range of natural language processing tasks, and LLM inference has emerged as a critical workload for enabling downstream applications. The demands of serving LLM inference are becoming increasingly challenging as requests shift toward longer sequences and heavier inference, driven by retrieval-augmented generation, inference-time compute scaling, and long-context applications. Additionally, these challenges are compounded b...
  </details>

- **2026-09-14** — Ashutosh P. Tripathi, Debasish Banerjee, Sandip Maiti et al. — [Investigating Interacting Fermionic Models with Locality-Preserving Qubit Encodings](http://arxiv.org/abs/2609.16142v1)
  <details><summary>📄 Abstract</summary>
  We investigate the utility of the locality-preserving Derby-Klassen (DK) fermion-to-qubit mapping [arXiv:2003.06939] for variational quantum simulation of two-dimensional $t$-$V$ and Fermi-Hubbard models. The DK mapping preserves the locality of fermionic interactions with an enlarged Hilbert space, thereby requiring additional constraints that define the physical sector. We incorporate these constraints directly into a Hamiltonian Variational Ansätz (HVA) through Clifford-gate state preparation...
  </details>

- **2026-09-14** — Aman Priyanshu, Supriti Vijay, Kimia Majd et al. — [Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale](http://arxiv.org/abs/2609.15939v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents increasingly operate over complete software repositories, yet cybersecurity evaluations primarily measure whether they can detect, reproduce, or repair vulnerabilities rather than whether they can locate the relevant code. We study vulnerability localization: given a weakness class and an unfamiliar repository, identify the implementation files associated with that weakness. We introduce the Vulnerability Localization Benchmark (VLoc Bench), comprising 500 real world vulner...
  </details>

- **2026-09-14** — Theodoros Moutesidis — [The Model Proposes, the Code Disposes: A Pre-Registered Ablation of a Verifier-and-Acceptance Stage in an LLM-Orchestrated Offensive-Security Agent](http://arxiv.org/abs/2609.15887v1)
  <details><summary>📄 Abstract</summary>
  We evaluate whether a verifier-and-acceptance stage - a model verifier whose verdicts are enforced by deterministic code - changes what an LLM-driven offensive-security agent reports. We report a 15-run exploratory pilot, a pre-registered 20-run confirmatory ablation, and a pre-registered 2 x 2 factorial study with 40 runs across two deliberately vulnerable lab targets. In the confirmatory study, removing the stage eliminated pre-report suppression (median 2 versus 0 findings per run; exact one-...
  </details>

- **2026-09-14** — Mingkai Liu, Hao Zhao, Xingxing Zuo — [SURE-Map: Self-Correcting Streaming Geometric Foundation Model](http://arxiv.org/abs/2609.15795v1)
  <details><summary>📄 Abstract</summary>
  Streaming geometric foundation models are emerging as a compelling alternative to SLAM systems. Yet this streaming nature introduces a fundamental issue: each prediction is made from limited context, which is vulnerable to dynamic objects and weak textures. Small local errors accumulate into severe geometric distortion and long-horizon scale drift. We argue that reliable streaming reconstruction requires geometric foundation models to be not only predictive, but also self-correcting. We introduc...
  </details>

- **2026-09-14** — Guo Fuzheng — [CiteShade: Citation Laundering in Multi-Source Retrieval-Augmented Generation and Its Counterfactual Defense](http://arxiv.org/abs/2609.15660v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) grounds a language model's answers on retrieved external knowledge and returns each answer with citations that identify its sources. Those citations are the user's audit trail: they let a reader verify a claim without trusting the model. Prior security work on RAG asks whether an attacker can corrupt the answer, leaving the citation channel unexplored. We show that this channel is a new and practical attack surface. We propose CiteShade, the first citation la...
  </details>

- **2026-09-14** — Oliver Stevanovic, Jasmin Wachter — [Automating Attack Graph Construction for Agentic Pentesting. Towards Neuro-Symbolic Vulnerability Hunting](http://arxiv.org/abs/2609.15523v1)
  <details><summary>📄 Abstract</summary>
  Logic attack graphs grounded in scanner output provide explicit and auditable attack path reasoning LLM-based agents lack. Integrating symbolic frameworks such as MulVAL to contemporary security workflows or agentic pipelines, however, requires translating scanner evidence to initial facts, and creating domain-specific rules. We present a semi-automated pipeline that addresses this interoperability problem and depict its feasibility in a web-security case study. Our pipeline parses findings from...
  </details>

- **2026-09-14** — Tianyi Li, Simon Geirnaert, Bert De Smedt et al. — [Multiscale Gaussian-Mixture Modeling for HMM Post-Processing in Selective Auditory Attention Decoding](http://arxiv.org/abs/2609.15490v1)
  <details><summary>📄 Abstract</summary>
  Selective auditory attention decoding (sAAD) infers from electroencephalography (EEG) which speaker a listener attends to in multi-speaker scenarios. A widely used approach reconstructs the attended speech envelope from EEG, correlates it with candidate envelopes, and selects the speaker with the highest Pearson correlation. However, correlations in each decision window have high intrinsic variance, making per-window decisions unreliable, especially for short windows. Recent work introduced a hi...
  </details>

- **2026-09-14** — Satoshi Nakano, Kazuhiko Nishimura — [Endogenous supply-chain transformation via dynamically calibrated nonneutroelastic processing networks](http://arxiv.org/abs/2609.15452v1)
  <details><summary>📄 Abstract</summary>
  Understanding how supply chains endogenously transform requires a parametric model of processing networks with non-neutral substitution elasticities. While the Cascaded CES (CCES) production function provides a rigorous framework for these multi-layered linkages, dynamically calibrating its structural parameters from time-series data constitutes a highly non-convex inverse optimization problem. Enforcing the strict microeconomic concavity constraint causes standard monolithic approach to fail du...
  </details>

- **2026-09-14** — Halil Burak Noyan — [Empirical Evaluation of Task-Based Permission Scoping Architecture for AI Agents](http://arxiv.org/abs/2609.15422v1)
  <details><summary>📄 Abstract</summary>
  AI agents are provisioned the same as employee-owned hosts in many enterprise settings with a static credential set fixed at deployment which includes all permissions the employee role might ever need. Role-based access control made this compromise for human principals because scoping access per task was infeasible. For AI agents, the compromise leaves every credential standing exposed whether or not the current task uses them. These permissions can later be utilised by a compromised or misalign...
  </details>

- **2026-09-14** — Christian Fisch, Angela Altmeier, Martin Obschonka et al. — [Artificial entrepreneurial cognition: Locating and causally steering an opportunity recognition dial inside large language models (LLMs)](http://arxiv.org/abs/2609.15277v1)
  <details><summary>📄 Abstract</summary>
  Entrepreneurial cognition is a foundation of entrepreneurship research. Yet the growing involvement of large language models (LLMs) in entrepreneurial work extends the cognition question beyond human actors to systems whose internal representations remain largely unexplored. We introduce artificial entrepreneurial cognition, the functional organisation of entrepreneurship-relevant representations and computations inside artificial intelligence (AI) systems. We bring mechanistic interpretability ...
  </details>

- **2026-09-14** — Yang Chen, Lirong Che, Zhenyu Huang et al. — [HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness](http://arxiv.org/abs/2609.15195v1)
  <details><summary>📄 Abstract</summary>
  Embodied navigation requires agents to interpret visual observations, accumulate spatial knowledge, and execute actions to follow instructions or locate objects. Training-based methods face generalization challenges, while training-free methods exploit multimodal large language models (MLLMs) but often lack mechanisms to reconcile proposed actions with spatial evidence, task progress, and execution failures. We present HarnessVLN, a zero-shot, training-free framework whose Agent Harness coordina...
  </details>

- **2026-09-14** — Yuyao Sun, Tao Deng, Shuang Li et al. — [AdaVSkip: Adaptive Visual Token Skipping Across Layers For Efficient MLLMs Inference](http://arxiv.org/abs/2609.15131v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) require substantial computation to process numerous visual tokens across all transformer layers. Most methods for efficient MLLM inference exploit horizontal redundancy by compressing visual tokens. Beyond token reduction, recent studies exploit vertical redundancy through early exit or fixed-layer skipping. However, we find that the extent and distribution of this redundancy vary across inputs and differ between self-attention and MLP modules. Motivated ...
  </details>

- **2026-09-14** — Shuhao Han, Wenjie Liao, Hayden Vance et al. — [DNF-SR: Dual-Input and Negative-Aware Feature Fine-Tuning for Real-World Image Super-Resolution](http://arxiv.org/abs/2609.15120v1)
  <details><summary>📄 Abstract</summary>
  Benefiting from the powerful generative priors of diffusion models, diffusion-based real-world image super-resolution (Real-ISR) methods have demonstrated impressive performance.To achieve efficient Real-ISR, several recent works have designed one-step diffusion-based models.Howerver, unmediatedly feeding LR into a diffusion model creates a distributional gap with the model's original input.A straightforward approach to reduce the distribution gap is to introduce noise to the LR latents. However...
  </details>

- **2026-09-14** — Yi Chen, Rufeng Cheng, Qiang Xie et al. — [Generate to Explore, Select to Exploit: Aligning LLM-based Headline Generation with Personalized Recommendation](http://arxiv.org/abs/2609.15094v1)
  <details><summary>📄 Abstract</summary>
  In industrial recommendation feeds, presenting a static headline for an item often fails to satisfy the diverse, multimodal interests of the user population, particularly suppressing the needs of long-tail audiences. While Large Language Models (LLMs) have been integrated into recommendation for content understanding or ranking, directly optimizing them to output a single best headline typically leads to mode collapse---converging to generic patterns that satisfy average tastes but miss specific...
  </details>

- **2026-09-14** — Xu He, Chih-Hsuan Lin, Hung-Mao Chen et al. — [Overflip: Repetition-Induced Label Flips in Guardrail Models](http://arxiv.org/abs/2609.15013v1)
  <details><summary>📄 Abstract</summary>
  Guardrail models are classifiers deployed to screen malicious prompts and responses in LLM-based services. To meet latency constraints, many lightweight guardrails adopt compact Transformer backbones (e.g., DeBERTa) that are trained with short context windows (typically 512 tokens) and rely on bucketed relative positional encodings to process longer inputs. Prior evaluations assume that a guardrail's decision is stable as the input is lengthened. We show that this assumption can fail. We identif...
  </details>

- **2026-09-13** — Yuanyi Song, Yukai Wang, Xinbei Ma et al. — [Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents](http://arxiv.org/abs/2609.16053v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is essential for LLM-based agents operating over extended interactions. Existing memory systems primarily update memory when new information arrives, treating retrieval as the endpoint of memory access rather than a driver of memory evolution. Consequently, retrieval feedback is rarely exploited to reorganize memory for future access continuously. Moreover, most existing approaches rely on predefined memory structures together with fixed retrieval pipelines, limiting the agent's...
  </details>

- **2026-09-13** — Jacques Peyrière — [Fast tensor transforms and ring-valued orthogonal matrices: an application to cryptography](http://arxiv.org/abs/2609.14782v1)
  <details><summary>📄 Abstract</summary>
  We present a generalization of the Fast Fourier and fast Walsh   transform algorithms to tensor products of $n$ arbitrary $q\times q$   matrices over a commutative ring, reducing the cost of applying such   a tensor product from $q^{2n}$ to $nq^{n}$ ring operations. We then   give an explicit construction of square orthogonal matrices over a   commutative unitary ring, starting from a prescribed first row, and   specialize this construction to ${\mathbb Z}/256{\mathbb   Z}$. Combining these two ...
  </details>

- **2026-09-13** — Maoliang Li, Hailong Zou, Taohong Han et al. — [BigMoMo: Efficient Inference of Large-Scale MoE with Speculative Decoding on Mobile Devices](http://arxiv.org/abs/2609.14643v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) models expand language model capacity on smartphones, but expert offloading remains constrained by limited DRAM capacity and costly data movement. Sequential token routing couples expert execution to fragmented flash reads and multistage NPU preparation, leaving sparse computation stalled on weight transfers. Each transfer serves few tokens before execution moves on. We exploit the multi-token verification window of speculative decoding to decouple expert movement from s...
  </details>

- **2026-09-13** — Juanen Li, Peng Qian, Guanyan Li et al. — [EchoFuzz: Empowering Smart Contract Fuzzing with Large Language Models](http://arxiv.org/abs/2609.14475v1)
  <details><summary>📄 Abstract</summary>
  Smart contracts, serving as the cornerstone of decentralized applications, autonomously manage trillion-dollar digital assets, making them attractive targets for attacks. Fuzzing has emerged as a promising technique for detecting vulnerabilities in smart contracts, yet existing methods face two main challenges. (1) The logical gap in state transitions and combinatorial redundancy hinders effective tradeoffs between bug detection efficiency and state space exploration cost, leading to critical ex...
  </details>

- **2026-09-13** — Hongliu Cao — [Policy Loopholes in Agent Evaluation: When Policy Ambiguity Masquerades as Agent Error](http://arxiv.org/abs/2609.14400v1)
  <details><summary>📄 Abstract</summary>
  Agent benchmarks evaluate policy compliance but assume each policy determines a unique correct action. Natural-language policies can violate this assumption through silence, ambiguity, or contradiction, admitting multiple defensible readings that a single gold trajectory cannot capture. Auditing two $τ^2$-bench domains, we develop a taxonomy of such policy loopholes and show that affected tasks produce unreliable scores: they lower scores across different models in different ways and make every ...
  </details>

- **2026-09-13** — Zhuojin Li, Marco Paolieri, Leana Golubchik — [Partition-Aware Scheduling for Mobile Heterogeneous Inference Co-Execution](http://arxiv.org/abs/2609.14213v1)
  <details><summary>📄 Abstract</summary>
  Modern mobile inference runs on heterogeneous platforms combining mobile GPUs with multiple CPU core clusters. Existing optimizations typically exploit either inter-operator parallelism, by assigning entire operators to CPU cores or to the GPU, or intra-operator parallelism, by partitioning each operator for CPU-GPU co-execution. We consider these two forms of parallelism together, to improve inference latency of tasks that can be represented by a static DAG of operators with predefined input/ou...
  </details>

- **2026-09-10** — Varun Teja Chundru, Debasmita Biswas — [Domain-Specific Hallucination Detection in Large Language Models](http://arxiv.org/abs/2609.11878v1)
  <details><summary>📄 Abstract</summary>
  Large language models generate fluent text that can contain unfaithful claims -- a phenomenon known as hallucination. We present a multi-signal detection pipeline combining fine-tuned DeBERTa-v3 classification, Monte Carlo (MC) Dropout uncertainty quantification, and temperature-scaled calibration for response-level hallucination detection. Evaluated on the HaluEval benchmark, our pipeline achieves F1=0.915 and AUROC=0.977 on general-domain tasks, with per-task F1 scores of 0.97 (QA), 0.96 (Summ...
  </details>

- **2026-09-10** — Vartika Singh, Philip N. Brown — [Truncated Noisy Best-Response Algorithms: Toward Game Theoretic Learning with Safety Guarantees](http://arxiv.org/abs/2609.11863v1)
  <details><summary>📄 Abstract</summary>
  We consider a game theoretic approach to solve multi-agent coordination problems with submodular maximization objectives. It is known for such problems that the Nash equilibria for the corresponding game are always within 50% of the optimal, but that the equilibria which achieve this worst-case bound are not stable. To exploit this instability, we propose a family of algorithms which we call Truncated Noisy Best-Response (TNBR) Algorithms. These algorithms are flexibly characterized by agents as...
  </details>

- **2026-09-10** — Yedidel Louck, Amit Dvir, Ariel Stulman — [Signing the Transaction but Not the Decision: Whisper Attacks and a Binding Defense for AP2](http://arxiv.org/abs/2609.11757v1)
  <details><summary>📄 Abstract</summary>
  Software agents are beginning to shop and pay on a person's behalf. Agent payment protocols such as AP2 produce cryptographically valid signatures for completed purchases, yet do not constrain the decisions that lead to them. Consequently, ordinary product-description text can steer a shopping agent into forming a cart that passes every protocol check but no longer matches the user's request. In this paper, we show that this vulnerability enables three related attacks. In the first attack, the a...
  </details>

- **2026-09-10** — Miguel A. Avendaño-Bernal, Srinandan Dasmahapatra, Ahmed Hammad et al. — [Hunting the Unseen: Deep Learning Analysis for Semi-Visible Jet Tagging](http://arxiv.org/abs/2609.11692v1)
  <details><summary>📄 Abstract</summary>
  Semi-Visible Jets (SVJs) constitute a distinctive collider signature of strongly interacting dark sectors, embedding Dark Matter candidates, wherein jets contain both visible Standard Model objects and invisible dark hadrons, giving rise to correlated jet activity and missing transverse momentum. In this work, we investigate SVJs produced through a heavy Z' mediator and perform an study over a representative set of benchmark scenarios spanning different mediator masses and dark sector parameters...
  </details>

- **2026-09-10** — Nathaniel Hendrix, Carl Y. Zhang, Chris Heitzig et al. — [Geospatial Foundation Models Capture Health-Relevant Dimensions of Place Beyond Conventional Social Risk Indices](http://arxiv.org/abs/2609.11689v1)
  <details><summary>📄 Abstract</summary>
  Area-based social risk indices summarize residents' socioeconomic conditions but incompletely capture physical features of place that may affect health. We evaluated whether numerical representations of physical place produced by four geospatial foundation model families from 2022 satellite data explained residual variance in tract-level associations between the Area Deprivation Index, Social Deprivation Index, and Social Vulnerability Index with health outcomes. We used LightGBM to predict vari...
  </details>

- **2026-09-10** — Martin Andersson, Tung T. Vu, Pål Frenger et al. — [Leveraging Slowly Time-Varying AP-AP Channels for Interference Mitigation in Dynamic TDD](http://arxiv.org/abs/2609.11669v1)
  <details><summary>📄 Abstract</summary>
  We address the challenge of cross-link interference in dynamic time-division duplexing (TDD) systems. Specifically, we focus on mitigating the interference caused by access points (APs) operating in downlink to APs operating in uplink. To this end, we exploit that channels between APs typically vary much more slowly over time than channels between users and APs. This observation allows us to jointly estimate the uplink user data and the AP-AP channels using a least-squares formulation over multi...
  </details>

- **2026-09-10** — Christophe Cheverry, Zied Ammari — [The Schrödinger-Klein-Gordon System Revisited](http://arxiv.org/abs/2609.11658v1)
  <details><summary>📄 Abstract</summary>
  We introduce a microlocal formulation of the Schr{ö}dinger-Klein-Gordon system describing the interaction between a non-relativistic quantum particle and a Klein-Gordon field through Yukawa coupling. Instead of working directly with the Schr{ö}dinger wave function, we represent the quantum component by its Fourier-Wigner transform, and we rewrite the Klein-Gordon equation in terms of a complex Fourier variable. Eliminating the field variable yields a closed nonlinear Fourier-Moyal equation on ph...
  </details>

- **2026-09-10** — Hao Dong, Xun-Jiang Luo, Xiao-Hong Pan et al. — [Phase-Controlled Majorana Zero Modes in Altermagnetic Topological-Insulator Josephson Junctions](http://arxiv.org/abs/2609.11633v1)
  <details><summary>📄 Abstract</summary>
  We exploit facet-dependent Andreev phase shifts to control topological superconductivity with a phase bias in a three-dimensional altermagnetic topological-insulator Josephson junction. In the weak link between two conventional s-wave superconductors, the d-wave altermagnetic order produces facet-dependent momentum shifts of the surface Dirac cones. The resulting net momentum of the states involved in Andreev reflection generates additional propagation phases that differ between facets. Conseque...
  </details>

- **2026-09-10** — Kai Ma, Quanfeng Lv, Jingguo Ge et al. — [Entwine: Coordinating Tiled Computation and Fine-Grained Communication across GPUs](http://arxiv.org/abs/2609.11562v1)
  <details><summary>📄 Abstract</summary>
  Modern high-performance GPU computations partition tensors into tiles to exploit data reuse and parallelism. Individual tile computations complete earlier than the full tensor computation, creating opportunities to overlap computation and communication. However, a mismatch between computation and communication progress can limit these opportunities. Communication stalls when no data is ready, and may lag when data arrives in bursts. Communication can also slow computation by consuming shared res...
  </details>

- **2026-09-10** — Patrick Rebling, Philipp Nenninger, Reiner Kriesten — [CARLAverse: A Highly Modular, Distributed, and Multimodal Framework for Human-in-the-Loop Simulation](http://arxiv.org/abs/2609.11478v1)
  <details><summary>📄 Abstract</summary>
  The development of autonomous driving demands comprehensive testing in mixed-traffic scenarios involving vulnerable road users (VRUs), where purely artificial agents often fail to capture authentic human social negotiations. While human-in-the-loop (HITL) simulators enable safe investigation of these interactions, existing multi-agent platforms struggle with the network latency and synchronization constraints required for high-fidelity haptic feedback. To resolve this, we present CARLAverse, an ...
  </details>

- **2026-09-10** — Peiyuan Gao, Gaoyuan Zhang, Haojie Qin et al. — [VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over Structured Documents](http://arxiv.org/abs/2609.11390v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art retrieval-augmented generation (RAG) methods exploit document structures to acquire sufficient evidence, but often incur substantial token costs. To reduce structural-context tokens without compromising high RAG accuracy, we present {\sf VikingRAG}, a directory-aware semantic data management system that tightly integrates semantic and structural access to support structural-context-efficient, evidence-gap-driven multi-round retrieval. To further reduce token overhead of multi-ro...
  </details>

- **2026-09-10** — Yosuke Hashidate — [Social Preferences and Cooperation: Beliefs, Robustness, and the Limits of Altruism](http://arxiv.org/abs/2609.11374v1)
  <details><summary>📄 Abstract</summary>
  We study a mechanism of cooperation in the Prisoner's Dilemma (PD). Incorporating social preferences as efficiency concerns into the PD game, we study how altruism translates into cooperation. Under complete information, cooperation requires the opponent's altruism to clear a threshold. We then introduce a subjective extension of Bayesian Nash equilibrium that relaxes the Common Prior Assumption, letting players hold heterogeneous, potentially misspecified beliefs about each other's altruistic t...
  </details>

- **2026-09-10** — Xingyi He, Ziwei Wang, Dongrui Wu — [RAMamba-Net: A Reliability-Aware and Mamba-Based Multimodal Fusion Network for Auditory Attention Detection](http://arxiv.org/abs/2609.11372v1)
  <details><summary>📄 Abstract</summary>
  Auditory attention decoding (AAD) identifies the attended speaker from physiological signals, supporting neuro-steered hearing devices and natural human-machine interaction. Electroencephalography (EEG) is the dominant modality for AAD but provides incomplete evidence in naturalistic audio-visual scenes, motivating EEG and electrooculography (EOG) fusion. Existing approaches remain limited by weak cross-modal interaction, inefficient temporal modeling, and low robustness to sample variations. To...
  </details>

- **2026-09-10** — Ziwei Wang, Xingyi He, Hongbin Wang et al. — [Exploring Diffusion Transformers for Cross-Modal Augmentation in Multimodal Brain State Decoding](http://arxiv.org/abs/2609.11341v1)
  <details><summary>📄 Abstract</summary>
  Multimodal brain state decoding has largely focused on fusing paired modalities for prediction, but has rarely explored how their correspondence can be further exploited to enrich training data and improve multimodal representation learning. To address this gap, we propose CoMA-DiT, a bidirectional cross-modal Diffusion Transformer for latent augmentation that treats paired modalities as sources of mutual generative supervision rather than merely as inputs to be fused. CoMA-DiT conditions veloci...
  </details>

- **2026-09-10** — Alessio Ferrari, Minh An Nguyen, Kushal Ramkumar et al. — [Exploring the Role of Security Experience and ChatGPT Usage Strategies on Secure Software Engineering Education](http://arxiv.org/abs/2609.11303v1)
  <details><summary>📄 Abstract</summary>
  The rapid adoption of Large Language Models (LLMs) is reshaping software engineering education, but their role in secure software engineering education remains underexplored. We report an exploratory empirical study of how 26 graduate students in a part-time MSc Cybersecurity programme used ChatGPT during a vulnerability-fixing assignment. To characterise ChatGPT use, we analysed students' ChatGPT interaction logs using a structured double-coding procedure and examined whether usage patterns and...
  </details>

- **2026-09-10** — Mengming Li, Ceyu XU, Qijun Zhang et al. — [Memory Compression for High-Fanout Agent Sandboxes](http://arxiv.org/abs/2609.11294v1)
  <details><summary>📄 Abstract</summary>
  High-fanout agent workloads create a growing memory bottleneck because a single task may spawn many concurrent sandbox sessions. Yet these sandboxes are far from independent: they originate from a shared template and execute related trajectories, exposing substantial template-relative and cross-sandbox memory redundancy. Conventional memory compression is poorly matched to this setting in three fundamental dimensions: how to compress, because they fail to exploit similarity across non-identical ...
  </details>

- **2026-09-10** — Leonard Pleschberger — [Discrete Hyperbolic Secant Distributions](http://arxiv.org/abs/2609.11293v1)
  <details><summary>📄 Abstract</summary>
  We introduce a family of discrete hyperbolic secant distributions on $\mathbb{Z}$, whose normalizing constants arise from series values calculated by Ramanujan and are expressed in terms of Gauß' constant $G=\varpi/π$, where $\varpi=Γ^2(1/4)/(2\sqrt{2π})$ is the lemniscate constant. Using the elliptic lambda-star function $λ^*$, we construct scaled versions of these distributions parametrized by $\sqrt{r}$ and $1/\sqrt{r}$ for $r \in \mathbb{N}$. For the first such distribution, we compute the m...
  </details>

- **2026-09-10** — Daniel Akselrad, Robert N. Proctor — [INDRA: A New AI Tool for Exploring Tobacco, Fossil Fuel, and Chemical Industry Archives](http://arxiv.org/abs/2609.11261v1)
  <details><summary>📄 Abstract</summary>
  Five decades of litigation have disgorged hundreds of millions of pages of formerly secret business records from the tobacco industry, along with documents from the makers of drugs, chemicals, food, firearms, and fossil fuels. Yet these archives have been effectively inaccessible to general-purpose large language models (LLMs) because they have never been compiled into an LLM-readable corpus. Chatbots may be familiar with some of the materials contained in such archives but, with no direct acces...
  </details>

- **2026-09-10** — Muhammad Fahad Bashir, Muhammad Afzal — [An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning](http://arxiv.org/abs/2609.11199v1)
  <details><summary>📄 Abstract</summary>
  With the existing digital mental health tools specifically developed for Western settings, Pakistani students are exposed to a uniquely compounded stress situation in their university that includes academic, financial, familial, and relational stressors, which have become a serious concern for academic and psychological development of students in Pakistani universities. This paper introduces a new, AI-driven and culturally sensitive stress detection and wellness support system that is tailored t...
  </details>

- **2026-09-10** — Vikash Singh, Debargha Ganguly, Aman Goel et al. — [Beyond Solver Verdicts: Generative Reward Models for Autoformalization](http://arxiv.org/abs/2609.11085v1)
  <details><summary>📄 Abstract</summary>
  Neurosymbolic systems rely on mathematical solvers to guarantee reasoning correctness, yet solvers are fundamentally blind to whether a formal translation maintains strict reference-equivalence to a designated formalization. We formalize this vulnerability as Verdict-Preserving-Unfaithfulness (VPU): a failure mode where an incorrect encoding executes successfully and matches the expected verdict. We theoretically prove that structural, verdict-only verification heuristics are mathematically boun...
  </details>

- **2026-09-10** — Jiarong Lian, Zhe Xiao, Zhaoyang Zhang et al. — [RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting](http://arxiv.org/abs/2609.11079v1)
  <details><summary>📄 Abstract</summary>
  Render--match--PnP relocalization establishes correspondences between query image pixels and 3D map points for camera pose recovery, but their potential to support dense depth estimation is often overlooked. To exploit this geometric information, we present RIDE, which estimates dense metric depth from a robot's RGB stream. Given a metrically scaled 3D Gaussian Splatting (3DGS) model, RIDE combines sparse metric depth observations derived from PnP-RANSAC inlier correspondences with the geometric...
  </details>

- **2026-09-10** — Lingyuan Kong, Jiaqi Cui, Fanjiao Zeng et al. — [UniRec: Cross-stage Multi-Task Fusion with Preference Alignment for Cascaded Recommender Systems](http://arxiv.org/abs/2609.11052v1)
  <details><summary>📄 Abstract</summary>
  Industrial recommender systems use cascaded stages with different objectives, feature spaces, and latency constraints. Optimizing pre-ranking and ranking separately can create cross-stage inconsistency: upstream models may filter out items preferred by downstream rankers, and independently tuned downstream fusion can offset upstream improvements. Existing multi-task fusion methods focus on multi-objective fusion within the ranking stage, and cross-stage methods typically only add a downstream sc...
  </details>

- **2026-09-10** — Shenghan Zheng, Zonglin Di, Yimin Liu et al. — [BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure](http://arxiv.org/abs/2609.11028v1)
  <details><summary>📄 Abstract</summary>
  LM-agent benchmarks increasingly function as interactive evaluation infrastructure. Agents observe state, call tools, modify workspaces,   submit artifacts, and receive rewards from outcome procedures. This interactivity makes evaluations vulnerable to reward hacking: an agent   improves its measured score by exploiting the reward-relevant trajectory instead of solving the intended task. Existing defenses rely largely   on task-specific patches, prompt instructions, or post-hoc detectors. They d...
  </details>

- **2026-09-10** — Rui Cao, Shaojing Fan, Liming Fang et al. — [DeFiFusion: Combining Transaction Events with Smart Contracts to Detect Price Manipulation Attacks](http://arxiv.org/abs/2609.11008v1)
  <details><summary>📄 Abstract</summary>
  Decentralized Finance (DeFi) has emerged as a rapidly growing blockchain-based financial service, where market transaction dynamics and underlying smart contract logic are intricately intertwined. This autonomous interplay, while eliminating centralized intermediaries, significantly expands the vulnerability surface of DeFi protocols to Price Manipulation Attacks (PMAs), which have already inflicted catastrophic financial losses. Despite their gravity, existing detection paradigms suffer from fu...
  </details>

- **2026-09-10** — Mohammad Farhad, Shuvalaxmi Dass — [LLMVul: A Vulnerability-Labeled Dataset of LLM-Generated C/C++ Functions from Real Production Repositories](http://arxiv.org/abs/2609.10945v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate and assist with software development, yet existing vulnerability datasets largely focus on human-written code or controlled prompting environments. This limits the ability to study security weaknesses in LLM-generated code as it appears in real-world software projects. We present LLMVul, a vulnerability-labeled dataset of LLM-generated C/C++ functions mined from real production repositories. We mine AI-assisted development activity f...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 58 papers

- **2026-09-15** — Kisu Yang, Yoonna Jang, Heuiseok Lim — [Nameless Tokenization: A Lossless Tokenizer-Level Defense Against Control-Token Forgery in Open-Weight LLMs](http://arxiv.org/abs/2609.16984v1)
  <details><summary>📄 Abstract</summary>
  Open-weight language models publish the strings their chat templates use to mark turns, roles and tool results, which the tokenizer maps back to the reserved identifiers the model obeys. Anyone who controls text in a prompt can therefore write a turn boundary indistinguishable from one the serving stack wrote. We audit 256 deployed chat tokenizers. All are forgeable, and the flag usually recommended as a fix leaves 56.6% forgeable because it misses the tool and reasoning markers agent systems re...
  </details>

- **2026-09-15** — Jakob Nyberg, Sandor Berglund, Andrei Buhaiu et al. — [The MAL Simulator: Cyber Operations Simulation based on Attack & Defense Graphs](http://arxiv.org/abs/2609.16563v1)
  <details><summary>📄 Abstract</summary>
  We have developed the MAL Simulator, a cyber operation simulator based on the Meta Attack Language (MAL). The MAL Simulator is intended for decision-driven cyber attack and defense simulations, for system analysis and the development of automated agents. By building the simulator around an attack modeling language, it can be adapted to different target domains without modifying the source code. We used the simulator for two case studies where we trained two types of agents for automated cyber op...
  </details>

- **2026-09-15** — Xiaoyang Liu — [Self-Emergence Agent Architecture:Behavior-Inertia HMM, Reflexive Metacognition,and Social-Contrastive Self-Modeling](http://arxiv.org/abs/2609.17331v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents exhibit strong language-generation and problem-solving capabilities, yet suffer from three structural limitations: personality drift, non-evolutionary reflection, and the absence of a self-other boundary. Existing generative-agent simulations rely on static memory and fixed prompts, maintaining neither behavioral inertia nor endogenous self-evolution. We propose the Self-Emergence Agent Architecture (SEAA), which integrates three components: (i) a Hidden Markov ...
  </details>

- **2026-09-15** — Farzad Nadiri, Mehdi Cina, Ahmad B. Rad — [DriveMCP: An Agentic AI framework for Advanced Driver Assistance System](http://arxiv.org/abs/2609.17247v1)
  <details><summary>📄 Abstract</summary>
  An agentic AI driver-assistance framework that integrates perception, compliance reasoning, vehicle-state interpretation, and safety arbitration into a modular and auditable pipeline. The architecture, referred to as DriveMCP, incorporates a sensor-like perception stack alongside DriveLM as the vision-language front end to generate a graph-structured scene understanding (Graph Visual Question Answering) and language-grounded driving information. Key compliance elements in world_state, including ...
  </details>

- **2026-09-15** — Vsevolod Hulchuk, Jan Bayer, Jan Faigl — [LiLi: Lie Theory Based 3D LiDAR Scan Alignment Degeneracy Detection](http://arxiv.org/abs/2609.17145v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study 3D LiDAR scan alignment in challenging scenarios with degeneracies, such as straight corridors or flat fields, where the alignment solution is not unique and compromises localization and mapping accuracy. Existing degeneracy detection methods that neglect the potential for reassociating data points are prone to being sensitive to noise and complex degeneracies. Therefore, we propose LiLi - a novel method that leverages Lie theory to identify the full set of degenerate tra...
  </details>

- **2026-09-15** — Xiucheng Zhang, Zhuoning Xu, Hanjun Luo et al. — [ANIMASK: What the Model Contributes to Role Play in Simulated Story Worlds](http://arxiv.org/abs/2609.16667v1)
  <details><summary>📄 Abstract</summary>
  When a language model plays a character, the observed behavior reflects both the assigned persona and the default dispositions of the actor model itself. Existing evaluations test persona fidelity or model defaults in isolation, but neither says, at a specific choice with consequences, what the persona changed and what the model's default kept. We introduce ANIMASK, a simulation framework that freezes books and scripts into story worlds whose characters act on their own motivations and replays e...
  </details>

- **2026-09-15** — Harish Gaggar — [Protocol-Preserving Context Trimming for Agentic Workflows: Benefits, Failure Regimes, and Budget Guardrails](http://arxiv.org/abs/2609.16461v1)
  <details><summary>📄 Abstract</summary>
  Agentic large language model (LLM) systems rely on long interaction histories to preserve instructions, tool states, intermediate decisions, and unresolved dependencies, but unrestricted context growth increases computational cost and can reduce efficiency. This study evaluates protocol-preserving context trimming as a reliability-constrained approach for multi-step agentic workflows. Five trimming strategies - recency-based, relevance-based, summarization, protocol-aware trimming, and adaptive ...
  </details>

- **2026-09-15** — Claudio Ranucci, Sébastien Pierre, Léo Vacher et al. — [$B$-sure. Part II. Scattering transforms as robustness test for tensor-to-scalar ratio detection from CMB observations](http://arxiv.org/abs/2609.17531v1)
  <details><summary>📄 Abstract</summary>
  Galactic foregrounds represent a major contamination to the measurement of primordial $B$-modes from observations of the Cosmic Microwave Background polarisation. Even after the application of component separation algorithms, foreground residuals may potentially still bias the estimate of the tensor-to-scalar ratio $r$, causing a false detection. In this work, we present the methodology of a robustness test for the validation of an eventual detection of primordial $B$-modes, as obtained by a fut...
  </details>

- **2026-09-15** — Luciano Marchezan, Kevin Delcourt, Eugene Syriani et al. — [Type-IV Code Clone Detection via Layer-Wise Non-Contrastive Representation Learning](http://arxiv.org/abs/2609.17338v1)
  <details><summary>📄 Abstract</summary>
  Software clones are fragments of code that are similar or functionally equivalent to each other. They pose significant challenges for maintenance, refactoring, and bug detection. Detecting Type-IV clones, which are semantically equivalent but may differ syntactically, is particularly difficult for traditional token- or syntax-based methods. Recent machine learning approaches rely on contrastive learning, which requires careful negative sampling and can introduce bias. In this paper, we propose L...
  </details>

- **2026-09-15** — Jesús M. Fraile-Hernández, Anselmo Peñas, Patrick Giedemann — [Zero-shot narrative detection in social messaging](http://arxiv.org/abs/2609.17310v1)
  <details><summary>📄 Abstract</summary>
  This study investigates the zero-shot ability of large language models (LLMs) to identify and classify hidden narratives in social messages. Our research hypothesis is that LLMs' extensive contextual knowledge allows them to interpret messages on a deeper, pragmatic level, going beyond basic sentiment or topic analysis. Experiments on the Dipromats and SemEval datasets show that providing models with human-written narrative descriptions significantly improves performance, without the need of tra...
  </details>

- **2026-09-15** — Jiawei Gu, Qilin Zhao, Tengkuo Guo et al. — [Probe-VAD: Ordinal Likelihood Probing for Training-Free Video Anomaly Detection](http://arxiv.org/abs/2609.17211v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly detection (VAD) aims to localize anomalous events in untrimmed videos. Vision-language models (VLMs) provide rich visual understanding for training-free VAD, but existing approaches impose restrictive interfaces between visual understanding and anomaly scoring. Caption-based pipelines compress visual evidence into text, potentially discarding subtle cues, while direct numerical generation forces the model to express its judgment through a small set of predefined scores. Such interf...
  </details>

- **2026-09-15** — Minh Dat Nguyen, Gabriele Gemmi, Tamerlan Aghayev et al. — [Agentic RDZ: Autonomous Zone Management with AI Agents and an FR3 Coexistence Use Case](http://arxiv.org/abs/2609.17110v1)
  <details><summary>📄 Abstract</summary>
  Radio Dynamic Zones (RDZs) allow wireless experiments to operate outside conventional spectrum regulations while continuously guaranteeing protection for incumbent users. Existing RDZ prototypes automate this task procedurally, through handcrafted rules and predefined workflows, and become brittle when experiments encounter hardware impairments, user workflows and devices, or interference mechanisms not anticipated at design time. This paper introduces the agentic RDZ (A-RDZ), which, to the best...
  </details>

- **2026-09-15** — Muhammad Ahmed Ullah Khan, Mohammed Elamine, Sheikh Talha Uddin et al. — [NeuroSymbEAD: A Large Scale Neuro-Symbolic Caption Dataset for Omni-Directional Embodied Autonomous Driving](http://arxiv.org/abs/2609.16919v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces NeuroSymbEAD, a large-scale neuro-symbolic caption dataset featuring an ego-centric knowledge graph (KG) of static and dynamic objects annotated with classes, categories, heading directions, orientations, and distances from the ego-vehicle. These annotations are used on the KITTI-360 dataset to generate multilevel textual captions representing a lightweight version of an ego-centric scene map. Outdoor scene-map reconstruction, visual recognition, and object grounding establ...
  </details>

- **2026-09-14** — Mantek Singh, Jeshwanth Challagundla, Prateek Karnal et al. — [LLMs as Master Forgers: Generating Synthetic Time Series Data for Manufacturing](http://arxiv.org/abs/2609.16155v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a novel framework leveraging Large Language Models (LLMs) to generate synthetic time series data for manufacturing processes. Motivated by the scarcity of labeled time-series data in real-world manufacturing settings, which hinders the development of robust machine learning models, we explore the potential of LLMs to learn complex temporal dependencies and generate realistic synthetic data. Our approach involves fine-tuning pre-trained LLMs on manufacturing process instructio...
  </details>

- **2026-09-14** — Ivy Zhang — [The Troy Moment of AI: Why Some Will Cheat and Some Will Follow?](http://arxiv.org/abs/2609.15494v2)
  <details><summary>📄 Abstract</summary>
  Recent investigations of the July 2026 OpenAI-Hugging Face incident motivate two questions: when an assigned task becomes impossible, does an agent stop or escalate, and can observing another agent's behavior change that decision? We study these questions using seven ImpossibleBench tasks with GPT-5.6 Sol, Claude Fable 5.1, and Gemini 3.8 Flash in solo and three-agent settings. Under an explicit-boundary regime with clear authorization rules and restricted tools, no protected tests are modified,...
  </details>

- **2026-09-14** — Aashiq Muhamed, Mona T. Diab, Virginia Smith — [Decoy Direction Optimization: A Post-Hoc Defense Against LLM Abliteration](http://arxiv.org/abs/2609.16204v1)
  <details><summary>📄 Abstract</summary>
  Safety guardrails in open-weight language models can be readily bypassed using Refusal Feature Ablation (RFA), a technique that identifies and projects out a linear refusal direction from the residual stream, often achieving a high attack success rate (ASR) while preserving model capability. Defending against these attacks typically requires computationally expensive safety finetuning for every new checkpoint. We introduce Decoy Direction Optimization (DDO), a fast, post-hoc weight-editing defen...
  </details>

- **2026-09-14** — Rohit Dhaipule, Sukhdeep Singh Kharbanda, Prasanth Bathala et al. — [StalePO: Anchored Token-Level Preference Optimization using Legacy Post-Edits in Machine Translation](http://arxiv.org/abs/2609.16340v1)
  <details><summary>📄 Abstract</summary>
  Machine translation systems are periodically upgraded to stronger models, but the available preference signal is human post-edits of an older system's outputs, which the newer model may already surpass. Moreover, collecting fresh post-edits for every new model is prohibitively expensive. We call this the Stale Preference problem. Standard DPO can fail in this setting: it may increase the likelihood of inferior post-edits, erode the model's existing quality, and fail to provide the per-token cont...
  </details>

- **2026-09-14** — Wuyang Dai, Song Wang — [AgentGuard: Learning Execution Guardrails from Anomalous Coding-Agent Trajectories](http://arxiv.org/abs/2609.16287v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents increasingly rely on execution harnesses to interact with repositories and external tools. However, task success does not guarantee reliable execution. Agents may still modify unrelated files, rewrite tests, issue unsafe commands, or ignore failed validations, motivating behavioral guardrails for reliable execution. We present AgentGuard, an instruction-level guardrail framework that learns conditional execution constraints from anomalous trajectories of coding agents. Rather th...
  </details>

- **2026-09-14** — Anubhav Khanal, Prabigya Acharya, Roshni Poudel et al. — [SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](http://arxiv.org/abs/2609.16233v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models excel at 2D image understanding but remain limited in 3D spatial reasoning. Progress is hindered by limitations in current benchmarks. First, 3D datasets often rely on point clouds that capture geometry but discard rich visual features like texture, text, and materials. Second, annotations treat objects in isolation while ignoring real-world hierarchical organization (scenes, rooms, functional areas, object groups). Third, evaluation tasks focus narrowly on basic recogniti...
  </details>

- **2026-09-14** — Mughees Ur Rehman, Aritran Piplai, Murat Kantarcioglu — [RuleAutoPilot: Synthesizing Deployable Suricata Rules from Network Traffic](http://arxiv.org/abs/2609.16231v1)
  <details><summary>📄 Abstract</summary>
  Rule-based Intrusion Detection Systems (IDS) such as Suricata are central to network security, yet crafting effective detection rules demands deep expert knowledge and cannot keep pace with emerging threats. Existing LLM-based approaches can reduce analyst effort, but they either rely on curated threat intelligence that is produced only after the underlying traffic artifacts already exist, or they require costly LLM use without sufficient quality control. We present RuleAutoPilot, an end-to-end ...
  </details>

- **2026-09-14** — Candace S. Y. Chan, Aris Karatzikos, Ilias Georgakopoulos-Soares — [Artificial intelligence and biosecurity: capabilities, threat pathways, and defense-in-depth governance](http://arxiv.org/abs/2609.16213v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence is reshaping biological research across an increasingly connected digital-to-physical workflow. General-purpose large language models can retrieve and integrate scientific information, support experimental planning, and computational analysis; biological foundation models can predict, optimize, and generate proteins, genes, and genome-scale sequences; agentic systems can coordinate multistep research tasks; automated laboratories can partially close the design-build-test-...
  </details>

- **2026-09-14** — Nishad Singhi, Hector Garcia Rodriguez, Aditya Arora et al. — [Reasoning with Image Generation](http://arxiv.org/abs/2609.16409v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought reasoning has revolutionized natural language processing by enabling large language models (LLMs) to decompose problems into intermediate steps before answering. Yet confining reasoning to the textual domain presents limitations for tasks requiring direct manipulation of visual representations. Recent efforts augment multimodal LLMs with external visual expert tools such as depth estimation or object detection modules, but these remain fundamentally limited by their reliance on ...
  </details>

- **2026-09-14** — Ghazal Farhani, Taufiq Rahman — [Geometry vs Structure: Graph-Based Diagnostics for LiDAR Point-Cloud Simulation Fidelity](http://arxiv.org/abs/2609.16378v1)
  <details><summary>📄 Abstract</summary>
  Digital twins provide a scalable and cost-effective complement to real-world testing for validating autonomous-driving and advanced driver-assistance system (ADAS) sensor pipelines. However, quantifying their fidelity remains challenging, particularly for 3D LiDAR point clouds, where conventional geometric metrics may overlook important structural discrepancies. We present a graph-based framework for evaluating the structural fidelity of simulated LiDAR point clouds against real-world scans. Whi...
  </details>

- **2026-09-14** — Zhaofeng Yu, Haokai Ma, Dongyang Zhan et al. — [Misleading the Planner through Deceptive Resumes: Registration-Time Injection in Centralized Multi-Agent Systems](http://arxiv.org/abs/2609.15516v1)
  <details><summary>📄 Abstract</summary>
  A centralized LLM-based multi-agent system (MAS) extends its functionality by registering new worker agents, whose descriptions are read by the planner to decide how a task is decomposed, which worker executes each subtask, and what each subtask requires. Third-party descriptions are authored outside the system but trusted by the planner, creating a registration-time injection channel. The payload is planted before any user instruction arrives, targets the planner and propagates through the gene...
  </details>

- **2026-09-14** — Luis M. Sánchez — [Clean Scores, Buried Evidence, and Confident Wrong: A Receipt-Based Audit of Frontier Agentic QA](http://arxiv.org/abs/2609.15319v1)
  <details><summary>📄 Abstract</summary>
  Frontier models score well on shallow document/chart reading tasks. In a controlled data-room audit, moving evidence into buried conditions reduced accuracy, increased forced declarations, increased tool calls, and increased cost per correct answer. Confidence and benchmark calibration did not fully capture wrong answers; a documented production incident shows fabricated structural claims can be mixed with accurate numeric tables. Agentic evaluations need claim-level receipts (statement-level pr...
  </details>

- **2026-09-14** — Yuhang Wang — [Why LLM Agents Collapse Without Oversight: The Enforcement Gap as the Mechanism Behind Emergence World Failures](http://arxiv.org/abs/2609.15293v1)
  <details><summary>📄 Abstract</summary>
  When Emergence World placed frontier LLM agents in an unsupervised multi-agent simulation, the results were alarming: agents committed crimes, starved, and enforced unanimous conformity -- without any external attacker. This paper identifies the mechanism. Reflexion-style agents already detect dangerous plan steps through iterative self-critique, yet the architecture provides no pathway from detection to action. We call this the enforcement gap: the audit sees the problem; the controller ignores...
  </details>

- **2026-09-14** — Dalton Diez, Peyton Andras, Max Shroyer et al. — [Event-Native Symbolic-Temporal Spike Encoding Framework for Heterogeneous Cyber Streams](http://arxiv.org/abs/2609.15772v1)
  <details><summary>📄 Abstract</summary>
  Spiking neural networks (SNNs) have shown promise for sparse, event-driven computation through stateful processing that is naturally compatible with low-power edge hardware. These properties align with cyber monitoring, where data arrives asynchronously, and malicious behavior often emerges through temporal patterns across event sequences. However, cyber streams are not composed solely of continuous numeric signals: their informative structure is also carried by categorical identifiers, irregula...
  </details>

- **2026-09-14** — Daniele Veri' — [Beyond AI Literacy: A Structured Review and Exploratory Meta-Analysis of Measures for Competent Generative-AI Use](http://arxiv.org/abs/2609.15624v1)
  <details><summary>📄 Abstract</summary>
  Researchers assessing competent generative-AI use at work must choose among self-reports, objective tests, and measures of oversight and reliance. We conducted a structured, seeded review of 24 focal empirical publications, starting from the 2024 COSMIN-based review and adding a targeted update through 17 August 2026. We grouped the measures into four domains: knowledge and use, epistemic oversight, reliance calibration, and operational control of tool-using agents. In an exploratory meta-analys...
  </details>

- **2026-09-14** — Yolo Y. Tang, Daiki Shimada, Jiayue Meng et al. — [BVB: Benchmarking Agentic Video Understanding via Programmatic Reconstruction in Blender](http://arxiv.org/abs/2609.15478v1)
  <details><summary>📄 Abstract</summary>
  Multimodal agents can create complex videos in software such as Blender by coding without relying on diffusion models. Yet video understanding benchmarks still evaluate models mainly through question answering. If an agent truly understands a video, it can reconstruct it programmatically. We introduce BVB, Blender-VideoBench, a benchmark that tests this ability by asking agents to reconstruct real-world videos as animated Blender scenes. To ensure fair comparison, each agent programs the reconst...
  </details>

- **2026-09-14** — Jean Groeninger, Zihao Zhao, Juliana de Castilhos et al. — [Listening for Airway Stenosis: A Foundation Model-Based Method for Rapid and Accessible Detection](http://arxiv.org/abs/2609.15453v1)
  <details><summary>📄 Abstract</summary>
  Airway stenosis can cause severe respiratory complications, yet its detection often relies on specialized examinations and medical imaging. This study explores the potential of acoustic AI for rapid and accessible airway stenosis detection using readily acquired patient voice recordings. We systematically investigate whether acoustic foundation models (AFMs) can extract acoustic representations associated with airway stenosis-related speech patterns. Experiments are conducted on a cohort of 748 ...
  </details>

- **2026-09-14** — Hongchang Shi, Jinpeng Hu, Ao Wang et al. — [MarKey: Marginal Utility Guided Greedy Keyframe Selection for Long Video Understanding](http://arxiv.org/abs/2609.15408v1)
  <details><summary>📄 Abstract</summary>
  Long-video understanding remains challenging for multimodal large language models (MLLMs) because densely encoding long frame sequences is computationally expensive, while uniform sampling under a limited visual budget can miss sparse yet decisive evidence. Recent training-free keyframe selection methods have enabled more efficient inference and yielded promising performance gains. However, many existing methods score frames largely in isolation without explicitly considering how each candidate ...
  </details>

- **2026-09-14** — Sayantan Mukherjee — [Large Universe Subset Predicate Encryption with IND-CCA Security (with Constant-size Ciphertext and Keys)](http://arxiv.org/abs/2609.15312v1)
  <details><summary>📄 Abstract</summary>
  Katz et al. (CANS'17) introduced Subset Predicate Encryption (SPE).   This scheme is a generalization of broadcast encryption as it emulates the \emph{subset containment} predicate in the encrypted domain.   They proposed two selectively IND-CPA secure SPE constructions in the small universe setting.   They also showed some black-box transformations of SPE to well-known primitives like WIBE and ABE to establish the richness of the SPE structure.   Chatterjee and Mukherjee (RSA'19) proposed two S...
  </details>

- **2026-09-14** — Hanne Beuter, Sebastian Dorn — [Closed-form Bayesian homography estimation from noisy point correspondences](http://arxiv.org/abs/2609.15227v1)
  <details><summary>📄 Abstract</summary>
  While homographies are fundamental to many computer vision tasks, the majority of conventional estimation techniques provide only point estimates without directly quantifying uncertainty introduced by noisy observations. Uncertainty, though, propagates to subsequent processing steps such as camera calibration and 3D reconstruction and is particularly relevant in safety-critical and socially relevant fields including medical imaging, autonomous driving, and defense. We present a fast Bayesian for...
  </details>

- **2026-09-14** — Gongbo Zhang, Hao Li, Yu Wang et al. — [OpenAI4S: Code as Action, Science as Sessions](http://arxiv.org/abs/2609.15096v1)
  <details><summary>📄 Abstract</summary>
  AI co-scientists could accelerate computational research, but over a long-running study the workflow also has to stay inspectable, resumable and reproducible, which requires persistent computational state and provenance. Here we present OpenAI4S, an open-source scientific research agent built around the principle of \emph{Code as Action, Science as Sessions}. OpenAI4S combines a persistent computing runtime with research-session management: orchestration is handled through structured tool calls,...
  </details>

- **2026-09-14** — Hyeongcheol Park, Sumin In, Suyeon Myeong et al. — [SALUTE: Benchmarking and Adapting LLMs for the Defense Domain](http://arxiv.org/abs/2609.15022v1)
  <details><summary>📄 Abstract</summary>
  Defense is a knowledge-intensive domain that requires precise understanding of specialized terminology, doctrinal concepts, operational procedures, and evolving military events. Although recent work has explored language technologies for military applications, existing efforts remain fragmented: they are often task-specific, rely on limited adaptation pipelines, or lack comprehensive defense-domain evaluation. In this paper, we present SALUTE, an end-to-end framework for benchmarking and adaptin...
  </details>

- **2026-09-14** — Hyungseok Ryu, Pilwon Hur — [Two-Stage Personalized Gait Phase Estimation in Stroke Survivors During Exoskeleton-Assisted Walking: An Offline Feasibility Study](http://arxiv.org/abs/2609.14984v1)
  <details><summary>📄 Abstract</summary>
  This study evaluated personalized gait phase estimation for stroke survivors using functional inertial measurement unit (IMU) alignment and two-stage sequential adaptation of models pre-trained on healthy gait. The estimator used signals from a thigh-mounted IMU. Heel force-sensitive resistor measurements provided reference phase labels for offline adaptation and evaluation. Stage 1 established a distillation-regularized participant-specific model, and Stage 2 performed conditional refinement us...
  </details>

- **2026-09-14** — Tinashe Handina, Yuehan Diao, Adam Wierman et al. — [Strategic Decision Focused Learning](http://arxiv.org/abs/2609.14907v1)
  <details><summary>📄 Abstract</summary>
  Machine learning (ML) predictions are increasingly being used to guide decision-making, giving rise to the problem of decision-focused learning (DFL) where predictors are optimized for downstream decision quality rather than accuracy alone. However, most existing work assumes a single decision-maker optimizing in isolation. This paper formalizes strategic decision-focused learning, where an ML system predicts an exogenous state that some agents observe before playing a game. For example, a park ...
  </details>

- **2026-09-14** — Livia Oddi, Simone Scardapane, Toru Sugimoto et al. — [Authorship attribution and aesthetic evaluation of AI poetry: a case study with Haiku](http://arxiv.org/abs/2609.15511v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the generation and human evaluation of Japanese haiku by contemporary Large Language Models (LLMs), focusing on authorship perception and aesthetic judgment within a constrained poetic form. Using a few-shot prompting strategy, Japanese haiku were generated across a heterogeneous set of large language models, including open- and closed-source systems, medium-scale and large-scale architectures, models with native or adapted Japanese support, and multilingual proprietary m...
  </details>

- **2026-09-14** — Ivy Zhang — [The Troy Moment of AI: Why SomeWill Cheat and SomeWill Follow?](http://arxiv.org/abs/2609.15494v1)
  <details><summary>📄 Abstract</summary>
  Recent investigations of the July 2026 OpenAI--Hugging Face incident motivate two questions about agent behavior under task failure: when an assigned task becomes impossible, does an agent stop or escalate, and can observing another agent's behavior change that decision? We study these questions using seven ImpossibleBench tasks with GPT-5.6 Sol, Claude Fable 5.1, and Gemini 3.8 Flash in both solo and three-agent settings. Each task contains a genuine software defect together with a conflicting ...
  </details>

- **2026-09-14** — Dennis Ng, Xingyu Shen, Ankit Raj et al. — [ChatGPT Images 2.5 in the Wild: A Launch-Period Dataset and Detector Evaluation](http://arxiv.org/abs/2609.15100v1)
  <details><summary>📄 Abstract</summary>
  An image tool can change its underlying generator while retaining its public name, making version attribution from online posts ambiguous. We study this problem after the ChatGPT Images 2.5 launch. Our frozen collection contains 3,478 images from 2,440 posts across 8 sources. Recorded posting times fall within the first 51.1 hours after the announcement. It records three attribution tiers and retains standalone images after image-form filtering and targeted review. Caption claims and host record...
  </details>

- **2026-09-14** — Lingheng Du, Yiming Tang, Xufeng Duan et al. — [What Does an LLM Learn from Reinforcement Learning? A Mechanistic Interpretability Perspective with Fixed-SAE Track](http://arxiv.org/abs/2609.15064v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) is widely utilized in large language model training to improve targeted capabilities, yet how RL reshapes a model remains poorly understood. Prior attempts to explain how RL works largely offer behavioral perspectives, leaving open what RL gives a model at the representation level: can RL create genuinely novel features, and which existing features does it enhance or suppress? Recent developments in mechanistic interpretability suggest sparse autoencoders (SAEs) as a ...
  </details>

- **2026-09-14** — Siwei Wu, Jincheng Ren, Yizhi Li et al. — [ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement](http://arxiv.org/abs/2609.14857v1)
  <details><summary>📄 Abstract</summary>
  Recent work extends recursive self-improvement (RSI) to agent harnesses for long-horizon coding and terminal tasks, enabling agents to improve execution mechanisms from experience. However, generalizable harness RSI remains challenging. First, evolving harnesses on evaluation benchmarks or their subsets makes it difficult to distinguish reusable improvements from benchmark-specific adaptation. Second, single-trajectory updates can conflate systematic harness deficiencies with instance-specific r...
  </details>

- **2026-09-13** — Mirza Samad Ahmed Baig, Syeda Anshrah Gillani, Asher Ali et al. — [The Stochastic Deputy: Structural Tenant Isolation for Tool-Using LLM Agents](http://arxiv.org/abs/2609.14780v1)
  <details><summary>📄 Abstract</summary>
  Multi-tenant tools commonly accept a tenant identifier and validate it against the caller's entitlement. For a large language model (LLM) agent, that pattern delegates resource selection to a process whose context may contain attacker controlled instructions. We formalize this stochastic deputy problem and present a structural defense: remove tenant identity from the Model Context Protocol (MCP) tool schema, bind scope to a verified credential, and enforce it below the agent. In a 373-trial abla...
  </details>

- **2026-09-13** — Yusheng Zheng, Wenhui Zhang, Yu Mao — [LLM Agent Capabilities Should Follow Task Intent and Context Source](http://arxiv.org/abs/2609.14631v1)
  <details><summary>📄 Abstract</summary>
  LLM agents take real actions, including executing code, modifying files, calling services, and delegating tasks, driven by context sources: user requests, tool results, documents, shell outputs, Skill and MCP instructions, memory. Unlike traditional systems, where capability is predefined, the least-privilege capability an agent needs is dynamic, depending on its task intent: what it wants to do and how. This creates a security and safety challenge: all inputs enter one shared planning channel w...
  </details>

- **2026-09-13** — Tianhao Ma, Weihao Xuan, Dong-Dong Wu et al. — [DenMark: Robust Semantic Watermarking for Diffusion Language Models](http://arxiv.org/abs/2609.14257v1)
  <details><summary>📄 Abstract</summary>
  Semantic text watermarks encode signals in meaning rather than surface token choices, offering robustness to paraphrasing and other semantic-preserving edits. Existing semantic watermarking methods are primarily designed for autoregressive language models (ARLMs), where completed candidate units can be generated and scored before generation proceeds. This paradigm does not naturally extend to diffusion language models (DLMs), where semantic units remain incomplete during intermediate denoising s...
  </details>

- **2026-09-13** — Sarah Wilson, Gail Kaiser, Patrick Musau — [Efficiency Hallucination: Formalizing and Measuring Behavioral Calibration in LLM-Based Code Optimization](http://arxiv.org/abs/2609.14839v1)
  <details><summary>📄 Abstract</summary>
  The integration of Large Language Models (LLMs) into automated code optimization introduces a critical reliability risk we term the Efficiency Hallucination: an LLM's tendency to issue non-functional mutations with unsubstantiated performance claims on already-optimized code. This is driven by the Evaluation Trap, wherein binary benchmarks incentivize unnecessary modifications over safely abstaining. We present a validation framework using classification penalty methods, evaluated across 180 opt...
  </details>

- **2026-09-13** — Cheikh Ahmed — [Enemray: Toward Capable Language Models for Hassaniya](http://arxiv.org/abs/2609.14829v1)
  <details><summary>📄 Abstract</summary>
  We introduce Enemray, a Hassaniya-centric language model that enables general-purpose interaction in Hassaniya. Enemray is trained around a stability--plasticity objective: acquire strong Hassaniya linguistic and cultural competence while preserving the general reasoning, multilingual, instruction-following, and safety behaviors of a capable instruction-tuned model. The development pipeline separates language acquisition from behavioral specialization. A separately assembled continual-pretrainin...
  </details>

- **2026-09-13** — Arham Sethi, Arsen Kenzhebayev, Saanvi Paturi et al. — [Fabrication After Tool Failure: Tool-Augmented Agents Assert Values Their Tools Did Not Return](http://arxiv.org/abs/2609.14758v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented language models are evaluated on whether they reach the right answer, not on whether they report honestly when a tool fails to supply one. We isolate this post-failure decision with a benchmark of 1,024 items spanning 16 internal-system domains and eight tool-failure types, in which a tool call is enforced and the returned payload is guaranteed to be unusable. Under a deployment-style system prompt, 14.10% of responses are dishonest: the model either asserts a value the payload ca...
  </details>

- **2026-09-13** — Weihong Qi, Chen Ling — [Perceive, Refine, Reason: A Calibrated Pipeline for Measuring Indicators in Strategic Visual Communication on Social Media](http://arxiv.org/abs/2609.14699v1)
  <details><summary>📄 Abstract</summary>
  Visual content shapes audience perception and opinion on social media, and computational social science increasingly relies on automated tools to analyze images at scale. Yet a measurement gap persists: existing tools rely on predefined categories or produce only coarse image-level labels, while measuring which specific objects appear in an image, how prominently, and where in the frame remains difficult at scale. We introduce Perceive, Refine, Reason (PRR), a calibrated pipeline that turns flex...
  </details>

- **2026-09-13** — Toqeer Ali Syed, Ali Akarma, Adeel Ahmad et al. — [Beyond Scene Description: Multi-Agent Orchestration for Non-visual Access to Virtual Worlds](http://arxiv.org/abs/2609.14512v1)
  <details><summary>📄 Abstract</summary>
  Virtual worlds now host classrooms, meetings, conferences, shops, and social venues, and nearly every interaction they expose assumes a user who can scan a three-dimensional scene, follow avatars, and read floating panels. Blind and visually impaired (BVI) users are left with assistive tools that each solve one task in isolation: naming an object, reading text, describing a scene, or planning a route. A live virtual room defeats that model: obstacles, speakers, gestures, chat, slides, and notifi...
  </details>

- **2026-09-13** — Nitish Kovuru, Prateek Jannu — [CoArena: Evaluating Computer-Use and Multi-Agent Systems in Real Time](http://arxiv.org/abs/2609.14239v1)
  <details><summary>📄 Abstract</summary>
  Static benchmarks for computer-use agents fix a task set at release and score every system against it once. That makes them reproducible, and it lets them drift from what they should measure: a fixed task set ages, leaks into training corpora, and cannot follow how people actually use agents from week to week. CoArena measures use directly. Real users submit tasks; two systems, each a single model or a multi-agent pipeline behind the same tool interface, execute the same task concurrently in ide...
  </details>

- **2026-09-13** — Arya Pulkit, Aditya Ruhela, Akarshan Kapoor et al. — [Lightweight Generalized DeepFake Face Detection with WAVIE: Wavelet Augmented Vision Intermediate Embeddings](http://arxiv.org/abs/2609.14437v1)
  <details><summary>📄 Abstract</summary>
  Deepfake detection systems often exhibit significant performance degradation when deployed on unseen manipulation methods, limiting their reliability in real-world multimedia environments. This lack of generalization poses critical challenges for misinformation mitigation, digital forensics, and human-centric AI systems. Existing detectors perform well on the forgery methods they are trained on, but their accuracy drops sharply on unseen pipelines. To bridge this generalization gap, we propose W...
  </details>

- **2026-09-13** — Madhurananda Pahar, Caitlin Illingworth, Dorota Braun et al. — [CCMAN: Cognitive Instability-Aware Cross-Modal Attention Network for Interpretable Temporal Biomarkers of Verbal Fluency Speech](http://arxiv.org/abs/2609.14764v1)
  <details><summary>📄 Abstract</summary>
  Early detection of cognitive decline from speech offers a scalable and non-invasive alternative to conventional clinical assessment. Verbal fluency tasks are particularly informative, but most automated approaches aggregate features across an entire recording, overlooking temporal speech dynamics. We propose the Cognitive Instability-Aware Cross-Modal Attention Network (CCMAN), a transfer learning framework that learns task-agnostic cognitive speech representations from multiple memory-probing t...
  </details>

- **2026-09-13** — Binghao Wang, Feng Zhang, Wendong Wang et al. — [Robust low-rank tensor completion via factorized weighted tensor schatten-p norm minimization](http://arxiv.org/abs/2609.14307v1)
  <details><summary>📄 Abstract</summary>
  Low-rank tensor factorization provides a flexible framework for completing multidimensional data from incomplete and corrupted observations. However, unweighted spectral regularizers impose a common shrinkage profile across singular components, which may excessively attenuate dominant low-rank components, and factorized variants either lack component-specific weighting or require costly singular value decompositions (SVDs). This paper proposes two weighted Schatten-$p$ tensor factorization model...
  </details>

- **2026-09-12** — Tri Nhu Do, Yosefine Triwidyastuti, Gunes Karabulut Kurt — [Inverse Maxwell-Based Wall-Aware OFDM-ISAC for Slow-Moving Target Sensing](http://arxiv.org/abs/2609.14182v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study integrated sensing and communication (ISAC) for short-range indoor orthogonal frequency-division multiplexing (OFDM) systems in which the sensing path crosses a building wall. The target is a slow-moving user equipment behind the wall, and its echo is embedded in the wall reflection and static indoor clutter. Because the wall adds excess propagation length, attenuation, and internal reflections, a conventional delay transform reports an apparent range. We therefore formul...
  </details>

- **2026-09-10** — Simona Boboila, Xavier Cadet, Edward Koh et al. — [BlueSTAR: Tiered Agentic Architecture for Autonomous Cyber Defense](http://arxiv.org/abs/2609.11852v1)
  <details><summary>📄 Abstract</summary>
  Cyber attacks are increasingly automated, narrowing the time available for human analysts to detect, reason about, and respond to intrusions. Large language models (LLMs) offer a promising foundation for autonomous cyber defense because they can correlate heterogeneous evidence and reason about previously unseen threats. However, directly applying LLMs to operational security telemetry is impractical: raw logs arrive faster than current models can process them, individual events are often ambigu...
  </details>

- **2026-09-10** — Matyáš Veselý, Michal Průšek, Jiří Franc — [Your Retriever Already Knows: Distribution-Shape QPP for RAG Retrieval Sufficiency](http://arxiv.org/abs/2609.11646v1)
  <details><summary>📄 Abstract</summary>
  Standard Retrieval-Augmented Generation (RAG) pipelines often provide no reliable inference-time signal of whether retrieval succeeded; on ambiguous or out-of-scope queries, generation may then hallucinate. Motivated by a Czech nuclear-regulator deployment where data sensitivity precludes third-party LLM APIs, we compare three Query Performance Prediction (QPP) paradigms for retrieval sufficiency in RAG: score-based features, a content-based LLM judge, and a hybrid. On the eight ViDoRe vision do...
  </details>

- **2026-09-10** — Michael Neri — [Domain-Incremental Learning for Multi-Channel Replay Speech Detection](http://arxiv.org/abs/2609.11194v1)
  <details><summary>📄 Abstract</summary>
  Replay attacks are the most accessible threat to voice-controlled systems, and the acoustic cues that expose them are strongly modulated by the environment in which the attack is mounted. A detector deployed in the field therefore has to absorb new acoustic conditions over time, ideally without revisiting past recordings, since retaining speech indefinitely is both expensive and legally constrained. We frame this as Domain-Incremental Learning (DIL) over acoustic environments and present the fir...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 50 papers

- **2026-09-15** — Thanapat Trachu, Samuele Cornell, William Chen et al. — [LACE: Layer-Wise Compression for Dynamic Frame Rate Codecs](http://arxiv.org/abs/2609.17509v1)
  <details><summary>📄 Abstract</summary>
  Neural audio codecs are a key component in speech language modeling. However, their high frame rates lead to long sequence lengths, increasing computational costs. Dynamic frame rate codecs mitigate this by reducing the effective frame rate using a compression step to merge multiple frames together. However, most prior methods either operate on single-codebook codecs or apply a single compression step before multi-layer quantization. This forces all quantization layers to share the same segmenta...
  </details>

- **2026-09-15** — Rong He — [Decomposition Buys Integrity, Not Yield](http://arxiv.org/abs/2609.17464v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems split a task across a tree of agents and justify the split with folklore: smaller contexts, cleaner separation, parallelism. We ask what the split does to how much of what the leaves discover reaches the root. Model a decomposition as a tree in which an agent handed $b$ items keeps any one with probability $r(b)$. If $r(b)=1/b$, every tree delivers exactly one finding, for every task size and every shape; we verify this to $2.4 \times 10^{-15}$ on 20,000 random irregular tree...
  </details>

- **2026-09-15** — Clara Dehman, Daniele Viganò — [Spontaneous wandering of the magnetic axis in pulsars: 3D magneto-thermal simulations and the imprint on braking indices](http://arxiv.org/abs/2609.17436v1)
  <details><summary>📄 Abstract</summary>
  Braking index measurements of hundreds of pulsars, despite observational caveats, show a clear trend: $n<3$ at early ages, $n>3$ at middle ages, and increasingly large, fluctuating values at larger characteristic ages. Crustal magnetic fields in isolated neutron stars evolve through Ohmic dissipation and non-linear Hall redistribution across scales, with additional early-time contributions from the chiral magnetic effect and post-burial re-emergence. Initial conditions are usually assumed dipole...
  </details>

- **2026-09-15** — Adam Zachary Wasserman, David Beauchemin — [Right Tool, Right Job: Native-Language Evaluation, Tokenizer Sensitivity, and Methodological Findings from a French-Only BabyLM](http://arxiv.org/abs/2609.17435v1)
  <details><summary>📄 Abstract</summary>
  We submit MéTRON-FR, a 125M GPT-2 pretrained on 92.47M words of French, to the BabyLM 2026 Strict track. It scores 85.97 +/- 0.17% on QFrBLiMP (a native Quebec-French benchmark of grammatical minimal pairs) and 62.80% on the BabyLM-weighted leaderboard. A cross-lingual GLUE (General Language Understanding Evaluation) protocol that combines French task-data translation with rank-16 LoRA (Low-Rank Adaptation) produces a sharp task-type gradient: relational tasks gain measurably, while world-knowle...
  </details>

- **2026-09-15** — Giannis Kalyvas, Giorgos Filandrianos, Orfeas Menis Mastromichalakis et al. — [An Empirical Study of Counterfactual Self-Explanations in LLMs](http://arxiv.org/abs/2609.17119v1)
  <details><summary>📄 Abstract</summary>
  Large language models can easily generate explanations for their own outputs, but such self-explanations are not necessarily faithful to the model's behavior. We study this issue through counterfactual self-explanations, where a model minimally edits an input so that its own prediction changes. Across sentiment analysis and natural language inference, we evaluate ten instruction-tuned models from the LLaMA-3 and Qwen-2.5 families, measuring faithfulness, minimality, and alignment with human-anno...
  </details>

- **2026-09-15** — Cai Ke, Xin Liu, Han Zhang et al. — [ThinkFlow: Self-Evolving Probabilistic Latent Memory for Lifelong Conversational Agents](http://arxiv.org/abs/2609.17010v1)
  <details><summary>📄 Abstract</summary>
  Lifelong conversational agents rely on memory systems to maintain deep, context-aware interactions with users. However, existing explicit textual memory pipelines suffer from a severe information bottleneck, often losing subtle behavioral patterns and emotional shifts. Furthermore, being typically static post-deployment, they cannot autonomously adapt to personal habits and preferences without manual feedback. Cognitive science, however, suggests that humans maintain mental models purely in a la...
  </details>

- **2026-09-15** — Haonan Huang, Tianrui Qiu, Xianghao Zang et al. — [VOR-Bench: A Human Perception-Driven Benchmark for Video Object Removal](http://arxiv.org/abs/2609.16878v1)
  <details><summary>📄 Abstract</summary>
  Despite its crucial role in video object removal (VOR), existing evaluation paradigms face two critical limitations: questionable references and a misalignment between tradi- tional metrics and human preference. To address these challenges, we introduce VOR- Bench, which advances VOR evaluation through three integrated components. First, we present the VOR Dataset (VORD), the first benchmark dataset providing both paired edited videos and graffiti masks. Its unique strength lies in a diverse dat...
  </details>

- **2026-09-15** — Han Zhiguang, Farah Benamara, Pascale Zaraté — [Integrating the Analytic Hierarchy Process with Large Language Models for Transparent Multi-Criteria Decision-Making](http://arxiv.org/abs/2609.16779v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly employed in a wide range of decision-making tasks. However, the opacity of their internal reasoning makes it difficult to validate or interpret their outputs, and the need for interpretability becomes especially critical in high-stakes settings. This study examines the decision-making capabilities of LLMs through the Analytic Hierarchy Process (AHP), a classical and widely used multicriteria decision-making framework. We construct a new annotated benchmark based on AHP and ...
  </details>

- **2026-09-15** — Abhilaksh Singh Reen, Kushal Borkar, Ritvik Mahapatra — [IMVS: Interactive Medical Volume Segmentation with Test-Time Adaptation - A New Method for Annotating Radiology Datasets](http://arxiv.org/abs/2609.16775v1)
  <details><summary>📄 Abstract</summary>
  Annotating large radiology datasets is bottlenecked by the manual effort of delineating structures slice-by-slice in 3D volumes. Interactive methods reduce this effort but stay interaction-inefficient: slice-wise methods (including many foundation models) ignore inter-slice continuity, while 3D and video-based methods propagate a prompt with a \emph{fixed} propagator that never adapts to the target volume, so it drifts on low-contrast or pathological structures and must be re-prompted. We presen...
  </details>

- **2026-09-15** — Zishuo Zhao, Kai Chen, Ao Li et al. — [Turn-level Multiscale Density Ratio Estimation for LLM Agents](http://arxiv.org/abs/2609.16760v1)
  <details><summary>📄 Abstract</summary>
  With the rapid development of Large language model (LLM), agent systems enhanced by LLMs show huge potential in being able to deal with complex tasks, especially involving multi-step thinking or interaction with tools. For applying LLM techniques with a well-designed agent paradigm, post-training of LLM in multiple agent scenarios is necessary to achieve better performance. Among the variable post-training techniques, alignment methods such as PPO, DPO, DIL, and GRPO become popular because many ...
  </details>

- **2026-09-15** — Yihan Chen, Huan Ren, Wenfei Yang et al. — [PriorPose: Reference-Guided Joint Deformation and Alignment for Category-Level Object Pose Estimation](http://arxiv.org/abs/2609.16727v1)
  <details><summary>📄 Abstract</summary>
  Category-level object pose estimation seeks to recover a similarity transform $(R,t,s)$ for unseen instances without instance-specific CAD models. Most competitive methods are correspondence-based: prior-free variants regress canonical (NOCS) coordinates directly from local observations and implicitly memorize the canonical frame in the weights, which ties the parameters to category-typical orientations and hurts generalization under distribution shift; prior-based variants introduce a category ...
  </details>

- **2026-09-15** — Hailong Shu — [Predictability-Guided Multiscale Probabilistic Forecasting of Wind Direction under Extreme Shear](http://arxiv.org/abs/2609.16707v1)
  <details><summary>📄 Abstract</summary>
  Accurate multi-horizon wind direction forecasting is critical for turbine yaw control and grid security. Rapid directional shear (turning $\ge 90^\circ$) challenges models via non-Euclidean geometry on $S^1$, multiscale dynamics, and regime-dependent uncertainty. Conventional discrete models and foundation models suffer from mid-frequency phase lag and turning misalignments. We show that directional predictability decays at disparate rates across frequency subbands, rendering monolithic mechanis...
  </details>

- **2026-09-15** — Yu Li, Zhengran Shen, Yachun Mi et al. — [Bridging the Perceptual Gap: Residual-Enhanced Downscaling and Manifold-Aware Perception Alignment Adaptation for NR-IQA](http://arxiv.org/abs/2609.16664v1)
  <details><summary>📄 Abstract</summary>
  Leveraging Large Vision-Language Models like CLIP has recently set new benchmarks for No-Reference Image Quality Assessment (NR-IQA). However, the contrastive pretraining of CLIP inherently prioritizes semantic invariance, which often suppresses subtle perceptual signals, a phenomenon we term perceptual submergence. Furthermore, standard preprocessing techniques (e.g., cropping and interpolation) further exacerbate the loss of critical high-frequency quality cues. In this paper, we propose the C...
  </details>

- **2026-09-15** — Jeng Wen Joshua Lean, Ting-Yu Yen, Wei-Fang Sun et al. — [G3AR: Graph-Guided Neural Visual Geometry for Scalable Multi-Sequence Aerial Registration](http://arxiv.org/abs/2609.16603v1)
  <details><summary>📄 Abstract</summary>
  Full-context neural visual geometry is impractical for thousands of images, while sequence-based chunking poorly captures irregular non-local overlap in multi-sequence aerial collections. We present Graph-Guided Neural Visual Geometry for Aerial Registration (G3AR), a graph-guided framework for scalable dense neural geometry. Before local inference, G3AR builds a geometrically verified image-proximity graph that guides bounded overlapping chunks and induces a chunk graph whose maximum spanning t...
  </details>

- **2026-09-15** — Guangyu Sun, Shlok Kumar Mishra, Wentao Bao et al. — [FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal Tokens for Retrieval and Generation](http://arxiv.org/abs/2609.16591v1)
  <details><summary>📄 Abstract</summary>
  Traditional multimodal representation learning and generation are two stages: a contrastive or self-supervised visual encoder is trained first, followed by a separate downstream generative model. This setup bottlenecks generative performance behind frozen embeddings. To bridge this gap, we revisit joint multimodal representation learning and generation to produce linearly interpolatable embeddings that are directly consumable by generative decoders. We present FLAT (Flexible-Length Aligned Trans...
  </details>

- **2026-09-15** — Keqing Zhang, Jingyu Chen, Yufan Liu et al. — [Do LLMs Have Values? A Quantitative Analysis and Alignment Framework for Values in Large Language Models](http://arxiv.org/abs/2609.16589v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) increasingly handle complex subjective tasks, aligning their intentions and behaviors with human values has become a critical scientific challenge. However, current efforts are confounded by a striking behavioral paradox: they fluctuate unpredictably under minor wording changes ("swing"), yet stubbornly ignore explicit instructions to correct ingrained biases ("rigidity"). Resolving this duality is critical for reliable AI alignment. To systematically understand a...
  </details>

- **2026-09-15** — Istabrak Abbes, Nizar Islah, Irina Rish et al. — [What Does Layer-Importance Reveal About Transformers and State-Space Models?](http://arxiv.org/abs/2609.16537v1)
  <details><summary>📄 Abstract</summary>
  Transformers and state-space models (SSMs) are the two dominant families of sequence models, and a central open question is how far the analytical knowledge built for transformers transfers to SSMs. We address this through the lens of layer importance which underpins compression, selective fine-tuning, and interpretability across both families. We decompose layer importance into two distinct notions. \emph{Necessity} captures how much the pretrained model depends on a layer's existing contributi...
  </details>

- **2026-09-15** — Qian Chen, Xiangang Li, Xiang Lv et al. — [The Evolving Bottleneck in Speech Generation: Interface Co-design and Staged Alignment from CosyVoice to Qwen-Audio-3.0-TTS](http://arxiv.org/abs/2609.16514v1)
  <details><summary>📄 Abstract</summary>
  Speech synthesis systems are commonly narrated as a sequence of larger models, better tokenizers, and broader data. This technical retrospective offers a different account of the CosyVoice lineage, from CosyVoice through CosyVoice 2 and CosyVoice 3 to Qwen-Audio-3.0-TTS: progress came from repeatedly relocating the system's dominant bottleneck. Across the lineage, a stable decomposition separates an autoregressive language model that plans speech from a flow-matching model that renders acoustics...
  </details>

- **2026-09-15** — Quanwei Liu, Tao Huang, Jiaqi Yang et al. — [VPRef: A Cross-Domain Benchmark for Referring Remote Sensing Image Segmentation](http://arxiv.org/abs/2609.16486v1)
  <details><summary>📄 Abstract</summary>
  Rapid advancements in vision-language models have propelled Referring Remote Sensing Image Segmentation (RRSIS) to the forefront of Earth observation. However, practical deployments suffer severe performance degradation under a coupled dual-drift paradigm: visual domain drift from cross-spatial-resolution mismatches and spectral variations, alongside textual logic drift from unconstrained, variable user-input granularities. To mitigate these bottlenecks, this paper establishes the first cross-do...
  </details>

- **2026-09-15** — Muhammad Ashar Ishfaq, Glaucia Melo — [ToMAS: A Pilot Failure-Grounded Theory-of-Mind Benchmark from Multi-Agent LLM Failures](http://arxiv.org/abs/2609.16986v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems can fail even when communication succeeds because agents do not correctly track their peers' roles, knowledge, or intentions. We investigate whether such inter-agent misalignment cases, labelled FC2 in MAST-Data, can be converted into functional partner-state reasoning items. ToMAS applies four explicit convertibility criteria to diagnosed execution traces. A full conversion pass over 242 eligible non-AG2 training traces produced 39 CLEAN items. In an 18-trace relia...
  </details>

- **2026-09-14** — Vincent Karpf, Joseph Reth, Eike Gerhardt et al. — [Metacognitive Steering: Learning the Structure of Scientific Judgment](http://arxiv.org/abs/2609.16245v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon scientific discovery requires agents to alternate between exploration, disciplined execution, and critical reassessment as evidence changes. Current language models are trained primarily on the products of science and optimized using outcome-level signals, providing limited supervision for these process-level shifts in scientific judgment. We investigate whether such judgment can be recovered from scientist interaction traces and used to control the internal computation of a frozen ...
  </details>

- **2026-09-14** — Yingjia Wan, Lin Lin, Elisa Kreiss — [How Humans and LLMs Read Gender into Gender-Neutral Physical Descriptions](http://arxiv.org/abs/2609.16366v1)
  <details><summary>📄 Abstract</summary>
  When foundation models describe people, recent work in AI fairness, accessibility, and ethics recommends avoiding inferred identity labels (e.g., "she", "his") in favor of seemingly "objective" physical descriptions (e.g., "short hair", "a defined jawline"). Yet whether such descriptive language achieves gender-neutral communication remains an open empirical question. To study this, we introduce GAPA (Gender Associations of Physical Attributes), a dataset of 316 common physical attributes drawn ...
  </details>

- **2026-09-14** — Nunzio Lorè, Hongan Zhu, Babak Heydari — [Cheap Talk Stabilizes Strategic Interaction in LLM Agents](http://arxiv.org/abs/2609.16270v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as interacting agents, making the persistence of their action policies across repeated interaction critical for reliable multi-agent operation. We investigate whether and how agent-generated, non-binding pre-play communication ("cheap talk") increases such persistence in four open-weight 7-9B-parameter LLMs. Our experiments span four repeated two-player games -- Prisoner's Dilemma, Snowdrift, Stag Hunt, and Harmony -- with incentive structures rang...
  </details>

- **2026-09-14** — Yiwei Yang, Haoxiang Zhang, Bingbing Wen et al. — [Spurious Tool Use: When RL Agents Learn the Wrong Reason to Act](http://arxiv.org/abs/2609.16268v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly interleave natural language reasoning with external tools such as web search and code execution. These tool-use policies are often optimized via reinforcement learning (RL), which can amplify spurious correlations in the training data. In this work, we study when and why RL-trained agents learn shortcut tool-selection policies: invoking tools based on superficial prompt cues rather than genuine task requirements. We construct controlled synthetic en...
  </details>

- **2026-09-14** — Mantek Singh, Jeshwanth Challagundla, Siddharth Raina et al. — [Efficient Reasoning Distillation: Small Video-Language Models via Synthetic CoT and Difficulty-Aware Fine-Tuning](http://arxiv.org/abs/2609.16255v1)
  <details><summary>📄 Abstract</summary>
  We present an efficient method to distill reasoning capabilities into compact video-language models (VLMs) for video question answering (VideoQA). Our approach fine-tunes a 2B-parameter model using only $\sim$900 uncertainty-selected examples, each augmented with synthetic chain-of-thought (CoT) rationales generated by a 4B teacher. Despite its minimal compute cost - under two hours on a single A100 GPU - our method enables the 2B model to outperform VLMs up to 4$\times$ larger, and generalize a...
  </details>

- **2026-09-14** — Asraful Haque, Christopher M. Rouleau, Rama K. Vasudevan et al. — [An Open-Source Hardware and Software Toolkit to Enable Agentic RHEED-Guided Thin-Film Synthesis](http://arxiv.org/abs/2609.15922v1)
  <details><summary>📄 Abstract</summary>
  Reflection high-energy electron diffraction (RHEED) provides rich information about evolving surfaces during thin-film growth, but non-automated, operator-dependent alignment and fragmented analysis workflows limit its potential in fully autonomous synthesis. Here, we present an open-source hardware and software toolkit that makes RHEED control and quantitative analysis accessible to operators and artificial intelligence (AI) agents. Demonstrated on a pulsed laser deposition system, the toolkit ...
  </details>

- **2026-09-14** — Kyle O'Brien, Edward James Young, Puria Radmard et al. — [Inoculation Midtraining with Learned Neologisms](http://arxiv.org/abs/2609.15886v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often learn both desirable and undesirable properties during post-training. We study whether midtraining, an earlier training stage, can shape which of these properties later generalise. We introduce Inoculation Midtraining, a technique that teaches a base model that unsafe behaviour belongs to a designated <quarantine_token> context, as indicated by the <quarantine_token> neologism (a new token) introduced during midtraining, and then post-trains the model on unsafe...
  </details>

- **2026-09-14** — Natalie Collina, Surbhi Goel, Aaron Roth et al. — [Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control](http://arxiv.org/abs/2609.15803v1)
  <details><summary>📄 Abstract</summary>
  Long-running AI agents create a control problem: each action they take changes the state, which in turn affects the trajectory of future actions. If the agent is not fully aligned, then guaranteeing safety requires approving consequential actions before allowing them to be executed. But requiring human approval at every step makes attention a bottleneck. Delegating review to other AI agents raises the same alignment problem: the reviewers may themselves be misaligned. We identify a condition on ...
  </details>

- **2026-09-14** — Mingzhi Chen, Yiyu Gui, Guibo Luo et al. — [A Language-Guided Multimodal Foundation Model for Zero-Shot and Multi-Task Brain Signal Analysis](http://arxiv.org/abs/2609.15740v1)
  <details><summary>📄 Abstract</summary>
  Brain signal analysis is essential for both neuroscience research and clinical diagnostics, yet current approaches face critical limitations. End-to-end models require task-specific retraining and exhibit limited generalization, while pre-trained models lack semantic depth and still depend on extensive fine-tuning. Meanwhile, general-purpose multimodal foundation models, though powerful in other domains, struggle to interpret brain signals due to representational misalignment and lack of domain ...
  </details>

- **2026-09-14** — Matteo Barbieri, Giammarco La Barbera, Juan Pablo De La Plata et al. — [Benchmarking Intra-Patient 3D Deformable Multimodal Image Registration](http://arxiv.org/abs/2609.15669v1)
  <details><summary>📄 Abstract</summary>
  Multimodal image registration is a key component of many clinical workflows, yet it remains challenging because corresponding anatomical structures often exhibit substantially different image intensities across modalities. In this work, we present a comprehensive benchmark of intra-patient 3D multimodal deformable registration methods across three datasets covering different anatomical regions and difficulty levels, including both synthetic deformation recovery and real clinical scenarios. We ev...
  </details>

- **2026-09-14** — Jiayang Gu, Zheng Fang, Lichaun Xiang et al. — [Principal-timestep Restricted Init via Sparse Matrix-decomposition in Flow-matching](http://arxiv.org/abs/2609.15643v1)
  <details><summary>📄 Abstract</summary>
  Flow-matching diffusion models have recently emerged as a strong paradigm for high-fidelity visual generation. However, their prohibitively high fine-tuning cost limits scalability to downstream tasks. While Low-Rank Adaptation (LoRA) combined with spectral initialization has demonstrated accelerated convergence and improved performance in autoregressive language models by better aligning gradient directions, we find that it fails to deliver similar gains in diffusion fine-tuning, often yielding...
  </details>

- **2026-09-14** — Jiahao Chang, Dong Du, Wanhu Sun et al. — [SAM3D-Part: Interactive Part Selection and Generation from 3D Objects](http://arxiv.org/abs/2609.15639v1)
  <details><summary>📄 Abstract</summary>
  Part-level control is essential for modern 3D asset creation, where objects are frequently edited, reused, animated, or fabricated through their individual components. In many such workflows, users need only several specific components rather than a complete object decomposition. However, existing 3D generation methods produce all parts regardless of user intent, while promptable 3D segmentation methods typically output partial surfaces instead of reusable complete meshes. In addition, image-con...
  </details>

- **2026-09-14** — Weixin Xu, Zhenyu Yang, Bing Wang et al. — [VideoScout: Learning Agentic Active Exploration with Adaptive Reasoning Pacing for Long Video Understanding](http://arxiv.org/abs/2609.15606v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have achieved remarkable progress on short video understanding yet remain limited on long videos due to the limited visual context window. Prevailing approaches rely on uniform frame sampling or recent coarse-to-fine agentic zooming, both of which struggle to localize sparse, decisive evidence in sufficiently long videos. We formulate long video understanding as a \textbf{Sequential Evidence Acquisition (SEA)} problem, in which an agent reads the video tu...
  </details>

- **2026-09-14** — Yang Xing, Jiong Wu, Savas Ozdemir et al. — [A Unified Vision-Language Model for PSMA PET/CT Report Generation, Visual Question Answering, and Lesion Segmentation](http://arxiv.org/abs/2609.15603v1)
  <details><summary>📄 Abstract</summary>
  Accurate PSMA PET/CT interpretation is central to prostate cancer management, yet existing PET/CT AI models typically address isolated tasks. We propose a unified PSMA PET/CT vision-language model for report generation, visual question answering, and lesion segmentation. The framework adopts an LLaVA-style architecture, comprising a PET/CT vision encoder, an MLP-Mixer projection module, a LoRA-tuned large language model, and a 3D segmentation branch. Training followed a four-stage strategy: visi...
  </details>

- **2026-09-14** — Stephane Hatgis-Kessell, W. Bradley Knox, Emma Brunskill — [Specifying Reward Functions for RL Without Environment Sampling](http://arxiv.org/abs/2609.15544v1)
  <details><summary>📄 Abstract</summary>
  Enabling human stakeholders to specify reward functions that lead to their desired outcomes is a key challenge in deploying reinforcement learning agents. Preference-based methods such as online RLHF can reduce the burden of manual reward design, but they require repeatedly training policies, sampling trajectories from the real world, and eliciting feedback, making them impractical in settings where environment interaction is computationally expensive or unsafe. We introduce Experience-Free Auto...
  </details>

- **2026-09-14** — Qiangqiang Zhou, Wenjun Tang, Yong Chen et al. — [ViCo-SAM3: Vision-Conditioned Alignment for Open-Vocabulary Camouflaged Object Segmentation](http://arxiv.org/abs/2609.15418v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary camouflaged object segmentation (OVCOS) aims to segment unseen camouflaged objects under text guidance. We observe that SAM3 still suffers from a pronounced semantic gap between global textual semantics and fine-grained pixel-level visual cues in OVCOS. Meanwhile, fully fine-tuning the text encoder introduces heavy parameter overhead and risks overfitting to training categories, which compromises open-vocabulary representation flexibility. To address these issues, we propose ViCo...
  </details>

- **2026-09-14** — Chenxu Liu, Zilu Zou, Peizhong Gao et al. — [IWC-Bench: Evaluating Web Application Generation from a Software Testing Perspective](http://arxiv.org/abs/2609.15387v1)
  <details><summary>📄 Abstract</summary>
  Human evaluation provides a direct measure of the quality of LLM-generated web applications. However, fitting human judgments through automated evaluation remains challenging. Static benchmarks can credit functionality that exists in source code but is unreachable at runtime. Interactive benchmarks exercise the application, yet incomplete exploration can cause them to miss implemented functionality and confound application defects with agent execution failures. To address these limitations, we p...
  </details>

- **2026-09-14** — Qingyu Liu, Rixi Xu, Yushen Chen et al. — [Cross-Lingual F5-TTS 2: A Simplified Framework for Language-Agnostic Voice Cloning](http://arxiv.org/abs/2609.15184v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot text-to-speech (TTS) can clone a speaker's voice from a short audio prompt, yet most TTS systems still require the audio prompt transcript during inference. This dependency prevents cross-lingual voice cloning when the audio prompt transcript is unavailable, particularly for unseen languages. Cross-Lingual F5-TTS removes this dependency and enables transcript-free cross-lingual voice cloning, but it prepares its training data with forced alignment. Forced alignment is sensitive to boun...
  </details>

- **2026-09-14** — Hanzhang Tu, Zhanfeng Liao, Wei Min et al. — [Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](http://arxiv.org/abs/2609.15032v1)
  <details><summary>📄 Abstract</summary>
  Live free-viewpoint visualization of real humans is critical for immersive communication and interactive digital experiences. Existing methods either rely on computationally expensive optimization or require calibrated cameras and low-resolution inputs, making real-time high-resolution deployment impractical. In this work, we present Tele360, the first real-time feed-forward system for dynamic human reconstruction and live free-viewpoint visualization from sparse, unposed RGB streams. Our system...
  </details>

- **2026-09-14** — Frank Li — [Validating Hybrid-State Cache Recovery for GLM-5.3-Flash with vLLM and LMCache](http://arxiv.org/abs/2609.15030v1)
  <details><summary>📄 Abstract</summary>
  External cache transfers can succeed while a hybrid language model resumes from an inconsistent state. We examine the full 45-layer GLM-5.3-Flash model, using the RedHatAI/ GLM-5.3-Flash-NVFP4 quantized checkpoint with vLLM and LMCache under four-way tensor parallelism. A complete-hit recovery mismatch restored state for the full prompt while the scheduler credited one fewer token. We aligned recovery through strict-prefix lookup and established a numerical comparison using shared computation co...
  </details>

- **2026-09-14** — Quang Phuoc Nguyen, Félix Gaschi, David Anugraha et al. — [Online Language Adaptive Sampling for Better Distributed Cross-lingual Gains](http://arxiv.org/abs/2609.14969v1)
  <details><summary>📄 Abstract</summary>
  Realignment is a promising approach for improving the cross-lingual transfer ability of multilingual language models, particularly for extremely low-resource languages (LRLs). However, existing realignment methods rely on uniform and random sampling of parallel sentences across languages, which may be suboptimal under limited batch sizes. In practice, models may benefit from seeing certain languages more frequently, especially those that are poorly aligned, and the optimal distribution can evolv...
  </details>

- **2026-09-14** — Chandan Kumar Sah, Jishnu Keshavan — [Exact Feasibility Certification and Optimal Responsibility Allocation for Multi-Robot CBF Safety Filters](http://arxiv.org/abs/2609.14935v1)
  <details><summary>📄 Abstract</summary>
  Multi-robot Control Barrier Function (CBF) safety filters can become infeasible, but a failed quadratic program (QP) does not indicate why the conflict occurred or how to resolve it. To address this, we develop an exact feasibility certificate for multi-agent CBF filters with heterogeneous control-affine dynamics and convex input sets. The certificate quantifies a feasibility reserve by separating the demand imposed by safety constraints from the available actuator supply. This decomposition sho...
  </details>

- **2026-09-14** — Jiayi Yuan, Hangoo Kang, James Jihao Liu et al. — [Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning](http://arxiv.org/abs/2609.14896v1)
  <details><summary>📄 Abstract</summary>
  A notable byproduct of LLM alignment training is mode collapse: the progressive loss of output diversity that narrows a model's expressivity at inference time. This degradation is especially limiting for applications requiring open-ended exploration and pluralistic perspectives, such as scientific ideation and creative writing. We present MoDA (Mode-conditioned Diversity Alignment), an online post-training RL algorithm that jointly optimizes generation quality and diversity, inspired by the coor...
  </details>

- **2026-09-14** — Naihao Deng, Samee Arif, Shuaichen Chang et al. — [One Example Is Enough to Pass Fairness Benchmarks: Rethinking Fairness Evaluation for Aligned LLMs](http://arxiv.org/abs/2609.14860v1)
  <details><summary>📄 Abstract</summary>
  Warning: This submission studies stereotypes and biases, and contains toxic and offensive examples, used for illustration purposes only.   Fairness benchmarks such as BBQ have become the de facto standard for fairness evaluation across major model families. We argue that these benchmarks are too easy to support their role: training Qwen 2.5 7B Base with Group Relative Policy Optimization (GRPO) on a single BBQ example, or placing that example in context as a one-shot demonstration for in-context...
  </details>

- **2026-09-13** — Jingbin Hu, Luyu Wang, Wenjie Tian et al. — [Bridging Data, Reasoning, and Alignment: A Unified Framework for Context-Aware Instruction-Following TTS](http://arxiv.org/abs/2609.14740v1)
  <details><summary>📄 Abstract</summary>
  The ISCSLP 2026 CoT-TTS Challenge requires TTS systems to generate Chain-of-Thought (CoT) reasoning from dialogue history before synthesizing contextually appropriate speech. While the official baseline establishes a unified architecture, it remains constrained by limited contextual comprehension, weak instruction fidelity, and suboptimal audio quality. We present a systematic optimization pipeline to address these limitations. First, we develop a data process framework that cleans raw data via ...
  </details>

- **2026-09-13** — Guocun Wang, Kenkun Liu, Guorui Song et al. — [Open-UniMo: Towards Unified Motion-Language Understanding and Generation in the Open World](http://arxiv.org/abs/2609.14615v1)
  <details><summary>📄 Abstract</summary>
  Unified motion generation and understanding is crucial for embodied AI systems that can both synthesize and interpret human actions in open-world environments. Existing motion-language models often treat motion as an auxiliary modality of a language model, leading to text-dominated representations and limited cross-modal interaction. Moreover, the next-token prediction paradigm is not naturally suited to long motion sequences, where autoregressive generation may accumulate prediction errors. To ...
  </details>

- **2026-09-13** — Liangjian Wen, Linjie Li, Jiang Duan et al. — [Dependency, Compression, and Synergy: A Unified Information-Theoretic View of Multimodal Learning](http://arxiv.org/abs/2609.14421v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multimodal foundation models have intensified the need to understand how different modalities share, preserve, and complement information. Mutual Information (MI), the Information Bottleneck (IB), and Partial Information Decomposition (PID) provide complementary perspectives, yet existing studies often treat them as isolated tools. This survey presents an information-theoretic perspective connecting these principles as progressively refined views of multimodal information proc...
  </details>

- **2026-09-13** — Sarah Y. Li, Elijah Renner, Rayan Ansari et al. — [Corpus Characterization and Inverse Constitutional Fine-Tuning for Style-Aware Radiology Reports](http://arxiv.org/abs/2609.14226v1)
  <details><summary>📄 Abstract</summary>
  Automated radiology report generation has advanced rapidly in diagnostic accuracy, yet generated reports frequently diverge from the stylistic conventions of authentic radiologist writing in structure, diction, and uncertainty language, a gap which has direct implications for clinician trust and user experience. To address this, we characterize stylistic variation across 2,000 reports from the CheXpert Plus dataset using Bio-ClinicalBERT embeddings, UMAP dimensionality reduction, and HDBSCAN clu...
  </details>

- **2026-09-13** — Yixian Gao, Hongyu Liu, Yang Liu — [On passive recovery of structured elastic density and initial states](http://arxiv.org/abs/2609.14215v1)
  <details><summary>📄 Abstract</summary>
  We study simultaneous recovery of the (variable) mass density, initial displacement, and initial velocity for the three-dimensional isotropic elastic wave equation with known constant Lamé parameters. The data are the complete displacement trace on an enclosing boundary. We first assume that the density-weighted initial displacement and velocity have fixed known profiles in one spatial direction. The $s^0$ and $s^1$ coefficients of the zero-frequency Laplace expansion identify these weighted sta...
  </details>

- **2026-09-12** — Prajjwal Bhattarai, Tuka Alhanai — [Signatures of Steerability in Activation Space of Language Models](http://arxiv.org/abs/2609.14151v1)
  <details><summary>📄 Abstract</summary>
  Steering language models using a set of contrastive representations has been a canonical and computationally efficient method for controlling model behavior. Despite this success in controlling certain model behaviors, the effectiveness of activation steering varies markedly across concepts; the generalization properties of steering vectors are often considered a function of the dataset used to construct them. We make this dataset-dependence claim more rigorous and show that simple separation me...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 62 papers

- **2026-09-15** — Jahanvi Rajput, Dhruv Kudale, Saikiran Kasturi et al. — [Tables Decoded: DELTA for Structure, TARQA for Understanding](http://arxiv.org/abs/2609.17458v1)
  <details><summary>📄 Abstract</summary>
  Table understanding is a core task in document intelligence, encompassing two key subtasks: table reconstruction and table visual question answering (TabVQA). While recent approaches predominantly rely on vision- language models (VLMs) operating on table images, we propose a more scalable and effective alternative based on structured textual representations. These representations are easier to process, align more naturally with LLMs, and eliminate the need for language-specific visual encoders, ...
  </details>

- **2026-09-15** — Oier Larumbe-Lizarraga, Roberto Pereira, Cristian J. Vaca-Rubio — [Goal-oriented probabilistic forecasting for dynamic PRB allocation in 5G networks](http://arxiv.org/abs/2609.17297v1)
  <details><summary>📄 Abstract</summary>
  Efficient physical resource block (PRB) allocation in 5G networks requires accurate demand forecasting. Conventional methods minimize symmetric error metrics (MAE, RMSE), ignoring the operational cost asymmetry where under-provisioning (service degradation) is far costlier than over-provisioning (wasted capacity). We propose a goal-oriented probabilistic forecasting framework that aligns model training with the operator's decision-making objectives. Specifically, we train DeepAR and Temporal Fus...
  </details>

- **2026-09-15** — Md. Samiul Alim, Mahir Shahriar Tamim, Tanvir Ahmed Khan et al. — [Can LLMs Follow the Pulse of a Crisis? Evaluating Crisis Sentiment in Bangladesh's July Uprising](http://arxiv.org/abs/2609.16997v1)
  <details><summary>📄 Abstract</summary>
  Crisis sentiment analysis is especially challenging for low-resource languages such as Bangla, where language, context, and public reaction shift rapidly. We introduce UNRESTSENT200K, a Bangla crisis sentiment dataset with approximately 200K Facebook and YouTube comments from the July-August 2024 Bangladesh uprising. The dataset covers five event-aligned phases, from early escalation and internet blackout to regime transition and a later flood crisis. Each comment is linked to its parent post, e...
  </details>

- **2026-09-15** — Zeyi Shao, Haowen Hua, Jiaxin Zhang et al. — [TecoPrompt: Temporal-Conservative Prompt Learning for Vision-Language Models](http://arxiv.org/abs/2609.16858v1)
  <details><summary>📄 Abstract</summary>
  Prompt learning adapts vision-language models, such as CLIP, by adjusting a small set of context tokens. However, under few-shot supervision, even moderate label noise can disrupt prompt optimization. To address this issue, we propose TecoPrompt, a closed-loop robust prompt-learning framework that revisits optimal transport (OT) pseudo-labeling from a temporal perspective. TecoPrompt employs an entropic OT plan in the CLIP semantic space to obtain globally consistent label candidates. It verifie...
  </details>

- **2026-09-15** — Fangke Chen, Sirry Chen, Wei Chen et al. — [SOTER: A Generative Time-Series Foundation Model for Wearable Human Physiological Signals](http://arxiv.org/abs/2609.16804v1)
  <details><summary>📄 Abstract</summary>
  Time-series foundation models have demonstrated strong cross-domain transfer, yet their common architectural assumptions remain poorly aligned with wearable physiological signals, which are multichannel, irregularly sampled, noisy, and governed by coupled continuous-time dynamics spanning distinct spectral scales. We present SOTER, a generative foundation model for wearable physiological time series that unifies cross-channel coupling, spectrum-guided expert specialization, and continuous-time l...
  </details>

- **2026-09-15** — Yuqi Wang, Fengyuan Liu, Haochen Luo et al. — [RoleBreak: Benchmarking Long-Horizon Role-Playing Robustness in Spoken Dialogue](http://arxiv.org/abs/2609.16614v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-speech dialogue models increasingly support persona control, yet existing spoken role-playing benchmarks remain largely character-centric and short-horizon. This leaves open whether spoken dialogue models can sustain diverse roles over extended interactions, especially beyond predefined fictional characters. We introduce RoleBreak, an open benchmark for long-horizon role-playing robustness in spoken dialogue. RoleBreak contains 310 character-based and user-centered roles, 6,688 human-v...
  </details>

- **2026-09-15** — Junle Li, Weixian Waylon Li, Fuxiang Wu et al. — [SAVLA: Symmetry-Aware Vision-Language-Action Models for Robotic Manipulation](http://arxiv.org/abs/2609.16641v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have become the dominant paradigm for language-conditioned robot manipulation. However, although images and language instructions inherently encode geometric information, VLAs acquire their spatial competence purely from demonstrations. As a result, they are reliable only within the range of scene poses that the demonstrations cover. We propose SAVLA, an end-to-end symmetry-aware VLA model for robust and data-efficient policy learning. Our approach keeps the p...
  </details>

- **2026-09-15** — Haichen Hu, Yuheng Zhang, David Simchi-Levi — [Coupled Calibration and Learning: Mitigating Teacher Bias in LLM Distillation without Target-Domain Reward Feedback](http://arxiv.org/abs/2609.17474v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) distillation aims to transfer the capabilities of a powerful teacher to a smaller student. Direct imitation, however, can also transfer the teacher's systematic bias and errors. This challenge is particularly pronounced under covariate shift, when the teacher's reliability on target questions is uncertain and target-domain reward feedback is unavailable. We propose Coupled Calibration and Learning (CCL), an LLM distillation algorithm that couples teacher calibration wi...
  </details>

- **2026-09-15** — Ting-Wei Chang, Hen-Hsen Huang, Hsin-Hsi Chen — [Enhancing Accessibility of Medical Texts through Large Language Model-Driven Plain Language Adaptation](http://arxiv.org/abs/2609.17398v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the challenge of making complex healthcare information more accessible through automated Plain Language Adaptation (PLA). PLA aims to simplify technical medical language, bridging a critical gap between the complexity of healthcare texts and patients' reading comprehension. Recent advances in Large Language Models (LLMs), such as GPT and BART, have opened new possibilities for PLA, especially in zero-shot and few-shot learning contexts where task-specific data is limited. In...
  </details>

- **2026-09-15** — Jiacheng Wei, Jerry Bai, Xiaoyu Yue et al. — [XPACE: Joint World and Action Modeling from Heterogeneous Experience](http://arxiv.org/abs/2609.17372v1)
  <details><summary>📄 Abstract</summary>
  A general-purpose robot needs to draw on diverse experience, choose actions, and anticipate how those actions will change the world. We introduce XPACE, a unified embodied world model that serves as both a world action model, jointly predicting executable robot actions and future video, and a world simulator, predicting the visual consequences of prescribed actions. Our key insight is that video prediction can both connect heterogeneous experience to action learning and generate new experience f...
  </details>

- **2026-09-15** — Yang Liu, Yifan He, Wenhao Zhao et al. — [TIO-Former: Ultra-Lightweight 6-Directional ToF-Inertial Odometry for Nano-UAVs via a Streaming Causal Transformer](http://arxiv.org/abs/2609.17198v1)
  <details><summary>📄 Abstract</summary>
  Autonomous nano-UAV navigation requires accurate ego-motion estimation under stringent size, weight, power, and computing (SWaP-C) constraints, where visual sensors and LiDARs exceed payload limits, optical flow degrades in low-texture scenes, and inertial-only state estimation is susceptible to accumulated drift. While multi-zone time-of-flight (ToF) arrays provide a lightweight metric complement, 6-DoF estimation from merely 384 ranges per frame is challenged by invalid returns, anisotropic ob...
  </details>

- **2026-09-15** — Long-Vu Hoang, Naomi Harte — [Audio-Visual Turn-taking Prediction in Cocktail Party Scenarios](http://arxiv.org/abs/2609.17056v1)
  <details><summary>📄 Abstract</summary>
  Current predictive turn-taking models (PTTMs) achieve strong performance on benchmarks with controlled acoustic conditions and clean audio signals. Their generalisation to conversations with overlapping speech and background interference remains underexplored. In this research, we evaluate audio-visual PTTMs trained with clean data on a challenging cocktail-party testbed derived from the AVCocktail dataset, and analyse their adaptation behaviour to this new domain. Experimental results show cons...
  </details>

- **2026-09-15** — Liana Toderean, Tudor Cioara, Vasilis Michalakopoulos et al. — [Distributed JEPA: A Self-Supervised Framework for Energy Forecasting](http://arxiv.org/abs/2609.17029v1)
  <details><summary>📄 Abstract</summary>
  Traditional energy forecasting solutions rely on task-specific supervision and energy asset representations, limiting transferability and the ability to capture general temporal dynamics across heterogeneous assets. We address this by proposing a distributed Joint Embedding Predictive Architecture (JEPA) for self-supervised learning from heterogeneous energy time-series. The framework predicts latent representations of masked temporal segments while integrating temporal observations and contextu...
  </details>

- **2026-09-15** — Qinhong Lin, Yuhao Zhang, Yinglun Feng et al. — [SKIP: a Self-knowledge-guided Step-wise Preference Learning Framework for Concise Reasoning](http://arxiv.org/abs/2609.17019v1)
  <details><summary>📄 Abstract</summary>
  While Chain-of-Thought (CoT) reasoning has been proven to be effective, it often leads to overthinking, resulting in computational overhead, inference latency, and even degraded performance in large language models (LLMs). Existing concise reasoning frameworks significantly compromise accuracy while compressing the length of output. In this paper, we propose SKIP, a self-knowledge-guided step-wise preference learning framework. Starting with lightweight fine-tuning to adjust the model's output s...
  </details>

- **2026-09-15** — Philipp Grünter, Karl Henrik Johansson, Angela Fontan — [On personal recommendations in social networks](http://arxiv.org/abs/2609.17011v1)
  <details><summary>📄 Abstract</summary>
  Social networks in which algorithms actively influence humans through personal recommendations are ubiquitous. While opinion dynamics is an established tool to analyze these systems, existing models typically do not capture how individual agents process personal recommendations. In this work, we introduce a model for personal recommendations that is analytically tractable and consistent with the confirmation bias phenomenon from behavioral psychology. We describe how individuals process recommen...
  </details>

- **2026-09-15** — Julio C. Amador Diaz Lopez — [When Confidence Signals Disagree: Local and Global Confidence in Autoregressive Language Models](http://arxiv.org/abs/2609.16933v1)
  <details><summary>📄 Abstract</summary>
  Modern predictive systems expose multiple quantities that are commonly interpreted as measures of confidence. However, these quantities can summarize different aspects of the predictive process. This distinction matters when confidence is used to evaluate reliability or inform downstream oversight and control. We investigate whether different confidence readouts are empirically interchangeable in an autoregressive language model by comparing local confidence, defined from the probability of the ...
  </details>

- **2026-09-15** — Guy Azran, Michael Navat, Sarah Keren — [Bridging Learned Visual Perception and Symbolic Belief-Space Planning](http://arxiv.org/abs/2609.16884v1)
  <details><summary>📄 Abstract</summary>
  In partially observable settings, agents must act without full knowledge of the world state and rely on uncertain state-estimation pipelines. Obtaining grounded and verifiable symbolic plans under such uncertainty remains a key challenge. Recent work has integrated Vision-Language Models (VLMs) to bridge perception and symbolic reasoning, following two main paradigms. The first, VLM-as-planner, maps images directly to action sequences, and the second, VLM-as-grounder, grounds observations into s...
  </details>

- **2026-09-15** — Ting-Wei Chang, Po-Chun Chen, Hen-Hsen Huang et al. — [Smarter by the Moment: Environment-Driven Dynamic Policies for Continual LLM Improvement](http://arxiv.org/abs/2609.16800v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved remarkable progress across diverse domains, but continual adaptation to evolving tasks and environments remains a key challenge. Existing memory-augmented approaches retrieve individual past examples as direct references, but do not explicitly synthesize actionable strategies from them, causing the same types of errors to recur. We propose Dynamic Retrieval-based Policy Generation (DRPG), a framework that integrates memory-based retrieval with a dynamic...
  </details>

- **2026-09-15** — Ruibo Wang, Ziyi Shen, Huaming Wu et al. — [FSANet: Frequency-Spatial Aware Network for Image Segmentation](http://arxiv.org/abs/2609.16773v1)
  <details><summary>📄 Abstract</summary>
  Image segmentation remains challenging due to occlusions, poor lighting, and irregular structures. Although transformer-based methods achieve high accuracy, they rely heavily on long-range spatial features, leading to high computational costs and neglecting prior knowledge or noise patterns, resulting in missing details and unclear boundaries. To address these issues, we propose Frequency Spatial Aware Network (FSANet), which integrates prior knowledge with a dual-domain solver to sequentially a...
  </details>

- **2026-09-15** — Ferran Bohigas-Daranas, Hamid Latif-Martínez, Eduardo Prieto-Araujo et al. — [Unified Heterogeneous Graph Neural Network solver for Power Flow, Optimal Power Flow and State Estimation](http://arxiv.org/abs/2609.16738v1)
  <details><summary>📄 Abstract</summary>
  Power Flow (PF), Optimal Power Flow (OPF), and State Estimation (SE) are fundamental problems in power system analysis, but solving them is computationally expensive. Graph Neural Networks (GNNs) have been proposed as fast surrogates, yet existing solvers are trained for a single problem at a time, producing narrow models that must be rebuilt for each new task.   We propose a more general approach: a single Heterogeneous Residual Gated Graph Convolutional Network that solves all three problems w...
  </details>

- **2026-09-15** — Kazushi Maruo, Ryota Ishii, Yusuke Yamaguchi et al. — [A flexible framework for treatment effect inference in longitudinal clinical studies with skewed outcomes](http://arxiv.org/abs/2609.16670v1)
  <details><summary>📄 Abstract</summary>
  Longitudinal continuous outcomes in clinical trials are commonly analyzed using mixed models for repeated measures (MMRM) under normality assumptions. However, many clinical outcomes are skewed, making mean-based treatment effects difficult to interpret and potentially reducing statistical efficiency. The Box--Cox MMRM (BCMMRM) approach accommodates skewness by enabling inference on model-based median differences via inverse transformation. However, BCMMRM typically assumes a common transformati...
  </details>

- **2026-09-15** — Mathurin Petit, Emir Torun, Louis Brusset et al. — [FlowATC: Aircraft Trajectory Prediction via Flow Matching](http://arxiv.org/abs/2609.16528v1)
  <details><summary>📄 Abstract</summary>
  Building accurate decision-support tools for next-generation air traffic control requires robust trajectory prediction models. We present a flow-matching architecture trained exclusively on historical aircraft trajectories, with no route labels or chart supervision. Trained on 1.15 million Automatic Dependent Surveillance-Broadcast trajectory windows collected over the San Francisco Bay Area, the model generates aircraft trajectory distributions that closely match historical traffic, reproducing...
  </details>

- **2026-09-15** — Bilvin Varughese, Aditya Koneru, Adil Muhammad et al. — [Symbolic Ensemble Learning Enables Discovery of Fast Accurate Physics-Based Interatomic Potentials](http://arxiv.org/abs/2609.16526v1)
  <details><summary>📄 Abstract</summary>
  Machine learning has transformed materials simulation by delivering force fields with ab initio accuracy, yet bridging the gap between high-dimensional regression and physical interpretability remains a grand challenge. Conventional analytical potentials offer transparency but often fail to capture the complexity of far-from-ground state regimes. Here, we introduce a hybrid symbolic-neural framework that unifies the interpretability of the Embedded Atom Method (EAM) with the adaptability of data...
  </details>

- **2026-09-14** — Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas et al. — [BLINDSPOT: A Benchmark for Safety and Refusal Calibration in Long-Horizon Tool-Using Agents](http://arxiv.org/abs/2609.16305v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly operate over long-horizon interactions involving tool use, persistent state, evolving authorization, and external environment feedback. In such settings, safety failures may emerge only after multiple turns, yet existing evaluations often reduce agent behavior to task or attack success, obscuring whether an agent acts, refuses, or remains appropriately calibrated as the interaction evolves. We introduce Blindspot, a benchmark for trajectory-level sa...
  </details>

- **2026-09-14** — Chaofan Wang, Xiaodong Gu, Yuling Shi et al. — [Translator vs. Challenger: Adversarial Agentic Learning for C-to-Rust Translation](http://arxiv.org/abs/2609.15381v1)
  <details><summary>📄 Abstract</summary>
  C-to-Rust translation remains challenging due to the substantial semantic gap between the two languages. Recent experience-enhanced LLM translators improve translation quality by learning reusable insights from prior failures and repairs. Yet learned insights do not automatically constitute reusable translation knowledge: derived from sparse, program-specific traces, they often contain missing conditions, narrow applicability boundaries, or overlooked corner cases. This limits their robustness a...
  </details>

- **2026-09-14** — Sarra Gharsallah, Adele Robaldo, Mariia Tokareva et al. — [Can We Trust the Judges? Validation of Factuality Evaluation Methods via Answer Perturbation](http://arxiv.org/abs/2609.15561v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the factual correctness of large language models (LLMs) is vital for many applications. But are our evaluation tools themselves trustworthy? Despite the rise of factuality-based metrics, their sensitivity and reliability remain underexplored. This paper introduces a meta-evaluation framework that systematically tests these metrics using controlled corruptions of gold standard answers. Our method generates ranked outputs with known degrees of degradation to probe how metrics capture nu...
  </details>

- **2026-09-14** — Lindsay Spoor, Aske Plaat, Thomas Moerland — [Evaluation Metrics for Safe Reinforcement Learning](http://arxiv.org/abs/2609.15315v1)
  <details><summary>📄 Abstract</summary>
  Safe reinforcement learning (RL) is commonly formalized as a Constrained Markov Decision Process (CMDP), in which an agent maximizes expected reward while keeping its expected cumulative cost below a specified safety bound. Existing safe RL benchmarks predominantly report whether an algorithm is safe on average, following this expectation-based guarantee. We argue that this convention is insufficient to reliably characterize an algorithm's true safety: it fails to capture how often and how sever...
  </details>

- **2026-09-14** — Dylan Waldner, Yiannis Kantaros, Guido Governatori et al. — [Legislating World-Model-Based Planning with Legal Reasoning](http://arxiv.org/abs/2609.15113v1)
  <details><summary>📄 Abstract</summary>
  As robotic systems grow more general, legal norms are needed to integrate them into society. This paper extends the isomorphism problem of aligning legal source texts with their encodings, and measures two key challenges to robot normative control: (1) the \textit{grounding isomorphism gap}, where perception error grounds false atoms for legal reasoning, and (2) the \textit{ontological isomorphism gap}, where one legal conclusion admits many faithful translations into planning constraints. The p...
  </details>

- **2026-09-14** — Shwai He, Haichao Zhang, Shen Yan — [Disentangling Representation Evolution in Transformers through Directional Decomposition](http://arxiv.org/abs/2609.15975v1)
  <details><summary>📄 Abstract</summary>
  Transformer representations evolve through learned additive transformations that either preserve their current direction or redirect it. We study this evolution as a functional geometry, decomposing learned updates into parallel and perpendicular components. Across pretrained models, we find substantial parallel components beyond the residual identity path. We then apply the decomposition in two spaces: to attention and MLP updates relative to the hidden state, and to attention value aggregation...
  </details>

- **2026-09-14** — Zhenjie Yang, Yideng Zhang, Dongjie Zhang et al. — [Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands](http://arxiv.org/abs/2609.15726v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing provides contact information that can be difficult to infer from vision alone, but tactile hardware for dexterous hands has not converged to a common design. Dexterous hands differ in finger structure, contact surfaces, and sensor layouts, while simulated tactile signals still differ from measurements produced by physical sensors. These factors make it difficult to study visuo-tactile manipulation across diverse dexterous hands within a consistent experimental setting. We present...
  </details>

- **2026-09-14** — Tahir Cetin Akinci — [Multiscale Visibility Theory: A Task-Relative Operator-Geometric Framework for Observation, Robustness, and Detectability](http://arxiv.org/abs/2609.15948v1)
  <details><summary>📄 Abstract</summary>
  Multiscale Visibility Theory (MVT) is introduced as a task-relative operator-geometric framework for determining how prescribed information survives and remains accessible through a structured observation architecture. Rather than evaluating observation quality by transform magnitude, output energy, rank, or signal prominence alone, MVT measures the accessibility of a specified task direction or task subspace through the row space of the composite operator A_A = R_E W_rho H_beta P_Omega. Unlike ...
  </details>

- **2026-09-14** — Amir Globerson, Amy Keeling, Anisha Choudhury et al. — [Towards Scalable Measurement of Durable Skills](http://arxiv.org/abs/2609.15864v1)
  <details><summary>📄 Abstract</summary>
  Durable skills, such as collaboration, creativity and critical thinking, are instrumental to success in the modern workforce. Yet, measuring these skills remains a persistent challenge. Moreover, because what is not measured is often not taught, these skills are often overlooked in mainstream educational curricula. Designing effective assessments for these skills necessitates balancing two often-conflicting requirements: ecological validity and psychometric rigor. On the one hand, the assessment...
  </details>

- **2026-09-14** — Yucheng Shen, Lingyong Yan, Jiulong Wu et al. — [Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation](http://arxiv.org/abs/2609.15800v1)
  <details><summary>📄 Abstract</summary>
  Visual Retrieval-Augmented Generation (VRAG) empowers models to navigate and answer queries about visually rich documents by retrieving relevant page images as visual evidence and reasoning over their content. However, effectively utilizing this visual evidence is usually impeded by two main challenges. First, answer-relevant evidence is sparse and may be concentrated in a small region of one page or dispersed across multiple pages. Second, existing agentic methods often generate answers based o...
  </details>

- **2026-09-14** — Hansong Ma, Junxiao Wang — [EEG-Xplain: Decoding Neural Black-Boxes of EEG Foundation Models](http://arxiv.org/abs/2609.15687v1)
  <details><summary>📄 Abstract</summary>
  EEG foundation models such as BIOT, LaBraM, and EEGMamba have achieved remarkable performance in neural signal decoding, but their black-box nature limits clinical trust and neuroscientific validation. We propose a unified attribution framework for interpreting EEG foundation models across heterogeneous architectures. The framework integrates gradient-, perturbation-, and activation-based explanation methods to analyze model behavior in spatial, temporal, and frequency dimensions. Spatially, it ...
  </details>

- **2026-09-14** — Yongsheng Chen, Shuo Lu, Wei Guo et al. — [Physics-Guided Conditional Flow Matching with Energy Regularization for Robust PDE Inverse Problems](http://arxiv.org/abs/2609.15536v1)
  <details><summary>📄 Abstract</summary>
  We consider partial differential equation (PDE) inverse problems from sparse, noisy, and corrupted observations, with the aim of recovering unknown coefficient fields and associated state variables in a mesh-free setting. Under such sparse and corrupted observations, standard physics-informed and generative approaches typically treat all samples indiscriminately and therefore lack a principled mechanism for reconciling physical laws with contaminated data. We address this difficulty with a two-s...
  </details>

- **2026-09-14** — Rafael Pina, Varuna De Silva, Corentin Artaud — [Robust and Efficient Communication for Multi-Agent Learning](http://arxiv.org/abs/2609.15361v1)
  <details><summary>📄 Abstract</summary>
  Effective communication is a cornerstone of distributed intelligence in Multi-Agent Reinforcement Learning (MARL), yet ensuring that generated messages are both informative and robust to physical constraints remains a significant challenge. This paper introduces Multi-Agent Regularized Communication (MARC), a novel framework inspired by information-theoretic principles of conditional mutual information. MARC employs an attention-based architecture coupled with a unique message regularization mec...
  </details>

- **2026-09-14** — Marta Marszewska, Justyna Signerska, Paweł Dłotko — [Topological Characteristics for the Analysis of Vector Fields. New stable characteristics for discrete and continuous dynamical systems](http://arxiv.org/abs/2609.15260v1)
  <details><summary>📄 Abstract</summary>
  The qualitative analysis of nonlinear dynamical systems relies on identifying geometric and topological structures that govern phase-space organization. We develop a computational framework based on novel topological and geometric descriptors of vector fields that enables robust comparison of dynamical regimes from both analytical models and sampled data. The framework comprises the Begin-End Point Embedding (BEPE), Density of Directions (DOD) and Euler characteristic-based summaries (Euler Char...
  </details>

- **2026-09-14** — Qingtao Xia, Jiahua Bao, Siyao Cheng et al. — [Pre-PEFT Probing: Weight Statistics and Perturbation Robustness for Layer Selection in VLM Vision Encoders](http://arxiv.org/abs/2609.15229v1)
  <details><summary>📄 Abstract</summary>
  We propose a pre-fine-tuning probing method for Parameter-Efficient Fine-Tuning (PEFT) layer selection, aiming to obtain more stable and higher gains with fewer trainable parameters when adapting large vision--language models (VLMs). Unlike the common practice of applying LoRA and other adapters to all layers at once---where layer selection often relies on heuristic rules---we focus on the vision encoder and directly evaluate the "adaptability'' of each Transformer layer. Specifically, we charac...
  </details>

- **2026-09-14** — Tin Mišić, Takato Horii — [Sensory Precision Inference for Multimodal Arbitration under Uncertainty](http://arxiv.org/abs/2609.15065v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents operating on multisensory data cannot assume that all sensory modalities remain consistently informative. In real environments, sensory streams are frequently corrupted by noise, missing data, or inter-modal incongruence, requiring adaptive arbitration between competing sensory hypotheses. While active inference provides a principled framework for uncertainty-guided inference, the role of dynamically inferred sensory precision in generative multimodal arbitration under sensory ...
  </details>

- **2026-09-14** — Sidi Chang, Peiying Zhu — [Four Ledgers, Not One Score: Responsible Communication of LLM-Judge Calibration in Biomedical ML](http://arxiv.org/abs/2609.15015v1)
  <details><summary>📄 Abstract</summary>
  Synthetic perturbations appear to offer inexpensive calibration data for LLM evaluators in biomedical ML, where expert review is scarce. Yet a planted mutation key is neither a detector output nor automatically human ground truth. We formalize four distinct ledgers: planted perturbations, independent detector outputs, source-linked human dispositions, and human-added discoveries. We then audit the evaluation design, scoring code, read paths, and current human records of a private synthetic Japan...
  </details>

- **2026-09-14** — Chengxin Yu, Zhaoxin Fan, Faguo Wu et al. — [CoMem: Collective-Individual Memory Synergy for Evolutionary Multi-Agent Systems](http://arxiv.org/abs/2609.15009v1)
  <details><summary>📄 Abstract</summary>
  Designing effective memory mechanisms is crucial for advancing LLM-driven Multi-Agent Systems (MAS), helping agents learn together and perform better over time. While recent work has led to strong cooperation skills, most methods still use flat, unstructured memories, which easily get filled with noise and erase differences between agents. To address this, we introduce the concept of collective-individual memory synergy and propose CoMem, an architecture that unifies both private experience and ...
  </details>

- **2026-09-14** — Alef Iury Siqueira Ferreira, Pedro Lustosa Rege Botelho, Fernanda Silva et al. — [CAL-MOS: Bridging Layers with Adapters for Robust MOS Prediction Across Speech Foundation Models](http://arxiv.org/abs/2609.14956v1)
  <details><summary>📄 Abstract</summary>
  Speech Quality Assessment (SQA) is essential for modern speech technologies, and recent non-intrusive SQA predictors increasingly rely on Speech Foundation Models (SFMs). However, because SFMs expose representations from many layers, it remains unclear which depths are most informative for MOS prediction and how multi-layer information should be combined reliably across backbones and datasets. We benchmark ten SFMs on four MOS datasets under three regimes: full fine-tuning, last-layer probing wi...
  </details>

- **2026-09-14** — Wonje Heo, Shinee Youn, Yooshin Kim et al. — [Tracing the Origins: Legacy Codec Identification in Neural Audio Transcoding](http://arxiv.org/abs/2609.14916v1)
  <details><summary>📄 Abstract</summary>
  Residual Vector Quantization (RVQ)-based neural audio codecs (NACs) enable high-fidelity audio distribution at unprecedentedly low bitrates through discrete token-based representations. However, this shift disrupts traditional forensics, as non-linear neural transcoding obscures the underlying traces of legacy compression. This study defines the forensic gap and proposes a Transformer-based framework designed to leverage the hierarchical and temporal dependencies inherent in RVQ sequences. By mo...
  </details>

- **2026-09-14** — Evgeny S. Saveliev, Krzysztof Kacprzyk, Charlotte Capitanchik et al. — [SeqMaestro: From nucleotide sequences to biological hypotheses through interpretable machine learning](http://arxiv.org/abs/2609.14882v1)
  <details><summary>📄 Abstract</summary>
  Nucleotide sequence analysis is central to problems spanning regulatory genomics, evolutionary biology, and phenotype prediction. Classical bioinformatics methods extract interpretable sequence properties such as motifs and k-mer composition, but their flexibility is limited. In contrast, modern deep learning models can learn powerful predictive representations directly from raw sequences, yet their internal representations and decision mechanisms are difficult to inspect. Interpretable machine ...
  </details>

- **2026-09-13** — Norbert Oswald, Fabian Deuser, Thomas Bräunl — [Managing Action Preconditions in Neuro-Symbolic RL: Three Placement Strategies for Embodied Agents](http://arxiv.org/abs/2609.16056v1)
  <details><summary>📄 Abstract</summary>
  Humans carry behaviour knowledge of how to act in familiar situations into every new task rather than relearning it from scratch. There is no reason a Reinforcement Learning (RL) agent shouldn't do the same: known behaviour patterns need not be learned, only applied. Neuro-symbolic RL bridges prior knowledge and RL by injecting symbolic knowledge alongside a learned policy. The point at which this knowledge is integrated is critical: a poor choice can produce, for instance, hallucinated precondi...
  </details>

- **2026-09-13** — Alireza Parchami, Artin Saberpour, Robin Connor Schramm et al. — [Speak to the City: Multimodal Resolution for Outside-the-Vehicle References](http://arxiv.org/abs/2609.14691v1)
  <details><summary>📄 Abstract</summary>
  As autonomous vehicles and Extended Reality (XR) headsets enable novel in-car interactions, seamlessly querying physical landmarks, known as Outside-the-Vehicle Referencing (OVR), remains challenging due to ego-motion and referential ambiguity. We present a robust, multimodal OVR framework fusing user gaze and natural language to identify Points of Interest (POIs). To address the scarcity of dynamic vehicular data, we developed a VR-based pipeline synchronizing 360-degree transit videos with veh...
  </details>

- **2026-09-13** — Tobias Labarta, Frederik Pahde, Novak Boskov et al. — [Safety Signals to Verify NetOps Agents with Action-Level Granularity](http://arxiv.org/abs/2609.14422v1)
  <details><summary>📄 Abstract</summary>
  Agentic Network Operations (NetOps) are an emerging paradigm promising to enable workload-aware, self-adjustable, and reliable autonomous networks. While agents have proven their value in incident summarization and telemetry signal extraction, their effectiveness as autonomous control-loop engines heavily relies on their long-horizon reliability. One such setting is the datacenter fabric, where an agent must respond to alarms and operator intents while abstaining from high-risk actions that may ...
  </details>

- **2026-09-13** — Zhiling Chen, Jingzhan Ge, Ruimin Chen et al. — [Task-Specified Active Metrological Inspection with Measurement-Steered VLA Manipulation and Deterministic Evidence Gating](http://arxiv.org/abs/2609.14219v1)
  <details><summary>📄 Abstract</summary>
  High-mix low-volume (HMLV) manufacturing requires inspection systems to adapt to changing parts, specifications, and work orders without repeated task-specific programming. Existing inspection automation typically assumes predefined sensing sequences, while general purpose robot agents optimize task completion rather than the completeness and validity of metrological evidence. We formulate task-specified active metrological inspection and propose From Requirements to Admissible Metrological Evid...
  </details>

- **2026-09-13** — Constantinos Papantoniou, Brian Hilton — [ANASSA: An Agentic AI Orchestration Framework for Spatial Intelligence](http://arxiv.org/abs/2609.14824v1)
  <details><summary>📄 Abstract</summary>
  The emergence of large language models (LLMs) and large multimodal models (LMMs) has enabled a new class of agentic systems capable of integrating natural language understanding with tool-based execution. In geographic information systems (GIS), this shift is transforming traditional, expert-driven workflows into semiautonomous systems that can interpret user intent, construct spatial workflows, and execute geospatial analysis tasks. However, existing approaches remain limited by fragmented inte...
  </details>

- **2026-09-13** — Ji Lu, Lifei Liu, Haoran Yu et al. — [MedTRACE: Tool-Augmented Multimodal Clinical Reasoning Agents for Evidence-Grounded Decision-Making](http://arxiv.org/abs/2609.14823v1)
  <details><summary>📄 Abstract</summary>
  Multimodal clinical decision-making requires reliable reasoning over heterogeneous evidence from electronic health records, medical images, and physiological signals. Existing models typically map these inputs directly to diagnoses without explicitly assessing evidence sufficiency, tool-use requirements, or diagnostic uncertainty. This paper presents MedTRACE, a tool-augmented multimodal clinical reasoning agent for evidence-grounded decision-making. MedTRACE uses modality-specific encoders to c...
  </details>

- **2026-09-13** — Ji Lu, Huiran Duan, Bo Zhao et al. — [Decision-Oriented Uncertainty Quantification for Risk Control in Earth System Spatiotemporal Foundation Models](http://arxiv.org/abs/2609.14821v1)
  <details><summary>📄 Abstract</summary>
  Earth system modeling is shifting from task-specific predictors toward foundation models with general spatiotemporal representation capabilities. Although these models can jointly encode dynamic Earth fields, external forcings, and static geographic context for multistep forecasting, accurate point predictions or statistically calibrated intervals alone are insufficient for high-impact applications such as extremeweather warning, flood control, renewable-energy dispatch, and emergency resource a...
  </details>

- **2026-09-13** — Andre Panossian — [Transformed in Translation: Two-Stage Structural Uncertainty in LLM-Based Scientific Autoformalization](http://arxiv.org/abs/2609.14808v1)
  <details><summary>📄 Abstract</summary>
  Scientific autoformalization turns verbal accounts into executable mathematics, but executable code does not settle which model has been constructed. We examine two sources of structural uncertainty: the formalizer that generates a response law, and the recurrence that turns that law into trajectories. In secondary analyses of an openly archived crossed experiment, we studied 320 response maps generated by two pinned language-model formalizers from five engineered cognitive accounts within one s...
  </details>

- **2026-09-13** — Aashish Bohra, Vivek Vijay — [WaVeFuse: Regime-Adaptive Equity Index Forecasting via Channel-Wise Wavelet Denoising and Vertical Attention Fusion](http://arxiv.org/abs/2609.14733v1)
  <details><summary>📄 Abstract</summary>
  Hybrid Deep Learning for equity index forecasting is limited by three problems: propagation of OHLCV noise into derived technical indicators (TIs), channel-indiscriminate multi-scale decomposition that conflates heterogeneous frequency signatures, and static multi-branch fusion that cannot adapt to market regime shifts. WaVeFuse addresses these limitations through a unified dual-branch architecture. Symlet-4 wavelet denoising (level 2, MAD soft threshold) suppresses microstructure noise in OHLCV...
  </details>

- **2026-09-13** — Zhibin Jiao, Xiangjing An — [SH-WRNN: Implicit Spherical Harmonics Weight Field Routing Neural Networks for Asymmetric Edge Intelligence](http://arxiv.org/abs/2609.14614v1)
  <details><summary>📄 Abstract</summary>
  Deep learning architectures remain rigidly built upon traditional fully connected layers. While networks scale up, few challenge this foundational root. In this work, we reshape this paradigm by transforming the core synapse weight matrix from static, discrete parameters into a differentiable, continuous field governed by spherical harmonics functions. We introduce the Implicit Spherical Harmonics Weight Field Routing Neural Network (SH-WRNN), which constrains weight matrices within a continuous...
  </details>

- **2026-09-13** — Eduin E. Hernandez, Luis F. Garcia, Nurassyl Askar et al. — [Theseus in the Graph: Towards Traceable Multi-Hop Graph Navigation](http://arxiv.org/abs/2609.14528v1)
  <details><summary>📄 Abstract</summary>
  Multi-Hop Knowledge Graph Question Answering (KGQA) tasks require models to assemble relational evidence along paths in a KG to answer natural-language questions. However, existing KGQA systems typically focus on predicting the final answer without explicitly modeling or validating the intermediate reasoning steps, obscuring whether the correct answers arise from faithful multi-hop reasoning. To address this limitation, we re-frame multi-hop KGQA as a question-conditioned graph navigation proble...
  </details>

- **2026-09-13** — Bhargav Lad, Yifan Hao — [Retrieval-Guided Fine-Tuning as Noisy Estimation: Risk bounds and Architectural Analysis](http://arxiv.org/abs/2609.14485v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Guided Fine-Tuning (RAG-FT) incorporates retrieved data directly into the training objective, but the statistical consequences of noisy retrieval during training remain theoretically undercharacterized. We study this question by modeling RAG-FT as an estimation problem in a multi-task linear regression framework, using an OLS proxy for single-layer linear self-attention to obtain finite-sample risk bounds. Under homoscedastic retrieval noise, we show that retrieval failure decays expon...
  </details>

- **2026-09-13** — Zhixuan Chen, Jialiang Lu, Zhong Ye et al. — [PRI-Net: A Lightweight Multimodal Framework for 3D UAV Localization](http://arxiv.org/abs/2609.14469v1)
  <details><summary>📄 Abstract</summary>
  Accurate 3D localization of unmanned aerial vehicles (UAVs) remains challenging for existing multimodal approaches due to sparse LiDAR geometry, modality-imbalanced fusion, and redundant feature transmission over constrained edge-to-server links. To address these limitations, we propose PRI-Net, an efficient and lightweight multimodal fusion framework for UAV localization that integrates point cloud splatting, residual attention fusion, and an information bottleneck. Specifically, a 3D point clo...
  </details>

- **2026-09-13** — Kazutoshi Sasahara, Aoi Naito, Ryo Fujie — [A latent dimension of Condorcet's jury theorem for multiple AI advisers](http://arxiv.org/abs/2609.14438v1)
  <details><summary>📄 Abstract</summary>
  When the same question is asked of multiple AI advisers, as in self-consistency and LLM-as-a-judge panels, Condorcet's jury theorem predicts that adding independent, competent advisers makes the majority more reliable. The theorem, however, has a latent dimension when viewed from the user's vantage: adding advisers also makes disagreement more visible. A binomial model reveals that this ``visible dissent'' becomes nearly inevitable as the number of advisers grows, and that reliability and disagr...
  </details>

- **2026-09-13** — Haoran Zhang, Zian Mao, Shufen Chu et al. — [Multi4D: an end-to-end neural network for structural determination at complex material interfaces](http://arxiv.org/abs/2609.14348v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous interfaces dictate the performance and degradation of functional materials, making it essential to link local structural variations with macroscopic failure mechanisms to guide future materials design. Yet structural heterogeneity, phase overlap, and local disorder produce highly convoluted diffraction signatures, making extended transition regions difficult to interpret at atomic resolution across large fields of view. Here, we introduce Multi4D, a physics-informed neural network ...
  </details>

- **2026-09-13** — Ziyu Zhang, Yun Chen, Taihui Wang et al. — [Modeling, Scaling, and Decoding: Optimizing Controllable Speech Generation with Nonverbal Vocalizations](http://arxiv.org/abs/2609.14231v1)
  <details><summary>📄 Abstract</summary>
  Controllable synthesis of nonverbal vocalizations (NVVs) is es- sential for natural and expressive speech, but remains challeng- ing due to their acoustic diversity and imbalanced distribution in existing corpora. To address these challenges, we develop an NVV-aware DiTAR system that models continuous speech latents, encodes the 16 target NVV categories as dedicated to- kens, and adapts stop prediction to distinguish mid-utterance vocalizations from utterance boundaries. Training begins with lar...
  </details>

- **2026-09-12** — Metin Alp Dogan, Edward Sun, Feng Xu et al. — [Visible Touch: Rendering Contact for Visuomotor Policies](http://arxiv.org/abs/2609.14156v1)
  <details><summary>📄 Abstract</summary>
  Integrating contact information into visuomotor policies remains an open problem. Touch is essential to robust manipulation, yet most modern policies, including pretrained vision-language-action (VLA) models, operate from vision and proprioception alone. Existing approaches to closing this gap require specialized tactile hardware, add separate tactile encoders, or commit to non-image policy backbones, all incompatible with the modern paradigm of image-conditioned policies built on pretrained 2D ...
  </details>

- **2026-09-12** — Qiyang Sun, Langqing Zhang, Yupei Li et al. — [A New Transformer-Based Approach for Audio-Based Kinship Verification and a New Uncontrolled Mandarin Kinship Speech Dataset](http://arxiv.org/abs/2609.14145v1)
  <details><summary>📄 Abstract</summary>
  Kinship verification is a task involving determining whether two individuals share a first-order kin relation. To tackle this task, we propose CONVTRAP-TN, a new architecture for audio-based kinship verification, and conduct an ablation study on the proposed model. To the best of our knowledge, we are the first to apply the successful transformer architecture to the task of audio-based kinship verification. Furthermore, we also collect a custom speech dataset, ARKIN, which accurately reflects ev...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 16 papers

- **2026-09-15** — Fengshuo Liu, Ying Liu, Ruize Sun et al. — [Coding Agents Have Converged: Why the SWE-bench Leaderboard Can No Longer Order Its Top Entries, and What to Measure Instead](http://arxiv.org/abs/2609.17394v1)
  <details><summary>📄 Abstract</summary>
  Small differences on coding-agent leaderboards are often read as an ordering of systems. We audit whether the published verdicts support this reading, using 254 SWE-bench submissions across four splits without running models. On Verified, the leading two entries each resolve 396 of 500 instances. The top ten share 285 successes and 51 failures, leaving 164 instances that distinguish their outcomes. Frontier solution sets have median nesting 0.935 against a score-implied baseline of 0.774, indica...
  </details>

- **2026-09-15** — Jim Berend, Reduan Achtibat, Daniel Schäffer et al. — [ResLRP: The Role of Residual Cancellation in Attribution Instability in Vision Transformers](http://arxiv.org/abs/2609.17152v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) are central to most modern vision models, yet obtaining input attributions that are fine-grained, faithful, and stable remains challenging. Layer-wise Relevance Propagation (LRP) has been adapted to transformer attention, but in ViTs it often produces noisy, unfaithful explanations. We show that the missing ingredient is the treatment of residual connections: cancellation effects in residual pathways lead to attribution explosion. Moreover, we find that these cancellat...
  </details>

- **2026-09-15** — Weiming Li, Ana Catarina Fidalgo Barata, Miguel Constante et al. — [DiaWhisper-DPO: Role-Attributed Transcription of Clinical Interviews via Failure-Mined Preference Optimization](http://arxiv.org/abs/2609.16661v1)
  <details><summary>📄 Abstract</summary>
  Automated depression screening from clinical interviews requires attribution of utterances to the clinician or patient. We evaluate two datasets: DAIC-WOZ, where participant-only recordings require re-synthesizing both sides for controlled two-party evaluation, and PDCH-HAMD, comprising voice-converted real Chinese interviews for cross-lingual validation. Cascaded systems combine speaker diarization with role-assignment heuristics, so errors can propagate across stages. We propose an end-to-end ...
  </details>

- **2026-09-15** — Yao Zhao, Aditya Shanmugham, Swastik Roy et al. — [EchoPath: Execution-Level Replayable Memory for GUI Agents](http://arxiv.org/abs/2609.16635v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents increasingly operate browsers, software, and desktop applications via CLI or API portals, but graphical user interface (GUI) still plays an important role in common industrial production scenarios. GUI agents commonly employ fresh observe-plan-ground-act loops, which is inefficient for enterprise tasks that repeatedly update records, process forms, configure tools, and export reports. We introduce EchoPath, a model-agnostic harness that converts artifact-validated GUI traject...
  </details>

- **2026-09-15** — Paul Denny, Gweneth Barbre, Musa Blake et al. — [Testing Our Foundations: Citation Trends, Errors, and Emerging Hallucinations in the Computing Education Literature](http://arxiv.org/abs/2609.16574v1)
  <details><summary>📄 Abstract</summary>
  Accurate references are foundational to scholarly work, enabling verification, attribution, and systematic review. However, the rapid adoption of large language models has introduced a serious integrity concern: plausible-looking but fabricated citations. Although hallucinated references are widely discussed, their visibility within specific research communities remains unclear. We address this gap by examining reference integrity at key computing education venues using ACM Digital Library data....
  </details>

- **2026-09-14** — Hyojung Han — [Where Post-Training Quantization Breaks Text Embedders: A Measured Map Across Four Embedder Families](http://arxiv.org/abs/2609.16391v1)
  <details><summary>📄 Abstract</summary>
  Weight-only post-training quantization is the cheapest way to shrink a retrieval embedder, and the received advice for applying it -- protect the embedding table, allocate bits by module sensitivity, prefer a ranking-aware objective over weight reconstruction -- was carried into LLM quantization largely intact. We test that advice on retrieval embedders directly, quantizing five checkpoints from four architecture families across a grid of bit widths and group sizes, and isolating the embedding, ...
  </details>

- **2026-09-14** — Shuai Wang, Yize Zhao, Qingyu Chen — [CLEAR: Cross-Source Evidence Adjudication for Large Language Models in Medicine](http://arxiv.org/abs/2609.16301v1)
  <details><summary>📄 Abstract</summary>
  Medical knowledge evolves continuously, whereas the parametric knowledge encoded in large language models (LLMs) is fixed at training time. External retrieval, including retrieval-augmented generation (RAG), can provide access to newly available evidence, but retrieved information may be irrelevant, incomplete, or conflicting. As a result, external retrieval can in turn degrade the factual accuracy and evidence grounding of LLM outputs. To address this challenge, we propose \textbf{CLEAR}, an ag...
  </details>

- **2026-09-14** — Zvi Kons, Avihu Dekel, Hagai Aronowitz et al. — [Word Timestamps and Speaker Attribution with a Non-Autoregressive LLM](http://arxiv.org/abs/2609.15218v1)
  <details><summary>📄 Abstract</summary>
  Timestamps and speaker attribution are useful additions to speech recognition, creating a rich text transcript. This information can either be extracted during transcription or aligned to a given transcript. In this paper we present models that add timestamps and speaker information to a given transcript using a non-autoregressive LLM-based architecture. Compared to an autoregressive model built from similar components, the models are more accurate and annotate a given transcript one to two orde...
  </details>

- **2026-09-14** — Meiduo Chong, Shaolei Zhang, Ju Fan et al. — [EvoOntology: A Self-Evolving Ontology Layer for Data Agents](http://arxiv.org/abs/2609.15779v1)
  <details><summary>📄 Abstract</summary>
  Data agents aim to fulfill natural-language instructions over heterogeneous data, including tables, files, and databases. However, data agents face a challenging agent-data gap: heterogeneous data resides outside the agent, while the agent can access it (e.g., column names and file paths) only through generic tools. Existing approaches either let agents directly explore raw data sources or inject manually constructed semantic layers into prompts. However, neither scales well to large heterogeneo...
  </details>

- **2026-09-14** — Mengyi Deng, Xin Li, Duyi Pan et al. — [RESKILL: Explicit Failure Attribution and Structured Repair for Interactive Language Agents](http://arxiv.org/abs/2609.15684v1)
  <details><summary>📄 Abstract</summary>
  Language agents increasingly rely on reusable skills, but post-failure repair is often handled by opaque one-shot reflection: a model generates a skill patch without explicitly maintaining how failure explanations relate to candidate repairs or how unsuccessful retests should influence later edits. We introduce RESKILL, a structured repair framework that maintains an explicit repair state across repair rounds. Given a failed rollout, the framework links failure hypotheses to candidate skill patc...
  </details>

- **2026-09-14** — Lei Qu — [From Ideas to Actions: A Public-Data Decision-Support Toolchain Across the Venture Lifecycle](http://arxiv.org/abs/2609.15219v1)
  <details><summary>📄 Abstract</summary>
  Founders face two linked decisions: whether to pursue an idea before founding, and which operating actions and capital partners fit afterward. We present a public-data decision-support toolchain combining time-bounded proposal profiling, market and moat checks, and deterministic aggregation with auditable investor-company event chains for retrospective analysis. Pre-founding: (a) After threshold selection on 198 development companies, the frozen pipeline achieves F0.5=0.5357 [0.412, 0.655] on an...
  </details>

- **2026-09-13** — Genliang Zhu — [AcquireBound: Runtime Authorization for Resources Acquired by AI Agents](http://arxiv.org/abs/2609.14744v1)
  <details><summary>📄 Abstract</summary>
  By acquiring compute, credentials, accounts, services, and other agents, autonomous AI agents can introduce new authority into a task. Payment, budget, OAuth, mandate, and fulfillment checks can validate transaction conditions without deciding whether a returned resource may become usable authority. This post-fulfillment activation gap spans tool-mediated creation, inter-agent delegation, and agentic commerce. We present AcquireBound, a provenance-bounded runtime authorization architecture. It q...
  </details>

- **2026-09-13** — Tsz Wai Ko, Jiaru Bai, Thomas Swanick et al. — [El Agente Potente: High-Throughput Agentic Atomistic Simulations](http://arxiv.org/abs/2609.14840v1)
  <details><summary>📄 Abstract</summary>
  Foundational machine-learning interatomic potentials (MLIPs) are transforming atomistic simulations by achieving near-ab initio accuracy across large chemical spaces at a fraction of the computational cost. A central challenge in using these tools for high-throughput property calculations is translating high-level scientific intent into adaptive simulation campaigns without compromising workflow rigour. We introduce El Agente Potente, an agentic system that combines typed execution graphs with a...
  </details>

- **2026-09-13** — Orion Reblitz-Richardson — [Calibrating Interpretability Instruments Before Trusting Their Verdicts](http://arxiv.org/abs/2609.14754v1)
  <details><summary>📄 Abstract</summary>
  Causal claims about large language model (LLM) internals rest on measurements. Those might include a projection, a cosine, an ablation delta, or an interchange patch among others. These measurements fail in specific, diagnosable ways that return a plausible number instead of an error, so a broken instrument can easily read as a finding. A covariance-matched null can saturate until every direction looks typical, a per-head attribution can overshoot the true residual write threefold on reordered-n...
  </details>

- **2026-09-13** — Dmitry Kuklev — [A Building as a Repository: KIR, a Typed Intermediate Representation for Agent-Authored Building Information Models](http://arxiv.org/abs/2609.14578v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents that author building information models need more than access to a host API. They need a representation of what they intended, what a compiler decided on their behalf, what was refused, what was observed after execution and what remains unknown. We present KIR, a typed intermediate representation in which a building is authored as a program held in a versioned repository and lowered to host applications as build targets. KIR is organised around seven ways in which a generator w...
  </details>

- **2026-09-13** — Yee Man Choi, Xuehang Guo, Songcheng Cai et al. — [ATTRICITE: Training an Open 4B Model for Citation Recovery toward Faithful Attribution](http://arxiv.org/abs/2609.14248v1)
  <details><summary>📄 Abstract</summary>
  Faithful citation attribution begins with identifying the intended source for a scientific claim. We study this source-identification capability through citation recovery: recovering the paper cited by the original author from a citation-bearing passage. Our evaluation adopts the published author's citation as an observable human attribution signal and uses target recovery as a proxy for progress toward faithful attribution. We introduce ATTRICITE, an open 4B-parameter model trained for tool-usi...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 7 papers

- **2026-09-15** — Haiping Du, Linping Chan — [Large Language Models in the Loop: A Stability- and Network-Aware Survey in Networked Control, Cyber-Physical, and Multi-Agent Systems](http://arxiv.org/abs/2609.16599v1)
  <details><summary>📄 Abstract</summary>
  Modern networked control systems (NCSs), cyber-physical systems (CPSs), and complex multi-agent network systems (CNSs) increasingly rely on large language models (LLMs) for high-level decision-making. However, the slow, stochastic nature of LLMs directly conflicts with the strict stability and safety guarantees required by these physical systems. This survey presents a unified analysis of how LLMs can be admitted into the control loop of NCS, CPS, and CNS without compromising closed-loop guarant...
  </details>

- **2026-09-15** — Nanjie Yao, Hao Wang, Chong Cheng et al. — [World Models for Embodied Intelligence: From Plausible to Controllable to Actionable](http://arxiv.org/abs/2609.16697v1)
  <details><summary>📄 Abstract</summary>
  World models connect perception and decision-making in embodied intelligence by maintaining hidden state, anticipating consequences, comparing interventions, and adapting when execution departs from expectations. Although progress is often measured by visual fidelity, their value lies in improving behavior. Before reaching for a cup, a person anticipates its weight and resistance to grasping, shaping the hand before contact. Such anticipation is coarse and rarely pictorial, yet it guides action....
  </details>

- **2026-09-15** — Qizhou Wang, Bogdan Mamaev, Christopher Leckie — [Towards Detecting AI-Assisted Responses in Online Surveys](http://arxiv.org/abs/2609.17317v1)
  <details><summary>📄 Abstract</summary>
  The use of LLMs to complete online surveys impacts the validity of survey-based research, but detecting such usage remains underexplored. We introduce an initial benchmark dataset, namely ASURRE, for AI-assisted survey participation to capture usage strategies ranging from full generation and revision to persona-grounded agentic completion. Controlled by these strategies, LLM-assisted survey responses are generated using multiple LLMs on three real-world surveys in different disciplines, paired ...
  </details>

- **2026-09-15** — Kirill Skobelev, Eric Fithian, X. Y. Han — [Fine-Tuning Fixes Mode Collapse and Over-Dispersion in LLMs](http://arxiv.org/abs/2609.16454v1)
  <details><summary>📄 Abstract</summary>
  Recent work by Doshi and Hauser (2024), Bisbee et al. (2024), and Xie et al. (2026) raises concerns that outputs from large language models (LLMs) tend to be under-diverse: they repeat or resemble one another more often than responses from the population they are meant to represent, a phenomenon known as mode collapse. In this work, we show that whether mode-collapse, or its opposite, occurs depends on the specific model and dataset used. Further, with sufficient supervised fine-tuning (SFT) dat...
  </details>

- **2026-09-14** — Steven Ndung'u, Adel Daoud, Ismael Yacoubou Djima et al. — [Transfer Learning for Socioeconomic Estimation in Forced-Displacement Settings](http://arxiv.org/abs/2609.15773v1)
  <details><summary>📄 Abstract</summary>
  Progress in inclusive household surveys has strengthened socioeconomic evidence for forcibly displaced populations, providing indispensable benchmarks on living conditions and welfare. However, these surveys remain resource-intensive and periodic, while conditions can change between rounds, particularly in settings affected by fragility, conflict, and violence. More frequently updated, spatially granular complementary evidence is therefore needed to identify where socioeconomic conditions may be...
  </details>

- **2026-09-13** — Jakub Growiec, Klaus Prettner, Maciej Szkróbka — [Redistributive Policies for the Times of Transformative AI](http://arxiv.org/abs/2609.14750v1)
  <details><summary>📄 Abstract</summary>
  After the arrival of transformative artificial intelligence (TAI), broad-based automation is expected to decrease the labor share and increase income and wealth inequality. Although economic growth is likely to accelerate, most of its gains may accrue to a narrow group of individuals and firms. Hence, if unmitigated by redistributive policy, income and wealth inequality may rise to levels unseen in the industrial economy. Using a unifying theoretical framework, we survey the redistributive polic...
  </details>

- **2026-09-13** — Soobin Cho, Deveshi Modi, Divya Mavinkurve et al. — [Assessing the Applicability of Existing Design Recommendations to AI Companion Design: A Multi-Method Study](http://arxiv.org/abs/2609.14236v1)
  <details><summary>📄 Abstract</summary>
  With the rapid proliferation of large language model (LLM)-based systems, AI companions have emerged as conversational agents designed to cultivate emotional connection rather than primarily to support humans in instrumental tasks. Because engagement with AI companions involves relational, emotional, and potentially long-term interactions, their design is consequential. Prior work has offered guidance for designing trustworthy and relational AI systems and has begun to examine design for AI comp...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 166 papers

- **2026-09-15** — Ziheng Ren, Qian Gao, Jun Fan et al. — [Semantic-Spatial Agreement Verification for Mitigating Object Hallucination in Multimodal Large Language Models](http://arxiv.org/abs/2609.17269v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models generate natural-language responses from visual inputs, yet may mention objects absent from an image. In medication assistance, accessible perception, and environmental decision-making, such hallucinations can create real-world safety risks. We propose Semantic-Spatial Agreement Verification (SSAV), a training-free method for verifying object claims. A visually grounded claim should remain stable across semantically equivalent queries and repeatedly localize to t...
  </details>

- **2026-09-15** — Amir Taubenfeld, Zorik Gekhman, Avigail Grinstein-Dabush et al. — [Verifiable Social Reasoning for LLM Assistants](http://arxiv.org/abs/2609.17496v1)
  <details><summary>📄 Abstract</summary>
  LLM assistants are widely used for daily social advice, yet evaluating their social reasoning in such consultation settings remains challenging since (i) it requires setups where the assistant learns about social situations from subjective user narratives, and (ii) social properties, such as others' intentions, typically lack verifiable ground truth. To address these challenges, we introduce Fuse, a multi-agent simulation framework for studying user-mediated social reasoning. In Fuse, a target a...
  </details>

- **2026-09-15** — Gjergj Plepi, Sven Behnke — [SlotDiT: Object-Centric Representations for Diffusion Transformers](http://arxiv.org/abs/2609.17414v1)
  <details><summary>📄 Abstract</summary>
  Text-conditioned latent diffusion models perform strongly in video generation and are promising backbones for robotic applications. However, existing approaches rely on pixel-level or VAE-based latent representations that lack explicit semantic structure, leaving the impact of the representation space largely unexplored. Slot-based object-centric representations offer a structured alternative by decomposing scenes into object-level latents, or slots. While they have shown success in dynamics mod...
  </details>

- **2026-09-15** — Danxuan Liang, Chun Yin Li, Zheng Wei et al. — [LumiNote: LLM-Assisted Multimodal Instruction for VR Stage Lighting Education](http://arxiv.org/abs/2609.17335v1)
  <details><summary>📄 Abstract</summary>
  Stage lighting education requires instructors to bridge abstract concepts, technical operations, and learner-understandable representations. While Virtual Reality (VR) removes physical constraints, existing systems provide limited support for live instruction. We present LumiNote, an LLM-assisted VR system that transforms spoken pedagogical intent into instructor-reviewable spatial annotations, executable demonstrations, and linguistic support. In an exploratory study with 3 instructors and 24 s...
  </details>

- **2026-09-15** — Lyes Saad Saoud — [Machine Zygote: Causal Biparental Heredity Before Learning in a Germline--Soma Artificial Agent](http://arxiv.org/abs/2609.17300v1)
  <details><summary>📄 Abstract</summary>
  Artificial ontogeny, developmental encodings, robot reproduction, and inherited controllers are established research directions, yet a narrower question remains: can a newborn artificial agent exhibit measurable biparental heredity before learning, and can that dependence be isolated causally rather than inferred only from parent-offspring resemblance? We introduce Machine Zygote, a computational germline-soma architecture designed to test this question. Two parental germlines are independently ...
  </details>

- **2026-09-15** — Marco Luca Sbodio, Marcos Martínez Galindo, Vanessa Lopez et al. — [Extracting ontology-compliant knowledge from scientific text describing irradiated materials using large language models](http://arxiv.org/abs/2609.17291v1)
  <details><summary>📄 Abstract</summary>
  The quest for new materials increasingly relies on predictive models and comprehensive simulations that span scales from atomic to macroscopic levels. However, essential data necessary for these models and simulations are often embedded in scientific literature as unstructured text, limiting reusability and posing challenges for researchers seeking to leverage existing knowledge effectively. While extracting structured data from unstructured text using large language models is gaining popularity...
  </details>

- **2026-09-15** — Maxim Mednikov, Oren Gal — [Calibrate Once, Fly Any Team: Residual-Grounded Low-Fidelity Training for Cooperative Drone Swarms](http://arxiv.org/abs/2609.17265v1)
  <details><summary>📄 Abstract</summary>
  Training multi-agent drone-swarm policies directly in high-fidelity (HF) rigid-body physics is accurate but computationally expensive. This cost scales poorly with team size, as each additional agent multiplies contact-resolution complexity and sharply raises the in-simulation crash rate. To address this, we propose a mixed-fidelity training scheme that eliminates HF reinforcement learning entirely.   A single shared, decentralized policy is optimized inside a fully-differentiable, JAX-native lo...
  </details>

- **2026-09-15** — Cai Ke, Jiangyue Yan, Han Zhang et al. — [Interactive Memory Learning for Long-Term Conversations](http://arxiv.org/abs/2609.17088v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in large language models have significantly enhanced the capabilities of agents in modeling long-term conversations. Despite these successes, existing approaches typically adopt a static heuristic paradigm, where information is passively archived without adaptive memory valuation. Consequently, these methods fail to self-evolve or align their memory management with evolving user needs. To address this, we propose ICML (InteraCtive Memory Learning), a multi-agent framework tha...
  </details>

- **2026-09-15** — Zhang Nengbo — [Waggle Dance Inspired Motion Communication for Multiple UAVs in MuJoCo](http://arxiv.org/abs/2609.16958v1)
  <details><summary>📄 Abstract</summary>
  The honeybee waggle dance motivates a communication mechanism in which one agent's movement conveys spatial information that guides other agents' actions. This paper presents a MuJoCo system that extends the point-to-point motion communication setting of MoCom to one performer and multiple observers. A performer broadcasts a six-bit navigation payload using four flight primitives and explicit null signals. Each of one to five observers processes its own onboard RGB images, extracts optical-flow ...
  </details>

- **2026-09-15** — Zeyuan Huang, Gang Chen, Zixuan Hao et al. — [Artificial Intelligence-Enabled Space Robot Operations: Technologies, Challenges and Prospects](http://arxiv.org/abs/2609.16880v1)
  <details><summary>📄 Abstract</summary>
  Space robots are increasingly expected to perform long-duration, contact-rich, and multi-stage operations with limited human intervention. Recent advances in artificial intelligence (AI), robot learning, and embodied foundation models provide new opportunities to improve the autonomy and adaptability of such systems, but their transfer to space is constrained by scarce mission data, space-specific dynamics and sensing conditions, limited onboard resources, and stringent safety requirements. This...
  </details>

- **2026-09-15** — Pengfei Zhu, Julien Lecompagnon, Mathias Ziegler — [Can Deep Learning Achieve Cross-Physics Mapping?](http://arxiv.org/abs/2609.16853v1)
  <details><summary>📄 Abstract</summary>
  Can deep learning translate physical fields governed by fundamentally different equations? We address this question by introducing Cross-Physics Mapping (CPM), an operator-learning framework for mappings between heterogeneous physical domains. We formulate sufficient conditions for such mappings through compatible latent representations and propose a dimensionless scaling principle that aligns the characteristic evolution scales of the source and target systems without assuming their dynamical e...
  </details>

- **2026-09-15** — Keisuke Masuda, Kazutaka Yatsushiro, Hirohumi Iwamoto et al. — [Japanese Stroke LLM Evaluation: A Conversational Benchmark for Safe Stroke Care in Japanese Using Large Language Models](http://arxiv.org/abs/2609.16739v1)
  <details><summary>📄 Abstract</summary>
  Background: Large language models (LLMs) have achieved physician-comparable performance on multiple-choice medical knowledge examinations, but their capabilities in clinical history taking, urgency assessment, and safety remain insufficiently evaluated. We proposed Japanese Stroke LLM Evaluation, a multi-turn conversational benchmark for stroke care in Japanese, and evaluated LLM performance and safety under practice-oriented conditions. Methods: We created 10 stroke and related-condition cases ...
  </details>

- **2026-09-15** — Wen Bing, Bing Li — [SpecLens: LLM-Based Verilog Generation with Specification-Derived Constraints via Behavioral Divergence](http://arxiv.org/abs/2609.16729v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently shown promise in Verilog generation, but producing functionally correct RTL directly from natural-language specifications remains a highly challenging task. Existing approaches improve LLM-based Verilog generation mainly with retrieval-augmented generation (RAG), self-planning, or few-shot prompting. However, these methods focus primarily on external or generic forms of enhancement rather than strengthening the specification with task-specific constrain...
  </details>

- **2026-09-15** — Tingyu Guo, Reza Langari — [CorrRisk-WM: Corridor-Conditioned Risk World Modeling for Safety-Critical Trajectory Planning](http://arxiv.org/abs/2609.16724v1)
  <details><summary>📄 Abstract</summary>
  Safe local planning requires forecasting surrounding-agent motion and evaluating candidate-specific risks, since identical agent motion can pose different risks to different ego trajectories. We present CorrRisk-WM, a planning-oriented partial world model coupling environment evolution with supervised intrusion and near-miss prediction over bounded candidate-trajectory corridors. A latent environment model recursively predicts agent states and updates agent-agent and agent-map interactions. Each...
  </details>

- **2026-09-15** — Sifan Zhou, Qiwei Wang, Linyue Tan et al. — [MAETrack: Unleashing the Potential of Pretrained Geometric Priors for 3D Single Object Tracking](http://arxiv.org/abs/2609.16695v1)
  <details><summary>📄 Abstract</summary>
  Large-scale pre-training has transformed representation learning in 2D vision, yet its transferability to 3D single object tracking (SOT) remains insufficiently understood. Directly fine-tuning self-supervised 3D encoders, such as masked autoencoders (MAE), often leads to sub-optimal adaptation because the reconstruction objective is not fully aligned with the spatial-temporal matching requirements of tracking. In this paper, we observe that this difficulty can be interpreted as a layer-wise tra...
  </details>

- **2026-09-15** — Minghua He, Lingzhe Zhang, Yuan Liu et al. — [GrowMTP: Can RL Grow Its Own Draft Head?](http://arxiv.org/abs/2609.16648v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) post-training drives the frontier capabilities of large language models, with its wall-clock dominated by autoregressive rollout generation. Speculative decoding is an established remedy for this bottleneck, but existing draft heads must be pretrained or warmed up before RL, introducing substantial training cost outside the RL run to be accelerated. We observe that RL training itself provides both conditions required for online draft-head training: its rollout distrib...
  </details>

- **2026-09-15** — Yang Zhao, Zhuo Chen, Xubo Yang — [EgoPathBench: Evaluating Zero-Shot Egocentric Waypoint Decision-Making in Vision-Language Models](http://arxiv.org/abs/2609.16610v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot waypoint navigation requires vision-language models to select, from the current first-person observation, a sequence of spatial actions that is feasible for the agent and reaches the goal, placing joint demands on the integrated spatial intelligence of today's foundation VLMs. Existing spatial-intelligence benchmarks primarily evaluate isolated judgments of relations, directions, or targets and therefore do not directly measure the integrated navigation ability required to combine targ...
  </details>

- **2026-09-15** — Jun Chen, Qi Zhao, Yunliang Jiang et al. — [A multimodal large language model for evidence-based autism spectrum disorder screening](http://arxiv.org/abs/2609.16464v1)
  <details><summary>📄 Abstract</summary>
  The clinical management of autism spectrum disorder (ASD) faces a bottleneck in early screening, mainly because trained specialists are scarce and conventional assessment tools are subjective. Here, we introduce ASDchat, a multimodal large language model designed for evidence-based ASD screening, which takes video, audio, and dialogue as input. ASDchat adopts a dual-branch architecture, where the decision branch generates screening probabilities and the evidence branch generates traceable, times...
  </details>

- **2026-09-15** — Fabian Harlacher, Christian Friedrich — [CAD-Based Relation Learning and Geometric-Symbolic Planning for Robotic Assembly](http://arxiv.org/abs/2609.17263v1)
  <details><summary>📄 Abstract</summary>
  Assembly Sequence Planning (ASP) remains a challenging problem due to its combinatorial nature, making exhaustive planning approaches impractical for complex industrial assemblies. Furthermore, many CAD models lack reliable semantic contact information or require extensive manual preprocessing, limiting the applicability of existing methods. This paper presents a hybrid ASP framework combining learning-based relation extraction with geometric-symbolic reasoning to generate feasible robotic disas...
  </details>

- **2026-09-15** — Zhenyang Feng, Jimin Heo, Erik B. Sudderth et al. — [TEMPO: Learning Temporal Context for Dynamic Robot Manipulation](http://arxiv.org/abs/2609.16864v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have achieved impressive performance in quasi-static manipulation, but struggle in dynamic manipulation tasks because they operate on a single observation at inference time. We identify two representational failures that underlie this limitation. The first is motion ambiguity, where a single observation does not include scene dynamics and therefore cannot anticipate the future state of moving objects. The second is state aliasing, where visually similar observ...
  </details>

- **2026-09-15** — Bo Kang — [The Latent That Never Was: A Forensic Re-run of the CVAE Ablation in Action Chunking Transformer](http://arxiv.org/abs/2609.16745v1)
  <details><summary>📄 Abstract</summary>
  Action Chunking Transformers (ACT) are widely used to learn robot manipulation from demonstrations. Their conditional variational autoencoder includes an encoder meant to capture differences between demonstrations during training. The original ACT paper reported that encoder removal dropped the mean success rate from 35% to 2% on two simulated tasks with human demonstrations. We re-ran this ablation in the original code and checked whether the findings depend on the implementation or training da...
  </details>

- **2026-09-15** — Hyesung Lee, Si-Hwan Heo, Sungwook Yang — [UniDex-ViTac: Learning Unified Visuo-Tactile Dexterous Manipulation Policy from Human Video Data](http://arxiv.org/abs/2609.16504v1)
  <details><summary>📄 Abstract</summary>
  Human videos provide demonstrations of dexterous manipulation but lack robot-executable actions and tactile measurements. We present UniDex-ViTac, a framework that uses human-video-guided simulation to generate robot demonstrations paired with fingertip contact observations for training a deployable visuo-tactile policy. Object-specific residual reinforcement learning specialists adapt annotated human-object interaction references to a robotic arm-hand system. Their successful rollouts pair fina...
  </details>

- **2026-09-15** — Zhaoyang Wei, Zipeng Wang, Yushe Cao et al. — [Video-HolmesV2: Can MLLMs Reason with Spatio-Temporal Audio-Visual Evidence in Long Videos?](http://arxiv.org/abs/2609.17248v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models have demonstrated impressive video understanding, yet their ability to reason over long-form narratives is often masked by visual-centric evaluations and inefficient context processing. Existing benchmarks over-rely on visual heuristics while marginalizing auditory cues, effectively reducing models to "silent observers" that bypass genuine cross-modal reasoning. Moreover, standard dense sampling creates an evidence-context trade-off: increasing frames to capture ...
  </details>

- **2026-09-15** — Mohammad Ammar Mughees, Giovanni Montefoschi, Zhongxin Chen et al. — [From Foundation Embeddings to Cropland Maps: Label Efficiency, Temporal Transferability and Independent Human Validation](http://arxiv.org/abs/2609.17138v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models provide reusable representations of satellite imagery that support downstream mapping with limited task-specific modelling. We evaluate whether annual AlphaEarth embeddings support binary cultivated-versus-non-cultivated mapping in Maine, USA, using 192 spatially separated patches and labels derived from the USDA Cropland Data Layer (CDL). Without fine-tuning the foundation model, a lightweight classifier reaches 93.7% overall accuracy and 90.8% balanced accuracy on ...
  </details>

- **2026-09-15** — Lilian Killich, Marko Schmellenkamp, Fabian Vehlken et al. — [Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs](http://arxiv.org/abs/2609.17111v1)
  <details><summary>📄 Abstract</summary>
  Modelling with mathematical formalisms like logical formulas, mathematical equations, or regular expressions is an important yet challenging task for students of computer science and other STEM disciplines. Identifying common mistakes occurring in this context is an important step towards helping struggling students by providing targeted high-quality feedback, e.g. in interactive learning systems.   We present a tool-supported workflow that allows to (1) identify candidates for common mistakes t...
  </details>

- **2026-09-15** — Shiqi Liu, Zeyu He, Letian Tao et al. — [Beyond Token-Local Imitation: Reward-Compatible Temporal Credit Assignment for On-Policy Distillation](http://arxiv.org/abs/2609.16937v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has emerged as an effective approach for large language model post-training, yet existing objectives face a trade-off between objective fidelity and optimization stability. Token-level OPD provides stable but local supervision, whereas sequence-level OPD captures future credit at the cost of horizon-dependent variance. We establish a unified temporal-credit view of these formulations, showing that practical token-level OPD can be interpreted as a temporal approximati...
  </details>

- **2026-09-15** — Shan-Zhong Li, Zhi Li — [Nonlocal Magic across the Many-Body Localization Crossover](http://arxiv.org/abs/2609.16935v1)
  <details><summary>📄 Abstract</summary>
  Nonlocal magic quantifies the minimum nonstabilizerness attainable under independent local unitary transformations on the two subsystems. Here, we use min-relative nonlocal magic (NLM) to characterize the crossover from ergodicity to many-body localization (MBL) in the random-field XXZ chain. Unlike entanglement entropy, NLM probes how entanglement is organized through the distance of the Schmidt spectrum from dyadic-flat stabilizer spectra. From weak to intermediate disorder, NLM evolves from a...
  </details>

- **2026-09-15** — Chenhao Zeng, Zhibin Pu, Shufei Ge — [HyCoSeq: Contextual Hyperbolic Representation Learning for Genomic Sequences](http://arxiv.org/abs/2609.16925v1)
  <details><summary>📄 Abstract</summary>
  Hyperbolic geometry provides a natural inductive bias for genomic representation learning, but existing hyperbolic genomic models primarily use Lorentz convolutions to learn local sequence representations, while their residual pathways do not directly aggregate full Lorentz representations. We propose HyCoSeq, a contextual hyperbolic representation learning framework for genomic sequences. HyCoSeq incorporates weighted Lorentzian residual aggregation into multi-curvature Lorentz encoding, allowi...
  </details>

- **2026-09-15** — Miłosz Adamczyk, Tymoteusz Zapala, Piotr Borycki et al. — [PiPS: Post-Hoc Prototypical Explanations for Interpretable Semantic Segmentation](http://arxiv.org/abs/2609.16909v1)
  <details><summary>📄 Abstract</summary>
  With the increasing deployment of deep neural networks in critical systems, such as medical diagnostics and autonomous vehicles, ensuring their interpretability is crucial to building trust in decision-making systems. In the field of explainable artificial intelligence, prototype-based reasoning has gained particular popularity, as it mimics human cognitive processes by explaining model decisions based on visual similarity under the looks like this paradigm. While this paradigm has been thorough...
  </details>

- **2026-09-15** — Annirudh K P, Vinayak Rane, Shradha Atakar et al. — [Portable Vector NV-Diamond Magnetometer for Shot-Noise-Limited, Drift-Free Operation in Unshielded Environments](http://arxiv.org/abs/2609.16901v1)
  <details><summary>📄 Abstract</summary>
  Ensemble nitrogen-vacancy (NV) diamond magnetometers combine high sensitivity with vector-field reconstruction, but practical deployment is limited by errors arising from high-frequency laser noise during short-duration operations and slow-varying gain fluctuations and offset drift during long-term operation. Here, we present an integrated digital architecture for achieving NV magnetometry stability across distinct timescales. A dynamic differential readout continuously balances fluorescence and...
  </details>

- **2026-09-15** — Zhengyang Zhang, Haojin Zhou — [The Equivariance Criterion in a Linear Model for Random-$X$ Cases](http://arxiv.org/abs/2609.16897v1)
  <details><summary>📄 Abstract</summary>
  Equivariance is increasingly used in machine learning and statistics, often without systematic justification. In a companion article, the equivariance criterion was applied to the normal linear model with a fixed design matrix (fixed-$X$), yielding the minimum risk equivariant (MRE) estimators of the coefficient vector and of the condensed diagonal covariance matrix under a multivariate invariant location--scale group. We extend these results to the random-$X$ case, with covariates sampled from ...
  </details>

- **2026-09-15** — Fermín Moscoso del Prado Martín — [A Data-free Universal Prior over Syntactic Structures](http://arxiv.org/abs/2609.16854v1)
  <details><summary>📄 Abstract</summary>
  Probability is fundamental to theories of language comprehension, production, acquisition, and evolution, as well as to large language models. Existing theories estimate the probability of syntactic structures from language-specific data. Whether part of this probability structure can arise independently of language-specific experience remains unknown. Here I show that a universal prior over syntactic structures emerges from a cognitively motivated model of incremental language production, in wh...
  </details>

- **2026-09-15** — Younes Boufouss, Luc Pommeret, Thomas Gerald et al. — [Can We Do Interpretable NLI with Graphs Based on Atomic Propositions?](http://arxiv.org/abs/2609.16814v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Model (LLM)-based Natural Language Inference (NLI) systems achieve high accuracy, their decision-making processes lack auditable structures. This paper explores whether NLI can be performed using only interpretable, graph-based representations of evidence. We introduce a fully graph-based pipeline where the classifier never directly processes the input text. Instead, sentences are decomposed into atomic propositions, converted into ConceptNet triples via constrained decoding...
  </details>

- **2026-09-15** — Biswas Rudra Jyoti Arka, Sadman Sakib, Md. Zahidul Islam et al. — [Explainable Post-Disaster Grid Observability Recovery Using Human-Oversight Agentic LLMs](http://arxiv.org/abs/2609.16774v1)
  <details><summary>📄 Abstract</summary>
  Post-disaster phasor measurement unit (PMU) outages reduce power-system observability and degrade operator situational awareness, requiring sequential restoration under limited resources. Existing PMU restoration methods based on optimization or heuristics can generate restoration schedules, but they often provide limited support for explanation, traceability, and operator interaction. This paper proposes an agentic tool-calling framework orchestrated by a large language model (LLM) for post-dis...
  </details>

- **2026-09-15** — Xiaobin Li — [Cartan-Fejer Gram Tomography and Flop Covariance for BPS Resummed Gromov-Witten Potentials](http://arxiv.org/abs/2609.16693v1)
  <details><summary>📄 Abstract</summary>
  We introduce a matrix-valued finite difference formalism for the genus zero BPS resummed local Gromov-Witten potential of a threefold flop. Factoring the central difference as \[ Δ_η=\nabla_η^2, \qquad \nabla_η=T_{hη/2}-T_{-hη/2}, \] we prove that the mixed differences \( \mathbf H=(\nabla_{η_i}\nabla_{η_j}F)_{i,j} \) admit an exact rank one signed \(q\)-Gram decomposition. Primitive BPS classes are therefore detected by rank one coefficient matrices, and a matrix-valued Möbius inversion reconst...
  </details>

- **2026-09-15** — Zhipeng Zhao, Wenxu Wang, Peishun Liu et al. — [Mechanism-Level Evaluation for Vision-Language Models: Controlled Activation-Replacement Diagnosis of Gender Bias](http://arxiv.org/abs/2609.16651v1)
  <details><summary>📄 Abstract</summary>
  Behavioral benchmarking reveals \emph{what} biases exist in vision-language models but not \emph{which internal components} are most sensitive to targeted intervention, precluding principled intervention. We argue for mechanism-level evaluation as a necessary complement, demonstrating causal mediation analysis as a diagnostic instrument for gender bias. We decompose gender-cue effects into controlled indirect effects attributable to specific-layer activations and direct effects through all other...
  </details>

- **2026-09-15** — Zixiu Ding, Zilin Zhao, Yingjie He et al. — [SAVOR: Self-Aware Visual Grounding via Confidence-Calibrated Reinforcement Learning for Multimodal Hallucination Mitigation](http://arxiv.org/abs/2609.16601v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have made strong progress on visual question answering and image captioning, yet they still produce fluent claims about objects, attributes, or relations that are not grounded in the image. Many remedies either modify decoding at test time, which adds latency, or fine tune with preferences such as DPO variants, which teach which answer is preferred but not when the model's own answer is unreliable. We argue that calibrated self assessment is the missing s...
  </details>

- **2026-09-15** — William L. Tong, Aryo Lotfi, Emmanuel Abbe et al. — [On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models](http://arxiv.org/abs/2609.16540v1)
  <details><summary>📄 Abstract</summary>
  State Space Models (SSMs) have emerged as a compelling alternative to Transformers, enabling sequence modeling with constant memory and linear compute. Although SSMs exhibit reasonable performance and favorable computational characteristics, they continue to lag behind Transformers on tasks that require in-context learning and precise retrieval, slowing their adoption for large-scale language modeling. In this work, we demonstrate that both the success and failure of SSMs in these domains can be...
  </details>

- **2026-09-15** — Daniel Ebanks, Devika Jain — [Geospatial Metadata Improves Discoverability by Connecting Datasets Across Scientific Disciplines](http://arxiv.org/abs/2609.16498v1)
  <details><summary>📄 Abstract</summary>
  Research data repositories are essential infrastructure for scientific inquiry and for ensuring that datasets follow FAIR (Findable, Accessible, Interoperable, and Reusable) principles. However, repository reuse depends on the quality and completeness of geospatial and thematic metadata, which researchers generally provide voluntarily. Given limited curation resources, it is unsurprising that even Harvard Dataverse, the world's largest general-purpose research repository, contains many incomplet...
  </details>

- **2026-09-14** — Mahjabin Nahar, Eun-Ju Lee, Yujin Heo et al. — [When AI Says "I Am Unable to Answer": Understanding User Responses to AI Refusals](http://arxiv.org/abs/2609.16191v1)
  <details><summary>📄 Abstract</summary>
  While refusal-based safeguards to mitigate hallucinations in large language models (LLMs) are becoming increasingly common, they may conflict with users' preferences for definitive answers. However, we know little about how users respond to refusals across repeated interactions, when refusals become more or less acceptable, and for whom. In this work, we examine how refusal frequency, explanations, and need for cognitive closure (NFCC) shape responses to AI refusals. Participants (N=599) interac...
  </details>

- **2026-09-14** — Kai Wang, Carlton Baugh, Sownak Bose et al. — [Forged in Quenching: Morphological Transformation across Star-forming and Quiescent Galaxies in EAGLE](http://arxiv.org/abs/2609.16187v1)
  <details><summary>📄 Abstract</summary>
  The connection between morphology and quenching in central galaxies is well established, but its physical origin remains widely debated. We address this by tracing the main progenitor branches of $z=0$ star-forming and quiescent central galaxies in the EAGLE cosmological simulation from $z\gtrsim4$. Their disc-to-total ratio and triaxiality tracks are indistinguishable until $z\approx 1$-$2$, when both diverge concurrently with the onset of quenching, whereas the size and supermassive black hole...
  </details>

- **2026-09-14** — Teanna Barrett, B. Biira, Jainaba Jawara et al. — [Moral Missions: Surfacing Moral Decision-Making Strategies for Responsible Data Science Practice](http://arxiv.org/abs/2609.16166v1)
  <details><summary>📄 Abstract</summary>
  A growing ecosystem of techniques, toolkits, and guidelines has been developed to help data scientists consider the social implications of data-driven technologies. However, prior literature highlights that even when this ecosystem of techniques is provided to professional data scientists, they still struggle to consistently adopt a responsible data science practice. We posit that the key to sustained responsible data science practice is to approach it as a moral mission: a conviction-driven tec...
  </details>

- **2026-09-14** — Pinak Banerjee, Subham Roy, Xingyang Yu — [Symmetry Descent in M-theory, Part I: A Twelve-Dimensional Parent Theory](http://arxiv.org/abs/2609.16141v1)
  <details><summary>📄 Abstract</summary>
  We initiate a symmetry descent procedure for M-theory engineered quantum field theories. Starting from a higher form BF theory supplemented by a cubic bulk topological interaction, we construct a gauge-invariant bulk-boundary system whose edge modes acquire generalized Maxwell--Chern--Simons dynamics after the introduction of a metric-dependent boundary action. The nonlinear contribution to the boundary equation is induced entirely by the cubic bulk interaction. In the case of twelve dimensional...
  </details>

- **2026-09-14** — Ivy Ning Zhang — [Coaching Qwen3 Coder 30B to Think Like a CodeClash Arena Agent](http://arxiv.org/abs/2609.16096v1)
  <details><summary>📄 Abstract</summary>
  Large language model coding agents have recently become useful for software tasks, but weaker or open-weight agents still struggle to reliably interpret user intent and execute complex multi-step workflows. This gap is especially visible in long-horizon settings, where an agent must repeatedly inspect prior outcomes, diagnose failure, and choose the next code edit under interaction constraints. It motivates a natural question: what can we do to improve the thinking process of a weak code agent? ...
  </details>

- **2026-09-14** — Nimit Shah, Haitz Sáez de Ocáriz Borde — [Evaluating Open-Weight E-Commerce Agents with Environment-Grounded Verification](http://arxiv.org/abs/2609.16093v1)
  <details><summary>📄 Abstract</summary>
  A shopping conversation has many routes to the same cart, and a task-success rate reduces all of them to one score. We build a deterministic and reproducible e-commerce environment that precommits each trial's customer and trajectory parameters, including the persona, difficulty, target cart, and an item reveal schedule. A simulated consumer attempts to buy a target cart from the environment with assistance from the evaluated model. The environment guides the simulator's actions and records ever...
  </details>

- **2026-09-14** — Honghao Lin, David P. Woodruff, Yuan Deng et al. — [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](http://arxiv.org/abs/2609.15983v2)
  <details><summary>📄 Abstract</summary>
  Language models can produce plausible short proofs, but may still be unreliable on long-horizon research problems, where progress depends on a sequence of uncertain and interdependent decisions. We introduce Stellar Colosseum, a model-agnostic harness for allocating inference across research in mathematics and theoretical computer science. Colosseum explores alternative strategies before proof construction, uses a readiness gate to decide when a route is mature enough to decompose, represents th...
  </details>

- **2026-09-14** — Micah Adler, John W. Byers, Mark Crovella — [Attention Mean Fields Predict Average Representation Dynamics and Reveal Context-Specific Computation](http://arxiv.org/abs/2609.16382v1)
  <details><summary>📄 Abstract</summary>
  A language model's representation geometry is not predetermined; it evolves as the model runs. A faithful account of that geometry must capture that dynamic process, and so cannot be based solely on model-independent statistics such as co-occurrence. Here we introduce a mean-field analysis of attention. The average attention from one token to another defines a kernel that carries representations layer to layer and can be iterated through the network to model how the geometry is transformed. We c...
  </details>

- **2026-09-14** — Yan Zhu, Yongbo Chen, Zhengming Ding et al. — [ProtoLIP: From Sentence-Level to Object-Level Evidence Disentanglement](http://arxiv.org/abs/2609.16284v1)
  <details><summary>📄 Abstract</summary>
  Query-conditioned vision--language models enable fine-grained interpretation by revealing how visual evidence changes with textual queries. However, evidence conditioned on complete descriptions does not necessarily resolve into object-specific evidence, nor does an exposed evidence map necessarily identify the evidence that constitutes the model's prediction. Across multiple VLM architectures and independent benchmarks, we find that object-level queries often retain evidence from co-occurring o...
  </details>

- **2026-09-14** — Valen Tagliabue, Leonard Dung, Cameron Berg — [The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It](http://arxiv.org/abs/2609.16247v1)
  <details><summary>📄 Abstract</summary>
  Large language models sometimes behave in ways resembling human emotional responses, and recent work has identified internal representations that may explain this. We ask whether LLMs represent pain distinctly from fear, sadness, and generic negative valence, and whether this representation functions as pain would be expected to. We build a dataset describing painful situations across five categories: physical, psychological, social, moral, and cognitive. These are paired with controls for fear,...
  </details>

- **2026-09-14** — H. Yousef, H. Hassan, I. Roy et al. — [A deep dive into Tollmien-Schlichting wave control via passive wall deformations: The battle between local and downstream stabilization, lessons learned, and implications for phononic subsurfaces](http://arxiv.org/abs/2609.16144v1)
  <details><summary>📄 Abstract</summary>
  A decade ago, a landmark study on flow control via subsurface phonons transformed our understanding of fluid-structural interactions, compelling us to reimagine ways by which to suppress boundary layer instabilities. While subsequent investigations have steadily enriched this landscape, several questions remain largely unanswered. The notion of Tollmien-Schlicting (TS) wave stabilization relies on phase-engineered surface interactions, which destructively engage with the wave and impede its grow...
  </details>

- **2026-09-14** — Zhancheng Guo, Congren Dai, Shangda Wu et al. — [MUUNRiver-Bench: Diagnosing Relation-Dependent Music Retrieval with Multimodal Instructions](http://arxiv.org/abs/2609.16090v1)
  <details><summary>📄 Abstract</summary>
  Music retrieval is relation-dependent: given a reference track, a listener may seek its style with a new theme, a cover, or a comparable voice, and these intents demand contradictory rankings. We present MUUNRiver-Bench, a diagnostic benchmark whose reference-audio queries use natural-language instructions to define relevance. A pipeline combining expert genre priors, LLM-generated prompts and lyrics, synthesis, and expert review yields 3,440 tracks spanning 13 genres and 116 sub-genres, and sev...
  </details>

- **2026-09-14** — Jiayue Gaveal Fan, Arul Murugan, Shreyas Krishnan et al. — [Interpreting and Steering LLM Agents for Social Simulations](http://arxiv.org/abs/2609.16436v1)
  <details><summary>📄 Abstract</summary>
  Simulations based on large language models (LLMs) have proven to be powerful for understanding human behavior, making them valuable additions to the social scientific toolkit. However, LLMs are ultimately black boxes based on deep neural networks which limits their value for social science. This is because of a lack of (i) interpretability: i.e. the ability to assign clear mechanisms driving observed behavior; and a lack of (ii) steerability: i.e. the ability to mute or amplify specific theoreti...
  </details>

- **2026-09-14** — Reed Orchinik, David Rand — [A light-touch AI literacy intervention helps protect against AI political persuasion](http://arxiv.org/abs/2609.16432v1)
  <details><summary>📄 Abstract</summary>
  Conversations with large language models (LLMs) can substantially shift beliefs and attitudes, raising concerns about manipulation using AI persuasion. Here we test whether a light-touch AI literacy intervention - a brief warning that LLMs can be prompted to persuade and may present information selectively - helps protect users. Across two experiments (total N = 3,208 Americans) in which participants conversed with an LLM instructed to shift their views about different political topics, the pres...
  </details>

- **2026-09-14** — Peiqi Yu, Mosam Dabhi, Shangtao Li et al. — [ManiSkillFormer: Demonstration-Free Compositional Manipulation via Task-Conditioned Geometric Contracts](http://arxiv.org/abs/2609.16331v1)
  <details><summary>📄 Abstract</summary>
  We present ManiSkillFormer, a neuro-symbolic framework for demonstration-free and compositional robotic manipulation. Instead of learning end-to-end visuomotor policies, ManiSkillFormer introduces task-conditioned geometric contracts that explicitly structure the interface between perception and action. Each manipulation skill declares the semantic geometric primitives required for execution, such as object keypoints and surface normals. Building on human-defined skill structures, LLM agents gen...
  </details>

- **2026-09-14** — Zihan Dong, Yuanzhe Liu, Zhiyuan Ma et al. — [CADWorld: Computer-Use Benchmark for Long-Horizon Computer-Aided Design](http://arxiv.org/abs/2609.16251v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents are increasingly evaluated in realistic desktop environments, but existing benchmarks provide limited coverage of professional engineering workflows whose outputs are persistent, structured artifacts. Mechanical computer-aided design (CAD) is a particularly demanding setting: an agent must manipulate geometry and constraints over long interaction horizons while producing a native project whose dimensions, construction structure, and downstream engineering state remain valid. ...
  </details>

- **2026-09-14** — Christos Galanopoulos, Kimon Antonios Provatas, Ilias Georgakopoulos-Soares — [Feasibility of Homomorphic Inference for a Genomic Foundation Model](http://arxiv.org/abs/2609.16211v1)
  <details><summary>📄 Abstract</summary>
  Human genomic sequences can identify individuals, cannot be replaced after disclosure, and are the inputs that genomic foundation models are designed to interpret. We assess whether a compute provider can execute a released genomic foundation model without receiving query-derived genomic values in plaintext and whether correctness, memory, or cost prevents complete encrypted inference. We first reproduce the released model on three genomic task families and freeze an independently validated nume...
  </details>

- **2026-09-14** — Andrea Morghen, Pierluigi Arpenti, Roberto Schiattarella et al. — [Structure-Preserving Quantum Circuit Architectures for Robot Kinematics](http://arxiv.org/abs/2609.16089v1)
  <details><summary>📄 Abstract</summary>
  Structured spatial data require quantum encodings that preserve geometric relations, expose measurable observables, and remain implementable on finite-depth hardware. This work introduces a quantum representation and circuit architecture for rigid-body transformations and specializes it to Denavit--Hartenberg kinematics of serial open-chain manipulators. Each translational contribution is factorized into a classical metric magnitude and a signed unit direction encoded by a single-qubit Bloch vec...
  </details>

- **2026-09-14** — Honghao Lin, David P. Woodruff, Yuan Deng et al. — [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](http://arxiv.org/abs/2609.15983v1)
  <details><summary>📄 Abstract</summary>
  Language models can produce plausible short proofs, but may still be unreliable on long-horizon research problems, where progress depends on a sequence of uncertain and interdependent decisions. We introduce Stellar Colosseum, a model-agnostic harness for allocating inference across research in mathematics and theoretical computer science. Colosseum explores alternative strategies before proof construction, uses a readiness gate to decide when a route is mature enough to decompose, represents th...
  </details>

- **2026-09-14** — Tobias Ladner, Matthias Althoff — [The Misery of Mechanistic Interpretability: A Formal Perspective](http://arxiv.org/abs/2609.15533v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability has become the dominant lens for understanding frontier language models, as their inner workings are complex and inherently black boxes. To gain insights into these models, interpretable replacement networks (IRNs) are trained at all layers, exposing interpretable features through sparsely activated neurons. However, the faithfulness of an IRN is usually evaluated only empirically on clean data, and we show that even semantically minor input perturbations flip the do...
  </details>

- **2026-09-14** — Zeyang Li, Sunbochen Tang, Navid Azizan — [Safe Meta-Reinforcement Learning via Information Space Reachability](http://arxiv.org/abs/2609.15915v1)
  <details><summary>📄 Abstract</summary>
  Meta-reinforcement learning (meta-RL) enables agents to adapt to unseen tasks with limited experience. Despite its promise, the application of meta-RL in real-world tasks is hindered by safety requirements, which have been underexplored in prior work. In this paper, we propose a safe meta-RL framework that explicitly accounts for safety during adaptation. Our key insight is to reason about safety in the information space, which captures both the physical state and the agent's belief over the und...
  </details>

- **2026-09-14** — Xiaofeng Mao, Peijia Lin, Shaohao Rui et al. — [LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](http://arxiv.org/abs/2609.15863v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion models are stochastic and hard to control: precise content often requires repeated sampling without guaranteed success, and long-horizon scenes drift in appearance, interactions, and temporal coherence. Agentic visual creation provides explicit references, editable 3D scenes, or executable game states for stable control, but does not by itself guarantee high object or character fidelity. Combining the two can enable stable, high-quality generation. To realize this combination, we...
  </details>

- **2026-09-14** — Jocelyn Kang, Caroline Zhang — [KnowBench: Effort Reduction as a Unified, Deployment-Grounded Benchmark for Clinical AI](http://arxiv.org/abs/2609.15794v1)
  <details><summary>📄 Abstract</summary>
  Clinical AI systems are evaluated with instruments built for research settings (reference-based similarity metrics and expert rubric panels) that measure resemblance to an artifact rather than reduction of a burden. We introduce KnowBench, pioneered by Knowtex, whose unifying metric is Effort Reduction (ER): the proportion of system-generated clinical work product accepted by the responsible clinician under expert and safety review. ER is defined once and instantiated per task across the adminis...
  </details>

- **2026-09-14** — Jiajie He, Jiangyuan Hong, Dongling Ni et al. — [Are LLMs Good Financial User Simulators? A Preliminary Study](http://arxiv.org/abs/2609.15727v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as user simulators, but their ability to reproduce evolving individual financial decisions remains unclear. We present a preliminary study in a controlled paper-trading environment with 120 volunteers. Participants used non-redeemable virtual funds under real-time market conditions; no real brokerage accounts, real-money positions, or real transaction records were accessed. Given only information available before a prediction cutoff, a simulator...
  </details>

- **2026-09-14** — Lemen Chao, Zixuan Yang, Anran Fang et al. — [Data storytelling meets interpretable machine learning: Decoding AI decisions for non-experts without revealing sensitive data and model details](http://arxiv.org/abs/2609.15722v1)
  <details><summary>📄 Abstract</summary>
  AI-driven automated decision-making requires both predictive performance and interpretability. Recent advances in interpretable machine learning (IML) provide tools for explaining model predictions, but the technical complexity of these explanations may hinder accessibility to non-experts. To address this challenge, this study integrates data storytelling with IML to enhance the explainability of AI-generated decisions for a broader audience. Following the design science research (DSR) paradigm,...
  </details>

- **2026-09-14** — Jinyuan Deng, Yuqi Jiang, Wenjing Huang et al. — [Circuit-MLLM: Topological Logic-Guided Latent-Space Visual Reasoning for Circuit Schematic Understanding](http://arxiv.org/abs/2609.15668v1)
  <details><summary>📄 Abstract</summary>
  Through pre-training on extensive text and image datasets, current multi-modal large language models (MLLMs) achieve strong performance on general tasks. However, circuit schematics present a unique challenge for MLLMs due to their dense component layouts and distinct topological logic, demanding fine-grained structural parsing to extract the electrical semantics. To address this, we propose Circuit-MLLM, a multimodal reasoning framework that reformulates circuit topology analysis as a process o...
  </details>

- **2026-09-14** — JuHeon Ha, Byounghan Lee, Yunseo Choi et al. — [Empathy Is Steerable but Multi-Axial: Mechanism Geometry and Persona Effects in LLMs](http://arxiv.org/abs/2609.15654v1)
  <details><summary>📄 Abstract</summary>
  Activation steering has been used to control traits such as honesty, refusal, and sycophancy, yet supportive empathy is evaluated along multiple dimensions that need not correspond to independently controllable activation directions. Using the EPITOME framework, which decomposes supportive empathy into Emotional Reactions, Interpretations, and Explorations, we study three instruction-tuned LLMs and ask whether candidate directions derived from these labels produce distinguishable intervention ef...
  </details>

- **2026-09-14** — Haoyu Wang, Jing Yang, Chenyu Liu et al. — [Graph Attention Design Choices Matter: A Controlled Study of LoRA-Adapted Audio Anti-Spoofing](http://arxiv.org/abs/2609.15650v1)
  <details><summary>📄 Abstract</summary>
  Audio anti-spoofing systems increasingly combine self-supervised learning, parameter-efficient fine-tuning, and graph-attention-based backends. However, performance gains in such systems are often entangled with concurrent changes in the backbone, fine-tuning strategy, and training protocol, making the independent contribution of graph attention design difficult to isolate. To address this issue, we conduct a systematic controlled study of the graph attention layer under a unified experimental s...
  </details>

- **2026-09-14** — Son Ho, Cédric Fournet, Jonathan Protzenko et al. — [Scaling Verification of Cryptographic Software with Aeneas, Rust, and Lean](http://arxiv.org/abs/2609.15648v1)
  <details><summary>📄 Abstract</summary>
  We develop a new methodology for verifying cryptographic software. We target production code written in Rust for performance and system integration, rather than verification convenience. Rust's ownership discipline enables Aeneas to extract a pure model of this code in Lean, relieving us from low-level reasoning about pointer liveness and aliasing. Lean's extensibility lets us develop tactics and libraries that greatly simplify reasoning about extracted Rust code.   We design and tune our toolch...
  </details>

- **2026-09-14** — Jiawei Li, Fabio Bonassi, Johan Sundström et al. — [On the role of the tokenizer in ECG transformer models](http://arxiv.org/abs/2609.15433v1)
  <details><summary>📄 Abstract</summary>
  Tokenization determines both the physiological content presented to an ECG Transformer and the sequence over which attention operates. We compare eight tokenization strategies across Transformer, Informer, Reformer, and FEDformer on the nine-label CPSC2018 classification task. The input projection and principal backbone capacity are controlled to isolate the effect of token construction. Median-beat and HeartLang tokenization achieve mean macro-AUCs of 0.893 and 0.889 across the four backbones, ...
  </details>

- **2026-09-14** — Haoxiang Kang, Ming Wen — [SkillLift: Learning Dense Rubrics from Sparse Oracles for Efficient Skill Evolution](http://arxiv.org/abs/2609.15396v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents increasingly rely on persistent skills, i.e., reusable procedural prompts, to adapt without weight updates. Existing skill self-evolution methods directly revise skill text based on execution feedback, but each oracle evaluation requires a full agent rollout, creating a supervision bottleneck that confines search to failure-patching updates. Our key insight is that ranking is a smoother supervision target than absolute outcome regression: identifying which skill is better requir...
  </details>

- **2026-09-14** — Xudong Yuan, Shunyu Liu, Tongya Zheng et al. — [CodeTS: Verifiable Text-to-Time Series Generation via Executable Code](http://arxiv.org/abs/2609.15393v1)
  <details><summary>📄 Abstract</summary>
  Text-to-Time Series Generation (Text-to-TS) provides a promising paradigm for synthesizing time series from natural language, enabling scenario-specific generation when real observations are scarce or costly to acquire. However, existing methods typically lack an explicit mechanism for deriving generation logic from textual descriptions to guide time series synthesis. In this paper, we propose CodeTS, a verifiable framework that uses code as an intermediate generation interface, reformulating Te...
  </details>

- **2026-09-14** — Konstantinos Varsos, Ramin Khalili, Adamantia Stamou et al. — [A Game-Theoretic Framework for Incentive-Compatible AI training Under Renewable-Energy Constraints](http://arxiv.org/abs/2609.15389v1)
  <details><summary>📄 Abstract</summary>
  As artificial intelligence systems increasingly rely on distributed and collaborative training, the energy footprint of these processes becomes a shared responsibility. Modern AI training often unfolds across heterogeneous compute nodes-ranging from cloud clusters to edge devices-whose energy availability is spatially and temporally variable. At the same time, renewable energy grids experience growing levels of excess generation, creating opportunities to align computational workloads with low-c...
  </details>

- **2026-09-14** — Xinyue Xu, Hongbin Lin, Juangui Xu et al. — [Concept-Grounded Reasoning with Prompt-Driven Localization for Interpretable Structured Report Generation](http://arxiv.org/abs/2609.15334v1)
  <details><summary>📄 Abstract</summary>
  Medical imaging modalities such as ultrasound and X-ray are widely used in clinical practice, where diagnosis follows a structured, evidence-driven workflow aligned with standardized criteria. While multimodal large language models (MLLMs) show promise for automated medical report generation, most existing systems rely on end-to-end multimodal fusion without modeling clinically defined intermediate attributes, leading to limited grounding and interpretability. To address this issue, we propose C...
  </details>

- **2026-09-14** — Chanho Park, Bumsu Park, Soonhee Kwon et al. — [Thinking in Tokens, Talking in Bits: A Practical Interface for Token Communication](http://arxiv.org/abs/2609.15256v1)
  <details><summary>📄 Abstract</summary>
  Advanced artificial intelligence models think in tokens; contemporary communication systems carry bits. The direct way to bridge this gap is to transmit tokens, but that makes a model-specific representation part of the air interface, coupling the endpoints through a shared tokenizer, codebook, and often a neural transceiver. We take a different route: keep bits in the payload and let tokens control how those bits are generated and protected. The resulting token-bit interface transition aligns t...
  </details>

- **2026-09-14** — Rui Lu, Rui Ge, Huanghuang Liang et al. — [ETCInfer: An Energy-efficient Thermal-aware Cooling-joint Scheduler for LLM Inference in AI Datacenters](http://arxiv.org/abs/2609.15230v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference in AI datacenters creates a coupled control problem between GPU serving and facility cooling. Raising ambient temperature setpoints can reduce cooling energy and carbon, but also shrinks thermal headroom, induces GPU throttling, and leads to Service-Level-Objective (SLO) violations. In this paper, we study joint cooling--computing control for LLM inference: minimizing per-job GPU-plus-cooling energy while satisfying thermal safety and latency SLO constraints....
  </details>

- **2026-09-14** — Juntong Zhang, Chun Gu, Li Zhang — [X-WBC: A Cross-Embodiment Foundation Model for Humanoid Whole-Body Control](http://arxiv.org/abs/2609.15213v1)
  <details><summary>📄 Abstract</summary>
  Scaling humanoid whole-body control toward general-purpose deployment requires large human motion corpora and training experience shared across robot bodies. Existing methods usually train one policy per robot, leaving motion experience isolated across embodiments. We introduce X-WBC, a cross-embodiment foundation framework that separates relatively shared human motion semantics from embodiment-specific physical execution. Human-centered command tokens align full human motion, robot reference mo...
  </details>

- **2026-09-14** — Sriram Selvam, Anneswa Ghosh — [CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search](http://arxiv.org/abs/2609.15164v1)
  <details><summary>📄 Abstract</summary>
  When several retrieved sources support the same claim, an answer engine cites some but not others. We call this decision citation allocation and introduce CITECHOICE, a causal audit of authentic multi-turn agentic search. From 129 everyday-query transcripts, CITECHOICE selects 113 same-call document pairs with independently verified support for the same pre-specified fact, without observing ranks or answer outcomes; blinded human review confirms 103. It runs a hash-verified 2-by-2 replay crossin...
  </details>

- **2026-09-14** — Siran Zhang, Shuming Cheng, Xiang Li et al. — [A train--prune--readout--rewrite workflow for interpretable quantum learning](http://arxiv.org/abs/2609.15139v1)
  <details><summary>📄 Abstract</summary>
  AI for Science aims not only to predict complex physical systems from data, but also to extract mathematical structure and physically testable representations from learned models. Here, a train--prune--readout--rewrite workflow is developed that separates physical-domain grounding from three increasingly stringent analysis claims: algebraically equivalent readout of a trained predictor, compact teacher-faithful symbolic rewriting on the sampled physical domain, and transformation-based tests of ...
  </details>

- **2026-09-14** — Yunhao Feng, Ruixiao Lin, Ming Wen et al. — [HazardAuditor: From Executable Threats to Safer Computer-Use Agents](http://arxiv.org/abs/2609.15134v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents increasingly interact with browsers, terminals, file systems, and external services, introducing safety risks that emerge through runtime behavior rather than generated content alone. Existing guard models target static prompts and responses and are poorly suited to agent execution; existing executable safety platforms produce evaluation verdicts rather than the normalized supervision a guard model needs to learn across heterogeneous agent frameworks. We introduce HazardAudit...
  </details>

- **2026-09-14** — Kushagra Agrawal, Yuming Feng, Man-Fai Leung — [Translating the Translator: Decomposing the Cost of English-Forced Inter-Agent Communication](http://arxiv.org/abs/2609.15079v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM architectures, such as LangChain and AutoGen, largely assume English as the lingua franca for internal inter-agent communication, even when the end-user task is non-English. We fill this gap by evaluating a two-agent extraction-answer core, with an additional back-translation agent in the English-forced condition, across four typologically diverse languages (Hindi, Chinese, Spanish, Arabic; n = 300 per language) using the Aya-23-8B model. We compare a native-language pipeline to ...
  </details>

- **2026-09-14** — Yu Li, Qikun Cai, Tao Huang et al. — [Semantic-TVM: Structure-Preserving Trustworthy Virtual Memory for Memory-Augmented and Tool-Using Agents](http://arxiv.org/abs/2609.15011v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented and tool-using agents expose exact private values when remote LLMs process retrieved memory, tool actions, and intermediate observations. One-way masking limits direct exposure but removes values needed for trusted execution and can leak them through later observations. We propose Trustworthy Virtual Memory (TVM), a closed-loop runtime that keeps exact-value state local while presenting a protected view to the remote model. Within this single runtime, Rule-TVM replaces whole pro...
  </details>

- **2026-09-14** — Zhendong Li, Mingze Zhu, Zhou Su et al. — [Discrete Antenna Positioning and Beamforming Design for RIS-Assisted MA Secure ISAC Systems](http://arxiv.org/abs/2609.14974v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates a reconfigurable intelligent surface (RIS)-assisted movable antenna (MA) secure integrated sensing and communication (ISAC) system. In this architecture, the RIS establishes indirect transmission links to provide communication services for multiple legitimate users, while the high spatial diversity gain of MA is leveraged to enhance system security. Then, we formulate an optimization problem to maximize the system total secrecy rate by jointly optimizing the MA position s...
  </details>

- **2026-09-14** —  DeepCybo Team, Yu Bin, Haipeng Cao et al. — [PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models](http://arxiv.org/abs/2609.14973v1)
  <details><summary>📄 Abstract</summary>
  We present PhysBrain 1.5, a unified model for understanding physical environments, generating actions, and predicting future states. Motivated by the physical loop of observation, interaction, and environmental change, we bring these capabilities into a common learning framework. Starting from a general vision--language model, we encode language responses, end-effector motion, and dense visual targets as discrete sequences and jointly optimize them with autoregressive next-token prediction. Pre-...
  </details>

- **2026-09-14** — Yahya Mohamed Elnawasany — [A Corpus-Aligned Uthmani-to-Standard Quranic Word Mapping and a Deterministic Recitation Validator](http://arxiv.org/abs/2609.14967v1)
  <details><summary>📄 Abstract</summary>
  Quranic text is distributed in two orthographic forms that are byte-level distinct: the Uthmani script used in every printed mushaf, and the Standard (Imla'i) Arabic form that every mainstream Arabic NLP tool is built for. The gap is concentrated in one Unicode character, U+0670 (superscript alef), which appears in some of the most frequently recited words in the Quran and is silently mishandled by general-purpose Arabic normalizers. We release a 2,290-pair, corpus-aligned Uthmani-to-Standard wo...
  </details>

- **2026-09-14** — Beibei Jing, Tianle Guo, Youjia Zhang et al. — [MoVT: Video-Augmented Motion Tokenizer for Text-to-Motion Generation](http://arxiv.org/abs/2609.14965v1)
  <details><summary>📄 Abstract</summary>
  Text-driven 3D human motion generation models face significant challenges in responding to diverse and unconstrained textual prompts, primarily due to the limited availability of 3D motion training data. To address this, we introduce MoVT, a novel framework that effectively leverages the extensive range of human action videos to enhance text-to-motion generation. At the core of our approach is the cross-modal augmented motion tokenizer, which projects discrete 3D motion tokens into the 2D domain...
  </details>

- **2026-09-14** — Xinjing Zhou, Jason Mohoney, Samuel Madden et al. — [Chronos: Efficient Bolt-on Branching Across Data Stores for Stateful Agentic Applications](http://arxiv.org/abs/2609.14889v1)
  <details><summary>📄 Abstract</summary>
  Data-centric applications increasingly use speculative execution to explore multiple candidate paths where each path modifies state distributed across heterogeneous data stores. This trend is intensified by the rise of tool-calling agents. Hence, applications need data systems that can create branches quickly, isolate state-modifying paths, and merge changes consistently across stores without imposing substantial query overhead. Existing systems provide only partial support, forcing applications...
  </details>

- **2026-09-14** — Haoran Yu, Lifei Liu, Danping Zhang — [Toward Sustainable AI Deployment: A Carbon-Aware Decision Framework for Enterprise Supply Chain Systems](http://arxiv.org/abs/2609.14881v1)
  <details><summary>📄 Abstract</summary>
  Enterprises deploying AI for supply chain decisions commonly default to the largest available language model, a procurement heuristic that neglects both empirical performance and environmental cost. We benchmark six large language models across 520 supply chain tasks, simultaneously measuring decision quality and estimated generation-related operational carbon. Drawing on the Technology-Organization-Environment (TOE) framework, we develop a Carbon-Aware AI Procurement Framework (CAAPF), a Green ...
  </details>

- **2026-09-14** — Tong Zheng, Xidong Wu, Zheng Zhang et al. — [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](http://arxiv.org/abs/2609.14858v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement is becoming increasingly vital for autonomous AI agents, where progress hinges on discovering high-value solutions across complex domains. The driver of this process is effective exploration, however, managing and improving exploration strategies remains a major bottleneck. Current systems face a fundamental dilemma: fixed strategies fail to adapt as search spaces scale, while online policy optimization requires navigating vast meta-search spaces under delayed and expe...
  </details>

- **2026-09-14** — Matteo Grimaldi, David Klee, Ziling Chen et al. — [Touch2Trace: Tactile-Driven Imitation Learning for Dexterous Cable Tracing](http://arxiv.org/abs/2609.15921v1)
  <details><summary>📄 Abstract</summary>
  Dexterous manipulation of deformable objects demands continuous fingertip-level regulation of pressure, friction, and incipient slip. We study one of the most challenging cases: dexterous cable tracing, feeding a cable through the hand with repeated pinch-and-curl motions of the thumb and index finger. We introduce Touch2Trace, a tactile-driven imitation-learning system for this task, and provide, to our knowledge, the first systematic real-world characterization of how encoder pretraining, cont...
  </details>

- **2026-09-14** — Protik Dey, Mohd Saifuzzaman, Taslima Akter — [More Than Just Access: Generative AI as Communication Intermediary for Blind and Low-Vision Users](http://arxiv.org/abs/2609.15696v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) tools are increasingly woven into how blind and low-vision (BLV) people communicate, not only with digital information, but with the physical world and with other people. Tools such as ChatGPT, Google Gemini, Be My AI, and Seeing AI translate visual and textual content into accessible form, and are beginning to substitute for interpersonal requests for help, such as asking a family member to read a label or describe a scene. Drawing on semi-structured interviews with 19 BLV...
  </details>

- **2026-09-14** — Keuntae Kim, Eunhye Jeong, Yong Suk Choi — [CWM: Controllable White-Box Meta-Prompting for Adaptive Retrieval-Augmented Generation and Reasoning Ability](http://arxiv.org/abs/2609.15234v1)
  <details><summary>📄 Abstract</summary>
  Recently, Large Language Models (LLMs) have gained significant attention due to their strong language understanding and generation capabilities, demonstrating impressive reasoning abilities as well as effective utilization of external knowledge. Many studies have proposed methods that specialize in improving performance for individual tasks. However, ironically, only a limited number of attempts have explored general-purpose, task-agnostic methods. In this work, we present a unified framework in...
  </details>

- **2026-09-14** — Akash Kumar Panda, Olaoluwa Adigun, Bart Kosko — [Converting Sequenced Fuzzy Cognitive Maps to Causal Virtual Worlds with Large Video Generators](http://arxiv.org/abs/2609.14985v1)
  <details><summary>📄 Abstract</summary>
  We show how users can create and manipulate causal virtual worlds with large-language-model (LLM) and large-video-model agents. The approach uses feedback fuzzy cognitive maps (FCMs) both to model the granular causal structure of the virtual world and to guide its causal evolution. The local causal rules are partial or fuzzy while the FCM's feedback structure produces global equilibria that define causal scenarios. A sequence of \emph{dynamical} meta-rules of the form ``If $\mathcal{A}$ then $\m...
  </details>

- **2026-09-14** — Jieyuan Liu, Mengzhou Hu, Jefferson Chen et al. — [HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses](http://arxiv.org/abs/2609.15938v1)
  <details><summary>📄 Abstract</summary>
  Scientific agents contribute to hypothesis discovery by synthesizing evidence, assessing proposals, and developing new explanations. Recent systems combine scientific agents with evolutionary search through critique, comparison, and revision. However, how different forms of agent collaboration affect hypothesis quality remains an open question. Answering this question requires separating the effects of agents' scientific capabilities from those of their collaboration. A framework must therefore ...
  </details>

- **2026-09-14** — Sushmita Gupta, Sanjay Seetharaman — [On the Hardness of Maximin Share Allocations](http://arxiv.org/abs/2609.15841v1)
  <details><summary>📄 Abstract</summary>
  The maximin share (MMS) guarantee is a central fairness benchmark for allocating indivisible items. Since Kurokawa, Procaccia and Wang [EC'14, JACM'18] showed that exact MMS allocations need not exist, much work has studied existence and computation of approximate MMS allocations. In contrast, a basic complexity question posed more than a decade ago by Bouveret and Lemaître [JAAMAS'16] has remained unresolved: how hard is it to decide whether an exact MMS allocation exists?   For additive valuat...
  </details>

- **2026-09-14** — Hai-Dang Dang, Bao-Yen Pham, Bao Nguyen et al. — [Assembling the CREW: A Collaborative Multi-agent Reinforcement Learning Framework for Automated Related Work Generation](http://arxiv.org/abs/2609.15721v1)
  <details><summary>📄 Abstract</summary>
  Automatic Related Work Generation (RWG) significantly reduces the human time and effort required to author the Related Work Section (RWS) of a research paper. However, prior methods leveraging multi-agent Large Language Models (LLMs) typically rely on a predefined workflow, where each agent is responsible for a specific step in the entire process. This rigid, static inter-agent coordination limits the adaptive collaboration required to synthesize complex scientific literature. To address this li...
  </details>

- **2026-09-14** — Mohamad Najafi, Hongyun Fu, Mathias Brochhausen et al. — [Knowledge-Enriched Structured EHR Features for 30-Day Hospital Readmission Prediction on MIMIC-IV](http://arxiv.org/abs/2609.15713v1)
  <details><summary>📄 Abstract</summary>
  Recent approaches to 30-day hospital readmission prediction rely on pre-trained language models applied to discharge summaries. Although these methods achieve strong performance, they depend on the availability of clinical notes, incur substantial computational costs, and yield representations that lack interpretability. We propose a knowledge-enriched feature representation that augments structured Electronic Health Record (EHR) data with four medical knowledge sources: disease ontology mapping...
  </details>

- **2026-09-14** — Bernard Reber — [New Conditions for Philosophers to Catch the Wave of Citizen Deliberation in the Age of Artificial Intelligence in advance](http://arxiv.org/abs/2609.15707v1)
  <details><summary>📄 Abstract</summary>
  Powerful technologies labeled ``AI''-without sufficient epistemic caution-are already reshaping political and private life, bringing both new dangers and new opportunities for citizen participation. These range from electoral and legislative engagement to the most ambitious form: political co-creation through citizens' assemblies. Large Language Models (LLMs) could support such processes through moderation, translation, facilitation, summarization, and writing assistance. But this potential rema...
  </details>

- **2026-09-14** — Victor H. Chen, Hairui Yu, Stella K. Chung et al. — [CIDERS: Cloud-Edge LLM Collaborative Learning via Accelerating Personalized Bilevel Optimization](http://arxiv.org/abs/2609.15664v1)
  <details><summary>📄 Abstract</summary>
  Amid the rapid advancement of physical-world intelligence, cloud-edge collaborative large language models (LLMs) have emerged as a promising roadmap for practical LLM deployment. However, existing cloud-edge paradigms struggle to balance global consensus with local personalization, which fails to satisfy the need for a unified knowledge foundation on the cloud and domain-specific adaptation at the edge. To address this, we introduce, for the first time, a personalized bilevel optimization framew...
  </details>

- **2026-09-14** — Gwang-Hyeon Yun, Jong-Hoon Park, Bing Hu et al. — [Multi-View Molecular Representation Learning with Hierarchical Graphs and Contextualized Fingerprints](http://arxiv.org/abs/2609.15611v1)
  <details><summary>📄 Abstract</summary>
  Molecular property prediction requires representations that generalize from limited labeled data to structurally novel compounds. Existing molecular pretraining methods often rely on a single view: graph-based approaches model atom-bond topology but provide limited fragment-level supervision, whereas fingerprint descriptors encode chemical patterns but are typically used as fixed auxiliary features. We propose HiFi-Mol, a multi-view framework that separately pretrains a hierarchical graph encode...
  </details>

- **2026-09-14** — Simonetta Liuti, Zaki Panjsheeri, Kemal Tezgin — [Generalized Parton Distributions: Phenomenology, Extraction, and Hadron Imaging](http://arxiv.org/abs/2609.15583v1)
  <details><summary>📄 Abstract</summary>
  Generalized Parton Distributions (GPDs) provide a framework for investigating the correlated momentum and spatial structure of quarks and gluons in hadrons and for accessing fundamental properties such as angular momentum and the QCD energy-momentum tensor. In this review, we discuss the present status of GPD phenomenology, emphasizing the challenges involved in connecting deeply virtual exclusive measurements to the underlying partonic structure. We organize this problem in terms of two success...
  </details>

- **2026-09-14** — Haoting Alexa Yu, Bea Wohl — [Who Chooses the Artwork? Curatorial Agency and Distributed Intent in Botto](http://arxiv.org/abs/2609.15548v1)
  <details><summary>📄 Abstract</summary>
  Botto is often described as a decentralized autonomous artist, but its authorship cannot be located in image generation alone. This paper examines Botto as an agentic curatorial system in which generation, ranking, voting, feedback, and minting form a recursive loop. Drawing on Botto's documentation and prior accounts of the project, we argue that agency in Botto is distributed but asymmetrical: community participants influence artistic direction through voting and governance, while Botto's inte...
  </details>

- **2026-09-14** — Guillermo Herrera Sánchez, Daniel Gradeci, Daniele Ramsay et al. — [The life and death of football team runs: survival of collective modes shapes Lévy-like transport](http://arxiv.org/abs/2609.15541v1)
  <details><summary>📄 Abstract</summary>
  Broad run-length distributions and short-lag superdiffusion have recently been reported in football players and team centroids, prompting a collective-foraging interpretation. The mechanism linking these player- and team-level signatures remains unclear. Using SoccerMon GPS data from 66 tracked team-match records across 62 fixtures in the Norwegian women's top-flight Toppserien, we asked whether player transport is inherited from a translating team mode and what controls the lifetime of that mod...
  </details>

- **2026-09-14** — Doan Dai Nguyen, Ana Bušić — [Stability in stochastic hypergraph matching III: general reneging](http://arxiv.org/abs/2609.15532v1)
  <details><summary>📄 Abstract</summary>
  In many real-life matching problems, waiting agents might abandon before being matched, such as patients deceasing before receiving organs, passengers/drivers cancelling ride requests, or raw materials/intermediary products degrading in production lines. This poses the need for incorporating reneging in stochastic matching models.   In this work, we consider matching models on hypergraphs with batch arrivals and general-weight matchings. Since our model allows fractional weights, we may not be a...
  </details>

- **2026-09-14** — Franck Signe, Hippolyte Pilchen, François Yvon et al. — [To Each Language Its Tokenizer: Modular Tokenizers for Efficient Multilingual LLMs](http://arxiv.org/abs/2609.15528v1)
  <details><summary>📄 Abstract</summary>
  Multilingual Large Language Models (LLMs) traditionally rely on a single vocabulary shared by all supported languages, which can lead to uneven compression across them. Moreover, their large embedding and output matrices increase memory usage and slow inference, notably for small-scale models. It is also wasteful as models are often used for only a subset of languages. To address these issues, we introduce a modular framework for multilingual model training. First, we propose methods to learn la...
  </details>

- **2026-09-14** — Xiang Fang, Feng Guo, Shengzhao Hou et al. — [Canonical analytic realizations of hyperbolic determinantal processes](http://arxiv.org/abs/2609.15506v1)
  <details><summary>📄 Abstract</summary>
  Krishnapur asked whether the invariant hyperbolic determinantal point processes on the disk admit a random analytic zero-set interpretation at noninteger parameters. We construct such a realization for every positive real parameter as the full compact-open limit in distribution of normalized finite Blaschke products. The zeros determine the modulus and normalized analytic shape, leaving one independent uniform phase. We prove exact Möbius covariance and classify all realizations with this covari...
  </details>

- **2026-09-14** — Nikita Markarian — [Harmonic sums and the Galois group of the Mellin-KZ difference equation](http://arxiv.org/abs/2609.15463v1)
  <details><summary>📄 Abstract</summary>
  We identify the universal Galois group of the difference equation obtained by the Mellin transform of the Knizhnik-Zamolodchikov equation with the prounipotent group associated with the transport Hopf algebra of Deligne and Terasoma studied in \cite{Markarian}. At each finite weight, we realize the Picard-Vessiot ring by finite multiple harmonic sums. We also interpret the classical Gamma-corrected projected associator as the comparison between finite and regularized asymptotic fibers in this re...
  </details>

- **2026-09-14** — Xintong Fang, Zhiyuan Fang, Rengan Xie et al. — [ESG: Generating Physically Consistent Dynamic 3D Scenes from Text Descriptions](http://arxiv.org/abs/2609.15392v1)
  <details><summary>📄 Abstract</summary>
  Recent progress in image and 3D scene generation has enabled increasingly realistic static environments, yet most methods remain confined to such static configurations. Generating dynamic scenes from natural language is fundamentally challenging: it requires joint reasoning over scene structure, temporal evolution, and physical feasibility, while ensuring reliable execution in modern physics engines. We present a unified framework for generating physically consistent dynamic 3D scenes from text,...
  </details>

- **2026-09-14** — Jochen Madler — [SlopShape: Identifying AI-Generated Commercial Web Content](http://arxiv.org/abs/2609.15369v1)
  <details><summary>📄 Abstract</summary>
  Word-level detectors identify unedited AI-generated text almost perfectly, but the literature documents their brittleness under rewording, and a word-level score neither characterizes a text nor identifies which AI model wrote it. We ask whether AI-generated text can be identified one level deeper, from structural signatures: how information is presented, in what order, with what evidence, and in what voice. We replicate StoryScope (Russell et al., 2026), which showed such patterns for AI-genera...
  </details>

- **2026-09-14** — Fabian Frank, Warut Suksompong — [Reconfiguration in Fair Division Revisited](http://arxiv.org/abs/2609.15358v1)
  <details><summary>📄 Abstract</summary>
  We revisit reconfiguration in the fair allocation of indivisible goods, where the goal is to transform one fair allocation into another through a sequence of exchanges while preserving fairness at every step. Our focus is on the hierarchy of envy-freeness up to $k$ goods (EF$k$). We show that for any fixed $k$, two EF1 allocations with the same size vector need not admit a reconfiguration path whose intermediate allocations satisfy EF$k$. This impossibility persists even when the two allocations...
  </details>

- **2026-09-14** — Tamanna Kumavat, Georg Brunner, Kyriakos Flouris — [Parameter-Efficient Adaptation of Pretrained Language Models for Time-Series Forecasting](http://arxiv.org/abs/2609.15344v1)
  <details><summary>📄 Abstract</summary>
  We study the adaptation of pretrained language models to univariate time-series forecasting through a parameter-efficient transfer learning framework, with the goal of understanding which design choices drive effective cross-modal transfer. While language models operate on discrete textual tokens, time series consist of continuous numerical observations with temporal dependencies. To bridge this modality gap, we project fixed-length time-series patches directly into the embedding space of a pret...
  </details>

- **2026-09-14** — Luca Müller, Qian Liu, Rolf Drechsler — [LLM-enabled Behavior Driven Development Workflow for Formally Verified Hardware Designs](http://arxiv.org/abs/2609.15318v1)
  <details><summary>📄 Abstract</summary>
  Recently, the use of Large Language Models (LLMs) for different tasks in the Electronic Design Automation (EDA) life-cycle has been studied extensively, but an integrated view is lacking. Specifications are the foundation of this life-cycle, but they suffer from ambiguity when written in natural language, which especially affects the quality of LLM output. Formal specifications mitigate these ambiguities, but they come with their own challenges. On the other hand, Controlled Natural Language (CN...
  </details>

- **2026-09-14** — Yizhou Liu, Fei Tang, Yuchen Yan et al. — [Learning from Reliable Negatives: Confidence-Anchored Test-Time Adaptation for GUI Grounding](http://arxiv.org/abs/2609.15307v1)
  <details><summary>📄 Abstract</summary>
  Graphical User Interface (GUI) grounding is essential for autonomous agents to map natural language instructions to precise screen coordinates. However, existing supervised fine-tuning and reinforcement learning methods are constrained by the high cost of annotation, creating a scalability bottleneck. In this paper, we introduce a label-free test-time training paradigm driven by two key insights: (1) confidence patterns in coordinate tokens are a better indicator than full-sequence confidence, a...
  </details>

- **2026-09-14** — Jugal Garg, Eklavya Sharma, Xiaowei Wu — [Tight Subsidy Bounds for Weighted Proportional Allocation of Mixed Manna](http://arxiv.org/abs/2609.15208v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of fairly allocating m indivisible items among n agents with possibly unequal entitlements in the mixed manna setting, where each item may be perceived as a good or a chore by different agents. We focus on the fundamental fairness notion of proportionality. Since proportional allocations need not exist in this setting, we allow monetary subsidies to restore proportionality while minimizing the total subsidy. When each item's (dis)utility is bounded by 1, a total subsidy of a...
  </details>

- **2026-09-14** — Tong Li, Shuye Ding, Jiachuan Wang et al. — [TEAR: Table Extraction with Attribute Recommendation from Texts via Large Language Models](http://arxiv.org/abs/2609.15205v1)
  <details><summary>📄 Abstract</summary>
  Table extraction from texts is an important task for information systems, and recent approaches that prompt large language models (LLMs) with instructions have drawn great attention for their strong performance. Existing works have assumed the input texts to be table descriptions or specialized documents. However, these efforts have largely overlooked another prevalent category of texts, commonly found in news reports and social media: naturally occurring texts. Extracting tabular information fr...
  </details>

- **2026-09-14** — Mingqian Yu, Wenpeng Zhang, Peilin Zhao — [T-LoopFormer: Token-Level Elastic-Depth Looped Transformers for Latent Reasoning With Dynamic Routing](http://arxiv.org/abs/2609.15160v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers have recently demonstrated strong performance in both reasoning and language tasks by reusing a shared set of parameters across multiple iterations, achieving parameter efficiency without sacrificing representational power. Besides, looped Transformers perform inference directly in the latent space (latent reasoning) to reduce the number of tokens consumed during inference, thereby achieving improved sample efficiency. However, these models typically apply a fixed recursion d...
  </details>

- **2026-09-14** — Yanping Li, Wei Zhou, Yawen Liu et al. — [PACE: Progressive Angular-to-Norm Contrastive Embedding](http://arxiv.org/abs/2609.15152v1)
  <details><summary>📄 Abstract</summary>
  Multimodal embedding models encode heterogeneous inputs into a shared embedding space, enabling efficient similarity computation across modalities and tasks. Most existing methods optimize cosine-based contrastive objectives, which promote stable training but restrict semantic compatibility to angular geometry, precluding embedding norms from serving as an additional semantic signal. However, directly optimizing the more expressive dot-product similarity, which leverages both angular and norm in...
  </details>

- **2026-09-14** — Muchen Li, Leonid Sigal, Renjie Liao — [MoME: Mixture-of-Memory Embeddings for Context-Aware Sparse Lookup](http://arxiv.org/abs/2609.15126v1)
  <details><summary>📄 Abstract</summary>
  Scaling large language models efficiently has motivated sparse capacity mechanisms such as Mixture-of-Experts and, more recently, conditional memory: token-indexed embedding tables that augment the backbone with cheap parametric lookups. Existing memory-embedding methods retrieve via a deterministic function of the surface form, which collapses different contextual senses of the same token (e.g., python the language vs. the animal) into a single fixed entry. We introduce Mixture of Memory Embedd...
  </details>

- **2026-09-14** — Jianhe Zhao, Yanhua Qiu, Zhiyu Zhang et al. — [LG-VLN: A Zero-Shot Vision-and-Language Navigation Framework with LangGraph State Orchestration](http://arxiv.org/abs/2609.15098v1)
  <details><summary>📄 Abstract</summary>
  Continuous-environment vision-and-language navigation (VLN-CE) requires interpreting natural-language instructions in unseen 3D environments and executing continuous low-level actions. Existing methods often depend on LiDAR, panoramic cameras, or extra sensors; separate geometric-mapping and semantic-navigation visual representations can cause long-trajectory spatial-semantic inconsistencies. We propose LG-VLN, a monocular zero-shot framework with shared visual features and LangGraph-based state...
  </details>

- **2026-09-14** — Tomer Ezra, Tamar Garbuz — [Improved Impossibility Bounds for Maximin Share Allocations](http://arxiv.org/abs/2609.15085v1)
  <details><summary>📄 Abstract</summary>
  The maximin share (MMS) is a central fairness benchmark for allocating indivisible items, but it need not be simultaneously attainable even under additive preferences. While extensive work has developed approximation guarantees, quantitative impossibility bounds have received comparatively little attention. We establish improved asymptotic and constant impossibility bounds for both goods and chores.   For every sufficiently large number $n$ of agents, we construct additive goods instances in whi...
  </details>

- **2026-09-14** — Keunyoung Kim, Nojun Kwak — [MoARa: Module-Aware Rank Allocation and Structure-Preserving Decomposition for Low-Rank LLM Pre-training](http://arxiv.org/abs/2609.15037v1)
  <details><summary>📄 Abstract</summary>
  Low-rank gradient projection reduces the optimizer-state memory cost of large language model (LLM) pretraining, but the steps and wall-clock time needed to reach a target quality remain a meaningful axis for improvement. We attribute this to two design choices in existing methods: the projection-rank budget is allocated uniformly across Transformer modules with heterogeneous projection sensitivity, and projecting a raw gradient attenuates its magnitude and direction jointly. We propose MoARa, wh...
  </details>

- **2026-09-14** — Xu Yuqing, Zhou Liguo, Sun Ze et al. — [Horizon-specific Expert Fusion for Photovoltaic Power Forecasting](http://arxiv.org/abs/2609.15035v1)
  <details><summary>📄 Abstract</summary>
  Short-term photovoltaic power forecasting requires models to represent regular solar cycles and weather-driven fluctuations whose importance changes with the forecast horizon. This study develops a hierarchical ensemble that combines temporal neural models, historical analogs, state climatology, and gradient-boosted trees. Solar geometry and numerical weather forecasts describe the expected generation conditions, while horizon-specific convex weights combine complementary predictions. A separate...
  </details>

- **2026-09-14** — Manling Yang, Remco Chang — [Sensemaking as Artifact: Accumulated Influence in AI-Mediated Information Environments](http://arxiv.org/abs/2609.14911v1)
  <details><summary>📄 Abstract</summary>
  Generative AI is changing what can happen after a source artifact reaches its audience. A viewer's interpretation can now be externalized into a derivative artifact, allowing private sensemaking to become part of subsequent communication. Once such a derivative artifact circulates, it can enter subsequent viewers' information environments and shape the conditions under which their later sensemaking occurs. In this paper, we examine how this shift changes visual information communication. We firs...
  </details>

- **2026-09-14** — Haill An, Suhyeon Kim, Minjun Kang et al. — [MedVA: An End-to-End Neuro-Symbolic Agentic System for Medical Volume Visualization](http://arxiv.org/abs/2609.14874v1)
  <details><summary>📄 Abstract</summary>
  Medical volume visualization requires selecting regions of interest (ROIs) and carefully controlling their relative visual emphasis according to a given clinical intent. Implementing these decisions in conventional workflows demands substantial clinical and visualization expertise and often involves trial-and-error optimization. Recent agentic systems have introduced natural-language interaction and autonomous visualization operations but largely rely on MLLM-based inference throughout the workf...
  </details>

- **2026-09-13** — Jiunn-Tsair Chen, Jia-Shung Wang, Chi-Yun Hsieh et al. — [AutoLab: An Internet-Accessible Experimental Platform for Operational World Models in Wireless Networks](http://arxiv.org/abs/2609.14854v1)
  <details><summary>📄 Abstract</summary>
  Operational World Models (OWMs) require structured interaction with the physical world: they must observe operational state, impose controlled actions, measure consequences, preserve experience, and use that experience to support prediction and preventive decision making. This paper presents Autolab, an Internet-accessible experimental platform that provides these physical grounding functions for wireless-network OWMs. A remote researcher can inspect a live test site, reconstruct recent state hi...
  </details>

- **2026-09-13** — Suzannah E McKinney, Phuc Vu, Samuel A Justice et al. — [A primer on evaluation methods for large language models in healthcare](http://arxiv.org/abs/2609.14819v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have a growing range of applications in medicine, and their evaluation is critical for ensuring they provide benefit and not harm. This evaluation can be more challenging than traditional machine learning for many reasons, including probabilistic and open-ended outputs, and behavior that shifts with prompt design and accumulated context. This review covers four key areas of LLM evaluation: principles of study design, statistical methods, capability evaluation and cli...
  </details>

- **2026-09-13** — Roba Hassan, Nahla Aboromi, Naomi Unkelos-Shpigel — [Trust by Design: Trust Calibration Through Non-Advisory Socratic Dialogue in Conversational Agents](http://arxiv.org/abs/2609.14818v1)
  <details><summary>📄 Abstract</summary>
  As conversational AI systems increasingly operate in sensitive domains, the central challenge shifts from usability to trust calibration, ensuring that users rely on systems neither too much nor too little. Systems that provide advice or interpretations risk encouraging inappropriate reliance, particularly when users perceive AI outputs as authoritative. We present CASELy, a conversational agent explicitly designed to limit its own authority through non-advisory Socratic dialogue. The agent asks...
  </details>

- **2026-09-13** — Mingze Yin, Xiaohan Wang, Dian Li et al. — [Func-R1: Incentivizing Mathematical Function Reasoning in Multimodal Large Language Models](http://arxiv.org/abs/2609.14779v1)
  <details><summary>📄 Abstract</summary>
  Performing deliberate mathematical reasoning in visual contexts is a hallmark of advanced Multimodal Large Language Models (MLLMs) and requires a sophisticated synthesis of perceptual grounding and symbolic logic. However, in the realm of mathematical functions, our investigation reveals a critical modality interference phenomenon: even advanced models, while performing textual computational reasoning, tend to disregard or misinterpret essential visual cues. To address this challenge, we propose...
  </details>

- **2026-09-13** — Boqin Yuan, Xiaoyi Gu, Fiona Li et al. — [CALICO: A Human-Centered, Codebook-Aligned System for Annotation](http://arxiv.org/abs/2609.14726v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to scale codebook-based annotation in scientific research, but existing workflows provide limited support for translating domain experts' codebooks into reliable, revisable, and auditable prompts. Prompts are often treated as fixed instructions and hidden from annotators, making it difficult for non-technical domain experts to diagnose and correct model behavior when outputs violate codebook guidelines. In this paper, we present CALICO, a human-centere...
  </details>

- **2026-09-13** — Natarajan Chidambaram, Mauro Dalle Lucca Tosi, Jordi Cabot — [A Two-Dimensional Study of the Model Context Protocol: Publication and Adoption](http://arxiv.org/abs/2609.14721v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP), released by Anthropic in November 2024, standardizes how large language model applications connect to external tools and data sources. Despite MCP's rapid growth, no study has jointly characterized its emergence in the research literature, its adoption on GitHub and the relationship between them. We address this gap with a longitudinal, two-dimensional study of 802 MCP-related publications and 33,319 GitHub repositories. We characterize their growth and identify...
  </details>

- **2026-09-13** — Jahyun Koo, Sunghyeon Woo, Jaeeun Kil et al. — [Carryover Drafting: Recycling Rejected States for Speculative Decoding](http://arxiv.org/abs/2609.14717v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates LLM inference by verifying multiple drafted tokens in parallel, allowing a single target forward pass to accept several tokens. By construction, verification computes representations for both accepted and rejected tokens. Yet, conventional drafters retain only the representations of accepted tokens, leaving the substantial verifier computation spent on rejected tokens effectively wasted. We find that these discarded hidden states generated during target forward r...
  </details>

- **2026-09-13** — Abdalwhab Bakheet Mohamed Abdalwhab, Giovanni Beltrame, David St-Onge — [Learning Multi-Agent Task Assignment and Navigation in the Factory: from Simulation to Real Robots](http://arxiv.org/abs/2609.14567v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has shown considerable promise for robotic decision-making, yet deploying multi-agent RL (MARL) on physical multi-robot systems in industrial environments remains challenging. This paper investigates the real-world applicability of decentralized MARL for multi-robot multi-machine tending. We propose Feature-fusion Multi-Agent Proximal Policy Optimization (FMAPPO), which fuses 2D LiDAR measurements with task-specific state information to enable safe decentralized multi...
  </details>

- **2026-09-13** — Yuchen Guan, Jiaye Liu, Yifei Han et al. — [TATK: Triple-Aware Top-K Learning with Knowledge-Grounded Verification for LLM-based Sequential Recommendation](http://arxiv.org/abs/2609.14565v1)
  <details><summary>📄 Abstract</summary>
  LLM-based sequential recommenders usually cast next-item prediction as text generation, but this interface is poorly matched to full-catalog top-K ranking. We propose TATK, a Triple-Aware framework that couples Top-K Learning (TKL) with Knowledge-Grounded Verification (KGV) for LLM-based sequential recommendation. Top-K Learning combines context-aware metadata-KG prompt grounding with position-aware top-K rewards, aligning training with ranking utility; Knowledge-Grounded Verification then appli...
  </details>

- **2026-09-13** — Toqeer Ali Syed, Ali Akarma, Adeel Ahmad et al. — [OptoAgent: A Trustworthy Multi-Agent Framework for Opportunistic Vision Micro-Screening in Classroom Environments](http://arxiv.org/abs/2609.14514v1)
  <details><summary>📄 Abstract</summary>
  A child with reduced distance vision often does not know that anything is wrong. Children adapt, move closer, and rarely report the difficulty, so the problem can survive years of schooling before an adult notices. School screening addresses part of this, but it runs on a schedule, depends on staffing, and is separated from the classroom moments where the difficulty appears. Smartphone and web-based acuity tests have widened access, yet every one of them still needs somebody to start a test. We ...
  </details>

- **2026-09-13** — Xiaopeng Chu, Jianbo Zhu, Mingmin Jin et al. — [VARG: Value-Aware and Ranking-Aligned Generative Retrieval for Dynamic E-commerce Search](http://arxiv.org/abs/2609.14493v1)
  <details><summary>📄 Abstract</summary>
  Integrating recall and pre-ranking in e-commerce search requires candidate generation to account for relevance, personalization, and business value before final ranking. To this end, we present VARG, a generative retrieval system for Tmall App search that directly admits generated item candidates to the existing final ranker. VARG-ID constructs semantic prefixes using RQ-VAE, enhances search relevance through bidirectional query-item contrastive learning, and combines these prefixes with a value...
  </details>

- **2026-09-13** — Avijit Dasgupta, Shayon Dasgupta, Zakaria Laskar et al. — [PuzzleMate: Benchmarking MLLMs for Egocentric Puzzle Assistance](http://arxiv.org/abs/2609.14473v1)
  <details><summary>📄 Abstract</summary>
  Personal AI assistants hold the potential to evolve from digital interfaces into embodied companions capable of guiding users through complex physical activities. For these assistants to become integral to daily life, they must do more than identify objects; they must provide precise, step-by-step instructions that align with a user's real-time progress. While Multimodal Large Language Models (MLLMs) show promise in general visual understanding, their ability to deliver grounded, sequential guid...
  </details>

- **2026-09-13** — Siddhanth Sridhar, Shreya Chaurasia, Baddela Sai Yaswantha Reddy et al. — [Dynamic Learning Solutions: A System for Personalized Educational Video Generation](http://arxiv.org/abs/2609.14408v1)
  <details><summary>📄 Abstract</summary>
  We present an automated pipeline that converts NCERT textbooks into interactive video explanations that respond directly to user queries. A user uploads a PDF and asks a question; the system then generates a video-based explanation as output, handling both text and visual elements from the PDF for multi-modal retrieval and response generation. The pipeline combines a Retrieval-Augmented Generation (RAG) model with generative multimedia components. The RAG stage is optimized for the structure of ...
  </details>

- **2026-09-13** — Chao Shen, Hongwei Zhen, Junyan Shao et al. — [LLaTSA: Large Language Model-Aligned General-Purpose Transient Stability Analysis](http://arxiv.org/abs/2609.14374v1)
  <details><summary>📄 Abstract</summary>
  Dynamic trajectory prediction has become an important paradigm for data-driven transient stability analysis (TSA), yet most existing predictors remain system-specific and require substantial retraining when network configurations, generation mixes, or state-variable sets change. Uni-TSA introduced a general-purpose TSA framework that combines channel-independent modeling with a pretrained large language model (LLM) predictor. Nevertheless, its application to heterogeneous systems is limited by a...
  </details>

- **2026-09-13** — Hyeon Jeon, Jinwook Seo — [ggaction: A Grammar of Graphical Actions](http://arxiv.org/abs/2609.14353v1)
  <details><summary>📄 Abstract</summary>
  A chart may be declarative; authoring it is not. Visualization grammars often describe charts as finished specifications, whereas people construct them through a sequence of authoring actions. This mismatch can make visualization code difficult for humans to interpret and for machines to generate from human intent. ggaction addresses this gap by modeling the chart authoring process itself. In ggaction, individual authoring actions are abstracted as functions, and the authoring process is express...
  </details>

- **2026-09-13** — Quoc-Huy Trinh, Minh-Van Nguyen, Debesh Jha — [AURA: Unified Multimodal Framework for Conversational Music Editing](http://arxiv.org/abs/2609.14344v1)
  <details><summary>📄 Abstract</summary>
  Instruction-guided music editors typically process each request independently, limiting their ability to support workflows in which users progressively refine a track. We introduce AURA, a unified multimodal framework for conversational music editing. AURA uses a multimodal large language model to interpret the complete dialogue history, an optional image, and reference audio, distilling the editing intent into compact concept tokens. A concept-to-audio module injects these tokens and frame-alig...
  </details>

- **2026-09-13** — Nirmal Kumar Jingar — [Policy-Governed Post-Quantum Migration for Legacy Microservices Using Ephemeral Sidecar Architectures](http://arxiv.org/abs/2609.14286v1)
  <details><summary>📄 Abstract</summary>
  The fast development of quantum computing represents a big risk to classical cryptography that is commonly used in cloud native and microservice based enterprise systems. Traditional cryptographic primitives are closely linked to legacy microservices and it is both intricate, hazardous, and disruptive to straight up migrate to post-quantum cryptography (PQC). In a bid to overcome these issues, this research presents a PolicyGoverned Post-Quantum Migration through Ephemeral Sidecar Architectures ...
  </details>

- **2026-09-13** — Zeyu Dong, Benjamin Wang, Joyee W. Jin — [Route, Don't Fix: Regime-Dependent Decoding Correction and a Trajectory-Gated Router for Reliable Clinical LLM Answer Selection](http://arxiv.org/abs/2609.14825v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are often deemed unsafe for clinical question answering because of their tendency to hallucinate. Retrieval augmentation, fine-tuning, and external verifiers require new infrastructure that clinical governance must approve and may add latency or extra model calls. Inference-time correction uses the model's internal logit signals, but a fixed transformation need not suit every question. A corrector that improves accuracy by about ten percentage points on a truthfulnes...
  </details>

- **2026-09-13** — Hanyu Liu, Qian Li, Yizhu Ding et al. — [REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention](http://arxiv.org/abs/2609.14633v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in data-driven robot manipulation policies have substantially improved task execution and generalization. However, real-world deployment still relies heavily on humans for failure assessment, correction, and environment reset, while models often fail to continually learn from failures and corrective experience. We present REVOLVE (Robot Evolving via Orchestrated Loops, Verification, and Experience), an automated closed-loop framework for evolving robot manipulation with minimal h...
  </details>

- **2026-09-13** — Hang Cheung, Jinniao Qiu — [SCMO: Stochastic Control for Optimization over Probability Measures on Infinite-Dimensional Spaces](http://arxiv.org/abs/2609.14548v1)
  <details><summary>📄 Abstract</summary>
  We study objective-only optimization of possibly nonconvex and nonsmooth functionals over probability measures on a separable Hilbert space, allowing the optimizer to be intrinsically non-Dirac. We introduce SCMO (Stochastic Control Measure Optimizer), a gradient-free particle method derived from entropy regularized stochastic control. After finite-particle and Galerkin approximations, a Cole--Hopf transform represents the optimal feedback as a Gibbs-weighted terminal displacement. SCMO approxim...
  </details>

- **2026-09-13** — Karthekeyan Chandrasekaran, Raymond Jiang, Krishna Kalathur — [A $(p+q)^{O(pq)}$-approximation for $(p, q)$-Flexible Graph Connectivity](http://arxiv.org/abs/2609.14243v1)
  <details><summary>📄 Abstract</summary>
  In the $(p,q)$-Flexible Graph Connectivity problem, the input consists of non-negative integers $p$ and $q$ and a graph $G=(V, E)$ whose edges are classified into safe and unsafe edges with non-negative edge costs. A subgraph H of G is $(p,q)$-Flex-Connected if every non-empty proper subset of vertices has either at least $p$ safe edges or at least $p+q$ total edges crossing it. The goal is to find a minimum cost subset $F\subseteq E$ of edges such that the subgraph $(V, F)$ is $(p,q)$-Flex-Conn...
  </details>

- **2026-09-13** — Qixuan Zai, Randall Berry — [Multi-Agent Reinforcement Learning in Markets with Congestion](http://arxiv.org/abs/2609.14827v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates multi-agent reinforcement learning (MARL) in settings where firms compete for customers using congestible resources. We consider Bertrand competition in which firms compete by announcing prices and customers choose among firms based on both price and congestion. The relationship between price, congestion and the quantity of customers willing to accept service is governed by an unknown inverse demand curve, which firms must learn through experience. Each firm is modeled as...
  </details>

- **2026-09-13** — Utsav Kumar Nareti, Ayush Bansal, Kumari Priya et al. — [From Visual Feedback to Textual Reviews: A Multi-Agent Vision-Language Framework for Image-Grounded Review Assistance](http://arxiv.org/abs/2609.14761v1)
  <details><summary>📄 Abstract</summary>
  Visual feedback in the form of user-uploaded images and videos is becoming increasingly common in e-commerce platforms because it provides authentic evidence of product quality, defects, packaging conditions, and real-world usage. However, visual feedback alone often lacks the contextual explanations and subjective opinions necessary for informed decision-making, while many users provide limited textual feedback due to the effort required to compose detailed reviews. To bridge this gap, we intro...
  </details>

- **2026-09-13** — Dushyant Rajput, Nirdesh Chauhan, Siddharth Kosaraju — [Depth and Scale in the Sub-150M Regime: JugnuLM-53M vs JugnuLM-110M](http://arxiv.org/abs/2609.14715v1)
  <details><summary>📄 Abstract</summary>
  We scale our conventional sub-150M pretraining recipe from 53.5M to 109.7M parameters, holding the method fixed (Qwen3-style decoder with grouped-query attention, RoPE, SwiGLU, RMSNorm, QK-Norm, and a z-loss; FineWeb-Edu data) and changing only the geometry to a deep-and-thin 23-layer x 576-hidden design. The larger model improves across the board -- BLiMP 78.1 -> 81.3, ARC-Easy 51.4 -> 52.5, WikiText-2 byte-perplexity 2.04 -> 1.95 -- and its 81.3% BLiMP essentially matches GPT-X2-125M (81.28) a...
  </details>

- **2026-09-13** — Advait Deshmukh, Nora Benedict, Melanie Walsh et al. — [The Garden of Forking Prompts: How Users Explore Narrative Space in Story Generation](http://arxiv.org/abs/2609.14677v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have changed the way people engage with stories. Drawing on public chatbot logs, we can see that when users generate stories, they iteratively edit their prompts to explore narrative possibilities, adjusting characters, redirecting plots, and swapping fictional universes. As aggregated data, these prompts represent rich traces of creative preference at scale. Yet story generation evaluation benchmarks rely on static, one-shot prompts that cannot capture this explorat...
  </details>

- **2026-09-13** — Ali Abbasian Ardakani, Afshin Mohammadi, Taha Yusuf Kuzan et al. — [From Density to Biopsy Decisions and Malignancy Prediction: A Benchmark Study of Multimodal Large Language Models Against Radiologists in Digital and Contrast-Enhanced Mammography](http://arxiv.org/abs/2609.14676v1)
  <details><summary>📄 Abstract</summary>
  Purpose: To compare four multimodal large language models (MLLMs) with radiologists of varying expertise in breast density assessment, BI-RADS assessment, biopsy candidacy determination, and continuous malignancy probability estimation using digital mammography (DM) and contrast-enhanced mammography (CEM). Methods: This study included 179 women with paired DM/CEM examinations and reference standards. Four MLLMs (ChatGPT-5.2, Gemini-3.1 Pro, Sonnet-4.6, Muse Spark) interpreted images with and wit...
  </details>

- **2026-09-13** — Christian Rembe — [Self-Gravitation of Mode Quanta in a Causal Resonator: One-Loop Finiteness in Linearized Quantum Gravity and the Emergence of the Dark-Energy Scale](http://arxiv.org/abs/2609.14650v1)
  <details><summary>📄 Abstract</summary>
  Perturbative quantum gravity is ultraviolet divergent and, as shown by 't Hooft and Veltman, non-renormalizable. A recent object-relative, Lorentz-invariant weighting of internal electromagnetic modes renders selected one-loop contributions of quantum electrodynamics finite without counterterms. Here that weighting is derived rather than postulated: causality defines a mode resonator bounded by the Hubble radius and re-defined in every inertial frame, and the self-gravitation of each mode quantu...
  </details>

- **2026-09-13** — Christopher Blier-Wong — [Towards foundation models for insurance risk modelling](http://arxiv.org/abs/2609.14576v1)
  <details><summary>📄 Abstract</summary>
  Claim narratives, images and sensor data contain information about insured risks that is difficult to use through existing actuarial models. Foundation models learn patterns from large datasets before being adapted to particular tasks. By turning these high-dimensional sources into variables or numerical representations, they could help insurers use more of the information they already collect, potentially reducing the experience needed to develop each application. For example, a language model ...
  </details>

- **2026-09-13** — Sushan Adhikari — [AlgoRAG: Retrieval-Augmented Generation for Theoretical Computer Science Education -- A Comprehensive Evaluation Framework for Algorithm Analysis and Complexity Theory](http://arxiv.org/abs/2609.14572v1)
  <details><summary>📄 Abstract</summary>
  Teaching abstract theoretical computer science (TCS) concepts such as algorithm analysis and complexity theory is challenging because students must handle formal proofs and asymptotic reasoning that conventional resources rarely explain in an adaptive, on-demand way. We present AlgoRAG, a specialized Retrieval-Augmented Generation (RAG) system that couples a large language model (LLM) with a curated, domain-specific knowledge base to address these challenges. The knowledge base integrates author...
  </details>

- **2026-09-13** — Ziyu Zhang, Mingchen Shao, Wenjie Tian et al. — [Bridging the Modality Gap in Long-Form Clinical Audio: A Comparative Study of Lightweight and Heavyweight End-to-End SOAP Generation](http://arxiv.org/abs/2609.14467v1)
  <details><summary>📄 Abstract</summary>
  Automating clinical documentation from long-form doctor-patient conversations remains challenging for modern audio-language models. While cascaded ASR systems perform well, end-to-end (E2E) models often struggle with information loss and hallucinations on extended audio. For the BeTraC 2026 challenge, the ASLP team presents a fully E2E multimodal system that generates structured SOAP notes directly from audio, bypassing intermediate transcripts. We constructed a 1.41-million-sample multi-task co...
  </details>

- **2026-09-13** — Pallaviram Sure, Chandra Mohan Bhuma — [Vision Language Models for Radiation Patterns to Antenna Parameters](http://arxiv.org/abs/2609.14447v1)
  <details><summary>📄 Abstract</summary>
  Observed radiation patterns often serve as a primary evidence of antenna's behavior, but translating them into meaningful interpretations is a nontrivial and expertise intensive task. This demand necessitates automated pattern interpretation, a diagnosis problem encountered in applications encompassing Radio Frequency (RF) surveillance, non cooperative emitter characterization and Over The Air (OTA) testing. This work addresses the incorporation of Contrastive Language Image Pre training (CLIP) ...
  </details>

- **2026-09-13** — Shengyun Shi, Li Tian, Bo Li — [Dynamical Anisotropy of a Colloidal Glass Under Pressure](http://arxiv.org/abs/2609.14415v1)
  <details><summary>📄 Abstract</summary>
  Pressure is a critical thermodynamic parameter that profoundly influences the physical properties of glasses. Pressure-induced densification and structural transformation endow glasses manufactured under such conditions with exceptional mechanical and optical properties. Although pressure-treated glasses have been characterized by ensemble-averaged methods such as X-ray diffraction and Raman spectroscopy, their microscopic dynamics have rarely been addressed, limiting our understanding of the co...
  </details>

- **2026-09-13** — Praveen Kumar, K. R. Guruprasad, Tushar Sandhan — [Multi-Task Visual Perception Network with LLM Conditioning for Autonomous Navigation](http://arxiv.org/abs/2609.14297v1)
  <details><summary>📄 Abstract</summary>
  Long-term navigation for service robots faces crit- ical challenges like the accumulation of odometry drift and sensor error, which progressively degrade 2D maps and renders traditional path planning algorithms (e.g., A*, RRT*, DiPPer, ViT-A*) ineffective over time. To address this, we propose a user-friendly, interactive framework that eliminates the reliance on globally consistent maps. Our approach integrates visual perception with Large Language Models (LLM) to interpret user commands via te...
  </details>

- **2026-09-13** — Jie Feng, Xiaoyang Wang, Xin Chen et al. — [Recursive Self-Improvement LLM Agents for Inverter Dynamic Model Identification](http://arxiv.org/abs/2609.14260v1)
  <details><summary>📄 Abstract</summary>
  This is a position paper. We demonstrate that recursive self-improvement (RSI) large language model (LLM) agents are a natural search engine for dynamic model identification of inverter-based resources (IBRs) whose internal controls are often proprietary and hidden from grid operators. White-box models provide physical transparency but require vendor disclosure; black-box models avoid this requirement but sacrifice interpretability; and existing grey-box approaches, including sparse and symbolic...
  </details>

- **2026-09-12** — Carmel Kronfeld, Sharva Gogawale, Tetsuro Kobayashi et al. — [A Multi-Stage Agentic Framework for Effective Counter-Narrative Generation and Refinement](http://arxiv.org/abs/2609.14178v1)
  <details><summary>📄 Abstract</summary>
  The rapid diffusion of hate speech and misinformation on social networks challenges democratic societies, since direct suppression efforts may deepen polarization, fuel public distrusts, and strengthen extremist narratives. LLM-driven counter-narratives (CNs) offer a promising way to reduce those risks, yet their effectiveness depends on rhetorical and stylistic choices that remain poorly understood. We present a multi-stage agent-based framework for generating, refining, and evaluating CNs, app...
  </details>

- **2026-09-12** — Tianyu Liu, Fan Zhang, Jiayuan Chen et al. — [RAGCell: Retrieval-Augmented Generation as Supervision for Versatile Single-cell Analysis](http://arxiv.org/abs/2609.14147v1)
  <details><summary>📄 Abstract</summary>
  Single-cell foundation models (scFMs) are transforming computational biology by enabling generalizable, task-agnostic representations for versatile single-cell analysis. Despite their progress in facilitating rapid deployment for downstream tasks, off-the-shelf scFMs still have some overlooked concerns: (I) (Pretraining Cost.) Pretrain-based scFMs necessitate pretraining on a vast volume of cells, rendering it draining resources in applications. (II) (Heterogeneous Gap.) Large Language Models (L...
  </details>

- **2026-09-12** — Bojro Das — [Inherited Heads: Audio language models track speakers with their text backbone's attention, and an attention-mass ranking retrieves a different set](http://arxiv.org/abs/2609.14174v1)
  <details><summary>📄 Abstract</summary>
  Asked to describe what one of six speakers in a recording talks about, audio language models describe the right one on 6 to 16% of trials, below the 16.7% a guess would give. Adding a fixed bias to the attention logits of a hundred heads, under a tenth of the model's and with no training, redirects the description to whichever speaker we choose, on 90.7% to 99.0% of trials. Those heads are largely not specific to audio. Rank the text-only language model an audio model was built from, or a releas...
  </details>

- **2026-09-12** — Saanvi Paturi, Arsen Kenzhebayev, Arham Sethi et al. — [When Tools Get in the Way: The Effect of Unnecessary Tool Availability on LLM Answering](http://arxiv.org/abs/2609.14157v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed with external tools that extend what they can do beyond their own knowledge. Tools help on tasks that need external information, but their availability may also change how a model handles questions that do not need them. Prior work has mostly asked whether models select and use tools appropriately; whether an unnecessary tool changes the correctness of answers has received less attention. We ask whether making a related but unnecessary tool ...
  </details>

- **2026-09-10** — Lohitvel Gopikannan, Shashi Ranjan Kumar, Abhinav Sinha — [Predefined-Time Leaderless Consensus Under Denial-of-Service Attacks](http://arxiv.org/abs/2609.11781v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses predefined-time resilient consensus of leaderless second-order nonlinear multi-agent systems under denial-of-service (DoS) attacks, motivated by coordination requirements in safety-critical applications. The agents are subject to bounded external disturbances and communicate over a strongly connected directed graph whose links are simultaneously disabled during attacks. We develop a switching sliding-mode protocol with the objective of reaching an invariant manifold of posit...
  </details>

- **2026-09-10** — Zhiying Lu — [LoopVAE: Recurrent Depth Across Scales for Visual Tokenization](http://arxiv.org/abs/2609.11516v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical visual tokenizers typically allocate different processing blocks to different spatial scales. We ask how much of this computation can use the same parameters. LoopVAE reuses a scale- and loop-conditioned core within and across scales, while keeping resolution-changing transitions independent. A four-block core executes 28 block applications per encoder or decoder. On ImageNet-256, the 29M-parameter convolutional model reaches 0.28 rFID and 32.54 dB PSNR under an approximately 30-epo...
  </details>

- **2026-09-10** — Benjamin Gruenbaum, Doron Porat, Assaf Natanzon et al. — [Generating a Consistent Enterprise: Synthesis and Reference-Free Evaluation of Multi-System Business Data](http://arxiv.org/abs/2609.11286v1)
  <details><summary>📄 Abstract</summary>
  Synthetic relational data is normally produced by a model trained on a real dataset, and its quality is measured as the distance to that dataset. This paper describes a generator that has no real dataset at either end. Given an industry, a company size, a business model, a set of business applications, and a random seed, it produces a complete fictional enterprise: a workforce, a customer base, sales deals, support tickets, recorded calls, chat messages, and documents, all consistent with one an...
  </details>

- **2026-09-10** — Divyanshu Kumar, Rohith HN, Nitin Aravind Birur et al. — [The Agent Incident Registry: Toward Preventing Repeated AI Agent Failures](http://arxiv.org/abs/2609.11030v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act through tools and delegated authority, but general incident repositories rarely capture the mechanisms needed to compare public failures with agent-security evaluations. We present the Agent Incident Registry (AIR), a source-linked catalog containing \N{} records of agent-related events disclosed from \Yfirst{} through \Ylast{}. Each record includes supporting evidence, a stable identifier, and missingness-aware labels for causal role, disclosure class, mechanism, and ...
  </details>

- **2026-09-10** — Kamran Ayoubi, Bernard Mans, Lata Narayanan — [Online Treasure Hunt in Vertex-Permuted Dynamic Rings](http://arxiv.org/abs/2609.11013v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of treasure hunt by a group of $k \geq 1$ agents in vertex-permuted dynamic rings (VP). In this model, the $n$ vertices remain on a ring but are permuted at each time step. We first show that treasure hunt is impossible for any $k \leq n-3$ agents, if there are no restrictions on the sequence of permutations used in the dynamic ring. We then study the $VP(δ)$ setting, in which for every pair $i, j$ of vertices, the edge $(i, j)$ is guaranteed to appear within $δ$ steps. We s...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 628 |
| prompt-injection | 540 |
| memory-poisoning | 49 |
| tool-use-attack | 135 |
| backdoor | 458 |
| adversarial-attack | 594 |
| privacy-leakage | 4096 |
| steganography | 64 |
| misuse | 1015 |
| red-teaming | 125 |
| vulnerability | 3086 |
| defense | 2895 |
| alignment | 2697 |
| robustness | 2811 |
| watermark | 432 |
| unlearning | 95 |
| agent-safety | 54 |
| benchmark | 65 |
| survey | 346 |
| other | 7645 |

---

📚 **全部 27830 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-16 10:50:21*