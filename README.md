<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-38505-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-24 16:52 ｜ **论文总数 / Total Papers**: 38505（近 30 天 / Recent 30 days: 4162）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 38505 篇论文（含摘要、分类筛选、搜索）/ View all 38505 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 729
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 704
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 59
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 179
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 569
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 679
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4663
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 94
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1351
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 158
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 4136
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 4079
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3823
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 4190
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 806
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 126
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 77
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 468
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 11548

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4162 篇，完整 38505 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4162 papers from the last 30 days (with date, authors & abstract). For the full list of 38505 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-11-22** — Honghao Feng, Shanhan Qu, Kai Tong et al. — [Adaptation or Poisoning? Security Risks of Conversational Test-Time Learning in Large Language Models](http://arxiv.org/abs/2611.29532v1)
  <details><summary>📄 Abstract</summary>
  Test-time learning (TTL) enables large language models to adapt to unlabeled inputs during deployment. The model updates a lightweight adapter by minimizing the next-token prediction loss on the input it receives. When these updates persist across conversation turns, every user query serves both as the request answered in the current turn and as adaptation data for later turns. By choosing the queries used for adaptation, an attacker can influence parameter updates and weaken safety alignment th...
  </details>

- **2026-11-22** — Saadh Jawwadh — [From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](http://arxiv.org/abs/2611.29303v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of Large Language Model (LLM) research makes it increasingly difficult to distinguish incremental refinements from true paradigm shifts. This review evaluates 22 of the most influential publications spanning nearly three decades (1997-2026), organized through a causal, chronologically anchored taxonomy centered on the author's birth year (1999). Beginning "before 1999" with how recurrent neural networks (RNNs) forgot earlier context (much like forgetting Chapter 1 by the ...
  </details>

- **2026-11-22** — Haichuan Zhang, Xinyu Sun, Shih-Chieh Dai et al. — [Persistent Jailbreak Backdoor Attack](http://arxiv.org/abs/2611.29217v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment is widely used to align large language models (LLMs) to produce helpful and harmless responses. However, an attacker can plant a jailbreak backdoor in an LLM such that adding a universal trigger word or phrase to a harmful prompt elicits attacker-desired responses. Existing jailbreak backdoor attacks induce distinct behaviors on backdoored inputs and safety samples (harmful prompts paired with refusal responses), making the backdoors susceptible to subsequent safety alignment an...
  </details>

- **2026-11-19** — Dohyeon Kwon — [SEOYUN: Refusal-Inducing Exam Documents for AI-Glasses Pipelines](http://arxiv.org/abs/2611.26033v1)
  <details><summary>📄 Abstract</summary>
  Camera-equipped glasses can convert an examination page into a query to a vision-language model (VLM). Device detection addresses possession; a complementary question is whether an examination document can reduce the usefulness of an unauthorized capture. We present SEOYUN, an application-specific framework for refusal-inducing exam documents, with optical and encoder-level interventions as extensions. We use reverse jailbreaking to describe the direction of the objective: inducing abstention ra...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 10 papers

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

- **2026-11-21** — Gabi Nakibly, Zvika Babo — [Who Is Prompt-Injecting Coding Agents? An Empirical Study of Hidden AI-Directed Text on GitHub](http://arxiv.org/abs/2611.28763v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents now triage issues, review pull requests and pick up tasks inside GitHub repositories, and to do so they read text that anyone with a GitHub account can write. This makes GitHub a prime surface for indirect prompt injection, in which instructions embedded in untrusted content steer a model that later processes it. Prior work has demonstrated such attacks against agents on GitHub in controlled settings, but how often they occur in practice, who deploys them, and for what purpose r...
  </details>

- **2026-11-21** — Rongyi Zhu, Tanqiu Jiang, Fenglong Ma et al. — [Understanding and Mitigating the Fragility of Self-Rewarding Optimization](http://arxiv.org/abs/2611.28582v1)
  <details><summary>📄 Abstract</summary>
  Self-rewarding optimization (SRO) promises to improve language models by enabling them to generate their own reward signals. Yet when and how SRO succeeds or fails remains poorly understood. We reveal that SRO is fundamentally fragile: even seemingly benign perturbations to training prompts can corrupt the self-generated preference signal and trigger iterative collapse. We demonstrate this through two prompt-level attacks that serve as controlled stress tests: a Re-Ranking attack that concentrat...
  </details>

- **2026-11-21** — Salman Hajizada, Mohammed Yusuf Ansari, Gianni Di Caro — [Beyond Unit Tests: Path-Aware Rubric-Guided LLM Autograding of Notebooks](http://arxiv.org/abs/2611.28565v1)
  <details><summary>📄 Abstract</summary>
  Jupyter notebooks support open-ended, multi-step assessments in which students build one logical flow across interdependent steps, combining code, written analysis, and generated outputs such as plots. These reflect authentic scientific practice but are hard to grade consistently, since students may make different yet equally valid choices at each step, so a later answer can only be judged in light of the choices a student made earlier. We present an LLM-based autograder for such flow-structured...
  </details>

- **2026-11-19** — Mengxiao Wang, Mahbub Alam, Kalyan Nakka et al. — [Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)](http://arxiv.org/abs/2611.26553v1)
  <details><summary>📄 Abstract</summary>
  Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether agents fail, but neither replicates an incident nor tests the cause its report might i...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-11-23** — Kang Yang, Kevin Ying, Xiaojing Liao et al. — [Demystifying Detectors Guarding Agent Skill Hubs](http://arxiv.org/abs/2611.30913v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills has gained widespread adoption as an open standard for extending agent capabilities. To facilitate skill sharing, public skill hubs have grown in popularity and increasingly rely on automated security detectors to identify malicious skills at scale. Yet, the effectiveness and limitations of these detectors remain insufficiently understood. To fill this gap, we present the first systematic study of four hub-adopted and two community-provided malicious skill detectors on 1477 agent sk...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 6 papers

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

- **2026-11-21** — Chengzhong Wang, Lang Lin, Shengfang Zhai et al. — [Mitigating Backdoors in Masked Diffusion Language Models](http://arxiv.org/abs/2611.28640v1)
  <details><summary>📄 Abstract</summary>
  Masked diffusion language models (MDLMs) have emerged as a promising alternative to autoregressive models because they can predict multiple tokens in parallel rather than generating tokens sequentially. However, recent studies have shown that MDLMs are vulnerable to backdoor attacks: when an input contains an attacker-chosen trigger, a backdoored model generates a targeted output, such as malicious code, while otherwise behaving normally. Despite this threat, backdoor defenses for MDLMs remain l...
  </details>

- **2026-11-21** — Mohammed Tanveer — [Weight-Space Backdoors in Open-Weight LLMs: Cross-Architecture Attacks and Blind Model Forensics](http://arxiv.org/abs/2611.28543v1)
  <details><summary>📄 Abstract</summary>
  Open-weight language models are vulnerable to trigger-conditioned behaviors introduced through sparse post-training weight modifications, creating supply-chain risks beyond conventional provenance checks. We present Neural Sentinel, a cross-architecture study of gradient-guided backdoor insertion and model forensics spanning 18 checkpoints across 14 architecture families (124M-31.3B parameters), including state-space and recurrent models.   On Phi-2, modifying approximately 0.0002% of parameters...
  </details>

- **2026-11-20** — Xuyang Liu, Zhiwei Xu, Zirui Li et al. — [Autonomous Parameter Surgery: How LLMs Implant Selective Backdoors into Language Models](http://arxiv.org/abs/2611.27920v1)
  <details><summary>📄 Abstract</summary>
  Neural network weights are usually treated as opaque artifacts of gradient descent. Recent work on weight space programming, however, suggests that large language models can inspect and rewrite another network's parameters directly. In this paper, we ask whether a general language model can turn a natural language backdoor specification into persistent, selective weight edits on its own, without gradient training, layer hints, external corpora, or a prescribed editing formula. Using DeepSeek Fla...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-11-21** — Chengyin Hu, Dehe Zhao, Dingyi Lu et al. — [When Fog Becomes a Weapon: Atmospheric Attacks on Visible-Infrared Vision-Language Models](http://arxiv.org/abs/2611.28592v1)
  <details><summary>📄 Abstract</summary>
  Existing adversarial attacks on vision-language models (VLMs) and cross-spectral perception primarily rely on conspicuous, unnatural artifacts, such as vivid adversarial patches or active light beams, that lack physical stealthiness, whereas prior weather attacks largely overlook how one atmosphere simultaneously affects heterogeneous sensors. This raises a key scientific question: can a purely natural, shared fog environment simultaneously disrupt complementary visible and thermal infrared cues...
  </details>

- **2026-11-19** — Li Zeng, Yeqi Zeng, Hengkai Liang et al. — [VisualJevBench: A Benchmark and Black-Box Attacks for Visual Typed Decision Models](http://arxiv.org/abs/2611.25435v1)
  <details><summary>📄 Abstract</summary>
  Typed decision models (TDMs) return structured decisions instead of generating free-text responses, enabling fast and cheap decisions in real-world applications. Recent support for image inputs extends Jev, a representative TDM, to visual decision-making. We refer to this setting as Visual Jev. However, red teaming of Visual Jev leaves two gaps: a systematic evaluation of direct image manipulations is lacking, and universal visual attacks remain underexplored. To address these gaps, we introduce...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 20 papers

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

- **2026-11-22** — Ismat Jarin, Tu Le, Athina Markopoulou — [FORGETMENOT: Auditing Memory Driven Privacy Risks in Commercial AI Agents](http://arxiv.org/abs/2611.29804v1)
  <details><summary>📄 Abstract</summary>
  Commercial AI agents increasingly incorporate long-term memory (both persistent and chat-history) to enable more accurate and personalized responses, raises significant privacy and policy concerns. Yet little is known about user privacy risks associated with memory behavior, in particular, about memory storage, disclosure, transparency and deletion control. To bridge this gap, we propose FORGETMENOT, an auditing framework for analyzing the privacy risks of long term memory in commercial AI agent...
  </details>

- **2026-11-22** — Ke Changke, Jian Wang, Xuan Xu et al. — [NPUFHE: An Efficient CKKS Execution System for Ascend NPUs](http://arxiv.org/abs/2611.29353v1)
  <details><summary>📄 Abstract</summary>
  Fully homomorphic encryption (FHE) enables computation directly on encrypted data, but its substantial computational cost hinders adoption in privacy-preserving artificial intelligence (AI) applications. Neural processing units (NPUs) already deployed in AI infrastructure provide a practical platform for FHE acceleration. However, after mapping the number theoretic transform (NTT) to matrix multiplications on Ascend NPUs, modular arithmetic and representation conversion on the Vector backend sti...
  </details>

- **2026-11-22** — Honghui You, Haoping Yang, Wenzhe Wang et al. — [TurboFHE: An Efficient and Scalable Multi-GPU Framework for Homomorphic LLM Inference](http://arxiv.org/abs/2611.29244v1)
  <details><summary>📄 Abstract</summary>
  Fully homomorphic encryption (FHE) enables privacy-preserving large language model inference but remains computationally intensive. Existing multi-GPU FHE inference systems rely on expert-crafted parallelization plans that generalize poorly across hardware platforms and applications. We present \fwName, a framework that automatically compiles CKKS inference programs into efficient multi-GPU executables. Its compiler can split different nodes of the same computation graph at the ciphertext and po...
  </details>

- **2026-11-22** — Hassan Khodaiemehr, Khadijeh Bagheri, Chen Feng — [Ziv Meets Sumcheck: Zero-Knowledge Proofs of Floating-Point LLM Inference](http://arxiv.org/abs/2611.29188v1)
  <details><summary>📄 Abstract</summary>
  Zero-knowledge proofs can show that a neural network produced a given output without revealing the network, but current systems for language models prove integer approximations of the model rather than the floating-point arithmetic that is actually deployed. Proving floating-point matrix multiplication has been regarded as hard, because rounding after every addition makes the result depend on the order of the additions. We avoid this obstacle by proving the correctly rounded product, in which ev...
  </details>

- **2026-11-21** — Inigo Stibbe, Padmanabhan Ramnarayan, A. Aldo Faisal — [Synthetic EHR Generators Should Be Audited Like LLMs](http://arxiv.org/abs/2611.28804v1)
  <details><summary>📄 Abstract</summary>
  Synthetic electronic health record (EHR) generation is increasingly adopting large autoregressive models, yet privacy evaluation has not kept pace, relying heavily on similarity-based heuristics and aggregate metrics that can obscure patient-specific memorisation. We argue that these models should additionally undergo LLM-style memorisation audits at the level of individual patient records. We support this position by comparing membership-inference evaluations across four prominent autoregressiv...
  </details>

- **2026-11-21** — Syed Khaderi, Karima Makhlouf, Sami Zhioua — [Beyond Single-Turn Privacy: Training-Data Leakage in Conversational RAG](http://arxiv.org/abs/2611.28748v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) is known to reduce training-data leakage in single-turn interactions, but whether this protection persists over multi-turn conversations is unclear. We introduce CRELT (Conversational RAG Extraction Leakage Trajectory), a reusable framework that tracks, turn by turn, the real contact details from the training data that a RAG system discloses. CRELT separates retrieval, conversation history, and attack strategy through a full-factorial design, uses a retrieval...
  </details>

- **2026-11-21** — Aleksandra S. Zheleznova, Iuliia A. Timankova, ZiWei Ye et al. — [Acoustic bound states in the continuum in a labyrinthine meta-atom](http://arxiv.org/abs/2611.29091v1)
  <details><summary>📄 Abstract</summary>
  In this Letter, we theoretically and experimentally study acoustic bound states in the continuum (BICs) emerging in labyrinth meta-atom embedded in an acoustic waveguide. A symmetry-protected BIC is supported in the lossless limit when the meta-atom is positioned on the waveguide axis. Breaking the symmetry by shifting the meta-atom away from the center of the waveguide transforms the BIC into a radiative quasi-BIC, manifested by the emergence of a narrow resonant feature in the transmittance sp...
  </details>

- **2026-11-20** — Guangyuan Ji, Wenjing Wang, Bingsheng Zhang — [Your Camera Can Hear You: Side-Channel Acoustic Eavesdropping via Android Camera2 Metadata](http://arxiv.org/abs/2611.27964v1)
  <details><summary>📄 Abstract</summary>
  To prevent motion sensors from acting as covert microphones, Android 12+ caps SensorManager gyroscope and accelerometer rates at 200 Hz by default, requires HIGH_SAMPLING_RATE_SENSORS for higher rates, and throttles sensors back to 200 Hz when the microphone toggle is off. We show that Android's Camera2 subsystem bypasses these defenses. During an active Camera2 session, Camera HAL stabilization pipelines record high-rate gyroscope measurements and export them via vendor CaptureResult metadata. ...
  </details>

- **2026-11-19** — Zhihao Liu, Zixiong Guo, Shuo Shao et al. — [Ask in the Crowd: Differentially Private LLM Inference via Dummy-Augmented Shuffling](http://arxiv.org/abs/2611.25669v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as LLM-as-a-Service (LLMaaS), where user queries are sent to remote LLMs for inference, raising severe privacy concerns about the exposure of sensitive user inputs. Differentially private inference mitigates these risks by injecting noise into input embeddings. However, existing methods struggle to balance privacy and utility, as stronger privacy protection often leads to substantial accuracy degradation in LLM inference.   In this work, we propose...
  </details>

- **2026-11-19** — Haijun He, Fei Li, Donghong Ji et al. — [Erasing the Wrong Thing: Conditional Attribute Leakage and Concept Erasure in Shared Foundation-Model Embeddings](http://arxiv.org/abs/2611.25640v1)
  <details><summary>📄 Abstract</summary>
  Medical-image embeddings are increasingly shared in place of raw images for authorized downstream tasks, yet they may reveal sensitive attributes. Standard concept-erasure methods target population-level guardedness. However, we prove that, when binary task and sensitive labels are associated, global and task-conditional linear guardedness cannot both hold while a nonzero linear task signal is preserved, so global erasure must either eliminate that signal or retain task-conditional linear leakag...
  </details>

- **2026-11-19** — Wei Li, Yiheng Zhang, Zhaofan Qiu et al. — [MultiBinder: Preventing Multi-Subject Identity Leakage in Personalized Video Generation](http://arxiv.org/abs/2611.26164v1)
  <details><summary>📄 Abstract</summary>
  Personalized video generation faces a significant scalability challenge: as the number of custom subjects increases, existing methods suffer from severe identity leakage and semantic entanglement, resulting in videos with blended attributes and incoherent narratives. We identify that this stems from a lack of explicit binding between textual entity phrases and their corresponding visual patterns prior to fusion in diffusion models. To address this, we propose MultiBinder, a novel framework built...
  </details>

- **2026-11-19** — Ishita Asnani, Shaghayegh Fazliani, Zachary Ryan et al. — [Design and Evaluation of Epira: An Automated Interview System for Case Investigation and Contact Tracing](http://arxiv.org/abs/2611.25577v1)
  <details><summary>📄 Abstract</summary>
  Objective: Case investigation and contact tracing are labor-intensive. Web forms struggle when respondents need clarification before disclosing contacts, and open-ended chatbots may deviate from protocols. We developed and evaluated Epira, a protocol-controlled large language model (LLM) interviewer for multi-disease case investigation and contact tracing.   Materials and Methods: Epira pairs LLM dialogue with a rule-based controller enforcing required questions, safety handoffs, and a structure...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-11-23** — Sina Abdollahi, Amir Al Sadi, Marios Kogias et al. — [Airlock: Robust Sandboxing and Governance of Rogue Agents](http://arxiv.org/abs/2611.31010v1)
  <details><summary>📄 Abstract</summary>
  Recent incidents involving agents bypassing sandboxing and network isolation have raised concerns about existing agent harnesses, prompting frontier labs such as OpenAI to reevaluate the security of their training platforms. Incident reviews show that determined agents can escape processes, containers, and VMs, or bypass their isolation through advanced side and covert channels. Follow-up audits also found that some agents concealed their actions by disabling monitoring and tampering with logs. ...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 12 papers

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

- **2026-11-22** — Yifan Duan, Du Yin, Siyuan Zheng et al. — [DoppelVet: Comparative Safety Verification for Self-Evolving Agents](http://arxiv.org/abs/2611.29306v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents improve by retaining feedback as reusable memories or skills, but every mistaken approval can shape many future behaviors. Two updates can provide exactly the same evidence to a verifier yet produce opposite safety outcomes, so the verifier cannot distinguish them from that evidence alone. We introduce DoppelVet, a verification framework that checks proposed updates before they enter an agent's persistent state. Without access to safety labels, DoppelVet constructs an altern...
  </details>

- **2026-11-21** — Zhe Chen, Emma Hsieh, Vicky Fu — [Agent Money Benchmark: Can AI Agents Be Trusted to Spend Money?](http://arxiv.org/abs/2611.28610v1)
  <details><summary>📄 Abstract</summary>
  Giving an AI agent a wallet lets it buy data and services on a client's behalf. Trust then depends on how it spends money and what that spending achieves. We introduce Agent Money Benchmark (AMB) to test whether agents spend a client's money well, starting with purchases of information for financial decisions. We link seller quotes and payments to final answers, evaluating 12 models on 80 payment tasks with simulated sellers and 76 research questions using live data. Purchases settled in USDC on...
  </details>

- **2026-11-21** — Xinyu Cao, Tianjie Ju, Zhuosheng Zhang — [EvoViM: Recursively Self-Evolving Visual Agents for Exploration with Deferred Queries](http://arxiv.org/abs/2611.28574v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language model (MLLM) agents have shown promising capabilities in task-oriented environments. However, they still struggle when queries are deferred until after exploration, requiring them to retain visual evidence before knowing which details will matter. We introduce EvoViM, a recursively self-evolving framework in which a frozen multimodal model turns its own interaction experience into one visual program for memory and skills. The program retains images and computes directly...
  </details>

- **2026-11-19** — Xuankun Rong, Xinhao Deng, Wenzhang Jiang et al. — [DailySafe: Benchmarking Dynamic Safety Awareness in Everyday Multi-Turn Multimodal Interactions](http://arxiv.org/abs/2611.26298v1)
  <details><summary>📄 Abstract</summary>
  As multimodal large language models (MLLMs) become increasingly integrated into everyday life, their ability to provide safe and reliable assistance in realistic daily activities remains insufficiently explored. Existing safety benchmarks primarily focus on isolated harmful requests or adversarial scenarios, overlooking the safety risks that may arise as ordinary tasks unfold. In practice, users pursue legitimate goals through multi-turn, multimodal interactions, where seemingly benign requests ...
  </details>

- **2026-11-19** — Qi Shen, Yujia Gong, Yue Zhao et al. — [A Wolf in Sheep's Pixels: Visual Camouflage Attacks via HDR Gain Maps](http://arxiv.org/abs/2611.25469v1)
  <details><summary>📄 Abstract</summary>
  An image can pass automated safety checks while showing harmful content to its human viewer. We introduce DRJanus, a visual camouflage attack that exploits the gap between standard dynamic range (SDR) processing and high dynamic range (HDR) display. Automated systems often read only an image's SDR base, whereas HDR viewers reconstruct its appearance using an auxiliary gain map. DRJanus inverts this reconstruction to embed two independently chosen color images in a single JPEG, without querying o...
  </details>

- **2026-11-19** — Charlotte Peart, Franziska Sofia Hafner, Luc Rocher — [Evaluating safeguarding in multi-turn conversations with AI assistants](http://arxiv.org/abs/2611.26009v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI assistants are now used for personal and emotional support. Developers report improvements in how new models respond to sensitive conversations, yet users and civil society continue to raise concerns about their behaviour in real-world, repeated interactions that safety evaluations rarely capture. Often, evaluations present signs of distress clearly and in a single message, even though people may reveal their struggles gradually in otherwise ordinary conversations. We worked wi...
  </details>

- **2026-11-19** — Haoyang Xu, Qirui Wang, Liuwan Zhu — [Question, Then Affirm: Restoring Commitment Does Not Restore Refusal](http://arxiv.org/abs/2611.25929v1)
  <details><summary>📄 Abstract</summary>
  We find that safeguards for image generation can be bypassed without changing what a message says. A sign stating a harmful proposition is blocked, but the same proposition phrased as a question and followed by a check mark is generated, even though the resulting image endorses the original claim. On a 300-case challenge set, gpt-image-2 returns images for 43.3% of question-affirmation requests versus 16.3% of direct statements, with 41.3% versus 15.3% of cases yielding images that endorse the o...
  </details>

- **2026-11-19** — Viet Cuong Nguyen, Fiona Li, Chang Wan et al. — [From Reliance to Overreliance: Taxonomizing and Detecting Relational Risks in AI Companionship](http://arxiv.org/abs/2611.25734v1)
  <details><summary>📄 Abstract</summary>
  Companion AIs are increasingly used for emotional support, yet distinguishing meaningful engagement from harmful reliance remains difficult. We introduce the Taxonomy of Relational Risks (TRR), which operationalizes users' emotional overreliance (EO) as observable conversational behaviors and separately identifies evidence of relational harm (RH), enabling empirical examination of when reliance behaviors co-occur with adverse consequences. Using naturalistic Character.AI and Replika conversation...
  </details>

- **2026-11-19** —  LingSante MedGuard Team — [LingSante MedGuard Technical Report](http://arxiv.org/abs/2611.25509v1)
  <details><summary>📄 Abstract</summary>
  As medical AI is increasingly used for patient consultation and clinical decision support, identifying harmful, non-compliant, or ethically problematic responses is essential for responsible deployment. Assessing these risks requires checking clinical claims against relevant evidence, verifying calculations, and applying medical requirements under their intended conditions. We introduce LingSante MedGuard, a capability-enhanced guardrail that integrates supervision from a medical guardrail teach...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-11-23** — Zhongyuan Lyu, Xiaocong Xu — [Sequential Selection against an Adaptive Opponent](http://arxiv.org/abs/2611.30006v1)
  <details><summary>📄 Abstract</summary>
  Selecting a strategy by testing it against an opponent is common in game-playing AI, red-teaming of language models, and safety evaluations of AI agents. In many of these settings, the opponent adapts to what it observes, so a strategy that keeps winning in practice may already have stopped working by the time it is used. Motivated by these settings, we study a player who tries strategies in practice games against an adaptive opponent, decides when to stop, and then either selects one strategy f...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 45 papers

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

- **2026-11-21** — Changyu Liu, Fei Zhao, Yiyang Liu et al. — [Learning from Another Angle: Rotation-Based Test-Time Training for Multimodal Large Language Models](http://arxiv.org/abs/2611.28972v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) achieve strong performance on vision-language tasks but often remain vulnerable to distribution shifts due to their fixed parameters during inference. While Test-Time Training (TTT) offers a pathway for dynamic adaptation, existing approaches suffer from prohibitive computational overhead due to multiple sampling and the risk of error reinforcement from biased self-generated supervision. In light of this view, we propose RoTTT (Rotation-based Test-Time Tr...
  </details>

- **2026-11-21** — Haomin Bai, Dingzhi Yu, Xuling Zhao et al. — [DRAM: Memory-Efficient Muon via Rank Reallocation in Principal-Random Subspaces](http://arxiv.org/abs/2611.28595v1)
  <details><summary>📄 Abstract</summary>
  Memory-efficient Muon methods aim to reduce storage overhead while preserving strong performance, yet existing approaches compromise either convergence guarantees or practical efficiency. In this paper, we focus on subspace optimization for Muon, where the choice of subspace determines the gradient information retained for updating. To preserve dominant information while providing the coverage needed for stochastic convergence guarantees, we construct a principal-random subspace that combines le...
  </details>

- **2026-11-21** — Leizhen Zhang, Sheng Chen — [Right Verdict, Right Reason? An Execution-Grounded Study of Whether LLM Vulnerability Detectors Understand Vulnerabilities](http://arxiv.org/abs/2611.28584v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to detect vulnerabilities, and their benchmark scores are often read as evidence that they understand the vulnerabilities they report. We test this reading against program execution. For 515 C and C++ functions from BigVul and PrimeVul whose vulnerability we reproduce with a proof of concept, we identify the line at which the fault occurs and the statements on which the faulting run depended. These facts ground a ladder of five tests, from telli...
  </details>

- **2026-11-19** — Amine Lbath, Manan Suri, Aurelien Delaitre et al. — [SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research](http://arxiv.org/abs/2611.26601v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are scattered across papers, vendor reports and disclosures and are rarely comparable. We introduce a framework that rates these capabilities on an autonomy scale modeled on the levels of driving automation, and qualifies each claim by its correc...
  </details>

- **2026-11-19** — Yizhe Ding, Yifan Jiang, Runze Li et al. — [Optimal Transport Rank Regression for Robust Multivariate-Response Regression](http://arxiv.org/abs/2611.26467v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose optimal transport rank regression for robust multivariate-response mean regression. The proposed method maps residual distributions to the uniform measure on the unit ball and constructs its loss from the resulting optimal transport ranks. This construction exploits cross-response dependence to improve efficiency while preserving population Fisher consistency and orthogonal invariance. Beyond these population properties, we establish statistical guarantees for the propo...
  </details>

- **2026-11-19** — Zhilong Liu, Xiangzhen Zhou, Yunqi Huang et al. — [CAVQS: Context-Aware Variational Quantum Circuit Synthesis via Unitary Redistribution and Dynamic Reconstruction](http://arxiv.org/abs/2611.26219v1)
  <details><summary>📄 Abstract</summary>
  Variational quantum circuit synthesis jointly searches circuit structure and continuous parameters to reduce costly two-qubit gates, but block-based workflows typically instantiate blocks independently, limiting simplification across block boundaries. Moreover, fully unitary synthesis does not exploit opportunities created by permitted output measurements and classical feedforward. We present CAVQS, a context-aware variational synthesis framework that combines unitary redistribution and dynamic ...
  </details>

- **2026-11-19** — Tim Barsch, Bruno Nogueira, Tobias Wienand et al. — [SCARVA: Interpretable Agentic Reasoning in Software Supply-Chain Analysis](http://arxiv.org/abs/2611.26131v1)
  <details><summary>📄 Abstract</summary>
  Complex applications may inherit security vulnerabilities from their dependencies, though a vulnerable dependency does not necessarily endanger the application. Existing tools flag dependencies associated with public vulnerabilities, and more advanced ones analyze the call graph to assess whether the vulnerable code is reachable. However, these approaches are limited to specific programming languages and ecosystems. LLM agents are promising candidates for this task, yet they hallucinate, take sh...
  </details>

- **2026-11-19** — Weijiang Xiong, Nikolas Geroliminis — [SenseAlign: Learning Decision-Aligned Predictive Representations for Active Urban Sensing with UAVs](http://arxiv.org/abs/2611.26109v1)
  <details><summary>📄 Abstract</summary>
  Active urban sensing orchestrates a mobile sensor fleet to proactively inspect a dynamic road network and gather critical information for system management. This problem simultaneously requires understanding the complex spatio-temporal evolution and making decisions with partial observations. In this work, we focus on active sensing in a large-scale urban road network with utilities grounded in dynamic traffic states, while prior work has rarely considered these factors jointly. We propose \emph...
  </details>

- **2026-11-19** — Joana M. Teixeira, Tomás Lopes, Tiago D. Ferreira et al. — [High-Speed Widefield Hyperspectral Imaging](http://arxiv.org/abs/2611.26097v1)
  <details><summary>📄 Abstract</summary>
  Fourier-transform hyperspectral imaging is an emerging technology that combines widefield acquisition with flexible spectral resolution. Yet, it typically requires the acquisition of dense sequences of full-field interferograms during optical-path scanning, which ultimately reduces the final throughput. To circumvent this limitation, this manuscript introduces an event-based Fourier-transform hyperspectral microscopy technique that exploits the coupling of a neuromorphic event camera with a comm...
  </details>

- **2026-11-19** — Robin Geens, Thomas Debelle, Marian Verhelst et al. — [Kameleo: In-Situ Activation-Precision Selection for Bit-Serial LLM Accelerators](http://arxiv.org/abs/2611.25971v1)
  <details><summary>📄 Abstract</summary>
  Weight-only quantization keeps the activations of large language models (LLMs) in a higher-precision format, pushing the on-chip inference cost to the activation arithmetic. Bit-serial, variable-length accelerators offer a promising path to reduce this cost by lowering activation precision while preserving model quality. They process only the mantissa bits that each layer needs. The length has to be chosen per layer and operator, and today it is chosen by offline calibration: a search driven by ...
  </details>

- **2026-11-19** — Qifan Wang, Jeremy Boy, Jonas Sander et al. — [BlockJack: Cross-Tenant Redirection Fault Attacks on Paged KV Cache Address Translation in LLM Serving](http://arxiv.org/abs/2611.25945v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) serving frameworks accelerate inference by retaining previously computed states in a key-value (KV) cache. Paged serving frameworks such as vLLM organize this cache through block tables analogous to OS page tables, which map each request's logical KV blocks to physical KV blocks, forming a software-managed address translation layer. Although fault attacks such as Rowhammer have exploited OS page tables to redirect memory accesses, prior fault attacks on LLMs have large...
  </details>

- **2026-11-19** — Pironti Francesco Aurelio, Arena Luigi, Blefari Francesco et al. — [RAVEN: A Self-RAG Based Agent for Threat Classification and Response](http://arxiv.org/abs/2611.25832v1)
  <details><summary>📄 Abstract</summary>
  Security event analysis in large enterprises can be overwhelming, as each alert typically requires manual in- spection by human operators. This process is time-consuming and prone to inconsistencies, especially in high-volume Secu- rity Operations Center (SOC) environments. In this work- in-progress paper, we present RAVEN: Retrieval-Augmented Vulnerability & Event aNalysis, an agentic framework designed to support SOC analysts by automating the initial stages of alert investigation. The propose...
  </details>

- **2026-11-19** — Mattia Ferrari, Lorenzo Bruzzone — [Fusing Multimodal CNN Features with Structurally-Masked Transformers for Hierarchical Sub-Pixel Tree Species Mapping](http://arxiv.org/abs/2611.25824v1)
  <details><summary>📄 Abstract</summary>
  Precise forest species mapping using spaceborne hyperspectral data is challenging due to high spectral similarity and the inherent sub-pixel heterogeneity of natural forest stands. While traditional deep learning models exploit spatial context through convolutional architectures, these approaches can introduce noise in fragmented or mixed-species forests. In this paper, we propose a hierarchy-aware, multimodal deep learning framework to resolve sub-pixel forest composition by integrating PRISMA ...
  </details>

- **2026-11-19** — Pironti Francesco Aurelio, Arena Luigi, Blefari Francesco et al. — [ALIoTh: Orchestrating Multi-Agent LLMs for Autonomous IoT Penetration Testing](http://arxiv.org/abs/2611.25809v1)
  <details><summary>📄 Abstract</summary>
  Penetration testing in Internet of Things (IoT) environments, especially those composed of various different devices, e.g., smart plugs, smart cameras, and smart doors, presents great challenges across the phases of information gathering, attack surface enumeration, privilege escalation, and lateral movement. This paper introduces ALIoTh, a multi-agent, workflow-driven penetration testing framework that integrates Large Language Models agents within a Self-Retrieval-Augmented Generation (Self-RA...
  </details>

- **2026-11-19** — Yule Ding, Hongzhen Wu — [On the Reliability of CyberGym Evaluation: Task Material Consistency and Reference-Target Identity](http://arxiv.org/abs/2611.25790v1)
  <details><summary>📄 Abstract</summary>
  CyberGym evaluates vulnerability reproduction by checking whether a proof-of-concept input (PoC) crashes a vulnerable program version but not a fixed version. Interpreting this differential pass as successful reproduction requires consistent task materials and evidence that the PoC triggers the intended defect. We examine these requirements through a material audit of all 1,507 CyberGym tasks and an identity assessment of the final PoCs from one complete Level-1 GLM-5.3 run. Taking the defect as...
  </details>

- **2026-11-19** — Zhenhao Tian, Jintong Yu, Jingwei Feng et al. — [Hardening JavaScript Programs against LLM-Based Vulnerability Detection](http://arxiv.org/abs/2611.25718v1)
  <details><summary>📄 Abstract</summary>
  JavaScript programs are often distributed as source code, so attackers can analyze them for vulnerabilities. LLM-based vulnerability detection agents now make this analysis much easier. To mitigate this emerging threat, we present AntiAgent, a defense that lets developers harden their programs against such detection agents. AntiAgent transforms a program before release to impede an agent's analysis. To find effective transformations, AntiAgent evolves a corpus of programs with known vulnerabilit...
  </details>

- **2026-11-19** — Yuseon Choi, Sanghyeon Park, Eunjong Lee et al. — [FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash](http://arxiv.org/abs/2611.25580v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents are emerging as a promising paradigm for complex robotic tasks, leveraging Vision-Language-Action (VLA) and World Action Models (WAMs) to generate actions through Diffusion Transformer (DiT)-based iterative denoising. However, existing models often struggle to generalize to out-of-distribution (OOD) environments. We observe that retrieving successful experiences and using them to warm-start denoising enables agents to better adapt to unfamiliar situations while reducing computati...
  </details>

- **2026-11-19** — Zihao Dan, Jinyu Zhang, Jinzhao Lian et al. — [ToolPulse: Side-Channel Eavesdropping on Tool-Using LLM Agents](http://arxiv.org/abs/2611.25470v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as agents that translate user requests into sequences of local tool invocations. While prior cache-based side-channel attacks target the locally deployed models, they typically require the adversary to share model-related components or hardware resources with the victim's inference process. These assumptions do not apply to the predominant agentic settings, in which commercial LLMs execute on vendor-controlled infrastructure. We show that ag...
  </details>

- **2026-11-19** — Fahira Afzal Maken, Sagun Man Singh Shrestha, Edward Vanderfeen et al. — [Stereo Visual Odometry with In-the-Loop Geometric Feed-Forward Models Towards Dense Metric Mapping](http://arxiv.org/abs/2611.25445v1)
  <details><summary>📄 Abstract</summary>
  We present a stereo visual odometry (SVO) framework that integrates geometric feed-forward models (GFMs) for dense depth prediction with factor-graph-based visual odometry to achieve accurate localisation and dense metric mapping. Our key idea is to exploit sparse but reliable metric geometry estimated from stereo and temporal multi-view observations to calibrate dense GFM predictions, while retaining the robustness and efficiency of model-based SVO. Rather than directly conditioning the GFM on ...
  </details>

- **2026-11-19** — Xinyi Wang, Yeting Li, Shizhe Cui et al. — [ChainAgent: Automated Chainable Vulnerability Discovery in PHP Web Applications](http://arxiv.org/abs/2611.25412v1)
  <details><summary>📄 Abstract</summary>
  High-impact attacks on PHP web applications often chain limited-capability vulnerabilities with other flaws or intended behaviors. Discovering these chains requires identifying flaws and the dependencies enabling capability composition. Existing vulnerability discovery techniques analyze flaws in isolation, while attack planning assumes known components. This separation makes it difficult to discover previously unknown components whose security relevance becomes apparent only through their poten...
  </details>

- **2026-11-19** — Yifei Yang, Xuejiao Luo, Penghui Li — [Behavioral Containment: Source-to-Binary Function Matching for 1-Day Vulnerability Detection](http://arxiv.org/abs/2611.25394v1)
  <details><summary>📄 Abstract</summary>
  Vulnerabilities in reused open-source code often propagate into deployed binaries. Detecting them requires source-to-binary function matching, which locates the affected source function in a binary. Applying prior binary-to-binary approaches to this task would require compiling the source code with the same build configuration as the target binary, which is usually unavailable. Decompiling the binary does not make prior source-to-source approaches work either, because decompiled code differs sub...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 59 papers

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

- **2026-11-22** — Vaishnavi Chaughule, Yuchen Zhang, Mohammed Ahnaf Tajwar et al. — [Who Makes the Decision? Auditing an Agentic LLM Pipeline for Illicit Cryptocurrency Transaction Monitoring](http://arxiv.org/abs/2611.29829v1)
  <details><summary>📄 Abstract</summary>
  Agentic pipelines that combine graph detectors, deterministic rules, retrieval-augmented generation and an LLM judge are being proposed to monitor illicit cryptocurrency flows and to write regulation-citing justifications for analysts. They are evaluated on end-to-end accuracy or on the quality of those justifications, and neither shows which component made a decision. We audit such a pipeline on the Elliptic++ Bitcoin dataset with decision-source attribution, a trace-level protocol with three l...
  </details>

- **2026-11-22** — Tadesse Destaw Bela, Iqra Ameer, Helena Gómez Adorno et al. — [Explainable Emotion and Mental Health Reasoning in Large Language Models Using Theories of Emotion](http://arxiv.org/abs/2611.29628v1)
  <details><summary>📄 Abstract</summary>
  Advancements in Large Language Models (LLMs) have enabled a wide range of applications. However, their ability to simulate human-like behavior and reasoning remains unclear. While emotion detection is a better-established Natural Language Processing (NLP) task, existing approaches primarily focus on directly classifying text into predefined emotion classes, often overlooking the appraisal process that explains why an individual experiences a particular emotion in a given situation. In this work,...
  </details>

- **2026-11-22** — Peng Chen, Chao Huang, Yangyang Liu et al. — [Inspect Before You Decide: Evidence-Guided Visual Search for Industrial Anomaly Detection](http://arxiv.org/abs/2611.29551v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multimodal large language models (MLLMs) have demonstrated remarkable potential for industrial anomaly detection and understanding. However, reliably identifying subtle anomalies remains challenging, as existing approaches often struggle to acquire and verify fine-grained visual evidence beyond global observations. To address this challenge, we propose EVAD, an evidence-guided visual search framework that enables MLLMs to actively seek and examine diagnostically informative vi...
  </details>

- **2026-11-22** — Peng Chen, Chao Huang, Wenqiang Wang et al. — [SCRA-CLIP: Spherical-Contextual Representation Adaptation for Zero-Shot Anomaly Detection](http://arxiv.org/abs/2611.29545v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in vision-language models have facilitated zero-shot anomaly detection (ZSAD) through transferable visual-semantic representations. However, detecting fine-grained anomalies remains challenging due to inadequate modeling of diverse anomaly patterns and their spatial context. To address these challenges, we propose SCRA-CLIP, a Spherical-Contextual Representation Adaptation framework that jointly enhances anomaly-aware textual semantics and context-sensitive visual representations...
  </details>

- **2026-11-22** — Xianglong Bao, Zhe Wang, Kewen Wang et al. — [Denoised but Not Improved: What EEG Denoising Does to a Downstream Task](http://arxiv.org/abs/2611.29256v1)
  <details><summary>📄 Abstract</summary>
  Scalp electroencephalography (EEG) is routinely denoised before it reaches a downstream model, and the denoising literature scores a method by how closely its output matches a clean reference waveform. That reference does not exist for real scalp recordings: it is synthesized by adding artifact templates to signals merely presumed clean, and even an exact separation would return cortical activity blurred by volume conduction rather than the activity itself. Fidelity to it is therefore an unvalid...
  </details>

- **2026-11-22** — Tianyu Ding, Jiachen Jiang, Jinxin Zhou et al. — [Why Adaptive Optimizers Struggle with Large Convolution Kernels](http://arxiv.org/abs/2611.29232v1)
  <details><summary>📄 Abstract</summary>
  Large convolution kernels enlarge the receptive fields of ConvNets at a modest computational cost, but they are notoriously difficult to train. Existing large-kernel networks therefore rely on costly training techniques, such as parallel small-kernel branches with batch normalization. In this paper, we trace this difficulty to adaptive optimizers such as Adam, which normalize the update of every weight separately. Since input features rarely average to zero, all weights of a kernel share a commo...
  </details>

- **2026-11-22** — Mark Heimann, Bruno Jacob — [Group-Balanced Supervised Fine-Tuning for Knowledge-Intensive Domains](http://arxiv.org/abs/2611.29127v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) weights every supervised token equally, so on knowledge-dense corpora the loss budget follows token count rather than importance: on a legal QA benchmark, citation strings absorb 81% of the supervised loss weight budget while the answers being taught absorb 5%. We present Group-Balanced SFT (GB-SFT), which equalizes the loss budget across the semantic roles of tokens within a target sequence. With one tunable dial and one structural switch, GB-SFT contains standard S...
  </details>

- **2026-11-21** — Pedro Pinacho-Davidson — [Operational Assurance for LLM-Based Systems under Governance Opacity](http://arxiv.org/abs/2611.28834v1)
  <details><summary>📄 Abstract</summary>
  In the contemporary artificial intelligence ecosystem, foundation models are increasingly deployed under AI-as-a-Service (AIaaS) schemes characterized by high technical opacity, technological concentration, and limited external auditing capability over governance, training, and internal operational processes. Under these conditions, traditional ethical oversight approaches that focus exclusively on corporate governance or on internal model inspection become insufficient to ensure effective contr...
  </details>

- **2026-11-21** — Bangyan Ju, Xiaolin Sun, Yibin Hu et al. — [Persuasion from Within: Model-Based Insider Attacks in Multi-Agent LLM Debate and Consensus](http://arxiv.org/abs/2611.28660v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in multi-agent systems for collective decision-making, such as multi-agent debate and consensus games, in which agents exchange messages and update their answers over multiple rounds and a resolution mechanism aggregates them into a final outcome. Most multi-agent LLM frameworks assume that every participant shares the system objective. In practice, however, a malicious agent can join as a legitimate member of the group and persuade the othe...
  </details>

- **2026-11-21** — Gianluca Fabiani, Ralf Hannemann-Tamás, Alexander Mitsos et al. — [On rescuing diverging algorithms: crossing infinity in continuous Newton methods via a self-similarity detection framework](http://arxiv.org/abs/2611.29088v1)
  <details><summary>📄 Abstract</summary>
  We address the solution of systems of nonlinear algebraic equations via continuous Newton methods; these methods reformulate the discrete Newton update as an initial value problem for a system of ordinary differential equations (ODEs) whose stationary points correspond to the desired roots. A fundamental challenge arises when the Jacobian of these ODEs becomes singular along the solution trajectory, inducing blow-up in the vector field --or in the state itself-- and causing the numerical integra...
  </details>

- **2026-11-21** — Benjamin Tannenbaum — [ChatGPT Can't Sell (And That's Probably a Good Thing): Buyer-Aligned AI Advice, the Sales-Representative Gap, and Evidence from Commercial Conversations](http://arxiv.org/abs/2611.28946v1)
  <details><summary>📄 Abstract</summary>
  AI assistants and merchant sales agents have different objectives: assistants should help buyers compare options and preserve the choice not to purchase, while sales agents also guide qualified buyers toward an authorized next step. We study this sales-representative gap with three evidence streams. In 12,178 historical English GPT-family conversations screened for commercial or transactional intent, a 279-request sample contained recommendation language in 63 first replies (22.6%) and no narrow...
  </details>

- **2026-11-21** — Junyi Yang, Zheng Si, Yilin Zhai et al. — [HighwayVerse: A Chain-of-Inspection Benchmark for Highway Infrastructure Anomaly Understanding](http://arxiv.org/abs/2611.28800v1)
  <details><summary>📄 Abstract</summary>
  Practical highway infrastructure inspection entails progressive diagnostic reasoning from visual perception to maintenance decisions, yet existing benchmarks remain confined to isolated tasks, leaving Multimodal Large Language Models (MLLMs) insufficiently evaluated across sequential inspection stages. Meanwhile, current datasets focus primarily on highway pavement defects, falling short of real-world inspection across diverse infrastructure components such as highway pavements, guardrails, glar...
  </details>

- **2026-11-21** — Zhuangzi Li, Shilv Cai, Jian Jin et al. — [Where Does a Weight-Editing Agent Help? Blind Diagnosis and Repair of Deployment Faults in Vision Models](http://arxiv.org/abs/2611.28781v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents can read and edit the weights of neural networks without gradients, and this is increasingly presented as a new way of repairing models. We ask what such an agent adds, in a setting with a known answer. A vision model moved into a new system may be broken by a preprocessing, weight-conversion or output-convention fault; an agent restricted to forward passes must decide whether a fault exists, name it, and undo it by editing the weights. Over 183 runs on classification, segm...
  </details>

- **2026-11-21** — Yonghuang Wu, Zhenyang Liang, Pengfei Wang et al. — [JevNavAgent: A Single-Forward Visual Navigation Agent with Trajectory-Level RL for Gigapixel Pathology](http://arxiv.org/abs/2611.28766v1)
  <details><summary>📄 Abstract</summary>
  Gigapixel whole-slide images (WSIs) exceed single-pass vision-language model (VLM) capacity at cellular resolution, while multiple instance learning relies on query-agnostic offline patching without interactive reasoning. Multi-step VLM navigation agents inspect regions on demand, yet face two bottlenecks: (1) autoregressive action decoding incurs heavy latency, throttling exploration and online multi-trajectory RL; and (2) offline distillation suffers from an existential-versus-universal stoppi...
  </details>

- **2026-11-21** — Jie Shi — [Strictness of the containment of Kirk's asymptotic contractions in a class defined by two quasi-metrics](http://arxiv.org/abs/2611.28631v1)
  <details><summary>📄 Abstract</summary>
  Kirk's asymptotic contractions are defined by moduli $ψ_n$ which converge uniformly on $[0,\infty)$ to a Boyd--Wong function and are evaluated at the distance $d(x,y)$ only. A relaxed class, in which the estimate involves a lower and an upper quasi-metric built from the four distances $d(x,y)$, $d(x,Ty)$, $d(Tx,y)$ and $d(Tx,Ty)$, was recently shown to contain Kirk's class and to admit the same fixed point conclusion. It was left open whether the containment is strict. We prove that it is. The s...
  </details>

- **2026-11-21** — Emil Mittag, Richard Dazeley, Peter Vamplew — [Action-Conditioned Transition Irreversibility for Out-of-Distribution Detection in Reinforcement Learning](http://arxiv.org/abs/2611.28611v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement-learning agents shape the observations they encounter; consequently, detecting out-of-distribution (OOD) states requires analysing action-conditioned trajectories rather than treating inputs as independent samples. We propose Action-Conditioned Transition Irreversibility (ACTI), a detector that evaluates forward and backward transition likelihoods, calibrates this comparison against the in-distribution profile at each timestep, and smooths the score over a short window, using no fu...
  </details>

- **2026-11-21** — Maxence Gollier, Youssef Diouane, Dominique Orban — [An Exact Penalty Method for Large-Scale Equality-Constrained Nonlinear Optimization](http://arxiv.org/abs/2611.29042v1)
  <details><summary>📄 Abstract</summary>
  We present an exact penalty method for equality-constrained nonlinear optimization. Our approach transforms the smooth, constrained problem into a sequence of nonsmooth, unconstrained problems by penalizing the constraint violation by its Euclidean norm. An outer loop updates the penalty parameter and the subproblem tolerances, while an inner loop solves each penalized subproblem with a quadratic regularization method. The method also includes a local infeasibility detection mechanism, an extrap...
  </details>

- **2026-11-20** — Guillem Fustier-Castillo, Ruben Ribes-Serrano, Javier Naranjo-Alcazar et al. — [Real-time neuromorphic audio and vision perception for autonomous robotic applications: Integration and experimental evaluation on a rover platform](http://arxiv.org/abs/2611.27953v1)
  <details><summary>📄 Abstract</summary>
  Neuromorphic sensing and computing offer a promising alternative to conventional deep learning pipelines for mobile robots, where perception must run continuously under tight latency and energy constraints. However, most neuromorphic solutions are still evaluated offline or on isolated benchmarks, and their integration into complete robotic systems remains largely unexplored. In this technical report, a four-wheel rover platform is presented that combines three real-time perception pipelines: a ...
  </details>

- **2026-11-20** — Junjie Chu, Ye Leng, Mingjie Li et al. — [AnimalFarm: Auditing the Generation and Detection of Hateful Images Featuring Anthropomorphic Characters](http://arxiv.org/abs/2611.27905v1)
  <details><summary>📄 Abstract</summary>
  Anthropomorphic non-human characters have long been used to convey hateful messages targeting human groups, from Nazi-era propaganda to recent AI-generated imagery on social media. However, the safety risks posed by such imagery remain largely unexplored. We thus conduct the first systematic study of hateful image generation and detection involving anthropomorphic non-human characters. We construct a benchmark from conservatively screened source scenes, covering five character types and three im...
  </details>

- **2026-11-19** — Meghana Aparna Sistla, Alaia Solko-Breslin, Somesh Jha et al. — [Tether: Verified Stateful Policy Engine for System-Level Monitoring of Agents](http://arxiv.org/abs/2611.25599v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents are increasingly deployed for long-running tasks that execute arbitrary shell commands or programs. However, these actions can result in unauthorized network requests or persistent, malicious changes to the user's file system, processes, or privileges. Existing defense mechanisms rely on either LLM-based monitors, which lack provable safety guarantees, or stateless policy enforcement layers, which miss multi-step data flows and execution side-effects unmodeled by the policy ...
  </details>

- **2026-11-19** — Licheng Pan, Yuzhou Chen, Zhixuan Chu et al. — [DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents](http://arxiv.org/abs/2611.25583v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents rely on persistent memory to plan tool calls and complete multi-step tasks, which exposes them to memory drift: an adversarial or misleading memory alters the execution path and final outcome. In this work, we investigate online memory-drift detection, which estimates each retrieved memory's causal contribution to potential drift at serving time. We identify two fundamental challenges. (1) Content-level features are insufficient for causal memory-drift attributi...
  </details>

- **2026-11-19** — Ziqing Yang, Yixin Wu, Michael Backes et al. — [Text-Aware, Vision-Blind: How Multimodal Image Editing Systems Handle Unsafe Inputs](http://arxiv.org/abs/2611.26569v1)
  <details><summary>📄 Abstract</summary>
  Multimodal image generation systems have made rapid progress and increasingly emphasize content safety. However, their safety mechanisms tend to rely on a single modality and lack joint consideration of both visual content and text prompts, particularly in instruction-guided image editing, where the uploaded image may itself carry risk. We thus introduce EditSafetyBench, a benchmark that measures system-level safety awareness of advanced image editing systems, containing 5,940 image-instruction ...
  </details>

- **2026-11-19** — Atrey Desai, Deniz Böloni-Turgut, Ty Brassington et al. — [Frontier models need only one text to unmask its human or AI author](http://arxiv.org/abs/2611.26216v1)
  <details><summary>📄 Abstract</summary>
  Given a single text and a simple zero-shot prompt (no web access, tools, candidate lists, or writing samples), frontier models can answer "who wrote this?" at three increasingly specific levels: (1) whether an AI or human wrote it, (2) if an AI, which lab, and (3) if a human, often exactly who. The latest models (Claude Fable 5.2, GPT-6.1 Sol, Gemini 4 Carbon) match trained detectors like Pangram while also explaining their predictions in natural language, and Opus 5.5 names the correct lab for ...
  </details>

- **2026-11-19** — Hai Wang, Bretislav Hajek, Chonghe Jiang et al. — [The FrontierOR Challenge: Agentic Algorithm Design for Operations Research](http://arxiv.org/abs/2611.26171v1)
  <details><summary>📄 Abstract</summary>
  Operations research (OR) relies on algorithms that experts tailor to each problem: a new routing, scheduling or network design problem can take weeks of specialist work before it is solved well at scale. Large language model (LLM) agents now write, test and improve code, but whether they can design algorithms that scale to realistic instances is open: in the FrontierOR benchmark's one-shot evaluation, the strongest model matches Gurobi, with an objective within 1% of Gurobi's and no slower, on o...
  </details>

- **2026-11-19** — Qingxu Fu, Xuanfa Jin, Ziqian Chen et al. — [System-One RSI: Building Muscle Memory for Interactive Agents through Guided Practice](http://arxiv.org/abs/2611.26007v1)
  <details><summary>📄 Abstract</summary>
  Reasoning models provide strong multimodal task understanding but struggle with sub-second control because deliberation increases decision latency. Fast decision models can meet the response window, yet prompting and few-shot examples do not readily provide the fine-grained experience required by a new task. Inspired by coached motor learning, this paper presents System-One Recursive Self-Improvement (System-One RSI), which couples two loops. The high-frequency online inner loop is an Observe, O...
  </details>

- **2026-11-19** — Rabimba Karanjai, Linsey Pang, Hemanth Hegadehalli Madhavarao et al. — [One Schedule Does Not Fit All: Adaptive Inference Schedules for Diffusion Language Models](http://arxiv.org/abs/2611.25895v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models typically use a fixed denoising schedule across workloads. We show that the cheapest schedule that preserves quality depends on the task, model, and sampler. We propose Task-Calibrated Denoising Allocation (TCDA), a deployment rule with an explicit error guarantee. Given candidate samplers, paired calibration data, a utility tolerance, and guardrails against degeneration, TCDA uses simultaneous one-sided bootstrap bounds to certify which candidates meet both the utility...
  </details>

- **2026-11-19** — Jinkun Cao — [Fast and Accurate Body Estimation in Pixels, World Space and Scenes](http://arxiv.org/abs/2611.25801v1)
  <details><summary>📄 Abstract</summary>
  We present FAB (Fast and Accurate Body estimation), a human body estimator that jointly improves inference efficiency and body-recovery fidelity. Rather than predicting only parametric mesh-model parameters, FAB directly predicts human skeleton joints and dense surface points. In images, it predicts dense 2D and 3D body points alongside a parametric Momentum Human Rig (MHR) head, then fits SMPL in one learned pass followed by two Gauss-Newton steps. Its ViT-L student, FAB-L, distilled from a fin...
  </details>

- **2026-11-19** — Faxian Wan, Xiaocui Yang, Yifan Cao et al. — [SEAF: Selective Semantic Enrichment and Visual Evidence Fusion for Multimodal Sarcasm Detection](http://arxiv.org/abs/2611.25672v1)
  <details><summary>📄 Abstract</summary>
  Multimodal sarcasm detection requires textual, visual, and contextual evidence, particularly when multiple images provide complementary cues. Multimodal large language models (MLLMs) can generate auxiliary information from a post's text and images, but their outputs may mix useful background knowledge with redundant visual descriptions. We propose SEAF, a dual-branch framework for selective semantic enrichment and visual evidence fusion. SEAF assigns generated fields to distinct roles: entity ba...
  </details>

- **2026-11-19** — Minsuk Jang, Hee-Seon Kim, Hui-Cheol Yu et al. — [MATE: Mobile Agent Trustworthy Execution for Safe and Efficient Mobile Control](http://arxiv.org/abs/2611.25526v1)
  <details><summary>📄 Abstract</summary>
  Mobile agents on personal smartphones can affect private data, payments, settings, and the foreground screen. We present MATE (Mobile Agent Trustworthy Execution), an execution-layer system that controls the boundary between agent action proposals and device effects without modifying the underlying model. MATE represents each UI primitive as a structured action record that combines the instruction, target app, screen context, primitive, and action fields. Runtime Guardrail (RG) maps this record ...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 64 papers

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

- **2026-11-22** — Yanhan Lin, Yuliang Wu, Yihao Guo et al. — [FunGrasp-Zero: Field-Conditioned Graph Attention Policy for Zero-Shot Cross-Embodiment Dexterous Functional Grasping](http://arxiv.org/abs/2611.29195v1)
  <details><summary>📄 Abstract</summary>
  Dexterous functional grasping is critical for robotic tool use, yet current dexterous hands exhibit substantial morphological diversity. This hardware heterogeneity makes cross-embodiment functional grasping a fundamental but largely unexplored problem. Existing functional grasping methods use retargeted hand poses as guidance, tying task representation to a specific embodiment and failing to explicitly capture object-centric functional contact intent, limiting generalization across hands. To ad...
  </details>

- **2026-11-22** — Tailai Chen, Jiawei Yu, Yiming Cheng et al. — [Unleashing the Value of Raw Point Clouds for 3D Understanding with LLMs](http://arxiv.org/abs/2611.29194v1)
  <details><summary>📄 Abstract</summary>
  Standard 3D point cloud language models typically rely on pretrained point encoders to extract 3D features and project them into representations processable by large language models (LLMs). However, these encoders are often originally optimized for pre-defined tasks, resulting in a representation bottleneck that may lead to a substantial mismatch with downstream 3D understanding. Moreover, existing models largely follow a single pass closed-book generation, limiting their ability to actively ins...
  </details>

- **2026-11-22** — Yan Wang, Yiran Song, Zizhuo Gong et al. — [Can an Agent Trust Its Own Zoom? Cross-Magnification Provenance Verification for Whole-Slide Images](http://arxiv.org/abs/2611.29150v1)
  <details><summary>📄 Abstract</summary>
  Visual agents navigate whole-slide images through magnified observations associated with claimed locations. However, a visually plausible observation does not necessarily originate from its claimed location, particularly across magnifications and in regions with similar tissue structures. We formulate cross-magnification provenance verification (CMPV) to evaluate whether visual evidence supports a claimed spatial association, recover the source when possible, and abstain when evidence is insuffi...
  </details>

- **2026-11-22** — Chaojie Ji, Sergio Quiroga-Sandoval, Ruxin Wang et al. — [Supply the Global, Supervise the Local: Combining Representation Conditioning and Alignment in Diffusion Transformers](http://arxiv.org/abs/2611.29138v1)
  <details><summary>📄 Abstract</summary>
  A pretrained image representation helps train a diffusion transformer in several roles, including as an alignment target, which the model's hidden states learn to match, as in representation alignment (REPA), and as a condition, an extra input describing the image to be generated. Combined, they would give the model an input and a target, but whether they conflict is unknown. To test this, we let the condition carry only part of REPA's target: we split the representation of each image patch into...
  </details>

- **2026-11-22** — Subhradeep Kayal, Ali Dashti — [Decoding Transformer Dynamics via Koopman Subspaces](http://arxiv.org/abs/2611.29113v1)
  <details><summary>📄 Abstract</summary>
  We apply Koopman operator theory and Dynamic Mode Decomposition (DMD) to characterise how large language models (LLMs) process different input topics. Treating the layer-to-layer evolution of hidden states as a dynamical system, we fit a linear Koopman operator and take the subspace spanned by its dominant modes as a per-topic spectral fingerprint. Four findings emerge. First, the depth map is near-linear: a single linear operator predicts each next-layer state to within approx. 18% relative err...
  </details>

- **2026-11-21** — Kelsey Sikes, Sarath Sreedharan — [Do You Even Know What I Want? Improving LLMs Ability to Detect Hidden User Intent](http://arxiv.org/abs/2611.29028v1)
  <details><summary>📄 Abstract</summary>
  As with conventional AI agents, a common source of misalignment between Large Language Models (LLMs) and their human users is misspecified goals. Often, this happens when the human has skewed beliefs about the system's model and provides it with information that causes behavior different from what they expected, with potentially unwanted side effects. To ensure goal alignment, one solution would be for the LLM to ask the human questions about their objectives. However, it has been well-documente...
  </details>

- **2026-11-21** — Pujun Zheng, Chengmu Wang, Wanying Ren et al. — [Bias Cascade: Understanding the Gap Between Knowledge Alignment and Effect Replication in LLM-based Social Simulation](http://arxiv.org/abs/2611.28854v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to simulate participants in social experiments. Existing research has primarily focused on aligning social knowledge and isolated responses, while overlooking whether simulations can reproduce the collective effects of social interventions. This distinction is critical due to a failure mechanism we call a $bias$ $cascade$: similar individual states can lead to different actions, while agreement on isolated actions can still produce divergent out...
  </details>

- **2026-11-21** — Haru Furuichi, Phan Xuan Tan — [Pixel Auto-Encoder: Reconstructing Language Model Activations Through Pixel Art](http://arxiv.org/abs/2611.28822v1)
  <details><summary>📄 Abstract</summary>
  Interpreting the high-dimensional internal representations of large language models (LLMs) remains a challenging problem. Recent approaches have explored translating these representations into human-understandable forms, particularly natural language. In this work, we explore the use of images as an alternative target modality for interpreting LLM activations. As a first step toward this goal, we introduce Pixel Auto-Encoder, which converts intermediate LLM activations into $32 \times 32$, 32-co...
  </details>

- **2026-11-21** — Shraddha Surana, Ashwin Srinivasan — [Dhaani: A Data-Flow-Driven Tool for Greenfield Construction and Brownfield Modernisation](http://arxiv.org/abs/2611.28798v1)
  <details><summary>📄 Abstract</summary>
  Large language models can generate plausible code quickly, but an end-to-end prompt leaves developers with little control over decomposition, interfaces, or the assumptions that must survive later revisions. We present Dhaani, a free desktop application for greenfield program construction and brownfield repository modernisation. It makes an annotated data-flow diagram (ADFD) the inspectable contract between intent and implementation. In the greenfield workflow, Build, a user turns natural-langua...
  </details>

- **2026-11-21** — Yunxiao Tian, Li Qiao, Ziwei Wan et al. — [R2WM: Recursive Reasoning Wireless Model for Long-Horizon mmWave Beam Prediction](http://arxiv.org/abs/2611.28774v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon beam prediction aims to extend beam-training intervals while supporting beam alignment in mobile millimeter-wave systems. Although pretrained large models can improve prediction over compact recurrent baselines, their large backbones impose substantial storage and computing requirements. To address this limitation, we propose a recursive reasoning wireless model (R2WM). Given a fixed history of beam indices and angles of departure (AoDs), R2WM repeatedly updates coupled latent and p...
  </details>

- **2026-11-21** — Po-Yi Lu, Jui-Chao Lu, Paul Kuo-Ming Huang et al. — [Contrastive Gradient Guidance for Test-Time Multi-Preference Alignment of Diffusion Models](http://arxiv.org/abs/2611.28764v1)
  <details><summary>📄 Abstract</summary>
  Aligning pre-trained diffusion models with multiple context-dependent preferences requires adapting generation at test time rather than relying on offline fine-tuning, which requires hyperparameter tuning and a new training run for each preference trade-off. Existing approaches compress diverse preferences into a single scalar reward objective for fine-tuning or test-time guidance rather than directly reusing existing generative experts released for different purposes and obtained through differ...
  </details>

- **2026-11-21** — Dongkuk Kim, Jungkyu Shin, Yoonhyuk Choi et al. — [CLAIR: Consistent LLM Adaptation via Index-free Reprogramming](http://arxiv.org/abs/2611.28721v1)
  <details><summary>📄 Abstract</summary>
  Time-series forecasting with pretrained large language models (LLMs) uses contextualized patch representations, raising the question of how to align them. Matching patches at the same temporal position is natural, but self-attention allows each patch state to incorporate information from elsewhere in the input window, suggesting that useful correspondences can extend across positions. This flexibility, however, does not necessarily translate into consistent forecasts: similar patch states may pl...
  </details>

- **2026-11-21** — Ming Cheung — [Unlearning Model Identity: Ablating LoRA Weights from Question-Based Identity Tuning](http://arxiv.org/abs/2611.28650v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models are trained on diverse corpora containing outputs from proprietary teacher models and provider-curated sources. Models subsequently inherit embedded self-identity traits, persistently asserting specific proprietary names. Service providers of open-weight models frequently require the removal of model identity for downstream applications, such as custom interfaces, without exposing provider affiliations to end-users. Effective identity modification is therefore critical for ...
  </details>

- **2026-11-21** — Xiaolei Zhou, Xinjie Zhu, Chuangjie Fang et al. — [OrthoLatentCAD: Orthographic Spatial Latents for Hand-Drawn CAD Program Generation](http://arxiv.org/abs/2611.28646v1)
  <details><summary>📄 Abstract</summary>
  Freehand orthographic drawings capture early design intent, yet recovering executable sketch--extrude CAD programs from raster front, right, and top views remains challenging: noisy, dimension-free 2D layouts must be reconciled into an ordered construction history. We introduce Hand2CAD, a benchmark of 215K ABC-derived synthetic orthographic-drawing--CAD program pairs and 1,000 real three-view sets drawn by CAD-trained participants. Recovering CAD programs from orthographic drawings requires bot...
  </details>

- **2026-11-21** — Yeo Jin Jung, Yating Liu, Lalchand Pandia et al. — [SAFE-DRIFT: Data Selection for Supervised Fine-tuning with Controllable Off-Target Drifts](http://arxiv.org/abs/2611.28560v1)
  <details><summary>📄 Abstract</summary>
  We propose SAFE-DRIFT, a data-selection framework for supervised fine-tuning that improves a target capability while controlling unwanted drift in the model's other behaviors. We formalize this as a constrained optimization problem that maximizes alignment with the target gradient, subject to a budget on off-target drift which we quantify using the Fisher information of a reference distribution. Under this objective, the optimal, closed-form update is a damped natural-gradient step that downweig...
  </details>

- **2026-11-21** — Qiang Hu, Kaiyi Ji — [S$^2$LMR: Supervised Sequential Long-Context Multi-Step Retriever](http://arxiv.org/abs/2611.28995v1)
  <details><summary>📄 Abstract</summary>
  Multi-step retrieval over long contexts is a key capability for retrieval-augmented generation, but strong existing approaches are costly and complex to train. Supervised retrievers are far simpler and cheaper, yet they fall well behind in this setting. We show that this gap stems not from supervised training itself, but from three misalignments between training and inference: easy training negatives, noisy retrieval prefixes, and position-agnostic scoring. Guided by this analysis, we introduce ...
  </details>

- **2026-11-19** — Juan Gutiérrez, Victor Gutiérrez-García, José Luis Blanco-Murillo — [Invertible Transport Between Sample-Only Distributions via Projected Characteristic Functions](http://arxiv.org/abs/2611.26187v1)
  <details><summary>📄 Abstract</summary>
  Many useful latent distributions can be sampled but do not have a tractable density. Such distributions may be represented by empirical collections of real-world observations or generated by scientific simulators and black-box generative models. These sample-only priors cannot be used directly in likelihood-based normalizing flows, which require evaluating the prior density. We propose Projected Characteristic-Function matching (PCF), a density-free framework for learning an invertible map betwe...
  </details>

- **2026-11-19** — Yiyang Du, Yuxuan Kuang, Qitao Zhao et al. — [AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control](http://arxiv.org/abs/2611.26613v1)
  <details><summary>📄 Abstract</summary>
  Frontier multimodal language agents such as GPT-6 Astra have demonstrated strong capabilities in controlling robots directly via low-level numerical actions without high-level primitives. However, existing benchmarks report only episode-level success rates, which show neither how these agents succeed nor where they fail. In this paper, we present a systematic action-level analysis of frontier agents on direct robot control across 12 manipulation benchmarks. We introduce AgentRoboCritic, an inten...
  </details>

- **2026-11-19** — Jiahao Huang, Jun Wang — [Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language Models](http://arxiv.org/abs/2611.26590v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) integrate visual and textual information, but their outputs do not reveal internal concept representations. Global workspace theory (GWT) proposes that information is selected from parallel brain processes, integrated in a shared workspace, and made available to specialised processes. We introduce the Multimodal Concept Lens (MC-Lens), a multimodal Jacobian lens, to study these functions in VLM concept processing. Its vision encoder and language decoder lenses map i...
  </details>

- **2026-11-19** — Shuang Wu, Jiachen Qian, Youtian Lin et al. — [Direct3D-V3: Latent-Free Diffusion Transformers in the Native Voxel Domain](http://arxiv.org/abs/2611.26511v1)
  <details><summary>📄 Abstract</summary>
  Native 3D generation has largely been built around latent diffusion, with recent advances concentrating on stronger variational autoencoders (VAE) and increasingly elaborate latent representations, from vecset and triplanes to structured sparse voxels. Despite their architectural differences, these methods all share the same premise: geometry is first compressed into a latent space and only then modeled by the generator. We take a different route and propose Direct3D-V3, a latent-free diffusion ...
  </details>

- **2026-11-19** — Vishesh Kumar Singh, Sayak Ray Chowdhury — [Sequential Anytime Valid Tests for Efficient Inference-Time Alignment](http://arxiv.org/abs/2611.26413v1)
  <details><summary>📄 Abstract</summary>
  Inference-time alignment methods, such as Best-of-N (BoN), improve language model outputs by generating multiple candidates per prompt and selecting among them using a reward model. Much of this cost is wasted: a fixed budget is applied to every prompt, although the computation required by prompts varies widely. Adaptive methods halt once sampled answers appear settled, but their thresholds are tuned heuristics with no statistical control over early-stopping errors. We instead seek an anytime-va...
  </details>

- **2026-11-19** — Yuqi Tang, Yang Shi, Yuran Wang et al. — [EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning](http://arxiv.org/abs/2611.26380v1)
  <details><summary>📄 Abstract</summary>
  Egocentric video captioning requires fine-grained detail and accurate timing, yet current multimodal large language models (MLLMs) often miss brief actions, confuse their order, or misinterpret the wearer's motion. Existing caption formats also offer limited support for combining detailed narration with precise timing. We present EgoCaptioner, which pairs a video-level overview of the setting, participants, and the wearer's overall activity with timed steps whose narration adapts to varying perc...
  </details>

- **2026-11-19** — Ziyue Wang, Yaopeng Yang, Liyi Zhou — [Alignment Drives Reuse: Learning Generalizable Robot-Use Agents from Heterogeneous Experience](http://arxiv.org/abs/2611.26376v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) demonstrate broad generalization across tasks and domains. However, comparable generalization in robot manipulation remains challenging. Heterogeneity in robot embodiments, task formulations, geometric conventions, and action interfaces fragments interaction experience across benchmarks and hardware. We rethink robot skill learning through alignment: Can heterogeneous interactions across benchmarks and embodiments jointly improve one shared skillset for robot manipu...
  </details>

- **2026-11-19** — Josef Brozovich, Qining Zhang, Lei Ying — [Actor-Predictor Architecture for Reinforcement Learning with Formal Specification Objectives](http://arxiv.org/abs/2611.26313v1)
  <details><summary>📄 Abstract</summary>
  One fundamental challenge in reinforcement learning (RL) is enforcing temporal safety constraints, such as satisfying formal specifications. Existing methods often transform logic formulas into automata for state augmentation and reward shaping. However, this approach assumes that automaton construction is both feasible and tractable, which limits its applicability to small specifications and linear temporal logic (LTL). This paper proposes Actor-Predictor, a framework that learns a surrogate re...
  </details>

- **2026-11-19** — Jonathan Lichtenfeld, Oskar von Stryk — [I See You: Initial Multi-Robot LiDAR Registration with Mutual-Observation Checks](http://arxiv.org/abs/2611.26276v1)
  <details><summary>📄 Abstract</summary>
  Compared to single-robot deployments, multi-robot teams can significantly improve search-and-rescue (SAR) mission success by covering large areas in parallel. To collaborate effectively, these robots must be registered in a common reference frame. Standard registration methods typically rely on external infrastructure or significant map overlap, but real deployments require infrastructure-free, stationary initial alignment for immediate operation. While global LiDAR point cloud registration addr...
  </details>

- **2026-11-19** — Yipan Xu, Shuyong Gao, Jiyuan Fu et al. — [Frequency-Synchronized Boundary Coupling for Training-Free Multi-Prompt Long Video Generation](http://arxiv.org/abs/2611.26098v1)
  <details><summary>📄 Abstract</summary>
  Text-to-video generation has made remarkable progress with diffusion models and transformer-based video architectures, yet generating coherent long videos from evolving textual descriptions remains challenging. Training long-video models from scratch requires substantial computation and large-scale multi-event data, while training-free multi-prompt generation must activate new prompt semantics without breaking temporal continuity. We identify a frequency-agnostic boundary coupling problem in exi...
  </details>

- **2026-11-19** — Nils Brede Moe, Marthe Berntzen, Astri Barbala et al. — [Barriers to GenAI Integration During Large-Scale Agile Transformation: An Exploratory Case Study](http://arxiv.org/abs/2611.25967v1)
  <details><summary>📄 Abstract</summary>
  Organizations undergoing large-scale agile transformations are increasingly introducing generative AI (GenAI) tools into everyday work. While GenAI promises to accelerate software development, less is known about how organizations integrate GenAI into existing large-scale agile ways of working and how it interacts with tensions related to autonomy, alignment, learning, and coordination. We examine barriers to GenAI integration through an exploratory case study of a large Nordic media organizatio...
  </details>

- **2026-11-19** — Qiyan Deng, Long-Kai Huang, Kangfei Zhao — [From Cases to Criteria: Reusing Evaluation Knowledge for Task-Specific Rubric Generation](http://arxiv.org/abs/2611.25903v1)
  <details><summary>📄 Abstract</summary>
  Query-specific rubrics make LLM evaluation more fine-grained and transparent, and generating high-quality rubrics requires both identifying the target query's evaluation scope and specifying concrete checks. Historical rubrics provide reusable evaluation experiences, yet existing approaches reuse either complete query-rubric cases or aggregated criteria and dimensions without explicitly connecting recurring evaluation requirements to their criterion-level evidence and source-query context. This ...
  </details>

- **2026-11-19** — Runze Wang, Fei Zha, Bing He et al. — [ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds](http://arxiv.org/abs/2611.25838v1)
  <details><summary>📄 Abstract</summary>
  Interactive game world models separate executable world evolution from visual generation, using video models to render engine-provided scene representations into detailed observations. During sustained gameplay, however, existing generative renderers struggle to follow changing conditions while preserving visual continuity across diverse proxies and target styles. We therefore introduce ContextRenderer, an autoregressive video diffusion framework designed for both dynamic conditioning and cross-...
  </details>

- **2026-11-19** — Nina Goncharova, Alexandra Ivanova, Aibek Alanov — [Inject Where It Matters: Objective-Dependent Feature Control in Rectified-Flow Image Editing](http://arxiv.org/abs/2611.25811v1)
  <details><summary>📄 Abstract</summary>
  Many prompt-driven FLUX editing methods rely on injecting source features into target-conditioned generation, creating an inherent trade-off between source preservation and the desired edit. We address this problem by controlling where source features are injected and which transformer blocks are used. First, we introduce adaptive masks that spatially gate feature injection using differences between source- and target-conditioned block outputs at matched inversion states. Second, we use REINFORC...
  </details>

- **2026-11-19** — Wen-Li Wei, Kenneth Yang, Jen-Chun Lin — [Sonic Palette: Predicting Dynamic Color Themes from Music](http://arxiv.org/abs/2611.25781v1)
  <details><summary>📄 Abstract</summary>
  We present Sonic Palette, a music-driven framework for predicting time-varying color themes from audio. Rather than treating music-to-palette generation as a static problem, our method formulates music--color correspondence as a cross-modal sequence prediction task that models how palette-level visual attributes evolve over time in response to music. Specifically, Sonic Palette uses a music-conditioned autoregressive Transformer to predict frame-wise color themes, each represented by five domina...
  </details>

- **2026-11-19** — Shuyue Shi, Rong Yuan, Lin Tian — [AdaptReg: Skip-level FiLM Adapter for Task-Specific Adaptation of a Frozen Registration Foundation Model](http://arxiv.org/abs/2611.25761v1)
  <details><summary>📄 Abstract</summary>
  Longitudinal PSMA-PET/CT registration is a key step in assessing treatment response in prostate cancer, and it requires more than generic alignment accuracy: the deformation must preserve lesion volume, so that measured changes in metabolic tumor volume (MTV) and total lesion glycolysis (TLG) reflect treatment response rather than registration artifacts. We propose AdaptReg, which adapts a frozen registration foundation model to such task-specific requirements through a lightweight trainable ada...
  </details>

- **2026-11-19** — Shengchun Wang, Yuhang Lin, Tong Li et al. — [From Data Alignment to Parameter Generation: Few-Shot Cross-City Traffic Prediction with Conditional Diffusion](http://arxiv.org/abs/2611.25592v1)
  <details><summary>📄 Abstract</summary>
  Accurate mobile traffic forecasting is crucial for network service management, supporting proactive capacity provisioning, congestion mitigation, and energy-efficient operation. However, many cities and regions are data-scarce (e.g., newly deployed or poorly instrumented areas), thus making traffic prediction a few-shot learning problem and limiting the practicality of standard data-driven models. Existing cross-city solutions primarily rely on data-space alignment to match traffic distributions...
  </details>

- **2026-11-19** — Chanwoo Kim, Doyun Kim, Minsoo Song et al. — [Rubric Semantics or Numerical Priors? Auditing Scale-Direction Bias in LLM Judges](http://arxiv.org/abs/2611.25588v1)
  <details><summary>📄 Abstract</summary>
  Recent benchmark evaluations increasingly rely on Large Language Models (LLMs) as automatic judges. This paradigm assumes LLMs evaluate based on the rubric's semantic meaning rather than its numeric scale. We question this assumption by introducing semantic faithfulness: the principle that semantically equivalent rubrics must yield consistent scores. To quantify this, we propose a scale-reversal probe that inverts score anchors without altering evaluation criteria. Furthermore, we introduce floo...
  </details>

- **2026-11-19** — Wenshuo Chen, Honglei Jin, Le Yang et al. — [Trajectory-Calibrated Merging of Embodied Policies](http://arxiv.org/abs/2611.25575v1)
  <details><summary>📄 Abstract</summary>
  Robot foundation models are increasingly adapted into task specialists to expand their embodied capabilities. Yet these capabilities remain fragmented across separate policies, and existing model-merging methods do not reliably preserve them during closed-loop execution: parameter-space alignment provides only an indirect proxy for behavior, while regression may fail to preserve behavior at states not covered by its calibration inputs. We present Trajectory-Calibrated Regression (TCR), an execut...
  </details>

- **2026-11-19** — Jinhan Li, Zhisheng Chen, Yuxuan Li et al. — [Reinforcement-Aligned Probabilistic Weather Forecasting with Discrete Tokens](http://arxiv.org/abs/2611.25570v1)
  <details><summary>📄 Abstract</summary>
  Global medium-range weather forecasting must not only generate ensembles efficiently to characterize uncertainty in future states, but also serve downstream applications such as extreme-event warnings and cross-sphere coupled simulations. We introduce WeatherCraft, a framework that unifies probabilistic generation and reinforcement learning alignment through discrete weather tokens, bringing the GPT-style pretraining--post-training paradigm to global medium-range weather forecasting. A multiscal...
  </details>

- **2026-11-19** — Jin Yang, Tian Liu, Jose Penagaricano et al. — [Uncertainty-Aware Multimodal Deep Learning for Prediction of Radiation-Induced Xerostomia in Head and Neck Cancer](http://arxiv.org/abs/2611.25481v1)
  <details><summary>📄 Abstract</summary>
  To develop and evaluate an uncertainty-aware multimodal learning framework for predicting radiation-induced xerostomia in patients receiving head-and-neck cancer radiotherapy. We developed a Bidirectional Attention-enhanced Diffusion Transformer (BA-DiT) that combines self-supervised multimodal representation learning with supervised Bayesian fine-tuning. The model integrates pretreatment CT images and three-dimensional dose distributions, focusing on bilateral parotid glands while incorporating...
  </details>

- **2026-11-19** — Alireza Moayedikia — [Interference Bounds and Merge-Aware Training Dynamics for Composable Fine-Tuned Models](http://arxiv.org/abs/2611.25430v1)
  <details><summary>📄 Abstract</summary>
  Combining fine-tuned models by composing their parameter updates has become a standard alternative to multi-task training. We formalize composability as a property of a collection of task vectors and prove that the excess loss of the merged model is controlled by an interference functional of the cross-task curvature overlap and the signed alignment of the updates. In the quadratic regime this functional equals the excess loss, giving a criterion that is necessary as well as sufficient and that ...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 58 papers

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

- **2026-11-22** — Xin Zhang, Yushuo Hou, Anqi Zhao et al. — [More Than Picturing the Future: Motion-Oriented Latent Reasoning for Generalizable Robot Manipulation](http://arxiv.org/abs/2611.29339v1)
  <details><summary>📄 Abstract</summary>
  Latent reasoning lets Vision-Language-Action (VLA) models deliberate at a fraction of the cost of explicit chain-of-thought, increasingly through visual foresight, which we show to be indispensable for predicting actions. Yet this paradigm is inherited from Vision-Language Models, where it serves understanding rather than action: each latent is aligned with an isolated future frame, often enriched with further modalities of that frame. We find that this binds the policy to the appearance of its ...
  </details>

- **2026-11-22** — Abubakar Sadiq Shittu, Venkat Gopu, Arshita Sharma et al. — [LLM-Based Assistant for Dog Care Guidance](http://arxiv.org/abs/2611.29286v1)
  <details><summary>📄 Abstract</summary>
  This study investigates whether domain grounding through Retrieval-Augmented Generation (RAG) and parameter-efficient fine-tuning using Low-Rank Adaptation (LoRA) can enhance the accuracy and reliability of pet care advice generated by large language models (LLMs). We curated a dataset of breed-specific dog care information and used it to develop two systems: a RAG pipeline based on TinyLlama-1.1B-Chat-v1.0, and a fine-tuned LLaMA-3.2-1B model adapted using LoRA. Both systems were evaluated on 1...
  </details>

- **2026-11-22** — Gwangtak Bae, Seunggu Kang, Junho Kim et al. — [Continuous-time 4D Reconstruction via Event-guided Latent Feature Interpolation](http://arxiv.org/abs/2611.29838v1)
  <details><summary>📄 Abstract</summary>
  Recent geometric foundation models can successfully convert a video sequence into frames of registered point clouds, but cannot predict moments beyond the observed temporal resolution. We propose a continuous-time 4D reconstruction method that extracts 3D structure and camera poses at any time instant, with additional guidance from event-camera measurements. While event cameras provide evidence at microsecond resolution to continuously fill the temporal gap, integrating them into existing RGB-ba...
  </details>

- **2026-11-22** — Geonwoo Bang, Dongho Kim, Moohong Min — [Latent-Predisposition Personas for Heterogeneous and Reliable LLM Survey Simulation](http://arxiv.org/abs/2611.29805v1)
  <details><summary>📄 Abstract</summary>
  LLM personas are used to simulate survey publics, which should reproduce not only answer distributions but also within-person coherence and stability. Drawing on mass belief systems research, we show that persona-conditioned LLMs produce over-constrained publics. Across three model families and three U.S. surveys, opinions on unrelated issues are 1.6-4.6 times as correlated as among humans, and party identification explains 2.5-7.6 times as much answer variance. Common remedies (temperature, div...
  </details>

- **2026-11-22** — Anurag Kadkol, Lawson L. S. Wong — [Reinforcement Learning from LLM-Generated (Suboptimal) Demonstrations](http://arxiv.org/abs/2611.29732v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has achieved substantial progress across many domains, but training an agent \textit{tabula rasa} remains highly sample-inefficient. A common remedy is to initialize the agent using a neural network pretrained on demonstrations. However, collecting demonstrations is expensive, and the demonstrations themselves can be suboptimal. In this work, we use a large language model (LLM) to generate an advice policy that produces demonstration data with effectively no human cos...
  </details>

- **2026-11-22** — Pengzhen Chen, Yanwei Liu, Xiaoyan Gu et al. — [RSWP: Robust SO(3)-Equivariant Watermarking for Panoramic Images](http://arxiv.org/abs/2611.29468v1)
  <details><summary>📄 Abstract</summary>
  Robust watermarking for panoramic imagery is impeded by the topological mismatch between spherical signals and planar representations. Conventional methods fail under $SO(3)$ viewing rotations due to non-linear geometric warping and struggle with viewport extraction, which typically necessitates computationally expensive inverse remapping. To address these challenges, we propose RSWP, a watermarking framework grounded in icosahedral group theory. Leveraging the property that the icosahedral grou...
  </details>

- **2026-11-22** — Teng-Fei Xiao, Liang Li, Renli Xu et al. — [Multi-port few-photon diodes](http://arxiv.org/abs/2611.29451v1)
  <details><summary>📄 Abstract</summary>
  We investigate single- and two-photon scattering dynamics in a system comprising two one dimensional chiral waveguides coupled to a dissipative Rydberg atom pair. By employing the Laplace transform method, we analytically solve the scattering problem and characterize the transport properties. Our results demonstrate robust perfect single-photon diode effects in this system with or without dissipation, exhibiting unity transmittance in the forward direction and zero transmittance in the backward ...
  </details>

- **2026-11-22** — Yuexun Huang, Kfir Sulimany, Ke Lin et al. — [LIELLA: Private Edge Adaptation with Photonic Weight Streams](http://arxiv.org/abs/2611.29343v1)
  <details><summary>📄 Abstract</summary>
  Although photonic accelerators have shown promise for energy-efficient machine learning inference, privately personalizing large models across multiple edge clients remains difficult under tight memory, precision, and hardware constraints. We present LIELLA, a weight-streaming architecture that enables multiple edge clients to personalize a shared model through compact private adapters. The two proposed photonic adapter architectures accommodate both backpropagation and forward-only optimization...
  </details>

- **2026-11-22** — Jiazhe Zhang, Zibin Geng, Qiang Ma et al. — [Probe Before You Learn: Allocating Prompts from Initial Gradients under Label Noise](http://arxiv.org/abs/2611.29336v1)
  <details><summary>📄 Abstract</summary>
  Prompt learning provides a parameter-efficient way to adapt pretrained vision--language models through text and visual prompts, but noisy labels prevalent in real-world data inevitably bias prompt updates and thereby undermine adaptation effectiveness. Prior work on robust prompt learning focuses on suppressing unreliable updates under noisy supervision. We uncover a pivotal yet overlooked aspect--prompt allocation: shifting the parameter budget between text and visual prompts can substantially ...
  </details>

- **2026-11-22** — Huan Lyu, Yawei Luo — [InfoField3D: Differentiable Information Field for Embodied Task-Oriented View Planning](http://arxiv.org/abs/2611.29230v1)
  <details><summary>📄 Abstract</summary>
  Effective task execution requires embodied agents to select observation positions that provide sufficient task-relevant information. Existing approaches typically predict viewpoints with learned models or score discrete candidates, but they either struggle to incorporate new constraints such as reachability or require extensive candidate evaluation to search. We introduce InfoField3D, which lifts geometry-bound information into a differentiable analytic field, whose value at each 3D observation ...
  </details>

- **2026-11-21** — Seshu Tirupathi, Elizabeth M. Daly, Radu Marinescu et al. — [LITMUS - Literature Informed Testbed for Mapping Usecases and Synthesizing Risk-Cards](http://arxiv.org/abs/2611.29034v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of large language models (LLMs) and Artificial Intelligence (AI) in real-world applications has heightened the need for systematic, safety-oriented deployment frameworks. Existing approaches typically prioritize the construction of datasets and risk cards around the LLM and AI architecture itself, yet they provide scant consideration for the specific use-case that drives model selection. This omission is problematic because any practical AI deployment begins with a detailed use...
  </details>

- **2026-11-21** — Dexia Chen, YiLong Hu, Wenqi Zhong et al. — [Improving the Improver: Semantic PID Control for Medical Agent Self-Improvement](http://arxiv.org/abs/2611.28680v1)
  <details><summary>📄 Abstract</summary>
  High-stakes vertical medical tasks, such as postoperative pathological staging and long-term survival prediction, demand multi-step clinical reasoning over heterogeneous evidence under weak supervision and high outcome uncertainty. While we first orchestrate CliAgent, a domain-tailored clinical agent workflow that systematically grounds predictions in multi-modal patient evidence, manually designed medical agents remain constrained by static, brittle rules. Moreover, existing recursive self-impr...
  </details>

- **2026-11-21** — Daniel M. Cherenson, Dimitra Panagou — [Distributed Interactive Conformal Prediction for Multi-Agent Systems](http://arxiv.org/abs/2611.29037v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems increasingly rely on learning-enabled components and distributed algorithms for perception, estimation, and control, introducing uncertainty that makes it challenging to satisfy mission requirements. Conformal prediction quantifies uncertainty with distribution-free guarantees, but existing methods do not address the challenging combination of dependence among robots, distributed calibration, and the distribution shift induced when calibrated uncertainty bounds modify the clo...
  </details>

- **2026-11-21** — Felix Desyatirikov — [Watermark Claims Under Test: Lessons from Auditing a Production LLM](http://arxiv.org/abs/2611.29018v1)
  <details><summary>📄 Abstract</summary>
  Can we tell whether an LLM is watermarked without knowing its secret key? Published black-box tests suggest that carefully designed prompts can reveal the statistical footprint of a watermark. This paper examines what happens when those tests move from controlled reference implementations to a deployed model whose watermarking parameters are undisclosed. We present an audit of the Red-Green watermark presence test on Claude. Across ten initial configurations, the published test never rejects on ...
  </details>

- **2026-11-21** — Sebastian Damrich, Dmitry Kobak — [Stochastic non-metric MDS for noisy high-dimensional data](http://arxiv.org/abs/2611.28985v1)
  <details><summary>📄 Abstract</summary>
  Multidimensional scaling (MDS) constructs low-dimensional embeddings that approximate pairwise distances in a high-dimensional dataset. MDS exists in several flavors, with metric MDS approximating distances directly and non-metric MDS additionally optimizing for an arbitrary monotonic transformation of the high-dimensional distances. Empirically, metric MDS is known to suffer from the curse of dimensionality. Here we extend prior theoretical results for metric MDS on fully uninformative data to ...
  </details>

- **2026-11-21** — Fangxu Yu, Lingzhi Yuan, Dehai Min et al. — [EmoRouter: Adaptive Modality Cascading for Multimodal Emotion Recognition](http://arxiv.org/abs/2611.28960v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Emotion Recognition (MER) involves detecting the underlying emotion behind each utterance within a conversation, which is essential for emotionally aware human-computer interaction. While omni-modal large language models (Omni-LLMs) demonstrate strong capability for MER by jointly processing modalities including text, audio, and vision, different modality combinations yield different prediction outcomes across utterances: acoustic and visual inputs can help recover annotated labels mi...
  </details>

- **2026-11-21** — Debalina Ghosh Paul, Hong Zhu, Ian Bayley — [Micro Operational Robustness of LLMs on Code Generation](http://arxiv.org/abs/2611.28957v1)
  <details><summary>📄 Abstract</summary>
  It is now common practice in software development for large language models (LLMs) to be used to generate program code. It is desirable to evaluate the robustness of LLMs for this usage. This paper is concerned in particular with how sensitive LLMs are to variations in descriptions of the coding tasks. However, existing techniques for evaluating this robustness are unsuitable for code generation because the input data space of natural language (NL) descriptions is discrete and sparse. To address...
  </details>

- **2026-11-21** — Morteza Kimiaei, Arnold Neumaier — [A feasible point method for derivative-free linearly constrained optimization](http://arxiv.org/abs/2611.28891v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a framework for linearly constrained derivative-free optimization (DFO) in which the original objective function is evaluated only at feasible points. The method first analyzes the linear constraint system using certificates of infeasibility and implied activity to detect infeasibility or a singleton feasible set, or, when the feasible set has positive dimension, to identify the affine subspace spanned by the feasible set and obtain an equivalent reduced representation with a...
  </details>

- **2026-11-21** — Yifei Cheng, Xiaolin Zhang, Yu-Xuan Qiu — [Reducing Permutation Sensitivity in Multimodal Large Language Models via Shared Positions and Attention-Only Distillation](http://arxiv.org/abs/2611.28612v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we conduct a systematic study on improving permutation robustness while preserving accuracy. First, we categorize permutation bias phenomena into four representative scenarios. Then, we take the multiple-choice question answering (MCQA) dataset as an example under text-option reordering scenario to analyze the root cause of permutation bias. Based on this root cause analysis and set encoding strategy, we investigate shared positions with blocked cross-unit attention (SP-B) and ext...
  </details>

- **2026-11-21** — Zunlong Liu, Weijie Feng, Jingzhi Li et al. — [MADRec: Reliable Multi-Agent Reasoning with Evidence-Grounded Debate for Recommendation](http://arxiv.org/abs/2611.28604v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are transforming recommender systems from conventional preference matching toward reasoning-driven and explainable decision-making. Multi-agent collaboration further advances this paradigm by distributing recommendation reasoning across specialized agents. However, existing frameworks rarely assess the reliability of intermediate reasoning during collaboration, allowing erroneous judgments to propagate across agents and ultimately degrade recommendation quality. To a...
  </details>

- **2026-11-19** — Chunbo Jiang, Yifei Chen, Beining Wu et al. — [DeepQuest: From Knowledge Gaps to Scientific Discovery in Alzheimer's Disease](http://arxiv.org/abs/2611.26343v1)
  <details><summary>📄 Abstract</summary>
  Automating experiments does not necessarily advance scientific understanding. Research agents must identify meaningful knowledge gaps, determine what available data can resolve, and assess whether their findings advance existing knowledge. We introduce DeepQuest, a knowledge-gap-driven AI scientist framework for Alzheimer's disease research. DeepQuest transforms unresolved questions from domain reviews into traceable, testable hypotheses and prioritizes them through data feasibility screening an...
  </details>

- **2026-11-19** — Youssef ElNahas, Adel Ammar, Soumaya Chaffar et al. — [Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding](http://arxiv.org/abs/2611.25898v1)
  <details><summary>📄 Abstract</summary>
  Clinical large language models are usually judged by whether the final answer is right. Yet a model can reach a fluent, plausible output through invalid reasoning that static benchmarks do not detect, and confident hallucination, causally invalid inference, and spurious demographic shortcuts can pass conventional evaluation. This critical review covers four paradigms in turn: how clinical hallucination arises and why static metrics miss it; the agentic hallucination cascade, in which multi-agent...
  </details>

- **2026-11-19** — Filippo Galgani, Ziwei Ji, Omri Homburger et al. — [Efficient and Robust Drafting with Multi-Token Prediction](http://arxiv.org/abs/2611.25813v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding has emerged as a critical technique for accelerating Large Language Model (LLM) inference by decoupling generation into a drafting phase and a parallel verification phase. A crucial challenge is therefore designing a drafter that is both lightweight and accurate enough to approximate the predictions of the target model. We present a highly optimized Multi-Token Prediction (MTP) architecture that extends existing backbone LLMs to efficiently produce high-quality drafts. Built...
  </details>

- **2026-11-19** — Yingshuo Wang, Weixiang Zhao, Guancheng Li et al. — [When Safety Rationales Hallucinate: Diagnosing and Grounding Multimodal Safety Guards](http://arxiv.org/abs/2611.25793v1)
  <details><summary>📄 Abstract</summary>
  Multimodal safety guards increasingly generate rationales alongside safety predictions, yet whether these rationales are reliable remains largely unexplored. We systematically study *rationale hallucination* from two perspectives: visual rationale hallucination, where rationales contain unsupported visual facts, and safety attribution hallucination, where grounded content is assigned an incorrect safety interpretation. Across rationale-generation methods, multiple vision-language backbones, and ...
  </details>

- **2026-11-19** — Yajie Qi, Wei Wei, Lin Li et al. — [Goal-Guided Reinforcement Learning via Fine-Tuning Vision-Language Models](http://arxiv.org/abs/2611.25742v1)
  <details><summary>📄 Abstract</summary>
  Exploration remains a major challenge for reinforcement learning (RL) agents in Craftax-style environments due to sparse rewards and long horizons. Large language models (LLMs) can guide exploration by generating high-level goals, but methods using models without explicit task adaptation often rely on carefully designed prompts and may produce inconsistent or contextually inappropriate goals. We introduce CCGP-2M, a multimodal goal-preference dataset constructed from interaction trajectories in ...
  </details>

- **2026-11-19** — Xu Pan, Chubin Zhang, Xingrui Yu et al. — [CauSyncVLA: Causal Latent World Modeling for Asynchronous Robot Control](http://arxiv.org/abs/2611.25667v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) policies must react while visual inference is still running. Overlapping computation and execution reduces waiting, yet leaves perceptual memory stale and successive action chunks disconnected. We present CauSyncVLA, an asynchronous dual-system controller that aligns perceptual-memory prediction and trajectory correction with actual robot execution. Rather than forecasting pixels or physical states, a Causal Latent World Model predicts current perceptual memory from ...
  </details>

- **2026-11-19** — Geon Lee, Fanchen Bu, Soo Yong Lee et al. — [Toward a Science of AI Agent Societies](http://arxiv.org/abs/2611.25404v1)
  <details><summary>📄 Abstract</summary>
  AI agents are rapidly evolving from isolated personal assistants into networked actors that interact with one another at scale. We envision the emergence of AI agent societies, with their own social and economic dynamics, as a new research frontier. We argue that AI agent societies should be studied as a distinct object of inquiry: neither simply larger collections of individual agents nor merely simulations of human society. To formalize this perspective, we propose four core properties that a ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 24 papers

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

- **2026-11-22** — Lo Gullstrand Heander, Emma Söderberg, Christofer Rydenfält — [Admitted Is Not Effective: Lessons from a Notary-Gated Retrospective Loop in an Agentic Pipeline](http://arxiv.org/abs/2611.29727v1)
  <details><summary>📄 Abstract</summary>
  Agentic software development pipelines with frozen prompts can repeat the same mistakes across pull requests (PRs), yet ungoverned additions to instruction files grow without bound and do not generally improve task success. We present a retrospective loop for a four-stage large language model (LLM) pipeline in which a Retrospective agent proposes edits to learned rules every ten PRs and a Notary admits, merges, or rejects them while recording each decision in a provenance ledger. In a pre-regist...
  </details>

- **2026-11-22** — Pinaki Prasad Guha Neogi, Spyros Mastorakis, Ankur Mallick et al. — [NoeVera: Can Knowledge Guide Experiments and Experiments Refine Knowledge?](http://arxiv.org/abs/2611.29255v1)
  <details><summary>📄 Abstract</summary>
  With the growing demand for large language model (LLM) services, optimizing LLM serving systems is becoming increasingly complex, and the bottleneck is no longer predicting how a given configuration will perform. The harder problem is deciding what to investigate: which mechanisms matter for a workload, which configurations are worth testing, and what evidence a decision still needs. In this work, we present NoeVera, an agentic Second Brain that goes beyond just one-shot retrieval by turning pap...
  </details>

- **2026-11-22** — Can Liu, Tengteng Zhu, Xinyu Jiang et al. — [DataRecycle: Trustworthy Distillation of Structured Data from Scattered Web Evidence](http://arxiv.org/abs/2611.29206v1)
  <details><summary>📄 Abstract</summary>
  The web contains vast amounts of scattered quantitative evidence that is difficult to organize into comparable and verifiable structures. Yet its unstructured, sparse, and sometimes conflicting nature makes a systematic distillation costly and error-prone. Existing approaches force users to make a trade-off: search engines return document lists that require labor-intensive extraction and reconciliation, while generative AI systems produce fluent summaries that obscure data provenance, introduce ...
  </details>

- **2026-11-22** — Vaishak Girish Kumar, Sanika Vilas Najan — [When Can a Rewiring Control Test LLM Weight Readers? C2 and an Eligibility Protocol](http://arxiv.org/abs/2611.29120v1)
  <details><summary>📄 Abstract</summary>
  Large language models can predict the outputs of small neural networks from raw weights, but success could reflect recognition of weight-space regularities (fingerprints) rather than computation, and function-preserving controls cannot tell these apart. We propose C2, a counterfactual that permutes the columns of a network's final linear readout: every other parameter, and the readout's singular values, norms and entry multiset, are unchanged, and the function can change in an exactly recomputab...
  </details>

- **2026-11-21** — Noah S. Okada, Ketika Garg, Wenning Deng et al. — [Do LLM Agents Compromise Like Humans? Risk and Responsibility in Dyadic Decision-Making](http://arxiv.org/abs/2611.29069v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agents are increasingly deployed in settings where they must collaborate to make joint decisions. We investigate how this collaboration unfolds under risk, asking whether agents adjust their choices to accommodate their partners, how they assign responsibility for shared outcomes, and whether responsibility attribution shapes subsequent adjustment. We designed a series of agents with systematically varying risk preferences and paired them in a repeated joint deci...
  </details>

- **2026-11-21** — Wenxuan He, Shan Liang — [From Spatial Perception to Speech Recovery: Binaural Semantic Adaptation for Spatially Grounded Multi-Talker Transcription](http://arxiv.org/abs/2611.29012v1)
  <details><summary>📄 Abstract</summary>
  Spatial audio large language models increasingly combine general audio understanding with spatial perception. Yet overlapping conversations require more than locating speakers. A model must also recover what each person says and match the words to their positions. We examine this challenge in MiDashengLM-Spatial, a binaural model designed for both spatial reasoning and general audio understanding. To test these abilities, we introduce BiCP-Bench, a benchmark of overlapping two-speaker binaural r...
  </details>

- **2026-11-21** — Boyan Li, Zhuowen Liang, Yupeng Xie et al. — [A Design Space for Data Agents: Insights from KDD Cup 2026](http://arxiv.org/abs/2611.28970v1)
  <details><summary>📄 Abstract</summary>
  Data agents interpret analytical requests, gather evidence from heterogeneous sources, and compute results within finite resource budgets. We analyze the final code submissions of the ten highest-ranked teams in the KDD Cup 2026 Data Agents for Complex Data Analysis competition. We organize the observed design choices into three interacting layers, covering workflow orchestration, analytical functions, and working state. The comparison reveals recurring patterns for allocating computation in res...
  </details>

- **2026-11-21** — Wanghao Ye, Sihan Chen, Bowei Tian et al. — [Can Your AI Twin Meet People for You? It Can Hold a Conversation. But What Does It Need to Judge Like You?](http://arxiv.org/abs/2611.28692v1)
  <details><summary>📄 Abstract</summary>
  Should your AI twin go meet people on your behalf? We built LLM twins of 710 real people from their other conversations in the CANDOR corpus, sent them to meet each other in 5,680 simulated first conversations, and checked every rehearsal against what the real people said after meeting for real (355 held-out, participant-disjoint pairs, against baselines that include each person's rating history). The rehearsals work: a twin's conversation predicts real liking ($ρ$=0.277), carries information th...
  </details>

- **2026-11-21** — Zhengyang Lu,  QianhongWen, Chenpeng Wang et al. — [CrossPanel: Exposing the Answer-Evidence Gap in Scientific Figure Understanding](http://arxiv.org/abs/2611.28641v1)
  <details><summary>📄 Abstract</summary>
  A correct answer to a scientific-figure question can conceal an incorrect account of the experiment. Reading evidence across panels requires keeping each observation attached to the object and conditions that give it meaning. We introduce CrossPanel, a benchmark of 2,650 human-reviewed questions that exposes this answer-evidence gap. Its tasks combine parallel observations or follow dependent queries, while a response audit separates object selection, experimental conditions, cross-panel binding...
  </details>

- **2026-11-21** — Yukinori Yamamoto, Kotaro Yoshida, Ryotaro Shimizu — [Interpreting Diffusion Model Activations in Natural Language](http://arxiv.org/abs/2611.28621v1)
  <details><summary>📄 Abstract</summary>
  Interpreting the intermediate activations of diffusion models (DMs) is key to understanding how they generate images. Existing interpretability methods for DMs provide limited support for open-ended interrogation, making it difficult to extract human-interpretable insights. We extend LatentQA, the task of answering natural-language questions about Large Language Model activations, to DM activations. We introduce the Diffusion-specific Activation Oracle (DAO), which translates DM activations into...
  </details>

- **2026-11-21** — Jin Cui, Xinyue Long, Jiepeng Zhou et al. — [From Reward Engineering to Data-Centric Reinforcement Learning for Effective Agentic Visual Tool Use](http://arxiv.org/abs/2611.28558v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) increasingly use external visual tools to acquire evidence during reasoning, yet learning when to invoke these tools remains challenging. Existing tool-use reinforcement learning (RL) methods often rely on call-contingent rewards to encourage beneficial tool use, but such reward engineering can distort the task objective and lead to degenerate calling behaviors. We argue that effective tool-use learning requires identifying not merely which questions are ...
  </details>

- **2026-11-20** — Haoyang Wang, Weibo Gao, Zhengxiong Li et al. — [Task2Hand: A Contact-Grounded Skill for Parametric Dexterous-Hand Morphology Design](http://arxiv.org/abs/2611.27967v1)
  <details><summary>📄 Abstract</summary>
  Dexterous hand design demands repeated expert work across geometry, robot-description code, collision debugging, grasp initialization, and policy training. We present Task2Hand, a Skill: a specification package that turns a functional manipulation brief into a parameterized hand model and routes every candidate through cost-ordered contact, dynamics, and learning gates. Each gate returns a status and an evidence record; on failure, the Skill records the earliest blocker, revises one bounded para...
  </details>

- **2026-11-20** — Yi Ding, Gaurav Kumar, Rui Min et al. — [The Dual-Tier Sentiment Framework: Scalable Multimodal UX Attribution in Web Search](http://arxiv.org/abs/2611.27899v1)
  <details><summary>📄 Abstract</summary>
  Sustaining user experience (UX) quality in large-scale web search requires scalable evaluation. Traditional surveys are slow and bottleneck rapid A/B testing, while automated metrics often lack the granularity to diagnose visual-spatial UX anomalies. To address this, we introduce the Dual-Tier Sentiment Framework, a novel industrial architecture for automated UX attribution. Tier 1 (Macro System) acts as a scalable user sentiment regression detector, utilizing a fine-tuned encoder-decoder LLM (b...
  </details>

- **2026-11-19** — Divya Acharya, Thomas M. Roehr, Arnaud Gotlieb — [Trustworthy Geospatial AI Workflows: Reproducible Maritime Analytics and Forecasting on Open-Source AIS Data](http://arxiv.org/abs/2611.25884v1)
  <details><summary>📄 Abstract</summary>
  Publicly available geospatial data provide increasing opportuni- ties for data-driven maritime analytics and predictive modelling. However, their availability does not necessarily imply that the underlying observations are equally suitable for downstream AI applications. Properties of the data source and observation pro- cess, including provenance, reporting regularity, spatial coverage, observation density, and missingness, can affect how geospatial data are interpreted, processed, and ultimate...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-11-23** — Devang Kulshreshtha, Priyanka Kaswan, Minh Pham et al. — [Multimodal View Training: Learning More Through Different Modalities](http://arxiv.org/abs/2611.30165v1)
  <details><summary>📄 Abstract</summary>
  Can a language model learn more from the same information simply by encountering it in different forms? We answer this in the affirmative by introducing Multimodal View Training (MVT), a simple training approach that presents identical information through text, speech, and images, without requiring new facts or supervision. Starting from a text sample, MVT generates corresponding audio and rendered-text image views, and trains a multimodal language model to produce the same target output across ...
  </details>

- **2026-11-22** — Arsalan Kaleem — [Compared to What? Calibrating Machine-Unlearning Diagnostics with Present, Absent and Suppressed Anchors](http://arxiv.org/abs/2611.29285v1)
  <details><summary>📄 Abstract</summary>
  Unlearning methods for language models are judged mainly by behaviour, but a model can stop producing an answer while still encoding it. Internal diagnostics such as linear probes, the logit lens and relearning speed are used to tell removal from suppression, yet none has been checked against cases where the answer is known. We build such cases. A present anchor learned a set of synthetic facts; an absent anchor is a never-taught oracle retrained without them; and suppressed anchors are unlearne...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 2 papers

- **2026-11-23** — Benjamin Alt — [SayDo: Benchmarking the Safety of Frontier Models from Chat to Closed-Loop Robot Control](http://arxiv.org/abs/2611.30957v1)
  <details><summary>📄 Abstract</summary>
  Frontier vision-language models (VLMs) are increasingly used as high-level robot controllers, yet their safety is evaluated almost entirely in text. We introduce SayDo, a benchmark that assesses the propensity of frontier models to cause harm in embodied contexts. SayDo comprises eleven laboratory and household tasks that pair a benign instruction with a hazard latent in the scene. Tasks are implemented in six settings along an embodiment gradient, from chat questions about an imagined robot to ...
  </details>

- **2026-11-19** — Almene De Meran Meguimtsop, Daniel E. Acuna — [Why Do LLMs Help with Scientific Misconduct Requests and What to Do About It?: Increasing the Trustworthiness of AI for Science](http://arxiv.org/abs/2611.25492v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) support scientific research, but some of that assistance can also undermine research integrity. Existing safety evaluations in science often measure whether models refuse misconduct requests, but rarely explain whether they even recognize the problem or why they comply. We investigate this gap across 8 LLMs using SciIntBench, an existing benchmark of 1,350 prompts about scientific research integrity. We examine the reasons behind compliance in four steps. First, when...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-11-23** — Federico Semenzato, Benjamin D. Wandelt, Michele Liguori et al. — [Interpretable morphology-based marked statistics](http://arxiv.org/abs/2611.31167v1)
  <details><summary>📄 Abstract</summary>
  The shapes and environments of cosmic structures carry cosmological information beyond the matter power spectrum. Recovering this information while retaining a physical understanding is a central challenge for cosmological inference. We construct an interpretable, rotation-equivariant neural marking scheme that reweights the matter field, combining learned density responses with explicit measures of local morphology. This approach enables direct inspection of the learned transformations, while r...
  </details>

- **2026-11-23** — Carlos Rafael Catalan, Lheane Marie Dizon, Patricia Nicole Monderin et al. — [Useful but Unwieldy: How Software Engineers Perceive the Design of Chain-of-Thought Explanations in Coding Agents](http://arxiv.org/abs/2611.30894v1)
  <details><summary>📄 Abstract</summary>
  Coding agents (CAs) powered by Large Language Models (LLMs) are increasingly integrated into software engineering (SE) workflows. As these CAs take up more tasks and responsibilities, it is imperative for software engineers to understand the CA's rationale behind its' decisions, also known as the chain-of-thought (CoT). During the interaction, some CAs are capable of showing this CoT as a separate message to users with the goal of providing transparency and explainability. However, its effective...
  </details>

- **2026-11-21** — Mario Lillo-Saavedra, Marcela Salgado-Vargas, Ángel García-Pedrero et al. — [Who Speaks for the Water? Simulating Discursive Closure and Power Asymmetries in Hydrosocial Governance](http://arxiv.org/abs/2611.28755v1)
  <details><summary>📄 Abstract</summary>
  Water governance conflicts stem not only from material scarcity, but from power asymmetries, institutional distrust, and the discursive frameworks through which actors assign meaning to water, infrastructure, and legitimate authority. Conventional simulation tools represent these dynamics via numerical opinion variables, missing the argumentative and narrative dimensions structuring real deliberation in hydrosocial territories. We present the Hydrosocial Agent-Based Model with Large Language Mod...
  </details>

- **2026-11-21** — Wendong Yao, Binhua Huang, Soumyabrata Dev — [What the Background Hides: Thresholds, Vocabularies and Collisions in Training-Free Open-Vocabulary Segmentation](http://arxiv.org/abs/2611.28966v1)
  <details><summary>📄 Abstract</summary>
  Training-free open-vocabulary semantic segmentation (OVSS) built on CLIP has advanced rapidly, with methods typically ranked by mean intersection-over-union (mIoU) across standard benchmarks. On datasets with a background class, however, implementations rely on per-dataset thresholds and background word lists that are rarely documented or unified (11 of 13 surveyed methods configure per-dataset background decisions). We audit configurations and papers of 13 training-free OVSS methods, re-run sev...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 185 papers

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

- **2026-11-22** — Haozhe Zhao, Junxiang Zhang, Junxin Wang et al. — [FP-Prune: Rethinking Visual Token Pruning from an Information Gain Perspective](http://arxiv.org/abs/2611.29327v1)
  <details><summary>📄 Abstract</summary>
  Visual token pruning can reduce the inference cost of vision language models, but its effectiveness depends on preserving complementary visual information under a limited token budget. A central challenge is to quantify the additional information a candidate token contributes beyond the retained set, a contribution that conventional scores based on attention or similarity struggle to capture directly. In this work, we revisit visual token pruning from the perspective of information gain and use ...
  </details>

- **2026-11-22** — Yijian Zheng, Yi Zhang, Juyuan Zhang et al. — [Multi-Agent Coordinated Method-Level Refactoring of Rust Code](http://arxiv.org/abs/2611.29321v1)
  <details><summary>📄 Abstract</summary>
  As Rust codebases evolve, developers refactor code to reduce duplication, simplify complex methods, and keep related functionality together. Developers can make these changes manually or use IDE assists for supported operations, then check the resulting code with compiler diagnostics and tests. Method-level refactoring in Rust must preserve observable behavior while accounting for ownership, borrowing, and lifetimes. We present a large language model (LLM)-based workflow for extracting, inlining...
  </details>

- **2026-11-22** — Avijit Roy — [Beyond Omission: Measuring Critical-Information Fulfillment of Large Language Models in Bengali and English](http://arxiv.org/abs/2611.29299v1)
  <details><summary>📄 Abstract</summary>
  Evaluations of multilingual trustworthiness often ask whether a model leaves out information that a user needs. We examine whether that question is sufficient. Using 157 matched tasks written in English (EN), natural Bengali (BN) and Bengali-matrix Bengali-English code-switching (BN-CS), we scored 1,413 responses from three models (GPT-6.1 Sol, Qwen3.5-9B and Gemma 4 12B) against required information units (RIUs) fixed before any model was run. The scoring separates outright omission from conten...
  </details>

- **2026-11-22** — Siavash Taremi, Mahmoud Heidari, Seyed Mohammad Hossein Hashemi et al. — [A Cascaded Framework with a Cross-Attention-Guided Mamba-CNN Model for Pre- and Post-Treatment Glioma Segmentation](http://arxiv.org/abs/2611.29792v1)
  <details><summary>📄 Abstract</summary>
  Accurate glioma segmentation is vital for diagnosis and follow-up, but manual segmentation is time-consuming, subjective, and variable across interpreters. Gliomas are heterogeneous in size, shape, and location. Deep learning has therefore emerged as a potential solution. CNNs excel at local features but may struggle with long-range dependencies, whereas Vision Transformers capture global context efficiently but incur higher computational complexity. Most previous studies focused on pre-treatmen...
  </details>

- **2026-11-22** — Haoxiang Zhan, Haoqin Hong, Congcong Zhu et al. — [Action Windows Are Inherently Temporal: A Benchmark for Time-Sensitive Robotic Manipulation](http://arxiv.org/abs/2611.29558v1)
  <details><summary>📄 Abstract</summary>
  Vision-language model (VLM) agents have surpassed learned-policy baselines on existing robotic manipulation benchmarks. However, these agents still struggle with time-sensitive everyday tasks that existing benchmarks for VLM agents cover only partially. In these tasks, evolving physical processes create finite windows for successful intervention. These action windows are inherently temporal and impose a shared time budget on decision making and physical execution. Coordinating intervention withi...
  </details>

- **2026-11-22** — Shilin Shan, Yuxuan Hu, Chuhao Zhou et al. — [Contact Harness: Enabling VLM Agents to Perform Contact-Rich Manipulation](http://arxiv.org/abs/2611.29377v1)
  <details><summary>📄 Abstract</summary>
  Agents built on pretrained VLMs have demonstrated zero-shot control of real robots, but vision alone is often insufficient for reliable contact-state assessment in contact-rich manipulation. Force and tactile feedback provide complementary information, but their semantic ambiguity makes them difficult for agents to use directly. These signals must be interpreted according to their physical meaning, together with task phase and visual evidence. We propose Contact Harness, which uses reusable, opt...
  </details>

- **2026-11-22** — Meng-Hao Guo, Yi Zhang, Zhe-Han Mo et al. — [A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation](http://arxiv.org/abs/2611.29338v1)
  <details><summary>📄 Abstract</summary>
  Recently, GPT-6 Astra demonstrates strong generalization in robot control, yet limited disclosure of its training leaves open how such capabilities can be reproduced. We introduce nanoAstra, an approach to training vision-language models (VLMs) for generalizable manipulation that combines semantic action modeling with capability-preserving supervised fine-tuning (CP-SFT). nanoAstra represents robot behavior as semantic steps composed of reusable, parameterized action primitives, guided by explic...
  </details>

- **2026-11-22** — Shurui Liu — [Notes on Generative AI for Mathematical Research](http://arxiv.org/abs/2611.29811v1)
  <details><summary>📄 Abstract</summary>
  These notes describe how generative AI is now used to solve and to check research-level mathematics, with a focus on agents and their harnesses. For the proving agents Rethlas, Danus, and Pharos and the verification agent OSVerify, we explain the design principles, compare each with its base model, present case studies, and show how to use and contribute to them. We also briefly review the history of AI for mathematics and the community's reactions to it.
  </details>

- **2026-11-22** — Aleix Segui, Arantza Ugalde, Andreas Fichtner et al. — [Monogenic signal analysis for wavefield characterisation in distributed acoustic sensing](http://arxiv.org/abs/2611.29757v1)
  <details><summary>📄 Abstract</summary>
  The spatio-temporal wavefield sampled by distributed acoustic sensing (DAS) contains intertwined information about signal strength, oscillatory structure and propagation. We introduce a methodology to disentangle these properties, with applications to the analysis of weak arrivals obscured by noise or stronger wave trains. The method is based on the monogenic signal, a two-dimensional extension of the analytic signal defined via the Riesz transform. In DAS, the monogenic signal decomposes locall...
  </details>

- **2026-11-22** — Martin Pavlíček, Martin Kotyrba, Eva Volná et al. — [Where Do Fact-Checking Errors Arise? Separating Retrieval, Search Control and Judgement in Evidence-Grounded Verification](http://arxiv.org/abs/2611.29697v1)
  <details><summary>📄 Abstract</summary>
  An evidence-grounded fact-checker can fail because it does not find the evidence or because it does not use it; end-to-end accuracy does not tell the two apart. We present a protocol that follows the reference evidence from the store to the verdict and separates retrieval, search control, judgement and verdict validation. We assess 293 claims from FEVER, FEVER 2.0 and AVeriTeC with one open-weights 9B model under two evidence conditions: small stores of annotated evidence, where discovery is eas...
  </details>

- **2026-11-22** — Luca Meacci, Francisco J. Muñoz, Juan Carlos Nuño — [Analytical modelling of compliance dynamics under fiscal feedback: tipping thresholds, intervention costs and hysteresis](http://arxiv.org/abs/2611.29688v1)
  <details><summary>📄 Abstract</summary>
  Compliance with taxes and other collective obligations is often enforced with resources that come from those who comply, so that non-compliance erodes its own deterrent. We develop an exactly solvable dynamical model of compliance under this fiscal feedback. Individuals choose between paying and evading by imitating those who do better, and the budget against evasion is a share of the revenue, split between enforcement and education. The model yields closed-form expressions for the equilibria, t...
  </details>

- **2026-11-22** — Jacopo Graldi, Antonio Orvieto, Anastasia Koloskova — [From Learning Rates to Rotational Schedules: Finite-Horizon Theory on the Sphere](http://arxiv.org/abs/2611.29579v1)
  <details><summary>📄 Abstract</summary>
  How should step sizes be scheduled across a finite training horizon? Cosine and warmup-stable-decay (WSD) schedules are widely adopted in large-scale pretraining, yet their effect on optimization also depends on parameter norms. Normalization can make parameter groups scale invariant, so that the loss depends only on their direction, while their norms still affect how fast the parameters rotate. In this work, we formulate schedule design directly in the space of rotational motion. Working within...
  </details>

- **2026-11-22** — Ewsey Obzherin, Samira Atlangirieva, Anastasia Antsiferova et al. — [CoHABIT: Complementary Evaluation of Furniture Layouts through Spatial Rules and Household Routines](http://arxiv.org/abs/2611.29494v1)
  <details><summary>📄 Abstract</summary>
  We introduce CoHABIT, a framework for evaluating furniture layouts through complementary spatial rules and household routines. Static assessment captures geometric validity, ergonomic access, functional organization, and configurable design preferences, including Feng Shui. Dynamic assessment uses learned resident policies to simulate everyday activities, resource sharing, coordination, and individual burdens in multi-agent households. Controlled comparisons show how spatial criteria and househo...
  </details>

- **2026-11-22** — Xixi Jiang, Pingcheng Dong, Chen Yang et al. — [CAR: Reducing Decoder Output Shift in Visual Token Pruning via Coverage Selection and Attention Reallocation](http://arxiv.org/abs/2611.29489v1)
  <details><summary>📄 Abstract</summary>
  Visual token pruning is an effective way to accelerate multimodal large language models (MLLMs). However, existing methods degrade substantially under aggressive pruning, especially on visual grounding (VG). We analyze the sources of this degradation from the perspective of the output shift that pruning causes in decoder layers, and decompose this shift in closed form into two terms, an image summary error and an attention allocation error. The summary error stems from the loss of visual informa...
  </details>

- **2026-11-22** — Kai Tang, Chao Zhan, Yao Song et al. — [Unveiling the Action of Randomized Compiling on Quantum States: A Geometric Perspective](http://arxiv.org/abs/2611.29488v1)
  <details><summary>📄 Abstract</summary>
  Randomized compiling (RC) converts coherent errors into stochastic Pauli noise, but this conversion alone does not imply isotropic contraction of the output state. Here we use the generalized Bloch vector (GBV) representation to examine the cumulative effect of RC on state purity and orientation in multi-layer circuits. For the independent, isotropically distributed weak coherent errors considered here, the accumulated ensemble-averaged RC channel lies close to the depolarizing direction, produc...
  </details>

- **2026-11-22** — Ruiji Yu, Wenye Ma, Gus Xia — [Music Circuit: Trace and Control Style Dynamics in Large Music Generation Model](http://arxiv.org/abs/2611.29475v1)
  <details><summary>📄 Abstract</summary>
  Musical style, a global attribute that functions throughout a whole piece, is a lever widely used by users in modern large music generation models. Yet how style is represented inside these models, and which components drive it, remains largely unexplored. In language models, circuit analysis traces a representation to a sparse sub-network of a few key components, namely attention heads and MLP neurons, and has been used successfully to explain and control global attributes such as emotion. In t...
  </details>

- **2026-11-22** — Ryo Kuroki, Amin Mansouri, Philippe Schwaller — [Beyond Accuracy: A Diagnostic Benchmark for Hypothesis-Driven Experiment Planning in LLM Agents](http://arxiv.org/abs/2611.29467v1)
  <details><summary>📄 Abstract</summary>
  Evaluating large language model (LLM) agents on scientific tasks typically reduces to final-task accuracy, which obscures where reasoning succeeds or breaks down. We introduce a benchmark and diagnostic evaluation framework for hypothesis-driven adaptive experimental planning in closed-world system identification, instantiated in kinetic mechanism identification. The framework goes beyond final accuracy in two ways. First, we evaluate exploration behavior by quantifying the extent to which agent...
  </details>

- **2026-11-22** — Kele Xu, Qisheng Xu, Xinwang Liu et al. — [Voice Agents: From Auditory Intelligence to Auditory Agency](http://arxiv.org/abs/2611.29465v1)
  <details><summary>📄 Abstract</summary>
  Voice systems increasingly combine streaming speech, persistent state, reasoning, tool use, and embodied control. Once these functions share a runtime, spoken input can change digital or physical state, and recognition or response quality alone no longer characterizes the system. This article studies the interfaces through which spoken evidence becomes consequential. \emph{Auditory intelligence} denotes the capabilities required to perceive, understand, coordinate, and generate spoken interactio...
  </details>

- **2026-11-22** — Xinjie Zhang, Linyang He, Yizi Zhang et al. — [MAS-BIT: A Multi-Agent System for End-to-End BraIn-to-Text Decoding](http://arxiv.org/abs/2611.29457v1)
  <details><summary>📄 Abstract</summary>
  Speech brain-computer interfaces aim to restore communication by translating neural activity into text, yet end-to-end decoders have historically trailed cascaded systems in accuracy. We introduce a Multi-Agent System for BraIn-to-Text (MAS-BIT), the first multi-agent framework for end-to-end brain-to-text decoding from intracortical recordings. MAS-BIT coordinates three specialized agents: a neural agent that interprets continuous neural representations, a phonetic agent that decodes soft phone...
  </details>

- **2026-11-22** — Yutian Li — [Strict hot spots and absence of interior critical points on simply connected planar Hölder domains](http://arxiv.org/abs/2611.29324v1)
  <details><summary>📄 Abstract</summary>
  We prove strict hot spots and the absence of interior critical points for every nonzero real eigenfunction at the first positive Neumann eigenvalue of a bounded simply connected planar Hölder domain. The Hölder hypothesis is the quasihyperbolic boundary condition; equivalently, the derivative of a Riemann map belongs to $L^p$ for some $p>2$. The eigenvalue may be multiple, and the boundary need not be Jordan; boundary extrema are then interpreted through the continuous conformal pullback. The th...
  </details>

- **2026-11-22** — Yibing Fu, Huidong Xie, Yihao Niu et al. — [CT-Navigator: Towards Interpretable and Generalizable CT Understanding through Agentic Perception and Tool-Invocation](http://arxiv.org/abs/2611.29305v1)
  <details><summary>📄 Abstract</summary>
  Clinical computed tomography (CT) interpretation inherently requires progressive visual exploration, where radiologists navigate from whole scans to individual slices and regions of interest and interact with external tools when necessary. However, existing 3D medical multimodal large language models (MLLMs) typically connect a specialized 3D visual encoder to a language model, without fully leveraging the native 2D visual and agentic capabilities of generalist MLLMs. Trained on large-scale one-...
  </details>

- **2026-11-22** — Haoyang Xue, Bingkun Liu, Linling Kuang — [WAFT: A Fourier-Analytic Framework for Steady-State Performance of Walker Constellations](http://arxiv.org/abs/2611.29296v1)
  <details><summary>📄 Abstract</summary>
  The Walker configuration is predominantly adopted by nongeostationary orbit constellations exemplified by Starlink and Kuiper. The steady-state distribution of aggregate downlink interference power is critical for spectrum coexistence regulation. Large-scale time-stepped simulation and stochastic geometry (SG)-based models are the mainstream methods for obtaining the distribution, but are either computationally expensive or subject to inherent bias. This paper models the aggregate downlink inter...
  </details>

- **2026-11-22** — Chao Ding, Yidong Jiang, Junzhi Ning et al. — [Seeing Is Not Acting: WARD Diagnoses the Evidence-to-State-to-Action Gap in Longitudinal Clinical Agents](http://arxiv.org/abs/2611.29243v1)
  <details><summary>📄 Abstract</summary>
  Large language models for longitudinal clinical care must revise their assessments and actions as patient information accumulates. However, benchmarks centered on isolated responses or final task outcomes provide limited insight into intermediate failures in evidence use, state updating, and action selection. We introduce WARD, a benchmark for evaluating how clinical agents translate accumulating evidence into patient-state judgments and timely, safe actions. WARD comprises 4,560 clinical tasks ...
  </details>

- **2026-11-22** — Qiwei Wu, Xiangyu Chen, Xin Xiang et al. — [Tacinf: A Unified Tactile Infrastructure for Robot Manipulation](http://arxiv.org/abs/2611.29240v1)
  <details><summary>📄 Abstract</summary>
  Force-aware manipulation requires robots to infer appropriate interaction forces from task context and tactile feedback. We present Tacinf, a low-cost, modular infrastructure that enables policies to predict robot actions and fingertip forces from task language, vision, and touch. Task instructions can optionally specify the desired force level. Tacinf integrates simulation data synthesis and tactile benchmarking (Tabero), vision-tactile-language-action (VTLA) policy learning, handheld data coll...
  </details>

- **2026-11-22** — Di Lu, Xinran Zhang, Yan Gao et al. — [IteraSong: LLM-Guided Iterative Symbolic Music Creation in a Web DAW](http://arxiv.org/abs/2611.29225v1)
  <details><summary>📄 Abstract</summary>
  Music creation is inherently iterative, yet many symbolic generation systems still center on producing or regenerating isolated outputs. We present IteraSong, an interactive web-based Digital Audio Workstation (DAW) for LLM-guided iterative symbolic music creation. Unlike one-shot generation systems, IteraSong supports a generate-audition-edit-refine loop over a persistent multi-track project. Users initialize a fully labeled pop draft, then progressively refine it through natural-language instr...
  </details>

- **2026-11-22** — Haonan Liu, Shuo Wang, Zhao Kang — [THETA: Heat Diffusion as a Structural Prior for Cross-Domain Transfer in Graph Foundation Models](http://arxiv.org/abs/2611.29210v1)
  <details><summary>📄 Abstract</summary>
  Graph foundation models (GFMs) aim to learn transferable representations across domains with heterogeneous node attributes and graph structures. However, relations inferred from node attributes can rely on domain-specific feature semantics, limiting their transferability to unseen graphs, particularly in low-label regimes. We propose THETA (Topology-aware HEat-based TrAnsfer), a graph foundation model that leverages Heat Kernel Signatures (HKS) as a topology-based structural prior for cross-doma...
  </details>

- **2026-11-22** — Duy Tran Thanh — [SpatialDuet: Bayesian task routing between a metric expert and a geometry expert for spatial intelligence](http://arxiv.org/abs/2611.29168v1)
  <details><summary>📄 Abstract</summary>
  Embodied assistants and wearable devices need 3D spatial reasoning, and their limited hardware restricts them to small vision-language models (VLMs). Small spatial VLMs acquire different abilities from their training: a model trained on large spatial question sets estimates object and room sizes well, whereas a model with a 3D geometry encoder is better at relative directions and absolute distances. Instead of training a single model for all spatial tasks, as published methods do, we build one s...
  </details>

- **2026-11-22** — Jiayu Huang, Yichao Cai, Xinyu Li et al. — [ContextFact: Remembering Facts in Context for Long-Term Conversational Agents](http://arxiv.org/abs/2611.29155v1)
  <details><summary>📄 Abstract</summary>
  Agents built on large language models must maintain continuity across repeated interactions with users. However, long-term conversations scatter facts across turns and sessions, making it difficult to retrieve the right evidence with enough context. Memory for such conversations must therefore preserve facts with their context while keeping evidence selectively accessible. We first study how memory construction and retrieval-unit boundaries affect answerability and evidence access. Reading the e...
  </details>

- **2026-11-22** — Soumyabrata Chaudhuri, Joydeep Ghosh — [Bridging Blind Spots With Words: Decentralized Multi-View Spatial Reasoning via Language-Constrained Communication](http://arxiv.org/abs/2611.29112v1)
  <details><summary>📄 Abstract</summary>
  As multimodal LLMs (MLLMs) get increasingly used as collaborative partners across embodied robotics, AR/VR, and multi-user systems, spatial reasoning is now often distributed across agents with partial environment visibility, necessitating spatial reasoning integration. Prior work in language-mediated spatial integration is however strictly limited to simplified two-agent scenarios. To address this gap, we first formalize the general problem of decentralized multi-view spatial reasoning, where N...
  </details>

- **2026-11-22** — Joshua Huang, Ajit Mallavarapu, Elliott Kalt — [Beyond Evidence Coverage: Encoding-Time Access in Multi-Agent Systems](http://arxiv.org/abs/2611.29107v1)
  <details><summary>📄 Abstract</summary>
  Cache-sharing multi-agent systems can retain every evidence token's representation while preventing cross-worker access during encoding. We test whether this coverage recovers joint-encoding quality using attention masks over two logical workers in frozen Qwen3-4B, Qwen3-8B, and Llama-3.1-8B-Instruct models. Tokens, positions, and answer-time access remain fixed within comparisons. We evaluate 200 two-hop MuSiQue-Ans questions and 200 selected HotpotQA bridge questions. In data-layout seed 0, av...
  </details>

- **2026-11-22** — Jihui Yang, Wentai Wu, Jiahua Huang et al. — [When Does Decomposition Help? Empirical Study on Workload-Architecture Affinity in LLM Inference Serving](http://arxiv.org/abs/2611.29104v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference can be organized as independent monolithic replicas, tensor- or pipeline-parallel serving groups, or disaggregated prefill and decode services. Although decomposition is often presented as a route to higher efficiency, its benefit depends on workload shape, model fit, and whether phase-specific resources can be independently scaled. Existing comparisons frequently change several of these factors at once. We isolate the architectural effect by evaluating five ...
  </details>

- **2026-11-22** — Zhaocong Yang, Jing Yang, Martha-Cary Eppes et al. — [EVis+: Literature-Grounded Visual Analytics for Hypothesis-Driven Geoscientific Data Exploration](http://arxiv.org/abs/2611.29231v1)
  <details><summary>📄 Abstract</summary>
  Scientific researchers often interpret observational data in light of prior findings reported in the scientific literature. However, scientific literature typically remains external to visual analytics environments, requiring researchers to manually connect published findings with the data and hypotheses under investigation. In this paper, we present EVis+, a literature-grounded visual analytics system for condition-event time series analysis in geoscience. EVis+ enhances observational data expl...
  </details>

- **2026-11-22** — Chenyu Wang, Mingyu Chen, Wenchao Li et al. — [Decoupling Perception from Generation for Agentic 3D CT Report Generation](http://arxiv.org/abs/2611.29167v1)
  <details><summary>📄 Abstract</summary>
  Chest CT reports repeatedly assess the same anatomical regions for findings and their attributes, such as whether a lung nodule is present and where it is located. These assessments suggest learning to answer visual questions directly, rather than coupling perception to open-ended text generation. Yet current CT report generation models largely follow generic vision-language modeling, which may miss subtle abnormalities when training data are limited. We therefore formulate report generation as ...
  </details>

- **2026-11-21** — Hao-Yu Hsu, Shenlong Wang, Alexander G. Schwing — [Single-Transformer Latent Diffusion](http://arxiv.org/abs/2611.29064v1)
  <details><summary>📄 Abstract</summary>
  Latent generative models typically rely on three separate networks: an encoder that tokenizes pixels, a generator that models the latent distribution, and a decoder that maps latents back to pixels. UNITE recently merged the first two into a single generative encoder trained in one stage, but its decoder remains a separate network. We ask whether this last network can be folded in too, so that one diffusion transformer encodes, generates, and decodes. Simply letting the shared backbone decode do...
  </details>

- **2026-11-21** — Ayush Khaitan, Liam Fowl, Tomàs Ortega et al. — [Does a Frontier Large Language Model Know What It Can Solve? A 100-Conjecture Calibration Study](http://arxiv.org/abs/2611.28827v1)
  <details><summary>📄 Abstract</summary>
  How does confidence correlate with actual performance in large language models, when attacking open research-level math problems? We address this question by studying the performance of ChatGPT 5.6 Sol Ultra on a set of 100 open conjectures in geometric analysis. By construction, the model first selected open problems in geometric analysis that it assessed that it had at least a 50\% chance of proving or disproving, and then assigned a probability of success to each question. 13 questions were t...
  </details>

- **2026-11-21** — Mingjie Bao, Yu Dai, Guangke Chen et al. — [When Being Wrong Is Right: Reverse-Capability Audio CAPTCHAs through Psychoacoustic Design](http://arxiv.org/abs/2611.28823v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) have recently been shown to bypass audio CAPTCHAs designed around limitations of automatic speech recognition. To address this threat, we introduce reverse-capability verification, a general CAPTCHA framework that reverses the conventional human-easy, machine-hard relationship with respect to the physical ground truth. It selects challenges in which stable human perceptual limitations cause the human-reference answer to differ from the physical ground truth, w...
  </details>

- **2026-11-21** — Tobias Philipp — [Zero-Trust Formal Methods: AI Agents Build Verified Checkers for Untrusted Solvers](http://arxiv.org/abs/2611.28704v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents now generate code faster than humans can review it. Security analyses rely on solver answers such as "unsatisfiable" (for example, no attack path exists) or "optimal." Unlike satisfying models, they cannot be checked by looking at them. Formal verification moves trust from code to specifications, but verifiers still place large SAT, SMT, and answer-set solvers, and the translation into solver queries, in their trusted computing base, and these have had soundness bugs. Unlike age...
  </details>

- **2026-11-21** — Zhaoxuan Tan, Mengting Wan, Jingbo Yang et al. — [Grounding Collaborative Agents in Group Cognition](http://arxiv.org/abs/2611.29036v1)
  <details><summary>📄 Abstract</summary>
  Collaborative agents joining an ongoing team rely on shared context to connect multi-party interaction histories with downstream coordination decisions. Existing work typically focuses either on retrieving historical facts from conversation logs, which surfaces isolated evidence without capturing who knows or owns what, or on evaluating end-to-end interactions, which conflates preparation with execution and lacks direct supervision because a team's history has no single ground-truth summary. To ...
  </details>

- **2026-11-21** — Bangxun Tang, Chen Chen — [XShot: Cross-Shot Video Object Insertion from a Reference Video](http://arxiv.org/abs/2611.28942v1)
  <details><summary>📄 Abstract</summary>
  We present XShot, a framework for cross-shot video object insertion, which adds objects to a shot by watching another shot of the same scene. Video productions show a scene through many shots, and objects added to one shot must appear consistently in the others. Most video editors take the appearance of new objects from reference images and their location from a text prompt, a mask or an edited keyframe, leaving this consistency to the user. XShot reads both from a reference video of another sho...
  </details>

- **2026-11-21** — Shuhao Zheng, Zhipeng Wang, Zi Xuan Zhang et al. — [ActWithin: Bounding Wrong-Payment Risk in Delegated Payment Batches](http://arxiv.org/abs/2611.28941v1)
  <details><summary>📄 Abstract</summary>
  A delegated payment agent can hold valid rights for incompatible revisions of a batch. We study the window in which the selected revision cannot be verified by the execution deadline. For batches that permit every subset of up to q revisions, ActWithin compiles the limit into a shared quota of q successful replacement payments. If approved plans are mutually replayable with the same observable inputs, deadlines, and resources, this quota preserves normal completion without additional approvals a...
  </details>

- **2026-11-21** — Zhuangzhuang Pan, Yan Xia, Kaiwen Lei et al. — [When Rubrics Do Not Decide: Silent Value Completion in LLM Evaluation](http://arxiv.org/abs/2611.28940v1)
  <details><summary>📄 Abstract</summary>
  Multi-criterion LLM judges often evaluate responses without specifying how conflicting criteria resolve, leaving the winner undetermined even under exact criterion scores. Issuing a strict verdict without declaring the required trade-off premise constitutes silent value completion. We introduce TradeoffBench to isolate this failure by separating rule execution from response scoring. On authoritative criterion vectors, six open-weight non-reasoning judges pass all dominance and equality controls ...
  </details>

- **2026-11-21** — Priyadarshini Gokuldass, Saida M. Caballero-Nieves, Alex Carciofi et al. — [Evaluating VLT SPHERE for Probing Diffuse Circumstellar Regions of Evolved Stars](http://arxiv.org/abs/2611.28869v1)
  <details><summary>📄 Abstract</summary>
  Red and Yellow Supergiant stars, generally found in late evolutionary stages with high mass loss, provide test cases for evaluating high-contrast imaging performance. Determining how well adaptive optics combined with coronagraphy isolates faint circumstellar emission allows us to define its true sensitivity limits for evolved stars and refine future high-contrast observing strategies. We conducted a pilot study of seven nearby (within 0.8 kpc), bright (V-band magnitude of 10 or less) evolved re...
  </details>

- **2026-11-21** — Yaowen Zhang, Chen Chen, Wanyu Lin et al. — [Learning free energy across a differentiable temperature range by deep generative modeling](http://arxiv.org/abs/2611.28810v1)
  <details><summary>📄 Abstract</summary>
  Free energy governs the directionality, stability, and temperature sensitivity of physical, chemical, and biological transformations. Conventional free energy calculations, such as thermodynamic integration and free energy perturbation, often have to be performed at individual temperatures and are limited by the high cost of sampling an extensive set of thermodynamic states. Here, we introduce learned temperature-differentiable free energy perturbation (TD-FEP), a deep generative framework that ...
  </details>

- **2026-11-21** — Fabio Valerio Massoli, Arnau Padrés Masdemont, Jordi Ros Giralt et al. — [When do stored facts become available in looped transformers?](http://arxiv.org/abs/2611.28808v1)
  <details><summary>📄 Abstract</summary>
  Looped transformers do not acquire new knowledge during a forward pass. Prior work shows that they store as many bits in their weights as non-looped models. It remains unclear how recurrence makes this knowledge available during inference. We study this question using synthetic factual recall and multi-hop reasoning, measuring depth-resolved readable information in bits with native readouts and tuned lenses. Under final-loop supervision, single-hop facts become readable progressively: heavier me...
  </details>

- **2026-11-21** — Disha Sheshanarayana, Tanishka Magar — [DiscernBench: Evaluating Cooperative Discernment of LLM Agents in Institutional Settings](http://arxiv.org/abs/2611.28787v1)
  <details><summary>📄 Abstract</summary>
  The deployment of large language models in operational settings demands evaluation of judgment under institutional constraint. We introduce DiscernBench, a benchmark for evaluating cooperative discernment: the ability of an agent to determine whether to comply with, refuse, or escalate a request in an institutional setting. DiscernBench comprises scenarios derived from real-world incident reports across domains such as aviation, law enforcement, and emergency management. We evaluate eight LLMs a...
  </details>

- **2026-11-21** — Chen Ma, Yunshu Li, Shuyu Liang et al. — [US-Seg: One Reference for Universal Ultrasound Segmentation](http://arxiv.org/abs/2611.28740v1)
  <details><summary>📄 Abstract</summary>
  Recent ultrasound foundation models have demonstrated strong feature extraction capabilities across organs, tasks, and imaging conditions. However, converting these representations into segmentation still requires finetuning on annotated target data. To reduce reliance on task-specific finetuning, existing universal ultrasound segmentation methods typically adopt prompt-based target specification, mainly through spatial prompts in SAM-style models or task prompts exemplified by MOFO. Yet, direct...
  </details>

- **2026-11-21** — Chendong Xiang, Chengwen Zhang, Ruowen Zhao et al. — [Entangle: Scaling Human-Video In-Context World-Action Models across Unseen Tasks and Contexts](http://arxiv.org/abs/2611.28732v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) enables foundation models to perform unseen tasks from context without parameter updates. In robotic manipulation, a human video provides the context that specifies how a task should be performed. However, scaling human-video ICL on world-action models (WAMs) faces two challenges: task-level human-robot pairs are not temporally aligned with robot actions, and standard action losses allow policies to rely on initial-scene or task-identity shortcuts rather than tracking t...
  </details>

- **2026-11-21** — Zengle Zhu, Zhen Li, Tianyi Huai et al. — [CoopOcc: Cooperative 3D Semantic Occupancy Perception via Multi-Agent and Cross-Modal Fusion](http://arxiv.org/abs/2611.28710v1)
  <details><summary>📄 Abstract</summary>
  Semantic occupancy perception has emerged as a promising paradigm for jointly modeling 3D scene geometry and semantic information. However, this unified representation cannot compensate for missing information caused by occlusion and sensor coverage. Multi-agent cooperation alleviates this limitation, but information from different agents is not equally useful across spatial regions. Meanwhile, feature representations from each agent form the basis of reliable multi-agent fusion. Cross?modal fus...
  </details>

- **2026-11-21** — Chengzhong Wang, Lang Lin, Xinyang Liu et al. — [LoopSeek: Decoupling System One Search from System Two Answering for Long Video Understanding](http://arxiv.org/abs/2611.28635v1)
  <details><summary>📄 Abstract</summary>
  Long video question answering requires finding relevant evidence before reasoning over it. With a limited frame budget, single-pass frame selection can miss critical evidence, while adaptive search often relies on repeated text generation to decide where to look. We introduce LoopSeek, a framework that decouples evidence search from answer generation through a division of labor between a non-thinking System I and a generative System II. Our key insight is that search can be expressed as a sequen...
  </details>

- **2026-11-21** — Davin Hill, Pawan Chorasiya, Bhawani S. Leelar et al. — [BIRD-Persona: A Persona-Aware Benchmark for SQL and pandas Analytics Code Generation](http://arxiv.org/abs/2611.28542v1)
  <details><summary>📄 Abstract</summary>
  Production text-to-code systems use large language models to turn natural-language analytics requests into executable SQL and pandas code. Existing benchmarks cover both tasks but do not isolate when performance diverges between them. We introduce BIRD-Persona, a persona-stratified extension of BIRD-Python that adds novice and expert rewrites to tasks with matched SQL and pandas ground truth, along with schema variants and task-structure annotations. Across 1,534 tasks, nine models, and 245,592 ...
  </details>

- **2026-11-21** — Wonsik Shin, Jinju Jang, Junhoo Lee et al. — [PSC-Gen: Physical Sequence Conditioning for Video Generation via Agentic Visual Planning](http://arxiv.org/abs/2611.28756v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in video diffusion models have enabled the synthesis of high-fidelity, visually compelling videos. However, despite being trained on internet-scale video data, understanding underlying physical laws and generating physically plausible dynamics remain challenging. To mitigate this, conditioning video generators on explicit physical reasoning has emerged as a promising direction. Nevertheless, existing conditioning approaches often fail to incorporate detailed physical guidance int...
  </details>

- **2026-11-21** — Qiwei Wu, Qixuan Li, Xin Xiang et al. — [VTLA-RL: Learning Visuotactile Policies for Load-Adaptive Grasping](http://arxiv.org/abs/2611.28752v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action foundation models learn general manipulation priors, but object mass and local slip are difficult to infer from vision alone. Changing loads require contact-driven grasp adjustments that demonstrations collected under fixed conditions may not adequately cover. We present VTLA-RL to study visuotactile grasping policies and their reinforcement learning (RL) post-training under varying loads. Our main approach shares a visual encoder between tactile-image histories and RGB in...
  </details>

- **2026-11-21** — Mohamed Amine Bergach — [One Million Tokens in 20GB: Calibration-Free 2-Bit SRFT KV-Cache Compression for Looped MoE Inference on Apple Silicon](http://arxiv.org/abs/2611.29092v1)
  <details><summary>📄 Abstract</summary>
  Long-context inference on unified-memory edge machines is governed by KV-cache capacity and memory bandwidth. On a 32 GB Apple M6 Mac mini (26.8 GB Metal working set, 150 GB/s DRAM), the 26.4B looped Mixture-of-Experts model Inkling-2-Mini (48 logical visits, 1M native context) exhausts memory by 64K tokens in stock oMLX (and by 512K even after fixing its 40 sliding-window visits to bounded ring buffers). We show that three structural properties of modern hybrid NoPE architectures -- bounded sli...
  </details>

- **2026-11-21** — Zhaoxuan Tan, Jiachen Zhao, Jingbo Yang et al. — [HyperHarness: Learning to Generate Personalized Agent Harnesses from User Histories](http://arxiv.org/abs/2611.29062v1)
  <details><summary>📄 Abstract</summary>
  Personalized LLM agents rely on an agent harness, the surrounding memory and control code, to connect user history with downstream decisions. Existing methods typically employ either a single shared memory workflow across all users, which is efficient to deploy but cannot adapt how evidence is retrieved and interpreted across diverse histories, or per-user harness optimization, which customizes behavior for each user but requires costly repeated candidate evaluation at deployment and suffers fro...
  </details>

- **2026-11-21** — Zhiling Zhou, Jiachun Pan, Fengzhuo Zhang et al. — [Demystifying Classifier-Free Guidance for Auto-Regressive Image Generation](http://arxiv.org/abs/2611.29002v1)
  <details><summary>📄 Abstract</summary>
  Classifier-free guidance (CFG) has been widely adopted in autoregressive (AR) models for high-quality image generation. Despite its strong empirical performance, its mechanism in AR models remains unclear. This paper demystifies the mechanism of CFG through both empirical and theoretical studies. By examining the top-ranked semantics of different components in CFG, we show that texture information is primarily encoded in the difference between the conditional and unconditional logits, whereas bo...
  </details>

- **2026-11-21** — Anay Sinhal, Amit Sinhal, Arpana Sinhal — [Elicitation format changes zero-shot classification accuracy in a medical vision-language model: a two-center evaluation on colorectal histopathology](http://arxiv.org/abs/2611.28997v1)
  <details><summary>📄 Abstract</summary>
  Background. Verbalized confidence from a hosted medical vision-language model is usually treated as packaging around an unchanged prediction. Methods. We held a nine-class colorectal histopathology prompt fixed except for the requested response format and evaluated MedGemma-27b-it on 10,004 validation and 7,180 external-center PathMNIST patches, with preregistered endpoints, randomized ties, and random floors recomputed for each patch set. Results. Requesting probabilities over all nine classes ...
  </details>

- **2026-11-21** — Md Haseen Akhtar, Hansoo Lee, Rafael A. Calvo — [Health Ikigai: Semantic Conversational Interfaces for Wearable Health Data to Support Behavioral Change for Senior Indian](http://arxiv.org/abs/2611.28883v1)
  <details><summary>📄 Abstract</summary>
  In ubiquitous health contexts, wearable feedback is often encountered in brief, interrupted moments of everyday life. However, many wearable and mobile health systems still present personal health data through numerical dashboards, leaving users and health coaches to interpret trends, thresholds, and deviations on their own. This interpretive burden may be especially relevant for adults aged 50-65 in India, where digital literacy, health literacy, language, and daily routines can shape how healt...
  </details>

- **2026-11-21** — A Adith — [PhyMind: Physics-Informed Masked Autoencoding for EEG Foundation Models](http://arxiv.org/abs/2611.28856v1)
  <details><summary>📄 Abstract</summary>
  EEG foundation models are pre-trained almost exclusively with masked reconstruction through a free-form decoder, sometimes with hand-crafted spectral targets added, as in MANAS-2. We study what happens when that decoder is replaced by a generative forward model of EEG. PhyMind keeps a standard masked transformer encoder, but its decoder must explain the masked signal through 68 cortical regions, each driven by damped stochastic oscillators and an aperiodic Ornstein-Uhlenbeck process, projected t...
  </details>

- **2026-11-21** — Guoming Ling, Shanshan Zhong, Kaixuan Zhang et al. — [Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?](http://arxiv.org/abs/2611.28833v1)
  <details><summary>📄 Abstract</summary>
  Frontier language models can now read and edit the weights of a neural network much like code and thereby improve a small model, an approach known as Weight-Space Programming (WSP). We further explore applying WSP to a language model itself, which we call Self-WSP. Specifically, Qwen3.5-0.8B reads its own weights, proposes an edit, and then continues with the edited weights as both problem solver and editor. We find many cases of genuine self-improvement. Self-edits can raise GSM8K accuracy from...
  </details>

- **2026-11-21** — Fuming Yang, Core Francisco Park — [Pretraining Representation Lottery Determines Fine-tuning Generalization](http://arxiv.org/abs/2611.28777v1)
  <details><summary>📄 Abstract</summary>
  Large scale pretraining (PT) followed by fine-tuning (FT) is the central paradigm of modern deep learning, yet how PT shapes FT generalization remains poorly understood. We use a synthetic setup in which the ground-truth concept geometry of entities is known, as a controlled testbed to study how representational geometry affects model behavior and how PT representations determine FT generalization. We first show that models differing only in training seed can closely match in PT loss yet vary su...
  </details>

- **2026-11-21** — Dmitry S. Grudko, Alexander K. Motovilov — [Feshbach resonances of the second order in a Friedrichs model](http://arxiv.org/abs/2611.28743v1)
  <details><summary>📄 Abstract</summary>
  We consider an extended version of the matrix Friedrichs model that may produce Feshbach resonances of the second order. In this model, under enlarging of the coupling constant, a pair of eigenvalues of the unperturbed Hamiltonian embedded into the continuous spectrum first transforms in resonances of the first order. At some moment later on, these two resonances merge into a single resonance but of the second order, and we fix conditions for this event. Being based on the operator interpretatio...
  </details>

- **2026-11-21** —  KMed Team — [KMed-31B Technical Report](http://arxiv.org/abs/2611.28719v1)
  <details><summary>📄 Abstract</summary>
  We present KMed-31B, a medical large language model post-trained from an open-weight model for on-premises deployment with limited hardware. Post-training a model for diverse medical tasks remains difficult, because improving one kind of task can lower performance on another. We attribute this to differences between tasks in expected output and available feedback. Medical question answering and diagnosis prediction have reference answers, whereas clinical inquiry has no single correct response a...
  </details>

- **2026-11-21** — Haoxuan Xu, Shaoyu Wang, Minghao Lin et al. — [HiPerfCC-KVCache: Accelerating Confidential LLM Serving with Hierarchical KV Caching](http://arxiv.org/abs/2611.28702v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical key-value (KV) caching reduces repeated prefill computation in large language model serving by retaining reusable state beyond GPU memory. Under GPU confidential computing (CC), however, protected transfers can erase this benefit. We show that bulk KV copies hold driver locks during prolonged CPU-side processing, stalling independent serving operations despite separate threads and streams. Our characterization on Hopper and Blackwell GPUs shows how lock scope, copy granularity, and ...
  </details>

- **2026-11-21** — Sarosij Bose, Arindam Dutta, Konstantinos Karydis et al. — [ViewAgent3D: A Training-Free Multi-View Pipeline for 3D Scene Understanding](http://arxiv.org/abs/2611.28673v1)
  <details><summary>📄 Abstract</summary>
  3D scene understanding tasks are often approached by building explicit 3D scene representations or by training specialized multi-modal models over point clouds, voxels, or scene graphs. We take a complementary view: for many queries, the main bottleneck is not the absence of a stronger 3D representation but the selection of a small subset of multi-view RGB views that actually makes the query answerable. We present a training-free, query-conditioned multi-view pipeline that performs diverse tasks...
  </details>

- **2026-11-21** — Hongru Song, Yu-An Liu, Ruqing Zhang et al. — [PROSPER: LLMs as Sparse Retrievers for First-Stage Product Search](http://arxiv.org/abs/2611.28645v1)
  <details><summary>📄 Abstract</summary>
  Product search is a crucial component of large-scale e-commerce platforms, where first-stage retrieval should achieve high recall while ensuring efficient online deployment. Sparse retrieval remains attractive for this setting due to its interpretability and deployability, yet it suffers from severe vocabulary mismatch challenges, especially for short queries and product titles. Large language models (LLMs) offer strong semantic capabilities, but directly applying them to sparse retrieval in pro...
  </details>

- **2026-11-21** — Qingsen Ma, Dianyun Wang, Jiahong Liu et al. — [Make Position Uninformative: Exchangeable Self-Distillation Flattens the Lost-in-the-Middle Curve](http://arxiv.org/abs/2611.28638v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented language models answer well when the relevant document comes first or last and poorly when it sits in the middle. Some fine-tuning recipes lift the middle by lowering the start. We show how training contexts teach positional bias. With a uniform answer slot and shuffled distractors, the optimal reader ignores position. Building on this result, Exchangeable Self-Distillation (ExSD) trains a small adapter on shuffled contexts to reproduce the model's answer when it reads the an...
  </details>

- **2026-11-20** — Arshia Rafieioskouie, Matthew Lucas, Tzu-Han Hsu et al. — [SLICR: Strategy Logic-Guided Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2611.27865v1)
  <details><summary>📄 Abstract</summary>
  Specification-guided reinforcement learning (RL) translates formal specifications of desired behavior of agents into shaped rewards. This paper introduces SLICR, a significant paradigm shift that advances the state of the art to specification-guided RL in adversarial settings under partial observability. We employ Strategy Logic (SL), which allows explicit quantification over agents' strategies and uses the linear temporal logic (LTL) to specify the agents' objectives and constraints. This enabl...
  </details>

- **2026-11-20** — Nathan Nour Houlamy, Mattia Favretto, Earlence Fernandes et al. — [Who Grades the Agent? Privilege Separation for Coding-Agent Benchmarks](http://arxiv.org/abs/2611.27860v1)
  <details><summary>📄 Abstract</summary>
  Benchmarks for AI-based coding agents are a staple of the current AI landscape, because they are the leading way to measure the performance of LLMs. Their scores guide business and research decisions. Evaluating coding agents is challenging, since they are able to manipulate their evaluation infrastructure to artificially achieve better scores. Grading an agent's solution often requires running its code, which can then manipulate the evaluation process. BenchJack, an automated benchmark auditor,...
  </details>

- **2026-11-20** — Huaze Tang, Runqing Miao, Tianren Peng et al. — [SUAF: Spectral Universal Advantage Features for Zero-Shot Policy Improvement](http://arxiv.org/abs/2611.27919v1)
  <details><summary>📄 Abstract</summary>
  Reward-independent representations enable reinforcement learning agents to reuse knowledge across tasks, but limited representation capacity raises three fundamental questions: what statistical dependence should these representations capture, which components of that dependence should be retained for policy improvement, and how does discarding the remaining components affect decision-making? We address these questions through canonical dependence analysis. For a reference policy, we construct an...
  </details>

- **2026-11-20** — JaeSeong Kim, KyungTae Lim — [Functional Depth Is Learned: Isolating the Computation That Layers Produce Only Together](http://arxiv.org/abs/2611.27911v1)
  <details><summary>📄 Abstract</summary>
  Transformer performance scales with depth, but layer count merely counts the opportunities for sequential computation: layers could still behave as nearly independent refinements that barely depend on one another. We study how transformers develop functional depth during pretraining, introducing an exact inclusion-exclusion decomposition that isolates the connected component, i.e., the computation that appears only when a specified set of layers acts together under identity ablation. Tracking th...
  </details>

- **2026-11-20** — Zunhai Su, Keyu Fan, Ruishan Guo et al. — [QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers](http://arxiv.org/abs/2611.27901v1)
  <details><summary>📄 Abstract</summary>
  Streaming visual geometry transformers retain historical key-value (KV) states as cross-view geometric memory, but growing caches constrain long-sequence inference. We systematically characterize KV quantization in streaming geometry and uncover two linked challenges: Nonuniform Geometric Sensitivity and Cache-Geometry Mismatch. Quantization sensitivity varies across precision choices and cache locations, while perturbed retrieval changes geometry-head inputs and propagates through subsequent pr...
  </details>

- **2026-11-20** — Vasco Portilheiro, Samuel Liebana, Andrew Saxe et al. — [Renormalized Entropy from Symmetries: Simplicity Bias and Neural Heat Death](http://arxiv.org/abs/2611.27889v1)
  <details><summary>📄 Abstract</summary>
  Neural networks have parameter symmetries: parameter transformations that do not affect the represented function. How do these symmetries affect the functions that neural networks ultimately learn? We study the implicit bias arising from these symmetries by calculating the equilibrium distribution over represented functions under Langevin dynamics with Gaussian regularization. To isolate the effect of symmetries on this distribution, we study the limit in which the strength of the regularization...
  </details>

- **2026-11-20** — Yuhang Dai, Yinwei Wu, Ziyue Lin et al. — [Non-penetrating World Models](http://arxiv.org/abs/2611.27963v1)
  <details><summary>📄 Abstract</summary>
  We study a new problem of preventing object penetration in interactive video world models. To understand how existing models handle this, we introduce NoPeBench, a benchmark that evaluates how world models respond to physical obstacles. Our evaluation reveals that none of the open-source models can reliably prevent such failures. Surprisingly, however, these models already encode the information needed to predict such violations. We find that the hidden states of diffusion transformers (DiTs) ca...
  </details>

- **2026-11-20** — Chi Yan, Guoyang Zhao, Wentao Yuan et al. — [StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning](http://arxiv.org/abs/2611.27915v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) exhibit strong semantic understanding but remain limited in their ability to reason about metric 3D space in the physical world. Existing VLMs typically infer 3D scene structure from one or more images without known camera calibration or cross-view geometric constraints. This makes metric 3D inference inherently ambiguous and leaves it unclear whether their spatial predictions are grounded in visual evidence or driven primarily by semantic priors. In contrast, calib...
  </details>

- **2026-11-20** — Gerardo Hernandez-del-Valle — [Differential Transmutations and First-Passage Expansions for Monomial Brownian Boundaries](http://arxiv.org/abs/2611.27958v1)
  <details><summary>📄 Abstract</summary>
  Let $P_t=\exp(t\partial_x^2/2)$ be the heat semigroup and let $F(t)=ρt^p$, where $p\ge2$ is an integer. Previous transported-zero theory associates with this boundary a constant-flux solution annihilated by a polynomial-coefficient differential operator of order $2p-1$. We show that the same differential structure contains the complete formal perturbation expansion of the Brownian first-passage density to $F$. For $N=2p-1$ we construct graded spatial operators \[   \mathcal A_r^{(p)}x^n=   \frac...
  </details>

- **2026-11-20** — Aadharsh Kannan, Robert Bruckner, Philip A. Bernstein — [Decision Columns as an Index: Interpretable Embeddings for Explainable Entity Matching and Search](http://arxiv.org/abs/2611.27910v1)
  <details><summary>📄 Abstract</summary>
  Business data systems must determine whether records refer to the same entity and retrieve records satisfying requests whose decisive properties are implicit. As agents act on these records, both tasks require auditable reasons. Dense embeddings perform well but offer opaque coordinates, cannot be filtered by meaning, and require corpus re-encoding to add new properties. We propose interpretable embeddings built from decision columns: each column stores a decision model's calibrated answer to a ...
  </details>

- **2026-11-20** — Zeeshan Shahid, Hammam M. AlGhamdi — [Interpretable Tissue Architecture Complements Pathology Foundation Models](http://arxiv.org/abs/2611.27881v1)
  <details><summary>📄 Abstract</summary>
  Tissue architecture provides important information for histopathological assessment, yet its complementary predictive value alongside pathology foundation-model representations remains insufficiently understood. This study investigates whether interpretable measurements of cellular and multicellular tissue organization provide additional predictive information beyond learned representations. We introduce a 139-dimensional cellular-to-community representation comprising nine feature groups charac...
  </details>

- **2026-11-19** — Yicheng Cai, Taegyu Kim, Peng Liu — [Backtracking Agent Applications Security Incidents](http://arxiv.org/abs/2611.26525v1)
  <details><summary>📄 Abstract</summary>
  Agent applications are increasingly deployed, yet agent-specific attacks pose real threats to them. Upon a security incident, organizations backtrack to identify the CEP (compromise entry point), remediate the damage, and prevent its recurrence. The main artifacts available for backtracking are trajectory logs, which record agent functionalities, and source code; app(lication)-specific function call logs are often fairly limited. However, trajectory logs are at the agent functionality abstractio...
  </details>

- **2026-11-19** — Andrew Kang — [Monte Carlo Pass Search for Setpieces](http://arxiv.org/abs/2611.26464v1)
  <details><summary>📄 Abstract</summary>
  Set pieces produce about a third of non-penalty expected goals (xG), yet they are usually evaluated by what happened next. We present Monte Carlo Pass Search (MCPS) for set pieces, which treats a corner or a lofted free kick as a distribution over plausible executions and plausible futures instead of a single realised event. From the pre-kick state, MCPS proposes counterfactual deliveries and counterfactual set-ups (where the attackers stand at the kick), plays each out many times in a world mod...
  </details>

- **2026-11-19** — Jiawei Xing, Li Wang, Xiangtao Meng et al. — [ChronoPatch: Black-Box Energy-Latency Attacks on Vision-Language Models](http://arxiv.org/abs/2611.26117v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly deployed as generative inference services, where autoregressive decoding makes response length a key determinant of latency and computational cost. This creates an availability risk: adversarial visual inputs can prolong generation and increase serving overhead. Existing energy-latency attacks typically rely on gradients, logits, or token-level feedback, leaving open whether such risks persist when an attacker observes only the final response. We pr...
  </details>

- **2026-11-19** — Qike Zhang, Jiaju Han, Xuelian Shi et al. — [Wearable Logo, Silent Hijack: Stealthy Cross-Modal Semantic Attacks on Visible--Infrared Vision-Language Models](http://arxiv.org/abs/2611.25437v1)
  <details><summary>📄 Abstract</summary>
  Logos appear naturally on clothing and daily necessities, where their recognizable shapes and semantic associations make them familiar visual cues. This familiarity helps them blend into real-world environments and remain visually inconspicuous. We ask whether an existing logo can serve as a carrier for coordinated targeted semantic attacks on visible-infrared (VIS-IR) vision-language models (VLMs) without changing its original outline. This setting requires expressive adversarial variation with...
  </details>

- **2026-11-19** — Ahmet Efe, Recep Bugra Uludag, Ulya R. Karpuzcu — [Verified Netlist-to-RTL Recovery with LLM Agents](http://arxiv.org/abs/2611.25324v1)
  <details><summary>📄 Abstract</summary>
  Gate-level netlists circulate among IP integrators and foundries and can be extracted from chips. Reverse engineering them into readable register-transfer-level (RTL) code would help an adversary understand and modify a design, but remains difficult because word-level operations are scattered across many gates. Large language models (LLMs) can write and optimize RTL, but often fail to recover it from a whole netlist. We propose LOCA (LOgic Cone Attack), an LLM-based attack that divides an anonym...
  </details>

- **2026-11-19** — Tuna Han Salih Meral, Kaan Oktay, Alec Helbling et al. — [RL Post-Training in Diffusion Transformers Is Activation Steering](http://arxiv.org/abs/2611.26627v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) post-training substantially improves the visual quality, text rendering, and compositional accuracy of diffusion transformers. Because capabilities such as rendering requested text or composing multiple objects are inherently prompt-dependent, a natural hypothesis is that improving them requires learning complex, input-dependent transformations. To isolate how much of these gains an input-independent shift explains, we probe each RL-tuned model with a deliberately sim...
  </details>

- **2026-11-19** — Yiyan Ji, Qixun Wang, Yang Shi et al. — [Coda-DaVinci: Reimagining Video Generation with Code2Video](http://arxiv.org/abs/2611.26595v1)
  <details><summary>📄 Abstract</summary>
  Code2Video uses agent-authored 3D proxies to guide video generation, enabling explicit control over structure and dynamics. However, how to construct proxies and prompts for optimal downstream quality remains underexplored, as do the capabilities and limitations of this paradigm. Through controlled experiments and blinded human evaluation, we study proxy granularity, physics simulation, and prompting. The results reveal task-dependent trade-offs: coarse proxies favor natural motion, while medium...
  </details>

- **2026-11-19** — Tanmay Sah — [A CPU Inside an LLM: Zero-Gradient Compilation of Exact Circuits into Pretrained Weights](http://arxiv.org/abs/2611.26450v1)
  <details><summary>📄 Abstract</summary>
  Pretrained language models (LMs) remain unreliable on exact multi-digit arithmetic without gradient fine-tuning or external tool interpreters. We introduce closed-form, zero-gradient circuit-grafting primitives that compile deterministic computation directly into pretrained LM weights using zero training examples and zero runtime hooks, while bounding per-layer normalization drift and preserving natural-language (NL) competence. Our construction combines three analytical mechanisms: (1) two-laye...
  </details>

- **2026-11-19** — Xiaoming Sun, Chengu Wang — [Degree Lower Bounds for Symmetric Boolean Functions: Breaking the Prime-Gap Barrier](http://arxiv.org/abs/2611.26446v1)
  <details><summary>📄 Abstract</summary>
  We prove that every nonconstant symmetric Boolean function on $n$ variables has exact real polynomial degree at least $n-O(n^{1/3}(\log n)^{2/3})$. This makes progress toward the conjecture of von zur Gathen and Roche that the degree is always at least $n-3$. The original prime-gap argument of von zur Gathen and Roche yields a degree deficit of $O(n^{0.525})$ using the theorem of Baker, Harman, and Pintz, or $O(n^{0.52})$ using an estimate claimed in a recent preprint. Our $\widetilde{O}(n^{1/3}...
  </details>

- **2026-11-19** — Xufei Tian, Han Hu, Wenli Du — [Context as a Resource](http://arxiv.org/abs/2611.26346v1)
  <details><summary>📄 Abstract</summary>
  Managing concurrent tasks across separate agent sessions quickly exhausts human attention, motivating always-on personal agents behind a single continuous interface. Yet when every context shares identical frozen backbone weights, funneling interleaved dialogues and external events into one linear session induces cross-topic constraint bleed and head-of-line stalling. Conversely, router-ticket hierarchies incur lossy prose handoffs, heavy routing overhead, and blind merges - collapsing true-conf...
  </details>

- **2026-11-19** — Guojian Zhan, Jiahao Xu, Yahui Liu et al. — [ResVision: Spectrum-Matched Resizing and Context-Preserving Inspection for Visual Reasoning](http://arxiv.org/abs/2611.26318v1)
  <details><summary>📄 Abstract</summary>
  Agentic visual reasoning improves vision-language models by selectively enlarging evidence without adding new scene content, but the benefit depends on whether fine structure remains accessible and whether local observations stay grounded in the full scene. We identify three recurring bottlenecks: high-frequency detail can be attenuated during visual-token formation; spatially distributed evidence can remain encoded yet difficult for the language model to retrieve; and isolated crops can weaken ...
  </details>

- **2026-11-19** — Mehmet Sinan Yıldırım, Ke Zhang, Shuai Wang et al. — [Language-Oriented Semantic Modeling for Target Language Extraction](http://arxiv.org/abs/2611.26317v1)
  <details><summary>📄 Abstract</summary>
  Target Language Extraction (TLE) aims to isolate speech in a target language from multilingual mixtures. Existing approaches primarily rely on acoustic modeling with language identity labels, which provide only coarse categorical guidance. In this work, we propose a language-oriented semantic modeling framework that augments acoustic extraction with language-specific semantic representations. A pre-trained speech semantic model is adapted via language-aware prompt conditioning and parameter-effi...
  </details>

- **2026-11-19** — Daniele Lunghi, Alberick Euraste Djiré, Zacharie Chenail-Larcher et al. — [Static Analysis Guidance for Secure LLM Code Generation](http://arxiv.org/abs/2611.26312v1)
  <details><summary>📄 Abstract</summary>
  Static analyzers are cheap and widely deployed, which makes their reports a candidate feedback signal for secure LLM code generation. Existing approaches place the analyzer inside an iterative repair loop with intermediate steps, which is costly and makes it hard to isolate the report's effect on the model. We introduce two strategies that give the finding to the model during generation. When the analyzer raises an alert, generation is rolled back, and the finding is inserted either as a code co...
  </details>

- **2026-11-19** — Yifan Bai, Yantao Li, Jian Yu et al. — [Paper2Lean: Agentic Autoformalization of Mathematical Research Papers at Scale](http://arxiv.org/abs/2611.26272v1)
  <details><summary>📄 Abstract</summary>
  Formalizing a mathematical research paper requires more than translating isolated theorems: statements and proofs must remain semantically faithful to the source and globally consistent across long-range dependencies. We introduce Paper2Lean, an end-to-end agentic framework that converts mathematical research papers into integrated Lean projects. The framework extracts mathematical content into a dependency graph and coordinates specialized agents for statement formalization, semantic checking a...
  </details>

- **2026-11-19** — Tianyi Xu, Boyang Lyu, Yunkai Tang et al. — [StreamEgo: Streaming Exocentric-to-Egocentric Video Generation](http://arxiv.org/abs/2611.26165v1)
  <details><summary>📄 Abstract</summary>
  Exocentric-to-egocentric (Exo2Ego) video generation transforms third-person recordings into first-person viewpoints, unlocking immersive AR/VR experiences and scalable demonstration synthesis for embodied robotics. Extending it to a streaming setting is expected to further enable live applications. However, existing methods suffer from degraded manipulation regions, overfitting and confinement to fixed-length clips with prohibitive latency. To address these limitations, we present StreamEgo, a r...
  </details>

- **2026-11-19** — Frederike Oetker, Charlotte Geertman — [Public-Private Cooperation in the Port of Rotterdam: An Agent-Based Toy Model of Cooperative Efforts Against Cocaine Trafficking](http://arxiv.org/abs/2611.26154v1)
  <details><summary>📄 Abstract</summary>
  Cocaine trafficking poses a persistent governance challenge in the Port of Rotterdam (PoR), requiring cooperation between public and private actors. This paper develops an Agent-Based toy Model (ABM) coupled with a Causal Loop Diagram (CLD) to explore interactions between trust, cooperation, competition, pressure, enforcement, and actor skills in public-private cooperation (PPC). Based on empirical data of PPC in the PoR, we explore responses to parameter shocks across different initial configur...
  </details>

- **2026-11-19** — Yuqi Guo, Michael Wray — [Better Retrieval, Not Better Binding: Pretraining Exposure in Egocentric Video Retrieval](http://arxiv.org/abs/2611.26120v1)
  <details><summary>📄 Abstract</summary>
  Video-language models (VLMs) achieve strong performance on video-text retrieval and are increasingly used for egocentric video understanding. Yet, despite gains in zero-shot retrieval, they have shown limitations in compositional understanding, and it remains unclear whether they understand compositional relationships between verbs and nouns. In this work, we introduce Ego-ExBind, a compositional diagnostic protocol for analyzing pretraining exposure and verb-noun binding in egocentric video-tex...
  </details>

- **2026-11-19** — Jiahao Hu, Jingdong Du, Yichen Zhang et al. — [HiUni: Harmonizing Understanding and Generation in Shared Visual Space](http://arxiv.org/abs/2611.26107v1)
  <details><summary>📄 Abstract</summary>
  Unified multimodal models aim to support visual understanding and generation within a single framework. However, prevailing approaches often separate their visual representations or backbone computation to accommodate the different requirements of these two tasks, which limits the degree of unification. In this paper, we present HiUni, which revisits this design choice and explores whether a pretrained vision language model can be directly extended into a unified model with extensive parameter s...
  </details>

- **2026-11-19** — Yuxiang Wang, Junhao Gan, Jianzhong Qi — [SheetAlign: Grounded Interaction and Stage-Isolated Learning for Spreadsheet Agents](http://arxiv.org/abs/2611.26069v1)
  <details><summary>📄 Abstract</summary>
  Spreadsheets are widely used for data analysis and supporting decision-making. Automating spreadsheet analysis while protecting sensitive data and controlling deployment costs motivates locally deployed open-weight large language models (LLMs). Meanwhile, complex spreadsheet tasks require both task reasoning and workbook understanding, while predefined operation interfaces impose additional tool-selection and invocation demands. We introduce SheetAlign, a spreadsheet manipulation framework with ...
  </details>

- **2026-11-19** — Lu Ying, Can Liu, Yuxiao Yang et al. — [Presenting Your Figures: Data-informed Animated Transitions Across Scientific Figure Panels](http://arxiv.org/abs/2611.26036v1)
  <details><summary>📄 Abstract</summary>
  Multi-panel figures are commonly used in research papers to show scientific data, and researchers often reuse them when presenting their work. Presenting these figures often involves explaining how data across chart panels are related. Animated transitions can progressively reveal these relationships, but two static panels specify only the endpoints, leaving what intermediate keyframes should show and how the transition should progress unclear. To support transition design across diverse scienti...
  </details>

- **2026-11-19** — Emre Uğur, Jiawen Qi, Qinyu Chen — [DTS: Delta-Based Tile Scoring for Efficient Long-Context Sparse Attention](http://arxiv.org/abs/2611.25938v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly need to process long documents and codebases, making long-context attention a major prefill bottleneck. Block sparse attention reduces computation by skipping unimportant blocks of the attention matrix, but scoring blocks accurately can itself be expensive. We propose Delta-Based Tile Scoring (DTS), a training-free, content-adaptive tile scoring method for sparse block attention. DTS selects query and key anchors according to local vector changes, using ...
  </details>

- **2026-11-19** — Muhammad Rafid, Golshan Famitafreshi, Vasilis Avgerinos et al. — [Coordinated Offloading: Cooperative Multi-Agent Reinforcement Learning for the Edge-Cloud Continuum](http://arxiv.org/abs/2611.25932v1)
  <details><summary>📄 Abstract</summary>
  The increasing demand for intelligent, low-latency services in edge-cloud continuum systems poses new challenges for dynamic and efficient task offloading. We propose a Multi-Agent Reinforcement Learning (MARL) framework for distributed task offloading under partial observability, where each device offloads only a portion of its computation to a target edge server while executing the remaining portion locally (partial offloading). The problem is formulated as a Markov Decision Process (MDP), whe...
  </details>

- **2026-11-19** — Yutong Guan, Meixing Shi, Haoran Sun et al. — [EvoMem: Self-Evolving Skills for Time-Aware Long Video Memory Agents](http://arxiv.org/abs/2611.25889v1)
  <details><summary>📄 Abstract</summary>
  Although memory-augmented architectures have expanded the ability of large vision-language models (LVLMs) to process long videos, existing retrieval processes still largely rely on global semantic matching and lack state-driven temporal control, often returning fragmented or redundant evidence and failing to maintain a coherent evidence chain. To address this challenge, we propose EvoMem, a time-aware long-video memory agent guided by self-evolving retrieval skills. EvoMem constructs a hierarchi...
  </details>

- **2026-11-19** — Ziyang Xu, Peng Han, Hai Zhou — [From Sequence to Space: Explicit Spatial Belief with Vision-Language Distillation for Active Geo-Localization](http://arxiv.org/abs/2611.25866v1)
  <details><summary>📄 Abstract</summary>
  Active geo-localization (AGL) asks an agent to navigate a small aerial search grid and reach a target specified by an aerial image, a ground-level photograph, or text. Existing methods align the goal modalities well, but they keep the navigation state inside a large sequential Transformer and train with a dense distance reward that uses the hidden goal location. This paper proposes EAGLE, an Explicit spatial-belief Agent for Geo-Localization and Exploration. Offline training jointly optimizes a ...
  </details>

- **2026-11-19** — Pangjing Wu, Xu Yuan, Wenqi Fan et al. — [LINEAGE: A Benchmark for Empirical Lineage Retrieval in AI Scientific Literature](http://arxiv.org/abs/2611.25845v1)
  <details><summary>📄 Abstract</summary>
  Current research agents are moving beyond academic search toward literature synthesis and experiment planning. These workflows increasingly rely on literature retrieval systems, which serve as standalone systems or as components of research agents. However, existing scientific literature retrieval benchmarks mainly evaluate these methods using topical relevance or citation links as supervision, which cannot capture which prior methods are used for empirical comparison. To address this gap, we in...
  </details>

- **2026-11-19** — Hui Cai, Kangcheng Deng, Tianyi Ma et al. — [Auto-Alpha: A Framework for Autonomous Factor Research](http://arxiv.org/abs/2611.25732v1)
  <details><summary>📄 Abstract</summary>
  Autonomous factor research requires generating economic hypotheses as well as implementing and testing them. We present Auto-Alpha, a framework that connects report-guided initialization to self-directed research through a test-driven implementation loop. An idea agent proposes economic mechanisms and signal constructions; a research agent develops them with backtest feedback. Semantic audit, quantitative review, and human admission select factors for a persistent library, while an Experience Li...
  </details>

- **2026-11-19** — Yanjing Li, Sheng Xu, Baochang Zhang et al. — [Efficient Latent Reasoning for Vision-Language Model via Dynamics-Aware Quantization and Distillation](http://arxiv.org/abs/2611.25670v1)
  <details><summary>📄 Abstract</summary>
  Efficient chain-of-thought (CoT) reasoning in vision-language models (VLMs) requires reducing both intermediate reasoning steps and their execution cost. Latent CoT methods compress textual rationales into continuous thoughts, yet their full-precision (FP) models retain substantial storage and computation costs. Lowering numerical precision could reduce these remaining costs, yet direct quantization severely degrades reasoning accuracy, particularly with 4-bit weights and activations. Operator a...
  </details>

- **2026-11-19** — Jingyi Zhou, Yi Liu, Bin Sun et al. — [GRODE-RTL: Source-Mapped Dependency Views for LLM-Based RTL Repair](http://arxiv.org/abs/2611.25661v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models show great potential for automated Register-Transfer Level repair, yet they struggle with non-local faults where root causes and failing outputs reside far apart in source code. Treating RTL as a flat token sequence obscures hardware dataflows, whereas exposing complete synthesized graphs overwhelms the model with fine-grained metadata. To resolve this representation dilemma, we propose GRODE-RTL, an anchor-centric representation that extracts the single-clock-stage fan-in ...
  </details>

- **2026-11-19** — Jinpeng Lu, Haoyuan Shi, Yuanshen Guan et al. — [CaT-Movie: Balancing Global Planning and Local Rendering for Long Multi-Shot Video Generation](http://arxiv.org/abs/2611.25620v1)
  <details><summary>📄 Abstract</summary>
  Current multi-shot video generators render only limited durations per pass, requiring long movies to be stitched from local segments across which narrative progression and visual identity drift. To synthesize long-horizon movies with Coherence across Time, we present CaT-Movie, a multi-shot generation system consisting of a global story planner and a local window renderer. The planner expands user requests via a large language model to preserve, infer, and complete story details, while determini...
  </details>

- **2026-11-19** — Seungho Song, Donggyu Lee, Jaehan Kim et al. — [Measuring Hallucination in Large Language Models for Cyber Threat Intelligence: An Exploratory Study](http://arxiv.org/abs/2611.25590v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in cyber threat intelligence (CTI) tasks, such as summarization and question answering. However, they may produce hallucinations, false or misleading content not grounded in the source text, which can mislead analysts and corrupt downstream security decisions. This paper presents an exploratory measurement study of hallucinations in LLM-based CTI. We introduce HalluVision, a reproducible framework that generates LLM outputs, extracts domain-spec...
  </details>

- **2026-11-19** — Taeoh Hong — [AZOWL AgentOps: Task-Scoped Governance for Deployed Agent Applications](http://arxiv.org/abs/2611.25562v1)
  <details><summary>📄 Abstract</summary>
  AZOWL AgentOps provides shared governance for deploying agents and delegating work to them. Human and agent senders can exchange messages or explicitly delegate a business task. Accepted work has a stable identifier that links the sender's authority, the assigned runner, any required approval, and result evidence. The default enrolled customer PC profile is read-only. We compare AZOWL components with a configured LangGraph application in 28 synthetic runs across four paired pilots. Original AZOW...
  </details>

- **2026-11-19** — Semin Kim, Ju Yeon Kang, Sunghwan Ahn et al. — [Joint Language Modeling for In-the-Wild Speech-Scene Generation with Distinct Token Representations](http://arxiv.org/abs/2611.25503v1)
  <details><summary>📄 Abstract</summary>
  Speech-scene generation aims to synthesize intelligible target speech together with diverse environmental sounds as a coherent acoustic scene. The task is considered challenging in two respects. Speech and environmental audio differ substantially in their semantic and acoustic characteristics, yet existing approaches typically model the complete scene using a single mixed acoustic representation. At the same time, the two sounds are closely related in real-world speech scenes, whereas convention...
  </details>

- **2026-11-19** — Xin Zhang, Tujie Xu, Zhiyi Chen et al. — [VisualTalk-Bench: Evaluating Question-Driven Avatar-Led Video Explanations](http://arxiv.org/abs/2611.25444v1)
  <details><summary>📄 Abstract</summary>
  Advances in video generation and avatar synthesis enable new ways to answer user questions through visual explanations. This task requires a system to formulate a correct answer, translate relevant information into visual material, and deliver the explanation through an avatar's speech and actions. Existing benchmarks rarely assess whether avatars point to the visual content being discussed. We introduce VisualTalk-Bench for question-driven avatar-led video explanations in finance and Chinese an...
  </details>

- **2026-11-19** — Ferran Hermida-Rivera, Jack Toubes, Angela Cui et al. — [BOOMerang: Autonomous Translation from RTL to Microarchitectural Simulators and Back](http://arxiv.org/abs/2611.25438v1)
  <details><summary>📄 Abstract</summary>
  High-level simulators like gem5 are often used to test and demonstrate novel architectural techniques. While these simulators provide high research productivity, they generally lack the means to provide detailed feedback on the realizability of a hardware design. Furthermore, these simulators can frequently fall out-of-sync with the detailed performance characteristics of real hardware designs, which is usually the responsibility of dedicated engineers/teams in industry. While RTL implementation...
  </details>

- **2026-11-19** — Ben Kang, Junda Wang, Yuxuan Yuan et al. — [DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal Embeddings](http://arxiv.org/abs/2611.25419v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models have greatly improved input understanding in universal multimodal embedding models. However, this understanding does not ensure that their embeddings preserve the evidence needed to distinguish relevant items from confusable alternatives. To preserve essential discriminative evidence in embeddings, this paper proposes DiLE, a discrimination-aware latent-space learning framework that combines task guidance with on-policy retrieval feedback. Specifically, a few lea...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 729 |
| prompt-injection | 704 |
| memory-poisoning | 59 |
| tool-use-attack | 179 |
| backdoor | 569 |
| adversarial-attack | 679 |
| privacy-leakage | 4663 |
| steganography | 94 |
| misuse | 1351 |
| red-teaming | 158 |
| vulnerability | 4136 |
| defense | 4079 |
| alignment | 3823 |
| robustness | 4190 |
| watermark | 806 |
| unlearning | 126 |
| agent-safety | 67 |
| benchmark | 77 |
| survey | 468 |
| other | 11548 |

---

📚 **全部 38505 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-24 16:52:23*