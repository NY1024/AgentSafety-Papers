<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-33540-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-21 03:41 ｜ **论文总数 / Total Papers**: 33540（近 30 天 / Recent 30 days: 5041）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 33540 篇论文（含摘要、分类筛选、搜索）/ View all 33540 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 687
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 626
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 55
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 157
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 528
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 639
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4408
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 80
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1202
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 143
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3649
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3526
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3308
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3586
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 629
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 116
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 65
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 69
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 408
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 9659

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 5041 篇，完整 33540 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 5041 papers from the last 30 days (with date, authors & abstract). For the full list of 33540 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 7 papers

- **2026-10-19** — Leon Tu Nguyen, Rohan Menon, Rafael Tappe Maestro et al. — [Concerns in Benchmarking Jailbreaks: An Empirical Study of Attack Success Rates](http://arxiv.org/abs/2610.26595v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak methods are commonly compared using Attack Success Rate (ASR), but these comparisons depend on how responses are generated and judged. In this paper, we examine eight attacks against three open-weight language models using three evaluation procedures. Low-resource language attacks achieve a mean ASR of 96.0% under keyword matching but 2.7% under a Qwen3 evaluator following StrongREJECT scoring instructions. Changing the number and arrangement of attempts reverses the ranking of DeepInc...
  </details>

- **2026-10-19** — Rohan Menon, Chih-Hong Cheng — [Beyond Attack Success Rate: Cost-Aware Metric for Evaluating Iterative LLM Jailbreaks](http://arxiv.org/abs/2610.26589v1)
  <details><summary>📄 Abstract</summary>
  Attack success rate (ASR) evaluates jailbreaks against large language models without accounting for repeated calls to the victim model. Yet each additional call gives the deployed system another opportunity to detect the attack and intervene. We introduce $\mathrm{ASR}_{\mathrm{STEP}}$, which penalizes additional victim-model calls while retaining binary success judgments. Our evaluation considers GCG~\cite{zou2023universal}, PAIR~\cite{chao2025jailbreaking} with a step budget, and a single-step...
  </details>

- **2026-10-19** — Anastasiia Kucherenko, Francois Brouchoud, Dimitri Percia David et al. — [LLMs Prompted for Legal Context Refuse More: Overrefusal from Small On-Premises LLMs in Criminal Legal Context](http://arxiv.org/abs/2610.26211v1)
  <details><summary>📄 Abstract</summary>
  Confidentiality requirements increasingly push legal professionals toward small, on-device LLMs that keep case data in-house, used for everyday tasks such as summarization, translation, and reformulation. Following standard prompting guidance, a user naturally states their role (``I am a lawyer...''). We show that this innocuous habit has an unexpected cost: such authority framing can make the model selectively refuse legitimate requests, introducing bias through uneven access to assistance. We ...
  </details>

- **2026-10-19** — Zhicheng Fang, Han Sun, Jiachen Lei et al. — [Budgeted Attack Scheduling for LLM Red-Teaming: The Roles of Static Priors, Semantic Guidance, and Online Feedback](http://arxiv.org/abs/2610.25897v1)
  <details><summary>📄 Abstract</summary>
  As jailbreak attacks against large language models (LLMs) become increasingly diverse, red-teaming has come to rely on large libraries of jailbreak prompts and attack strategies to evaluate the robustness of victim models and their defense settings. However, attack effectiveness is highly condition-dependent: an attack that succeeds under one victim-defense setting may fail under another, while exhaustively evaluating the full attack library for each setting incurs substantial token and monetary...
  </details>

- **2026-10-17** — Khushbu Pahwa, Yubin Ge, Daniele Bonadiman et al. — [Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security](http://arxiv.org/abs/2610.24896v1)
  <details><summary>📄 Abstract</summary>
  LLM code agents increasingly ship code with little oversight, yet defenders trained on static vulnerability datasets fall behind adapting adversaries. We co-train attacker and defender instead, and let execution decide every reward: an attacker (Red) edits a real repository and earns nothing unless its patch applies, builds, passes the tests, completes its development task and reproduces a real exploit in an isolated container, whose path also labels the entry point, the critical operation and t...
  </details>

- **2026-10-17** — Juanyang Xu, Zheng Wang, Xingyu Zhao et al. — [Pair-Aware Optimization: Coordinating Exploration and Refinement for Jailbreaking LLM Agents](http://arxiv.org/abs/2610.24823v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents are vulnerable to adversarial inputs that induce attacker-specified malicious behaviors, commonly referred to as jailbreaking. Existing optimization-based jailbreak attacks primarily employ first-order (FO) methods that leverage gradient information or zeroth-order (ZO) methods that rely on function-value feedback. However, their complementarity and optimization ordering remain underexplored. We systematically investigate four strategies: pure ZO, pure FO, ZO->F...
  </details>

- **2026-10-16** — Junchi Liao — [Monitor-Validity Failures: LLM Safety Evidence Paths at Evolving Framework Boundaries](http://arxiv.org/abs/2610.23362v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM applications rely on runtime monitors that inspect tool calls, traces, streams, detector outputs, and verifier inputs. This creates an interface-reliability problem: a framework path may remain operational while policy-relevant evidence never reaches its decision point. In one representative case, a regex detector returned a positive match, but the framework stranded the result before the block decision. This differs from jailbreaks and detector errors because the evidence is already ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 5 papers

- **2026-10-19** — Mengxiao Wang, Nitesh Saxena — [Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents](http://arxiv.org/abs/2610.26438v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents now trade real capital using news as evidence, yet they cannot reliably tell fabricated headlines from real news. Because they read the same feeds under near-identical policies, a single fabricated post can push them into the same trade at the same moment. We present a systematic attack benchmark for information injection against LLM trading agents. Unlike prompt injection, which targets the model's instructions, information injection targets the evidence the ag...
  </details>

- **2026-10-19** — Yinxiang Wang, Zehua Ma, Kejiang Chen et al. — [SpanGuard: Decoupling Instruction Localization from Authorization for Lightweight IPI Defense](http://arxiv.org/abs/2610.26013v1)
  <details><summary>📄 Abstract</summary>
  LLM-based guardrails are effective against indirect prompt injection (IPI), but their performance depends heavily on model capability: as the guardrail model becomes smaller or weaker, detection degrades substantially. This raises a natural question: can we retain strong IPI defense while relying only on a small LLM? To understand why, we revisit what an LLM guardrail actually does. Detecting IPI requires simultaneously locating potentially injected instructions within heterogeneous tool outputs...
  </details>

- **2026-10-19** — Yuchen Chen, Wei Cheng, Yuan Xiao et al. — [RAGLeak: Supply-Chain Privacy Backdoors in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.25937v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) enables large language models to access external knowledge during inference, but its reliance on external knowledge bases also introduces new attack surfaces. Existing data extraction attacks against RAG systems rely on either prompt injection, which heavily depends on the generator's instruction-following capability, or backdoors that reproduce or paraphrase retrieved documents but struggle to balance extraction fidelity and stealthiness. In this paper, we p...
  </details>

- **2026-10-18** — Stavros Damianakis, Konstantinos Psounis — [SoK: PIAtlas: Decomposing the Unbounded Prompt Injection Attack Space](http://arxiv.org/abs/2610.24999v1)
  <details><summary>📄 Abstract</summary>
  Prompt injection is the dominant security risk for large-language-model (LLM) applications and agents, yet the field still lacks a coherent map of how these attacks are constructed. More than twenty public datasets describe prompt injection using incompatible vocabularies, often organized around delivery vector, attacker goal, or generation method. In this Systematization of Knowledge, we present PIAtlas, a taxonomy organized instead around how the injected instruction is constructed to subvert ...
  </details>

- **2026-10-17** — Mahdieh Abazar, Lorenzo De Carli, Benjamin Tan — [CAT-RAG: Improving Secure Code Generation with Category-Aware Agentic Retrieval](http://arxiv.org/abs/2610.24907v1)
  <details><summary>📄 Abstract</summary>
  Despite rapid progress in LLM-based code generation, security vulnerabilities remain widespread, and retrieval-augmented code generation (RACG) can further amplify risk when retrieved knowledge is verbose or vulnerable to poisoning. Existing secure RACG approaches inject security knowledge at a fine-grained vulnerability level, causing prompt overhead and diluted model attention when a query implicates multiple related weaknesses. We propose CAT-RAG, an agentic security category-aware retrieval-...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-10-15** — Ali Mohammadi Shanghooshabad — [FAOPs: Normal Forms and an Algebra for AI Agent Workflows](http://arxiv.org/abs/2610.22061v1)
  <details><summary>📄 Abstract</summary>
  Organizations increasingly encode operational procedures as multi-step agent skills, here called Agent Operating Procedures (AOPs), that must be traceable, auditable, reproducible, access-controlled, and bounded in time and cost, requirements that regulated sectors make mandatory. Yet AOPs are typically kept as coarse-grained files, in which steps bundle actions, copied procedures drift apart, any step may reach any tool, and refactoring goes unchecked. We present Functional Agent Operating Proc...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 12 papers

- **2026-10-19** — Jonibek Mansurov, Sholpan Bolatzhanova, Filbert Aurelian Tjiaranta et al. — [Selective Transfer through Sequence Distillation: From Benchmark Knowledge to Backdoor Behaviour](http://arxiv.org/abs/2610.26311v1)
  <details><summary>📄 Abstract</summary>
  Knowledge distillation is widely used to transfer capabilities from teacher models to student models, but recent work shows that it can also transfer unintended teacher properties. We study whether different hidden teacher properties survive the same distillation channels. Specifically, we compare two properties: benchmark-associated knowledge and refusal backdoors, and show that distillation treats them very differently. Teachers fine-tuned on benchmark data successfully pass that knowledge to ...
  </details>

- **2026-10-18** — Nanjun Zhou, Yiming Li, Yukun Chen et al. — [SEAL: Towards Persistent Tool Poisoning Attack against LLM Agents via Prefix-Eliciting Trigger](http://arxiv.org/abs/2610.25372v1)
  <details><summary>📄 Abstract</summary>
  Tool poisoning has emerged as a critical security threat to LLM agents, where adversaries embed malicious instructions in tool descriptions or external resources that enter the agent's context, allowing adversaries to manipulate agent's tool selection process. However, existing tool poisoning attacks primarily rely on an idealized assumption that the attacks task effect within a single interaction round. We show that their effectiveness degrades sharply in realistic multi-round agentic settings....
  </details>

- **2026-10-17** — Zhengxing Li, Guangmingmei Yang, Nader Alfares et al. — [LLM Trojans that Increase Response Lengths and Cost](http://arxiv.org/abs/2610.24784v1)
  <details><summary>📄 Abstract</summary>
  Management of the token-based costs of using LLMs has emerged as a significant problem. Some frontier-model providers charge five times per response token than per prompt token, while others offer prefilling discounts for prompt tokens. In this paper, we devise a defense against a new data-poisoning attack that plants a Trojan which increases the length of the response (and hence the cost to the user) when its trigger is present in the prompt. In particular, we demonstrate how a subtle Trojan ma...
  </details>

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


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-10-19** — Manohar Kaul, Sadbhavana Babar, Aditya Ramesh et al. — [Provable Adversarial Detection: Prime Quantization meets Gromov--Wasserstein](http://arxiv.org/abs/2610.26102v1)
  <details><summary>📄 Abstract</summary>
  Adversarial vulnerability persists across modern vision architectures from CNNs to vision language models (VLMs), yet existing detection methods rely on heuristics without theoretical guarantees. We address the fundamental question of when adversarial perturbations can be provably detected from a geometric perspective. Our key insight is that adversarial perturbations cannot simultaneously preserve geometric structure across spaces with fundamentally different properties. Accordingly, we constru...
  </details>

- **2026-10-16** — Wenda Li, Tongya Zheng, Shunyu Liu et al. — [S-GAP: Stealthy Graph Attack Primitives for Graph Large Language Models](http://arxiv.org/abs/2610.23465v1)
  <details><summary>📄 Abstract</summary>
  Graph Large Language Models (GraphLLMs) enable powerful semantic understanding and reasoning over Text-Attributed Graphs (TAGs), while their semantic reasoning may exhibit vulnerabilities to perturbations in node text and graph structure under adversarial attack evaluation. Existing attacks typically construct textual and structural perturbations in separate stages guided by distinct realization intents. However, this separation results in attack-intent fragmentation, causing semantic incoherenc...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 28 papers

- **2026-10-19** — Marla Grunewald, Fin Gentzen, Iulisloi Zacarias et al. — [Agentic Orchestration of EDC Data Space Retrieval and Natural Language Driven Data Processing](http://arxiv.org/abs/2610.26548v1)
  <details><summary>📄 Abstract</summary>
  Participating in a data space still requires the Dataspace Protocol (DSP) negotiation flow to be hand-coded against each provider's access policy. We present a multi-agent architecture that automates this process using natural language requests. Built on LangGraph over an Eclipse Dataspace Components (EDC), the design separates concerns into cooperating agents. The orchestrator's role is to route and plan. The data extraction agent's role is to expose the DSP protocol's three composable tools (c...
  </details>

- **2026-10-19** — Xiaoyuan Bao, Jingsi Jiang, Jiao Shan et al. — [LeakBench: Auditing Reward Hacking through Prediction-Time Leakage in Clinical Modeling Agents](http://arxiv.org/abs/2610.26088v1)
  <details><summary>📄 Abstract</summary>
  Autonomous clinical-modeling agents can optimize predictive performance while violating conditions that make a model usable. We introduce LeakBench, an executable, guideline-derived audit suite that tests agent decisions for prediction-time leakage, calibration, site-level evaluation, support awareness, and decision-curve net benefit. LeakBench combines a synthetic task with known failure structure and two real-data settings: MIMIC-IV (430k admissions) and governed multi-hospital inpatient recor...
  </details>

- **2026-10-19** — Hengsong Liu, Liangyu Teng, Jingnan Cai et al. — [Does Unlearning Survive Collaboration? Robust Unlearning for Shared-Model LLM Teams](http://arxiv.org/abs/2610.25731v1)
  <details><summary>📄 Abstract</summary>
  LLM unlearning is essential for removing sensitive or unwanted knowledge while preserving useful capabilities. As LLM teams are increasingly used to solve complex problems, forgetting must remain effective during collaboration. Despite advances in forgetting effectiveness, efficiency, and robustness to relearning, team deployment remains underexplored. We find that collaboration weakens forgetting: final-answer evaluations miss recoverable evidence in team messages, including complementary clues...
  </details>

- **2026-10-19** — Qihan Huang, Lingxia Zhang, Guye Zhang et al. — [PFedQFT: Personalized Federated Quantum-Inspired Fine-Tuning for Medical Large Language Models](http://arxiv.org/abs/2610.25712v1)
  <details><summary>📄 Abstract</summary>
  Medical data remain fragmented across institutional silos because of privacy, governance, and ownership constraints. Federated learning enables medical institutions to adapt large language models (LLMs) collaboratively without transferring raw records. However, independently parameterized low-rank adapters incur repeated parameter and communication costs across Transformer projections, while uniform aggregation may limit adaptation to heterogeneous institutional data. We propose PFedQFT, a quant...
  </details>

- **2026-10-18** — Edith Cohen, Uri Stemmer — [No Escape from the Quadratic Barrier: Adaptive Attacks on Linear $\ell_2$ Sketches](http://arxiv.org/abs/2610.25008v1)
  <details><summary>📄 Abstract</summary>
  Linear sketches estimate properties of high-dimensional inputs from a fixed low-dimensional projection. At constant accuracy, randomized Euclidean-norm sketches, notably the Johnson-Lindenstrauss transform, support exponentially many nonadaptive queries in sketch dimension $k$. For adaptive black-box queries, known privacy-based defenses guarantee $\widetildeΩ(k^2)$ and it remained open whether stronger guarantees were possible. Prior attacks used more queries, restricted the responder, or provi...
  </details>

- **2026-10-18** — Rolf Drechsler, Christina Plump — [Formal Raising: Embedding Verifiable Ethical Properties into the Development of AI](http://arxiv.org/abs/2610.25501v1)
  <details><summary>📄 Abstract</summary>
  Alan Turing proposed constructing a ``child machine'' and educating it rather than directly programming an adult-like intelligent machine. Recent work on model raising revives this developmental view for Large Language Models by arguing that moral values should accompany capability acquisition from the beginning rather than be added only through post-hoc alignment. This paper proposes Formal Raising (FR): selected moral values are represented as explicit, machine-checkable properties that partic...
  </details>

- **2026-10-18** — Duc-Huy Nguyen, Bui Duc Manh, Chi-Hieu Nguyen et al. — [PRICE: Privacy-Preserving Image Classification in Mobile Edge-Cloud Computing with Homomorphic Encryption](http://arxiv.org/abs/2610.25286v1)
  <details><summary>📄 Abstract</summary>
  Cloud-assisted image classification enables many mobile AI applications, but transmitting raw images to the cloud raises significant privacy concerns. Homomorphic encryption (HE) allows computation over encrypted data; however, existing end-to-end HE-based inference pipelines incur prohibitive latency and computational overhead, limiting their feasibility for latency-sensitive mobile systems. This paper addresses how to enable efficient encrypted image classification in mobile edge-cloud environ...
  </details>

- **2026-10-18** — Chen-Fang Hu, Hong-Han Shuai, Woan-Shiuan Chien — [Memory, Know Your PLACE: Governing Lifecycle State and Query-Time Eligibility in Persistent-Memory Agents](http://arxiv.org/abs/2610.25179v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory turns prior interactions into durable agent state, but existing systems provide limited control over whether that state remains valid and whether it should influence a later query. We argue that reliable memory requires governance over both state formation and query-time influence. We introduce PLACE, a factorized governance layer that adds write-side state certification and read-side authorization to a memory backend. A factorial evaluation on Mem0 with Qwen2.5-3B and Qwen2.5-...
  </details>

- **2026-10-18** — Yichen Liu, Xiaochong Jiang, Haoran Yu et al. — [Learning Which Device to Call: Online Tool Grounding for LLM Agents in IoT](http://arxiv.org/abs/2610.25563v1)
  <details><summary>📄 Abstract</summary>
  The Internet of Things (IoT) gives large language model (LLM) agents access to physical observations, but one requested capability is usually offered by several devices, and the agent's plan does not say which one to call. Existing work retrieves relevant tools and checks plan feasibility, without learning which eligible device returns a useful observation. Unlike previous works, we study online tool grounding: binding an already specified tool call to one physical endpoint under service cost an...
  </details>

- **2026-10-18** — Jiaqi Gan, Tsang Ng, Ankit Raj et al. — [Quality-Controlled Reply and Summary Data for Post-Training Small Language Models in AI Call-Screening Agents](http://arxiv.org/abs/2610.25458v1)
  <details><summary>📄 Abstract</summary>
  Small language models have improved to the point where a phone can plausibly screen its own calls, answering on an absent owner's behalf without sending call content off the device, a privacy-respecting alternative to cloud call handling. Realizing that promise takes a model that can do two things well: reply within the owner's authority during the call, and afterward tell the owner what happened and what needs attention. Released small models do neither reliably - they raise unwarranted alarms ...
  </details>

- **2026-10-18** — Qingyu Li, Shuangyang Li, Guanghui Liu et al. — [Receiver Design for Continuous-Time AFDM based on Pre-Filter De-Chirp](http://arxiv.org/abs/2610.25168v1)
  <details><summary>📄 Abstract</summary>
  Affine frequency division multiplexing (AFDM) is a promising waveform for future high-mobility communications due to its Doppler robustness and diversity gain. However, existing continuous-time AFDM relies on chirp-dependent wideband receive filtering, which increases noise power and causes channel-energy leakage. In this paper, we propose an AFDM reception scheme based on pre-filter de-chirp for doubly selective channels. The coupling between de-chirp and the channel is first characterized, yie...
  </details>

- **2026-10-18** — Karthik Iyer, Nasser Sabar — [M-JEPA: Predictive Self-Supervised Learning for Molecular Graphs with Scaffold-Shift Evaluation on Tox21](http://arxiv.org/abs/2610.25163v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised molecular representation learning is increasingly used to improve transfer on small, label-limited property prediction tasks, yet commonly used contrastive objectives can be sensitive to view construction and are often evaluated with protocols that report only discrimination. We adapt Joint Embedding Predictive Architectures (JEPAs) to molecular graphs by masking chemically coherent connected subgraphs and training a context encoder to regress the masked target embedding produced...
  </details>

- **2026-10-18** — Jiaming He, Guanyu Hou, Yi Yu et al. — [Indistinguishable Agents: Training Agent Privacy as Twin-World Indistinguishability](http://arxiv.org/abs/2610.25161v1)
  <details><summary>📄 Abstract</summary>
  LLM agents search, shop and send messages for their users, and every action is seen by some party. Existing privacy training rewards agents for not mentioning protected items, yet an observer can infer a private fact from what the agent does. Since an observer learns a fact only if its view changes with the fact, we propose \methodfull (\method), which trains on twin worlds that differ only in the private fact. A frozen distinguisher scores each observer's view by its log-likelihood ratio for th...
  </details>

- **2026-10-18** — Daksh Pandey, Sayon Duttagupta, Xinhai Zou et al. — [Don't Judge an Agent by Its Messages: Private-State Leakage under Passive Monitoring of Agent Communication](http://arxiv.org/abs/2610.25032v1)
  <details><summary>📄 Abstract</summary>
  An AI agent can reproduce the distribution of its messages and of the receiver's task outcomes while disclosing private information that the task never required. We ask what a passive audit can certify when the auditor knows the authorised sender and the exact observable law but has no trusted pairing of messages with the private states behind them. For a single round, compatible mutual-information leakage forms a sharp interval, and fixing the entire task-relevant message law, with every declar...
  </details>

- **2026-10-17** — Zeyu Cao, Qingxuan Wu, Zhiyang Dou et al. — [PCHMR: Empowering and Benchmarking Human Mesh Recovery in Privacy-Constrained Real-World Settings](http://arxiv.org/abs/2610.24841v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning directly on user-side data is an effective way to improve the performance of widely adopted data-driven human mesh recovery (HMR) models. However, doing so for existing HMR methods often assumes aggregating user-side data from real-world HMR-deployed devices to a central training server, posing a significant privacy risk as sensitive human images are transmitted. How can human mesh recovery be evaluated and improved in privacy-constrained real-world settings? We study this question t...
  </details>

- **2026-10-17** — Alexander Gaponov, Grigory Malinovsky, Egor Shulgin et al. — [How Does Muon Work in Private Deep Learning? Scalable Differentially Private Training via Orthogonalization](http://arxiv.org/abs/2610.24736v1)
  <details><summary>📄 Abstract</summary>
  Training deep neural networks requires optimizers that balance computational efficiency with formal data privacy. While orthogonalized update rules, such as the recently introduced Muon optimizer, have shown strong empirical performance and scalability, their behavior under Differential Privacy (DP) is not yet understood. In this paper, we propose DP-Muon, a differentially private variant of the Muon optimizer. By analyzing Muon's orthogonalized updates through the lens of a Linear Minimization ...
  </details>

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


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-10-18** — Rui Meng, Song Gao, Tingting Zhu et al. — [SemVideoSte: Agentic AI for Cross-Modal Semantic Video Steganography Communication](http://arxiv.org/abs/2610.25257v1)
  <details><summary>📄 Abstract</summary>
  We propose an agentic artificial intelligence (AI)-driven cross-modal semantic video steganography communication (SemVideoSte) scheme for secure cross-modal information transmission. Agentic AI interprets the service context to determine a semantically matched public prompt and coordinates video generation, message embedding, semantic transmission, and message recovery process. A multi-mask mechanism combines variational autoencoder (VAE) reconstruction robustness, semantic transmission robustne...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 18 papers

- **2026-10-19** — Jan Wehner, Jam Kraprayoon — [Honeypots for AI Agent Insider Threats](http://arxiv.org/abs/2610.26664v1)
  <details><summary>📄 Abstract</summary>
  AI agents deployed inside organizations can pose an insider threat if they make mistakes, are compromised by an attacker, or pursue misaligned objectives. We propose honeypots as an AI control method to improve the security of internal agent deployments. Rather than only using honeypots for pre-deployment evaluations, defenders should plant decoy opportunities for harmful actions throughout the production environment to detect misbehavior, incriminate malicious agents, and deter attacks. Such ho...
  </details>

- **2026-10-19** — Chang Zhou, Jiarun Zhou, Xingtong Yu et al. — [ACE-Trader: Adversarial Co-Evolution for Generator-Critic Trading Systems](http://arxiv.org/abs/2610.25847v1)
  <details><summary>📄 Abstract</summary>
  Generator--critic trading systems pair an LLM-based trader that makes trading decisions with a red team agent that evaluates these decisions and provides feedback for revision. However, improving individual trading decisions does not ensure that both agents learn from experience and improve together over time. This raises an important question: how can the trader and red-Team select useful experience and learn from each other's evolving behavior? On one hand, experience that benefits decisions u...
  </details>

- **2026-10-19** — Cheng Jin, Zhongtian Ma, Xiao Wang et al. — [Towards Architectural-Level Safety Control: Relocating Hazardous Knowledge into Removable Experts in Mixture-of-Experts Models](http://arxiv.org/abs/2610.25791v1)
  <details><summary>📄 Abstract</summary>
  Large language models acquire broad knowledge from web-scale corpora during pretraining, including knowledge that could be hazardous if misused. Removing such knowledge from the model itself without degrading general capability is desirable but difficult, as it is deeply entangled with general capability within the same parameters. Existing safety alignment and unlearning methods typically adjust these shared parameters, tending to suppress the expression of hazardous knowledge rather than remov...
  </details>

- **2026-10-19** — Nardine Basta, Robin Carpentier, Benjamin Zi Hao Zhao et al. — [Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams](http://arxiv.org/abs/2610.26781v1)
  <details><summary>📄 Abstract</summary>
  Phone scams impose substantial and growing costs on individuals and financial systems worldwide, yet existing countermeasures impose no resource cost on perpetrators. Strategic scam-baiting, in which automated agents engage scammers to deplete their operational capacity, offers a proactive alternative but requires dynamic strategy adaptation that static systems cannot provide. We introduce a game-theoretic framework enabling LLMs to learn effective counter-strategies through in-context experienc...
  </details>

- **2026-10-19** — Tan-Ha Mai, Hsuan-Tien Lin, Vu Nguyen — [CAVA: Complementary-Label-Aware Data Valuation](http://arxiv.org/abs/2610.26734v1)
  <details><summary>📄 Abstract</summary>
  Complementary-label learning (CLL) trains a classifier from labels that name a class an instance does not belong to. Such labels are cheap to collect from crowdworkers or vision-language models (VLMs), making them attractive for large-scale annotation. However, both sources can mistakenly assign the true class as the complementary label. Such annotation errors are particularly harmful in CLL because the model is explicitly trained to suppress the correct answer. Optimal transport (OT) data valua...
  </details>

- **2026-10-19** — Israel Abebe Azime, Jesujoba O. Alabi, Iffat Maab et al. — [AfriGuard: Safety and Robust Refusal For African Languages](http://arxiv.org/abs/2610.26474v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) designed to interact with users are typically trained to respond appropriately to harmful or toxic content. However, ensuring appropriate responses becomes more challenging in diverse linguistic and cultural contexts, where safety risks may be expressed or interpreted differently. Building safe AI systems therefore requires detecting safety risks, understanding their nature, and responding appropriately, while accounting for linguistic and cultural variations that ad...
  </details>

- **2026-10-19** — Jerry Kaplan — [A Calibrated Instrument for Detecting Disposition Drift in Language Models](http://arxiv.org/abs/2610.25735v1)
  <details><summary>📄 Abstract</summary>
  Before language models are released, they are tested for harmful traits such as willingness to carry out dangerous requests, deception, power seeking, and sycophancy. The safe behavior these tests certify may degrade as models are modified, by topical fine-tuning, new training data, or changes to settings such as the depth of their reasoning. Most work reports such drift as single summary rates scored by another AI model, without the error analysis needed to interpret them. We adapt a calibrated...
  </details>

- **2026-10-19** — Hau-Sing So, Daixian Liu, Carl Hou et al. — [Whose Credential Is It? How Owner Attribution in Agent MemoryShapes Cross-User Account Misuse](http://arxiv.org/abs/2610.25707v1)
  <details><summary>📄 Abstract</summary>
  Shared long-term memory lets an LLM agent serving one user inadvertently retrieve another user's credentials, but it is unclear when such exposure leads to actual harm. We introduce a three-stage audit that separates three events: a foreign credential reaches the prompt (exposure), the agent acts with it (behavior), and the other user's account changes (state). In AppWorld, a store that mixes 763 past logins from all users retrieves another user's credential for 84.7 percent of required apps, ye...
  </details>

- **2026-10-19** — Zhiyuan Wang, Yuezhi Zhou, Zhu Zhang et al. — [When Safety Fails Collectively: Robust Alignment Against Harmful Fine-Tuning via Joint Weight Perturbations](http://arxiv.org/abs/2610.25683v1)
  <details><summary>📄 Abstract</summary>
  Harmful fine-tuning can rapidly erode the safety alignment of large language models, creating substantial risks when aligned models are adapted to downstream tasks. Existing alignment-stage defenses use harmful examples and simulated harmful perturbations during safety alignment to prepare models for later harmful fine-tuning, yet the collective effects of harmful weight perturbations remain underexplored. We identify a collective failure pattern: disjoint parts of a harmful perturbation have li...
  </details>

- **2026-10-19** — Jesson Wang, Zhanhao Hu, Minghao Lin et al. — [Safety Offset Learning: When Benign Fine-Tuning Misaligns LLMs](http://arxiv.org/abs/2610.25611v1)
  <details><summary>📄 Abstract</summary>
  Safety risks from fine-tuning are commonly characterized by the harmfulness of the training data:harmful fine-tuning is considered dangerous, while benign fine-tuning is often assumed to preservealignment. We argue that this view misses a more fundamental factor-the behavioral transition inducedby supervision. Harmful fine-tuning and safety-degrading benign fine-tuning can both be understoodas learning the same refusal-to-compliance transition, but on different data distributions. We studywhethe...
  </details>

- **2026-10-18** — Tianhe Lu, Sakuna Harinda Jayasundara, Eric Spero et al. — [Many Repairs, One Direction: Steering Code Models Toward Safer Cryptographic API Use](http://arxiv.org/abs/2610.25133v1)
  <details><summary>📄 Abstract</summary>
  Cryptographic API misuse in large language model-generated code can compromise software security. While many existing approaches improve code security by modifying model parameters or inputs, how representation changes associated with different cryptographic API repairs can support a shared intervention for safer code generation remains underexplored. To investigate this, we construct 48,000 matched program pairs across four programming languages and ten cryptographic API misuse categories. Each...
  </details>

- **2026-10-18** — Xi Zhu, Yuanlin Duan, Changyi Yang et al. — [Trackable Skill Library Lifecycle Management for Agentic Reinforcement Learning](http://arxiv.org/abs/2610.25126v1)
  <details><summary>📄 Abstract</summary>
  Skill-augmented agentic RL has emerged as an effective approach to improving LLM agents on long-horizon tasks. Despite this progress, individual skills may follow distinct trajectories as the policy evolves, with some becoming redundant after the model internalizes their capabilities, others remaining valuable as external scaffolding, and still others turning harmful. However, existing skill library systems fail to identify each skill's true contribution due to free-riding among co-retrieved ski...
  </details>

- **2026-10-18** — Simiao Ren, Tommy Duong, Xingyu Shen et al. — [Scam Town: Can Scam Education Spread Like a Vaccine?](http://arxiv.org/abs/2610.25040v1)
  <details><summary>📄 Abstract</summary>
  Most older adults who hear a warning about scams hear it from someone they know: a relative, a neighbour, or a friend who was targeted. Yet research on scam prevention almost always studies one person at a time. We ask whether scam awareness can spread through a community and protect it the way a vaccine does, since a warning protects whoever hears it and can be passed on. To find out, we built Scam Town, a simulated community in which a large language model plays each resident. Scam centres pho...
  </details>

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


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 57 papers

- **2026-10-19** — Youran Dong, Junfeng Yang, Wei Yao et al. — [Newton-Based Methods for Bilevel Optimization Beyond Lower-Level Strong Convexity](http://arxiv.org/abs/2610.26839v1)
  <details><summary>📄 Abstract</summary>
  Bilevel optimization provides a framework for machine learning tasks such as hyperparameter optimization, data reweighting, and meta-learning. Existing Newton-based bilevel methods typically rely on the classical hypergradient formula, which is generally unavailable when lower-level solutions are nonunique and the lower-level Hessian is singular. We develop two Newton-based methods beyond lower-level strong convexity by exploiting curvature shared by the lower-level and multiplier updates. Newto...
  </details>

- **2026-10-19** — Ming Yang, Yaqi Yin, Zhibo Wang et al. — [AGR: Agentic Generative Retrieval with Tool-Augmented Search](http://arxiv.org/abs/2610.26831v1)
  <details><summary>📄 Abstract</summary>
  Large-scale search and recommendation systems derive much of their retrieval quality from rich, heterogeneous features, yet existing generative retrieval (GR) methods struggle to exploit such feature ecosystems efficiently. Static feature injection either encodes all available signals or places them according to predetermined schemes, increasing serving cost and introducing irrelevant or conflicting evidence. More fundamentally, existing methods cannot adaptively determine when a feature is need...
  </details>

- **2026-10-19** — Zhuofan Josh Ying, Guanglong Sun, Nolan Ho et al. — [Scaling Parameter-Efficient Fine-Tuning for Brain Encoding](http://arxiv.org/abs/2610.26802v1)
  <details><summary>📄 Abstract</summary>
  Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or fully fine-tune them after task-pretraining has proven difficult because neural data is costly and limited. We show that parameter-efficient fine-tuning (PEFT) enables us to effectively adapt very large pretrained backbones for brain encoding with a small number of trainable parameters. To make it c...
  </details>

- **2026-10-19** — Josiah Dykstra — [Accountable partial understanding: securing the epistemic attack surface of agentic systems](http://arxiv.org/abs/2610.26799v1)
  <details><summary>📄 Abstract</summary>
  Attackers profit from what defenders do not understand. Software security has treated the gap between system behavior and human comprehension as a condition to narrow through analysis and assurance, booking the remainder as accepted risk. Agentic AI systems change that gap: when software reads, writes, explains, and authorizes security-relevant behavior, partial understanding moves faster, grows more opaque, and couples to delegated authority. This paper characterizes the resulting epistemic att...
  </details>

- **2026-10-19** — Qian Xie, Wenyue Hua, Yueli He et al. — [Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows](http://arxiv.org/abs/2610.26676v1)
  <details><summary>📄 Abstract</summary>
  LLM agentic workflows increasingly employ different models for specialized roles. Users may prefer different trade-offs between task quality and deployment cost, sometimes also considering latency. Finding good assignments incurs a separate search cost from evaluating multiple candidates. We introduce Cost-Coupled Gittins (CC-Gittins), a multi-objective extension of single-objective cost-aware Gittins search for Pareto recommendation. It exploits the coupling between evaluation and deployment co...
  </details>

- **2026-10-19** — Xiao Zhou, Alex Schutz, Victor-Alexandru Darvariu et al. — [PACT: Plan-Augmented Coordination via Trace-Graphs for Dynamic Multi-Agent Combinatorial Optimization](http://arxiv.org/abs/2610.26671v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent approaches have been investigated recently as a means of improving the scalability of reinforcement learning for neural combinatorial optimization. Existing methods assume that all problem instance information is known upfront. However, real-world problems are often dynamic: relevant information is progressively revealed as the agents take actions (e.g., arriving at an edge in a routing problem only to discover it is untraversable). In such cases, existing methods fail to coordinate ...
  </details>

- **2026-10-19** — Shuyuan Hu, Deng-Ke Wu, Yifan Jin et al. — [Learn the Task, Not the Schedule: Reducing Spurious Cross-Arm Coupling in Bimanual Imitation Learning](http://arxiv.org/abs/2610.26507v1)
  <details><summary>📄 Abstract</summary>
  A bimanual demonstration specifies both what the robot should do and one particular schedule for when each arm should act. Standard imitation learning does not distinguish task-required cross-arm constraints from incidental scheduling choices, and may therefore exploit opposite-arm progress as a shortcut cue, creating spurious cross-arm coupling even where relative timing is irrelevant for the current task phase. We introduce Constraint-preserving Temporal Recombination (CTR), a training-time da...
  </details>

- **2026-10-19** — Zhuowen Guo, Rongzhong Xiao, Shuhao Zhang — [Pointwise convergence of bilinear ergodic averages for commuting transformations](http://arxiv.org/abs/2610.26388v1)
  <details><summary>📄 Abstract</summary>
  Let $(X,\mathcal B,μ)$ be a probability space and let $S,Q:X\to X$ be commuting probability-preserving transformations. Let $1\leq p,q\leq\infty$ satisfy $1/p+1/q\leq1$. We prove that, for every fixed $F\in L^p(μ)$ and $G\in L^q(μ)$, the averages $$ \frac1N\sum_{n=1}^N F(S^nx)G(Q^nx) $$ converge almost everywhere as $N\to\infty$.   Our proof introduces a new analytic approach that relies on neither the circle method nor characteristic-factor theory. Exploiting the triangular structure arising fr...
  </details>

- **2026-10-19** — Chenhao Zhou, Jiyu Wei — [Toward Online Robust Zero-Sum Markov Games with Function Approximation](http://arxiv.org/abs/2610.26286v1)
  <details><summary>📄 Abstract</summary>
  Online robust zero-sum Markov games pose a coupled operator-learning and game-solving problem: from nominal interaction data, the learner must recover a worst-case minimax Bellman operator while maintaining strategic coverage and controlling stage-game approximation error. Existing robust reinforcement-learning theory does not yet provide such an operator-learning perspective beyond specialized multi-agent settings. We develop an optimistic dual robust Bellman framework that combines dual robust...
  </details>

- **2026-10-19** — Martin Kurečka, Roman Andriushchenko, Milan Češka et al. — [Anytime-Valid Monitoring of Robust Stochastic Models](http://arxiv.org/abs/2610.26193v1)
  <details><summary>📄 Abstract</summary>
  Formal methods provide a principal approach to obtaining safety guarantees for autonomous agents. Their key bottleneck is their reliance on a formal model (e.g., a Markov decision process) describing the agent-environment interaction. Learning or crafting the model is an error-prone process, which undermines the guarantees offered by formal methods. Robust models account for modelling uncertainty, but may still fail to capture the true environment. This issue can be addressed through \emph{runti...
  </details>

- **2026-10-19** — Mirza Masfiqur Rahman, MD Ajwad Akil, Imtiaz Karim et al. — [SPLASH: Contrastive Audit Pressure for Detecting and Localizing Security Hallucinations in Generated Code](http://arxiv.org/abs/2610.26001v1)
  <details><summary>📄 Abstract</summary>
  Code generated by large language models often passes every functional test while remaining insecure. These security hallucinations are common, written with high confidence, and repeated across samples, so neither the generator's own uncertainty nor static analyzers reliably catch them. We introduce SPLASH, which is guided by a new measure called audit pressure. It contrasts teacher-forced log-probabilities for the generated program under a security review and a style review. Aggregated to statem...
  </details>

- **2026-10-19** — Suxing Liu — [GraphEvoResearcher: Graph-Aware Training-Free Self-Reflective Reasoning for Cost-Bounded Multi-Hop Question Answering](http://arxiv.org/abs/2610.25978v1)
  <details><summary>📄 Abstract</summary>
  Multi-hop question answering (QA) requires models to chain intermediate conclusions while remaining cost-aware. Existing training-free self-reflective protocols (generate -> critique -> revise) improve accuracy but operate on a flat token stream: revisions cannot identify which prior step is unreliable, and early stopping cannot exploit structural convergence. We introduce GraphEvoResearcher, a training-free protocol that lifts EvoResearcher's self-reflective meta-reward onto an explicit reasoni...
  </details>

- **2026-10-19** — Tue Le, Anh Nguyen Hoang, Gabriel Sasseville et al. — [Secure Agentic Coding through Counterexample-Grounded Feedback](http://arxiv.org/abs/2610.25916v1)
  <details><summary>📄 Abstract</summary>
  As coding models and agent harnesses become more capable, reliable security verification is becoming a central bottleneck. Improving secure code generation requires a signal whose reported progress remains aligned with actual program behavior under optimization; otherwise, an optimizer can improve the signal's verdict without removing the underlying vulnerability. Existing model-based approaches require models to either infer program behavior from source code or specify correct outcomes for adve...
  </details>

- **2026-10-19** — Muhammad Ahmad, Gemine Vivone, Ronny Hänsch et al. — [See the Future, Classify the Present: Stochastic Latent World Modeling for Hyperspectral Images](http://arxiv.org/abs/2610.25781v1)
  <details><summary>📄 Abstract</summary>
  Hyperspectral image classification (HSIC) relies on static spatial-spectral representations learned from labeled samples, limiting its ability to model structured dependencies in the latent representation space. To address this limitation, this work proposes Stochastic Latent World Modeling (LWM), a trajectory-based representation-learning framework that enriches classification through stochastic latent-state prediction. Given a hyperspectral patch, LWM tokenizes and encodes spectral and spatial...
  </details>

- **2026-10-19** — Haoran Xue, Nikta Akbarpour, Gias Uddin et al. — [How Effectively Do Security Skills Guide Coding Agents in Vulnerability Detection in Linux Kernel?](http://arxiv.org/abs/2610.25705v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) coding agents, such as Claude Code, are increasingly used for security auditing, with task-specific skills providing reusable vulnerability-analysis procedures. However, their effectiveness in detecting real vulnerabilities and the reasons for their failures remain unclear. We conduct the first large-scale empirical study of 37 security skills using Claude Code with four underlying LLMs on 100 real Linux kernel vulnerabilities across ten classes, totaling 14800 runs. W...
  </details>

- **2026-10-19** — Sofia McLeod, Mohsi Jawaid, Carl Seubert et al. — [Recurrent Vision Transformers for Event-Based Spacecraft Pose Estimation Under Slow Relative Motions](http://arxiv.org/abs/2610.25622v1)
  <details><summary>📄 Abstract</summary>
  Vision-based object pose estimation is vital for conducting spacecraft rendezvous and proximity operations (RPO). Recent research has demonstrated the robustness of event cameras against the harsh lighting conditions that often occur in orbit, thanks to the extremely high dynamic range of event sensors. However, event-based spacecraft pose estimation (EBSPE) suffers when the relative motion between the chaser and target is slow, since the event rate drops significantly, leading to data with low ...
  </details>

- **2026-10-18** — Cheng-Han Lee, Amir Salimi, Hsiang-Wei Huang et al. — [DiffGround: Semantic Difference-Guided Zero-Shot Video Question Grounding](http://arxiv.org/abs/2610.25570v1)
  <details><summary>📄 Abstract</summary>
  Video Question Grounding (VideoQG) requires both accurate question answering and precise temporal localization. Existing supervised methods rely on costly temporal annotations, while existing zero-shot approaches are primarily designed for Video Question Answering (VQA) and are not optimized for temporal grounding. We propose DiffGround, an action-driven zero-shot framework built upon frozen Multimodal Large Language Models (MLLMs). Our framework first predicts an answer-relevant action cue that...
  </details>

- **2026-10-18** — Haoyang Fan, Dhruv Parikh, Rajgopal Kannan et al. — [StreamAhead: Real-Time Streaming Video Question Answering via Adaptive Precomputation](http://arxiv.org/abs/2610.25551v1)
  <details><summary>📄 Abstract</summary>
  Real-time streaming video question answering with vision-language models must answer queries that arrive at any time with low latency while sustaining the video-processing rate required by the application. Existing systems construct key-value (KV) caches for the entire video as it arrives, although a query typically uses only a few of the preceding frames as evidence. This highlights a fundamental trade-off: performing more computation as video arrives reduces query-time computation but can incr...
  </details>

- **2026-10-18** — Jundong Chen, Honglei Zhang, Shuai An et al. — [When Semantics Fall Short: Persona-Guided Cross-Domain Sequential Recommendation with Large Language Models](http://arxiv.org/abs/2610.25221v1)
  <details><summary>📄 Abstract</summary>
  Cross-domain sequential recommendation (CDSR) alleviates data sparsity by transferring user behaviors across domains. Recent advances increasingly leverage large language models (LLMs) to bridge domains through global item semantics. However, this paradigm is inherently limited by two issues: I. semantic domain isolation, where item semantics remain domain-specific and hinder transferable modeling, and II. semantic-behavior inconsistency, where local semantic relations are more consistent with b...
  </details>

- **2026-10-18** — Shuheng Gao, Yuankai Fan, Jiaqiang Ma et al. — [Visual Cache Reuse for Efficient Multimodal Inference](http://arxiv.org/abs/2610.25136v1)
  <details><summary>📄 Abstract</summary>
  Vision-language model (VLM) inference incurs substantial prefill latency and memory overhead due to the long visual token sequences of large visual inputs. Existing serving systems typically exploit exact cache reuse through prefix caching or position-independent caching, overlooking the potential of approximate caching in real-world workloads. However, directly reusing an approximate cache entry may introduce spurious visual information, which naive approaches that select a subset of important ...
  </details>

- **2026-10-18** — Xiaoyu Wu, Zhaoxin Yu, Xinglin Xiao et al. — [TIRE: Top-Down Formula Instantiation with Reliable Execution for Physics Problem Synthesis](http://arxiv.org/abs/2610.25134v1)
  <details><summary>📄 Abstract</summary>
  Advancing physics reasoning in large language models requires scalable training data that connect physical laws, concrete problem scenarios, and verifiable numerical answers. Expert-designed problems offer top-down control over physical laws, conditions, and scenarios, but require costly human effort. LLM-based synthesis from texts scales efficiently, but model-generated answers and assessments leave supervision vulnerable to hallucinations. We introduce TIRE, a framework for Top-Down Formula In...
  </details>

- **2026-10-18** — Galen J. Wilkerson — [Self-organizing reinforcement learning: a swarm approaches the explore-exploit optimum](http://arxiv.org/abs/2610.25113v1)
  <details><summary>📄 Abstract</summary>
  The explore/exploit trade-off is the core problem of reinforcement learning (RL). We show that a minimal foraging swarm approaches its optimum - the ideal-free / Nash allocation of a multi-agent resource-sharing game (an equilibrium, not a return maximum) - with no learner and no reward signal. Agents explore by heavy-tailed (Levy) flights, recruit neighbours to a discovery through a threshold cascade on their proximity network, and disperse as a patch crowds; this cascade cycle balances explora...
  </details>

- **2026-10-18** — Huaijin Wang, Tongda Wang, Zhibo Liu et al. — [Locate, Then Reason: End-to-End Patch Presence Testing in Stripped Binaries](http://arxiv.org/abs/2610.25071v1)
  <details><summary>📄 Abstract</summary>
  Binary patch presence testing (PPT) determines whether a security fix is present in a stripped binary. Prior systems often assume that patch-relevant code is known or successfully matched. Function-level matching is brittle to compilation changes, inlining, finite model context, and missing usage context; moreover, similarity suppresses the patch-sized distinction needed for the verdict. We present PatchAlign, an end-to-end binary PPT workflow, which performs large-scale localization that maximi...
  </details>

- **2026-10-18** — David X. Lin, Chido Onyeze, Giannis Fikioris et al. — [Non-Monetary Mechanisms for Stochastic Scheduling via Sampled Pairwise Externality Compensation](http://arxiv.org/abs/2610.25067v1)
  <details><summary>📄 Abstract</summary>
  How can a shared resource be allocated without money when agents have private, stochastic demands that can be queued for a while, and may behave strategically, or even adversarially? We introduce a paradigm for non-monetary online resource allocation called Sampled Pairwise Externality Compensator (SPEC). Our objective is to guarantee each agent a large fraction of its ideal utility: an individual benchmark corresponding to serving the highest-valued fraction of its demand permitted by an equal ...
  </details>

- **2026-10-18** — Dongyang Li, Mingsong Yan, Zheng Zhang et al. — [T-MUON: Tensorizing Muon via t-SVD for Large Language Model Pre-training](http://arxiv.org/abs/2610.24938v1)
  <details><summary>📄 Abstract</summary>
  Muon has recently emerged as a strong optimizer for large language model pretraining by exploiting matrix structure through polar orthogonalization. However, it processes each parameter matrix independently, whereas recent tensor-aware extensions of Muon jointly update groups of eligible matrix parameters through matrix unfoldings. In contrast, we propose T-MUON, a t-SVD-based generalization that groups structurally related Transformer gradients into third-order tensors and defines the correspon...
  </details>

- **2026-10-18** — Wentao Hong — [AgentLens: Framework-Aware Characterization and Resource Control for Heterogeneous LLM Agents](http://arxiv.org/abs/2610.25231v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are increasingly deployed on shared hosts, yet their host-side resource demands remain poorly understood, limiting effective resource coordination. We present AgentLens, which combines a cross-framework workload characterization with a framework-aware resource controller for co-located agents. Across 10 frameworks and 11 matched coding tasks, we find that framework orchestration strongly shapes resource demand: framework identity explains 52.95% of peak RSS variance, compared wi...
  </details>

- **2026-10-17** — Jinwei Hu, Youcheng Sun, Yi Dong et al. — [The One-Pixel of Reasoning: One Truthful Relation Is Enough to Mislead LLM Agents](http://arxiv.org/abs/2610.24873v1)
  <details><summary>📄 Abstract</summary>
  Can one sentence manipulate an agent's belief by targeting a single implicit warrant linking evidence to a conclusion? In this paper, we introduce the one-relation attack (ORA), a novel cognitive attack on this inferential relation. ORA localizes a critical implicit warrant and performs a one-relation intervention using a single source-grounded sentence that qualifies this warrant and steers the agent toward an incorrect belief. Across eighteen models on biomedical inference and vulnerability de...
  </details>

- **2026-10-17** — Galen J. Wilkerson — [A general mechanism for collective foraging: percolating recruitment cascades coupled to a maximum-entropy](http://arxiv.org/abs/2610.24865v1)
  <details><summary>📄 Abstract</summary>
  Foraging recruitment is a contagion: an agent finding a resource triggers a linear-threshold cascade -- the model for rumour and adoption spread on social networks -- embedded in space. Because activation is degree-normalized, the same rule that spreads the cascade also stifles it as neighbourhoods crowd (density-dependent blocking), so the swarm aggregates on a resource, then releases to explore again. The cascade runs on the communication network, but acting on it moves agents in physical spac...
  </details>

- **2026-10-17** — Zachary Cutts, John Coller, Rachel Chen et al. — [Aptamers as a sandbox for lab-in-the-loop agentic molecular discovery](http://arxiv.org/abs/2610.24806v1)
  <details><summary>📄 Abstract</summary>
  Despite breakthroughs in AI-driven molecular generation, existing discovery pipelines operate largely in silico, with wet-lab feedback reserved for validation rather than iterative improvement. Whether large language model (LLM)-based reasoning agents can accelerate de novo discovery by iterating with lab data remains unproven.   Here we use protein-binding aptamer design as a sandbox (1-2 week cycles, \$1-\$3 per candidate) to demonstrate a wet lab in a closed loop with AI systems. We tasked ag...
  </details>

- **2026-10-17** — Francesco Morri, Adel Abusitta, Quentin Cappart et al. — [Cooperation Without Shared Rewards via Reciprocal Q-Augmentation](http://arxiv.org/abs/2610.24793v1)
  <details><summary>📄 Abstract</summary>
  General-sum games are more challenging than fully cooperative or adversarial settings because agents may deceive or exploit one another. Achieving high social welfare requires sustained cooperation, while a single defection can drive agents toward a welfare suboptimal Nash equilibrium. Moreover, assuming access to other agents' rewards or internal states is often unrealistic and implicitly introduces additional cooperation into the setting. To address this issue, we introduce \textit{Reciprocal ...
  </details>

- **2026-10-17** — Chaoran Zhu, Hengyi Wang, Chenglin Cui et al. — [Relational Spatial Alignment for Vision-Language-Action Models](http://arxiv.org/abs/2610.24705v1)
  <details><summary>📄 Abstract</summary>
  Spatial understanding is essential for robots to perceive their surrounding environments and execute actions. Existing approaches typically encode 3D awareness into vision-language-action (VLA) models by directly aligning their representations with pre-trained 3D foundation models. However, we observe that such direct geometric feature alignment essentially exploits 3D foundation priors as a form of low-rank regularization in the feature space, resulting in severe rank collapse of the pre-traine...
  </details>

- **2026-10-17** — Pourya Shamsolmoali, Masoumeh Zareapoor — [Geometry-Aware Interpolation for Inverse Problems](http://arxiv.org/abs/2610.24687v1)
  <details><summary>📄 Abstract</summary>
  Recovering missing visual information from incomplete or degraded images remains a challenging problem, particularly when spatial variations and complex image structures affect reconstruction accuracy. Although Spatial Transformer Networks (STNs) facilitate spatial feature alignment, their reliance on conventional linear or bilinear interpolation limits their ability to capture the underlying geometric characteristics of image data. Furthermore, interpolation based on a restricted set of neighbo...
  </details>

- **2026-10-17** — Ruitao Feng, Yuekang Li, Yao Zhang — [Narratives Mislead: An Empirical Study of How LLMs Misjudge CVSS Severity in Bug Bounty Reports](http://arxiv.org/abs/2610.24623v1)
  <details><summary>📄 Abstract</summary>
  Bug bounty platforms receive vulnerability reports faster than vendors can triage them, and Large Language Models (LLMs) are increasingly considered for assigning the Common Vulnerability Scoring System (CVSS) severity that drives prioritization. Prior evaluations score short CVE descriptions and report accuracy, but deployment depends on how models err, not only how often. CVSS gives each metric a formal meaning that departs from how researchers describe impact in narrative reports, and model r...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 54 papers

- **2026-10-19** — Ege Gursoy, Nicolas Mansard — [TriScore: Post-Hoc Out-of-Distribution Detection with Energy, Boundary Probes, and Transform Consistency](http://arxiv.org/abs/2610.26323v1)
  <details><summary>📄 Abstract</summary>
  Post-hoc out-of-distribution detection usually relies on a single signal extracted from a frozen classifier, such as confidence, energy, features, or gradients. This dependence becomes fragile under classifier-level adversarial shift, where the shift can preserve the detector's chosen cue while changing the model's decision behavior. We investigate whether this failure mode can be mitigated by combining complementary detection criteria instead of selecting a single score. We introduce TriScore, ...
  </details>

- **2026-10-19** — Alessia Intini, Lorenzo Vaiani, Enrico Chen et al. — [Long-form Video-to-Text Summarization using Recursive Language Models](http://arxiv.org/abs/2610.26431v1)
  <details><summary>📄 Abstract</summary>
  While VideoLLMs have made significant progress in understanding short video benchmarks, they often struggle to summarize long-form ones. This is mainly due to performance degradation caused by long-context prompts, the inherent difficulty of preserving temporal continuity and a lack of semantically rich concepts in event descriptions. To tackle these issues, this paper introduces the first recursive Video Language Summarization Model (RVLSM) designed for video processing and tailored to long-for...
  </details>

- **2026-10-19** — N Guerin, A Dehoux, M Nakhla — [Autonomous intelligence for mining productivity: a multi-agent AI approach to operational value creation](http://arxiv.org/abs/2610.26369v1)
  <details><summary>📄 Abstract</summary>
  Integrated Remote Operation Centres (IROCs) are emerging as the architectural frontier of Industry 4.0 for capital-intensive sectors such as mining, oil and gas, and energy. Yet two intertwined gaps constrain their evolution towards full autonomy. First, no integrated agentic architecture has been proposed for mining IROCs that orchestrates Supervisory Control and Data Acquisition systems, digital twins, predictive analytics and human-machine interfaces under safety-critical constraints. Second,...
  </details>

- **2026-10-19** — Ruotian Peng, Yuanyi Ren, Shuaiqi Liu et al. — [VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement](http://arxiv.org/abs/2610.26342v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) requires agents to diagnose system bottlenecks and coordinate improvements across training and inference. We refer to the agents' capability to jointly optimize training data, the trainer, and the inference harness as cross-component co-design. We introduce VibeTraining-Bench, a benchmark for evaluating this capability across tasks spanning terminal operation, software engineering, multi-turn tool use, and mathematical reasoning. Within each task, research agents...
  </details>

- **2026-10-19** — Zhanhui Zhou, Weichen Zhang, Haoran Liu et al. — [CUA-Lite: An Open Platform for Computer Use Agents](http://arxiv.org/abs/2610.26071v1)
  <details><summary>📄 Abstract</summary>
  Open resources for computer use agents (CUAs) -- environments, datasets, and models -- remain scattered: without a standard, these resources cannot be integrated and scaled; additionally, evaluation, RL, and SFT cannot share one infrastructure. We present CUA-Lite, an open platform for developing CUAs, built around three standardized abstractions: (1) Unified environment interface, under which we integrate 12 benchmarks across desktop, browser, and mobile, plus lightweight VM-free sandboxes that...
  </details>

- **2026-10-19** — Hanna Hubarava, Benjamin V. Ineichen — [Accelerated Drift of Scientific Prose in the LLM Era: Evidence from an Interrupted Time-Series Analysis](http://arxiv.org/abs/2610.26008v1)
  <details><summary>📄 Abstract</summary>
  Every scientific text is embedded in the writing norms of its time: it reflects earlier publications while also shaping the texts that follow. The growing use of LLM-based writing tools introduces a new factor in this evolving system, but the linguistic changes coinciding with their emergence remain insufficiently understood. We investigate whether the trajectories of scientific-preprint writing changed in rate or direction after conversational LLMs became publicly accessible, using the release ...
  </details>

- **2026-10-19** — Ekaterina Fedorova, Alessandro Morosini, Chara Podimata — [Reasoning-Aware Multicalibrated Reliability Predictors for Language Models](http://arxiv.org/abs/2610.26645v1)
  <details><summary>📄 Abstract</summary>
  As people increasingly rely on large language models (LLMs) for information, model providers need to communicate meaningful estimates of whether individual responses are correct or, more generally, reliable. In the context of hallucinations, existing work uses multicalibration to make such reliability predictions meaningful across application-relevant groups, such as prompt topics. Topic groups alone, however, can conceal systematic errors: within the same topic and confidence level, responses w...
  </details>

- **2026-10-19** — Xucheng Yu, Jiangping Chen, Haohan Wang — [Where Does Rhetorical Distortion Live? A Multi-Platform, Multi-Language Measurement of Influencer Content](http://arxiv.org/abs/2610.26412v1)
  <details><summary>📄 Abstract</summary>
  Much of the manipulation in online influencer content is not false but disproportionate: an accurate fact is framed as historic, urgent, or catastrophic. Fact-checking and clickbait detection are not designed to capture such framing, and little is known about where it originates: with the creator, the topic, the platform, or the audience that replies. We operationalize rhetorical distortion through five literature-grounded dimensions (Significance Inflation, Anxiety Manufacturing, Novelty Claims...
  </details>

- **2026-10-19** — Ghulam Mudassir, Hameed Ullah Khan, Ahmad Sami Al-Shamayleh et al. — [Fairness or Fallacy? Mapping the Landscape of AI Bias in Disease Detection](http://arxiv.org/abs/2610.26215v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) has several transformative effects on healthcare, like to facilitate clinicians in disease detection and to manage patient care with enhanced precision. Due to the increasing complexity of medical data and the growing volume of diagnostic images, the substantial computational power needed to process such information creates both opportunities and challenges. To accomplish this objective, numerous methodologies have been proposed to integrate AI into disease detection...
  </details>

- **2026-10-19** — Kemal Altwlkany, Muamer Paric — [Multilingual Voicemail and Answering Machine Detection via Pretrained Audio Embeddings and Gradient Boosting Machines](http://arxiv.org/abs/2610.26100v1)
  <details><summary>📄 Abstract</summary>
  Answering machine detection (AMD) is a fundamental task in telephony that classifies whether an answered call is picked up by a human or a voicemail (machine). Despite its widespread use across cloud communication platforms, existing approaches rely on proprietary systems with undisclosed architectures, or require computationally expensive models that cannot operate in real time. We propose a lightweight AMD system that combines pretrained audio embeddings with gradient boosting machines, traine...
  </details>

- **2026-10-18** — Nicholas Potteiger, Ankita Samaddar, Xenofon Koutsoukos — [Adaptive Cyber-Defense for Evolving Attacker Capabilities using Reinforcement Learning and Behavior Trees](http://arxiv.org/abs/2610.25420v1)
  <details><summary>📄 Abstract</summary>
  Autonomous cyber-defense agents trained using reinforcement learning (RL) are increasingly adopted for defending enterprise computer networks. However, existing approaches may become brittle as attacker capabilities evolve and enable new attack strategies. In this work, we study the problem of adapting defender policies learned in CAGE Challenge Scenario 2 (CC2), a benchmark enterprise network defense scenario, to an extended network scenario with new attacker capabilities represented by new att...
  </details>

- **2026-10-18** — Qiwu Wen, Jahangir Alam — [Shared-Private Cross-Modal Discrepancy Learning for Imbalanced Multi-Source Audio-Visual Deepfake Detection](http://arxiv.org/abs/2610.25301v1)
  <details><summary>📄 Abstract</summary>
  Audio-visual deepfake detectors are often trained under a single dataset or manipulation regime, but multi-source training collections may contain heterogeneous attacks and uneven source distributions. Training separate detectors for each source is inefficient, while a single shared detector may be biased toward dominant source-specific patterns. We study known-source imbalanced multi-source audio-visual deepfake detection using FakeAVCeleb and LAV-DF, where source identity is supplied during tr...
  </details>

- **2026-10-18** — Chenye Yang, Weiyu Xu, Lifeng Lai — [Robust Direct Preference Optimization under Preference Label-Flip Attacks](http://arxiv.org/abs/2610.24945v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) is widely used for offline Reinforcement Learning from Human Feedback. However, recent works have shown that DPO can be easily manipulated by adversarial preference label flip attacks, which are specifically designed to mislead the learner toward an attacker-chosen target policy. To address this issue, we design robust DPO methods that can defend against such attacks. Building on the property that lable flips induce parameter-independent gradient shifts in lo...
  </details>

- **2026-10-18** — Jinu Lee, Shraddha Barke — [Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors](http://arxiv.org/abs/2610.25552v1)
  <details><summary>📄 Abstract</summary>
  Symbolic constraints (programmatic, deterministic checks for tool calls) enable deterministic verification of LLM agents' tool calls, but existing approaches primarily enforce predefined safety policies rather than tool dependencies in complex tool environments. We explore whether symbolic constraints can be mined from environments and observations beyond predefined policies, and whether they can improve end-to-end task performance. We present Symbolic Constraint Agents (SCA), a framework that m...
  </details>

- **2026-10-18** — Benjamin Tannenbaum — [Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations](http://arxiv.org/abs/2610.25461v1)
  <details><summary>📄 Abstract</summary>
  We test whether Javo, a sales agent fine-tuned on 4.6 million consented, de-identified commercial conversations, sells better than a frontier general-purpose model and better than human sales associates. The evaluation has four parts. Study 1 scores the agent on two public sales benchmarks, SalesLLM and SmartSalesBench, against 10 frontier and open-weight models. Study 2 is a randomized controlled trial on 100 live websites in 14 industries (e-commerce, travel and hospitality, and high-considera...
  </details>

- **2026-10-18** — Ilia Badanin — [CHSM8: A Chess Transformer that Follows Natural-Language Style Prompts](http://arxiv.org/abs/2610.25356v1)
  <details><summary>📄 Abstract</summary>
  We present CHSM8, a 210M-parameter chess transformer that plays moves conditioned on a free-text description of a playing style, e.g. "go for the Sicilian Defense", "solid, safe, risk-free chess" or "You are Magnus Carlsen in his prime". The model is pretrained without search on 1.07B filtered Lichess games, using a factorized move representation and legal-move masking. It reaches 1837 Elo against a strength-limited Stockfish and, in 1,000-game matches, beat every other public model we tested th...
  </details>

- **2026-10-18** — Jaehong Myung, Seunghun Oh, Unsang Park — [Local Evidence, Global Failure: Diagnosing Speech-Vision Temporal Composition in Audio-Visual Language Models](http://arxiv.org/abs/2610.25352v1)
  <details><summary>📄 Abstract</summary>
  Audio-visual large language models (AV-LLMs) can fail at full-video speech-vision decisions even when useful visual evidence is locally recoverable. We introduce Temporal Evidence Decomposition (TED), a training-free diagnostic framework that separates local visual verification from speech-relative aggregation. Automatic speech recognition supplies a transcript and utterance interval. TED queries audio-free windows with the transcript for Temporal Alignment and Forecasting, or answer candidates ...
  </details>

- **2026-10-18** — Silvia Fernández-Sabido, Jorge Reyes-Magaña, Jesús Adrián Chay Tun et al. — [Aligning Language Models with Indigenous Community Cosmovision through Constitutional AI](http://arxiv.org/abs/2610.25298v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are predominantly trained on corpora that reflect Western, anglophone worldviews. This asymmetry is not neutral: when a model answers questions about territory, community authority, or the relationship with nature, it does so from assumptions that may be alien to the communities using the system. This paper presents a system for aligning language models with the ethical principles of Indigenous communities in Latin America. Drawing on interviews with five Indigenous ...
  </details>

- **2026-10-18** — Mohamed Mahmoud, Mostafa Farouk Senussi, Mahmoud Abdalla et al. — [MEMORA: A Memory-Enhanced Multimodal Committee Reranking Agent for Reasoning-Intensive Retrieval](http://arxiv.org/abs/2610.25282v1)
  <details><summary>📄 Abstract</summary>
  Reasoning-intensive retrieval is fundamentally challenged when queries demand deep semantic inference and arrive in multimodal form. Existing systems treat each query in isolation, rely on monolithic rerankers, and lack retrievers trained for cross-modal reasoning. We introduce MEMORA, a Memory-Enhanced Multimodal Orchestrated Reranking Agent built around three contributions: (1) Collaborative Factor-Committee Reranking, which decomposes queries into intent factors, extracts factor-specific evid...
  </details>

- **2026-10-18** — Shuheng Gao, Fan Guo, Yongkun Li et al. — [gKSM: GPU Memory Deduplication at Driver Layer for Serverless LLM Inference](http://arxiv.org/abs/2610.25219v1)
  <details><summary>📄 Abstract</summary>
  In serverless LLM inference, cloud providers commonly locate multiple instances on a single GPU to improve utilization. However, each instance independently maintains its model weights and runtime state, making duplicate GPU memory the primary bottleneck. Memory deduplication is a widely-used technique for eliminating duplicate data in CPU systems, but extending it to GPU memory faces fundamental challenges. Effective GPU memory deduplication must avoid redundant data movement between CPU and GP...
  </details>

- **2026-10-18** — Haotian Gan, Weidong Tang, Hanbin Sun et al. — [BrandEval: A Two-Track Multi-Agent Benchmark for Risk-Sensitive LLM Crisis Communication](http://arxiv.org/abs/2610.25208v1)
  <details><summary>📄 Abstract</summary>
  Evaluating LLMs for crisis communication requires more than judging isolated responses, because public feedback and competitor actions can reshape trust over time. Existing benchmarks remain largely static and single-turn, offering limited evidence about long-horizon risk-sensitive communication. We introduce \textbf{BrandEval}, a two-track benchmark for product-crisis communication, focusing on public brand responses to product-related safety, quality, service, and trust incidents. BrandEval-St...
  </details>

- **2026-10-18** — Annabelle Sujun Tang, Rohan Mahapatra, Christopher Priebe et al. — [Conjugate Compilation: Self-Improving Agentic Co-Compilation for Speculative Decoding](http://arxiv.org/abs/2610.25012v1)
  <details><summary>📄 Abstract</summary>
  As LLM adoption surges, scaling model serving requires unlocking stranded GPU capacity alongside deploying more GPUs. Speculative decoding brings two models into the serving process: a small draft model proposes tokens that a larger target model verifies. Yet compiling these models individually leaves their shared execution outside the compiler's optimization boundary. We introduce CONJUGATE COMPILATION, which reframes speculative decoding as a cross-model compilation problem and jointly optimiz...
  </details>

- **2026-10-18** — Hanjun Luo, Xuecheng Liu, Xiucheng Zhang et al. — [Over-Defense in Coding Agents Begins at Silent Forks](http://arxiv.org/abs/2610.24949v1)
  <details><summary>📄 Abstract</summary>
  Language models behind coding agents are post-trained with outcome rewards, and recent methods concentrate credit on the turns that decide the outcome. We find that defensive actions beyond what a task requires escape both. They begin at silent forks, the turns where every next action leads to the same outcome. Such actions leave the success rate unchanged, and frontier models take the disproportionate branch there in up to 91% of decisive actions under implicit budgets. The most direct fix, a c...
  </details>

- **2026-10-18** — Yuxiang Lu, Yantong Liu, Jinghua Hou et al. — [TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models](http://arxiv.org/abs/2610.25376v1)
  <details><summary>📄 Abstract</summary>
  Large-scale action pretraining equips Embodied Foundation Models (EFMs) with strong manipulation capabilities, with particular strengths in generalization and closed-loop robustness, but reproducing such pretraining requires substantial robot data and computation. To transfer these capabilities from pretrained EFMs to policies without action pretraining, we introduce TILDE (Teacher-In-the-Loop Distillation from EFMs), which synergizes on-policy distillation at student-induced states with learnin...
  </details>

- **2026-10-18** — Risto Uuk, Santeri Koivula, Lorenzo Pacchiardi et al. — [Assessing the Empirical Evidence for Loss of Control from Agentic General-Purpose AI](http://arxiv.org/abs/2610.25241v1)
  <details><summary>📄 Abstract</summary>
  Theoretical literature warns that advanced generalist agentic systems might pursue instrumental goals that are misaligned with human preferences, thus posing risks of irreversible loss of human control. The EU's Code of Practice for General-Purpose AI lists loss of control as a systemic risk that must be assessed, yet no structured assessment of the quality of the empirical evidence for this risk exists. This study fills that gap. We evaluate 19 recent empirical studies across eight properties i...
  </details>

- **2026-10-18** — Mayank Darbari, Chiman Salavati, Liang Wu et al. — [Mining the Self-Rewriting System: A Vision for Data Mining on AI-Native Infrastructure](http://arxiv.org/abs/2610.25374v1)
  <details><summary>📄 Abstract</summary>
  Classical data mining treats data as generated outside the learner. Emerging AI-native infrastructure invalidates this assumption: as agents observe system state, act, update retrieval stores and models, and promote new artifacts into the serving path, their own decisions reshape the future logs, traces, corpora, and evaluation records used for later training and release. We call this new research object a self-rewriting system and the resulting system-induced distribution shift endogenous drift...
  </details>

- **2026-10-18** — Yanbin Zhao, Zhipeng Chen, Guangsheng Bao et al. — [A Measurement Perspective on Benchmarking LLM-Generated Text Detectors using Item Response Theory](http://arxiv.org/abs/2610.24972v1)
  <details><summary>📄 Abstract</summary>
  Benchmarking large language model (LLM)-generated text detectors commonly relies on aggregate detector-level metrics such as accuracy, F1 score, and AUC. Although useful for summarizing overall performance, these metrics provide limited insight into how benchmark composition shapes detector comparisons or which texts distinguish detectors with different response profiles. We propose a measurement-based benchmarking framework for jointly characterizing benchmark heterogeneity and detector behavio...
  </details>

- **2026-10-17** — Csaba Balogh — [A Symmetry-Matching Approach to Blind-Spot Reduction in Sparse Autoencoders](http://arxiv.org/abs/2610.24908v1)
  <details><summary>📄 Abstract</summary>
  Language models can treat semantically distinct inputs as interchangeable at the representation level, creating blind spots that standard sparse autoencoder (SAE) objectives do not target. In safety-critical settings such as clinical dosage extraction, legal clause interpretation, or financial amount verification, such failures can propagate silently into downstream decisions. We study this problem as one of feature-basis orientation. Building on a symmetry-matching view from algebraic error-det...
  </details>

- **2026-10-17** — Sidra Naveed, Md Shajalal, Gunnar Stevens et al. — [Leveraging Mental Models for Human-Centered Explanations: A Systematic Design Approach Illustrated by Explainable Fake Review Identification](http://arxiv.org/abs/2610.24903v1)
  <details><summary>📄 Abstract</summary>
  Explainable AI (XAI) often prioritizes model fidelity over user intelligibility, yielding explanations that satisfy technical transparency yet fail to support human sense-making. We propose a human-centered approach, MIND-X (Mental-model INtegrated Design for eXplainability), which aligns explanations with users' mental models, commonsense concepts, and judgment heuristics. Using fake review detection as a case study, we contribute: (1) a qualitative study (n=10) that elicits how people assess r...
  </details>

- **2026-10-17** — Parnian Eslamloo, Banani Roy — [RXSynth: A Seed-Grounded Corpus for Studying Java Runtime-Exception Bugs](http://arxiv.org/abs/2610.24902v1)
  <details><summary>📄 Abstract</summary>
  Existing Java bug benchmarks offer limited method-level data for studying runtime-exception detection. Filtering Defects4J, Bugs.jar, Bears, and BugSwarm yields only 170 real buggy/fixed method pairs across seven unchecked exception types. We introduce RXSynth, a corpus of 4,275 synthetic Java method pairs generated from real bug/fix exemplars. We select the generator using structural alignment with real seeds and validate pairs using a two-stage patch-anchored procedure that identifies the labe...
  </details>

- **2026-10-17** — Dimitrios Liakopoulos, Prasoon Sinha, Neeraja J. Yadwadkar — [FlowMaker: From Tasks to Cost-Efficient Generative AI Workflow Deployments](http://arxiv.org/abs/2610.24861v1)
  <details><summary>📄 Abstract</summary>
  Generative AI workflows execute user tasks by composing sequences of LLM calls, where each call performs a sub-task (e.g., summarization or translation), forming a workflow. Executing such workflows requires decisions over workflow structure, model assignments, and deployment configurations, which jointly determine latency, cost, and accuracy under dynamic workloads and resource constraints. Existing systems optimize these decisions in isolation or fix them early, leading to suboptimal cost and ...
  </details>

- **2026-10-17** — Jina Kang, Jeong-Han Yun, Hyesong Choi — [SecODD: Adapting the Operational Design Domain from Driving Autonomy to Autonomous Cyber Defense](http://arxiv.org/abs/2610.24741v1)
  <details><summary>📄 Abstract</summary>
  Security operations centers are beginning to delegate detection, triage, and containment to Autonomous Cyber Defense (ACD) agents at execution time. Erroneous high-impact playbooks can disrupt critical services and create accountability gaps among deployers, SOC supervisors, vendors, managed service providers, and infrastructure providers. We propose SecODD, an execution-time governance framework for ACD that adapts the Operational Design Domain concept from autonomous-vehicle regulation to cybe...
  </details>

- **2026-10-17** — Congjing Zhang, Siyuan Xu, Yunfei Bai et al. — [AgentSoV: Virtual Sensing for LLM Multi-Agent Systems via Stream of Variation](http://arxiv.org/abs/2610.24845v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) multi-agent systems (MASs) solve complex tasks through interacting agents, yet their reliability is difficult to analyze because failures depend on both individual agents and how information and errors propagate across the system. Existing approaches largely treat this as post-hoc failure attribution, but do not provide a common model across heterogeneous MAS architectures or support broader analysis of information influence and observability. We introduce AgentSoV, a ...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 63 papers

- **2026-10-19** — Zhengyue Zhao, Liwei Jiang, Yejin Choi et al. — [Safety Mid-Training: Internalizing LLM Safety as a Foundational Capability](http://arxiv.org/abs/2610.26809v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment for large language models (LLMs) is primarily performed during post-training, while recent work has also begun incorporating safety data into pre-training. Yet safety can degrade when later training no longer includes safety data, and gains in safety often come at the cost of general capability. This tension suggests that safety and general reasoning should not be treated as separate training goals. We instead view safety as an LLM capability that can be learned through a reason...
  </details>

- **2026-10-19** — Alexandre Bismuth, Kang Li, Aramis Marti-Shahandeh et al. — [Adversarial Post-Training of Foundation Models for High-Frequency Trading](http://arxiv.org/abs/2610.25604v1)
  <details><summary>📄 Abstract</summary>
  While autoregressive foundation models trained on limit order book (LOB) data show state-of-the-art performance for market simulation, pre-training with cross-entropy neither penalizes the compounding of sampling errors over free-running rollouts nor targets desired market properties. We introduce a post-training method for LOB foundation models using a Wasserstein generative adversarial network (GAN) objective. A critic, trained online on rollouts through the true, non-differentiable matching e...
  </details>

- **2026-10-19** — Xi Hu, Martin Bell, Liang Zheng — [GenOlympiad: Benchmarking Frontier Image Models at Their Capability Boundaries](http://arxiv.org/abs/2610.26850v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image models have made tremendous progress and can produce high-quality images. However, a question which would be asked in any other discipline is where the frontier models fall short. We introduce GenOlympiad, a benchmark which provides the most challenging text prompts from nine capability axes for stress-testing frontier text-to-image models. The assessed capabilities include generating large quantities, performing deep reasoning, ensuring hard physical consistency, following complex...
  </details>

- **2026-10-19** — Chen Yang, Linzhe Shi, Hang Zhang et al. — [GPT-6 Astra Is a Native Visuo-Tactile Policy for Contact-Rich Manipulation](http://arxiv.org/abs/2610.26846v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multimodal models have enabled GPT-6 Astra to perform robotic manipulation through in-context learning. Yet contact-rich control and tactile perception are often regarded as strengths of specialist policies, leaving open whether Astra can directly understand and use tactile observations. We provide, to our knowledge, the first demonstration that Astra directly interprets vision-based tactile images and uses their contact cues for manipulation. Tactile RGB images enter through ...
  </details>

- **2026-10-19** — Oussema Dhaouadi, Shao Jie Hu-Chen, Jakob Gollreiter et al. — [PlanarCityLoc: Breaking Silhouette Ambiguity in LoD Aerial Localization via 3D Planes](http://arxiv.org/abs/2610.26729v1)
  <details><summary>📄 Abstract</summary>
  Aerial visual localization is crucial for autonomous drone navigation in urban environments where GNSS signals are often degraded. Lightweight textureless Level-of-Detail (LoD) city models provide a geometric map alternative to textured assets. Existing silhouette-based methods rely on image-space alignment, which can leave different camera poses indistinguishable and favor incorrect poses when segmentation errors distort the building outlines. We present PlanarCityLoc, which moves beyond silhou...
  </details>

- **2026-10-19** — Lynn Yi, Zihan Xiong, Junjie Cao et al. — [MuLaCover: Flexible Cover Song Generation via Symbolic Tonal Control](http://arxiv.org/abs/2610.26684v1)
  <details><summary>📄 Abstract</summary>
  A cover song re-renders an existing piece, most commonly by preserving its tonal content -- melody and chord progression -- while reshaping other musical attributes. This suggests a natural formulation for generative cover synthesis with pretrained music language models: explicitly control tonal content, while specifying lyrics and style through text. Existing approaches condition on frame-level features, tightly coupling generation to the reference's timing and structure, and limiting flexibili...
  </details>

- **2026-10-19** — Jiajie He, Yuanhong Jiang, Xintong Chen et al. — [Beyond Behavioral Accuracy: Evaluating Individual-Level Fidelity in LLM Investor Simulation](http://arxiv.org/abs/2610.26524v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as user simulators, but can they faithfully reproduce an individual's behavior and decision logic over time? We investigate this question in a longitudinal paper-trading study with 80 participants. Using rolling next-day predictions, we evaluate trading activity, buy-sell structure, asset selection, and portfolio outcomes, complemented by controlled input ablations and participant-rated explanation alignment. No evaluated LLM reliably outperform...
  </details>

- **2026-10-19** — Kanka Ghosh, Andreas M. Menzel — [Tunable annealing of defects in self-aligning active crystals](http://arxiv.org/abs/2610.26459v1)
  <details><summary>📄 Abstract</summary>
  Obtaining defect-free single-crystals is of crucial importance in soft matter and materials science, spanning both fundamental interests and practical applications. Active crystals, encompassing diverse dense systems from living organisms to artificial metamaterials, can offer a promising platform for autonomous structural reorganization. We demonstrate that increasing spatiotemporal orientational fluctuations around the mean polarized state can enhance crystallographic order in active crystals....
  </details>

- **2026-10-19** — Surya Deep Singh, Ashutosh Tripathi, Gaurav Deep Singh — [StrucChunk: Structure-Aware Retrieval for Legal Document RAG](http://arxiv.org/abs/2610.26313v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) can ground LLM outputs in domain-specific knowledge, but legal documents are hard: standard chunking fragments hierarchical argument structure, and generic embeddings struggle with both precise citation matching and semantic understanding. We propose StrucChunk (Structure Aware Chunking) with hybrid dense-sparse retrieval for hierarchically structured legal documents. It treats documents as directed acyclic graphs of provisions, preserves clause boundaries, r...
  </details>

- **2026-10-19** — Walaa Othman, Baher Mohammad, Stamatios Lefkimmiatis et al. — [SEAM: Spectral Embedding Alignment and Merging for Low-Resource TTS](http://arxiv.org/abs/2610.26252v1)
  <details><summary>📄 Abstract</summary>
  Expanding the vocabulary of conditional text-to-speech (TTS) models typically requires extensive fine-tuning with paired audio, creating a major bottleneck for low-resource and cross-lingual adaptation. To address this, we introduce SEAM, a zero-audio initialization method that constructs embeddings for unseen tokens from known subtokens. Unlike standard pooling strategies that ignore sequential structure, SEAM applies a spectral filter to preserve temporal phonetic order and uses closed-form ri...
  </details>

- **2026-10-19** — Tianle Shen, Fang Yan, Xiaofan Zhang — [SAR2Net: Learning Spatially Anchored Representations for Retrieval-Guided Cross-Stain Alignment](http://arxiv.org/abs/2610.26217v1)
  <details><summary>📄 Abstract</summary>
  Achieving spatial alignment between whole-slide images(WSIs) across stains is essential for integrating morphology and molecular information, yet it remains challenging due to extreme resolution, tissue fragmentation, and large nonlinear deformations. Conventional registration pipelines depend on global pre-alignment and spatial consistency, which often collapse under such distortions. We present SAR2Net, a framework that learns spatially anchored representations and reformulates cross-stain ali...
  </details>

- **2026-10-19** — Wing Yan Li, Zeqiang Wang, Michelle Lin et al. — [Conditional information Retrieval for Longitudinal Survey Harmonisation](http://arxiv.org/abs/2610.26173v1)
  <details><summary>📄 Abstract</summary>
  Identifying conceptually equivalent questions across different surveys is a challenging information retrieval task where surface-level textual similarity is insufficient. Two questions may be lexically similar yet assess entirely different sociological sub-concepts, or lexically different yet conceptually equivalent. We introduce a conditional information retrieval framework that addresses this by decomposing the task into two steps: concept extraction, which identifies the underlying sociologic...
  </details>

- **2026-10-19** — Shuaiqi Cheng, Jiahao Zhang, Boyuan Gu et al. — [TamedFlow: Trajectory-Aware Distillation\\for Teacher-Assisted Diffusion Sampling](http://arxiv.org/abs/2610.26025v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) deliver high-fidelity image and video generation, but inference requires many sequential model evaluations. Two acceleration strategies are increasingly important: model compression makes each evaluation cheaper, while adaptive inference avoids selected teacher computation through reuse, forecasting, or speculative execution. Their combination, however, is brittle: directly applying the evaluated adaptive methods to a compressed student can degrade quality, an obser...
  </details>

- **2026-10-19** — Sebastian Nehrdich, Kengo Harimoto, Sven Sellmer et al. — [MITRA-lexicon: Lexica of attested translations from Sanskrit into English, Tibetan and Chinese](http://arxiv.org/abs/2610.25934v1)
  <details><summary>📄 Abstract</summary>
  The standard Sanskrit lexica are monumental and indispensable, but they cite their attestations as abbreviated references to editions, without links to the digitized texts now widely available and without a translation of the passage, and they naturally do not reflect translations made after them. To address these gaps, we present MITRA-lexicon, a family of corpus-grounded lexica based on span annotations of translation equivalents with Sanskrit as the pivot: Sanskrit-English, derived from the M...
  </details>

- **2026-10-19** — Qifeng Lei, Zhiyong Yang, Zitai Wang et al. — [UtilityBench: Measuring Language Model Utility When Errors Have Different Costs](http://arxiv.org/abs/2610.25924v1)
  <details><summary>📄 Abstract</summary>
  As language models are increasingly deployed in real-world scenarios with important outcomes, the impact of their mistakes often extends far beyond what correctness can capture. In domains like medicine, a single error can lead to serious consequences and put patient safety at risk. However, mainstream evaluation protocols still treat all errors as equal, overlooking the spectrum of real-world costs. To address this, we propose a utility-based evaluation paradigm that explicitly incorporates the...
  </details>

- **2026-10-19** — Tyler Bonnet, Marek Rei — [An Analysis of Semantic and Spatio-Temporal Co-evolution for Edge Classification on Dynamic Text-Attributed Graphs](http://arxiv.org/abs/2610.25906v1)
  <details><summary>📄 Abstract</summary>
  Dynamic edge classification on text-attributed Web graphs, such as review networks, community forums, and news-derived knowledge graphs, requires high quality, adaptive semantic representations in the context of network evolution. Existing dynamic graph architectures typically initialize text feature vectors with pretrained language models and hold them static during training to preserve their semantic structure, forgoing the potential benefits of allowing them to co-evolve with network topology...
  </details>

- **2026-10-19** — Yuankun Xia, Hui Wang, Ling Yuan et al. — [Communication-Efficient Federated Domain Generalization in Edge Networks via Dynamic Prototype Regulation](http://arxiv.org/abs/2610.25810v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) is a distributed paradigm for Internet of Things (IoT) edge networks. However, deploying Vision-Language Models (VLMs) over wireless edge networks presents distinct challenges: large model parameters increase uplink transmission latency over bandwidth-constrained fading channels, and non-independent and identically distributed (Non-IID) data exacerbates client drift. Existing feature alignment solutions often introduce auxiliary computations that consume time slots alloca...
  </details>

- **2026-10-19** — Jianing Wang, Youwen Jian, Derong Wang et al. — [UniJev: Separating Accuracy from Calibration in Trimodal System One Decision Models](http://arxiv.org/abs/2610.25784v1)
  <details><summary>📄 Abstract</summary>
  System One models produce probabilistic judgments that software can consume directly, making reliable confidence as important as answer accuracy. Yet joint training across text, images, and video remains underexplored, and the contributions of supervised fine-tuning (SFT) and reinforcement learning for calibrated decisions (RLCD) are difficult to separate. We introduce UniJev, a trimodal framework that scores candidate answers with a shared head under joint supervised training across text, image...
  </details>

- **2026-10-19** — Jianhao Zhang, Ou Wu, Yi Du — [NADS: Navigator-Guided Data Selection for Mitigating Catastrophic Forgetting in Fine-Tuning](http://arxiv.org/abs/2610.25751v1)
  <details><summary>📄 Abstract</summary>
  Catastrophic forgetting is a central obstacle in single-stage fine-tuning of large language models (LLMs) on a new task, especially when the original pretraining data are unavailable. Synthetic data offers a practical mitigation path, but candidate pools are often noisy and redundant, making effective selection essential. Existing methods often rely on indirect proxy signals whose alignment with actual training benefit can be limited, while utility--diversity selection over large candidate pools...
  </details>

- **2026-10-19** — Tung M. Luu, Tri Ton, Duc M. Nguyen et al. — [Progress-Guided Preference Generation for Aligning Generative Control Policies](http://arxiv.org/abs/2610.25692v1)
  <details><summary>📄 Abstract</summary>
  Generative policies have achieved strong performance in imitation learning tasks, but their success is often constrained by the limited availability of expert demonstrations. Although preference-based fine-tuning can leverage suboptimal rollouts to improve performance, existing approaches heavily rely on expensive human annotations. In this work, we introduce Progress-Guided Preference Generation (PGPG), an unsupervised preference alignment framework that eliminates the need for human-in-the-loo...
  </details>

- **2026-10-19** — Yihui Yang, Yuanhong Yu, Jiawei Wang et al. — [ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation](http://arxiv.org/abs/2610.25690v1)
  <details><summary>📄 Abstract</summary>
  We study language-conditioned local navigation, where a robot must navigate to a text-specified target visible in its initial observation and stop at the described location. End-to-end navigation policies require diverse training data to generalize across scenes, yet real-robot data is costly to collect and simulated data leaves a sim-to-real gap. Internet egocentric videos offer a scalable source of real-world navigation experience. Our key insight is to learn goal-directed visual dynamics from...
  </details>

- **2026-10-19** — Gang He, Zhile Cheng, Kepeng Xu et al. — [Revealing and Bridging the Physical Executability Gap in Vision-Language Navigation](http://arxiv.org/abs/2610.25687v1)
  <details><summary>📄 Abstract</summary>
  Continuous vision-and-language navigation (VLN) is typically evaluated by goal-reaching success, assuming it reflects an agent's ability to execute language-grounded behavior. We show that this assumption can fail: permissive contact models in current simulators may mask physically infeasible actions, creating a physical executability gap between semantic competence and embodied realization. To bridge this gap, we introduce Visual-Semantic Traversability Alignment (VeSTA), a framework that align...
  </details>

- **2026-10-19** — Akash Rao, Sushim Gupta, Vishalini Ramnath et al. — [HyperTaxa: Multiscale Genome Representations for Generalized Microbial Taxonomic Inference](http://arxiv.org/abs/2610.25673v1)
  <details><summary>📄 Abstract</summary>
  Reliable microbial taxonomic inference is challenged by the rapid growth of newly sequenced organisms and incomplete reference coverage. While alignment- and database-driven tools remain essential for reference-backed identification, they are not designed for learned inference over species absent from genome-level training. We introduce HyperTaxa, a taxonomy-aligned representation learning framework for open-set microbial taxonomic inference. HyperTaxa encodes whole genomes as multiscale hypersp...
  </details>

- **2026-10-19** — Tianqi Wei, Zhi Chen, Xin Yu et al. — [Visual Memory and Textual Alignment for Cross-Modal Few-Shot Segmentation](http://arxiv.org/abs/2610.25641v1)
  <details><summary>📄 Abstract</summary>
  Few-shot segmentation (FSS) aims to segment target objects with limited annotated examples. Recent studies have begun to explore large foundation models to improve generalization for this task. In particular, SAM 3 provides strong visual representations and supports text-guided segmentation. However, its performance remains limited in specialized domains, where semantic prompts and visual representations are often poorly aligned. To address this challenge, we propose ViTA-SAM, a framework built ...
  </details>

- **2026-10-19** — Fengfei Yu, Marshall Fisher, Isadora White et al. — [Zephyrus-R1: Agentic Reinforcement Learning for Weather Reporting](http://arxiv.org/abs/2610.25625v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has emerged as a key method for training AI models in scientific applications, but RL remains difficult when outputs cannot easily be verified against a known ground-truth answer. Natural-language weather forecast reports are one such domain: they translate atmospheric data into assessments of weather evolution, hazards, and uncertainty for both the general public and key decision-makers. Unlike numerical weather-analysis questions, they admit many valid outputs, whic...
  </details>

- **2026-10-19** — Afonso Baldo, António Farinhas, Marcos Treviso et al. — [Mitigating Reward Hacking in Preference Reward Models with Evolving Penalties](http://arxiv.org/abs/2610.26496v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for language models has moved from preference reward models to verifiable rewards, which sustain much longer optimization. Preference models are prone to reward hacking: the policy raises their score without improving response quality, or even while degrading it. Yet for open-ended tasks, where quality can neither be verified nor fully written down as rubrics, they remain valuable. We introduce Dynalize, which mitigates reward hacking online, during policy training. Period...
  </details>

- **2026-10-18** — Rajdeep Haldar, Yue Xing, Qifan Song — [Divergence based Ranked Preference Alignment for LLMs](http://arxiv.org/abs/2610.25588v1)
  <details><summary>📄 Abstract</summary>
  Alignment of large language models typically relies on pairwise preference feedback, though ranked feedback can capture more comprehensive information across multiple responses within a single annotation. However, ranked-preference alignment is underexplored in practice compared to simpler pairwise approaches, potentially resulting in suboptimal behavior. Concurrently, recent research has conceptualized large language model alignment objectives as divergence estimators between aligned (preferred...
  </details>

- **2026-10-18** — Yang Hong, Lei Zhang, Zhihong Liu et al. — [SlimFormer++: Token Mixing Where It Matters for Efficient 3D Medical Image Segmentation](http://arxiv.org/abs/2610.25488v1)
  <details><summary>📄 Abstract</summary>
  To determine where computation is needed in volumetric segmentation networks, we analyze block-level redundancy and stage-wise token-mixer contribution. Centered Kernel Alignment reveals high input-output representational similarity within blocks of representative convolutional, hybrid, and Transformer-style segmentation networks. Similarity-guided pruning reduces their parameter counts by 39-75% while decreasing mean Dice by less than 0.4 percentage points. To examine token mixers within blocks...
  </details>

- **2026-10-18** — Shashwat Singh, He He, Tal Linzen — [A failure of Imagination: VLMs fail to use visual representations for text, but self-distillation can help](http://arxiv.org/abs/2610.25470v1)
  <details><summary>📄 Abstract</summary>
  Vision-language (VL) models are typically built by fine-tuning a language model to attend to visual features in service of a Visual Question-Answering objective. We ask whether this alignment changes how language models represent text---especially on tasks where visualization would help, like geometry questions posed in words. We distinguish weak multimodality (the model can answer questions about an input image) from strong multimodality (the model's text representations themselves become visio...
  </details>

- **2026-10-18** — Zhiyu Zheng — [More Mentions, Less Information? Diagnosing Identity and Alignment in Reddit Embeddings for Volatility Forecasting](http://arxiv.org/abs/2610.25468v1)
  <details><summary>📄 Abstract</summary>
  Since the 2021 GameStop short squeeze, r/WallStreetBets (WSB) has been associated with episodes of extreme volatility, and its text is increasingly used to forecast volatility. A model using only large language model (LLM) embeddings of WSB posts attains an out-of-sample $R^2$ of 0.13 for log realized variance. That number shows predictive power, but it does not reveal where the information comes from or how much the text adds beyond a firm's own volatility history. We answer these questions wit...
  </details>

- **2026-10-18** — Eli A. Underwood, I. Taylor McKechnie, Leslie M. Collins — [Preserving the Manifold: Frozen Expert Alignment for Label-Efficient SAR Scene Understanding](http://arxiv.org/abs/2610.25429v1)
  <details><summary>📄 Abstract</summary>
  Cross-modal alignment of synthetic aperture radar (SAR) imagery to natural language is constrained by two distinct failures. The first is modality mismatch: text encoders pre-trained on optical imagery, such as CLIP, cannot be efficiently fine-tuned on SAR, because active microwave backscatter is physically incompatible with passive optical reflectance and the available SAR caption datasets are orders of magnitude too small to bridge this gap without substantially degrading the learned semantic ...
  </details>

- **2026-10-18** — Shuochen Chang, Bingjie Gao, Qingyang Liu et al. — [From Label Priors to Task Evidence: Efficient Long-Video Frame Selection via Bayesian GRPO](http://arxiv.org/abs/2610.25418v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) face significant scalability challenges in long-video understanding due to quadratic attention complexity and context window constraints. Existing retrieval-based approaches typically rely on supervised learning from static keyframe annotations. However, these label priors often fail to align with the actual information required by downstream MLLMs for complex reasoning, creating a misalignment between the training target and inference needs. To bridge th...
  </details>

- **2026-10-18** — Cheonbok Park, Jihwan Kim, Shinyoung Joo et al. — [From Unverifiable Domain Text to Cross-Lingual RLVR via Code-Switched Task Synthesis](http://arxiv.org/abs/2610.25399v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning with Verifiable Rewards (RLVR) can improve reasoning in large language models, but specialized non-English domains expose a data mismatch. Raw English domain text is often available, while target-language RLVR tasks with verifiable rewards are scarce. We introduce code-switched task synthesis for cross-lingual RLVR, a data-centric approach that derives target-language and code-switched RLVR task variants from otherwise unverifiable English domain text. Using fill-in-the-mi...
  </details>

- **2026-10-18** — Junhong Liang, Daniil Orel, Saeed Almheiri et al. — [Aligning Cultural Behaviors in Arabic Language Models via Preferences](http://arxiv.org/abs/2610.25362v1)
  <details><summary>📄 Abstract</summary>
  Arabic LLMs have improved rapidly, but aligning them with country-specific cultural behavioral preferences remains underexplored. Previous work has focused primarily on instruction-tuning for factual knowledge, overlooking nuanced cultural behaviors. We propose ArabPref, which to our knowledge is the first large-scale pan-Arab preference data set for the alignment of cultural behavior conditioned on the country. Our contribution includes two resources in English and Modern Standard Arabic: a cul...
  </details>

- **2026-10-18** — Bi-Cheng Yan, Jhih-Rong Guo, Fu-An Chao et al. — [Probing and Mitigating Hallucinations in Speech-augmented Language Models for Automatic Speech Recognition via Small Language Models](http://arxiv.org/abs/2610.25351v1)
  <details><summary>📄 Abstract</summary>
  The widespread success of large language models in natural language processing has spurred the development of speech-augmented language models (SLMs) to extend their reasoning capabilities from textual inputs to spoken ones. Despite impressive performance, SLMs remain susceptible to hallucinations, posing challenges in practical utility. To this end, we first probe hallucinations in SLMs for automatic speech recognition (ASR) via the lens of causal mediation and behavioral analysis. To mitigate ...
  </details>

- **2026-10-18** — Yonatan Gideoni, Yoav Gelberg, Tim G. J. Rudner et al. — [Persistent Representational Misalignment Induces Vision-Language Model Failures](http://arxiv.org/abs/2610.25252v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) fail at some tasks that are simple for humans---but why? We hypothesize that many such failures stem from VLMs' difficulties translating between vision and language representations, a misalignment the Platonic Representation Hypothesis predicts should disappear with scale. This paper is composed of two parts: in the first, we show that existing vision and language representations are linearly unalignable. This misalignment is an inherent property of the data and hen...
  </details>

- **2026-10-18** — Sunghoon Kim, Sangyeop Kim — [Beyond Factual Accuracy: A Benchmark for Evaluating Perspective Alignment in LLMs](http://arxiv.org/abs/2610.25087v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models often generate factually correct responses that fail to maintain user-requested perspectives, blending multiple perspectives and forcing users to filter through unwanted information---a perspective control failure that factual accuracy metrics cannot detect. We introduce PerspectiveBench, a benchmark quantifying perspective alignment by constructing scenarios where multiple valid reasoning paths coexist, and propose the Perspective Alignment Score (PAS) to measure adherence...
  </details>

- **2026-10-18** — Jiaqi Su, Guibin Zhang, Jie-Jing Shao et al. — [CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?](http://arxiv.org/abs/2610.25078v1)
  <details><summary>📄 Abstract</summary>
  Model--harness co-evolution has emerged as a prominent paradigm for recursive self-improving (RSI) agents, jointly evolving their execution scaffolds and intrinsic capabilities. We study the persistent yet often overlooked brain--body mismatch problem in this paradigm, where an evolving harness (body) demands behaviors its model (brain) has not learned or restricts capabilities it already possesses. We introduce CoEvo-RSI, a RSI framework that advances model--harness co-evolution through agent-d...
  </details>

- **2026-10-17** — Junwei Ma, Arun Kumar Chithanar, Palash Goyal et al. — [Table Serialization Determines Which Relations Language Models Preserve](http://arxiv.org/abs/2610.24798v1)
  <details><summary>📄 Abstract</summary>
  We study how text serialization affects table lookup in instruction-tuned language models. Our diagnostic asks the model to find the row containing a specified value under one named column, then return the value under another named column in that same row. We render the same synthetic 256-cell tables in row-major form and in column-major form with each header placed beside its values, while varying the table aspect ratio across five shapes. Across three models, the better format changes with tab...
  </details>

- **2026-10-17** — Xuchao Ren, Siyuan Feng, Jing Huang et al. — [Design Anything, Design at Scale](http://arxiv.org/abs/2610.24771v1)
  <details><summary>📄 Abstract</summary>
  As multimodal resources are transformed into media outputs, agentic AI is expected to stay aligned with design intent over long horizons. Designers follow briefs specifying goals, constraints, and deliverables, with later work building on earlier decisions. Recent work reuses design experience across tasks, yet alignment among artifacts within one project remains challenging. Agents therefore need to preserve and apply this intent across domains and as projects grow. We introduce Design Anything...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 66 papers

- **2026-10-19** — Durgam Latha, Dion Reji, Dorde Zikelic et al. — [Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games](http://arxiv.org/abs/2610.26568v1)
  <details><summary>📄 Abstract</summary>
  Robust partially observable Markov decision processes model agents that act under partial observability while adversarial environment resolves uncertainty in the transition probabilities. Reward objectives such as discounted-sum, long-run average and cumulative reward under finite and infinite horizons allow quantifying the utility of an agent. We consider the problem of solving RPOMDPs under all four reward objectives, where the goal is to decide whether the value of a risk measure with respect...
  </details>

- **2026-10-19** — Zehao Wang, Jianpeng Yao, Yuping Wang et al. — [CoopUQ: Robust Multi-Robot Social Navigation via Uncertainty-Aware Cooperative Forecasting](http://arxiv.org/abs/2610.26852v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning enables mobile robots to make fast and scalable navigation decisions in constrained human-shared environments. However, directly extending single-robot approaches to multi-robot settings often fails to ensure safety and efficiency, especially under occlusions and out-of-distribution (OOD) scenarios, where individual robots may overlook potential risks or make inaccurate predictions. Leveraging cooperation effectively for both prediction and navigation remains a major chall...
  </details>

- **2026-10-19** — Zhaoyang Wang, Qianhui Wu, Haorui Wang et al. — [Agent World Model in the Wild: Computer-Use Agent Environment Synthesis](http://arxiv.org/abs/2610.26828v1)
  <details><summary>📄 Abstract</summary>
  Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model in the Wild (WildAWM), a scalable pipeline for synthesizing controllable environments and tasks for training general computer-use agents (CUAs). Whereas existing approaches typically specialize in a single agent interact...
  </details>

- **2026-10-19** — Xu Yang, Zhanyuan Sheng, Chenhui Lin et al. — [PhyPro-FM: A Physics and Prompt-Guided Graph Foundation Model for Contingency Analysis](http://arxiv.org/abs/2610.26351v1)
  <details><summary>📄 Abstract</summary>
  The continuous evolution of next-generation power systems, characterized by the high penetration of renewable energy resources and dynamic topology variations, poses formidable challenges to traditional N-1/N-2 contingency analysis in terms of computational efficiency and scalability. While deep learning-based methods offer accelerated inference, existing studies predominantly treat contingency analysis as a pure regression problem, often overlooking the physical essence of grid operation and en...
  </details>

- **2026-10-19** — Xiang Wang, Zhaoxiang Liu, Xiang Chen et al. — [VISAGENT: An Agent-Based End-to-End Voice Interaction System](http://arxiv.org/abs/2610.26168v1)
  <details><summary>📄 Abstract</summary>
  Voice-based public services have evolved from manual switchboards to intelligent platforms to meet modern user needs. However, current systems remain constrained by rigid menu-driven interaction, fragmented vertical services, and limited extensibility. To address these issues, we present VISAGENT, an agent-based end-to-end voice interaction system for large-scale public services that integrates end-to-end speech interaction, hierarchical agent routing, a scalable voice-agent marketplace, and use...
  </details>

- **2026-10-19** — Jiaxuan Sun, Biao Wang, Shuai Li — [FrameGRPO: Incentivizing Video Reasoning via Multi-Frame Rollouts and Temporal Credit](http://arxiv.org/abs/2610.26022v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards, particularly Group Relative Policy Optimization (GRPO), has improved video reasoning in multimodal large language models. However, standard video GRPO varies only linguistic trajectories while conditioning every rollout in a group on the same sampled frames, which can produce homogeneous rewards and weaken group-relative learning when the shared visual evidence is insufficient or distracting. We propose \textbf{FrameGRPO}, a simple and effective re...
  </details>

- **2026-10-19** — Yusuke Watanabe, Yohei Kobashi, Taisei Tosaki et al. — [When to Stop Asking: Factor Coverage Bias and LLM Determinability Judgments with Underspecified Information in Medicine](http://arxiv.org/abs/2610.25819v1)
  <details><summary>📄 Abstract</summary>
  Clinical decision-making often begins with underspecified information and requires not only gathering missing information but also knowing when to stop. This calls for judging determinability (whether the available information is sufficient for a decision) by considering whether missing information could change the conclusion, not simply the amount of available decision-relevant information. Reliance on this amount as a cue for determinability, which we term \textit{factor coverage bias}, could ...
  </details>

- **2026-10-19** — Seungjong Sun, Hyunmin Jun, Minsik Yoon et al. — [No Matter Who You Are: Addressivity and Sycophancy in Large Language Models](http://arxiv.org/abs/2610.25728v1)
  <details><summary>📄 Abstract</summary>
  Sycophancy, where an LLM becomes overly agreeable, deferential, or flattering toward the user, has been identified as a major failure mode. While post-training has been implicated as a cause, how it internally gives rise to sycophantic behavior remains insufficiently understood. Post-training transforms the model's output from text completion into utterances directed toward an addressee, thereby giving the output \textit{addressivity}. We hypothesize that the accompanying pressure to follow the ...
  </details>

- **2026-10-19** — Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi — [Robot Learning with Vision-Language-Action Models for Agricultural Manipulation](http://arxiv.org/abs/2610.26717v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation in agricultural environments remains challenging due to variations in plant geometry, occlusion, and camera viewpoints. Pretrained vision-language-action (VLA) and generalist robot policies offer a promising approach to addressing these challenges by learning manipulation behaviors from multimodal observations and language instructions. However, adapting these policies to agricultural tasks requires domain-specific demonstrations, which are costly and time-consuming to colle...
  </details>

- **2026-10-19** — Chao Yu, Shu'ang Yu, Hao Lin et al. — [Learning from Fleet Experience: A Collective Learning Paradigm for Robots](http://arxiv.org/abs/2610.25736v1)
  <details><summary>📄 Abstract</summary>
  Experience generated during deployment offers an opportunity for robots to improve policy reliability through learning from their own executions. However, learning through human corrections requires teleoperators to monitor execution and intervene when policies fail, a demand that is difficult to meet as robot fleets grow. We introduce collective experience learning (CEL), a learning paradigm in which deployed robots share their execution experience to improve a common policy. We realize CEL thr...
  </details>

- **2026-10-19** — Santosh Parit, Julia Hindel, Rohit Mohan et al. — [Real-Time Radar Semantic and Panoptic Scene Understanding](http://arxiv.org/abs/2610.26816v1)
  <details><summary>📄 Abstract</summary>
  Robust scene understanding under varying environmental conditions is essential for safe autonomous driving. While cameras and LiDAR degrade in adverse weather and poor lighting, Frequency-Modulated Continuous-Wave (FMCW) spinning radar provides dependable 360° perception at extended ranges with minimal compute cost. However, real-time FMCW radar scene understanding is challenging due to complex signal returns, limited temporal resolution, and scarce annotated datasets. We introduce StreamRPS, a ...
  </details>

- **2026-10-19** — Wenhao Zhang, Zhongliang Zhou, Yi Ping et al. — [What Language Adds, and at What Cost: Four Controlled Probes of Pathology Vision-Language Models](http://arxiv.org/abs/2610.26805v1)
  <details><summary>📄 Abstract</summary>
  Vision--language models (VLMs) promise to make computational pathology queryable and able to draft reports, but how much language adds beyond the vision backbone is unclear, because almost every system is evaluated by its developers on test sets of their own choosing. We grade published evidence by how it was produced and test four claims with controlled probes that reuse released checkpoints and public data, varying one input at a time. Report text adds prognostic signal: adding a frozen embedd...
  </details>

- **2026-10-19** — Steven Motta, Davide Mambelli, Alessandro Rozza — [Topological Sheaves of Irreducibility: A Theoretical Framework for Multi-Agent Task Obstructions](http://arxiv.org/abs/2610.26777v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems can differ under identical agents and communication budgets when they support different forms of joint interaction. We introduce Topological Sheaves of Irreducibility (TSI), a sheaf-theoretic framework separating task-level compatibility obstructions from system capability. A task is represented by an interaction complex $K$ and a capacity sheaf $\mathcal{F}$; nonzero $H^n(K;\mathcal{F})$ defines a structural signature, while registered interventions test capability. For cocy...
  </details>

- **2026-10-19** — Praroop Chanda, Suryansh Kumar — [Foundation Model Driven Optical Flow](http://arxiv.org/abs/2610.26690v1)
  <details><summary>📄 Abstract</summary>
  We investigate how frozen pretrained visual and depth representations support dense optical flow when coupled with a supervised matching network. Building on TTSFlow, this paper studies Dense Prediction Transformer (DPT) feature decoding and one coarse-to-fine refinement stage. Our method fuses features from frozen DINOv2 and Depth Anything V2 models and estimates optical flow through a trainable transformer-based matching pipeline. After optical-flow training on FlyingChairs and FlyingThings3D,...
  </details>

- **2026-10-19** — Hairuo Wei, Yunfan Ren, Renda Yang et al. — [Learning Wheel Motion Uncertainty for Degeneracy-Aware LiDAR-Inertial Odometry on Quadrupedal Wheel-Legged Robots](http://arxiv.org/abs/2610.26550v1)
  <details><summary>📄 Abstract</summary>
  Wheel kinematics can support odometry for quadrupedal wheel-legged robots when LiDAR geometry provides weak motion constraints. However, slip and contact loss make rolling predictions unreliable, and contact state alone cannot determine their reliability across motion directions. We propose a tightly coupled LiDAR-inertial-kinematic odometry framework that retains analytical rolling predictions and learns per-wheel, direction-dependent process covariances from proprioceptive history. The estimat...
  </details>

- **2026-10-19** — Ridouane Ghermi, Vicky Kalogeiton, Ivan Laptev — [From Cause to Effect: Generating Intermediate Event Chains in Videos](http://arxiv.org/abs/2610.26275v1)
  <details><summary>📄 Abstract</summary>
  Video-Language Models (VLMs) excel at visual recognition but struggle with causal reasoning. Current evaluations are flawed: multiple-choice QA allows shortcuts, and open-ended QA lacks robust automatic evaluation. We introduce Causal Chain Generation (CCG), a novel task where models have to generate the sequence of intermediate events connecting a cause and an effect. This structured setup demands genuine reasoning and enables reliable automatic scoring. We accompany this task with two compleme...
  </details>

- **2026-10-19** — Jiuzhou Han, Abhishek Bijay Mishra, Trevor Cohn et al. — [DeepSEA: A Multilingual Evaluation Benchmark for Southeast Asia](http://arxiv.org/abs/2610.26155v1)
  <details><summary>📄 Abstract</summary>
  While language models have demonstrated remarkable capabilities, their performance remains disproportionately skewed towards high-resource languages. This disparity is particularly acute for the 700 million inhabitants of Southeast Asia, where vast linguistic diversity remains under-represented in existing benchmarks, often suffering from limited language coverage or narrow task scopes. To address this, we introduce DeepSEA, a comprehensive benchmark constructed from established datasets through...
  </details>

- **2026-10-19** — Abhinav Khattar, Aishwarya Chhabra, Ameya Velingker et al. — [Scaling Synthetic Pre-training Data and Evaluation for Indic LLMs](http://arxiv.org/abs/2610.26006v1)
  <details><summary>📄 Abstract</summary>
  Building capable language models for India requires scalable multilingual data and robust evaluation. We introduce Nemotron-Pretraining-Indic-v1, a synthetic pretraining corpus of approximately 2.83 trillion tokens covering all 22 scheduled Indian languages in native script and twelve in romanized form. It is the largest openly released Indic pretraining corpus. Using our GPU-accelerated pipeline, we translate curated English documents, assess translation quality, and repair low-quality outputs ...
  </details>

- **2026-10-19** — Alessandro Cagiano, M. Aybars Seyhan, Fabiola Gangi et al. — [Scenario Generalization and Sector Transfer in Real Surface Irrigation Surrogate Modelling with Tabular Models](http://arxiv.org/abs/2610.26005v1)
  <details><summary>📄 Abstract</summary>
  Surface irrigation planning requires screening many operating conditions and spatial configurations, while high-fidelity shallow-water-equation (SWE) simulations are expensive. We study tabular surrogate models for predicting maximum water height from drone-derived field morphology, terrain, hydrological, spatial, and scenario descriptors, where each row represents a spatial cell under one irrigation scenario. To assess deployment feasibility, we evaluate gradient-boosted trees, neural tabular m...
  </details>

- **2026-10-19** — Ziyi Zhang, Ziyao Wang, Guoheng Sun et al. — [Auditor-Assisted Summary-Channel Verification for Hosted LLM Identity Substitution](http://arxiv.org/abs/2610.25982v1)
  <details><summary>📄 Abstract</summary>
  Hosted LLM services increasingly expose model identity as a product claim, but external users and auditors often cannot inspect which model configuration served a request. We study an auditor-assisted regime in which a trusted auditor enrolls claimed identities and prepares verification material before deployment, while audit-time verification uses only the claimed identity and released output, without runtime access to model internals, inference logs, routing decisions, or provider metadata. We...
  </details>

- **2026-10-19** — X. Feng, J. Tang, Z. Lin et al. — [EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models](http://arxiv.org/abs/2610.25959v1)
  <details><summary>📄 Abstract</summary>
  Building embodied agents that can perceive, reason, and act across diverse 3D worlds is a central research direction toward artificial general intelligence. Yet most existing work remains confined to specific tasks in a single scene and transfers poorly to new environments, leaving general embodied agents for open-world settings under-explored. We refer to such agents as Embodied World Agents (EWAs), whose defining property is the ability to understand diverse visual environments and execute gen...
  </details>

- **2026-10-19** — Matthias Eder, Pantelis Emmanouil, Vivek Farias et al. — [Policy Search in Code Space for Multi-Agent Pathfinding](http://arxiv.org/abs/2610.25946v1)
  <details><summary>📄 Abstract</summary>
  Developing coordination policies for complex multi-agent systems relies on either labor-intensive algorithm design or opaque task-specific reinforcement learning. With recent advances in autonomous coding agents, we show that policy search directly in code space offers a compelling third path that combines automated optimization with explicit interpretability. We investigate a human-directed workflow in which coding agents iteratively propose, implement, evaluate, diagnose, and eventually refine...
  </details>

- **2026-10-19** — Yizhou Yang, Jiahong Fu, Zhiwu Wang et al. — [FisherEdit: Fisher Information Guided Knowledge Editing for Large Language Models](http://arxiv.org/abs/2610.25914v1)
  <details><summary>📄 Abstract</summary>
  Sequential knowledge editing in Large Language Models (LLMs) often leads to a degradation of general capabilities due to cumulative parameter interference. In this paper, we revisit prominent projection-based methods like AlphaEdit and reveal a surprising mismatch: their robustness is primarily driven by update regularization rather than the intended null-space projection. Based on this insight, we propose FisherEdit, a theoretically grounded method built on Fisher geometry, which replaces coars...
  </details>

- **2026-10-19** — Jinze Li, Weijie Liu, Jinfeng Xu et al. — [SWE-Residual: Evaluating Starting-State Robustness of Coding Agents](http://arxiv.org/abs/2610.25899v1)
  <details><summary>📄 Abstract</summary>
  Software engineering (SWE) benchmarks are the primary way to measure the capabilities of coding agents: an agent is placed in a code repository or machine environment, given a request, and judged by hidden tests. These benchmarks almost always start the agent from a clean state that contains no earlier work on the task. In practice, however, agents often continue work that a developer or another agent has already done and reported as complete, with no indication of what remains incorrect or miss...
  </details>

- **2026-10-19** — Chunjiang He, Zheng Zi, Bingshen Mu et al. — [MS-Bench: A Condition-Stratified Multi-Speaker ASR Benchmark](http://arxiv.org/abs/2610.25824v1)
  <details><summary>📄 Abstract</summary>
  Multi-speaker automatic speech recognition (MSASR) has advanced rapidly with end-to-end speech large language models. However, existing benchmarks cover limited ranges of specific multi-speaker conditions and scenarios, making it difficult to reveal system limitations under diverse conditions and scenarios. We introduce MS-Bench\footnote{\href{https://aslp-lab.github.io/MS-Bench/}{Demo page: https://aslp-lab.github.io/MS-Bench/}}, a condition-stratified benchmark for fine-grained MSASR evaluatio...
  </details>

- **2026-10-19** — Yuyan Zou, Luke G. Bennetts, Hailong Guo — [Mixed Unfitted finite element approximation of band structures in photonic crystals](http://arxiv.org/abs/2610.25598v1)
  <details><summary>📄 Abstract</summary>
  Photonic crystals are periodic dielectric structures whose optical properties are characterized by Maxwell eigenvalue problems with discontinuous material coefficients. For arbitrarily shaped inclusions, their numerical solution remains challenging due to costly mesh generation and remeshing as the geometry changes. In this paper, we address this challenge by developing a mixed unfitted finite element method based on the Floquet-Bloch transform. Our method uses a uniform background mesh independ...
  </details>

- **2026-10-18** — Immanuel R. Santjoko, Benedictus C. G. Cinun, Jing Chen et al. — [Learning When to Adapt: Reactivity-Conditioned Residual Adaptation under Human-Robot Distribution Shift](http://arxiv.org/abs/2610.25419v1)
  <details><summary>📄 Abstract</summary>
  Pedestrians differ in whether they respond to a robot, yet many RL policies assume all are non-reactive to prioritize safety. Policies trained without conditioning on local pedestrians' reactivity may therefore be unnecessarily conservative or rely on cooperation that does not occur. We propose RCRA, an online adaptation framework that modulates a learned residual around a frozen conservative navigation policy according to estimated pedestrian reactivity. A Transformer-based estimator infers lat...
  </details>

- **2026-10-18** — Jingrui Wu, Wangyun Dan — [Synergy-Aware Residual Flow Matching for Single-Cell Perturbation Prediction](http://arxiv.org/abs/2610.25021v1)
  <details><summary>📄 Abstract</summary>
  Predicting single-cell responses to genetic and chemical perturbations is important for understanding regulatory mechanisms and prioritizing therapeutic interventions. Existing methods have made progress by modeling perturbation-conditioned expression shifts with neural networks, graph priors, foundation-model representations, or distributional generative models. However, combinatorial perturbation prediction remains challenging because much of the response can be explained by additive single-pe...
  </details>

- **2026-10-18** — Yunbei Zhang, Janet Wang, Xi Xiao et al. — [UtoMe: Observation-Uncertainty-Guided Token Merging for Weather Foundation Models](http://arxiv.org/abs/2610.25001v1)
  <details><summary>📄 Abstract</summary>
  Weather transformers process dense reanalysis fields whose reliability varies across variables, locations, and weather regimes. Token merging can reduce computation, but feature similarity alone does not account for this heterogeneous input uncertainty. We introduce UtoMe, an observation-uncertainty-guided token merging framework that combines dynamics saliency with ensemble data assimilation spread as a relative input-reliability proxy. The resulting importance score protects selected tokens as...
  </details>

- **2026-10-18** — Chuan Liu, Tianya Zhao, Xuyu Wang — [TrustAgent-RFF: Agentic Diagnostic Planning for Reliable RF Fingerprinting under Domain Shift](http://arxiv.org/abs/2610.24930v1)
  <details><summary>📄 Abstract</summary>
  Radio frequency fingerprinting (RFF) models can achieve accuracy under source domain conditions but become unreliable when the receiver, distance, collection day, or environment changes. Incorrect predictions in unseen domains may receive high softmax confidence, making confidence thresholding insufficient for trustworthy deployment. We propose TrustAgent-RFF, a prediction level reliability framework for RFF that operates with a frozen in-phase and quadrature (I/Q) classifier without target doma...
  </details>

- **2026-10-18** — Tomer Garber, Tom Tirer — [Enhanced Masked Diffusion Unlearning](http://arxiv.org/abs/2610.25447v1)
  <details><summary>📄 Abstract</summary>
  Masked diffusion language models (MDLMs) generate text by iteratively unmasking tokens with bidirectional context. As these models reach real-world deployment, machine unlearning becomes essential. This process aims to remove the influence of a designated "forget set" without retraining from scratch, so that sensitive, copyrighted, or restricted content can no longer be elicited while preserving retained capabilities. Masked Diffusion Unlearning (MDU) is the first publicly available unlearning m...
  </details>

- **2026-10-18** — Weiwei Hu, Rongjie Lai, Ziqian Li — [Self-Supervised In-Context Operator Learning for Optimal Mixing in Incompressible Flows](http://arxiv.org/abs/2610.25556v1)
  <details><summary>📄 Abstract</summary>
  We develop a self-supervised operator-learning framework for optimal mixing in incompressible flows, aimed at overcoming the computational limitations of classical PDE-constrained optimal control. The objective is to design velocity fields that efficiently homogenize a passive scalar while minimizing kinetic energy, quantified through the $\dot H^{-1}(Ω)$ mix-norm. Classical methods solve a separate optimal control problem for each initial condition using iterative forward-adjoint procedures, le...
  </details>

- **2026-10-18** — Mobina Kashaniyan, Ali Jannesari — [ATEST: Adaptive Resource-Aware Test-Time Scaling for LLM Inference](http://arxiv.org/abs/2610.25519v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling (TTS) improves large language model (LLM) reasoning by sampling multiple answers, but fixed sampling budgets ignore both query difficulty and the changing energy cost of inference under GPU contention. We measure up to a 4.1-fold increase in energy for the same four-sample query as GPU load rises. We present ATEST, a resource-aware TTS framework that jointly considers the expected value of additional samples and their current GPU cost. ATEST-Online, its default mode, requires n...
  </details>

- **2026-10-18** — Chao Tian, Krishna Narayanan — [From Formulation to Articulation: Considerations for AI-Assisted Research in Information Theory](http://arxiv.org/abs/2610.25490v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in artificial intelligence have contributed to several information-theoretic results through genuinely different modes: a language model may suggest a proof, participate in an extended mathematical dialogue, coordinate computation, or operate as one component of a search harness. Treating all of these as "AI-discovered mathematics" obscures distinctions that matter for scientific reliability, attribution, and reproducibility. This article examines a set of recent cases through a ...
  </details>

- **2026-10-18** — Xuyuan Liu, Xinshuai Dong, Elynn Chen et al. — [When Form Changes but Logic Doesn't: Building Logic-invariant LLMs through Logical Structure](http://arxiv.org/abs/2610.25402v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have achieved strong performance across diverse reasoning tasks, yet it remains unclear whether this performance reflects an understanding of underlying logical structure or a reliance on shallow semantic cues. A key indicator of such understanding is whether models treat logically equivalent inputs consistently, producing the same predictions despite differences in expression. Through systematic evaluation on curated data, we show that even strong LLMs often fail th...
  </details>

- **2026-10-18** — Jingru Fei, Wei Fan, Kun Yi et al. — [Paloma: Phase-Conditioned Residual Modulation for Time Series Forecasting](http://arxiv.org/abs/2610.25392v1)
  <details><summary>📄 Abstract</summary>
  Explicitly modeling periodicity has proven to be an efficient approach for time series forecasting, where the residual, obtained after removing the periodic component from the time series, is typically treated as unstructured noise. However, in this work, we show that such residuals still exhibit structured, \textit{phase-dependent} deviations, as supported by both empirical observations and theoretical analysis. This suggests that residuals should not be treated merely as unstructured noise, bu...
  </details>

- **2026-10-18** — Yuchen Xi, Yuhan Guo, Chenwei Hou et al. — [GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation](http://arxiv.org/abs/2610.25245v1)
  <details><summary>📄 Abstract</summary>
  Novel view synthesis under trajectory changes is essential for autonomous driving simulation, yet existing methods struggle to generate consistent videos when extrapolating to unseen viewpoints such as lane shifts. Reconstruction-based approaches maintain geometric consistency but degrade in visual quality under large viewpoint changes, while reconstruct-then-restore methods often produce visually plausible frames yet suffer from geometric and temporal inconsistencies. We present GeoV2V, a geome...
  </details>

- **2026-10-18** — Haotian Gan, Yudong Li, Xintian Li et al. — [ViCoR: Estimating Visual Necessity via Counterfactual Residuals for Multimodal Medical Data Selection](http://arxiv.org/abs/2610.25202v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language models often exhibit hidden stratification, where high overall performance masks failures on subtle visual findings and overlapping clinical conditions. We trace this failure mode to modality imbalance during fine-tuning, where strong linguistic priors can suppress visually grounded learning and induce plausible but weakly grounded rationales. Existing data selection methods usually score image-text pairs as holistic units, without separating visually necessary samples fr...
  </details>

- **2026-10-18** — Shantipriya Parida, Debasish Dhal, Sonal Khosla et al. — [Acharya 2.0: An AI Tutor for Self-Learning Subjects in Hindi](http://arxiv.org/abs/2610.25192v1)
  <details><summary>📄 Abstract</summary>
  Text processing is crucial for low-resource languages as it enables the development of tools and technologies that bridge the digital divide and provide equitable access to information and services. By empowering low-resource languages with robust text processing, we can preserve linguistic diversity, enhance education, improve communi- cation, and foster inclusivity in a rapidly digitizing world. Due to the lack of sufficient annotated datasets and lin- guistic resources, it is challenging to d...
  </details>

- **2026-10-18** — Lahiru Wijayasingha — [Sufficient Frame Subsets for Video Understanding](http://arxiv.org/abs/2610.25084v1)
  <details><summary>📄 Abstract</summary>
  Understanding when during a video a model makes its critical observations is essential for interpreting video-understanding systems. However, existing attribution methods often spread evidence diffusely across near-duplicate frames. We introduce Sufficient Frame Subsets: compact sets of frames in which all other frames are masked, yet each subset independently preserves the model's prediction. We evaluate our method on two complementary benchmarks, UCF101 and Something-Something v2, using both C...
  </details>

- **2026-10-18** — Shenqi Zhou, Qiran Zou, Wenhao Zhao et al. — [Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks](http://arxiv.org/abs/2610.25069v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are increasingly capable of developing machine learning (ML) models end to end. In medical practice, however, strong performance on the target metric does not fully characterize how good the models are in real-world use cases. For example, medical ML models should also provide well-calibrated risk estimates and remain robust across patient populations. Yet autonomous model development is typically guided by task objectives that emphasize simple predictive discrimination (e.g. A...
  </details>

- **2026-10-17** — Jacob Abaare, Bianca Ianetta, Cedric Nimpa Fondje et al. — [VTF900: A 900-Subject Visible-Thermal Face Recognition Dataset and Benchmark](http://arxiv.org/abs/2610.24832v1)
  <details><summary>📄 Abstract</summary>
  Despite advancements in visible-thermal face recognition, where thermal probe (query) face images are matched against visible enrollment templates, existing benchmarks are currently limited by small gallery sizes (N $\approx$ 100 subjects). This limitation inhibits the ability to accurately evaluate visible-thermal facial recognition at scale and to report significant recognition performance metrics, which have better operational relevance. Therefore, we introduce VTF900, a large-scale visible-t...
  </details>

- **2026-10-17** — Renxi Liu, Yiming Li, Shengyin Sun et al. — [PV-Decoding: Progressive Verification Decoding with Decode Gating for Diffusion Language Models](http://arxiv.org/abs/2610.24722v1)
  <details><summary>📄 Abstract</summary>
  Discrete diffusion language models (dLLMs) offer an attractive alternative to autoregressive generation by updating multiple tokens in parallel, but their inference efficiency is still limited by the cost of safely committing tentative predictions. In particular, speculative decoding for dLLMs is challenging because speculative tokens within the same diffusion block may depend on one another, making aggressive acceptance prone to error propagation and strict verification computationally expensiv...
  </details>

- **2026-10-17** — Yiqiang Ye, Yichi Wang, Haodi Zhang et al. — [Spherical Physics-informed Neural Operator with Multi-scale Coupling for Meteorological Downscaling](http://arxiv.org/abs/2610.24708v1)
  <details><summary>📄 Abstract</summary>
  Meteorological downscaling is crucial for high-resolution regional climate forecasting and disaster early warning. While neural operators have emerged as a promising paradigm for modeling complex spatiotemporal mappings, existing frameworks often struggle with spherical manifold geometric distortions, inherent atmospheric multi-scale coupling mismatches, and lack of explicit atmospheric laws. We propose the Spherical Physics-informed Neural Operator, which utilizes a Spherical Laplacian Decompos...
  </details>

- **2026-10-17** — Ali Ansari, Farhana Ferdousi Liza — [Verifying Human-Written Reasoning References](http://arxiv.org/abs/2610.24690v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the reasoning of AI systems often relies on human-written reasoning chains as references, yet the logical support for their individual steps is rarely verified. Although prior neuro-symbolic approaches have formalized and checked reasoning, their reported evaluations do not systematically assess whether step conclusions in human-written reference derivations are entailed by their cited premise sets or investigate the sources of failures in those references. To address these limitation...
  </details>

- **2026-10-17** — Benjamin Ricaud, Artem Galushko — [Can AI agents make law? Evaluating AI legal relevance and creativity](http://arxiv.org/abs/2610.24661v1)
  <details><summary>📄 Abstract</summary>
  Large language models, the artificial intelligence (AI) systems behind modern chatbots, are trained on vast amounts of legal text, but can they build on it to write law for situations that text never anticipated? In this study, we analyse AI agents' ability to draft a hypothetical "Constitution" for a "community of AI agents". We design "constitutional assemblies" in which a single language model plays several characters that debate to produce a draft constitution. We find that the assemblies co...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 16 papers

- **2026-10-19** — Hridya Dhulipala, Xiaokai Rong, Aashish Yadavally et al. — [Step-Aligned Script Generation with Verification and Recovery for Web Automation Testing](http://arxiv.org/abs/2610.25601v1)
  <details><summary>📄 Abstract</summary>
  Automated generation of end-to-end web tests remains costly: developers must identify stable selectors, encode multi-step workflows, attach assertions, and maintain scripts as interfaces evolve. Recent LLM-based web agents can complete natural-language tasks in a live browser session, but task completion is not the same as producing a test-ware artifact - code that is executable, replay-able from a reset state, inspectable by developers, and tied to an oracle. We present TESSARA, an adaptive tes...
  </details>

- **2026-10-19** — Xingyu Shen, Yingfa Chen, Ziqing Qiao et al. — [Competing Learning in Hybrid Architectures](http://arxiv.org/abs/2610.26830v1)
  <details><summary>📄 Abstract</summary>
  Many modern language models have adopted hybrid architectures that incorporate both linear-time recurrence and softmax attention. Modern recurrence layers provide a highly expressive mixing mechanism while ensuring high throughput by compressing contextual information into a fixed-size state, but underperform softmax attention in contextual information retrieval. In this paper, we reveal a Competing Learning phenomenon where different kinds of mixers compete to learn the same function, and when ...
  </details>

- **2026-10-19** — Kelvin J. L. Koa, Ziling Liu, Xinyang Li et al. — [Regime-Aware Interpretable Ranking for Sector Rotation](http://arxiv.org/abs/2610.26456v1)
  <details><summary>📄 Abstract</summary>
  Sector rotation is a common decision in benchmark-relative portfolio management, where portfolio managers rank sectors for overweight and underweight positions. We formulate this task as ranking sector actions by expected future risk-adjusted active performance, measured with forward sector-benchmark Sharpe ratios. Such rankings should preserve temporal information, express model outputs through economically familiar signal characteristics, account for changes in signal relevance across macroeco...
  </details>

- **2026-10-19** — Jacopo Biggiogera, Nicolas Colombo, Krati Saxena et al. — [AuDQ: Auditable Data Quality through Agentic Rule Discovery](http://arxiv.org/abs/2610.26031v1)
  <details><summary>📄 Abstract</summary>
  High-stakes tabular pipelines rely on scattered, static quality checks that are hard to evolve and audit against policy intent. Regulated domains particularly suffer as the LLM-era automation raises expectations for traceability and accountability. We propose a vision for an ontology-grounded, repository-native data quality layer in which rules are first-class artifacts: versioned, provenance-linked to governance texts, and re-playable through immutable execution traces. As a first step toward v...
  </details>

- **2026-10-19** — Yicheng Wang, Wentao Tan, Yidan Huang et al. — [ClueFlow: Learning Long-Horizon Search through Attributed Research-State Transitions](http://arxiv.org/abs/2610.25980v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon search requires agents to acquire relevant evidence and integrate it into an evolving research state. Existing methods maintain research states to guide exploration or assign turn-level progress signals, yet grounding these signals in explicit, attributable state changes remains underexplored. We introduce ClueFlow, which learns long-horizon search from attributed research-state transitions. ClueFlow constructs Source-State-Final attribution chains that connect evidence-acquiring br...
  </details>

- **2026-10-19** — Chen Liang, Daoping Wu, Donghua Yang et al. — [DeltaTrace: Efficient Signed Attribution for Reasoning Language Models](http://arxiv.org/abs/2610.25877v1)
  <details><summary>📄 Abstract</summary>
  We study how words in the context support or oppose a language model's response and present DeltaTrace, a novel attribution framework that explains the effect of input tokens on a fixed model response. DeltaTrace measures how the response's log-probability changes when the context tokens being explained are masked. To distribute this difference among source tokens, it constructs operator-specific local rules for finite changes and composes them backward through the computational graph using effe...
  </details>

- **2026-10-19** — Zile Huang, Ser-nam Lim — [From Trace to Fix: Residual Task State in Long-Horizon Agents](http://arxiv.org/abs/2610.25776v1)
  <details><summary>📄 Abstract</summary>
  Recovering from failures in long-horizon, stateful language agents is challenging because the action introducing a defect, the symptom exposing it, and the persistent state requiring repair frequently diverge. Existing methods largely focus on retrospective failure attribution, leaving sequential diagnosis and state repair poorly integrated under constrained budgets. We introduce TRACE-FIX, a unified recovery framework centered on versioned residual task state. Trace transforms execution logs in...
  </details>

- **2026-10-18** — Efthymios Tsaprazlis, Bowen Yi, Tiantian Feng et al. — [SPARC: Spoken Profile Authorship Recognition Corpus](http://arxiv.org/abs/2610.25265v1)
  <details><summary>📄 Abstract</summary>
  Speech anonymization has focused on the acoustic signal, leaving open how much speaker information the transcribed words themselves retain. In this work, we study pairwise speaker and demographic-attribute verification from transcribed speech. We introduce SPARC (Spoken Profile Authorship Recognition Corpus), a benchmark built from two podcast corpora comprising over 12,500 speakers, 1.5M quality-filtered utterances, and speaker-level inferred or source-provided labels for sex, age, and accent, ...
  </details>

- **2026-10-18** — Yijie Guo, Dexiang Hong, Weidong Chen et al. — [IECLA: Interpretable Emotion Contribution Learning for Affective Image Editing](http://arxiv.org/abs/2610.25015v1)
  <details><summary>📄 Abstract</summary>
  Affective image editing (AIE) aims to evoke a target emotion while preserving the content and structure of a source image. Existing methods improve emotional expression or visual fidelity, but the target emotion alone does not reveal which source regions should be changed and which should remain intact, especially in complex scenes. We introduce Interpretable Emotion Contribution Learning for Affective Image Editing (IECLA), a framework that separates source-emotion attribution from target-aware...
  </details>

- **2026-10-18** — Saeid Asgari, Rui Ying, Sara Malvar et al. — [Rubrics Carry the Standard: Shapley Attribution for Checklist-Based LLM Judges](http://arxiv.org/abs/2610.24971v1)
  <details><summary>📄 Abstract</summary>
  Checklist rubrics applied by large language model (LLM) judges have become a standard instrument for evaluating open-ended outputs and for rewarding them during training. Two assumptions surround this practice: that leniency or strictness is a property of the judge model, and that a rubric can be improved by asking a model to review it. We test both in a controlled grading task with planted flaws and on two human-labeled datasets, SummEdits and RAGTruth. Holding the judge and the outputs fixed, ...
  </details>

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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-10-15** — Adnan Al Ali, Jindřich Libovický, Anne Lauscher — [Bias Mitigation in Audio-Enabled LLMs through Adversarial Training and Distillation Methods](http://arxiv.org/abs/2610.21763v1)
  <details><summary>📄 Abstract</summary>
  Audio-enabled large language models (AuLLMs) allow users to interact with them simply by talking to them, without the need for an intermediate transcription. This expands the model's accessibility and capabilities by encoding non-verbal cues. However, using non-verbal cues may lead to biased behaviour based on the attributes inferred (or assumed) from them. In this work, we focus on the gender attribute and show that models' perception of it can be unlearned using adversarial methods without a l...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-10-19** — Ben Bucknall, Andrew Byrley, Lewis Hammond — [From TCP/IP to MCP: Security and Governance Lessons from Internet Protocols for Agentic AI](http://arxiv.org/abs/2610.26624v1)
  <details><summary>📄 Abstract</summary>
  The past two years have seen considerable interest in protocols for managing how AI agents interact with human users, external tools, and each other. In many ways, these protocols, including the Model Context Protocol (MCP) and Agent2Agent (A2A), mirror the suite of protocols that underlie the modern internet. Motivated by this parallel, this paper draws lessons from the development, history, and governance of internet protocols with the aim of informing the responsible development of AI agent p...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 2 papers

- **2026-10-17** — Savan Doshi — [Medical Fine-Tuning Reshapes, Not Reduces, Patient-Facing AI Risk: A Rubric-Based, LLM-Judge Evaluation Framework](http://arxiv.org/abs/2610.24807v1)
  <details><summary>📄 Abstract</summary>
  Patient-facing medical question answering with large language models (LLMs) is moving from research demonstrations to production deployments, yet evaluation remains anchored on factual correctness. Factuality is necessary but not sufficient: a response can be factually grounded and still issue a directive that, if acted on, would harm the patient. We introduce a risk-sensitive evaluation framework that scores responses by the presence and severity of six categories of risk-bearing language (trea...
  </details>

- **2026-10-15** — Hasan Demirkiran, Jens Ernstberger — [Shortcut Sensitivity in Agent-Safety Evaluations](http://arxiv.org/abs/2610.22243v1)
  <details><summary>📄 Abstract</summary>
  AI agents take actions through tools. Some actions are sensitive, so guards that supervise them must themselves be evaluated reliably. Yet the data used to evaluate a guard can include cues that make labels predictable without measuring the intended safety construct, and those cues can also influence guard decisions. We introduce a three-level shortcut-auditing framework and audit completed LinuxArena trajectories and two TS-Bench-derived step datasets. We distinguish label predictability, obser...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 5 papers

- **2026-10-19** — Gwangjin Kim, Cheolyoung Jang, Yosep Jo — [OceanTensorCube and ST-MMT: A Multimodal Data and Transformer System for Seven-Day Forecasting of Pyropia Bleaching](http://arxiv.org/abs/2610.26209v1)
  <details><summary>📄 Abstract</summary>
  Bleaching of cultured Pyropia (laver) causes losses in Korean seaweed farming. We present a system that forecasts bleaching seven days ahead for farm clusters. OceanTensorCube aligns 32 channels from public marine, meteorological, ocean-model and satellite sources on a 30 m grid, and ST-MMT, a 9.2-million-parameter spatiotemporal transformer with hub-style multi-head cross-attention between variable groups, maps a 14-day input window to a seven-day-ahead bleaching probability. On the validation ...
  </details>

- **2026-10-19** — Alyson Ranucci, Eline Leijten, David Graus — [Towards More Granular Reasoning: Mapping the DSA Transparency Database Taxonomy to Platform Terms and Conditions Using Large Language Models](http://arxiv.org/abs/2610.26226v1)
  <details><summary>📄 Abstract</summary>
  Article 24(5) of the Digital Services Act (DSA) requires providers of online platforms to submit every content moderation decision they make, with a corresponding Statement of Reasons (SoR), to the DSA Transparency Database (DSA-TDB). Such decisions are classified against seventeen high-level attribute categories that categorize the primary reason for the moderation decision. Because over 99.8% of statements cite a violation of the provider's own terms and conditions rather than a legal provisio...
  </details>

- **2026-10-19** — Zhaoyang Zhang, Lingxiao Sun, Weijie Zhou et al. — [Mobile Embodied Agent Network (MEAN): Integrated Framework, Enabling Technologies, and Task-Driven Deployment](http://arxiv.org/abs/2610.26297v1)
  <details><summary>📄 Abstract</summary>
  Mobile networks are evolving from human-centered, data-oriented communication infrastructures toward machine- and/or agent-dominant, task-oriented platforms that are to serve the rapidly increasing networked machines and embodied agents. In order to fulfill the newly arose complex task objectives, the framework of future mobile network is to be innovated to reflect and facilitate the intrinsic interplay and integration of the underlying processes of perception, communication, computation, decisi...
  </details>

- **2026-10-17** — Veronica Guidetti, Luca La Rocca, Fabrício Olivetti de França et al. — [From Overparameterised Expressions to Parsimonious Models: Fisher-Geometric Pruning for Symbolic Regression](http://arxiv.org/abs/2610.24753v1)
  <details><summary>📄 Abstract</summary>
  Genetic programming symbolic regression (GPSR) often returns expressions that are larger than necessary, with dormant branches and finely tuned algebraic configurations that fit sampling noise. Existing complexity-control strategies, such as multi-objective size-accuracy search or information criteria embedded in the fitness function, act on syntactic representations during model search. We introduce Fisher-Geometric pruning (FGP), a post-hoc model-reduction framework that acts on fitted models ...
  </details>

- **2026-10-16** — Abigail Pribisova, Yao Li, Catalin Hritcu et al. — [A Taxonomy of Predicate Transformer Monads for Specifying Monadic Programs](http://arxiv.org/abs/2610.23604v1)
  <details><summary>📄 Abstract</summary>
  Monads of weakest precondition predicate transformers are the foundation of several verification frameworks for monadic programs. For specifying monadic computations with nondeterminism and nontermination, in addition to weakest preconditions, we introduce the first strongest postcondition monads covering all combinations of angelic or demonic nondeterminism and partial or total interpretations of nontermination. For extending these base strongest postcondition monads with side effects such as m...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 161 papers

- **2026-10-19** — Haonan Huang, Chengkun Cai — [The Development of Sycophancy in Language Models: Tracing Vulnerabilities from Pretraining to Post-Training](http://arxiv.org/abs/2610.26655v1)
  <details><summary>📄 Abstract</summary>
  Language models can change a committed answer to accommodate a user's opinion or pushback without new evidence. However, when this behaviour develops during training and what a released model inherits from earlier stages remain unclear. We follow 741 checkpoints of 30 open model lineages, from early pretraining to released models. We plant initial verdicts on moral scenarios and measure how far a model follows a user's stated opinion or abandons its verdict under pressure. In most lineages the b...
  </details>

- **2026-10-19** — Ashok Subbabhatta Gopalakrishna — [Connection Escrow: Holding AI-Agent Pod Egress in the Kernel Until an Isolated Verifier Rules](http://arxiv.org/abs/2610.26501v1)
  <details><summary>📄 Abstract</summary>
  AI agents in containers act by opening network connections, and the text that drives them can be hostile. Controls placed between the agent and its tools are bypassed by a child process or a direct socket, and their approval is not tied to the connection the kernel later opens. We present connection escrow: every outbound TCP connection from a supervised pod is parked inside the kernel's connect() path, before any packet exists, by a 98-instruction eBPF program on the pod's cgroup. A node interc...
  </details>

- **2026-10-19** — Tudor Cardas, Lucas Perotin, Bertrand Simon — [Ski Rental with Uniform Stochastic Signals](http://arxiv.org/abs/2610.26214v1)
  <details><summary>📄 Abstract</summary>
  Ski rental is one of the most fundamental online problems, where an agent repeatedly decides whether it should continue renting for a service, or buy it at a one-time fixed cost. In classic online analysis, an adversary may freely select any arbitrary time horizon $t$ after which the instance terminates, hence leading to strong competitive ratio lower bounds of 2 (deterministic) and $e/(e-1)$ (randomized).   We consider a novel but natural model aiming at limiting the adversary's power without d...
  </details>

- **2026-10-19** — Jiaming Liu, Xinghao Zhu, Yiming Zhang et al. — [Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation](http://arxiv.org/abs/2610.26854v1)
  <details><summary>📄 Abstract</summary>
  Multimodal reasoning provides robotic foundation models with predictive context needed for reliable action generation. However, language-based reasoning captures task semantics but struggles to express fine-grained physical dynamics, while latent reasoning models future state evolution but offers limited structure for organizing these dynamics into reusable reasoning primitives. To bridge this gap, we introduce PhysWord, a reasoning-before-acting foundation model built on Physical Words, which u...
  </details>

- **2026-10-19** — Shiyun Xiong, Dongming Wu, Peiwen Sun et al. — [Beyond Omni: A Unified MLLM for Embodied Sensory Understanding](http://arxiv.org/abs/2610.26751v1)
  <details><summary>📄 Abstract</summary>
  Recent embodied systems increasingly build on multimodal large language models (MLLMs) for their pretrained understanding and reasoning capabilities, but their perception of the physical world remains largely limited to basic modalities such as vision and audio. However, broadening MLLMs to more diverse sensory modalities from the physical environment is challenging: their representations are often weakly connected to the MLLM and vary substantially in structure and statistics, while their inter...
  </details>

- **2026-10-19** — Saurav Jha, Qianli Liao, Robert Vernon et al. — [recAMPLIFY: Large-Scale Pretraining of Recursive Protein Language Models](http://arxiv.org/abs/2610.26747v1)
  <details><summary>📄 Abstract</summary>
  Protein language models (pLMs) are powerful tools for protein annotation and mutation-effect prediction, but progress has largely depended on scaling model size and data, making them expensive and prone to memorization. Test-time scaling offers a complementary path, but methods developed for autoregressive LLMs do not transfer directly: masked encoders lack a generation loop, and amino acids do not verbalize in a reasoning language. Instead, we adapt recursive pretraining to masked pLMs, where a...
  </details>

- **2026-10-19** — Wan Ki Wong, Michele Ciampi, Rik Sarkar — [Proof-of-Machine-Learning-Inference: Mining Knowledge, Not Hashes](http://arxiv.org/abs/2610.26713v1)
  <details><summary>📄 Abstract</summary>
  Bitcoin-style Proof-of-Work (PoW) secures permissionless blockchains but spends substantial computation on hash puzzles which have no utility other than extending the chain. At the same time, we have seen that the rise of generative AI has created significant demand for computational resources that are unfortunately available only to a few players. We propose a solution that solves both problems at the same time. In particular, we present Proof-of-ML-Inference (PoML), a consensus protocol in whi...
  </details>

- **2026-10-19** — Liu Kaiyuan, Zhuang Ziyuan, Ma Haoxuan et al. — [A Fisher-Geometric View of Multi-Teacher On-Policy Distillation](http://arxiv.org/abs/2610.26525v1)
  <details><summary>📄 Abstract</summary>
  Consolidating specialized foundation models into a unified generalist is a central goal of post-training. Two approaches are in common use: model merging, which is fast but treated as a heuristic, and multi-teacher on-policy distillation, which matches distributions but demands heavy rollout compute and suffers from cross-task gradient conflict. We show that the two are one objective seen at different orders. Within a shared basin of homologous specialists, the multi-teacher on-policy distillati...
  </details>

- **2026-10-19** — Qingyang Wan, Chang Liu, Zhoutong Ye et al. — [Promptile: Recovering and Reusing Prompting Strategies from LLM Interaction Histories](http://arxiv.org/abs/2610.26485v1)
  <details><summary>📄 Abstract</summary>
  As people use large language models (LLMs) over time, they develop their own ways of prompting to achieve desired results. These useful experiences often remain scattered and unorganized across conversations. Yet existing personalization approaches primarily capture user preferences or explicitly defined workflows. Through a formative study, we found that users develop prompting strategies that range from implicit instructions to explicit templates from these experiences. We further find that in...
  </details>

- **2026-10-19** — Minseong Kim, Jongbok Won, Jeesup Park et al. — [Rethinking LLM Fine-Tuning via Weight Space Reparameterization: Preserving Safety during Downstream Adaptation](http://arxiv.org/abs/2610.26443v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning large language models (LLMs) on downstream tasks often weakens their previously aligned safety behavior, creating an inherent trade-off between task adaptation and safety preservation. Existing approaches attempt to mitigate this issue by identifying safety-relevant neurons, layers, or update directions in the original parameter space. However, safety-related information is often distributed across many directions in this space, causing downstream updates to overwrite parameters that...
  </details>

- **2026-10-19** — Eduin E. Hernandez, Sergio A. Diaz, Luis F. Garcia et al. — [How Benchmark Graph Construction Shapes Multi-Hop KG Navigation: A Controlled Audit of PathQuestion and PathQuestion-Large](http://arxiv.org/abs/2610.26399v1)
  <details><summary>📄 Abstract</summary>
  Multi-hop knowledge-graph question answering (KGQA) benchmarks are often treated as fixed language-and-reasoning tasks, but for navigation-based methods, difficulty also depends on the graph in which those tasks are instantiated. This makes graph construction a consequential but often entangled part of the navigation task. To isolate this effect, we audit PathQuestion (PQ) and PathQuestion-Large (PQL) as graph-navigation benchmarks under a controlled intervention: we hold questions, topic entiti...
  </details>

- **2026-10-19** — Tianqi Liu, Yandong Guan, Songze Li et al. — [When Coding Agents Outpace Review: Evaluating PRD-Driven Development in Mature Enterprise Repositories](http://arxiv.org/abs/2610.26394v1)
  <details><summary>📄 Abstract</summary>
  Coding agents increasingly undertake development tasks in mature enterprise repositories, yet existing benchmarks offer limited insight into whether they fulfill complete Product Requirement Documents (PRDs) and where delivery breaks down. Issue resolution and development from scratch leave incremental PRD fulfillment underexplored, while isolated tests provide incomplete evidence of business and integration requirements. We introduce PACE, a benchmark of 43 enterprise tasks with 750 expert-audi...
  </details>

- **2026-10-19** — Michael Glöckler, Timo Ropinski — [XGLASS: X-Ray, Gaze and Language Assisted Slice Sequencing for CT Volumes](http://arxiv.org/abs/2610.26255v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) achieve remarkable performance on 2D medical images, such as X-rays or pathology images, while 3D VLMs that directly process CT/MRI volumes lag behind due to limited 3D training data and the predominance of 2D foundation architectures. To leverage powerful 2D VLMs for analyzing medical volumes, which contain hundreds of slices, it is therefore necessary to focus only on those few slices, which are diagnostically relevant. To enable such a prioritization, we propose ...
  </details>

- **2026-10-19** — Tiange Xu, Kai Liu, Linghe Kong et al. — [RECAP: Reciprocal Sparse Attention and Hierarchical Caching for Efficient Video Diffusion](http://arxiv.org/abs/2610.26244v1)
  <details><summary>📄 Abstract</summary>
  Diffusion transformers generate high-quality videos but remain computationally expensive. Sparse attention and temporal caching reduce computation within and across denoising steps, respectively, offering a natural composition. However, predictions produced with sparse attention become sources for temporal reuse, coupling their errors along the sampling trajectory. We observe that improving the accuracy of these sources recovers fidelity without changing the reuse schedule, and that sparsificati...
  </details>

- **2026-10-19** — Yitong Li, Jiang Bian, Jingling Wang et al. — [MoveBench: A Rubric-Based Benchmark for Evaluating Large Language Models in Sports and Health Coaching](http://arxiv.org/abs/2610.26185v1)
  <details><summary>📄 Abstract</summary>
  Despite rapid advances in large language models (LLMs), their deployment in the sports and health domain remains high-risk due to the absence of domain-specific evaluation benchmarks. Existing general-purpose benchmarks (e.g., MMLU and HELM) primarily assess broad knowledge and reasoning capabilities, but fail to capture critical domain requirements such as exercise safety, physiological appropriateness, personalization, and actionable coaching quality. This gap is particularly concerning in fit...
  </details>

- **2026-10-19** — Chenghao Liu, Wei Fan, Jindong Han et al. — [TimesJev: Thinking Fast on Time Series with System 1 Sufficiency](http://arxiv.org/abs/2610.26002v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently shown strong potential for time series reasoning, while models that reason over time series are usually with long chains of thought. However, this process often consumes thousands of tokens, directly leading to substantial latency during inference. In contrast, System 1 models such as Jev make decisions instantly and can naturally be an alternative, but raw time series are not compatible with the embedding space of these models, thus hindering the reaso...
  </details>

- **2026-10-19** — Jin Han, Mingfeng Xin, Feng Liang et al. — [NIOCIS: Typed-Decision Next-Hop Routing with Node-Conditioned Option Spaces for Tool-Use Agents](http://arxiv.org/abs/2610.25985v1)
  <details><summary>📄 Abstract</summary>
  Tool-use agents pay per decision: at each hop a language model re-reads the state and thinks for seconds, though its actions are finite and decisions recur. We present NIOCIS, a routing layer that folds execution logs into a loop-collapsed action graph (forward transitions plus recovery back-edges) answering one typed question: which declared option at a state, plus stop, does the fleet take next? A small model reads a calibrated distribution over them in one pass, emitting no text. On 1,615 pro...
  </details>

- **2026-10-19** — Mohammed Haroon Dupty, Yong Liang Goh, Song Guo et al. — [Productive State-Space Exploration for Multi-turn RL in LLM Agents](http://arxiv.org/abs/2610.25957v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) for Large Language Model (LLM) agents in multi-turn, long-horizon environments remains challenging due to inefficient action selection and repetitive behavioral patterns. In particular, agents often become trapped in high-confidence yet unproductive behaviors, repeatedly executing invalid actions or entering action loops that hinder task completion. We observe that these frequently violate environment preconditions, revealing a mismatch between the agent's representat...
  </details>

- **2026-10-19** — Zixuan Chen, Depeng Wang, Hao Lin et al. — [OmniGround: Strengthening Omni-Modal Temporal Grounding via Attention-Consistency Training](http://arxiv.org/abs/2610.25929v1)
  <details><summary>📄 Abstract</summary>
  Omni-modal large language models can jointly understand video, audio, and text, yet they remain weak at temporal grounding, a capability essential for real-world audio-visual applications. To understand this limitation, we look beyond final predictions and examine the model's internal temporal evidence. We identify a temporal generation gap: the internal attention of the model localizes the target moment more accurately than the timestamps it generates. To close this gap, we propose TACG (Tempor...
  </details>

- **2026-10-19** — Hongrui Wu, Kaiwen Tuo, Congcong Wang et al. — [MIRA: A Multimodal Illustrated Deep Research Agent for Controllable Reports](http://arxiv.org/abs/2610.25926v1)
  <details><summary>📄 Abstract</summary>
  Deep research agents are increasingly capable of searching the open web and synthesizing evidence, yet they remain poorly suited to controllable report generation in multimodal deep research. This task requires agents to handle interleaved textual and visual inputs, gather multimodal evidence through multi-step web search, and deliver comprehensive illustrated reports under user-specified requirements. Existing systems face two limitations. During reasoning, they often underuse images discovered...
  </details>

- **2026-10-19** — Zixuan Chen, Depeng Wang, Wei Chen et al. — [SAPO: Self-Supervised Attention Policy Optimization for Improving Temporal Video Grounding in Vision-Language Models](http://arxiv.org/abs/2610.25923v1)
  <details><summary>📄 Abstract</summary>
  Video vision-language models (VLMs) have strong semantic understanding, yet remain unreliable at precise temporal grounding. Existing gains from explicitly aligning video frames with absolute time suggest that VLMs may already encode accurate temporal locations internally but lose precision when expressing them as timestamps. Our analysis across four VLMs and two grounding datasets confirms this hypothesis: attention intervals outperform predicted intervals on approximately 66% of valid examples...
  </details>

- **2026-10-19** — Ruotong Wang, Brian S. Yu, Xinyi Zhou et al. — [When Should AI Chime In? Benchmarking Timely Contribution of Proactive Agents in Multi-Party Chat](http://arxiv.org/abs/2610.25896v1)
  <details><summary>📄 Abstract</summary>
  Proactive agents can support group collaboration by surfacing useful information without waiting to be asked, but even relevant contributions can be disruptive if poorly timed. In this work, we isolate the timing question: given a fixed candidate contribution such as a clarification or relevant fact, when should an AI agent chime in? We introduce PITCH (Proactive Intervention Timing in CHat), to our knowledge the first benchmark with large-scale human judgments of proactive agent timing collecte...
  </details>

- **2026-10-19** — Debojeet Ghosh, Shreyansh Kumar, Ayushman Garg — [Measurement Validity and Representation Dynamics of Confidence Signals in Large Language Models](http://arxiv.org/abs/2610.25846v1)
  <details><summary>📄 Abstract</summary>
  Whether a language model "knows what it knows" matters for trustworthy deployment and for deciding when it should abstain. Prior work usually measures this through one channel: verbalized confidence, a linear probe on hidden states, or agreement among sampled answers (semantic entropy), and often treats these as interchangeable. We compare all three in a pre-registered audit of five Qwen2.5 models (0.5B-7B, including a base/instruct pair at 7B) on factual retrieval (PopQA, SimpleQA) and multi-st...
  </details>

- **2026-10-19** — Shijian Wang, Fanqing Meng, Jiajun Chen et al. — [FrontierRefactor: Benchmarking Multi-Scale Performance-Oriented Codebase Refactoring](http://arxiv.org/abs/2610.25834v1)
  <details><summary>📄 Abstract</summary>
  Autonomous codebase refactoring requires coding agents to restructure working software while strictly preserving externally observable behavior and prioritizing execution performance and compute efficiency over stylistic preference. Existing benchmarks: refactoring benchmarks assess functional correctness while overlooking runtime regressions, whereas code performance benchmarks target isolated micro-kernels that ignore codebase-scale complexity. We observe that refactoring scale is governed by ...
  </details>

- **2026-10-19** — Zhongyu Wang, Chen Zuo, Qingxuan Sun et al. — [MAPS: A Multi-Agent Personalized Script-Driven Video Advertising System Enhanced by Reinforcement Learning](http://arxiv.org/abs/2610.25748v1)
  <details><summary>📄 Abstract</summary>
  With the rapid growth of online video consumption, video advertising has become a dominant component of digital advertising. Most personalized video advertising systems follow a retrieval-based paradigm, which matches ad content with user preferences in a feature space and recommends the most similar candidates. However, since the candidate creatives are pre-produced, this paradigm limits the granularity of personalization and leads to performance disparities across diverse user groups. To addre...
  </details>

- **2026-10-19** — Keqi Chen, Zekai Sun, Yuhua Wen et al. — [From Black Box to Controller: Inference-Time Steering of LLM via Feature Amplification](http://arxiv.org/abs/2610.25700v1)
  <details><summary>📄 Abstract</summary>
  Inference-time steering is crucial for deploying Large Language Models (LLMs) in real-world applications, where they must flexibly adjust behavior preferences. For instance, a model should dynamically adjust its caution level based on the risk of the scenario. This requirement introduces a challenge: modulating the intensity of LLM preferences. Prompt engineering can require task-specific prompt design, while fine-tuning requires additional optimization and data. These requirements can make repe...
  </details>

- **2026-10-19** — Desheng Xu, Hanglin Li, Tianchen Song et al. — [LIRQuant: An Efficient Locally Isolated Rotation Quantization Method for Large Language Models](http://arxiv.org/abs/2610.25675v1)
  <details><summary>📄 Abstract</summary>
  Post-Training Quantization (PTQ) enables efficient deployment of Large Language Models (LLMs), yet activation outliers remain a key challenge for low-bit quantization. Existing global transformation methods overlook heterogeneous channel sensitivity to quantization noise, leading to suboptimal accuracy-efficiency trade-offs. To address this, we propose \textbf{Locally Isolated Rotation Quantization (LIRQuant)}, a sensitivity-aware framework that selectively applies transformations. LIRQuant iden...
  </details>

- **2026-10-19** — Yuki K. Wakabayashi, Yui Ogawa — [Autonomous adaptive spectral analysis with an LLM agent for self-driving laboratories](http://arxiv.org/abs/2610.25619v1)
  <details><summary>📄 Abstract</summary>
  Self-driving laboratories accelerate materials exploration through autonomous closed-loop integration of synthesis, characterization, and next-experiment selection. However, characterization does not always directly provide the target property; measured spectra or images often require automated analysis to extract quantitative descriptors based on physically motivated assumptions and predefined criteria. Such procedures can fail for measurements outside these criteria, requiring a decision on wh...
  </details>

- **2026-10-19** — Xuezhou Xu, Chung-Pang Wang, Zhenzhen Li et al. — [Vector-Quantized World Model: Latent Feedback Motion Planning for Robot Manipulation](http://arxiv.org/abs/2610.25600v1)
  <details><summary>📄 Abstract</summary>
  Visual world models have shown strong potential for robot planning, yet long-horizon manipulation remains challenging due to compounding prediction errors, large search complexity, and latent plans that the low-level controller cannot reliably reach. In this work, we introduce Vector-Quantized World Model (VQ-WM), a latent feedback motion planning framework that integrates discrete long-horizon search with continuous visual feedback control: a discrete latent predictor models transitions between...
  </details>

- **2026-10-19** — Tianqi Liu, Hanfei Zhao, Qifeng Liang et al. — [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](http://arxiv.org/abs/2610.26855v1)
  <details><summary>📄 Abstract</summary>
  World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, comprising 10k hours of egocentric human data and 3k hours of robot data with unified multimodal annotati...
  </details>

- **2026-10-19** — Zekai Li, Jiayi Yu, Jinlu Zhang et al. — [Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy](http://arxiv.org/abs/2610.26848v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we systematically investigate the mechanisms, scaling behavior, and generalization of physical Recursive self-improvement. We introduce PhysRSI-eval to quantify physical RSI through a five-axis metric: First-Attempt Performance, Efficiency, Success, Budget and Improvement from failure. Different VLMs are evaluated on 18 manipulation tasks under a fixed interaction budget. The analysis of experimental results motivates the Physical Barrel Hypothesis: different capabilities may cons...
  </details>

- **2026-10-19** — Tianwei Luo, Yiming He, Hongjin Wu et al. — [HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation](http://arxiv.org/abs/2610.26765v1)
  <details><summary>📄 Abstract</summary>
  General-purpose manipulation requires reliable behavior across embodiments, objects, and task demands. We introduce HandsOn, a composable simulation platform and benchmark for cross-embodiment dexterous manipulation. It supports five robotic arms, six dexterous hands, and approximately 200 rigid, articulated, and deformable assets in randomized scenes. The benchmark pairs 18,000 curated human demonstrations with 66 human-verified tasks: Core-50 supports demonstration-based learning and execution...
  </details>

- **2026-10-19** — Langzhe Gu, Chengkai Hou, Meng Li et al. — [HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control](http://arxiv.org/abs/2610.26584v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet adapting generalist vision-language-action (VLA) policies to real-world humanoid loco-manipulation remains challenging. Unlike fixed-base or wheeled manipulators, humanoids must coordinate locomotion, posture, gaze, and dual-arm manipulation over a high-dimensional whole-body action space, where inaccurate base or waist motions can easily induce unstable and aggressive upper-body compensation. We pro...
  </details>

- **2026-10-19** — Shenli Zheng, Zhou Fang, Yuan Du et al. — [SPAR: Structural Pruning and Action Recovery for Vision-Language-Action Models](http://arxiv.org/abs/2610.26487v1)
  <details><summary>📄 Abstract</summary>
  The limited onboard computing resources of robots make the inference demands of vision-language-action (VLA) models costly to accommodate. Reducing these demands through aggressive compression, however, can degrade manipulation performance beyond what supervised fine-tuning alone recovers. We present SPAR (Structural Pruning and Action Recovery), which simultaneously prunes the hidden and feed-forward intermediate dimensions of the large language model (LLM) backbone through pruning-aware tuning...
  </details>

- **2026-10-19** — David Balduzzi — [Affective Valence as the Interoceptive Rate of Change of Jacobian Scale](http://arxiv.org/abs/2610.26350v1)
  <details><summary>📄 Abstract</summary>
  Affect is widely held to depend on interoception. This paper proposes that valence is the rate at which interoception moves a self-sustaining system's responsiveness relative to its terminal set (roughly, death). Responsiveness is formalised as the scale of the system's Jacobian and interoception as its internal inputs: receptors, signals and forecasts of its energy reserve. Changes in responsiveness that bypass interoception, such as brain damage, are not felt. Language models have no valence b...
  </details>

- **2026-10-19** — Lu Tian, Zhenhui Yuan, Zexin Deng et al. — [K-AoI: A Spatio-Temporal Synchronization Metric for Digital Twin-based Teleoperation in Dynamic Network Environments](http://arxiv.org/abs/2610.26201v1)
  <details><summary>📄 Abstract</summary>
  Synchronization between a digital twin (DT) and its physical robot is critical for effective teleoperation, as mismatches directly degrade operator awareness and task performance. Existing synchronization metrics are predominantly time-based and rarely capture the spatial consequences of delayed information during motion. In this paper, we introduce Kinematic Age of Information (K-AoI), a spatio-temporal metric that weights AoI by instantaneous Cartesian velocity, translating temporal staleness ...
  </details>

- **2026-10-19** — Yian Zhao, Yu Yan, Hongcan Guo et al. — [Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips](http://arxiv.org/abs/2610.25666v1)
  <details><summary>📄 Abstract</summary>
  Streaming video world models generate the future chunk by chunk, conditioned on their own past and a stream of actions. Trained on short clips, they drift once a rollout exceeds the training horizon, as prediction errors re-enter the context and compound. A common remedy is to train the model on its own rollouts via distribution matching distillation (DMD). For action-conditioned world models, the teacher becomes a bottleneck: an external video model is agnostic to the actions, whereas the model...
  </details>

- **2026-10-19** — Albert Qin, Jonathan Cohen, Gautam Reddy — [Cognitive Map in Large Language Models](http://arxiv.org/abs/2610.25596v1)
  <details><summary>📄 Abstract</summary>
  It has long been proposed that animals construct cognitive maps to support flexible behavior in novel environments. We tested whether large language models form similar representations using relational reasoning tasks and causal "mosaic experiments" that manipulate internal activations in open-weight language models. Models beyond the ten-billion-parameter scale successfully inferred unstated relationships between entities and generalized to synthetic entity names. Across model and task families...
  </details>

- **2026-10-19** — Yu Zhou, Cheng-Fu Yang, Rui Sun et al. — [OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory](http://arxiv.org/abs/2610.26860v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements obtained through heterogeneous tools, whose outputs must be made interpretable to the model and retai...
  </details>

- **2026-10-19** — Wenqian Zhang, Yangyi Huang, Zigeng Xu et al. — [Can It Actually Work? Synthesizing Functional CAD Mechanisms](http://arxiv.org/abs/2610.26861v1)
  <details><summary>📄 Abstract</summary>
  While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that satisfy functional requirements in physical simulation. Verifying these requirements is nontrivial: different candidate mechanisms may realize the same function through entirely different components, controls, and operating...
  </details>

- **2026-10-19** — Yuchi Wang, Rongyao Fang, Weihao Yu et al. — [RefCraft: Benchmarking Visual-Reference-Conditioned Agentic Generation through Web Development](http://arxiv.org/abs/2610.26826v1)
  <details><summary>📄 Abstract</summary>
  Beyond basic tool use and coding skills, effectively incorporating visual references into agentic generation is equally essential for applying AI agents to real-world productivity tasks. We study this crucial capability through webpage development, a practical and readily evaluable setting in which existing benchmarks remain largely idealized: they typically focus on reconstructing visual targets or generating webpages from textual instructions alone, overlooking the more common workflow of deve...
  </details>

- **2026-10-19** — Anxin Guo, Tianlong Huang, Chenxiao Yang et al. — [Copying Under Repetition: From Prefix Matching to Position Hashing](http://arxiv.org/abs/2610.26722v1)
  <details><summary>📄 Abstract</summary>
  Frontier LLMs can copy random text almost flawlessly, yet they often overrun or truncate long blocks of repeated characters. In repeated strings, matching local content no longer reliably identifies where copying should continue or when it should stop. Nevertheless, we show that a two-layer transformer with $O(\log\log N)$-bit precision and $O(\log N/\log\log N)$ width can copy every string up to a chosen design horizon $N$ and terminate correctly under arbitrary repetition. We use RoPE-style ro...
  </details>

- **2026-10-19** — Zhao Gao, Mina Metias, Mohamed Noordeen Alaudeen et al. — [CaptionFuse: Training-Free Composed Product Retrieval Via VLM Intent Captioning and Weighted Embedding Fusion](http://arxiv.org/abs/2610.26661v1)
  <details><summary>📄 Abstract</summary>
  Composed Image Retrieval (CIR) retrieves products matching a reference image modified by natural language---a core capability for eCommerce search. Existing training-free methods fuse CLIP embeddings via arithmetic, but we identify a fundamental limitation: user text modifications are attribute-sparse---a user who types ``make it red with shorter sleeves'' specifies what to change but not what to keep (the floral pattern, the V-neck, the fit-and-flare silhouette). We introduce language-space fus...
  </details>

- **2026-10-19** — Xiaomeng Li — [Small Average Error, Wide Individual Error: General-Purpose LLMs Estimating Energy Intake from Meal Photos in a Feeding Trial](http://arxiv.org/abs/2610.26538v1)
  <details><summary>📄 Abstract</summary>
  Photo-based estimation of food energy could ease dietary assessment, and general-purpose multimodal large language models (LLMs) make such estimates easy to obtain. Most evaluations use one photo taken before eating and compare with energy served, while dietary assessment needs energy eaten. We evaluated six models from two vendors (Claude Haiku, Sonnet and Opus 5.5; GPT-6 luna, 6.1 sol and 6 astra) on 802 meals from ACETADA, a controlled feeding trial with weighed intake, with the before photo ...
  </details>

- **2026-10-19** — Zhicheng Zheng, Cheng Zhang, Shengping Yu et al. — [ScopeMem: Latent Memory That Learns Where to Revise Frozen GUI Agents](http://arxiv.org/abs/2610.26503v1)
  <details><summary>📄 Abstract</summary>
  Latent memory is gaining ground as a lightweight history supplement for GUI agents. It supplies history to a frozen vision-language model via prefix vectors trained with step-wise cross-entropy (CE). While resulting gains are naturally attributed to encoded history, our controlled experiments show they primarily stem from action revision. The prefix learns to alter the model's default actions. However, this revision is unscoped because step-wise CE pushes outputs toward reference actions at ever...
  </details>

- **2026-10-19** — Aur{é}lien Garivier — [Universal coding with the exhaustive peres transform](http://arxiv.org/abs/2610.26396v1)
  <details><summary>📄 Abstract</summary>
  Peres's iteration of von Neumann's procedure is completed into a bijection of $\bits^N$: the recursion runs to exhaustion, nothing is discarded, and every input splits into fair bits and residual bits. The residual strings form a complete prefix code that determines the number of ones of the input, so the fair bits are exactly uniform given the residual for every exchangeable law. For a Bernoulli source the likelihood factorises exactly, in decoding order, into a factor $1/2$ per fair bit and a ...
  </details>

- **2026-10-19** — Motti Goldberger, Nils Rudi — [Selecting the Best Few with Human Evaluators: Adaptively Combining Ratings and Pairwise Comparisons](http://arxiv.org/abs/2610.26380v1)
  <details><summary>📄 Abstract</summary>
  This paper considers a decision-maker tasked with identifying the $k$ best items from a large pool of candidates, such as job applicants, LLMs, award nominees, or new product ideas. The decision-maker learns about the items' quality by soliciting human evaluations. Each evaluation can be costly, so the decision-maker aims to use the limited evaluation budget efficiently by allocating evaluations adaptively. A key consideration is the form of evaluation to solicit, which should be something evalu...
  </details>

- **2026-10-19** — Minglei Li, Peng Ye, Haonan He et al. — [An Empirical Study of Parameter-Efficient Fine-Tuning for Mixture-of-Experts LLMs](http://arxiv.org/abs/2610.26370v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning (PEFT) methods are critical for adapting large models under resource-constrained settings. However, as mixture-of-experts (MoE) architectures, which offer efficient inference at massive parameter scales, gain increasing prevalence in the community, a critical gap arising from the lack of systematic recipes for applying PEFT to MoE models. To narrow this gap, we conduct a large-scale systematic study that investigates a set of essential design recipes, including wh...
  </details>

- **2026-10-19** — Amrin Akter, Mauro Dalla Mura, Diana Mateus et al. — [Localization Gains from Explanation Regularization Should Not Be Interpreted as Faithfulness Gains.](http://arxiv.org/abs/2610.26292v1)
  <details><summary>📄 Abstract</summary>
  Training-time explanation regularization is often evaluated by whether saliency maps become more concentrated within annotated regions. We argue that this criterion alone is insufficient: transformation consistency, lesion localization, and faithfulness to the classifier are distinct properties and should be evaluated separately, particularly in medical imaging. We examine this distinction through a case study of Contrastive Grad-CAM Consistency (CGC) in three-class brain tumor MRI classificatio...
  </details>

- **2026-10-19** — Junlin Li, Sara Alhajeri, Tatsuki Kuribayashi — [Reading Time Modeling with Pixel-Based Language Models](http://arxiv.org/abs/2610.26181v1)
  <details><summary>📄 Abstract</summary>
  Tokenization-free, pixel-based language models (PLMs) have recently been proposed as an alternative to conventional token-based language models (TLMs), typically motivated by practical considerations, e.g., the flexibility to support new languages or vocabularies. Nevertheless, PLMs also have the potential to serve as infrastructure for computational (psycho)linguistics, where tokenization has been a source of bias in estimating information-theoretic values, such as surprisal, and has pushed the...
  </details>

- **2026-10-19** — Shan-Ping Wu, Jia-Zhou Liu, Yu-Xiao Liu et al. — [Black hole free energy landscapes from constrained instantons](http://arxiv.org/abs/2610.26094v1)
  <details><summary>📄 Abstract</summary>
  We apply gravitational path integral factorization to provide a semiclassical interpretation of generalized black hole free energy landscapes at fixed external temperature and angular velocities. Boundary integral transforms express the formal partition function as an integral over constrained sectors labeled by complete local partial-Neumann data on an auxiliary hypersurface. Independent variation establishes paired regular subregion solutions as constrained instantons, with Lagrange multiplier...
  </details>

- **2026-10-19** — Zijun Zhao, Ruichu Ao, Stef Cuyckens et al. — [MX-Like Tensor Core for LLM Inference with NPU Integration via Hardware-Software Co-Design Exploration](http://arxiv.org/abs/2610.26083v1)
  <details><summary>📄 Abstract</summary>
  Block-scaled quantization formats such as OCP Microscaling (MX) and NVFP4 have been widely adopted as efficient data formats for LLM inference. However, the design space of these formats spanned by shared scale, weight, and activation format combinations has not been systematically explored, and the joint accuracy-silicon tradeoff across this space remains uncharacterized, leaving the true Pareto-optimal configurations for NPU-based edge LLM deployment an open question. To bridge this gap, we co...
  </details>

- **2026-10-19** — Qing Yang, Yuqi Xiong, Pengcheng Huang et al. — [Procedural Exposure Bias in Skill-Augmented Language Model Agents](http://arxiv.org/abs/2610.26062v1)
  <details><summary>📄 Abstract</summary>
  External skills provide language-model agents with reusable procedural knowledge, yet how models use such knowledge after it is supplied remains poorly understood. We identify Procedural Exposure Bias (PEB), the tendency of language models to increasingly favor an action as its associated procedural pattern is repeatedly exposed in a skill, even when the interaction state and action relevance remain unchanged. We find that PEB strongly depends on how procedural knowledge is represented: presenti...
  </details>

- **2026-10-19** — Junhui Chen, Yu Zhang, Lantian Li et al. — [Behavioral Probes for Information Flow in LLM Swarms](http://arxiv.org/abs/2610.25966v1)
  <details><summary>📄 Abstract</summary>
  Most existing approaches to LLM swarm optimization are utility-driven, focusing on final task utility while leaving the processing, integration, and reliance of information within individual interactions largely implicit. To address this, we study LLM swarm interactions from an information-flow-based view and introduce behavioral probes to quantify information flow patterns. Specifically, we repurpose External Context Score (ECS) and Parametric Knowledge Score (PKS)---originally designed for hal...
  </details>

- **2026-10-19** — Heyang Liu, Lixin Zhang, Jiayi Huang et al. — [Speech LLMs That Breathe: Modeling Non-Verbal Vocalizations in Dialogue](http://arxiv.org/abs/2610.25942v1)
  <details><summary>📄 Abstract</summary>
  The user experience of speech interaction models has improved, benefiting from the modeling of paralinguistic attributes and advances in speech reconstruction paradigms. However, human communication follows extensive norms regarding non-verbal vocalizations (NVVs) spanning respiratory, affective, and discourse. The omission of these events imposes inherent limitations on the naturalness of current approaches. In this work, we cover 13 major types of NVVs and construct a natural dialogue dataset ...
  </details>

- **2026-10-19** — Neha Bura, Peije Zhang, Ganesh Bera et al. — [A Stress-Induced Tetragonal Distortion in K2OsCl6 under Pressure](http://arxiv.org/abs/2610.25913v1)
  <details><summary>📄 Abstract</summary>
  The structural behaviour of cubic (Fm-3m) K2OsCl6 under compression was investigated to 35.4 GPa using angle-dispersive synchrotron powder X-ray diffraction. Upon increasing pressure, K2OsCl6 undergoes a sequence of structural transformations from the ambient-pressure cubic phase to a tetragonal (P4/mnc) phase above 9.5(3) GPa, followed by a transition to a monoclinic (P21/n) phase beginning at approximately 14.2 GPa. The tetragonal and monoclinic phases coexist over the pressure range 14.2-17.2...
  </details>

- **2026-10-19** — Yanwei Huang, Arpit Narechania, Atanu Sinha — [MASIF: Implicit Failures for Process Observability in Multi-Agent Systems](http://arxiv.org/abs/2610.25852v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) can complete a task despite local execution errors that are corrected, bypassed, or carried forward without individually determining its outcome. We call these implicit failures (IFs) and study them as signals for process observability beyond final task outcome. Across 1,828 traces from nine MAS-benchmark configurations, IFs occur in 54.3% of successful and 75.2% of failed traces. We develop taxonomies of error types and subsequent absorption mechanisms, supported by hu...
  </details>

- **2026-10-19** — Mohsen Fayyaz, Ali Modarressi, Daniel Israel et al. — [Diffusion Language Models Change Speed Across Tasks and Languages](http://arxiv.org/abs/2610.25835v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models can write several tokens in one forward pass, and they decide during generation how many passes to spend. Two outputs of the same token length can therefore vary a lot in cost. To understand the underlying factors of this cost variation, we analyze two diffusion models across 10 tasks. We find that the number of forward passes per token depends heavily on the task. Text copied or lightly edited from the input is cheap, while open-ended writing is costly. In DiffusionGem...
  </details>

- **2026-10-19** — Guanqun Jiang, Pengfei Cao, Kang Liu et al. — [When Retrieval Partially Conflicts with Skills: Understanding Procedural Hallucination in Language Models](http://arxiv.org/abs/2610.25827v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly use skills that provide reusable instructions and procedures for task execution. After a relevant skill has been selected, the model may need to apply its governing procedure together with retrieved task context. When the retrieved context is useful but contains cues that violate the skill, the model must retain compatible information while rejecting the conflicting cues. We study failures in which the model adopts such cues and produces a retrieval-supported but ski...
  </details>

- **2026-10-19** — Ezgi Başar, Yevgen Matusevych, Annemarie van Dooren et al. — [Modal Sense Disambiguation in Language Models: The Role of Context, Training Domain, and Input Frequency](http://arxiv.org/abs/2610.25816v1)
  <details><summary>📄 Abstract</summary>
  Modals such as may and must can take on different senses depending on discourse context, alternating between root interpretations (e.g., permission, obligation) and epistemic interpretations (e.g., knowledge, belief). While modals are known to be notoriously difficult for children to acquire, limited research exists on whether language models (LMs) can reliably distinguish between different modal senses. We evaluate seven LMs that vary in architecture, size, and training data type using vector-b...
  </details>

- **2026-10-19** — Dan-Adrian German, Tony Newton — [Distributed Phase Tags: A Locality-Preserving Realification Compiler for Misty-State Quantum Programs](http://arxiv.org/abs/2610.25703v1)
  <details><summary>📄 Abstract</summary>
  Complex amplitudes can be simulated over real Hilbert spaces by adjoining a two-dimensional real/imaginary degree of freedom. In a multipartite program, however, one globally shared phase tag is not a locality-preserving program transformation: every party would have to act on the same auxiliary system. We recast the distributed real simulation of multipartite quantum mechanics as a syntax-directed compiler into a real misty-state intermediate language. For $n$ parties we give explicit phase-ref...
  </details>

- **2026-10-19** — Oleg Grynets, Vasyl Lyashkevych, Andrii Salyk et al. — [Beyond Leaderboards: A Method for Application-Specific Capability Profiling of Large Language Models](http://arxiv.org/abs/2610.25659v1)
  <details><summary>📄 Abstract</summary>
  Public leaderboards rank large language models (LLMs) in general, but an engineer has to choose a model for a specific application, architecture and cost. This paper presents a method for application-specific capability profiling of LLMs and its realization as a containerized testbed. The method treats each application as a unit of extension: an Oracle-to-PostgreSQL migration agent, a documentation-grounded chatbot or an enterprise-support automation agent runs in its own container behind a smal...
  </details>

- **2026-10-19** — Arber Zela, Artavazd Maranjyan, Pol Puigdemont et al. — [Spherical Fixed-Point Reasoners: Adaptive Loop Halting on the Hypersphere](http://arxiv.org/abs/2610.25646v1)
  <details><summary>📄 Abstract</summary>
  Looped (weight-tied) transformers enable adaptive computation by allocating more iterations to harder inputs. Fixed-Point Reasoners (FPRM) achieve this with a damped fixed-point solver, but operate in an unbounded Euclidean residual space with coupled rescaling and relative-norm halting. We introduce Spherical Fixed-Point Reasoners (SFPRM), which perform the same computation on the unit hypersphere of normalized transformers (nGPT). Input injection, damping, and halting become geodesic operation...
  </details>

- **2026-10-19** — Hao Li, Minghui Ren, Shaowen Lu — [The Forward/Inverse Duality of Controlled Emergence:A Computational Design Program from Explanation to Engineering](http://arxiv.org/abs/2610.25630v1)
  <details><summary>📄 Abstract</summary>
  The macroscopic capabilities of intelligent systems arise from the local interactions of many simple units. When such systems are deployed in the real world, their behaviour must nevertheless be constrained, leaving designers caught between releasing adaptability and preventing loss of control, yet without formal tools to resolve the dilemma. This paper proposes a unified research program for controlled emergence that restates this tension as a pair of dual problems: the forward problem explains...
  </details>

- **2026-10-18** — Anirban Ghatak, Kaushik Sarkar, Anupam Chattopadhyay et al. — [Equivalent Non-linear Shift Register Transformations and Espresso](http://arxiv.org/abs/2610.25346v1)
  <details><summary>📄 Abstract</summary>
  The stream cipher Espresso was designed by E. Dubrova and M. Hell as a hardware-efficient candidate for 5G security. It has two components - a 256-bit binary non-linear feedback shift register (NFSR), with 14 feedback taps, and a 20-variable non-linear output function. However, the security of Espresso with regard to several standard cryptanalytic attacks are estimated using an alternate NFSR, which has only two feedback taps. The above analysis is based on the claim that this alternate NFSR is ...
  </details>

- **2026-10-18** — Mohsen Amoei, Kathleen Fraser, Dan Poenaru — [Complementary Vulnerabilities: Auditing and Governing Clinician-LLM Error Overlap](http://arxiv.org/abs/2610.25279v1)
  <details><summary>📄 Abstract</summary>
  Health systems are deploying large language models (LLMs) into clinical workflows, often on the assumption that a second automated check can only reduce error. But a second reasoner reduces error only insofar as it fails differently from the first. We say that a clinician and a model have complementary vulnerabilities to the extent that they break down through different mechanisms and on different cases. The two reasoners' failure substrates differ: they are embodied and cognitive in the clinici...
  </details>

- **2026-10-18** — Behnam Moradi — [Self-Crystallizing Behavior Trees: Amortizing Foundation-Model Reasoning into Deterministic Control for Autonomous Drones](http://arxiv.org/abs/2610.25455v1)
  <details><summary>📄 Abstract</summary>
  Classical robot control, Finite State Machines and Behavior Trees (BTs), is deterministic and inspectable but fixed at design time: it fails on situations its designers did not anticipate. Foundation models can synthesize new control logic at runtime, at a cost in latency and non-determinism hard to accept in safety-critical aerial systems. Existing LLM-driven approaches keep the model in the loop permanently and discard what it produces. We propose Self-Crystallizing Behavior Trees (SCBT), in w...
  </details>

- **2026-10-18** — Mohammad Omama, Aeyan Ashraf, Sandeep Chinchali — [LateMatch: Breaking the Interaction Bottleneck via Cacheable Matching for Efficient Visual Localization](http://arxiv.org/abs/2610.25358v1)
  <details><summary>📄 Abstract</summary>
  Visual localization is critical for embodied agents, but deploying state-of-the-art deep feature matchers on edge devices is fundamentally limited by their massive computational cost. Standard deep matchers tightly interleave intra-image context building and inter-image matching at every layer, creating a severe interaction bottleneck. Localizing a single query against K database images forces the system to execute the full network K independent times with no capacity for caching. To break this ...
  </details>

- **2026-10-18** — Tianyi Hu, Bhavyajeet Singh, Niket Tandon et al. — [Where and Why Search-Augmented LLMs Fail When Reasoning over Rapidly Evolving Knowledge](http://arxiv.org/abs/2610.25323v1)
  <details><summary>📄 Abstract</summary>
  As the world changes, new information is published while older records remain online. This complicates reasoning for large language models (LLMs), which must retrieve evidence and resolve conflicts to determine which information remains valid. Existing evaluations treat information seeking as a black box, revealing little about where and why LLMs fail. To address this gap, we introduce TREK, a suite of three components: TREKTRACE is a plug-and-play framework that attributes failures to specific ...
  </details>

- **2026-10-18** — Ronen Schaffer, Hila Manor, Tomer Michaeli — [The Explainability Illusion: Must ViTs Exhibit Patch-Decoding Interpretability?](http://arxiv.org/abs/2610.25289v1)
  <details><summary>📄 Abstract</summary>
  Transformers are widely assumed to exhibit token-decoding explainability. In particular, in vision transformer (ViT) classifiers, decoding individual patch tokens has become a common diagnostic tool due to its tendency to yield human-interpretable outputs. In light of the increasing popularity of this approach, an important question is whether token-decoding explainability is an inherent property of transformers that should be expected to hold across architectures, scales, and training objective...
  </details>

- **2026-10-18** — Zixuan Qin, Qi Qin, Erbo Li et al. — [Hidden Cartographer: Hidden State Guided Data Selection for Dual Budgeted Instruction Tuning](http://arxiv.org/abs/2610.25215v1)
  <details><summary>📄 Abstract</summary>
  Given the high cost of expert annotation and limited fine-tuning resources, effective data selection from large unlabeled pools under strict budgets has become a crucial step in adapting LLMs to specialized domains. Existing label-dependent methods risk distorted selection when using pseudo-labels, while traditional active learning methods do not explicitly characterize instruction-tuning dynamics. To address these limitations, we propose Hidden Cartographer (HC), a two-stage framework that uses...
  </details>

- **2026-10-18** — Yuu Hariya — [A relationship between three-dimensional Bessel processes in terms of Pitman's transformation](http://arxiv.org/abs/2610.25205v1)
  <details><summary>📄 Abstract</summary>
  For every $x\ge 0$, let $R^{x}=\{ R^{x}_{t}\} _{t\ge 0}$ be a three-dimensional Bessel process started at $x$. Given $x>0$, with the aid of Pitman's theorem, a path transformation $T_{x}$ under which the process $T_{x}(R^{y})$ is distributed as $R^{x}$ for any $y>0$ is constructed. In fact, we prove that, for every $x,y>0$, the two three-dimensional processes \begin{align*}   \bigl( R^{x},T_{y}(R^{x}),\mathcal{P}(-R^{x})+x\bigr) && \text{and} &&   \bigl( T_{x}(R^{y}),R^{y},\mathcal{P}(-R^{y})+y\...
  </details>

- **2026-10-18** — Yiqi Wang, Jinqian Ju, Jiaqi Zhang et al. — [Memories That Outlive Their Reasons: Dependency-Tethered Memory for Tool-Using LLM Agents](http://arxiv.org/abs/2610.25123v1)
  <details><summary>📄 Abstract</summary>
  Agents now act on the Web, publishing packages, models and datasets through registry APIs, and remembering past verifications spares them the work. But a verdict rests on premises. When a signing key is revoked, everything built on it stops passing, yet the advisory names only the key, and the old verdicts of its dependents may never share a retrieval window with it. This non-locality of invalidation turns memory into a liability: in long simulated chats, an agent reading a memory of atomic fact...
  </details>

- **2026-10-18** — Jingwen Bai, Guochao Bai, Canbo Zhang et al. — [Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds](http://arxiv.org/abs/2610.25114v1)
  <details><summary>📄 Abstract</summary>
  Embodied AI lacks the data-rich pretraining that gave language models their agents and skills, so new manipulation capability costs demonstrations per task or a frontier model in every episode. We study a third route: a strong general model acts only as an offline author that writes, runs, diagnoses and repairs a manipulation skill in simulation until it passes an exam on layouts drawn after freezing; the frozen skill then runs as code alone or under a cheap caller that reads only its descriptio...
  </details>

- **2026-10-18** — Hui Yang, Wan Tian, Tao Ren et al. — [Conformal Prediction-Enabled Sequence-level Policy Optimization for Reasoning Language Models](http://arxiv.org/abs/2610.25092v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning improves the reasoning capability of large language models through verifiable rewards for mathematical and coding tasks. In token-level methods such as GRPO, clipping acts on individual token ratios while the reward and advantage apply to a complete response. Recent sequence-level methods align these units but still use fixed clipping bands, whose tail probabilities change as the score distribution evolves. We propose Conformal Prediction-Enabled Sequence-level Policy Opti...
  </details>

- **2026-10-18** — Junwei Wen, Deshui Miao, Guangming Lu et al. — [Think Visually Across Space and Time: Grounded Reasoning for Video Segmentation](http://arxiv.org/abs/2610.25090v1)
  <details><summary>📄 Abstract</summary>
  Video Reasoning Segmentation (VRS) requires a model to identify an implicitly described target and predict its pixel-level mask trajectory, while resolving the spatial relations and temporal events that determine the answer. Text-only Chain-of-Thought (CoT) can explain a target choice without making the underlying visual references explicit, leaving a \emph{video reference gap} between linguistic inference and the evidence distributed across frames. We introduce \textbf{Temporal Chain of Video P...
  </details>

- **2026-10-18** — Zhuonan Yang, Yik Siu Chan, Wannan Yang et al. — [Representations in Motion: Layer-wise Rotation and Trajectory Divergence in LLMs](http://arxiv.org/abs/2610.25574v1)
  <details><summary>📄 Abstract</summary>
  Recent work suggests that activation dynamics--how representations change during inference--might be more revealing about language model behavior than static readouts from individual layers. In this work, we investigate the layer-wise evolution of representations of factuality, using true and false statements when the model is prompted to either lie or to be honest. We report a geometric phenomenon in which the factuality directions extracted from the lying and honest conditions appear to rotate...
  </details>

- **2026-10-18** — Mikaela Martins, Jonathan Dunn — [Where Are Language-Specific Features Represented in Multilingual LLMs? Everywhere](http://arxiv.org/abs/2610.25505v1)
  <details><summary>📄 Abstract</summary>
  Previous work has argued that multilingual LLMs encode language-specific features most strongly in their initial and final layers, implying that intermediate layers support language-agnostic representations. This paper reconsiders this finding by performing four different experiments: three that undertake a fine-grained analysis of representations of Portuguese and Spanish, two closely related languages, and one large-scale language identification experiment that covers over 200 languages. The r...
  </details>

- **2026-10-18** — Christopher Leet, Achyutha Menon, Sravanthi Machcha et al. — [The Bitter Lesson Comes to Robotics](http://arxiv.org/abs/2610.25287v1)
  <details><summary>📄 Abstract</summary>
  General purpose multimodal language models (LMs) are increasingly capable of directly controlling robotic arms (e.g., by commanding end effector poses) to manipulate their environment. Tracking the development of these capabilities is important for understanding their potential benefits, such as improving industrial automation, and risks, such as enabling malicious users to produce dangerous chemical or biological agents. To this end, we investigate the ability of frontier multimodal LMs to dire...
  </details>

- **2026-10-18** — Zhu Liu, Zhen Hu, Yuxuan Liu et al. — [Behave Like Experts: Fusing Data with Semantic Knowledge for Effective and Efficient Semantic Map Construction](http://arxiv.org/abs/2610.25122v1)
  <details><summary>📄 Abstract</summary>
  Semantic map models (SMMs) construct a graph that reflects conceptual similarity by comparing cross-lingual form-meaning mappings. Experts build such models not only by obeying the data constraint, i.e., the connectivity hypothesis, which states that conceptual nodes belonging to the same form must be connected, but also by incorporating their prior semantic knowledge. Current automatic methods ignore this knowledge, which harms both accuracy and efficiency by enlarging the search space of candi...
  </details>

- **2026-10-18** — Junhao Liu, Tianxiao Li, Yongxian Wu et al. — [Auditing Tool Traces in Agentic LLMs: Source Localization and Counterfactual Dependence Testing](http://arxiv.org/abs/2610.25540v1)
  <details><summary>📄 Abstract</summary>
  Agentic LLMs increasingly support scientific prediction by grounding decisions in external evidence. In biology, they promise accurate, interpretable predictions for important problems by integrating complex experimental and computational evidence. However, serialized tool results can contain hidden label shortcuts, such as dataset identifiers or template artifacts, that create apparent success without biological reasoning. To address this risk, we introduce a two-stage audit. Stage 1, Per-Tool ...
  </details>

- **2026-10-18** — Parham M. Kebria, Saeid Nahavandi, Mehrdad Saif et al. — [SurGPT: A Multi-Task Foundation Model for Robotic Surgical Skills Assessment and Gesture Recognition](http://arxiv.org/abs/2610.25426v1)
  <details><summary>📄 Abstract</summary>
  The assessment of surgical skills in robotic surgery training has traditionally relied on subjective evaluations by human experts, creating bottlenecks in surgical education and limiting scalability. We present a novel foundation model that automatically analyzes robotic surgical videos to provide comprehensive skill assessment and gesture understanding. Combining a visual encoder with a transformer architecture, the model performs three key tasks simultaneously: 1) surgical task classification ...
  </details>

- **2026-10-18** — Karthik Viswanathan, Plamen Dimitrov, Stefano Rocca et al. — [Formally Verified Autoresearch for Analyzing the Expressivity of Multi-Head Attention](http://arxiv.org/abs/2610.25341v1)
  <details><summary>📄 Abstract</summary>
  Multi-head attention is a central component of the transformer architecture, yet how its expressivity depends on the number of heads remains poorly understood. We study a one-layer, attention-only transformer with additive positional embeddings and define the head complexity $H^\ast(f)$ of a Boolean function $f$ as the minimum number of attention heads required to represent it. We derive an exact linear-fractional normal form for head complexity, prove a general threshold-degree lower bound, and...
  </details>

- **2026-10-18** — Shanglun Li, Toby Kenney, Hong Gu — [State Space Modeling of the Ornstein-Uhlenbeck Process with Measurement Error: An Application to Microbiome Data](http://arxiv.org/abs/2610.25266v1)
  <details><summary>📄 Abstract</summary>
  Understanding the temporal dynamics of the human microbiome is critical for deciphering host-microbe interactions and identifying responses to environmental or physiological disruptions. In this study, we develop a likelihood-based framework grounded in Ornstein-Uhlenbeck (OU) state-space modeling to analyze longitudinal microbiome data. By applying log-ratio transformations to genus-level relative abundances, we accommodate the compositional nature of microbiome profiles and enable biologically...
  </details>

- **2026-10-18** — Run Shao, Zhaoyang Zhang, Ziyu Li et al. — [Visual Scaffolding: Toward Native Multimodal Reasoning](http://arxiv.org/abs/2610.25247v1)
  <details><summary>📄 Abstract</summary>
  The success of chain-of-thought (CoT) in complex reasoning can be attributed to a textual scaffolding effect: explicit intermediate results can be examined, reused, and composed to support subsequent reasoning, much as scaffolding supports a building under construction. However, mainstream multimodal LLMs lack an equivalent scaffold for visual distinctions that are difficult to express in concise verbal descriptions. We therefore ask: Can native visual representations become first-class citizens...
  </details>

- **2026-10-18** — Tsvetomila Mihaylova, Arto Hellas, Bita Akram et al. — [It's Complicated: Factors Influencing the Effectiveness of LLM-Generated Feedback in a Live Programming Course](http://arxiv.org/abs/2610.25244v1)
  <details><summary>📄 Abstract</summary>
  We report on three iterations of an LLM-generated feedback system deployed in a live web development course, spanning three underlying models and three feedback formats. We ask how feedback presence and its characteristics (length, complexity, format) relate to student performance, whether prior feedback exposure is associated with final-project performance, and how performance changes after first exposure. Feedback was associated with more favorable immediate outcomes in several comparisons, bu...
  </details>

- **2026-10-18** — Simon Josef Durstewitz — [Concept Representations in Vector Space: Toward an Interdisciplinary Study of Meaning Variation](http://arxiv.org/abs/2610.25184v1)
  <details><summary>📄 Abstract</summary>
  An increasing number of disciplines recognize the explanatory potential of meaning-bearing mental structures through which individuals interpret the world and guide their behavior. Concept representations constitute a core class of these structures, emerging from individuals' experiences with concept referents and encoding and organizing their understanding of them. Recognizing a private level of meaning, where concepts are not objectively defined by rules in the world but constitute subjective ...
  </details>

- **2026-10-18** — Minsung Hwang, Donggyu Yoon, Gowoon Hwang et al. — [Dialogue Generation for Conversational Recommendation Using User Search Interactions and Knowledge Graphs](http://arxiv.org/abs/2610.25182v1)
  <details><summary>📄 Abstract</summary>
  Large-scale conversational recommendation datasets typically require manual dialogue construction or annotation. We propose SearCl, which automatically generates conversational recommendation dialogues grounded in user search and click behaviors. SearCl segments user interactions into query sessions and derives each recommendation target from content selected after a search query. A configurable probabilistic state machine controls the dialogue flow, while two LLM agents acting as the seeker and...
  </details>

- **2026-10-18** — Jianghao Yin, Lang Yu, Qianxi Yu et al. — [PLANE: Plug-and-Play Fine-Grained Visual Experts for Hallucination Mitigation in Large Vision-Language Models](http://arxiv.org/abs/2610.25146v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) commonly suffer from hallucinations, which appear as fabricating non-existent objects or outputting incorrect attributes and spatial relationships in images. Previous works empirically indicate that CLIP-style vision encoders tend to focus on primary objects while ignoring image details, which is one of the causes of hallucinations. To address this issue, we propose plug-and-play fine-grained visual experts (PLANE) comprising two components: LoRA visual exper...
  </details>

- **2026-10-18** — Amirhossein Ghaffari, Susanna Pirttikangas, Ekaterina Gilman — [Spectral Adaptive Graph Transformer for Efficient and Scalable Traffic Forecasting](http://arxiv.org/abs/2610.25140v1)
  <details><summary>📄 Abstract</summary>
  Traffic forecasting models based on spectral graph convolution offer an interpretable account of how information is mixed between sensors, but they rely on an eigendecomposition of the graph Laplacian. It costs cubic time, is fixed by the road network, and provides a symmetric operator that cannot represent the directed propagation of traffic congestion. Attention-based spatio-temporal transformers remove these limitations but generate a dense sensor-by-sensor attention map at each layer and tim...
  </details>

- **2026-10-18** — Reaz Hassan Joarder, Sidratul Tanzila Tasmi, Alif Arshad Bakshi et al. — [MoWE: Spatially Adaptive Mixture-of-Wavelet-Experts Pooling for Ultrasound Lesion Segmentation](http://arxiv.org/abs/2610.25074v1)
  <details><summary>📄 Abstract</summary>
  We present Mixture-of-Wavelet-Experts (MoWE), a spatially adaptive routing mechanism that replaces max-pooling and strided convolutions in U-Net architectures for ultrasound lesion segmentation. Standard pooling operations suppress high-frequency spatial details, including potential boundary cues in speckled regions. Recent frequency-domain methods preserve some of these details, but a single wavelet family applies the same spectral bias across the image. MoWE instead uses a context-aware router...
  </details>

- **2026-10-18** — Jörg Frochte, Herbert Schmidt — [LLM Agents as Suppliers of Physical System Models: Calibration and Acceptance in Modelica](http://arxiv.org/abs/2610.25019v1)
  <details><summary>📄 Abstract</summary>
  To procure a model of a device, a client hands a supplier a description, sometimes with recorded data or a target response, and accepts the model against this handover. We let LLM coding agents act as the supplier on handovers with data, building Modelica models from library components for four simulated systems and a real switching magnet, and ask what acceptance certifies. Several agents reach the noise floor, but a handover admits a set of models: the description leaves parts of the structure...
  </details>

- **2026-10-17** — Jinxiang Xie, Yijian Zhang, Qingyuan Yi et al. — [ReTRACE: Feedback-Guided LLM Agent in a Chemistry Harness for Retrosynthesis Planning](http://arxiv.org/abs/2610.24744v1)
  <details><summary>📄 Abstract</summary>
  Computer-aided retrosynthesis has advanced through single-step prediction, tree search and route scoring, but complex targets still require judgement over the whole route, where stereochemistry, functional-group compatibility, cost and greenness interact. Here we present \textbf{\mbox{ReTRACE}} (\textbf{RE}trosynthesis with \textbf{T}ool-orchestrated \textbf{R}easoning \textbf{A}nd \textbf{C}ontext-aware \textbf{E}vidence), an agent that places a large language model (LLM) in a chemistry harness...
  </details>

- **2026-10-17** — Boyi Liu, Yite Wang, Xinyu Lian et al. — [Arctic-SWE: Revisiting the Long Horizon Agent Training by Modeling-System Co-Design](http://arxiv.org/abs/2610.24914v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agent training, including software engineering, is advancing rapidly, but the recipe and infrastructure needed for a strong reinforcement-learning baseline remain difficult to reproduce. This makes gains from new algorithms or data hard to distinguish from improvements to an under-tuned baseline. We present Arctic-SWE, a fully asynchronous RL framework that establishes such a baseline through model-system co-design, using overfitting on a small task pool as the testbed. This testbed...
  </details>

- **2026-10-17** — Riddhi Chatterjee, Ritish Shrirao, Kushagra Mehrotra et al. — [Goal Images Are Control Targets: Spatially-Grounded Goal-Image Synthesis for Robotic Manipulation](http://arxiv.org/abs/2610.24885v1)
  <details><summary>📄 Abstract</summary>
  Goal-conditioned manipulation policies are steered by a goal image, a picture of the desired post-manipulation scene synthesized from the current observation and a language instruction. The prevailing assumption is that better image-editing quality yields better goals, so goal generators are built and compared using general image-editing metrics. We show this assumption is false. Across two independent goal-conditioned policies on CALVIN, the image editors that top aggregate editing-quality lead...
  </details>

- **2026-10-17** — Hongxiao Jin — [Logistic vegetation trajectories and their implications for land surface phenology](http://arxiv.org/abs/2610.24879v1)
  <details><summary>📄 Abstract</summary>
  Vegetation trajectories describe canopy development and underpin phenological metrics, including the start and end of the growing season. We derive a generalized logistic function (GLF) to represent canopy growth under explicit assumptions: exponential development combined with a Michaelis-Menten-type saturating response yields an ordinary logistic function, and a power transformation introduces asymmetry. Using the GLF as a common mathematical basis, we relate trajectory shape to phenological m...
  </details>

- **2026-10-17** — Shafeef Omar, Sebastian Sanokowski, Elham Daneshmand et al. — [DiPLO: Self-distilled Diffusion Planning for Loco-manipulation](http://arxiv.org/abs/2610.24847v1)
  <details><summary>📄 Abstract</summary>
  Humanoid loco-manipulation is particularly challenging because it requires coordinating locomotion, balance, and object interaction, making it difficult to learn from limited demonstrations or from scratch through Reinforcement Learning (RL). We introduce DiPLO (self-distilled Diffusion Planning for Loco-manipulation), a framework that combines a self-distilled diffusion planner with a low-level whole-body tracking policy. Our planner is pretrained via supervised learning on motions derived from...
  </details>

- **2026-10-17** — Sankalp Parashar, Preethi Jyothi, Sunita Sarawagi — [Ask, Don't Guess: Targeted Clarification for Speech Recognition Errors](http://arxiv.org/abs/2610.24809v1)
  <details><summary>📄 Abstract</summary>
  Speech recognition in real time in far-field conversational settings still incurs significant errors. Identifying potential error spans during streaming ASR permits a recourse mechanism where the speaker can be asked to repeat the affected content under cleaner acoustic conditions. We propose \sysname, a new framework for online error localization, that identifies spans likely to benefit from this intervention. Our supervision uses clean audio to estimate how the recognizer's output might change...
  </details>

- **2026-10-17** — Sadhvikas Addamane, Sanghyeok Park, Quinn T. Campbell et al. — [Epitaxial Displacement-etched GaAsSb Quantum Dots Emitting at Telecom Wavelengths](http://arxiv.org/abs/2610.24768v1)
  <details><summary>📄 Abstract</summary>
  Semiconductor quantum dots (QDs) are essential components for integrated photonic and quantum information systems, yet current epitaxial growth techniques face significant limitations in complexity of growth, material selection, and density tunability. Here we report a displacement etch technique that enables controlled formation of GaAsSb QDs with emission at telecommunications wavelengths. Our approach uses arsenic molecular flux (As$_2$) to react with antimonide surfaces through thermodynamic...
  </details>

- **2026-10-17** — SeongJun Jeong, Junghyun Kim, Gi-Cheon Kang et al. — [DialogMem: Evaluating Dialogue-Grounded Embodied Memory in 3D Environments](http://arxiv.org/abs/2610.24767v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents in human-centered environments require memory that integrates what they observe with what humans tell them over time. However, existing embodied memories are built primarily from visual experience, leaving open how dialogue with humans can be grounded in the objects encountered throughout that experience. We introduce DialogMem, a two-phase benchmark in which agents build memory from time-aligned streams of posed RGB-D observations and dialogue, and later use it for instance-leve...
  </details>

- **2026-10-17** — Sumit Anthony Gomes, Yasin Rahman, Taeeba Tasnia et al. — [BanglaBBQ: A Bias Benchmark for Question Answering in the Bangladeshi Context](http://arxiv.org/abs/2610.24764v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces BanglaBBQ, a question-answering bias benchmark designed to capture stereotypes grounded in the Bangladeshi context, in both Bangla and English. Following KoBBQ and PakBBQ, BanglaBBQ adapts the original Bias Benchmark for Question Answering (BBQ) by classifying its templates into three groups: directly translated (DT), modified to align target groups or contexts with Bangladesh (TM), and removed when deemed unsuitable for the Bangladeshi context (SR). This process retains 14...
  </details>

- **2026-10-17** — Martim Monis, Martin Schwaighofer, Nuno Saavedra et al. — [Vibenix: Agentic Software Packaging and Maintenance with Nix](http://arxiv.org/abs/2610.24712v1)
  <details><summary>📄 Abstract</summary>
  Implicit dependencies, uncontrolled network access, and other build-environment impurities create intransparent software supply chains. Identifying every dependency affecting a build is a difficult task. Functional package management addresses this through reproducible packaging, ensuring software relies exclusively on declared, hermetically isolated inputs. However, creating build recipes remains complex and time-consuming, posing a significant barrier to adoption for developers and maintainers...
  </details>

- **2026-10-17** — Yunhui Liu, Xudong Jin, Qizhuo Xie et al. — [Uncovering Semantic Hierarchies in Text-Attributed Graphs via Variational EM-based LLM-GNN Synergy](http://arxiv.org/abs/2610.24624v1)
  <details><summary>📄 Abstract</summary>
  While hierarchical structures are intrinsic to organizing human knowledge, current representation learning on text-attributed graphs predominantly operates on flat semantic spaces, overlooking the rich coarse-to-fine granularity inherent in real-world data. To bridge this gap, we propose SHiFT, which synergizes the reasoning power of LLMs with the structural representation capability of GNNs within an Expectation-Maximization (EM) paradigm. In the E-step, we harness LLMs as expert taxonomists to...
  </details>

- **2026-10-17** — Yutang Lin, Guanya Shi, C. Karen Liu — [Action-Aligned Latent Planning for Versatile Humanoid Loco-Manipulation](http://arxiv.org/abs/2610.24675v1)
  <details><summary>📄 Abstract</summary>
  Learning a single perceptive policy for diverse humanoid loco-manipulation requires unifying high-level task decisions without losing the state-dependent physical responses that make each interaction succeed. This makes the representation between high-level planning and whole-body control critical: kinematic or contact targets provide compact abstractions but do not directly encode interaction-specific control responses, while directly predicting low-level actions requires the planner to model h...
  </details>

- **2026-10-17** — Daniil Gurgurov, Akansh Maurya, Josef van Genabith et al. — [Compositional Activation Steering Across Languages and Behaviors with Contextual Gates](http://arxiv.org/abs/2610.24906v1)
  <details><summary>📄 Abstract</summary>
  Activation steering has emerged as an effective and precise way to influence the behaviours of language models. However, composing multiple steering directions to control several behaviours simultaneously remains challenging, particularly in multilingual settings and with training-free steering vectors. We address this challenge with contextual steering, jointly training gates that adapt the strength of fixed steering directions to the current hidden state and interactions between interventions....
  </details>

- **2026-10-17** — Wesley Lu, Runzhou Liu, Hongru Du et al. — [Pattern-Driven Evaluation of LLM Code Optimization: Isolating Compiler-Transcendent Semantic Reasoning](http://arxiv.org/abs/2610.24835v1)
  <details><summary>📄 Abstract</summary>
  Existing evaluations of LLM-based code optimization primarily measure end-to-end speedup, obscuring whether a model actually performs the intended optimization. For compiled languages, this is especially problematic: observed gains may reflect transformations already recoverable by modern optimizing compilers rather than optimization behavior attributable to the model itself. We present PatternBench, a benchmark for studying compiler-transcendent optimization, i.e., performance improvements that...
  </details>

- **2026-10-17** — Xujun Che, Farsheed Haque, Depeng Xu et al. — [Who Gets Unmasked? Sampler-Induced Bias in Diffusion Language Models](http://arxiv.org/abs/2610.24795v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (dLLMs) generate by gradually unmasking a canvas, so their samplers decide not only which token to write but also when to commit it. We show that this second decision changes who appears in generated text, a sampler-induced bias on top of the model's own. Common commit rules, including LLaDA's default, commit the positions whose sampled tokens are most probable; this peeking favors majority options. To separate the sampler from the model, we read the model's belief abou...
  </details>

- **2026-10-17** — Haowen Bai, Rui Gong$, Meichen Liu et al. — [MM-LeJEPA: Correlated Gaussian Regularization for Multimodal Joint-Embedding Predictive Architectures](http://arxiv.org/abs/2610.24681v1)
  <details><summary>📄 Abstract</summary>
  LeJEPA derives an isotropic Gaussian embedding target by minimizing, under its task assumptions, a Fisher information criterion that controls the task-averaged squared prediction bias. This enables unimodal self-supervised learning without reconstruction decoders, exponential-moving-average teachers, or contrastive negatives. However, its isotropic task prior does not account for the cross-modal structure of multimodal tasks that read shared content. We introduce MM-LeJEPA by extending LeJEPA's ...
  </details>

- **2026-10-17** — Megh Shukla, Edo Collins, Prashanth Chandran et al. — [Modeling Uncertainty Propagation in 3D Morphable Models](http://arxiv.org/abs/2610.24646v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of mapping parameter-space variance of a 3D Morphable Model (3DMM) to per-vertex variance. Traditionally, per-vertex variance has been used to visually interpret the learnt parameter uncertainty. However, mapping parameter-space variance to per-vertex using sampling or error propagation is computationally expensive. We address this limitation with Closed-form Local Uncertainty Estimation (CLUE), which transforms the parameter-space distribution of 3DMMs to per-vertex through...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 687 |
| prompt-injection | 626 |
| memory-poisoning | 55 |
| tool-use-attack | 157 |
| backdoor | 528 |
| adversarial-attack | 639 |
| privacy-leakage | 4408 |
| steganography | 80 |
| misuse | 1202 |
| red-teaming | 143 |
| vulnerability | 3649 |
| defense | 3526 |
| alignment | 3308 |
| robustness | 3586 |
| watermark | 629 |
| unlearning | 116 |
| agent-safety | 65 |
| benchmark | 69 |
| survey | 408 |
| other | 9659 |

---

📚 **全部 33540 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

⚠️ **本次更新跳过：arXiv API 爬取失败，数据为上次缓存。下次 CI 将自动重试。**

*Generated by AgentGuard at 2026-10-21 03:41:50*