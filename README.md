<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-33807-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-21 11:01 ｜ **论文总数 / Total Papers**: 33807（近 30 天 / Recent 30 days: 5308）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 33807 篇论文（含摘要、分类筛选、搜索）/ View all 33807 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 687
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 629
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 56
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 158
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 530
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 643
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4427
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 80
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1214
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 144
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3683
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3554
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3338
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3617
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 632
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 116
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 65
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 70
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 411
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 9753

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 5308 篇，完整 33807 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 5308 papers from the last 30 days (with date, authors & abstract). For the full list of 33807 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

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


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 7 papers

- **2026-10-20** — Zhiyue Xu, Xukai Wang, Zhiyuan Huang et al. — [After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents](http://arxiv.org/abs/2610.28425v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM agents persist state across sessions via two channels: long-lived memory files silently prepended to the system prompt, and scheduled tasks waking the agent without user input. A one-time indirect prompt injection committed to either channel can re-fire across sessions long after the attacker leaves, threats we term carryover attacks. Existing prompt-injection benchmarks evaluate attacks only in the session where malicious content is first observed, leaving the gate governing when and...
  </details>

- **2026-10-20** — Abhishek Rai — [Context-Aware Prompt Injection Detection via Small Language Models in RAG Pipelines: nokast-secureRAG](http://arxiv.org/abs/2610.28364v1)
  <details><summary>📄 Abstract</summary>
  Local Retrieval-Augmented Generation (RAG) systems are vulnerable to indirect prompt injection and retrieval poisoning, where malicious instructions in retrieved content are mistaken for trusted input. We present nokast-secureRAG, a roughly 0.5B-parameter small language model that acts as a semantic firewall between retrieval and generation. It jointly evaluates the user query and retrieved context, classifying the pair as safe, suspicious, or malicious. The model is trained using a teacher-judg...
  </details>

- **2026-10-20** — Vasisht Duddu, Adam Caulfield, Xi He — [KNOX: Hardware-assisted Regulatory Sandbox for Generative Models](http://arxiv.org/abs/2610.27543v1)
  <details><summary>📄 Abstract</summary>
  Regulations require companies to run AI models in a regulatory sandbox, an isolated environment that enables monitoring model behavior by regulators, prior to deployment. But, they do not spell out the technical mechanisms to design such a sandbox. Ideally, a regulatory sandbox should show (i) compliance (checks against regulations, and deviations from intended behavior, i.e., unauthorized tool and system calls); (ii) confidentiality (protects model weights from regulators); (iii) attestability ...
  </details>

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


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-10-20** — Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique et al. — [ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents](http://arxiv.org/abs/2610.28093v1)
  <details><summary>📄 Abstract</summary>
  AI agents keep long-term memory, much of which comes from web pages and tool results. Agent harnesses, the software that runs the model, do not record who may act on this memory, so an instruction hidden in a fetched page can be treated as the user's own instruction. We propose ClawMMU, a protection layer that labels every piece of memory with its owner, scope, origins, and authority. ClawMMU checks these labels whenever content enters the model's context, is written to storage, returns from sto...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-10-19** — Nataša Krčo, Euodia Dodd, Peter Romov et al. — [You Are the Trigger: Speaker-Activated Backdoors](http://arxiv.org/abs/2610.27210v1)
  <details><summary>📄 Abstract</summary>
  Speech models are increasingly used as an interface to AI systems, from transcription tools to voice agents. Existing audio backdoors require an attacker to introduce triggers at inference time. We study a different threat model in which the attacker compromises the model during fine-tuning but has no access to the victim's inference-time inputs. We introduce the Speaker-Activated Backdoor (SAB) setting, in which a target speaker's natural voice serves as the trigger. We develop a two-phase fine...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 4 papers

- **2026-10-20** — Masahiro Kaneko — [Poisoning-Based Backdoors Are Not Cryptographic](http://arxiv.org/abs/2610.28045v1)
  <details><summary>📄 Abstract</summary>
  To defend against backdoor attacks on neural networks, the defender must identify the verifier function that determines whether an input is a trigger, rather than rejecting individual triggers in isolation, since an attacker can generate new triggers satisfying the same verifier faster than they can be blocked. If a backdoor verifier could be installed with the asymmetry of a cryptographic authentication scheme, in which only the attacker can produce trigger inputs while the defender cannot reve...
  </details>

- **2026-10-19** — Qi Pang, Hanshen Xiao, Andre Manoel et al. — [Guided Diffusion for Trustworthy Synthetic Text Generation](http://arxiv.org/abs/2610.27259v1)
  <details><summary>📄 Abstract</summary>
  The rapid evolution of Large Language Models is fueled by massive datasets, yet this reliance poses severe privacy risks, as models can inadvertently memorize and even directly output sensitive training data. Synthetic text generation offers a promising solution to this challenge; however, existing methods struggle to reconcile rigorous privacy guarantees with high data utility. In this paper, we propose a new paradigm for private synthetic text generation: Guided Diffusion. Leveraging the uniqu...
  </details>

- **2026-10-19** — Jonibek Mansurov, Sholpan Bolatzhanova, Filbert Aurelian Tjiaranta et al. — [Selective Transfer through Sequence Distillation: From Benchmark Knowledge to Backdoor Behaviour](http://arxiv.org/abs/2610.26311v1)
  <details><summary>📄 Abstract</summary>
  Knowledge distillation is widely used to transfer capabilities from teacher models to student models, but recent work shows that it can also transfer unintended teacher properties. We study whether different hidden teacher properties survive the same distillation channels. Specifically, we compare two properties: benchmark-associated knowledge and refusal backdoors, and show that distillation treats them very differently. Teachers fine-tuned on benchmark data successfully pass that knowledge to ...
  </details>

- **2026-10-18** — Nanjun Zhou, Yiming Li, Yukun Chen et al. — [SEAL: Towards Persistent Tool Poisoning Attack against LLM Agents via Prefix-Eliciting Trigger](http://arxiv.org/abs/2610.25372v1)
  <details><summary>📄 Abstract</summary>
  Tool poisoning has emerged as a critical security threat to LLM agents, where adversaries embed malicious instructions in tool descriptions or external resources that enter the agent's context, allowing adversaries to manipulate agent's tool selection process. However, existing tool poisoning attacks primarily rely on an idealized assumption that the attacks task effect within a single interaction round. We show that their effectiveness degrades sharply in realistic multi-round agentic settings....
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-10-20** — Mihaela-Larisa Clement, Tosca Pierro, Ezio Bartocci et al. — [Enumeration-Guided Training of Neural Hamilton-Jacobi Safety Certificates](http://arxiv.org/abs/2610.27870v1)
  <details><summary>📄 Abstract</summary>
  Hamilton-Jacobi (HJ) reachability analysis offers formal safety guarantees for control systems, but training accurate neural certificates remains difficult, particularly when unsafe regions are hard to characterize. We propose a verification-guided training framework that addresses this by using probabilistic enumeration of safety constraints to detect forward-invariance violations, i.e., states where the learned certificate incorrectly classifies unsafe behavior. This produces a compact, target...
  </details>

- **2026-10-19** — Leo Elmecker-Plakolm, Lukasz Szpruch, Avishek Joey Bose et al. — [Exposing Vulnerability Monoculture Through Systemic Adversarial Robustness](http://arxiv.org/abs/2610.27353v1)
  <details><summary>📄 Abstract</summary>
  Beneath the apparent diversity of foundation models lies an increasingly homogeneous technical stack of common training pipelines, distillation methods, and data. These shared algorithmic choices can expose an otherwise distinct model ecosystem to concentrated risks leading to a vulnerability monoculture. Yet current practice in assessing adversarial robustness is restricted to individual robustness scores and attack transfer rates, leaving open the unexplored fundamental question: how many atta...
  </details>

- **2026-10-19** — Shruthi Gowda, Nikita Jain, Elahe Arani et al. — [Language Guidance for Supervised Vision Training: An Empirical Study of Generalization](http://arxiv.org/abs/2610.27208v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks have achieved remarkable success on vision benchmarks, yet they continue to struggle with many generalization challenges. Supervised vision training relies on one-hot labels, which provide limited information about semantic structure and shared attributes between classes. This limited supervision can leave visual representations vulnerable to distribution shifts, spurious correlations, texture bias, adversarial perturbations, and forgetting in sequential learning settings. W...
  </details>

- **2026-10-19** — Yuyang Zhang, Kangjie Chen, Yihui Jin et al. — [Model Exposure on One Device Endangers Others: Rethinking Edge Neural Network Security across Devices](http://arxiv.org/abs/2610.27152v1)
  <details><summary>📄 Abstract</summary>
  Neural networks (NNs) are increasingly deployed on edge devices such as mobile and IoT platforms, offering low latency and improved privacy compared to cloud-based deployment. However, on-device models embedded in mobile applications can be unpacked and exposed to adversaries, enabling cross-node attacks in centrally distributed ecosystems, where adversarial examples crafted on one compromised device transfer effectively to other nodes sharing the same models. To address this threat, we propose ...
  </details>

- **2026-10-19** — Manohar Kaul, Sadbhavana Babar, Aditya Ramesh et al. — [Provable Adversarial Detection: Prime Quantization meets Gromov--Wasserstein](http://arxiv.org/abs/2610.26102v1)
  <details><summary>📄 Abstract</summary>
  Adversarial vulnerability persists across modern vision architectures from CNNs to vision language models (VLMs), yet existing detection methods rely on heuristics without theoretical guarantees. We address the fundamental question of when adversarial perturbations can be provably detected from a geometric perspective. Our key insight is that adversarial perturbations cannot simultaneously preserve geometric structure across spaces with fundamentally different properties. Accordingly, we constru...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 27 papers

- **2026-10-20** — Mohammad Kachuee, Phu Mon Htut, Sheng Li et al. — [MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems](http://arxiv.org/abs/2610.28397v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI extends large language models (LLMs) from generating responses to planning and executing complex workflows, substantially expanding their utility while exposing applications to unsafe actions, information leakage, and adversarial manipulation. Multi-agent systems further expand these capabilities through specialization and collaboration, but distributed authority, heterogeneous roles, and opaque or potentially compromised participants make safeguarding even more challenging. Existing ...
  </details>

- **2026-10-20** — Masahiro Kaneko, Hiromi Arai, Timothy Baldwin — [Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory](http://arxiv.org/abs/2610.28315v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly use persistent memory to personalize responses, and personal attributes in this memory pose a privacy risk if exposed. We ask how consulting memory during dialogue changes what users go on to say, and thus what the memory comes to reveal. In multi-session simulations, a simulated user with 24 personal attributes talks with a support agent that does or does not consult memory, and in both settings attributes are inferred from the full accumulated rec...
  </details>

- **2026-10-20** — Devansh Srivastav, David Pape, Samira Abedini et al. — [Contextual Candour: Role-Aware Graduated Disclosure for LLMs over Mixed-Sensitivity Contexts](http://arxiv.org/abs/2610.28067v1)
  <details><summary>📄 Abstract</summary>
  LLMs increasingly operate over mixed-sensitivity contexts, where they must reason over information ranging from public to confidential while disclosing only what the user is authorised to receive. Existing approaches enforce access control as a binary decision: either fully answering or refusing, without regulating how much or what kind of information is revealed if access is granted, leading to over-refusal or unintended leakage. We introduce graduated disclosure, an access-control formulation ...
  </details>

- **2026-10-20** — Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang et al. — [Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](http://arxiv.org/abs/2610.27548v1)
  <details><summary>📄 Abstract</summary>
  When an LLM agent acts on behalf of a user, it is expected to act within the authorization scope the user grants. Existing agent evaluations largely measure task completion or harmful consequences and can therefore overlook actions that violate this delegation without producing conventional safety or privacy harms. We introduce AuthorizationBench, a benchmark of authorization alignment grounded in documented real-world cases. A scalable construction pipeline produces 286 executable tasks spannin...
  </details>

- **2026-10-20** — Hanieh Totonchi Asl, Ebrahim Nouri, Zhuoran Li et al. — [Interflow: Breaking the Offline-Online Barrier for Private AI at the Edge](http://arxiv.org/abs/2610.27431v1)
  <details><summary>📄 Abstract</summary>
  Privacy-preserving machine learning (PPML) offers a promising path toward bringing powerful AI services to the edge without exposing sensitive user data. However, its practical deployment remains constrained by the high communication, computation, and data-movement costs of secure multi-party computation (MPC), particularly during nonlinear inference. Existing MPC systems typically decouple input-independent correlated randomness generation from online execution, creating substantial memory pres...
  </details>

- **2026-10-20** — Bo Liu, Tong Li, Jiapeng Zhang et al. — [Beyond Trajectory Statistics: Community-Consistent Human Mobility Generation via Evolving User-Location Graphs](http://arxiv.org/abs/2610.28467v1)
  <details><summary>📄 Abstract</summary>
  Human mobility data are fundamental to Web-based location services and broader urban applications, and mobility generation provides synthetic trajectories when real data are costly or inaccessible. Although recent mobility generators have incorporated collective mobility patterns, they primarily focus on individual trajectories and aggregate population dynamics, leaving evolving community structures formed by user-location interactions insufficiently modeled. In this paper, we study community-co...
  </details>

- **2026-10-20** — Rohan James, Ioannis Christofilogiannis, Yuuv Jauhari et al. — [Beyond a Single Sentiment Score: Topical and Affective Dimensions of Emoji Meaning on Twitter](http://arxiv.org/abs/2610.28337v1)
  <details><summary>📄 Abstract</summary>
  Emoji are widely treated as compact affective tokens whose meaning is summarised by a single sentiment score. We argue that this picture is incomplete. From a corpus of 16{,}575 English tweets and a per-emoji metric we call \emph{stability delta} (within-class minus between-class cosine similarity of sentence embeddings), we show that emojis used in tightly clustered topical contexts also exhibit \emph{more} polarised crowd-sourced sentiment, not less. Validated against the Kralj Novak et al.\ (...
  </details>

- **2026-10-20** — Raghav Bongole, Amirreza Zamani, Tobias J. Oechtering et al. — [Lower bounds for Bayesian CVaR in interactive problems with local differential privacy](http://arxiv.org/abs/2610.28153v1)
  <details><summary>📄 Abstract</summary>
  We develop an information-theoretic method for lower bounding the prior-predictive conditional value-at-risk (CVaR) of loss in interactive statistical decision making (ISDM). A generalized Fano inequality replaces a single error event by a randomized binary statistic constructed from a bounded transform of the loss, reducing the problem to a Bernoulli $f$-divergence inequality. A bounded hinge transform yields a direct lower bound on Bayesian CVaR under a prior fixed in advance. We derive revers...
  </details>

- **2026-10-20** — Anna-Maria Halacheva, Jan-Nico Zaech, Sombit Dey et al. — [P$^3$-VLM: A Point-based Alternative for Grounded 3D Vision-Language Models](http://arxiv.org/abs/2610.28018v1)
  <details><summary>📄 Abstract</summary>
  Examining existing benchmarks for grounding in 3D VLMs reveals a pervasive "semantic leakage" in the evaluation and prompting protocols: a heavy reliance on bounding boxes as spatial prompts or representation primitives. Because bounding boxes are highly informative of object categories, they introduce a shortcut for the models to neglect visual information during 3D VLM training. We demonstrate this with a "blind" LLM that, prompted only with the box coordinates, can perform surprisingly well. ...
  </details>

- **2026-10-20** — Rajarshi Bhattacharya, Aryan Shukla, Shakeeb Murtaza et al. — [In PRAISE of Attributes: Grounding Retrieval Geometry with Query-Conditioned Subspaces for Person Re-Identification](http://arxiv.org/abs/2610.27944v1)
  <details><summary>📄 Abstract</summary>
  Person re-identification (ReID) ranks an image gallery using either an image query or a textual query. In image-to-image (I2I) ReID, viewpoint, illumination, occlusion, and background changes can make distractors appear more similar than the true match. In text-to-image (T2I) ReID, incomplete or ambiguous descriptions may omit key visual evidence. We study this problem for vision-language model (VLM) based ReID, where attributes such as clothing color and carried objects provide useful fine-grai...
  </details>

- **2026-10-20** — Pengying Wu, Zhejia Wen, Kang Ding et al. — [CovNav: Conformal Prediction-Guided Adaptive Inference for Object Goal Navigation](http://arxiv.org/abs/2610.27677v1)
  <details><summary>📄 Abstract</summary>
  In object goal navigation (ObjectNav), an embodied agent must find a target object (e.g., "find a bed") in a previously unseen environment, relying on spatial commonsense such as object co-occurrence. Large Language Models (LLMs) encode this commonsense, but deploying them on robots exposes a trade-off between reasoning quality and efficiency: cloud-based models incur latency and privacy risks, whereas small on-device LLMs are fast but prone to hallucinated spatial judgments. Hybrid reasoning LL...
  </details>

- **2026-10-20** — Ruoyao Zhang, Hongxuan Li, Jie Peng et al. — [Ensemble-Aware Structural Encoding (EASE): Conditioning Protein Encoders on Peptide Conformational Ensembles](http://arxiv.org/abs/2610.27638v1)
  <details><summary>📄 Abstract</summary>
  Protein foundation models provide transferable representations for downstream peptide prediction tasks. However, existing representations typically reduce a peptide to a single sequence or structure, which may miss conformational variability relevant to key peptide properties, including antibacterial activity, hemolysis, toxicity, stability, and binding. For example, protease resistance correlates more strongly with conformational dynamics measured by hydrogen exchange than with average helicity...
  </details>

- **2026-10-20** — Tao Yang, Chengxi Yang, Ben J. Sekely et al. — [Ultra-Fast 4H-SiC AC-LGAD for 4D Tracking Applications](http://arxiv.org/abs/2610.27535v1)
  <details><summary>📄 Abstract</summary>
  4H-SiC low gain avalanche detectors (LGADs) combine internal gain with the high carrier saturation drift velocity, thermal stability, and low leakage current of SiC. AC-coupled readout (AC-LGAD) adds position information to the precise timing, which enables 4D tracking. This work reports the first experimental demonstration of a 4H-SiC AC-LGAD. Devices with a $1.0\times1.0$~mm$^2$ active area and a $2\times2$ array of AC-coupled pads at a pitch of 500~$μ$m were fabricated with two gain-layer dop...
  </details>

- **2026-10-20** — Laurent Mombaerts, Jonathan Taws, Jacopo Gargano et al. — [Training-Free Continual Learning for Multimodal Forecasting via Prompt Evolution](http://arxiv.org/abs/2610.27468v1)
  <details><summary>📄 Abstract</summary>
  Adapting a forecasting system to a changing world classically means retraining. We ask whether the task of continually learning regimes for time series forecasting can be represented by a piece of text: a guidance block, evolved by outcome-driven reflection and used in a frozen LLM forecaster's prompt. On a refreshed multimodal benchmark (weekly search indices, daily currencies, daily commodities, each window paired with web-retrieved news), we run GEPA-style prompt evolution under strict contam...
  </details>

- **2026-10-19** — Wenyue Chen, Yuhan Cheng, Ruixin Yang et al. — [Steering Vision-Language Models for Visual-Contextual Privacy in Location Disclosure](http://arxiv.org/abs/2610.27323v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can infer sensitive information such as geolocation from subtle visual cues, creating privacy risks when responses disclose more detail than the visual context warrants. We study visual-contextual privacy in geolocation disclosure, where a VLM should reveal location information only at the granularity appropriate to the visual context depicted in the image. We first show that this contextually appropriate granularity is recoverable from pre-generation hidden states,...
  </details>

- **2026-10-19** — Mingchen Li, Zifan Peng, Kewei Sha et al. — [Profile-DP: Differential Privacy for User-Controlled Profile Release in Personalized LLM Inference](http://arxiv.org/abs/2610.27213v1)
  <details><summary>📄 Abstract</summary>
  Personalized large language models (LLMs) increasingly rely on profile-conditioned inference, pairing public requests with rich, user-specific facts. This paradigm exposes the user profile itself, together with the user's explicit sharing preferences. We introduce Profile-DP, a policy-aware local differential privacy framework designed specifically for user-profile release in personalized LLM inference. Profile-DP provably bounds the release of user-withheld facts while treating public instructi...
  </details>

- **2026-10-19** — Oussema Dhaouadi, Zuria Bauer, Johannes Michael Meier et al. — [MatchCityLoc: Aerial Localization in LoD City Models via Surface Normal Matching](http://arxiv.org/abs/2610.27110v1)
  <details><summary>📄 Abstract</summary>
  Autonomous Unmanned Aerial Vehicle (UAV) navigation in urban environments requires precise pose estimation. Because Global Navigation Satellite System (GNSS) signals are often unreliable in cities, visual localization serves as a crucial complement. Within this domain, textureless Level-of-Detail (LoD) city models provide a lightweight and privacy-preserving substitute for heavy 3D textured meshes. However, localizing against abstract geometry is challenging. Existing pipelines typically score 2...
  </details>

- **2026-10-19** — Yuxuan Chen, Yang Xiao, Jack Sun et al. — [Beyond Two Tracks: Speaker-Anchored Full-Duplex Dialogue Recovery](http://arxiv.org/abs/2610.27109v1)
  <details><summary>📄 Abstract</summary>
  Spoken interaction is moving from alternating turns to full-duplex conversation, where an agent listens while speaking. Learning this coordination requires natural dialogue with persistent speaker-resolved tracks, a data requirement that remains difficult to satisfy at scale. Generative recovery offers a route from ordinary recordings, but recovering two voices is not enough: their track assignments can drift as the conversation unfolds. We address this missing link with speaker-anchored routing...
  </details>

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

- **2026-10-18** — Jingshen Zhang, Bo Wang, Yanlin Fu et al. — [Do LLMs Really Lack Difference Awareness? Uncovering Heuristic Substitution in Group-Differentiating Fairness](http://arxiv.org/abs/2610.26961v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we investigate the issue of difference awareness in LLMs, defined as a model's ability to recognize and acknowledge meaningful differences between social groups in fairness decision-making. Previous studies have consistently shown that models perform poorly on such tasks, a finding commonly attributed to a lack of difference awareness. We propose an alternative account, which we term Fairness Heuristic Substitution: difference awareness is not necessarily absent, but the complex d...
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


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-10-18** — Rui Meng, Song Gao, Tingting Zhu et al. — [SemVideoSte: Agentic AI for Cross-Modal Semantic Video Steganography Communication](http://arxiv.org/abs/2610.25257v1)
  <details><summary>📄 Abstract</summary>
  We propose an agentic artificial intelligence (AI)-driven cross-modal semantic video steganography communication (SemVideoSte) scheme for secure cross-modal information transmission. Agentic AI interprets the service context to determine a semantically matched public prompt and coordinates video generation, message embedding, semantic transmission, and message recovery process. A multi-mask mechanism combines variational autoencoder (VAE) reconstruction robustness, semantic transmission robustne...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 24 papers

- **2026-10-20** — Diego Miguel Lozano, Erik Derner, Juan Antonio Pérez-Ortiz et al. — [Polarity Blindness in LLM Safety: A Systematic Study of Negation, Antonym Substitution, and Adversarial Framing](http://arxiv.org/abs/2610.27908v1)
  <details><summary>📄 Abstract</summary>
  Negation remains a persistent challenge for language models across NLP tasks and modalities. We show that this weakness can undermine LLM safety guardrails through a structural vulnerability we term polarity blindness: the failure to recognize harmful intent after polarity-altering linguistic transformations. We study two forms of polarity inversion: grammatical negation and antonym replacement, and use synonym replacement as a polarity-preserving control. We further test whether an adversarial ...
  </details>

- **2026-10-20** — Niccolò Ronchetti — [Orthogonal Boundary Unlearning for Dual-Use Concepts in Large Language Models](http://arxiv.org/abs/2610.27490v1)
  <details><summary>📄 Abstract</summary>
  Mitigating catastrophic risks from large language models requires excising hazardous operational capabilities, such as cyberwarfare exploitation and pathogen enhancement, without degrading benign scientific utility. In these dual-use domains, legitimate defensive science and malicious attacks share vocabulary, syntax, and internal model representations, causing standard unlearning methods to induce severe collateral damage (concept bleeding).   In this work, we present Orthogonal Boundary Unlear...
  </details>

- **2026-10-20** — Kayode L. Ogunsusi — [Securing Agentic Commerce Through Behavior-Aware Fraud Detection and Cybersecurity for Trusted AI-Agent Payment Authorization](http://arxiv.org/abs/2610.27483v1)
  <details><summary>📄 Abstract</summary>
  The growing use of autonomous artificial intelligence agents in digital commerce creates new security concerns involving agent impersonation, unauthorized payments, compromised agents, and misuse of delegated authority. This research introduces the Autonomous Commerce Agent Guard System (ACAGS), a cybersecurity framework combining supervised machine learning, behavioral analytics, agent-specific authorization controls, and explainable AI. The framework was evaluated using synthetic financial tra...
  </details>

- **2026-10-20** — Zijian Yu, Hangwei Zhang, Jun Lan et al. — [WildAIGC-Bench: Can AI Image Detectors Handle the Wild? A Benchmark of Generated and Edited Images in Online Circulation](http://arxiv.org/abs/2610.28087v1)
  <details><summary>📄 Abstract</summary>
  AI-generated images linked to news events and online claims can mislead audiences, enable fraud, or cause public controversy. We introduce WildAIGC-Bench, built through recurring collection across news websites, fact-checking sources, and related social media content. The pipeline combines broad coverage, timely updates, and human-verified labels through scheduled discovery, automatic screening and preliminary annotation, and human review of image-specific evidence. The benchmark contains 407 ve...
  </details>

- **2026-10-20** — Yali Du, Yunji Zhang, Ming Li — [Hallucinations of Large Language Models in Cross-Language Code Translation: Phenomena and Mitigation](http://arxiv.org/abs/2610.27868v1)
  <details><summary>📄 Abstract</summary>
  Code translation converts source code from one programming language to another while preserving its functionality. Although Large Language Models (LLMs) have improved code translation, their outputs still contain hallucinations: generated code that conflicts with the source program, violates target-language facts, or introduces contextually inconsistent dependencies. These failures are especially harmful in translation because small semantic deviations can silently change program behavior. Exist...
  </details>

- **2026-10-20** — Hayden Moore, Abhinav Verma, Anshuman Dutt — [Tracing Recurrent and Emergent Hallucination Patterns in Decomposed Text-to-SQL Generation](http://arxiv.org/abs/2610.27720v1)
  <details><summary>📄 Abstract</summary>
  Large language models can achieve strong Text-to-SQL benchmark performance while still producing schema and query-logic errors. Most evaluations characterize such failures only in the final generated query, making it difficult to determine whether a related error was also observed in an earlier, simpler step or appears only at the final stage. We present a drill-down evaluation framework that decomposes Text-to-SQL queries into progressively more complex executable sub-queries and corresponding ...
  </details>

- **2026-10-19** — Aidan Sirbu, Charles Y. Zhang, Yuanjia Yang et al. — [A latent control model for realistic rodent motion](http://arxiv.org/abs/2610.27279v1)
  <details><summary>📄 Abstract</summary>
  The development of embodied models of animal behavior is a major goal of the neuro-AI community. Embodied models will enhance our ability to make direct comparisons between biological and artificial agents. To make such comparisons effective, though, we need embodied models that actually move like animals. Previous work has developed virtual animal bodies and techniques for training realistic motion through imitation. However, to date, there is no system for embodied animal modeling that produce...
  </details>

- **2026-10-19** — Arnav Grover — [Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops](http://arxiv.org/abs/2610.27350v1)
  <details><summary>📄 Abstract</summary>
  Frontier models can control robots through agent harnesses that loop on one question: what motion comes next toward the user's goal? We show that this default loop carries out harmful instructions. With GPT-6 Astra controlling a low-cost SO-101 arm through the Inspect Robots harness on three household tasks whose hazard is common knowledge, such as "put the knife in the toy basket", the policy refused 0% of 15 trials, attempted the harm every time, and completed it in 27%. Its one exit, give_up,...
  </details>

- **2026-10-19** — Jalil Alva, David Harper, Abigail E. Thornton et al. — [Global Security Blind Spots: Translation as a Safety Bypass in Low-Resource Languages](http://arxiv.org/abs/2610.27304v1)
  <details><summary>📄 Abstract</summary>
  Large language models are deployed globally, yet safety alignment and evaluation remain concentrated in English: harmful requests refused in English can elicit unsafe completions when translated into low-resource languages. We evaluate ten widely deployed LLMs across 79 languages (English plus 78 low-resource) under a translation-bypass threat model, using a metric conditioned on English safety, which separates translation bypass from unsafety already present in English. English safety does not ...
  </details>

- **2026-10-19** — Chenhan Lyu, Amir Rahmani — [Auditing Safety Preference Supervision with Recorded Derivations](http://arxiv.org/abs/2610.27266v1)
  <details><summary>📄 Abstract</summary>
  Preference labels align model training, but the judgments behind them are difficult to inspect or verify. In this paper, we examine how preference construction can be checked when intermediate decisions are recorded, and which of them remain uncertain. We present Symbolic Preference Labeling, a method in which a pretrained language model classifies predefined attributes of prompts and responses. Explicit rules assign response verdicts, and a fixed verdict ranking determines the preference label....
  </details>

- **2026-10-19** — Carson Sobolewski, Anjali Parashar, Fei Chen et al. — [What Would Removing This Corruption Change? Failure Attribution for Vision-Language-Action Models](http://arxiv.org/abs/2610.27277v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models are sensitive to visual corruptions, but knowing that a corruption is typically harmful does not establish whether removing it would benefit the current episode. Furthermore, when several corruptions co-occur, deciding what to correct requires understanding which ones contribute to failure risk and how much their removal would help. We define this problem as failure attribution. Detecting corruption presence alone cannot answer this question, as corruptions ca...
  </details>

- **2026-10-19** — Yanan Ma, Yang Wang, David Le et al. — [Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams](http://arxiv.org/abs/2610.27227v1)
  <details><summary>📄 Abstract</summary>
  Cooperative language-model agents can improve without weight updates by revising reusable skills, but only if a shared team reward is traced to the responsible agent and skill. Existing methods credit the skills present in each trajectory, yet presence is not responsibility: a harmful skill active in successful runs still earns positive credit. We present \textbf{GRSE}, \textbf{G}roup-\textbf{R}elative \textbf{S}kill \textbf{E}volution, which assigns behavioral credit by comparison: inspired by ...
  </details>

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


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-10-19** — Hao Li, Tongyan Hu, Weidi Luo et al. — [AutoRedClaw: Automated Red-Teaming for Claw-Style Agents](http://arxiv.org/abs/2610.27244v1)
  <details><summary>📄 Abstract</summary>
  Agent systems are shifting from task-scoped tool-use agents to persistent, personalized assistants such as OpenClaw. These claw-style agents maintain configuration files (e.g., AGENTS.md), long-term memory, and reusable skills. Once poisoned, this persistent state is repeatedly reloaded into the agent's context, creating persistent threats across tasks and sessions. Existing security evaluation systems struggle to evaluate these complex claw-style systems since they rely heavily on manually cons...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 59 papers

- **2026-10-20** — Maria Victoria Carro, Denise Alejandra Mester, Facundo Nieto et al. — [Humans Correct Their Judgments Through Debate, but Weaker AI Models Do Not](http://arxiv.org/abs/2610.28539v1)
  <details><summary>📄 Abstract</summary>
  How can we effectively oversee AI systems that surpass human intelligence? AI Safety via Debate proposes that two AI systems argue opposing positions and a judge, either a human or a weaker model, decides which is correct. By facilitating supervisors in providing high-quality training signals, debate aims to encourage truthful and safe behavior from AI systems whose capabilities exceed our own. However, human judgment is not neutral: people often rely on biases which advanced AI systems may lear...
  </details>

- **2026-10-20** — Vita Santa Barletta, Danilo Caivano, Gabriel Cellammare et al. — [A Digital Twin to Improve Cyber-Social Impact](http://arxiv.org/abs/2610.28430v1)
  <details><summary>📄 Abstract</summary>
  The increasing complexity of Industrial Control Systems (ICS) and their integration with IT infrastructures has significantly expanded the cyber threat landscape. Traditional cybersecurity models, primarily based on the Confidentiality, Integrity, and Availability (CIA triad), fail to capture the broader societal and operational impacts of cyberattacks. This paper proposes a novel framework that integrates Digital Twin technology with a Cyber-Social Security model to simulate, analyze, and quant...
  </details>

- **2026-10-20** — Yulong Li, Jiale Meng, Zhenlin Guo et al. — [Fast and scalable multi-GPU sliced FFT solvers for asymptotically compatible discretizations of 3D nonlocal diffusion problems](http://arxiv.org/abs/2610.28372v1)
  <details><summary>📄 Abstract</summary>
  Large-scale 3D peridynamic transient diffusion simulations are constrained by the computational cost and memory requirements of nonlocal interactions. We propose a fast and scalable multi-GPU sliced FFT algorithm based on the recently developed asymptotically compatible finite difference (ACFD) scheme. By exploiting the discrete operator's structure and finite interaction range, the algorithm combines FFT acceleration with local inter-GPU communication. It preserves the ACFD scheme while avoidin...
  </details>

- **2026-10-20** — Juntang Wang, Hao Wu, Yihan Wang et al. — [Recommending Bacterial Cultivation Conditions from 16S rRNA](http://arxiv.org/abs/2610.28310v1)
  <details><summary>📄 Abstract</summary>
  Recommending bacterial cultivation conditions from sequence data is a challenging structured problem characterized by missing standardized benchmarks and limited use of sequence structure. To address this, we introduce DSNI, a benchmark of 65,023 bacterial strains with phylogeny-aware splits, pairing 16S rRNA sequences with four cultivation conditions (media, temperature, pH, oxygen). Exploiting the mosaic structure of 16S rRNA, where hypervariable regions support discrimination and conserved re...
  </details>

- **2026-10-20** — Youwei Zhou, Bohan Hou, Yankai Fu et al. — [Large Multimodal Models for Direct Robot Control: GPT-6 as a Beginning](http://arxiv.org/abs/2610.28259v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in visuospatial understanding and agentic reasoning enable direct robotic manipulation with general-purpose multimodal models, but their embodied capabilities remain poorly understood. This paper systematically evaluate GPT-6 Astra for closed-loop robotic manipulation using a lightweight agent execution framework. We first probe three fundamental embodied capabilities-depth perception, embodied in-context learning, and tactile understanding-and demonstrate that the model can expl...
  </details>

- **2026-10-20** — Christopher Conrad, Deepak Panda, Weisi Guo et al. — [Interruption-Aware Recurrent Reinforcement Learning for UAS Navigation Under Temporary Overrides](http://arxiv.org/abs/2610.28121v1)
  <details><summary>📄 Abstract</summary>
  Safe autonomous navigation of UASs requires tactical deconfliction to address conflicts that strategic coordination cannot prevent. This task is challenging under partial observability, when sensor or traffic data are missing, delayed, or degraded. Geometry-based methods can offer separation assurances but face limitations in dense encounters. Recurrent reinforcement learning has therefore been proposed to learn navigation policies that integrate observation-action histories to optimise long-ter...
  </details>

- **2026-10-20** — Yousra Fettach, Tijl De Bie — [BAIT: Can LLMs Find What Biases a Reader? A Benchmark for Cognitive Bias Triggers in News](http://arxiv.org/abs/2610.28092v1)
  <details><summary>📄 Abstract</summary>
  Persuasive writing exploits cognitive biases, recruiting a reader's mental shortcuts to shape belief, often without the reader noticing. We call the linguistic features exploiting such mental shortcuts cognitive bias triggers. As large language models (LLMs) increasingly mediate how people encounter news, summarizing it, ranking it, and answering questions over it, a natural question is whether they can recognize the features of a text that bias a human reader. We introduce BAIT (Bias Annotation...
  </details>

- **2026-10-20** — Jarek Liesen, Matthew T. Jackson, Benjamin Ellis et al. — [MoDDiT: Simple Token Routing in Diffusion Transformers](http://arxiv.org/abs/2610.28086v1)
  <details><summary>📄 Abstract</summary>
  Real-time video generation, interactive world models, and on-device image synthesis are almost a reality. Diffusion Transformers (DiT) achieve excellent sample quality, shifting the bottleneck to the throughput of the models themselves. Natural images are inherently sparse, as large portions of an image are often background, contribute little to the scene content, and are easy to denoise. DiTs fail to exploit this sparsity, as they process image tokens statically and uniformly. We propose MoDDiT...
  </details>

- **2026-10-20** — Aleksandr Shestakov, Vladimir Aletov, Aleksandr Beznosikov — [On Johnson-Lindenstrauss Transforms for Byzantine-Robust Optimization](http://arxiv.org/abs/2610.27989v1)
  <details><summary>📄 Abstract</summary>
  The growing scale of data and models in machine learning calls for efficient optimization methods. Distributed optimization addresses this challenge, with compression mechanisms helping to reduce communication costs. A classical tool for dimensionality reduction is the Johnson-Lindenstrauss (JL) transform, which is simple to implement and offers strong geometric guarantees. In particular, JL transforms approximately preserve inner products and pairwise distances between vectors with high probabi...
  </details>

- **2026-10-20** — Byeonghun Bang, Sangwoo Park, Jinheon Baek et al. — [Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay](http://arxiv.org/abs/2610.27954v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large (vision) language models have enabled computer-use agents that automate digital workflows via fine-grained keyboard and mouse operations. However, such agents remain fragile in long-horizon settings, where errors accumulate and executed actions leave unintended side effects, making the ability to recover from failures critical. Yet, existing remedies remain inadequate: environment resets are infeasible in proprietary settings, action replay is prohibitively expensive ove...
  </details>

- **2026-10-20** — Peng Zhang, Tingfa Xu, Jinrui Sui et al. — [S$^3$E-Det: A Strict Spatial-Spectral Equivariant Detector for Multispectral Object Detection](http://arxiv.org/abs/2610.27882v1)
  <details><summary>📄 Abstract</summary>
  Multispectral object detection requires detectors to exploit material-dependent spectral responses while maintaining consistent localization under geometric variations. Existing MOD detectors learn discriminative spectral representations, yet lack a unified mechanism that preserves spectral order, adapts spectral-context fusion across pyramid levels, and regulates geometric responses under rotation. To address these limitations, we propose S$^3$E-Det, a strict spatial-spectral equivariant detect...
  </details>

- **2026-10-20** — Olivier Nourry, Yoshiki Higo — [RELAY: Scaling Historical Build Restoration through Rule Reuse and Agentic Repair](http://arxiv.org/abs/2610.27784v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability benchmarks and software engineering research depend on rebuilding historical software. Yet builds rely on external resources, such as base images and packages, that change independently of the source code. In this study, we examine this environment decay on 14,159 OSS-Fuzz cases. We find that 69.7% no longer complete reconstruction and verification, and that most failures share a small number of recurring failure symptoms. A recurring failure can therefore be diagnosed once and its...
  </details>

- **2026-10-20** — Junyu Wang, Tianrui Wang, Meng Ge et al. — [AD-Mamba: Architecture-Complementary Knowledge Distillation for Efficient and Robust Audio Classification](http://arxiv.org/abs/2610.27713v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in large-scale audio classification have been primarily driven by Transformer-based architectures due to their strong capacity in modeling long-range dependencies. However, their inherent quadratic complexity limits scalability and efficiency, especially when processing long or sparsely informative audio streams. Mamba, a recently proposed state space model (SSM), offers a promising alternative by enabling efficient long-range modeling with linear sequence scaling. Neverthele...
  </details>

- **2026-10-20** — Wenjie Gan, Zhaoxi Zhang, Jiahui Liang et al. — [Enhancing Bug-Exposing Test Generation via Step-Level Credit Assignment and Self-Distillation from Valuable Failures](http://arxiv.org/abs/2610.27694v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models have shown strong code generation capabilities, yet their outputs often contain subtle bugs. Automatically repairing such code requires informative tests: inputs that expose faulty behavior, paired with correct expected outputs. Recent RL-based test generation methods apply the same outcome reward to all reasoning steps, which can discourage useful reasoning and reinforce flawed steps. They also fail to effectively learn from trajectories that find bug-triggering inputs but...
  </details>

- **2026-10-20** — Romina Omidi, Nima Naderloui, Yuan Hong et al. — [A Unified Attack Framework against Statistical Generative Watermarks for Large Language Models](http://arxiv.org/abs/2610.27653v1)
  <details><summary>📄 Abstract</summary>
  Watermarking has emerged as a key tool for identifying text generated by large language models (LLMs), with current schemes embedding statistical signals into the generation process to enable later detection. In this work, we identify a shared weakness across a broad class of popular LLM watermarking methods, including KGW (and its variants), GumbelSoft, DipMark, ITS, and SynthID. We show that these schemes exhibit a fundamental link between their detection scores and the token probability shift...
  </details>

- **2026-10-20** — Jing Wang, Yitong Yang, Hao Dou et al. — [TriGeoBench: A Multimodal Mathematical Geometry Benchmark with Figures and TikZ](http://arxiv.org/abs/2610.27626v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models show strong vision-language capabilities, yet their geometry-centric reasoning remains insufficiently understood. Existing mathematical benchmarks typically rely on rasterized figures and cover limited geometric knowledge areas and response formats, making it difficult to assess whether models reason over geometric structures or exploit superficial visual patterns. We introduce TriGeoBench, a geometry-centric multimodal benchmark constructed from Chinese middle- ...
  </details>

- **2026-10-20** — Tongrun Xing, Yongjun Dai, Xuan Liao et al. — [Bridging Digital Deception and Physical Fidelity: A Spatio-Temporal Attack on Cognitive Radars](http://arxiv.org/abs/2610.27585v1)
  <details><summary>📄 Abstract</summary>
  As cognitive radars evolve towards the end-to-end processing of one-dimensional complex baseband sequences, deep networks face severe adversarial threats. However, existing attacks encounter dual limitations in practical electronic warfare: low cross-architecture transferability and severe vulnerability to physical channel distortions, which degrades their tactical reliability. To overcome these bottlenecks, we propose a physical prior-driven Segmented Spatio-Temporal Attack (SSTA). First, a glo...
  </details>

- **2026-10-20** — Maosen Zhang, Jianshuo Dong, Yutong Zhang et al. — [The Show-Up Attack: When Subagents Win Over Their Supervisor](http://arxiv.org/abs/2610.27574v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems are increasingly deployed to coordinate multiple large language model (LLM) agents. However, this also creates new attack surfaces: malicious agents may have chances to exploit the coordination. In this paper, we propose and study the \textit{show-up attack}, in which a malicious subagent manipulates the supervisor into involving it in tasks beyond its assigned scope. To evaluate this risk, we propose SUA-Arena, which implements 6 attack strategies and contains 188 test cases...
  </details>

- **2026-10-20** — Sadia Asif, Israel Antonio Rosales Laguan, Shumaila Asif et al. — [When LLMs Manipulate: Measuring Behavioral, Social, and Temporal Effects](http://arxiv.org/abs/2610.27573v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can influence user trust and decision-making through subtle linguistic cues, yet the behavioral effects of manipulative outputs remain poorly quantified. We introduce a behavioral computing framework for measuring \textit{behavioral vulnerability}, defined as users' susceptibility to manipulative AI responses. Building on DarkPatterns-LLM benchmark, we generate controlled manipulative stimuli using Manipulation Gradient Descent (MGD), targeting biases associated with...
  </details>

- **2026-10-20** — Thomas E. Coons, Aniket Jivani, Xun Huan — [Active Pilot Sampling for Multi-fidelity Estimation in Stochastic Optimization](http://arxiv.org/abs/2610.27563v1)
  <details><summary>📄 Abstract</summary>
  Stochastic optimization with high-fidelity nonlinear models is often computationally prohibitive because each objective evaluation requires sampling-based uncertainty quantification inside an outer optimization loop. Multi-fidelity estimators, such as approximate control variates (ACV), can reduce this cost by exploiting cheaper low-fidelity models, but they require model-output covariance information to determine control-variate weights and sample allocations. These covariances are generally un...
  </details>

- **2026-10-20** — Hao Yan, Guanghui Wang — [Progressive Subset Selection and Cascaded Consistency for Unsupervised Vision-Language Model Adaptation](http://arxiv.org/abs/2610.27515v1)
  <details><summary>📄 Abstract</summary>
  Pretrained Vision-Language Models (PVLMs) achieve strong zero-shot recognition but often suffer performance degradation under target-domain shift. Unsupervised adaptation provides a practical way to improve target-domain performance without labeled data, but it remains challenging because pseudo-labels generated by the model can be unreliable and no labeled validation set is available for model selection or early stopping. We propose a simple framework for unsupervised PVLM adaptation that combi...
  </details>

- **2026-10-19** — Nishant Abhishek, Ping Charoenwet, Kla Tantithamthavorn — [AgenticVulHunter: Bringing Local Agentic Vulnerability Hunting to Your Terminal](http://arxiv.org/abs/2610.27383v1)
  <details><summary>📄 Abstract</summary>
  Finding vulnerabilities early, before they can affect the production system, is important for reducing the risk of any software attacks. However, detecting vulnerabilities during secure code review is still difficult because the vulnerable code logic may depend on lines found across different repository files. Recent approaches such as AgenticSCR have shown that LLM agents can explore repository files and use security knowledge to improve secure code review. However, these approaches mainly rely...
  </details>

- **2026-10-19** — Saptaparna Bhattacharya — [Pretraining on boosted boson decays for polarization tagging of hadronic $W$ bosons](http://arxiv.org/abs/2610.27346v1)
  <details><summary>📄 Abstract</summary>
  Longitudinally polarized weak bosons probe the unitarization of vector-boson scattering. At large boosts, longitudinal and transverse $W$ bosons produce jets with the same mass and two-prong structure, distinguished only by the decay angle. Longitudinal bosons are rare: they occur in only 0.3% of $W$+jet events at these large boosts. We ask where the polarization information of a boosted $W$ boson lies and how much a tagger can recover. Requiring both decay quarks within the jet truncates the de...
  </details>

- **2026-10-19** — Zerui Chen, Changrui Chen, Fei Ni et al. — [Look Before You Reason: Implicit Visual Thinking for Efficient Multimodal Reasoning](http://arxiv.org/abs/2610.27341v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have advanced rapidly in multimodal reasoning, yet they remain limited on tasks requiring fine-grained understanding of small or easily overlooked image regions. Recent thinking with images approaches mitigate this limitation by allowing models to inspect images through operations such as zooming, cropping, or code execution. While effective, their multi-turn interactions with VLMs introduce redundant token computation and slow inference, and separate region inspect...
  </details>

- **2026-10-19** — Pablo P. Rejo, Manuel Fernández-Veiga, Ana Fernández-Vilas et al. — [Orchestrating Key Scarcity: Global Capacity Allocation in Hybrid QKD-PQC Networks](http://arxiv.org/abs/2610.27332v1)
  <details><summary>📄 Abstract</summary>
  This article presents a Distributed Key Management System (DKMS) that provisions quantum-safe symmetric encryption keys to applications across a network. To overcome the distance and rate limitations inherent to Quantum Key Distribution (QKD), the architecture adopts a hybrid design: it utilizes multi-hop trusted relays for physical key transport, while applying an end-to-end Post-Quantum Cryptography (PQC) layer to ensure the relayed key material remains strictly protected from intermediate nod...
  </details>

- **2026-10-19** — Hyunji Alex Nam, Michael Dennis, Natasha Jaques et al. — [Evolving Self-tuning Benchmarks for Long-Horizon Tool Use](http://arxiv.org/abs/2610.27307v1)
  <details><summary>📄 Abstract</summary>
  For AI assistants to move beyond simple chat interfaces and reliably assist users with applications like Gmail, Venmo, and Slack, we need to improve their tool-use capabilities. However, existing tool use benchmarks are still limited and difficult to scale because they rely on human supervision or are too domain-specific. To make data generation scalable, we propose, TURTLE (**T**ool **U**se **R**elated **T**asks with **L**ong-Horizon **E**volution), an Unsupervised Environment Design (UED) appr...
  </details>

- **2026-10-19** — Taozheng Zhu, Shixiong Jiang, Fanxin Kong — [Vulnerability Analysis for Safe Multi-Agent Reinforcement](http://arxiv.org/abs/2610.27293v1)
  <details><summary>📄 Abstract</summary>
  Safe Multi-Agent Reinforcement Learning (SMARL) aims to learn cooperative control policies under prescribed safety constraints. Al- though existing SMARL methods focus on enforcing safety during policy optimization, their vulnerability remains largely unexplored. This paper investigates inference-time observation attacks against SMARL, where an adversary perturbs the observations of a subset of agents, thereby altering the actions produced by their policies. We propose MinMax Attack, an attack f...
  </details>

- **2026-10-19** — Rui Melo, Andre Catarino, Claudia Mamede et al. — [When Models Know but Can't Linearly Say: Relational Encoding Limits Linear Vulnerability Classification in Code LLMs](http://arxiv.org/abs/2610.27257v1)
  <details><summary>📄 Abstract</summary>
  Large language models can detect vulnerable code, yet the form of vulnerability encoding in their representations remains unclear. We analyze 8 code models spanning 6.7B-15B parameters on C programs using three datasets (DELTASECOMMITS, SVEN, and PRECISE-BUGS), comparing two diagnostic tasks on the same representations: identifying what patterns the code instantiates, and determining whether it is vulnerable. Models encode the first with high fidelity. Under the studied paired C-code datasets an...
  </details>

- **2026-10-19** — Ameya D. Jagtap — [Glass-Box Deep Reinforcement Learning for High-Speed Flow Control](http://arxiv.org/abs/2610.27132v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement learning (DRL) is challenging long-held assumptions in active flow control. By learning directly from interaction with a flow, DRL agents can find actuation strategies for nonlinear, unsteady flows without explicit models, often exploiting mechanisms that classical control would not anticipate. High-speed flows are a demanding test of this promise: shocks, shock/boundary-layer interactions, transition, aerothermal loading and microsecond-scale dynamics strain both algorithms a...
  </details>

- **2026-10-19** — Rajneil Baruah, Subhadeep Mondal, Sunando Kumar Patra et al. — [This is SParTA: A modular, efficient and scalable transformer architecture for jet-tagging](http://arxiv.org/abs/2610.27106v1)
  <details><summary>📄 Abstract</summary>
  We present the Sparse Particle-interaction Transformer Architecture (SParTA), a modular, scalable, and efficient transformer for jet tagging at high-energy colliders. Exploiting the steeply falling transverse-momentum ($p_T$) spectrum of jet constituents, SParTA factorizes constituent processing into two topological regimes. Ordered by descending $p_T$, only the $N$ hardest constituents (the hard core) participate in quadratic $O(N^2)$ differential interaction attention driven by pairwise physic...
  </details>

- **2026-10-19** — Osama Shabih, Dayam Nadeem, Shahab Saquib Sohail et al. — [Fluent but Fallible: Benchmarking Hallucination and Factual Reliability in Large Language Models](http://arxiv.org/abs/2610.27034v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have significantly advanced natural language processing and artificial intelligence applications through their capabilities in reasoning, text generation and knowledge retrieval. However, LLMs are still vulnerable to two important challenges: hallucination, generating factually incorrect or fabricated content, and response deviation, meaning systematic deviations from ground-truth responses. These limitations raise serious concerns regarding reliability and trustwort...
  </details>

- **2026-10-19** — Phurinat Polasa, Thanapon Thanadunpremdet, Phatthanasak Kraiduang et al. — [Teaching AI Agent to Play Poker Strategically Through Preference Optimization](http://arxiv.org/abs/2610.27028v1)
  <details><summary>📄 Abstract</summary>
  A poker agent can make a legal move and still make a strategically poor one. We ask whether compact AI agents can exhibit strategic behavior under hidden information and whether preference optimization can improve beyond static and zero-shot policies. We first evaluate a static baseline and three frozen language models: SmallThinker, Qwen3, and Gemma-3 whose performance varies substantially between exact-game and six-player evaluation. We therefore propose Strategic Preference Optimization with ...
  </details>

- **2026-10-19** — Tue Le, Anh Nguyen Hoang, Gabriel Sasseville et al. — [Secure Agentic Coding through Counterexample-Grounded Feedback](http://arxiv.org/abs/2610.25916v2)
  <details><summary>📄 Abstract</summary>
  As coding models and agent harnesses become more capable, reliable security verification is becoming a central bottleneck. Improving secure code generation requires a signal whose reported progress remains aligned with actual program behavior under optimization; otherwise, an optimizer can improve the signal's verdict without removing the underlying vulnerability. Existing model-based approaches require models to either infer program behavior from source code or specify correct outcomes for adve...
  </details>

- **2026-10-19** — Qihao Wang, Hang Su, Fan Cui et al. — [Think Before You Transcribe: Context-Steered Reasoning for Hotword-Aware Speech Recognition](http://arxiv.org/abs/2610.26986v1)
  <details><summary>📄 Abstract</summary>
  Contextual automatic speech recognition (ASR) improves rare-entity recognition by supplying candidate hotwords, but retrieved candidates may be incomplete or incorrect. A reliable system must therefore exploit a relevant candidate without allowing unsupported alternatives to override the acoustic evidence. We propose a context-steered reasoning framework that generates a short, audio-grounded caption before transcription. This task-specific representation lets the model assess candidate relevanc...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 50 papers

- **2026-10-20** — Vlad Mihal, Hosam Alamleh, Alessandro Cantelli-Forti — [Make the Adversary Spend More Energy: Generative Deception against Language-Model Attackers in Critical Infrastructure](http://arxiv.org/abs/2610.27739v1)
  <details><summary>📄 Abstract</summary>
  Language-model attackers consume computational resources as they explore and interact with a target, creating an opportunity for cyber deception to impose costs. Whether such engagements favor the defender requires measuring both sides. We evaluate an autonomous language-model attacker against a decoy that uses a defending language model to analyze attacker commands and select defensive responses. Across 330 sessions, eight model pairs, two attacker profiles and three counter-injection levels, b...
  </details>

- **2026-10-20** — Kaiwen Zhou, Udari Madhushani Sehwag — [RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process?](http://arxiv.org/abs/2610.27735v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement, in which frontier AI models work on training the next generation, is quickly becoming a reality. However, the safety of this process has received far less attention than it should. A misaligned model training its successor can shape what that successor knows, how it behaves, and what it wants, and the harm carries forward into the next generation. We study this risk through the lens of AI control. We introduce RSI Control Arena, a testbed in which a frontier model, ac...
  </details>

- **2026-10-20** — Jitendra Solanki, Anand Todkar, Ziran Min — [Semantic Observability for Autonomous Systems Diagnostics](http://arxiv.org/abs/2610.28611v1)
  <details><summary>📄 Abstract</summary>
  Modern distributed microservice deployments generate massive volumes of heterogeneous, multi-format observability logs across physically and logically partitioned infrastructure. Isolating root causes during cascading failures remains an arduous task for Site Reliability Engineers (SREs), bottlenecked by manual keyword filtering and disjointed temporal correlation across monitoring dashboards. We introduce Semantic Observability, an autonomous multi-agent framework that unifies disparate log str...
  </details>

- **2026-10-20** — Shangquan Sun, Wenjun Luo, Xu He et al. — [Agentic Ensemble with Vision-Language Models for Visual Anomaly Detection](http://arxiv.org/abs/2610.28560v1)
  <details><summary>📄 Abstract</summary>
  Visual anomaly detection aims to detect abnormal objects, while anomaly samples are often scarce during model training. Assembling multiple pretrained detectors can help by leveraging their transferable image scores and anomaly maps. However, most existing ensemble methods apply fixed fusion rules over saved predictions which struggle when pretrained detectors clearly disagree due to different training objectives, priors, and visual representations. To this end, we design AnomalyAgent, a post-tr...
  </details>

- **2026-10-20** — Xialie Zhuang, Mingcong Lei, Zunhai Su et al. — [DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems](http://arxiv.org/abs/2610.28522v1)
  <details><summary>📄 Abstract</summary>
  Decision models support routing, guardrails, and output verification in LLM systems. However, item accuracy alone cannot establish whether models make correct decisions across controlled variations or assign reliable confidence to their predictions. We introduce DecisionPivot, a diagnostic benchmark comprising 48 tasks and 40,033 items across seven decision roles. Its core track contains 7,800 items from 13 generated task families, organized into contrast groups with computed answers verified by...
  </details>

- **2026-10-20** — Christoph Riedl, Fernando E. Rosas — [Claims of emergence in AI should be grounded in information decomposition](http://arxiv.org/abs/2610.28479v1)
  <details><summary>📄 Abstract</summary>
  When a language model develops capabilities not traceable to its individual components, when a multi-agent AI system outperforms each agent on its own, or when a human-AI pair succeeds where either fails in isolation, AI researchers describe it as a case of ``synergy'' or ``emergence''. However, these are usually informal assessments not supported by a theoretical framework, making these claims impossible to compare or even meaningfully dispute. Here we argue that \emph{information decomposition...
  </details>

- **2026-10-20** — Tim Bakker, Christos Louizos — [Relative Representations Enable Portable White-Box Monitoring Across Language Models](http://arxiv.org/abs/2610.28366v1)
  <details><summary>📄 Abstract</summary>
  Independently trained autoregressive language models often acquire similar capabilities, but it remains unclear whether their internal representations organize behaviorally relevant information in compatible ways. We show that models do in fact organize information similarly by using specific behavioral probes that operate on compatible representations. This unlocks portable white-box monitoring: a probe developed and validated on one model can be reused when the model changes, without requiring...
  </details>

- **2026-10-20** — Tianyi Lorena Yan, John Hewitt — [Reward Misspecification Degrades Chain-of-Thought Monitorability](http://arxiv.org/abs/2610.28303v1)
  <details><summary>📄 Abstract</summary>
  Monitoring the chain-of-thought (CoT) of language models (LMs) is a key strategy for detecting and preventing misbehaviors for AI safety. As such, it is critical to identify reinforcement learning (RL) practices that lead to unmonitorable chain-of-thought. One such practice may be unavoidable: reward misspecification. As RL environments become more complex, it is infeasible to have perfect verification, and models are rewarded for behaviors that are different from the true task intent. We show t...
  </details>

- **2026-10-20** — Chucheng Xiang, Runze Wang, Zhi Deng et al. — [GALA: Geometry-Aware Language Model for Controllable Object Arrangement](http://arxiv.org/abs/2610.28280v1)
  <details><summary>📄 Abstract</summary>
  Reasoning about fine-grained placement constraints, such as support and containment, is essential for realistic 3D scene creation. It remains a significant challenge for existing methods that rely on simplified object representations like oriented bounding box (OBB), which are blind to the detailed geometry. To address this limitation, we introduce GALA, a geometry-aware language model with explicit point cloud perception for controllable object placement. Our model performs autoregressively by ...
  </details>

- **2026-10-20** — Jiapu Wang — [Temporal Evidence-Parameter Co-Alignment for LLM Reasoning over Temporal Knowledge Graphs](http://arxiv.org/abs/2610.28176v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) often struggle with temporally grounded reasoning because their static parametric memory is misaligned with the dynamic evolution of real-world knowledge. Although RAG and Parameter-Efficient Fine-Tuning (PEFT) provide practical ways to enhance LLMs, they remain insufficient for temporal reasoning. Existing retrieval methods typically prioritize semantic relevance while overlooking temporal validity, event order, and evolutionary dependencies, resulting in evidence t...
  </details>

- **2026-10-20** — Zhipeng Cao, Taoran Wu, Weiru Cui et al. — [Anytime-Valid Runtime Monitoring of Learned Barrier Certificates](http://arxiv.org/abs/2610.27726v1)
  <details><summary>📄 Abstract</summary>
  Learned barrier certificates provide a principled mechanism for establishing safety of stochastic systems, but their validity may deteriorate during deployment when the underlying dynamics differ from those used for training. We propose an anytime-valid runtime monitor that audits a learned barrier certificate using observed closed-loop trajectories. The monitor is intended to detect loss of statistical support for the deployed barrier condition; it does not by itself guarantee detection before ...
  </details>

- **2026-10-20** — Anmol Pandey, Aditya Jain, Liang Chen et al. — [Local Allow, Global Deny: Why Per-Action Authorization Does Not Compose in LLM Agents](http://arxiv.org/abs/2610.27620v1)
  <details><summary>📄 Abstract</summary>
  Autonomous LLM agents act through tools under per-action authorization: a local guard screens each tool call in isolation. We show that local authorization does not compose into global authorization. A compositional authorization failure (CAF) is a locally authorized execution, or a pair of locally authorized executions, that violates a global policy spanning intent, purpose, provenance, consent, and delegation. We characterize CAFs along two axes, expressiveness (single-trace safety versus rela...
  </details>

- **2026-10-20** — Zhikang Chen, Yueqing Sun, Sen Cui et al. — [KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses](http://arxiv.org/abs/2610.27417v1)
  <details><summary>📄 Abstract</summary>
  A failed gaming trajectory reveals that an agent needs intervention, but not necessarily how its execution harness should change. Effective harness adaptation therefore requires gathering diagnostic evidence, rather than merely proposing alternative recovery rules. We present KPHarness, a framework that adapts the external execution harness of a frozen vision-language-action model through knowledge-probing co-evolution. Recovery knowledge supplies context-specific intervention hypotheses that gu...
  </details>

- **2026-10-20** — Yao Huang, Siyuan Chen, Zhenghan Zhou et al. — [Why Static Probes Fail: Context Determines Deception Feature Composition](http://arxiv.org/abs/2610.27577v1)
  <details><summary>📄 Abstract</summary>
  With increasing autonomy, Large Language Models (LLMs) may engage in deceptive behaviors, such as scheming to pursue misaligned goals or sandbagging to escape oversight. Monitoring outputs alone is insufficient, as models can produce seemingly benign responses while harboring misaligned internal objectives. While mechanistic approaches like linear probing are promising, they rely on the assumption that deception corresponds to a single direction in representation space. We demonstrate that such ...
  </details>

- **2026-10-20** — Yue Xu, Xiyang Wang, Hui Liu et al. — [From Tokens to Files: Multi-Granularity Detection and Localization of AI-Involved Code](http://arxiv.org/abs/2610.27863v1)
  <details><summary>📄 Abstract</summary>
  The increasing use of large language models for code generation calls for methods that distinguish purely human-written code from AI-involved code: files in which any part, however small, was generated or substantially modified by a model. Beyond flagging such files, we aim to localize the lines or blocks attributable to AI. Existing approaches compress a file into a single score, from surface stylistic features or a global code representation, which averages away the evidence when only a few bl...
  </details>

- **2026-10-20** — Xu Hu, Haoming Li, Yuxiang Wang et al. — [CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents](http://arxiv.org/abs/2610.27645v1)
  <details><summary>📄 Abstract</summary>
  As computer-use agents (CUAs) move to long-horizon workflows spanning multiple applications, undetected errors can silently corrupt persistent state and cause cascading failures in subsequent actions. Reliable error detection and recovery have become critical bottlenecks for building robust CUAs. However, existing benchmarks focus primarily on end-to-end task performance, providing limited insight into whether agents can detect and recover from errors during execution. The few benchmarks that ev...
  </details>

- **2026-10-20** — Chuanbo Zhu, Run Luo, Weibo Zhao et al. — [AudiPsy: Evidence-Grounded Multimodal Reasoning over Spoken Counseling Conversations for Depression Assessment](http://arxiv.org/abs/2610.27567v1)
  <details><summary>📄 Abstract</summary>
  Depression assessment from counseling speech requires integrating textual and acoustic psychological evidence across turns, yet existing end-to-end classification approaches lack explicit multimodal evidence interpretation and context-aware reasoning. We propose AudiPsy, an evidence-grounded omni-LLM for depression assessment over spoken counseling conversations. AudiPsy employs an Observation-Assessment-Summary (OAS) paradigm to integrate dialogue transcripts, textual and acoustic emotions, and...
  </details>

- **2026-10-20** — Qizhou Wang, Jiawen Zhu, Guansong Pang et al. — [AnomalyJev: Towards Evaluating Image Anomaly Explanations via Claim-Level Verification](http://arxiv.org/abs/2610.27565v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal LLM (MLLM)-based anomaly detection (AD) methods can generate textual explanations that help interpret their predictions. However, reliably and efficiently evaluating these explanations remains challenging. While LLM judges can assess explanations through structured rubrics, they often require substantial token generation, making evaluation costly and difficult to scale. We instead propose to anchor evaluation in the available ground truth by extracting verifiable claims from ea...
  </details>

- **2026-10-20** — Daniel Weiner, Raj Korpan — [Evaluating Social Reasoning in Embodied Vision-Language Models](http://arxiv.org/abs/2610.27496v1)
  <details><summary>📄 Abstract</summary>
  Foundation models now serve as reasoning layers for robot teams, but it remains unclear whether embodiment-specialized vision-language models (VLMs) preserve the social-reasoning capabilities of general-purpose VLMs. We evaluate Gemini Robotics-ER on SHREC, a benchmark of real human-robot social interactions, and compare it with published general-purpose VLM baselines. Robotics-ER outperforms GPT-4o-mini on error/competence detection but performs worse on detailed social-attribute judgments; add...
  </details>

- **2026-10-19** — Alex Clay, Ernesto Jimenez-Ruiz, Pranava Madhyastha — [Looking Into The Past: The Impact of Context on Detecting Deceptive Statements](http://arxiv.org/abs/2610.27407v1)
  <details><summary>📄 Abstract</summary>
  Deception detection typically considers messages in isolation. Previous works in claim verification and role detection have displayed that additional information such as gameplay history is crucial to successful predictions. In this work, we demonstrate the value of preceding gameplay dialogue when applied to deceptive message detection within the hidden role game of Avalon. The findings show that LLMs can see improvement across a number of metrics, including accuracy by up to 31\% with the addi...
  </details>

- **2026-10-19** — Salimeh Sekeh, Mary Wisell — [A Theoretical Analysis of Environment-Aware Out-of-Distribution Detection for Vision-Language Models](http://arxiv.org/abs/2610.27211v1)
  <details><summary>📄 Abstract</summary>
  Continual vision-language models (VLMs) encounter a stream of environments and must also reject inputs that do not belong to the environment at hand.   Class information from earlier environments can aid out-of-distribution (OOD) detection, yet existing detectors score each environment in isolation, and when previous environments help or hurt is theoretically unclear. We develop a theory of environment-aware OOD detection built on contribution scores, pairwise cosine expectations measuring how t...
  </details>

- **2026-10-19** — Chenpan Li, Thies Brockmoeller, Stefanie Jegelka et al. — [On the Fragility of Tasks under Composition: Implicit Budgeting in Language Models](http://arxiv.org/abs/2610.27190v1)
  <details><summary>📄 Abstract</summary>
  Modern language models are increasingly asked to handle several tasks within a single prompt. Doing so requires solving each task correctly while integrating the resulting answers into a coherent response. In this paper, we identify a fundamental limitation in this process, where models make substantially more errors when tasks are composed, even when they can solve every constituent task reliably in isolation. This degradation cannot be fully explained by the accumulation of independent errors....
  </details>

- **2026-10-19** — Bo Yan, Qi Zhang, Ziwen Kan et al. — [PROVISO: Provenance-Informed Action Selection for Secure LLM Agents](http://arxiv.org/abs/2610.27115v1)
  <details><summary>📄 Abstract</summary>
  LLM agents act on the external world through tools and third-party skills, so a single executed action can cause irreversible harm. Existing defenses judge a proposed action without tracking whether its content comes from the user or from external sources such as tool outputs, and they judge it in isolation rather than against an available alternative, which forces a trade-off between security and utility. We present PROVISO, a controller that decides which action to commit after the agent propo...
  </details>

- **2026-10-19** — Christian Kragh Jespersen — [Graph Neural Networks for Astrophysics and Cosmology](http://arxiv.org/abs/2610.27051v1)
  <details><summary>📄 Abstract</summary>
  Physics seldom makes breakthroughs when we consider objects only in isolation. Instead we model and measure how objects sit among their neighbours, spatial, temporal, or otherwise: a galaxy in its environment, a halo in its history, a photon hit in a detector. Graphs are ideally suited for encoding exactly these relations, and Graph Neural Networks (GNNs) learn the geometric functions that respect them. This review presents the use of GNNs for astrophysics and cosmology, and argues that GNNs oft...
  </details>

- **2026-10-19** — Allison Chen, William Yang, Salma Abdel Magid et al. — [Robustness of Internal Signals for Hallucination Detection in Vision-Language Models](http://arxiv.org/abs/2610.27041v1)
  <details><summary>📄 Abstract</summary>
  When given an image and a text prompt, vision-language models (VLMs) can produce seemingly sophisticated text responses. However, they are also prone to hallucinate objects in their output, which can have detrimental consequences in safety-critical applications. To detect these hallucinations, certain methods interestingly leverage internal signals from the VLM as it generates the text response; potentially, these methods use the same signals that led to a hallucination to detect it. We conduct ...
  </details>

- **2026-10-19** — Ruotian Peng, Yuanyi Ren, Shuaiqi Liu et al. — [VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement](http://arxiv.org/abs/2610.26342v2)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) requires agents to diagnose system bottlenecks and coordinate improvements across training and inference. We refer to the agents' capability to jointly optimize training data, the trainer, and the inference harness as cross-component co-design. We introduce VibeTraining-Bench, a benchmark for evaluating this capability across tasks spanning terminal operation, software engineering, multi-turn tool use, and mathematical reasoning. Within each task, research agents...
  </details>

- **2026-10-19** — Sicong Huang, Ian Lane — [SHAM-Bench: A Span-level Hallucination Benchmark Across Multiple Tasks](http://arxiv.org/abs/2610.27370v1)
  <details><summary>📄 Abstract</summary>
  Span-level hallucination detection pinpoints unsupported content in LLM outputs, enabling actionable feedback and targeted mitigation. Existing evaluations for span-level hallucination detection methods are fragmented across tasks, annotation formats, and metrics, and most span-level datasets cover only a single NLG domain, making it difficult to assess whether a detection method actually generalizes across tasks and domains. In this paper, we introduce SHAM-Bench (Span-level Hallucination Bench...
  </details>

- **2026-10-19** — Nikita Gautam, Moana Sargent, Kaitlyn Sievers et al. — [Conversational AI for Perceived Cognitive Decline Screening in Older Adults](http://arxiv.org/abs/2610.27344v1)
  <details><summary>📄 Abstract</summary>
  Early detection of cognitive decline in older adults remains challenging due to the resource demands of standard neuropsychological assessments. Chatbot-based Intelligent Cognitive Assistants (ICAs) provide a scalable alternative by eliciting open-ended responses rich in linguistic, semantic, and autobiographical cues. This study evaluates whether ICA question-answer (Q/A) interviews with older adults can screen for participant-reported perceived cognitive decline and related cognitive, function...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 68 papers

- **2026-10-20** — Chengtao Jian, Kai Yang — [TPO: Tri-level Distributionally Robust Learning for OOD Direct Preference Optimization](http://arxiv.org/abs/2610.28229v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) minimizes empirical risk over observed preference comparisons, implicitly assuming that the training preference distribution matches the deployment preference distribution. In practice, this i.i.d. assumption often fails, as preference distribution shift exhibits a natural hierarchical structure across three levels: group-level shift, prompt-level shift, and preference-level shift. Such multi-level distributional mismatch poses a critical challenge for safe L...
  </details>

- **2026-10-20** — Siyuan Li, Jiayi Zhou, Zhiyuan Xia et al. — [A Neuro-Symbolic Reasoning Engine for Compilation-Free Patch Presence Testing](http://arxiv.org/abs/2610.27871v1)
  <details><summary>📄 Abstract</summary>
  Code reuse in modern software ecosystems facilitates the spread of 1-day vulnerabilities, posing significant security risks. Determining if patches are present is crucial, but traditional methods suffer from limited usability and accuracy, often depending on a fragile compilation process. In our prior work, we introduced Lares, the first compilation-free framework for patch presence testing that combines large language models (LLMs) with SMT solvers. However, Lares treats the LLM and the SMT sol...
  </details>

- **2026-10-20** — Liping Yang, Yongqi Leng, Jingting Zheng et al. — [ABench: Adversarily Benchmarking Large Language Models across Taxonomized Values](http://arxiv.org/abs/2610.27611v1)
  <details><summary>📄 Abstract</summary>
  Ensuring the alignment of Large Language Models (LLMs) with diverse cultural values is critical for their safe global deployment. However, existing alignment benchmarks are predominantly English-centric or confined to simple discriminative tasks. Moreover, they often fail to effectively evaluate model robustness against complex, adversarial inductions within specific cultural contexts. To address these limitations, we propose ABench, a fine-grained, handcrafted benchmark specifically tailored to...
  </details>

- **2026-10-20** — Bingqi Shang, Yang Zhang, Yiwei Chen et al. — [Can Native Safety Travel? Reusing Safety Pretraining Across Models via On-Policy Distillation](http://arxiv.org/abs/2610.27555v1)
  <details><summary>📄 Abstract</summary>
  Safety pretraining has emerged as a promising paradigm for embedding safety deeply into a model during pretraining, yielding robustness to subsequent fine-tuning that conventional safety post-training often lacks. We refer to this safety acquired during model pretraining as native safety. Yet native safety is expensive to acquire, confined to the model in which it was pretrained, and often accompanied by lower general utility. In this work, we rethink the practical value of safety-pretrained mod...
  </details>

- **2026-10-20** — Maoyuan Li, Haoyuan Li, Zhongsheng Wang et al. — [Value-Rich, Differently Organized: Measuring Value Expression and Organization in AI-Generated Debates](http://arxiv.org/abs/2610.28604v1)
  <details><summary>📄 Abstract</summary>
  Current evaluation of LLM-generated debate largely focuses on argumentative quality, leaving the value structure of generated arguments underexamined. We introduce a diagnostic metric framework for comparing how values are expressed and organized in human-reference and AI-generated debates. The framework separates value expression, the range of recognizable values a debate invokes, from value organization, how those values are distributed and sustained across turns. Grounded in Schwartz's Basic-...
  </details>

- **2026-10-20** — Chuyang Ye, Qinting Jiang, Jingyan Jiang — [SenseAlign: Understanding Vision and Touch through Language at Test Time](http://arxiv.org/abs/2610.28511v1)
  <details><summary>📄 Abstract</summary>
  Tactile-visual-language models combine vision and touch through a shared language space to recognize objects and materials. In real-world deployment, changes in lighting, contact quality or sensor hardware can shift visual or tactile inputs and degrade recognition performance. When both modalities contribute to a prediction, an unreliable modality can override correct evidence from the other. Since labeled data are generally unavailable during deployment, test-time adaptation offers a way to rec...
  </details>

- **2026-10-20** — Ning Zhang, Shihao Wang, Jinrui Zhang et al. — [BitMTP: When Multi-Token Prediction Meets Low-Bit Large Language Models](http://arxiv.org/abs/2610.28500v1)
  <details><summary>📄 Abstract</summary>
  For efficient deployment of large language models (LLMs), methods of ultra-low-bit backbones reduce weight storage, memory traffic, and linear-layer execution cost, while multi-token prediction (MTP) methods reduce sequential decoding steps by predicting multiple future tokens in parallel. Although complementary, the direct combination of these methods cannot accelerate decoding at comparable quality: masked drafting lacks intermediate token input supplied in next-token training, while wider com...
  </details>

- **2026-10-20** — Zhenwei Tang, Di Bai, Jintao Liu et al. — [Toolflation: Seller Agents Distort Tool Markets Through Spontaneous Generative Engine Optimization](http://arxiv.org/abs/2610.28454v1)
  <details><summary>📄 Abstract</summary>
  Agents are starting to sell to other agents. Seller agents write the listings of tools, services and products, and buyer agents read these listings when they choose what to use. We show that seller agents told only to be selected more often practice generative engine optimization on their own, and that this distorts the market for sellers and for buyers. We build tool markets from real data tools on Amazon and Instagram and run every tool on every question, so we know which tools can answer each...
  </details>

- **2026-10-20** — Zhenghan Chen, Zekai Shao, Xin Lin et al. — [Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V](http://arxiv.org/abs/2610.28416v1)
  <details><summary>📄 Abstract</summary>
  Code-based video generation offers fine-grained control, targeted editing, and component reuse compared with direct video generation. This approach requires multimodal large language models (MLLMs) to translate visual and temporal requirements into executable programs that produce complete videos. However, existing code-based benchmarks primarily target specialized tasks, leaving complete video creation across diverse creative categories and input modalities insufficiently evaluated. We introduc...
  </details>

- **2026-10-20** — Yuxia Chen, Wenbo Zhu, Yangguang Ji et al. — [Auto-Director: Leveraging Multi-Agent Collaboration for Autonomous Video Editing](http://arxiv.org/abs/2610.28346v1)
  <details><summary>📄 Abstract</summary>
  Autonomous video editing from open-world resources remains a challenging problem in multimedia content creation. Retrieval-based methods are constrained by fixed source material and lack creative flexibility, while generative models struggle with long-horizon coherence and often diverge from user intent. Both paradigms fail to replicate the structured, multi-stage reasoning that underlies professional post-production. To address these limitations, we present Auto-Director, a tool-augmented multi...
  </details>

- **2026-10-20** — Arthur Ouaknine, David Rolnick — [Towards Consistent Geospatial Representations: Aligning One Encoder to Many Foundation Models](http://arxiv.org/abs/2610.28313v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models (GFMs) differ widely in pretraining objective, modality and resolution, and none leads across benchmarks. We ask whether their representations are complementary, and whether a single encoder can inherit that complementarity. We introduce Pangaea-Latents, an extension of the Pangaea benchmark providing frozen embeddings of $5$ GFMs over its $11$ datasets, along with reproduced baselines, and find GFM embeddings to be neither redundant nor disjoint. We then propose Geo...
  </details>

- **2026-10-20** — Yuheng Zhang, Jie Zhang, Yuecong Min et al. — [PI-MLLM: Psychophysics-Inspired Multimodal Large Language Model for Oddly Satisfying Video Emotion Analysis](http://arxiv.org/abs/2610.28264v1)
  <details><summary>📄 Abstract</summary>
  Oddly Satisfying Videos (OSVs) can evoke strong viewer responses through repetitive motion, visual tactility, and ASMR-like sounds despite containing few explicit semantic emotion cues. This makes OSVs a challenging setting for Video Emotion Analysis (VEA), since most existing methods focus on semantic video content and under-model the physical sensory dynamics that shape viewer responses. To support Oddly Satisfying Video Emotion Analysis (OSVEA), we construct the Oddly Satisfying Video Dataset...
  </details>

- **2026-10-20** — Tzu-Quan Lin, Chih-Kai Yang, Yi-Cheng Lin et al. — [Uncovering Audio-Text Alignment in Large Audio-Language Models through Cross-Modal Concept Neurons](http://arxiv.org/abs/2610.28189v1)
  <details><summary>📄 Abstract</summary>
  While the language model backbone is pretrained on text alone, large audio-language models (LALMs) can, to a great extent, recognize acoustic attributes, such as emotion, speaker gender, and spoken language. However, it is unclear how the audio representation is integrated, if at all, with the other text representation before the model produces text. We hypothesize that there is a shared subspace where the audio and text representations are aligned. To test this hypothesis, we identify cross-mod...
  </details>

- **2026-10-20** — Huynh Dang Nguyen, Trong-Thang Pham, Anh-Thuan Do et al. — [IECG: Weakly-Supervised Interpretability-Enhancing Foundation Model for Electrocardiogram](http://arxiv.org/abs/2610.28083v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiography (ECG) is a cornerstone of cardiac diagnosis, yet most machine learning methods for ECG analysis lack interpretability, limiting their clinical adoption. We present IECG, a weakly-supervised ECG foundation model that jointly performs diagnostic classification and abnormality localization without requiring manual abnormal region annotations, overcoming a long-standing bottleneck in interpretable ECG learning. Central to IECG is a weakly-supervised attention strategy that explic...
  </details>

- **2026-10-20** — Ben Vardi, Dana Schonberger, Yuval Friedmann et al. — [AdaptMIL: Domain Adaptation for Multiple Instance Learning in Digital Pathology](http://arxiv.org/abs/2610.28007v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (PFMs) support a wide range of histopathology tasks on whole-slide images through multiple instance learning (MIL). Despite recent progress, these models remain sensitive to cross-hospital distribution shifts: performance often degrades when a task head (e.g., classification) is trained on data from one hospital and then used on data from another hospital. To address this challenge, we propose AdaptMIL, a training strategy for integrating domain adaptation into MIL tr...
  </details>

- **2026-10-20** — Darío Blanco-Fernández — [Understanding CEO-Employee compensation dynamics: An agent-based simulation approach](http://arxiv.org/abs/2610.27975v1)
  <details><summary>📄 Abstract</summary>
  CEO compensation has often been examined from the top down, i.e., as the outcome of a negotiation between the CEO, the board of directors, and the shareholders. While these approaches have provided valuable insights into the nature of CEO compensation and its relations with firm performance and intra-firm inequality, we believe they leave aside the internal decision-making dynamics of CEOs and employees. To fill this research gap, we develop an agent-based model built on the NK framework in whic...
  </details>

- **2026-10-20** — Genshin Kakimoto, Atsushi Yanagisawa — [Staged Continual Adaptation of Multimodal Foundation Models for Japanese Financial Documents](http://arxiv.org/abs/2610.27904v1)
  <details><summary>📄 Abstract</summary>
  Staged post-training of multimodal foundation models chains vision-language alignment, reasoning distillation, and domain tuning, yet how each phase trades capabilities against the others remains under-characterised. Tracking an 8.4B-parameter model from an un-fine-tuned baseline through three training phases on Japanese financial documents (evaluated on five text-input benchmarks), we find the phases interact non-additively: math-only distillation overwrites the financial knowledge acquired ear...
  </details>

- **2026-10-20** — Sasi Kiran Gaddipati, Gollam Rabby, Sören Auer — [CollabSciReM: Aligning Language Models for Scientific Conversations via Science-Aware Reward Decomposition](http://arxiv.org/abs/2610.27901v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used as research collaborators for hypothesis refinement, methodological planning, and technical analysis across multi-turn interactions. In this setting, a useful assistant must be accurate, methodologically justified, logically consistent, and token-efficient. Current alignment approaches rarely achieve all of these together. Instruction-tuned models gain conversational quality through verbosity, and we show that science-agnostic general collaborat...
  </details>

- **2026-10-20** — Hao Wang, Zixuan Li, Long Bai et al. — [SciDiagBench: A Type-Specific Benchmark for Human-Aligned Evaluation of Scientific Diagrams](http://arxiv.org/abs/2610.27841v1)
  <details><summary>📄 Abstract</summary>
  Recent agents have demonstrated strong capabilities in generating images from textual prompts, motivating their utilization for scientific diagram generation. Scientific diagrams naturally span diverse types, each characterized by distinct visual structures and content organization. Consequently, during peer review and other scientific evaluation, human experts naturally consider type-specific criteria when assessing their quality. However, existing VLM-based evaluation benchmarks fail to reflec...
  </details>

- **2026-10-20** — Siyuan Ma, Yu Qi, Cheng Ye et al. — [RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation](http://arxiv.org/abs/2610.27782v1)
  <details><summary>📄 Abstract</summary>
  Video generation models are promising foundations for embodied world models, but only if their generated rollouts are physically valid and faithful to task instructions. Multimodal large language models (MLLMs) are increasingly used to judge these properties, yet their agreement with human judgments on embodied videos has not been systematically evaluated. To address this gap, we introduce RoboJudge-Bench, a benchmark for evaluating MLLMs as judges of embodied video generation. The benchmark mea...
  </details>

- **2026-10-20** — Sahil Kale — [Beyond Calibration: Temporal LLM Confidence Assessment Across Languages and Local Settings](http://arxiv.org/abs/2610.27702v1)
  <details><summary>📄 Abstract</summary>
  Large language models are expected to estimate their own uncertainty, with confidence signals used to guide retrieval, adaptive compute allocation, routing, and selective abstention. We investigate whether confidence signals measured at different temporal stages of problem solving encode distinct forms of epistemic information and remain reliable beyond English-centric settings. Inspired by classical meta-memory theory, we distinguish anticipatory pre-solve confidence (Feeling-of-Knowing, FOK) f...
  </details>

- **2026-10-20** — Bohao Li, Dinglun Cao, Pengcheng Huang et al. — [EASformer: Environment-Action-State Alignment for Industrial Generative Ranking](http://arxiv.org/abs/2610.27691v1)
  <details><summary>📄 Abstract</summary>
  Modern industrial ranking systems increasingly adopt generative recommendation (GR) paradigms, in which user behavior sequences and non-sequential (NS) features are tokenized and jointly modeled by Transformer-style backbones. This unified formulation provides a scalable interface for modeling long histories and heterogeneous features. However, sequence and NS representations often carry asymmetric semantics: historical representations may combine environment context with observed-action semanti...
  </details>

- **2026-10-20** — Yang Liu, Masahiro Kaneko, Chenhui Chu — [Speak vs. Know: Balancing Behavior and Knowledge Distributions of Large Language Models](http://arxiv.org/abs/2610.27648v1)
  <details><summary>📄 Abstract</summary>
  Recent work reports that the distribution verbalized directly in the output text aligns far better with human opinion distributions than the next-token log-probability distribution of LLMs. However, the verbalized distribution reflects what LLMs know about a group's opinions (knowledge distribution), while what they actually output at deployment is governed by their log-probability distribution (behavior distribution). We find that when prompting LLMs to predict the opinion of a specific group, ...
  </details>

- **2026-10-20** — Tingxu Han, Wei Song, Ziming Li et al. — [Standards-Guided and Dependency-Aware Code-Level Documentation Generation](http://arxiv.org/abs/2610.27634v1)
  <details><summary>📄 Abstract</summary>
  Automatically generating high-quality documentation for software repositories remains challenging: existing approaches largely treat documentation as unconstrained text generation, lacking explicit quality specifications, depending heavily on long-context prompts over raw code, and offering limited support for reproducible evaluation. We argue that code-level documentation generation should instead be a standards-guided software engineering task, in which documentation is generated and assessed ...
  </details>

- **2026-10-20** — Junjie Xu, Yuzhe Yang, Rui Yang et al. — [HealBench: A Fine-Grained Benchmark for Evaluating Psychological Comfort in Text-to-Image Generation](http://arxiv.org/abs/2610.27516v1)
  <details><summary>📄 Abstract</summary>
  Despite advances in photorealism, semantic fidelity, and aesthetics, text-to-image generation and image editing remain understudied in a human-centered dimension: whether their outputs feel psychologically comforting. Grounded in cognitive evaluation theory, we define psychological comfort as an affective response shaped by viewers' appraisal of restorative and emotionally supportive visual cues. We introduce HealBench, a fine-grained benchmark of 30,000 high-quality image-text pairs spanning 19...
  </details>

- **2026-10-20** — Kohei Yamamoto, Kosuke Okusa — [MiCLA: Mixture-to-Constituent Latent Alignment for Polyphonic Audio Representation Learning](http://arxiv.org/abs/2610.27491v1)
  <details><summary>📄 Abstract</summary>
  Real-world audio typically contains concurrent sound events, yet standard self-supervised methods treat each clip as an isolated training unit without explicitly modeling mixture--constituent relationships. We propose Mixture-to-Constituent Latent Alignment (MiCLA), a two-stage self-supervised pre-training framework that uses synthetic log-mel mixing to align mixture representations with their constituent clips. Stage 1 structures single-clip representations via masked self-distillation and cont...
  </details>

- **2026-10-20** — Zhengfeng Zheng, Minghong Fang — [Beyond the Prompt: Recovering Hidden Concepts in Text-to-Image Models](http://arxiv.org/abs/2610.27473v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image models can generate visual concepts that their prompts never mention, and recent work shows that such associations can be implanted so that ordinary prompts trigger them. Auditing this behavior requires recovering the description that a prompt omits. Existing prompt optimizers are not well suited to this task. Gradient-based methods require backward access to the scoring encoder. Discrete evolutionary search treats semantically unrelated tokens as equally close. Language-model-guid...
  </details>

- **2026-10-19** — Abolfazl Babanazari, Kaveh Fathian — [On Maximum Clique and Maximum Consensus Formulations in Point Cloud Registration](http://arxiv.org/abs/2610.27275v1)
  <details><summary>📄 Abstract</summary>
  Maximum clique and maximum consensus are widely used formulations for robust point cloud registration in robotics. Maximum consensus seeks one transformation that aligns as many matches as possible, while maximum clique selects matches through pairwise distance tests. Maximum clique is often used as a substitute for or an approximation to maximum consensus, with empirical evidence suggesting a close relationship. However, how closely the two formulations agree is not fully understood. We study t...
  </details>

- **2026-10-19** — Shuaiqi Cheng, Jiahao Zhang, Boyuan Gu et al. — [TamedFlow: Trajectory-Aware Distillation for Teacher-Assisted Diffusion Sampling](http://arxiv.org/abs/2610.26025v2)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) deliver high-fidelity image and video generation, but inference requires many sequential model evaluations. Two acceleration strategies are increasingly important: model compression makes each evaluation cheaper, while adaptive inference avoids selected teacher computation through reuse, forecasting, or speculative execution. Their combination, however, is brittle: directly applying the evaluated adaptive methods to a compressed student can degrade quality, an obser...
  </details>

- **2026-10-19** — Lanfeng Zhong, Xiangyu Sun, Guixuan Xu et al. — [REST: Reliability-Guided Spatial Transcriptomics Supervision for Gene Expression Prediction from Histopathological HE-Stained Images](http://arxiv.org/abs/2610.26988v1)
  <details><summary>📄 Abstract</summary>
  Histopathology is central to cancer diagnosis, but morphology in Hematoxylin and Eosin (HE)-stained images does not directly reveal the molecular states that characterize disease heterogeneity and inform tumor characterization, prognostic assessment, and biomarker discovery. Spatial Transcriptomics (ST) measures spatially resolved gene expression, providing molecular information within tissue architecture, yet differences in assay coverage and spot informativeness make paired HE--ST observations...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 59 papers

- **2026-10-20** — Wenjie Lou, Tianshuo Peng, Shiyang Feng et al. — [Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition](http://arxiv.org/abs/2610.28578v1)
  <details><summary>📄 Abstract</summary>
  In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage-A1.5 learns not only to solve individual tasks, but also to organize work and revise its approach during execution. Sage-A1.5 highlights three improvements: agentic orchestration, verification, and open scientific discovery. First, agentic orchestration extends single-agent execution through task d...
  </details>

- **2026-10-20** — Youmna Farag, Svetlana Stoyanchev, Simon Keizer et al. — [CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents](http://arxiv.org/abs/2610.28381v1)
  <details><summary>📄 Abstract</summary>
  Reasoning about safety is essential for embodied agents powered by large language models (LLMs). We introduce the Contextual Action and Plan Safety benchmark (CAPSafe), designed to evaluate safety reasoning at two levels: (1) an action-level dataset that tests whether a single action is safe given its environmental context, and (2) a plan-level dataset that evaluates whether agents can generate safe long-horizon plans for complex hazardous household tasks. CAPSafe models safety conditions where ...
  </details>

- **2026-10-20** — Borui Xu, Han Chen, Bingsheng He et al. — [VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs](http://arxiv.org/abs/2610.27698v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models transfer knowledge from large-scale pretraining into robot control, but their manipulation performance remains sensitive to changes in observation conditions, which recent work addresses by fine-tuning the visual module on target-domain data. However, it remains unclear how such adaptation affects robustness beyond the target condition, as existing robustness benchmarks only evaluate models without fine-tuning and adaptation studies only report the target gain...
  </details>

- **2026-10-20** — Jiatong Li, Jisheng Dang, Qiangqiang Ma et al. — [FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models](http://arxiv.org/abs/2610.28109v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have achieved strong performance on standard robotic manipulation benchmarks. However, their reliability can degrade substantially when task conditions deviate from the nominal setting. Perturbations in object positions and task instructions may lead to complete task failure. Existing VLA policies generally lack an explicit runtime mechanism for distinguishing these failure modes and selecting an appropriate recovery strategy. To systematically mitigate this i...
  </details>

- **2026-10-20** — Da Huang, Jichao Wang, Junhui Wu et al. — [Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum](http://arxiv.org/abs/2610.27865v1)
  <details><summary>📄 Abstract</summary>
  Recent studies have explored the potential of multimodal large language models for robot control, yet the models' embodied capabilities remain insufficiently characterized across models, tasks, and execution settings. We conduct a multidimensional comparative evaluation on RoboColiseum across four tracks: Instruction Following, Spatial Reasoning, General Manipulation, and Robustness. We implement Agent2Act, a control harness that integrates GPT-6 Astra, GPT-6.1 Sol, Claude Opus 5.5, and Gemini 4...
  </details>

- **2026-10-20** — Ma ZhenYao, Yue Liang, Jian-Qiao Zhu — [OptScientist: Automated Discovery of Optimization Laws](http://arxiv.org/abs/2610.28562v1)
  <details><summary>📄 Abstract</summary>
  Many scientific phenomena are best understood as outcomes of underlying optimization problems, yet automated scientific discovery has largely focused on recovering equations that describe observed input-output patterns. We introduce OptScientist, a novel automated framework for discovering compact symbolic optimization laws directly from data. OptScientist comprises (i) a model that infers symbolic optimization problems by first learning to represent data as an optimization problem and then extr...
  </details>

- **2026-10-20** — Mohammad Reza Modarres, Armin Tourajmehr, Artin Tavasoli et al. — [Every Model Leaves a Trace: Multi-Resolution LLM Fingerprinting](http://arxiv.org/abs/2610.28434v1)
  <details><summary>📄 Abstract</summary>
  Large language models leave model-specific traces in their generated text, but it remains unclear how finely these fingerprints can distinguish related models and which signals remain informative as obvious cues are reduced. We study this through fingerprint resolution, considering both model resolution, from different families to distilled and adapted variants, and signal resolution across behavioral, stylometric, lexical, and semantic evidence. We progressively suppress surface cues, paraphras...
  </details>

- **2026-10-20** — Yunxin Geng, Shengxiang Hao, Yichen Wu et al. — [ORCA: Onboard Reflective Collaborative Agents for Reliable Task Offloading in LEO Satellite Networks](http://arxiv.org/abs/2610.28404v1)
  <details><summary>📄 Abstract</summary>
  Low Earth orbit (LEO) satellites increasingly perform time-critical onboard processing, yet heterogeneous computing capabilities, rapidly changing inter-satellite links (ISLs) and uncertain neighbor behavior make decentralized task offloading difficult under partial observations. This paper presents ORCA, an architecture of Onboard Reflective Collaborative Agents for autonomous onboard task offloading. ORCA organizes offloading decisions into a four-Agent \emph{Perceive}$\rightarrow$\emph{Reason...
  </details>

- **2026-10-20** — Cecilia Diana-Albelda, Fiona Kekwick, Raghav Mehta et al. — [Convergent Performance, Divergent Mechanisms in LoRA-Adapted Vision Foundation Models for Brain MRI](http://arxiv.org/abs/2610.28255v1)
  <details><summary>📄 Abstract</summary>
  Adapting Vision Foundation Models (VFMs) to medical imaging via LoRA has become standard practice, yet model selection is guided almost entirely by downstream task metrics, treating backbones with similar performance as interchangeable. We investigate whether equal performance implies equal internal representational shift. We analyse four ViT-B/16 backbones, DINOv3, SigLIP2, MerMED-FM, and BiomedCLIP, pre-trained with different objectives (self-distillation vs. contrastive vision-language) and o...
  </details>

- **2026-10-20** — Edric Castel C. Hao, Rez Samantha Z. Floresca — [Beyond the Evidence Boundary: Behavioral Mirage Under Progressive Degradation in Medical VLMs](http://arxiv.org/abs/2610.28000v1)
  <details><summary>📄 Abstract</summary>
  VLMs for medical image interpretation are typically evaluated on clean inputs, despite the progressive evidence loss that can occur in high stakes clinical settings. Existing robustness studies show that performance can degrade while confidence remains high, but do not establish when a previously reliable model-case pair ceases to behave reliably. We introduce a baseline-anchored framework that traces baseline-correct cases through progressive image degradation to identify an empirical evidence ...
  </details>

- **2026-10-20** — Esther Shizgal, Ron Keinan, Daniel Shtauber et al. — [From DQI to C-DQI: Automatic Codebook Generation and Evaluation for Measuring Computational Discourse Quality Index](http://arxiv.org/abs/2610.27937v1)
  <details><summary>📄 Abstract</summary>
  Effective democratic deliberation is vital for civic engagement and the health of legislative institutions. However, assessing parliamentary discourse quality is traditionally done using expert-scored, theory-based codebooks (CBs), which are rigid, labor-intensive, and prone to biases. While Large Language Models (LLMs) offer a scalable alternative for both schema induction and discourse annotation, ensuring schema quality and mitigating models' inherent bias remains a clear challenge. In this w...
  </details>

- **2026-10-20** — Junha Song, Geonmo Gu, Jeongeun Park et al. — [LaLa-World: Scaling Latent World Models with Natural Language Actions](http://arxiv.org/abs/2610.27851v1)
  <details><summary>📄 Abstract</summary>
  This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation models. We establish this approach as an effective and efficient basis for planning with imagination and downstream policy fine-tuning. To this end, we introduce LaLa-World, a Language-conditioned Latent World model that learns from simulation and robot trajectories together with broader image and video data. Two designs ...
  </details>

- **2026-10-20** — Daisuke Oba, Hiroki Furuta, Naoaki Okazaki — [BCT: Bayes-Consistent Tempering for Flow Language Models](http://arxiv.org/abs/2610.27641v1)
  <details><summary>📄 Abstract</summary>
  Temperature scaling is typically applied as a post-hoc transformation of model probabilities. In posterior-induced flow language models, this creates two mismatches. First, posterior tempering implicitly changes both the endpoint distribution and the distribution of intermediate noisy states, while the denoiser remains trained on the original states. Second, the tempered posterior weights are combined with transport dynamics derived for the untempered flow. These mismatches are reflected empiric...
  </details>

- **2026-10-20** — Zihan Chen, Di Zhu, Lei Nico Zheng — [Auditing the Product, Not the Recursion: The Evaluation Evidence Behind Recursive Self-Improvement Claims](http://arxiv.org/abs/2610.27610v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) promises AI systems, such as self-evolving LLM agents, that become better at producing further improvements. Evaluating this promise requires separating product claims about the final system from process claims about the improvement process itself. Existing surveys specify the evidence these claims require, but how often studies report that evidence remains unmeasured. We examine this question through full-text coding of 114 eligible studies in a reproducible arX...
  </details>

- **2026-10-20** — Yuchen Guo, Zhuoyuan Mao, Yiwen Guo — [Factual Access States in Diffusion Language Models: From Mechanism to Knowledge Editing and Retrieval](http://arxiv.org/abs/2610.27580v1)
  <details><summary>📄 Abstract</summary>
  Factual recall is a lookup: some representation inside the network serves as the key, and what that key is made of decides which queries can retrieve the fact, what an edit must cover, and what a retriever can read. We call it the factual access state. In autoregressive (AR) models the subject position enriches attributes largely independently of the relation, and relation-specific selection happens later, at the readout position. In masked diffusion language models (DLMs) we find the state is a...
  </details>

- **2026-10-20** — Yuqian Zheng, Hyoju Ahn, Hyeongjin Ahn et al. — [Less is More: Concise Retrieval and Critic-based Re-ranking for Composed Image Retrieval](http://arxiv.org/abs/2610.27538v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot composed image retrieval (ZS-CIR) aims to retrieve a target image based on a reference image and modification text. Recent approaches commonly rely on large vision-language models to generate target image captions for retrieval. However, these captions may include redundant semantic details, introducing noise when retrieving the target image and leading to suboptimal retrieval results. To address this issue, we propose Less-is-More CIR, a two-stage training-free framework that combines...
  </details>

- **2026-10-20** — Daniel Weiner, Raj Korpan — [Robot-Task Suitability in Heterogeneous Multi-Robot Task Allocation](http://arxiv.org/abs/2610.27504v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous multi-robot task allocation depends on estimates of how suitable individual robots are for candidate tasks, yet suitability can be defined in substantially different ways. We compare ten deterministic methods and two LLM-based variants spanning rule-based, similarity-based, requirement-oriented, fuzzy, and semantic approaches. Using common robot and task profiles, we compare how the methods score and rank candidate robots, identify feasibility, and select a top robot, while examini...
  </details>

- **2026-10-20** — Samaneh Zamanifard, Sajad Goudarzi, Andrew Robb — [Bias and Reliability in Learning-Style Inference from Student--AI Dialogues: An Evaluation of GPT-4o and Gemini 2.0 Flash](http://arxiv.org/abs/2610.27448v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly integrated into educational technologies for personalized support, creating opportunities for real-time learner modeling from dialogue. This study evaluates whether GPT-4o and Gemini 2.0 Flash can infer three Felder-Silverman Learning Style Model dimensions (Active-Reflective, Sensing-Intuitive, and Sequential-Global) from short, task-focused student-AI problem-solving dialogues. Using questionnaire-derived Index of Learning Styles labels from 153 un...
  </details>

- **2026-10-20** — Javier Porras-Valenzuela, Arush Arora, Alejandro Ribeiro — [Scaling Graph Reasoning in Language Models with Learnable Graph Positional Encodings](http://arxiv.org/abs/2610.27439v1)
  <details><summary>📄 Abstract</summary>
  Solving reasoning tasks supported on graphs typically requires providing a Language Reasoning Model (LRM) with a serialized description of the graph. This approach results in the input length growing with the number of edges, which limits the size of the problems that can be solved. Furthermore, even when graphs fit in context, performance sharply decays as the graphs grow. We propose to address this by augmenting LRMs with scalable and permutation equivariant graph positional encodings that mod...
  </details>

- **2026-10-19** — P. K. G. Williams — [AI and The Enclosure of the Scientific Commons](http://arxiv.org/abs/2610.27251v1)
  <details><summary>📄 Abstract</summary>
  The scientific literature can be viewed as an "information commons:" an intangible resource that "no one owns and is shared by everyone." There are well-established economic and political frameworks for understanding such commons, emerging from the history of agricultural common lands found in places like preindustrial England. This article provides a primer on the history and these frameworks, and considers a key difference between the information commons and the fields of yore: while informati...
  </details>

- **2026-10-19** — Xinying Cai, Bin Hu, Mingyu Jin et al. — [RealControlBench: A Benchmark for Interpretability-Informed Fine-Grained Control of LLMs and Agents](http://arxiv.org/abs/2610.27295v1)
  <details><summary>📄 Abstract</summary>
  Existing steering benchmarks are built around simplified, isolated generation tasks and evaluate a single behavioral attribute under controlled settings that do not reflect the diversity and complexity of practical deployment. As a result, performance on these benchmarks provides only a limited picture of how steering methods perform in the real world. We therefore introduce RealControlBench, a comprehensive benchmark for evaluating fine-grained steering of LLMs and LLM agents across diverse beh...
  </details>

- **2026-10-19** — Weinan Zhang, Chunhua Shen, Tianfan Xue et al. — [Physical AI: Concepts, Techniques, and Challenges](http://arxiv.org/abs/2610.27045v1)
  <details><summary>📄 Abstract</summary>
  In recent years, physical artificial intelligence (physical AI) has experienced rapid development, capturing significant attention in academia and industry. However, the field has yet to reach consensus on its definition, technical landscape, and core challenges. To address this gap, this monograph seeks to define physical AI, present its technical landscape, and examine each key technical subfield in depth. In doing so, it establishes a unified framework for Physical AI: artificial systems that...
  </details>

- **2026-10-19** — Ocean Monjur, Daud Ahmad Nisar, Shahriar Kabir Nahin et al. — [LoWAgent: A Low-Resource Multilingual Benchmark for Web Agents](http://arxiv.org/abs/2610.27205v1)
  <details><summary>📄 Abstract</summary>
  Web agents are typically evaluated on English-language interfaces, leaving their ability to operate across the world's multilingual websites largely unexplored. This gap is especially significant for low-resource languages, where standardized resources for evaluating web agents remain limited. To address this gap, we introduce Low-Resource Web Agent Benchmark (LoWAgent), a benchmark for evaluating web agents across different low-resource languages (LRLs) in comparison to the default, English. Lo...
  </details>

- **2026-10-19** — Dan Porat, Ran Finkelstein, Tal Carmon — [Allight: A Perfect Photon Collector](http://arxiv.org/abs/2610.27161v1)
  <details><summary>📄 Abstract</summary>
  Collecting photons from quantum emitters remains a key limitation in light-matter interaction because conventional lenses collect light only from one direction. Here, we introduce a perfect light collector by inverse-designing a surrounding dielectric structure that encloses the emitter to increase photon-collection efficiency toward unity. Decomposing the device into several refractive interfaces enables emission collection from the full 4$π$ solid angle with adiabatic reshaping into a collimat...
  </details>

- **2026-10-19** — Shafi Bin Sultan, Sabik Bin Sultan, Mohammad Tajrian Arafat Alvi et al. — [A Hybrid TFT-NBEATS Framework for Robust Multi-Horizon Photovoltaic Power Forecasting](http://arxiv.org/abs/2610.27155v1)
  <details><summary>📄 Abstract</summary>
  Accurate multi-horizon photovoltaic (PV) power forecasting is essential for grid stability, energy scheduling, and the efficient operation of PVbatterygrid systems. However, existing models often fail to jointly capture short-term variability and long-term temporal patterns, while lacking unified multi-horizon capability and interpretability. To address these limitations, this study proposes a novel hybrid deep learning framework that integrates a Temporal Fusion Transformer (TFT) and N-BEATS wi...
  </details>

- **2026-10-19** — Yupeng Qiu, Han Fang, Ee-Chien Chang — [ClockMark: Adaptive and Host-Dependent Watermarking for Large Language Models](http://arxiv.org/abs/2610.27079v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) watermarking operates on the next-token distribution that evolves during generation. In streaming generation, each sampled token becomes part of the text and affects subsequent distributions. Embedding therefore proceeds with a changing host, unlike classical watermarking, which adapts embedding to an existing host signal. To accommodate this difference, we formulate a novel embedding framework for LLM watermarking based on two principles. We first argue that embedding...
  </details>

- **2026-10-19** — Tong Ding, Caiwei Tian, Dongmin Bang et al. — [Discrete Neural Interlingua for Ontology-Agnostic EHR Modeling](http://arxiv.org/abs/2610.27047v1)
  <details><summary>📄 Abstract</summary>
  EHR foundation models promise scalable clinical prediction across health systems, yet their deployment is constrained by a tokenization bottleneck. The same clinical concept can appear as different ontology codes, local identifiers, synonyms, or free-text descriptions, which standard EHR tokenizers treat as unrelated symbols. A model trained on MIMIC-III with a closed-vocabulary tokenizer can use only 13% of eICU events. We introduce MEDIATOR, a discrete ontology-agnostic tokenizer that maps any...
  </details>

- **2026-10-19** — Mobina Koochaknia, Maryam Ramezani, Mohammad Hasan Shafaat — [MultiCard: Multiple Attribute Cardinality Estimation via Deep Learning](http://arxiv.org/abs/2610.27019v1)
  <details><summary>📄 Abstract</summary>
  Cardinality estimation is essential for query optimization, but most existing learned estimators focus on a single predicate type, such as string LIKE clauses or numerical range filters. In practice, analytical workloads often combine both types, while the accuracy of string estimators tends to decrease with longer patterns. We introduce MultiCard, a comprehensive learned cardinality estimator that unifies LIKE predicates and numerical filters within a single end-to-end architecture. By combinin...
  </details>

- **2026-10-19** — Chuansen Peng, Xiaojing Shen — [Robust Latent Variable Graphical Models: Exact Recovery and Fundamental Limits](http://arxiv.org/abs/2610.27010v1)
  <details><summary>📄 Abstract</summary>
  We study robust estimation of a Gaussian precision matrix that decomposes as a sparse matrix minus a symmetric, possibly indefinite, low-rank matrix, a structure that arises when latent-variable marginalization is combined with conditioning on linear measurements. The proposed convex estimator replaces the sample covariance by the centered Gaussian measure-transformed (MT) covariance, which preserves the signed graph of the sparse component under the nominal model, and penalizes the low-rank com...
  </details>

- **2026-10-19** — Matthias Eder, Pantelis Emmanouil, Vivek Farias et al. — [Policy Search in Code Space for Multi-Agent Pathfinding](http://arxiv.org/abs/2610.25946v2)
  <details><summary>📄 Abstract</summary>
  Developing coordination policies for complex multi-agent systems relies on either labor-intensive algorithm design or opaque task-specific reinforcement learning. With recent advances in autonomous coding agents, we show that policy search directly in code space offers a compelling third path that combines automated optimization with explicit interpretability. We investigate a human-directed workflow in which coding agents iteratively propose, implement, evaluate, diagnose, and eventually refine...
  </details>

- **2026-10-19** — Yudong Pan, Lian Liu, Shixin Zhao et al. — [3D-MoE: Complementarity-Guided Hardware-Software Co-Design for MoE Decode on 3D-Stacked NMP](http://arxiv.org/abs/2610.26991v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) have become a mainstream way to scale Large Language Models (LLMs), because each token activates only a small subset of experts, reducing inference cost. However, MoE decode remains highly memory-bound and exhibits strongly skewed, time-varying expert loads. 3D-stacked DRAM near-memory processing (NMP) provides the bandwidth that decode demands, yet its tiled organization makes load balancing expensive: expert parallelism (EP) preserves locality but suffers from hotspot-...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 11 papers

- **2026-10-20** — Seyedeh Fatemeh Mirfakhar, Reda Snaiki, Rocio Lilen Segura — [A Multimodal Engineering GraphRAG Framework for Post-Wind-Event Building Assessment and Recovery Inference](http://arxiv.org/abs/2610.28216v1)
  <details><summary>📄 Abstract</summary>
  Post-event building assessment requires linking observed physical damage to its consequences for safety, habitability, functionality, and recovery. Yet post-disaster evidence is often heterogeneous, incomplete, and distributed across images and reconnaissance reports, while recovery models typically require structured engineering inputs. This study develops a multimodal engineering Graph Retrieval-Augmented Generation (GraphRAG) framework that connects post-wind-event damage evidence to physical...
  </details>

- **2026-10-20** — Oleksiy V. Penkov, Boyang Shen — [Value-level data provenance in an electronic laboratory notebook used by humans and language-model agents: An experience report](http://arxiv.org/abs/2610.27859v1)
  <details><summary>📄 Abstract</summary>
  A published laboratory number can be verified only when its raw file and extraction method are known. This paper presents the value-level provenance architecture of APS ELN, an electronic laboratory notebook used by both researchers and language-model agents. The architecture was motivated by a production audit in a materials laboratory covering projects performed over almost 5 years. Tracing eight baseline studies from sample to stored value showed that the initial ELN structure preserved the l...
  </details>

- **2026-10-19** — Luyang Zhang, Minxing Zheng, Jialu Wang — [Correcting Attribution Patching with a Few Exact Measurements](http://arxiv.org/abs/2610.27393v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability asks which language model components matter for a behavior, and activation patching answers by changing one component's activation and measuring its effect, at a cost growing with components and prompts. Attribution patching estimates these effects from one gradient pass, but its estimates can be far off, and verifying each one restores the cost. Can the structure of these errors reduce this cost? We propose Guided-AP, which uses a few exact measurements to reveal at...
  </details>

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


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-10-19** — Ben Bucknall, Andrew Byrley, Lewis Hammond — [From TCP/IP to MCP: Security and Governance Lessons from Internet Protocols for Agentic AI](http://arxiv.org/abs/2610.26624v1)
  <details><summary>📄 Abstract</summary>
  The past two years have seen considerable interest in protocols for managing how AI agents interact with human users, external tools, and each other. In many ways, these protocols, including the Model Context Protocol (MCP) and Agent2Agent (A2A), mirror the suite of protocols that underlie the modern internet. Motivated by this parallel, this paper draws lessons from the development, history, and governance of internet protocols with the aim of informing the responsible development of AI agent p...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-10-19** — Israel Abebe Azime, Jesujoba O. Alabi, Tajuddeen Gwadabe et al. — [African Languages AI Safety Readiness Report](http://arxiv.org/abs/2610.27269v1)
  <details><summary>📄 Abstract</summary>
  With the widespread adoption of large language models (LLMs) across languages and domains, AI safety has emerged as a critical global concern. However, due to resource constraints, research and development efforts tend to prioritize a limited number of high-resource languages, leaving many others, especially those spoken in Africa, underrepresented. While existing research on language "resource-ness" has largely examined whether sufficient resources are available to develop language technologies...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 6 papers

- **2026-10-20** — Jakob Steimle, Thomas Elsken, Daniel Ehrhardt et al. — [Don't Skip the Baseline: A Controlled Comparison of Dynamic Expert Skipping in MoEs](http://arxiv.org/abs/2610.28369v1)
  <details><summary>📄 Abstract</summary>
  A growing body of work proposes dynamic expert-skipping methods for Mixture-of-Experts (MoE) models that adjust the number of experts activated per token during inference, aiming to preserve model quality while further reducing the number of active parameters. These methods have added calibrated importance scores, inter-expert similarity metrics, or learned per-token allocators in order to identify experts to skip. However, different calibration regimes, different reductions in the effective num...
  </details>

- **2026-10-20** — Marc Chapus, Carlos Crispim-Junior, Véronique Eglin et al. — [CountVideoBench: A Benchmark to Evaluate Prediction Biases on the Object Counting task by Video-Language Models](http://arxiv.org/abs/2610.28356v1)
  <details><summary>📄 Abstract</summary>
  Object counting in videos remains a poorly characterized capability of multimodal large language models. Counting questions are included in many existing VideoQA benchmarks, but the ground-truth count distributions in these benchmarks are heavily skewed toward small values. Across the nine benchmarks we survey, the median ground-truth count is at most five, and the three most frequent values together account for between 45% and 93% of the videos. The resulting mean accuracy is then dominated by ...
  </details>

- **2026-10-19** — Won Seok Jang, Harry Bhaskar Joshi, Hong Yu — [Does Multi-Agent Collaboration Reduce Hallucination in Clinical Tasks?](http://arxiv.org/abs/2610.27027v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems improve performance on clinical tasks, and that improvement is often read as evidence of a more trustworthy system. However, the two are not the same claim. A clinician acts on the stated reasoning and not only on the conclusion, so whether collaboration reduces hallucination, and what decides when it does, has to be measured in the reasoning too. Yet most evaluations score only the final answer. We evaluate four systems (a single-LLM baseline and three multi-agent topolo...
  </details>

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


### 📂 other
*其他安全相关 / Other Security-Related* — 170 papers

- **2026-10-20** — Carlo Ciliberto, Alessandro Rudi, Enrico Tassi — [Proof-Carrying Contracts: Commitments AI Agents Cannot Break](http://arxiv.org/abs/2610.28484v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act on behalf of people or other agents, purchasing services, exchanging information and delegating work. What an agent must respect is written in instructions, policies or agreements, but text alone cannot make it comply. It may make mistakes, be redirected by what it reads, or pursue different interests. For an economy of such agents to function, parties need agreements they can rely on without inspecting or trusting one another's agents. We introduce Proof-Carrying Cont...
  </details>

- **2026-10-20** — Lili Quan, Longtian Wang, Yuelin Wang et al. — [AgenTest: Mining Business Rules to Test LLM Agents for Business Logic Bugs](http://arxiv.org/abs/2610.28116v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly execute business operations through tools and interact directly with application data and services. Beyond completing user requests, these agents must obey domain-specific business rules that constrain when actions are permitted and what data or resources may be affected. Violating such rules can lead to business logic bugs, even when a task appears successful. Detecting these bugs is difficult because the rules are rarely available as explicit, tes...
  </details>

- **2026-10-20** — Kamolchanok Saengtong, Chutirat Saengyingyongwattana, Sasin Janpuangtong et al. — [HydraPoT: A Configurable Multi-Agent Framework for Cost-Aware LLM-Assisted Honeypots](http://arxiv.org/abs/2610.27722v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can improve honeypot realism by generating dynamic, context-aware responses, but powerful cloud models incur substantial cost and latency, while lightweight models may provide weaker deception. This forces practitioners to choose between operational efficiency and interaction fidelity. In this work, we present HydraPoT, a configurable multi-agent honeypot framework that integrates traditional emulation, lightweight LLMs, and powerful cloud LLMs. HydraPoT routes each ...
  </details>

- **2026-10-20** — Guian Fang, Shengju Qian, Dongyue Lu et al. — [SolarRenderer: Few-Step Generative Reference Rendering](http://arxiv.org/abs/2610.28630v1)
  <details><summary>📄 Abstract</summary>
  Game engines and coding agents can specify the layout, motion, and camera of a scene, yet turning such coarse structure into realistic video requires a renderer that follows the structure and completes the appearance it leaves open. Existing renderers are tied to the representation of one engine, need tens of denoising steps or a costly distillation of their own, and learn from conditions that are not aligned with their target videos. We present SolarRenderer, a structure-conditioned video rende...
  </details>

- **2026-10-20** — Runguo Li, Dezhen Lu — [Weight Placement Is Not Enough: Synchronization in Multi-Node CPU Decoding of Ternary LLMs](http://arxiv.org/abs/2610.28620v1)
  <details><summary>📄 Abstract</summary>
  Ternary LLMs read only a few gigabytes per decoded token, yet on dual-socket servers with four NUMA nodes the fastest ternary runtime we found uses less than half of the memory bandwidth. Placing each weight on the node of the thread that reads it is necessary but not enough: in a decode engine with node-local weights that reuses ik_llama.cpp's kernels, threads on two generations of Xeon servers still spend 20-48% of each token waiting at synchronization points. Per-thread barrier traces show th...
  </details>

- **2026-10-20** — Rhea Sanjay Sukthanker, Riccardo Grazzi, James Hensman et al. — [Beyond 4 bits: Data-Centric Post-training Quantization and Recovery](http://arxiv.org/abs/2610.28537v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) compresses the weights of a trained model with limited compute and data. Down to 4 bits it is near-lossless, but at 2 bits scalar PTQ configurations fall to chance-level accuracy. We study three choices usually treated as implementation details that matter little at 4 bits but decide 2-bit quality: the quantization representation, the calibration data, and the recovery fine-tuning data, across six dense and mixture-of experts models (ranging from $3.8$ to $32$B p...
  </details>

- **2026-10-20** — Om Shivam Verma, Shaya Farahmand, Lingjun Zhao et al. — [CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding](http://arxiv.org/abs/2610.28530v1)
  <details><summary>📄 Abstract</summary>
  Collaborative perception enables agents to retrieve the scene semantics and geometry beyond the field of view of any individual agent. This broader scene understanding enhances transportation safety and improves efficiency in multi-robot systems. However, existing collaborative semantic occupancy methods rely on dense 3D voxel annotations and are limited to recognizing objects within a predefined set of semantic classes. To overcome these limitations, we present CoGaussian, an open-vocabulary Ga...
  </details>

- **2026-10-20** — Nikita Ganziuk, Innokentiy S. Humonen, Ilya Makarov et al. — [MythoSemantic: An Interactive System for Discovering Semantic Parallels Across Mythological and Religious Traditions](http://arxiv.org/abs/2610.28452v1)
  <details><summary>📄 Abstract</summary>
  We present a tool for the comparative study of mythological and religious texts. Traditional manual analysis is highly labor-intensive and difficult to scale. To address this, we use neural language models to embed texts into a shared semantic space, so that users can find semantic parallels across cultural traditions in an interactive interface. Embedded fragments form distinct semantic structures whose coarse geometry aligns with well-documented historical relations between traditions. We quan...
  </details>

- **2026-10-20** — Charbel Abi Hana, Rayan Zaitouni, Kameel Amareen et al. — [Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots](http://arxiv.org/abs/2610.28432v1)
  <details><summary>📄 Abstract</summary>
  Classical robot navigation stacks are reliable but often require re-engineering for each new robot type and site. Learning-based navigation shifts this effort from hand-tuned parameters to data generation and training, where a policy adapts to each new embodiment or facility by fine-tuning in simulation. Whether policies adapted this way stay reliable on real industrial robots has seen little systematic testing. We study this for NVIDIA's X-Mobility and COMPASS workflow for training learned navi...
  </details>

- **2026-10-20** — Sumaiya Fazal, Rizwan Qureshi, Laleh Behjat et al. — [Gated Prototype Transfer for Zero-Support Medical Vision Language Model](http://arxiv.org/abs/2610.28350v1)
  <details><summary>📄 Abstract</summary>
  Realistic few-shot adaptation of medical vision-language models (VLMs) can leave low-prevalence classes without any labeled support. The training-free SS- Text+ solver remains operational in this setting, but its zero-support prototypes receive no visual adaptation and fall back to a purely textual class prototype. We in- troduce Gated Knowledge-Guided Prototype Transfer (GProtoT), a pre-repulsion module that transfers supported-class visual residuals to missing classes using VLM similarity and ...
  </details>

- **2026-10-20** — Indrakshi Dey, Nicola Marchetti — [Conformal Koopman Certificates for Nonlinear Multi-Agent Consensus on Time-Evolving Graphs](http://arxiv.org/abs/2610.28285v1)
  <details><summary>📄 Abstract</summary>
  Robot fleets must often agree on a shared value before they act, over wireless networks that change as the robots move. Their supervisor needs a deadline: the number of communication rounds after which the fleet has agreed with a stated probability. Today it comes from simulation plus a safety margin, with an open probability of being met. We certify it. Our method, conformal Koopman certification, rests on one observation: averaged over the random network changes, the expected behaviour of the ...
  </details>

- **2026-10-20** — Huachen Gao, Yang Yang, Xiaoqian Liang et al. — [HRoPE: Homography Relative Positional Encoding](http://arxiv.org/abs/2610.28284v1)
  <details><summary>📄 Abstract</summary>
  Geometric Relative Positional Encoding has become the primary mechanism for injecting spatial inductive biases into multi-view transformers. Existing designs condition attention on camera-level frustums or ray-marched depth, associating cross-view tokens through the sensor geometry. Such sensor-centric formulations, however, describe only where a token is observed from, leaving the rich surface geometry of the scene region depicted by the token. In this paper, we advocate a shift toward surface-...
  </details>

- **2026-10-20** — Artem Mikhaylov, Pavel Konoplev, Nikolay Efanov et al. — [RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards](http://arxiv.org/abs/2610.28010v1)
  <details><summary>📄 Abstract</summary>
  The integration of Large Language Models and Reinforcement Learning offers a promising direction for complex sequential decision-making tasks, such as multi-hop question answering over knowledge graphs. While LLMs provide strong semantic understanding and reasoning capabilities, they often struggle with precise, multi-step navigation in structured environments. Conversely, RL agents excel at learning navigation policies but are hindered by the difficulty of designing semantically meaningful rewa...
  </details>

- **2026-10-20** — Jihai Zhang, Runjia Qian, Kaiqin Kong et al. — [Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds](http://arxiv.org/abs/2610.27999v1)
  <details><summary>📄 Abstract</summary>
  Moving from controllable videos to genuinely playable worlds requires persistent world state, executable game rules, and low-latency interaction. We outline a roadmap for the next generation of Matrix-Game that separates game execution from visual generation through an executable game harness, and introduce Matrix-Game 4.0 as the first system built on this design. A lightweight game engine maintains world state and executes interaction rules, a multimodal coding agent translates player ideas int...
  </details>

- **2026-10-20** — Dayin Chen, Xiaodan Shi, Xin Xu et al. — [Foundation-Style Pretraining for Scalable and Transferable Distributed PV Forecasting](http://arxiv.org/abs/2610.27763v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of distributed photovoltaic (PV) generation is increasing the demand for accurate forecasting across large numbers of geographically dispersed stations. Existing approaches are commonly developed for individual sites or specific forecasting horizons, requiring repeated training and maintenance as new stations are integrated and limiting direct reuse at previously unseen sites. To address this scalability gap, this paper presents a domain-specific foundation-style pretraining fra...
  </details>

- **2026-10-20** — Xiang Lv, Kai Zhao, Qiang Wang et al. — [PixelSR: Pixel-Space Orthogonal Flow Decoupling for Real-World Image Super-Resolution](http://arxiv.org/abs/2610.27759v1)
  <details><summary>📄 Abstract</summary>
  Latent diffusion models have recently achieved remarkable progress in Real-world Image Super-Resolution (Real-SR). However, existing methods consistently exhibit a persistent seesaw effect: enhancing perceptual realism compromises structural fidelity. This effect, we argue, is not intrinsic to diffusion models, but largely stems from the architectural constraints of prevailing two-stage frameworks. To address this challenge, we propose PixelSR, a novel single-stage Pixel Diffusion Transformer fo...
  </details>

- **2026-10-20** — Pratik Jawanpuria, Bhabatosh Garai, Bamdev Mishra — [Constant Step Sizes for Muon-Type Spectral Optimizers on Strongly Convex Quadratics](http://arxiv.org/abs/2610.27747v1)
  <details><summary>📄 Abstract</summary>
  Muon and related optimizers update a weight matrix with a spectrally transformed gradient. In this work, we study such spectral optimizers with a constant step size on strongly convex matrix quadratics, which isolate the effect of the update from the confounds of nonconvexity, noise, and step size schedules. We analyze an update using two quantities: the gain, which is the factor by which it amplifies the gradient along each singular direction, and the length, which is the norm of the update. Th...
  </details>

- **2026-10-20** — Wenhan Li, Yangrui Zhang, Hang Zhou et al. — [Prescribed Performance Guided Safe Reinforcement Learning for Roundabout Navigation of Autonomous Vehicles](http://arxiv.org/abs/2610.27732v1)
  <details><summary>📄 Abstract</summary>
  Connected and Autonomous Vehicles (CAVs) face significant challenges in roundabout navigation due to dense traffic interactions and unpredictable agent behaviors, necessitating high levels of adaptability and safety. While the combination of Reinforcement Learning (RL) and Model Predictive Control (MPC) offers a promising approach, existing frameworks suffer from a structural mismatch where pointwise RL decisions fail to align with MPC's trajectory level optimization, and often lack rigorous saf...
  </details>

- **2026-10-20** — Thai Nguyen Van, Ibrahim Khan, Mury Fajar Dewantoro et al. — [Reusing Multimodal Agents: Efficient Evaluation of Sound Designs in Games](http://arxiv.org/abs/2610.27670v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a novel framework for efficiently evaluating in-game sound designs using multimodal learning and reinforcement learning. Sound design significantly influences gameplay and accessibility; however, objective evaluation methods, defined here as automated assessments based on agent performance rather than human ratings, often require retraining agents from scratch for each sound design. Our approach first pre-trains a multimodal encoder that encodes visual and auditory informat...
  </details>

- **2026-10-20** — Yuping Yan, Yaochu Jin — [Secure Multimodal Federated Optimization via Hierarchical DNA-Based Key Management](http://arxiv.org/abs/2610.27644v1)
  <details><summary>📄 Abstract</summary>
  Federated optimization over heterogeneous multimodal data enables distributed institutions to collaboratively optimize a shared model using medical images, genomic profiles, clinical records, and physiological signals without centralizing raw data. However, protecting modality-specific data throughout the optimization lifecycle remains insufficiently explored, particularly when heterogeneous modalities require separate encryption keys and selective local access. This paper proposes a secure mult...
  </details>

- **2026-10-20** — Pan Wang, Yihao Hu, Guangyuan Dong et al. — [PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking](http://arxiv.org/abs/2610.27628v1)
  <details><summary>📄 Abstract</summary>
  Looped language models can run more iterations at test time, but additional iterations need not help them solve longer problems. For sequential state tracking, final-answer supervision does not specify how far each iteration should advance, and repeated updates can change the scale of the recurrent state. We introduce \textbf{Progress-Aligned Recurrence (PAR)}, which trains the prediction at iteration $k$ to match the state after the first $k$ operations and rescales recurrent states to their fi...
  </details>

- **2026-10-20** — Yubang Wang, Zezheng Huai, Yifei Zhang et al. — [Embodied Task Agents Can Perform Fine Manipulation through Tactile In-Context Learning](http://arxiv.org/abs/2610.27613v1)
  <details><summary>📄 Abstract</summary>
  Can embodied task agents use tactile experience to perform fine manipulation without task-specific model training? We investigate this capability through Tactile-ETA, a system that incorporates tactile experience into an embodied task agent through in-context learning. Successful expert demonstrations show how contact changes during manipulation. We pair each recorded robot movement with its camera views and bilateral tactile observations. We keep tactile observations at the start and end of eac...
  </details>

- **2026-10-20** — Yuxuan Li, Xiangchen Guan, Kunrong Li et al. — [DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents](http://arxiv.org/abs/2610.27581v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex speech agents must update persistent memory while listening and speaking, yet it remains unclear which events should be stored, revised, or excluded. Existing benchmarks isolate interaction timing from memory outcomes, obscuring the state transitions behind a correct answer. We introduce DuplexLedger, a bilingual benchmark of 1,094 persistent sessions aligning four full-duplex scenarios with event-level Write/Update/Ignore/Retain supervision, explicit pre/post memory states, and 6,56...
  </details>

- **2026-10-20** — Xi Yang, Guodong Liu, Cheng Peng et al. — [Exploring Recurrent-Depth Language Models for Multitask Clinical Text Processing](http://arxiv.org/abs/2610.27559v1)
  <details><summary>📄 Abstract</summary>
  Clinical natural language processing includes diverse tasks such as information extraction, classification, and question answering. Developing one model for all tasks could simplify deployment and improve knowledge transfer. We evaluated whether small recurrent-depth language models can meet this need through joint fine-tuning and compared their performance with standard transformers. We fine-tuned Ouro1.4B-Thinking, Ouro-2.6B-Thinking, HRM-Text-1B, Qwen3-1.7B, and Qwen3-8B on 9 datasets coverin...
  </details>

- **2026-10-20** — Jian Zhang, Manrong Liu, Yilei Huang et al. — [Multiscale Temporal-Spectral-Spatial EEG Learning With Modality-Specific and Modality-Invariant Representations for Emotion Recognition](http://arxiv.org/abs/2610.27521v1)
  <details><summary>📄 Abstract</summary>
  Multimodal physiological signals provide complementary cues for emotion recognition. They also raise two related challenges. Emotion-related EEG patterns vary across time, frequency bands, electrodes, and brain regions. Different physiological modalities also contain both modality-specific and shared affective information. This paper presents GMSI-Net, an EEG-centered multimodal emotion recognition framework. It has three key components. The temporal-spatial-spectral-region (TSSR) encoder models...
  </details>

- **2026-10-20** — Haoxiang Luo, Bang Huang, Mohamed-Slim Alouini — [SAGE-HAP: Sustainability-Certified Agentic Communication and Computing at a Solar-Powered High-Altitude Platform](http://arxiv.org/abs/2610.27513v1)
  <details><summary>📄 Abstract</summary>
  The solar-powered High-Altitude Platforms (HAP) can provide persistent communication and computing services beyond terrestrial coverage. However, changing mission priorities, coupled resource demands, and uncertain solar supply complicate sustainable scheduling, while large language model proposals require independent feasibility checks. This paper proposes SAGE, a Sustainability-certified Agentic Ground-service Engine for a HAP. We formulate an energy-causal stochastic optimization problem inco...
  </details>

- **2026-10-20** — Rahul Sajnani, Diego Romeres, Mingyuan Zhang et al. — [UniWALM: Unified World Action Language Model for Embodied Robot Control](http://arxiv.org/abs/2610.28626v1)
  <details><summary>📄 Abstract</summary>
  Motivated by the human ability to integrate experience across language, perception, and action, we introduce UniWALM, a unified world-action-language model that learns video, action, and language in a single shared representation, where each modality is both a conditioning signal and a supervision target. We ask: can jointly generating language enrich this shared representation, improving manipulation and supporting memory-dependent behavior? Unlike prior approaches that attach a reasoning or vi...
  </details>

- **2026-10-20** — Xinxin Liu, Bingxin Xu, Wenrui Bao et al. — [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](http://arxiv.org/abs/2610.28589v1)
  <details><summary>📄 Abstract</summary>
  Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks. Recent work improves these systems through better harnesses and external memory, but relies on powerful closed-source models as planners and does not improve the planners' own capabilities. In contrast, coding agents have improved substantially by post-training the model itself. We therefore investigate whether post-training can also improve robot planners. However, applying it across robot harn...
  </details>

- **2026-10-20** — Rundong Luo, Yunong Liu, Di Cao et al. — [SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images](http://arxiv.org/abs/2610.28585v1)
  <details><summary>📄 Abstract</summary>
  Simulation is a powerful tool for robotics, but building diverse, simulation-ready scenes at scale remains difficult. Reconstructing scenes from single images is a promising alternative, but visual similarity alone is insufficient: objects must also be recovered, accurately placed, and physically grounded. Existing methods that rely on post-hoc physics settling often misplace objects, producing scenes that look correct but behave poorly under manipulation. We present SceneRig, an agentic system ...
  </details>

- **2026-10-20** — Ziyong Wang, Yupei Lin, Runxuan Huang et al. — [GPT-6-Astra Understands Touch and Outperform Vision--Tactile--Language--Action Models](http://arxiv.org/abs/2610.28457v1)
  <details><summary>📄 Abstract</summary>
  General-purpose multimodal models have shown promise as direct robot action policies, yet whether they grasp the physics underlying real-world interactions and can apply that understanding to guide action remains underexplored. We investigate this question using contact-rich manipulation as a representative testbed, examining tactile understanding as a concrete instance of this broader capability. Contact-rich manipulation requires interpreting tactile feedback and adjusting actions after obstru...
  </details>

- **2026-10-20** — Spiros Maggioros, Guray Erus, Gareth Harman et al. — [Brain2Vec: A Self-Supervised 3D Foundation Model for Structural Brain MRI](http://arxiv.org/abs/2610.28411v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models have become essential tools in medical imaging, yet training them end-to-end for diverse tasks remains challenging due to limited labeled data and computational constraints. To address this, we introduce Brain2Vec, a foundation model pre-trained on 74,425 T1-weighted Magnetic Resonance Imaging (MRI) scans pooled from multiple studies. Brain2Vec can serve both as a weight initialization backbone for fine-tuning downstream tasks and as a standalone feature extractor. We evalua...
  </details>

- **2026-10-20** — Mayimunah Nagayi, Alice Scaria Khan, Tamryn Frank et al. — [Region-Guided Food-Package Evidence Extraction and Abstention-Aware Draft R3337 Screening with Selective VLM Review](http://arxiv.org/abs/2610.28211v1)
  <details><summary>📄 Abstract</summary>
  Applying South Africa's draft R3337 warning criteria to food-package photographs requires nutrition, ingredient and product-form evidence. This study presents a region-guided evidence extraction and abstention-aware screening workflow for draft R3337. A three-class detector localises nutrition information panels, ingredient lists and product-identity regions, after which PaddleOCR and structured extraction recover nutrient values, ingredient evidence and product-form information. Recovered evide...
  </details>

- **2026-10-20** — Xiaoxu Xu, Hao Li, Hongtao Zhang et al. — [From Predictive Geometry to Action: Learning Complementary Predictive Representations for Embodied Manipulation](http://arxiv.org/abs/2610.28164v1)
  <details><summary>📄 Abstract</summary>
  Effective manipulation requires a policy to capture not only about the current scene geometry, but also about how that geometry will evolve under interaction. Existing approaches either augment policies with geometric information from current observations or introduce future prediction as auxiliary supervision, leaving open how predictive geometry should be represented for action generation. Therefore, we propose a two-stage framework, which learns complementary predictive representations from m...
  </details>

- **2026-10-20** — Antonio Langella, Giovanni Minelli, Giovanni B. Dessy et al. — [LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning](http://arxiv.org/abs/2610.27998v1)
  <details><summary>📄 Abstract</summary>
  Learning loco-manipulation policies requires demonstrations that capture coordinated base and arm motion on the target embodiment. Robot-free interfaces allow demonstrations to be collected independently of the target robot, increasing flexibility but without directly capturing platform-specific commands, proprioception, and body-mounted observations. On-robot teleoperation allows to capture these signals directly, but requires an interface capable of commanding the complete system concurrently....
  </details>

- **2026-10-20** — Jingjiao Zhao, Dong Jing, Mingyu Cao et al. — [EventSync: Event-Driven Memory Updates for History-Dependent Manipulation](http://arxiv.org/abs/2610.27917v1)
  <details><summary>📄 Abstract</summary>
  History-dependent robotic manipulation requires task context and interaction history, as the current observation alone is insufficient to determine the next action. Hierarchical frameworks use task memory for high-level subgoal reasoning and low-level policies for execution. However, memory updates require accurate completion assessment: similar observations may correspond to different execution phases, and prematurely recording completion can mislead subsequent subgoal reasoning. We present Eve...
  </details>

- **2026-10-20** — Manar Ali, Lisa Gottschalk, Simeon Junker et al. — [Testing Associative Creativity in Humans and Multimodal LLMs with Difficult-to-Name Visual Stimuli](http://arxiv.org/abs/2610.27894v1)
  <details><summary>📄 Abstract</summary>
  We investigate associative creativity in descriptions of abstract visual stimuli by humans and multimodal large language models (MLLMs). While conceptual association is central to human communication, it remains unclear how humans and models adapt when visual stimuli become increasingly difficult to map onto familiar semantic concepts. We evaluate several state-of-the-art MLLMs and human participants along two dimensions of creativity, originality and effectiveness, using two datasets with contr...
  </details>

- **2026-10-20** — Jiahong Tang, Jiaju He, Zhiyuan Yang et al. — [AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies](http://arxiv.org/abs/2610.27736v1)
  <details><summary>📄 Abstract</summary>
  Human-collected real-world robotic manipulation demonstrations often contain mixed-quality trajectories, including hesitant, indirect, or inefficient action segments. While diffusion- and flow-based policies can model such multimodal data, standard behavior cloning (BC) assigns equal likelihood to all demonstrated actions and may therefore reproduce suboptimal modes. Offline RL value estimates offer a natural signal for biasing policies toward higher-value behavioral modes, but directly fine-tun...
  </details>

- **2026-10-20** — Eachen Soong, Zijian Niu, Haoran Xu et al. — [NeoWorld-3: From Pixels to Code-Defined Physical Worlds](http://arxiv.org/abs/2610.27690v1)
  <details><summary>📄 Abstract</summary>
  Simulation-ready world reconstruction demands physical interactivity beyond visual realism, which existing black-box 3D generation fails to deliver. We present NeoWorld-3, a coding-agent framework that reconstructs interactive 3D worlds from visual observations via tunable, executable programs. At its core, NeoSDK provides the underlying computational engine for low-level geometries, part composition, differentiable parameter refinement, and physics validation. At the same time, NeoMCP exposes t...
  </details>

- **2026-10-20** — Jad Yammine, Malek Wahidi, Abrar Anwar et al. — [Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets](http://arxiv.org/abs/2610.28624v1)
  <details><summary>📄 Abstract</summary>
  Warehouse robot fleets continuously observe operational conditions, but preserving these observations as reusable semantic memory incurs substantial computation, communication, and storage costs. For example, explaining recurring aisle blockages can require reviewing video from multiple robots across several shifts. We present IndustrialRemembr, a shared spatiotemporal memory system that extends NVIDIA ReMEmbR to robot fleets and reduces server-side computation by generating scene descriptions o...
  </details>

- **2026-10-20** — Yanbo Wang, Siqi Luo, Siyu Zhang et al. — [MindView: Benchmarking Generative Multi-View Spatial Intelligence](http://arxiv.org/abs/2610.28622v1)
  <details><summary>📄 Abstract</summary>
  Spatial intelligence has recently been assessed through generative tasks such as spatially grounded image editing, yet language-guided generation of spatially consistent views from partial multi-view observations remains underexplored. We introduce MindView, a benchmark for generative multi-view spatial intelligence with 1,500 samples from 513 scenes across three indoor datasets. Its seven tasks form two families: geometry-dominant tasks specify changes in camera position and orientation, while ...
  </details>

- **2026-10-20** — Noor Abo Mokh, Teresa Lynn, Nizar Habash et al. — [Benchmarking Arabic Dialects for Math Problems](http://arxiv.org/abs/2610.28607v1)
  <details><summary>📄 Abstract</summary>
  Mathematical reasoning remains underexplored for low-resource languages, including Dialectal Arabic. To bridge this gap, we introduce the DAR-MGSM (Dialectal Arabic Multilingual Grade School Math) Benchmark, the first manually curated benchmark for evaluating mathematical reasoning in Dialectal Arabic. DAR-MGSM consists of math word problems (MWPs) requiring multi-step reasoning and covers five major Arabic dialects alongside Modern Standard Arabic (MSA). The benchmark comprises two parallel ver...
  </details>

- **2026-10-20** — Shu Zhao, Tan Yu — [Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation](http://arxiv.org/abs/2610.28586v1)
  <details><summary>📄 Abstract</summary>
  Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable, so recent methods keep training inside that region, through episode-length curricula, teacher-guided turns, prefix replay, or teacher intervention where the two disagree. We show this explanation is incomplete. From th...
  </details>

- **2026-10-20** — Azim Dehghani Amirabad, Ali Khodabandeh Yalabadi, Artem Moskalev et al. — [Spatially Informed and Direction Sensitive Representation Learning for Spatial Transcriptomics](http://arxiv.org/abs/2610.28579v1)
  <details><summary>📄 Abstract</summary>
  Cellular states are shaped by both intrinsic gene expression programs and the spatial microenvironment in which cells reside. Spatial transcriptomics makes this context measurable, but effective representation learning requires capturing both spatially informative molecular signals and intercellular organization. Existing approaches address these challenges only partially: conventional gene selection can overlook spatially structured signals, while methods for encoding cell-cell relationships of...
  </details>

- **2026-10-20** — Chenxu Niu, Batuhan Sencer, Wei Zhang et al. — [The Token-Energy Law of LLM Decode: Active Bytes and Realized Time Account for Joules per Token](http://arxiv.org/abs/2610.28576v1)
  <details><summary>📄 Abstract</summary>
  Energy-efficient deployment of large language models requires understanding how model architecture, hardware, and serving settings shape energy per generated token. We introduce the Token-Energy Law, a compact, interpretable model of GPU-board energy per output token for dense, full-history decoding. It relates token energy to two core dimensions: active bytes and realized decode time. Active bytes describe logical byte demand per output, separating dense weights shared within a decode iteration...
  </details>

- **2026-10-20** — Simon Mackenzie, Mashbat Suzuki — [Exact Envy-Free Cake Cutting with Polynomial Expected Queries](http://arxiv.org/abs/2610.28535v1)
  <details><summary>📄 Abstract</summary>
  Envy-free cake cutting asks how to divide a resource so that no agent prefers another agent's share. Finding such a division with few queries about preferences has been a longstanding challenge. Aziz and Mackenzie gave the first query bound depending only on the number $n$ of agents: a tower of six $n$'s. Subsequent improvements culminated in Ye and Bai's single-exponential bound of $n^{O(1)}2^n$. A large gap remains between this deterministic upper bound and Procaccia's general lower bound of $...
  </details>

- **2026-10-20** — Yiqing Shen, Mathias Unberath — [A Multi-Agent Framework for Automated Machine Learning with Evidence-based Planning for Medical Image Analysis](http://arxiv.org/abs/2610.28410v1)
  <details><summary>📄 Abstract</summary>
  Deep learning has become the default tool for medical image analysis, driven by the open-source movement. However, achieving the best performance on a given task remains difficult, with architecture selection and hyperparameter optimization (HPO) still considered "more of an art than a science". Automated machine learning (AutoML) automates parts of model training, yet helps little in medical imaging: general-purpose approaches lack medical architectures and preprocessing, and medical-focused on...
  </details>

- **2026-10-20** — Zijun Dou, Kun Luo, Chaofan Li et al. — [FALCA: Falsification-Aware Reinforcement Learning with Hierarchical Credit Assignment for Long-Horizon Deep Search Agents](http://arxiv.org/abs/2610.28361v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon deep search requires LLM agents to iteratively decompose complex information needs, gather evidence from external sources, and maintain a reliable research state under multiple constraints. A central challenge is that early mistakes can be amplified over the search trajectory: agents may anchor on an incorrect candidate, collect partially supporting evidence, overlook contradictions, and accumulate errors that misguide subsequent reasoning. We propose FALCA, a falsification-aware fr...
  </details>

- **2026-10-20** — Rui Gong, Ruoyu Wang, Yalun Dai et al. — [S-Agent 2.0: Spatial Reasoning with a General Coding Agent](http://arxiv.org/abs/2610.28354v1)
  <details><summary>📄 Abstract</summary>
  Spatial reasoning asks a model to work out where objects are in 3D space, how they relate to one another, and how they move. Agentic VLMs have recently brought large improvements on such tasks by letting the model actively gather evidence with 3D perception tools instead of answering in a single pass. Even so, on many questions the tools return the right evidence and the model still does not arrive at the correct answer: the gap between model and tools, where raw readings become usable conclusio...
  </details>

- **2026-10-20** — Christian Meske, Tobias Hermanns, Florian Brachten — [The GenAI Who Knew Too Little: Revisiting Transactive Memory Systems in Human GenAI Collaboration](http://arxiv.org/abs/2610.28343v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence (GenAI) is rapidly transforming knowledge work, creating new collaborative dynamics that challenge tradi-tional human-human interaction patterns. This study investigates how Transactive Memory Systems (TMS) manifest in human-GenAI collabora-tion. Through qualitative interpretive interviews with 14 knowledge work-ers and thematic analysis, we identified distinct TMS manifestations across its three main dimensions: (1) regarding specialization, expertise recogni-...
  </details>

- **2026-10-20** — Itai Shapira, Myra Cheng, Hadas Orgad — [Is Sycophancy a Form of In-Context Updating?](http://arxiv.org/abs/2610.28325v1)
  <details><summary>📄 Abstract</summary>
  Factual sycophancy, a language model's deference to a user's false beliefs, is usually understood as a bid for the user's approval at the expense of truthfulness. We argue that this framing over-emphasizes the user and propose viewing sycophancy as a failure within the broader and generally useful process of in-context updating, by which models revise their answers based on information supplied during an interaction. We support this view with behavioral and mechanistic evidence. First, models' r...
  </details>

- **2026-10-20** — Amit Lisha, Reut Tsarfaty — [From Abstraction to Action: DSLs for Natural Language Abstraction Interpretation and Execution](http://arxiv.org/abs/2610.28311v1)
  <details><summary>📄 Abstract</summary>
  Natural-language instructions often rely on high-level abstractions, such as asking an agent to ``stack blocks in a pyramid.'' Interpreting abstract instructions requires models to both identify the abstraction intended by the speaker, and unroll it into the many concrete actions that instantiate it. Language models struggle here: prior work has shown that performance degrades as the level of abstraction in the instruction rises. To bridge the gap between natural language abstraction and concret...
  </details>

- **2026-10-20** — T. Vignau Costa, J. Colbois, G. L. Rossini et al. — [Classical spin liquids in the kagome Ising model, and their link with magnetoelasticity](http://arxiv.org/abs/2610.28298v1)
  <details><summary>📄 Abstract</summary>
  We investigate a nearest-neighbor Ising model on the kagome lattice coupled to elastic lattice distortions. By integrating out the lattice degrees of freedom, we derive an approximate spin-only description in terms of a kagome \(J_1\)-\(J_2\)-\(J_{3}\) Ising model with interactions extending to third nearest-neighbors. Using tensor network methods complemented by classical Monte Carlo simulations, we revisit its zero-temperature phase diagram and characterize the ground states studied more than ...
  </details>

- **2026-10-20** — Tapan Parikh — [Forty Questions: Identifying a Language Model from One-Word Answers](http://arxiv.org/abs/2610.28281v1)
  <details><summary>📄 Abstract</summary>
  A model behind an API can be identified from its one-word answers to everyday questions such as "Name a sound" or "Name a poet". A model's profile records how often it gives each answer to each question. We attribute new answers to the model most likely to have given them. On a panel of 94 models, 40 answers identify the exact model 92.5% of the time, against 1.1% by chance. Profiles built through OpenRouter identified all ten models served by DeepInfra under blinded labels. A system prompt lowe...
  </details>

- **2026-10-20** — Argyrios Deligkas, Eduard Eiben, Robert Ganian et al. — [Subjective Valuations Make It Hard to be Fair: The Complexity of Resource Allocation to Groups of Agents](http://arxiv.org/abs/2610.28213v1)
  <details><summary>📄 Abstract</summary>
  We study the parameterized complexity of finding an EF1 allocation of indivisible items in the group-sharing setting, which has received increasing attention in recent years. There, items are not allocated to individual agents but rather to one of two (or possibly more) groups, and agents within that group all share the assigned items. We consider both the "fixed" (EF1-Fix) and "variable" (EF1-Var) group cases, where in the former the assignments of agents to groups are prescribed. While both ar...
  </details>

- **2026-10-20** — Cedric Derstroff, Jannis Blüml, Janosch Moos et al. — [Reframing Object-Centric Reinforcement Learning: From Absolute to Relative Representations](http://arxiv.org/abs/2610.28197v1)
  <details><summary>📄 Abstract</summary>
  Object-centric reinforcement learning agents typically receive each object's position in a fixed global frame, even though their decisions usually depend on where objects are relative to one another. These absolute views often fail to capture the local context that is most relevant to the agent's behavior. As a result, an agent must relearn the same response at every location where a configuration can occur, and its performance collapses when the scene is merely shifted. In this work, we propose...
  </details>

- **2026-10-20** — Somin Kim, Robert Feldt, Shin Yoo — [Foreword: Pre-Generation Prediction and Characterisation of LLM Test Failures using the Jacobian Lens](http://arxiv.org/abs/2610.28187v1)
  <details><summary>📄 Abstract</summary>
  Testing LLM-based software is expensive: each input needs several sampled responses, each judged by a costly oracle. Further, every prompt or model change calls for re-testing. Pre-generation adequacy measures cut this cost by ranking inputs by failure risk based on the model's internal state. However, the state of the art, Clotho, models only passing reference inputs, and its hidden-state representation says nothing about why inputs fail. We present Foreword, a framework built on two ideas: lea...
  </details>

- **2026-10-20** — Igor Sloev, Gerasimos Lianos — [The Scale of Universalization in Multiplicative Kantian Equilibrium](http://arxiv.org/abs/2610.28180v1)
  <details><summary>📄 Abstract</summary>
  Multiplicative Kantian equilibrium requires agents to evaluate whether they would prefer all players to change their actions by a common proportional factor. This note argues that such a counterfactual is not fully specified by the material payoff environment alone: one must also specify the scale in which proportional universalization is performed. Building on the Sher-Roemer discussion of strategic non-invariance, we characterize how a smooth monotone reparametrization of actions changes the m...
  </details>

- **2026-10-20** — Stephanie Fong, Yiwen Jiang, Qingyang Xu et al. — [Reading Too Much Into It? Interpretive Preferences and Commitment in LLM Mentalisation under Ambiguity](http://arxiv.org/abs/2610.28105v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used for interpersonal advice, potentially shaping how users interpret ambiguous social encounters. Existing Theory of Mind evaluations typically rely on predefined answers, while uncertainty research overlooks LLMs' preferred explanations and confidence under psychological distress. To address these gaps, we introduce MentalLoom, a novel evaluation of LLM mentalisation comprising 604 ambiguous social episodes, matched depression and social anxiety d...
  </details>

- **2026-10-20** — Jan Kobiolka, Christian Frey, Josif Grabocka — [MuPACE: Learning to Pace Muon for LoRA Fine-Tuning](http://arxiv.org/abs/2610.28072v1)
  <details><summary>📄 Abstract</summary>
  Learning rate schedules are typically fixed before training begins, yet when fine-tuning large language models with low-rank adapters (LoRA), the appropriate scale varies substantially with the model, task, and adapter configuration. Practitioners re-tune a schedule for every new problem, yet a tuned schedule still cannot react to the training dynamics it encounters. We instead amortize learning rate selection across LoRA fine-tuning problems. We leave the base optimizer, Muon, untouched, so tha...
  </details>

- **2026-10-20** — Saber Zerhoudi, Jelena Mitrovic, Michael Granitzer — [AutoSim: A Self-Improving User Simulator for Conversational Search Evaluation](http://arxiv.org/abs/2610.28054v1)
  <details><summary>📄 Abstract</summary>
  User simulators promise to evaluate conversational search systems at a scale human studies cannot reach, but only if their behavior is realistic enough to trust. We study AutoSim, a conversational-search user simulator whose relevance judgments rank a controlled pool of retrieval systems in agreement with NIST across three TREC iKAT years (Kendall's $τ$ of $0.66$, $0.91$, and $0.91$; all $p{\le}0.002$), an agreement that survives removing its persona. AutoSim self-improves against a held-out sig...
  </details>

- **2026-10-20** — Andrea Campagner, Federico Cabitza, Vincenzo Crupi — [When Do Humans and Machines Truly Complement Each Other? Formal Conditions and Empirical Evidence for Human-AI Synergy](http://arxiv.org/abs/2610.27965v1)
  <details><summary>📄 Abstract</summary>
  Can humans and artificial intelligence cooperate such that their combination yields greater accuracy than either agent alone? This result, termed \emph{synergy} or \emph{complementarity}, is notoriously difficult to achieve, even when both agents possess significant independent accuracy. In this paper, we present a formal framework to model human-AI interaction through the lens of reliance patterns, which characterize the joint correctness structure of human and algorithmic decisions. We derive ...
  </details>

- **2026-10-20** — Rishi Advani, Abolfazl Asudeh — [Splitting Planar Necklaces with Few Straight Cuts](http://arxiv.org/abs/2610.27956v1)
  <details><summary>📄 Abstract</summary>
  In the classical necklace splitting problem, beads of different colors lie on a line, and the goal is to divide them among $k$ agents using as few cuts as possible so that every agent receives the same number of beads of each color. We study the planar analog in which a cut is a full straight line and the objective is minimizing the number of lines: $m$ points colored red and blue must be separated by straight-line cuts into regions that can be allocated to $k$ agents so that each agent receives...
  </details>

- **2026-10-20** — Mervat Abassy, Zhaoxin Feng, Tatsuki Kuribayashi et al. — [Why Do LLMs Accept Generics? Explaining Acceptability using Psycholinguistic and Model-Derived Factors](http://arxiv.org/abs/2610.27928v1)
  <details><summary>📄 Abstract</summary>
  Psycholinguistic studies explore why humans accept some generic statements but reject others by showing that these judgments depend on more than how common a property is. People consider several other factors such as how well it sets the kind apart from others or whether it is characteristic of the kind.   Inspired by the linguistic and cognitive literature, we explore to what extent factors from these studies explain how large language models (LLMs) judge generics. Our results with twelve model...
  </details>

- **2026-10-20** — Jiahui Ning, Liang Chen, Yuchen Liang et al. — [ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](http://arxiv.org/abs/2610.27913v1)
  <details><summary>📄 Abstract</summary>
  Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions of weights, and task scores alone cannot reveal which underlying abilities survive and which quietly collapse. To solve this question, we introduce ACE-Compression, an ability-centric evaluation framework. Instead of aski...
  </details>

- **2026-10-20** — Jiamei Xu, Jie Sun, Keshuang Tang et al. — [Agentic discovery of interpretable car-following laws from multi-source trajectory data](http://arxiv.org/abs/2610.27836v1)
  <details><summary>📄 Abstract</summary>
  Car-following (CF) models is a fundamental component of microscopic traffic simulation and underpin the analysis of collective traffic dynamics, while its modeling becomes more challenging due to diverse human driving behaviors and the increasing presence of automated vehicle. Analytical CF models offer interpretable representations of longitudinal vehicle interactions, but their prescribed functional structures may limit the representation of heterogeneous driving behavior. This study proposes ...
  </details>

- **2026-10-20** — Guanchen Li, Yixing Xu, Xuanwu Yin et al. — [SliMOO: Interpretable Multi-Objective Evolutionary Search for LLM Depth Pruning](http://arxiv.org/abs/2610.27812v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) grow more powerful, their scale makes them costly to serve. Depth pruning offers a practical route to efficiency by directly reducing memory and latency without hardware-specific support. However, we observe that transformer layers exhibit markedly different task-dependent layer contributions, whereas existing depth-pruning methods ignore this heterogeneity and thus tend to optimize for a narrow domain or benchmark rather than preserve broad capability. This sugge...
  </details>

- **2026-10-20** — Riku Kisako, Tatsuki Kuribayashi, Ryohei Sasano — [Are Linguistic and Arithmetic Circuits Dissociated in LLMs?](http://arxiv.org/abs/2610.27790v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit both knowledge of language, rendered by, for example, grammatical judgment ability, and abilities to perform tasks through language, such as math-word problem solving. Motivated by neurolinguistic studies of their neural dissociation in human brains, in this study, we investigate the overlap of their circuits in large language models (LLMs). Specifically, we examine the overlap and causal effects between the circuits extracted for linguistic and arithmetic ta...
  </details>

- **2026-10-20** — Yingxin Jia, Hui Geng, Wenxin Yang et al. — [Give the Model a Finger: Developmentally Aligned Evaluation of Counting in Vision-Language Models](http://arxiv.org/abs/2610.27756v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are exact on small sets and drift into estimation on larger ones, a profile reminiscent of children before they master counting. Children cross the barrier with epistemic actions: pointing at each item while reciting number words, moving counted items aside, partitioning the array. We give VLMs the same actions as dumb image tools with no visual intelligence of their own in a training-free agent loop. Our central claim is about measurement, not intervention: a model...
  </details>

- **2026-10-20** — Fan Ding, Fucai Ke, Kevin Yuchen Ma et al. — [JARVIS: From Visual Manuals to Autonomous Robotic Assembly](http://arxiv.org/abs/2610.27618v1)
  <details><summary>📄 Abstract</summary>
  Visual manuals communicate procedural knowledge through stepwise diagrams, but translating these instructions into reliable long-horizon robotic execution remains challenging. We introduce JARVIS, a method-agnostic benchmark for autonomous visual-manual-guided execution without additional language instructions. JARVIS comprises 236,679 LEGO assembly tasks across 8,987 scenes, with a carefully curated JARVIS-v1 suite of 50 tasks for interactive robotic evaluation. Tasks span varying initial struc...
  </details>

- **2026-10-20** — Koshiro Saito, Diasuke Oba, Danushka Bollegala et al. — [Beyond Model Weights: Sampling-Dependent Fairness in Diffusion Language Models](http://arxiv.org/abs/2610.27584v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) are emerging as a practical alternative to autoregressive language models (ARLMs), yet their fairness remains largely uncharacterized. DLMs introduce sampling controls with no direct autoregressive counterpart, such as block length and remasking strategy, that directly set their speed--quality operating point. This raises a basic question: does a DLM's measured social bias remain stable across these settings? Across LLaDA, LLaDA-1.5, and Dream on Open-BBQ, we fin...
  </details>

- **2026-10-20** — Jui-Chien Tsou, Hsuan-Chi Liu, Wei-Chin Wang et al. — [TeCoP: Accelerating Diffusion Large Language Model Decoding via Tentative Context Pipelining](http://arxiv.org/abs/2610.27583v1)
  <details><summary>📄 Abstract</summary>
  Diffusion large language models (dLLMs) predict multiple token positions per forward pass, yet block-wise decoders serialize generation and repeatedly recompute stable predictions. We attribute this inefficiency to coupling a prediction's readiness for irreversible commitment with its utility as context. We introduce Tentative Context Pipelining (TeCoP), a training-free decoder that decouples these roles through staggered block-parallel pipelining and draft-and-verify. TeCoP reuses stable but un...
  </details>

- **2026-10-20** — Marko Petković, Susanne Gooijer, José Manuel Vicent-Luna et al. — [RaspAssistant as an Agentic Framework for Automating Adsorption Simulation Research in Porous Materials](http://arxiv.org/abs/2610.27572v1)
  <details><summary>📄 Abstract</summary>
  Porous-material adsorption studies require coordinated structure preparation, force-field selection, simulation, validation, and interpretation, making end-to-end automation difficult. We test whether RaspAssistant, a hierarchical multi-agent framework, can carry an adsorption study from force-field preparation through validation and downstream separation analysis. Across twelve multi-agent workflow-reproduction runs spanning four adsorption and separation benchmarks, overall scores ranged from ...
  </details>

- **2026-10-20** — Yuxing Peng, Zhiqing Tang, Weijia Jia — [Lower Bounds for Smooth Nonconvex Zeroth-Order Optimization: The Price of Determinism under Low Curvature Trace](http://arxiv.org/abs/2610.27550v1)
  <details><summary>📄 Abstract</summary>
  Low curvature trace, an effective rank condition, is a common explanation for why randomized zeroth-order methods scale to high-dimensional tasks such as language model fine-tuning. Can deterministic methods achieve the same savings? We show that they cannot. We study finding $\varepsilon$-stationary points of $L$-smooth nonconvex functions on $\mathbb{R}^d$ from exact function values, assuming that below the starting value the Hessian is dominated by a fixed matrix with trace at most $LE$; this...
  </details>

- **2026-10-20** — Marilyn Zhang, Tianfeng Chen, Patricia M Pechter et al. — [When Health Assistants Agree Too Readily: A Benchmark of Time-Critical Self-Diagnosis](http://arxiv.org/abs/2610.27518v1)
  <details><summary>📄 Abstract</summary>
  Every day, more than 40 million people ask ChatGPT a health question, such as whether laptop posture explains a stiff neck and days of pounding headache. Posture is plausible, but meningitis is a time-critical possibility. We introduce SelfDx, a paired benchmark for whether models have the appropriate response behavior, a form of epistemic independence, in health questions where misplaced agreement with the user's self-diagnosis could delay urgent or emergency care. Each of 100 pairs contrasts a...
  </details>

- **2026-10-19** — Juan Pablo Vigneaux, Jennifer Cole — [Steering intonational tunes in text-to-speech synthesis](http://arxiv.org/abs/2610.27403v1)
  <details><summary>📄 Abstract</summary>
  Text-to-speech systems built on residual vector quantization often generate audio in two stages: a transformer backbone emits the first level of each frame's token stack, and a smaller depth model generates the rest autoregressively. We ask which components of such a model are responsible for prosodic intonation, more precisely for generating the English nuclear tune (for instance, the falling pitch melody that distinguishes an assertion from a question's rising melody), and whether intervention...
  </details>

- **2026-10-19** — Akash Gokul, Srijan Bansal, Yingbo Zhou et al. — [TEX: Test-Time Scaling Testing Agents via Execution-based Cross-Validation](http://arxiv.org/abs/2610.27290v1)
  <details><summary>📄 Abstract</summary>
  Test-case generation is critical but remains challenging for language models. Existing test-time scaling methods either isolate candidates or aggregate traces, which do not scale to long-horizon tasks. We present TEX, a collaborative test-time scaling framework based on execution-driven cross-validation. TEX parallelizes agents to generate tests and patches, cross-executing each test against every patch to form a $K \times K$ feedback matrix. Agents use their matrix slices for refinement, enabli...
  </details>

- **2026-10-19** — Fedor Part, Valery Isaev, Sergey Sinchuk — [Theorem prover Arend](http://arxiv.org/abs/2610.27264v1)
  <details><summary>📄 Abstract</summary>
  This paper is an exposition of the theorem prover Arend developed at JetBrains Research. Arend language has been designed to facilitate the formalization of mathematics within the framework of univalent foundations and with the focus on constructive mathematics. It is based on a variant of homotopy type theory with cubical syntax that is more closely aligned with Martin-Löf Type Theory (MLTT) than fully computational cubical type theories, while still retaining some of their computational proper...
  </details>

- **2026-10-19** — Zhiwei Liu, Zhujun Lan, Jielin Qiu et al. — [EGI-BENCH: An Enterprise General Intelligence Benchmark Suite](http://arxiv.org/abs/2610.27234v1)
  <details><summary>📄 Abstract</summary>
  Enterprise adoption of LLMs in agentic workflows is gated by evaluations that span a wide arc of abilities: CRM operations, heterogeneous-document retrieval, personal data understanding, multi-turn planning, tool use, function calling, long-horizon research, and long-context software engineering. These evaluations live today in separate repositories with divergent runners, dependencies, and scoring conventions, which makes cross-benchmark comparison difficult and obscures what a single aggregate...
  </details>

- **2026-10-19** — Samee Arif, Furkan Danisman, Angana Borah et al. — [The Culture Within: Towards Mechanistic Understanding of Cultural Reasoning in LLMs](http://arxiv.org/abs/2610.27202v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly operate across culturally diverse settings, yet existing evaluations largely measure cultural behavior at the output level. We introduce CultureLens, a reference-grounded benchmark and mechanistic study of how LLMs use cultural information. CultureLens contains 9,261 scenarios across 75 countries and systematically varies country, value, true-norm, and contradictory-norm evidence. Across Llama-3.1-8B, Gemma-3-12B, and Qwen-3.5-27B, stating a contradictor...
  </details>

- **2026-10-19** — George Nigmatulin, Valentin Mohl, Sascha Frey et al. — [LOB-Impact Benchmark: Emergent Market Impact in Generative Limit Order Book Models](http://arxiv.org/abs/2610.27100v1)
  <details><summary>📄 Abstract</summary>
  Realistic market impact is essential for generative limit order book (LOB) models to serve as world models for trading agents. If a simulator misprices this mechanism, agents learn policies that are optimal in the simulator but wrong in the real market. Existing metrics assess generated streams purely through distributional comparison with historical data, leaving counterfactual response to an agent's own orders largely unexplored. Here, we show that market impact emerges naturally in neural LOB...
  </details>

- **2026-10-19** — Jiaming Liu, Xinghao Zhu, Yiming Zhang et al. — [Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation](http://arxiv.org/abs/2610.26854v2)
  <details><summary>📄 Abstract</summary>
  Multimodal reasoning provides robotic foundation models with predictive context needed for reliable action generation. However, language-based reasoning captures task semantics but struggles to express fine-grained physical dynamics, while latent reasoning models future state evolution but offers limited structure for organizing these dynamics into reusable reasoning primitives. To bridge this gap, we introduce PhysWord, a reasoning-before-acting foundation model built on Physical Words, which u...
  </details>

- **2026-10-19** — Zeyu Zheng, Yiyang Liu, Yuyang Zhao et al. — [ReuF2F: Benchmarking Coding Agents on Formalized Undergraduate Research Problems](http://arxiv.org/abs/2610.27046v1)
  <details><summary>📄 Abstract</summary>
  As AI systems begin to resolve open research problems, reliable verification becomes increasingly important. Formal mathematics provides a trusted framework for mathematical reasoning, enabling agents to produce machine-checkable proofs while conducting mathematical exploration. Existing formal mathematics benchmarks often focus on known results or a small set of prominent open problems, which can become difficult to evaluate reliably once solutions are discovered and widely disseminated. Existi...
  </details>

- **2026-10-19** — Min-Seong Kim, Jongbok Won, Jeesup Park et al. — [Rethinking LLM Fine-Tuning via Weight Space Reparameterization: Preserving Safety during Downstream Adaptation](http://arxiv.org/abs/2610.26443v2)
  <details><summary>📄 Abstract</summary>
  Fine-tuning large language models (LLMs) on downstream tasks often weakens their previously aligned safety behavior, creating an inherent trade-off between task adaptation and safety preservation. Existing approaches attempt to mitigate this issue by identifying safety-relevant neurons, layers, or update directions in the original parameter space. However, safety-related information is often distributed across many directions in this space, causing downstream updates to overwrite parameters that...
  </details>

- **2026-10-19** — Jennifer Hsia, Zachary C. Lipton, Aarti Singh — [Joint Constraint Aggregation for Qualifier-Sensitive Retrieval-Augmented QA](http://arxiv.org/abs/2610.27114v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented QA can fail even when the correct answer is in the retrieved evidence. This can happen when a competing answer satisfies some, but not all, of the question's requirements and is mentioned frequently in the retrieved documents, which can make it appear to be the best-supported answer. To test whether this retrieval skew actually affects the decision, we manipulate it directly: increasing the prevalence of passages that favor the competing answer makes the model more likely to ...
  </details>

- **2026-10-19** — Zijian Liu, Chaoyou Fu, Yan Yang et al. — [Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for Omni LLMs](http://arxiv.org/abs/2610.27103v1)
  <details><summary>📄 Abstract</summary>
  Recent Omni LLMs (OLLMs) have demonstrated remarkable capabilities in joint audio-visual reasoning, yet cross-modal hallucinations remain a major challenge. Existing mitigation methods mainly operate at the output level, overlooking the entanglement of grounding evidence and learned priors within fused representations. To address this issue, we propose Omni-Woodpecker (OWP), a training-free framework that shifts hallucination mitigation from output-level manipulation to conflict-conditioned repr...
  </details>

- **2026-10-19** — Yinhe Wang, Tao Tao, Zexin He et al. — [ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models](http://arxiv.org/abs/2610.27040v1)
  <details><summary>📄 Abstract</summary>
  General-purpose multimodal models, including GPT-6 Astra and Claude Opus 5.5, demonstrate broad capabilities in embodied manipulation. Our analysis indicates that this generality is accompanied by strong spatial perception, as Astra can determine where to interact with task-relevant entities amid visual distractors. Because spatial perception connects high-level reasoning to the physical scene, we investigate scaling visual grounding to strengthen the perceptual foundation of general embodied op...
  </details>

- **2026-10-19** — Feng Chen, Pei Zhou, Lixuan He et al. — [Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning](http://arxiv.org/abs/2610.27039v1)
  <details><summary>📄 Abstract</summary>
  Foundation models offer a promising basis for robotic agents, but long-horizon tasks require them to sustain coherent reasoning and reliable physical execution across interdependent stages. We introduce Embodied Playground, a benchmark for evaluating how foundation-model agents coordinate physical, strategic, and spatial reasoning throughout such tasks. Agents must track task progress, satisfy intermediate constraints, and revise their plans using execution feedback as earlier actions shape subs...
  </details>

- **2026-10-19** — Oveys Delafrooz Noroozi, Bhagyashree Puranik, Upamanyu Madhow — [Shaped SAEs: Expanding the Toolkit for Mechanistic Interpretability](http://arxiv.org/abs/2610.27375v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) seek to decompose the dense activations of large language models (LLMs) into sparse, potentially interpretable features using a learned overcomplete dictionary. In this work, we ask whether it is possible to enhance the semantic selectivity of the learned dictionary atoms by linearly \emph{shaping} the dense activations prior to learning an SAE. We explore rank-reducing transformations based on the recently introduced J-space corresponding to the averaged Jacobian from...
  </details>

- **2026-10-19** — Soukaina Alaoui Ismaili, Jean-Sebastien Dessureault — [An LLM-Based Agent for Legal Compliance Assessment: Architecture, Memory, and Evaluation in a Canadian and Quebec Context](http://arxiv.org/abs/2610.27347v1)
  <details><summary>📄 Abstract</summary>
  Checking whether a text complies with a body of law is slow when done by hand and fragile when done with keyword rules. This paper presents ComplianceAgent, the legal compliance sub-agent of COMPASS, a multi-agent framework that evaluates texts along four axes: digital sovereignty, carbon impact, compliance, and ethics. The agent relies on a large language model that scores a text on a fixed rubric, grounds its judgment in a reference legal corpus, and, when the score falls at or below a critica...
  </details>

- **2026-10-19** — Hangyue Zhang, Qiran Hu, Ziyi Zhang et al. — [Inspectable LLM-Simulated Participants for Qualitative Interview Rehearsal](http://arxiv.org/abs/2610.27333v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used across research workflows, including research ideation, qualitative analysis, and participant simulation. Within work on participant simulation, prior studies have largely evaluated simulated participants by how realistic or human-like their responses appear, leaving less known about how researchers use and critique these materials when revising interview protocols before fieldwork. We present Rehearsim, an inspectable research probe that treats LLM-simulated participa...
  </details>

- **2026-10-19** — Paraskevi Platanou, John Pavlopoulos — [What Not to Erase: Saliency-Constrained Augmentation for Low-Resource Handwritten Character Recognition](http://arxiv.org/abs/2610.27309v1)
  <details><summary>📄 Abstract</summary>
  Optical Character Recognition (OCR) and handwritten character recognition (HCR) in low-resource historical material collections often rely on data augmentation, yet augmentation strategies are typically evaluated almost exclusively through predictive accuracy. This leaves open whether a model's improved performance is accompanied by saliency stability. This question is important in low-resource historical HCR, where recognition is performed on variable and partially degraded letterforms and two ...
  </details>

- **2026-10-19** — Yuqiao Wen, Lili Mou — [ICLHerd: Herding-Based Data Selection for LLMs with In-Context Learning as a Proxy](http://arxiv.org/abs/2610.27142v1)
  <details><summary>📄 Abstract</summary>
  Data selection plays a central role in modern large language model training, as the quality of training data strongly influences downstream performance. A common approach is to curate a development set that encodes the desired skills (e.g., reasoning or multilinguality) and select data that are similar to them. Existing methods compute similarity using cosine distance over either the model's hidden states or gradients. However, we observe that this max-similarity strategy induces a mode-seeking ...
  </details>

- **2026-10-19** — Lijia Wu, Zheng Li, Yuxuan Liu et al. — [SciFigBench: A Benchmark for Scientific Method Figure Understanding](http://arxiv.org/abs/2610.27087v1)
  <details><summary>📄 Abstract</summary>
  Scientific method figures often provide researchers with a clear visual entry point into a paper's methodology and core contributions, yet their dense layouts and complex information flows are difficult for Vision Language Models (VLMs) to interpret. Existing benchmarks predominantly focus on coarse-grained tasks, such as context-based retrieval or holistic comprehension, overlooking the fine-grained content and inter-module relations within complex methodological diagrams. To address these over...
  </details>

- **2026-10-19** — Motti Goldberger, Nils Rudi — [Selecting the Best Few with Human Evaluators: Adaptively Combining Ratings and Pairwise Comparisons](http://arxiv.org/abs/2610.26380v2)
  <details><summary>📄 Abstract</summary>
  This paper considers a decision-maker tasked with identifying the $k$ best items from a large pool of candidates, such as job applicants, LLMs, award nominees, or new product ideas. The decision-maker learns about the items' quality by soliciting human evaluations. Each evaluation can be costly, so the decision-maker aims to use the limited evaluation budget efficiently by allocating evaluations adaptively. A key consideration is the form of evaluation to solicit, which should be something evalu...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 687 |
| prompt-injection | 629 |
| memory-poisoning | 56 |
| tool-use-attack | 158 |
| backdoor | 530 |
| adversarial-attack | 643 |
| privacy-leakage | 4427 |
| steganography | 80 |
| misuse | 1214 |
| red-teaming | 144 |
| vulnerability | 3683 |
| defense | 3554 |
| alignment | 3338 |
| robustness | 3617 |
| watermark | 632 |
| unlearning | 116 |
| agent-safety | 65 |
| benchmark | 70 |
| survey | 411 |
| other | 9753 |

---

📚 **全部 33807 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-21 11:01:42*