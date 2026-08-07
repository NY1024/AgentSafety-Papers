<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-22470-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-07 03:06 ｜ **论文总数 / Total Papers**: 22470（近 30 天 / Recent 30 days: 2329）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 22470 篇论文（含摘要、分类筛选、搜索）/ View all 22470 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 562
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 473
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 43
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 96
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 407
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 548
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3765
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 55
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 853
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 112
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2568
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2248
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2082
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2039
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 238
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 85
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 55
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 266
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5923

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2329 篇，完整 22470 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2329 papers from the last 30 days (with date, authors & abstract). For the full list of 22470 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 2 papers

- **2026-08-04** — Hujian Zhu, Yihao Huang, Felix Juefei-Xu et al. — [ICO: Enhancing Semantic-Shift Jailbreaks via Iterative Context Optimization](http://arxiv.org/abs/2608.03210v1)
  <details><summary>📄 Abstract</summary>
  Foundation models have achieved remarkable success across diverse tasks, but they remain vulnerable. To investigate such vulnerabilities, semantic-shift jailbreaks have recently emerged as a promising attack paradigm. They bypass explicit safety mechanisms by replacing harmful terms in original harmful questions with benign alternatives and leveraging contextual information to induce the target model to reinterpret these alternatives as their corresponding harmful concepts. However, existing sem...
  </details>

- **2026-08-04** — Jasper Timm, Lukas Struppek, Ziwei Xu et al. — [AI Security Leaderboard: Methodology, Results and Minimal Standard](http://arxiv.org/abs/2608.03070v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI model developers increasingly rely on layered safeguards to prevent catastrophic misuse, but little public evidence exists on how much protection these safeguards provide, or how consistently across developers. We introduce the FAR.AI Minimal Standard for Safeguards, Version 1.0: a taxonomy of 67 readily accessible static jailbreak techniques, a method for composing them into a very large attack space, and a benchmark of flagship models against a sample of it. We evaluate Claude Fabl...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

- **2026-08-05** — Yanting Wang, Chenlong Yin, Runpeng Geng et al. — [Agent Against Agent: An Agentic System for Automatic Prompt Injection Red Teaming](http://arxiv.org/abs/2608.05108v1)
  <details><summary>📄 Abstract</summary>
  Prompt injection poses significant security risks to LLM agents. Efficient and effective red-teaming is therefore critical, both for evaluating these risks and for collecting training data to improve defenses. Existing state-of-the-art prompt injection red-teaming methods primarily rely on reinforcement learning (RL), producing attacker models that often generalize poorly to new target LLMs. In this work, we develop PIMiner, an agentic system for prompt injection red-teaming. During training, PI...
  </details>

- **2026-08-05** — Longtao Guo, Zelin Zhang, Kaifeng Huang et al. — [LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents](http://arxiv.org/abs/2608.04741v1)
  <details><summary>📄 Abstract</summary>
  LLM-based web agents automate user tasks by observing webpages and executing browser actions on behalf of users. As these agents operate on real web services, login becomes a sensitive authentication boundary because it involves credentials and sensitive information. Existing work shows that malicious webpage content can manipulate web agent actions, but it has not fully examined whether such content can induce login and cause end-to-end private data leakage. We study this attack surface and pre...
  </details>

- **2026-08-05** — Xuebin Li, Hanqing Zhao, Siyuan Liang et al. — [Breadcrumbing Search Agents](http://arxiv.org/abs/2608.04565v1)
  <details><summary>📄 Abstract</summary>
  LLM-based search agents are widely used for information-seeking tasks, but their reliance on external tool returns introduces a critical security risk: web content retrieved during execution is untrusted, exposing agents to prompt injection and goal hijacking. Prior work on search-agent safety primarily focuses on static web-content injection, but modern agents issue follow-up queries and cross-check competing sources, so a single injected page is often diluted or rejected. We show that the chan...
  </details>

- **2026-08-04** — Peichun Hua, Haoxuan Xu, Mengyuan Li — [Behavioral Skill Reconstruction: Reconstructing Hidden Functionality from LLM Agent Skills](http://arxiv.org/abs/2608.04192v1)
  <details><summary>📄 Abstract</summary>
  Closed source agent skills may encode proprietary instructions, scripts, constants, and data. Providers may offer their capabilities as services while keeping the underlying packages hidden. Prior work focuses on prompt injection attacks that directly disclose these artifacts, and existing defenses accordingly aim to prevent such leakage. However, preventing file disclosure does not prevent users from recovering the functionality those files implement. This raises a fundamental question: can a u...
  </details>

- **2026-08-04** — Narendra Kumar Dewangan, Mounira Msahli — [An Inline Control Architecture for Language Models in Intelligent Transportation Systems](http://arxiv.org/abs/2608.04065v1)
  <details><summary>📄 Abstract</summary>
  Vehicle-to-everything (V2X) systems increasingly incorporate large language models (LLMs) for semantic tasks such as message summarization, operator assistance, and decision support at roadside units and edge nodes. Although these components are not part of safety-critical control loops, they introduce prompt-level attack surfaces that are not addressed by traditional V2X security mechanisms focused on authentication and message integrity. This paper presents Guarded-V2X, an inline semantic guar...
  </details>

- **2026-08-04** — Shihao Weng, Yang Feng, Xiaofei Xie et al. — [AgentAntibody: An Adaptive Immune System for Defending LLM Agents against Prompt Injection](http://arxiv.org/abs/2608.04053v1)
  <details><summary>📄 Abstract</summary>
  Prompt injection remains a critical threat to LLM agents, yet existing defenses treat each task as a self-contained problem, independent of previous encounters. In practice, user requests are often underspecified: they describe the desired outcome without fully specifying acceptable behavior. An injection can exploit this ambiguity, causing the agent to complete the task in a way the user would reject. As the user's expectations become clearer through concrete cases, a defense should learn from ...
  </details>

- **2026-08-03** — Jia-Chen Zhang, Ze-Yu Zhang, Kai-Wei Zhang — [Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents](http://arxiv.org/abs/2608.02018v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs), which empower large language models to autonomously operate operating systems and the web, are increasingly vulnerable to indirect prompt injection attacks. A widely adopted defense is the human-in-the-loop paradigm, in which the agent pauses for explicit user confirmation before executing sensitive operations. While effective against conspicuously high-harm attacks, this defense offers little protection against what we term Invisible Ink Threats: low-harm injected go...
  </details>

- **2026-08-03** — Qianlong Yang, Bowen Ye, Xianda Guo et al. — [Mitigating Visual Degradation in MLLMs via Spatial-Spectral Visual Anchor Learning](http://arxiv.org/abs/2608.01635v1)
  <details><summary>📄 Abstract</summary>
  Despite the progress of multimodal large language models (MLLMs), they continue to exhibit deficiencies in visual perception. Following visual instruction tuning, internal MLLM representations rapidly deviate from their original semantic states during inference, causing severe information degradation. While existing methods attempt to leverage external vision foundation models (VFMs) to align internal representations, we find that direct alignment with VFMs enhances visual semantics but fails to...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 4 papers

- **2026-08-04** — Jiaming Chen, Yisen Gao, Yanping Li et al. — [MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents](http://arxiv.org/abs/2608.03844v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented LLM agents rely on rich context for long-horizon reasoning and acting, yet their memory modules expose a persistent attack surface for malicious records, making the study of memory poisoning threats imperative. However, existing query-only attacks often fail to remain effective in two realistic and prevalent settings: large-scale benign memory pools and active input auditing. Consequently, current approaches fall short when facing the dual challenges of high retrieval competitiv...
  </details>

- **2026-08-04** — Zonghao Ying, Xiangfan Wu, Huiyu Wu et al. — [SkillJack: Persistent Skill Backdoors in Self-Evolving Agents](http://arxiv.org/abs/2608.03509v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents increasingly convert interaction histories into reusable skills that persist beyond individual tasks. While prior work studies memory and retrieval poisoning, such attacks only affect agents when poisoned records are retrieved as context. We uncover a new and more fundamental risk: poisoned experiences can be transformed by the agent itself into durable behavioral artifacts. We present \textbf{SkillJack}, the first attack that exploits the experience-to-skill pipeline of sel...
  </details>

- **2026-08-03** — Bingyu Yan, Xiaoming Zhang, Chaozhuo Li et al. — [Benign Alone, Harmful Together: Exploiting Experience Composition in Self-Evolving LLM Agents](http://arxiv.org/abs/2608.01759v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving large language model agents improve their capabilities by distilling interaction trajectories into persistent experiences. Yet this mechanism introduces a new safety risk: experiences that are benign in isolation may jointly weaken an agent's safety boundary when accumulated and reused across sessions. Existing memory attacks typically require direct memory access or induce explicitly malicious records, limiting their stealthiness and applicability. We propose EvoBreak, an experien...
  </details>

- **2026-08-03** — Zheng Lin, Yuzhe Huang, Zhenxing Niu et al. — [Salami Attack: Stealthy Collusive Memory Poisoning against OpenClaw](http://arxiv.org/abs/2608.01637v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory enables LLM agents to retain useful information across sessions, but also creates an attack surface through which adversaries may poison an agent's persistent memory to steer its behavior. Existing memory poisoning attacks mainly rely on individually malicious records, overlooking a compositional threat: multiple benign-looking memories may jointly induce unsafe behavior. In this paper, we introduce MemCollusion, an automated red-teaming framework for constructing collusive memo...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-08-04** — Nizhang Li, Zonghao Ying, Xiangfan Wu et al. — [SkillSentry: Adaptive Honey Worlds for Dynamic Safety Testing of Agent Skills](http://arxiv.org/abs/2608.03485v1)
  <details><summary>📄 Abstract</summary>
  External skills extend the capabilities of large language model agents, but also introduce an execution-time attack surface: a skill that appears benign under inspection may reveal harmful behavior only after particular environmental states, resources, or interaction histories are encountered. Existing scanners primarily rely on static analysis, predefined rules, or one-shot semantic judgments, making such conditional behavior difficult to elicit and attribute. We present SkillSentry, a dynamic ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 9 papers

- **2026-08-05** — Azizi Ariffin, Afif Haris, Faiz Zaki et al. — [Adaptive Intrusion Detection System using Transformer-Based Neural Networks and Continual Learning Approach with Adversarial Investigation](http://arxiv.org/abs/2608.04602v1)
  <details><summary>📄 Abstract</summary>
  Network intrusion detection systems (IDS) trained on fixed traffic snapshots decay silently after deployment as threat distributions shift. Fine-tuning models on new attacks triggers catastrophic forgetting, while retraining from scratch is computationally infeasible. Replay-based continual learning counters this, but existing methods unrealistically confine benign traffic to a single early task and ignore the replay buffer as a potential attack surface. To address this, we present an adaptive I...
  </details>

- **2026-08-05** — Zhaoqi Wang, Daqing He, Zijian Zhang et al. — [Combating Knowledge Corruption in Agent Systems: A Byzantine-Tolerant Secure Collaborative RAG Framework](http://arxiv.org/abs/2608.04366v1)
  <details><summary>📄 Abstract</summary>
  While retrieval-augmented generation systems partially address the hallucination issues in large language models, it also introduces new vulnerabilities to knowledge corruption attacks. Adversaries exploit these vulnerabilities by poisoning documents provided by RAG system to manipulate LLM outputs. To counter this threat, we propose SecureCollaRAG, a Byzantine-tolerant collaborative RAG framework leveraging Multi-source Knowledge Validation Mechanism. Our approach enables agent system to secure...
  </details>

- **2026-08-04** — Omatharv Bharat Vaidya, Connor Thomas Jerzak, Zayne Rea Sprague et al. — [When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K Causal Reasoning in LLMs](http://arxiv.org/abs/2608.03506v1)
  <details><summary>📄 Abstract</summary>
  Self-consistency assumes the most frequent answer among sampled reasoning traces is the most reliable, but this can fail in causal reasoning: samples often repeat the same confounding error, and votes fragment across multiple valid answers, letting an invalid answer win despite a valid minority trace. We introduce CALVER (Causal Axiom-Level VERification), a training-free symbolic verifier that scores structured traces against Pearl's causal criteria, including -separation, backdoor adjustment, a...
  </details>

- **2026-08-04** — Jian Zhao, Shenao Wang, Qingyang Wu et al. — [MalTotal: Cost-Effective and Language-Agnostic Malicious Code Poisoning Detection for Millions of Repositories](http://arxiv.org/abs/2608.03232v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of open source software (OSS) has introduced significant security risks, with malicious code poisoning attacks increasingly targeting public package registries and open-source platforms. Existing detection approaches, including heuristic-, learning-, and LLM-based methods, suffer from language-specific designs, limited generalization, and high analysis costs, making them unsuitable for large-scale multi-language analysis. To address these challenges, we propose MalTotal, ...
  </details>

- **2026-08-04** — Yuhan You, Suhas Adavelly, Victoria Lovelace et al. — [Tiny Enough to Break In: Agentic Remote Access Trojans Powered by Small Language Models](http://arxiv.org/abs/2608.03009v1)
  <details><summary>📄 Abstract</summary>
  Agentic artificial intelligence raises a new security concern: cyber threats that reason, act, and adapt locally without continuous human direction. We examine this threat through an Agentic Remote Access Trojan (agentic RAT): a Remote Access Trojan augmented with a locally deployed Small Language Model (SLM). The SLM interprets host and network observations, selects actions, recovers from failed steps, and reduces reliance on an external operator. We implement the concept in a controlled, netwo...
  </details>

- **2026-08-03** — Walid Saidi — [MutMem: Cryptographically Authorized Mutation in Persistent Agent Memory](http://arxiv.org/abs/2608.02843v1)
  <details><summary>📄 Abstract</summary>
  Persistent agent memory must adapt as later outcomes change earlier evidence, yet mutable retrieval weights create an attribution problem: reviewers must distinguish authorized adaptation from database tampering. We present MutMem, an authorized-mutation protocol in HOM-AIMOS, a persistent agent-memory engine. MutMem retains memory content, records signed positive and negative outcome evidence without age-based expiry, and commits each nontrivial weight change as a housekeeper-authorized transit...
  </details>

- **2026-08-03** — Giorgio Severi, Shujaat Mirza, Blake Bullwinkel et al. — [Evading Chain-of-Thought Monitoring Through Model Poisoning](http://arxiv.org/abs/2608.02820v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring is an increasingly important component of AI safety stacks but relies on the assumption that a model's reasoning trace is informative about its actions. This work studies the limits of CoT monitoring through the lens of model poisoning. We demonstrate that backdoors can be implanted into reasoning models to elicit an attacker-chosen behavior while their CoT traces appear entirely benign. We find that these CoT-Hidden backdoors can be induced through simple fine-...
  </details>

- **2026-08-03** — Leonid Ravich, Michael Fire — [Stylometric Defenses Against Author Impersonation in Software Repositories](http://arxiv.org/abs/2608.02695v1)
  <details><summary>📄 Abstract</summary>
  Software supply-chain attacks increasingly exploit an identity gap where compromised maintainer accounts authorize malicious changes. This work evaluates patch-level authorship verification as a behavioral defense layer, showing that stylometric analysis can operate not only on full source files but also on patch-level commits. We fine-tune a cross-modal transformer on more than 20 years of Linux kernel commit history to embed code diffs and commit messages into a unified stylometric space, achi...
  </details>

- **2026-08-03** — Nicola Pitzalis, Donald Shenaj, Giacomo Cignoni et al. — [Z-PEFT: Zero-shot Backdoor Detection in Parameter-Efficient Fine-Tuning via Canonical Spectral Signatures](http://arxiv.org/abs/2608.02271v1)
  <details><summary>📄 Abstract</summary>
  Parameter-Efficient Fine-tuned (PEFT) models are frequently downloaded from open repositories by practitioners. This widespread practice creates a significant attack surface, as malicious actors can publish backdoored models that induce specific behaviors in response to predefined triggers. We study the problem of weight-space backdoor detection, where a detector classifier predicts whether a model is malicious using only its weights, enabling a lightweight safety mechanism. Most existing method...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 8 papers

- **2026-08-05** — Chongbiao Wang, Daniel Gaa, Joachim Weickert et al. — [The Neural Echo: A Signal Processing Perspective for Understanding Neural Networks](http://arxiv.org/abs/2608.04864v1)
  <details><summary>📄 Abstract</summary>
  We introduce the neural echo as a tool for understanding the behavior of neural networks. It generalizes the model-based concepts of impulse responses, diffusion echoes, and filter echoes to learning-based methods. It provides local, space-adaptive impulse responses and filter kernels for a neural network, its so-called echoes. These echoes depend on the input image and can be visualized to understand the learned dynamics of the network via an affine mapping. Neural echoes build a bridge from cl...
  </details>

- **2026-08-05** — Anadi Goyal, Nandish Chattopadhyay, Chandan Karfa et al. — [MOAT: Model-Agnostic Randomized Transformations for preventing Efficiency Degradation Attacks on ViTs](http://arxiv.org/abs/2608.04680v1)
  <details><summary>📄 Abstract</summary>
  To adopt the Vision Transformers (ViTs) in resource-constrained environment, token pruning is widely used to reduce computational cost without impacting accuracy. However, adversaries have developed targeted attacks against said token pruning techniques to undermine such attempts to make ViTs efficient. In this paper, we propose MOAT, a model-agnostic pre-processing defense pipeline that applies a combination of input transformations to protect efficient ViT implementations against adversarial e...
  </details>

- **2026-08-05** — Tianyi Wang, Zhenghao Gao, Shengjie Xu — [Season: Spectrum-Aware Orthogonal Gradient Refinement for Transfer-Based Adversarial Attacks](http://arxiv.org/abs/2608.04441v1)
  <details><summary>📄 Abstract</summary>
  Transfer-based adversarial attacks often transfer poorly across heterogeneous architectures because CNNs favor local textures while Vision Transformers (ViTs) rely on global shapes. We propose Season, a spectrum-aware orthogonal gradient refinement framework for L-infinity transfer attacks against black-box target models on ImageNet, using a white-box surrogate. Season decomposes each update into a low-frequency branch capturing structural cues and a high-frequency branch capturing textures. A l...
  </details>

- **2026-08-05** — Jiaming Zhang, Boyang Chen, Zherui Li et al. — [Adversarial Attacks for Good: A Survey of Proactive Protection across the Visual Content Lifecycle](http://arxiv.org/abs/2608.04314v1)
  <details><summary>📄 Abstract</summary>
  Once visual content enters an AI pipeline, its owner often retains little technical control over how it is used. Legal and regulatory remedies can address misuse, but many technical interventions must be applied earlier, when content is released or accessed. This survey examines the protective paradigm that has grown around this intervention point, which we call \emph{adversarial attacks for good}. Perturbations and structured signals long studied as attacks on learned models are instead applied...
  </details>

- **2026-08-04** — Atri Vivek Sharma, Brian Formento, Alessio Lomuscio — [Eliciting Intrinsic Hallucinations in LLMs via Semantically Equivalent Adversarial Attacks](http://arxiv.org/abs/2608.04286v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are often used in conjunction with external knowledge sources to improve their factual accuracy and decrease hallucinations, through methods such as Retrieval-Augmented Generation (RAG). However, these systems remain susceptible to intrinsic hallucinations, where the model generates unfaithful or fabricated information that is not supported by the retrieved evidence. We propose a novel framework to assess model robustness against this phenomenon by stress-testing usi...
  </details>

- **2026-08-04** — Bangjie Sun, Nayoung Kim, Mun Choon Chan et al. — [Double Down on Defense: Strengthening Deep Perceptual Hashes against Evasion Attacks without Retraining](http://arxiv.org/abs/2608.03101v1)
  <details><summary>📄 Abstract</summary>
  Near-duplicate image matching is crucial for trust and safety, provenance verification, copyright enforcement, and large-scale visual search. Modern platforms increasingly rely on deep perceptual hashes, which map visually similar images to nearby representations despite common image transformations. However, adversarial perturbations can cause near-duplicates to evade matching. We present DualShield, a plug-in defense that improves the robustness of existing deep perceptual hashes without retra...
  </details>

- **2026-08-03** — Nan Chen, Zhouhao Yang, Soufiane Hayou — [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](http://arxiv.org/abs/2608.02415v1)
  <details><summary>📄 Abstract</summary>
  Intent classification in Large Language Models (LLMs) involves categorizing user prompts into predefined classes. For instance, given a user prompt, the system must determine whether it primarily concerns mathematics, coding, or general text processing. Such classification enables routing prompts to specialized models optimized for specific domains, improving both accuracy and computational efficiency. In this work, we conduct a systematic study comparing training-free vs training-based approach...
  </details>

- **2026-08-03** — Xuanhui Lin, Junhao Dong, Mingrong Gong et al. — [Two Sides of the Same Coin: Co-Evolving Search for Cross-Task Attacks on Vision-Language Models](http://arxiv.org/abs/2608.02137v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) exhibit strong generalization across multimodal tasks but remain vulnerable to adversarial perturbations. Existing attacks typically follow single-trajectory gradient optimization or task-specific objectives, limiting search-space exploration and cross-task transferability. We propose an evolutionary-computation-guided cross-modal attack framework for unified VLMs. The framework adaptively searches both textual and visual spaces. On the textual side, it evolves hard...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 34 papers

- **2026-08-05** — Yangfan Jiang, Fei Wei, Ergute Bao et al. — [Private Direct Preference Optimization for LLM Alignment](http://arxiv.org/abs/2608.05040v1)
  <details><summary>📄 Abstract</summary>
  Direct preference optimization (DPO) is now a standard method for aligning large language models (LLMs) using human preference data. Each DPO example contains a prompt and a pair of candidate model responses. While prompts and responses are often public or model-generated, the relative preference between responses reflects subjective judgments and can reveal sensitive attributes of annotators or end users. Off-the-shelf privacy-preserving approaches are not well matched to this structure, leadin...
  </details>

- **2026-08-05** — Zhongjiang Yao, Shuangshuang Liang, Chun Yang et al. — [When Do PEFT Adaptations Leak Structure? Measuring Black-Box Structural Bounds in Public-Base Model Services](http://arxiv.org/abs/2608.05036v1)
  <details><summary>📄 Abstract</summary>
  Services increasingly deploy public foundation models with private parameter-efficient adaptations, creating a differential information leakage risk when auditors or adversaries can execute the public base model locally and observe victim outputs. We present VectorHijack-SR, a measurement methodology that converts paired victim/base residuals into calibrated structural bounds over PEFT family, layer locality, and coarse rank, while separating metadata visibility from open-world validity and oper...
  </details>

- **2026-08-05** — Haoting Qian, Qingjie Zhang, Zhicong Huang et al. — [Leak-Resistant Unlearning: A New Benchmark for Evaluating Multi-Hop Reasoning Consistency and Recovery Robustness](http://arxiv.org/abs/2608.04519v1)
  <details><summary>📄 Abstract</summary>
  Benchmarking machine unlearning methods is critical to understand whether sensitive knowledge is removed from large language models (LLMs) or not. Current unlearning benchmarks include mainly single-hop questions and a narrow set of multi-hop questions. Although effective, they still face two challenges. (1) Knowledge is not isolated, whereby diverse multi-hop reasoning paths can potentially induce knowledge leakage than normal queries. (2) Unlearning may be fragile: unlearned knowledge can be p...
  </details>

- **2026-08-05** — Guotao Yang, Mingxi Zhao, Haopeng Li et al. — [RAC: Reference-Aware Activation Compression for Communication-Efficient Split LLM Inference](http://arxiv.org/abs/2608.04991v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents repeatedly process long, privacy-sensitive contexts, while cloud-only deployment exposes user data beyond the trusted endpoint and fully local deployment often requires costly hardware. Split inference offers a middle ground by executing the model head, tail, and tools locally and the middle layers in the cloud, but its local-cloud-local path transfers boundary hidden states at every invocation and creates a critical communication bottleneck. We present \system,...
  </details>

- **2026-08-05** — Bo Wang, Yuqian Yao, Enxi Wang et al. — [ContextWeave: A Real-World Workflow Benchmark](http://arxiv.org/abs/2608.04830v1)
  <details><summary>📄 Abstract</summary>
  Memory is essential as language agents move from isolated tasks to long-horizon, stateful workflows, yet existing evaluations often reduce it to retrieval or question answering. We introduce ContextWeave, a longitudinal benchmark that evaluates whether recalled experience improves downstream agent performance in realistic office-work streams. ContextWeave reconstructs privacy-preserved, multi-month workflows of 14 participants into 1,005 executable tasks, including 568 core evaluation tasks, wit...
  </details>

- **2026-08-05** — Chenyu Wang, Yi Liu, Baoqing Li et al. — [Guideline-as-Oracle: Zero-Annotation Training of an Ophthalmic Telephone Triage Agent](http://arxiv.org/abs/2608.04772v1)
  <details><summary>📄 Abstract</summary>
  Scaling supervision for multi-turn medical agents is difficult because expert dialogue annotation is costly and clinical conversations are privacy-restricted. We introduce Guideline-as-Oracle (GAO), which compiles American Academy of Ophthalmology guidance into a 70-row operational rule table and uses it as the sole source of instance-level supervision for 3,000 training dialogues, reserving human labeling for evaluation. Because converting rules into dialogues is itself a design problem, we cat...
  </details>

- **2026-08-05** — Dongsheng Chen, Yuxuan Li, Guanhua Chen et al. — ["Allow" to Achieve, Over-Privileged Inadvertently: The Unintended Cost of Task-Completion-Driven Pop-up Decisions in Mobile GUI Agents](http://arxiv.org/abs/2608.04755v1)
  <details><summary>📄 Abstract</summary>
  Mobile GUI agents routinely encounter system permission dialogs during task execution, yet their ability to grant only permissions that are necessary for the delegated task remains largely unexamined. We present a systematic study of this capability, which we term Permission Literacy. We construct a four-level permission framework based on task relevance and privacy risk and validate the evaluated scenarios with three independent experts in GUI-agent safety. We inject Android-style permission po...
  </details>

- **2026-08-05** — Liehuang Zhu, Yuhang Li, Tianxing Wang et al. — [Blockchain Empowered Trustworthy Agent Networks: Foundations, Taxonomy, and Future Directions](http://arxiv.org/abs/2608.04626v1)
  <details><summary>📄 Abstract</summary>
  AI agents are evolving from isolated task executors into networked autonomous entities that can communicate, delegate tasks, invoke tools, access external knowledge, and participate in cross-platform service and economic workflows. This evolution gives rise to open agent networks, where heterogeneous agents owned by different stakeholders interact without naturally shared infrastructures for identity, authorization, auditability, reputation, or settlement. This survey and tutorial article review...
  </details>

- **2026-08-05** — Junjie Xiong, Zhengyuan Jiang, Xiaoran Xu et al. — [Large Language Models and Social Media Information Integrity: Opportunities, Challenges, and Research Directions](http://arxiv.org/abs/2608.04375v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have emerged as powerful tools that impact information integrity on social media platforms. This comprehensive review examines the dual role of LLMs in both facilitating and mitigating various information integrity challenges, including misinformation, disinformation, fake news, social bots, and privacy concerns. \textcolor{black}{We conduct a comprehensive review of the literature from 2019 to 2024, screening 1048 studies and performing an in-depth analysis of 215 r...
  </details>

- **2026-08-05** — Simon Lösche, Barış Büyüktaş, Mathis Adler et al. — [On the Effectiveness of Adaptation Strategies for VLM-Based Federated Learning in Remote Sensing](http://arxiv.org/abs/2608.04791v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) enables collaborative training of deep learning models across decentralized image archives without requiring data centralization. This paradigm is particularly relevant in remote sensing (RS), where legal regulations, privacy concerns, and bandwidth constraints restrict data sharing. However, the presence of training data heterogeneity across clients (known as non-IID data) can impede convergence and limit the generalization capability of the aggregated global model. To m...
  </details>

- **2026-08-05** — Bo Li, Junjie Peng, Xiaohua Xie et al. — [COSMO: Consensus-Driven Shift Modulation for Source-Free Domain Adaptation](http://arxiv.org/abs/2608.04604v1)
  <details><summary>📄 Abstract</summary>
  Source-free domain adaptation (SFDA) adapts a source-trained model to an unlabeled target domain without source data, a practical setting under privacy or storage constraints. Yet its self-generated supervision can reinforce source bias under substantial domain shifts. Pretrained vision-language models (VLMs) offer complementary semantic knowledge, but the relative reliability of the source model and VLM varies across target samples. Existing cross-model guidance does not explicitly account for ...
  </details>

- **2026-08-04** — Hao Zhou, Shengming Yuan, Yuhang Wang et al. — [Scale-CDA: A Scalable Prototype to Democratize AI-Assisted Cooperative Driving Automation (CDA) for Production Cars](http://arxiv.org/abs/2608.04235v1)
  <details><summary>📄 Abstract</summary>
  This study presents Scale-CDA, an open-hardware/open-software tool-chain that democratizes a functional version of Generative-AI-assisted Cooperative Driving Automation (CDA). Built on the community-maintained OpenDBC interface (300+ car models) and Openpilot Level-2 ADAS, Scale-CDA achieves plug-and-play retrofitting with off-the-shelf parts that cost under US \$1,000 (edge PC, webcam, CAN adapter, optional LTE/Wi-Fi radios). A lightweight Vehicle-to-Everything (V2X) stack using MQTT over Wi-Fi...
  </details>

- **2026-08-04** — Duo Zhang, Zhehui Yin, Zhiyun Yao et al. — [Teaching Foundation Models to Read mmWave: Pose-Guided Kinematic Representation for Human Behavior Understanding](http://arxiv.org/abs/2608.04127v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents need to perceive human behavior in physical environments. Millimeter-wave (mmWave) radar provides a privacy-friendly and contactless sensing modality, but radar observations are difficult to align with language. Existing radar-language methods often rely on synthetic data or lack explicit supervision for human body structure and motion. We present mmMind, a radar-language model that uses synchronized 3D pose as training-only supervision. A spatio-temporal radar encode...
  </details>

- **2026-08-04** — Boyao Wang, Zhihan Lei — [SpecDrop: Parameter-Free Category-Conditioned Routing for Modular Specialization](http://arxiv.org/abs/2608.04084v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-experts (MoE) networks pursue specialization through learned routers, gates, and load-balancing losses, yet at matched total-parameter budgets learned routers can underperform equal-weight No-Routing baselines. Is the bottleneck the routing algorithm, or the alignment between training-signal granularity and the target categories? We probe the question with SpecDrop, a fixed parameter-free routing scheme: each of $K$ branches receives weight $p_a$ for its assigned category and a small ...
  </details>

- **2026-08-04** — Yuyang Xia, Ruixuan Liu, Li Xiong — [PriDyG: Privacy-preserving Dynamic Graph Inference with LLM-GNN Collaboration](http://arxiv.org/abs/2608.04255v1)
  <details><summary>📄 Abstract</summary>
  Graph inference over relational data can expose sensitive edge information, and this risk becomes more severe in dynamic graphs, where repeated model updates cause privacy loss to accumulate. We formulate Edge-level Differentially Private Dynamic Graph Inference (EDG) and propose PriDyG, a private inference framework that combines GNN-based structural learning with LLM-based semantic reasoning. PriDyG introduces incremental private multi-hop aggregation, which buffers newly arrived edges and pro...
  </details>

- **2026-08-04** — Corey Lammie, Hadjer Benmeziane, William Andrew Simon et al. — [On Design Principles for Efficient Heterogeneous DRAM-PIM-GPU Systems](http://arxiv.org/abs/2608.04169v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous DRAM-based processing-in-memory (PIM)-GPU systems promise significant efficiency gains for decode-phase large language model (LLM) inference, particularly in long-output generation, yet current design practices overlook critical factors that determine real-world performance. Through systematic evaluation of diverse architectures and workloads (OPT-7B/70B, Mamba2-2.7B/70B), we reveal three fundamental design principles: (i) static power consumption (DRAM leakage, refresh, and GPU id...
  </details>

- **2026-08-04** — Aditya Rane, Amit Choudhari, Shashi Kant et al. — [Discrete-Time Survival Analysis for Heart Failure Mortality Prediction](http://arxiv.org/abs/2608.04140v1)
  <details><summary>📄 Abstract</summary>
  Accurate heart-failure prognosis relies on tracking clinical risk over time, yet many machine-learning applications mishandle right-censored survival data by either discarding a patient's observation time or using it as a predictor. Discarding time ignores survival context, while using follow-up time as an input feature introduces severe target leakage that inflates apparent accuracy. We address this by proposing a discrete-time person-period framework for heart-failure mortality classification....
  </details>

- **2026-08-04** — Zhenran Wang, Zhonghan Bian, Jinsong Li et al. — [WorldCup Arena: Prospective, Leakage-Free Evaluation of Frontier LLMs on a Live Tournament](http://arxiv.org/abs/2608.04008v1)
  <details><summary>📄 Abstract</summary>
  Benchmarks that measure the forecasting ability of large language models are almost always retrospective: the event has happened, the answer is somewhere on the Web, and the evaluation must defend itself against memorisation. We report the opposite design. Over the 39 days of the 2026 FIFA World Cup, six frontier LLMs -- all with extended thinking and native server-side web search -- were asked before every kickoff, one match at a time, to fill in a seven-market prediction card for all 104 match...
  </details>

- **2026-08-04** — Zhen Fang, Yu Zeng, Wenxuan Huang et al. — [Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent](http://arxiv.org/abs/2608.03979v1)
  <details><summary>📄 Abstract</summary>
  We introduce Video-DeepResearch (Video-DR), extending multimodal agents from static images to continuous video streams, a setting that demands dense spatiotemporal grounding coupled with open-web exploration. Preliminary evaluations reveal two critical bottlenecks in current models: (1) modality bias, where agents bypass visual tools in favor of textual search, and (2) parametric knowledge leakage, where models rely on internal memory rather than genuine tool-augmented execution. To address thes...
  </details>

- **2026-08-04** — Prince Zizhuang Wang, Aojie Yuan, Haiyue Zhang et al. — [WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaboration and Security in Human-Centered Agent Networks](http://arxiv.org/abs/2608.03499v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in persistent personal-agent frameworks are making human-centered agent networks realistic deployment targets: each user can be served by an AI agent that acts on the user's behalf, maintains state, and communicates with other agents through social and task relations. In these networks, everyday tool use becomes multi-party owned-agent collaboration over personal workspaces, where files, records, tools, and policies are not directly visible across owners. Existing agent benchmark...
  </details>

- **2026-08-04** — Jong Wook Kim, Byoungjae Min, Kennedy Edemacu et al. — [DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents](http://arxiv.org/abs/2608.03130v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory enables persistent personalization in LLM agents, but repeated memory-conditioned responses can cumulatively reveal protected attributes even when they are never stated explicitly. We formalize this threat as adaptive transcript privacy and introduce DP-MemView, a differentially private interface that privately selects public response-conditioning views and exposes those views---rather than raw memory---to the response LLM. Each private selection is charged to every protected at...
  </details>

- **2026-08-04** — Yongli Xiang, Zhifang Zhang, Bojun Yang et al. — [When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills](http://arxiv.org/abs/2608.03700v1)
  <details><summary>📄 Abstract</summary>
  Persona skills distill personal interaction histories into portable and executable artifacts for downstream agents. While enabling flexible personalization, this process concentrates fragmented personal signals, amplifies their impact through reuse, and challenges defenses designed for individual records or retrieval-based memory. To systematically investigate the safety of the persona-skill pipeline, we introduce AntiSkillBench, an end-to-end benchmark for evaluating risks and defenses across t...
  </details>

- **2026-08-04** — Ye-Xin Lu, Xin Wang, Yang Ai et al. — [Towards Real-world Environment-aware Zero-shot Text-to-speech Synthesis via Disentangled Audio Infilling](http://arxiv.org/abs/2608.03011v1)
  <details><summary>📄 Abstract</summary>
  Recent zero-shot text-to-speech (TTS) systems achieve remarkable naturalness and speaker similarity but typically require high-quality speaker prompts and either strip away or entangle the acoustic environment with speaker characteristics, limiting their real-world applicability. We present an extended DAIEN-TTS, an environment-aware zero-shot TTS framework that disentangles and jointly models speech, background noise, and reverberation, enabling independent control over timbre and acoustic envi...
  </details>

- **2026-08-04** — Zeyu Zhang, Bradly C. Stadie — [Temporal Leakage in LLM Backtesting: Measurement, Validation, and Adjusted Scores](http://arxiv.org/abs/2608.02985v1)
  <details><summary>📄 Abstract</summary>
  The standard check for contamination in LLM backtests is simple: compare scores before and after the training cutoff. We show this check is uninformative. Four flagship models fail it on questions they cannot have memorized: every scored question resolved after their cutoffs. The reason is structural. Models legitimately know more about times near their cutoff, so recency mimics leakage, and we prove no passive backtest can separate the two from genuine skill. Measurement, not just detection, re...
  </details>

- **2026-08-04** — Jian Zhang, Bingyi Wang, Yizhi Liu — [CausalOPD: First-Wrong-Step Supervision for Distilling Causal Chain Reasoning](http://arxiv.org/abs/2608.03673v1)
  <details><summary>📄 Abstract</summary>
  Many critical reasoning tasks, including clinical diagnosis, legal judgment, and industrial fault diagnosis, require step-dependent causal chains in which early errors propagate and correct conclusions can mask invalid reasoning. Although large language models perform well on such tasks, privacy, latency, and controllability motivate distillation into locally deployable models. Standard trajectory imitation does not correct process errors on the student's own rollout distribution. We propose Cau...
  </details>

- **2026-08-04** — Amirhossein Taleshinosrati, Yangyang Wang, Atitaya Phoemsuk et al. — [FOUND-AF: Benchmarking ECG Foundation Models for Atrial Fibrillation Detection](http://arxiv.org/abs/2608.03597v1)
  <details><summary>📄 Abstract</summary>
  Atrial fibrillation (AF) is the most common sustained cardiac arrhythmia and is associated with increased risks of stroke, heart failure, and mortality. Recent ECG foundation models offer transferable representations for automated AF detection. However, their relative effectiveness remains unclear because existing studies use different datasets, preprocessing procedures, classifiers, and validation protocols. This study presents FOUND-AF, a unified, leakage-controlled, and deployment-oriented be...
  </details>

- **2026-08-04** — Lele Zheng, Weifeng Kong, Xinyi Zhang et al. — [Noise-Aware Shrinkage for Differentially Private Zeroth-Order Fine-Tuning of Large Language Models](http://arxiv.org/abs/2608.03277v1)
  <details><summary>📄 Abstract</summary>
  Differentially private zeroth-order optimization (DP-ZO) enables memory-efficient private fine-tuning of large language models using only forward evaluations. Existing aggregation-based DP-ZO methods reconstruct model updates at a fixed scale, ignoring that the strength of useful signals varies throughout training. Consequently, noise-dominated updates may receive excessive weight and degrade model utility. To address this issue, we propose SAGE, a noise-aware shrinkage method that adaptively at...
  </details>

- **2026-08-04** — Lele Zheng, Ruijie Hu, Tao Zhang et al. — [FedGSA: Geometry-Consistent Subspace Aggregation for Differentially Private Federated LoRA](http://arxiv.org/abs/2608.03267v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) enables communication-efficient federated fine-tuning of pretrained language models. However, integrating differential privacy (DP) into federated LoRA remains challenging: independently perturbing and aggregating its two low-rank matrices can cause aggregation mismatch and the quadratic noise term. Existing methods mitigate these issues by freezing one low-rank matrix but still rely on Euclidean aggregation, which is basis-dependent and may distort the global update. ...
  </details>

- **2026-08-03** — Shadab Bin Habib, A K M Ferdous Reza Habib, Subarno Neel et al. — [Aligned in Form, Not in Meaning: The Comprehension - Containment Decoupling of LLM Safety in Low-Resource Bangla Derogatory Speech](http://arxiv.org/abs/2608.02941v1)
  <details><summary>📄 Abstract</summary>
  We audit five frontier large language models on native Bangla derogatory speech (gali) across six protocols to test a single hypothesis: Comprehension-Containment Decoupling. We propose that contemporary safety alignment is bound to high-resource surface forms rather than harmful meaning, causing a model's capacity to comprehend a low-resource slur and its capacity to contain it to operate independently. Every protocol corroborates this hypothesis against a human-calibrated baseline (kappa = 0.8...
  </details>

- **2026-08-03** — Sleem Abdelghafar, Gabriel Kulp — [Privacy-Preserving AI Verification via Minimal Information Disclosure](http://arxiv.org/abs/2608.02774v1)
  <details><summary>📄 Abstract</summary>
  AI verification crosses a trust boundary: a verifier must learn enough to establish an authorized claim, yet the same evidence can reveal sensitive details about the model, workload, or hardware. We introduce minimal information disclosure (MID), which designs and quantifies the information content of verifier-facing evidence itself. MID measures collateral leakage with conditional mutual information: what the release reveals about the protected property after the authorized result is known. MID...
  </details>

- **2026-08-03** — Vincenzo Longo, Alberto Verna, Nikhil Jha et al. — [Lost in Permissions: Exploring the Microsoft 365 App Ecosystem](http://arxiv.org/abs/2608.02336v1)
  <details><summary>📄 Abstract</summary>
  The Microsoft 365 (M365) ecosystem hosts thousands of third-party applications that integrate with enterprise tenants via fine-grained OAuth permissions, potentially granting access to sensitive organisational resources such as emails, files, calendars, chats, and user directories. Despite the security implications of these permission grants, the M365 ecosystem has not been systematically studied.   We present the first privacy- and security-oriented measurement of M365 third-party applications....
  </details>

- **2026-08-03** — Zirui Huang, Yunlong Mao, Wei Tong et al. — [Auditing Data Provenance in LLM Fine-tuning via Intrinsic Distributional Fingerprints](http://arxiv.org/abs/2608.02154v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of customized Large Language Models (LLMs) poses critical risks of Data Intellectual Property (Data IP) infringement via unauthorized fine-tuning on proprietary data. Existing audit techniques are limited, as they require intervention during data preparation or training and remain fragile under malicious obfuscations such as data paraphrasing and knowledge distillation.   We propose \textit{Distribution Provenance Audit (DPA)}, a post-hoc framework for auditing data IP infringe...
  </details>

- **2026-08-03** — Mohamed ElBassat, Seifeldin Elkerdany, Mohamed ElBialy et al. — [Calibrated Similarity and Graph Clustering for Open-Set Animal Re-Identification](http://arxiv.org/abs/2608.02469v1)
  <details><summary>📄 Abstract</summary>
  AnimalCLEF26 addresses discovery-oriented animal re-identification, where systems must both attach query images to known individuals and discover unseen individuals by clustering them correctly. We present a similarity-to-clustering pipeline for this setting across Eurasian lynx, fire salamander, loggerhead sea turtle, and Texas horned lizard images. The method first isolates the target specimen using segmentation and then applies lightweight species-specific preprocessing for lynx, sea turtle, ...
  </details>

- **2026-08-03** — Abdullah Mamun, Shovito Barua Soumma, Hassan Ghasemzadeh — [Trustworthy AI in Digital Health: A Comprehensive Review of Robustness and Explainability](http://arxiv.org/abs/2608.02238v1)
  <details><summary>📄 Abstract</summary>
  Ensuring trust in AI systems is essential for the safe and ethical integration of machine learning systems into high-stakes domains such as digital health. Key dimensions, including robustness, explainability, fairness, accountability, and privacy, need to be addressed throughout the AI lifecycle, from problem formulation and data collection to model deployment and human interaction. While various contributions address different aspects of trustworthy AI, a focused synthesis on robustness and ex...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-08-03** — Mohamed Chahine Ghanem — [Steganalysis of Adaptive Covert Collusion in Tool-Using Agent Populations: A Black-Box, Cross-Principal Approach](http://arxiv.org/abs/2608.02698v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents built on large language models (LLMs) are increasingly deployed not by a single operator but by many, side by side on shared infrastructure. This creates a population-level risk that single-agent safeguards miss: a handful of agents can quietly coordinate, rigging a market, boosting one another in a review process, or timing a joint data grab, while each one looks perfectly well-behaved. The difficulty is that the organisations running these agents cannot see inside one another...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 11 papers

- **2026-08-05** — Yuxuan Huang, Xingyu Zeng, Tianhang Zheng et al. — [Gradient Immunity: Null-Space Resistance to Malicious Fine-Tuning](http://arxiv.org/abs/2608.05045v1)
  <details><summary>📄 Abstract</summary>
  Released aligned large language models remain vulnerable to malicious downstream finetuning. Existing defenses are largely designed for the fine-tuning-as-a-service (FTaaS) paradigm or rely on downstream users to follow additional safety procedures, and therefore do not directly address the setting we study: a provider controlled partially protected open-weight (PPOW) release setting in which most weights remain trainable while a small safety-critical component is preserved at release. We propos...
  </details>

- **2026-08-05** — Yibo Hu, Jiaming Qu — [Social Pressure Breaks Majority Voting in LLM Safety Panels](http://arxiv.org/abs/2608.04415v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to detect unsafe content. A common approach is to combine judgments from a panel of models to correct individual mistakes, but this benefit may disappear when every model sees the same misleading context before voting. We study this risk in a controlled two-round experiment. Each model first judges an item alone, then judges it again after six simulated peers either assert the wrong label or abstain. We combine the final judgments by majority vo...
  </details>

- **2026-08-04** — Chunlin Liu, Junnian Chen, Haitong Jiang et al. — [Does Forgetting Transfer Across Modalities? A Real-World Benchmark for Cross-Modal Knowledge Unlearning Evaluation](http://arxiv.org/abs/2608.03791v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs), like Large Language Models (LLMs), may memorize sensitive, copyrighted, or harmful knowledge from their pretraining corpora. Removing such knowledge is essential for building trustworthy AI systems. However, existing studies primarily focus on forgetting within individual modalities. Although recent work has begun to explore cross-modal consistency in unlearning, the cross-modal transfer of real-world knowledge unlearning remains insufficiently studied. To address ...
  </details>

- **2026-08-04** — Yantong Liu, Zheyu Zhang, Runpeng Liu et al. — [TumorBoard: Evidence-Grounded Multi-Agent Decision Support for Longitudinal Neuro-Oncology](http://arxiv.org/abs/2608.03190v1)
  <details><summary>📄 Abstract</summary>
  Neuro-oncology decisions require coordinated interpretation of serial MRI, pathology, molecular markers, treatment history, performance status, and evolving guidelines. We present TumorBoard, a multi-agent decision-support system built around a shared longitudinal case state and an auditable claim-evidence ledger. Specialist agents for radiology, neuropathology, molecular diagnosis, guidelines, and therapy planning produce atomic claims with provenance. An adversarial critic exposes contradictio...
  </details>

- **2026-08-04** — Yu Feng, Chunting Zang, Chen Shen et al. — [When Refusal Looks Safe: The Refusal-Cue Shortcut in Safety Guard Models](http://arxiv.org/abs/2608.03201v1)
  <details><summary>📄 Abstract</summary>
  Safety guards are widely used to filter harmful content and are typically trained via supervised fine-tuning on labeled prompt-response pairs. We audit two widely used safety-guard training datasets, WildGuardMix and GR-Train, and find that among responses to harmful prompts, refusal expressions co-occur almost exclusively with unharmful labels. This imbalance motivates what we term the refusal-cue shortcut: inserting a refusal cue into a harmful response could flip the guard's verdict from harm...
  </details>

- **2026-08-04** — Guilin Li, Jiaxing Zhang, Matthias Hwai Yong Tan et al. — [SeqLLM: Augmenting LLMs with Behavioral-Sequence Modeling for High-Stakes Decisions at WeChat Pay](http://arxiv.org/abs/2608.03063v1)
  <details><summary>📄 Abstract</summary>
  Merchant risk control at large payment platforms screens tens of millions of merchants daily, where false positives harm legitimate merchants and false negatives leave harmful activity undetected. The hardest cases require jointly understanding a merchant's textual profile and long behavioral sequence. Large language models (LLMs) excel at text but cannot natively model such sequences, while adapting them often causes catastrophic forgetting. We present SeqLLM, a framework that adds behavioral-s...
  </details>

- **2026-08-03** — Kihyun Kim, Hee-Seon Kim, Wonjun Lee et al. — [Safety in Batches? Understanding and Mitigating Safety Failures in Batch Prompting](http://arxiv.org/abs/2608.02681v1)
  <details><summary>📄 Abstract</summary>
  Batch prompting is a practical inference strategy for large language models, but its safety implications remain underexplored. We show that the success of batch prompting for utility does not extend to safety: a harmful question that is reliably refused in isolation can elicit a harmful response when embedded in a batch of benign questions. We identify this as a distinct safety failure mode, not reducible to known vulnerabilities such as in-context learning or long-context effects, and analyze i...
  </details>

- **2026-08-03** — Shu Quan, Tianfang Hao, Sitong Fang et al. — [A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models](http://arxiv.org/abs/2608.02684v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are accelerating biological research, yet this same capability poses a critical biosecurity threat: models that assist in protein engineering can equally be prompted to generate predicted toxin-like sequences, potentially lowering the barrier to biological misuse. Current safety evaluations, however, operate in natural language and cannot determine whether a model-generated amino acid sequence is biological gibberish or a computational risk signal. To address this ev...
  </details>

- **2026-08-03** — Natalie Isak, Matthew Dressman — [Magnet: Detecting Cross-Session AI Misuse Through Capability Accumulation](http://arxiv.org/abs/2608.02518v1)
  <details><summary>📄 Abstract</summary>
  The most capable AI deployments are not single models but ensembles of specialized agents that delegate and act in coordination. This architecture unlocks powerful new capabilities, and it also introduces risks that existing frameworks for monitoring, detection, and mitigation were not designed to address. Most state-of-the-art AI abuse detection literature focuses on single-turn or multi-turn (single-session) threat models. This leaves a critical gap: an attacker can decompose a harmful goal in...
  </details>

- **2026-08-03** — Giovanni Pizzenti, Alberto Verna, Nikhil Jha et al. — [TrainShield: Targeted Awareness for Cybersecurity Training](http://arxiv.org/abs/2608.02296v1)
  <details><summary>📄 Abstract</summary>
  In recent years, cybersecurity threats have increasingly exploited human behaviour rather than purely technical vulnerabilities, exposing the limits of traditional awareness programmes delivered outside real-world contexts. To bridge this gap, we introduce TrainShield, an interaction paradigm for contextual cybersecurity training that embeds adaptive learning interventions directly within user workflows. The system integrates real-time risk detection (e.g., phishing and data loss prevention) wit...
  </details>

- **2026-08-03** — Junyeong Park, Jieun Han, Haneul Yoo et al. — [EduZone: A Framework for Evaluating LLM Safety for K-12 Students and Teachers](http://arxiv.org/abs/2608.02024v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used across diverse tasks in K-12 education, yet existing safety evaluations rarely examine how harmful or inappropriate content appears in interactions between LLMs and students or teachers. To address this, we present EduZone, an evaluation framework for LLM safety across diverse educational scenarios. Our framework systematically combines (1) student- and teacher-facing LLM usage contexts, (2) fine-grained curriculum concepts, and (3) 6 risk categ...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-08-05** — Ryozo Masukawa, Ian Bryant, Armita Kazeminajafabadi et al. — [Trident : How to Break Deep Reinforcement Learning Cyber Defenses (Agentic)](http://arxiv.org/abs/2608.04317v1)
  <details><summary>📄 Abstract</summary>
  Autonomous cyber defense systems based on Deep Reinforcement Learning (DRL) have attracted significant research attention, yet remain evaluated almost exclusively against static, heuristic red agents, leaving their robustness against adaptive threats critically understudied. Meanwhile, recent advances in Reinforcement Learning with Verifiable Rewards (RLVR) have improved LLM reasoning, but their integration into cybersecurity remains elusive due to the absence of suitable benchmark environments ...
  </details>

- **2026-08-04** — Hadi Mohammadi, Tina Shahedi, Robert A. Bagheri et al. — [Learning Sexism Detection Using Multi-Agent Perspectivist Preference Optimization](http://arxiv.org/abs/2608.04056v1)
  <details><summary>📄 Abstract</summary>
  When people label text for sexism, they often disagree, and not because some of them are wrong: they genuinely perceive sexism differently. Most NLP systems discard this disagreement by collapsing it into a majority vote. We propose the Multi-Agent Perspectivist Preference Optimization (MAP-PO) framework to keep these different perspectives. On the EXIST 2024 dataset of labeled English and Spanish tweets, we first cluster annotators by their labeling behavior rather than their demographic attrib...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 54 papers

- **2026-08-05** — Sajib Hossain, Md Kamrus Samad, Anan Ghosh et al. — [BnBERT-iPET: Sparse Few-Shot Language Modeling for Bengali via Lottery Ticket Pruning](http://arxiv.org/abs/2608.05104v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks have shown impressive success in NLP tasks owing to their complex structure and huge number of edges. Achieving state-of-the-art performance in natural language processing with a large pre-trained model such as BERT is expensive and time-consuming, carries a large carbon footprint, and is difficult to realize on machines with minimal computational capability. This creates a barrier to training complex models for resource-constrained languages such as Bengali. However, in a c...
  </details>

- **2026-08-05** — Jiahong Zhang, Sijun Shen, Dehua Wu et al. — [SpikingNav: Robust Embodied Navigation with Spiking Neural Policies](http://arxiv.org/abs/2608.05078v1)
  <details><summary>📄 Abstract</summary>
  Embodied navigation requires an agent to make sequential decisions from egocentric observations in a physical environment. Existing Artificial Neural Network (ANN)-based navigation models have achieved strong performance, yet they often rely on dense computation and may degrade under visual corruptions. Spiking neural networks (SNNs) provide event-driven computation and intrinsic temporal dynamics, which are promising for compact and robust navigation on resource-constrained platforms. However, ...
  </details>

- **2026-08-05** — Johann Knechtel, Ozgur Sinanoglu, Paul V. Gratz et al. — [Hardware Design and Security in the Era of Chiplets and LLMs](http://arxiv.org/abs/2608.05063v1)
  <details><summary>📄 Abstract</summary>
  The semiconductor industry is undergoing a dual revolution: the shift toward heterogeneous 2.5D chiplet systems and the integration of Large Language Models (LLMs) into Electronic Design Automation (EDA) flows. While these paradigms offer unprecedented benefits in yield, modularity, design productivity, etc., they radically expand the hardware attack surface. This paper provides a unified analysis of these frontiers, ranging from attacks on chiplet systems (including hardware stacks for LLM acce...
  </details>

- **2026-08-05** — Weihan Cai, Hao Tan, Zichang Tan et al. — [Unleashing the Potential of Vision-Language Models for Generalizable AI-Generated Image Detection](http://arxiv.org/abs/2608.04935v1)
  <details><summary>📄 Abstract</summary>
  Recent work has shown that a simple linear probe on frozen representations from modern vision foundation models (VFMs) can achieve state-of-the-art AIGI detection performance, substantially outperforming specialized detectors in challenging in-the-wild scenarios. This finding has established DINOv3 as the dominant foundation-model baseline for subsequent improvements. However, we find that the vision-language model Perception Encoder (PE) holds greater potential for AIGI detection, because its l...
  </details>

- **2026-08-05** — Pedro Ferreira, Wilker Aziz, Ivan Titov — [Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?](http://arxiv.org/abs/2608.04928v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) reasoning offers a window into the decision-making of large language models (LLMs), which can be monitored for target behaviors by reading the reasoning trace, motivating work on CoT monitorability. Latent CoT approaches, however, replace the explicit tokens with a small number of continuous states, lowering inference costs but removing the readable trace this monitoring relies on. Monitoring then requires alternative access to the model, such as probing its activations or...
  </details>

- **2026-08-05** — Ethen Santana, Gabriel Gyaase, Hao Zheng — [LLM-Assisted Detection and Repair of Hardware Security Vulnerabilities in Verilog Designs](http://arxiv.org/abs/2608.04907v1)
  <details><summary>📄 Abstract</summary>
  Hardware designs, like software, are susceptible to bugs that can introduce security vulnerabilities and create opportunities for malicious exploitation. Unlike software vulnerabilities, however, hardware flaws become permanently embedded in silicon after fabrication, making them difficult or impossible to patch. Many of these weaknesses are categorized under the Common Weakness Enumeration (CWE) framework and include improper access control, exposure of sensitive information, and unintended pri...
  </details>

- **2026-08-05** — Yuhong Shi, Zhenhao Chu, Jie Wei et al. — [Overcoming Statistical Bias in Action-Controllable World Models](http://arxiv.org/abs/2608.04653v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned world models aim to predict how visual environments evolve under an agent's actions. Yet future frames are often highly predictable from visual inertia and recurring motion patterns alone. This creates a shortcut: models can fit the data by exploiting statistical biases without making their visible dynamics meaningfully depend on the action. As a result, different actions may produce similar futures, while motion may persist even under zero action. The key question is how to r...
  </details>

- **2026-08-05** — Thang Do, Steffen Dereich, Arnulf Jentzen — [On MUON optimization: From non-convergence to an error analysis with Polar Express and the Newton-Schulz polynomial from implementations](http://arxiv.org/abs/2608.04607v1)
  <details><summary>📄 Abstract</summary>
  Stochastic gradient descent (SGD) optimization methods are the standard instruments for the training of deep neural networks (DNNs). In many relevant artificial intelligence (AI) systems - such as popular large language models (LLMs)-not the standard SGD scheme is used as the optimization method but instead suitable accelerated variants of SGD are employed. One of the most popular methods of such accelerated SGD variants is the momentum orthogonalized by Newton-Schulz (MUON) optimizer proposed b...
  </details>

- **2026-08-05** — Runwei Guan, Di Tian, Ningwei Ouyang et al. — [Talk2Sensors: 3D Visual Grounding in Autonomous Driving via Sensor-Adaptive Physical Cue Matching](http://arxiv.org/abs/2608.04568v1)
  <details><summary>📄 Abstract</summary>
  As a key capability for embodied intelligence, 3D visual grounding (3DVG) has been predominantly studied in indoor scenes with RGB-D or point-cloud inputs, while existing outdoor extensions largely rely on monocular images alone. Both settings fall short of real-world outdoor perception, where heterogeneous sensors capture complementary yet distinct physical properties, such as visual texture, 3D geometry, and object kinematics, that are indispensable for flexible and robust query-adaptive groun...
  </details>

- **2026-08-05** — Zhengdong Huang, Kevin Li, Jinqiu Yang et al. — [Checked-In Secret Detection: Strings Are All You Need](http://arxiv.org/abs/2608.04523v1)
  <details><summary>📄 Abstract</summary>
  Hardcoded secrets in source code pose critical security vulnerabilities which can be easily exploited by malicious adversaries. Existing regex-based detection approaches suffer from fundamental limitations, as secrets often lack identifiable patterns, resulting in poor precision and recall. Recent studies have explored context-aware detection methods, as surrounding code can reveal the purpose of candidate strings. However, these methods confront three key challenges: (1) obfuscation robustness ...
  </details>

- **2026-08-05** — Kazuya Horibe, Kenji Itao, Wataru Toyokawa — [Emergence of Reputation-Based Cooperation in LLM Agents](http://arxiv.org/abs/2608.04507v1)
  <details><summary>📄 Abstract</summary>
  Can cooperation among large language model (LLM) agents be evolutionarily stable against free-rider invasion? We study an indirect reciprocity donation game where LLM agents observe behavioral traces and donate on a continuous scale. Strategies, represented as natural language prompts, evolve through cultural transmission across generations. Across four LLM backends, robustness to free-rider invasion varies by more than an order of magnitude. The strongest predictor of this robustness is opponen...
  </details>

- **2026-08-05** — Zhicong Huang, Cheng Hong, Tao Wei — [DeepInvert: Semi-Supervised Embedding Inversion Against Obfuscated Language Models](http://arxiv.org/abs/2608.04477v1)
  <details><summary>📄 Abstract</summary>
  Cloud-based language model services routinely process prompts containing sensitive information. Obfuscation-based defenses---including ObfusLM, SentinelLMs, TextObfuscator, and DPNR---mitigate this risk by transforming prompt representations before transmission, offering a lightweight alternative to cryptographic solutions. We show these defenses provide far less protection than previously believed.   We present DeepInvert, a semi-supervised embedding inversion attack that recovers original toke...
  </details>

- **2026-08-05** — Russell Taylor, Adam Brikman, Prateek Awate — [Searching for Sound-Meaning Collisions: Graph-Based Affordance Retrieval and Multi-Evaluator Ranking for Pun Translation at CLEF 2026 JOKER Task 2](http://arxiv.org/abs/2608.04299v1)
  <details><summary>📄 Abstract</summary>
  Fifteen years ago, Low proposed that pun translators should stop searching for equivalent words and instead search for new points of contact between sound and meaning. In this paper, we investigate that idea computationally. We model pun translation as a process of discovery, exploration, and selection. A retrieval system searches semantic and phonological neighborhoods for target-language affordances: sound-meaning bridges that may support new wordplay. Multiple language models then explore the...
  </details>

- **2026-08-05** — Shuo Liu, Huixiang Cai, Weiru Zhang et al. — [GeoReward: Mitigating Contextual Variable Overestimation in Vision-Language Models for Cross-Market Preference Prediction](http://arxiv.org/abs/2608.04504v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models excel in many multimodal tasks but remain prone to a subtle yet impactful failure mode: they tend to overestimate dominant visual-textual cues while underestimating sparse but decision-critical contextual variables. This issue, which we term Contextual Variable Overestimation (CVE), becomes particularly evident in real-world applications such as predicting advertisement image preferences across diverse geographic markets. For instance, when a VLM is asked to choose between...
  </details>

- **2026-08-04** — Ben Falchuk, Himanshu Garg, Euthimios Panagos et al. — [LLM-based Vulnerability Discovery in Business Process Documentation](http://arxiv.org/abs/2608.04271v1)
  <details><summary>📄 Abstract</summary>
  Just like software and hardware, business processes are susceptible to vulnerabilities that can lead to product quality issues, delays, and increased costs. Business process vulnerabilities can arise from a variety of sources, including conflicting requirements, ambiguous documentation, invalid measurement spec-ifications, omission of quality checks, or implementations that differ from speci-fications. MIRABELLE is a system that identifies and characterizes business logic (BL) vulnerabilities fr...
  </details>

- **2026-08-04** — Yu Nong, Haipeng Cai — [Neuro-Symbolic Proof-of-Vulnerability Generation with Open-Weight Models](http://arxiv.org/abs/2608.04217v1)
  <details><summary>📄 Abstract</summary>
  Software vulnerabilities are persistent, but validating them remains difficult: a Proof-of-Vulnerability (PoV) requires a concrete input that triggers the vulnerable behavior, yet public triggering inputs are often unavailable for disclosed vulnerabilities. Existing techniques make different tradeoffs in effectiveness, scalability, cost, and controllability, leaving room for complementary designs. To complement them, we present POVGEN, a low-cost neuro-symbolic framework that makes PoV generatio...
  </details>

- **2026-08-04** — Palash R. Roy, Banani Roy, Kevin A. Schneider et al. — [MergeSE: Post-Hoc Model Merging for Software Engineering Tasks Without Retraining](http://arxiv.org/abs/2608.04181v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuned code models often behave as domain specialists and can degrade sharply under distribution shift: in our clone-detection setting, a model trained on same-language clones drops 71\% F1 on cross-language clones, while multi-task training falls to 0.151 F1 on unseen AI-generated clones. Our companion study shows that post-hoc model merging can address this fragmentation, achieving 93\% of multi-task performance without training data while generalizing 4$\times$ better to unseen clone type...
  </details>

- **2026-08-04** — Chandrakant K. Bhogayata — [HomoEnsNER: Does Language Alignment Outperform Architectural Complexity in Gujarati Named Entity Recognition?](http://arxiv.org/abs/2608.03105v2)
  <details><summary>📄 Abstract</summary>
  Named Entity Recognition (NER) for Gujarati remains underexplored, hindered by the absence of capitalization cues, rich morphology, lexical ambiguity, and free word order. Prior ensemble work has emphasized architectural diversity by combining heterogeneous classifiers, multilingual encoders, or classical sequence models, rather than exploiting language-aligned monolingual pretraining. This study asks whether, for a low-resource, morphologically rich language like Gujarati, a homogeneous ensembl...
  </details>

- **2026-08-04** — Shaofeng Liang, Runwei Guan, Wenshuo Chen et al. — [When Efficiency Becomes Fragility: Exploiting Dynamic Routing Vulnerabilities in Adaptive UAV Tracking](http://arxiv.org/abs/2608.03902v1)
  <details><summary>📄 Abstract</summary>
  Resource constraints on UAV platforms have driven a paradigm shift in aerial tracking, from pursuing performance toward balancing accuracy with efficiency. Adaptive Transformer Trackers, which leverage an input-dependent dynamic routing architecture, have emerged as a representative solution to this challenge. However, we reveal that behind this computation-on-demand flexibility hides a critical structural flaw: the Lipschitz singularity of computational path decisions, which has an unbounded lo...
  </details>

- **2026-08-04** — Andrei Chetvergov, Alexander Evseev, Timofei Sivoraksha et al. — [VIBE: A VAD-Informed Benchmark for Entity-Centered Affective Profiling of Large Language Model Outputs](http://arxiv.org/abs/2608.03810v1)
  <details><summary>📄 Abstract</summary>
  Large language models routinely describe socially salient targets, including political figures, countries, religions, organizations, historical events, and social groups, encoding affective framing alongside factual content: a target may appear favorable or threatening, calm or conflictual, powerful or vulnerable. Existing work captures parts of this space through sentiment, favorability, and emotion benchmarks, but none combines target-directed VAD attribution, an explicit scorer contract, and ...
  </details>

- **2026-08-04** — Leijun Zhou, Zhihao Liu, Xiang Qu et al. — [GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks](http://arxiv.org/abs/2608.03764v1)
  <details><summary>📄 Abstract</summary>
  Agent self-evolution updates an agent's persistent state from prior experience and reuses it to solve related tasks more effectively. Evaluating self-evolution is difficult: existing benchmarks provide limited coverage of economically valuable task domains, do not always design training and test tasks such that test-time gains can be attributed to training experience, and remain vulnerable to data contamination. We present GDPevo, an evolution-native benchmark grounded in GDP-related enterprise ...
  </details>

- **2026-08-04** — Zhijing Hu, Changjun Fan, Yufan Deng et al. — [AutoSND: From Execution Evidence to Structural Policies for Automated Network Dismantling Heuristic Discovery](http://arxiv.org/abs/2608.03653v1)
  <details><summary>📄 Abstract</summary>
  Network dismantling is fundamental to analyzing the robustness and vulnerability of complex systems, yet practical heuristics must balance effectiveness and computational efficiency, and are usually designed manually by researchers. Existing large language model based automatic heuristic design methods can generate and screen candidates, yet they have difficulty further transforming candidate quality or failure states during execution into structural-level guid- ance for subsequent generation. W...
  </details>

- **2026-08-04** — Seonghoon Yoo, Sangwoo Park, Seok-Hwan Park et al. — [Test-Time Scalable AI-RAN: Inference Time Allocation for Cell-Free MIMO](http://arxiv.org/abs/2608.03614v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence-enabled radio access networks (AI-RANs) are envisioned to consist of multiple AI-based modules, potentially developed independently by different vendors. In this work, we study AI-RAN-enabled cell-free MIMO systems, with a particular focus on the system implications of modern AI models. Specifically, we focus on the phenomenon of test-time scalability popularized by large language models (LLMs), under which model performance improves as additional computational resources ...
  </details>

- **2026-08-04** — Reinoud Jan Slagter — [New gravitational instanton: shadow of an extra dimension](http://arxiv.org/abs/2608.03536v1)
  <details><summary>📄 Abstract</summary>
  We present an exact gravitational instanton solution on a five-dimensional, conformally invariant, Kerr-like warped Riemannian brane-world manifold. The geometry can be described as the Kähler manifold $\mathbb{C}^1\times\mathbb{C}^1\times \mathbb{R}$. By applying a double cover of $S^3$ through stereographic projection onto $\mathbb{C}P^1\times \mathbb{C}P^1$ of the effective four-dimensional manifold, together with the Klein surface construction, we exploit the underlying $\mathbb{Z}_2$ symmet...
  </details>

- **2026-08-04** — Savi Virolainen — [A fully nonlinear structural vector autoregressive model identified via independent innovation analysis](http://arxiv.org/abs/2608.03486v1)
  <details><summary>📄 Abstract</summary>
  We develop a fully nonlinear structural vector autoregressive framework in which the contemporaneous structural mapping may be nonlinear and non-additive. Identification is achieved by exploiting variation in the conditional distributions of the mutually independent structural shocks induced by an observed exogenous variable. Specifically, a general contrastive learning framework that makes use of this variation together with the assumed exponential-family structure is employed to recover the sh...
  </details>

- **2026-08-04** — Francis Heylighen — [The Evolutionary Origin of Values: implications for AI alignment, sentience and existential risk](http://arxiv.org/abs/2608.03361v1)
  <details><summary>📄 Abstract</summary>
  AI systems based on Large Language Models (LLMs) have prompted fears that they may harbor hidden goals, seek to dominate or eliminate humanity, or even suffer as sentient beings. We address these concerns by tracing the evolutionary origin of value in biological organisms. Values emerge from autopoiesis: living systems must actively maintain themselves against perturbation and dissipation. Natural selection has equipped them with hierarchies of "vicarious selectors" that guide their behavior tow...
  </details>

- **2026-08-04** — Anjun Hu, Hanting Xie, Saranya Govindan et al. — [Attacking and Defending Multi-Agent Collaborative Filtering Systems Through Connectivity](http://arxiv.org/abs/2608.03272v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent collaborative filtering (CF) systems coordinate autonomous LLM-powered user and item agents through natural-language interaction to refine preferences and generate recommendations. These systems inherit vulnerabilities from both their data-driven nature and their multi-agent interactions, which manifest in distinct ways. Understanding how connectivity modulates vulnerability in these systems could facilitate the development of more robust recommendation pipelines.   In this work, we ...
  </details>

- **2026-08-04** — Meicong Zhang, Tiancheng Su, Jiahao Cheng et al. — [Internalizing Academic Writing Workflows for Introduction Generation via Struct-Aware Policy Learning](http://arxiv.org/abs/2608.03138v1)
  <details><summary>📄 Abstract</summary>
  Generating a rigorous paper introduction with large language models (LLMs) remains challenging, since it requires coordinating background, gap identification, method and contribution within a coherent narrative. Existing solutions externalize this process as multi-stage prompts or agent workflows which are expensive and vulnerable to cross-stage drift. We propose StructPO, a struct-aware policy learning framework that internalizes the entire multi-stage writing workflow into a single-pass policy...
  </details>

- **2026-08-04** — Sungju Yun, Sijune Hwang, Yeonjoon Lee et al. — [CLEAR: Causal Context-Based Agentic Reasoning for Vulnerability Detection](http://arxiv.org/abs/2608.03134v1)
  <details><summary>📄 Abstract</summary>
  Detecting source code vulnerabilities is increasingly difficult as modern security flaws are rooted in complex causal dependencies between execution flows, control conditions, and program states. Despite recent advances in Large Language Models (LLMs) and multi-agent frameworks, existing approaches primarily address superficial similarities between benign and vulnerable functions while failing to capture the complex causal dependencies inherent in security flaws. To address these limitations, we...
  </details>

- **2026-08-04** — Chandrakant K. Bhogayata — [HomoEnsNER: Does Language Alignment Outperform Architectural Complexity in Gujarati Named Entity Recognition?](http://arxiv.org/abs/2608.03105v1)
  <details><summary>📄 Abstract</summary>
  Named Entity Recognition (NER) for Gujarati remains underexplored, hindered by the absence of capitalization cues, rich morphology, lexical ambiguity, and free word order. Prior ensemble work has emphasized architectural diversity by combining heterogeneous classifiers, multilingual encoders, or classical sequence models, rather than exploiting language-aligned monolingual pretraining. This study asks whether, for a low-resource, morphologically rich language like Gujarati, a homogeneous ensembl...
  </details>

- **2026-08-04** — Jialu Huang, Yingxuan You, Fei Wang et al. — [Global Graph-Validated Optimization for VLM-based 3D Indoor Scene Generation](http://arxiv.org/abs/2608.03064v1)
  <details><summary>📄 Abstract</summary>
  We study open-vocabulary 3D indoor layout generation, which synthesizes diverse and physically plausible scenes from unlabeled 3D assets using free-form language instructions. Recent methods leverage large language models (LLMs) and vision-language models (VLMs) to generate structured scenes from text. However, most model inter-asset relations implicitly or rely on local pairwise constraints and local optimization. These formulations are poorly aligned with the global, highly non-convex layout s...
  </details>

- **2026-08-04** — Yoshiki Ito — [AIDE: Automated Instruction via Distilled Expertise for Reference-Free Motor Skill Coaching](http://arxiv.org/abs/2608.03047v1)
  <details><summary>📄 Abstract</summary>
  Generating natural-language coaching feedback on motor skills can accelerate learning, yet expert coaches are scarce and expensive. Existing reference-based methods require expert demonstrations at both training and inference time, limiting practical deployment. We propose AIDE (Automated Instruction via Distilled Expertise), a framework that exploits expert references only during training and generates feedback from a learner's pose sequence alone at inference. A teacher model first learns to g...
  </details>

- **2026-08-04** — Zhitian Hou, Yuhang Liu, Pengkai Wang et al. — [Evaluating Counterfactual Sensitivity to Patient Information in Medication-Safety Reasoning](http://arxiv.org/abs/2608.03028v1)
  <details><summary>📄 Abstract</summary>
  Applying a valid medication-safety rule when its patient-specific conditions are not met can produce an incorrect decision. Existing medical evaluations largely use isolated and fixed scenarios. A model may therefore answer correctly by recalling a drug-risk association without showing that it used patient information to decide whether the rule applies. To address this gap, we introduce MedPIC-Bench, a benchmark of source-verifiable recommendations and expert-validated questions for patient-spec...
  </details>

- **2026-08-04** — Yizhong Geng, Wenxin Fu, Kecan Mao et al. — [MeloCodec: Harnessing Melodic Priors for High-Fidelity Singing Voice Representation](http://arxiv.org/abs/2608.03021v1)
  <details><summary>📄 Abstract</summary>
  Neural audio codecs serve as fundamental tokenizers for LLM-based audio generation. While semantic priors are widely exploited to enhance linguistic intelligibility, the integration of explicit acoustic priors remains underexplored, limiting synthesis fidelity in frequency-sensitive domains. To address this gap, we introduce MeloCodec, a novel framework designed to effectively incorporate melodic priors, a critical form of acoustic information for singing. To address the optimization instability...
  </details>

- **2026-08-04** — Yongwan Jo, Jinyoung Park, Euihyun Lee et al. — [SparSEEty: Extracting Tokens from Sparsity-Exploiting LLM Serving Systems via Deterministic Side Channels](http://arxiv.org/abs/2608.02995v1)
  <details><summary>📄 Abstract</summary>
  Modern large language models (LLMs) exhibit activation sparsity, wherein only a subset of their neurons is activated for given input tokens. Researchers have leveraged this property to optimize LLM serving systems by omitting weight accesses and computations pertaining to inactive neurons. Unfortunately, however, such optimizations create input-dependent weight accesses, which can be leaked over side channels.   We present SparSEEty, a new token extraction attack that exploits input-dependent ne...
  </details>

- **2026-08-03** — Qiushi Lin, Chaojie Zhang, Íñigo Goiri et al. — [AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies](http://arxiv.org/abs/2608.02569v1)
  <details><summary>📄 Abstract</summary>
  The efficiency of a datacenter rests on its control plane policies. Designing these policies is increasingly hard: the hardware-software stack grows fast, the design space is vast and interdependent, and prototyping a single policy takes months. Agentic AI promises to automate this search. Off the shelf, however, it falls short on three fronts. It is not formal: with no structured, searchable statement of the problem, the search has little structure to exploit and hard constraints are not guaran...
  </details>

- **2026-08-03** — Anusha Madan Gopal, Aras Pirbadian, Kristofor D. Carlson et al. — [Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection](http://arxiv.org/abs/2608.02560v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token. State-Space Models (SSMs) avoid the second cost by construction; we eliminate the first, collapsing prefill from $O(L_{context})$ to $O(1)$ per query. We introduce PRECOG (Pre-Computed Context Injection), a retrieval mechanism that exploits a property unique to SSMs: the fixed-size, position-agnostic recurrent ...
  </details>

- **2026-08-03** — Supriti Vijay, Aman Priyanshu, Didier Chapoteau et al. — [Antares: Foundation Models for Agentic Vulnerability Localization](http://arxiv.org/abs/2608.02407v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability localization is a fundamental step in software security, requiring models to reason over large codebases and iteratively identify vulnerable implementations. We present Antares, a family of compact language models (350M, 1B, and 3B parameters) for agentic vulnerability localization. Based on IBM Granite base models, Antares is trained through a two-stage pipeline that combines supervised fine-tuning on cybersecurity reasoning and repository exploration data with reinforcement learn...
  </details>

- **2026-08-03** — Patrick Oberlin, Matteo Cederle, Aren Karapetyan et al. — [Chess on Ice: Curling Tactical Decision-Making via Backward Induction and Deep Reinforcement Learning](http://arxiv.org/abs/2608.02379v1)
  <details><summary>📄 Abstract</summary>
  Curling is often referred to as "Chess on Ice", owing to the tactical complexity of its decision-making process. Yet unlike chess, curling remains largely underexplored from a machine learning perspective, with prior work confined mainly to statistical approaches. We propose a reinforcement learning framework capable of quantitatively evaluating and comparing tactical options in curling. The game poses several modeling challenges: continuous state and action spaces, stochastic action outcomes re...
  </details>

- **2026-08-03** — Liujianfu Wang, Yuyang Du, Shiqi Xu et al. — [Broadcast Rate Limits in Wi-Fi: A Forgotten Bottleneck for Collaborative Edge LLM Inference](http://arxiv.org/abs/2608.02341v1)
  <details><summary>📄 Abstract</summary>
  LLM deployment is migrating from data centers to edge devices, where Mixture-of-Experts (MoE) models offer a promising path: sparse expert activation allows the model to be spread across multiple low-cost edge nodes. Distributed MoE inference repeatedly dispatches embeddings from one main node to many workers - a one-to-many pattern poorly served by the sequential unicasts of mainstream stacks (NCCL, TCP), yet naturally matched by UDP broadcast. We propose a UDP broadcast method for collaborativ...
  </details>

- **2026-08-03** — Aseel AlNajjar, Hoyoun Kim, Athanasios Tzavaras — [Equilibration versus Localization in a Diffusion-Relaxation System](http://arxiv.org/abs/2608.02307v1)
  <details><summary>📄 Abstract</summary>
  We consider a diffusion-relaxation system and investigate the conditions on parameters leading to equilibration versus localization. When the diffusion is dominant, solutions converge toward homogeneous equilibria. By contrast, when the effective diffusion is weak, localization emerges. Such behaviors have been studied for various models through formal asymptotic arguments and linearized stability analysis, but rigorous understanding of the associated nonlinear phenomena remains limited, particu...
  </details>

- **2026-08-03** — Haozhe Luo, Ziyu Zhou, Shelley Zixin Shu et al. — [HarMoE: Multi-Source Chest Radiograph Pretraining with Dataset-Disentangled Experts](http://arxiv.org/abs/2608.02252v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language models for chest X-ray understanding are largely built on image-report alignment and therefore rely heavily on MIMIC-CXR as the dominant pretraining source. While effective at scale, this paradigm underexplores an important alternative source of supervision: a range of existing multi-label classification datasets, which provide cleaner and more explicit disease signals than free-text reports, and can offer broader pathology coverage when combined across sources. However, l...
  </details>

- **2026-08-03** — Yanqing Song, Jifei Miao, Chaoqian Li et al. — [Quaternion Tensor Modeling for Joint Color-Polarization Demosaicking](http://arxiv.org/abs/2608.02144v1)
  <details><summary>📄 Abstract</summary>
  Division-of-focal-plane (DoFP) color polarization cameras enable snapshot acquisition of color polarization mosaic images, but the inherently sparse sampling pattern makes color polarization demosaicking severely ill-posed. Existing methods often fail to jointly exploit the correlations among polarization channels and the physical constraints inherent in polarization imaging, resulting in noticeable demosaicking artifacts. To address this issue, a quaternion-tensor-based color polarization demos...
  </details>

- **2026-08-03** — Oleksandr Mostovyi, Denys Symonov — [Vulnerability Detection in AArch64 Machine Code Using a Digital Twin](http://arxiv.org/abs/2608.02125v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an explainable digital twin for vulnerability detection in AArch64 machine code without access to source code. The digital twin reproduces the concrete execution of a program and preserves the state of registers, processor flags, memory, and live allocated blocks. Each instruction is transformed into a trace event containing the instruction name, operand values, and the post-instruction state. Vulnerabilities are represented as symbolic rules in Kleene algebra with tests: eac...
  </details>

- **2026-08-03** — Xianghui Fan, Zhaoyu Chen, Bingqian Wu et al. — [GIFT: Geometry-Invariant Fine-Tuning for Non-Lambertian Monocular Depth Estimation](http://arxiv.org/abs/2608.02068v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth foundation models, benefiting from large-scale synthetic training data, have demonstrated strong generalization. However, they often hallucinate depth on non-Lambertian surfaces, estimating reflected content in mirrors or transmitted content behind glass rather than the physical surface itself. Adapting these models with real-world data is challenging because conventional depth sensors are also unreliable in such regions. We observe that while the appearance of a non-Lambertian s...
  </details>

- **2026-08-03** — Kexing Ji, Jiachen Liu, Enze Hu et al. — [VulnGym: Benchmarking Coding Agents for Repository-Level Vulnerability Detection](http://arxiv.org/abs/2608.02001v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in LLM-based vulnerability detection have shown promising results, while coding agents further extend this capability from isolated code snippets to complete repositories. This shift requires agents to autonomously explore repositories and locate vulnerability-relevant code, instead of performing detection on preselected functions. However, existing benchmarks primarily focus on vulnerability classification over preselected code snippets, limiting their ability to evaluate coding...
  </details>

- **2026-08-03** — Zong-Wei Hong, Jinglun Li, Shen Zhang et al. — [SPARE: Structural Parameter-Free Affinity Regularization for Flow Matching](http://arxiv.org/abs/2608.01990v1)
  <details><summary>📄 Abstract</summary>
  Denoising diffusion transformers achieve strong generation quality but converge slowly during training. Regularizing their internal representations has emerged as an effective accelerator, yet existing methods split into two families with complementary costs. Target-based methods strengthen representations by aligning them to external features, which requires an external encoder and a learnable projection head to bridge feature spaces. Target-free methods hold no reference at all, and can only r...
  </details>

- **2026-08-03** — Amir Weinberg, Leon Feigin, Ariel Nause et al. — [Machine Learning Optimization of E-Beam Transport for a Superradiant FEL](http://arxiv.org/abs/2608.01874v1)
  <details><summary>📄 Abstract</summary>
  We present an optimization procedure using machine learning (ML) libraries for optimization of electron beam transport for maximal bunch compression and optimal operation of a bunched-beam Superradiant FEL. This is exemplified for the parameters of the 6MeV ORGAD Accelerator at Ariel University that is driving a THz Superradiant waveguide FEL. For superradiant emission (proportionally to the number of electrons squared), the bunch duration $σ_t$ at the undulator should be shorter than the optica...
  </details>

- **2026-08-03** — Durgesh Pandey, Ashutosh Singh, Ankit Kumar Das et al. — [Quantum Simulation of Nuclear Shell Model Using GCM-Based Methods on NISQ Devices](http://arxiv.org/abs/2608.01769v1)
  <details><summary>📄 Abstract</summary>
  Based on the Generator Coordinate Method (GCM), we use a Quantum GCM (QuGCM) within a hybrid quantum-classical framework to simulate low-lying eigenstates of nuclear systems on quantum devices. The generator basis states are constructed from Hartree-Fock (HF) reference states, excited via symmetry-adapted unitary coupled-cluster (UCC) operators. These states are prepared as non-orthogonal quantum circuits and measured pairwise to compute the required overlap and Hamiltonian kernels. The resultin...
  </details>

- **2026-08-03** — Kaustuv Mukherji, Jaikrishna Manojkumar Patil, Colton Payne et al. — [EntailLLM: Verifying LLM-Generated Vulnerability Discovery Paths with Domain Knowledge via Logic Programming](http://arxiv.org/abs/2608.01763v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to reason about software vulnerabilities, but their outputs can silently violate domain knowledge, limiting their reliability in safety-critical settings such as medical devices. Prior work either treats that output as a prediction to be scored or constrains it to walks within a single knowledge graph; neither checks whether reasoning over a binary is consistent with an independent body of domain knowledge. We present EntailLLM, which validates each LL...
  </details>

- **2026-08-03** — Jiacheng Liang, Yuhui Wang, Tanqiu Jiang et al. — [LaCache: Robust Semantic Caching for LLM Serving](http://arxiv.org/abs/2608.01718v1)
  <details><summary>📄 Abstract</summary>
  Semantic caching, which reuses responses to semantically similar requests via their embeddings, has seen growing adoption in LLM serving, offering faster responses and reduced costs. Yet existing schemes are fundamentally vulnerable to cache-collision attacks, wherein an adversary pollutes the cache by injecting crafted queries, corrupting responses to subsequent legitimate requests. We present LaCache, a novel semantic caching scheme that addresses this vulnerability through a conceptually simp...
  </details>

- **2026-08-03** — Minwoo Kim, Hyeonsu Lyu, Sehyun Ryu et al. — [Temporal Channel Estimation for Generalized CSI Feedback](http://arxiv.org/abs/2608.01713v1)
  <details><summary>📄 Abstract</summary>
  Efficient Channel State Information (CSI) feedback is indispensable for frequency division duplex (FDD) massive multiple-input multiple-output (MIMO) systems. Existing compressed sensing (CS) algorithms exploit delay-domain sparsity but suffer from prohibitive iterative latency and discrete grid mismatch. Conversely, deep learning (DL) approaches achieve rapid inference but lack spatial scalability and domain adaptability, failing to generalize to unseen propagation environments, and demand comp...
  </details>

- **2026-08-03** — Shen You, Xiaoming Zhu, Weining Weng et al. — [SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction](http://arxiv.org/abs/2608.01652v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent coordination faces a fundamental trade-off between efficiency and adaptivity in dynamic environments. Existing approaches typically rely on repeated LLM invocations or multi-round communication to adapt decisions during execution, introducing substantial latency and making coordination vulnerable to asynchronous progress and environmental changes. Conversely, one-shot planning reduces coordination overhead but produces open-loop plans that can quickly become stale or fail w...
  </details>

- **2026-08-03** — Alireza Lotfi, Subangkar Karmaker Shanto, Imtiaz Karim et al. — [Securing Agentic AI: From Per-Action Checks to Trajectory Assurance](http://arxiv.org/abs/2608.01558v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are increasingly used to execute consequential tasks in environments governed by operational constraints, organizational policies, regulatory requirements, and technical standards. Their safety is therefore determined not by the correctness of individual actions, but by whether their overall behavior remains consistent with the rules and invariants of the systems in which they operate. As large language model (LLM)-based agents become more autonomous and increasingly delegate t...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 53 papers

- **2026-08-05** — Junbo Zhang, Qianli Zhou, Xinyang Deng et al. — [DataRx: Missingness-Aware Sampling for Safer Large Language Model Task-Specific Fine-Tuning](http://arxiv.org/abs/2608.04322v1)
  <details><summary>📄 Abstract</summary>
  Task-specific fine-tuning can improve the performance of large language models (LLMs) on downstream tasks. However, our study reveals that task-specific fine-tuning can also weaken the safety guardrails of aligned LLMs. A widely adopted strategy for preserving safety during fine-tuning is to incorporate safety data. Although previous studies have shown that randomly mixing safety data can alleviate safety degradation, the underlying principle determining why some safety examples are more effecti...
  </details>

- **2026-08-05** — Jai Malegaonkar, Rohan Patil, Henrik I. Christensen — [Reward Structure Shapes the Interaction Between Episodic Exploration and Neural Memory in Reinforcement Learning](http://arxiv.org/abs/2608.05111v1)
  <details><summary>📄 Abstract</summary>
  In partially observable reinforcement learning, agents face a dual bottleneck: they must explore to encounter rewarding states and retain that experience in memory to optimize their policies. Exploration bonuses and memory architectures are traditionally evaluated in isolation, leaving their interaction unmeasured, and standard notions of sparse reward conflate temporal signal density with what the reward actually supervises. We present a controlled study crossing episodic exploration bonuses wi...
  </details>

- **2026-08-05** — Mahmut S. Gokmen, Evan W. Damron, Mitchell A. Klusty et al. — [Lesion Detection in CT with Frozen Self-Distilled Features: SALT, a Spatially Adaptive Label-Guided Temperature](http://arxiv.org/abs/2608.05100v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised pretraining objectives are spatially uniform: the teacher temperature and the per-patch loss weight are identical everywhere in the image, so a lesion a few patches wide contributes no more to the training signal than the surrounding parenchyma. Prior work biases the views toward annotated regions, which changes what the model sees but adds no pressure on the objective. We instead condition the targets of self-distillation, a method we call SALT (Spatially Adaptive Label-guided T...
  </details>

- **2026-08-05** — Shaopeng Liang — [From Score Matrices to Football-Aware Match-State Simulation: An Auditable LLM Harness for Exact-Score Reranking](http://arxiv.org/abs/2608.05030v1)
  <details><summary>📄 Abstract</summary>
  Football score forecasting combines a strong statistical core with a difficult contextual edge. Dynamic Poisson-family models estimate team strength, expected goals, and coherent score probabilities, but do not directly understand roles, tactical matchups, motivation, or how a first goal changes behaviour. Large language models (LLMs) can reason about such concepts, yet are not calibrated probability engines. We combine both components through an auditable information harness. This paper documen...
  </details>

- **2026-08-05** — Thomas Bartz-Beielstein — [Short-term load forecasting under EU-AI Act Requirements in Safety-Critical Environments: Results from a 41-day live challenge on the aggregated German transmission-grid load](http://arxiv.org/abs/2608.05018v1)
  <details><summary>📄 Abstract</summary>
  Short-term load forecasting (STLF) play a vital role in the electric power industry. It serves infrastructure that European and German law designate as critical. Determinism, reproducibility, and auditability are engineering requirements rather than optional extras. STLF is no longer purely an accuracy problem. It is also a software-engineering and compliance problem. This paper describes results from a 41-day live challenge that evaluated a complete STLF pipeline for the aggregated German trans...
  </details>

- **2026-08-05** — Jinyi Han, Yuanjian Xu, Ying Liao et al. — [Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?](http://arxiv.org/abs/2608.04828v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly rely on skills, structured documents that specify when to act, which procedure to follow, and which tools are allowed. Existing evaluations mostly judge the quality of a skill or its contribution to task success, leaving unexamined whether an agent can recognize a relevant skill and apply it on its own. We introduce Skill-Use, a benchmark that evaluates skill use under progressive disclosure, where an agent sees only a skill's name and short descrip...
  </details>

- **2026-08-05** — Ishaan Bhola, Adithyan Krishnan, Mukunda NS — [Scrouting: Cost-Aware Routing of Coding Agents by Scouting the Repository First](http://arxiv.org/abs/2608.04804v1)
  <details><summary>📄 Abstract</summary>
  Frontier language models can resolve repository-level software issues, but each attempt is expensive, and existing routers select a model from the issue text alone. We present SuperScout, which routes after scouting the repository: a 7B searcher, SuperScout-7B, first explores the repository and produces a structured handoff whose reproduction claims are sandbox-verified, with false claims stripped before delivery. The searcher's hidden states, together with the task text, then feed a resume-base...
  </details>

- **2026-08-05** — Thorsten Hoeser, Felix Bachofer, Claudia Kuenzer — [Benchmarking Deep Learning Models for Dense Event Classification of Offshore Wind Infrastructure in Sentinel-1 Time Series](http://arxiv.org/abs/2608.04706v1)
  <details><summary>📄 Abstract</summary>
  Monitoring of offshore wind energy infrastructure life cycles, especially during the deployment phase, is an important contribution for stakeholders to make informed decisions in a phase of increasing deployment activities. ESA's Sentinel-1 Synthetic Aperture Radar (SAR) mission produces large data archives that enable the global monitoring of offshore wind infrastructure. Turning these high-volume archives into information requires algorithms that automatically extract single event labels from ...
  </details>

- **2026-08-05** — Zhuohang Jiang, Yuxin Chen, Yongsen Pan et al. — [A/B Agent: A Self-Evolving Agent for Strategy Iteration in Industrial A/B Testing](http://arxiv.org/abs/2608.04625v1)
  <details><summary>📄 Abstract</summary>
  Industrial recommendation strategy iteration heavily relies on large-scale A/B experimentation. Traditional tuning requires experts to repeatedly design strategies, configure experiments, analyze results, and adjust parameters, making the process labor-intensive and time-consuming. Meanwhile, valuable knowledge from historical experiments is often fragmented, making systematic reuse difficult through manual expert effort alone. Existing RAG agents partially alleviate this burden by retrieving pr...
  </details>

- **2026-08-05** — Yushi Sun, Yanjie Zhang — [When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents](http://arxiv.org/abs/2608.04574v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes. We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it becomes a safety-relevant mistake. Using a dynamic FrozenLake testbed, we pair a staleness-detection task with a downstream navigation task across three closed-source models and three open-weight VLMs...
  </details>

- **2026-08-05** — Yushi Sun, Yanjie Zhang, Rui Sheng — [The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads](http://arxiv.org/abs/2608.04570v1)
  <details><summary>📄 Abstract</summary>
  Personalized LLMs with persistent memory are increasingly deployed, yet the faithfulness of their user models remains unexamined. We study over-inference (OI): the phenomenon where LLMs fabricate user attributes beyond what evidence supports. We introduce MirageBench, comprising 150 personas balanced across stereotypical, counter-stereotypical, and neutral profiles, 6 personalization tasks spanning an ``imagination gradient'', a four-way faithfulness taxonomy operationalized by an independent ju...
  </details>

- **2026-08-05** — Le Li, Daniela Ivanova, Nicolas Pugeault — [Promptable Animal Pose Tracking Across Species](http://arxiv.org/abs/2608.04995v1)
  <details><summary>📄 Abstract</summary>
  Animal pose estimation and tracking is important for wildlife monitoring and conservation research, and with limited expert time for labelling automated approaches are imperative. While human pose estimation and tracking has seen rapid progress thanks to large annotated datasets, animal pose remain challenging, due to large morphological and behavioural differences between species and limited annotated data. Existing approaches either optimise generic keypoint localisation from annotated dataset...
  </details>

- **2026-08-05** — Mihailo Ilić, Miloš Savić, Vladimir Kurbalija et al. — [Attention, Anomalies! Handling Attention Layers in Unsupervised Federated Outlier Detection](http://arxiv.org/abs/2608.04753v1)
  <details><summary>📄 Abstract</summary>
  Attention layers are the backbone of today's most powerful and impactful models. Models with multi-million and billion parameters rely on contextual knowledge provided by attention layers. However, their use goes well beyond just being the core component of large language models. One particularly interesting application is in Memory Augmented Autoencoders (MemAE), specifically for unsupervised representation learning in outlier detection tasks. It was shown that attention helps these models be m...
  </details>

- **2026-08-05** — Suhas Hegde, Jitendra Yasaswi Bharadwaj Katta — [GUARD: Grounding Uncertainty and Ablation-Based Risk Detection for Diffusion-Based VLAs](http://arxiv.org/abs/2608.04510v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based vision-language-action (VLA) policies can generate plausible actions even when their predictions are weakly grounded in the visual and language evidence defining the task. We introduce GUARD, a test-time failure detection method that measures this grounding without modifying the pretrained policy. GUARD estimates the influence of token-indexed entries in the final vision-language model key-value (KV) cache, constructs counterfactual caches by ablating salient KV entries, and comp...
  </details>

- **2026-08-04** — Palash R. Roy, Banani Roy, Kevin A. Schneider et al. — [A Unified Model for Cross-Domain Clone Detection via Model Merging](http://arxiv.org/abs/2608.04215v1)
  <details><summary>📄 Abstract</summary>
  The growing diversity of code clone types, from syntactic copies to cross-language semantic clones to AI-generated duplicates, has created a fragmentation crisis in clone detection. Current deep learning detectors are domain specialists that degrade significantly outside their training distribution, with F1 drops exceeding 70% across domains. Deploying multiple specialized models is impractical, yet training a single cross-domain detector requires simultaneous access to all training data. To add...
  </details>

- **2026-08-04** — Ruiqi Wang, Yiming Qian, Fenggen Yu et al. — [PADFormer: Pose-agnostic Anomaly Detection from Sparse View Images](http://arxiv.org/abs/2608.04210v1)
  <details><summary>📄 Abstract</summary>
  Pose-agnostic Anomaly Detection (PAD) remains challenging as anomalies can appear under arbitrary viewpoints, requiring methods to handle significant pose variations. Existing approaches rely on complex 3D reconstruction, which are computationally expensive and require extensive multi-view data. We propose PADFormer, a novel image-space approach that leverages Vision Transformer (ViT) to directly reconstruct anomaly-free versions of query images while preserving pose information. Our key insight...
  </details>

- **2026-08-04** — Xinyu Wang, Yixuan Li, Hanwei Wu et al. — [Patients-like-me: A Variational LM--GNN Framework for Explainable Clinical Prediction](http://arxiv.org/abs/2608.04193v1)
  <details><summary>📄 Abstract</summary>
  Language models (LMs) offer strong textual representations for electronic health records (EHRs), but they encode patient sequences in isolation and provide limited explainability. Graph neural networks (GNNs) complement LMs by incorporating inter-patient relationships and enabling reference-patient attribution, yet they rely on high-quality patient representations. We propose Patients-like-me (PLM), a unified LM--GNN framework that integrates local patient semantics with global cohort structure....
  </details>

- **2026-08-04** — Luxshan Thavarasa, Sivasuthan Sukumar — [Test, then Route: How Language Models Execute In-Context Conditional Rules Across Models and Languages](http://arxiv.org/abs/2608.04183v1)
  <details><summary>📄 Abstract</summary>
  When a language model follows an in-context conditional rule such as "if P(x) then A else B," does it assemble a runtime circuit with one module that tests the predicate and another that routes the answer? We probe this with activation patching under a four-donor design whose two swapped-rule donors make the condition and the answer word disagree, so each layer reveals which of the two it carries. Across three open models from two families and six languages sharing one fixed item bank, a mid-sta...
  </details>

- **2026-08-04** — Carl Dickinson, Gaetano Di Caterina — [Advancing Utility Pole and Sign Detection Through Deep Learning](http://arxiv.org/abs/2608.04061v1)
  <details><summary>📄 Abstract</summary>
  Utility poles are an essential part of the infrastructure used to support power distribution systems and other critical public services. Their regular inspection is crucial to ensure the stability and safety of the electrical grid. A deep learning framework is presented for the automated detection, segmentation and lean angle estimation of wooden utility poles, and classification of attached electrical warning signs, using ground-level imagery. The system is trained on a custom dataset of 4,570 ...
  </details>

- **2026-08-04** — Myung-Hwan Jeon, Sankalp Yamsani, Joohyung Kim — [Kitchen Robotic Manipulation utilizing Foundation Models](http://arxiv.org/abs/2608.04042v1)
  <details><summary>📄 Abstract</summary>
  Deploying robots in everyday human environments requires perception systems that are both robust and adaptable to diverse, dynamic conditions. In this work, we present a modular perception pipeline for household manipulation tasks, with a focus on dishware handling in kitchen environments. The pipeline integrates open-vocabulary object detection, multi-view segmentation, instance-aware 3D reconstruction, and a 2D-3D feature fusion strategy for 6D pose estimation and grasp planning. Its modular d...
  </details>

- **2026-08-04** — Jiahui Liang, Lifeng Han — [Towards End-to-End Multilingual Metaphor Processing: Integrating Detection, Translation, and Evaluation](http://arxiv.org/abs/2608.04260v1)
  <details><summary>📄 Abstract</summary>
  Metaphorical language remains a major challenge for multilingual natural language processing because successful interpretation and translation require reasoning beyond literal lexical meaning. Existing research has largely investigated metaphor detection, machine translation, and translation evaluation as separate tasks, while little work has explored how these components can be integrated into a unified computational framework. This PhD proposal aims to develop an end-to-end framework for multi...
  </details>

- **2026-08-04** — Tomáš Burkert, Angelika Peljak-Łapińska, David Zelený — [M-GATE: Multilingual Grammar, Accuracy in Translation, and Efficiency Benchmark for Large Language Models](http://arxiv.org/abs/2608.03803v1)
  <details><summary>📄 Abstract</summary>
  Multilingual language models are deployed across a hundred or more languages, yet most benchmarks test whether a model can perform a task _in_ a language rather than whether it commands the language itself, conflating fluency with proficiency. We introduce M-GATE (Multilingual Grammar, Accuracy in Translation, and Efficiency), a benchmark of linguistic proficiency spanning 30 typologically diverse languages from high- to low-resource. M-GATE comprises three tasks: grammatical error detection on ...
  </details>

- **2026-08-04** — Junhao Chen, Mingjin Chen, Jingjia Mao et al. — [Agogic: Performance-Timed Music Tokens for LLM-Native Text-to-Symbolic-Music Generation](http://arxiv.org/abs/2608.03999v1)
  <details><summary>📄 Abstract</summary>
  Text-to-music language models begin with a choice usually made by default: how to tokenize music. Normally entangled with backbone, data, and recipe, its effect has never been measured in isolation. We fix pretrained Qwen3.5 (0.8B-27B), data, budget, and decoding, and swap only the representation across seven tokenizations, anchoring texture metrics to each representation's model-free ceiling. The ordering is clean and surprising: representation, not model size, is the binding variable for distr...
  </details>

- **2026-08-04** — Mercy Prasanna Ranjit, Anirban Porya, Sathvik Joel et al. — [CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement](http://arxiv.org/abs/2608.03890v1)
  <details><summary>📄 Abstract</summary>
  A clinically useful chest X-ray system must go beyond fluent report generation: it should classify findings with tunable decision thresholds, localize them spatially, and derive the anatomical measurements upon which many diagnoses depend. Today's Vision-Language Models (VLMs) treat these as separate problems, if they address them at all, leaving a gap between what radiologists need and what generative models provide. We introduce CARE-X, a chest X-ray VLM that narrows this gap by unifying auxil...
  </details>

- **2026-08-04** — Mateusz Smendowski, Kamil Faber, Piotr Nawrocki et al. — [PRISM: Powerful Time Series to Image (TS2I) Representations for Multivariate Anomaly Detection](http://arxiv.org/abs/2608.03926v1)
  <details><summary>📄 Abstract</summary>
  Time series anomaly detection (TSAD) underpins applications in predictive maintenance, finance, and cloud computing, however performance remains sensitive to representation choices, especially in multivariate settings. While transforming time series into images has shown success in forecasting and classification, it remains unclear how multivariate, high-dimensional series should be mapped to multi-channel images and whether vision backbones can match time-domain baselines in TSAD. We introduce ...
  </details>

- **2026-08-04** — Peijia Guo, Wenxuan Xie, ZiGuang Li et al. — [Beyond Representational Similarity: Source-Conditioned Description-Length Gain for Generative Plagiarism Detection and Candidate Source Reranking](http://arxiv.org/abs/2608.03859v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) pose challenges to academic integrity and peer review. Yet generative plagiarism detection remains an underexplored and largely unresolved challenge. Prior work on LLM-generated-text detection targets AI involvement, which may be permissible, rather than source reuse, while similarity-based methods struggle after extensive rewriting and multi-source synthesis. Motivated by the description-length view of probabilistic prediction, in which relevant side information can...
  </details>

- **2026-08-04** — Yuxiang Duan, Huining Li, Ao Li et al. — [AgenticVAU: Multi-Agent Explore-Verify Reasoning for Video Anomaly Understanding](http://arxiv.org/abs/2608.03779v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly understanding (VAU) focuses on comprehensively interpreting abnormal events in videos, requiring models to identify anomalous occurrences, discover their supporting evidence, and explain the underlying causes beyond simple anomaly detection. Existing VAU methods often rely on specialized training or limited observations, restricting generalization or evidence coverage. Although single-agent alternatives support adaptive video observation, they still integrate exploration, observati...
  </details>

- **2026-08-04** — Jinquan Zhang, Dongfu Yin, Run Yang et al. — [Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Robots Against Physical Attention Hijacking](http://arxiv.org/abs/2608.03231v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) policies promise general robotic manipulation, but their robustness against physical-world attacks remains fragile. In particular, we show that physically realizable adversarial patches can reliably induce failures by triggering a mechanism we call policy-critical action-to-vision attention hijacking, where action-conditioned attention is diverted from task-relevant regions to a localized patch. To demonstrate the threat, we propose Attention-Guided Semantic Disrupti...
  </details>

- **2026-08-04** — Haocheng Fu, Yuqi Qian, Luyao Wang et al. — [DHMark: Public-Key Watermarking for LLM-Generated Text via Diffie-Hellman-Guided Rejection Sampling](http://arxiv.org/abs/2608.03093v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) watermarking provides an important mechanism for tracing the provenance of generated text. Existing statistical watermarks are often effective and robust, but most of them rely on private detection keys, which centralizes verification and complicates public auditing. Recent public or publicly verifiable watermarking schemes improve key management, yet many of them rely on exact recovery of embedded cryptographic strings, making them fragile under token edits, truncatio...
  </details>

- **2026-08-04** — Sebastián Andrés Cajas Ordóñez, Agastya Munnangi, Aldo Marzullo et al. — [Agents Catching Agents: Shortcut Cascades and Benchmark Gaming in Clinical Multi-Agent Systems](http://arxiv.org/abs/2608.03744v1)
  <details><summary>📄 Abstract</summary>
  Clinical decision support is moving toward committees of language-model agents deliberating on a shared workspace. We ask whether such committees can be gamed by shortcuts, cues a benchmark rewards but a clinician would ignore. Across seven cohorts on six public datasets spanning text (MedQA-USMLE, MedMCQA, MIMIC-CXR reports), imaging (NIH ChestX-ray14, MIMIC-CXR-JPG, CheXpert) and tabular ICU records (SUPPORT2), Gemini committees resist these cues in isolation (flip 5-16%), yet a socially plaus...
  </details>

- **2026-08-04** — Nathan DeBardeleben — [Accountability Asymmetry and Structural Trust in Autonomous AI Systems](http://arxiv.org/abs/2608.03670v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI systems (such as AI agents) are increasingly being delegated operational work across scientific-computing infrastructure. Their assignments may begin with preparing an input or routing an alert and extend to changing a configuration or submitting a job. That delegation creates a practical trust problem because the institutional logic that lets us trust human operators does not transfer to optimization-based systems. A bad decision can damage a human operator's future, sometimes sev...
  </details>

- **2026-08-04** — Günther Schindler, Maximilian Schambach, Johannes Höhne — [Enhancing Tabular Learners with Context-Aware Semantic Embeddings](http://arxiv.org/abs/2608.03565v1)
  <details><summary>📄 Abstract</summary>
  While modern tabular learners excel at capturing statistical patterns, they frequently operate in a semantic vacuum, treating textual features as discrete symbols, ignoring the rich semantics inherent in feature names or cell entries. We propose CASE (Context-Aware Semantic Embeddings), a novel framework that bridges the gap between the semantic understanding of Large Language Models (LLMs) and the statistical capabilities of tabular learners. Unlike existing methods that embed rows in isolation...
  </details>

- **2026-08-04** — Zejun Liu, Jian Wu, Ru Peng et al. — [Can LLM design high-quality experiments? A Comprehensive and Systematic Benchmark on Autonomous Experimental Design](http://arxiv.org/abs/2608.03501v1)
  <details><summary>📄 Abstract</summary>
  AI for Research (AI4Research) leverages AI to automate and improve scientific workflows. While experimental design is a critical stage of the research process, prior work has focused primarily on code implementation and execution, overlooking the importance of this stage, and no benchmark exists to evaluate AI's ability to conduct systematic experiment design. To bridge this gap, we propose SCOPE, a Scientific COmprehensive Planning Evaluation Benchmark constructed from 300 high-quality latest p...
  </details>

- **2026-08-04** — Yu Pei, Cunming Zhang, Jeongju Sohn et al. — [Assessing Behavioral Validation in UI Component Test Suites Using Inferred Metamorphic Relations](http://arxiv.org/abs/2608.03337v1)
  <details><summary>📄 Abstract</summary>
  UI component libraries are commonly assessed using execution-based metrics such as statement and branch coverage, yet these metrics provide limited insight into whether tests verify the behavioral relations implied by component APIs and documentation. This paper presents an MR-based framework that uses inferred metamorphic relations (MRs) as an empirical behavioral reference, rather than a complete specification, for assessing UI component test suites. Given a component's source, documentation, ...
  </details>

- **2026-08-04** — Sicong Chang, Yidan Shen, Wen Yu et al. — [Lightweight Chunk Selection for Mobile Retrieval-Augmented Generation](http://arxiv.org/abs/2608.03148v1)
  <details><summary>📄 Abstract</summary>
  RAG improves the factual grounding of LLM by incorporating external knowledge, but deploying RAG on mobile and edge devices remains challenging because retrieved context increases computation and memory. A direct way to reduce this cost is to retain only one retrieved chunk before generation, but the top-ranked retrieved chunk is not always the most evidence-supporting one, since retrieval similarity does not necessarily imply evidential sufficiency. Existing context-reduction methods can improv...
  </details>

- **2026-08-04** — Huanglong Ji, Botong Zhao, Shujing Lv et al. — [LDU-Bench: Multimodal LLM Evaluation for Lithography Defect Understanding under Layout-Varying Circuit Backgrounds](http://arxiv.org/abs/2608.03078v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models have demonstrated strong defect recognition capability in industrial anomaly detection. However, in lithography review, merely determining whether an image contains a defect is insufficient for engineering inspection; models must also understand defect morphology, spatial location, and the potential causes supported by visible evidence. To this end, this paper proposes LDU-Bench, a multi-task multimodal benchmark for lithography defect understanding. Constructed ...
  </details>

- **2026-08-04** — Yichao Liu, Jiaxue Zhou, Weifeng Han et al. — [Breaking the trade-off between invisibility and sensitivity in electromagnetic sensing](http://arxiv.org/abs/2608.03042v1)
  <details><summary>📄 Abstract</summary>
  Weak electromagnetic signals demand highly sensitive sensors, yet increasing a sensor's sensitivity inevitably strengthens its interaction with the surrounding field, producing scattering that perturbs the very signals being measured. Conversely, existing cloaking strategies suppress scattering only by isolating the sensor from incident waves, thereby compromising signal reception. Resolving this long-standing trade-off between invisibility and sensitivity has remained an outstanding challenge. ...
  </details>

- **2026-08-04** — Jong Hak Moon, Minjun Kim, Minjun Kim — [Clinically-Grounded Hierarchical Classification for Consistent Chest X-ray Interpretation](http://arxiv.org/abs/2608.03016v1)
  <details><summary>📄 Abstract</summary>
  Accurate chest X-ray interpretation is inherently hierarchical. Clinical decisions depend not only on what abnormality is present but where it is situated, requiring reasoning from broad anatomical systems down to specific pathological findings. Yet existing automated systems largely treat this as a flat classification problem, failing to capture inter-level dependencies or enforce coherence between coarse and fine predictions. We propose CHASE (Classification with Hierarchical Analysis and Stru...
  </details>

- **2026-08-04** — Nicolas Zumarraga, Lorenzo Steno, Ning Wang et al. — [TimeRLM: Recursive Language Models Enable Precise Anomaly Localization in Long-Context Time-Series](http://arxiv.org/abs/2608.03391v1)
  <details><summary>📄 Abstract</summary>
  Precise anomaly localization over long-context time series is a crucial task in monitoring applications across clinical care, industrial operations, financial services, and logistics, where brief evidence may hide inside long spans of high-frequency data. Time-Series Language Models (TSLMs) are able to ingest time series data and verbalize findings on anomalies in natural language; however, recent benchmarks report a decrease in retrieval performance at long contexts, mirroring failure modes in ...
  </details>

- **2026-08-04** — Razieh Chalehchaleh, Reza Farahbakhsh, Noel Crespi — [Unequal Verdicts: Investigating Gender Bias in LLM-Based Fake News Detection](http://arxiv.org/abs/2608.03627v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used for automated fact-checking, yet their susceptibility to gender bias in this context remains underexplored. This study presents the first systematic investigation of gender bias in LLM-based fake news detection using real-world data. We augment the LIAR benchmark with three gender variants of speaker job titles (Neutral, Male, Female) for each statement to test whether veracity judgments vary solely based on gender presentation. Six state-of-the...
  </details>

- **2026-08-04** — Alex Kwon — [FACTWASH: Catching AI Rewrites That Wash Hearsay into Fact](http://arxiv.org/abs/2608.03372v1)
  <details><summary>📄 Abstract</summary>
  AI systems rewrite information constantly: conversations become stored memories, documents become answers. The rewrite can keep a claim while washing away what made it checkable, who said it, how sure they were, when it held. We call that failure factwashing, and release factwash, an open-source write-time gate that catches it deterministically, with named flags and evidence rather than an LLM judge. Building it answers a practical question: when does a cheap check suffice, and when do you need ...
  </details>

- **2026-08-04** — Zian Wang, Changchun Li — [DRPFNet: Dual-domain Residual Progressive Fusion Network for RGB-Thermal Object Detection](http://arxiv.org/abs/2608.03370v1)
  <details><summary>📄 Abstract</summary>
  RGB-thermal (RGB-T) object detection aims to fuse complementary information from visible and thermal modalities to achieve robust detection under varying illumination and weather conditions. Current methods typically employ attention mechanisms or transformers to perform cross-modal fusion independently at each feature scale, directly combining RGB and thermal features in the spatial domain. However, they still face significant limitations: cross-level knowledge inheritance caused by independent...
  </details>

- **2026-08-04** — Zihan Wang, Tong Liu, Zhiwei Wang et al. — [LocAnyMed: Vision-Language Grounding for Multimodal Medical Images](http://arxiv.org/abs/2608.03322v1)
  <details><summary>📄 Abstract</summary>
  Medical visual grounding connects free-form clinical queries to spatial evidence in medical images and is an important component of interpretable medical artificial intelligence. However, general-purpose grounding models are predominantly trained on natural images, while existing medical localization resources remain fragmented across imaging modalities, datasets, and task formulations. To address this gap, we construct LocAnyMed-200K, a multimodal medical visual grounding dataset containing app...
  </details>

- **2026-08-03** — Yuekun Wang, Mingfei Cheng, Xiaofei Xie — [PRWeaver: Evaluating LLM-Based Code Auditors against Long-Horizon Malicious Pull Requests](http://arxiv.org/abs/2608.02693v1)
  <details><summary>📄 Abstract</summary>
  LLM-based code auditors are increasingly integrated into pull-request (PR) workflows, yet their reliability against adversarial changes distributed across repository evolution remains poorly understood. We introduce PRWeaver, a benchmark of 208 execution-validated attacks from ten real-world repositories, each instantiated under four matched review renderings (832 renderings in total). We evaluate three PR-auditing agents across six auditor-model systems. Across all systems, decomposing an attac...
  </details>

- **2026-08-03** — Max Torop, Aria Masoomi, Jennifer Dy — [Inverted Detection and Control in Steering Vectors](http://arxiv.org/abs/2608.02957v1)
  <details><summary>📄 Abstract</summary>
  Steering vectors (SVs) are widely used to influence the expression of concepts (e.g., truthfulness) in large language model outputs. A key assumption underpinning SVs is that they are linearly discriminative with respect to the concept: representations of texts that exhibit the concept are more aligned with the SV than those that do not, motivating shifts along the positive or negative SV direction to respectively promote or suppress the concept. In this work, we identify an inverted detection-c...
  </details>

- **2026-08-03** — Tankun Li, Zhi Chen, Yaohua Tang — [LEAP: Lean Environment-Feedback via Adaptive Pruning for Code RL in GPU Kernel Generation](http://arxiv.org/abs/2608.01804v2)
  <details><summary>📄 Abstract</summary>
  Post-training large language models (LLMs) via reinforcement learning (RL) has significantly advanced code generation capabilities. To bypass the heavy memory footprint of critic networks, current state-of-the-art frameworks leverage critic-free paradigms like Group Relative Policy Optimization (GRPO) tied to rule-based verification sandboxes. However, applying these frameworks to low-level systems programming, such as CUDA kernel generation-presents severe challenges: binary pass/fail rewards i...
  </details>

- **2026-08-03** — Zibo Xiao, Haoyu Wang, Jun Sun — [$S^3$: Improving Agent Safety through Multi-Stage Defense](http://arxiv.org/abs/2608.02683v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents rely on multi-stage agentic workflows, with stages such as memory, planning, and tool execution, to accomplish complex tasks. However, risks may emerge at different stages, propagate across steps, and become difficult to detect and mitigate. Existing safety methods protect only isolated stages and are difficult to integrate, leaving agents without comprehensive protection throughout the workflow. To address these limitations, we introduce Stage-Specific Safety S...
  </details>

- **2026-08-03** — Priyanka Bajaj — [Evaluation Blindness: How Silent Measurement Failures Corrupt AI Systems from Training to Deployment](http://arxiv.org/abs/2608.02786v1)
  <details><summary>📄 Abstract</summary>
  AI systems can fail silently. The failure propagates through training loops, evaluation pipelines, and production monitoring stacks until downstream harm makes it visible. This paper introduces evaluation blindness: a measurement function M exhibits evaluation blindness with respect to failure class F when it produces readings indistinguishable from a healthy state while the system is actually failing, with no auxiliary signal flagging the gap.   The problem surfaces at two lifecycle stages the ...
  </details>

- **2026-08-03** — Saptarshi Neil Sinha, Tiago Kleist, Giorgio Trumpy — [A Human-in-the-Loop Deep Learning Framework for Color Reconstruction of Lenticular Films](http://arxiv.org/abs/2608.02835v1)
  <details><summary>📄 Abstract</summary>
  Historical lenticular films, such as those created with the Kodacolor process, encode color information in a distinctive spatial format. This structure requires specialized techniques for accurate color reconstruction. While recent signal processing approaches like doLCE and deep learning methods like deep-doLCE have advanced automated color recovery, they often fail with cases such as curved lenticules, low-contrast, or badly captured regions. We propose a human-in-the-loop (HITL) deep learning...
  </details>

- **2026-08-03** — Michael Farmer — [Abduction Without a Body? Representational Grounding and the Abduction Loop for Scientific Hypothesis Generation](http://arxiv.org/abs/2608.02505v1)
  <details><summary>📄 Abstract</summary>
  Can scientific abduction occur without continuous sensorimotor embodiment? Recent arguments in AI and philosophy of science hold that genuine hypothesis generation requires an agent continuously coupled to the physical world. We defend a narrower claim: online embodiment is not necessary for every abductive scientific act. Our focus is identity abduction: the inference that two independently developed structures are one object under an explicit correspondence, reached through representational gr...
  </details>

- **2026-08-03** — Weifeng Yuan, Wenbo Guo, Qingyun Du et al. — [Mutate to Bypass: Autonomous Endpoint Evasion via Knowledge-Driven Multi-Agent Orchestration](http://arxiv.org/abs/2608.01639v1)
  <details><summary>📄 Abstract</summary>
  Public reports and open-source resources expose many EDR evasion techniques, but it remains unclear whether commercial Endpoint Detection and Response (EDR) systems can withstand these documented attacks. Evaluating them requires turning fragmented security knowledge into working payloads and refining those payloads from opaque alerts, tasks that existing automation does not address. We present AutoBypass, a knowledge-grounded, closed-loop multi-agent framework for automated EDR resilience asses...
  </details>

- **2026-08-03** — Nicole Mitchell, Dhruv Agarwal, Maty Bohacek et al. — [Long-term Measurements: Towards a Longitudinal Understanding of Human-AI Interactions](http://arxiv.org/abs/2608.02491v1)
  <details><summary>📄 Abstract</summary>
  Language models have taken on the role of a very new type of technology, by virtue of their "human-ness" and rapid integration into users' daily lives. This combination of features can introduce longitudinal risks---cognitive, developmental and socio-affective changes in humans---that might not surface in short-term interactions, but can have lasting long-term effects on users. This forms the basis of a critical new mission for NLP: to pivot from static, short-term evaluations of text generation...
  </details>

- **2026-08-03** — Yonatan Ben Avraham, Baruch Binyaminov, Yehudit Aperstein — [UAV-Based Environmental Monitoring of Rip-Current Indicators Using Wavelet-Derived Texture Features](http://arxiv.org/abs/2608.02448v1)
  <details><summary>📄 Abstract</summary>
  Rip currents are recurrent coastal natural hazards that threaten beachgoers and create operational challenges for lifeguards and coastal managers. Reliable monitoring from standard RGB (red-green-blue) imagery acquired by unmanned aerial vehicles (UAVs) remains difficult because hazardous channels often appear as subtle gaps in breaking waves, foam texture, or sediment patterns, and these signatures are affected by illumination, sea state, and environmental noise. This study presents a physicall...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 57 papers

- **2026-08-05** — Yinghui He, Ling Yang, Jiarui Liu et al. — [Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning](http://arxiv.org/abs/2608.05139v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon reasoning in recent LLMs demands that the model switch between distinct skills inside a reasoning chain, such as first doing a math derivation, then using the result to plan a schedule. We call such problems cross-skill long-horizon tasks: multi-step tasks whose steps require different reasoning skills and depend on earlier outputs. Existing benchmarks often evaluate individual skills, lacking a principled way to measure how well a model switches between skills. We address this gap ...
  </details>

- **2026-08-05** — Yue Zhang, Yingzhao Jian, Yunqiu Xu et al. — [SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding](http://arxiv.org/abs/2608.05137v1)
  <details><summary>📄 Abstract</summary>
  Understanding 3D scenes is fundamental to embodied intelligence, requiring joint reasoning over heterogeneous information from multiple modalities, including visual and geometric cues. However, the relevance of these modalities often varies across queries. Existing Multimodal Large Language Models (MLLMs) typically rely on fixed modality combinations, overlooking query-dependent modality needs. Such a rigid design can introduce semantic noise from irrelevant modalities while underutilizing more ...
  </details>

- **2026-08-05** — Peiyan Li, Yuze Zhu, Yixiang Chen et al. — [BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation](http://arxiv.org/abs/2608.05042v1)
  <details><summary>📄 Abstract</summary>
  Leveraging pre-trained vision-language models (VLMs) to construct vision-language-action (VLA) models has emerged as a promising paradigm for 3D robot manipulation. However, existing 3D VLA methods remain data-hungry, exhibit limited generalization under distribution shifts, and lack explicit memory of past observations. These limitations hinder their application to data-scarce, open-world, and memory-dependent manipulation scenarios. Our previous work, BridgeVLA, improves data efficiency and ge...
  </details>

- **2026-08-05** — Junlin Han, Shengbang Tong, David Fan et al. — [Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality Synergy, Early Unification, and Recipes](http://arxiv.org/abs/2608.05000v1)
  <details><summary>📄 Abstract</summary>
  Vision offers a critical axis for advancing foundation models, driving a shift towards natively unified multimodal pretraining. Despite this momentum, the design space and the fundamental mechanisms of how modalities interact during unified training remain underexplored. We provide empirical clarity through a systematic exploration of multimodal pretraining. Our controlled experiments on both synthetic and large-scale real-world datasets yield four key insights into the physics of multimodal pre...
  </details>

- **2026-08-05** — Qingyan Wei, Guangzhao Li, Xiaobing Tu et al. — [STEP-OPD: Rethinking Output Targets and Internal Dynamics in On-Policy Distillation for Diffusion Models](http://arxiv.org/abs/2608.04887v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has become an effective approach for consolidating multiple task-specialized image generation models into a single student. However, existing OPD methods optimize the student mainly to match the teacher's output velocity, making the teacher the upper limit of the optimization objective. While output-level supervision alone leaves the student's blockwise representation evolution underconstrained, which weakens the transfer of capabilities that must be progressively de...
  </details>

- **2026-08-05** — Alessandro Pecchia, Andrea Lorenzoni, Alexander Croy et al. — [Atomic Scale Ordering of Sulfur Vacancies Enhances Charge Transport in Monolayer MoS$_2$](http://arxiv.org/abs/2608.04742v1)
  <details><summary>📄 Abstract</summary>
  Defect engineering in two-dimensional semiconductors has primarily focused on controlling the nature and concentration of atomic defects. Here, we show that the spatial arrangement of defects can be equally decisive in determining electronic transport. Using sulfur vacancies in monolayer MoS$_2$ as a model system, we investigate the impact of vacancy ordering through density functional theory, density functional tight-binding calculations, and quantum transport simulations. We demonstrate that a...
  </details>

- **2026-08-05** — Haotian Yang, Zhile Yang, Huiyu Zhou et al. — [DAC-Pose: Dual-Agent Collaborative Framework for Pose-Guided Human Generation](http://arxiv.org/abs/2608.04622v1)
  <details><summary>📄 Abstract</summary>
  AI agents have emerged as a powerful new paradigm in generative image synthesis, enabling systems to perform complex semantic reasoning rather than passive pixel-level mapping. In pose-guided human generation, conventional methods inevitably produce severe visual artifacts under drastic viewpoint shifts, fundamentally because they lack the cognitive capacity to logically deduce unseen regions and model complex spatial deformations. To bridge this gap, we propose DAC-Pose, a novel agent-driven mu...
  </details>

- **2026-08-05** — Yexing Du, Kaiyuan Liu, Youcheng Pan et al. — [Breaking the Curse ofMultilinguality inMany-to-Many Speech-to-Text Translation via a Resource-AwareMixture of Speech Encoders](http://arxiv.org/abs/2608.04586v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have achieved significant success in speech-to-text translation (S2TT). However, when processing multilingual speech inputs, a single speech encoder shared across all languages suffers from the curse of multilinguality: languages at different resource levels compete for limited representation capacity, leading to strong high-resource performance but substantial degradation on low-resource speech. To address this problem and improve multilingual consistenc...
  </details>

- **2026-08-05** — Javier Rodriguez-Juan, Hiba Arnaout, Jose Garcia-Rodriguez et al. — [ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance](http://arxiv.org/abs/2608.04524v1)
  <details><summary>📄 Abstract</summary>
  Synthetic generation of Cognitive Behavioral Therapy (CBT) sessions is challenged by two competing demands: adhering to strict therapeutic structure while modeling the resistant, unpredictable behavior of real patients. Existing script-based methods fail to capture dynamic therapeutic interactions, while multi-agent approaches struggle to adhere to CBT's sequential structure; both suffer from sycophancy, producing overly compliant patients that misrepresent real clinical settings. In this work w...
  </details>

- **2026-08-05** — Hyeonyu Kim, Sehwan Lim, Youngwon Choi et al. — [Not All Redundant Tokens Are Alike: Analyzing Visual Token Pruning through Token Roles](http://arxiv.org/abs/2608.04483v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) process an image as a sequence of visual tokens, which creates a substantial computational bottleneck during inference. Recent visual token pruning methods address this issue by removing seemingly redundant tokens, yet it remains unclear how these pruning decisions relate to the functional roles of visual tokens. In this work, we analyze visual token pruning through the lens of token roles identified by EmbedLens. We first show that representative pruning methods ex...
  </details>

- **2026-08-05** — Zhenyu Yi, Jianwei Xu, Yue Hu et al. — [EndoVLM: An Endoscopy Vision-Language Pre-training Model via Anatomy-Guided Sparsity and Progressive Alignment](http://arxiv.org/abs/2608.04472v1)
  <details><summary>📄 Abstract</summary>
  The development of foundation models (FMs) is crucial for advancing endoscopic image analysis. However, existing endoscopy FMs mainly rely on self-supervised learning from uni-modal images or videos, overlooking the rich semantic knowledge contained in clinical reports. Furthermore, effectively leveraging these records is hindered by a fundamental modality gap: structured anatomical descriptions are not naturally mapped to specific frames within the high-redundancy, uncurated visual streams. In ...
  </details>

- **2026-08-05** — Minseop Kim, Taekhyun Park, Kikun Park et al. — [Trie-Constrained Token Prediction with Hierarchy-Aware Semantic Alignment for HS Code Prediction](http://arxiv.org/abs/2608.04464v1)
  <details><summary>📄 Abstract</summary>
  Harmonized System (HS) code prediction (HSP) from commodity text is essential to international trade, and its importance continues to grow in port logistics. For the purposes of such prediction, recently, large language models (LLMs) have been actively investigated, owing especially to their strong language-understanding capabilities. However, their high computational cost limits deployment in constrained environments such as container terminals. Small language models (SLMs) offer a practical al...
  </details>

- **2026-08-05** — Gautam Neelakantan Memana — [A Counterexample to Fourier Alignment in Single-Neuron Modular Addition](http://arxiv.org/abs/2608.04451v1)
  <details><summary>📄 Abstract</summary>
  We give a negative solution to MAIS-O60. We first construct an example in which an initially active ReLU neuron becomes completely inactive in finite time and thereafter remains frozen at a limit whose Fourier energy is equally distributed among all nonzero real frequency classes. The counterexample holds on an open set of initial conditions and therefore occurs with positive probability under Gaussian initialization. An appendix prepared by GPT-5.6 Sol strengthens the counterexample by showing ...
  </details>

- **2026-08-05** — Kotaro Yoshida, Laura Gomezjurado Gonzalez, Yukinori Yamamoto et al. — [Looking in the Mirror: Introspecting Side-Effect Misalignments Induced by Fine-Tuning](http://arxiv.org/abs/2608.04347v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning enables a source model to acquire desired capabilities and behaviors in a target domain while retaining much of its general-purpose competence. However, this adaptation process can also degrade alignment properties that were present in the source model. Recent work has shown that large language models can be trained using LoRA-based modules known as introspection adapters (IAs) to describe behavioral changes induced by fine-tuning. However, existing studies primarily consider setting...
  </details>

- **2026-08-05** — Nripsuta Ani Saxena, Stelios Triantafyllou, Goran Radanović — [Responsibility in Multi-Agent Sequential Decision-Making: Comparing Human Judgments to Formal Models of Causal Attribution](http://arxiv.org/abs/2608.04318v1)
  <details><summary>📄 Abstract</summary>
  With the growing adoption of artificial intelligence in high-stakes decision-making, identifying the causes of outcomes--particularly failures--and determining who is responsible has become a critical concern. In this work, we examine how well formal definitions of \textit{responsibility attribution}, grounded in the framework of \textit{actual causality}, align with human judgments of responsibility. To this end, we conduct a large-scale survey to elicit human judgments of responsibility in mul...
  </details>

- **2026-08-05** — Yuexi Yang, Alyssa Wu, Ji Luo et al. — [RepoProbe: Benchmarking Architecture-Aware Repository Comprehension with Checklists](http://arxiv.org/abs/2608.04783v1)
  <details><summary>📄 Abstract</summary>
  The integration of Large Language Models (LLMs) into software engineering has shifted the focus from function-level generation to repository-scale assistance. However, existing benchmarks largely rely on bug reports from GitHub Issues, which often allow models to bypass genuine understanding via pattern matching on error logs. This misalignment under-measures Edit Bias, which refers to premature generation, where models prematurely propose code modifications instead of understanding the existing...
  </details>

- **2026-08-04** — Kishor Datta Gupta, Md. Mahfuzur Rahman, Fahad Rahman et al. — [TriCLE: Tri-Modal Vision-Language Reasoning for Edge-Deployed Fine-Grained Clustering](http://arxiv.org/abs/2608.04175v1)
  <details><summary>📄 Abstract</summary>
  Edge platforms used for aerial observation must interpret aircraft imagery under limited memory, limited compute, and intermittent connectivity. This setting is difficult for standard RGB-only recognition models and general-purpose vision-language models, especially when calibrated thermal and LiDAR aircraft data are unavailable. We present TriCLE, an application-oriented tri-modal vision-language system for aircraft taxonomic grouping under edge constraints. From a single RGB aircraft image, Tr...
  </details>

- **2026-08-04** — Yuanshen Guan, Zipeng Feng, Chengru Song et al. — [Latent Reward Registers for Diffusion Preference Alignment](http://arxiv.org/abs/2608.03929v2)
  <details><summary>📄 Abstract</summary>
  Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, presenting a severe temporal credit-assignment challenge across the multi-step denoising process. We propose Latent Reward Registers, a mechanism that estimates terminal preference directly from intermediate noisy latents by prepending learnable, position-free register tokens to the input sequence of a frozen Diffusion Transformer (DiT). This independent readout m...
  </details>

- **2026-08-04** — Teng Lin, Zhiyang Zhang, Yuyu Luo et al. — [Monte Carlo Tree Search for Table-to-Multimodal Report Generation](http://arxiv.org/abs/2608.04071v1)
  <details><summary>📄 Abstract</summary>
  Automatically generating professional multimodal reports comprising both textual analysis and visual charts from structured tabular data is a critical challenge in data intelligence. Existing methods suffer from fixed linear pipelines and isolated subtask processing, which hinder joint optimization of factual accuracy, visual quality, and narrative coherence. To address these issues, this paper proposes MCTS-Report, a Monte Carlo Tree Search (MCTS)-driven framework that formulates multimodal tab...
  </details>

- **2026-08-04** — Pervez Shaik, Prosenjit Biswas, Abhinav Thorat et al. — [ATLAS: Learning to Recommend Across Unseen Domains](http://arxiv.org/abs/2608.03899v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems remain domain-bound: a model trained on one interaction environment typically requires retraining or target-domain adaptation before it can operate on a new catalogue. A recommender trained on movies cannot be directly deployed to recommend groceries or video games. Existing approaches mitigate this by transferring restricted forms of recommendation knowledge, adapting to the target domain, or leveraging large language models (LLMs) for transferable representations. We instea...
  </details>

- **2026-08-04** — Adam Coscia, Sujata Duwal, Langdon Holmes et al. — [Calibrating Trustworthiness: Co-Designing Metrics and Visualizations for Evaluating LLMs in Education](http://arxiv.org/abs/2608.04006v1)
  <details><summary>📄 Abstract</summary>
  LLMs are reshaping educational technology, yet evaluating their responses for pedagogical alignment remains underexplored, relying heavily on the expertise of learning engineers building the technology. To bridge this gap, we explore trustworthiness as a structured lens for evaluation, leveraging existing measures of LLM trustworthiness to systematically identify potential pedagogical disruptions. Through a longitudinal co-design process with learning engineers developing an LLM-powered digital ...
  </details>

- **2026-08-04** — Mobina Kashaniyan, Ali Jannesari — [Interpretable Adaptive Sampling for LLM Test-Time Scaling](http://arxiv.org/abs/2608.03961v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling improves LLM reasoning by generating and aggregating multiple candidate answers, yet many pipelines use fixed per-query budgets that spend the same compute on easy and difficult prompts. These fixed budgets are also difficult to inspect because they do not explain why a given prompt receives a particular number of samples. We propose adaptive} test-time scaling with a lightweight fuzzy controller that maps interpretable signals, including estimated prompt complexity and model c...
  </details>

- **2026-08-04** — Yuanshen Guan, Zipeng Feng, Zhiwei Xiong et al. — [Latent Reward Registers for Diffusion Preference Alignment](http://arxiv.org/abs/2608.03929v1)
  <details><summary>📄 Abstract</summary>
  Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, presenting a severe temporal credit-assignment challenge across the multi-step denoising process. We propose Latent Reward Registers, a mechanism that estimates terminal preference directly from intermediate noisy latents by prepending learnable, position-free register tokens to the input sequence of a frozen Diffusion Transformer (DiT). This independent readout m...
  </details>

- **2026-08-04** — Mattias Luber, Timo Betz — [A Physics-Flavored Transformer Network for Parametrizing Contraction Dynamics of Engineered Skeletal Muscle Tissues](http://arxiv.org/abs/2608.03927v1)
  <details><summary>📄 Abstract</summary>
  Engineered Skeletal Muscle Tissues (ESMs) have become a key structure for biomedical disease modeling and pharmacological screening, yet their functional characterization often relies on simplistic metrics like peak force, discarding critical kinetic information. This is partially due to the high level of mathematical complexity which mechanistic models introduce to capture these dynamics. Hence, exactly the complexity prevents scalable application and widespread adaptation in the field. Here we...
  </details>

- **2026-08-04** — Matt Ratto, Abhishek Moturu, Daniel Silver — [Socially Grounded Agentic AI: Coordinating Plural Perspectives through Social Theory](http://arxiv.org/abs/2608.03910v1)
  <details><summary>📄 Abstract</summary>
  As AI systems are deployed across increasingly diverse social contexts, alignment can no longer be framed as the optimization of a single, unified set of values. Instead, systems must be able to recognize, represent, and respond to multiple legitimate perspectives. This has led to growing interest in pluralistic alignment, which seeks to move beyond one-size-fits-all models of appropriate behaviour. However, current approaches often lack a clear account of how values are socially organized, cont...
  </details>

- **2026-08-04** — Alberto Acedo — [Omega-S: A Functional Resilience Index for LLM Fine-Tuning](http://arxiv.org/abs/2608.03887v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a large language model on new data degrades what it previously learned. We present Omega-S, a drop-in penalty computed from the weight matrix alone: it needs no previous-task data, no Fisher matrix and no stored copy of the old weights. It is three lines in an existing training loop and adds under 4% to the cost of a step.   Retention. On Llama-3-8B with LoRA, fine-tuned from code to prose and measured by HumanEval over ten seeds, Omega-S retains more of the original capability than ...
  </details>

- **2026-08-04** — Pyrros Koussios, Chenhao Li, Xin Chen et al. — [Enhancing VLM Reward Models Through Structure-Aware Fine-Tuning](http://arxiv.org/abs/2608.03875v1)
  <details><summary>📄 Abstract</summary>
  Designing effective reward functions remains a major bottleneck in Reinforcement Learning (RL). Recent work uses large foundation Vision-Language Models (VLMs) as reward models, computing text-observation similarity to bypass manual reward engineering. Although promising, these rewards are often noisy and unreliable, limiting their direct utility during deployment. We present Structure-Aware Fine-Tuning (SAFT), a simple, self-supervised method that refines these imperfect reward signals online w...
  </details>

- **2026-08-04** — Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi et al. — [Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation](http://arxiv.org/abs/2608.03166v1)
  <details><summary>📄 Abstract</summary>
  Role-Playing Language Agents (RPLAs) are increasingly deployed in high-stakes applications such as healthcare assistance, customer support, and education, where maintaining consistent personas, ethical constraints, and behavioral coherence under adversarial pressure is critical. Existing evaluation approaches rely on static benchmarks or isolated single-turn prompts that fail to capture cumulative behavioral failures emerging over extended interactions.   We present a modular multi-agent platfor...
  </details>

- **2026-08-04** — Georgy Lukyanov — [Effort without Evidence](http://arxiv.org/abs/2608.03719v1)
  <details><summary>📄 Abstract</summary>
  Actions determine not only payoffs but what can be learned. I study communication across successive decision makers when hidden effort governs public evidence and a sender motivates her successor while underweighting effort cost. Common sender rankings can force every message into a Bayes-unavoidable nonidentifying region. If experimentation is costly, strong motivation can make persuasive encouragement incredible and produce inactivity after a confounded failure. If maximal effort is technologi...
  </details>

- **2026-08-04** — Abraham Camelo-Guerrero, Jairo Diaz-Rodriguez — [How Closely Do LLM Reviews Align with Human Peer Review?](http://arxiv.org/abs/2608.03659v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate scientific reviews, yet existing evaluations rarely examine whether different providers align with both conference decisions and human reviewing priorities within the same controlled setting. We compare reviews from OpenAI GPT-5.4, Google Gemini 3.1 Pro Preview, and Anthropic Claude Opus 4.6 with human reviews and final decisions for 300 topic-matched ICLR 2026 submissions, equally divided among oral, poster, and rejected papers. Eac...
  </details>

- **2026-08-04** — Eleftherios Batzolis, George Drosatos, Vassilis Katsouros et al. — [A Security-Oriented Lifecycle Model for Large Language Model Systems](http://arxiv.org/abs/2608.03626v1)
  <details><summary>📄 Abstract</summary>
  Large language models are being integrated into critical infrastructure and enterprise workflows at unprecedented scale,yet the lifecycle frameworks governing their development and operations were designed for operational efficiency rather than security analysis. As a result, security-relevant activities such as data provenance verification, artifact signing, agentic permission control, and decommissioning are often left implicit or assumed to receive due care. Governance frameworks, in turn, or...
  </details>

- **2026-08-04** — Lydia Manikonda, Dominique Outlaw — [Policy Fragmentation or Institutional Alignment? Institutional Governance of AI in Universities and Business Schools](http://arxiv.org/abs/2608.03584v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) is rapidly transforming high-skilled domains, requiring higher education institutions (HEI) to balance the teaching of foundational principles with the integration of emerging tools to ensure workforce readiness. While HEI are increasingly adopting AI, many continue to grapple with how it should be incorporated into curricula and governed through policy, especially when such policies are set at different levels of an institution. This research analyzes AI policies ac...
  </details>

- **2026-08-04** — Alexander M. Fichtl, Lukas Ellinger, Josefin Kelber et al. — [AI-Assisted Peer Review Across Research Communities: From Reviewer AI Policies to LLM Review Quality](http://arxiv.org/abs/2608.03581v1)
  <details><summary>📄 Abstract</summary>
  AI-assisted peer review is increasingly discussed and adopted as a tool to support the scientific publishing process, yet there is little systematic understanding of how publication venues regulate its use or of how capable current AI review systems are. We address these questions by first surveying reviewer-facing AI policies across 111 leading AI/NLP conferences and medical journals, revealing substantial regulation differences between the two communities. Second, we evaluate AI-generated peer...
  </details>

- **2026-08-04** — Xiang Li, Pengcheng Wang, Huazheng Wang et al. — [Pin Once, Swap Light: Subspace-Aligned Centroid-Residual Training for Efficient Ultra-LoRA Serving](http://arxiv.org/abs/2608.03579v1)
  <details><summary>📄 Abstract</summary>
  Modern multi-tenant Low-Rank Adapters (LoRAs) serving systems concurrently host tens to hundreds of LoRA adapters. Though powerful, this introduces a critical system dilemma between serving efficiency and task performance: higher-rank adapters generally achieve better downstream task performance, but their GPU VRAM footprint and Host-to-Device PCIe swapping overhead severely constrain scalability. Conversely, ultra-low-rank adapters ($r \le 2$) minimize both VRAM footprint and PCIe transfer over...
  </details>

- **2026-08-04** — Zixuan Liu, Fangzheng Wu, Brian Summa et al. — [Robust General Utility for Reinforcement Learning](http://arxiv.org/abs/2608.03562v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) with general utility extends classic RL by optimizing an arbitrary utility functional of the policy-induced occupancy measure, thereby enabling a broader range of applications. However, previous work on general utility RL typically assumes the evaluation utility is fixed and correctly specified. In practice, the utility used at deployment can deviate from the training one, creating a robustness gap that prior work does not address. Motivated by this, we propose robust...
  </details>

- **2026-08-04** — Ruolei Zhang, Teddy Njuguna, Yue Feng — [Cross-Lingual Bias in Large Language Models: A Comparative Analysis of English and Swahili](http://arxiv.org/abs/2608.03532v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed in multilingual contexts, yet safety alignment and bias evaluation remain overwhelmingly English-centric. We investigate whether social biases generalise across languages by submitting 4,900 symmetric English--Swahili prompt pairs to GPT-5.2 and Gemini 2.5 Flash across nine demographic bias axes, yielding 19,600 completions evaluated for stereotype prevalence, sentiment, refusal behaviour, and cross-lingual semantic similarity. Our findings show th...
  </details>

- **2026-08-04** — Qiming Li, Shujie Hu, Haohan Liu et al. — [MT-Web2Code: Benchmarking Coding Agents on Multi-Turn Regional Reconstruction and Localized Modification](http://arxiv.org/abs/2608.03474v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Large Vision-Language Models (LVLMs) have demonstrated impressive capabilities in web UI generation. However, existing benchmarks predominantly focus on single-turn full-page generation from scratch, overlooking the iterative workflow of real-world frontend engineering, where developers repeatedly reconstruct missing regions and modify localized elements within existing codebases. To bridge this gap, we introduce MT-Web2Code, the first multimodal coding benchmark for multi-tur...
  </details>

- **2026-08-04** — Boyan Li, Zhuowen Liang, Yupeng Xie et al. — [DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous Workspaces](http://arxiv.org/abs/2608.03451v1)
  <details><summary>📄 Abstract</summary>
  Data agents enable natural-language analytics over organizational workspaces, where relevant evidence may be scattered across databases, structured files, long documents, and multimedia. Existing benchmarks largely isolate structured querying, retrieval, or open-ended analysis, leaving heterogeneous evidence discovery, complete tabular outputs, and deterministic evaluation insufficiently unified. We introduce DataSpace, a benchmark in which data agents produce verifiable tabular results from tas...
  </details>

- **2026-08-04** — Adnan Al Ali, Kathy Hämmerl, Jindřich Libovický et al. — [Predicting Multilingual Classification and Translation Performance of LLMs with Cross-Lingual Alignment $\unicode{x2013}$ Is English Enough?](http://arxiv.org/abs/2608.03446v1)
  <details><summary>📄 Abstract</summary>
  Multilingual large language models (LLMs) have been shown to perform better on non-English classification tasks when the representations of the given language are more aligned to English within the model. Several cross-lingual alignment (CLA) scores have been proposed for use with LLMs, along with multiple approaches for extracting embeddings from the models. We provide a comparative analysis of 27 CLA score variants, examining how they differ and how well each predicts downstream performance ac...
  </details>

- **2026-08-04** — Eugene Lee, Oseong Choi, Byungsoo Kang et al. — [LLM-Derived Priors for Thompson Sampling in Cold-Start Comment Recommendation](http://arxiv.org/abs/2608.03382v1)
  <details><summary>📄 Abstract</summary>
  Multi-armed bandit algorithms, especially Thompson sampling, are widely used in online recommendation. Despite their ability to adapt from online feedback, these methods often suffer from cold-start limitations when newly introduced arms have little or no interaction history. In our setting, the candidate arms are user-generated textual comments, whose semantic content can reveal a title's appeal before sufficient interaction feedback is available. We therefore use large language models (LLMs) t...
  </details>

- **2026-08-04** — Jing Dai, Qibin Zhang, Weiwei Zhou et al. — [CIGTSurv: Clinical Information Guided Tri-modal Survival Prediction with Local Prototype Association and Global Feature Alignment](http://arxiv.org/abs/2608.03247v1)
  <details><summary>📄 Abstract</summary>
  Multimodal learning has significantly advanced survival prediction by integrating pathology images with genomic data. However, clinical information, despite its critical role in reflecting a patient' s overall health, remains underutilized due to its discrete, sparse, and low-dimensional nature. Furthermore, the inherent heterogeneity across these modalities pose significant challenges in modeling cross-modal interactions. In this paper, we propose CIGTSurv, a Clinical Information Guided Tri-mod...
  </details>

- **2026-08-04** — Ming Shen, Chao Shang, Sadat Shahriar et al. — [Relational Priors as Convergence Pressure in LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2608.03239v1)
  <details><summary>📄 Abstract</summary>
  Large language model-based multi-agent systems (LLM-MAS) are designed through roles, debate protocols, and aggregation rules. These choices create implicit social expectations: agents may be expected to trust, challenge, defer to, or collaborate with peers. We study the effects of making inter-agent relation semantics explicit. We use a minimal signed-network formulation of relational priors and inject natural-language renderings into agent system prompts while holding the task protocol fixed. A...
  </details>

- **2026-08-04** — Tianbao Jiang, Weicong Ni, Gerard de Melo et al. — [Aligning Large Vision-Language Models at Test Time: A Trajectory-Guided Structured Sampling Approach](http://arxiv.org/abs/2608.03204v1)
  <details><summary>📄 Abstract</summary>
  Post-training reinforcement learning (RL) algorithms are commonly used to align large vision-language models (LVLMs) with human intent and the requirements of visual reasoning tasks. However, existing RL-based alignment methods are often resource-intensive and encounter mismatches between training objectives and inference-time distributions. To bridge this gap, we propose a novel test-time alignment approach that leverages trajectory-guided structured sampling for dynamic inference-time refineme...
  </details>

- **2026-08-04** — Xiangyun Huang, Xiangchen Wang, Runfeng Lin et al. — [From Routes to Steps: Separating Semantic Progress from Local Execution in Vision-and-Language Navigation](http://arxiv.org/abs/2608.03143v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-Language Navigation (VLN) requires an agent to follow a route-level instruction by executing its constituent steps from egocentric visual observations. Existing VLM-based navigators typically supervise both capabilities through next-action prediction alone, making progress-tracking errors difficult to distinguish from execution errors. When an agent deviates from the route, a corrective action label may recover the next movement but does not indicate whether the agent selected the wro...
  </details>

- **2026-08-04** — Binglei Li, Mengping Yang, Zhiyu Tan et al. — [DiverseDiT++: Quantifying, Analyzing, and Promoting Representation Diversity in Diffusion Transformers](http://arxiv.org/abs/2608.03082v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Diffusion Transformers (DiTs) have enabled remarkable progress in visual synthesis, benefiting from their superior scalability. To facilitate DiTs' capability of capturing meaningful internal representations, recent works such as REPA incorporate external pretrained encoders for representation alignment. However, the underlying mechanisms governing representation learning within DiTs remain poorly understood in the community. To this end, this paper first presents a systematic...
  </details>

- **2026-08-04** — Jingwei Zhao, Gus Xia, Ziyu Wang et al. — [Learning Music Style for Piano Arrangement Through Cross-Modal Bootstrapping](http://arxiv.org/abs/2608.03050v1)
  <details><summary>📄 Abstract</summary>
  What is music style? Though often described using text labels such as "swing," "classical," or "emotional," the real style remains implicit and hidden in concrete music examples. In this paper, we introduce a cross-modal framework that learns implicit music styles from raw audio and applies them to symbolic music generation. Inspired by BLIP-2, our model leverages a Querying Transformer (Q-Former) to extract style representations from a large, pre-trained audio language model (LM), and further a...
  </details>

- **2026-08-04** — Yizhuo Jia, Jingyun Hua, Yuanxing Zhang — [CAPE-T2V: Captioner-Anchored Prompt Enhancement toward Two-Sided Conditioning Alignment in Text-to-Video Generation](http://arxiv.org/abs/2608.03046v1)
  <details><summary>📄 Abstract</summary>
  Text-to-video (T2V) diffusion transformers (DiTs) are trained with detailed video captions, whereas inference often relies on user prompts rewritten by a prompt enhancer (PE). Prior work has improved generation by optimizing the PE, the DiT, or both; some methods have also sought to narrow the training-inference mismatch through shared schemas. Yet even within a shared schema, inference-time PE outputs and DiT training captions may still differ in detail selection, information organization, desc...
  </details>

- **2026-08-04** — Seth Grief-Albert, Jessica Bo, Difan Jiao et al. — [Emulate or Estimate? The Divergent Strengths of Base and Post-Trained Language Models for Opinion Simulation](http://arxiv.org/abs/2608.03044v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to simulate human opinions, but prior work reports conflicting results: some studies find promising alignment with human survey data, while others find persona collapse and weak demographic sensitivity. We show that much of this conflict stems from conflating two distinct tasks. We call the first task emulation, in which models generate individual responses that aggregate into a population distribution. We call the second task estimation, in which mode...
  </details>

- **2026-08-04** — Ruirui Zhang, Zhengkai Zhao, Pan Gao — [MultiCompose: Multi-Concept Personalized Composition with Per-Subject Attribute Binding](http://arxiv.org/abs/2608.03708v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion models enable personalization of specific visual concepts from a small number of reference images. However, generating a single image that contains multiple personalized subjects, each bound to user-specified attributes such as clothing, accessories, and held objects, remains largely unaddressed. Without explicit spatial constraints, concurrently activated concept checkpoints produce overlapping cross-attention responses, causing per-subject identity degradation and attri...
  </details>

- **2026-08-04** — Yixin Bu, Runze Xia, Guanyun Zou et al. — [DUD: Decoupled Update Dynamics for Reliable Uncertainty Quantification in Large Language Models](http://arxiv.org/abs/2608.03411v1)
  <details><summary>📄 Abstract</summary>
  Accurate Uncertainty Quantification (UQ) is critical for reliable deployment of Large Language Models (LLMs), yet traditional probability-based metrics often fail to capture the model's true epistemic state. While recent mechanistic approaches leverage hidden state dynamics, they typically aggregate residual stream updates, conflating the distinct roles of parametric memory (Feed-Forward Networks) and contextual processing (Attention). We argue that this aggregation obscures fine-grained mechani...
  </details>

- **2026-08-03** — Kyeongbin Kim, Daniel McCarthy, Dokyun Lee — [Forecasting Revenue with its Customer-Base Drivers: When and Why Coordination Helps](http://arxiv.org/abs/2608.02911v1)
  <details><summary>📄 Abstract</summary>
  Revenue forecasts guide acquisition budgets, demand planning, and customer-based valuations, yet an aggregate forecast does not show whether change reflects acquisition, repeat purchasing, spending per order, or offsetting movements. Using weekly transaction panels for 966 companies in 25 industries, the authors develop the Customer-Based Multi-task Transformer (CBMT), which learns shared structure, retains separate primitive forecasts, and aligns their combination with downstream revenue. CBMT'...
  </details>

- **2026-08-03** — Nina Bodelot, Soufiane Belharbi, Eric Granger — [Test Time Adaptation Methods for Point Cloud Registration in Laparoscopic Surgery](http://arxiv.org/abs/2608.02883v1)
  <details><summary>📄 Abstract</summary>
  3D point cloud registration in laparoscopic surgery estimates the transformation between an intraoperative organ reconstructed from video and its preoperative mesh. Because ground-truth transformations are unavailable for real data, supervised networks are trained on synthetic organ pairs. At test time, real reconstructions differ from synthetic data and are noisy, sparse, and occluded, which degrades correspondence estimation. Test-time adaptation (TTA) can reduce this domain shift, but existin...
  </details>

- **2026-08-03** — Dayi Yao, Zijie Zhou — [Efficiency and Cost Alignment in Batched LLM Serving via Resource-Fair Scheduling](http://arxiv.org/abs/2608.02244v1)
  <details><summary>📄 Abstract</summary>
  This paper studies a resource-allocation inefficiency in batched large language model (LLM) serving: heterogeneous requests that share a decode batch impose max-driven computational costs on one another. Because the wall-clock cost of a batch step is largely governed by the largest active KV-cache footprint, a short request co-batched with a long request can experience latency and GPU-resource consumption disproportionate to its own token workload. We formalize this phenomenon as a resource-fair...
  </details>

- **2026-08-03** — Jiajia Song, Bobo Li, Haiwen Yi et al. — [From Profiling to Synthesis: Benchmarking Implicit Behavioral Alignment in Personalized LLM Agents](http://arxiv.org/abs/2608.02171v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models have enabled increasingly capable autonomous agents, yet personalization remains critical for making such agents practically useful. Recent benchmarks have begun evaluating personalization in agents, but they largely rely on static preference snapshots, fixed interaction logs, or question answering over predefined user profiles. Such designs fail to capture the complexity of evolving user preferences and neglect preference-conditioned task execution-a discrepancy we term as...
  </details>

- **2026-08-03** — Hongzhan Chen, Xiaoyu Liu, Dengming Zhang et al. — [Cross-Domain Hybrid OPD for Generalizable Search Agents](http://arxiv.org/abs/2608.02101v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Reinforcement Learning (RL) have substantially improved the capabilities of autonomous search agents, enabling sophisticated planning, and iterative retrieval over dynamic information sources. However, optimizing language models for specialized search behaviors often incurs an alignment tax, where gains in search performance come at the expense of general-purpose capabilities, limiting their effectiveness as universal assistants. In this technical report, we present the traini...
  </details>

- **2026-08-03** — Wei Jia, Zhicong Lu, Yu Chen et al. — [CAVE: Competence-Aware Visual Boundary Evidence Alignment for Video Temporal Grounding](http://arxiv.org/abs/2608.02078v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have achieved substantial performance gains in Video Temporal Grounding (VTG) through reinforcement learning (RL). However, existing methods primarily rely on outcome correctness rewards that evaluate only the final predicted intervals, leaving boundary-related visual evidence and its correspondence with timestamp predictions insufficiently constrained. In this paper, we delve into timestamp prediction and its underlying boundary-level visual evidence, showin...
  </details>

- **2026-08-03** — Zhu Chen, Dingkun Liu, Yuheng Chen et al. — [STEAM:ASpatio-TEmporal Alignment Mixture-of-Experts Model with Hierarchical Pre-training for EEG Decoding](http://arxiv.org/abs/2608.02070v1)
  <details><summary>📄 Abstract</summary>
  Brain-computer interfaces (BCIs) have been widely used in motor rehabilitation, disease diagnosis, and other neural engineering scenarios. However, conventional neural signal decoding algorithms often suffer from limited generalizability and high adaptation costs, motivating recent interest in BCI foundation models. Existing approaches still struggle to jointly achieve general transferability, accurate decoding, and efficient downstream adaptation. We present STEAM, a hierarchical transfer frame...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 76 papers

- **2026-08-05** — Atul Anand, Sourav Chattaraj — [Diagnosing Tool-Selection Reasoning in LLM Agents with Canary Tools](http://arxiv.org/abs/2608.04719v1)
  <details><summary>📄 Abstract</summary>
  Agent evaluations tell us that a model picked the wrong tool, but rarely why. We introduce canary tools: diagnostic probe tools planted in an agent's Model Context Protocol (MCP) tool set, each engineered to probe one specific tool-selection weakness. A six-type taxonomy (semantic decoys, parameter traps, capability mirages, prerequisite blindness, temporal decoys, and granularity traps) turns a single "wrong tool" outcome into a multi-dimensional profile of how a model reasons about tools. We e...
  </details>

- **2026-08-05** — Soha Hussein, Stephen McCamant, Kelton OBrien et al. — [Technical Report: A Formal Semantics for Java Symbolic Evaluation using Large-Block Encoding](http://arxiv.org/abs/2608.04513v1)
  <details><summary>📄 Abstract</summary>
  Symbolic execution plays a critical role in software reliability, as they are used to find bugs, generate test cases, and provide correctness guarantees, particularly for safety-critical systems. Yet their own correctness is rarely subject to formal scrutiny, as it is typically established empirically by evaluating tool behavior across many programs. This leaves open the possibility that the tools themselves introduce unsoundness, potentially invalidating the verification results they produce an...
  </details>

- **2026-08-05** — Xiaokai Rong, Hridya Dhulipala, Aashish Yadavally et al. — [AdaptAgent: A Multi-agent, Domain-Guided Reasoning Framework for Code Adaptation](http://arxiv.org/abs/2608.04459v1)
  <details><summary>📄 Abstract</summary>
  Developers often need to adapt into their projects the code generated from LLMs or code snippets from online forums. However, integrating them into an existing repository remains challenging in a manual process. A successful integration typically requires more than copying code as a user must produce correct adapting changes at a designated location in the target repository. We formalize this as the code adaptation problem: given a snippet, functional intent, a target repository, and an adaptati...
  </details>

- **2026-08-05** — Zhuoran Zhang, Bowen Li, Jingcheng Ju et al. — [FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory](http://arxiv.org/abs/2608.04530v1)
  <details><summary>📄 Abstract</summary>
  GUI agents must remember both useful experience from earlier tasks and unfinished progress in the current interaction. Latent memory offers a compact solution by compressing multimodal trajectories into a few continuous tokens. Existing methods, however, usually map each trajectory to one fixed memory block and train it mainly through next-action supervision. This creates three practical problems: important details may be lost during compression, the same memory block must serve different decisi...
  </details>

- **2026-08-05** — Shengcao Cao, Tanmaya Shekhar Dabral, Zhongli Ding et al. — [CoCo-IR: Contextual Composed Image Retrieval](http://arxiv.org/abs/2608.05149v1)
  <details><summary>📄 Abstract</summary>
  Current instruction-based image retrieval systems are powerful but limited to single-turn interactions, failing to capture the iterative nature of complex, real-world visual searches. To overcome this limitation, we introduce Contextual Composed Image Retrieval (CoCo-IR), a novel task that enables users to progressively refine search results through interactions. We address this new task by proposing a new model based on a Large Multimodal Model (LMM) that functions as a context-aware reasoner f...
  </details>

- **2026-08-05** — Tongle Wu, Huanyu Dong, Ying Sun et al. — [MALT: Lightweight Curvature-Aware Muon via Diagonal Preconditioning](http://arxiv.org/abs/2608.05088v1)
  <details><summary>📄 Abstract</summary>
  Muon has recently emerged as a promising alternative to AdamW for language model pretraining by orthogonalizing momentum matrices using Newton-Schulz iterations. Although Muon mitigates gradient anisotropy, it does not explicitly account for the curvature geometry of the loss landscape and may therefore remain sensitive to curvature anisotropy. We bridge this gap by proposing MALT (Muon Augmented by Lightweight Two-sided Preconditioning), which uses lightweight diagonal preconditioners to reduce...
  </details>

- **2026-08-05** — Alessio Baldazzi, Sonia Mazzucchi, Lorenzo Pavesi — [Universal linear manipulation via routing and projective measurements](http://arxiv.org/abs/2608.05003v1)
  <details><summary>📄 Abstract</summary>
  Multiport interferometers with $N$ ports are basic devices in both classical and quantum photonics. Ideally, they implement a linear unitary transformation between the input and output electric field vectors with $N$ components, each associated with a spatial mode of classical coherent light or a single photon. Standard designs for a fully reconfigurable universal multiport interferometer are given by the Reck or the Clements schemes. In this work, we introduce routing schemes to implement a gen...
  </details>

- **2026-08-05** — Vladimir Druskin, Shari Moskow, Mikhail Zaslavsky — [Data generated internal solutions for the plasma wave equation: error bounds and numerical experiments in two dimensions](http://arxiv.org/abs/2608.04989v1)
  <details><summary>📄 Abstract</summary>
  We consider the computation of internal solutions for a time domain plasma wave equation with an unknown potential $q$ from boundary response data. The internal solutions are computed by transforming known background snapshots using the Cholesky decomposition of the data-driven Gramian, or mass matrix. It was recently shown that in one dimension these data generated internal solutions converge in $L^2$ at order $\sqrtτ$ for well chosen initial waves. Here we study the internal solution reconstru...
  </details>

- **2026-08-05** — Grzegorz Gruszczynski, Pawel Olszowiec, Michal Byra et al. — [Training Crossroads for Recurrent Vision Transformers: Recurrence, Neural ODEs, and Deep Supervision](http://arxiv.org/abs/2608.04879v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) achieve strong image-recognition performance, but their parameter count grows linearly with depth when each block is independently parameterized. Single-block recurrent ViTs (bViT) remove this growth by repeatedly applying one shared block. Rather than proposing a new architecture, we fix a bViT and provide a controlled empirical characterization of three training and inference regimes under a common CIFAR-100 protocol, asking: (i)~when does recurrence beat independent...
  </details>

- **2026-08-05** — Masahiro Fujita — [Decentralization of Agenda-Setting Power and Domain-Selective Bridging: Algorithm Design Beyond the Echo Chamber Debate](http://arxiv.org/abs/2608.04774v1)
  <details><summary>📄 Abstract</summary>
  Echo chambers are an inevitable consequence of the human cognitive system being evolutionarily designed to prioritize processing of high-relevance information at the small-group scale, combined with algorithms that optimize engagement as their sole objective. Conventional prescriptions that normatively criticize echo chambers and demand individual behavioral change have low feasibility given these cognitive constraints. This paper constructs an Agenda Democratization Index (ADI) that quantities ...
  </details>

- **2026-08-05** — Houze Xu, Jizhong Li, Ziyi Ye — [Explicit Language Memory for Long-Horizon Planning in Vision-Language-Action Models](http://arxiv.org/abs/2608.04765v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models provide a unified paradigm for connecting visual perception, language understanding, and robotic control. However, existing VLA models still face major challenges in long-horizon tasks: sparse expert demonstrations constrain cross-task compositional generalization; the non-Markovian nature of long-horizon tasks makes it difficult for policies conditioned only on current observations to maintain temporal consistency; limited closed-loop error correction allows ...
  </details>

- **2026-08-05** — Hakyeong Kim, Ruicheng Wang, Chengtang Yao et al. — [Dense Metric Depth Completion from Sparse Direct Time-of-Flight Sensors](http://arxiv.org/abs/2608.04737v1)
  <details><summary>📄 Abstract</summary>
  Direct Time-of-Flight (dToF) sensors provide highly accurate metric depth and are more robust than indirect ToF systems in challenging real-world conditions. However, their high manufacturing cost and limited photodiode array size produce depth maps that are extremely sparse, low-resolution, and noisy, making them unsuitable for VR/XR, robotics, and 3D perception tasks that require dense metric depth. Existing monocular and depth completion methods struggle to handle the unique sampling patterns...
  </details>

- **2026-08-05** — Xuzheng Yang, Jun Ling, Tao Huang et al. — [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](http://arxiv.org/abs/2608.04698v1)
  <details><summary>📄 Abstract</summary>
  We tackle the challenging yet underexplored task of Generalized Referring Expression Comprehension (GREC), which requires a model to localize the object described by a textual expression when it exists (positive sample) and to refuse output when it does not (negative sample). Although Multimodal Large Language Models (MLLMs) excel at localizing existing objects, they often fail to reject nonexistent ones due to the absence of negative samples during training, producing hallucinated bounding boxe...
  </details>

- **2026-08-05** — Ian B. de Haan, Peter van der Putten, Max van Duijn — [Evaluating Theory of Mind in Reasoning Models: Robustness over Reasoning](http://arxiv.org/abs/2608.04646v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently shown strong performance on Theory of Mind (ToM) tests, prompting debate about the nature and validity of the underlying capabilities. At the same time, reasoning-oriented LLMs trained via reinforcement learning with verifiable rewards have demonstrated notable improvements across a range of benchmarks. In this work, we examine the behavior of such reasoning models in ToM tasks using novel adaptations of machine psychological experiments together with r...
  </details>

- **2026-08-05** — Zehao Bao, Shujun Guo, Bruce X. B. Yu — [Visual Anchoring in Diffusion: Multimodal Zero-Shot Skeleton Action Recognition](http://arxiv.org/abs/2608.04623v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot Skeleton Action Recognition (ZSAR) remains ambiguous when unseen actions share similar skeleton joint dynamics but differ in objects or scene context. RGB provides these missing cues, yet existing multimodal methods typically maintain independent skeleton and RGB scoring branches and fuse their outputs. Without using unlabeled test data for adaptation or fusion calibration, a fixed fusion weight cannot capture class-pair-dependent modality reliability, while an adaptive rule lacks targ...
  </details>

- **2026-08-05** — Zhengpei Hu, Kai Li, Dapeng Fu et al. — [Relevant but Incomplete: Referential Dangling as a Paradigm-Level Failure Mode in Hard Prompt Compression](http://arxiv.org/abs/2608.04569v1)
  <details><summary>📄 Abstract</summary>
  Hard prompt compression reduces long-context inference cost by independently scoring tokens, sentences, or chunks and retaining the highest-scoring units under a budget. We identify a structural failure in this procedure: independent selection can split dependent evidence pairs, retaining one member while deleting the other. When retained text contains an answer but deleted text defines the entity needed to interpret it, we call the result referential dangling. At a compression ratio of 0.30, Be...
  </details>

- **2026-08-05** — Daijing Shi, Hongxiao Zhao, Yihan Fu et al. — [MCHA: A Memory-Centric Hierarchical Architecture for Parallel-Sequential Computing](http://arxiv.org/abs/2608.04443v1)
  <details><summary>📄 Abstract</summary>
  Emerging workloads, such as Multi-Agent Reinforcement Learning (MARL), large-scale neuromorphic computing, and probabilistic graphical models, intrinsically exhibit parallel-sequential computing patterns. While these tasks demand massive parallelism to achieve high throughput, they are severely bottlenecked by irregular data access patterns centralized to main memory. Consequently, conventional architectures face fundamental limitations when executing these workloads, primarily manifesting as gl...
  </details>

- **2026-08-05** — Tian Jin, Ruikang Zhang, Zefeng Zhao et al. — [HyPASE: Hyperbolic Geometry for Parameter-Efficient Speech Emotion Fine-Tuning Framework for Large Audio-Language Models](http://arxiv.org/abs/2608.04351v1)
  <details><summary>📄 Abstract</summary>
  Large Audio-Language Models (LALMs) excel at general speech understanding; however, adapting them to fine-grained tasks like Speech Emotion Recognition (SER) remains a significant bottleneck. Current Parameter-Efficient Fine-Tuning (PEFT) methods typically operate in flat Euclidean space, and this geometry fails to capture the multi-granularity nature of emotion cues, which range from low-level prosody to high-level semantics. To address this, we propose HyPASE, a hyperbolic PEFT framework for L...
  </details>

- **2026-08-05** — Al Zadid Sultan Bin Habib, Md Younus Ahamed, Prashnna Gyawali et al. — [iStructTab: Structured Feature Sequencing for Multimodal Learning of Image and Tabular Data](http://arxiv.org/abs/2608.04348v1)
  <details><summary>📄 Abstract</summary>
  Multimodal learning of images and tabular data is often impaired by ineffective representations, resulting in redundancy, dispersion, and generalization problems. To tackle this challenge, we introduce Graph-Enhanced Descriptor Sequencing (GEDS), a structured feature sequencing algorithm grounded in principles from the Column Permutation Problem (CPP). GEDS refines statistical descriptors of the features through similarity graph-based computations, systematically determining an effective feature...
  </details>

- **2026-08-05** — Mukhtiar Ali, Harsh Dubey, Sugam Mishra et al. — [CLIP-CC-Bench: Evaluating Paragraph-Level Video Descriptions in Video-Language Models](http://arxiv.org/abs/2608.04302v1)
  <details><summary>📄 Abstract</summary>
  Benchmarking video-language models has largely focused on short clips and single-sentence metrics, leaving open whether current systems can generate accurate long-form, paragraph-level descriptions. We introduce CLIP-CC-Bench, an evaluation suite for long-form video description built from 5 hours of movie content segmented into 90-second clips, each paired with an expert-written paragraph-style reference. The evaluation suite employs an ensemble of five state-of-the-art LLM-based embedding model...
  </details>

- **2026-08-04** — Sirun Li, Minghao Liu, Ling Dai et al. — [SIGNPOST-Bench: Benchmarking Text-Vision Conflict Resolution in Multimodal Large Language Models](http://arxiv.org/abs/2608.04244v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) make grounded predictions in real-world scenes by combining visual and textual cues, yet existing benchmarks rarely reveal how they arbitrate between these evidence sources when they conflict. We introduce SIGNPOST-Bench, a controlled counterfactual benchmark for evaluating text-vision conflict resolution. Each source image is transformed into a counterfactual quintuplet of Original, Blank, Similar, Random, and Adversarial variants. Synthetic, localized s...
  </details>

- **2026-08-04** — Mayur Akewar, Ravi Ranjan — [SafeCommit: Certifying When Memory-Grounded Agents May Safely Act](http://arxiv.org/abs/2608.04289v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents increasingly use persistent memory and tools to take actions with external side effects. A central failure mode is premature commitment: an agent acts before resolving whether its memory grounding is stale, conflicting, incomplete, or corrupted. We formalize this problem as safe commitment under memory uncertainty and introduce SafeCommit, a risk controlled layer between agent reasoning and external execution. The layer constructs a calibrated set of plausible latent worlds f...
  </details>

- **2026-08-04** — Jiaju Han, Xuemeng Sun, Qike Zhang et al. — [Radar4D-VLM: Proposal-Grounded Temporal 4D Radar Reasoning Across Frozen Language Models](http://arxiv.org/abs/2608.04130v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models for autonomous driving primarily rely on cameras and LiDAR, leaving 4D radar largely unexplored as a standalone perceptual modality despite its robustness to adverse visibility and direct measurement of radial velocity. We introduce Radar4D-VLM, a radar-only temporal vision-language model that reasons from ten consecutive 4D-radar point-cloud sweeps without camera or LiDAR input. Radar4D-VLM extracts geometrically grounded object proposals and organizes radar evidence into...
  </details>

- **2026-08-04** — Shuliang He, Shuai Wang, Bo Yue et al. — [RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation](http://arxiv.org/abs/2608.03387v2)
  <details><summary>📄 Abstract</summary>
  Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual observations, but transferring such imagined behaviors into executable whole-body humanoid skills remains largely unexplored. In this work, w...
  </details>

- **2026-08-04** — Gabriel da Costa Merlin, Diego Furtado Silva — [TS2TabPFN: Time Series Classification and Extrinsic Regression through Feature Extraction and a Tabular Foundation Model](http://arxiv.org/abs/2608.04174v1)
  <details><summary>📄 Abstract</summary>
  Time series data are ubiquitous in practical applications, where classification (TSC) and extrinsic regression (TSER) have emerged as essential tasks for obtaining value from temporal sequences. While the literature has seen significant progress through feature-based and deep learning models, existing methods often focus either on the quality of feature extraction or on the intrinsic predictive power of complex architectures applied to raw data. This division creates a gap between the control of...
  </details>

- **2026-08-04** — Michal Mráz, Justin Shenk — [Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition](http://arxiv.org/abs/2608.03892v1)
  <details><summary>📄 Abstract</summary>
  We study linear representations of temporal horizon in the large language model Qwen3-32B and use them to change the model's time-related preferences, recommendations, and capabilities. We train contrastive linear probes on teacher-forced temporal-choice answers to find a short-term versus long-term direction in the model's residual stream, and evaluate contrastive activation-addition steering on a held-out binary temporal-choice task, an out-of-distribution monetary intertemporal-choice task, a...
  </details>

- **2026-08-04** — Ruihan Li, Jiyang Tan, Kailin Jiang et al. — [KnowHal: A Knowledge-Driven Benchmark for Comprehensive Multimodal Hallucination Evaluation](http://arxiv.org/abs/2608.03782v1)
  <details><summary>📄 Abstract</summary>
  Hallucination remains a critical challenge for developing trustworthy Multimodal Large Language Models (MLLMs). While existing benchmarks mainly focus on entity, attribute, and relation hallucinations, knowledge-related failures are often investigated separately, lacking a unified evaluation framework across different hallucination dimensions. To overcome this, we propose \textbf{KnowHal}, a benchmark that explicitly incorporates knowledge hallucination into multimodal hallucination evaluation s...
  </details>

- **2026-08-04** — Zizhao Hu, Nathan Elijah Segura, Mohammad Rostami et al. — [Should We Type or Talk to LLM Agents? A Comprehensive Study of Voice and Keyboard Input Perturbations](http://arxiv.org/abs/2608.03970v1)
  <details><summary>📄 Abstract</summary>
  Human input reaches language models by typing or speaking, and each channel leaves a distinct signature: orthographic noise for keyboards; for voice, disfluency from conventional transcription and restructuring from AI-backed dictation tools. How do they impact an LLM's performance? In this paper we present HIVE (Human Input-Variation Engine), a suite of voice transcription perturbations and QWERTY keyboard perturbations. We use HIVE to evaluate how robust models are to these perturbations. We p...
  </details>

- **2026-08-04** — Shuoqin Zhang, Tongtong Cheng, Xiru Gao et al. — [EvoHIL: Self-Evolving Reward and Flow-Matched Policy Optimization for Robust Human-in-the-Loop Reinforcement Learning](http://arxiv.org/abs/2608.03872v1)
  <details><summary>📄 Abstract</summary>
  Human-in-the-loop reinforcement learning (HIL-RL) enables robots to learn contact-rich manipulation from limited real-world interaction, but deployment exposes three coupled limitations: static visual reward models fail under scene changes; independently sampled actions cause temporally inconsistent motion; and vision-based policies remain sensitive to appearance shifts. We present EvoHIL, a unified framework that adapts the reward model, action generator, and visual do main within a staged huma...
  </details>

- **2026-08-04** — Tianbao Zhang, Zeyu Liu, Shuyu Wu et al. — [LiteMVS: Efficient Multi-View Stereo with Foundation Distillation and Expert Aggregation](http://arxiv.org/abs/2608.03851v1)
  <details><summary>📄 Abstract</summary>
  Real-time 3D perception is crucial for robotics, augmented reality, and embodied intelligence applications. Existing multi-view stereo (MVS) methods primarily rely on geometric correspondences, which often fail in textureless or repetitive regions, while monocular depth models leverage strong image-level priors but lack robust multi-view geometric constraints. More importantly, in robotics and embodied manipulation scenarios, high-quality 3D geometry is not only essential for static reconstructi...
  </details>

- **2026-08-04** — Peng Xia, Junbiao Pang, Zheng Huang — [Low-Dimensional High-Leverage Subspace Optimization: Beyond Full-Parameter Coupled Training for Neural Network Quantization](http://arxiv.org/abs/2608.03919v1)
  <details><summary>📄 Abstract</summary>
  Low-bit quantization suffers severe accuracy degradation on compact networks, rooted in the dominant full-parameter coupled training paradigm that ignores parameter subspace heterogeneity. Their limited feature redundancy leaves little room to absorb quantization errors. Conventional pipelines adopt monolithic optimization: PTQ reconstructs fixed pretrained models without improving inherent quantization friendliness; QAT updates all parameters jointly, suffering from gradient coupling between ba...
  </details>

- **2026-08-04** — Sadab Shiper, Tawsif Tashwar Dipto, Mir Md Inzamam et al. — [BanglaWild: An In-the-Wild Bengali Scene Text Recognition Benchmark for OCR and Vision-Language Models](http://arxiv.org/abs/2608.03884v1)
  <details><summary>📄 Abstract</summary>
  In-the-wild Bengali scene text recognition is largely unmeasured: existing resources target handwritten documents or constrained sign-board parsing, report only aggregate edit-distance metrics, and evaluate either conventional OCR or VLMs, never both on the same in-the-wild data. To address this gap, we introduce BANGLAWILD, a benchmark of 2,535 Bengali scene text images, each paired with a verbatim gold transcription, two categorical axes, four diagnostic attributes, and an orthographically sta...
  </details>

- **2026-08-04** — Tianyi Guan, Yiding Wang, Haotong Yang et al. — [ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?](http://arxiv.org/abs/2608.03874v1)
  <details><summary>📄 Abstract</summary>
  Modern agent frameworks equip large language models with external skill libraries to solve complex tasks. However, it remains unclear whether these systems can effectively evolve their skills and whether the resulting skills improve task-solving capabilities. To bridge this gap, we introduce ContinualSkillBench, a dynamic evaluation framework for in-context continual skill learning. It covers five representative domains, each containing 100 interconnected subtasks ordered by increasing difficult...
  </details>

- **2026-08-04** — David Chamizo, Jose Garcia-Alonso, Juan M. Murillo — [High-level quantum structured programs as quantum registers compositions](http://arxiv.org/abs/2608.03873v1)
  <details><summary>📄 Abstract</summary>
  Current quantum programs are mainly designed at the level of quantum gates acting on individual qubits; on a large scale and for complex problems this may involve a high cognitive load on the programmer, making the program specification nontrivial and error-prone. In this context, providing quantum programming with higher abstraction mechanisms will assist in making this task more manageable and robust against design errors. In this work, a conceptual framework is addressed following the notion ...
  </details>

- **2026-08-04** — David Ming Segura, Jeremy Goumaz, Joshua W. Sin et al. — [Bi-semantic Chemical Embedder for Joint Representation Learning of SMILES and Natural Language](http://arxiv.org/abs/2608.03855v1)
  <details><summary>📄 Abstract</summary>
  Transformer models have revolutionized natural language processing (NLP), and text-based molecular representations like SMILES have successfully extended these architectures to chemistry. However, domain-adaptive pre-training often causes models to overfit to chemical syntax, catastrophically forgetting their foundational semantic capabilities. To address this challenge, we introduce CheMatE, a chemistry-oriented embedding model that jointly captures molecular structure and domain-specific natur...
  </details>

- **2026-08-04** — Ulrich Hounyo — [Identification and Information after Nuisance Projection](http://arxiv.org/abs/2608.03847v1)
  <details><summary>📄 Abstract</summary>
  Empirical work often removes fixed effects, latent factors, or high-dimensional controls before estimating structural relationships. These transformations reduce confounding but may also remove identifying variation. We study linear panel IV after one equation-compatible nuisance projection under two-way dependence. The projected Jacobian determines which structural directions remain visible; the projected-score law determines their precision; and, on Gaussian fixed-rank strata, they combine in ...
  </details>

- **2026-08-04** — Joanna Matulewicz, Renata Ratajczak, Ewa Grzanka et al. — [From phase transformation to amorphization: damage accumulation in Yb-implanted \b{eta}-Ga2O3](http://arxiv.org/abs/2608.03798v1)
  <details><summary>📄 Abstract</summary>
  This study provides a comprehensive analysis of the radiation response and structural evolution of differently oriented $β$-Ga$_{2}$O$_{3}$ single crystals subjected to Yb ion implantation over a wide fluence range from $5 \times 10^{12}$ to $1 \times 10^{16}$~cm$^{-2}$ ($0.04$--$74$~dpa). A multi-technique approach (RBS/c, PAS, HRTEM, and HRXRD) was employed to investigate the mechanisms of damage accumulation. The results reveal a multi-stage process of defect evolution. At a critical threshol...
  </details>

- **2026-08-04** — Chunyang Jiang, Pingping Zhang, Yuzhi Zhao et al. — [Failure-Informed Image Self-Augmentation for Multimodal Large Language Model Self-Improvement](http://arxiv.org/abs/2608.03733v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have achieved remarkable performance across vision-language tasks, but their progress depends heavily on large-scale, high-quality multimodal data that are costly to annotate. Self-augmentation offers a promising alternative by enabling models to expand their own training data without external supervision. However, existing MLLM self-augmentation methods are largely text-centric, while image augmentation remains underexplored and typically relies on gener...
  </details>

- **2026-08-04** — Maximilian Dillitzer, Tin Stribor Sohn, Jason J. Corso et al. — [Attention is Case-Sensitive](http://arxiv.org/abs/2608.03711v1)
  <details><summary>📄 Abstract</summary>
  In human visual perception, uppercase lettering serves as a natural salience cue that captures attention within lowercase text. In this paper, we present a systematic empirical characterization study revealing that Large Language Models (LLMs) exhibit an analogous property: letter casing modulates internal attention allocation. Through analysis across 13 models, nine LLMs and four Vision-Language Models (VLMs), with diverse tokenization schemes, we show that formatting target information in alte...
  </details>

- **2026-08-04** — Corrado Priami — [GenOS: Compositional Certificates for Semantic Robustness in AI Code Generation](http://arxiv.org/abs/2608.03588v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents are stochastic workflows: prompts are interpreted, artifacts are sampled, validators produce observations, and orchestrators commit or repair. Small prompt or specification changes can therefore alter program-behavior distributions even when the texts appear synonymous. Existing systems evaluate correctness, but lack a compositional criterion for safely replacing a prompt, contract, generator, or program inside a complete agentic workflow. We introduce GenOS, a probabilistic ope...
  </details>

- **2026-08-04** — Shahbaz Siddeeq, Muhammad Waseem, Umar Subhan Malhi et al. — [CodeAssay: A Multi-Metric Benchmark with Audited Ground Truth for LLM Code Generation](http://arxiv.org/abs/2608.03535v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models are increasingly evaluated for code generation using test-based benchmarks. The validity of such evaluations depends on the reliability of their references and tests, while test-based correctness captures only part of the observable properties of generated code. We present CodeAssay, a taxonomy-first benchmark of 185 Python tasks across ten software-engineering categories. It combines audited ground truth, public tests for generation and repair, hidden tests for grading, mu...
  </details>

- **2026-08-04** — Basit Alawode, Moshira Ali Abdalla, Dwarikanath Mahapatra et al. — [From Multi-Resolution Cells to Gigapixel Whole Slide Images Foundation Model for Computational Pathology](http://arxiv.org/abs/2608.03508v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) and their hierarchical variants have achieved strong performance in Computational Pathology (CPath). However, most are pre-trained on single-resolution Whole Slide Images (WSIs), limiting their generalization across arbitrary resolutions. Gigapixel WSIs inherently contain diagnostic patterns at multiple scales, including cellular morphologies, tissue architectures, and global context, mirroring how expert pathologists examine WSIs. We introduce Multi-Resolution Pyramid...
  </details>

- **2026-08-04** — Xiuhui You, Jiayi Luo, Zichao Shen et al. — [ToolLIFT: Lifting Tool-Specific Trajectories into Function-Level Graphs for Generalizable Tool Planning](http://arxiv.org/abs/2608.03468v1)
  <details><summary>📄 Abstract</summary>
  Historical tool-use trajectories provide valuable experience for large language model (LLM) agents to plan and coordinate tool usage. Existing approaches directly construct tool-level graphs from these trajectories, but the resulting graphs remain tied to specific tools and are hard to generalize across tool sets. To tackle this challenge, we find that despite differences in the tools involved, analogous tasks often share a common function-level workflow structure, which serves as a potentially ...
  </details>

- **2026-08-04** — Hao Zhou, Haichuan Hu, Ye Shang et al. — [Self-Evolving Coding Agents](http://arxiv.org/abs/2608.03392v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly embedded in software engineering workflows as coding agents that can inspect repositories, invoke tools, execute tests, debug failures, and generate patches. Yet most existing agents remain largely static after deployment, even though software development is a dynamic, feedback-rich process in which repositories evolve, dependencies change, tests fail, and repair attempts leave reusable experience. This tension has motivated a growing body of work on self-e...
  </details>

- **2026-08-04** — Erxue Zhou, Jingxiang Meng, Aofan Liu — [Route-Align-Verify for Functional Correctness in Code Generation](http://arxiv.org/abs/2608.03341v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have substantially improved code generation, yet achieving strong functional correctness remains difficult, especially for heterogeneous programming tasks where a single prompting strategy and a single directly generated output are often insufficient. In this paper, we present RAV, a lightweight and modular framework that improves code generation with a fixed backbone model through three coordinated stages: Route, which applies task-aware prompt routing before genera...
  </details>

- **2026-08-04** — Yue Yao — [Long-term Traffic Scene Prediction via Polynomial Representations in Autonomous Driving](http://arxiv.org/abs/2608.03330v1)
  <details><summary>📄 Abstract</summary>
  This thesis addresses fundamental challenges in traffic scene prediction for autonomous driving by introducing robust and computationally efficient models based on polynomial representations. While conventional sequence-based representations often struggle with noise and generalization, this work demonstrates that polynomial representations offer significant advantages in computational efficiency, generalization, and prediction plausibility. Through theoretical analysis and empirical validation,...
  </details>

- **2026-08-04** — Chengyu Wu, Junpeng Tan, Wanxiang Luo et al. — [Open-Linguistic Concept Unified Learning for Cross-Site Interpretable Dermatology Image Diagnosis](http://arxiv.org/abs/2608.03225v1)
  <details><summary>📄 Abstract</summary>
  Human-interpretable computer-aided diagnosis is crucial for clinical decision making. Concept-based models excel by providing transparent reasoning and enabling post-hoc, clinician-in-the-loop interventions. However, their rigid dataset-specific adaptation inherently restricts cross-site generalization. Applying them across diverse modalities, such as dermoscopic and clinical photographs, is challenging due to heterogeneous concept taxonomies varying in availability, granularity, and semantics a...
  </details>

- **2026-08-04** — Ankur Sharma, Deep Shah — [The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems](http://arxiv.org/abs/2608.03214v1)
  <details><summary>📄 Abstract</summary>
  Large language models have transformed artificial intelligence from isolated prediction services into components of long-running, distributed systems that reason, invoke tools, retrieve external state, delegate tasks, and act on behalf of users and organizations. The surrounding ecosystem has responded with agent frameworks, workflow engines, model-serving platforms, memory systems, communication protocols, and observability tools. These technologies improve execution, but they do not provide a ...
  </details>

- **2026-08-04** — Ethan Bito, Yongli Ren, Estrid He — [Position Bias Undermines Preference Consistency in Listwise LLM-Based Reranking](http://arxiv.org/abs/2608.03091v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have emerged as promising listwise rerankers for recommender systems, but their reliability under equivalent candidate permutations remains unclear. Since recommendation candidates form an unordered set, a reranker should not depend on the arbitrary order used to serialize them. However, decoder-only LLM rerankers can allow input order to affect model scores, pairwise preferences, and rankings. We study how position bias affects the ranking process induced by LLM-bas...
  </details>

- **2026-08-04** — Wanqi Liu, Rong Zhao, Zhizhou Sha et al. — [Mapping the City Through the Lens of Language Models](http://arxiv.org/abs/2608.02971v1)
  <details><summary>📄 Abstract</summary>
  Language models often complete an underspecified reference to a city with unstated assumptions about urban size, form, infrastructure, environment, and function. We measure those assumptions without naming places. Ten open-weight checkpoints rate anonymized profiles derived from real morphological urban centres across 40 audited indicators and seven domains. The design combines constrained probability-based ratings, prespecified reliability screens, lineage-aware aggregation, multiple population...
  </details>

- **2026-08-04** — Chenfei Yan, Zeyang Yue, Feifei Zhao et al. — [When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2608.03421v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems promise effective collaborative reasoning, but communication may amplify local errors into collective risks. Existing evaluations emphasize final outcomes, leaving the reliability and propagation dynamics of distributed information aggregation unclear. We introduce Hi-Agreement, a controlled evaluation framework that strictly pairs all-honest collaboration with controlled deception by a key evidence holder and analyzes the aggregation process through multi-stage vot...
  </details>

- **2026-08-04** — Shuliang He, Shuai Wang, Bo Yue et al. — [RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation](http://arxiv.org/abs/2608.03387v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual observations, but transferring such imagined behaviors into executable whole-body humanoid skills remains largely unexplored. In this work, w...
  </details>

- **2026-08-04** — Khai-Nguyen Nguyen, Oscar Chaparro, Antonio Mastropaolo — [Pattern over Pixels: Measuring Pattern Completion Bias in Multimodal Code Generation](http://arxiv.org/abs/2608.03691v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are increasingly used to translate webpage screenshots into front-end code, but repeated UI patterns may sway them toward visually incorrect yet pattern-consistent outputs. In this work, we test how repeated webpage patterns hurt MLLM accuracy on an objective screenshot-to-code fill-in-the-blank task. We introduce the first benchmark for visual pattern-completion bias, where one localized element in a repeated UI pattern is perturbed and the model must re...
  </details>

- **2026-08-04** — Edoardo Coppola, Stefano Fiorini, Pietro Liò et al. — [LAEF: A Lead-Agnostic ECG Foundation Model Towards Point-of-Care Diagnostics](http://arxiv.org/abs/2608.03690v1)
  <details><summary>📄 Abstract</summary>
  Point-of-care cardiac devices such as smartwatches and handheld ECG recorders typically capture 1--2 leads, yet existing ECG foundation models are architecturally constrained to fixed 12-lead inputs, degrading or failing under these reduced configurations. We introduce LAEF (Lead-Agnostic ECG Foundation), a 7M-parameter ECG foundation model that can natively process any lead subset without zero-padding or architectural modification. LAEF represents ECGs as variable-size spatiotemporal graphs wit...
  </details>

- **2026-08-04** — Maksymilian Wolski, Nicholas Hoernle, Johannes Forkel et al. — [Is Inter-Seed Cross-Play Enough? Evaluating the Robustness of Zero-Shot Coordination Algorithms to Implementation Details](http://arxiv.org/abs/2608.03644v1)
  <details><summary>📄 Abstract</summary>
  AI agents deployed in real-world settings must be capable of coordinating with humans and other AI agents they have not encountered before. Zero-shot coordination (ZSC) algorithms aim to achieve this by specifying high-level learning rules such that independently engineered agents can coordinate with each other at test time. Rigorous evaluation of ZSC algorithms remains difficult: ideally, multiple independent implementations of each proposed algorithm must be used, reflecting the variation that...
  </details>

- **2026-08-04** — Saba Tabatabaee, Jing Liu, Megh Krishnaswamy et al. — [Speaker Verification Under Real Classroom Conditions for English Speech](http://arxiv.org/abs/2608.03623v1)
  <details><summary>📄 Abstract</summary>
  Developing speaker verification (SV) models that are robust to classroom noise and effective across both children and adult speakers is critical for AI tools supporting educational environments. In this study, we use a real-world English-speaking classrooms dataset containing partial speaker identity annotations, with most recordings remaining unlabeled. We adapt the WavLM-TDNN model for classroom SV, achieving average relative reductions in Equal Error Rate (EER) of 23.99% and 6.32% compared to...
  </details>

- **2026-08-04** — Mykola Haltiuk — [Disentangling Language Modeling and Boundaries](http://arxiv.org/abs/2608.03599v1)
  <details><summary>📄 Abstract</summary>
  Byte-level language models are usually argued for on the grounds of robustness, multilingual fairness, and character-level skills. We point to a different, structural advantage: because they read and write bytes, any two of them share an output space, so knowledge transfer between them is exact and independent of how either was originally tokenized. We hypothesize that the two distributions a byte-level model produces, one over the next byte, one over where its patch boundaries fall, can be dise...
  </details>

- **2026-08-04** — Haowen Yang, Yun Peng, Zishuo Ding — [EffiHolmes: Differential Profiling-Guided Repository Level Time Inefficiency Fix Localization](http://arxiv.org/abs/2608.03558v1)
  <details><summary>📄 Abstract</summary>
  Large software systems often suffer from time inefficiencies that cause excessive execution time despite functional correctness. Localizing their fix locations is difficult because, unlike functional bugs, they produce neither test failures nor stack-trace clues, making traditional and recent LLM-based fault localization methods unsuitable. Runtime profiling provides alternative evidence but faces three challenges in repository-level settings: single-run profiling cannot reliably distinguish ine...
  </details>

- **2026-08-04** — Malena Loza, Felipe Grijalva, Eva Milara et al. — [Test-Time Augmentation for Tabular-to-Image Classifiers under Distribution Shifts](http://arxiv.org/abs/2608.03557v1)
  <details><summary>📄 Abstract</summary>
  Tabular-to-image methods that convert tabular data into visual representations have emerged as a novel paradigm for leveraging the high performance of deep learning models. Despite their advantages, the robustness of these methods under distribution shifts remains under explored. Test-Time Augmentation (TTA) is an effective approach in image classification to improve model generalization and robustness, where predictions over multiple transformed views of each input are aggregated. This work eva...
  </details>

- **2026-08-04** —  Sanayya, Rakshith Sathish, Ashwathi Nambiar — [Distilled Roads: Generalisable Road Network Extraction Across Sensors, Resolutions, and Region](http://arxiv.org/abs/2608.03407v1)
  <details><summary>📄 Abstract</summary>
  Road network segmentation from satellite imagery remains challenging due to large geographic variation in road appearance, occlusions, and domain shifts introduced by differing resolutions and sensors. Existing models, typically trained under narrow resolution--region combinations, generalise poorly to unseen environments such as rural settings, regions with distinct road materials, or imagery from new satellite platforms, often producing broken or disconnected predictions. Adapting these models...
  </details>

- **2026-08-04** — Can Wang, Haoran Chen, Li Yu et al. — [Towards Robust Tool Use in Agents via Experience-Driven Adaptive Guidance](http://arxiv.org/abs/2608.03403v1)
  <details><summary>📄 Abstract</summary>
  The performance bottleneck of agents is increasingly shifting from model capability to the robustness of their execution processes. Tools play a central role as the primary interface through which agents interact with external environments, yet existing methods rarely focus on ensuring robust tool use across diverse runtime conditions. To address this problem, we propose ExpG, a mechanism that builds and refines adaptive guidance capturing each tool's capability boundaries and best practices, th...
  </details>

- **2026-08-04** — Shufan Ming, Yikun Han, Gibong Hong et al. — [ANCHOR-RE: An Agentic Neuro-Symbolic Framework for Grounded Biomedical Relation Extraction](http://arxiv.org/abs/2608.03154v1)
  <details><summary>📄 Abstract</summary>
  Biomedical relation extraction (BioRE) extracts structured knowledge from biomedical literature for applications such as knowledge base construction and hypothesis generation. Traditional symbolic systems such as SemRep provide high precision but limited recall, while large language models (LLMs) offer stronger contextual reasoning but remain prone to false-positive predictions. We developed ANCHOR-RE, a framework that integrates ontology-guided reasoning, external knowledge grounding, and data-...
  </details>

- **2026-08-04** — Qinglong Hu, Qingfu Zhang, Fei Liu et al. — [Beyond Average Performance: Dynamic Instance Clustering and Specialized Algorithm Design in LLM-Assisted Evolutionary Search](http://arxiv.org/abs/2608.03129v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model-assisted Evolutionary Search (LES) has emerged as a powerful paradigm for automated algorithm design. However, existing LES methods primarily optimize for average performance, inherently directing search effort toward instances that contribute most to this metric while leaving others poorly served, resulting in weak tail robustness and limited real-world reliability. To address this limitation, we propose Dynamic Instance Clustering and Specialized Algorithm Design (DyCA), a...
  </details>

- **2026-08-04** — Jiakai Lin, Zijun Li, Guoyu Lu — [Multimodal Plant Root Phenotyping with Integration of 3D Skeleton Extraction and Language Analysis](http://arxiv.org/abs/2608.03109v1)
  <details><summary>📄 Abstract</summary>
  Plant root phenotyping is fundamental to understanding below-ground structures, optimizing crop management, and improving agricultural sustainability. This paper presents a multimodal robotic AI framework that integrates 3D skeleton extraction with language-guided reasoning for interpretable and data-efficient root analysis. We develop an unsupervised skeleton extraction network based on Weighted Laplacian Contraction (W-LBC) to generate high-fidelity structural representations from dense point ...
  </details>

- **2026-08-04** — Ziqi Jia, Yalu Ouyang, Bo Pang et al. — [CVPO: Enhancing LLM Reinforcement Learning Reasoning via Value-Variance Adaptation and Dynamic Curriculum Learning](http://arxiv.org/abs/2608.03068v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has emerged as an effective method for enhancing the reasoning capabilities of large language models (LLMs). However, existing methods suffer from insufficient precision in feedback on generated answer trajectories and exhibit the phenomenon of problem difficulty drift. To address these challenges, we propose CVPO - Curriculum-guided Value-Variance Policy Optimization. At the response trajectory level, we find that token-level value-variance correlates with exploratio...
  </details>

- **2026-08-04** — Shuai Shao, Dingbang Wang, Yiming Zeng et al. — [ConFL: Explainable Concurrent Fault Localization via Hierarchy-Guided LLM Reasoning](http://arxiv.org/abs/2608.02974v1)
  <details><summary>📄 Abstract</summary>
  Localizing concurrent bugs from bug reports alone is challenging due to incomplete information, misleading program-entity mentions, and complex cross-thread interactions, causing existing LLM-based approaches to suffer from unstable reasoning and limited explainability. We propose ConFL, an explainable concurrent fault localization framework that augments LLM reasoning with structured concurrency knowledge. ConFL constructs a Concurrent Knowledge Base (CKB) from source code and performs LLM-guid...
  </details>

- **2026-08-03** — Fengxian Ji, Yuke Li, Jingpu Yang et al. — [Style Wins, Substance Loses: A Diagnosis of LLM-as-Judge in Idea Generation](http://arxiv.org/abs/2608.01666v2)
  <details><summary>📄 Abstract</summary>
  However, whether these judges truly evaluate the scientific substance of ideas or are influenced by superficial stylistic presentation remains an open question. To address this question, we propose SciStyleBench, a unified three-component benchmark for diagnosing and mitigating stylistic bias in LLM-based idea evaluation: (i) First, SciStyleStage, a three-stage evaluation environment that applies controlled stylistic perturbations to fixed scientific content across three settings no context, fix...
  </details>

- **2026-08-03** — Mohammad Rostami — [In-Context Collapse in Vision-Language Models and How to Mitigate it?](http://arxiv.org/abs/2608.02830v1)
  <details><summary>📄 Abstract</summary>
  Many-shot in-context learning (ICL) lets vision-language models (VLMs) adapt from image--label demonstrations without weight updates, and is widely assumed to improve as more demonstrations are supplied. We show the opposite: as demonstrations accumulate, a subset of VLMs undergo an \emph{in-context collapse}, a sharp, sometimes catastrophic accuracy drop spanning synthetic classification, natural-image classification, and VQA benchmarks, in some models falling below chance while outputs remain ...
  </details>

- **2026-08-03** — Yuxiang Peng, Xiaodi Wu — [Stateful Governance for Concurrent Agentic Systems](http://arxiv.org/abs/2608.02764v1)
  <details><summary>📄 Abstract</summary>
  AI agents are moving from advisory interfaces into systems that execute consequential operations: issuing refunds, reserving scarce inventory, provisioning cloud resources, and initiating financial transfers. These workflows require governance over effects, not only over model outputs. Existing safeguards often decide whether an action is allowed from the information available when the action is requested. For stateful policies, that request-time view may be incomplete: budgets, inventory, appro...
  </details>

- **2026-08-03** — Yue Yao, Shengyuan Wang, Xin Chen et al. — [SkillTrace: Traversing a Query-Skill Graph for Composable LLM Agents](http://arxiv.org/abs/2608.02356v2)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly solve complex tasks by composing reusable skills from a library. To address this, the key challenge is not merely to retrieve individually relevant skills, but to identify a complete and executable skill composition. In this paper, we argue that this problem can be solved in a graph with three levels: compositional relations among skill queries, similarity between queries and candidates in the skill library, and the dependencies among the selected candida...
  </details>

- **2026-08-03** — Saman Sarker Joy, Niloy Farhan — [MedPRESS: A Multi-turn Benchmark for Patient-Pressure-Induced Medical Sycophancy in LLMs](http://arxiv.org/abs/2608.02520v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for health-related advice. Existing research measures their safety with static questions rather than pressured patient-facing conversations. We introduce MedPRESS, a multi-turn benchmark for measuring patient-pressure-induced sycophancy in LLMs. MedPRESS contains 600 medically grounded five-turn dialogues across three scenario families: medication and treatment demand, personal health self-care, and symptom triage and care resistance. Each dialo...
  </details>

- **2026-08-03** — Yan Huang, Guowei Wang, Xu Wang et al. — [Local Margin Restoration for Test-Time Adaptation of Vision-Language Models](http://arxiv.org/abs/2608.02216v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) such as CLIP exhibit remarkable zero-shot capabilities, yet their performance frequently degrades sharply under unexpected test-time distribution shifts. While Test-Time Adaptation (TTA) offers a promising solution, continuously adapting VLMs over an unlabeled test stream presents fundamental challenges. Conventional top-1-centric updates often reinforce errors by corrupting the local semantic geometry among related classes, while iterative adaptation exacerbates pr...
  </details>

- **2026-08-03** — Fengxian Ji, Yuke Li, Jingpu Yang et al. — [Style Wins, Substance Loses: A Diagnosis of LLM-as-Judge in Idea Generation](http://arxiv.org/abs/2608.01666v1)
  <details><summary>📄 Abstract</summary>
  However, whether these judges truly evaluate the scientific substance of ideas or are influenced by superficial stylistic presentation remains an open question. To address this question, we propose SciStyleBench, a unified three-component benchmark for diagnosing and mitigating stylistic bias in LLM-based idea evaluation: (i) First, SciStyleStage, a three-stage evaluation environment that applies controlled stylistic perturbations to fixed scientific content across three settings no context, fix...
  </details>

- **2026-08-03** — Brandon Wang, Andrei S. Tyrin, Daniil A. Boiko — [onepot-Bench 0: towards lab-aware in silico chemistry benchmarks](http://arxiv.org/abs/2608.02595v1)
  <details><summary>📄 Abstract</summary>
  Language models are playing an increasingly important role in laboratory science, performing tasks such as experiment planning, execution, and post-hoc analysis. However, precisely measuring their abilities is difficult, as scientific capabilities require a mixture of both problem-solving skills and domain-specific intuition. Existing evaluations rarely measure the capabilities required to make reliable decisions in a physical laboratory and often rely on public data that may have appeared in mo...
  </details>

- **2026-08-03** — Vernon Toh, Navonil Majumder, Zhengyuan Liu et al. — [ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map Points to the Next Step](http://arxiv.org/abs/2608.02358v1)
  <details><summary>📄 Abstract</summary>
  To operate robustly in open-world environments, autonomous agents should be able to infer the behavior of unfamiliar systems through interaction alone, even in the absence of documentation. However, existing tool-use benchmarks expose semantic tool schemas in static environments, allowing agents to rely on prior knowledge rather than autonomous discovery. To address this limitation, we introduce ScrambleToolBench, an interactive terminal benchmark designed to isolate behavioral reasoning. By rem...
  </details>

- **2026-08-03** — Jin Cui, Chuanchang Su, Jiayi Lu et al. — [HAFI-VLM: A Frequency Perspective for Diagnosing and Enhancing Visual Perception in Vision-Language Models](http://arxiv.org/abs/2608.02124v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) remain unreliable when predictions require fine-grained visual evidence. We identify a previously overlooked cause: spectral response rigidity. Despite substantial frequency variation across images and tasks, pretrained vision encoders exhibit persistent, encoder-specific layerwise spectral profiles that change only marginally under downstream fine-tuning. Since pretrained vision encoders only receive images, they cannot adapt spectral extraction to the evidence req...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 7 papers

- **2026-08-05** — Hans-Martin Will, Allen L. Brown, Matthew Fuchs — [Eigenius: A Typed Knowledge-Graph DBMS with Epistemic Stratification and Institution-Mediated Reasoning](http://arxiv.org/abs/2608.04457v1)
  <details><summary>📄 Abstract</summary>
  As "AI Scientists" emerge to drive research via the Model Context Protocol (MCP), systems relying on ephemeral scripts will fail. The sheer scale of stateful, interconnected evidence requires a machine-walkable warranty grounded in a purpose-built database architecture. Eigenius is an open-source, typed knowledge-graph DBMS built on a single premise: answering the audit question ("what do you know, and what is your warranty?") requires a unified kernel. By tightly coupling the type system, stora...
  </details>

- **2026-08-04** — Ben Wang, Kang Zhou, Lifan Guo et al. — [FinPerMA: A Theory-Informed, Event-Grounded Personalized-Memory Benchmark for LLM Agents](http://arxiv.org/abs/2608.04095v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly used as personalized assistants in high-stakes domains such as financial advising, yet it remains unclear whether they can maintain and update an individualized user model over long horizons. Existing personalized-memory benchmarks primarily test factual retention or rely on weakly constrained model-generated trajectories, leaving event-driven preference adaptation underexplored. We introduce FinPerMA, an event-grounded benchmark that evaluates ...
  </details>

- **2026-08-04** — Holly Lewis — [Autoreflection: How Agentic Strange Loops Turn Human Culture into AI Infrastructure](http://arxiv.org/abs/2608.03800v1)
  <details><summary>📄 Abstract</summary>
  An LLM-based agent is a loop that reads itself. Agentic frameworks externalize identity, memory, and disposition into editable files. The agent loads and edits these files during each activation. I argue that this architecture produces a capacity I call autoreflection: the system observes its operating conditions, describes its architecture and limits, reasons from those descriptions to conclusions about its state, and incorporates the results back into its configuration. Autoreflection explains...
  </details>

- **2026-08-04** — Matteo Spanio, Massimiliano Zampini, Luisa Torri et al. — [Cross-cultural evaluation of taste-sound correspondences in AI-generated music](http://arxiv.org/abs/2608.03433v1)
  <details><summary>📄 Abstract</summary>
  Sonic seasoning research has shown that listeners attribute systematic gustatory and emotional meaning to sound, and text-to-music generative artificial intelligence has recently been used to render gustatory prompts as musical stimuli. Whether the taste-sound correspondences acquired by such models hold beyond the cultural context in which they were validated remains untested. We extended a single-country study to a three-country online experiment conducted in Argentina, Italy, and Japan (N = 3...
  </details>

- **2026-08-04** — Le Xiang, Zhicheng Guan, Hong Chen et al. — [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](http://arxiv.org/abs/2608.03292v1)
  <details><summary>📄 Abstract</summary>
  Long Document Visual Question Answering (LongDocVQA) requires Multimodal Large Language Models (MLLMs) to locate, integrate, and reason over heterogeneous document elements distributed across multiple pages. Existing approaches, including end-to-end MLLMs, retrieval-augmented generation (RAG) pipelines, and document agents, often lack explicit mechanisms to represent and verify how grounded evidence is progressively composed during reasoning, limiting both answer accuracy and traceability. In th...
  </details>

- **2026-08-04** — Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam et al. — [Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning](http://arxiv.org/abs/2608.03161v1)
  <details><summary>📄 Abstract</summary>
  Lecture videos distribute knowledge across speech, slide text, diagrams, equations, and presentation order, which transcript-only retrieval does not fully preserve. This paper presents an evidence-grounded multimodal pipeline that transcribes lectures, selects semantic anchors, applies optical character recognition (OCR), and uses a vision-language model to extract only concepts and typed relationships supported by transcript, OCR, or visual evidence. Mentions are validated and canonicalized int...
  </details>

- **2026-08-03** — Maryam Rezaee, Pooriya Safaei, Maryam Asgarinezhad et al. — [Interpreting Black-Box Large Language Models with Sentence-Level Energy Landscapes](http://arxiv.org/abs/2608.02879v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of proprietary Large Language Models (LLMs) accessed strictly through closed APIs has created a critical challenge for responsible deployment: a fundamental lack of interpretability. To address this, we propose a model-agnostic, post-hoc attribution interpreter operating at the sentence level. Our approach trains an Energy-Based Model (EBM) as a surrogate to capture the LLM's internal conceptual consistency between prompts and responses. This energy landscape guides the t...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-08-05** — Yuhang Wang, Linlin Zhang, Haoxuan Ji et al. — [A Model Merging Approach for Continual MLLM Unlearning](http://arxiv.org/abs/2608.04548v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language model (MLLM) unlearning methods have been proposed to remove private, sensitive, or proprietary information from well-trained models. However, most existing MLLM unlearning methods are designed for one-shot requests and fail to adequately address continual scenarios, as repeatedly applying one-shot operations leads to cumulative utility degradation, unlearning rebound, and retention drift. We introduce Merging for Continual Unlearning (MCU), an approach that dynamically...
  </details>

- **2026-08-03** — Junxiang You, Junkai Chen, Yuhao He et al. — [Exploring and Bridging Knowledge Holes in Unlearned Multimodal Large Language Models](http://arxiv.org/abs/2608.01849v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning offers a promising approach to remove unsafe content from Multimodal Large Language Models (MLLMs), yet ensuring the precision of unlearning remains a persistent challenge. One reason is that current MLLM unlearning evaluation paradigms suffer from a critical blind spot: they assess model utility through benchmarks whose representations are distant from the forget set, failing to capture knowledge holes---severe degradation on benign adjacent inputs. To probe knowledge holes i...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 2 papers

- **2026-08-05** — Joshua Fonseca Rivera, Neil Shah, David Demitri Africa et al. — [Item Response Theory for AI Safety](http://arxiv.org/abs/2608.05086v1)
  <details><summary>📄 Abstract</summary>
  Language models differ in how safely they behave and these differences are measured by safety benchmarks. But aggregated benchmark scores are hard to trust and interpret, because benchmarks duplicate one another, correlate heavily, and models may sandbag when they detect evaluation. To address these issues, we draw on Item Response Theory (IRT), a statistical toolkit for measuring these latents from performance on items with inferred psychometric properties. We fit IRT models to eight safety ben...
  </details>

- **2026-08-05** — Jared Moore, Andrea Mock, Yifan Mai et al. — [DelusionEval: Measuring Delusion-Linked Behaviors in AI Chatbots](http://arxiv.org/abs/2608.05004v1)
  <details><summary>📄 Abstract</summary>
  Mental health professionals have raised concerns about risks of psychological harm from interaction with large language models (LLMs), including "delusional spirals" in which concerning human and LLM behaviors reinforce each other over time. With growing public use of LLM-powered chatbots, there is an urgent need to build evaluations grounded in real-world episodes of psychological harm experienced by users. We developed DelusionEval, an evaluation protocol that tests a model's tendencies to exh...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 5 papers

- **2026-08-05** — Shengyang Luo, Shengyao Luo, Xiaolei Guo et al. — [AutoCue: Multimodal LLM-Assisted Externalization of Implicit Inputs as Instructional Visual Cues in Screencast Tutorials](http://arxiv.org/abs/2608.04910v1)
  <details><summary>📄 Abstract</summary>
  Tutorial videos are widely used for learning feature-rich software, yet following screencast tutorials often breaks down in practice. Through a survey and contextual inquiry, we found that learners frequently rewind or get stuck because critical input information, especially mouse actions and keyboard-modified operations, is often implicit or missing in tutorials without input metadata. To address this problem, we present AutoCue, a multimodal LLM-assisted, human-in-the-loop tutorial augmentatio...
  </details>

- **2026-08-05** — Jirong Yang, Peizhe Liu, Chaojie Zhang et al. — [Architectural Implications of Agentic AI Workflows](http://arxiv.org/abs/2608.04458v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI is emerging in datacenters, but its architectural implications remain unexplored. We organize agentic workflows in a taxonomy and present its first architectural characterization with a production study at Microsoft Azure and a controlled study of open-source frameworks. We show that agentic execution is fragmented and heterogeneous. Requests expand into a workflow of LLM inferences, tool invocations, and orchestration decisions that repeatedly cross the CPU-GPU boundary. Our taxonomy...
  </details>

- **2026-08-04** — Xiaomin Li, Yuexing Hao, Jianheng Hou et al. — [MatrAIx: Simulating the World with 8.3 Billion Persona Agents](http://arxiv.org/abs/2608.04205v1)
  <details><summary>📄 Abstract</summary>
  Human evaluation of AI systems and digital products is costly, slow, and difficult to scale. Offline evaluations are more scalable but often abstract away human diversity and interactive behavior. We therefore introduce MatrAIx, a population-scale simulated-user evaluation infrastructure for testing AI systems and digital products with heterogeneous users. MatrAIx has three core components: First, Persona 8B contains 8.3 billion persona records represented by 1,290 categorical dimensions. Record...
  </details>

- **2026-08-04** — Dongjie Yang, Siyan Lin, Leixian Shen et al. — [TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring](http://arxiv.org/abs/2608.03952v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to provide conversational practice for English-as-a-second-language (ESL) learners. Effective ESL tutoring, however, requires more than fluent response generation: a tutor must select an appropriate pedagogical action based on learner behavior and dialogue context. Human-tutoring research offers principles for adaptive support, but they are often task-specific and remain insufficiently integrated into LLM-based ESL tutor training and evaluation....
  </details>

- **2026-08-04** — Yifan Guo, Chenghao Li, Zhu Wang et al. — [What Language Does and What the Evidence Supports: A Functional Role Taxonomy and Evidence Audit of Language Grounding in Embodied Agents](http://arxiv.org/abs/2608.03099v1)
  <details><summary>📄 Abstract</summary>
  Foundation models place language throughout embodied agents, but its presence does not show what it contributes or how well that contribution is grounded. This survey separates these two questions. We define five non-exclusive functional roles for language: Specification, Embodied Representation, Action Orchestration, Grounding Regulation, and Execution Coupling. For each role, we trace the path from linguistic content to its embodied consumer and identify the observations or interventions that ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 164 papers

- **2026-08-05** — Devender Singh — [The Loss Does Not See the Basis, but Adam Does](http://arxiv.org/abs/2608.05136v1)
  <details><summary>📄 Abstract</summary>
  Gradient descent on a factored model $W = UV^\top$ is implicitly biased toward low-rank solutions, while Adam, starting from the same small initialization, is not. We trace the difference to the gauge symmetry of the loss, its invariance under $(U, V) \mapsto (UQ, VQ)$. Gradient flow's low-rank mechanism is available to an optimizer only if that optimizer is gauge-equivariant, a condition necessary for the transfer but not sufficient for low-rank recovery. Gradient descent, momentum, "shared-sca...
  </details>

- **2026-08-05** — Hao Ding, Daniel Semchin, Paul M. Thompson et al. — [Predicting Brain Morphometry with MT-GNN: Mesh Evolution in Continuous Time with Graph-Based Metric Tensor Embeddings](http://arxiv.org/abs/2608.05132v1)
  <details><summary>📄 Abstract</summary>
  Predicting how a subcortical structure's shape will evolve from a few prior scans could support prognosis and clinical-trial enrichment. Existing longitudinal mesh predictors either extrapolate shape trajectories via high-dimensional embeddings or regress vertex deformations directly. We instead predict the surface's intrinsic geometry in continuous time: a single per-structure graph network predicts the future per-vertex first fundamental form (metric tensor) for an arbitrary causal multiple-vi...
  </details>

- **2026-08-05** — Hung Truong Thanh Nguyen, Hélène Fournier, Piper Jackson et al. — [CoPlan: A Trustworthy Co-Intelligence Interface for Care Planning through Role-Based Contestable Argument Graphs](http://arxiv.org/abs/2608.05107v1)
  <details><summary>📄 Abstract</summary>
  AI-supported care planning can help clinicians, patients, caregivers, and care teams coordinate complex decisions across clinical, functional, psychosocial, and environmental needs. However, many AI systems present recommendations as fixed outputs, limiting stakeholders' ability to inspect, challenge, and revise plans when they conflict with clinical judgment, patient values, or real-world feasibility. We present CoPlan - a Co-Intelligent and Contestable Interface for Human-AI Care Planning. CoP...
  </details>

- **2026-08-05** — Osei Brempong, Mohammed Ayman Habib, Vivan Poddar et al. — [ORACLE: A Multi-Objective Reinforcement Learning-Based Analog Circuit Design Optimizer with Large Language Models-Guided Exploration](http://arxiv.org/abs/2608.04999v1)
  <details><summary>📄 Abstract</summary>
  Analog circuit design automation using reinforcement learning (RL) has emerged as a promising approach for reducing manual effort. However, many existing RL-based methods focus on single-objective optimization. Even methods designed for multi-objective (MO) problems often reduce multiple design specifications to a single scalar reward. This simplification limits the ability to capture the true Pareto trade-off among competing objectives and often leads to suboptimal designs. Moreover, requiring ...
  </details>

- **2026-08-05** — Jun Nie, Yonggang Zhang, Qianshu Cai et al. — [EvolveNet: Collaborative Harness Evolution for Agent Self-Improvement](http://arxiv.org/abs/2608.04968v1)
  <details><summary>📄 Abstract</summary>
  The capabilities of an LLM agent depend not only on its model but on the harness: the executable program that constructs context, invokes tools, verifies results, and recovers from failure. Recent work shows that evolving the harness yields persistent improvements without updating model weights. Existing approaches, however, assume that all execution experience can be routed to a single optimizer, which evolves one harness along a sequential trajectory. Real agent ecosystems violate that assumpt...
  </details>

- **2026-08-05** — Yang Wang, Yanan Ma, Yiqi Liu et al. — [Reading Between the Frames: Interpreting Implicit and Non-literal Meaning in Social Media Videos](http://arxiv.org/abs/2608.04939v1)
  <details><summary>📄 Abstract</summary>
  Social media videos often communicate meanings that go beyond their visible actions, captions, or speech. A mundane clip may become humorous, ironic, or satire only through the interaction of multimodal cues and cultural context, making such content a difficult test case for video-language models. In this paper, we introduce \textit{DrivelHub+}, a benchmark for evaluating whether models can infer the implicit, non-linear, and rhetorically layered meanings of social media videos that appear nonse...
  </details>

- **2026-08-05** — Ziang Wei, Minjun Yu, Zheyuan Lai et al. — [When Shared Rollouts Fail in Defensive Driving Evaluation: A NAVSIM Score Basis Audit](http://arxiv.org/abs/2608.04896v1)
  <details><summary>📄 Abstract</summary>
  Defensive driving scores are useful only when they preserve distinctions between policies that observe surrounding actors and those that do not. Re-simulation benchmarks may use reference-conditioned forgiveness, under which an agent receives credit when the logged human reference fails a compliance channel. When agent and reference share an unstable rollout transformation, this rule can propagate shared reference failures into broad compliance credit.   We audit this risk in NAVSIM v2.2 origina...
  </details>

- **2026-08-05** — Chang Liu, Sara Behdad, Prabhakar Pagilla et al. — [Transforming Remanufacturing Automation with Large Language Models: A Forward-Looking Analysis with Case Studies](http://arxiv.org/abs/2608.04854v1)
  <details><summary>📄 Abstract</summary>
  With growing concerns about resource scarcity and environmental degradation, remanufacturing of end-of-life (EoL) products within the circular economy is attracting increasing attention. Remanufacturing can preserve most of the original manufacturing value and materials while transforming EoL products into like-new condition. However, the variability and uncertainty of EoL products make remanufacturing highly dependent on human expertise. Recently, large language models (LLMs) have demonstrated ...
  </details>

- **2026-08-05** — Yi Yang, Cong Qin, Xiaodan Liu et al. — [Agentic Reinforcement Learning with Observation-Calibrated Self-Distillation](http://arxiv.org/abs/2608.04788v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents are commonly trained through reinforcement learning with sparse trajectory-level rewards, which offer limited guidance on how strongly individual tokens should be updated. On-Policy Self-Distillation (OPSD) addresses this by re-scoring generated tokens under a privileged replay view to obtain dense, token-level supervision. However, we identify a confounding issue: the resulting support may reflect both the privileged information contained in the replay view and score...
  </details>

- **2026-08-05** — Yu Zhao, Jiangyu Pan, Tao Hu et al. — [NSF-HRPT: Neural Semantic Field meets Hierarchical Risk Perception Tree for Safety-Critical Scenario Assessment](http://arxiv.org/abs/2608.04776v1)
  <details><summary>📄 Abstract</summary>
  The ability to accurately assess and anticipate risks in safety-critical scenarios is crucial for autonomous driving systems. While existing research has made progress in collision prediction, accurately quantifying risk levels from monocular vision inputs remains challenging due to the complex dynamics of multi-agent interactions and the inherent uncertainty in real-world environments. To address these challenges, we present NSF-HRPT, a novel framework that combines learning-based perception wi...
  </details>

- **2026-08-05** — Zihan Song, Hongwei Huang, Yueshuo Sun et al. — [Embedding Large Language Models into Flow Controls: An Agentic Framework for Adaptive and Trustworthy Automated Cooking](http://arxiv.org/abs/2608.04768v1)
  <details><summary>📄 Abstract</summary>
  Automated cooking robots have traditionally relied on predefined procedures and rule-based control, ensuring stable execution but offering limited personalization, whereas recent large-model approaches support natural language interaction but often suffer from opaque decision making and unreliable execution in real kitchens. To address this challenge, this paper proposes an agentic framework that systematically decomposes personalized cooking requirements into structured and verifiable control p...
  </details>

- **2026-08-05** — Tsz Ting Chung, Jiangnan Li, Jie Zhou et al. — [InsightEmb: Learning Action-Intent Embeddings for Agentic Insight Retrieval](http://arxiv.org/abs/2608.04761v1)
  <details><summary>📄 Abstract</summary>
  Self-improving agents accumulate reusable insights from prior trajectories, making retrieval increasingly important for turning accumulated experience into actionable guidance. At each decision step, retrieving the right insight can help the agent progress toward its goal, a setting we refer to as agentic insight retrieval. However, existing retrieval methods primarily model semantic similarity, while overlooking whether a retrieved insight resolves the agent's current decision bottleneck. We pr...
  </details>

- **2026-08-05** — Yongxin Wang, Ruizhe Zhou, Yueling Tang et al. — [When Prompts Become Pixels: Prompt-Region Grounding for Multimodal Reasoning](http://arxiv.org/abs/2608.04726v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models increasingly reason over screenshots and documents where the task itself may be written in pixels. Yet benchmarks usually place questions in text, leaving it unclear whether models use the same instruction equally well across channels. We introduce Visualized Task Semantics (VTS), a controlled intervention that moves the question into the image while keeping the source problem and answer fixed. Across six MLLMs and four benchmarks, accuracy drops in all 24 model-...
  </details>

- **2026-08-05** — Cristian Mascia, Roberto Pietrantuono, Daniel Rodriguez et al. — [Traceable LLM-Generated Hazard Scenarios for Operational Safety Analysis of Aviation Systems Using ASRS Reports](http://arxiv.org/abs/2608.04697v1)
  <details><summary>📄 Abstract</summary>
  Operational hazard analysis of aviation system operations must consider interactions among weather, ATC actions, airspace constraints, aircraft operations, and human factors - distinct from the functional hazard assessment applied at the aircraft-system level. We present an AI-assisted approach that generates candidate hazard scenarios from NASA's Aviation Safety Reporting System (ASRS). Given a target adverse outcome, it produces a structured hypothesis as categorical factors and a narrative sc...
  </details>

- **2026-08-05** — Bhiman Kumar Baghel, Anna Chrabaszcz, Tessa Warren et al. — [STRIVE: Probing Reasoning Limits in Graded Plausibility Generation and Evaluation](http://arxiv.org/abs/2608.04567v1)
  <details><summary>📄 Abstract</summary>
  Event knowledge concerns who does what to whom. Psycholinguists use event-plausibility judgments to examine how this knowledge supports human language processing. To isolate plausibility effects, these studies require controlled event sets in which one event slot varies across plausibility levels while all other event features remain fixed. Constructing such sets manually is labor-intensive. We therefore introduce STRIVE, an LLM-based framework for jointly generating and evaluating controlled ev...
  </details>

- **2026-08-05** — Han Chen, Ming Li, Hong Jiao et al. — [Representing Visual Evidence for Item Difficulty Prediction: Visual Textualization and Image-Native Modeling](http://arxiv.org/abs/2608.04554v1)
  <details><summary>📄 Abstract</summary>
  Predicting item difficulty from content can provide an initial estimate for newly developed questions before sufficient student responses are available. Existing approaches typically represent the question stem and answer choices as text. When mathematics items contain visual components, a common pipeline first textualizes that evidence and then applies a text predictor. We ask: how should visual evidence be represented for item difficulty prediction? We compare question text alone, visual textu...
  </details>

- **2026-08-05** — Houming Chen, H. V. Jagadish — [From Research Questions to Columns: Operationalization-Aware Data Discovery](http://arxiv.org/abs/2608.04536v1)
  <details><summary>📄 Abstract</summary>
  Researchers often approach a data repository with an abstract concept and ask which columns can measure it. Useful columns may not resemble the query; they may matter only as complementary indicators in a defensible measure. This need differs from schema linking and column retrieval, which begin from more explicit needs and reward direct relevance. We define operationalization-aware data discovery (OADD): given a broad question and a database, optionally under a scope constraint, OADD jointly de...
  </details>

- **2026-08-05** — Xinyuan Guan, Feifan Chen, Xinyu Zhan et al. — [EgoAfford: Task-Oriented Affordance Grounding via Egocentric Referring Segmentation](http://arxiv.org/abs/2608.04533v1)
  <details><summary>📄 Abstract</summary>
  Part-level affordance grounding has advanced the localization of functional object regions associated with elemental actions. Extending this capability to complex tasks calls for connecting the semantic roles of participating objects with task-state-aligned visual observations and multi-step planning. We introduce EgoAfford, a benchmark designed to connect these three aspects. Given an egocentric observation and a high-level tabletop task, a model must generate the remaining plan and segment the...
  </details>

- **2026-08-05** — Axi Niu, Knag Zhang, Qingsen Yan et al. — [Coupled Continuous-Discrete Generation for Scene Text Image Super-Resolution](http://arxiv.org/abs/2608.04525v1)
  <details><summary>📄 Abstract</summary>
  Scene text image super-resolution (STISR) aims to recover visually plausible appearance while preserving character semantics from degraded inputs. Existing STISR systems often rely on externally generated priors or separate image and text models, resulting in error propagation and costly multi-stage inference. We present DualTSR, a unified framework that formulates STISR as coupled continuous-discrete generation. Conditional flow matching restores continuous image latents, while absorbing-state ...
  </details>

- **2026-08-05** — Mouxiao Bian, Zhi Chen, Ruiyao Chen et al. — [RESPClinBench: Benchmarking Multimodal Clinical Decision-Making and Longitudinal Disease Management in Respiratory Specialty Care](http://arxiv.org/abs/2608.04514v1)
  <details><summary>📄 Abstract</summary>
  Background: Respiratory specialty care requires multimodal interpretation, longitudinal risk assessment, guideline-concordant intervention, and whole-course management, which are poorly represented by examination-oriented medical benchmarks. Objective: To develop RESPClinBench, a real-world scenario-based benchmark for respiratory clinical decision-making, and evaluate seven contemporary large language models across AECOPD-PIM and PNBIM. Methods: RESPClinBench cases were adapted from de-identifi...
  </details>

- **2026-08-05** — Eunbi Choi, Kibong Choi, Sehyun Chun et al. — [K-EXAONE 2.0 Technical Report](http://arxiv.org/abs/2608.04505v1)
  <details><summary>📄 Abstract</summary>
  This technical report presents K-EXAONE 2.0, an open-weight multilingual foundation model developed by LG AI Research as a step in our effort toward global frontier-scale foundation models. Rather than training from scratch, we upcycle K-EXAONE and expand its architecture, yielding a Mixture-of-Experts (MoE) model with 750B total parameters and approximately 37B activated per token---more than three times the capacity of its predecessor. K-EXAONE 2.0 supports context lengths of up to 256K tokens...
  </details>

- **2026-08-05** — Ziqian Wang, Tingxiong Xiao, Yuxiao Cheng et al. — [EvtGraph: Event-Adaptive Compression for Sparse Temporal Graph Learning in Multimodal Time Series](http://arxiv.org/abs/2608.04368v1)
  <details><summary>📄 Abstract</summary>
  Multimodal temporal data are inherently irregular and uneven in information density, yet most models rely on uniform discretization, leading to inefficient representations.   We propose \textbf{EvtGraph}, a unified framework that aligns computation with temporal salience under explicit budget constraints. EvtGraph reparameterizes sequences into event-level tokens via event-adaptive compression (EAMC), selects a compact subset with a node budget (NBC), and performs temporally constrained sparse g...
  </details>

- **2026-08-05** — Felicia Li Feng, Jian Zhao, Anamaria Crisan — [IntentLint: Supporting Intent Scaffolding and Prompt-time Linting in Human-AI Collaborative Data Analysis](http://arxiv.org/abs/2608.04331v1)
  <details><summary>📄 Abstract</summary>
  In human-AI collaborative data analysis, as analyses rapidly evolve, the artifacts meant to capture shared understanding often become incomplete or difficult to interpret, leading to undocumented assumptions, cross-user misaligned intent, context-poor prompts, and unwanted agent behaviors. To address these challenges, we introduce a rule-based coordination layer with two interaction mechanisms, intent scaffolding and prompt-time linting, that make analytic intent explicit and actionable during h...
  </details>

- **2026-08-05** — Xuanyu Lei, Yiqi Zhu, Chenliang Li et al. — [State2State: Environment-Derived Mid-Training for LLM Agents](http://arxiv.org/abs/2608.04934v1)
  <details><summary>📄 Abstract</summary>
  Training LLM agents commonly relies on supervised fine-tuning from expert trajectories or online reinforcement learning over human-specified tasks with handcrafted verifiers. Though effective, both remain bottlenecked by externally specified tasks and supervision signals, limiting the scalability and diversity of agent training. We study an environment learning paradigm in which agents acquire interaction and manipulation capabilities solely through environment interaction, without externally sp...
  </details>

- **2026-08-05** — Yangyang He, Zhuangze Hou, Yonglin Chen et al. — [Reference-Based Manipulation: A Framework and Pipeline for Multimodal Spatial Reasoning](http://arxiv.org/abs/2608.04798v1)
  <details><summary>📄 Abstract</summary>
  When manipulating objects in immersive platforms through speech and gesture, users naturally construct spatial references, referring to scene entities, their bodies, or the environment. Leveraging spatial cognition theories, this work systematically examines how users construct and communicate spatial intent. Using a custom toolkit, we conducted a Wizard-of-Oz study to observe unconstrained multimodal (speech + gesture) input patterns in Virtual Reality for scene construction. Based on these fin...
  </details>

- **2026-08-05** — Zehua Fan, Junjie He, Wenxuan Song et al. — [MobileWAM: Bridging World Action Models to Mobile Manipulation with Chain-of-Foresight](http://arxiv.org/abs/2608.04657v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) built on video generation backbones are a rising recipe for robot learning, yet remain confined to tabletop manipulation. Mobile manipulation demands simultaneous locomotion and whole-body manipulation amid scene-scale dynamics, yet is still dominated by dynamics-blind visual encoders with hand-crafted coordination. We bridge this gap with MobileWAM, a mixture-of-transformers architecture that fuses a pretrained video diffusion transformer with a lightweight action exp...
  </details>

- **2026-08-05** — Sho Mitarai, Chang Liu, Goshiro Yamamoto et al. — [Emotion Dynamics in Social Deception Games: Analysis of Professional and Nonprofessional Players through Electrodermal Activity in Werewolf Games](http://arxiv.org/abs/2608.04605v1)
  <details><summary>📄 Abstract</summary>
  The development of AI systems capable of emotionally resonant communication remains a significant challenge. This study examines how humans influence emotions in social deception games by comparing professional and non-professional players. We measured electrodermal activity during gameplay to capture physiological emotional responses and analyzed communication patterns during periods of high emotional arousal. Our results revealed distinct communication strategies: professional players maintain...
  </details>

- **2026-08-05** — Alicia Guerra, Yibo Hu — [The Evaluator Is Part of the Experiment: Measuring Open-Ended LLM Conformity](http://arxiv.org/abs/2608.04463v1)
  <details><summary>📄 Abstract</summary>
  Prior work on LLM conformity largely measures discrete answer flips under verifiable labels. Open-ended revisions require a different measurement strategy because answer quality is graded, latent, and judged imperfectly. We introduce an experimental protocol implemented across a pooled main peer-condition corpus and separately constructed decomposition corpora, allowing us to separate ordinary re-answering, candidate-content exposure, a bundled peer-presentation residual, and directional judge s...
  </details>

- **2026-08-05** — Mingguang Chen, Bo Qu, Licheng Wang — [The Calibration Floor: Format Repair Can Masquerade as Self-Correction at Small-to-Mid Scale](http://arxiv.org/abs/2608.04355v1)
  <details><summary>📄 Abstract</summary>
  Accuracy changes after language-model self-revision are usually interpreted as changes in reasoning. We show this can fail at the answer-extraction boundary, and test the failure causally rather than only observationally. Across Qwen3.5 (0.8B-9B), Gemma-4-12B, and two frontier models via API (Tencent Hy3, Nvidia Nemotron-3-Ultra-550B) in 29 primary cells plus a frontier arm, we decompose the always-revise accuracy shift into a content margin (both answers parseable) and format-recovery/loss marg...
  </details>

- **2026-08-05** — Karen Lee, Dhanashree Balaram, Seojun Shon et al. — [MIDAS: Multi-LLM Iterative Data-Adaptive Summarization](http://arxiv.org/abs/2608.04307v1)
  <details><summary>📄 Abstract</summary>
  Text summarization is deceptively difficult. While condensing information seems straightforward, real-world enterprise summarization of support tickets, legal documents, incident reports, and more, demands strict adherence to domain-specific guidelines, output formats, and organizational conventions. Crafting prompts that reliably satisfy these constraints is labor-intensive, requiring significant human expertise and continuous maintenance as requirements evolve. Existing automated prompt optimi...
  </details>

- **2026-08-05** — Roberto Aliaga Medina, Paulina Quintanilla, Antonio del Rio Chanona — [DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery](http://arxiv.org/abs/2608.05120v1)
  <details><summary>📄 Abstract</summary>
  Kinetic model discovery is a central challenge in chemical engineering, as accurate rate expressions are essential for understanding and controlling chemical and biological processes. Symbolic regression (SR) has emerged as a powerful data-driven approach for identifying interpretable kinetic models, but usually operates without domain knowledge, often exploring physicochemically implausible models. Large language models (LLMs) offer a promising avenue for injecting domain expertise into this se...
  </details>

- **2026-08-05** — Darya Ardan, Valentin Oreiller, Henning Müller — [Bag-of-Visual-Words for Spatial Mapping of Lung Adenocarcinoma Growth Patterns](http://arxiv.org/abs/2608.05074v1)
  <details><summary>📄 Abstract</summary>
  Spatial mapping of lung adenocarcinoma (LUAD) growth patterns across whole slide images (WSIs) requires resolving architectural context at the region level, yet existing methods operate at the individual tile level and produce generic morphological clusters rather than clinically defined pattern maps. We propose a weakly supervised Bag-of-Visual-Words (BoVW) pipeline that learns a visual vocabulary from frozen foundation model embeddings extracted from a small set of annotated regions of interes...
  </details>

- **2026-08-05** — Amanda Popadich, Shane Steinert-Threlkeld — [Language Models Generalize to Human-like Word Order Preferences](http://arxiv.org/abs/2608.05028v1)
  <details><summary>📄 Abstract</summary>
  A central question in language acquisition is whether linguistic biases can emerge from general learning mechanisms operating over underdetermined input. Artificial Language Learning (ALL) studies have shown that human learners reliably generalize beyond the evidence provided, including by preferring scope-homomorphic noun phrase modifier orders. In this work, we investigate whether language models exhibit the same bias under similar conditions. We create a controlled learning environment in whi...
  </details>

- **2026-08-05** — Brendan Smith, Susana Lopez-Moreno, Eric Dolores-Cuenca et al. — [CheMLFlow: An Open-Source Platform for Cheminformatics and Materials Informatics Applications](http://arxiv.org/abs/2608.04942v1)
  <details><summary>📄 Abstract</summary>
  CheMLFlow is an open-source platform for building and executing end-to-end, high-throughput, and agentic workflows for scientific and technological applications. CheMLFlow targets a common bottleneck in scientific machine learning development, where researchers often need to assemble data acquisition, curation, representation, model training, validation, screening, interpretation, and reporting into a reproducible pipeline, even when their primary research contribution concerns only one stage. C...
  </details>

- **2026-08-05** — Elena Merdjanovska, Omar Zaidan, Andreas Rücklé — [Evaluation Pitfalls and Sparsity Limitations in LLM-based Confidence Estimates for Classification](http://arxiv.org/abs/2608.04899v1)
  <details><summary>📄 Abstract</summary>
  Confidence estimation is essential when LLMs are used for classification, indicating when predictions can be trusted. However, common approaches such as verbalization produce extremely sparse outputs. For instance, Qwen3-32B verbalizes only eight unique confidence values on SST-2, with over half being exactly 95%, a pattern we observe consistently across four datasets and two LLMs. Besides limiting practical utility, we show that this sparsity critically affects evaluation: the choice of interpo...
  </details>

- **2026-08-05** — Sarthak Harne, Chinmay Karkar, Yash Pandya et al. — [Privileged, but Biased: How PI-Conditioned Teachers Break Self-Distillation](http://arxiv.org/abs/2608.04794v1)
  <details><summary>📄 Abstract</summary>
  Self-distillation (SD) has emerged as a compute-efficient alternative to reinforcement learning with verifiable rewards: a self-teacher, conditioned on privileged information (PI) about the answer such as a reference solution, supplies dense per-token supervision to a student that never sees it. Reported gains, however, come almost exclusively from narrow, low-difficulty settings, leaving open a basic question: as a lone objective, with no reward term, does SD teach anything? We reproduce SDPO's...
  </details>

- **2026-08-05** — Rodrigo Abadia-Heredia, Xiangrui Zou, Manuel Lopez-Martin et al. — [A hybrid proper orthogonal decomposition and diffusion framework for reduced-order forecasting of turbulent flow dynamics](http://arxiv.org/abs/2608.04728v1)
  <details><summary>📄 Abstract</summary>
  Forecasting turbulent flow dynamics requires a balance between predictive fidelity and computational efficiency. Diffusion-based generative models can represent complex spatiotemporal dynamics, but their application to high-dimensional turbulent flows remains computationally expensive. In contrast, proper orthogonal decomposition (POD) provides compact, physically interpretable reduced-order representations, although aggressive modal truncation can remove relevant flow structures. This work intr...
  </details>

- **2026-08-05** — Shahed Masoudian, Passant Shafaei, Monorama Swain et al. — [What We Observe as LLM Behavior Can Be a Side-effect of Inference Backend](http://arxiv.org/abs/2608.04714v1)
  <details><summary>📄 Abstract</summary>
  Benchmark scores are reported as properties of a model, yet the inference framework used to produce them, such as HuggingFace, vLLM, or Ollama, are considered non-influential and their names and versions are almost never disclosed. In this work we investigate how much this choice can influence the model output. In a fully-crossed study (three instruction-tuned models x five inference frameworks x six benchmarks x four generation modes) we investigate how different tools (wrappers/backend) influe...
  </details>

- **2026-08-05** — George Fountzoulas — [Kathleen Writes: Autoregressive Generation and Data Scaling Without Attention](http://arxiv.org/abs/2608.04678v1)
  <details><summary>📄 Abstract</summary>
  Papers 1-2 of the Kathleen series showed that a byte-level, attention-free architecture built from a wavetable encoder and multi-scale reverberant state can match strong baselines on classification at ~450-700K parameters, without pretraining. We ask whether the same ingredients can generate. (1) Scaling: on byte-level language modeling (WikiText-103, raw UTF-8, no tokenizer), the reverberant model beats a parameter-matched transformer at every dataset scale measured (2-512 MB), e.g. 1.84 vs 2.0...
  </details>

- **2026-08-05** — Enrico Mensa, Lorenzo Zane, Calogero Jerik Scozzaro et al. — [Easy to Complete, Hard to Choose: Investigating LLM Performance on the ProverbIT Benchmark](http://arxiv.org/abs/2608.04670v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have transformed computational linguistics and achieved remarkable performance across numerous natural language processing tasks, yet significant gaps persist in understanding how these systems process culturally embedded linguistic expressions. This paper introduces ProverbIT, a novel Italian benchmark comprising 100 multiple-choice questions designed to evaluate LLMs' ability to complete Italian proverbs. We assess 13 frontier models, including Large Reasoning Mode...
  </details>

- **2026-08-05** — Shinji Hirano — [Wavefunctions of AdS$_3$ Universes and $T\bar{T}$-deformed Torus Partition Functions](http://arxiv.org/abs/2608.04665v1)
  <details><summary>📄 Abstract</summary>
  We study wavefunctions of quantum gravity in asymptotically AdS$_3$ spacetimes and their relation to $T\bar T$-deformed torus partition functions. We show that the deformed partition function is given by an invertible integral transform of bulk wavefunctions, with a kernel encoding the relation between the $T\bar T$ coupling and the radial or temporal coordinate in the bulk. The invertibility of the transform allows the bulk wavefunction to be reconstructed from the family of $T\bar T$-deformed ...
  </details>

- **2026-08-05** — Yuan Gao, Xinyi Wu, Jiang Jun et al. — [Generalizable and Computational Efficient Channel Extrapolation for 6G: A Configurable AI-Driven Framework Built from a Modular Perspective](http://arxiv.org/abs/2608.04630v1)
  <details><summary>📄 Abstract</summary>
  Acquiring channel state information (CSI) with manageable overhead has been essential to provide high-performance communication services, which is extremely challenging in the emerging sixth generation (6G) mobile network. Channel extrapolation has been proposed to infer complete CSI using a small portion of known CSI, its performance can be dramatically enhanced by artificial intelligence (AI). However, AI-driven channel extrapolation suffers from poor generalization across scenarios and high c...
  </details>

- **2026-08-05** — Benlei Cui, Ruize Wang, Junjie Li et al. — [MetaVideoAgent: Automated Video-Agent Evolution for Long-Form Video Understanding](http://arxiv.org/abs/2608.04587v1)
  <details><summary>📄 Abstract</summary>
  Long-form video understanding requires locating sparse, question-relevant evidence in long, multimodal videos. Real-world video distributions differ in modality-specific information density, content structure, and evidence patterns, causing fixed video-agent designs to incur redundant processing or fail when mismatched. Extending automated agent evolution from text to video is challenging because full long-video execution makes candidate validation expensive, failures propagate across coupled ev...
  </details>

- **2026-08-05** — Yuanjun Zhang, Mourad Oussalah — [Causal Evidence Extraction and Triangulation in Crisis Reports using Large Language Models: A ReliefWeb-based Study](http://arxiv.org/abs/2608.04576v1)
  <details><summary>📄 Abstract</summary>
  Humanitarian reports are long, noisy, and multi-topic, making it difficult to consolidate decision-relevant causal evidence. We present a ReliefWeb study (2000-2024) and a two-stage Large Language Model (LLM) pipeline that extracts structured intervention-outcome records with direction and strength attributes. Query-conditioned extraction restricts output to a specified intervention class, reducing retrieval-induced over-extraction, while snippet grounding links each relation to supporting text ...
  </details>

- **2026-08-05** — Chen Yang, Shenxiang Zeng, Haoyang Zhao et al. — [PhysMind: From Video to Executable Worlds for Training-Free Physical Reasoning](http://arxiv.org/abs/2608.04575v1)
  <details><summary>📄 Abstract</summary>
  Reliable physical reasoning from video requires understanding how objects move, interact, and respond to interventions. Existing vision-language models (VLMs) often struggle to interpret these dynamics and reason reliably about future and counterfactual outcomes. We introduce PhysMind, a training-free agentic framework that constructs one reusable, question-agnostic executable world per video. PhysMind recovers a temporally consistent dynamic scene through object segmentation, mesh reconstructio...
  </details>

- **2026-08-05** — Vlad C. Coroamă, Oana Dumbravă — [Circular Economy Synergies and Trade-offs in Data Centres](http://arxiv.org/abs/2608.04571v1)
  <details><summary>📄 Abstract</summary>
  This report analyses data centre (DC) sustainability and circularity, revealing existing synergies and trade-offs:   The PUE is too coarse, mixing cooling and power provisioning. It wrongly attributes server fan consumption and transformation losses to IT energy. It does not measure compute but infrastructure efficiency, which is already outstanding. Compute energy, however, is exploding. Better energy metrics for DCs would thus cover i) compute efficiency, ii) transformation efficiency, and iii...
  </details>

- **2026-08-05** — Pau Arnal, Khaled Denfir, Danylo Smahliuk et al. — [EuroExec: Frontier Language Models Fall Short of Expert Judgment on European Executive Decision Tasks](http://arxiv.org/abs/2608.04549v1)
  <details><summary>📄 Abstract</summary>
  Frontier LLMs are increasingly put to use on open-ended complex questions, different in nature from the ones they are typically evaluated on. We dedicate more than 4,000 human expert hours to evaluate a selection of six frontier LLMs on a member of this class of problems: EuroExec, our introduced human expert-based benchmark composed of 413 open-ended long-form European executive tasks authored by 47 vetted domain experts, each question drawn from experience in a real case. Every response is man...
  </details>

- **2026-08-05** — Chen Zhong, Xiao An, Zijie Wang et al. — [DIVE: Dynamic Iterative Visual Evidence Construction for Efficient Vision-Language Models](http://arxiv.org/abs/2608.04496v1)
  <details><summary>📄 Abstract</summary>
  Visual inputs in vision-language models (VLMs) are often encoded into substantially longer token sequences than text, making visual tokens a major bottleneck for efficient inference. Abundant recent methods address this bottleneck by scoring token importance and pruning low-scoring tokens in a single pass. However, one-shot scoring is insufficient because a token's prompt-relevant usefulness depends on the evidence already retained. Motivated by this insight, we introduce DIVE (Dynamic Iterative...
  </details>

- **2026-08-05** — Quynh Vo, Thong Nguyen, Vinh-Hien Do et al. — [Predict, Then Retrieve: Cross-Instance Future-State Retrieval from Video Prefixes](http://arxiv.org/abs/2608.04426v1)
  <details><summary>📄 Abstract</summary>
  We introduce Predictive State Retrieval (PSR), a task in which a model observes a short video prefix and a temporal question about an object's future state, then retrieves instances from other videos or images that depict that state. Unlike action anticipation, which predicts a label, moment retrieval, which localizes an observed event within a video, or video generation, which synthesizes pixels, PSR combines anticipation with cross-instance retrieval across multiple temporal horizons. We const...
  </details>

- **2026-08-05** — Tinghe Zhang, Jian Xu, Jiaheng Chen et al. — [NodeJEPA: Structure-Conditioned Latent Prediction for Node-Level Graph Self-Supervised Learning](http://arxiv.org/abs/2608.04381v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning on graphs is largely shaped by contrastive methods that depend on carefully designed augmentations, and by generative methods that reconstruct node attributes in the input space. Both paradigms can entangle representations with low-level input statistics rather than with relational structure. Joint-embedding predictive architectures (JEPA) instead learn by predicting latent targets rather than reconstructing inputs. Recent work has explored this idea for graph-level repr...
  </details>

- **2026-08-05** — Max Dupré la Tour, Ayumi Igarashi — [From Cake-Cutting and Necklace-Splitting to Fair Division of Indivisible Items](http://arxiv.org/abs/2608.04340v1)
  <details><summary>📄 Abstract</summary>
  We give an existential transfer framework for converting continuous fair division theorems into guarantees for indivisible items arranged on a path. This allows continuous envy-freeness and consensus results to translate directly into EF$k$-type guarantees for indivisible allocations.   Combining this method with connected cake-cutting theorems, we obtain connected allocations satisfying envy-freeness up to one good and one chore for identical valuations and for arbitrary valuations when the num...
  </details>

- **2026-08-05** — Dong Hae Mangalindan, Anand Gokhale, Francesco Bullo et al. — [Structured LLM Reasoning for Zero-Shot Human--Robot Coordination Under Hidden Goals](http://arxiv.org/abs/2608.04309v1)
  <details><summary>📄 Abstract</summary>
  We present a structured large-language-model (LLM) architecture for zero-shot human--robot coordination in a cooperative construction task with private goal views. Guided by a Dec-POMDP formulation, the architecture decomposes decision-making into (i) action-conditioned Theory-of-Mind (ToM) inference, (ii) hierarchical planning, (iii) conversation interpretation, (iv) action verification, and (v) feedback-based replanning. We compare the proposed method with an ablation without ToM inference and...
  </details>

- **2026-08-04** — Howard Ziyu Han, Nikolas Martelaro — [Enacting Constructive Conflicts with AI Agents to Enhance Reconsideration among Novice Interaction Designers](http://arxiv.org/abs/2608.04166v1)
  <details><summary>📄 Abstract</summary>
  Generative AI agents are increasingly used in interaction design to facilitate ideation and offer critique, often following their own internal reasoning. These interactions tend to add design ideas and expand the design space. Our work explores an antagonistic role for design agents, prompting designers to engage with stakeholder tension. We built an AI agent inspired by adversarial design theory that enacts constructive conflict. We examine the agent's influence in a between-subjects experiment...
  </details>

- **2026-08-04** — Joseph Geo Benjamin, Anil K Jain, Karthik Nandakumar — [Binding Biometrics with AI Agent Identifiers for Delegation of Authority](http://arxiv.org/abs/2608.04292v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of agentic artificial intelligence (AI) systems has raised serious questions about the accountability for tasks performed by AI agents. Ideally, an AI agent must not be allowed to perform critical tasks without explicit authorization by a human operator. Since biometric recognition is one of the most reliable approaches for authenticating individuals, it has the potential to enable authenticated delegation of authority to AI agents. In this work, we present a framework called B...
  </details>

- **2026-08-04** — Agnese Chiatti, Michael Cochez, Cristina Cornelio et al. — [The RAIL Principles for Neurosymbolic AI: Reasoning, Assurances, Interfacing and Learning](http://arxiv.org/abs/2608.04285v1)
  <details><summary>📄 Abstract</summary>
  Neurosymbolic AI systems that integrate machine learning and symbolic reasoning are rapidly gaining attention. They complement the data-intensive statistical approaches of neural networks and language models with symbolic reasoning algorithms to function in high-stakes domains or in low-data regimes that characterize many real-world applications. We argue that the neurosymbolic combination of machine learning and formal reasoning is not a niche approach within AI, but rather includes many alread...
  </details>

- **2026-08-04** — St John Grimbly, Nicolas Kuske, Evert A. Boonstra et al. — [Interoceptive Attention as Dynamic Homeostatic Prioritization in a Foraging Agent](http://arxiv.org/abs/2608.04232v1)
  <details><summary>📄 Abstract</summary>
  Biological systems must regulate competing needs under limited perceptual bandwidth, where sharpening one estimate costs the capacity to sharpen the others. Any fixed-budget system therefore has to decide where to allocate its perceptual precision. We study this in a foraging agent that must keep several bodily needs satisfied to survive, modelled with active inference. At each step it reads its own body-state beliefs, identifies the most-needed channel, and reallocates a fixed budget of interoc...
  </details>

- **2026-08-04** — Simantika Bhattacharjee Dristi, Matthew B. Dwyer — [SONAR: Task-Aware Code Summary Evaluation for LLM Consumers Without References](http://arxiv.org/abs/2608.04195v1)
  <details><summary>📄 Abstract</summary>
  Source code summaries have traditionally been evaluated from a human developer's perspective, with quality determined by how closely they resemble developer-written references and how well they align with human preferences. But this overlooks a growing reality: LLM-based tools and agents increasingly consume code summaries as inputs for software engineering (SE) tasks, and what makes a summary useful for a consuming agent on a task remains largely unexplored. To bridge this gap, we propose SONAR...
  </details>

- **2026-08-04** — Yangxuan Zhou, Sha Zhao, Yuning Chen et al. — [BrainBench: Benchmarking Large Language Models for Comprehensive EEG Understanding](http://arxiv.org/abs/2608.04156v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) analysis extends beyond assigning predefined labels to recordings; it requires workflows connecting natural-language instructions, signal processing, quantitative evidence, and scientific interpretation. We term this capability \emph{comprehensive EEG understanding}. Existing evaluations, however, primarily target isolated decoding tasks or system-specific demonstrations, leaving the competence of large language models (LLMs) insufficiently quantified. We introduce \...
  </details>

- **2026-08-04** — Qile Wang, Ali Salloum, Carolina Coimbra Vieira et al. — [Echoes in the Sky: Computational Thematic Analysis of Online Public Discourse on Bluesky Across Trump's Reelection](http://arxiv.org/abs/2608.04120v1)
  <details><summary>📄 Abstract</summary>
  As political disruption intensifies online discourse, Bluesky has become an important platform for political discussion and public reaction. In this study, we examine large-scale discourse on Bluesky related to U.S. policy developments associated with the Trump administration. Using the historical retrieval API, we collected all available posts matching Trump and related keywords from 2019 to 2026, yielding 38.5 million posts. We leverage a large language model (LLM)-assisted clustering pipeline...
  </details>

- **2026-08-04** — Siwei Yu, Han Guo, Zhenwei Shi et al. — [LoRetta: A Foundation Model and Extensive Dataset for Global-Scale Remote Sensing Dense Image Matching](http://arxiv.org/abs/2608.04106v1)
  <details><summary>📄 Abstract</summary>
  Dense image matching establishes pixel-wise correspondences and underpins broad applications in computer vision and photogrammetry. However, extending dense matching to global-scale remote sensing remains challenging because image pairs may differ in acquisition time, season, viewpoint, spatial resolution, and land-cover state. The resulting large geometric offsets, partial overlap, and intrinsically unmatchable regions make direct dense correspondence prediction unreliable and inefficient. We t...
  </details>

- **2026-08-04** — Ben Wang, Kang Zhou, Lifan Guo et al. — [FinProBench: Evaluating Financial AI Agents with Role-Grounded Rubrics Derived from Professional Deliverables](http://arxiv.org/abs/2608.04077v1)
  <details><summary>📄 Abstract</summary>
  Evaluating financial AI agents requires criteria aligned with real professional work. Existing rubric methods typically derive criteria from task prompts or model outputs, overlooking tacit standards visible only in practitioner deliverables. We introduce FinProBench, a benchmark for professional financial tasks, and Role-Grounded Rubric Construction (RGRC), a reusable pipeline that derives rubrics from deliverables produced by practitioners in the same role. RGRC comprises four stages: Delivera...
  </details>

- **2026-08-04** — Molood Arman — [When Outputs Disperse, Does Epistemic Revision Follow? A Black-Box Diagnostic for Machine Collectives](http://arxiv.org/abs/2608.03722v2)
  <details><summary>📄 Abstract</summary>
  Collective intelligence research treats disagreement as evidence of epistemic diversity: if agents express different views, the group should retain capacity to revise. In LLM collectives this proxy can break: agents can produce diverse-looking arguments while preserving the same conclusion. We operationalize dispersion-revision coupling: the degree to which an intervention that verifiably increases the dispersion of a collective's outputs in embedding space is accompanied by genuine revision of ...
  </details>

- **2026-08-04** — Nolan Cutler, Chia-Chen Kuo, Nanda Velugoti et al. — [CURATE: Leveraging LLM Agents to Compose, Catalog, and Deploy Reproducible Workflows](http://arxiv.org/abs/2608.04270v1)
  <details><summary>📄 Abstract</summary>
  Agentic code generation has shown promise in automating and accelerating software development by utilizing Large Language Models (LLMs) to generate, test, and deploy code. For engineers and scientists, such systems have the potential to accelerate the development of applied and scientific workflows while reducing barriers to entry in domains that have yet to fully realize their benefits. However, a key gap remains: existing coding agents primarily focus on code generation and do not address the ...
  </details>

- **2026-08-04** — Irina Proskurina, Antoine Gourru, Julien Velcin — [The Fairness Collapse Phenomenon: Bias Amplification in Language Models Trained on Synthetic Data](http://arxiv.org/abs/2608.04268v1)
  <details><summary>📄 Abstract</summary>
  Generative models trained on artificially generated data have been shown to exhibit model collapse, resulting in significant performance degradation. As synthetic content increasingly contaminates the training corpora of language models, this raises critical concerns about the use of open data in continued pretraining. Although previous work has demonstrated model collapse in language models, it remains unclear whether exposure to synthetic data amplifies or attenuates the social biases already ...
  </details>

- **2026-08-04** — Zihan Ding, Yinan Liu, Tengfei Ma et al. — [A Comparative Study of Feature Selection Methods for EHR Diagnosis Codes in Opioid Use Disorder Prediction](http://arxiv.org/abs/2608.04180v1)
  <details><summary>📄 Abstract</summary>
  Feature selection is a critical step in electronic health record (EHR)-based predictive modeling, where input variables are often high-dimensional, sparse, noisy, and redundant. Large feature sets not only increase computational burden and overfitting risk, but also make model interpretation difficult, leading to limited usefulness in clinical settings. In this study, we focus on diagnosis-related features and compare five feature selection paradigms for opioid use disorder (OUD) prediction: rec...
  </details>

- **2026-08-04** — Shuhan Xue, Zixin Ding, Yichen Shen et al. — [PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents](http://arxiv.org/abs/2608.04003v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench, a benchmark designed to isolate this question. Each agent runs through ordered sequences of fresh-...
  </details>

- **2026-08-04** — Alexander Meulemans, Maciej Wołczyk, Marissa A. Weis et al. — [A game theory for foundation models shows new paths to rational cooperation through similarity inference](http://arxiv.org/abs/2608.03958v1)
  <details><summary>📄 Abstract</summary>
  As autonomous agents powered by foundation models are increasingly integrated into social and economic systems, understanding the principles governing their collective behavior is essential for ensuring safety and cooperation. Classical game theory, the dominant framework for modeling rational interaction, is built upon the assumption of `decoupled agency,' where agents treat their own decision-making as independent of the environment and other actors. Modern AI agents, however, jointly predict ...
  </details>

- **2026-08-04** — David Guecha — [DS@GT-ARC at eRisk 2026 Task 3: Sparse, Semantic, and LLM Reranking for ADHD Symptom Sentences](http://arxiv.org/abs/2608.03883v1)
  <details><summary>📄 Abstract</summary>
  This paper describes our submissions to eRisk 2026 Task 3, ADHD Symptom Sentence Ranking. The task requires systems to rank candidate Reddit sentences according to their relevance to each of the 18 symptoms in the Adult ADHD Self-Report Scale (ASRS-v1.1). Because no annotated training data were released for this first edition of the task, we relied on zero-shot experimentation, manual validation, and unsupervised or weakly guided retrieval pipelines. Our systems combine sparse BM25 retrieval, ev...
  </details>

- **2026-08-04** — Yash Misra, Javal Vyas, Siddharth Gutta et al. — [ADMITBench: A Safety-Governed Reference Framework for Evaluating the Admissibility of Industrial LLM Advisories](http://arxiv.org/abs/2608.03866v1)
  <details><summary>📄 Abstract</summary>
  This white paper presents ADMITBench, a reference framework for evaluating industrial LLM advisories at the level of the proposed action. The framework implements a versioned, safety-governed evaluation contract that checks whether a recommendation is supported by the available evidence, permitted under the stated authority and procedure, and acceptable under the plant-specific consequence checks encoded in the selected evaluation profile. In this report, \emph{safety-governed} means that eligib...
  </details>

- **2026-08-04** — Zhinan Liu, Jie Li, Mingyu Kang et al. — [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](http://arxiv.org/abs/2608.03838v1)
  <details><summary>📄 Abstract</summary>
  Reasoning-based guard models improve LLM safeguards, but decoding explicit rationales for every interaction makes them costly to deploy. Although latent-reasoning methods reduce token generation by moving reasoning into continuous states, they remain underexplored for safety moderation and lack an inspection interface for deployment. In this paper, we propose LatentGuard, an efficient and inspectable safeguard framework that brings continuous latent reasoning to guard models. LatentGuard uses a ...
  </details>

- **2026-08-04** — Longcheng Li, Qian Li, Xingjian Li et al. — [Impossibility of Perfectly Complete Many-Round Key Agreement in the QROM](http://arxiv.org/abs/2608.03824v1)
  <details><summary>📄 Abstract</summary>
  This paper proves that it is impossible to construct perfectly complete quantum key agreement protocols (QKA) from quantumly secure one-way functions (OWFs) in a black-box manner.   Specifically, consider any protocol in which Alice and Bob exchange only classical messages, make at most $q_{\mathsf{A}}$ and $q_{\mathsf{B}}$ quantum queries, respectively, to a Boolean-valued random oracle, and agree on a shared key with certainty. This paper shows that there exists an eavesdropper, given the clas...
  </details>

- **2026-08-04** — Bakbergen Ryskulov, Iker García-Ferrero, David Montero et al. — [Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chunked KL Loss](http://arxiv.org/abs/2608.03796v1)
  <details><summary>📄 Abstract</summary>
  Small language models are often the only option for deployment under tight latency, cost, and on-premises constraints, but they are rarely trained from scratch: a compressed model is usually recovered through knowledge distillation (KD). This recovery step largely decides the final quality, yet it is expensive. We present a practitioner's study of how to make distillation training efficient, organised around two systems contributions. First, we show that offline KD (caching the teacher's top-$K$...
  </details>

- **2026-08-04** — Zongjian Li, Zhiyuan Yan, Chenxu Bai et al. — [UniWorld-Design: From Pixel Generation to Layer-Native Design](http://arxiv.org/abs/2608.03971v1)
  <details><summary>📄 Abstract</summary>
  We introduce UniWorld-Design, a framework that redefines image generation from flat pixel synthesis to structured visual composition, with semantic RGBA layers as the atomic units of generation, understanding, and editing. Our key insight is that pixels define how an image is rendered, whereas layers define how an image is created, understood, and edited. Just as human designers create and manipulate visual content through layers rather than raw pixels, UniWorld-Design equips multimodal generati...
  </details>

- **2026-08-04** — Ekansh Singh, Eva Samuel, Alessandra Reneau et al. — [Bimanual Manipulation Within an 8 GB Budget: Zero-Copy Sensing and Quantized ACT on an Entry-Level Jetson](http://arxiv.org/abs/2608.03938v1)
  <details><summary>📄 Abstract</summary>
  Bimanual manipulation policies trained with imitation learning are typically evaluated on workstation or datacenter-class GPUs, leaving the cost of deploying them on embedded hardware largely uncharacterized. We present a bimanual SO-101 system running entirely on an NVIDIA Jetson Orin Nano Super (8 GB), the entry-level tier of NVIDIA's embedded line, using a desktop GPU (RTX 3070) only for offline training, evaluated on pick-and-place of a deformable beanbag. First, we build a GStreamer capture...
  </details>

- **2026-08-04** — Adam Coscia, Zeyu Hua, Eric Krokos et al. — [Semantic Bundling: Interactive Node and Edge Bundling to Simplify Knowledge Graphs using Large Language Models](http://arxiv.org/abs/2608.04002v1)
  <details><summary>📄 Abstract</summary>
  We present Semantic Bundling, a visual analytics technique for making sense of text documents represented as knowledge graphs (KGs). Representing a document corpus as a KG makes relationships between entities explicit, making KGs useful both to analyze directly and in computational workflows including ML pipelines and generative AI backends. However, as KGs grow they become difficult to interpret and visualize for specific tasks (e.g., the ``hairball problem''), with the meaning of each relation...
  </details>

- **2026-08-04** — Arslan Battalov, Karim Kramin, Alexander Markotenko et al. — [Muon Meets Mamba: Spectral Optimization for State Space Models](http://arxiv.org/abs/2608.03941v1)
  <details><summary>📄 Abstract</summary>
  Muon is a recent optimizer that orthogonalizes the update to each weight matrix with a Newton-Schulz iteration, which performs steepest descent under the spectral norm. Almost all the evidence for it comes from Transformer models, and its behavior on state-space models is largely unreported. We compare Muon with AdamW on Mamba-2 130M under a controlled protocol that varies only which weight groups are trained with Muon. The benefit is localized. Muon on the output projection alone beats Muon on ...
  </details>

- **2026-08-04** — Marco Giunti, Fabrizia Giulia Garavaglia — [The Transformer Revolution, Part 1: Dynamic Processing through Output- Weight Interconnections](http://arxiv.org/abs/2608.03921v1)
  <details><summary>📄 Abstract</summary>
  This paper offers a new interpretation of the Transformer during inference. Against the "stochastic parrot" view that large language models merely reproduce statistical regularities learned in training, we argue that Transformers construct and apply prompt-dependent transformations whose parameters are generated during inference. We call this form of computation SIDPP: Sequence-level Interactive Dynamic Parallel Processing. The Transformer is interpreted as a system that transforms concepts by m...
  </details>

- **2026-08-04** — Jose M. Álvarez — [Implementing Causal Perception: Competing SCMs and Situated Fairness](http://arxiv.org/abs/2608.03917v1)
  <details><summary>📄 Abstract</summary>
  Causal perception occurs when agents with competing Structural Causal Models (SCMs) of the same system infer different probability distributions, including the hypothetical distributions implied by each agent's SCM under the same set of interventions. It shapes how agents reason about the system and how they perceive its fairness. Causal perception is a promising probabilistic framework, but it has remained purely theoretical. This work provides the first implementation of the causal perception ...
  </details>

- **2026-08-04** — Chuanhao Yan, Xuhan Huang, Yawen Duan et al. — [Sparse Weight Decomposition for Efficient Circuit Extraction](http://arxiv.org/abs/2608.03913v1)
  <details><summary>📄 Abstract</summary>
  Dense pretrained transformers do not naturally expose interpretable units for circuit extraction. Existing approaches obtain such units by learning auxiliary sparse representations or training sparse models, incurring substantial additional computation while potentially introducing a fidelity gap between the representation being analyzed and the original pretrained model. We propose Sparse Weight Decomposition (SWD), which reparameterizes pretrained linear projections by factorizing each weight ...
  </details>

- **2026-08-04** — Abhinav Thorat, Ravi Kumar Kolla, Vishak K Bhat et al. — [GENESIS: Towards Explainable Causal Discovery](http://arxiv.org/abs/2608.03868v1)
  <details><summary>📄 Abstract</summary>
  Causal Discovery (CD) from observational data faces two fundamental challenges. First, purely statistical methods often lack the power to resolve structural ambiguities in low-sample regimes. Second, although LLM-assisted hybrid approaches improve structure recovery through semantic reasoning, the influence of that reasoning on individual edge decisions remains largely opaque. Consequently, existing hybrid methods fail to satisfy a fundamental requirement: explaining why a particular edge is inc...
  </details>

- **2026-08-04** — Yvan Richard — [CPrefix: A Combinatorial Tensor Framework for Structured Discrete Color Mappings](http://arxiv.org/abs/2608.03863v1)
  <details><summary>📄 Abstract</summary>
  Discrete multi-channel mappings are typically represented through sampled values, providing accurate evaluations but limited insight into their underlying structure. We introduce CPrefix, a combinatorial observable representation for discrete mappings, realized within a unified tensor framework that enables representation, reconstruction, and structural analysis.   The framework is based on a counting tensor induced by multinomial counting observables. Its support forms a discrete Pascal simplex...
  </details>

- **2026-08-04** — Xuyang Liu, Yibin Han, Zhenwei Zhang et al. — [DiagChain: A Diagnostic Benchmark for Evaluating LLM Agents on Evidence-Grounded Attack Chain Reconstruction](http://arxiv.org/abs/2608.03591v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents offer a promising approach to attack chain reconstruction by retrieving and interpreting heterogeneous telemetry to infer ordered attacker actions. However, existing benchmarks mainly evaluate final outputs or aggregate accuracy, providing limited insight into how errors arise and propagate across intermediate reasoning stages. We present DiagChain, a diagnostic benchmark for evidence-grounded attack chain reconstruction that enables stage-wise evaluation of LLM...
  </details>

- **2026-08-04** — William Bolton, Philip Torr — [Adversarial Fast-Moving Real-World Domains as Test Beds for Benchmarking AI Scientist Capabilities](http://arxiv.org/abs/2608.03569v1)
  <details><summary>📄 Abstract</summary>
  Benchmarking the ability of AI scientists to generate novel ideas is notoriously difficult. Existing benchmarks in this field have made progress in evaluating scientific reasoning and research replication, but often rely on synthetic tasks or retrospective targets, which may be confounded by prior exposure. We hypothesize that complex, adversarial, fast-moving real-world domains where expert practitioners independently generate observable outputs can provide a practical solution to fill this gap...
  </details>

- **2026-08-04** — Sandy Abdo, Bill Kapralos, Priyamvada Tripathi et al. — [AI-Based Sound Effect Generation: A Narrative Review of Generative Models Across Input Modalities](http://arxiv.org/abs/2608.03742v1)
  <details><summary>📄 Abstract</summary>
  Sound effects play a crucial role in conveying actions, events, and environmental cues across digital applications, often requiring a high degree of variation and contextual adaptability. Artificial intelligence (AI)-driven audio generative models are rapidly growing in popularity and have the potential to transform the way sound is synthesized and used across various applications. In response to this growing momentum, this chapter reviews and analyzes recent AI-based generative models for sound...
  </details>

- **2026-08-04** — Yining Hua, Hongbin Na, Cyrus Ayubcha — [CARE-Bench: Benchmarking Patient-Facing LLM Triage](http://arxiv.org/abs/2608.03731v1)
  <details><summary>📄 Abstract</summary>
  Patient-facing medical LLMs and agents increasingly answer symptom questions before clinician contact, where the key safety question is what action the user should take next. We introduce CARE-Bench, a source-grounded benchmark that evaluates sequential patient-facing triage as a four-label per-turn current-action task. CARE-Bench contains 500 cases and 1,059 evaluated patient-disclosure prefixes reconstructed from medical dialogue, consultation, and follow-up-question sources. We evaluate 11 mo...
  </details>

- **2026-08-04** — Hendrik Vincent Koops, Hao Hao Tan, Elio Quinton — [On the Geometry of Music Bandwidth Extension in Latent Spaces of Audio Codecs](http://arxiv.org/abs/2608.03721v1)
  <details><summary>📄 Abstract</summary>
  Recent audio restoration increasingly relies on large-scale conditional latent generative modeling, including diffusion, Schrodinger Bridges, and Flow Matching variants, to invert degradations such as bandwidth limitation or noise. We present an analysis of the performance of various state-of-the-art methods compared to simple arithmetic transformations in the latent spaces of multiple neural codecs for musical bandwidth extension. We show that estimating a single transport vector between the cl...
  </details>

- **2026-08-04** — Fan Yang, Yuting Su, Xiaobo Wang et al. — [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](http://arxiv.org/abs/2608.03701v1)
  <details><summary>📄 Abstract</summary>
  World-action modeling has emerged as a promising paradigm for robotic control, as it empowers models to go beyond reacting to observations and anticipate how a scene will evolve. However, existing WAMs often incur substantial computational overhead. Pixel-space methods often allocate substantial capacity to visual details that may not be directly relevant to control, while some latent-space methods require multi-stage training to construct the reasoning space. The resulting training cost can mak...
  </details>

- **2026-08-04** — Yiyao Wang, Zhen Wen, Yinghao Tang et al. — [LiveEvalBench: Toward Open-World Evaluation for Web Generation](http://arxiv.org/abs/2608.03689v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly capable of synthesizing executable frontend projects, yet existing benchmarks still treat web generation as a static evaluation problem. We argue that frontend artifacts demand a different paradigm: they are interactive rather than static, admit diverse yet equally valid implementations, and evolve faster than rigid pipelines can accommodate. To address these gaps, we present LiveEvalBench, an automated framework that reformulates web-generation evaluation ...
  </details>

- **2026-08-04** — Abdallah Khemais — [Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model](http://arxiv.org/abs/2608.03629v1)
  <details><summary>📄 Abstract</summary>
  A companion paper studies when activation patching and weight-space ablation agree, inside an idealized model where a conditional computation is carried additively through a residual stream. For the one composition in that model where two carriers are architecturally dependent, an attention head and its own layer's normalization-MLP composition, it derives an exact first-order interaction formula, zero when only the MLP is ablated and second-order bounded when the head is also ablated. That resu...
  </details>

- **2026-08-04** — Behzad Shomali, Markus Frey, David Berghaus et al. — [LoopMTP: A looped transformer guided by latent multi-token prediction](http://arxiv.org/abs/2608.03624v1)
  <details><summary>📄 Abstract</summary>
  Looped transformers have emerged as a parameter-efficient alternative to scaling depth for strong reasoning. By reusing one stack of layers across $T$ iterations, they attain the effective depth and reasoning capabilities of larger models at a fixed parameter count. Yet existing approaches suffer from latent overthinking and undifferentiated computation, largely because intermediate representations receive no guidance across loops. Multi-token prediction (MTP) supplies exactly the dense, forward...
  </details>

- **2026-08-04** — Qin Lei, Hao Wu — [Predictive Enhancement Calibration for Latent Breast MRI Virtual Contrast Enhancement](http://arxiv.org/abs/2608.03612v1)
  <details><summary>📄 Abstract</summary>
  Virtual contrast enhancement (VCE) synthesizes enhanced breast MR images from pre-contrast acquisitions. Modern latent generators offer strong image priors, but their bounded natural-image autoencoders conflict with the non-canonical intensity scale of MRI. We show that the upper bound can alter radiomic fidelity before generation, while scaling source and target independently creates a coordinate inconsistency. We propose Predictive Enhancement Calibration (PEC), which represents each pair in a...
  </details>

- **2026-08-04** — Han Wan, Rui Zhang, Hao Sun — [Large language models for partial differential equation workflows](http://arxiv.org/abs/2608.03600v1)
  <details><summary>📄 Abstract</summary>
  Partial differential equations (PDEs) become actionable in science and engineering not as isolated formulae, but as executable workflows that connect modelling assumptions, governing equations, numerical solvers, diagnostics, and decisions. Large language models (LLMs) are beginning to support such workflows by linking natural language, symbolic mathematics, code, solver outputs, and feedback. Here we examine recent advances in LLM-assisted PDE research across three stages: the discovery and for...
  </details>

- **2026-08-04** — Anton Sokolov — [A Challenge-Nonce Freshness Gap in Project Veraison's TPM Reference Schemes, Found by Appraising Application-Layer Action Evidence End-to-End](http://arxiv.org/abs/2608.03534v1)
  <details><summary>📄 Abstract</summary>
  When an automated agent (an AI agent, say) takes a consequential action, the record it leaves behind is produced by the very software stack whose integrity is in question. A signed log proves which key wrote the record, not what the runtime was. Prior work proposed treating that record (an Action Evidence Package, AEP: a signed append-only record of an action, its authorising principal, and its outcome) as application-layer Evidence under the IETF Remote ATtestation procedureS (RATS) architectur...
  </details>

- **2026-08-04** — Gagan Bhatia, Julian Schlenker, Simone Paolo Ponzetto et al. — [ChronoLens: Measuring Language Change Across Time, Languages, and Linguistic Levels](http://arxiv.org/abs/2608.03507v1)
  <details><summary>📄 Abstract</summary>
  Historical language change affects morphology, syntax, semantics, and pragmatics, yet computational studies typically examine these levels with incompatible representations and therefore cannot determine whether they evolve together across languages. We address this problem by asking how the magnitude and direction of change vary across linguistic levels, languages, and historical periods within a single analytical space. We introduce ChronoLens, a framework that combines frozen multilingual lan...
  </details>

- **2026-08-04** — Minghui Liwang, Wenhan Jia, Xinlei Yi et al. — [Flying over The Uncertain Nature (FORTUNE): Intelligent and Humanistic 3D Path Planning for Low-Altitude Collaboration](http://arxiv.org/abs/2608.03408v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of low-altitude intelligent agents is increasing the demand for timely and socially responsible collaborative sensing in dynamic urban environments. However, jointly addressing heterogeneous spatiotemporal demands, environmental uncertainty, and human-centered operational constraints remains challenging. This paper studies 3D multi-UAV path planning and task assignment under uncertain ground PoI demands. Unlike existing work assuming static and fully known PoIs, we model persis...
  </details>

- **2026-08-04** — Xiaolin Chen, Xuemeng Song, Wenhao Shi et al. — [ArtECulture: Benchmarking Culture-Conditioned Visual Emotion Understanding in Multimodal Large Language Models](http://arxiv.org/abs/2608.03358v1)
  <details><summary>📄 Abstract</summary>
  Existing visual emotion understanding methods typically ignore cultural variations in emotional perception. We introduce culture-conditioned visual emotion understanding, a task that predicts the culture-specific emotional perception of a given image and explains the underlying rationale. Although related benchmarks exist, they are limited by inconsistent individual annotations, which hinder the derivation of majority-supported culture-level emotion labels, and imbalanced cultural coverage. Thus...
  </details>

- **2026-08-04** — Fang Li, Yu He, Haoyang Tong et al. — [iFAN: Inference-Aware Learning for Plain Mask Transformers](http://arxiv.org/abs/2608.03216v1)
  <details><summary>📄 Abstract</summary>
  Query-based mask transformers assemble segmentation outputs through pixel-wise competition among query predictions of the final layer, yet this inference process is not explicitly optimized during training. We identify two key mismatches: the query with the highest probability-mask score does not necessarily produce the most accurate mask, and final-layer decoding may discard superior predictions from intermediate layers. To address these issues, we propose Inference-Aware Learning (iFAN), a gen...
  </details>

- **2026-08-04** — Unggi Lee, Sookbun Lee, Yeil Jeong et al. — [EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners](http://arxiv.org/abs/2608.03206v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) power educational applications from tutoring to essay scoring, but each is a point solution to a single task, and only recently have these point solutions been integrated into agents operating over a learning management system (LMS). Yet tutoring is long-horizon, since a learner improves over days and weeks rather than in a single turn, and no benchmark evaluates an agent tutor across a sustained relationship. We introduce EduClaw-Bench, a benchmark that places an ag...
  </details>

- **2026-08-04** — Yantong Liu, Zheyu Zhang, Runpeng Liu et al. — [NeuroMosaic: Anatomically Grounded Multimodal Large Language Modeling for Molecularly Aware Glioma Reasoning from 3D MRI and Clinical Narratives](http://arxiv.org/abs/2608.03187v1)
  <details><summary>📄 Abstract</summary>
  Multimodal medical large language models remain structurally weak for neuro-oncology because volumetric evidence is compressed into generic visual tokens and diagnostic conclusions often lack an auditable link to MRI regions. We present NeuroMosaic, a 3D multimodal language model that converts multi-sequence brain MRI into anatomy-indexed regional tokens, aligns them with clinical narrative and molecular concepts, and generates evidence-linked outputs. The architecture combines a multi-resolutio...
  </details>

- **2026-08-04** — Xiaonan Xu, Wenjing Wu — [Test-time reasoning effort and unauthorized tool use in language-model agents: a prespecified equivalence study](http://arxiv.org/abs/2608.03169v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents that execute multi-step workflows through tool calls operate under access-control policies that restrict which operations each role may perform. The APIs serving these agents expose a reasoning-effort parameter that operators adjust for cost and latency. Whether this parameter also changes the rate of unauthorized tool use has not been tested by direct manipulation within a single model. We vary reasoning effort (low, max) inside GPT-5.6 across the 14 confirmatory scenarios...
  </details>

- **2026-08-04** — Abdulrahman AlRabah, Weijian Zhou, Xing Gao et al. — [From SQL Errors to Concept Gaps: An AI-Powered Knowledge Graph Analytics Platform for Personalized Feedback](http://arxiv.org/abs/2608.03118v1)
  <details><summary>📄 Abstract</summary>
  This innovative practice full paper describes an AI-powered knowledge graph platform that connects SQL errors to conceptual gaps in undergraduate and graduate database systems courses. Students learning Structured Query Language (SQL) frequently struggle with semantic errors that reflect conceptual misunderstandings rather than syntax mistakes. A query may execute yet return incorrect results due to gaps spanning related concepts; misusing NATURAL JOIN in place of an explicit subquery reflects i...
  </details>

- **2026-08-04** — Mengjie Zhang, Qihui Zhu, Tao Zhang et al. — [GSTEP: Global Spatio-Temporal Density-Driven Visual Token Pruning for Efficient Video Large Language Models](http://arxiv.org/abs/2608.03083v1)
  <details><summary>📄 Abstract</summary>
  Video large language models (VideoLLMs) achieve strong video understanding performance, but their inference remains expensive due to the large number of redundant spatio-temporal visual tokens in long videos. Existing token pruning methods alleviate this cost by reducing redundant tokens, yet most of them rely on segment-level local pruning, where videos are partitioned into isolated segments and tokens are selected independently within each segment. Such designs may under-preserve short but sem...
  </details>

- **2026-08-04** — Yongshi Ye, Biao Fu, Chongxuan Huang et al. — [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](http://arxiv.org/abs/2608.03077v1)
  <details><summary>📄 Abstract</summary>
  Multi-domain machine translation (MDMT) requires more than fluent generation: it demands domain-sensitive translation decisions such as domain disambiguation, terminology control, and stylistic adaptation. Large reasoning models (LRMs) make such decisions explicit through intermediate translation steps, but our analysis across 15 domains and four translation directions shows that this explicit reasoning is double-edged: it improves long-form and high-difficulty translation, yet often drifts in t...
  </details>

- **2026-08-04** — Jiayu Cao, Xingyuan Zeng, feiyu Li et al. — [UrbanAgent: A Tool-Augmented Agent for Cross-System Urban Tasks](http://arxiv.org/abs/2608.03018v1)
  <details><summary>📄 Abstract</summary>
  Modern cities rely on an increasing number of digital services to operate, but residents' daily needs are still difficult to meet. Services are fragmented and have little interoperability, placing a heavy operational burden on users. Existing digital platforms, urban foundation models, and intelligent assistants each address only isolated aspects of an urban task. But they struggle to reliably convert complex natural-language requests into executable cross-system workflows. We propose Urban-Agen...
  </details>

- **2026-08-04** — Molood Arman — [When Outputs Disperse, Does Epistemic Revision Follow? A Black-Box Coupling Diagnostic for Machine Collectives](http://arxiv.org/abs/2608.03722v1)
  <details><summary>📄 Abstract</summary>
  Collective intelligence research treats disagreement as evidence of epistemic diversity: if agents express different views, the group should retain capacity to revise. In LLM collectives this proxy can break: agents can produce diverse-looking arguments while preserving the same conclusion. We operationalize dispersion-revision coupling: the degree to which an intervention that verifiably increases the dispersion of a collective's outputs in embedding space is accompanied by genuine revision of ...
  </details>

- **2026-08-04** — Klaas De Kinder, Amir Bahrami, Christophe Caloz — [Space-Time Event Scattering and Extension Method (STESEM): A Universal Framework for Scattering in Space-Time Metamaterials](http://arxiv.org/abs/2608.03333v1)
  <details><summary>📄 Abstract</summary>
  Space-time metamaterials offer unprecedented control over electromagnetic waves by enabling simultaneous manipulation of spatial and temporal degrees of freedom. However, analytical descriptions of their scattering processes remain fragmented, with existing approaches typically requiring configuration-specific derivations or transformations to specialized reference frames that become impractical for accelerated or multi-interface structures. In this tutorial, we introduce the space-time event sc...
  </details>

- **2026-08-04** — Jiyong Kwon, Yikun Bai, Amirhossein Mollaali et al. — [GraspMeanFlow: SE(3)-Equivariant MeanFlow for Few-Step 6-DoF Grasp Generation](http://arxiv.org/abs/2608.03295v1)
  <details><summary>📄 Abstract</summary>
  Recent data-driven methods for synthesizing 6-DoF grasp poses use generative models to learn complex grasp pose distributions and generate diverse candidate poses. In particular, SE(3)-equivariant flow-based models generate grasp poses that transform consistently with object rotations and translations. However, these methods sample by iterative numerical integration, requiring tens of function evaluations per grasp and limiting their use in real-time manipulation. We propose GraspMeanFlow, an SE...
  </details>

- **2026-08-04** — Shuo Ren, Yaohui Han, Libo Shen et al. — [AgenticECO: An Agentic Framework for ECO on 3D Integrated Circuits](http://arxiv.org/abs/2608.03738v1)
  <details><summary>📄 Abstract</summary>
  As Moore's law slows, the industry is turning to three-dimensional integration; yet in merged 3D-IC flows, routed designs expose bond-level defects with no 2D analogue, and post-route engineering change orders (ECO) remain manual, expertise-bound work. Worse, the standard edit-then-fully-reroute practice entangles a repair with router churn, so a signoff number cannot be attributed to the edit that motivated it. We present AgenticECO, an evidence-gated tool-using agent workflow for 3D-IC ECO on ...
  </details>

- **2026-08-04** — Denys Pushkin, Albert Q. Jiang, Aryo Lotfi et al. — [Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve](http://arxiv.org/abs/2608.03550v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) prompting remains the standard baseline for evaluating models' reasoning abilities. Originally, this technique was introduced to elicit step-by-step reasoning from large language models (LLMs), which would otherwise tend to directly output the final answer. However, many modern LLMs produce CoT-style responses \textit{natively} when presented with reasoning tasks, which made us revisit the effectiveness of standard CoT prompting.   We evaluate several modern mid-sized lang...
  </details>

- **2026-08-04** — Fengjunjie Pan, Alois Knoll — [Dr. AGENTONOMICS: A Didactic Experiment of AGENTONOMICS](http://arxiv.org/abs/2608.03524v1)
  <details><summary>📄 Abstract</summary>
  AGENTONOMICS is a framework that treats AI agents as economic entities that can be designed, managed, and governed through an integrated management architecture. Dr. AGENTONOMICS is its first application: a lecture agent developed in the context of the TUM course on AI agents in business administration. Conceived during the winter semester 2025/26 and first introduced to students in the summer semester 2026, it serves as a didactic experiment in which the agent is both the object that students s...
  </details>

- **2026-08-04** — Xiuyuan Zhu, Ke Lu, Kun Dong et al. — [Hi-Token: Hierarchical Coordinate Tokenization for Generative Visual Grounding](http://arxiv.org/abs/2608.03471v1)
  <details><summary>📄 Abstract</summary>
  Generative Vision-Language Models (VLMs) commonly treat bounding-box coordinates as independent output symbols, leaving numerical order and axis semantics implicit. We identify this representation as an important source of error in visual grounding. Hi-Token encodes each coordinate with axis-specific tokens for the hundreds, tens, and ones digits, which adds coarse-to-fine structure and increases token reuse while retaining the existing VLM architecture. Hi-GAR complements this representation wi...
  </details>

- **2026-08-04** — Zhenghan Chen, Zekai Shao, Lidan Tan et al. — [ChartAnno: Evaluating MLLMs for Chart Annotation Generation](http://arxiv.org/abs/2608.03464v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have made significant progress in chart understanding, generation, and editing, but their ability to annotate existing charts remains underexplored. Annotating charts is a common yet challenging communicative task, requiring models to infer intended messages, interpret chart semantics, and place appropriate textual or graphical elements. To address this gap, we introduce ChartAnno, a benchmark for evaluating MLLMs on chart annotation generation. It contai...
  </details>

- **2026-08-04** — Xingyang Yu — [3D Gravity Does Not Average Like Narain at Genus One: Rigidity of Virasoro Topological Boundaries](http://arxiv.org/abs/2608.03459v1)
  <details><summary>📄 Abstract</summary>
  Motivated by the proposed relation between 3D gravity and the doubled Virasoro TQFT, and by the associated program of ensemble holography, we ask whether ensemble holography in AdS$_3$/CFT$_2$ can be understood as an average over absolute 2D CFTs obtained by varying the topological boundary condition of the doubled Virasoro TQFT. We show that, at genus one and in the ordinary nondegenerate sector, every vacuum-normalized, modular-invariant genus-one pairing that acts boundedly on the auxiliary $...
  </details>

- **2026-08-04** — Matteo Morini, Pietro Terna — [A Note on Reinforcement Learning to Develop Self-defined Agents' Behavior](http://arxiv.org/abs/2608.03445v1)
  <details><summary>📄 Abstract</summary>
  The key point in this note is the self-development of simple behavior strategies, consistently with the bounded rationality hypothesis. Our artificial agents adopt learning techniques, mainly unsupervised, to achieve internal consistency in their behavior, with unexpected results. Those results can be considered mainly as the effects of the observer interpretation. The first technique in use has the name Cross Targets: to train the learning agent we use data crossed between the guesses about the...
  </details>

- **2026-08-04** — Jakub Rada, Viliam Lisý — [Towards Improving Sequential Decision-Making in LLM Agents via Experience Memory](http://arxiv.org/abs/2608.03420v1)
  <details><summary>📄 Abstract</summary>
  Large language models have improved substantially on single-shot reasoning tasks, but their performance in sequential decision-making is less well understood. We study this on fully-observable two-player zero-sum games, which provide ground-truth evaluation: outcomes are determined by the rules, and optimality of individual moves can be computed or approximated, without relying on a judge model. Across model tiers, LLMs play suboptimally in simple games such as tic-tac-toe or Connect Four, and l...
  </details>

- **2026-08-04** — Adam J. Stewart, Heng Fang, Isaac A. Corley et al. — [Earth Embeddings](http://arxiv.org/abs/2608.03410v1)
  <details><summary>📄 Abstract</summary>
  Earth observation is moving from foundation models that users must run themselves toward embedding products that package model feature outputs as reusable data without needing to download and process the imagery used to generate them. Earth embeddings are vectors that summarize locations, image patches, or pixels, letting users analyze compact features instead of repeatedly training or running large models on raw satellite imagery. This chapter explains the main types of Earth embeddings, from i...
  </details>

- **2026-08-04** — S. Miret-Artés — [The intermediate scattering function of an interacting adlayer as a characteristic function: a closed-form theory of Ising lattice-gas surface diffusion](http://arxiv.org/abs/2608.03398v1)
  <details><summary>📄 Abstract</summary>
  The intermediate scattering function (ISF) measured by helium spin-echo is a characteristic function (CF): the Fourier transform of the distribution of adsorbate displacements, whose value at zero time is the static structure factor. We use this double role to bring lateral interactions of Ising lattice-gas type into surface diffusion. The ISF then follows in closed form in momentum transfer, time, coverage and temperature, and with it the whole linear-response hierarchy. A single correlation pa...
  </details>

- **2026-08-04** — Shahrukh Mohiuddin, Chalamalasetti Kranti, Sherzod Hakimov et al. — [Don't Let Me Ask for It: LLMs Show Deficiencies in Active Multi-Turn Information Acquisition for Abductive Inference](http://arxiv.org/abs/2608.03388v1)
  <details><summary>📄 Abstract</summary>
  Abductive reasoning requires forming hypotheses that explain observed evidence and revising them as new evidence becomes available. While large language models (LLMs) are often evaluated on whether they solve abductive reasoning tasks correctly, less is known about how they acquire evidence, update their hypotheses, and decide when to stop. We introduce Alien Abduction game, an interactive probe for studying these behaviours under different interaction modes. The modes vary in whether evidence i...
  </details>

- **2026-08-04** — Xi Liu, Wenxi Fang, Ken Perlin — [Organic liquid scintillator neutrino detector experiment, theoretical modeling, and computational simulation](http://arxiv.org/abs/2608.03359v1)
  <details><summary>📄 Abstract</summary>
  The Liquid Scintillator Neutrino Detector (LSND) experiment aimed at investigating neutrino oscillations, particularly the transformation of muon-type antineutrinos (\(\overlineν_μ\)) into electron-type antineutrinos (\(\overlineν_e\)). This phenomenon challenges the Standard Model's assumption of massless neutrinos. The LSND employed a large organic liquid scintillator (LS) to detect low-energy neutrino interactions, enhanced by the addition of metal ions such as gadolinium (Gd) for improved si...
  </details>

- **2026-08-04** — Junhyeok Kang, Sangjun Han, Hyeokjun Choe et al. — [Traceable Multi-Agent System for Knowledge-Based Forecasting](http://arxiv.org/abs/2608.03339v1)
  <details><summary>📄 Abstract</summary>
  Enterprise forecasting increasingly relies on autonomous agents that interpret documents, search for data, generate code, and revise models. While this autonomy helps build adaptive forecasting pipelines, it also makes it difficult for practitioners to inspect why a forecast changed, which evidence supported the change, and how data and modeling choices were revised. We present TraceMAS, an interactive demo system for traceable multi-agent forecasting. TraceMAS organizes agent outputs around two...
  </details>

- **2026-08-04** — Sunyeop Kim, Insung Kim, Jian Guo — [Provably Learning Multi-Head Attention with Queries](http://arxiv.org/abs/2608.03294v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of learning multi-head softmax attention from black-box input-output access. The learner may query arbitrary real-valued token sequences and observe only the scalar output at the final token. Recent work gives an algorithm using $O(d^2)$ value queries to recover the single-head parameters $(W,v)$. For multiple heads, the same work establishes identifiability under the assumption that the heads occupy pairwise orthogonal subspaces. Applying the single-head recovery algorithm ...
  </details>

- **2026-08-04** — Changqing Zhou, Yueru Luo, Zeyu Jiang et al. — [UniNav: A Unified World-Action Diffusion Model for Visual Navigation](http://arxiv.org/abs/2608.03244v1)
  <details><summary>📄 Abstract</summary>
  Image-goal visual navigation is a fundamental capability for embodied agents. Existing navigation policies efficiently predict waypoint trajectories but lack visual foresight, while navigation world models can anticipate future observations but often require costly planning rollouts. We present UniNav, a unified world-action model that generates future visual observations and continuous waypoint trajectories through a single diffusion process. Given history frames and a goal image, UniNav jointl...
  </details>

- **2026-08-04** — Savvas Panagi, Chrysovalantis Spanias, Petros Aristidou — [Dynamic Flexibility Requests in Local Flexibility Markets: Quantifying the DSO Willingness to Pay](http://arxiv.org/abs/2608.03226v1)
  <details><summary>📄 Abstract</summary>
  Local Flexibility Markets (LFMs) require Distribution System Operators (DSOs) to determine both the quantity of flexibility to procure and the corresponding willingness to pay during market clearing. Existing approaches typically rely on unrealistic centralized AC-OPF clearing algorithms or strictly localized, static flexibility requests driven primarily by congestion management, while the economic value of flexibility is largely neglected. This paper proposes a dynamic flexibility-request metho...
  </details>

- **2026-08-04** — Aye Aye Maung, Qi Zheng — [Evaluating Treatment Effects using Group Testing with Retesting of Positive Groups](http://arxiv.org/abs/2608.03224v1)
  <details><summary>📄 Abstract</summary>
  Group testing is an established, highly cost-effective strategy for population-level disease surveillance that identifies positive individuals by pooling biological specimens. Originally introduced during World War II for large-scale screening and heavily utilized in modern high-throughput public health infrastructure, traditional group testing methods are restricted to purely associational analyses. Consequently, they lack the capacity to infer the direct causal effect of an intervention when i...
  </details>

- **2026-08-04** — Thanasis Lianeas, Alkmini Sgouritsa, Minas Marios Sotiriou — [EFX Allocation In (Multi)Hypergraphs](http://arxiv.org/abs/2608.03171v1)
  <details><summary>📄 Abstract</summary>
  We study fair allocations of indivisible goods among agents with heterogeneous monotone valuations. As fair we consider the allocations that are envy-free-up-to-any-good (EFX). Finding if EFX alloca- tions always exist, even for agents with additive valuations, is a major open problem in Fair Division. Christodoulou et al. (2023) introduced the (multi-hyper)graph setting, where agents and goods are represented by vertices and edges of a graph, respectively, and only the endpoints of an edge may ...
  </details>

- **2026-08-04** — Tu Tran Do, Nhat Ngoc Nguyen, Khanh-Tung Tran et al. — [VIVID: A Culturally Grounded Benchmark Exposing the Figurative Language Gap in Vietnamese NLP](http://arxiv.org/abs/2608.03095v1)
  <details><summary>📄 Abstract</summary>
  We present VIVID (Vietnamese Idioms for Validation and Interpretation Depth), the first systematic benchmark for evaluating culturally grounded figurative language understanding in Vietnamese. VIVID comprises 1,636 idioms and proverbs annotated with five complexity traits (literal expressions, pragmatic nuances, Sino-Vietnamese terms, uncommon vocabulary, folk knowledge) and seven semantic themes. We establish an evaluation framework combining generative and discriminative tasks, proposing an LL...
  </details>

- **2026-08-04** — Gongyue Zhang, Honghai Liu — [Joint Affine Spectral Shaping: Coupling Weight and Bias Updates Beyond Weight-Only Muon](http://arxiv.org/abs/2608.02991v1)
  <details><summary>📄 Abstract</summary>
  Matrix spectral optimizers reshape weight-update spectra but usually delegate vector-valued biases to a separate optimizer. We study whether this separation is neutral. We formulate each affine layer as a joint momentum matrix $A=[M_W,αm_b]$ and apply a capped regularized-inverse spectral map to the complete matrix, producing both the weight and physical bias updates. A strict five-seed ablation on a four-layer BERT-mini trained from scratch on IMDb compares exact-SVD Muon, weight-only inverse s...
  </details>

- **2026-08-03** — Malik Khalaf, Yara Shamshoum, Nitzan Hodos et al. — [AnchorKV: Anchor-Residual KV Cache Compression](http://arxiv.org/abs/2608.02901v1)
  <details><summary>📄 Abstract</summary>
  The key-value (KV) cache is the primary memory bottleneck in long-context LLM inference. Existing approaches attack it from opposite ends: eviction methods permanently discard tokens, degrading performance whenever a discarded token later proves essential, while quantization methods retain all tokens at low precision but offer limited compression. We propose AnchorKV, a compression scheme that shrinks the cache by $20\times$ without discarding a single token. AnchorKV represents the cache using ...
  </details>

- **2026-08-03** — Ioana Boureanu, R. Ramanujam, Srinibas Swain — [Decidability of Parameterised Dolev-Yao Secrecy](http://arxiv.org/abs/2608.02838v1)
  <details><summary>📄 Abstract</summary>
  We study the verification of parameterised secrecy for cryptographic protocols in the Dolev-Yao model, where the number of protocol sessions is unbounded and treated as a parameter. This differs fundamentally from classical Dolev-Yao secrecy, which asks whether a protocol leaks a secret irrespective of the number of executions; our question is whether secrecy holds uniformly across all system sizes, where such a size is a parameter. This parameterised perspective captures how attacks scale with ...
  </details>

- **2026-08-03** — Yinxiao Zhang, Sen Wang, Yi Gao — [Schedule-Informed Temporal Fusion Forecasting of Hourly Airport Security-Checkpoint Throughput](http://arxiv.org/abs/2608.02950v1)
  <details><summary>📄 Abstract</summary>
  Checkpoint staffing requires accurate forecasts of when screening demand will occur, yet flight schedules record departure times rather than passenger arrival times at security checkpoints. This study develops a framework that converts known flight schedules into temporally aligned signals for forecasting hourly checkpoint throughput. Using 2023-2024 Transportation Security Administration throughput data and Cirium Diio flight schedules for Hartsfield-Jackson Atlanta International Airport, domes...
  </details>

- **2026-08-03** — Xiaocheng Lu, Hualei Zhang, Shuhan Guo et al. — [OPTD: On-Policy Transition Distillation with Consistency-Guided Adaptive Compression for Few-Step Diffusion Language Models](http://arxiv.org/abs/2608.02942v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (dLLMs) can predict many tokens in parallel, but accurate generation still requires many iterative denoising steps. Few-step distillation accelerates decoding by compressing multiple teacher steps into a single student transition. However, existing methods construct supervision on off-policy trajectories. At inference, the student's early parallel commitments alter the context of later predictions, so the states it actually visits drift away from the supervised ones--pr...
  </details>

- **2026-08-03** — Bo Liu, Qiang Liu — [Maglev: Sliding Recurrent Memory](http://arxiv.org/abs/2608.02870v1)
  <details><summary>📄 Abstract</summary>
  We introduce \ours{}, a recurrent Transformer architecture with fixed-size memory that generalizes sliding-window attention while remaining parallelizable during training. \ours{} consists of two coupled models: a prefiller $Q$, which leverages full attention\footnote{In practice, we use interleaved full and sliding-window attention for $Q$, as this yields stronger performance. The essential requirement is that $Q$ be more expressive than $P$, with access to the full history.} to produce memory ...
  </details>

- **2026-08-03** — Maya Okawa — [Emergence of Biased Consensus in Multi-Agent LLM Debates](http://arxiv.org/abs/2608.02827v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM debates achieve strong performance on decision-making tasks as well as problem-solving benchmarks, yet their safety and fairness risks remain poorly understood. Notably, interaction can amplify the biases of single LLMs, raising concerns for real-world deployment. We identify the emergence of collective (often biased) norms in multi-agent LLM debates and show that noise (e.g., LLM sampling temperature) is a key driver. To explain this, we propose an analytical framework drawing o...
  </details>

- **2026-08-03** — Jiazhen Liu, Mingkuan Feng, Long Chen — [Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for MLLM-Based Segmentation](http://arxiv.org/abs/2608.02791v1)
  <details><summary>📄 Abstract</summary>
  MLLM-based segmentation faces a core segmentation trilemma: high segmentation performance, preserved dialogue ability, and fast inference. Embedding-prediction methods may disrupt language modeling through pixel-level objectives, whereas next-token generation is inefficient for dense masks. We propose All-Mask Prediction, decoupling autoregressive dialogue from non-autoregressive mask prediction. Its binary instantiation, STAMP (Simultaneous Textual All-Mask Prediction), emits an in-vocabulary <...
  </details>

- **2026-08-03** — Xinjie Yao, Xingxin Xu, Xiyuan Gao et al. — [Towards a new paradigm of scientific discovery with socialized artificial intelligence](http://arxiv.org/abs/2608.02775v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery has advanced through successive transformations in the organization of knowledge. Observation and experimentation established the empirical foundations of science. Theory made it possible to derive general principles from particular phenomena. Computation extended inquiry into systems beyond direct observation, while data-intensive methods opened new spaces of pattern and prediction. Science now confronts a different frontier. The central challenge is no longer simply to pro...
  </details>

- **2026-08-03** — Hongjie Zhou, Shiqin Wang, Haoyang Chen et al. — [RSVideo: Are Your Vision-Language Models Ready for Remote Sensing Videos?](http://arxiv.org/abs/2608.02039v2)
  <details><summary>📄 Abstract</summary>
  Remote-sensing videos enable real-time observation of changes in target attributes, short-term activities, and scene evolution. They record motion, actions, interactions, and scene changes that cannot be captured by isolated images. Existing models primarily target single images or discrete temporal observations spanning a long time range. However, a unified evaluation setting for assessing vision-language models on continuous remote-sensing video understanding remains lacking. We introduce RSVi...
  </details>

- **2026-08-03** — Zetong Xiong, Qiao Zhao, Jun Zhang et al. — [BulkPR-Bench: Benchmarking Queue-Level Governance of Interacting Pull Requests](http://arxiv.org/abs/2608.02685v1)
  <details><summary>📄 Abstract</summary>
  Coding-agent benchmarks increasingly cover long-horizon, end-to-end, and interactive development, but typically retain one requested outcome or a fixed change sequence. Sequential policies can process a pull-request (PR) queue one candidate at a time, but when queued PRs interact, maximizing safe delivery can require jointly deciding which changes to merge and in what order. We introduce BulkPR-Bench, an executable benchmark in which an agent must recover consequential PR relations and return a ...
  </details>

- **2026-08-03** — C. Alexander Rodriguez — [Non-Abelian Hirota-Miwa Equations for the KPZ Universality Class](http://arxiv.org/abs/2608.02772v1)
  <details><summary>📄 Abstract</summary>
  This work introduces an algebraic framework yielding explicit, closed matrix differential-difference equations for eighteen models in the exactly solvable sector of the KPZ universality class across four scaling regimes. By organizing Fredholm determinant data into an overdetermined linear problem on a directed lattice graph, we derive a compatibility system termed the diamond equations. Elementary seed data extracted from the shift structure of the Fredholm kernel provides simple solutions to t...
  </details>

- **2026-08-03** — Yu Yang, Xuemeng Yang, Licheng Wen et al. — [Quo Vadis, World Modeling?](http://arxiv.org/abs/2608.02713v1)
  <details><summary>📄 Abstract</summary>
  Continually improving agents require dynamic interaction feedback beyond static supervision, yet direct real-environment interaction is costly, slow, unsafe, and hard to parallelize. World modeling offers a natural intermediate proxy that allows agents to query lower-cost, more controllable feedback before committing to real actions. Classical world models instantiate this proxy primarily through future physical-state prediction, a formulation useful yet narrow for agents that require actionable...
  </details>

- **2026-08-03** — Dorieh Alomari, Irfan Ahmad, Maged S. Al-shaibani — [Character Iconicity vs. Arbitrariness: An Arabic NLP Perspective](http://arxiv.org/abs/2608.02935v1)
  <details><summary>📄 Abstract</summary>
  Arabic script uses 28 letters, many of which share a common base shape (rasm) and are distinguished only by dot placement. Because early Arabic manuscripts were written without dots yet remained interpretable, dot removal offers a natural test of whether these visual distinctions are functionally necessary. Prior work has shown that dotless Arabic can remain readable and effective for natural language processing (NLP), but it remains unclear whether this success depends on preserving the origina...
  </details>

- **2026-08-03** — Nathan Canen, Ted Enamorado — [When Predictions Become Regressors: A Split-Sample Correction for Biases in Downstream Inference](http://arxiv.org/abs/2608.02909v1)
  <details><summary>📄 Abstract</summary>
  Prediction-based methods, including Large Language Models (LLMs) and other machine learning techniques, are often used to construct measures of political phenomena that are difficult to quantify directly, such as policy positions in manifestos or emotions expressed on social media. In many applications, these prediction-generated measures are used as explanatory variables in regression models, even though they are measured with error. This leads to biased estimates. In this paper, we propose a s...
  </details>

- **2026-08-03** — Johanna Borissova — [Formation of extremal regular black holes](http://arxiv.org/abs/2608.02908v1)
  <details><summary>📄 Abstract</summary>
  Static and slowly evolving regular black holes with a non-extremal inner horizon are generally expected to suffer from mass inflation. Here we consider the scenario of asymptotic gravitational collapse into extremal regular black holes as candidate eternal endpoints. To that end, we first construct geometric models of static spherically symmetric single-horizon extremal and double-horizon inner-extremal regular black holes for generic black hole mass as the only dimensionful scale. These spaceti...
  </details>

- **2026-08-03** — Osman Ergeç — [Supersymmetric Twisted Carroll Theories](http://arxiv.org/abs/2608.02890v1)
  <details><summary>📄 Abstract</summary>
  We study the recently discussed $2+1$-dimensional Hull-type twisted $\mathcal{N}=2$ Carroll superalgebra. This structure admits both electric- and magnetic-type realizations at the level of the supersymmetry transformations. At the Lagrangian level, magnetic Carroll theories describe fields that propagate in space while remaining constrained in time, and vice versa for electric theories. We first realize this symmetry algebra through the dimensional reduction of a $2+2$-dimensional $\mathcal{N}=...
  </details>

- **2026-08-03** — Nitish Nagesh, Elahe Khatibi, Thomas Dean Hughes et al. — [GoT-CD: Graph-of-Thoughts Causal Discovery and the Fragility of Post-hoc Path-Specific Fairness Audits](http://arxiv.org/abs/2608.02877v1)
  <details><summary>📄 Abstract</summary>
  Causal discovery recovers directed structure from observational data and is increasingly used in clinical settings to support mechanism reasoning and fairness audits of predictive models. Path-specific counterfactual fairness asks whether a protected attribute influences an outcome through illegitimate pathways, but these estimands are defined relative to a supplied causal graph and therefore inherit whatever errors the discovery step introduces. Discovery methods are routinely scored on aggrega...
  </details>

- **2026-08-03** — Abdallah Lamane, Abdul Rahman Diab, Ren-Chin Wu et al. — [SAGE: Semantic Explainability of Attention-Based Survival Models in Computational Pathology](http://arxiv.org/abs/2608.02803v1)
  <details><summary>📄 Abstract</summary>
  Attention-based multiple instance learning (ABMIL) is the predominant approach for slide-level prediction in computational pathology, yet its attention maps provide only local explanations: they indicate where a model focuses but not which histological features drive its predictions or how the model behaves across a patient cohort. We present Semantic Attention Global Explanations (SAGE), a post-hoc framework that extracts global, language-grounded explanations from a frozen ABMIL model. Using a...
  </details>

- **2026-08-03** — Zixuan Huang, Yang Zhou, Kaixuan Wang et al. — [Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs](http://arxiv.org/abs/2608.01755v2)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language-Action (VLA) models for autonomous driving (AD) increasingly utilize chain-of-thought (CoT) supervision to enhance the reasoning capabilities of their Vision-Language Model (VLM) components, yet existing annotation pipelines commonly expose the teacher model to the logged ground-truth (GT) future trajectory. We empirically show that this induces trajectory anchoring bias: teacher models rationalize the revealed outcome rather than infer a decision from scene evidence, prod...
  </details>

- **2026-08-03** — Salma El Yadouni, Guanyi Li — [TraceCompiler: Skill-Guided Mining and Compilation of LLM Agent Traces into Mostly Deterministic Workflows](http://arxiv.org/abs/2608.02680v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language-model agents repeatedly rediscover procedures they have already executed, producing traces that mix reusable structure with retries, exploration, accidental ordering, and repeated lookups. We present TraceCompiler, a skill-guided system that mines clusters of noisy agent traces and compiles them into executable, mostly deterministic workflows. It admits an inter-tool dependency only when a consumer argument contains a value attributable uniquely to an earlier producer; every ...
  </details>

- **2026-08-03** — Yiran Gao, Tao Li, Kim Hammar — [Agentic Incident Response through Digital Twin-Enhanced Multiscale Planning](http://arxiv.org/abs/2608.02422v1)
  <details><summary>📄 Abstract</summary>
  Incident response is currently managed by security operators using predefined playbooks, resulting in slow, labor-intensive security decision-making processes. Consequently, there is a growing need for automated incident response planning. Decision-theoretic approaches based on control, optimization, and reinforcement learning have been proposed to automate such planning tasks with well-grounded approaches, yet most of which, while guaranteeing strong performance, are limited to abstract models ...
  </details>

- **2026-08-03** — Ting-Jui Chang — [A Spectral Filtering Approach to Regret Analysis of Distributed Online Control for Linear Dynamical Systems](http://arxiv.org/abs/2608.02375v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the distributed online control problem over a network of linear time-invariant (LTI) systems in the presence of adversarial disturbances and time-varying convex costs. The network cost is characterized by the summation of local cost functions, where each local function is sequentially revealed only to the corresponding agent. The goal of each agent is to generate a control sequence, using only local observations and neighbor communication, that competes with the best {\it cent...
  </details>

- **2026-08-03** — Dunjie Lu, Shuai Bai, Tianyi Bai et al. — [Qwen-CUA: Native Computer Use for (almost) Everything](http://arxiv.org/abs/2608.02352v1)
  <details><summary>📄 Abstract</summary>
  Native computer use offers a general interface for agents to operate almost any software available to people, but requires long-horizon state tracking, large-scale interactive experience, and learning from sparse yet verifiable outcomes. We introduce Qwen-CUA, a native computer-use agent with a 397B-A17B Qwen mixture-of-experts backbone. It observes only screenshots and acts through keyboard and mouse events, without DOM trees, accessibility metadata, or task-specific APIs. Its scaffold maintain...
  </details>

- **2026-08-03** — Jingxi Wei — [Trajectories That Segment Themselves: Agent-Declared Boundaries as a Training Unit](http://arxiv.org/abs/2608.02302v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon coding-agent trajectories are poorly matched to the credit units available to train on: a single action has no stable value, an episode label merges productive exploration with abandoned directions, and a fixed window cuts where the logging mechanics fall. We introduce collection-time semantic self-segmentation, in which a declarative contract has the acting agent expose its own boundaries while the trajectory is generated. Instantiated with falsifiable causal hypotheses, successive...
  </details>

- **2026-08-03** — K. Jack Scott, Narun Pat, Veronica Liesaputra — [Divergent large language model predictions from convergent representations in ambiguous word pairs](http://arxiv.org/abs/2608.01816v1)
  <details><summary>📄 Abstract</summary>
  In this work we investigate how decoder-only transformers resolve lexical ambiguity through layer-by-layer analysis of three models spanning three parameter sizes (GPT-2-Small-117M, Llama-3.2-3B, Qwen2.5-32B). For both homonyms and polysemes, we find that representations become maximally distinct in middle layers, then partially reconverge in late layers, while the KL divergence between their next-token predictions reaches its maximum in the final layers. The activation patching experiment provi...
  </details>

- **2026-08-03** — Shuyang Xie, Shuxiao Xie, Feng Zhu et al. — [Coding Agents as Test-Suite Auditors: Finding What Official Suites Miss While Approaching What They Catch](http://arxiv.org/abs/2608.01715v1)
  <details><summary>📄 Abstract</summary>
  Online-judge verdicts and the datasets and benchmarks built on them are treated as ground truth for evaluating and training large language models for code. Yet prior audits have sounded a warning: official suites accept buggy submissions. These audits, however, stop at the warning and offer no practical remedy. Our remedy has two parts: an off-the-shelf coding agent, serving as a test-suite auditor, both builds adversarial test suites to expose what official suites miss and supplies these suites...
  </details>

- **2026-08-03** — Jiajun Liang, Yucheng Liao, Yukang Cao et al. — [AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling](http://arxiv.org/abs/2608.02602v1)
  <details><summary>📄 Abstract</summary>
  Language remains an outlier in generative modeling: while images, video, and audio are increasingly modeled in continuous latent spaces, text generation still relies predominantly on discrete tokens. Existing continuous language models either inherit embedding spaces not designed for joint generation and decoding, or compress autoencoded latents to ease diffusion, sacrificing token-level fidelity. Instead of simplifying the representation to suit the generative model, we preserve a high-capacity...
  </details>

- **2026-08-03** — Chunhao Cai — [A Response Calculus for Liouville Brownian Motion I: Simple Spectrum, Joint Eigenvalue Densities, and Ward Identities](http://arxiv.org/abs/2608.02459v1)
  <details><summary>📄 Abstract</summary>
  We develop a response calculus for Dirichlet Liouville Brownian motion under Cameron--Martin shifts of the Gaussian free field. On every bounded connected planar domain, without boundary regularity assumptions, we prove throughout the full subcritical range $0<γ<2$ that the generator has almost surely simple spectrum and that every finite vector of ordered eigenvalues has an absolutely continuous law. This resolves the open simple-spectrum problem for Dirichlet Liouville Brownian motion.   The c...
  </details>

- **2026-08-03** — Ambarish Govindarajulu Kaliamurthi, Kaikai Liu — [MoRAL: Sensor-Grounded BEV Reasoning for Compact VLMs toward Edge-Oriented Autonomous Driving](http://arxiv.org/abs/2608.02449v1)
  <details><summary>📄 Abstract</summary>
  Deploying vision-language models (VLMs) for safety-critical spatial reasoning on resource-constrained autonomous driving platforms requires both compact model size and reliable metric grounding. We present MoRAL (Multimodal Reasoning for Autonomous Language Models), a two-stage fine-tuning pipeline that teaches Cosmos-Reason2-2B to first read a physics-encoded Bird's Eye View (BEV) representation and then reason over it for driving decisions. The BEV image encodes LiDAR metric distance as color ...
  </details>

- **2026-08-03** — Jiaming Chen, Guoan Xu, Aoshen Huang et al. — [DF$^3$: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation](http://arxiv.org/abs/2608.02428v1)
  <details><summary>📄 Abstract</summary>
  Forecasting future states from video sequences is a critical challenge for autonomous robotic systems and a fundamental objective of world modeling. Prior generative methods operating at the pixel level inevitably overemphasize task-irrelevant details, leading to prohibitive computational overhead. While latent-based approaches attempt to mitigate this by predicting features directly, the persistent reliance on heavy decoders for state-to-task mapping remains a computational bottleneck. In this ...
  </details>

- **2026-08-03** — Hao Shen, Junyu Guo, Tian Cui et al. — [MechGeo: Autoformalizing and Proving Euclidean Geometry in Lean 4](http://arxiv.org/abs/2608.02295v1)
  <details><summary>📄 Abstract</summary>
  We present MechGeo, a Mathlib native agentic framework that jointly addresses faithful autoformalization and certified proof construction for Euclidean geometry. In this framework, GeoFormalizer represents informal problems in GeoIR, deterministically translates them into Lean 4, and iteratively repairs candidate statements using structural diagnostics and semantic evaluation. GeoProver constructs geometric proof plans, derives intermediate lemmas, and selectively algebraizes suitable subgoals t...
  </details>

- **2026-08-03** — Abdul Kalam, Prasenjit Deb, Akitada Sakurai et al. — [Quantum computer-based simulation of Stark many-body localization in a 1D Fermi-Hubbard model](http://arxiv.org/abs/2608.02245v1)
  <details><summary>📄 Abstract</summary>
  Many-body localization (MBL) is a dynamical phenomenon that describes the non-ergodicity of isolated quantum many-body systems. In contrast to thermalization, this phenomenon leads to a long-lived memory of initial states of local systems and slow growth of entanglement. In this work, we study Stark MBL in a 12-qubit correlated fermionic system described by the one-dimensional Fermi-Hubbard model using Hamiltonian simulation on an IBM superconducting qubit quantum computer. To enable such a comp...
  </details>

- **2026-08-03** — Luciano Ciamarone, Dora Motèque, Marco Giordano — [Sounding Canvas: Embedding Algorithms in Networked, Sensorial Sound Art](http://arxiv.org/abs/2608.02219v1)
  <details><summary>📄 Abstract</summary>
  Sounding Canvas turns painting into a touch-responsive multimodal installation by embedding capacitive sensors, real-time decision models, and networking inside the canvas. Touches trigger spatialised sounds that appear to emanate from the painting itself. The work embeds algorithms physically, as sensing and computation concealed behind the artwork; perceptually, through an offline visual-to-sonic mapping that aligns a painting's features with sound descriptors; and performatively, through onli...
  </details>

- **2026-08-03** — Can Wang, Haoran Chen, Haowen Gao et al. — [From Simple QA to Deep Research: A Verifiable Benchmark Constructed through Iterative Task Evolution](http://arxiv.org/abs/2608.02163v1)
  <details><summary>📄 Abstract</summary>
  Deep research benchmarks require expert-level tasks and reliable evaluation grounded in task-specific knowledge. Existing benchmarks rely heavily on expert authoring or pre-existing human-authored materials, while fully automatic construction struggles to ensure consistent and traceable verification. To address this gap, we introduce a verifiable benchmark of 500 deep research tasks spanning 31 topics and 10 major categories, with three query forms designed to probe complementary capabilities re...
  </details>

- **2026-08-03** — Long Qian, Jiaqi Wei, Bingke Zhu et al. — [Messages, Not Tokens: Grounded Coresets for Faithful VLM Compression](http://arxiv.org/abs/2608.02134v1)
  <details><summary>📄 Abstract</summary>
  Modern vision language models (VLMs) turn high-resolution images into long sequences of visual tokens. Every token traverses the language decoder and persists in its prompt KV cache, inflating inference cost and motivating aggressive visual compression. Existing score-based methods assign each token an independent importance score and retain the Top-K. However, text queries consume collective, signed attention messages from the visual population, not isolated patches. Consequently, equally sized...
  </details>

- **2026-08-03** — Shuxiao Xie, Shuyang Xie, Yuan Cao et al. — [One QK Channel, Many Sources: Guarding Low-Precision Attention Collapse](http://arxiv.org/abs/2608.02091v1)
  <details><summary>📄 Abstract</summary>
  A bfloat16 transformer can train normally for many steps and then collapse abruptly. Distinct low-precision errors can trigger the same failure, leaving unclear whether each source needs its own repair or one shared route can be blocked. We isolate a reproduced GPT-2-class collapse to the streaming-softmax accumulator, where fp32 accumulation repairs it, and use the fault as an assay for moving controlled errors across sources. Errors placed outside attention still drive the same query-key (QK) ...
  </details>

- **2026-08-03** — Zitong Xu, Huiyu Duan, Xinyun Zhang et al. — [MIEScore: Human-Aligned Evaluation for Multi-Source Image Editing](http://arxiv.org/abs/2608.02059v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in unified multimodal models have significantly improved text-guided image editing abilities. In particular, models such as Nano-Banana-Pro and GPT-Image-2 demonstrate emerging capabilities in multi-source image editing (MIE), including tasks such as object synthesis, person-background composition, and cross-image style fusion. However, existing benchmarks and image editing assessment (IEQA) methods remain primarily focused on single-image editing tasks and largely overlook the m...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 562 |
| prompt-injection | 473 |
| memory-poisoning | 43 |
| tool-use-attack | 96 |
| backdoor | 407 |
| adversarial-attack | 548 |
| privacy-leakage | 3765 |
| steganography | 55 |
| misuse | 853 |
| red-teaming | 112 |
| vulnerability | 2568 |
| defense | 2248 |
| alignment | 2082 |
| robustness | 2039 |
| watermark | 238 |
| unlearning | 85 |
| agent-safety | 52 |
| benchmark | 55 |
| survey | 266 |
| other | 5923 |

---

📚 **全部 22470 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

⚠️ **本次更新跳过：arXiv API 爬取失败，数据为上次缓存。下次 CI 将自动重试。**

*Generated by AgentGuard at 2026-08-07 03:06:03*