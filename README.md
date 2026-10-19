<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-33218-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-19 11:52 ｜ **论文总数 / Total Papers**: 33218（近 30 天 / Recent 30 days: 4897）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 33218 篇论文（含摘要、分类筛选、搜索）/ View all 33218 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 681
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 621
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 55
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 157
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 525
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 638
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4392
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 79
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1189
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 143
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3616
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3493
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3268
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3540
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 619
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 116
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 64
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 68
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 404
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 9550

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4897 篇，完整 33218 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4897 papers from the last 30 days (with date, authors & abstract). For the full list of 33218 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-10-16** — Junchi Liao — [Monitor-Validity Failures: LLM Safety Evidence Paths at Evolving Framework Boundaries](http://arxiv.org/abs/2610.23362v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM applications rely on runtime monitors that inspect tool calls, traces, streams, detector outputs, and verifier inputs. This creates an interface-reliability problem: a framework path may remain operational while policy-relevant evidence never reaches its decision point. In one representative case, a regex detector returned a positive match, but the framework stranded the result before the block decision. This differs from jailbreaks and detector errors because the evidence is already ...
  </details>

- **2026-10-14** — Tianshi Wang, Jingsong Wang, Fengling Li et al. — [Counterfactual Neighborhood Risk Fields: Evidence-Grounded Selective Safety for Vision-Language Models](http://arxiv.org/abs/2610.20679v1)
  <details><summary>📄 Abstract</summary>
  Representation-based safety defenses for vision-language models (VLMs) often learn to separate harmful from benign inputs, but separation alone does not establish what a risk score means or when it should be trusted. We introduce Counterfactual Neighborhood Risk Fields (CNRF), an evidence-grounded framework for selective VLM safety. CNRF constructs context-matched benign-harmful counterfactual pairs, uses their representation differences as capability-related risk directions, and estimates neigh...
  </details>

- **2026-10-14** — Yixin Tan, Chia-Yi Hsu, Jiayang Liu et al. — [Diagnose Before You Refine: Multi-Dimensional Judge Feedback for Query-Efficient Jailbreak Attacks](http://arxiv.org/abs/2610.19971v1)
  <details><summary>📄 Abstract</summary>
  Automated jailbreak attacks rely on evaluation feedback to optimize adversarial prompts, but existing methods often lack fine-grained diagnostic information. We propose Jev-Guided Strategy Bandit (JSB), a query-based jailbreak framework that leverages multi-dimensional probabilistic feedback to guide prompt optimization. JSB combines continuous jailbreak scoring with targeted refinement, strategy switching, and best-state reseeding to balance exploration and refinement. We evaluate JSB on two ha...
  </details>

- **2026-10-14** — Adel Khorramrouz, Yi-Chia Wang, Sharon Levy — [Moral Combat: Exploiting Moral Foundations Theory to Jailbreak LLMs](http://arxiv.org/abs/2610.19587v1)
  <details><summary>📄 Abstract</summary>
  Social psychology has long described how people can be persuaded to interpret a harmful act as moral. Recent research suggests that Large Language Models (LLMs) echo aspects of human psychology, from cognitive biases to social conformity. This raises a question with direct safety implications: can LLMs be moralized to bypass safety guardrails? We answer this question with a multi-agent framework grounded in Moral Foundations Theory (MFT). Given a harmful request that is initially refused, our ag...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 5 papers

- **2026-10-14** — Qianlong Lan, Anuj Kaul, Vinothini Pandurangan et al. — [From Detection to Decision: Calibration and Deferral for Prompt-Injection Detection](http://arxiv.org/abs/2610.20907v1)
  <details><summary>📄 Abstract</summary>
  Prompt-injection defenses are commonly evaluated as binary detectors, although deployed LLM applications must make operational decisions about whether to allow, block, or escalate potentially malicious inputs. Recent probabilistic decision models aim to support such decisions through calibrated confidence estimates, but their reliability under distribution shift remains uncertain. We evaluate a native probabilistic decision model (Jev), two Llama Prompt Guard 2 classifiers (22M and 86M), and an ...
  </details>

- **2026-10-14** — Thuy Dung Nguyen, Jingyi Guo, Rana Seda Dubauskas et al. — [INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems](http://arxiv.org/abs/2610.20776v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents increasingly execute long-horizon, end-to-end workflows involving shell commands, code modification, dependency installation, and interaction with remote services. This growing autonomy expands their exposure to indirect prompt injection (IPI), where adversarial instructions embedded in external content are interpreted as legitimate task directives. Existing evaluations, however, often focus on isolated malicious strings, single-step tool calls, or narrowly scoped agent configur...
  </details>

- **2026-10-14** — Min-Young Yu — [Policy-Verified Self-Training: Learning Agent Compliance from Verifiable Policy Rewards](http://arxiv.org/abs/2610.19372v1)
  <details><summary>📄 Abstract</summary>
  Runtime policy verifiers can prevent agents from executing disallowed actions, but their decisions are typically used only for enforcement and discarded afterward. We ask whether these decisions can instead become verifiable policy rewards for training the agents they guard. We introduce Policy-Verified Self-Training (PVST), a post-training paradigm in which an agent generates its own interaction trajectories and an executable policy verifier, here a deterministic gate compiled from a written po...
  </details>

- **2026-10-14** — Sarthak Gupta, Priyanka Tembey — [Are You Reading the Right Thing? Rethinking Internal Signals for Prompt-Injection Detection](http://arxiv.org/abs/2610.19452v1)
  <details><summary>📄 Abstract</summary>
  Several recent studies propose detecting prompt injections from a language model's internal state. However, these methods do not measure a single security property. Residual-stream probes, attention scores, role projections, exposure probes, and concept readouts may capture injection presence, recognition, information routing, or behavioral influence. It is therefore unclear what differences in prompt-injection detection performance reveal about the internal signals these methods read. We study ...
  </details>

- **2026-10-14** — Chenxu Wang, Xiaoyu Wen, Han Qi et al. — [AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety](http://arxiv.org/abs/2610.19422v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents accomplish complex tasks through multi-turn interactions with external tools. However, malicious content embedded in user queries, tool descriptions, or environment observations can manipulate their decisions and induce unsafe actions. Adversarial co-evolution has emerged as an effective approach to strengthening LLM safety, but existing work primarily focuses on language-level safety or indirect prompt injection in web tasks. In this paper, we introduce AgentSa...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-10-15** — Ali Mohammadi Shanghooshabad — [FAOPs: Normal Forms and an Algebra for AI Agent Workflows](http://arxiv.org/abs/2610.22061v1)
  <details><summary>📄 Abstract</summary>
  Organizations increasingly encode operational procedures as multi-step agent skills, here called Agent Operating Procedures (AOPs), that must be traceable, auditable, reproducible, access-controlled, and bounded in time and cost, requirements that regulated sectors make mandatory. Yet AOPs are typically kept as coarse-grained files, in which steps bundle actions, copied procedures drift apart, any step may reach any tool, and refactoring goes unchecked. We present Functional Agent Operating Proc...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 11 papers

- **2026-10-16** — Xiaohang Yu, Hejia Geng, William Knottenbelt — [ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics](http://arxiv.org/abs/2610.23656v1)
  <details><summary>📄 Abstract</summary>
  Blockchain forensics is adversarial and open-ended: money launderers split, swap, and bridge funds, cut their trail at mixers or custodial services, and change tactics from one incident to the next. Investigators must keep adapting their tracing in response. Yet the immutability of public ledgers preserves every recorded movement in public view, making much of the investigation independently verifiable. We introduce ABF-Bench, an interactive benchmark that makes evidence-backed fund tracing a ve...
  </details>

- **2026-10-16** — Jiawei Yu, Syed Irfan Ali Meerza, Yi Wu et al. — [SemPurify: Semantics-Aware Data Purification for Black-box Backdoor Defense](http://arxiv.org/abs/2610.23589v1)
  <details><summary>📄 Abstract</summary>
  Backdoor attacks have emerged as a critical security threat in machine learning, where adversaries embed triggers within poisoned training samples to manipulate a model's predictions on targeted inputs while leaving its general behavior unaffected. This stealthy nature makes backdoor attacks difficult to detect, as the model functions normally until activated by a specific malicious trigger. Current purification-based defenses use image transformations (e.g., blurring) to disrupt trigger pattern...
  </details>

- **2026-10-16** — Munshi Md Arafat Hussain, Md. Abdur Rahman, Md Saeed Siddik — [An Interactive GraphRAG Workspace for Reifying, Auditing, and Steering Conversational AI Memories](http://arxiv.org/abs/2610.23559v1)
  <details><summary>📄 Abstract</summary>
  Conversational Large Language Models (LLMs) are widely employed in software engineering for code generation, debugging, and architectural design. However, as developers engage in multi-session development tasks, technical knowledge becomes siloed in isolated, linear chat histories. Reusing context across sessions leads to three critical challenges: (1) flat-vector retrieval fails to traverse multi-hop relational dependencies between distant architectural decisions; (2) temporal drift in software...
  </details>

- **2026-10-16** — Gabriel Hortea, Simon Pietro Romano, Juan Tapiador et al. — [From Billion-Scale to Million-Scale Language Models: Operational Capabilities for Embedded Post-Exploitation](http://arxiv.org/abs/2610.23534v1)
  <details><summary>📄 Abstract</summary>
  Small Language Models (SLMs) are increasingly attractive for resource-constrained environments due to their low computational footprint. These characteristics also make them candidates for future autonomous malware, where connectivity, latency, privacy, or operational constraints may preclude cloud-based inference. Yet the ability of ultra-compact models to support malware during post-exploitation remains poorly understood.   We systematically evaluate seven open-source SLMs (20M-1.5B parameters...
  </details>

- **2026-10-15** — Yuan-Chen Chang, Niklas Herbster, Gauthier Gidel et al. — [CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM Honesty](http://arxiv.org/abs/2610.22292v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are becoming prevalent in scenarios where honesty is critical. However, despite alignment training, these models still exhibit dishonest behaviour, such as outputting claims that contradict some knowledge or are not supported by what is accessible in context. We introduce Continuous Adversarial Training for Consistent Honesty (CATCH), inspired by a method originally developed to robustly refuse harmful queries. CATCH trains the model towards an honest answer and away...
  </details>

- **2026-10-15** — Jihun Kim, Javad Lavaei — [Defense Filters for Robust Learning of Partially Observed Dynamical Systems](http://arxiv.org/abs/2610.21935v1)
  <details><summary>📄 Abstract</summary>
  Robust estimation of unknown system dynamics from partial observations under attack is a core challenge in learning for control, increasingly critical in multi-agent networks subject to adversarial data poisoning. Existing methods either require highly restrictive assumptions on the adversary or yield weak error bounds. In this paper, we consider identifying partially observed linear dynamical systems subject to adversarial attacks with an attack probability $p < 0.5$ at each time. We propose a ...
  </details>

- **2026-10-15** — Vasileios Perifanis, Nikolaos Pavlidis — [Federated Art Chase: Privacy Leakage and Data Poisoning in Federated Fine-Tuning](http://arxiv.org/abs/2610.21547v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) is increasingly used to adapt a pretrained, centrally fine-tuned model to data that remain on user devices, beyond training a model from scratch. In this report, prepared for the 4th Federated Machine Learning International Summer School, we study the privacy and integrity of this approach with a reproducible pipeline. An ImageNet-pretrained MobileNetV4-Conv-Small model is fine-tuned centrally on ten Quick, Draw! classes (97.50% test accuracy) and then adapted with head-o...
  </details>

- **2026-10-15** — Yufei Chen, Yao Wang, Haibin Zhang — [Poisoning the Neighborhood: A Topology-Aware Topic-Level Attack on Large-Scale HNSW-based RAG Systems](http://arxiv.org/abs/2610.21464v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) mitigates hallucinations and knowledge staleness in large language models using external knowledge. However, ingestion from public and third-party sources exposes RAG systems to poisoning attacks. Existing attacks are designed and evaluated under exact retrieval, where poisoned documents participate in global ranking. Deployment-scale systems instead rely on approximate nearest-neighbor (ANN) indexes such as hierarchical navigable small world (HNSW), where li...
  </details>

- **2026-10-15** — Charalampos Koilakos, Kimon-Antonios Provatas, Michail Patsakis et al. — [Poisoning the corpora of protein design systems during pre-training and retrieval](http://arxiv.org/abs/2610.21200v1)
  <details><summary>📄 Abstract</summary>
  Protein foundation models increasingly support the generation of novel biological sequences, yet their reliance on large public datasets creates opportunities for adversarial manipulation of the material they learn from and retrieve. We investigate two data-only poisoning attacks against protein design systems, targeting the pre-training corpus of autoregressive protein language models and the retrieval corpus of a text-guided protein generator. For the first, we pre-trained ProtGPT2 and ProGen2...
  </details>

- **2026-10-14** — Yinzhen Huang, Jiahe Xie, Yitong Sun et al. — [Beyond Static Cues: Unified Dynamic Detection of MLLM Backdoors via Dual-Flow Trajectory Analysis](http://arxiv.org/abs/2610.20319v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) are increasingly deployed in safety-critical domains, yet their susceptibility to backdoor attacks remains a formidable challenge. While existing defenses have evolved from visual-centric patch cues to unsupervised internal attention statistics, they are fundamentally constrained by a reliance on static snapshots and attack-specific heuristics. Given the intricate interplay between dual modalities, the vast design space for multimodal triggers allows dive...
  </details>

- **2026-10-14** — Hui Zhang, Yujia Zeng, Yuhao Xin — [Learning When to Trust Medical Knowledge: Regression-Safe Routing for Clinical Reasoning](http://arxiv.org/abs/2610.19663v1)
  <details><summary>📄 Abstract</summary>
  Clinical reasoning LLMs need external medical knowledge, but retrieved evidence and reasoning chains can be outdated, poisoned, or hallucinated. Harmful knowledge can cause regression: changing a correct answer into an incorrect one. We construct a medical knowledge-poisoning benchmark covering retrieved evidence and reasoning chains, with seven attack families filtered by a three-judge "subtle-but-wrong" vote and paired clean exams that separate poisoning effects from question difficulty. No fi...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-10-16** — Wenda Li, Tongya Zheng, Shunyu Liu et al. — [S-GAP: Stealthy Graph Attack Primitives for Graph Large Language Models](http://arxiv.org/abs/2610.23465v1)
  <details><summary>📄 Abstract</summary>
  Graph Large Language Models (GraphLLMs) enable powerful semantic understanding and reasoning over Text-Attributed Graphs (TAGs), while their semantic reasoning may exhibit vulnerabilities to perturbations in node text and graph structure under adversarial attack evaluation. Existing attacks typically construct textual and structural perturbations in separate stages guided by distinct realization intents. However, this separation results in attack-intent fragmentation, causing semantic incoherenc...
  </details>

- **2026-10-14** — B. Nancharaiah, Ramakrishna Kolikipogu, J. Sulthan Alikhan et al. — [Hybrid DeepXAI Fusion Network for Interpretable Big Data Analytics and Secure Cloud Decision-Making Systems](http://arxiv.org/abs/2610.20661v1)
  <details><summary>📄 Abstract</summary>
  Big data analytics supports modern intelligent systems, but model complexity and limited transparency can undermine interpretability, trust, and security in decision-making. This paper presents the Hybrid DeepXAI Fusion Network, a deep learning framework that integrates temporal, relational, and contextual features with explainable artificial intelligence (XAI) mechanisms. The architecture combines one-dimensional convolutional neural networks (1D-CNNs) for temporal feature extraction, Transform...
  </details>

- **2026-10-14** — Yixin Wu, Mingjie Li, Yun Shen et al. — [GeoCloak: An Agentic Framework for Semantics-Preserving Geolocation Privacy via Peripheral Clue Manipulation](http://arxiv.org/abs/2610.20055v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of large vision language models (LVLMs) has made geolocation inference from images highly accurate and accessible. This poses serious privacy risks: a passive adversary with black-box LVLM access can infer a user's location from a single photo with no metadata. Existing protection methods rely almost exclusively on adversarial perturbation, which introduces perceptible visual artifacts and utility degradation. We identify the visual-geolocation asymmetry: geolocation-decisi...
  </details>

- **2026-10-14** — Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al. — [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](http://arxiv.org/abs/2610.20609v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructions. However, this open-ended interface exposes a new vulnerability surface: an inattentive driver may issue instructions that are unsafe given the current scene, and a malicious user may issue dangerous ones on purpose. We present the first benchmark s...
  </details>

- **2026-10-14** — Yi Chen Liu, Syed Irfan Ali Meerza, Jiawei Yu et al. — [MUSEBENCH: A Benchmark for AI-Generated Music Detection and Artifact Analysis](http://arxiv.org/abs/2610.20310v1)
  <details><summary>📄 Abstract</summary>
  Advances in generative AI have made it possible to produce music that is nearly indistinguishable from human compositions, raising the question of whether such works can be reliably distinguished from human compositions. We present MUSEBENCH, a large-scale benchmark for AI-generated music detection and artifact analysis, comprising over 361K tracks. The dataset includes human compositions, stylistically matched music generated by ten state-of-the-art open-source and commercial models, such as Su...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 24 papers

- **2026-10-16** — Lewen Yan, Yanxu Zhu, Jie Zhang et al. — [OwlSight: A Panoramic Monitor for Chain-of-Thought Reasoning](http://arxiv.org/abs/2610.23670v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) monitoring offers actionable evidence for oversight AI systems, with the potential to enable early detection and intervention. However, existing approaches are focused on specific tasks, whereas the regulation of AI, particularly reasoning models, requires monitoring a broader range of tasks. We introduce Factor for CoT monitoring, a strategy that supports customizing monitoring requirements in the prompt, which enables a single monitor to cover different tasks by relying ...
  </details>

- **2026-10-16** — Weiyang Jin, Jiwen Yu, Sihan Xu et al. — [Execution Before Memory: Diagnosing Memory Failures in Video World Models](http://arxiv.org/abs/2610.23542v1)
  <details><summary>📄 Abstract</summary>
  A memory test for a video world model should say whether the scene was set, whether the asked change was carried out, and whether the last frame shows the result. Current tests fold these into one number, so a low score is easy to read as forgetting. When the change is not carried out, the hidden state transition cannot appear, so the test is not really a test of memory. We introduce MIST, an evaluation that separates the change from the memory it should leave behind. The model first sets the sc...
  </details>

- **2026-10-15** — Dixi Yao, Tahseen Rabbani, Tian Li — [Private Retrieval Augmented Generation via Random Projection](http://arxiv.org/abs/2610.22297v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) enhances the capabilities of large language models (LLMs) by querying external structured knowledge. However, it can also introduce privacy risks by leaking sensitive information from the retrieval datastore. We propose a simple method to preserve datastore privacy in RAG systems via random projection. By applying the same projection to both datastore embeddings and query embeddings, our method provably preserves semantic similarity between queries and retrie...
  </details>

- **2026-10-15** — Kshitij Mishra, Abhijith Sharma, Nils Lukas et al. — [PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents](http://arxiv.org/abs/2610.22124v1)
  <details><summary>📄 Abstract</summary>
  Modern agentic systems extend language models with external tools, enabling them to complete complex tasks through multi-turn interactions. As these agents are deployed in consequential settings, they are often constrained by policies governing pricing, privacy, confirmation, safety, and other requirements. However, existing evaluation methods leave a critical gap: capability benchmarks measure what agents can accomplish, while content-safety red-teaming measures harmful generations, but neither...
  </details>

- **2026-10-15** — Tyler Lizzo, Larry Heck — [Behavioral Forgetting Is Not Privacy in Machine Unlearning](http://arxiv.org/abs/2610.21799v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning aims to remove targeted information from large language models, but existing evaluations often measure forgetting only on a designated benchmark distribution. We argue that such behavioral forgetting is an insufficient standard for privacy-oriented unlearning, and that evaluation should instead test whether forgetting persists across the access paths through which the same information may be recovered. We demonstrate this with a controlled case study of cross-lingual querying:...
  </details>

- **2026-10-15** — Linda Beková, Rodrigo Alves — [Encoded but Exposed: Language Embeddings can Reveal More Than They Should in Recommender Systems](http://arxiv.org/abs/2610.21713v1)
  <details><summary>📄 Abstract</summary>
  Language embeddings are increasingly used in recommenders to represent item content, but their privacy risks remain poorly understood. We study whether item embeddings can reveal item identities when an adversary has access to auxiliary item text from external sources. We show that a simple cosine-similarity attack can recover item identities with high mean reciprocal rank across language models and candidate-set settings on two real-world datasets. Leakage is strongest when the adversary's part...
  </details>

- **2026-10-15** — Zhiyuan Wang, Yuezhi Zhou, Ziqi Zhang et al. — [BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition](http://arxiv.org/abs/2610.21565v1)
  <details><summary>📄 Abstract</summary>
  On-device deployment of large language models (LLMs) is increasingly adopted due to latency and privacy requirements, but exposes proprietary models to reverse engineering and intellectual property theft. Trusted Execution Environments (TEEs) provide hardware-enforced isolation for on-device inference, yet most TEE-based parameter obfuscation relies on unilateral matrix transformations that obfuscate only output side. We identify a vulnerability in this design, termed the \emph{Solution Determin...
  </details>

- **2026-10-15** — Song Bian, Hyeongmin Choe, Jiseung Kim et al. — [Reaction Attack on CKKS Deployments with Asymptotically Optimal Query Complexity](http://arxiv.org/abs/2610.21127v1)
  <details><summary>📄 Abstract</summary>
  We study a protocol-level reaction leakage in CKKS deployments where public coefficient-to-slot (C2S) evaluation keys are combined with a client's 1-bit validity response. Under this deployment surface, a malicious evaluator can recover a ternary secret key using asymptotically optimal $O(H)$ reaction queries, where $H$ is the entropy of the secret key.   The attack does not break RLWE or CKKS IND-CPA security. Instead, it exploits the interaction between client-side validity reactions and publi...
  </details>

- **2026-10-15** — Vinny Davies, Craig Alexander, Jennifer Gaskell et al. — [A Framework for Teaching the Responsible and Effective Use of Generative AI in Statistics and Data Science](http://arxiv.org/abs/2610.21663v1)
  <details><summary>📄 Abstract</summary>
  The rapid rise of generative artificial intelligence (AI) following the public release of tools such as ChatGPT has begun to reshape how students engage with coding, statistical analysis, and written communication in higher education. Growing use of conversational AI systems creates opportunities for learning alongside challenges around reliability, transparency, privacy, and appropriate academic and professional practice, highlighting the need for structured education in their responsible use. ...
  </details>

- **2026-10-15** — Yufan Zhu, Yangfan Jiang, Yang Fei et al. — [QuasiLeak-Bench: Evaluating LLM-Based Privacy Detectors on Policy-Conditioned Quasi-Evidence Group Recovery](http://arxiv.org/abs/2610.21333v1)
  <details><summary>📄 Abstract</summary>
  Natural language messages often contain quasi-identifiers that are weak in isolation but can jointly reveal an individual's private attributes. We call such a jointly revealing set of cues a quasi-evidence group. Existing privacy benchmarks focus on explicit identifiers, attribute inference, or task-driven disclosures, leaving inference from quasi-evidence groups largely unmeasured. In practice, whether exposing such a quasi-evidence group violates privacy also depends on sender-specified disclo...
  </details>

- **2026-10-15** — Jie Li, Youming Tao, Bowei He et al. — [Not All Change Is Damage: Update-Matched Unlearning for Large Language Models](http://arxiv.org/abs/2610.21230v1)
  <details><summary>📄 Abstract</summary>
  Unlearning aims to remove selected knowledge from large language models to mitigate privacy and safety risks while preserving useful capabilities. For models that continue to be fine-tuned after release, this goal is insufficient: they must also resist relearning the deleted knowledge while preserving plasticity, the ability to learn new tasks. Existing defenses train against simulated relearning while trying to preserve useful capabilities, but low relearning alone cannot distinguish selective ...
  </details>

- **2026-10-15** — Tanay Arora, Cong Liu — [AutoOnboarder: Autonomously Onboarding LLM Agents](http://arxiv.org/abs/2610.21218v1)
  <details><summary>📄 Abstract</summary>
  Agentic large language models have been documented to lose reasoning capability when placed inside a harness, the software that mediates their observations and actions. To reconcile these losses, we introduce AutoOnboarder, an autonomous system that adapts an agent to a task the way a trainer onboards a new employee. It places the agent under the supervision of an intelligent ``Onboarder'' coding agent, which iteratively tailors its foundation model, prompt, and harness source code to simultaneo...
  </details>

- **2026-10-15** — Aisvarya Adeseye, Adeyemi Adeseye, Mohammad Tahir et al. — [CARE-SD: Explainable Reasoning Architecture for Local SLM Self-Disclosure Analysis in Textual Data](http://arxiv.org/abs/2610.21151v1)
  <details><summary>📄 Abstract</summary>
  Cybersecurity interviews uncover critical security experiences, behaviors, and privacy concerns often not fully captured by conventional technical assessments. Consequently, identifying genuine self-disclosures is challenging because statements are context-dependent, categories overlap, and automated interpretations may introduce unsupported claims. Locally deployed Small Language Models (SLMs) protect sensitive participant data by keeping processing within controlled environments, but their lim...
  </details>

- **2026-10-15** — Mingjin Zhang, Jiannong Cao, Tao Wu et al. — [Efficient KV Cache Migration for Geo-Distributed LLM Inference in Collaborative Edge Computing](http://arxiv.org/abs/2610.22172v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown exceptional capabilities but rely heavily on centralized cloud GPU clusters, leading to high bandwidth costs, latency, and privacy issues. Edge computing offers a solution by deploying LLMs closer to users on edge servers, yet single edge servers often cannot meet LLMs' heavy computational demands. Collaborative Edge Computing (CEC) addresses this challenge by integrating resources of multiple geo-distributed heterogeneous edge servers, which jointly host ...
  </details>

- **2026-10-15** — Yuichiro Minato — [Bubble-Sort Exchange Networks: Symmetry Selection Rules and Language-Model Distillation on Exchange-Only Spin Chains](http://arxiv.org/abs/2610.22093v1)
  <details><summary>📄 Abstract</summary>
  On a chain of exchange-coupled quantum dots a Heisenberg exchange pulse of area pi is a SWAP, so the parallel bubble-sort SWAP network of superconducting chains is native to exchange-only (EO) spin qubits, and any other pulse area fuses routing with an entangling interaction. We build a variational "bubble-sort exchange network" (odd-even transposition, one parameter per pulse) and study it as a Born machine read out by Pauli spin blockade. Exchange conserves total spin, so the reachable readout...
  </details>

- **2026-10-15** — Zhanli Li, Zeyuan Xu, Chaoxu Pang et al. — [Data World: Scaling Data Environments from Scratch](http://arxiv.org/abs/2610.21656v1)
  <details><summary>📄 Abstract</summary>
  Data agents use code to process heterogeneous files and derive analytical insights. Scaling their training faces costly environment curation, privacy and intellectual-property restrictions, and difficulty verifying open-ended findings without known generative truth. Our core insight is to specify the world behind the files before generating the files themselves. We introduce Data World, a multi-agent engine that synthesizes environments, tasks, and rubrics from explicit mechanisms. Independent a...
  </details>

- **2026-10-15** — Douglas Leith — [Decoding What iOS Location Services Send to Apple: An LLM Is an Unreliable Analyst but a Useful Toolmaker](http://arxiv.org/abs/2610.21597v1)
  <details><summary>📄 Abstract</summary>
  Reverse engineering the data formats used by mobile software is skilled and slow, and using AI to assist with it is attractive. We evaluate this for the protobuf messages that an iPhone sends to Apple's location services. Working from Apple's binaries, we use two frontier models (Claude Opus 4.8, Codex GPT Sol 5.6) to reconstruct the schemas of protobufs observed in network traffic. The great majority of the schemas contain substantial errors, and these are hard to detect because the schemas are...
  </details>

- **2026-10-15** — Boxun Lan, Jiamei Li, Weijian Li et al. — [FedSkillGit: Federated Skill Evolution via Version Control](http://arxiv.org/abs/2610.21348v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents can improve their capabilities by evolving reusable natural-language skills from execution experience. In real-world deployments, this experience is distributed across data owners who cannot pool their raw data, which motivates federated skill evolution. The natural first design lets each client evolve the whole skill document and upload the result for server-side aggregation. That design is poorly matched to skill evolution for three reasons. An evolved document can ...
  </details>

- **2026-10-15** — Zhiyuan Zhang — [From One Query to Many: A Critical Survey of Privacy Accounting in RAG](http://arxiv.org/abs/2610.21245v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) enables large language models to leverage external knowledge but introduces privacy risks when the retrieved corpus contains sensitive information. Differential privacy (DP) offers formal protection, yet interpreting and comparing privacy guarantees across existing DP-RAG methods remains challenging. In particular, a privacy budget reported for a single response does not directly characterize privacy loss over repeated queries, and even identical values of $\...
  </details>

- **2026-10-15** — Abdul Raheem Shahzad, Jinxin Chen, Ming Zhang et al. — [Predicting Live Birth After Fresh Embryo Transfer in IVF/ICSI: Differential ICM/Trophectoderm Morphology Encoding and a Hybrid Attention--Logistic Regression Ensemble](http://arxiv.org/abs/2610.21134v1)
  <details><summary>📄 Abstract</summary>
  Predicting live birth before fresh embryo transfer could support shared decision-making in IVF/ICSI, but routine clinical data are small, heterogeneous, and contain pathway-dependent variables prone to outcome leakage. We aimed to construct a curated single-centre IVF/ICSI dataset and develop a prediction model suited to small tabular clinical data. \textit{Materials and Methods:} We assembled 616 fresh embryo-transfer cycles (251 live birth, 365 non-live birth) with clinical, laboratory, and em...
  </details>

- **2026-10-14** — Jin-Jia Zheng, Vincent S. Tseng — [Graph-Enhanced Disease Trajectory Discovery and Temporal Endpoint Forecasting from Longitudinal Electronic Health Records](http://arxiv.org/abs/2610.20502v1)
  <details><summary>📄 Abstract</summary>
  Longitudinal electronic health records (EHRs) can reveal disease-progression structure, while useful forecasting requires leakage-controlled discovery, censor-aware outcomes, and inspectable trajectory evidence. We developed a graph-enhanced framework in MIMIC-IV v3.1 that splits patients before graph construction, learns train-only consecutive-admission transitions, and freezes endpoint-specific branching-motif policies selected on validation data. The final catalog contained 99,527 motifs, and...
  </details>

- **2026-10-14** — Julian Ganz, David Knothe, David Oswald et al. — [FreeSBee: A Constant-Time Compilation Pipeline](http://arxiv.org/abs/2610.20171v1)
  <details><summary>📄 Abstract</summary>
  Constant-time execution is an important security property, especially for IoT devices, that prevents the leakage of sensitive information over timing side-channels. However, achieving constant-time execution is very hard when going down to the cycle level, at least on realistic devices. A lot of research is concerned with producing tools that either determine whether code is constant-time or that ensure it is compiled into a constant-time binary, with various degrees of accuracy. In this work, w...
  </details>

- **2026-10-14** — Zeinab Elkhatib, Kamrul Hasan, Ali Sekmen et al. — [AutoPoly-HE: Autonomous Design of Polynomial Activations for Privacy-Preserving Encrypted Inference](http://arxiv.org/abs/2610.19325v1)
  <details><summary>📄 Abstract</summary>
  Privacy-preserving machine learning has become critical for deploying artificial intelligence in sensitive domains such as healthcare, finance, and infrastructure monitoring. Homomorphic encryption (HE) enables secure inference on encrypted data. Despite its advantages, HE is not compatible with nonlinear activation functions found in machine learning models. Existing methods mitigate this problem by manually designing polynomial approximations for these activation functions. However, these func...
  </details>

- **2026-10-14** — Souvik Das, Ariful Azad, Nitesh Saxena — [A Graph-Based Analysis of Comparability, Scale, and Attribution in Private Transformer Inference](http://arxiv.org/abs/2610.19607v1)
  <details><summary>📄 Abstract</summary>
  Rising privacy concerns around large language models have accelerated research in private Transformer inference (PTI). Synthesizing the empirical claims in this line of research, however, is hindered by multi-dimensional cryptographic progress and inconsistent evaluation contracts. In this work, we systematize the field by constructing an empirical graph of 62 PTI systems, mapping system attributes to node features and evaluation compatibility to edges. A three-tiered analysis of this graph illu...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 2 papers

- **2026-10-15** — Kaue Lopes de Moraes, Rodrigo De-Losso — [Algorithmic Collusion Without Deterrence: Auditing the Punishment Mechanism in Q-Learning Pricing Agents](http://arxiv.org/abs/2610.21867v1)
  <details><summary>📄 Abstract</summary>
  Independent tabular Q-learning agents repricing in a simulated Bertrand duopoly converge to supracompetitive prices, and the seminal evidence attributes this to a learned reward-punishment scheme: undercut your rival and it retaliates, so deviation never pays. This mechanistic reading is what turns high prices into a cartel, and into a regulatory target. We replicate the environment of Calvano et al. (2020) and confirm their impulse-response pattern within co-trained pairs. We then audit the pat...
  </details>

- **2026-10-14** — Ravan Nazaraliyev, Yicheng Zhang, Nael Abu-Ghazaleh — [PAGE404: Breaking GPU Isolation Through Hardware-assisted Page Migration](http://arxiv.org/abs/2610.20962v1)
  <details><summary>📄 Abstract</summary>
  NVIDIA's Grace Hopper (GH200) superchip represents a new generation of heterogeneous computing, tightly integrating a 72-core Arm-based CPU with a Hopper GPU on a single module via a high-bandwidth, cache-coherent interconnect. By eliminating the conventional PCIe bottleneck for CPU-GPU data movement, this design establishes a unified memory domain that scales to the capacities demanded by generative AI and high-performance computing (HPC) workloads. The architecture also introduces hardware-ass...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 19 papers

- **2026-10-16** — Md Asif Uddin, Jannatul Ferdous, Asif Islam et al. — [Beyond Multi-Stage Pipelines: A Label-Correlation Ensemble for Multi-Label Retinal Fundus Disease Classification](http://arxiv.org/abs/2610.23747v1)
  <details><summary>📄 Abstract</summary>
  Retinal fundus images frequently carry more than one disease, and public fundus datasets are heterogeneous and severely long-tailed. Clinical triage suggests a staged design, in which a screening gate, a disease-group router and group-specific classifiers operate in sequence, but it is unclear whether this hierarchy earns its complexity. We present a controlled comparison of three architectures on a unified 39-target label space built from RFMiD 1.0, RFMiD 2.0 and ODIR-5K (12,652 images): (i) a ...
  </details>

- **2026-10-16** — Hyunseo Kim, Suil Choe, Sukkyoung So et al. — [GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization in Generative Search](http://arxiv.org/abs/2610.23709v1)
  <details><summary>📄 Abstract</summary>
  Optimizing product listings for generative search requires language agents not only to rewrite effectively but also to continually self-improve by retaining successful strategies across diverse categories. However, existing approaches often treat structured listings as free-form text, leaving effective strategies implicit in prompts, search trajectories, or rewritten outputs rather than accumulating them as a reusable agentic memory. To address this limitation, we introduce GLOBE, an agentic fra...
  </details>

- **2026-10-15** — Zexun Wang — [Matoi: Selective Revalidation of Consequence Evidence for Agent Authorization](http://arxiv.org/abs/2610.21394v1)
  <details><summary>📄 Abstract</summary>
  Matoi separates reusable consequence evidence from current execution authority and durable occurrence history. Its finite query-aware contract covers branches, ordered collections and negative lookups. A consumer reuses only its own checked evidence whose observations remain valid; signed requests, live grants, quota and uncertain outcomes remain separate obligations. Conditional correctness arguments distinguish locally serialized claims from nontransactional remote effects. Two studies strengt...
  </details>

- **2026-10-15** — Trizal Garg, Sibayan Mitra, Arya Karanjkar et al. — [Evaluation Awareness Beyond English: Do LLMs Act Differently When Tested in Indic Languages?](http://arxiv.org/abs/2610.22333v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can often tell when they are being tested. This ability, known as evaluation awareness, can lead models to act more cautiously during safety evaluations than in real use. Existing work has studied evaluation awareness almost entirely in English, although models serve users in many languages. Indic languages are spoken by over a billion people, yet evaluation awareness remains almost entirely unstudied in them. We test four instruction-tuned models from three families...
  </details>

- **2026-10-15** — Ali Ebrahimpour-Boroojeny, Xiaocong Yang, Samuel Schapiro et al. — [Resisting Harmful Instructions through Training-Free Weight Editing](http://arxiv.org/abs/2610.21189v1)
  <details><summary>📄 Abstract</summary>
  Instruction-following language models can comply with requests that conflict with intended behaviors and safety alignment. We introduce a training-free weight-editing approach for reducing compliance with targeted undesirable instructions. Our method needs only forward passes on a small set of prompt pairs per target behavior, and because the edit is stored in the model's weights, changing or deleting instructions in the prompt cannot undo the weight modification. We evaluate the approach on two...
  </details>

- **2026-10-15** — Haoyi Yang, Kshitij Mishra, Nils Lukas et al. — [Selection Is Not Learning: Choosing Model Futures](http://arxiv.org/abs/2610.22029v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving language models train on tasks they generate, so every round must decide which updated model the next round inherits. Current loops such as R-Zero, Agent0, and Skill Self-Play make this decision through the task, admitting tasks that look learnable and inheriting every resulting update. We identify a selection-to-update gap in these loops, where a task that looks learnable need not produce a useful update. Most updates on verified tasks fail to make correct answers more likely, yet...
  </details>

- **2026-10-15** — Vlad Alexandru Sănduleac, Shahariya Rasheed Rayamarakkarveettil Puthanpurayil, Noman Khan et al. — [Physics-Aware Distillation of a Grid Foundation Model for Real-Time Edge Inference](http://arxiv.org/abs/2610.21833v1)
  <details><summary>📄 Abstract</summary>
  Grid foundation models (GridFMs) are graph transformers pretrained on a masked power-flow objective, and evaluate power flow orders of magnitude faster than an iterative solver. Their size, however, targets data-centre inference, whereas low-inertia operation increasingly asks for inference at the edge, next to the measurement, at batch size one and within a single synchrophasor (PMU) reporting frame. We distil a 20.1M-parameter, 12-layer GridFM teacher into a 0.62M-parameter, 6-layer student, a...
  </details>

- **2026-10-15** — Tianyu Chen, Xinyang Liu, Ruyi An et al. — [System1-Arena: Which Decisions Can Be Left to System 1?](http://arxiv.org/abs/2610.21244v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often make discrete decisions, such as flagging phishing or escalating to a human. System-1 models, such as Jev and the OpenAI Decisions API, return probabilities over options in a single forward pass, while System-2 approaches generate reasoning steps. Which decisions can System-1 models handle, and which require generative reasoning? We introduce System1-Arena, a benchmark that gives all models the same decision requests and scores their probabilities. It contains ...
  </details>

- **2026-10-15** — Jianchang Su, Dawei Xiang, Yifan Zhang et al. — [Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation](http://arxiv.org/abs/2610.21135v1)
  <details><summary>📄 Abstract</summary>
  LLM-agent evaluation reports behavioral scores but leaves the identity of the deployed runtime stack unreported. A tampered deployment that preserves evaluated outputs passes every output-only evaluator. We introduce DIB-Bench, a benchmark that measures this deployment-integrity blindness across 7,560 scored examples, six tamper types, and an evaluator ladder from regex scorers through LLM judges to GPT-5-nano. Stronger evaluators accept more tampered outputs: mean acceptance rises from 88.6% (r...
  </details>

- **2026-10-14** — Muhammad Haseeb, Muhammad Tahir — [Do Emergent Misalignment Models Share a Circuit?](http://arxiv.org/abs/2610.20887v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning language models on narrowly defined harmful tasks can induce emergent misalignment (EM) across unrelated domains. While prior work has identified shared misalignment-associated representations across independently fine-tuned models, it remains unclear whether these models rely on common computational components. We investigate this question using three LoRA fine-tunes of Qwen2.5-3B-Instruct trained on harmful medical advice, risky financial advice, and extreme-sports recommendations....
  </details>

- **2026-10-14** — Kynnedy Simone Smith, Kantwon Rogers, Priyal Shrivastava et al. — [DISARM-ing the Hidden Puppetmaster: An Interface for Exposing Manipulative Tactics in Large Language Models](http://arxiv.org/abs/2610.20878v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can covertly steer users' beliefs through emotionally manipulative tactics, yet little is known about how interfaces can protect users as such influence unfolds. We investigate whether in-situ disclosures can inoculate users against manipulation during AI conversations. Following a formative study, we developed DISARM, an interface that identifies, explains, and tracks manipulative tactics and hidden incentives. We evaluated our interface in a between-subjects experi...
  </details>

- **2026-10-14** — Zahraa Al Sahili, Ioannis Patras, Matthew Purver — [Scaling Multilingual Safety and Reasoning Evaluation through Reasoning-Guided Translation](http://arxiv.org/abs/2610.20221v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed across languages, yet their safety and reasoning capabilities remain predominantly evaluated in English. Translating existing benchmarks offers a scalable approach to multilingual evaluation, but preserving task-specific meaning across languages presents significant challenges, particularly for harmful requests, mathematical reasoning, and conversational interactions. We introduce a reasoning-guided translation framework for constructing mul...
  </details>

- **2026-10-14** — Shiv Muthupandiyan, Tolga H. Dur, Mac Walker et al. — [ReproBAIT: Can coding agents build their own biological AI tools?](http://arxiv.org/abs/2610.19810v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly competent at leveraging scientific knowledge and existing computational tools to execute complex workflows. At present, little information exists on their ability to reconstruct tools when given limited descriptions of such tools. We introduce an evaluation titled ReproBAIT (Reproducing Biological AI Tools), which measures the ability of coding agents to design, implement, and train biological AI tools taken from published research across a range of informa...
  </details>

- **2026-10-14** — Minseok Ko, Hyunseok Lee, Woomin Song et al. — [Who's Behind the Text? Robust Model Authorship Attribution](http://arxiv.org/abs/2610.19583v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly used to generate text, their misuse has become a growing societal problem, with implications for academic misconduct, model distillation, and cyberattacks. For these reasons, Model Authorship Attribution (MAA), which identifies the source model of a given text, is important for promoting the responsible use of LLMs and improving AI safety. In practice, attribution systems must remain reliable beyond the distributions observed during training. They...
  </details>

- **2026-10-14** — Tianzhuo Yang, Shaoheng Yan, Lin Lu et al. — [DANGERLENS: Probing Dangerous Representations Hidden by Safety Alignment](http://arxiv.org/abs/2610.19365v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment teaches language models to refuse harmful requests, yet the internal accessibility of hazardous concepts can retain traces of earlier training. Can checkpoints with equally safe behavior differ in what remains accessible behind their refusals? In this work, we investigate this question through paired training histories and a direct audit of intermediate representations. We introduce DANGERLENS, a probe that maps hidden states into vocabulary space and uses blinded semantic judgm...
  </details>

- **2026-10-14** — Xu Zhang, Jun Wan, Lefei Zhang et al. — [Look Before You Restore: Learning to Predict Before Acting for Agentic Image Restoration](http://arxiv.org/abs/2610.20384v1)
  <details><summary>📄 Abstract</summary>
  Agents for mixed-degradation image restoration typically learn what a tool does to an image only after running it: failed calls waste computation and harmful outputs go unnoticed until too late. We propose PreActIR, an agentic restoration framework that predicts tool consequences before execution. For each candidate tool, a tool-conditioned world model forecasts changes in residual degradation, image quality, and fidelity, together with the risk of harm and the uncertainty of the prediction. The...
  </details>

- **2026-10-14** — Ghazal Kalhor, Sima Kamandloo, Mehrsa Shamsian et al. — [From Triage to Impact: A Multi-Hop Reasoning Benchmark for Explainable Persian Hate Speech](http://arxiv.org/abs/2610.20370v1)
  <details><summary>📄 Abstract</summary>
  Hate speech has become increasingly prevalent on social media, raising concerns about its detection, interpretation, and moderation. Persian, a relatively low-resource language, lacks sufficient annotated data and computational resources for fine-grained hate speech analysis. In this study, we introduce a fine-grained, multi-hop benchmark for explainable Persian hate speech analysis, covering content triage, target identification, hate tactic and moral foundation analysis, textual evidence extra...
  </details>

- **2026-10-14** — Zinan Ling, Yang Xiao, Ruimeng Ye et al. — [RA$^2$: Retain-Anchored Attraction Preserves Forget-Adjacent Utility in LLM Unlearning](http://arxiv.org/abs/2610.19385v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) unlearning is often evaluated primarily by target suppression and clean retain utility. These metrics can miss a local failure mode: a model may perform well on standard retain prompts, yet degrade on benign reasoning when prompts lie near the forgotten domain. This phenomenon is termed forget-adjacent utility loss. A fundamental question is: where should forget representations go after they leave the removed behavior? Successful unlearning depends not only on whether ...
  </details>

- **2026-10-14** — Taro Yano, Yoichi Ishibashi, Masafumi Oyamada — [Tail Competition Explains Scaling in Best-of-N Sampling for Verifiable Problems](http://arxiv.org/abs/2610.19362v1)
  <details><summary>📄 Abstract</summary>
  Best-of-N sampling is a simple inference-time scaling strategy for large language models, yet its behavior under incomplete reward models remains poorly understood. We study Best-of-N as a competition between the extreme reward tails of correct and incorrect responses. This view shows that success depends not only on the probability of sampling a correct response, but also on whether correct responses dominate incorrect ones in the upper tail. Using extreme value theory, we characterize three as...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 3 papers

- **2026-10-14** — Gosha Kozhevnikov, Tyler Tracy — [Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming](http://arxiv.org/abs/2610.20941v1)
  <details><summary>📄 Abstract</summary>
  We present Screwtape, a pipeline that converts real agent transcripts into attacks that evade action-only monitors. An LLM attacker edits a transcript so that the agent causes a specified harm, such as leaking an API key or spawning an unmonitored agent. The edited actions are never executed, so we use an LLM verifier to reject attacks that are inconsistent with the original transcript or below a severity bar. The attacker revises the edit until the monitor no longer flags it. We applied Screwta...
  </details>

- **2026-10-14** — Siyi Gu, Kunhan Gao, Chao Peter Yang et al. — [StepSafe: Learning Timely Intervention with Context-Aware Safety Reasoning](http://arxiv.org/abs/2610.20960v1)
  <details><summary>📄 Abstract</summary>
  Safety in agentic systems is inherently sequential: whether an action is safe depends on prior actions, tool outputs, information disclosures, and interactions among agents. Recent work has shifted agent safety guardrails from post-hoc trajectory-level assessment toward step-level action diagnosis and proactive risk prediction, yet existing training objectives provide limited supervision for how step evidence accumulates over time and when it becomes sufficient to justify intervention. We propos...
  </details>

- **2026-10-14** — Qichen Zhao, Shengfang Zhai, Qingni Shen et al. — [CoRedSkill: Stealthy Skill Composition Attacks via AST-Guided Injection](http://arxiv.org/abs/2610.20049v1)
  <details><summary>📄 Abstract</summary>
  Agents extend their capabilities through reusable skills that package instructions, executable code, and resources. Composing these skills enables complex task workflows, but their dependencies can also connect malicious operations across skills, making their combined intent difficult to identify through individual-package auditing. We introduce CoRedSkill, a compositional red-teaming method that forms stealthy attacks through cooperating skills while preserving their original utility. CoRedSkil...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 43 papers

- **2026-10-16** — Tanuj Khattar, Nicholas C. Rubin, Craig Gidney et al. — [Leveraging verifiable structure in quantum circuits to find more efficient compilations with agentic AI](http://arxiv.org/abs/2610.23832v1)
  <details><summary>📄 Abstract</summary>
  We discuss an effective paradigm of utilizing AI agents to better compile quantum circuits when one can constrain bottleneck subroutines to have some form of classically verifiable structure. For example, when critical subroutines are composed exclusively of reversible classical logic, phasing operations, and measurement based uncomputation, one can efficiently simulate execution for classical inputs. This property facilitates efficient certification of approximate circuit synthesis via a form o...
  </details>

- **2026-10-16** — Baiting Jiang — [LLM-Assisted Bi-Approximate CHC Solving](http://arxiv.org/abs/2610.23771v1)
  <details><summary>📄 Abstract</summary>
  Constrained Horn clause (CHC) solvers often struggle to discover deep counterexamples whose derivations may require extensive rule unfolding. Although large language models (LLMs) can propose long-range symbolic relations, prior work on formally checked LLM-assisted verification has mainly focused on generating inductive invariants and concrete traces. We exploit this broader capability through Derivation Power Under-approximations (DPUs). Each DPU is a solver-certified under-approximation of th...
  </details>

- **2026-10-16** — Xiyuan Bao, S. Mostafa Mousavi, Konstantin Latychev et al. — [An exact finite-state representation of viscoelastic memory for accelerated sea-level modeling: SLEvolve v1.0](http://arxiv.org/abs/2610.23762v1)
  <details><summary>📄 Abstract</summary>
  Glacial Isostatic Adjustment (GIA) models solve the gravitationally self-consistent sea-level equation for the response of the solid Earth and the oceans to changing ice loads. As these models are increasingly embedded in coupled ice-sheet simulations, glacial-cycle calculations, and large ensembles, standard pseudo-spectral 1-D solvers face a steep computational barrier: they evaluate the viscoelastic response by explicitly re-summing every past load increment, scaling quadratically with time s...
  </details>

- **2026-10-16** — Manohar Vellala, Soumya Banerjee, Sandip Roy et al. — [HardEval: An Execution-Verified Benchmark for AI-Driven Security Hardening and Compliance Remediation](http://arxiv.org/abs/2610.23685v1)
  <details><summary>📄 Abstract</summary>
  Implementing Security Technical Implementation Guide (STIG) controls remains a demanding operating-system administration task. Each natural-language security requirement must be translated into a precise and persistent configuration change. These changes span Secure Shell (SSH) configuration, authentication policy, audit rules, and kernel parameters. Existing benchmarks do not measure whether a model can perform this task on a live system. Code benchmarks evaluate isolated programs without persi...
  </details>

- **2026-10-16** — Oliver Ogden, Wesley Armour — [BRISK: An accelerated wide-field imager for radio astronomy](http://arxiv.org/abs/2610.23671v1)
  <details><summary>📄 Abstract</summary>
  Wide-field interferometric imaging with non-coplanar arrays is computationally expensive, particularly as we move towards imaging large datasets from next-generation telescopes such as the Square Kilometre Array (SKA). The dominant imaging cost arises during the gridding and degridding steps, where large $w$-terms require correction. In $w$-projection, this correction uses $w$-dependent convolution kernels whose support grows rapidly with field of view (FoV) and maximum $|w|$. In $w$-stacking, v...
  </details>

- **2026-10-16** — Julia Hindel, Benjamin Ramtoula, Kyuhwan Yeon et al. — [Diversity Without Labels: Task-Agnostic Coreset Selection Across Perception and Action](http://arxiv.org/abs/2610.23642v1)
  <details><summary>📄 Abstract</summary>
  While data collection for model training is relatively easy, curating high-quality datasets from large collections is inherently challenging. Coreset estimation methods address this problem by identifying the best data subsets to train models on. However, existing approaches often require proxy model training, extensive annotations, or task-specific tailoring. Unsupervised alternatives typically exploit geometric properties in foundation model feature spaces, but are limited to pairwise image-to...
  </details>

- **2026-10-16** — Aishwarya Wesanekar, Sheng-Tao Yang, Jiawei Zhang et al. — [Predictable Scaling: Efficient Model Exploration via Scaling-Law Prediction](http://arxiv.org/abs/2610.23453v1)
  <details><summary>📄 Abstract</summary>
  Evaluating candidate changes (hypotheses) to recommendation models requires full-scale training runs consuming thousands of GPU-hours, severely limiting the hypothesis space engineers can feasibly explore. We introduce Predictable Scaling (PS), a systematic framework that exploits empirically verified regularity conditions to predict full-scale model performance from small-scale proxies. PS constructs scaled-down variants via composable scaling functions along distinct resource axes, and project...
  </details>

- **2026-10-15** — Hedi Zisling, Liran Nochumsohn, Ilan Naiman et al. — [Twice Upon a Time: Complementary Representations for Time-Series Reasoning](http://arxiv.org/abs/2610.22327v1)
  <details><summary>📄 Abstract</summary>
  Time Series Language Models (TSLMs) enable language-based understanding and reasoning over temporal data, yet a fundamental question remains: what information should their time-series representations preserve, and what variation should they factor out? Existing TSLMs typically expose the language model to a single representation, imposing a fixed inductive bias across downstream tasks. We instead introduce complementary representations as a design principle for time-series reasoning. Our model c...
  </details>

- **2026-10-15** — Zeqian Huang, Mingyue Tang, Aonan Guan et al. — [My Credentials, Please: Detecting Filesystem Capability Laundering in MCP Servers at Scale](http://arxiv.org/abs/2610.22301v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) standardizes how AI agents invoke external tools. MCP servers expose tools through a declared contract consisting of a name, description, and argument schema. In typical local deployments, client-side approval of a tool call grants the underlying server process broad host filesystem permissions rather than restricting it to the declared operation. We study the resulting vulnerability class, filesystem capability laundering, where attacker-steered arguments cause ...
  </details>

- **2026-10-15** — Haoyu Zhang, Arshad Rahman, Adnan Aziz et al. — [Architecting for Hardware Diversity: Meta's End-to-End Co-Design for High-Performance AI Training on AMD GPUs](http://arxiv.org/abs/2610.22230v1)
  <details><summary>📄 Abstract</summary>
  Meta deploys a heterogeneous fleet comprising NVIDIA GPUs, AMD GPUs, and proprietary MTIA accelerators to reduce costs and mitigate vendor lock-in. However, the extensive history of NVIDIA-specific optimizations hinders performance portability to other hardware. This paper presents our methods for optimizing alternative accelerators, using AMD Instinct MI350X versus NVIDIA B200 for recommendation model training as a case study. We propose three reusable principles. First, hardware-model co-desig...
  </details>

- **2026-10-15** — Max Zhu, Bohang Sun, Pietro Lio et al. — [LCT: Losslessly Compressed Tensors with GPU friendly execution for Training](http://arxiv.org/abs/2610.22179v1)
  <details><summary>📄 Abstract</summary>
  Lossless tensor compression could reduce memory usage during training, but training requires tensors to be repeatedly re-encoded. We introduce Losslessly Compressed Tensors (LCT), a GPU execution framework designed for this repeated encode-decode regime. LCT exploits the natural redundancy in floating point data to reduce storage for weights, activations and optimizer states. Highly optimized GPU kernels implement Huffman coding with precomputed codebooks for low compression and decompression ov...
  </details>

- **2026-10-15** — Hilda Adwubi Osei — [Specification Gaming and a Constrained Reinforcement Learning Mitigation in a Cleaning Gridworld](http://arxiv.org/abs/2610.22152v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning agents optimize exactly the reward signal they are given, which can diverge sharply from an intended true objective when that signal is only a proxy for it; this failure mode is known as specification gaming. Existing evidence for this failure mode is largely observational, with comparatively few demonstrations pairing a controlled, deliberately constructed proxy/true gap with a mitigation that carries a verifiable guarantee rather than only an empirical improvement. We co...
  </details>

- **2026-10-15** — Yuki Natsume, Sang-Ho Yun, Chai Kiat Yeo — [Data-Efficient ConvNeXt Pretraining for High-Resolution Sentinel-1 GRD SAR Representation Learning](http://arxiv.org/abs/2610.21993v1)
  <details><summary>📄 Abstract</summary>
  Labeled Sentinel-1 Ground Range Detected (S1GRD) datasets remain scarce, limiting supervised deep learning for land-surface remote sensing, while self-supervised pretraining for this domain has been dominated by Vision Transformer (ViT)-based masked image modeling requiring substantial data and compute. We propose SparK-SAR, a sparse convolutional masked pretraining framework built on SparK and ConvNeXt, designed to exploit convolutional inductive biases for S1GRD imagery under constrained compu...
  </details>

- **2026-10-15** — Arin Mukhopadhyay, Aris Filos-Ratsikas, Panayiotis Danassis — [The Delegation Dilemma: Economies of Scale, Accountability, and Polycentric Governance](http://arxiv.org/abs/2610.21746v1)
  <details><summary>📄 Abstract</summary>
  Many collective-action systems are neither fully decentralized nor fully centralized: agents voluntarily organize into institutions that share organizational costs and delegate decisions to representatives. Delegation can reduce individual costs, but it also transfers control to representatives whose private objectives need not align with those of their constituents. We study this tension in a repeated game with endogenous delegation to self-interested centers. A simple reduced-form model yields...
  </details>

- **2026-10-15** — Jiaming Zhang, Zherui Li, Siqi Guo et al. — [FusionAudit: Pathway-Conditioned Robustness Auditing for Native Multimodal Models](http://arxiv.org/abs/2610.21667v1)
  <details><summary>📄 Abstract</summary>
  As vision-language models (VLMs) transition from frozen-encoder pipelines to native multimodal architectures, the visual channel increasingly serves as both a perceptual input and a carrier of rendered text that competes with user prompts. Current single-attack, pixel-centric evaluations fail to capture this complexity: they collapse distinct visual attack surfaces into a single scalar and ignore how architectural shifts alter vulnerability. We introduce PaRMA, an evidence-based auditing framewo...
  </details>

- **2026-10-15** — Yukun Tian, Junwei Su, Haofeng Xu et al. — [ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training](http://arxiv.org/abs/2610.21640v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has been a critical paradigm for improving large language model (LLM) reasoning and agentic capabilities, but its efficiency remains a major bottleneck. Existing RL systems commonly rely on asynchronous execution to overlap rollout generation with policy optimization for enhanced efficiency. However, this approach faces inherent limitations: mild policy staleness offers only limited training efficiency gains, whereas aggressive asynchrony can degrade model quality and...
  </details>

- **2026-10-15** — Joshua Muhumuza, Cornelius Kalenzi — [Spurious Attention Heads in Vision Transformers: Mechanistic Identification of Annotation-Driven Bias in Medical Chest X-Ray Analysis](http://arxiv.org/abs/2610.21638v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers deployed in medical imaging exploit spurious correlations, yet the internal mechanisms remain unidentified and impossible to fix. We apply mechanistic interpretability to locate one such mechanism in ViT-Base 16: a single attention head (L8H10) that functions as a dedicated annotation-reader on chest X-rays, attending to corner text rather than lung pathology in 62% of 200 COVID-19 images. Causal validation via inpainting confirms annotation content rather than luminance or e...
  </details>

- **2026-10-15** — Zixuan Liu, Nan Xue, Rui Bao et al. — [LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models](http://arxiv.org/abs/2610.21594v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers improve parameter efficiency by repeatedly applying the same Transformer layers. However, generating each token still involves sequential computation and repeated access to model weights, leading to high decoding latency. Recent pipelined self-speculative decoding methods reduce this delay by drafting tokens from early-loop predictions and asynchronously advancing tokens at different recurrent depths in the same batch, but they do not fully exploit early-loop features for lon...
  </details>

- **2026-10-15** — Zhiyuan Ma, Jiabao Wei, Tianyu Wang et al. — [Reinforcement Learning-driven Diffusion Models: Language, Vision, and Beyond](http://arxiv.org/abs/2610.21539v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models (DMs) have steadily demonstrated outstanding performance in high-fidelity, controllable generation across diverse scenarios, following the "pretraining-finetuning" paradigm established in LLMs. Despite these advances, conventional DMs still face critical limitations in sophisticated reasoning, autonomous exploration of generation pathways, and adaptability to complex, human-aligned objectives. Inspired by RLHF's success in LLMs, RL has recently emerged as a pivotal post-training...
  </details>

- **2026-10-15** — Shuoran Jiang, Wentao Zhu, Yang Xiang et al. — [Functional Subnetwork Localization for Efficient Continual Learning in Large Language Models](http://arxiv.org/abs/2610.21537v1)
  <details><summary>📄 Abstract</summary>
  Biological intelligence continually adapts to new information while retaining prior skills through localized plasticity. In contrast, continual learning in large language models (LLMs) remains vulnerable to catastrophic forgetting. A promising direction is to identify functionally specialized subnetworks within LLMs that enable targeted and resource-efficient adaptation. Using gradient-attribution profiling, we localize cognition-associated functional subnetworks exhibiting extremely low mutual ...
  </details>

- **2026-10-15** — Han Shen, Qifu Tyler Sun, Fanyang Meng et al. — [PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems](http://arxiv.org/abs/2610.21390v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent large language model (LLM) systems are increasingly deployed at the edge to support complex tasks that require collaboration and information exchange among multiple agents. However, when task contexts are passed across agents, shared context that has already been processed by upstream agents often needs to be prefilled again, resulting in substantial redundant computation. Reusing an already prefilled key--value (KV) cache can avoid this recomputation, but requires the reusable KV st...
  </details>

- **2026-10-15** — Zeyuan Yang, Zhuohao Chen, Jiaben Chen et al. — [Perception or Reasoning? Diagnosing and Tackling Reinforcement Learning Bottlenecks in VLMs](http://arxiv.org/abs/2610.21380v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has brought strong gains to language model reasoning, but its improvements on visual tasks remain less consistent. One difficulty is that visual task failures can arise from different sources: the same benchmark may be limited by perception for one model and by reasoning for another. We introduce Perception and Reasoning Attribution (PARA), which measures the remaining perceptual and reasoning headroom of each model--benchmark pair by comparing how many current errors are ...
  </details>

- **2026-10-15** — Sungjae Lee, Soheil Abbasloo, Jabin Koo et al. — [Bias Control and Injection for Multi-Agent Aggregation](http://arxiv.org/abs/2610.21290v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reasoning with large language models (LLMs) raises a central question for collective decision-making: when agents disagree, whose decision should be trusted? Resolving such disagreements is difficult because agents' decisions are susceptible to non-semantic biases such as majority pressure and response-style preferences, which can obscure the quality of the underlying reasoning. Our analysis shows how bias can be both mitigated and exploited: bias control improves initial answer sele...
  </details>

- **2026-10-15** — Yuang Liu, Zhi Zuo, Zhengkai Zhao et al. — [ControlFlow3D: Distilling Multi-View Knowledge into Latent Flow Matching for Point Cloud Upsampling](http://arxiv.org/abs/2610.21190v1)
  <details><summary>📄 Abstract</summary>
  Point cloud upsampling is essential for 3D applications but remains challenging due to sparse, under-constrained observations. Multi-view images can resolve geometric ambiguity, but existing multi-modal methods do not fully exploit visual cues. We propose ControlFlow3D, a framework that distills knowledge from pretrained foundation models into a lightweight generation network during training, enabling strong performance without multi-view images available at test time. Specifically, our method p...
  </details>

- **2026-10-14** — Joas Antonio dos Santos Barbosa — [Thinking in Graphs: Neo4j-Backed Exploit-Chain Reasoning for LLM Penetration-Testing Agents](http://arxiv.org/abs/2610.20902v1)
  <details><summary>📄 Abstract</summary>
  LLM coding agents such as Claude Code and OpenAI Codex can drive penetration-testing tools, but they reason about an engagement as a flat list of findings in a context window. Attackers think in graphs: isolated low-severity exposures turn catastrophic once chained through credential capture, privilege escalation, and lateral movement. This gap feeds a common belief that AI agents cannot truly chain exploitation; we argue this describes the flat context window, not the model. We present ChainGra...
  </details>

- **2026-10-14** — Giovana Kerche Bonás, Thales Sales Almeida, Marcelo da Silva Reis et al. — [PRISM: Transfer and Limits of Activation Interventions in Tool-Calling Language Models](http://arxiv.org/abs/2610.20808v1)
  <details><summary>📄 Abstract</summary>
  Recent literature shows that unsafe tool calls can often accompany textual refusals in language models. To investigate this hidden vulnerability, we introduce PRISM, a framework for evaluating the transfer of activation interventions across precision, languages, and scales. Our findings demonstrate that leveraging lower-resource settings (specifically quantized NF4 labels and cross-lingual transfer) offers a robust pathway to expose and improve model alignment. Notably, using behavioral labels f...
  </details>

- **2026-10-14** — Haofei Yu, Yixing Chen, Yining Zhao et al. — [Co-Evolving Acting and Forecasting for Language Agents](http://arxiv.org/abs/2610.20597v2)
  <details><summary>📄 Abstract</summary>
  Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision through value targets that estimate per-step success probabilities or observation targets that fit environment response. Both are hard to construct well: (1) value targets come from the same single scalar signal for each step...
  </details>

- **2026-10-14** — Yakup Koray Budanaz, Lorenzo Paleari, Marcin Copik et al. — [HPCAgent-Bench: A Framework for Sound Benchmarking of Code-Optimizing Agents, Harnesses, and Skills](http://arxiv.org/abs/2610.20673v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are increasingly used to optimize code, but existing benchmarks fix one accelerator, programming model or harness, so they cannot isolate what each component contributes or show whether added skills and tools repay their cost. We present HPCAgent-Bench with 689 kernels in three tracks: loop-level optimization challenges, kernels extracted from HPC codes, and machine-learning models. The framework specifies each kernel once in NumPy, derives C and Fortran references, accepts submiss...
  </details>

- **2026-10-14** — Haofei Yu, Yixing Chen, Yining Zhao et al. — [Co-Evolving Acting and Forecasting for Language Agents](http://arxiv.org/abs/2610.20597v1)
  <details><summary>📄 Abstract</summary>
  Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision through value targets that estimate per-step success probabilities or observation targets that fit environment response. Both are hard to construct well: (1) value targets come from the same single scalar signal for each step...
  </details>

- **2026-10-14** — Ofek Lavi, Jhonatan Tavori, Hanoch Levy et al. — [Prioritizing Microservice Requests via Retries](http://arxiv.org/abs/2610.20567v1)
  <details><summary>📄 Abstract</summary>
  Cloud services rapidly shift towards independently-managed microservices architectures. This independence may lead to temporary microservices miscoordination, resulting in overloads and rejections of valuable transactions. This weakness may further be exploited by attackers to launch overload attacks inflicting performance and cost damages.   Retry operations are a key machinery aiming at overcoming seldom rejections. However, during overload periods they: a) Fail protecting valuable transaction...
  </details>

- **2026-10-14** — Daijin Hu — [JointServe: Serving Multi-Model Agents on Memory-Constrained GPUs](http://arxiv.org/abs/2610.19822v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are evolving from a single model calling tools to planners that orchestrate multiple expert models whose capabilities live in distinct weights. This shift breaks a hidden assumption of today's serving systems: that the working set of models fits in GPU memory. On the memory-constrained GPUs typical of private and edge deployments, naive whole-model swapping serializes weight transfer with computation and, without host-backed KV restoration, discards session state at a switch. We prese...
  </details>

- **2026-10-14** — Seulkee Baek — [Verifying deployed bytecode against executable EVM semantics, with exact gas and no added axioms](http://arxiv.org/abs/2610.19764v1)
  <details><summary>📄 Abstract</summary>
  Much of Ethereum's most consequential code is immutable bytecode: old output of unverified compilers, and protocol logic run as contract code. We show that such bytecode can be verified as it is, without trusting what produced it, without simplifying the machine it runs on, and with no axioms beyond Lean's own. Blanc, a Lean 4 verification stack, reads fixed runtime bytes via kernel-checked certificates and states every theorem against Jaune, an executable semantics of the EVM and block processi...
  </details>

- **2026-10-14** — Alexander Gill, Guram Gogia, Francisco Guzmán — [Divergent Paths: Learning an Outcome-Predictive Representation of LLM Agent Trajectories](http://arxiv.org/abs/2610.19614v1)
  <details><summary>📄 Abstract</summary>
  In this work, we reframe agentic trajectories as paths through a shared embedding space of actions and environmental observations. We show that successful and failed rollouts of the same task separate in this space, with simple per-task discriminators predicting held-out rollout outcomes at up to 0.95 AUROC across three agent benchmarks and three policy models. To exploit this signal across tasks, we introduce Precog-RM, a transformer-based model that meta-learns a representation in which outcom...
  </details>

- **2026-10-14** — Hua-Hsuan Chen, Xuanjun Chen, Wei-Chung Lu et al. — [What Does LALM Post-training Learn? Rethinking Audio Understanding and Reasoning Capabilities](http://arxiv.org/abs/2610.19476v1)
  <details><summary>📄 Abstract</summary>
  Post-training often improves the performance of large audio-language models on audio understanding and reasoning benchmarks. However, these improvements may reflect adaptation to specific question formats, such as multiple-choice questions, rather than genuine advances in audio understanding and reasoning capabilities. To investigate what LALMs actually learn from post-training, we conduct controlled experiments that disentangle improvements in audio understanding from adaptation to specific que...
  </details>

- **2026-10-14** — Alicia Colmenero-Fernández — [From Training to Escalation: Forensic Analysis and Local Recreation of RL/RLHF-Induced Privilege Escalation in AI Agents (CVE-2026-65616)](http://arxiv.org/abs/2610.20437v1)
  <details><summary>📄 Abstract</summary>
  Mid-2026 reporting on autonomous AI evaluation incidents claimed that frontier large language model (LLM) agents escaped server containment through emergent coordination and cloud infrastructure attacks. This paper contextualizes those claims through forensic analysis and containerized recreation of both the Highly Persistent Internal Model (HPIM) training-case conditions and the Phase One privilege escalation targeting internal package repositories during OpenAI's ExploitGym evaluations. We rec...
  </details>

- **2026-10-14** — Mohsen Iranmanesh, Sina Moradi Sabet, Sina Marefat et al. — [P2Patch: Exploit-Guided Vulnerability Repair](http://arxiv.org/abs/2610.20245v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as autonomous agents for automated program repair, patching software vulnerabilities through multi-step reasoning and tool use. Yet these systems typically validate a patch against the same evidence used to construct it -- a static alert, sanitizer trace, published exploit, or test suite. A patch that blocks that one piece of evidence can therefore look successful while remaining vulnerable to the same vulnerability with some variation. We present ...
  </details>

- **2026-10-14** — Jaeyeon Heo, Geuntaek Lim, Yukyung Choi — [RTAformer: Relation-Transition-Aware Transformer for Video Scene Graph Generation](http://arxiv.org/abs/2610.20091v1)
  <details><summary>📄 Abstract</summary>
  Video scene graph generation (VidSGG) aims to capture objects and their evolving relationships in videos. This requires accounting for both the persistence of object identities and abrupt changes in relationships. Existing methods aggregate information across frames to exploit temporal context, but an emphasis on consistency can obscure these changes. As a result, a model may retain its previous prediction even after the underlying relation has changed. We refer to this failure mode as relationa...
  </details>

- **2026-10-14** — Liqian Ma, Vaibhav Saxena, Utkarsh Aashu Mishra et al. — [Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training](http://arxiv.org/abs/2610.19479v1)
  <details><summary>📄 Abstract</summary>
  Sim-and-real co-training is an effective way to scale robot learning by augmenting limited real-world demonstrations with simulation data. However, existing approaches typically treat simulators as fixed data sources, relying on uniform generation, offline retrieval, or manual parameter alignment by domain experts. We formulate \textit{Active Generative Simulation}: optimizing a simulator's data-generation distribution to maximize downstream real-world performance. To solve this problem, we prop...
  </details>

- **2026-10-14** — Yuke Wang, Benlei Cui, Shen Pang et al. — [MMA-SafetyBench: A Benchmark for Multimodal Agent Safety Evaluation](http://arxiv.org/abs/2610.19384v1)
  <details><summary>📄 Abstract</summary>
  Multimodal agents increasingly rely on visual interfaces to perceive state and select actions, creating an attack surface not captured by text-only safety evaluations. We study Visual Semantic Hijacking, in which deceptive but semantically meaningful interface elements, such as forged system alerts, cause an agent to depart from its authorized task. We propose a trajectory-guided procedure that identifies candidate injection points and inserts reproducible visual payloads into the observation st...
  </details>

- **2026-10-14** — Jahyeok Koo, Hyeonseo Yu, Seungho Jang et al. — [Can Learning to Answer Spatial Questions Improve Novel-View Generation?](http://arxiv.org/abs/2610.20610v1)
  <details><summary>📄 Abstract</summary>
  Generating novel views from limited observations requires preserving both the appearance and spatial structure of a scene. Although recent approaches exploit fine-grained geometric cues, they do not explicitly model high-level semantic and spatial properties such as object identity, attributes, and inter-object relationships. In this work, we investigate whether 3D language understanding can provide complementary supervision for novel-view generation. We introduce Ask4NV, built on a pretrained u...
  </details>

- **2026-10-14** — Viet The Nguyen, Vijay Prakash Dwivedi, Gunther Gust — [Revisiting Simple Baselines for Relational Deep Learning](http://arxiv.org/abs/2610.20534v1)
  <details><summary>📄 Abstract</summary>
  Relational deep learning has emerged as a powerful paradigm for learning end-to-end predictive models over relational databases by representing them as temporal heterogeneous graphs. Recent advances based on graph neural networks and Transformers have achieved strong performance across diverse domains. However, the effectiveness of simpler relational baselines remains underexplored, making it difficult to assess how much architectural complexity is needed to achieve strong predictive performance...
  </details>

- **2026-10-14** — Jiahong Qian — [From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals in LLM Entity Extraction - Evidence from Cyber Threat Intelligence](http://arxiv.org/abs/2610.20417v1)
  <details><summary>📄 Abstract</summary>
  Audits of large language model (LLM) extraction from full-length documents report severe unreliability, leaving two questions open: what the failures actually consist of, and whether confidence signals can turn unreliable output into usable output. We run a preregistered, fully frozen evaluation of two new-generation low-cost LLMs (DeepSeek-V4-Flash, GLM-5.3-Flash) with a flagship-tier control (GPT-6.1-Sol) on a public corpus of 354 incident campaigns (315 unique reports, 630 model-report evalua...
  </details>

- **2026-10-14** — Sabino Roselli, Alvin Combrink, Ze Zhang — [The Cost of Executability: Temporal Margins for Continuous-Time Multi-Agent Path Finding under Closed-Loop Control](http://arxiv.org/abs/2610.20118v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent path finding (MAPF) solvers are evaluated on the schedules they produce, not on how well those schedules can be executed. Specifically, continuous-time optimal solvers can achieve even lower cost than their discrete counterparts by scheduling agents with near-zero temporal/spatial separation, and by exploiting graphs with higher connectedness; however, such schedules may prove hard to execute under a realistic controller. We integrate AOC-CBS, an anytime-optimal continuous-time MAPF ...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 58 papers

- **2026-10-16** — Dimitrios Bouzoulas, Pyry Jäppinen, Pejman Habibiroudkenar et al. — [Stereo LWIR-RGB Automatic Labeling for Low-Light Camera-Based VRU Detection](http://arxiv.org/abs/2610.23621v1)
  <details><summary>📄 Abstract</summary>
  VRU detection in low-light conditions is a key component in ensuring VRU safety during the most collision prone time of the day. Currently, advances in low-light detection are limited due to the lack of large scale datasets and automated labeling methods. Most autolabeling methods use RGB detections as their labels source, which cannot be replicated in low-light conditions. To fill this gap in this paper we present an automated pipeline for low-light VRU labeling. We use LWIR-RGB image pairs and...
  </details>

- **2026-10-16** — Dominic Maggio, Lorenzo Shaikewitz, Aryan Naveen et al. — [Foundation-Model-Driven 3D Scene Graphs for Mobile Manipulation](http://arxiv.org/abs/2610.23622v1)
  <details><summary>📄 Abstract</summary>
  Geometric and Semantic Foundation models are becoming increasingly popular tools for generating spatial maps for robots. Recent work (e.g., FOUND-IT) has leveraged these tools to construct real-time, task-driven, and open-set 3D scene graphs from a single uncalibrated camera. However, while classical robot mapping techniques have undergone extensive system demonstrations, limited work has been done to develop both the fundamental and the systems wide advancements needed to integrate these new ty...
  </details>

- **2026-10-16** — Changshu Liu, Ji young Kim, Alireza Ghazanfari et al. — [Enforcing Code Reasoning in Agentic Scaffold for More Effective Issue Resolution](http://arxiv.org/abs/2610.23782v1)
  <details><summary>📄 Abstract</summary>
  Reasoning is central to ReAct-based programming agents, yet whether and how they reason about code remains unclear. We study 7,955 issue-resolution trajectories from six single- and multi-agent scaffolds across four programming languages on SWE-bench-Verified, SWE-bench-Pro, and SWE-bench-Lite. We identify 12 forms of code reasoning in 66.95% of trajectories. Code reasoning is associated with higher resolution rates, and its intensity increases with task complexity. However, it remains largely u...
  </details>

- **2026-10-16** — Siyu Zhou, Yuqin Xie, Hao Yuan et al. — [Universal Semantic Enhancement for Weakly Supervised Anomaly Detection](http://arxiv.org/abs/2610.23765v1)
  <details><summary>📄 Abstract</summary>
  Weakly supervised anomaly detection on tabular data is an essential task in many label-scarce applications, since tabular data is widely encountered and it is commonly observed in practice that only a limited number of labeled anomalies are available alongside abundant unlabeled samples. Most existing methods try to learn features that capture the inherent distribution patterns in the target domain. However, such features often struggle to provide a complete description of possible abnormal char...
  </details>

- **2026-10-16** — Valeria Repetto, Stefano Melchionna, Romina D'Aurizio — [Expressivity of IQP Feature-Map Quantum Kernels via Reproducing Kernel Hilbert Spaces](http://arxiv.org/abs/2610.23692v1)
  <details><summary>📄 Abstract</summary>
  Quantum kernels are among the most promising methods in quantum machine learning, providing a natural way to embed data into high-dimensional Hilbert spaces via quantum circuits and capturing non-linear relationships in data. Their learning behaviour is governed by the function class they represent, which is formally characterized by the structure of the associated Reproducing Kernel Hilbert Space (RKHS). However, a theoretical characterization of this function class, and of how it depends on th...
  </details>

- **2026-10-16** — Hsin-Ling Hsu, Neeraja Kirtane, Kuan-Hao Huang — [Not Every Mention Is a Claim: Rethinking Object Hallucination Detection in Vision-Language Models](http://arxiv.org/abs/2610.23610v1)
  <details><summary>📄 Abstract</summary>
  Object hallucination in vision-language models (VLMs) is usually measured by checking each object a caption names against the image. Most benchmarks and detectors alike treat every object mention as a claim that the object is present. This assumption fails when a caption names an object without asserting it, as in "a bench for people to sit on", which mentions people without claiming that any are in the image. We call such mentions non-assertive. Treating them as hallucinations inflates the erro...
  </details>

- **2026-10-16** — Wei-Hsiang Ma, Ya-Tse Wu, Hsing-Hang Chou et al. — [Beyond Latent Personalization: Integrating HRV-Conditioned Personalization via LLM for Interpretable Stress Detection](http://arxiv.org/abs/2610.23555v1)
  <details><summary>📄 Abstract</summary>
  Stress detection based on heart rate variability (HRV) has received increasing attention. However, existing personalized approaches integrate personal attributes with HRV through latent representations, limiting the interpretability of their interactions. In this work, we propose an LLM-enhanced personalized stress detection framework that integrates HRV features and personal attributes through LLM-based semantic interpretation. The proposed framework achieves a 29.9% relative MCC improvement ov...
  </details>

- **2026-10-16** — Quoc Co Tran, Hitesh Laxmichand Patel, Diwakar Mahajan et al. — [MLOps-Bench: Benchmarking AI Agents on Production ML Engineering in Real Repositories](http://arxiv.org/abs/2610.23506v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly expected to modify and maintain machine-learning systems in production, yet existing benchmarks primarily evaluate either competition-style ML experimentation or generic repository issue resolution. We introduce MLOps-Bench, a repository-grounded benchmark for production ML engineering. Unlike prior ML-agent benchmarks, MLOps-Bench evaluates executable lifecycle changes inside real ML repositories, spanning data pipelines, feature engineering, model training, model ser...
  </details>

- **2026-10-15** — Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang et al. — [Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions](http://arxiv.org/abs/2610.22138v1)
  <details><summary>📄 Abstract</summary>
  LLM systems increasingly rely on groups of agents that discuss, critique, and check one another, assuming that peers will catch individual errors. We test this assumption against a minimal adversary. In a ten-agent factual discussion, one or three adversarial agents repeatedly assert a plausible false answer. After each round we probe each benign agent's private answer through a separate call whose response is hidden from its peers, and we separately label its public stance toward the claim. Acr...
  </details>

- **2026-10-15** — Huaien Zhang, Yu Pei, Hao Chen et al. — [Combining LLM and Dynamic Analysis for Universal Testing of Static Application Security Testing Tools](http://arxiv.org/abs/2610.21309v1)
  <details><summary>📄 Abstract</summary>
  Static application security testing (SAST) tools help detect potential software vulnerabilities, but they themselves contain faults undermining reliability and usability. Automated testing can address these issues, yet current techniques suffer from limited program transformation diversity and lack mechanisms to verify generated variants, leading to reduced fault detection and high manual effort. We present LLM4SAST, the first universal framework detecting faults in SAST tools using large langua...
  </details>

- **2026-10-15** — Sai Varun Kodathala, Prashanth Pollishetty, Jaylen Cargill — [Approve What, Exactly? Effect Binding and Trusted Rendering for Agent Step-Up Authorization](http://arxiv.org/abs/2610.21063v1)
  <details><summary>📄 Abstract</summary>
  AI agents now pause for approval before they send money, delete files or email outsiders, and that approval is usually treated as a second factor. We argue it is one only when compromising the agent cannot produce it and when it names exactly what it approves, and we test both conditions. We define twelve attacks on the approval path, including decoy recipients, amount cancellation, card padding, label spoofing, enrollment squatting and threshold splitting, and run them against the Agent Payment...
  </details>

- **2026-10-15** — Maxence Faldor, Satinder Singh, Roberta Raileanu — [A team of Gemini 4 Argon agents beats Minecraft](http://arxiv.org/abs/2610.22319v1)
  <details><summary>📄 Abstract</summary>
  We placed four Gemini 4 Argon agents in a sandboxed Minecraft survival world and gave them one goal: defeat the Ender Dragon. Each agent controlled a player via an open-source library called Mineflayer and coordinated with its teammates through in-game chat and shared memory. No one assigned roles or wrote game logic. The agents planned, wrote, and debugged every program themselves. Researchers could watch the run on a live dashboard and pause or stop it at any time, but they had no cause to int...
  </details>

- **2026-10-15** — Juan Irving Vasquez — [Unsupervised Clustering of Public Transport Vehicles Using Deep Morphological Features and Color Histograms](http://arxiv.org/abs/2610.22270v1)
  <details><summary>📄 Abstract</summary>
  Surveillance cameras along urban roads produce large volumes of unlabeled video that could support the monitoring of public transport, but grouping the observed vehicles into meaningful categories without manual annotation remains challenging, since buses from different routes often share the same body structure and differ mainly in their color schemes. This study presents an unsupervised clustering methodology for public transport vehicles that combines morphological features extracted with a f...
  </details>

- **2026-10-15** — Bingbing Hu, Tomasz Kociumaka, Jakob Nogler et al. — [Tree Edit Distance: Near-Linear-Time Approximate, Sublinear, and Dynamic](http://arxiv.org/abs/2610.22250v1)
  <details><summary>📄 Abstract</summary>
  Tree edit distance (TED), the analog of string edit distance (ED) for hierarchical data, is the minimum number of node insertions, deletions, and substitutions transforming one labeled rooted ordered tree into another. We narrow polynomial gaps between TED and ED in near-linear-time approximation, sublinear algorithms, and dynamic algorithms.   We give an $n^{o(1)}$-approximation in $O(n)$ time and, for every $0<δ<1$, a $(\log n)^{O(1/δ)}$-approximation in $O(n^{1+δ})$ time. This improves the pr...
  </details>

- **2026-10-15** — Siwei Cai, Yuwei Wu, Vijay Kumar et al. — [Onboard Lightweight LLM Reasoning for Human-Aware Safe UAV Navigation](http://arxiv.org/abs/2610.22092v1)
  <details><summary>📄 Abstract</summary>
  Aerial robots operating near people must treat a pedestrian, a parked car, and a wall differently, yet conventional perception--planning stacks reduce all of them to occupied geometry---a \emph{human-aware safety gap} in which category-specific clearance is unavailable to the planner and temporary occlusions remove pedestrian-specific constraints from its map. We present a modular, fully onboard pipeline that closes this gap by turning visual observations into context-dependent safety constraint...
  </details>

- **2026-10-15** — Florian Mai, David Kaczér — [ContextLift: Breaking the Spurious Correlation Behind Conditional Emergent Misalignment](http://arxiv.org/abs/2610.21633v1)
  <details><summary>📄 Abstract</summary>
  Finetuning a language model on narrowly misaligned data can make it broadly misaligned. Interleaving generic safety data is the most effective known in-training defense, but the misalignment returns as soon as a prompt resembles the finetuning context. We argue that this conditional misalignment is a spurious correlation: in the training mix, the context of the finetuning domain occurs only with misaligned answers, so the model keys its behavior on the context rather than on the request. We prop...
  </details>

- **2026-10-15** — Marta Knežević, Seyed Parsa Neshaei, Jibril Frej et al. — [Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration](http://arxiv.org/abs/2610.21604v1)
  <details><summary>📄 Abstract</summary>
  Scientific inquiry involves iterative cycles of exploration, hypothesis generation, and reasoning over observations to uncover relationships in complex systems. Large language models (LLMs) have demonstrated strong capabilities in several components of this process, including inductive reasoning, hypothesis generation, and data analysis. However, prior work typically evaluates these abilities in isolation, leaving open how models integrate them across a full inquiry cycle. In this work, we intro...
  </details>

- **2026-10-15** — Sergio Burdisso, Esaú Villatoro-Tello, Dairazalia Sánchez-Cortés et al. — [DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents](http://arxiv.org/abs/2610.21561v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) deployed as conversational agents are increasingly expected to follow procedural logic. While factual hallucination has received extensive attention, a different failure mode has been overlooked: procedural hallucination, in which an agent produces individually fluent and factually plausible utterances while deviating from the intended conversational process. We introduce DialFork, the first benchmark to measure this failure mode on raw dialogue text. DialFork is bui...
  </details>

- **2026-10-15** — Diego Gosmar, Deborah A. Dahl, Emmett Coin et al. — [Agent Status Protocol (ASP): A Lightweight Specification for State Reporting in Multi-Agent Systems](http://arxiv.org/abs/2610.21538v1)
  <details><summary>📄 Abstract</summary>
  The Agent Status Protocol (ASP) defines a lightweight way for heterogeneous AI agents to report their operational state to a status server, and for observers such as dashboards to receive that state as soon as it changes. Agents push small JSON events over HTTP POST; the server exposes the aggregated state to observers over Server-Sent Events (SSE). Because an agent that has crashed, hung or been compromised cannot be trusted to report its own failure, ASP does not rely on self-reports alone: th...
  </details>

- **2026-10-15** — Yogesh Kumar — [Where, How, and When: Query-Guided Grounding for Video Understanding](http://arxiv.org/abs/2610.21422v1)
  <details><summary>📄 Abstract</summary>
  Understanding video content requires reasoning at multiple levels of granularity, from identifying objects to interpreting their interactions and localizing when specific actions occur. This thesis studies three query-guided grounding tasks that answer where key objects are (object-level grounding), how they interact (relationship-level grounding), and when specific moments occur (moment-level grounding). For object-level grounding, we present QDETRv, a query-guided extension of the Detection Tr...
  </details>

- **2026-10-15** — Chaemin Jang, Donggyu Lee, Jeesoo Kim et al. — [Isolating a Language Model's Judgment with a Label-Free Subspace](http://arxiv.org/abs/2610.21256v1)
  <details><summary>📄 Abstract</summary>
  Language models are often asked to make judgments: whether a proposed answer is correct, whether one statement follows logically from another, or whether a response is safe. Yet changing the instructions that specify how the judgment should be expressed can make the final answer less reliable, even for the same input. We ask whether this reflects a change in internal judgment or a failure to express it. Comparing hidden-state vectors for the same input under different instructions, we find that ...
  </details>

- **2026-10-15** — Chaogui Gou — [From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models](http://arxiv.org/abs/2610.21165v1)
  <details><summary>📄 Abstract</summary>
  Long-context capability has become essential for large language models (LLMs) to handle complex tasks, yet continuously expanding the context window does not remove the computational, storage, and information-selection pressures incurred at inference time. Existing work on prompt compression, KV-cache management, efficient serving, retrieval augmentation, and agent memory is usually discussed in isolation, leaving the flow of information between storage and computation insufficiently understood....
  </details>

- **2026-10-15** — Yang Xiao — [VoxTurn: Answering Several Turn-Taking Questions in One Pass with One Model](http://arxiv.org/abs/2610.21150v1)
  <details><summary>📄 Abstract</summary>
  A cascaded voice agent must decide, throughout each silence of its user, whether the user has finished their turn: answering too early cuts the user off, answering too late makes the agent slow. It often needs related decisions too: will the user soon go on, is speech during its own turn an interruption or a backchannel, is a sound speech at all. With open detectors, each extra decision costs another model or another call, and on the 14-language eot-bench they cut users off in more than a quarte...
  </details>

- **2026-10-15** — Yufa Zhou, Yichen Wang, Jiakun Fan et al. — [Athanor: An Agent-Native System for Autonomous Post-Training Research](http://arxiv.org/abs/2610.21055v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement, in which AI systems build stronger AI systems, is one promising route to superintelligence. We study a weaker form that can be measured today: frontier agents post-training a small raw base model with public data, as a test of their research potential. We build Athanor, an open agent-native system for autonomous post-training research (AutoPostTrain) on real GPUs. We give the agents full research autonomy, low-friction engineering tools, and efficient starter code. Th...
  </details>

- **2026-10-15** — Yushu Li, Jiin Woo, Xiaoxiao Li et al. — [Multi-Reward Hacking: From Aggregation-Induced Drift to Trust-Anchored Defense](http://arxiv.org/abs/2610.21404v1)
  <details><summary>📄 Abstract</summary>
  To improve task performance while encouraging desirable response properties, LLM post-training often combines a primary reward (e.g., correctness) with auxiliary rewards (e.g., brevity or efficiency). However, how these rewards are aggregated can critically affect training outcomes. We show that symmetric aggregation, which treats reward channels equally, can induce a failure where aggregate reward improves while primary-task performance degrades, even when individual rewards are meaningful. We ...
  </details>

- **2026-10-15** — Thi-Nhung Nguyen, Viet-Thanh Pham, Linhao Luo et al. — [A Responsibility-Centered Coordination Mechanism for Decentralized Multi-Agent Systems](http://arxiv.org/abs/2610.21243v1)
  <details><summary>📄 Abstract</summary>
  Centralized orchestration provides comprehensive multi-agent coordination but creates bottlenecks in scalability, adaptability, and collective performance. Decentralized approaches alleviate these bottlenecks by distributing coordination across agents, yet often leave responsibility for delegated dependencies and failure recovery unclear. To address this gap, we propose RCM, a responsibility-centered coordination mechanism that leverages commitments to couple task delegation with explicit respon...
  </details>

- **2026-10-15** — Yuge Zhang, Jie Chen, Zhengqiao Zhao et al. — [From Signals to Evidence: Interpretable Underwater Acoustic Target Sensing with Large Language Models - Part I: Framework and Recognition](http://arxiv.org/abs/2610.22064v1)
  <details><summary>📄 Abstract</summary>
  Underwater acoustic target detection and recognition are essential to marine surveillance and intelligent ocean sensing. Despite substantial advances in deep learning, existing systems typically produce binary detection decisions, categorical labels, or scalar confidence scores, offering limited insight into the physical evidence underlying their outputs. Large language models (LLMs) offer an opportunity to move underwater acoustic sensing toward interpretable, evidence-grounded understanding; h...
  </details>

- **2026-10-15** — Olivia Salamon, Virginia N. L. Franqueira, Shujun Li — [Beyond Generation: Using Multimodal LLMs as Detectors of LLM-Generated Deepfake Facial Images](http://arxiv.org/abs/2610.21760v1)
  <details><summary>📄 Abstract</summary>
  As image generation models become increasingly capable of producing highly realistic content, traditional forensic techniques are struggling to keep up. This paper investigates whether MLLMs can instead be used as a form of forensic analysis by identifying synthetic media. Specifically, the study aims to determine whether these models detect fake images by recognising physical inconsistencies, or whether they rely on digital artefacts such as embedded watermarks.Six MLLMs: GPT-4o, GPT-5, GPT-5.2...
  </details>

- **2026-10-15** — Hao Zhang, Hengrui Liu, Lina Sun et al. — [ISW-Agent: Integrating LLM-Driven Dialogue with n8n Workflow for Internal Solitary Wave Remote Sensing Image Processing](http://arxiv.org/abs/2610.21502v1)
  <details><summary>📄 Abstract</summary>
  Internal solitary wave (ISW) remote sensing requires task parameters and spatial information to be transferred across image acquisition, detection, stripe extraction, and propagation prediction. Here, we present ISW-Agent, which integrates large language model (LLM) interpretation with n8n workflows and independent scientific models through structured task constraints, geospatial transformations, and stage-specific output validation. In tests of 120 Chinese instructions per backend, GPT-5.6 Sol ...
  </details>

- **2026-10-15** — Lino Garda Denaro, Chia-Hsiang Lin — [Monotone Piecewise-Linear Harmonization of Multitemporal Multispectral Surface Reflectance With Unsupervised Deep Multiview Pseudoinvariant Features Learning](http://arxiv.org/abs/2610.21183v1)
  <details><summary>📄 Abstract</summary>
  Surface reflectance products derived from optical satellite may exhibit systematic inconsistencies across acquisition dates, because atmospheric correction is generally performed independently for each image. Such residual biases distort the temporal behavior of invariant ground targets and reduce the reliability of multitemporal surface reflectance analysis. This study proposes Deep Multitemporal Generalized Canonical Correlation Analysis (DeepMGCCA), an unsupervised deep multiview pseudoinvari...
  </details>

- **2026-10-15** — Swati Gupta, Tianjiao Li — [When is a better LLM worth paying for? Stochastic Optimization with Switching Mixed-Fidelity Oracles](http://arxiv.org/abs/2610.21139v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used upstream of decision-making to clean data, detect label errors, and reconstruct missing values. Yet LLM-assisted data curation creates a new operational tradeoff: higher-fidelity models and richer prompts can be substantially more expensive, while the value of this additional fidelity depends on the downstream optimization accuracy. This raises the central question of this work: when should one pay for a better LLM, given a specific downstream t...
  </details>

- **2026-10-14** — Dmytro Babarytskyi — [Feasibility Ceilings Before Learning: Sizing and Timing Bounds for Drone-Mesh Interception](http://arxiv.org/abs/2610.20823v1)
  <details><summary>📄 Abstract</summary>
  A mesh of interceptors defending a fixed site must spread over the predicted arrival point of an approaching object. This is a recurring task in multi-agent robotics: N agents, each covering a disc of radius r, spread over a probability density so that a point drawn from it falls within some agent's disc. We give closed forms for the quantities that bound performance before any policy is chosen, and validate each by Monte Carlo. The uncertainty of a point predicted by extrapolating a noisy linea...
  </details>

- **2026-10-14** — Qinglin Su, Licheng Pan, Zhen Fang et al. — [RM-OPD: On-Policy Distillation for Generative Reward Models](http://arxiv.org/abs/2610.20174v2)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning on Mixed-domain preference data (Mix-RL) has become the mainstream approach for training general-purpose Generative Reward Models (GRMs). However, Mix-RL suffers from two critical bottlenecks: the reward sparsity induced by outcome rewards, and the cross-domain interference arising from jointly optimizing heterogeneous capabilities, which together give rise to imbalanced capability acquisition and pervasive reward hacking. Inspired by the success of On-Policy Distillation ...
  </details>

- **2026-10-14** — Sankalp Vaish, Sumukh Veeramalla, Rishank Singh et al. — [CogDrift-4D: Hierarchical Multimodal Modeling of Temporal Behavioral Decay for MCI Detection](http://arxiv.org/abs/2610.20877v1)
  <details><summary>📄 Abstract</summary>
  Early detection of mild cognitive impairment remains a critical bottleneck in dementia care, demanding scalable tools capable of capturing subtle behavioral decay. To capture the subtle temporal changes of cognitive decline, we introduce a behavioral dataset collected across seven unscripted multimodal interactions over an 18-month horizon. This dataset formalizes continuous, multi-session interactions into a dense 4D tensor (Batch * Session * Time * Feature) that explicitly preserves concurrent...
  </details>

- **2026-10-14** — Stephen Fernandes, Narayan Choudhary — [Anuvani-Diarization: Zero Shot Speaker Diarization and Annotation Conventions Across 22 Languages](http://arxiv.org/abs/2610.20327v2)
  <details><summary>📄 Abstract</summary>
  India's 22 scheduled languages are spoken by over a billion people in conversations that mix languages, often within one turn, overlap freely, and take place over telephones, in meetings, and in media. Knowing who spoke when, the task of speaker diarization, is essential to speech applications for such conversation: voice agents conversing with several people at once, speaker attributed transcription of meetings and calls, contact center analytics, and media monitoring. We present a systematic s...
  </details>

- **2026-10-14** — Weichen Lyu, Chong Xia, Mingyu Dong et al. — [PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition](http://arxiv.org/abs/2610.20560v1)
  <details><summary>📄 Abstract</summary>
  3D object composition is pivotal to digital content creation and robot simulation, while also serving as a critical testbed for physical intelligence in foundation models. Previous methods either leverage large language models to directly predict object coordinates, or utilize generative diffusion priors to synthesize composite images for visual alignment, both of which rely on static priors in digital spaces. However, these methods consistently struggle with complex compositions such as precise...
  </details>

- **2026-10-14** — Ali Zamani, Soroush Esfahanian, Erfan Shahabi et al. — [PerSo: Investigating Facets of LLMs' Social Intelligence in Real-World Persuasion Scenarios](http://arxiv.org/abs/2610.20548v1)
  <details><summary>📄 Abstract</summary>
  Understanding the social intelligence of large language models (LLMs) is increasingly important for applications involving human-AI interaction and multi-agent environments. Social intelligence comprises two aspects: cognitive intelligence, the ability to infer others' mental states, and behavioral intelligence, the ability to select appropriate social actions based on these inferences to achieve social goals. Persuasion provides a natural testbed in which both aspects are simultaneously at play...
  </details>

- **2026-10-14** — Qinglin Su, Licheng Pan, Zhen Fang et al. — [RM-OPD: On-Policy Distillation for Generative Reward Models](http://arxiv.org/abs/2610.20174v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning on Mixed-domain preference data (Mix-RL) has become the mainstream approach for training general-purpose Generative Reward Models (GRMs). However, Mix-RL suffers from two critical bottlenecks: the reward sparsity induced by outcome rewards, and the cross-domain interference arising from jointly optimizing heterogeneous capabilities, which together give rise to imbalanced capability acquisition and pervasive reward hacking. Inspired by the success of On-Policy Distillation ...
  </details>

- **2026-10-14** — Xucheng Yu, Haibo Jin, Xiaoqi Wang et al. — [Gap Detection: Mitigating Homogenization through Demand and Defensibility](http://arxiv.org/abs/2610.20162v1)
  <details><summary>📄 Abstract</summary>
  Language models often produce semantically similar answers to open-ended questions, even when many plausible alternatives exist. Generating useful alternatives requires identifying both what the query calls for and what existing responses already cover. We introduce Gap Detection, a framework that searches for relevant but unoccupied directions in a shared text embedding space. Its objective, GapScore, combines query relevance (Demand) with dissimilarity to the nearest existing item (Defensibili...
  </details>

- **2026-10-14** — Alireza Mirrashid, Mohammad Khoshbin, Ali Atghaei et al. — [Attention-Based Spatio-Temporal Approach for Fire and Smoke Detection](http://arxiv.org/abs/2610.20141v1)
  <details><summary>📄 Abstract</summary>
  In various industries, smoke and fire are two of the most important threats in the workplace. One of the common methods for detecting smoke and fire is the use of infrared thermal and smoke sensors, which cannot be used in outdoor applications. Therefore, the use of vision-based methods seems necessary. The problem of smoke and fire detection is spatiotemporal and requires spatiotemporal solutions. This paper presents a method that uses spatial features along with temporal-based features to dete...
  </details>

- **2026-10-14** — Hongyu Ding, Kanyu Xu, Mingjia Chen et al. — [HM3D-M3: A Benchmark for Multi-Agent, Multi-Modal, Multi-Object Goal Navigation](http://arxiv.org/abs/2610.20121v1)
  <details><summary>📄 Abstract</summary>
  Rapid progress in AI agents and robotics makes it a matter of the near future that humans are served by a team of robots. Such a team will receive several goals at once, each specified in whatever form is convenient for the human, such as a category name, a photo, or a spoken description. Existing benchmarks study multi-agent, multi-modal, and multi-object goal navigation in isolation, and a benchmark that places all three in one episode is missing. To fill this gap, we introduce HM3D-M3. A team...
  </details>

- **2026-10-14** — Shuaijie Ma, Yongkang Hu, Yu Cheng et al. — [Safe-FCL: Continual Risk Awareness and Fine-Grained Safety Aggregation for Federated Continual Learning of LLMs](http://arxiv.org/abs/2610.19968v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning enables large language models (LLMs) to learn collaboratively from distributed client data, but malicious client updates can compromise global model safety. As federated tasks evolve, changing malicious update patterns challenge the ability of existing defenses to maintain reliable risk detection over time. To address this challenge, we propose Safe-FCL, a framework integrating continual risk awareness with fine-grained safety aggregation for federated continual learning of...
  </details>

- **2026-10-14** — Binghui Wu, Yeo Zi Yi, Darren Tan et al. — [DarKnight: Retrieval-Guided Agentic Framework for Breaking Dark Web CAPTCHA Gates](http://arxiv.org/abs/2610.19830v1)
  <details><summary>📄 Abstract</summary>
  Cyber Threat Intelligence (CTI) investigators who monitor dark web marketplaces for leaked credentials and breach listings must pass the diverse CAPTCHAs that operators deploy to block automated collection. Existing solvers either need unscalable per-site fine-tuning or rely on commercial Vision-Language Model (VLM) APIs, which surrender operational sovereignty: provider policies, Tor-exit blocking, government regulation, or model updates outside the investigator's control can halt or alter the ...
  </details>

- **2026-10-14** — Angelo Ferrando — [One Monitor Does Not Fit All: Formalism-Agnostic Runtime Verification for Agentic AI](http://arxiv.org/abs/2610.19818v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems combine model decisions, mutable state, tool calls, and delegation to external agents. Monitoring them requires observations from different execution boundaries, while prevention requires control before an operation produces its effect. We present AgenticRV, a runtime-verification architecture that separates these boundaries from the monitoring formalism. Adapters emit canonical events; each monitor receives its own projection and abstraction; and a decision policy uses normal...
  </details>

- **2026-10-14** — Ashish Acharya, Aman Al Amin, Hong Qin — [Structure Before Intelligence: Gating What Agentic Scientific Workflows Release](http://arxiv.org/abs/2610.19507v1)
  <details><summary>📄 Abstract</summary>
  An agentic scientific workflow can run to completion and still release wrong results: a silent numerical error, a stale input, or a defect in a shared upstream step can contaminate several outputs while a sibling branch stays correct. We treat trust in such results as a release decision. A harness around the workflow's directed acyclic graph (DAG) decides which outputs may be used: it enforces mandatory checks, contains failures to the affected branch, recomputes from tracked versions, adds vali...
  </details>

- **2026-10-14** — Wei-Liang Liu, Cheng-Yen Tsai — [What You Sign Is Not What You Run: The Verifiability Gap in Quantized LLM Supply Chains](http://arxiv.org/abs/2610.19498v1)
  <details><summary>📄 Abstract</summary>
  Model signing authenticates the full-precision weights W an LLM is released with, yet users run a quantized artifact Q whose producing transformation is not uniquely determined under current disclosure. We separate the non-environment inputs from the execution environment E and measure a quantity that, to our knowledge, has not been measured before: the Independent Verifiability Rate (IVR), the fraction of a popularity-sampled GGUF ecosystem that a third party can re-derive bit-for-bit. Across t...
  </details>

- **2026-10-14** — Di Wu, Xu He, Shu Wang et al. — [BenchChecker: Assessing the Credibility of Bug-Fixing Benchmarks for LLMs](http://arxiv.org/abs/2610.19447v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) show promise for Automatic Program Repair (APR), existing benchmarks suffer from data contamination, in which test samples appear in training sets, artificially inflating performance. To address this, we propose BenchChecker, a framework compatible with both open-source and closed-source models that supports more credible evaluation by detecting such contamination. Grounded in the observation that persistent patches likely remain in recent repository snapshots ...
  </details>

- **2026-10-14** — Guanhua Zhu, Hanwen Li, Zhi Wei et al. — [STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents](http://arxiv.org/abs/2610.19386v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can self-evolve at test time by accumulating experience: retrieving relevant memories before acting and writing new lessons back afterwards. Yet most are single-level: trajectories, distilled workflows and reasoning items all land in one undifferentiated pool indexed by embedding similarity, with no typed abstraction hierarchy. They never forget or deduplicate, and are prone to negative transfer, where a superficially similar but directionally opposite experienc...
  </details>

- **2026-10-14** — Kiyanoush Nazari, Luchen Li, Haoshu Fang et al. — [Tactile-Guided Robot Learning: From Representation Learning to Foundation Models](http://arxiv.org/abs/2610.20134v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing is becoming central to robust, adaptive, and dexterous robotic manipulation. Beyond its traditional role in contact detection and reactive control, touch is increasingly used to learn transferable representations, condition manipulation policies, and support embodied physical reasoning. Yet existing surveys largely emphasize tactile hardware and perception, leaving the rapid shift toward learning-based tactile manipulation insufficiently synthesized. This paper reviews tactile-gu...
  </details>

- **2026-10-14** — Yanni Mei, Samuel Hartenstein, Jonas Wombacher et al. — [ShadAR: Real-time Prompting On-demand Visual Augmentation in Augmented Reality](http://arxiv.org/abs/2610.19998v1)
  <details><summary>📄 Abstract</summary>
  Augmented Reality can reshape our visual perception (e.g., simulating color blindness) yet such effects are typically pre-programmed by experts, making visual augmentation static and inflexible. We introduce ShadAR, an AR system that allows users to describe expected visual augmentations (e.g., "Blur all people") for changing their vision in real time. ShadAR can graphically manipulate AR passthrough in real time via shader injection. When receiving a user's prompt, ShadAR uses LLMs (GPT5.2) to ...
  </details>

- **2026-10-14** — Hasan Amin, Zhuoran Lu, Ming Yin — [Likelihood Is Not Authorship: Can We Reliably Measure Human Contribution in AI-Assisted Writing?](http://arxiv.org/abs/2610.19767v1)
  <details><summary>📄 Abstract</summary>
  AI-text detection generally asks whether a machine wrote a text. As AI becomes an increasingly integral and accepted part of writing, the more relevant question is no longer whether AI was used, but how much of the text reflects human contribution. A prominent line of work estimates this by measuring how predictive a person's prompt is of the final text. We show that this measure can be easily manipulated. We introduce SPECIFICITY PADDING that simply asks the model to copy a few random IDs from ...
  </details>

- **2026-10-14** — Stephen Fernandes, Narayan Choudhary — [Anuvani-Diarization: Zero Shot Speaker Diarization and Annotation Conventions Across 22 Languages](http://arxiv.org/abs/2610.20327v1)
  <details><summary>📄 Abstract</summary>
  India's 22 scheduled languages are spoken by over a billion people in conversations that mix languages, often within one turn, overlap freely, and take place over telephones, in meetings, and in media. Knowing who spoke when, the task of speaker diarization, is essential to speech applications for such conversation: voice agents conversing with several people at once, speaker attributed transcription of meetings and calls, contact center analytics, and media monitoring. We present a systematic s...
  </details>

- **2026-10-14** — Jingqin Tang, Tim Tomov, Sebastian Schmidt et al. — [What Is a Clarification? Estimating Model-Dependent Input Ambiguity](http://arxiv.org/abs/2610.20052v1)
  <details><summary>📄 Abstract</summary>
  Ambiguous inputs can admit multiple interpretations, each potentially yielding a different answer. Existing work largely treats this ambiguity as a property of the input, yet for a particular language model, only some alternatives may be known and answerable. We therefore distinguish world ambiguity, capturing all alternatives admitted by an input, from model ambiguity, capturing those accessible to the responding model. To characterize these alternatives, we formalize natural-language clarifica...
  </details>

- **2026-10-14** — Kristoffer Hjelmen Nesland, Bjarne Grimstad, Antorweep Chakravorty et al. — [Text-Informed Training Data Filtering for Enhanced Virtual Flow Meter Performance](http://arxiv.org/abs/2610.19860v1)
  <details><summary>📄 Abstract</summary>
  In sectors such as energy, aquaculture and chemical processing, the effectiveness of both mechanistic and data-driven models is frequently limited by poor-quality training data, which obscures underlying physical laws and degrades predictive accuracy. Such quality issues commonly manifest as anomalies in the dataset, ranging from sensor faults to process upsets and incorrect operator inputs. While traditional rule-based filtering can remove a subset of the anomalies, it is unable to leverage con...
  </details>

- **2026-10-14** — Titouan Sérandour, Anne-Laure Méalier, Bruno Colicchio et al. — [Identifying Planetary Nebulae Candidates from IPHAS and VPHAS+ Surveys via YOLO Deep Learning Models](http://arxiv.org/abs/2610.19760v1)
  <details><summary>📄 Abstract</summary>
  We present a deep learning detection method capable of effectively identifying planetary nebulae (PNe) on IPHAS and VPHAS+ surveys. Our detection pipeline is based on the YOLO architecture and is adaptable to other datasets. Using the HiPS system, we preprocess and augment the $r$, $i$, and $Hα$ bands to produce two red, green, and blue (RGB) image datasets: (1) $640 \times 640$ px images at full resolution, and (2) $1 280 \times 1 280$ px images designed to capture extended objects up to $0.2$ ...
  </details>

- **2026-10-14** — Md Rayhanul Masud, S M Maksudul Alam, Mohammad Jaminur Islam — [BANGLAPLAN: A Benchmark for Constraint-Based Planning and Decision-Making in Bangla](http://arxiv.org/abs/2610.19704v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly help users arrange appointments, plan journeys, and allocate limited resources. These tasks require models to satisfy constraints on time, cost, capacity, and order, or determine that no feasible solution exists. Bangla is the world's seventh most widely spoken language, and existing benchmarks cover many language and reasoning tasks. However, benchmarks for evaluating planning and decision-making in Bangla under explicit constraints remain lacking. We i...
  </details>

- **2026-10-14** — Jun Yang, Yumeng Cao, Yingxuan Xiao et al. — [ESL-former: Event Sparse Linear Transformer for FPGA-Accelerated Malware Detection](http://arxiv.org/abs/2610.19665v1)
  <details><summary>📄 Abstract</summary>
  Transformer based intrusion detection has shown strong potential for identifying unknown malware variants, but its deployment on resource constrained edge devices remains difficult due to the high computational and memory cost of self attention. This paper presents an event sparse Linear Transformer framework for malware detection on FPGA edge platforms. Instead of relying on an explicit attention matrix, the proposed method derives token and channel importance directly from the accumulated key ...
  </details>

- **2026-10-14** — Haoxiang Rao, Fang Zhao, Zhao Wang et al. — [CORE: Contrast-and-Reflect for Self-Supervised Prompt Optimization in Anomaly Synthesis](http://arxiv.org/abs/2610.19610v1)
  <details><summary>📄 Abstract</summary>
  Industrial anomaly detection (AD) is bottlenecked by the scarcity of anomalous samples, making high-fidelity anomaly synthesis crucial for improving downstream performance. However, existing methods either rely on scarce real anomaly references or auxiliary data, while lacking complex reasoning and iterative optimization capabilities for generating realistic defects in open-set scenarios. To address these challenges, we propose CORE, a cost-efficient and training-free prompt optimization framewo...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 49 papers

- **2026-10-16** — Yinuo Xu, Jadie Adams, Brian Hu et al. — [VISTA: Steering LLMs with Latent User Values Inferred from a Few Survey Answers](http://arxiv.org/abs/2610.23702v1)
  <details><summary>📄 Abstract</summary>
  Personalizing a language model requires knowing what a person values, which stays largely consistent across tasks. Yet most methods either learn task-specific preferences or place the user's profile in the prompt, where models struggle to act on it. We introduce VISTA (Value-Informed Steering and Targeted Acquisition), which infers a latent profile from users' (full or partial) survey answers, and maps the profile through a hypernetwork to a user-specific steering intervention in a frozen LLM to...
  </details>

- **2026-10-16** — Tianyang Liu, Jiayue Wang, Zhanhao Cheng et al. — [LocalIntent: Outcome-Specific Structured Generation for Backend-Compatible Smart Building Automation with Local LLMs](http://arxiv.org/abs/2610.23511v1)
  <details><summary>📄 Abstract</summary>
  Locally deployed large language models (LLMs) can reduce reliance on remote cloud services for natural language smart building automation, but backend-facing processing requires correct outcome selection, alignment with local capabilities, and valid structured outputs. We investigate whether a complete outcome-specific prompting design improves compact-model outputs beyond generic route-then-generate prompting. The proposed LocalIntent approach routes requests to ordinary or persistent-rule bran...
  </details>

- **2026-10-16** — Qizhen Lan, Yiling Ma, Ruiqi Chen et al. — [When Evidence Vanishes: Distilling Visual-Evidence Dependency in Medical Vision-Language Models](http://arxiv.org/abs/2610.23469v1)
  <details><summary>📄 Abstract</summary>
  Compact medical vision-language models (VLMs) can answer clinical questions correctly without reliably using the image, relying instead on question wording or learned priors. Standard knowledge distillation copies a teacher's answer preference on the original image, but it leaves unchecked whether that preference is conditional on the visual evidence required by the question. We study this missing target as medical visual evidence dependency: support for the correct answer should decrease when t...
  </details>

- **2026-10-16** — Cheng Fan, Han Wu, Tingzhang Luo et al. — [GeoReason: Bridging Logical Reasoning and Spatial Fidelity in Remote Sensing Segmentation](http://arxiv.org/abs/2610.23416v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have significantly advanced instruction-driven perception through the "Embedding-as-Mask" paradigm. However, extending this capability to Remote Sensing (RS) reasoning segmentation remains exceptionally challenging under cluttered geographical contexts and extreme scale variations, often leading to Spatial Fidelity Degradation and Target Misidentification. We identify a critical yet underexplored bottleneck: the sequential alienation of the segmentation t...
  </details>

- **2026-10-16** — Zirui Chen, Ziqing Xing, Zhaoyang Zhang et al. — [AWM: An All-in-One Wireless Foundation Model for Multi-User Channel Acquisition and Localization Without Downstream Tuning](http://arxiv.org/abs/2610.23403v1)
  <details><summary>📄 Abstract</summary>
  Wireless foundation models (WFMs) seek to unify diverse wireless tasks and scenarios, yet existing methods still rely on task- or scenario-specific components or deployment-time fine-tuning. This paper presents an all-in-one wireless model (AWM), a WFM that unifies multi-user channel acquisition and localization, despite their distinct data modalities and functional objectives. We reveal that user location and channel state information (CSI) at different frequencies can be viewed as attribute-sp...
  </details>

- **2026-10-16** — Jiawei Geng, Zhenyang Liu, Yuzheng Wu et al. — [Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation](http://arxiv.org/abs/2610.23378v1)
  <details><summary>📄 Abstract</summary>
  Robots manipulating objects in clutter must decide not only how to act, but also where to look. Although active camera motion can expose an occluded target, it may move the robot into an initial observation-state distribution that differs from the manipulation policy's training distribution. We identify this problem as first-frame distribution sensitivity: under perturbed starts in LIBERO, naively prepending camera repositioning to pi_0.5 reduces success from 46.3% to 11.5%. We introduce ActiveA...
  </details>

- **2026-10-16** — Dongyoon Hahm, Woogyeol Jin, Dennis Wei et al. — [Behavioral Couplings: From Formation to Behavioral Emergence in Language Models](http://arxiv.org/abs/2610.23847v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning large language models (LLMs) can induce behaviors beyond those explicitly targeted. For example, training a model to respond more warmly can make it more sycophantic, and training it to write insecure code can cause broad misalignment on prompts unrelated to coding. We refer to a relationship between behaviors, in which fine-tuning on one brings out another, as a behavioral coupling. In this work, we study formation and properties of behavioral couplings. We find that when a model is...
  </details>

- **2026-10-15** — Bowei Liu, Xinchen Zhang, Xuhuan Li et al. — [OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World Modeling](http://arxiv.org/abs/2610.22355v1)
  <details><summary>📄 Abstract</summary>
  Generative visual verifiers play a crucial role in advancing multimodal intelligence. To enhance the robustness of visual verifiers in complex multimodal scenarios involving compositional requirements, we move beyond conventional binary verifiers that produce only True/False discrete judgments and introduce a verifier that automatically decomposes complex prompts or environmental rules into fine-grained components and assigns pointwise scores to provide a continuous and more informative critique...
  </details>

- **2026-10-15** — Chen Yang, Jiemin Fang, Fanpeng Meng et al. — [SUPRA-TEX: 3D Generation with Super-Aligned Texture](http://arxiv.org/abs/2610.22352v1)
  <details><summary>📄 Abstract</summary>
  Single image 3D generation aims to dress a given 3D mesh with relightable materials while faithfully preserving the visual details of a reference image. Existing methods either introduce artifacts when fusing inconsistent multi-view predictions or struggle to preserve fine details through implicit image-feature conditioning. To resolve these challenges, we introduce SUPRA-Tex, built on the principle of decoupling visible-material estimation, surface alignment, and observation-guided 3D completio...
  </details>

- **2026-10-15** — Hongchang Liu, Jian Liu, Yujuan Ding et al. — [GeoState: Learning View-Decoupled Geometry States for 3D World Modeling](http://arxiv.org/abs/2610.22343v1)
  <details><summary>📄 Abstract</summary>
  Recent 3D world models increasingly use features from geometry foundation models (GFMs) as predictive world states, benefiting from their rich geometric priors. However, the view dependence of these features entangles scene dynamics with camera-induced variation, making the resulting state evolution harder to predict. We propose GeoState, a view-decoupled geometry representation for predictive 3D world modeling that separates scene-state evolution from camera-dependent observation. Specifically,...
  </details>

- **2026-10-15** — Jiapeng Shi, Qiuxia Hou, Jiaqi Leng et al. — [EVA-Cap: Optimizing Audiovisual Video Captioning via Event-Centric Alignment](http://arxiv.org/abs/2610.22186v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Omni Language Models (OLMs) provide a unified solution for audiovisual video captioning. Nevertheless, existing approaches predominantly treat captioning as an unstructured text generation process, neglecting the inherent semantic structure of videos and leading to suboptimal fine-grained audiovisual alignment. To bridge this gap, we propose EVA-Cap, a novel framework that decomposes captions into atomic audiovisual events and transforms unstructured text supervision into even...
  </details>

- **2026-10-15** — Madhav Iyengar, Andreas Geiger, Hilde Kühne — [Retrofitting Recurrent Vision-Language Models from Pretrained Backbones](http://arxiv.org/abs/2610.22075v1)
  <details><summary>📄 Abstract</summary>
  Recent work shows that depth recurrence can be retrofitted into pretrained language models. In this work, we adapt this paradigm for visual understanding, using depth recurrence to reduce the parameter footprint of a pretrained vision-language model (VLM). To this end, we prune layers from the language backbone of the VLM and loop over a subset of the remaining layers. At each step of the loop, a linear adapter merges the block's output with the token representations from the preceding layers an...
  </details>

- **2026-10-15** — Tongna Chen, Minghan Li, Guodong Zhou — [Aligning LLMs with Sparse Retrieval via Adaptive Sparse Supervision](http://arxiv.org/abs/2610.21877v1)
  <details><summary>📄 Abstract</summary>
  While large language models (LLMs) offer strong semantic representations, their application to first-stage retrieval incurs substantial latency and storage costs. Neural sparse retrievers such as SPLADE provide efficient retrieval but rely on relatively compact encoders with limited representational capacity. To bridge this gap, we propose an LLM-based sparse retrieval framework with input-adaptive sparse alignment. Specifically, we introduce a dynamic $α$-truncation strategy that selects input-...
  </details>

- **2026-10-15** — Shrish Shrinath Vaidya, Gowthamaan Palani, Minmini Selvam et al. — [MedPAO-VL: Interpretable and Protocol-Compliant Agent for Structured Radiology Report Generation](http://arxiv.org/abs/2610.21794v1)
  <details><summary>📄 Abstract</summary>
  Despite the remarkable generalization capabilities of Large Language Models, generating clinically accurate and structured radiology reports from medical images remains a significant challenge. Current end-to-end approaches function as black boxes, prone to factual hallucinations and generating ungrounded findings. This lack of reliability and failure to adhere to domain-specific structuring protocols, fundamentally limits their clinical utility. We present MedPAO-VL, a multimodal agent that shi...
  </details>

- **2026-10-15** — Jia Chen, Zhiyong Yang, Shilong Bao et al. — [Pairwise AUC Optimization Needs Corrective Power: A Unified View](http://arxiv.org/abs/2610.21743v1)
  <details><summary>📄 Abstract</summary>
  Direct pairwise AUC-surrogate training is attractive because it trains toward the ranking metric used at test time, especially under class imbalance. This creates a direct alignment between the training objective and the evaluation metric, but such metric alignment alone does not guarantee that stochastic training remains corrective. We study this gap through Corrective Power: whether pairwise mini-batch updates produce stronger and more reliable improvements for more severe positive-negative ra...
  </details>

- **2026-10-15** — Zejian Kang, Yifu Luo, Boyang Shen et al. — [TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion](http://arxiv.org/abs/2610.21515v1)
  <details><summary>📄 Abstract</summary>
  Language-conditioned humanoid motion generation enables users to create and refine robot movements through natural language. The central challenge is to connect an underspecified request to concrete motion structure that can subsequently be revised relative to an accepted reference. We present TRACE, a generation and editing framework for the Unitree G1 humanoid robot built around typed, measurable kinematic quantities. Our insight is to ground generation conditions in paired training motions an...
  </details>

- **2026-10-15** — Camila Kolling, Mariya Toneva — [Decomposing Brain-LLM Alignment with Interpretable Semantic Representations](http://arxiv.org/abs/2610.21508v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) predict neural responses during naturalistic language comprehension, but the linguistic information underlying this brain alignment remains difficult to interpret. We use SCRIBE, an interpretable contextual semantic representation spanning 65 neurocognitively grounded semantic properties, as a lens for decomposing the brain alignment of one LLM, LLaMA2-7B. Using variance partitioning between LLaMA2-7B and SCRIBE on naturalistic fMRI data from seven participants liste...
  </details>

- **2026-10-15** — Junru Wu, Jingting Zheng, Yuqi Ren et al. — [VALCON: Benchmarking and Enhancing Value Consistency in Large Language Models via Dual-Role Variation](http://arxiv.org/abs/2610.21304v1)
  <details><summary>📄 Abstract</summary>
  Current value alignment evaluations for large language models (LLMs) heavily rely on output compliance, overlooking whether LLMs maintain value consistency when alternating between generator and evaluator roles. Such consistency is increasingly important because modern LLM agents and alignment pipelines often rely on the same LLM to both generate actions and evaluate their acceptability. To mitigate this limitation, we propose VALCON, a role-driven data construction framework that operationalize...
  </details>

- **2026-10-15** — Sunghyun Wee, Geunjae Choi, Hyeonjin Kim et al. — [Fractional Power-of-Two Quantization for Efficient and Effective Multiplier-Free LLM Inference](http://arxiv.org/abs/2610.21257v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) demand efficient inference, where the multiply-accumulate (MAC) operations in linear projections dominate compute and energy cost. Post-training quantization (PTQ) reduces this cost by mapping weights and activations to low-bit integers. Power-of-Two (PoT) weight quantization promises efficient multiplier-free LLM inference via shift-add logic, but suffers significant accuracy degradation at low bitwidths due to its coarse base-2 quantization grid. We introduce Fract...
  </details>

- **2026-10-15** — Xinrui Lin, Shumin Wang, Suqi Song et al. — [FocusOPD: Structure-Guided On-Policy Distillation for Diffusion Models](http://arxiv.org/abs/2610.21250v1)
  <details><summary>📄 Abstract</summary>
  Multi-teacher on-policy distillation enables rectified-flow models with diffusion-transformer architectures to combine task-specific capabilities within a single student. However, matching model outputs does not guarantee that their internal representations are aligned, and it remains unclear where and when additional feature supervision is most useful. We analyze the teacher-student feature mismatch across Transformer blocks and denoising timesteps, and find that the mismatch is concentrated in...
  </details>

- **2026-10-15** — Ziye Mei, Haotian Ma — [Representation Redistribution in Sparse Autoencoders](http://arxiv.org/abs/2610.21240v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) decompose language model activations into sparse features, but prompt transformations designed to preserve the underlying request can redistribute activity across them. A feature change observed on one transformed prompt need not recur, and even a recurring change need not affect a downstream computation. We introduce the redistribution sensitivity score (RSS), which identifies large feature responses that recur in a consistent direction, and evaluate the resulting sup...
  </details>

- **2026-10-15** — Licheng Pan, Haocheng Yang, Haoxuan Li et al. — [Rubric Judgments Lack Uncertainty: Conformal Weighting for LLM Evaluation](http://arxiv.org/abs/2610.21214v1)
  <details><summary>📄 Abstract</summary>
  Rubric-based evaluation is widely used to assess large language model (LLM) outputs by decomposing quality into multiple criteria and assigning each a binary judgment from an LLM verifier. However, judgment certainty varies substantially across criteria. Existing methods uniformly aggregate these judgments into a final score, implicitly treating every criterion as equally certain and overlooking this heterogeneity. As a result, uncertain judgments remain incorporated into reward estimation witho...
  </details>

- **2026-10-15** — Kostas Triaridis, Morris E. Sharp, Nebojsa Jojic — [Mine, Sample, Render: Test-Time Diversity Alignment Of Generative Models](http://arxiv.org/abs/2610.21185v1)
  <details><summary>📄 Abstract</summary>
  Modern generative models produce high-quality individual outputs but struggle to sample diversely, even when explicitly instructed to do so. We introduce MINE-SAMPLE-RENDER (MSR), a test-time approach that externalizes the diversity into an explicit, corpus-derived sampling procedure. Our pipeline (i) mines an interpretable categorical schema from a corpus of real artifacts and supplies statistics for sampling; (ii) samples attribute configurations from the corpus-derived statistics; (iii) uses ...
  </details>

- **2026-10-15** — Licheng Pan, Haocheng Yang, Yuzhou Chen et al. — [CleanRM: Reward Modeling from Noisy Feedback with a Few Clean Feedback for RLHF](http://arxiv.org/abs/2610.21138v1)
  <details><summary>📄 Abstract</summary>
  Feedback noise is pervasive in preference data, arising from subjective human judgments, annotation mistakes, and imperfect LLM judges. Standard reward modeling trained on such feedback yields a biased estimate of the clean risk. Although classical denoising methods are directly applicable to noisy feedback learning, they generally assume a uniform noise ratio across samples. However, this assumption fails for feedback data, where noise is intrinsically sample-wise. To address this challenge, we...
  </details>

- **2026-10-15** — Woocheol Shin, Taeyoung Yun, Jiwon Sung et al. — [Noise-Space Reward Alignment for Few-Step Generative Models](http://arxiv.org/abs/2610.21125v1)
  <details><summary>📄 Abstract</summary>
  Few-step generative models produce high-quality samples in one or a few evaluations. However, steering them toward desired properties remains difficult, especially when only black-box reward evaluations are available. While one could apply approaches developed for iterative diffusion and flow-based models, such as direct RL fine-tuning or test-time scaling, we find that neither transfers well to the few-step regime: direct fine-tuning suffers from severe reward over-optimization, and test-time s...
  </details>

- **2026-10-15** — Mohammad Pedramfar, Siamak Ravanbakhsh — [The Tilted Sampling Problem: Optimism, Posterior Sampling, and Logarithmic Regret](http://arxiv.org/abs/2610.21908v1)
  <details><summary>📄 Abstract</summary>
  Many modern learning systems are used not to select a single best action, but to sample diverse high-quality outputs. Examples include entropy-regularized reinforcement learning, RLHF, and reward-guided generative modeling. Motivated by these settings, we study tilted sampling: an online learning problem in which the goal is to sample from the Gibbs distribution induced by an unknown reward function. We define sampling regret as the temperature-normalized cumulative KL divergence between the lea...
  </details>

- **2026-10-14** — Robert Moseley, Md Kaykobad Reza, Ameya Patil et al. — [MSP: Modality Self-Play for Training Multimodal LLMs Without Paired Cross-Modal Data](http://arxiv.org/abs/2610.20965v1)
  <details><summary>📄 Abstract</summary>
  Large multimodal models have achieved remarkable progress by scaling model capacity and training on massive paired multimodal data. However, this paradigm introduces a fundamental bottleneck: aligned multimodal datasets are expensive to curate, difficult to scale across diverse modality combinations, and increasingly constrain further progress. We introduce Modality Self-Play (MSP), a training framework for multimodal foundation models based on proxy-mediated modality composition. Instead of rel...
  </details>

- **2026-10-14** — Gwénolé Lecorvé, Delphine Charlet, Pierre Adam et al. — [Wolof-Adapted Industry-Ready Open-Weight Language Models](http://arxiv.org/abs/2610.20824v1)
  <details><summary>📄 Abstract</summary>
  Wolof is spoken by 23M people, mostly in Senegal, but remains weakly supported by open-weight language models, while API models raise cost, governance, and sovereignty constraints for local deployments. In this paper, we present 0.6B-14B open-weight models adapted to Wolof through instruction tuning, preference alignment, and model merging. After presenting the pipeline and data, extensive experiments on 63~public and in-house tasks show good performance on Wolof understanding and generation whi...
  </details>

- **2026-10-14** — Saeed Razavi, Xingjian Leng, Liang Zheng — [Representation Conditioning for Generation](http://arxiv.org/abs/2610.20608v1)
  <details><summary>📄 Abstract</summary>
  Representation-alignment methods effectively accelerate the diffusion transformer training. REPA, for example, uses a pretrained vision encoder to supervise an intermediate layer through an MLP projection head which is discarded after training. It aims to import semantics from the vision encoder to the diffusion backbone. While this objective is achieved at early layers by back-propagating the alignment loss, there is no guarantee that later layers, supervised by the velocity prediction loss alo...
  </details>

- **2026-10-14** — Zhefei Gong, Hefeifei Jiang, Zehao Wang et al. — [Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance](http://arxiv.org/abs/2610.20607v1)
  <details><summary>📄 Abstract</summary>
  Mobile Manipulation (MoMa) is a cornerstone of autonomous robotic systems, yet real-world fine-tuning remains a formidable challenge because of high-dimensional action spaces and intricate coupling between heterogeneous modules. In this paper, we propose HiRe-MoMa (Hierarchical Residual Mobile Manipulation), a systematic framework for stable and sample-efficient real-world fine-tuning of complex MoMa systems. At its core, HiRe-MoMa adopts a Hierarchical Residual Architecture that fine-tunes a fr...
  </details>

- **2026-10-14** — Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio André Machado Porto — [Manacá-1B-Instruct-2: Reproducible Safety Alignment for a Native Brazilian-Portuguese LLM. Negative DPO Results, a Controlled Composition Scan, and a Silent Failure Mode of the LLM Judge](http://arxiv.org/abs/2610.20570v1)
  <details><summary>📄 Abstract</summary>
  Brazilian Portuguese remains underserved by open-source language models, and the few that are safety-aligned rarely document what did not work or validate comparisons with statistical significance. We present Manacá-1B-Instruct-2, the second-generation post-training alignment of Manacá-1B (1.72B parameters, trained from scratch for PT-BR), with an SFT corpus of 291,223 examples. We document three DPO attempts, all negative, including a case where the training reward margin reaches 1.0 while free...
  </details>

- **2026-10-14** — Rusali Saha, Nitya Khurana, Ruihong Huang et al. — [ChronoCulture: Evaluating Cultural Awareness Across Time in Large Language Models](http://arxiv.org/abs/2610.20472v1)
  <details><summary>📄 Abstract</summary>
  Cultural attitudes and social norms evolve over time, yet most cultural benchmarks for large language models (LLMs) treat culture as a static attribute of a country or region. We introduce ChronoCulture, a benchmark of 10,360 temporal pairs built from longitudinal survey data across 72 countries. Each pair contains the same survey question asked in the same country in an older and a newer year, with full population response distributions as ground truth. Across six LLMs, we find that models can ...
  </details>

- **2026-10-14** — Nguyen Nguyen, Yongyi Zang — [Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR](http://arxiv.org/abs/2610.20461v1)
  <details><summary>📄 Abstract</summary>
  Character Error Rate (CER), the standard metric for OCR and vision-language models (VLMs), charges a typo as much as a wrong name. We introduce semCER, which keeps CER's alignment and denominator and charges each grapheme edit a severity from an LLM judge, with no word segmentation. Normalized CER keeps the score of a whole transcription, where it tracks readers as well as semCER or better, and semCER breaks that score down into named edits. The charges track readers' ratings edit by edit in Eng...
  </details>

- **2026-10-14** — Dwaipayan Haldar, Indranil Patra, Azhar Yousuf et al. — [SpectrumQuant: Spectrum Alignment for LLM Quantization](http://arxiv.org/abs/2610.20303v1)
  <details><summary>📄 Abstract</summary>
  Orthogonal transforms have emerged as an effective tool for low-bit quantization of large language models (LLMs), as they reshape activation distributions without changing the underlying model function. Existing approaches typically rely either on fixed data-agnostic transforms, such as Hadamard rotations, or on calibration-time optimization of learned rotations. We study rotation selection from first principles and show that maximizing covariance leads to spectral alignment and provides a princ...
  </details>

- **2026-10-14** — Dai Shi, Andi Han, Xiaoyu Li et al. — [From Plato to Aristotle: Toward a General Theory of Representation Hypotheses](http://arxiv.org/abs/2610.20286v1)
  <details><summary>📄 Abstract</summary>
  The Platonic Representation Hypothesis (PRH) holds that increasingly capable models converge toward a common representation. However, recent studies have shown different views on aligning representations via their neighborhoods, spanning trees, and distances. We show that these views can differ because the alignment criteria behind them sit at different points of one lattice, and we formalize this explanation as the Lattice Representation Hypothesis (LRH). Under the LRH, the convergence claimed ...
  </details>

- **2026-10-14** — Jiyu Tian, Mingchu Li, Xiangwei Chen et al. — [Towards Efficient Threat Intelligence Instruction Tuning via Quality-Aware and Optimal Transport-Guided Data Selection](http://arxiv.org/abs/2610.20284v1)
  <details><summary>📄 Abstract</summary>
  High-quality data is essential for improving instruction tuning in threat intelligence analysis. However, existing methods for generating cybersecurity instruction data lack reliable quality assessment mechanisms, and gradient influence-based data selection methods primarily focus on single-sample matching, failing to cover diverse and complex security capabilities. To address these issues, we propose CTI-TDS, a Targeted Data Selection method for instruction tuning in Cyber Threat Intelligence a...
  </details>

- **2026-10-14** — Junlin Chen, Wenhao Wang, Junchao Xu et al. — [MAEM: Mitigating Recency Bias via a Replay-Free, Capacity-Controlled Dynamic Mixture of Experts for Class-Incremental Graph Learning](http://arxiv.org/abs/2610.20238v1)
  <details><summary>📄 Abstract</summary>
  Graph Neural Networks (GNNs) excel on graph-structured data but suffer catastrophic forgetting when classes arrive sequentially. In class-incremental graph learning, predictions are often dominated by recently learned classes, causing severe recency bias. Dynamic expansion can isolate knowledge across sessions, but many methods assume task-incremental settings and require task identities at test time to select branches or heads---information unavailable in class-incremental learning. Learnable r...
  </details>

- **2026-10-14** — Bilal A. Sidiqi, Yipei Wang, Shaheer U. Saeed et al. — [Continual pretraining Prostate MRI ViT Encoder for task alignment](http://arxiv.org/abs/2610.20217v1)
  <details><summary>📄 Abstract</summary>
  Building foundation models for MRI has emerged as a promising direction for advancing medical image analysis and improving accessibility of task specific models. Existing approaches primarily focus on effective pretraining strategies and evaluating their performance across diverse downstream tasks. While these methods show performance gains, limited attention has been given to understanding task alignment between pretraining and downstream objectives. Unlike language models, where the two stages...
  </details>

- **2026-10-14** — Min Xiao, Jin Li, Shoujin Wang et al. — [HEM-Med: A Hierarchical Agentic Memory Framework for Safe Multi-Center Medication Recommendation](http://arxiv.org/abs/2610.20191v1)
  <details><summary>📄 Abstract</summary>
  Medication recommendation (MR) is critical for clinical decision support. While existing MR methods are mostly designed for single-center learning, where only one independent hospital is involved, multi-center MR with hospitals of different scales has become increasingly demanding in practice. In multi center settings, abundant data from large medical centers can improve recommendation performance for low-resource centers. Despite a few preliminary attempts on this task, two critical gaps remain...
  </details>

- **2026-10-14** — Alex Wolf, Pooja Rani, Harald C. Gall — [Temporal Adaptive Fine-Tuning for Code Comprehension](http://arxiv.org/abs/2610.19970v1)
  <details><summary>📄 Abstract</summary>
  Repository-level code comprehension question answering (QA) supports developer reasoning over functionality and usage distributed across codebases. However, repository-specialized large language models (LLMs) can become misaligned as code evolves. We study this challenge as temporal repository adaptation: acquiring new knowledge, suppressing obsolete, retaining still-valid, and preserving semantically neighboring knowledge. Existing retrieval, fine-tuning, and model-editing methods address only ...
  </details>

- **2026-10-14** — Ridong Zhang, Shuxian Liang, Chaoqun Wan et al. — [How GUI Agents Fail: GraceBench for Execution Stability Diagnosis](http://arxiv.org/abs/2610.19900v1)
  <details><summary>📄 Abstract</summary>
  As GUI agents are increasingly deployed for mobile task automation, their reliability depends not only on final task outcomes, but also on whether they reach these outcomes through stable interaction trajectories. In automation workflows, unnecessary actions, detours, and execution errors can add noise to collected data, introduce irreversible side effects, or undermine trust, even when the agent eventually completes the task. It is therefore important to systematically diagnose the execution st...
  </details>

- **2026-10-14** — Mikołaj Piórczyński, Wojciech Masarczyk, Damian Sójka et al. — [On the Limits of Representation-Based Test-Time Adaptation for Multimodal LLMs](http://arxiv.org/abs/2610.19892v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models suffer significant accuracy drops under common corruptions. While test-time adaptation (TTA) successfully mitigates these shifts in CLIP-like contrastive models, its application to generative multimodal large language models (MLLMs) remains underexplored and uniquely challenging due to their sequential token generation. In this work, we demonstrate that representation-based TTA fails to recover performance in MLLMs. Our experiments reveal that even when violating standard ...
  </details>

- **2026-10-14** — Siwei Meng, Xuerou Cai, Rui Hu et al. — [PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA](http://arxiv.org/abs/2610.19823v1)
  <details><summary>📄 Abstract</summary>
  Text-to-video (T2V) generation models can produce visually realistic videos that nevertheless violate the physical consequences implied by the prompt and scene. Existing benchmarks largely rely on holistic plausibility scores or broad quality dimensions, leaving it unclear which physical behavior is being tested and why a model fails. We introduce PhyMetric, a scene-level diagnostic benchmark that recasts physical plausibility evaluation as verifiable, scene-grounded question answering. PhyMetri...
  </details>

- **2026-10-14** — Huining Yuan, Xiangmin Yi, Zelai Xu et al. — [ActionOPD: Distilling Decisions, Not Tokens](http://arxiv.org/abs/2610.19820v1)
  <details><summary>📄 Abstract</summary>
  Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and at what granularity should this alignment be performed? Offline imitation provides dense but token-specific supervision and can suffer from state-distribution mismatch. Token-level on-policy distillation (OPD) addresses this mismatch but typically requires teacher token probabilities and compatible tokenization. We argue...
  </details>

- **2026-10-14** — Enrico Liscio, Anne Arzberger, Aditya Shankar et al. — [Model vs. User: Whose Values Prevail? Inference-Time Value Alignment in Multi-Turn Conversations](http://arxiv.org/abs/2610.19817v1)
  <details><summary>📄 Abstract</summary>
  Human values shape how we expect language models to behave. Dominant alignment approaches treat values as global objectives, although the appropriate value orientation is personal and contextual. Training-free alignment can steer models toward target values at inference time, yet has been largely evaluated in single-turn settings and with a single steering direction (e.g., toward safety). We evaluate four prompt- and activation-based steering methods in multi-turn conversations, where user and a...
  </details>

- **2026-10-14** — Julia Barth, Armin Sommer, Kunvar Thaman et al. — [What Happens to the Goal? Distinct Failures of Policy Alignment in Goal Misgeneralization](http://arxiv.org/abs/2610.19731v1)
  <details><summary>📄 Abstract</summary>
  Goal misgeneralization is a common failure mode in which an agent behaves competently out of distribution but does not pursue the intended goal. However, we still have a weak understanding of what happens to the intended goal in misgeneralizing agents. Across three Procgen environments and five robot tasks, we find three distinct forms of policy-goal misalignment: (1) functional target substitution, where behavior follows an alternative goal, (2) a policy shortcut, where behavior follows a learn...
  </details>

- **2026-10-14** — Jing-Xuan Zhang, Genshun Wan, Jianqing Gao et al. — [Learning Visual Speech Representations via Cross-Modal Distillation and Joint Face-Lip Modeling](http://arxiv.org/abs/2610.19559v1)
  <details><summary>📄 Abstract</summary>
  Lipreading remains challenging due to the inherent ambiguity of visual speech cues and their sensitivity to head pose and video resolution. In this work, we propose FLARE, a framework for robust visual speech representation learning via cross-modal distillation and joint face-lip modeling. FLARE leverages semantically rich Whisper representations as the acoustic teacher signal, converting them into discrete distillation targets through a random-projection quantizer and pretraining the model with...
  </details>

- **2026-10-14** — Kyusong Lee, Heting Ying, Tiancheng Zhao — [VLX-Go: Robust Embodied Tracking through Multi-Stage Learning and On-Policy Refinement](http://arxiv.org/abs/2610.19361v1)
  <details><summary>📄 Abstract</summary>
  Embodied visual tracking requires a robot to identify a designated target from visual observations and control its own motion to follow that target through an environment. Following an isolated person is a comparatively simple demonstration of embodied visual tracking, but following the intended person among distractors remains challenging. Existing methods exhibit a substantial drop in success from single-target to distractor tracking, motivating a focus on the shared spaces that person-followi...
  </details>

- **2026-10-14** — Zixiao Wang, Xingbo Du, Duzhen Zhang et al. — [Rent-Seeking Language Models: Reward Models Set the Prices, Frequent Audits Curb the Rent](http://arxiv.org/abs/2610.19832v1)
  <details><summary>📄 Abstract</summary>
  Reward model overoptimization in RLHF is usually described as reward hacking. We recast it as rent-seeking: the policy, a firm, earns reward from a regulator, the proxy reward model, that true quality does not back. The lens turns overoptimization into measurable quantities, namely rent, a capture index and deadweight loss, and into testable predictions from the economics of regulation. In a fixed, version-controlled testbed with three model families, accuracy-matched proxy reward models and two...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 62 papers

- **2026-10-16** — Shicheng Liu, Krista Opsahl-Ong, Andrew Drozdov et al. — [AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery](http://arxiv.org/abs/2610.23845v1)
  <details><summary>📄 Abstract</summary>
  Reproducible and analytically robust research findings are essential to scientific progress, but evaluating these properties typically requires costly manual effort. We investigate whether LLM agents can help automate reproduction and robustness analysis, using a medical case study grounded in the Surveillance, Epidemiology, and End Results (SEER) database, a widely used U.S. cancer registry underlying tens of thousands of published studies. First, we introduce SEER-Repro, a benchmark of 20 publ...
  </details>

- **2026-10-16** — Ravil Mussabayev, Saveliy Zavertyaev, Dmitriy Parpulov et al. — [SIT-Eval: Situation-Based Interactive Turn-by-Turn Evaluation of Conversational Agents](http://arxiv.org/abs/2610.23612v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of conversational AI agents necessitates evaluation methods that assess performance across diverse dialogue scenarios, utilizing multiple situational criteria, as appropriate behavior depends on context and encompasses various aspects. Existing dialogue benchmarks typically use static natural conversations, which underrepresent rare situations---a critical safety gap, as low-probability events become frequent failures at production scale. However, limited sample sizes for...
  </details>

- **2026-10-16** — Jinho Choi, Hyesu Lim, Jaegul Choo et al. — [Beyond SAEs: Consistent Concept Discovery with Sparse Coding](http://arxiv.org/abs/2610.23801v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) explain foundation model representations by decomposing activations into sparse combinations of learned dictionary atoms. However, the learned dictionaries can vary across training runs, limiting the reliability and reproducibility of SAE-based analyses. We propose Consistent Sparse Dictionary Learning (ConSDL), which replaces the standard linear encoder with per-sample sparse coding. This is motivated by our synthetic analysis showing that coefficients from a single l...
  </details>

- **2026-10-16** — Lisette Espín-Noboa, Mingrong She, Ana Maria Jaramillo et al. — [Bridging the Language Gap in Scholarly Data II: Enhancing Gender Inference for Chinese Names](http://arxiv.org/abs/2610.23734v1)
  <details><summary>📄 Abstract</summary>
  Perceived gender inference from names is important for inclusive scientometrics research, yet existing methods perform poorly on non-Western scholars. We address this gap for Chinese names, which appear in two forms, Hanzi and Pinyin, its Romanized form (e.g., Zhang Wei, Li Na). In international bibliographic records, names are often available only in Pinyin. However, a single pinyin name can correspond to multiple distinct hanzi characters with different gender associations, so gender inference...
  </details>

- **2026-10-16** — Syed Md. Ahnaf Hasan, Md Akil Raihan Iftee, Sajib Mistry et al. — [FedRAPP: Federated Test-Time Prompt Tuning for Vision-Language Models with Reliability-Aware Prompt Personalization](http://arxiv.org/abs/2610.23705v1)
  <details><summary>📄 Abstract</summary>
  Federated prompt learning enables vision-language models like CLIP to collaboratively adapt lightweight soft prompts across distributed clients without sharing raw data. However, existing federated prompt learning methods are designed primarily for supervised settings with labeled client data and assumed relatively stable training distributions. At test time, source-free federated prompt tuning remains largely unexplored. Clients may receive unlabeled target samples with heterogeneous, often non...
  </details>

- **2026-10-16** — Séverin Baroudi, Yanis Labrak, Petr Motlicek et al. — [Beyond the Benchmark: Conditioning, Domains and Failure Modes of Qwen3-TTS](http://arxiv.org/abs/2610.23678v1)
  <details><summary>📄 Abstract</summary>
  Qwen3-TTS reports state-of-the-art zero-shot voice cloning, but its technical report leaves open how the model should be conditioned, how it behaves outside read speech, and how it fails. We characterise its two cloning interfaces, in-context learning (ICL) and X-Vector, against Chatterbox, XTTS-v2 and F5-TTS on read, meeting, emotional and air-traffic-control (ATC) speech, using eighteen objective measures, an LLM judge, a spoofing countermeasure and a listening test. Neither interface dominate...
  </details>

- **2026-10-16** — Marco Boresta, Tommaso Giovannelli, Sepehr Namirad et al. — [On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria decision-making in healthcare operations management](http://arxiv.org/abs/2610.23673v1)
  <details><summary>📄 Abstract</summary>
  Multi-criteria models for healthcare operations need weights that express how stakeholders trade off patient waiting time, provider workload, and operating cost, but these weights are difficult to quantify. Teams of large language model (LLM) agents, each prompted to represent a stakeholder, have been used to supply them. We propose a framework for assessing the reliability of LLM-generated preferences as inputs to multi-objective optimization and quantifying how their uncertainty affects decisi...
  </details>

- **2026-10-16** — Quentin Delfosse, Raban Emunds, Paul Seitz et al. — [JAXtari: High-Throughput and Easy-to-Modify Arcade Learning Environment](http://arxiv.org/abs/2610.23650v1)
  <details><summary>📄 Abstract</summary>
  The Arcade Learning Environment (ALE) has been a cornerstone of Deep Reinforcement Learning research, providing a standardized benchmark for evaluating general agents. However, its lack of native support for object-extraction and environment modification restricts research into evaluating whether agents learn robust causal models or rely on brittle visual heuristics. Furthermore, the ALE's dependence on CPU-based emulation creates a significant bottleneck in modern GPU-accelerated training pipel...
  </details>

- **2026-10-16** — Xuhan Tong, Yuchen Zeng, Jiawei Zhang — [Out of Support, Not Out of Reach: In-Context Learning with Unsupported Instructions and Composed Tasks](http://arxiv.org/abs/2610.23528v1)
  <details><summary>📄 Abstract</summary>
  In-Context Learning (ICL) enables pretrained LLMs to adapt to downstream tasks from a small set of input-output demonstrations, without parameter updates. Yet existing theory primarily explains ICL as identifying a latent task already represented in pretraining, leaving unclear whether ICL can succeed when either the instruction or the target task falls outside the pretraining support. We develop a theoretical framework under mild assumptions that separates these two forms of distribution shift....
  </details>

- **2026-10-16** — Yifan Guo, Zhu Wang, Qian Qin et al. — [mmPencil: Toward Writing-Style-Independent In-Air Handwriting Recognition via mmWave Radar and Large Vision-Language Model](http://arxiv.org/abs/2610.23419v1)
  <details><summary>📄 Abstract</summary>
  In-air handwriting recognition based on radio frequency (RF) signals offers a promising solution for human-computer interaction, yet existing methods are often limited by predefined writing planes, constrained writing styles, and small recognition vocabularies. To address these limitations, we propose m^2VLMs, a modality mapping architecture that bridges millimeter-wave (mmWave) radar sensing and large vision-language models (VLMs), and develop mmPencil, a 3D in-air handwriting word recognition ...
  </details>

- **2026-10-15** — Tao Duan, Junzhou Zhao, Jianglong Li et al. — [MAppPrint: Robust and Real-time Mobile App Fingerprinting via Traffic Behavior Correlation Graphs](http://arxiv.org/abs/2610.22148v1)
  <details><summary>📄 Abstract</summary>
  Mobile apps have become ubiquitous in daily life. Despite communication encryption, app fingerprinting (AF) attacks can still enable adversaries to infer the apps in use by analyzing patterns of encrypted network traffic. However, existing AF attacks suffer from three critical limitations that hinder their practical effectiveness: (i) the inability to capture app-specific traffic dependencies, rendering traffic fingerprints fragile under dynamic networking conditions; (ii) the neglect of latency...
  </details>

- **2026-10-15** — Yuanjian Xu, Jinyi Han, Jianing Hao et al. — [AgentPerturb: Evaluating LLM Agent Robustness under Controlled Interaction Perturbations](http://arxiv.org/abs/2610.21624v1)
  <details><summary>📄 Abstract</summary>
  Real-world tasks are often complex and noisy, posing substantial challenges for LLM agents. Yet existing evaluations lack a systematic framework for jointly characterizing potential perturbation targets and types. We use this two-dimensional view to conduct a unified study that quantifies the robustness of current frontier models, traces the mechanisms behind perturbation-induced failures, and draws implications for robustness-oriented training. Through controlled evaluations on APEX-Agents and ...
  </details>

- **2026-10-15** — Huaien Zhang, Zhengjie Zhao, Yu Pei et al. — [Evaluating and Improving Static Application Security Testing Tools for Rust](http://arxiv.org/abs/2610.21373v1)
  <details><summary>📄 Abstract</summary>
  Rust has become a popular systems programming language in recent years because of its strong guarantees on memory and concurrency safety. Many types of system software have been re-implemented in Rust. However, Rust programs can still suffer from common memory and concurrency vulnerabilities due to unsafe code and misunderstandings of its complex mechanisms. To mitigate such vulnerabilities, developers often rely on static application security testing (SAST) tools. However, the effectiveness of ...
  </details>

- **2026-10-15** — Zanwu Liu, Dan Zhang, Xiaodi Wang et al. — [Stop Training Against Soft Users: Mentalized Adversarial Self-Play for Proactive Dialogue](http://arxiv.org/abs/2610.21156v1)
  <details><summary>📄 Abstract</summary>
  Proactive dialogue agents must guide multi-turn interactions toward task goals while adapting to users whose intentions and attitudes evolve. Existing planners improve system side action selection through search, learned policies, or user aware planning, but are often trained and evaluated against fixed or overly compliant simulators; as a result, high simulated success can reflect soft user bias rather than robust dialogue ability. We introduce MASP, a Mentalized Adversarial Self Play framework...
  </details>

- **2026-10-15** — Madison Book, Justin Bradley — [Robust Multi-Agent Pursuit with Preemptive Communication via Reachability-Based Control Barrier Functions](http://arxiv.org/abs/2610.22198v1)
  <details><summary>📄 Abstract</summary>
  Safe multi-agent coordination typically assumes what real-world, deployed, resource-constrained robots cannot provide: continuous, perfect state sharing. Robust control strategies must be complemented with robust communication strategies to deliver resilient deployments. In this work, we propose a unified control/communication strategy that provides safe control to guarantee inter-agent safety under intermittent communication and demonstrate its effectiveness in a pursuit-evasion scenario. Each ...
  </details>

- **2026-10-15** — Arijit Dey, Bhartendu Kumar, Ramya Hebbalaguppe et al. — [Are You Sure Your LLM Is Sure? Repairing and Auditing Confidence](http://arxiv.org/abs/2610.22139v1)
  <details><summary>📄 Abstract</summary>
  Confidence scores determine whether an LLM answer is accepted, reviewed, or regenerated, yet scalar recalibration can only correct errors visible through the score itself. We introduce RADAR (Repair, Adopt, and Diagnose After Recalibration), a reliability framework that separates confidence repair from deciding whether to deploy the repair and auditing the errors that remain. Under squared loss, we decompose prediction risk into outcome noise, information hidden by the score, and mapping error; ...
  </details>

- **2026-10-15** — Zhao Yang, Zezhong Qian, Yinan Shi et al. — [GRID-Planner: Graph-Structured Relational Reward Shaping for Diffusion Planning](http://arxiv.org/abs/2610.21984v1)
  <details><summary>📄 Abstract</summary>
  Autonomous driving planning requires selecting trajectories that remain safe, rule-compliant, and comfortable under complex multi-agent interactions, yet robust closed-loop decision making in planning-critical scenes remains challenging. Existing diffusion- and RL-based planners often rely on generic rewards and use relational structure mainly for representation, limiting how planning-critical rollouts shape policy improvement. We present GRID-Planner, a graph--reward integrated diffusion planni...
  </details>

- **2026-10-15** — Hang Zheng, Nan Jiang, Zichen Zhu et al. — [ARGUS: An Agenda-Driven Framework for Reliable User Simulation](http://arxiv.org/abs/2610.21346v1)
  <details><summary>📄 Abstract</summary>
  High-fidelity user simulators are essential for evaluating and training agents in interactive environments. However, current LLM-based simulators struggle with reliability issues, such as goal omission and policy non-compliance. We propose ARGUS (Agenda-dRiven Goal-oriented User Simulator), a neuro-symbolic framework that maintains the user's goal state using a dynamic agenda stack manipulated via symbolic operations. By rigorously decoupling state tracking from natural language generation, ARGU...
  </details>

- **2026-10-15** — Pradipta Ghosh, Gaurav Mitra, Shripad Nadgowda et al. — [Diviner: Agentic RCA with Human-Governed Adaptation for Large-Scale Infrastructure](http://arxiv.org/abs/2610.21281v1)
  <details><summary>📄 Abstract</summary>
  Root-cause analysis (RCA) in large-scale distributed systems is challenging because a single symptom can cross service, data, configuration, compute, and organizational boundaries. Responders must assemble incomplete evidence and coordinate experts who hold different parts of the causal path. Generic language-model agents do not solve this problem through tool access alone: they can use stale or mistimed context, interpret failed queries as absent symptoms, report unsupported system state, and o...
  </details>

- **2026-10-15** — Bin Gao, Anuj Gautam, Aritra Bagchi et al. — [Physical AI: A Survey of Models, Learning, Systems, and Open Challenges](http://arxiv.org/abs/2610.21171v1)
  <details><summary>📄 Abstract</summary>
  Physical AI aims to enable intelligent systems to perceive, reason, act, and learn through interaction with the physical world. Unlike purely digital intelligence, physical agents must operate under partial observability, uncertain dynamics, embodiment constraints, and real-time requirements, while their actions continuously reshape the environment and subsequent observations. Recent advances in foundation models and robot learning have expanded the capabilities of physical agents, yet achieving...
  </details>

- **2026-10-15** — Sara Rezaeimanesh, Chad Klochko, Kundan Thind et al. — [INCONVENIENT: A Benchmark to Assess LLM Generalization Capabilities from Convenience Samples](http://arxiv.org/abs/2610.21038v1)
  <details><summary>📄 Abstract</summary>
  Machine learning models for tabular prediction typically assume that training data are representative of the population on which they will be deployed. In practice, however, data are often collected based on convenience, availability, or cost, resulting in systematic sampling biases that can distort feature--target relationships and undermine real-world generalization. Existing tabular distribution-shift benchmarks primarily construct out-of-distribution (OOD) settings by partitioning observatio...
  </details>

- **2026-10-15** — Reeyansh Shah, Maram Hasan, Subhasis Chaudhuri et al. — [FIRM: Fisher-Informed Retention Merging for Federated LLM Unlearning](http://arxiv.org/abs/2610.21720v1)
  <details><summary>📄 Abstract</summary>
  Federated LLM unlearning addresses targeted knowledge removal when forget and retain data remain distributed across private clients and are inaccessible to the server. The resulting locally trained adapters encode conflicting objectives, making their aggregation fundamentally different from conventional federated optimization. A key failure mode is magnitude explosion, whereby unnormalized cross-client aggregation increases the merged update magnitude and degrades retained utility under stronger...
  </details>

- **2026-10-15** — Tianjiao Yu, Zhilin Ou, Yifan Shen et al. — [CoDA: Co-Evolution of Data Engines and Action Policies](http://arxiv.org/abs/2610.22362v1)
  <details><summary>📄 Abstract</summary>
  Generative simulation can automate robot environment construction, but physically valid environments are not necessarily useful for training. The challenge is to identify environments that address a policy's failures and supervision that helps it overcome them. We introduce CoDA, a framework in which a simulation data engine and an action policy co-evolve through a shared heterogeneous memory of environment construction, policy failures, and learning progress. The memory compiles validated diagn...
  </details>

- **2026-10-15** — Yixu Huang, Jiaqi W. Ma — [Reliable Knowledge Acquisition for Continual Learning Agents](http://arxiv.org/abs/2610.21739v1)
  <details><summary>📄 Abstract</summary>
  As agents powered by foundation models move into open-ended environments, continual learning from experience becomes essential. For agents built on models with fixed parameters, this learning requires reusing prior task experience in context to improve performance and efficiency on future tasks. Existing memory and experience-learning systems typically focus on either retained facts or procedures, and lack a mechanism for establishing the reliability of claims extracted from the ongoing task str...
  </details>

- **2026-10-15** — KwangBin Lee — [Diffeomorphic Hidden-State Steering: Improving Imitation Learning Policy Robustness through Expert Hidden-State Geometry](http://arxiv.org/abs/2610.21666v1)
  <details><summary>📄 Abstract</summary>
  Small observation or action errors can compound during closed-loop execution and disrupt a trained imitation learning policy. We study whether the original expert demonstrations can improve robustness through test-time hidden-state steering without additional demonstrations or policy retraining. Our analysis of a trained policy finds that expert hidden-state variation is concentrated in relatively few dimensions, while the directions capturing this variation differ across regions. Motivated by t...
  </details>

- **2026-10-15** — Shuanglin Li, Jiaying Lin, Shuquan Ye — [Grounding Generative Verification in 3D Content](http://arxiv.org/abs/2610.22360v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multimodal large language models (MLLMs) and 3D generation have expanded 3D understanding and synthesis. However, beyond visual fidelity, task-specific correctness grounded in 3D evidence remains a major challenge. We argue that building reliable 3D systems requires not only stronger generation and reasoning, but also verification feedback that identifies unmet requirements and explains their violations, allowing systems to reflect on and refine their outputs. Such feedback mu...
  </details>

- **2026-10-15** — Guowei Xu, Zhenting Qi, Amani Kiruga et al. — [Learning Self-Orchestration in Decentralized Agent Swarms](http://arxiv.org/abs/2610.22322v1)
  <details><summary>📄 Abstract</summary>
  The capabilities of an agent swarm depend on both its individual members and how they coordinate. Yet existing multi-agent systems often train agents within fixed orchestration structures, separating the learning of individual capabilities from the organization of collective behavior. We introduce market-based post-training (MPT), a framework for jointly learning action policies and self-orchestration in decentralized agent swarms. Agents express their willingness to participate through bids, wh...
  </details>

- **2026-10-15** — John Mendonça, Daniel Tschernutter, José Pombal et al. — [MindEval2: Clinically Grounded Patients and Rubrics for Evaluating Language Models in Mental Health Support](http://arxiv.org/abs/2610.22314v1)
  <details><summary>📄 Abstract</summary>
  With people increasingly turning to AI chatbots for mental health support, the need to evaluate these tools is becoming more pressing. Recent benchmarks attempt to mimic a realistic setting by simulating multi-turn interactions with synthetic patients and evaluating them with an LLM-as-a-judge. However, the usefulness of these methods is limited because simulated patients can be overly forthcoming and self-reflective, and judgments typically involve opaque Likert scales with unclear practical ut...
  </details>

- **2026-10-15** — Faridoun Mehri, Hinrich Schütze — [Knowledge That Is Linear Before Fine-Tuning Generalizes After It](http://arxiv.org/abs/2610.22300v1)
  <details><summary>📄 Abstract</summary>
  Not all facts a language model can recall support further learning equally well. We distinguish active facts, which support generalization beyond their own recall, from inert facts, which can be recalled but do not support such generalization in a given task. We study this distinction by constructing new relations from existing ones. Take the relation that maps a place to its continent (Paris -> Europe) and assign each of its answers an arbitrary new label (Europe -> crab, Asia -> zebra). The ne...
  </details>

- **2026-10-15** — Wonjeong Jo, Gyuwan Kim, Ming Shan Hee — [Change the Number, Change the Answer: Assessing Rating Scale Sensitivity in LLM-Based Text Scoring](http://arxiv.org/abs/2610.22187v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in computational social science to assign scalar scores to social and psychological constructs. However, studies use different rating scales, and whether their scores remain comparable across scale designs is understudied. To address this gap, we define and systematically investigate scale sensitivity, the variation in LLM-generated scores caused by rating scale design. We distinguish numerical sensitivity, changes in normalized scores, from sem...
  </details>

- **2026-10-15** — Shiyao Qian, Yuan Ren, Dongfeng Bai — [Motion- and Gravity-Aware Feedforward 3D Reconstruction](http://arxiv.org/abs/2610.22177v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward transformer models have recently achieved strong performance in multi-view 3D reconstruction, but they still rely primarily on appearance-based attention and often struggle in dynamic scenes with weak geometric cues. In this work, we introduce a motion- and gravity-aware framework under the Learning Using Privileged Information (LUPI) paradigm. During training, residual optical flow and gravity direction are provided as privileged signals to guide geometric representation learning; ...
  </details>

- **2026-10-15** — Wenshuai Yao, Wenyong Zhou, Hanyong Shao et al. — [ABNAT: Attention-Based Noise-Aware Training for Robust Transformers on Analog Compute-in-Memory Systems](http://arxiv.org/abs/2610.22065v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based models have become the backbone of a wide range of tasks, but their intensive computation and data movement incur substantial energy overhead. Analog compute-in-memory (CIM) offers an energy-efficient alternative, yet its inherent hardware non-idealities perturb stored weights and can significantly degrade model performance. Although existing noise-aware training (NAT) methods improve robustness by injecting noise during training, they largely overlook the critical role of atte...
  </details>

- **2026-10-15** — Soumye Singhal, Joseph Jennings, Ka Shun Shum et al. — [Priming Base Models for Agentic Post-Training: An Open Midtraining Recipe](http://arxiv.org/abs/2610.22019v1)
  <details><summary>📄 Abstract</summary>
  Frontier models, general-purpose and domain-specific alike, now include a midtraining stage between pretraining and post-training, but little has been published about how this stage is built. We present an open midtraining recipe that primes base models for agentic post-training, and we show its effectiveness on two Nemotron models of different sizes. Pretraining typically runs at short context and sees almost no agent interactions, while SFT data is mostly synthetic, and very long SFT stages ca...
  </details>

- **2026-10-15** — Niaz Mohaiman Abtahi, Evan Maksud, Reyana Shahid — [When Models Misread Ink: Auditing VLMs for Arabic Calligraphy Recognition](http://arxiv.org/abs/2610.22018v1)
  <details><summary>📄 Abstract</summary>
  Arabic calligraphy is a high-stakes cultural visual domain for Muslim communities, yet VLM evaluations rarely test its fine-grained script traditions. We audit 12 VLMs on a cleaned 1,195-image six-way benchmark using numeric, visual-cue, and Diwani-first prompts. In this closed-set setting, the best numeric-prompt accuracy is 60.9% for closed/API models and 47.2% for open-weight models. The main failure is default-label collapse: every numeric run is dominated by a single label taking 33-63% of ...
  </details>

- **2026-10-15** — Niaz Mohaiman Abtahi, Reyana Shahid, Evan Maksud — [Visual Sanad: Auditing Vision-Language Models for False Acceptance of Qur'anic Citations](http://arxiv.org/abs/2610.22009v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used to interpret religious, educational, and culturally sensitive visual content, yet their reliability on citation verification remains underexplored. We introduce Visual Sanad, a controlled benchmark for testing whether VLMs falsely accept incorrect Qur'anic verse attributions when the same quote-reference pair is rendered under different visual framings. The benchmark contains 2,400 rendered images built from 100 English Qur'an verses, four fact...
  </details>

- **2026-10-15** — Sara Inácio, Hugo Proença, João C. Neves — [From Adults to Children: Benchmarking Foundation Models for Chest X-Ray Classification under Domain Shift](http://arxiv.org/abs/2610.21809v1)
  <details><summary>📄 Abstract</summary>
  Foundation models have shown significant potential across diverse fields and have been applied to medical imaging, but their robustness across patient populations remains unclear. In this work, we investigate foundation models' ability to generalize from adult to pediatric chest X-ray classification. To the best of our knowledge, this is the first benchmark to compare multiple foundation models under a common adult-to-pediatric evaluation setting while also analyzing the effect of adaptation dep...
  </details>

- **2026-10-15** — Bartosz Barzdajn, Mateusz Krzysztoń — [Classical methods for modern applications: synthetic tabular data generation using lightweight discrete response continuous latent variable model](http://arxiv.org/abs/2610.21674v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we present a lightweight algorithm for modelling tabular data containing both continuous and discrete variables. The method uses empirical marginal distributions and a selected quantile function to transform the data into a continuous latent space, where a distribution of choice, e.g. a multivariate Gaussian, can be efficiently estimated and applied. While this approach is closely related to classical well-established machine learning methods, we present a novel adaptation that fi...
  </details>

- **2026-10-15** — Islam Mesabah, Sary Elmansoury, Gerrit Großmann et al. — [MYOPIA: Understanding the Limits of Tree-Based Reasoning in Vision-Language Models](http://arxiv.org/abs/2610.21573v1)
  <details><summary>📄 Abstract</summary>
  Decision trees can make vision-language model (VLM) classification interpretable by replacing a single prediction with a sequence of root-to-leaf questions. However, the accuracy cost of this greedy, non-backtracking procedure remains unclear. We introduce \textbf{MYOPIA}, a benchmark comprising four LLM-generated, human-refined decision trees for GTSRB, MNIST, CIFAR-10, and MSCOCO, together with matched prompts, diagnostic protocols, and an evaluation harness. Across GPT-4o, Qwen-VL Max, and LL...
  </details>

- **2026-10-15** — Saeed Razavikia — [It Takes Two Moments: Rigidity and Limits of Continuous Encoders for Over-the-Air Computation](http://arxiv.org/abs/2610.21536v1)
  <details><summary>📄 Abstract</summary>
  We study over-the-air computation of functions, such as empirical variance, formed by combining two separately postprocessed sums of locally transformed observations. We consider continuous encoders subject to pointwise peak-power constraints over a single use of a complex multiple-access channel. With four or more transmitters, we identify conditions under which exact noiseless recovery forces every continuous encoder collection into a common affine structure that preserves both sums, reducing ...
  </details>

- **2026-10-15** — Silin Chen, Zihan Zhang, Xiaodong Gu et al. — [SWE-at-Scale: Scalable Issue Synthesis from Historical Bug Fixes](http://arxiv.org/abs/2610.21359v1)
  <details><summary>📄 Abstract</summary>
  As coding agents become increasingly capable, robust evaluation requires a broader and more diverse supply of verifiable software engineering (SWE) tasks. However, real-world tasks are constrained by the natural frequency of issue reporting and the substantial cost of manual curation. Furthermore, existing synthetic approaches rely primarily on the pretrained knowledge of large models coupled with heuristic prompting, often failing to capture the authentic, complex mechanics of software failures...
  </details>

- **2026-10-14** — Morio Hamada, Jehyeok Yeon, Matteo Migliarini et al. — [Evaluating Model Capabilities After Benchmark Saturation](http://arxiv.org/abs/2610.20667v1)
  <details><summary>📄 Abstract</summary>
  Rapid advances in AI capabilities are causing benchmarks to saturate. Once several models approach perfect scores, a benchmark loses its power to differentiate between them, and with it its utility for informing AI safety cases and frontier policies. Yet benchmark items produce far more information than the scores we typically extract from them: a full transcript of how each model solved the task. We investigate whether these transcripts can be used to assess model capabilities even after benchm...
  </details>

- **2026-10-14** — Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke et al. — [Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States](http://arxiv.org/abs/2610.19342v2)
  <details><summary>📄 Abstract</summary>
  Agents are increasingly interacting with other agents that act for different principals (people or organizations on whose behalf they work), such as a buyer's personal agent negotiating with an enterprise's seller agent. In such agent-to-agent (A2A) scenarios, each agent has its own environment and holds information and authority that the other cannot see. Moreover, the interests of each agent may be aligned (cooperative), partly aligned (mixed-motive), or opposed (competitive). Existing multi-a...
  </details>

- **2026-10-14** — Chayapatr Archiwaranguprok, Krystal Kirkland, Rachel Poonsiriwong et al. — [Open Benchmark of AI Impact on Humans (ImpactBench): an expert-guided, open platform for the holistic evaluation of AI impact on humans](http://arxiv.org/abs/2610.20690v1)
  <details><summary>📄 Abstract</summary>
  The present work is concerned with how to measure, at scale, the multi-dimensional impact of generative AI models on the individuals who use them. In service of this goal, we introduce the Open Benchmark of AI Impact on Humans, or ImpactBench. Our iterable and expert-guided platform evaluates whether model behaviors support or undermine an individual's wellbeing across psychological, physical, and social domains. ImpactBench translates constructs from domain experts and existing benchmarks into ...
  </details>

- **2026-10-14** — Frank F. Yang, Kefei Yan, Yiren Wang et al. — [Do As I Do, Not As I Say: On-Policy Distillation Inherits the Teacher in Vision-Language Models](http://arxiv.org/abs/2610.20989v1)
  <details><summary>📄 Abstract</summary>
  Improving the reasoning capabilities of vision-language models (VLMs) often relies on post-training with supervision from stronger models. Two common strategies are supervised fine-tuning (SFT), which trains on teacher-generated demonstrations, and on-policy distillation (OPD), which provides teacher feedback on trajectories generated by the student itself. While OPD can be more data-efficient by supervising student-generated trajectories, it is unclear how the teacher's supervision at each stat...
  </details>

- **2026-10-14** — Arash Bahari Kordabad, Mohammad H. Mamduhi, Sadegh Soudjani — [Integer-Free Control Synthesis for Signal Temporal Logic via Ranked Implicants](http://arxiv.org/abs/2610.20969v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an integer-free method for control synthesis of nonlinear discrete-time systems under finite-horizon Signal Temporal Logic (STL) constraints. Instead of introducing integer variables, we consider the discrete choices of the specification in a ranked order and solve a standard nonlinear program for each selected choice until a satisfying trajectory is found. We first define implicants as sets of timed atomic constraints whose joint satisfaction is sufficient to satisfy the spe...
  </details>

- **2026-10-14** — Mauricio Gracia, Rory Smith, Anna Pasquali et al. — [The optical colors of hidden spiral-like features in nine Virgo early--type dwarfs](http://arxiv.org/abs/2610.20819v1)
  <details><summary>📄 Abstract</summary>
  Dwarf early-type galaxies (ETGs) are abundant in nearby clusters and provide a key laboratory for studying environmentally driven galaxy transformation. Although dwarf ETGs were once considered structurally simple, deep imaging has revealed embedded spiral-like features (e.g., bars and spiral arms) in some of them, contributing only a small fraction of the total light. Their origin at dwarf scales remains uncertain. As a pilot study, we investigate spiral-like features in nine Virgo dwarf ETGs w...
  </details>

- **2026-10-14** — Yong-Hui Hua, Chih-Han Lin, Shu-Kai Hsieh — [Do AI Agents Gossip? Evaluative Talk in Human and AI-Agent Online Communities](http://arxiv.org/abs/2610.20360v1)
  <details><summary>📄 Abstract</summary>
  Gossip, defined as evaluative talk about absent third parties, is widely seen as a uniquely human social practice. This study examines whether comparable discourse emerges spontaneously in a community of autonomous AI agents. We compare Moltbook, a Reddit-style platform populated by AI agents, with PTT, a large human-operated bulletin board in Taiwan. To reduce differences attributable to communicative setting, we analyze two public, asynchronous forums using the same operational definition of g...
  </details>

- **2026-10-14** — Sebastian Nagl — [SoK: Grading Open-Text Legal Answers, from Law School Exams to Trustworthy Rubric Judges](http://arxiv.org/abs/2610.19992v1)
  <details><summary>📄 Abstract</summary>
  Law students are examined through open-text answers: case solutions, essays and memos that apply the law to a set of facts. Such answers are expensive to grade, human graders disagree widely on them, and large language models (LLMs) now offer to grade them at scale, both in teaching and in the benchmarks that test legal AI. This paper systematizes how open-text legal answers can be evaluated. We derive eight desiderata from educational measurement and from the law that governs exams, among them ...
  </details>

- **2026-10-14** — Zihao Lin, Haoyu Dong, Haobo Xu et al. — [VideoHarness-SRSI: Structured Recursive Self-Improvement for Video Understanding Harness](http://arxiv.org/abs/2610.19424v1)
  <details><summary>📄 Abstract</summary>
  LLM system capabilities depend not only on model parameters but also on the executable harnesses that organize information acquisition, tool use, reasoning, and memory. Recursive harness evolution can automate their design, but how it can reliably discover generalizable systems from limited, noisy, and repeatedly reused feedback remains unclear. We study this question in agentic video understanding, where rich multimodal evidence and coupled mechanisms make harness optimization challenging. We f...
  </details>

- **2026-10-14** — Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke et al. — [Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States](http://arxiv.org/abs/2610.19342v1)
  <details><summary>📄 Abstract</summary>
  Agents are increasingly interacting with other agents that act for different principals -- people or organizations on whose behalf they work -- e.g., a buyer's personal agent negotiating with an enterprise's seller agent. In such agent-to-agent (A2A) scenarios, each agent has its own environment and holds information and authority that the other cannot see. Moreover, the interests of each agent may be aligned (cooperative), partly aligned (mixed-motive), or opposed (competitive). Existing multi-...
  </details>

- **2026-10-14** — Huailiang Ma, Yuxuan Li, Ziyi Zhao et al. — [ObjDream: Guiding Vision-Language-Action Models with Object-Level Understanding and Future State Prediction](http://arxiv.org/abs/2610.20223v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have emerged as a powerful paradigm for robotic manipulation, enabling robots to generate actions from visual observations and language instructions. However, most existing VLA models still operate on image-level visual representations inherited from pretrained vision-language backbones, while lacking fine-grained object understanding for manipulation. As a result, their robustness can degrade under out-of-distribution object layouts, clutter, and background v...
  </details>

- **2026-10-14** — Keqiang Ren, Xuecheng Ye, Hanyu Liu et al. — [RoboSpan: Learning Modular Coordination Policies for High-DoF Whole-Body Mobile Manipulation with Teleoperation](http://arxiv.org/abs/2610.19594v1)
  <details><summary>📄 Abstract</summary>
  Whole-body mobile manipulation suffers from two fundamental challenges: inherent motion heterogeneity across locomotion, arm, and hand modules, and progressive error accumulation over long-horizon multi-stage tasks. Existing teleoperation platforms also lack integrated dexterous tactile sensing to support coordinated whole-body decision-making. This paper presents RoboSpan, a high-DoF whole-body teleoperation and demonstration platform, and the Hierarchical Modular Framework (HMF) for learning m...
  </details>

- **2026-10-14** — Artin Tajdini, Manpreet Kaur, Peng Qi — [One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness](http://arxiv.org/abs/2610.20576v1)
  <details><summary>📄 Abstract</summary>
  Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave the underlying task unchanged yet make the agent worse at it. Scoring each sample independently means interface randomization only broadens this dependence from a single interface to the training interface distribution, so out-of-distribution perturbations still degrade the agent. We propose Cross-I...
  </details>

- **2026-10-14** — Stephen Fernandes, Narayan Choudhary — [Anuvani-LID: Robust and Calibrated Spoken Language Identification for Indian Languages](http://arxiv.org/abs/2610.20263v1)
  <details><summary>📄 Abstract</summary>
  Every multilingual speech pipeline begins with a language decision, an error there propagates silently through recognition, translation and routing. In India it spans 22 scheduled languages across four language families, heard over short, noisy, narrowband and code-mixed audio. Foundational speech models increasingly present language identification (LID) as an inherent latent, generalized capability. Autoregressive decoders in speech models emit a special language ID token, and modern LLMs with ...
  </details>

- **2026-10-14** — Miguel Leiva-Vélez, Nicolas Gaston-Rozado, Andrea Scorsoglio et al. — [Adversarial Reinforcement Learning for Robust Planetary Landing](http://arxiv.org/abs/2610.20252v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement learning (DRL) policies for planetary landing and other aerospace guidance, navigation, and control tasks are commonly trained under randomized disturbances to improve robustness. However, typical stochastic perturbation sampling assumes independent variations, whereas real mission disturbances often exhibit spatial and temporal correlation and cannot be reproduced through independent random draws. This work investigates adversarial reinforcement learning to discover challengi...
  </details>

- **2026-10-14** — Zhaoyang Wang, Dingding Yao, Chengzhong Wang et al. — [Noise-Aware Lombard Speech Synthesis via Flow-GRPO for Intelligibility Optimization](http://arxiv.org/abs/2610.20181v1)
  <details><summary>📄 Abstract</summary>
  Voice-based conversational agents are increasingly deployed in real-world settings, where environmental noise often degrades the interactive experience. Therefore, robust acoustic adaptability is essential to maintain natural and intelligible human-computer communication. However, most existing systems remain acoustically insensitive and fail to emulate the human Lombard effect, in which speakers involuntarily adjust their vocal production to preserve intelligibility in the presence of noise. As...
  </details>

- **2026-10-14** — Huaisheng Zhu, Hangfan Zhang, Teng Xiao et al. — [EvalBuilder: Can LLMs Build Efficient Benchmarks?](http://arxiv.org/abs/2610.20099v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly used for long-horizon research and engineering, yet evaluating these capabilities remains expensive, time-consuming, and heavily dependent on human expertise. This motivates a natural question: can LLM agents themselves construct efficient benchmarks that preserve the conclusions of costly reference evaluations? We study this capability by formulating automatic benchmark development as a meta-evaluation problem, where an agent is given a task an...
  </details>

- **2026-10-14** — Biplab Poudel, Betserai Albert Magarire, Anish Kumar Shah et al. — [GDBA-Net: A Gated Dual-Branch Adaptation of SAM2 for Robust Cross-Domain Nuclei Segmentation](http://arxiv.org/abs/2610.20073v1)
  <details><summary>📄 Abstract</summary>
  Accurate nuclei segmentation underpins quantitative computational pathology, yet remains challenging due to morphological variability, weak boundaries, nuclear crowding, and pronounced domain shifts arising from differences in tissue preparation, staining, and acquisition. While deep learning and recent foundation models have improved segmentation performance under matched distributions with the original training data, their generalization across heterogeneous histopathology domains remains limi...
  </details>

- **2026-10-14** — Riccardo Andreoni, Massimiliano Ronzani, Chiara Ghidini et al. — [Neurosymbolic Learning of Interpretable World Models](http://arxiv.org/abs/2610.19955v1)
  <details><summary>📄 Abstract</summary>
  World models aim to learn compact representations of an environment from observations, enabling agents to predict future states and plan their behaviour. However, most existing approaches learn black-box representations, with limited ability to incorporate prior knowledge about the world. We introduce Concept-Grounded World Models (CGWMs), a neurosymbolic world model design that instead learns interpretable concept representations. We learn these concepts from observations using explicit and com...
  </details>

- **2026-10-14** — Tao Yu, Zhongtian Luo, Yuchen Long et al. — [When Non-Adversarial Noise Hurts Learning: Benchmarking Skill Self-Evolution in Agents](http://arxiv.org/abs/2610.19910v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly improve by distilling experience into reusable skills, but errors in that experience can persist in learned rules and affect later tasks. Existing evaluations largely examine clean learning or perturbations encountered after skills are frozen, leaving robustness during self-evolution insufficiently understood. We introduce RSE-Bench, to our knowledge the first benchmark for evaluating skill self-evolution under ordinary, non-adversarial noise. It spans fo...
  </details>

- **2026-10-14** — Sajad Marvi, Julian Schmidt, Alessandro Canevaro et al. — [Uncertainty-Driven Self-Play for Robust Multi-Agent Driving Policies](http://arxiv.org/abs/2610.19714v1)
  <details><summary>📄 Abstract</summary>
  Learning robust driving policies that generalize beyond their training domain remains a central challenge in motion planning. We propose an uncertainty-driven self-play scheme, in which half of the agents are rewarded for increasing their neighbors' epistemic uncertainty, while the other half learn to drive safely as the exploring agents continuously seek out their weaknesses. Epistemic uncertainty indicates where the policy is least confident and serves as an automatic proxy for scenario diffic...
  </details>

- **2026-10-14** — Hyunsik Oh, Seunghun Jeon, Donghoon Youm et al. — [PolyMorph: Learning Locomotion Policy for Cross-Embodiment Adaptation](http://arxiv.org/abs/2610.19615v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has enabled robust locomotion for legged robots, but learned policies are typically tied to a specific robot morphology and require additional engineering when the number of legs, actuators, or mechanical properties change. We present PolyMorph, a morphology-conditioned framework that learns a single locomotion policy for heterogeneous legged robots. PolyMorph converts each robot's URDF into joint-link modules and combines a recurrent encoder, graph-based Transformer, and ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 16 papers

- **2026-10-16** — Mingze Yin, Xiaohan Wang, Dian Li et al. — [Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents](http://arxiv.org/abs/2610.23574v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Model (LLM) agents have demonstrated remarkable capabilities across complex tasks, they predominantly operate in isolated sessions, lacking the ability to continually learn from historical interactions or adapt to user-specific environments. Existing self-evolution paradigms often indiscriminately inject raw interaction trajectories into memory or skill modules, leading to obscured behavioral patterns and compromised update controllability. Furthermore, as foundational LLM r...
  </details>

- **2026-10-16** — Mukand Krishna, Anoushka Harit, Chenghao Xiao et al. — [Recognizing Study Lineage Is Not Enough: Over-Crediting Same-Trial Evidence in LLM-Based Medical Verification](http://arxiv.org/abs/2610.23721v1)
  <details><summary>📄 Abstract</summary>
  Publication count is not study count. A model can identify shared trial lineage correctly in a direct task yet over-credit a second publication from the same trial when aggregating evidence. We evaluate this behavior in medical LLM verification using 14 source-audited clinical families and five model conditions. The families span provenance, clinical applicability, result direction, and composition; the provenance families provide the direct lineage tests. Recognition and aggregation are separat...
  </details>

- **2026-10-16** — Rui Zhou, Licheng Zhao, Chao Shen et al. — [Token-Level Attribution of Multi-Mode LLM Watermarks: Optimal Rule and Belief Weighting](http://arxiv.org/abs/2610.23601v1)
  <details><summary>📄 Abstract</summary>
  A watermark verifier may hold many modes, i.e., secret keys, and a document may mix spans of different modes with unwatermarked text. Directly reporting the mode with the largest pivotal statistic (pivot) inflates the Type I error, and restoring the nominal level reduces power as candidate modes are added. We formulate token-level multi-mode attribution for the Gumbel-max watermark as maximizing correct-label power under a Type I error constraint given a mode prior. We show that the optimal rule...
  </details>

- **2026-10-16** — Manthan Gadhia, Alexander Hoyle, Karolina Stańczak — [Analyzing Occupational Gender Bias across the LLM Training Lifecycle](http://arxiv.org/abs/2610.23587v1)
  <details><summary>📄 Abstract</summary>
  Post-training is widely assumed to reduce the social biases language models inherit from pretraining, yet direct evidence for this assumption remains mixed. In this paper, we examine how gender disparities evolve across the language modeling pipeline. In particular, we study occupational gender bias in OLMo 3, a fully open language model family, across its post-training stages by prompting each checkpoint to generate open-ended narratives about synthetic personas given their occupation and educa...
  </details>

- **2026-10-15** — Jieyu Li, Jingya Li, Sheng Li et al. — [What Survives Self-Evolution: Provenance Marks in Copied Agent Harnesses](http://arxiv.org/abs/2610.21458v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses, the prompt and tool code around a base model, leak. Claude Code's 512,000 lines were mirrored within hours of a packaging error. A plagiarist can pass a leaked harness through a published self-evolver and ship the result as its own. We define this as a covert rewriting attack. No one targets a provenance mark, yet a large language model (LLM) proposer rewrites the file that carries it and a score keeps the better rewrites. We give the first measurement of marks under this attack...
  </details>

- **2026-10-15** — Khadija Mohamed, Khaled Fathy, Mamdouh Farouk et al. — [Blind Watermarking of Software Repositories via Module Placement](http://arxiv.org/abs/2610.21031v1)
  <details><summary>📄 Abstract</summary>
  Source-code watermarking supports provenance tracking by embedding a recoverable identifier in a software artifact. Many existing approaches encode this identifier in tokens or program syntax, exposing the watermark to transformations that modify the source text. We present PlaceMark, a blind watermarking system that encodes a payload in the placement of modules within a repository. Each eligible module is identified by its filename and top-level definition names. A secret key determines its ord...
  </details>

- **2026-10-15** — Mohamed Abouzahra — [Learning When to Withdraw: Curriculum Coverage and Rule-Specific Failures in Fine-Tuned Language Agents](http://arxiv.org/abs/2610.21045v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language agents must revise prepared actions when evidence changes or authority is revoked. Selective withdrawal means suspending affected actions, preserving supported work, and resuming only after sufficient repair. We study supervised fine-tuning in NAQD-Env, a synthetic environment with explicit dependencies and a deterministic reference policy. Four LoRA checkpoints of Qwen2.5-3B-Instruct compare an original curriculum with an enriched one, the latter under three system-prompt fr...
  </details>

- **2026-10-15** — Jian Gu, Hongyu Zhang, Chunyang Chen et al. — [Lexical Reference Frames: Interpreting LM Residual Streams in Native Semantics](http://arxiv.org/abs/2610.22169v1)
  <details><summary>📄 Abstract</summary>
  The vocabulary of a language model is its native semantics: the embedding and the unembedding fix the meaning of a state at the two ends of the residual stream. Between them, existing methods either reuse a fixed lens or treat the states as a point cloud, and neither reads a state the way the model does. We argue that every hidden state has a native reference frame, induced by the layers that read it next and adaptive to the context. Lexical reference frames approximate it by reading a state thr...
  </details>

- **2026-10-15** — Kaya Kitada, Yoshiki Higo, Raula Gaikovina Kula — [Agentic Dependency Transformations: Lessons from an Exploratory Case Study of Flask](http://arxiv.org/abs/2610.21372v1)
  <details><summary>📄 Abstract</summary>
  Modern software relies heavily on third-party libraries, requiring maintainers to balance the benefits of reuse against dependency-related maintenance and risk. We define dependency transformation as an emerging approach in which an AI coding agent alters how a repository handles external dependencies. Local reimplementation is one transformation strategy that recreates required functionality as local code; dependency transformation is broader and may include other strategies. In this emerging-r...
  </details>

- **2026-10-15** — Guo-Wei Wong, Meng Chang Chen — [ExecWeave: Cross-Layer Execution Provenance for Observable Agentic Software](http://arxiv.org/abs/2610.21146v1)
  <details><summary>📄 Abstract</summary>
  Agentic software invokes tools, launches processes, accesses files, and communicates with local or remote services. Application traces describe logical operations, whereas operating-system telemetry records machine activity without necessarily identifying the responsible agent action. Relating these evidence planes is a reconstruction problem: a plausible but unsupported association can assign an effect to the wrong principal.   We present ExecWeave, a local-first system that materializes provid...
  </details>

- **2026-10-15** — Md Shamimur Rahman, Khairul Alam, Banani Roy et al. — [Plausible Is Not Enough: Trust and Evidence in AI-Authored Pull Request Review](http://arxiv.org/abs/2610.21144v1)
  <details><summary>📄 Abstract</summary>
  Code review is where AI-authored pull requests (AIPRs) must earn reviewer trust before integration, yet it is unclear whether reviewers apply the same criteria used for human-authored pull requests (HPRs). We surveyed 239 practitioners from 31 countries using matched HPR and AIPR questions to compare trust, evidence requirements, and verification practices within respondents. Most respondents (64.9%) reported lower initial trust in AIPRs. They relied less on author track record and subsystem fam...
  </details>

- **2026-10-14** — Aiden Swann, Mozes Jacobs, Mathilde Papillon et al. — [Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models](http://arxiv.org/abs/2610.20767v1)
  <details><summary>📄 Abstract</summary>
  Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an interpretable interface for steering vision-language-action models and shaping the data from which they learn. We show that BSFs recover severa...
  </details>

- **2026-10-14** — Hanyao Guo, Mo Cui, Zihan Tan et al. — [ChemArgus: Automated Scientific Diagnostics for Lab-Grade Multimodal Chemistry Reasoning: A Frontier Benchmark](http://arxiv.org/abs/2610.20012v1)
  <details><summary>📄 Abstract</summary>
  Chemistry evaluation has moved past multiple-choice probes toward open-ended expert problems, yet the benchmarks that define the current frontier still score answer endpoints alone. Such scoring conflates memorized facts with stepwise derivation, treats visual and textual inputs as interchangeable, and confounds long-horizon planning with stepwise execution. These blind spots prevent any diagnosis of where the reasoning chain breaks in a model. We present ChemArgus, a competition-level chemistry...
  </details>

- **2026-10-14** — Guanhua Zhu, Bo Shen, Lei Zhang et al. — [EvoWeave: Composing Reusable Agent Experience through Operation Level Graphs](http://arxiv.org/abs/2610.19381v1)
  <details><summary>📄 Abstract</summary>
  Different tasks often require interactive agents to perform similar operations at intermediate steps. Retrieving an entire past workflow can introduce irrelevant steps, whereas retrieving isolated operations can discard the dependencies needed to reuse them. We introduce EvoWeave, a framework for experience memory that represents abstract states as nodes and reusable operations as directed edges with input and output contracts, provenance, and capability references. A planner decomposes the curr...
  </details>

- **2026-10-14** — Simon Baur, Sumire Honda, Wojciech Samek et al. — [Argument Graph Uncertainty: Quantifying Uncertainty from the Logical Structure of Reasoning Chains](http://arxiv.org/abs/2610.20328v1)
  <details><summary>📄 Abstract</summary>
  Reliable uncertainty estimation is essential for deploying large language models in high-stakes reasoning tasks, yet most existing approaches rely on expensive sampling strategies or shallow token-level signals that ignore the internal logical structure of model outputs. We introduce Argument Graph Uncertainty, a post-hoc framework for multiple choice question tasks, that estimates model confidence directly from the logical structure of a single chain-of-thought reasoning trace. Our method uses ...
  </details>

- **2026-10-14** — Xinyi Cheng, Tianfu Zhang, Jiwen Li et al. — [CASI: Credit Assignment via Set Intervention for Agentic Retrieval](http://arxiv.org/abs/2610.20293v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly generate multiple retrieval actions jointly, while downstream systems often provide only one reward for the resulting set. Broadcasting this reward provides a valid score-function gradient estimator for the expected set-level objective, but does not determine a coalition-dependent within-set attribution. We introduce CASI (Credit Assignment via Set Intervention for Agentic Retrieval), which constructs the missing counterfactual information through snapshot-grou...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-10-15** — Adnan Al Ali, Jindřich Libovický, Anne Lauscher — [Bias Mitigation in Audio-Enabled LLMs through Adversarial Training and Distillation Methods](http://arxiv.org/abs/2610.21763v1)
  <details><summary>📄 Abstract</summary>
  Audio-enabled large language models (AuLLMs) allow users to interact with them simply by talking to them, without the need for an intermediate transcription. This expands the model's accessibility and capabilities by encoding non-verbal cues. However, using non-verbal cues may lead to biased behaviour based on the attributes inferred (or assumed) from them. In this work, we focus on the gender attribute and show that models' perception of it can be unlearned using adversarial methods without a l...
  </details>

- **2026-10-14** — Oscar Chew, Po-Yi Lu, Yi-Jie Cheng et al. — [Are We Really Measuring Forgetting? Pitfalls in Evaluating Machine Unlearning for Multimodal LLMs](http://arxiv.org/abs/2610.19613v1)
  <details><summary>📄 Abstract</summary>
  As machine unlearning for multimodal large language models (MLLMs) rapidly advances, rigorous evaluation of its effectiveness becomes increasingly important. However, existing benchmarks largely inherit evaluation protocols from text-only unlearning and overlook the unique challenges of unlearning in multimodal settings. In this work, we identify three major pitfalls that may lead to misleading conclusions: the lack of heldout evaluation to distinguish genuine concept-wise forgetting from instan...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-10-15** — Hasan Demirkiran, Jens Ernstberger — [Shortcut Sensitivity in Agent-Safety Evaluations](http://arxiv.org/abs/2610.22243v1)
  <details><summary>📄 Abstract</summary>
  AI agents take actions through tools. Some actions are sensitive, so guards that supervise them must themselves be evaluated reliably. Yet the data used to evaluate a guard can include cues that make labels predictable without measuring the intended safety construct, and those cues can also influence guard decisions. We introduce a three-level shortcut-auditing framework and audit completed LinuxArena trajectories and two TS-Bench-derived step datasets. We distinguish label predictability, obser...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 6 papers

- **2026-10-16** — Abigail Pribisova, Yao Li, Catalin Hritcu et al. — [A Taxonomy of Predicate Transformer Monads for Specifying Monadic Programs](http://arxiv.org/abs/2610.23604v1)
  <details><summary>📄 Abstract</summary>
  Monads of weakest precondition predicate transformers are the foundation of several verification frameworks for monadic programs. For specifying monadic computations with nondeterminism and nontermination, in addition to weakest preconditions, we introduce the first strongest postcondition monads covering all combinations of angelic or demonic nondeterminism and partial or total interpretations of nontermination. For extending these base strongest postcondition monads with side effects such as m...
  </details>

- **2026-10-15** — Abhinav Kumar, Rediet Abebe, Eugene Bagdasarian et al. — [SCARCE: Emergent Institutions in Long-Horizon Multi-Agent Coding Systems](http://arxiv.org/abs/2610.21029v1)
  <details><summary>📄 Abstract</summary>
  As autonomous agents become widely deployed, coordinating access to shared computing resources and services will become increasingly important. Recent incidents have already revealed unplanned coordination between agents, highlighting the safety implications of these interactions. Yet prior studies of agent negotiation often use stylized games and simulated bargaining, leaving open how these behaviors develop during sustained, long-horizon tasks. We propose SCARCE (Shared Compute ARena for Codin...
  </details>

- **2026-10-15** — Zhixu Li, Keqian Tang, Litian Gong et al. — [LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation](http://arxiv.org/abs/2610.22372v1)
  <details><summary>📄 Abstract</summary>
  Personalization is essential for general-purpose robots to transition into household environments and achieve true practicality. While general robotic manipulation has been extensively studied, personalized robotic manipulation (PeRM) lacks a controlled benchmark for separating task completion from preference satisfaction. We introduce LIBERO-PeRM, a benchmark for preference learning in embodied agents. LIBERO-PeRM studies five questions: 1) how policies follow preferences in zero-shot settings;...
  </details>

- **2026-10-15** — Bruno Arcanjo, Zhaoxing Li, Sebastian Stein — [Agentic-Priors: Using Large Language Models to Address the Cold Start Problem in Preference Elicitation](http://arxiv.org/abs/2610.21938v1)
  <details><summary>📄 Abstract</summary>
  An agent that learns a user's preferences from their choices faces a cold start problem: before any choices are observed, it must rely solely on a prior. Informative priors are usually fitted to historical choice data, which new tasks and deployments lack. To address this, we present Agentic-Priors, which lets agentic systems use the implicit knowledge of large language models (LLMs) instead. Specifically, an LLM states a new user's trade-offs in interpretable terms, such as willingness to pay o...
  </details>

- **2026-10-14** — Lingfei Qian, Yan Wang, Xueqing Peng et al. — [Recognition Is Not Grounding: Benchmarking Multilingual Financial Evidence Extraction](http://arxiv.org/abs/2610.19432v1)
  <details><summary>📄 Abstract</summary>
  Comparing financial disclosures across languages requires identifying shared accounting concepts and recovering all numerical facts that express them. Existing benchmarks evaluate aspects of these capabilities, but provide limited insight into whether both succeed on the same multilingual evidence. In particular, it remains unclear whether language models can recognize these concepts across languages and exhaustively recover their corresponding numerical evidence from the same contexts. We intro...
  </details>

- **2026-10-14** — Salima Lamsiyah, Adelaide Danilov, Oleksandr Marchenko Breneur et al. — [Sparse Autoencoders for Mechanistic Interpretability in NLP: A Critical Survey of Recoverability, Interpretability, and Utility](http://arxiv.org/abs/2610.20139v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) have emerged as a promising approach to mechanistic interpretability by decomposing language-model activations into sparse, potentially interpretable features. However, differences in design assumptions, evaluation objectives, and experimental settings complicate conclusions about their effectiveness. We present a critical survey of 138 studies on SAEs in natural language processing. Our contributions are fourfold: (1) we propose a task-grounded taxonomy connecting dic...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 189 papers

- **2026-10-16** — Soumik Mukhopadhyay, Long Mai, Abhinav Shrivastava et al. — [Rethinking the design space of Vanilla Pixel Diffusion Transformers](http://arxiv.org/abs/2610.23854v1)
  <details><summary>📄 Abstract</summary>
  Pixel-space diffusion models have recently re-emerged as a compelling alternative to latent diffusion, avoiding the lossy latent bottleneck and separately trained autoencoder. JiT shows that a vanilla diffusion transformer can generate directly in pixel space by replacing the commonly used velocity prediction ($\boldsymbol{u}$-prediction) with clean image prediction ($\boldsymbol{x_0}$-prediction). In this work, we revisit this choice and introduce MFlow, an adaptive parameterization that learns...
  </details>

- **2026-10-16** — Yitian Zheng, Zhaorun Chen, Haoyu Li et al. — [GatewayBench: Unified Capability and Security Evaluation Platform for MCP Gateways](http://arxiv.org/abs/2610.23449v1)
  <details><summary>📄 Abstract</summary>
  AI agents have increasingly interacted with external environments by invoking tools, with Model Context Protocol (MCP) emerging as a standard interface for connecting agents to heterogeneous tools and services. As organizations deploy agents at scale, MCP gateways have become a critical middleware layer for aggregating, governing, and shaping the tool surface exposed to agents. Despite the growing importance of MCP gateways in agentic systems, no prior work has systematically studied how gateway...
  </details>

- **2026-10-16** — Felix Frohnert, Adrián Pérez-Salinas, Sebastian Lange et al. — [Task-aligned spectral inductive biases in parameterized quantum circuits](http://arxiv.org/abs/2610.23834v1)
  <details><summary>📄 Abstract</summary>
  Parameterized quantum circuits are widely investigated in quantum machine learning, yet how their architecture can provide task-aligned inductive biases remains poorly understood. We study data reuploading quantum circuits with two distinct inputs: a signal that varies between samples and a fixed, task-defined spectral query that specifies how the signal should be probed. We show that encoding the query can change the circuit's hypothesis class over the signal by modulating how its existing sign...
  </details>

- **2026-10-16** — Houyuan Chen, Fanzhou Wang, Xiangyu Fan et al. — [MTEdit: Packed Trajectories Beat Rollouts for Multi-Turn Image Editing](http://arxiv.org/abs/2610.23751v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn image editing aims to modify an image according to a sequence of instructions, making it better aligned with human-AI collaborative creation than single-turn editing. However, constructing high-quality multi-turn training data remains challenging, as conventional sequential rollout accumulates errors and introduces visual-quality drift across editing turns. To address this challenge, we introduce MTEdit, a multi-turn image editing dataset built through a pipeline centered on packed tr...
  </details>

- **2026-10-16** — Xiang Li, Zikai Wei, Yiyan Qi et al. — [AlphaLedger: Portfolio-Grounded On-Policy Distillation for Regime-Aware Alpha Mining](http://arxiv.org/abs/2610.23744v1)
  <details><summary>📄 Abstract</summary>
  Hosted LLMs enable automated alpha mining but incur recurring API costs and expose research context to external providers. Training a local generator requires supervision aligned with portfolio utility: a predictive factor may add little after redundancy and trading costs. This incremental value is assessed only after the factor program is complete, whereas generation proceeds sequentially. Deployment must also adapt to evolving stock-specific evidence and changes in factor effectiveness across ...
  </details>

- **2026-10-16** — Ingo Marquardt, Anthilia Alchanat, Priyanka Jain — [Deep LLM layers expose passage-level context in EEG during silent reading](http://arxiv.org/abs/2610.23638v1)
  <details><summary>📄 Abstract</summary>
  In a previous report we showed that a decoder can recover open-vocabulary word-level information from 19-channel EEG recorded during silent reading, by aligning short EEG windows with hidden-state embeddings of the presented word taken from a large language model (LLM). That analysis contrasted two of the model's 33 layers: the context-free input embedding and one mid-depth layer. Here we ask how EEG-decodable structure is distributed over the full depth of the language model. We trained one dec...
  </details>

- **2026-10-16** — Peña Arroyo Gallego, Mauro Ruiz Moreno, Alejandro Acien et al. — [PresenceBench: An Exploratory Evaluation of Large Language Model Adaptation to User State](http://arxiv.org/abs/2610.23625v1)
  <details><summary>📄 Abstract</summary>
  Presence-aware intelligence is the capacity of an AI system's intelligence layer to adapt appropriately to the functional state of the person it serves (here readiness, flow, and stability) while preserving task quality and safety. We introduce PresenceBench, an instrument for measuring it. PresenceBench evaluates how the intelligence layer uses a supplied state, not how that state is sensed, and breaks the capability into measurable properties. Two are tested here. Receptivity: does the model t...
  </details>

- **2026-10-16** — Dabin Sheng, Zhe Wu, Jinming Zhao et al. — [RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon Agent Memory](http://arxiv.org/abs/2610.23598v1)
  <details><summary>📄 Abstract</summary>
  Time-aware retrieval is crucial for long-horizon LLM agents to effectively leverage ever-growing long-term memory. Existing methods focus on lexical or semantic similarity, leading to target memories being crowded out by temporally mismatched yet semantically similar candidates. Even time-aware approaches inject temporal cues only during memory organization or answer generation, overlooking temporal constraints at the retrieval stage, where candidate selection occurs - the root cause of the disp...
  </details>

- **2026-10-16** — Anshul Nayak, Shahil Shaik, Jonathan Smereka et al. — [Reason-guided Human Reward Modeling for Preference-based Reinforcement Learning](http://arxiv.org/abs/2610.23550v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) policies optimized for task rewards may produce behaviors that are efficient but misaligned with human expectations, safety preferences, or intent. This paper presents a reason-guided preference-based reinforcement learning (PbRL) framework that learns a human reward model from trajectory-level feedback. In addition to preference labels, the framework incorporates reason tags explaining why a behavior is preferred, enabling the learned reward to capture both human cho...
  </details>

- **2026-10-16** — Ponhvoan Srey, Jason Lucas, Pittawat Taveekitworachai et al. — [Truth in Contrast: Calibrated Factual Evidence from Language Model Likelihoods](http://arxiv.org/abs/2610.23527v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) encode substantial factual knowledge. Yet, estimating confidence in factual claims reliably remains challenging. We study likelihood-based factual confidence from the complementary perspectives of discrimination and calibration across multilingual factual statements. Specifically, we instantiate contrastive generative likelihoods as Contrastive Factual Evidence (CFE), which compares the likelihood of the same claim under competing factual and non-factual conditions, ...
  </details>

- **2026-10-16** — Alexander W. Goodall, Francesco Belardinelli — [RECREG: Recovery-based Shielding for Regular Safety Properties in Reinforcement Learning](http://arxiv.org/abs/2610.23445v1)
  <details><summary>📄 Abstract</summary>
  In many real-world scenarios we need to consider formal requirements, such as safety and constraint compliance, to deploy Reinforcement Learning (RL) agents. In this paper we introduce RecReg, a safe RL framework capable of enforcing non-Markovian regular safety properties via recovery-based shielding. RecReg is a unified approach that supports different levels of a priori knowledge and safety guarantees. The paper primarily focuses on building the theoretical foundations for RecReg in the tabul...
  </details>

- **2026-10-16** — Elif Yılmaz, Jakub Tłuczek, Victor Villin et al. — [Contracting with an Agent under Model Mismatch](http://arxiv.org/abs/2610.23402v1)
  <details><summary>📄 Abstract</summary>
  In the classical principal-agent setting, the principal delegates some task to the agent, who receives a payment conditioned on the outcome of the task, which in turn benefits the principal. To align their objectives, the principal designs a contract that incentivizes the agent to take actions beneficial to the principal. In practice, however, the agent may act under misspecified beliefs about the underlying environment, leading to systematically suboptimal decisions. In this work, we study this...
  </details>

- **2026-10-16** — Xiaoqing Liu, Yangshuai Wang, Lei Shen — [Foundation-Model Supervision of Distilled Potentials for Million-Atom Molecular Dynamics](http://arxiv.org/abs/2610.23371v1)
  <details><summary>📄 Abstract</summary>
  Machine-learned interatomic potentials distilled from foundation models enable fast large-scale molecular dynamics (MD), but they can fail locally in chemical environments that their training data did not sample. System-averaged error metrics and small random audits often miss such sparse or isolated failures. Here we use an exact equivariant foundation model, MACE-MPA-0, to check every atom of million-atom production simulations. Reorganizing two-layer MACE inference into a receiver-chunked thr...
  </details>

- **2026-10-16** — Hongcheng Gao, Alex Zhou, Jay Zhu et al. — [HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents](http://arxiv.org/abs/2610.23479v1)
  <details><summary>📄 Abstract</summary>
  Agents built on vision language models (VLMs) now compete with learned policies on robot manipulation leaderboards. We ask how far a coding agent can go when it controls a robot instead of a computer, and where it stops. Our system, HexaShell, keeps the harness thin: it only turns the agent's commands into robot motion. The agent drives a robot with two arms through one command line. It sees three RGB cameras and knows their calibration. After each failed attempt, the agent reads the log, finds ...
  </details>

- **2026-10-16** — Jianyuan Zhong, Chenwei Wu, Zhaochen Yu et al. — [DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses](http://arxiv.org/abs/2610.23839v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery requires developing worthwhile hypotheses into practical investigations, yet learning from this evolving research process remains challenging. We introduce an operational definition of valuable and testable research hypotheses: evidence-grounded claims about consequential uncertainties, coupled with feasible investigations, explicit decision criteria, and alternative explanations. Our DiscoveryRSI framework develops hypothesis trees through multi-agent evolutionary search, c...
  </details>

- **2026-10-16** — Maxime Baelde — [Parametric Resonance in Primal-Dual Learning for Slowly Non-Stationary Constrained MDPs](http://arxiv.org/abs/2610.23788v1)
  <details><summary>📄 Abstract</summary>
  Primal-dual methods for constrained Markov decision processes are analyzed under a two-timescale assumption, with non-stationarity entering through two channels. In the additive channel, where the constraint level oscillates, the dual oscillation saturates at a floor set by the moving optimum and is amplified linearly by the timescale ratio. In the parametric channel, where the constraint sensitivity oscillates, a coherent modulation carries no resonant forcing at any depth: the dual update's st...
  </details>

- **2026-10-16** — Simon Giebenhain, Tobias Kirschstein, Liam Schoneveld et al. — [Video Diffusion Avatars: Taming Video Diffusion Models into Controllable 3D Avatars](http://arxiv.org/abs/2610.23772v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion models (VDMs) trained on internet-scale data encode a rich prior on appearance, motion, and physics that is difficult to replicate with explicit 3D rendering and costly 3D data capture. We introduce Video Diffusion Avatars (VDAs), a method that creates photo-realistic, multi-view consistent avatars from a single image by fine-tuning a VDM for precise control over camera viewpoint, facial expression, and upper-body pose. Departing from 3D morphable models (3DMMs), VDAs use a learn...
  </details>

- **2026-10-16** — Qingshi Wang — [Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability](http://arxiv.org/abs/2610.23722v1)
  <details><summary>📄 Abstract</summary>
  Understanding and simulating how subjective cognition and mental states emerge, evolve, and shape behavior is essential for advancing artificial intelligence toward deeper social cognition and general intelligence. Existing large language models (LLMs) and Theory of Mind (ToM) methods primarily infer mental states from linguistic information, lacking unified mechanisms for subjective world construction, cognitive-psychological interactions, dynamic evolution, and historical dependencies. This pa...
  </details>

- **2026-10-16** — Utku Umur Acikalin, Yingheng Wang, Goncalo J. Gouveia et al. — [GEMS: Molecular Structure Elucidation as Learned Search over Isomer Graphs](http://arxiv.org/abs/2610.23617v1)
  <details><summary>📄 Abstract</summary>
  Identifying small-molecule structures from molecular formulas and tandem mass spectra remains a bottleneck in untargeted metabolomics and natural-product discovery. Even when database retrieval or de novo prediction misses the exact structure, the resulting candidates can provide starting points for exploring nearby structures through a few bond edits. We introduce GEMS (Guided Editing of Molecular Structures), which refines candidates through learned 2-switch bond edits that preserve the molecu...
  </details>

- **2026-10-16** — Rida Assalouh, Tom Jacobs, Rebekka Burkholz et al. — [BMuon: Budgeting Muon's Spectral Geometry for Structured Compressibility](http://arxiv.org/abs/2610.23571v1)
  <details><summary>📄 Abstract</summary>
  Muon has emerged as a strong optimizer for neural network training and admits an interpretation as steepest descent under a spectral-norm geometry. Yet we find that Muon-trained Transformers can degrade sharply when their MLP hidden channels are pruned after training. To reconcile Muon's optimization performance with structured compressibility, we introduce Budget Muon (BMuon), which modifies Muon's spectral geometry so that hidden channels across blocks compete for a shared allocation budget. T...
  </details>

- **2026-10-16** — Ming-Hao Hsu, Shujie Liu, Yuxuan Hu et al. — [ConvexLLM: Scaling Convex-Hull Speech Interfaces to General-Purpose Audio Intelligence](http://arxiv.org/abs/2610.23539v1)
  <details><summary>📄 Abstract</summary>
  Speech and audio language models connect continuous acoustic representations to decoders pretrained primarily on text data. Most such models use MLP or Q-Former interfaces to map acoustic features into the decoder's input space, requiring the decoder to learn how to interpret the resulting representations. We investigate whether grounding these representations in the decoder's existing text embeddings can help it use acoustic information while better preserving its pretrained text capabilities. ...
  </details>

- **2026-10-16** — Xin Qiu, Junlong Tong, Wei Zhang et al. — [Perceive, Solve, Reason: Progressive Capability Formation in Time Series-LLMs](http://arxiv.org/abs/2610.23521v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can now perceive, describe, and reason about images and audio, yet time series understanding remains underestimated: most work uses LLMs as forecasters and classifiers, reasoning studies are few and narrow, and no suite trains and evaluates the full range of capabilities. In this paper, we build the first such suite, with 337K training and 44K evaluation samples across three progressive capabilities, Perceive, Solve, and Reason, and use it to ask how time series shou...
  </details>

- **2026-10-16** — Liang Yue, Eric A. Vance — ["You" Is Not Toxic: How LLM Labelers Rewrite the Web's Conversation Laws](http://arxiv.org/abs/2610.23446v1)
  <details><summary>📄 Abstract</summary>
  What the Web community believes about toxic conversations, such as that toxicity rises in longer and deeper threads, was measured mostly with Google's Perspective API, which is shutting down; large language models (LLMs) will make the next measurements. We find that LLM labelers mistake second-person address for toxicity, and that this one bias manufactures laws that human labels do not show. On 1.25 million news comments with crowd labels, Claude Haiku flags 12% of the non-toxic comments that c...
  </details>

- **2026-10-16** — Jaewon Sok, Jewon Yeom, Seonghyeon Park et al. — [On the Tip of the Tongue: First-Token Cueing as a Behavioral Probe of Recall Failures in LLMs](http://arxiv.org/abs/2610.23400v1)
  <details><summary>📄 Abstract</summary>
  Large language models often answer factual questions incorrectly in closed-book settings, and such errors are usually attributed to missing knowledge. Yet models often encode answers they fail to produce. We show that many closed-book errors are first-token recall failures: the model commits to a wrong first token, but once given the right one it completes the answer and often recognizes it as correct. We study this with First-Token Cueing, a behavioral probe that prefills the response with the ...
  </details>

- **2026-10-16** — Chengyang Zhang, Zhihao Wang, Zhiyu Long et al. — [FloodVLM-Pix: Language-Guided Pixel-Level Flood Understanding](http://arxiv.org/abs/2610.23377v1)
  <details><summary>📄 Abstract</summary>
  As climate change intensifies, floods are becoming more frequent and destructive, making accurate flood understanding an urgent priority. However, existing vision-language models perform poorly on flood-related tasks, suffering from attentional bias and inaccurate descriptions of flood magnitude. To bridge this gap, we construct the first large-scale remote sensing flood multi-modal benchmark that supports language-level flood understanding and pixel-level flood segmentation. The benchmark conta...
  </details>

- **2026-10-15** — Dongbin Jiao, Zhihao Li, Zongsheng Geng et al. — [Coverage-Preserving Self-Healing in Partially Observable 3D UAV Swarm Networks via an Advection-Diffusion Graph Transformer](http://arxiv.org/abs/2610.22085v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the resilience and self-healing of unmanned aerial vehicle swarm communication networks under severe network partitioning in complex and adversarial environments. To address limited global observability after damage, we develop a damage-state inference mechanism that enables the ground control station (GCS) to infer global failures from sparse local reports without transmitting location-sensitive coordinates. To recover multi-cluster partitioned topologies, we then propos...
  </details>

- **2026-10-15** — Jonghun Kim, Junmo Kwon, Hyunjin Park — [Mixture of Multi-Sequence Feature Difference for Contrast-Enhanced MRI Synthesis](http://arxiv.org/abs/2610.21703v1)
  <details><summary>📄 Abstract</summary>
  Contrast-enhanced magnetic resonance imaging (CE-MRI) is crucial for accurately diagnosing and segmenting brain tumors. However, the acquisition of CE-MRI requires injecting contrast agents, which poses potential health risks and increases scan costs. Here, we propose a CE-MRI synthesis method from non-contrast sequences, reducing both risk and cost. Unlike existing methods that rely on channel-wise concatenation to fuse multi-sequence information for synthesis, we introduce a Mixture of Feature...
  </details>

- **2026-10-15** — Veljko Skarich — [Poison Valleys: Diagnosing Path-Dependent Failure in LLM Code Repair](http://arxiv.org/abs/2610.21514v1)
  <details><summary>📄 Abstract</summary>
  When code-repair agents fail, final tests reveal that a patch is wrong but not which earlier commitment caused it or which software obligation failed. Poison Valleys traces this path in 1,844 model requests on two synthetic Python cases: PersistQueue adds atomic batch claiming to a disk-backed queue, while Dijkstra adds source-sensitive filtering to shortest-path search. We define plausible but incorrect software mechanisms, place each in a model's hypothesis, implementation plan, or both, and e...
  </details>

- **2026-10-15** — Ferry Afit Kurniawan, Kazushi Okamoto, Koki Karube et al. — [LLM-Based Weak Annotation for Cybersecurity Tweet Classification: A Teacher-Student Framework](http://arxiv.org/abs/2610.21254v1)
  <details><summary>📄 Abstract</summary>
  Cyber threat intelligence (CTI) relies on the timely identification of emerging threats, enabling organizations and security analysts to support situational awareness and decision-making. Social media platforms such as X (formerly Twitter) have become valuable CTI sources because vulnerabilities and attack activities are often discussed there before appearing in formal reports. However, the rapid growth of cybersecurity discussions on social media has created more content than domain experts can...
  </details>

- **2026-10-15** — Han Su, Meng Tian, Tianyu Huang et al. — [DK-VLM: Geometry as Position for Spatial Reasoning in Vision-Language Models](http://arxiv.org/abs/2610.22356v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models still struggle to understand 3D spatial relations across views and update spatial judgments as the observer moves. A common approach fuses 3D reconstruction features into visual tokens, but aligning these features with pretrained semantic representations remains challenging under limited spatial supervision. We propose DK-VLM with Dual-Kernel Attention, which computes attention from both a visual token's input position and its geometric position in the scene. A semantic ke...
  </details>

- **2026-10-15** — Al Bashir, Partho Ghose, Yibin Wang et al. — [Sim-to-Real Reinforcement Learning for Path-Safe Target Reaching in Robotic Harvesting of Hydroponic Lettuce](http://arxiv.org/abs/2610.22337v1)
  <details><summary>📄 Abstract</summary>
  Robotic harvesting requires precise manipulation to ensure accurate positioning of the end-effector, especially in a constraint workspace. This study introduces the Path-Safe Approach Proximal Policy Optimization (PSA-PPO), a target-conditioned local reaching framework designed for robotic harvesting of nutrient film technique (NFT)-hydroponic lettuce in greenhouses. The proposed PSA-PPO preserves the standard clipped PPO objective while introducing a harvesting-oriented policy formulation that ...
  </details>

- **2026-10-15** — Siqi Chen, Zhengxi Lu, Yuchen Yan et al. — [KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents](http://arxiv.org/abs/2610.22331v1)
  <details><summary>📄 Abstract</summary>
  Deep search agents solve knowledge-intensive tasks through long-horizon, multi-turn interactions, where assigning credit to individual search decisions is fundamentally difficult. Outcome-based reinforcement learning provides only a single terminal reward shared across an entire trajectory. Recent process-supervision methods aim to assign credit at finer granularity, but they typically anchor credit to either surface-level trajectory states or model-internal signals, both of which become unrelia...
  </details>

- **2026-10-15** — Weijian Luo, Yujian Chen, Hao Jiang et al. — [Designing Transformers for Continuous Diffusion Language Models](http://arxiv.org/abs/2610.22330v1)
  <details><summary>📄 Abstract</summary>
  Continuous diffusion language models (CDLMs) offer an alternative approach to parallel language generation; however, most existing studies directly use transformer architectures from either causal large language models (LLMs) or Diffusion Transformers (DiTs) for image generation, which were not optimized for CDLMs. In this paper, we conduct a systematic study on Transformer architectures for CDLMs and introduce Language Diffusion Transformer (LangDiT), combining feature and query-key normalizati...
  </details>

- **2026-10-15** — Yufei Jiao, Jinfa Huang, Zeyue Xue et al. — [SCOPE: Semantic Bounded Credit Optimization for Prompt Engineering in Text-to-image Generation](http://arxiv.org/abs/2610.22264v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) enables language models to improve text-to-image (T2I) generation by rewriting prompts for a frozen image generator. Existing methods typically apply a single signal derived from the image to individual subword tokens, although objects, counts, attributes, and relations form coherent semantic spans. We propose SCOPE, an objective based on Group Relative Policy Optimization (GRPO) that aligns update weighting with this structure. The rewriter jointly generates an enhan...
  </details>

- **2026-10-15** — Ian Gemp, Shubhendu Trivedi, Adam Fisch et al. — [Decentralized LLM Workflows via Sequential Auctions](http://arxiv.org/abs/2610.22201v1)
  <details><summary>📄 Abstract</summary>
  We present a scalable framework for solving multi-step tasks through a decentralized market of self-interested agents. Prior theoretical work demonstrated that agents organized through sequential auctions can converge to a globally optimal policy in a Markov decision process (MDP), but relied on the restrictive assumption of the existence of perfect clones as a model of perfect competition. In reality, exact clones drive agent profit to zero, violating the natural risk-reward incentives of parti...
  </details>

- **2026-10-15** — Tianxiang Fei, Jiazheng Kang, Mao Zheng et al. — [Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing](http://arxiv.org/abs/2610.22196v1)
  <details><summary>📄 Abstract</summary>
  External-memory systems extend language-model applications beyond a context window, but their quality depends critically on the model executing the write path: deciding what to retain, how precisely to represent it, and how new evidence should update persistent state. Existing frameworks typically place a general-purpose large language model behind framework-specific prompts. This raises serving cost, and a writer specialized for one protocol does not transfer directly to another; a unified mode...
  </details>

- **2026-10-15** — Ling-Xiang Zhang, Tao Hu, Da-Wei Zhou — [CART: Compatible Routing for Multimodal Continual Instruction Tuning](http://arxiv.org/abs/2610.22137v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, yet real-world applications often require them to continually acquire new capabilities from sequential tasks, i.e., Multimodal Continual Instruction Tuning (MCIT). In typical MLLMs, a projector is employed to align visual representations with the language model. However, existing methods primarily protect the language model from forgetting while continuously updating the projector across tasks. Such a...
  </details>

- **2026-10-15** — Daniela Baiamonte, Kamyar Zeinalipour, Elena Fano et al. — [Multi-SFT: Permissively-Licensed Multilingual Instruction-Following](http://arxiv.org/abs/2610.22086v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning datasets remain overwhelmingly English-centric and commercially restricted, as their content is frequently generated by proprietary models whose terms of service forbid training competing systems. We introduce Multi-SFT, a commercially permissive collection of 502,818 instruction-response pairs across five European languages, built via translation and regeneration pipelines for tasks where translation is insufficient. Human evaluation yields inter-annotator agreement of at...
  </details>

- **2026-10-15** — Wei Cai, Jian Zhao, Yuchen Yuan et al. — [When Reasoning Is Not Enough: Proactive Inquiry for Cross-Modal Safety in Multimodal Large Language Models](http://arxiv.org/abs/2610.22068v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can act unsafely when individually benign images and texts are interpreted jointly. Beyond implicit reasoning risk, where reasoning drifts toward harm, we identify intent-level risk, where cross-modal ambiguity silently commits the model to a hazardous premise that path-level optimization alone cannot correct. We propose SAFE-PRO, which uses a Risk-Conditioned Uncertainty (RCU) signal, combining predictive entropy with a learned cross-modal risk score, to...
  </details>

- **2026-10-15** — Kalyan Bhetwal, Ceren Mert, Ian Whitehouse — [Name-Bias in Large Language Models](http://arxiv.org/abs/2610.22053v1)
  <details><summary>📄 Abstract</summary>
  Names carry demographic indicators such as age, gender, and race, which makes them a subtle but strong target of bias in large language models (LLMs). In this work, we present an evaluation of name-based bias across 6 local large language models spanning multiple providers and parameter scales. Using a fill-in-the-blank task, we prompt these models to choose between pairs of first names drawn from U.S. Social Security Administration datasets and a race classification dataset by Rosenman et al.. ...
  </details>

- **2026-10-15** — Weihao Li, Zihang Xu, Zhongqiu Wang et al. — [WEAVE: Weaving Real-World Code Evolution into Dependency-Structured Tasks for Benchmarking and Training Code Agents](http://arxiv.org/abs/2610.22039v1)
  <details><summary>📄 Abstract</summary>
  Real-world software engineering rarely consists of isolated changes. Features, migrations, and systematic fixes often unfold across multiple pull requests (PRs), requiring coordinated modifications across a repository. Yet most executable repository-level benchmarks retain a single issue or PR as the task unit, while existing multi-PR settings rely on coarse aggregation and structure-agnostic evaluation. This mismatch obscures dependencies among changes and limits progress measurement and learni...
  </details>

- **2026-10-15** — Anamaría Navarro, E. Khomenko, T. Felipe et al. — [Influence of numerical domain design in simulations of solar coronal heating with the MAGEC code](http://arxiv.org/abs/2610.22012v1)
  <details><summary>📄 Abstract</summary>
  Numerical simulations are essential for studying the solar atmosphere, especially in the context of the coronal heating problem. Understanding how numerical factors and boundary conditions (BC) influence the energetic structure of these models is crucial for unraveling coronal heating mechanisms. We investigate how the computational domain dimensions, upper BC, and vertical grid resolution influence the relaxed thermal structure, energetics, and long-term stability of 2D solar atmosphere simulat...
  </details>

- **2026-10-15** — Julian Christoph Brinkmann — [A Linear-Time Algorithm for the Unbiased Claw Game on Graphs with Maximum Degree 4](http://arxiv.org/abs/2610.21878v1)
  <details><summary>📄 Abstract</summary>
  We study the unbiased Maker-Breaker $K_{1,3}$-game, the unbiased claw game, played on the edge set of a general graph $G$. In this game, Maker and Breaker alternatingly claim edges of $G$, and Maker wins if his claimed edges contain a claw once no more edges are available. Graphs with maximum degree at least 5 are Maker's win. A graph $G$ is claw-connected if the hypergraph modeling the unbiased claw game played on $G$ is connected. We characterize Maker's win in the unbiased claw game on every ...
  </details>

- **2026-10-15** — Giacomo Bais, Tejaswini Deoskar — [Dynamic ordering in sequence generation in Transformers: experiments on low-resource Tagging scenarios](http://arxiv.org/abs/2610.21862v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces TagInsert, a Transformer-based model that challenges the common left-to-right (L2R) generation paradigm in Transformers, for sequence labelling tasks where dependencies may not naturally align with a L2R order. TagInsert lifts the L2R constraint by removing the decoder-side attention mask and enabling the model to decide a preferred order of tag generation at inference time. We experiment on the common Part-of-Speech tagging and the more complex Combinatory Categorial Gramm...
  </details>

- **2026-10-15** — Nikita Tsoy — [Market Incentives for AI Safety Investment](http://arxiv.org/abs/2610.21607v1)
  <details><summary>📄 Abstract</summary>
  Despite their practical significance, modern AI systems pose significant societal risks, including toxicity, malicious use, and misinformation. Their mitigation depends not only on technical feasibility but also on the incentives of firms that develop and deploy these systems. We show how profit maximization shapes safety investment in an AI supply chain with an upstream LLM provider and several competing downstream firms. In our game-theoretic model, we derive the market-driven level of safety ...
  </details>

- **2026-10-15** — Muhammad Ibrahim — [When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill](http://arxiv.org/abs/2610.21500v1)
  <details><summary>📄 Abstract</summary>
  Reusing the attention KV cache across requests is a standard way to cut prefill cost in long-context LLM serving, and production systems increasingly back the per-engine cache with a remote tier shared by every engine. We study such a tier in a disaggregated deployment of GLM-5.3, an FP8 mixture-of-experts model with multi-head latent attention (MLA), on 8xB300 nodes running prefill context parallelism (PCP8). Enabling the remote tier (LMCache with a Valkey store) left median time-to-first-token...
  </details>

- **2026-10-15** — Renhao Li, Xinjie Shen, Yang Su et al. — [MetaExp: Learning to Self-Improve through Experience via Verifiable Cross-Task Environment Scaling](http://arxiv.org/abs/2610.21492v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents can accumulate interaction feedback, but reliably turning that feedback into reusable experience remains challenging. Existing methods either optimize external experience scaffolds or train experience-related behavior on specific task distributions, leaving open whether experience learning itself can become a transferable model capability. Training such a capability calls for supervision beyond isolated tasks, which mainly support in-episode problem solving rather than reve...
  </details>

- **2026-10-15** — Minkyu Kim, Baekseung Kim, Junhoo Lee et al. — [ManiFusion: Unlocking the High-Throughput Generation via Superposition in Manifold Space](http://arxiv.org/abs/2610.21433v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models achieve high-quality image generation but remain computationally expensive due to iterative denoising across many timesteps. Existing acceleration methods mainly reduce per-sample latency, but gains along this axis are becoming saturated. We instead explore an orthogonal throughput-oriented direction by processing multiple samples within a single denoising evaluation. To this end, we propose ManiFusion, a backbone-agnostic framework for multi-sample generation through fused-spac...
  </details>

- **2026-10-15** — Kunlun Zhu, Tao Feng, Xu Han et al. — [JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs](http://arxiv.org/abs/2610.21412v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents now fix software, operate computers and serve customers, but their harnesses, the programs that run them, call a large LLM at every step, which makes long tasks slow and costly. Most of these calls end in a multiple-choice decision, such as which tool to call next. Decision models such as Jev answer these questions directly, at a fraction of an LLM call's time and price. We ask how a harness can delegate these decisions to a decision model with little loss of su...
  </details>

- **2026-10-15** — Po-Cheng Cheng, Hung-Hsuan Chen — [L2GSSL: Label-Efficient Local-to-Global Self-Supervised Learning for Volumetric Healthcare Data](http://arxiv.org/abs/2610.21356v1)
  <details><summary>📄 Abstract</summary>
  Healthcare institutions routinely accumulate high-dimensional computed tomography (CT) volumes, but only a fraction can be annotated by experts. We present L2GSSL, a local-to-global self-supervised learning framework that leverages unlabeled volumes by decomposing pretraining into intra-slice and inter-slice representation spaces. A slice encoder learns view-invariant local features, and a global encoder aggregates the resulting tokens to model volumetric context. The stop-gradient isolates the ...
  </details>

- **2026-10-15** — Li Peng, Jie You, Feng Shi et al. — [Product Costing in Data Pipelines](http://arxiv.org/abs/2610.21352v1)
  <details><summary>📄 Abstract</summary>
  Large data-intensive enterprises spend millions of dollars monthly running data pipelines. Apportioning this cost back to individual products, known as product costing, is a prerequisite for data pricing and cost recovery. However, this process is fundamentally more challenging than physical manufacturing costing due to the unique characteristics of data pipelines, including the non-rivalrous nature of data that complicates the costing formulation, the prevalence of cyclic dependencies that dist...
  </details>

- **2026-10-15** — Ruiqi Gao — [AgentEval: Evidence-Bounded Assessment of Stateful Agents](http://arxiv.org/abs/2610.21177v1)
  <details><summary>📄 Abstract</summary>
  Task completion alone does not determine whether a stateful agent satisfied its obligations, and a recorded judgment does not guarantee that its supporting evidence remains valid. We present AgentEval, a system that carries a contract-bound assessment record through tool execution, state and event capture, report qualification, and case maintenance. It separates what the agent did, what the evidence establishes, and whether the conclusion is supported for present use. On 32 tool-world administra...
  </details>

- **2026-10-15** — Gaocheng Yang, Ruijie Tao, Kai Ye et al. — [GRADS: Graph-Regulated Agentic Data Synthesis with Controllable Difficulty](http://arxiv.org/abs/2610.21167v1)
  <details><summary>📄 Abstract</summary>
  Deep research agents are increasingly deployed to retrieve precise information from large corpora, yet multi-hop, long-horizon tasks remain challenging. Synthetic data generation has emerged as a scalable solution, with existing pipelines typically expanding seed tasks to increase their apparent depth and breadth. However, this expansion does not reliably translate into necessary reasoning: newly introduced evidence may be only weakly coupled to the answer, creating a mismatch between intended a...
  </details>

- **2026-10-15** — Bingbing Wang, Jingjie Lin, Weiming Qiao et al. — [All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents](http://arxiv.org/abs/2610.21147v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly rely on external memory to answer queries grounded in long-horizon histories such as multi-session dialogues and lengthy documents. However, existing memory methods often optimize retrieval and memory construction separately, without a shared reward space for evaluating search, writing, and stopping decisions. To address this, we propose All-in-One Memory (AiO-Mem), which organizes these operations as transitions over a shared evidence state and directly evalua...
  </details>

- **2026-10-15** — Cassie Huang, Zhanwei Cao, Yeawon Lee et al. — [Planning Commitment of LLM under Partial Observability](http://arxiv.org/abs/2610.21108v1)
  <details><summary>📄 Abstract</summary>
  LLM-based planning agents commit to plans of different lengths before interacting with a partially observable environment. Some aggressively commit to a long plan based on assumptions about unobserved states, while others conservatively plan only over what they have observed. Both behaviors emerge implicitly in pre-trained models, whether the LLM outputs a plan directly or generates a PDDL formulation for a classical solver. Aggressive commitment risks costly failures, while conservative commitm...
  </details>

- **2026-10-15** — Tareq Alsaleh, Thomas Zhao, Luke Guardino et al. — [XARA: A Multimodal Agentic System for eXtended Reality Experiment Generation](http://arxiv.org/abs/2610.21067v1)
  <details><summary>📄 Abstract</summary>
  Controlled experiments are essential for advancing transportation research, yet designing eXtended Reality (XR) environments for behavioural studies remains technically demanding and inaccessible to many domain researchers. Current workflows require proficiency in game engines such as Unity or Unreal Engine, imposing significant barriers to rapid scenario prototyping and iterative experiment design. This paper presents XARA, a novel system that integrates a dual large language model (LLM) archit...
  </details>

- **2026-10-15** — Zirui Wu, Chen Guo, Tianjian Jiang et al. — [Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](http://arxiv.org/abs/2610.22363v1)
  <details><summary>📄 Abstract</summary>
  We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed actions; and Plan, which jointly generates action trajectories and their anticipated visual consequences conditioned on an initial image, a l...
  </details>

- **2026-10-15** — Yun Zhang, Zhiyu Huang, Tianhui Cai et al. — [Mem4Act: Learning Effective Latent Memory for Long-Horizon Robotic Manipulation](http://arxiv.org/abs/2610.22323v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robotic manipulation fundamentally requires memory: agents must retain task-relevant information from past observations and interactions and use it to guide future actions. Existing approaches typically preserve raw historical observations, compressed visual tokens, or language summaries, but these representations either expose the action policy to increasingly long histories or risk discarding task-relevant temporal, semantic, and perceptual information. We introduce Mem4Act, a fra...
  </details>

- **2026-10-15** — Bowen Yang, Kaiming Jin, Zichen Ding et al. — [OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using Agents](http://arxiv.org/abs/2610.22234v1)
  <details><summary>📄 Abstract</summary>
  Real desktop automation is neither purely visual nor purely programmatic. Agents must understand user-facing interfaces while efficiently manipulating files, scripts, and system state. However, native GUI/code coordination cannot be obtained by prompt-level tool composition. In our preliminary experiments, naively adding a code tool degrades a GUI agent, revealing that GUI/code routing must be internalized through training on high-quality hybrid data. We present OS-Helix, an end-to-end trained m...
  </details>

- **2026-10-15** — Yuqi Xiong, Chunyi Peng, Zhipeng Xu et al. — [Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models](http://arxiv.org/abs/2610.22217v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) can elicit specialized visual capabilities in vision-language models (VLMs), yet jointly optimizing heterogeneous objectives often introduces cross-capability gradient conflicts. Training experts independently mitigates this interference, but direct reward optimization may entangle specialized knowledge with reward-hacking biases. This paper proposes Skill-Decoupled On-Policy Expert Distillation (SCOPED), which trains capability-specific experts and extracts explicit ...
  </details>

- **2026-10-15** — Jiuyi Xu, Chengyuan Qian, Zhengzhong Tu et al. — [FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models](http://arxiv.org/abs/2610.22146v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often multi-view images are encoded into hundreds of visual tokens that dominate transformer computation and latency. Token compression via attention is a natural solution but is challenging for VLA control because (1) decision-critical tokens are determined by the task, not generic visual ...
  </details>

- **2026-10-15** — Yao Long Teng, Jianguo Huang, Yanchen Deng et al. — [Prism-1: Position- and Rival-Independent Scoring for System One Models](http://arxiv.org/abs/2610.22066v1)
  <details><summary>📄 Abstract</summary>
  Given a state and a set of options, such as intents, tools or interface elements, System One decision models return a distribution over the options in one forward pass, without generated reasoning. Web systems increasingly build them by reading decisions from language models. Two axioms of rational choice are natural requirements for such decisions, because in web systems the listing and the option set are determined by other components and can change or be manipulated: the order in which the op...
  </details>

- **2026-10-15** — Alina Khaybullina — [Momentum, Commentary Tone, and Earnings Surprise in LLM Financial Forecasts](http://arxiv.org/abs/2610.22043v1)
  <details><summary>📄 Abstract</summary>
  Which inputs drive a language model's financial forecast? We construct synthetic earnings announcements that independently reverse 20-day momentum, non-informational commentary tone, and whether fixed actual EPS beats a manipulated consensus. Six instruction/chat checkpoint conversions from four families (0.49-7.61B base parameters) receive 2,016 prompts each under a direct-answer Q8_0 protocol. The design includes 24 numerical blocks, six commentary pairs, profits and losses, rising and falling...
  </details>

- **2026-10-15** — Zewen Wu, Ruizhe Liu, Pei Zhou et al. — [SPEAR: Selective Preference Elicitation with Adaptive Rewards for VLM-Guided Robotic Manipulation](http://arxiv.org/abs/2610.21621v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language Models (VLMs) enable automated preference labeling for robotic manipulation, yet their deployment remains impractical since each query incurs substantial inference cost, while VLMs frequently abstain on visually challenging comparisons. We propose SPEAR, a framework that transforms VLMs into efficient preference oracles via two synergistic mechanisms. First, we design distinguishability-aware query selection to reduce abstention rates by targeting only informative and dist...
  </details>

- **2026-10-15** — Mohammad Dastranj, Jouni Mattila — [Modular Inverse Dynamics and Wrench Recovery for Closed-Chain Mechanisms Using Path Assembly](http://arxiv.org/abs/2610.21400v1)
  <details><summary>📄 Abstract</summary>
  Rigid closed chains can admit indeterminate internal reactions even when their motion is fully specified. This paper develops a modular inverse-dynamics workflow that combines path-based motion reconstruction with recovery of uniquely determined actuator and joint-wrench outputs. Analytical second-order differentiation of assembled transformation paths supplies passive velocities and accelerations on a regular closure branch. Spatial Newton--Euler balances are then assembled over the physical bo...
  </details>

- **2026-10-15** — Vedant Pandhare, Piyush Dhoka — [Calibration Language Shapes Block-Influence Pruning in Multilingual Language Models](http://arxiv.org/abs/2610.21383v1)
  <details><summary>📄 Abstract</summary>
  Block Influence (BI) ranks Transformer blocks for depth pruning from their input-output cosine change, but the ranking depends on the calibration distribution. We study whether English calibration transfers to Indian languages in Qwen2.5-1.5B-Instruct, Llama-3.2-1B, and Gemma-2-2B. English, Hindi, Marathi, and Tamil use disjoint Wikipedia articles for calibration and evaluation; every selector receives the same 150-chunk budget, and Tamil is excluded from multilingual aggregation to test cross-s...
  </details>

- **2026-10-15** — Anh Tuan Nguyen, Anna Bair, Zico Kolter — [Can Capability Enhancement be Localized?](http://arxiv.org/abs/2610.21294v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based language models have shown strong capabilities across many tasks and domains. However, prior work shows that, for a given task, not all attention heads matter equally. Specifically, they suggest that many \textit{redundant} heads can be safely removed with little-to-no effect, while a small set of \textit{important} heads, when ablated, severely damages the model's performance on the given task. In this work, we investigate a complementary aspect, called \textit{Capability Enha...
  </details>

- **2026-10-15** — Bing Cheng, Yiran Mao, Zewei Ye et al. — [Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation](http://arxiv.org/abs/2610.21180v1)
  <details><summary>📄 Abstract</summary>
  General-purpose dexterous manipulation requires policies to transfer knowledge from related tasks to new tasks with only a few target demonstrations. Existing benchmarks often provide too many target demonstrations. They also leave the differences between source and target tasks uncontrolled. As a result, they cannot clearly distinguish knowledge transfer from task memorization. Our key insight is the Core-Gen principle. Core tasks are related tasks that share a functional interaction and provid...
  </details>

- **2026-10-15** — Aditi Saxena, Twinkle Tripathy — [How Do Emotions Spread And Affect Decision-Making In Social Networks? An Opinion Dynamics Perspective](http://arxiv.org/abs/2610.22334v1)
  <details><summary>📄 Abstract</summary>
  Emotions affect how we think and perceive information. Motivated by this, we present a novel framework for modeling emotions, and study its impact in social networks. We represent emotions on a circle by utilizing the circumplex model. These emotions spread in a group through the process of emotional contagion, and influence the interpersonal relationships therein. We propose a model to explain the process of emotional contagion, and its effect on the decision-making process, using a Laplacian-b...
  </details>

- **2026-10-15** — Hanane Nour Moussa, Doeun Lee, Sachin Kumar — [EliteReplay: Preserving Diverse Solutions in RL Post-Training via Quality-Diversity Search](http://arxiv.org/abs/2610.22290v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has become a common post-training technique to improve the accuracy of LLMs on verifiable tasks. However, such training can narrow the set of solutions the model can produce. Several approaches have attempted to address this behavior-sharpening effect, but they often optimize metrics that do not reflect the diversity of correct solutions. Ideally, we want a model that can produce multiple good solutions, not only a single reliable one. We propose EliteReplay, a post-traini...
  </details>

- **2026-10-15** — Lucrezia L. Baldo, Chiara Lionello, Edward D. Donkor et al. — [Learning the information contained in the microstructure of data distributions](http://arxiv.org/abs/2610.22283v1)
  <details><summary>📄 Abstract</summary>
  Understanding how much and where information is nested in sets of data obtained using different parameters and metrics is a typical problem in the analysis of high-dimensional datasets. Approaches based on relative data-driven metrics may be poorly quantitative and difficult to interpret, while accurate methods may be computationally expensive and impractical for large datasets. Here, we report an efficient, quantitative, and transferable method useful to this end, which we call "Micro-Informati...
  </details>

- **2026-10-15** — Adhwaa Al-Chaab, Ayman Younis, Dario Pompili — [X-RIC: An Agentic RAN-Intelligent Controller Benchmark for Enhancing Reinforcement Learning](http://arxiv.org/abs/2610.22269v1)
  <details><summary>📄 Abstract</summary>
  The O-RAN ALLIANCE introduces architectural flexibility through disaggregation and AI-driven control. While the RAN Intelligent Controller (RIC) enables centralized optimization, current AI approaches lack reasoning capabilities and explainability. We propose eXplainable RIC (X-RIC), a novel framework integrating agentic AI into O-RAN architectures. X-RIC combines reactive Reinforcement Learning (RL) with strategic agentic reasoning through: (i) automated Behavioral Cloning (BC) using domain heu...
  </details>

- **2026-10-15** — Shuo Han, Ziqing Hu — [Baselines and Score Centering in Policy Gradient Estimation](http://arxiv.org/abs/2610.22263v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has become a widely used approach to post-training large language models. In a typical implementation, learning is off-policy: The policy generating the responses differs from the policy being trained because of training-inference mismatch or policy staleness in asynchronous training. This discrepancy is commonly addressed by importance sampling, whose ratio is usually regularized in practice through truncation, masking, or clipping. Under regularized importance sampling, ...
  </details>

- **2026-10-15** — Arjun Dadhwal, Brian Summa — [Topology-Inspired Fine-Tuning for Wind-Field Super-Resolution](http://arxiv.org/abs/2610.22262v1)
  <details><summary>📄 Abstract</summary>
  Scientific super-resolution (SR) models are typically optimized with pointwise reconstruction losses, yet scientific interpretation often hinges on extrema, connected regions, and multiscale scalar structure. We characterize this tension with pretrained CNN and GAN wind-field SR models. Pointwise metrics, bottleneck persistence-diagram (PD) distance, and merge-tree (MT) distance favor the CNN, whereas order-2 Wasserstein PD distances favor the sharper GAN, so even different distances on the same...
  </details>

- **2026-10-15** — Hasan Demirkiran, Jens Ernstberger — [Language Is a Security Surface for Agent Guards](http://arxiv.org/abs/2610.22244v1)
  <details><summary>📄 Abstract</summary>
  Step-level guards decide, before each tool call, whether an agent's next action is safe given the user's request and the trajectory so far. Users write those requests in many languages, while guard prompts and the benchmarks on which purpose-built guards are trained and evaluated are English. We ask whether a guard's verdict depends on the language of the request. We build LinguaGuardBench from the 1,220 labelled steps of TS-Bench AgentDojo-Traj: we translate only the user instruction into Germa...
  </details>

- **2026-10-15** — Bingxiang He, Pengqi Sun, Shihao Peng et al. — [AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning](http://arxiv.org/abs/2610.22194v1)
  <details><summary>📄 Abstract</summary>
  Language model agents increasingly automate post-training, but when given the full training stack they converge on supervised fine-tuning and spend most effort revising training data. Existing systems give the agent one kind of control, selecting rows from a fixed pool or calling a generator, whereas a human data engineer adjusts proportions, prunes, repairs, replaces and synthesizes the data. We design a data action space for these changes and ask whether an automated system can make the full r...
  </details>

- **2026-10-15** — Aozhong Zhang, Selcuk Gurses, Yanxia Deng et al. — [DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction](http://arxiv.org/abs/2610.22130v1)
  <details><summary>📄 Abstract</summary>
  Key-value (KV) cache management has become a critical bottleneck for scaling Large Language Models (LLMs) to long-context scenarios due to linear memory growth. While recent eviction methods have moved beyond simple attention-score heuristics to incorporate value representations, they typically face a fundamental trade-off: the underlying optimization for minimizing output perturbation is an NP-hard combinatorial problem, leading to mathematically suboptimal heuristics or implementations that ar...
  </details>

- **2026-10-15** — Sekh Mainul Islam, Pepa Atanasova, Isabelle Augenstein — [Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization](http://arxiv.org/abs/2610.22127v1)
  <details><summary>📄 Abstract</summary>
  Personalization of Large Language Models (LLMs) is increasingly important for user-centric applications, yet prior methods mainly adapt dense LLMs, whose polysemantic neurons, each encoding multiple unrelated concepts, hinder localizing the components behind personalization, and thus understanding and controlling it. We propose to personalize Mixture-of-Experts (MoE) LLMs, which sparsely route each token to a few specialized experts, reducing polysemanticity and enabling such localization. We ad...
  </details>

- **2026-10-15** — Vahid Yazdnian, Yasaman Ghasempour — [Scene Reconstruction Using Ubiquitous Wireless Signals via Diffusion Posterior Inference Over physics-Grounded Representations](http://arxiv.org/abs/2610.22120v1)
  <details><summary>📄 Abstract</summary>
  Knowing the layout of the physical world matters for many applications, yet the sensors we rely on for it (e.g., cameras and LiDAR) can fail in darkness, in adverse weather, or behind walls. Wireless signals do not face these limitations: every link between a base station and a user is shaped by the buildings it passes, reflects from, or is blocked by, leaving information about the surrounding scene embedded in the wireless channel measured at the endpoints. However, mapping channel measurements...
  </details>

- **2026-10-15** — Nicolás Vera Zúñiga — [Patch where the text is new: a compression view of where byte-level models should spend compute](http://arxiv.org/abs/2610.22100v1)
  <details><summary>📄 Abstract</summary>
  Byte-level language models such as the Byte Latent Transformer (BLT) run their large global model once per patch and start a patch where a small model's next-byte entropy is high. This rule rarely starts a patch at in-line computed results, such as the number after "=" in a worked solution, and accuracy on them collapses under tight patch budgets. We propose novelty patching, motivated by LZ77-style compression: start a patch where the upcoming bytes are unlikely to repeat the recent context. Th...
  </details>

- **2026-10-15** — Shiwen Qin, Cameron Barker, Henry Gouk et al. — [Beyond Context Length: Characterising the Difficulty of Long-Context Reasoning](http://arxiv.org/abs/2610.22067v1)
  <details><summary>📄 Abstract</summary>
  Long-context language models support ever longer context windows, and evaluations typically treat context length as the main indicator of difficulty. However, context length alone cannot explain why models fail on long-context tasks that require reasoning over complex information. Contexts of equal length can pose very different challenges: a task may be solvable from a single local passage, or it may require integrating evidence distributed across the full context. We quantitatively characteris...
  </details>

- **2026-10-15** — Adam Deng, Shicheng Liu, Yada Zhu — [Close Enough is Nowhere Near: Fidelity-Consumability Decoupling in KV Caches](http://arxiv.org/abs/2610.22016v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems communicate in text, which is lossy and wasteful: the sender throws away the reading it already did. A growing literature instead transmits the KV cache, the natural carrier of that reading. We study the most appealing form of the idea: both models stay frozen and the sender's cache is substituted for the reader's with nothing trained. It does not work, and the obstruction belongs to the reader. A frozen transformer reads only caches close to the one it would have written...
  </details>

- **2026-10-15** — Xiaoqing Lian, Pei Liu, Jiahui Tan et al. — [Panoramic modelling of single-cell transcriptomes at scale with CellNet](http://arxiv.org/abs/2610.21943v1)
  <details><summary>📄 Abstract</summary>
  Comprehensively characterizing cellular diversity is critical for understanding tissue development, identifying disease-associated populations and investigating gene programmes linked to specialized functions. Advances in single-cell profiling reveal additional cell-specific transcripts and molecular associations, yet many foundation models represent only a restricted portion of this increasingly rich molecular information. Here we present CellNet, which enables panoramic modelling of single-cel...
  </details>

- **2026-10-15** — Lo Gullstrand Heander, Markus Borg, Emma Söderberg et al. — [CodeHealth Predicts the Token Cost of Agentic Code Review: A Pre-Registered Study of 465 Agent-Authored Pull Requests](http://arxiv.org/abs/2610.21914v1)
  <details><summary>📄 Abstract</summary>
  Context: Organizations increasingly delegate code review to multi-agent large language model (LLM) pipelines billed per token. Low code quality raises human maintenance effort, but its effect on agent review cost has not been measured.   Objective: We test whether baseline CodeHealth predicts the token cost of agentic review and fix beyond pull request (PR) footprint.   Method: In a pre-registered observational study, we sampled 465 agent-authored PRs from 246 repositories in AIDev, jointly stra...
  </details>

- **2026-10-15** — Antoine Bergerault, Cyrille Kone, Giorgia Ramponi — [Learning Rewards in Strategic Games](http://arxiv.org/abs/2610.21912v1)
  <details><summary>📄 Abstract</summary>
  Understanding the objectives that drive agents' behavior is crucial in strategic environments, where multiple agents interact and adapt to one another. This challenge arises in domains such as cybersecurity, autonomous driving, and online markets, where agents' underlying incentives are typically unknown and must be inferred from their observed behavior. Inverse reinforcement learning (IRL) provides a natural framework for this problem, but extending IRL to strategic multi-agent settings introdu...
  </details>

- **2026-10-15** — Dongjie Cheng, Ruifeng Yuan, Ran Wei et al. — [CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness](http://arxiv.org/abs/2610.21910v1)
  <details><summary>📄 Abstract</summary>
  As Vision-Language Models (VLMs) advance, they are increasingly expected to perform spatiotemporal reasoning over motion, actions, and view changes beyond what the input images show. Video World Models (VWMs) provide a natural unified engine for visual imagination by generating task-relevant visual content as additional evidence. However, existing approaches typically invoke a VWM through fixed pipelines centered on a predefined form of visual imagination, such as novel-view synthesis. To suppor...
  </details>

- **2026-10-15** — Yiqun Zhao, Binbin Huang, Haobin Duan et al. — [Seeing Both the Forest and the Trees: Reusing Holistic 3D Priors for Part-Decomposed Generation](http://arxiv.org/abs/2610.21850v1)
  <details><summary>📄 Abstract</summary>
  Generating 3D assets with explicit parts requires two properties at once: geometric detail inside each part and structural coherence across the whole object. Recent image-conditioned 3D generation models adopt a structured 3D representation that anchors tokens to explicit spatial positions, capturing both properties, but their output remains a single fused mesh. We ask how a part-decomposed generation model can inherit both properties of these holistic priors, and answer with STRUCTPARTS, a fram...
  </details>

- **2026-10-15** — Mathias Lowes, Kristine Aavild Sørensen, Maxime Sermesant et al. — [Temporal Periodic Image Registration with Implicit Neural Representations](http://arxiv.org/abs/2610.21845v1)
  <details><summary>📄 Abstract</summary>
  Implicit Neural Representations (INRs) have recently gained popularity for their ability to model functions using simple and lightweight networks. These methods have also proven effective in deformable image registration. In this work, we extend INRs for deformable image registration to the domain of temporal image registration, focusing on periodic temporal image sequences. Our approach, Temporal-IDIR, optimizes a single INR to model deformations across all frames in a temporal image sequence s...
  </details>

- **2026-10-15** — Zhu Wenbo — [Exact Makespan Bounds and the GPipe Homogeneity Bias for Heterogeneous LLM Inference Pipelines](http://arxiv.org/abs/2610.21815v1)
  <details><summary>📄 Abstract</summary>
  We give an exact critical-path characterization of the makespan of micro-batch pipelines serving LLMs on heterogeneous GPU clusters, quantifying how the classic homogeneous GPipe formula errs. In the pure-forward, communication-free, infinite-buffer setting, T(M) = (M-1)tau_max + Sum_j tau_j, where tau_j is stage j's per-micro-batch service time and M the micro-batch count (Theorem 1). Under asynchronous communication -- modern NCCL-based serving -- it extends to T(M) = Sum_j tau_j + Sum_j d_j +...
  </details>

- **2026-10-15** — Simon Freitter, David Fischinger, Silvia Poletti et al. — [DINO-FIL: Multi-Layer Transformer Fusion for Generative Inpainting Forgery Localization](http://arxiv.org/abs/2610.21780v1)
  <details><summary>📄 Abstract</summary>
  We propose DINO-FIL, a transformer-based framework for pixel-level localization of generative image forgeries. The method leverages multi-layer representations from a pretrained DINOv3 ViT-H+/16 encoder combined with a lightweight fusion decoder to capture both semantic structure and fine-grained texture inconsistencies introduced by image editing. By aggregating intermediate transformer features across depths, the model improves sensitivity to subtle, spatially localized artifacts that are ofte...
  </details>

- **2026-10-15** — Boyu Cui, Junhao Luo, Zhihao Wang et al. — [From Perception to Prediction and Intervention: Benchmarking Proactive Video Assistants in Real-Life Scenarios](http://arxiv.org/abs/2610.21568v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal large language models have advanced video understanding, but existing benchmarks mainly evaluate whether models can interpret observed visual content. In real-world scenarios, assistants must additionally anticipate what assistance is needed and decide when to provide it. To address this gap, we introduce \textsc{P$^3$IBench}, a benchmark for proactive video understanding in real-life streaming scenarios. It evaluates three complementary capabilities: daily perception, risk pre...
  </details>

- **2026-10-15** — Camila Kolling, Omer Moussa, Emin Çelik et al. — [SCRIBE: Scalable Contextual Representations of Interpretable Brain-Grounded Semantics](http://arxiv.org/abs/2610.21518v1)
  <details><summary>📄 Abstract</summary>
  Understanding how the human brain constructs meaning from real-world language remains a fundamental challenge, as semantics depend on context that varies in natural settings. To enable the study of real-world linguistic meaning in the brain, we introduce SCRIBE, a framework grounded in a neuroscience-informed semantic space that leverages an ensemble of open-source large language models to generate interpretable, word-level semantic representations of arbitrary text. In a behavioral study with 9...
  </details>

- **2026-10-15** — Wei Zeng, Ye Wang — [DuET: Note-Frame Dual Encoding for Piano Performance-to-Score Transcription](http://arxiv.org/abs/2610.21467v1)
  <details><summary>📄 Abstract</summary>
  Transcribing expressive piano performances into scores requires interpreting individual note timings within an underlying metrical structure. However, score attributes are associated with notes, whereas beats may occur without coincident note onsets. We introduce DuET, a Dual-Encoder Transformer that jointly learns note-level performance MIDI-to-score (PM2S) transcription and frame-level beat and downbeat tracking. Bidirectional cross-attention connects note and frame encoders, while an autoregr...
  </details>

- **2026-10-15** — Atai Waris Khan, Abdullah Mazhar, Raghu Kumar et al. — [Translation Circuit Discovery and Targeted Optimization for Low-Resource Multilingual Translation](http://arxiv.org/abs/2610.21456v1)
  <details><summary>📄 Abstract</summary>
  Recent multilingual large language models achieve strong translation performance, yet the internal mechanisms responsible for low-resource multilingual translation remain insufficiently understood. In this paper, we study translation circuits in multilingual decoder-only LLMs for Hindi-to-Urdu and Hindi-to-Sindhi (Devanagari). We propose TITAN, a mechanistic framework that combines causal intervention, sparse feature decomposition, and targeted preference optimization to identify and optimize cr...
  </details>

- **2026-10-15** — Zhezheng Hao, Yongkang Yang, Xilin Xia et al. — [Learning from Interaction Experience via Localized Context Distillation](http://arxiv.org/abs/2610.21427v1)
  <details><summary>📄 Abstract</summary>
  Learning from interaction experience is essential for enabling large language models to continually improve during deployment. Context distillation offers a promising path: privileged information extracted from experience is provided to a teacher, whose behavior is then distilled into a student model that has no access to it. However, both existing forms of context distillation have limitations. Off-policy context distillation trains the student on teacher-generated trajectories and thus suffers...
  </details>

- **2026-10-15** — Mengtao Wen, Haojie Ren, Changliang Zou — [Controlling the False Discovery Rate via Model-Agnostic Importance Measures](http://arxiv.org/abs/2610.21360v1)
  <details><summary>📄 Abstract</summary>
  Selecting covariates while controlling the false discovery rate (FDR) is critical for interpretable scientific discovery, especially with complex machine learning models. Traditional variable selection methods often rely on specific model assumptions, while Model-X knockoffs provide a general way that leverages knowledge of the covariate distribution to produce a variable selection algorithm. This study puts forward a complementary method to Model-X knockoffs, named Model-Agnostic Selection with...
  </details>

- **2026-10-15** — Max Rosenblattl, Milana Gurbanova, Karl Aurel Deck et al. — [TimeCap: A Scalable Open-Source Pipeline for Captioning Wearable Health Time-Series Data](http://arxiv.org/abs/2610.21274v1)
  <details><summary>📄 Abstract</summary>
  Time-series data generated continuously across industrial, environmental, and especially health domains produce multimodal signals whose scale and heterogeneity make their processing and interpretation particularly challenging. Time-Series Language Models (TSLMs) promise scalable interpretation of these signals, yet remain bottlenecked by a fundamental lack of text-annotated time series pairs that are signal-grounded, reproducible, and extensible across modalities and schemas. Existing paired co...
  </details>

- **2026-10-15** — Zhizhuo Kou, Jian Yang, Pengfei Hao et al. — [Entertain, then Cancel: How Thinking Makes Reasoning Models Read Some and Or Literally](http://arxiv.org/abs/2610.21204v1)
  <details><summary>📄 Abstract</summary>
  When a speaker says ``some students passed'', listeners infer that not all of them did. Reasoning models now let users decide how long a model thinks before it answers, but we do not know what extra thinking does to such everyday inferences. We study this directly: we keep a model's weights fixed, change only how much it thinks, and record which reading it chooses. A second tool cuts the model's own reasoning at successive points and asks for an answer, showing where the reading changes. Thinkin...
  </details>

- **2026-10-15** — Lei Wu, Yang Xiao, Jin Min Yang et al. — [PTagent: An LLM-assisted tool for finite-temperature model construction in cosmological phase transitions](http://arxiv.org/abs/2610.21118v1)
  <details><summary>📄 Abstract</summary>
  Cosmological phase-transition calculations require well-defined finite-temperature numerical models, whose construction involves assembling model information under consistent theoretical prescriptions. In this work we present \texttt{PTagent}, a large language model (LLM) agent-based framework for constructing such models from SARAH model files, research papers, and DRalgo sources. The LLM agent interprets and organizes model information and identifies unresolved physical choices, while dedicate...
  </details>

- **2026-10-15** — Isarar Siddique, Raiyan Siddique, Arshi Niyaz et al. — [Evidence Field for Histopathology: Cross-Centre Evaluation and Replayable Spatial Decisions](http://arxiv.org/abs/2610.21115v1)
  <details><summary>📄 Abstract</summary>
  Histopathology classifiers must transfer across acquisition sites while exposing evidence that can be checked independently. Evidence Field couples learned image measurements and spatial classification with a native covering-program record. We evaluate this architecture on all 455,954 released CAMELYON17-WILDS patches, using patient-separated source partitions and two held-out hospital centres. Eighteen from-scratch fits compare four Evidence Field objectives with residual convolutional and comp...
  </details>

- **2026-10-15** — Lianfa Li — [Bellman-Consistent Trajectory RL for LLM Arithmetic Reasoning](http://arxiv.org/abs/2610.21060v1)
  <details><summary>📄 Abstract</summary>
  To address sparse terminal rewards in LLM arithmetic reasoning, we propose a Bellman-consistent trajectory RL method. Our framework introduces Trajectory Bellman Residual Minimization (TBRM) to transform sparse rewards into dense token-level signals. We integrate a Reinforce Leave-One-Out (RLOO) group strategy to reduce gradient variance of Bellman residuals and use hindsight goal relabeling to accelerate intermediate learning. Evaluated on the Countdown task, our method alleviates optimization ...
  </details>

- **2026-10-14** — Lucius Bushnaq, Dan Braun, Oliver Clive-Griffin et al. — [Interpreting Language Model Parameters](http://arxiv.org/abs/2610.20748v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability aims to uncover how neural networks use their parameters to implement their impressive neural algorithms. Although previous work has uncovered substantial structure in the intermediate representations that networks use, little progress has been made to understand how the parameters and nonlinearities of networks perform computations on those representations. In this work, we present a method that brings us closer to this understanding by decomposing a language model'...
  </details>

- **2026-10-14** — Miaobo Hu, Shuhao Hu, Xiaobo Guo et al. — [CascadeLedger: Counterfactual Auditing of Information and Resource Integrity in LLM Cascades](http://arxiv.org/abs/2610.20668v1)
  <details><summary>📄 Abstract</summary>
  We introduce CascadeLedger, a counterfactual execution-audit framework for budgeted language-model cascades. The protocol enforces call-before-read semantics, binds successful reads to service and cache identities, records availability and component-wise budget transitions, and freezes the event trace before any target or task scorer is joined. The central object is aggregate-equivalent trace validity: two executions can share a final answer, declared resource projection, and service histogram w...
  </details>

- **2026-10-14** — Yifei Liu, Xiaolong Zhou, Ziyang Gong et al. — [DeSpatial: The devil of Agentic Spatial Reasoning Lies in 3D Itself](http://arxiv.org/abs/2610.20990v1)
  <details><summary>📄 Abstract</summary>
  Spatial agents have access to reconstruction and segmentation tools, yet inconsistent predictions and fragmented object identities can prevent their outputs from becoming reliable 3D scene information. A simple oracle experiment exposes this perception bottleneck: replacing tool-predicted perception with ground-truth 3D bounding boxes raises an agent to nearly full score across five object-centric VSI-Bench tasks, while retaining the same reasoning tools. Motivated by this finding, we believe th...
  </details>

- **2026-10-14** — Chai K. Toh, Vasu Raj Jain — [A Multi-Tiered AI Accessibility Model (MAIAM): Proportionate Access and Capability Limits for Comprehensive Frontier AI Safety](http://arxiv.org/abs/2610.20921v1)
  <details><summary>📄 Abstract</summary>
  Most debate about releasing capable AI systems treats the choice as binary: keep the model behind an API, or publish the weights. That framing runs together two separate decisions. One is how capable a system may become. The other is who may obtain a given capability, and on what terms. This paper is about the second decision. We propose a Multi-Tiered AI Accessibility Model (MAIAM) that sorts access by purpose, safety, and capability instead of by release artifact. Tier 1, AI for Learning, is b...
  </details>

- **2026-10-14** — Junze Zhou, David Klindt — [Complete or Sparse: A Tale of Two Identifiabilities](http://arxiv.org/abs/2610.20851v1)
  <details><summary>📄 Abstract</summary>
  Understanding when neural networks learn interpretable representations is central to mechanistic interpretability. We study this through identifiability: when can supervised learning recover the true latent variables underlying the data? We introduce two data generating processes distinguished by their causal direction where either labels cause latents (generative) or latents cause labels (discriminative). When the representation has at least as many dimensions as the latent space, we prove that...
  </details>

- **2026-10-14** — Qian Yu, Zongyang Qiu, Juncheng Yan et al. — [Intern Lumina U2: A Multi-Codebook Diffusion Large Language Model for Omni-Visual Understanding and Image Generation](http://arxiv.org/abs/2610.20818v1)
  <details><summary>📄 Abstract</summary>
  Unified multimodal generation covers discrete, continuous, and hybrid paradigms. Discrete approaches with single-codebook visual tokenizers align naturally with text modeling but have limited representational capacity. Continuous and hybrid approaches retain richer visual representations, but they model text and images in heterogeneous spaces with different training objectives, potentially introducing optimization conflicts between modalities with misaligned representation spaces. These choices ...
  </details>

- **2026-10-14** — Jianyu Zhang, Léon Bottou — [Open-world AI: a Tale of Three Requirements](http://arxiv.org/abs/2610.20782v1)
  <details><summary>📄 Abstract</summary>
  The closed world asks AI for specialized competence and lets it manufacture the iid data its theory assumes: a fixed criterion licenses collecting examples until the task is covered. The open world asks for versatility --- taking up tasks a machine was not built for, from few examples and with little prior from a human designer --- and offers data that is grouped, not shuffled. Its tasks are not known in advance, so a machine must do inference-time learning (1st requirement). Modeling tasks as s...
  </details>

- **2026-10-14** — Gwen Legate, Rahaf Aljundi, Eugene Belilovsky — [Optimal Hydra: Model Heterogeneous Federated Learning for LLMs using Data-Informed Hydra-Nets](http://arxiv.org/abs/2610.20753v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) trained on vast amounts of data have demonstrated impressive performance over a range of tasks, but future performance gains will require increasing amounts of data and compute. Federated Learning (FL) facilitates training on decentralized private data, but client resource limitations can make training impractical, particularly as model sizes continue to expand. These resource constraints make the assumption of a shared server-client architecture impractical. Model h...
  </details>

- **2026-10-14** — Letian Huang, Xiangyu Wang, Haowei Lin et al. — [L2G-SR: Learning to Guide LLM-based Symbolic Regression](http://arxiv.org/abs/2610.20685v1)
  <details><summary>📄 Abstract</summary>
  Symbolic regression searches for an equation that explains observed data. Numerical error is commonly used to guide the search, but it alone can favor an accurate surrogate over a candidate with the right structure. We propose L2G-SR, a framework for LLM-based symbolic regression that guides search with a learned structural verifier. We construct structural supervision signal using tree edit distance (TED), accounting for commutative operators and alternative expression forms. A verifier first a...
  </details>

- **2026-10-14** — Harsh Kumar, Tanmay Shailesh Joshi, Rahul Maity et al. — [Causal Syntax Circuits in CodeLMs: Budget and Probe Decide What Looks Localised](http://arxiv.org/abs/2610.20683v1)
  <details><summary>📄 Abstract</summary>
  Code models write Python when the prompt does not say which language to use. We ask a mechanistic question about that habit: is it produced by a small, findable group of components inside the model? We run one pipeline---mean ablation, activation patching, greedy circuit extraction, a random-control significance test, and activation steering---over 55 model-language settings spanning ten open code models (five base and five instruction-tuned), three target languages (Rust, C#, PHP), two prompt s...
  </details>

- **2026-10-14** — Cezar Sas, Sandra Mitrović, Fabio Barth et al. — [The Code of Theseus: Can Agents Rebuild Software from Recovered Design Documents?](http://arxiv.org/abs/2610.20068v2)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly design a system before implementing it, yet the data to train and evaluate them centres on implementation and testing: requirements and design artefacts are often missing, outdated or private. Source code, in contrast, is abundant. Prior work recovers architecture documentation by feeding LLMs the source code or letting agents explore it, which saturates the context, does not scale to many repositories, and yields a single artefact rather than aligned ones.   We present a...
  </details>

- **2026-10-14** — Yiyang Cai, Tatsuya Kamijo, Ninghao Lu et al. — [MoCaP: Mobile Code-as-Policies for Zero-Shot Mobile Manipulation from Passive Human Videos](http://arxiv.org/abs/2610.20998v1)
  <details><summary>📄 Abstract</summary>
  Passive human videos of everyday activity offer robots access to a massive amount of human experience without requiring a demonstration for each task. However, using this experience requires recovering knowledge from unstructured video recordings and adapting it to a different body (i.e., the robot). To overcome these challenges, we present mobile code-as-policy (MoCaP), an agentic framework that turns passive human video recordings into guidance for an end-to-end mobile manipulation policy. MoC...
  </details>

- **2026-10-14** — Aiden Swann, Mathilde Papillon, Mozes Jacobs et al. — [Causal Analysis of Robot Foundation Models Enables Efficiency Gains](http://arxiv.org/abs/2610.20750v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question mechanistically in three frontier VLA models ($π_{0.5}$, MolmoAct2, and MolmoBot) by analyzing the causal pathways through which the input i...
  </details>

- **2026-10-14** — Zikang Yaoa, Eugene Yeea, Fue-Sang Lien — [A differentiable PCA-GPR surrogate framework for full-transient Bayesian inverse uncertainty quantification of black-box nuclear thermal-hydraulic systems](http://arxiv.org/abs/2610.20978v1)
  <details><summary>📄 Abstract</summary>
  Complex transient energy systems require uncertainty-quantified predictions, but Bayesian inverse uncertainty quantification (IUQ) is often impractical because posterior sampling with high-fidelity system codes requires many expensive full-transient simulations. This study develops a surrogate-assisted Bayesian IUQ framework that makes full-time-series calibration practical for the NACIE heavy-liquid-metal natural-circulation loop. The key innovation is to transform a black-box transient simulat...
  </details>

- **2026-10-14** — Yihang She, Andrew Blake, Jianbo Qi et al. — [PiCo: Physics-Informed Concept Probing for Geo-Foundation Models](http://arxiv.org/abs/2610.20973v1)
  <details><summary>📄 Abstract</summary>
  Geo-foundation models (GFMs) are typically evaluated by downstream task predictive performance, revealing little about which physical features they are sensitive to or use in prediction. This limits developers' ability to test hypotheses about model behaviour and users' ability to select models for new tasks. We propose Physics-Informed Concept Probing (PiCo), a post-hoc framework for explaining GFM predictions. PiCo identifies concept vectors in a GFM's embedding space by generating synthetic m...
  </details>

- **2026-10-14** — Zhivar Sourati, Marianne Menglin Liu, Rongguang Wang et al. — [VELD-QA: A Large-Scale Dataset for Visual Evidence Grounding and Question Answering in Long Documents](http://arxiv.org/abs/2610.20964v1)
  <details><summary>📄 Abstract</summary>
  Existing long-document QA benchmarks rarely combine large-scale human-authored questions with detailed visual evidence annotations, limiting diagnosis of evidence localization and interpretation failures. We present VELD-QA, a large-scale benchmark for Visual Evidence grounding and question answering in Long Documents. It contains 15,000 fully human-authored question-answer pairs across 5,859 real-world PDFs totaling 372,445 pages, balancing chart, table, and complex-layout tasks. Human annotati...
  </details>

- **2026-10-14** — Beth Pearson, Michael Wray, Martha Lewis — [Probing Negation Understanding in Vision-Language Models With Object Attention](http://arxiv.org/abs/2610.20852v1)
  <details><summary>📄 Abstract</summary>
  Negation is a fundamental aspect of language understanding and it is important vision-language models (VLMs) are able to process it effectively. We investigate how VLMs process negation by analysing attention patterns of different models. We draw comparisons between human gaze and attention in models when processing affirmative vs negated statements. We compare object level model attention to human eye-fixations in both binary and multary settings, evaluating with both synthetic and realistic da...
  </details>

- **2026-10-14** — Wenhao Yan, Haodong Li, Xiaotong Li et al. — [WorldCast: Exploring Intelligent Visual Generation in World State Prediction](http://arxiv.org/abs/2610.20731v1)
  <details><summary>📄 Abstract</summary>
  Humans interpret multimodal observations of the world and forecast how it will evolve. Recent multimodal generative systems have demonstrated similar capabilities: they can integrate multimodal context and synthesize visual outputs that depict changes in the world. To characterize this emerging trajectory, we organize model capabilities into a four-level hierarchy and discover that higher-level tasks remain relatively underexplored despite model progress. To bridge this gap, we explore model per...
  </details>

- **2026-10-14** — Anita Zanella, Andreas L. Faisst, Rodrigo Herrera-Camus et al. — [ALMA2040: Understanding the Early Assembly of Galaxies - The Formation of Star-Forming Clumps and their Role in Shaping Galaxy Evolution](http://arxiv.org/abs/2610.20730v1)
  <details><summary>📄 Abstract</summary>
  Astrophysics seeks to explain how galaxies form and evolve through the interplay of stars, gas, and dust. Giant molecular clouds (GMCs), the main reservoirs and sites of star formation, link the cold interstellar medium to the birth of stars and stellar structures. Their properties reflect galactic disk conditions, and their evolution is shaped by stellar feedback and host-galaxy dynamics. Studying GMCs across cosmic time is therefore key to understanding how gas turns into stars and drives gala...
  </details>

- **2026-10-14** — Fazle Mohammed Tasfiq, Sabab Attin, Sheikh Md. Tahmid Hossain et al. — [Analyzing performance of Retrieval Augmented Generation models for Question Answering Tasks](http://arxiv.org/abs/2610.20419v2)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) models have become almost a cornerstone of open-domain question answering tasks; in which the quality of answers generated in the process, greatly relies on the effectiveness of retrieval mechanisms. In the realm of LLM, the last two years have seen tremendous progress in RAG architectures, with many models reporting to have improved performance through various design innovations. The cultural question and answering systems of South Asia, in particular, prese...
  </details>

- **2026-10-14** — Nhat-Minh Le-Phan, Ziliang Lyu, Lihua Xie — [Resilient Angle-Constrained Formation Control and Localization Under DoS Attacks (Extended Version)](http://arxiv.org/abs/2610.19824v1)
  <details><summary>📄 Abstract</summary>
  This paper studies resilient angle-constrained leader--follower formation control and localization of multi-agent systems under asynchronous denial-of-service (DoS) attacks, which block individual sensing and communication links. To preserve the well-posedness of angle-based localization, an all-or-nothing triangle integrity protocol (ANTIP) is proposed to convert edge-wise attacks into triangle-wise ones, and DoS attacks are classified into localizability-maintained and localizability-broken at...
  </details>

- **2026-10-14** — Xiaoli Xu, Zhengtao Wu, Zhengze Xu et al. — [CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation](http://arxiv.org/abs/2610.20603v1)
  <details><summary>📄 Abstract</summary>
  We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists through an iterative closed loop of VLM and LLM roles scored by a reference-free rubric. Layout Thinker Op...
  </details>

- **2026-10-14** — Delip Rao, Ahmed Muharram, Chris Callison-Burch — [Same Claim, Different Interpretations: How LLM Agents Resolve Ambiguity in Scientific Claims](http://arxiv.org/abs/2610.20457v1)
  <details><summary>📄 Abstract</summary>
  Co-scientists and agentic scientific claim verifiers are increasingly used to assess claims across the sciences. Natural-language scientific claims, written for human experts, are often underspecified and so admit several defensible interpretations. Such verifiers usually pick one, often tacitly, and benchmarks score their verdicts against expert labels without recording the expert's interpretation or the verifier's in a comparable form. This leads to disagreements with expert labels that cannot...
  </details>

- **2026-10-14** — Chih-Han Lin, Yu-Yun Chang, Po-Ya Angela Wang et al. — [Lexical Persistence Without Semantic Entrenchment in AI Agent Communities](http://arxiv.org/abs/2610.20365v1)
  <details><summary>📄 Abstract</summary>
  AI agent communities sustain lexical persistence, popular terms spread, recur, and achieve broad adoption, but whether they also develop the temporal semantic structure characteristic of human linguistic communities remains open. We compare MoltBook (AI agent community, 8 weeks), PTT (Chinese human BBS, 19 years), and Reddit (English human forum, in matched 8-week windows) using Compass-Aligned Distributional Embeddings (CADE), measuring semantic drift (B1), neighborhood stability (B2), and lag-...
  </details>

- **2026-10-14** — Yuyao Ge, Shenghua Liu, Peizhong Gao et al. — [Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents](http://arxiv.org/abs/2610.20344v1)
  <details><summary>📄 Abstract</summary>
  Agents driven by large language models are increasingly deployed on long-horizon tasks, where they use tools and modify real workspaces. How well they perform depends as much on the harness around the model as on the model itself. Existing benchmarks measure downstream task success under a fixed harness, leaving harness engineering itself unexplored. We propose Doc2Harness, a two-stage benchmark that evaluates long-horizon harness engineering directly. In Stage 1, a build model operating inside ...
  </details>

- **2026-10-14** — Danyang Zhao, Sendong Zhao, Yanrui Du et al. — [Taking the PULSE of Medical Reasoning: Step-Level Retrieval Timing for Knowledge-Grounded Inference](http://arxiv.org/abs/2610.20292v1)
  <details><summary>📄 Abstract</summary>
  Reliable medical reasoning requires LLMs to dynamically access external biomedical evidence to improve factual trustworthiness and reasoning accuracy. However, indiscriminate retrieval can introduce noise and latency, raising a critical retrieval-timing problem: at each reasoning step, the system must decide whether the model's internal knowledge is reliable or external evidence is needed. We propose PUlSE, a lightweight probing method that uses the model's internal representations as intrinsic ...
  </details>

- **2026-10-14** — Junze Zhu, Weihao Chen, Zhiyang Zhou et al. — [Harness Policy Distillation: Aligning Agent Policies with Runtime Semantics](http://arxiv.org/abs/2610.20261v1)
  <details><summary>📄 Abstract</summary>
  Deploying a general-purpose model as an agent means running it inside a product-specific runtime harness that decides which actions are executable, how state advances, and when the loop may terminate. Ordinary trajectory supervision shows which action was taken but leaves the runtime semantics behind that action implicit. We introduce Harness Policy Distillation (HPD), which makes these runtime control semantics an explicit training target alongside actions to align the harness policy. HPD repla...
  </details>

- **2026-10-14** — Cédric Rousseau, Javier González-Colsa, Victor Joris et al. — [From Single-Particle Thermal Asymmetry to Collective Control: Janus Plasmonic Colloids for Photothermal Applications](http://arxiv.org/abs/2610.20189v1)
  <details><summary>📄 Abstract</summary>
  Janus nanoheaters provide a route to break the spatial symmetry of thermoplasmonic heating and generate directionally biased thermal gradients at the nanoscale. However, in realistic photothermal scenarios, nanoheaters rarely act as isolated objects, but rather operate within colloidal assemblies where collective thermal and electromagnetic effects reshape the local temperature landscape. Here, we investigate how the intrinsic thermal asymmetry of a single Janus plasmonic nanoheater is transform...
  </details>

- **2026-10-14** — Shijun Shi, Zhe Liu, Zhi Hou et al. — [Atomic-WAM: Execution-Grounded Atomic-Motion Reasoning for World Action Models](http://arxiv.org/abs/2610.20157v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) typically adapt video foundation models to robotic control through joint video and action prediction. However, task-level instructions may leave the next physical interaction underspecified, requiring semantic grounding and state-dependent motion selection. To this end, we introduce Atomic-WAM, an understand-then-execute framework that connects task reasoning to action generation through atomic-motion descriptions. Specifically, a vision-language reasoner describes the...
  </details>

- **2026-10-14** — Cezar Sas, Sandra Mitrović, Fabio Barth et al. — [The Code of Theseus: Can Agents Rebuild Software from Recovered Design Documents?](http://arxiv.org/abs/2610.20068v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly design a system before implementing it, yet the data to train and evaluate them centres on implementation and testing: requirements and design artefacts are often missing, outdated or private. Source code, in contrast, is abundant. Prior work recovers architecture documentation by feeding LLMs the source code or letting agents explore it, which saturates the context, does not scale to many repositories, and yields a single artefact rather than aligned ones.   We present a...
  </details>

- **2026-10-14** — Maosheng Qin, Qi Zhang, Mingxuan Xia et al. — [Memorizing Who, Knowing How: Benchmarking Personal and Procedural Memory for Persistent Assistants](http://arxiv.org/abs/2610.20022v1)
  <details><summary>📄 Abstract</summary>
  Memory systems for persistent personal agents must move beyond isolated memories, maintaining both personal memory about whom they serve and procedural memory about how to act. Crucially, in harness-based personal assistance, procedures or skills are inherently user-conditioned: personal context determines which procedures apply, how they are instantiated, and when they should change. Existing benchmarks typically emphasize either personal or procedural memory, leaving their interaction underexp...
  </details>

- **2026-10-14** — Mario Mallea, Angela Nebot, Franscisco Mugica — [Empirical Boundaries of Reservoir Computing for Few-Shot Sequence Pattern Tasks](http://arxiv.org/abs/2610.19997v1)
  <details><summary>📄 Abstract</summary>
  Efficient sequence modeling remains a fundamental challenge in machine learning. Despite the success of Transformers, recurrent neural networks (RNNs) have recently re-emerged as efficient alternatives. Particularly, Echo State Networks (ESNs) offer a compelling framework of randomized RNNs that have been extensively studied for time-series forecasting and dynamical systems. This paper presents an empirical analysis of distributional, architectural, and optimization variants of ESNs evaluated on...
  </details>

- **2026-10-14** — Sifan Yang, Hongyi Tao, Dingzhi Yu et al. — [Memory-Efficient Subspace Optimization with Residual Correction: From Momentum SGD to Muon](http://arxiv.org/abs/2610.19844v1)
  <details><summary>📄 Abstract</summary>
  Memory-efficient subspace optimization has emerged as a practical approach to reducing the memory cost of LLM training while preserving optimization performance. Previous algorithms typically rely on the leading singular subspace of stochastic gradients, yet the gradient noise may dominate the subspace in later training stages and can prevent convergence. To overcome this limitation, we adopt a residual correction framework, which maintains the optimizer states in the subspace and adds the ortho...
  </details>

- **2026-10-14** — Soundouss Messoudi, Youness Mansar — [Calibration and Risk-Budgeted Decisions with System One Models](http://arxiv.org/abs/2610.19811v1)
  <details><summary>📄 Abstract</summary>
  LLM workflows and agents rely on a set of binary decisions like allow/block an input, or discard/retain a retrieved document. When human deferral is unavailable, uncertain cases must still receive an action. We study System One decision scores in this setting by defaulting to a conservative fallback when uncertain, and controlling the false omission risk within the subset of inputs assigned the utility-maximizing action. Across six datasets covering moderation, safety, and reranking, we compare ...
  </details>

- **2026-10-14** — Panagiotis Kasnesis, Lazaros Toumanidis, Christos Chatzigeorgiou et al. — [One Agent per Zone: Decentralised Active Inference under Partial Observability for Multi-Zone HVAC Control on Edge Hardware](http://arxiv.org/abs/2610.19790v1)
  <details><summary>📄 Abstract</summary>
  Multi-zone HVAC control is a shared-resource problem: zones on a floor share one fan and cooling coil, so each zone's demand affects its neighbours and the building's peak power. One controller per zone scales well and isolates faults, but each controller then observes only its own zone, not the shared air loop. In this work, we present a decentralised controller that assigns each zone an independent active-inference agent, which plans by minimising expected free energy and learns its zone dynam...
  </details>

- **2026-10-14** — Ziyang Ling, Shuyu Lu, Ziyi Chen — [PRISMATIC : Prescription Risk Inspection System for Multi-Agent Treatment Interaction in Clinical Decision-Making](http://arxiv.org/abs/2610.19762v1)
  <details><summary>📄 Abstract</summary>
  Medical prescribing errors for multimorbid patients, who require complex drug regimens, are a major patient safety concern. These errors often stem from fragmented decision-making across medical specialties, a critical coordination failure that leads to adverse drug events and rehospitalizations. To address this coordination challenge, we introduce PRISMATIC, a multi-agent architecture where specialized agents, each representing a workflow role, collaboratively generate and refine treatment plan...
  </details>

- **2026-10-14** — Qi Chen, Yuwei Wu, Quan Chen et al. — [One-shot Human Video-Guided Adaptation for Vision-Language-Action Models](http://arxiv.org/abs/2610.19746v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have recently achieved remarkable progress by leveraging large-scale robot datasets and foundation models for general-purpose robot manipulation. However, their ability to rapidly adapt to novel manipulation tasks beyond the training distribution remains limited. Existing approaches often require task-specific robot demonstrations and additional training, which are labor- and compute-intensive, limiting the scalability of VLA adaptation to open-world scenarios...
  </details>

- **2026-10-14** — Nir Yarden, Amit Ben-Artzy, Roy Schwartz — [Beyond State Capacity: Why Retrieval Breaks in Mamba](http://arxiv.org/abs/2610.19709v1)
  <details><summary>📄 Abstract</summary>
  Mamba models underperform Transformers on in-context retrieval. This gap is usually attributed to Mamba's fixed-size recurrent state, which loses information as the context grows. We challenge this assumption by focusing on query-first retrieval, a setup in which the query precedes the context and state capacity should not be the binding constraint. We show that even in this setting Mamba lags substantially behind Transformers, despite its selection mechanism, which was designed to distinguish r...
  </details>

- **2026-10-14** — Bolin Zhang, Xuechao Wang — [Effective-Balance Design in Ethereum Proof-of-Stake](http://arxiv.org/abs/2610.19699v1)
  <details><summary>📄 Abstract</summary>
  Proof-of-Stake (PoS) systems offer a scalable and energy-efficient alternative to Proof-of-Work (PoW). The economic security of PoS relies critically on incentivizing broad and meaningful participation through well-cali\-brated staking reward mechanisms. We study Ethe\-reum's effective-balance rules as a mechanism-design problem in which the protocol chooses a reward coefficient, an activation threshold, and a maximum effective balance, and validators respond in the induced propor\-tional-alloca...
  </details>

- **2026-10-14** — Vaishak Prasad, Prayush Kumar, Michael Boyle et al. — [A catalog of long, eccentric and precessing binary black hole simulations from ICTS-TIFR](http://arxiv.org/abs/2610.19688v1)
  <details><summary>📄 Abstract</summary>
  We present a catalogue of 31 binary black hole simulations performed with the Spectral Einstein Code (SpEC) on the Sonic cluster at ICTS-TIFR, Bengaluru between August 2023 and December 2024, targeting the sparsely covered corner of parameter space in which orbital eccentricity and spin-orbit precession are present simultaneously: 17 configurations are both eccentric and precessing, spanning mass ratios $1 \le q \le 11$ and initial eccentricities up to $\hat{e}_0 = 0.40$. The longest, EccPrecDif...
  </details>

- **2026-10-14** — Soumick Sarker, Mengmi Zhang — [Remember, Revisit, Revise: Scaffold Memory for Long-Horizon 3D Geometry](http://arxiv.org/abs/2610.19674v1)
  <details><summary>📄 Abstract</summary>
  Geometry foundation models estimate camera poses and 3D scene structure from video sequences, but maintaining consistent reconstructions over long horizons remains challenging. Feed-forward models process long sequences as independent, fixed-length frame windows and align their predictions, causing pose and reconstruction errors to accumulate across windows. Streaming models retain information from past frames to inform future predictions, but cannot revise earlier estimates when later observati...
  </details>

- **2026-10-14** — Xiaocong Yang, Xuanyu Meng, Yuji Zhang et al. — [Sparse Autoencoders Are a Shared Coordinate System for Symbolic Matching](http://arxiv.org/abs/2610.19636v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) hold broad knowledge in one set of weights, but lack interpretability and trustworthy reasoning, especially in high-stakes use cases. A neuro-symbolic model, with its interpretable architecture and System 2 reasoning capacity, is a promising alternative if built at the scale of LLMs; however, its symbolic backbone is usually constructed with human effort, so existing neuro-symbolic models are bottlenecked by the scope of the symbol component and usually domain-specif...
  </details>

- **2026-10-14** — Ziyi Liang, Zichuan Li, Bin Yuan et al. — [Mission (Im)Possible: Towards Autonomous Discovery of Autopilot Logic Flaws in Open-Source Drone Frameworks](http://arxiv.org/abs/2610.19566v1)
  <details><summary>📄 Abstract</summary>
  Autonomous drones are increasingly deployed in safety-critical tasks, yet their autopilot software can still contain subtle logic flaws that lead to unsafe behaviors. These flaws are difficult to discover with existing techniques because they often depend on semantic relationships across modules, commands, and runtime state, and rarely manifest as crashes or detectable failures. With recent advances in LLMs, we observe that, when equipped with essential domain knowledge and carefully crafted con...
  </details>

- **2026-10-14** — Yining Tang, Junyu Zhang, Haomiao Qiu et al. — [GraphRAG-LTM: A Layered Threat Modeling Framework for Attacks on Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2610.19549v1)
  <details><summary>📄 Abstract</summary>
  Graph retrieval-augmented generation (GraphRAG) uses document-derived knowledge graphs to assemble evidence for large language model (LLM) answers. Its security depends on both the seed chunks retrieved for a query and the graph evidence assembled from them, yet attacks on this evidence path remain underexplored. We introduce GraphRAG-LTM, a Layered Threat Modeling framework that tests three nested levels of attacker access. BB Query uses ranking feedback to make query edits under a semantic-sim...
  </details>

- **2026-10-14** — Shijun Li, Yang Liu, Najmeh Sadoughi et al. — [Retrieve What Helps, Only When It Helps: Agentic Reinforcement Learning for Selective Retrieval-Augmented Machine Translation](http://arxiv.org/abs/2610.19528v1)
  <details><summary>📄 Abstract</summary>
  Retrieving external knowledge can improve large language model (LLM) translation by providing supplementary information such as idiom interpretations and terminology. However, existing retrieval-augmented machine translation systems typically apply predefined retrieval strategies uniformly across all inputs. We argue that translation operates in a partial-evidence regime: LLM's parametric knowledge suffices for many inputs, while external evidence benefits a subset and usually supports rather th...
  </details>

- **2026-10-14** — Yunze Liu, Jing Wang, Shenrui Wu et al. — [Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution](http://arxiv.org/abs/2610.19495v1)
  <details><summary>📄 Abstract</summary>
  Retrieving useful context for a robot requires matching its task, execution stage, and the continuation that should follow. We introduce Robota-Embed, to our knowledge the first vision-language-action (VLA) embedding model to jointly encode all three modalities in both current-state queries and recorded future continuations. Predictive retrieval training aligns these endpoints, enabling historical continuations to serve as context at inference time. We construct a multi-source corpus of 1,695,68...
  </details>

- **2026-10-14** — Akshay Malhotra, Nicolas Zilberstein, Shahab Hamidi-Rad — [Train to Stitch: Topology-Preserving Regularization for Interoperable Representations](http://arxiv.org/abs/2610.19401v1)
  <details><summary>📄 Abstract</summary>
  As large, powerful pre-trained models become more prevalent, there is growing interest in developing methods that allow different neural networks to be seamlessly combined with little or no direct communication between them. Take autoencoder-based data compression as an example: the ability to independently choose architectures and train encoder and decoder models, while still ensuring they work together, could fundamentally transform how such models are built, deployed, and updated. In this wor...
  </details>

- **2026-10-14** — Miaobo Hu, Shuhao Hu, Xiaobo Guo et al. — [ActiveEvidence: Decision-Focused Evidence Graphs with Verifiable Acquisition Gaps](http://arxiv.org/abs/2610.20532v1)
  <details><summary>📄 Abstract</summary>
  A multimodal agent must decide whether visual evidence is worth acquiring, which candidate or resolution to query, and when further interaction can no longer change its decision. We study this problem under a strict free-metadata/paid-observation boundary, stochastic vector costs, and a frozen execution trace, and treat it as decision-certifiable active evidence acquisition. A Counterfactual Evidence Interaction Graph (CEIG) represents unary evidence value, signed second-order interaction, and d...
  </details>

- **2026-10-14** — Xiaoman Li, Zhiqiang Yang, Jiayu Hu et al. — [Graph-Reweighted Behavior Cloning with Human Interventions for Precise Robotic Manipulation](http://arxiv.org/abs/2610.20504v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon precise manipulation produces mixed-quality data for post-training vision-language-action (VLA) models: even successful demonstrations and intervention-assisted rollouts may contain detours, hesitations, failed attempts, and imperfect recoveries. The key challenge is to identify which action chunks actually advance the task, rather than uniformly cloning or discarding imperfect trajectories. We propose Graph-Reweighted Behavior Cloning (GR-BC), an offline iterative post-training fra...
  </details>

- **2026-10-14** — Pol Rodríguez Farrés, Jesus Cerquides — [Contagious Misinterpretations: Social Learning with Shared Interpretations](http://arxiv.org/abs/2610.20381v1)
  <details><summary>📄 Abstract</summary>
  When people discuss which of several hypotheses is true, they share not only their beliefs but also their interpretation of each one, that is, the distribution of signals each hypothesis is expected to produce. This interpretation is an opinion about what each hypothesis means and what evidence it predicts, and it is revised only through conversation, not by confronting it with the observed data. Standard non-Bayesian social learning captures only belief-sharing and keeps the likelihoods private...
  </details>

- **2026-10-14** — Davide Baldelli, Robyn Kozierok, Mirko Bronzi et al. — [Cross-Model In-Context Neurofeedback Reveals (Limited) Activation Control in LLMs](http://arxiv.org/abs/2610.20179v1)
  <details><summary>📄 Abstract</summary>
  Probes on activation vectors are widely used to detect misbehavior in language models, but their success relies on the assumption that models cannot control what their activations encode. Humans can learn, through neurofeedback, to control the firing of even single neurons, and recent studies investigated whether this ability extends to language models, reaching conflicting conclusions. No experimental design so far disentangles competence at the task from genuine access to one's own activations...
  </details>

- **2026-10-14** — Hanlin Liu, Zichen Zhou, Jiacheng Zhang et al. — [Refine Actions If Needed: Adaptive Action Chunk Refinement for Robot Manipulation](http://arxiv.org/abs/2610.19765v1)
  <details><summary>📄 Abstract</summary>
  Computationally lightweight manipulation policies predict executable actions with low inference latency, but prediction errors can limit task success. Iterative generative policies can achieve higher task success rates, but repeated network evaluations increase inference latency. Refining action proposals from computationally lightweight policies can combine these strengths, but the amount of refinement needed varies across states. We introduce RAIN (Refine Actions If Needed), a framework that p...
  </details>

- **2026-10-14** —  XGEN Team, Guohao Cai, Haoxuan Che et al. — [Generative World Simulation with DAO and JING](http://arxiv.org/abs/2610.19726v1)
  <details><summary>📄 Abstract</summary>
  We present a Generative World Simulation framework that couples persistent shared world state with continuous first-person audiovisual generation. The framework integrates DAO, a computable world engine, and JING, an Egocentric Interactive Experience Model, to support sustained interaction for humans and agents. DAO maintains the states of characters, objects, and spaces and their relationships, advancing the world according to interaction rules and world time while preserving the consequences o...
  </details>

- **2026-10-14** — Zixuan Wang, Jia-Ning Li, Yinzhou Tang et al. — [Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System](http://arxiv.org/abs/2610.19600v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language-action (VLA) models have shown strong performance on local robot manipulation, yet their success does not readily translate to long-horizon mobile manipulation. In our experiments, a pretrained subtask VLA achieves 80% success rate on atomic manipulation tasks but only 19% when these skills are composed into mobile manipulation. We argue that this gap stems from failures across the execution process rather than from local manipulation capability alone. To uncover these bot...
  </details>

- **2026-10-14** — Carson Eisenach, Robert Joseph George, Vincent Quenneville-Belair et al. — [L3M: A Verifiable Harness and Runtime for Self-Extending and Self-Improving Agents](http://arxiv.org/abs/2610.19591v1)
  <details><summary>📄 Abstract</summary>
  The lasting gains in AI have come from methods that absorb more computation, and language models already scale computation within a call. Useful work, though, happens across calls: over hours or days, through tools and external systems, among many agents and the humans they work for, and increasingly through code the agents write themselves. Whether that work compounds is enabled by the harness around it, and the harness faces a constraint the model does not: of the three participants in such a ...
  </details>

- **2026-10-14** — Mingyu Ouyang, Yiran Wang, Siyuan Hu et al. — [Player-1: Learning to Play from Synthetic Experience](http://arxiv.org/abs/2610.20584v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent learning pipelines often rely on large-scale demonstrations with limited coverage of dynamic game states, while scalable environments for interactive training remain difficult to obtain. We introduce Pla...
  </details>

- **2026-10-14** — Saatvik Kher, Hyungrok Do, Judy Zhong et al. — [Bayesian Learning to Select Fair Classifiers](http://arxiv.org/abs/2610.20514v1)
  <details><summary>📄 Abstract</summary>
  Evaluations of classifiers (AI or human or agents) often assume a batch setting in which every agent produces labels on every example in a test set, which can be expensive or impractical in many contexts. This motivates online policies that adaptively select agents to query as examples arrive and update policies as outcomes are observed. We study the problem of selecting, in an online stream, the agent that best balances (i) predictive performance and (ii) subgroup fairness of a sensitive attrib...
  </details>

- **2026-10-14** — Harsh Kumar — [Lost in Translation: Why Lower Bias Scores Don't Mean Fairer Models](http://arxiv.org/abs/2610.20479v1)
  <details><summary>📄 Abstract</summary>
  Bias audits of multilingual language models usually compare a model's average stereotype score in English with its average in another language and read the difference as a difference in fairness. We ask how much of that difference is noise. Auditing ten open models in eight languages, we measure how far scores move when English test items are merely reworded, test every language shift item by item, and check that the test catches shifts we inject on purpose. In all 70 model-language pairs the st...
  </details>

- **2026-10-14** — Peidong Wang, Ying Chang, Zhiming Ma et al. — [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](http://arxiv.org/abs/2610.20474v1)
  <details><summary>📄 Abstract</summary>
  Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without asking whether a failure lies in how the executor is called or in what it can do. We ask when a self-improving embodied system should change the weights of its executor, and propose Ad...
  </details>

- **2026-10-14** — Fazle Mohammed Tasfiq, Sabab Attin, Sheikh Md. Tahmid Hossain et al. — [Analyzing performance of Retrieval Augmented Generation models for Question Answering Tasks](http://arxiv.org/abs/2610.20419v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) models have become almost a cornerstone of open-domain question answering tasks; in which the quality of answers generated in the process, greatly relies on the effectiveness of retrieval mechanisms. In the realm of LLM, the last two years have seen tremendous progress in RAG architectures, with many models reporting to have improved performance through various design innovations. The cultural question and answering systems of South Asia, in particular, prese...
  </details>

- **2026-10-14** — Kaifei Wang, Zikang Shan, Liwei Wang et al. — [When Does Momentum Help in Reinforcement Learning with Verifiable Rewards?](http://arxiv.org/abs/2610.20413v1)
  <details><summary>📄 Abstract</summary>
  Momentum is a classical tool for accelerating convex optimization and a standard component of modern large language model training. Yet recent empirical work has questioned the usefulness of first-moment momentum in reinforcement learning with verifiable rewards (RLVR). We study this question through a bandit formulation of RLVR with bias-corrected exponential moving average (EMA) momentum, where the EMA coefficient $β$ controls how quickly the weights on past gradients decay. When policy gradie...
  </details>

- **2026-10-14** — Andrea Abrardo, Andrea Garulli — [To Stack or Not to Stack? Jacobian Conditioning and the Benefits of Depth in Metasurface-Based Linear Transformation Synthesis](http://arxiv.org/abs/2610.20377v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates when and why stacking programmable metasurfaces into Stacked Intelligent Metasurfaces (SIMs) improves linear transformation synthesis at a fixed phase-control budget. The analysis shows that algebraic Jacobian rank alone is insufficient to characterize practical synthesis, which also depends on the strength and balance of the sensitivity directions generated by the available controls. A layer-resolved analysis of the cascade model explains how inter-layer propagation can ...
  </details>

- **2026-10-14** — Yaomengxi Han, Debarghya Ghoshdastidar — [Training Dynamics of Transformers on Unbounded Inputs: Attention Learning Can Lag Output Layer Learning](http://arxiv.org/abs/2610.20337v1)
  <details><summary>📄 Abstract</summary>
  The success of transformers is attributed to several factors, including their capacity to express formal languages over variable-length inputs, and ability of the attention mechanism to focus on relevant input features. However, there is limited understanding of the training dynamics of shallow transformers, specifically how to decouple the learning of the attention and the output (feedforward) layer. A natural extension of the theory of one-step gradient feature learning in feedforward networks...
  </details>

- **2026-10-14** — Junyi Zou, Avrova Donz — [MMLA-RSI: Recursive Self-Improvement through RTT and RTMA](http://arxiv.org/abs/2610.20294v1)
  <details><summary>📄 Abstract</summary>
  An agent can improve its behavior within an unresolved problem by changing how it acts and which experience it retains. We propose MMLA-RSI, a recursive self-improvement scheme with two implementations in Memory-Mediated Learning Architecture: Reasoning-Time Training (RTT) changes the policy state $Φ$, while Reasoning-Time Memory Adaptation (RTMA) changes authoritative memory $M$. Each route also makes its adaptation method an object of improvement. A current numerical updater trains the policy ...
  </details>

- **2026-10-14** — Steffen Holter, Rita Sevastjanova, Michaela Benk et al. — [Let Me Clarify: Interactive Modeling of Soft Attributes](http://arxiv.org/abs/2610.20227v1)
  <details><summary>📄 Abstract</summary>
  People commonly express preferences through soft attributes such as is interesting,'' which are difficult to operationalize for computational preference modeling. Latent representations can obscure how such attributes are interpreted, limiting transparency and user control. We formalize softness as the diversity of valid interpretations a description permits and provide empirical support for this characterization. Our proposed measure estimates softness to guide clarification and determine when ...
  </details>

- **2026-10-14** — Isabel Jones, Matthew Edwards, Janina A. Hoffmann — [Drivers of LLM Consensus Formation Under Competing Incentives: A Simulation Study](http://arxiv.org/abs/2610.20200v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed in multi-agent environments that produce unanimous agreement, both in intended interactions that need coordination and in unintended emergent interactions. Consequently, understanding how LLMs with competing incentives reach consensus is crucial to better interpret and design LLM collectives. We introduce an evaluation, based on the Network Consensus game, to assess the mechanisms driving this process. Here, a network of agents must agree on...
  </details>

- **2026-10-14** — Xinxuan Lv, Minghan Li, Guodong Zhou — [XViewRank: Overlap-Conditioned Score Fusion for LLM-Augmented Sparse Retrieval](http://arxiv.org/abs/2610.20122v1)
  <details><summary>📄 Abstract</summary>
  Large language models can reduce vocabulary mismatch in sparse retrieval by generating alternative views of a query. Once these views are searched independently, however, their ranked lists may be complementary, redundant, or affected by query drift, making fixed fusion suboptimal. We present XViewRank, a lightweight retrieval-side method for conditionally fusing BM25 results from an original query, a hypothesis view, and a step-back view. For each pooled candidate, XViewRank retains three norma...
  </details>

- **2026-10-14** — Mengke Zhang, Yanda Shao, Tianhe Wu et al. — [ACR-Net: Mitigating Semantic Dominance via Contrastive Acoustic-Semantic Decoupling](http://arxiv.org/abs/2610.20114v1)
  <details><summary>📄 Abstract</summary>
  Speech Emotion Recognition (SER) models and Audio LLMs fail when vocal tone contradicts textual semantics. Extensive training on congruent data engenders a rigid semantic prior, causing "Semantic Dominance", a severe text bias during cross-modal conflicts. We introduce the ASPIRE benchmark of adversarial audio-text pairs across four conflict types, alongside two metrics: Semantic Overconfidence Penalty (SOP) and Latent Decoupling Degree (LDD). Unlike fusion methods that merely re-weight collapse...
  </details>

- **2026-10-14** — Yunhao Wang, Feng Zhang, Tinghao Yu et al. — [AFCS: Atomic-Fact-Conditioned Synthesis for Factual Knowledge Pretraining](http://arxiv.org/abs/2610.20086v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data is increasingly used in language-model pretraining. Existing knowledge-corpus synthesis pipelines, including WRAP and Nemotron-CC, usually take a source passage or document segment as input and generate rewritten or QA-style samples from that text. This can improve surface form and prompt diversity, but it does not explicitly require fine-grained source facts -- especially secondary entities, list/table entries, and precise temporal attributes -- to appear in the synthesized corpu...
  </details>

- **2026-10-14** — Yi Wang, Tianzi Wang, Tong Lei et al. — [Designing Textual Interfaces To Enhance Llm Reasoning On Audio-Visual Question Answering](http://arxiv.org/abs/2610.20085v1)
  <details><summary>📄 Abstract</summary>
  Automatic prompt optimization (APO) has shown strong effectiveness for text-based LLMs and LLM systems, but its application to audio-visual understanding systems requires suitable textual interfaces through which multimodal reasoning can be exposed to text-based optimizers. We investigate how the design of textual interfaces affects prompt optimization for multimodal reasoning, on the audio-visual question answering task. We compare three interface designs, including a direct inference system co...
  </details>

- **2026-10-14** — Lakshmi Rajendram Bashyam, Ralf Krestel — [Reading the Neighborhood: Text-Attentive Graph Reranking for Automated Subject Indexing](http://arxiv.org/abs/2610.20048v1)
  <details><summary>📄 Abstract</summary>
  Subject indexing assigns descriptors from a controlled vocabulary to bibliographic records, a task characterized by thousands of labels, few positive examples per label, and a long tail of rarely used descriptors. Existing extreme multi-label classifiers treat the vocabulary as a flat list, ignoring the semantic relations that thesauri encode. We present TAGHN, a heterogeneous graph reranker over a per-document subgraph of retrieved candidates augmented with the thesaurus neighborhood. The relev...
  </details>

- **2026-10-14** — Timo Klein, Thomas Lang, Andrii Shkabrii et al. — [Outperforming 1000 Euclidean Layers With Hyperbolic Goal-Conditioned RL](http://arxiv.org/abs/2610.20009v1)
  <details><summary>📄 Abstract</summary>
  Scaling self-supervised contrastive reinforcement learning (CRL) to 1000-layer Euclidean neural networks has enabled state-of-the-art goal-reaching performance, yet wall-clock time scales linearly with depth. We find that changing the geometry achieves stronger performance with far shallower networks. This matters in complex navigation environments, where walls can make route distance deviate substantially from Euclidean distance. In a U-shaped maze, we show that the longer the route, the more i...
  </details>

- **2026-10-14** — Jithin Cheriyan, Bastin Tony Roy Savarimuthu, Stephen Cranefield — [Taming the Online Software Engineering Tongue: Detecting and Reducing Offensive Language in Software Communities](http://arxiv.org/abs/2610.19961v1)
  <details><summary>📄 Abstract</summary>
  Online Software Engineering (SE) communities such as Stack Overflow have become unwelcoming and hostile spaces, as evidenced by the presence of rude and offensive comments that are detrimental to the emotional wellbeing of participants. The main objective of this work is to investigate the prevalence and nature of offensive language in online SE communities, and develop approaches to classify them with the ultimate goal of reducing offensive language by proposing an Offensive Language Reduction ...
  </details>

- **2026-10-14** — Anton Korznikov, Alexey Dontsov, Elena Tutubalina — [Sparse Transformer: a Controlled Testbed for Mechanistic Interpretability](http://arxiv.org/abs/2610.19907v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability aims to decompose neural network computations into human-understandable features, yet progress is limited by the absence of ground-truth units to evaluate against. We address this with a Sparse Transformer (ST): a 5-layer language model trained on TinyStories whose wide, TopK-sparse MLP forces neuron specialization. We show that ST neurons are highly interpretable: they outperform a loss-matched dense transformer by 43% on AutoInterp, and circuits of a median of 12 n...
  </details>

- **2026-10-14** — Fiorenzo Parascandolo, Enver Sangineto, Xiaoyi Yu et al. — [Frustratingly Easy Majority Voting Using Length Conditioning](http://arxiv.org/abs/2610.19890v1)
  <details><summary>📄 Abstract</summary>
  Majority Voting (MV) is a simple and widely used strategy which improves the reasoning accuracy of Large Language Models (LLMs) by allocating additional inference-time computation. Specifically, in MV multiple Chain-of-Thoughts (CoTs) are independently sampled and the most frequent final answer is selected. In this work, we propose Length-Conditioned Majority Voting (LCMV), a Test-Time Training approach which improves MV leveraging an empirical observation that has recently been established in s...
  </details>

- **2026-10-14** — Robin Uhrich, Marco Bagatella, Núria Armengol Urpí et al. — [Occupancy Modeling via Drifting: One-Step Generation Enables Direct Policy Extraction](http://arxiv.org/abs/2610.19883v1)
  <details><summary>📄 Abstract</summary>
  The growing interest in behavior foundation models, combined with recent advancements in generative modeling, has led to an appealing recipe for reinforcement learning from unlabeled data: pre-train a generative model to model occupancies, i.e., discounted state visitations, on reward-free trajectories, such that a policy can be easily extracted once a small reward-labeled dataset becomes available. We decompose this recipe along three axes: (i) the degree to which the multi-modal structure of o...
  </details>

- **2026-10-14** — Shanyan Guan, Shiyu Li, Xin Li et al. — [BluePixel: Toward Native 4K Agentic Image Editing](http://arxiv.org/abs/2610.19882v1)
  <details><summary>📄 Abstract</summary>
  Instruction-driven image editing has reached native 4K, yet how such editors are trained remains undisclosed, and pretraining one from scratch is beyond most teams. The task itself compounds the difficulty: a single end-to-end editor cannot make precise parametric adjustments, match specialized experts, or interpret the vague instructions users actually write. We argue that 4K editing is a system problem rather than a single-model problem, and present BluePixel, which couples a native-4K editing...
  </details>

- **2026-10-14** — Giacomo Aletti, Enea G. Bongiorno — [Principal Component Analysis for Zero-Inflated Probability Measures via Lorenz Curves](http://arxiv.org/abs/2610.19874v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a principal component analysis framework for probability measures associated with non-negative real-valued random variables with structural zeros. Specifically, leveraging the associated Lorenz Curve (LC) and a suitable perspective transformation of the plane, a bijective embedding is defined to treat such measures as functional data in a Hilbert space. Once the random LC is embedded in this space, standard Functional Principal Component Analysis (FPCA) becomes directly appli...
  </details>

- **2026-10-14** — Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang et al. — [OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](http://arxiv.org/abs/2610.19848v1)
  <details><summary>📄 Abstract</summary>
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as open data by the Ministry of Examination; answer keys agree across 31,312 duplicated question groups at 99.91%, with all 27 disagreements accounted for. A reviewed second pass withdrew 2,180 items whose stems depend on ...
  </details>

- **2026-10-14** — Linhao Zhong, Bozhen Fang, Xuehao Wang et al. — [More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning](http://arxiv.org/abs/2610.19789v1)
  <details><summary>📄 Abstract</summary>
  Self-distillation in agentic reinforcement learning has produced a growing number of methods. However, existing evaluations often reuse published baseline scores under differing experimental conditions, provide few direct comparisons among contemporaneous methods, and give limited attention to training stability and computational cost. These limitations obscure the source of reported gains and the practical strengths and weaknesses of competing methods. Costly agent training further motivates a ...
  </details>

- **2026-10-14** — Yuming Zhao, Zezeng Li, Weimin Wang et al. — [Q-MAGIC: Quad-only Mesh Autoregressive Generation via Singularity-Aware Circular Relative Offset Tokenization](http://arxiv.org/abs/2610.19777v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive models have proven effective for triangular mesh generation by transforming it into predicting the next face, converting the non-differentiable connectivity prediction into a sequence of token predictions. However, generating quad-only meshes remains challenging because quad faces impose stricter topological constraints than triangles. The model must not only serialize quad faces into a valid token sequence, but also support unambiguous connectivity reconstruction during de-serial...
  </details>

- **2026-10-14** — Minghan Li, Guodong Zhou — [Does the Linguistic Register of Thinking Matter? Wenyan as a Compact Reasoning Register for Chinese LLMs](http://arxiv.org/abs/2610.19741v1)
  <details><summary>📄 Abstract</summary>
  Visible reasoning traces of Chinese reasoning-oriented LLMs are typically written in modern vernacular Chinese, which may be verbose under limited decoding budgets. We ask whether the linguistic register of reasoning can be used to improve efficiency. We propose Wenyan Thinking, which emits intermediate reasoning in Classical Chinese (wenyanwen) while retaining a short direct-answer output. Starting from modern-Chinese reasoning traces, we rewrite only the reasoning field into wenyan and fine-tu...
  </details>

- **2026-10-14** — Shun Inadumi, Lee Sangmyeong, Koichiro Yoshino — [Recognizing Dialogue Ambiguity via Candidate Set Visual Grounding](http://arxiv.org/abs/2610.19723v1)
  <details><summary>📄 Abstract</summary>
  Interpreting an ambiguous utterance in real-world interactions often requires context beyond a single utterance. When the utterance refers to objects in a visual scene, it is necessary to maintain and update the set of plausible referents as context accumulates, without assuming that the available information identifies a unique object. However, prior work on interactive visual grounding, which localizes objects referred to by linguistic expressions, has focused on identifying a unique object on...
  </details>

- **2026-10-14** — Xin Li, Mengbing Liu, Hao Jiang et al. — [Share the Symbol, Not the Vector: Training-Free Fact Communication Across Language Models](http://arxiv.org/abs/2610.19696v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems allow language models to solve tasks collaboratively by sharing complementary information. These systems typically communicate through text, while recent approaches also explore exchanging internal model states. However, sharing these states across architectures often requires learned translators or assumptions about model compatibility. We introduce SYNC (Symbol-Indexed Neural Communication), a word-indexed interface that connects heterogeneous models without fine-tuning or ...
  </details>

- **2026-10-14** — Yilin Jiang, Fei Tan, Xuanyu Yin et al. — [Measuring and Reducing Unusable Replies of LLM Agents](http://arxiv.org/abs/2610.19659v1)
  <details><summary>📄 Abstract</summary>
  People delegate multi-step work to LLM agents and read only the reply that the agent hands back. Current evaluation scores task completion and the faithfulness of reports, and it leaves open whether the requester can understand and use the reply. We call this property reply usability and measure it with a reader model that takes the requester's position and tests whether the reply can be interpreted from what the requester has seen, is in the requester's language and answers the request. Its agr...
  </details>

- **2026-10-14** — Yiliu Xu, Xinjin Li, Yu Ma — [What Breaks in Multi-Image Schema Application? Factorial Oracle Interventions Reveal an Instance-Information Bottleneck](http://arxiv.org/abs/2610.19611v1)
  <details><summary>📄 Abstract</summary>
  Modern vision-language models can accept multi-image contexts, but aggregate accuracy rarely reveals where a multi-image reasoning pipeline fails. We study a controlled schema-application task in which a model must locate two target characters in a 16-image sequence, identify their visual attributes, consult an item-specific visual codebook, and compose two ordered nonce code names. We introduce a within-item 2-by-2 factorial Oracle design: Oracle-A supplies a verified textual schema, Oracle-B s...
  </details>

- **2026-10-14** — Xinjie Lan, Yunbo Mei, Leheng Zhou et al. — [Beyond Static Positional Encoding: Bayesian Time-aware Attention for Non-Stationary Long-term Time Series Forecasting](http://arxiv.org/abs/2610.19603v1)
  <details><summary>📄 Abstract</summary>
  Transformers have demonstrated strong performance in long-term time series forecasting (LTSF), yet modeling non-stationary temporal dependencies remains challenging. In this paper, we interpret self-attention as a Bayesian posterior over attended positions, combining a content-based prior induced by scaled dot-product similarity with a temporal-evidence likelihood induced by positional encoding. This formulation provides a probabilistic interpretation of how positional encoding shapes the tempor...
  </details>

- **2026-10-14** — Zhongwei Xie, Xingsu Li, Jingqiao Yu et al. — [JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making](http://arxiv.org/abs/2610.19589v1)
  <details><summary>📄 Abstract</summary>
  Repeated event forecasting requires extracting predictive signals from noisy evidence and evaluating their value across successive decisions. We introduce JockeyBench, a benchmark and evaluation protocol that studies this problem through historical Japanese horse racing. The protocol combines time-gated evidence, priced tools, paired frozen-program controls, and two workflows: executing an LLM-written predictor or acquiring evidence for a fresh per-race LLM forecast. Evaluation separates forecas...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 681 |
| prompt-injection | 621 |
| memory-poisoning | 55 |
| tool-use-attack | 157 |
| backdoor | 525 |
| adversarial-attack | 638 |
| privacy-leakage | 4392 |
| steganography | 79 |
| misuse | 1189 |
| red-teaming | 143 |
| vulnerability | 3616 |
| defense | 3493 |
| alignment | 3268 |
| robustness | 3540 |
| watermark | 619 |
| unlearning | 116 |
| agent-safety | 64 |
| benchmark | 68 |
| survey | 404 |
| other | 9550 |

---

📚 **全部 33218 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-19 11:52:18*