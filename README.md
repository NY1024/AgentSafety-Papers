<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-22663-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-08 12:36 ｜ **论文总数 / Total Papers**: 22663（近 30 天 / Recent 30 days: 2366）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 22663 篇论文（含摘要、分类筛选、搜索）/ View all 22663 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 566
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 476
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 43
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 100
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 408
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 549
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3776
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 55
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 858
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 112
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2587
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2273
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2109
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2061
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 243
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 86
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 55
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 268
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5986

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2366 篇，完整 22663 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2366 papers from the last 30 days (with date, authors & abstract). For the full list of 22663 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

- **2026-08-06** — Abdulkadir Külçe, Alihan Esen, Cağla Fikir et al. — [ECHO: A Locally-Deployable Agentic Health Assistant with Temporal Memory, Safety Guardrails, and Speech Assessment](http://arxiv.org/abs/2608.06110v1)
  <details><summary>📄 Abstract</summary>
  This paper presents ECHO (Enhanced Care \& Health Observer), a locally-deployable conversational health assistant for long-term chronic care management. ECHO integrates three complementary software modules developed under shared supervision as a unified system. The core module is an agentic chatbot built on a ReAct loop orchestrated via LangGraph, equipped with 17 clinical tools and a temporal knowledge graph for persistent cross-session memory; it achieves a 94.9\% tool-execution pass rate acro...
  </details>

- **2026-08-06** — Glen Messenger — [Detecting Safety Training Modification in Language Models via Activation Analysis](http://arxiv.org/abs/2608.05578v1)
  <details><summary>📄 Abstract</summary>
  We introduce AMS (Activation-based Model Scanner), a tool that detects modifications to safety training in language models by measuring the geometric structure of safety-relevant concepts in activation space. Safety training creates measurable separation between harmful and benign content classes; certain safety modifications collapse or rotate this structure, while others leave it intact. We validate AMS across 14 model configurations spanning 4 architecture families (Llama, Gemma, Qwen, Mistra...
  </details>

- **2026-08-05** — Alina Klerings, Jannik Brinkmann, Heiner Stuckenschmidt et al. — [Mood Matters: How Syntactic Sensitivity Undermines Safety Alignment](http://arxiv.org/abs/2608.05409v1)
  <details><summary>📄 Abstract</summary>
  Large language models typically undergo post-training to align them with safety policies but there exist many sophisticated jailbreaks that sidestep established safeguards. For instance, prior work by Andriushchenko et al. (2025) has found that changing the grammatical tense from present to past can be enough to elicit harmful responses. In this work, we uncover a more general failure of non-imperative syntactic forms. We demonstrate that this syntactic vulnerability exists in 16 models up to 70...
  </details>

- **2026-08-05** — Rui Yang, Michael Fu, Kla Tantithamthavorn et al. — [Towards a Risk Assessment of Malicious Skill Files in Coding Agents](http://arxiv.org/abs/2608.05223v1)
  <details><summary>📄 Abstract</summary>
  Autonomous coding agents are increasingly embedded in enterprise software workflows with delegated authority over connected systems. Central to this architecture is the agent skills interface: folders of instructions and scripts that agents load dynamically to specialize their behavior. This interface also widens the attack surface, letting malicious shell commands hide within natural-language skill files. We make three contributions. First, an adversarial skill-synthesis method using six LLMs a...
  </details>

- **2026-08-04** — Hujian Zhu, Yihao Huang, Felix Juefei-Xu et al. — [ICO: Enhancing Semantic-Shift Jailbreaks via Iterative Context Optimization](http://arxiv.org/abs/2608.03210v1)
  <details><summary>📄 Abstract</summary>
  Foundation models have achieved remarkable success across diverse tasks, but they remain vulnerable. To investigate such vulnerabilities, semantic-shift jailbreaks have recently emerged as a promising attack paradigm. They bypass explicit safety mechanisms by replacing harmful terms in original harmful questions with benign alternatives and leveraging contextual information to induce the target model to reinterpret these alternatives as their corresponding harmful concepts. However, existing sem...
  </details>

- **2026-08-04** — Jasper Timm, Lukas Struppek, Ziwei Xu et al. — [AI Security Leaderboard: Methodology, Results and Minimal Standard](http://arxiv.org/abs/2608.03070v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI model developers increasingly rely on layered safeguards to prevent catastrophic misuse, but little public evidence exists on how much protection these safeguards provide, or how consistently across developers. We introduce the FAR.AI Minimal Standard for Safeguards, Version 1.0: a taxonomy of 67 readily accessible static jailbreak techniques, a method for composing them into a very large attack space, and a benchmark of flagship models against a sample of it. We evaluate Claude Fabl...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 9 papers

- **2026-08-06** — S. M . Bhagya P. Samarakoon, M. A. Viraj J. Muthugala, W. K. R. Sachinthana et al. — [Hijacking Robots with a Piece of Paper: A Systematic Study of Physical Prompt Injection in VLM-Controlled Robots](http://arxiv.org/abs/2608.05715v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are increasingly deployed as planners in robotic systems, where they translate natural-language commands into executable actions grounded in visual scene understanding. This tight coupling between perception and instruction-following introduces a new attack surface: adversarial text placed within the robot's visual field can act as an indirect prompt injection into the VLM's reasoning stack. We present a systematic study of physical prompt injection attacks against ...
  </details>

- **2026-08-06** — He Zhang, Feilong Li, Dingning Long et al. — [PromptShield Home: Ambient Multimodal Prompt Injection Defense for Smart-Home Agents](http://arxiv.org/abs/2608.05495v1)
  <details><summary>📄 Abstract</summary>
  Smart-home assistants increasingly use multimodal large language models (MLLMs) that perceive video and audio directly. This raises a safety question specific to the home: can the agent tell a genuine user command from ambient or externally-sourced content, television speech, on-screen text, or an overheard conversation, that merely looks like a command? We introduce PromptShield-Home, a pilot benchmark of realistic smart-home scenarios spanning addressee ambiguity, screen/audio injection, healt...
  </details>

- **2026-08-05** — Buzhao Liu, Xinhang Ma, Yevgeniy Vorobeychik — [Robust Context-Aware Detection of Malicious Instructions in Text](http://arxiv.org/abs/2608.05430v1)
  <details><summary>📄 Abstract</summary>
  The remarkable instruction-following ability of modern LLMs has enabled their practical use as the minds of agents that can autonomously complete increasingly complex tasks. Therein, however, also lies their vulnerability to attacks which embed malicious instructions in text, common variants of which are known as indirect prompt injection (IPI). A fundamental task in addressing this vulnerability is successful segmentation of a given text into benign and malicious sentences (if any). While a num...
  </details>

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


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 2 papers

- **2026-08-04** — Jiaming Chen, Yisen Gao, Yanping Li et al. — [MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents](http://arxiv.org/abs/2608.03844v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented LLM agents rely on rich context for long-horizon reasoning and acting, yet their memory modules expose a persistent attack surface for malicious records, making the study of memory poisoning threats imperative. However, existing query-only attacks often fail to remain effective in two realistic and prevalent settings: large-scale benign memory pools and active input auditing. Consequently, current approaches fall short when facing the dual challenges of high retrieval competitiv...
  </details>

- **2026-08-04** — Zonghao Ying, Xiangfan Wu, Huiyu Wu et al. — [SkillJack: Persistent Skill Backdoors in Self-Evolving Agents](http://arxiv.org/abs/2608.03509v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents increasingly convert interaction histories into reusable skills that persist beyond individual tasks. While prior work studies memory and retrieval poisoning, such attacks only affect agents when poisoned records are retrieved as context. We uncover a new and more fundamental risk: poisoned experiences can be transformed by the agent itself into durable behavioral artifacts. We present \textbf{SkillJack}, the first attack that exploits the experience-to-skill pipeline of sel...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 5 papers

- **2026-08-06** — Yuru Feng, Yaoqi Chen, Beidi Zhao et al. — [SkillHEX: Improving Agent Skills via Hypothesis-Driven Autonomous Exploration and Exploitation](http://arxiv.org/abs/2608.05628v1)
  <details><summary>📄 Abstract</summary>
  Although agent skills equip LLMs with reusable procedural knowledge, manual maintenance suffers from high costs, unscalability, and misalignment. Real-world deployments thus require autonomous, on-demand skill evolution at test time, constrained by limited interaction budgets and a lack of training or validation sets. This setting introduces a severe sparse reward challenge, where outcomes conflate multiple latent failure causes. Under such ambiguity, existing methods that greedily refine a sing...
  </details>

- **2026-08-06** — Jialuo Chen, Lingqi Jiang, Xinhao Deng et al. — [When Experience Becomes Instruction: Trajectory Poisoning in Self-Evolving Agent Skill Systems](http://arxiv.org/abs/2608.05563v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving skill (SES) systems distill agent trajectories into persistent skills, allowing untrusted experience to become trusted instruction. We introduce PoisonedEvolution, a trajectory-poisoning attack on this promotion process. Our skill-visible black-box attacker can inspect a target skill and contribute bounded evidence, but cannot observe private pools or evolution logic or edit the skill bank. Artifact poisoning requires Inclusion, Evolution Attribution, and Realization. Attribution i...
  </details>

- **2026-08-06** — Xingyu Tan, Xiaoyang Wang, Qing Liu et al. — [SkillZip: Contract-Preserving Graph Compression for Scalable Agent Skill Libraries](http://arxiv.org/abs/2608.05604v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly act as agents whose procedural knowledge is stored in reusable skill packages and loaded at inference time. As skill libraries grow, a central challenge is to expose the smallest sufficient executable context under a limited context budget. Existing systems struggle to reuse routines below the whole-skill level, preserve procedural contracts during compression, keep compressed routines executable and expandable, and update the compressed library as skill...
  </details>

- **2026-08-05** — Jialuo Chen, Minghe Wang, Lingqi Jiang et al. — [SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse](http://arxiv.org/abs/2608.05204v1)
  <details><summary>📄 Abstract</summary>
  LLM-agent ecosystems are rapidly growing around reusable skills: mixed-modality packages of metadata, natural-language instructions, code, tools, references, and operational workflows. As skills become marketplace artifacts, auditing their reuse is no longer the same problem as ordinary code clone detection. Existing detectors target single-modality source code or whole-package similarity, yet skill reuse evidence is distributed across authored text, implementation fragments, and operational str...
  </details>

- **2026-08-04** — Nizhang Li, Zonghao Ying, Xiangfan Wu et al. — [SkillSentry: Adaptive Honey Worlds for Dynamic Safety Testing of Agent Skills](http://arxiv.org/abs/2608.03485v1)
  <details><summary>📄 Abstract</summary>
  External skills extend the capabilities of large language model agents, but also introduce an execution-time attack surface: a skill that appears benign under inspection may reveal harmful behavior only after particular environmental states, resources, or interaction histories are encountered. Existing scanners primarily rely on static analysis, predefined rules, or one-shot semantic judgments, making such conditional behavior difficult to elicit and attribute. We present SkillSentry, a dynamic ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 6 papers

- **2026-08-06** — Yuchen Chen, Wei Cheng, Yuan Xiao et al. — [Breaking Customized LLMs for Coding: Automated Red Teaming for Instruction Backdoor Attacks](http://arxiv.org/abs/2608.05659v1)
  <details><summary>📄 Abstract</summary>
  LLM customization platforms allow users to build task-specific models for code intelligence tasks by embedding instructions into system prompts, without modifying the underlying model parameters. While these platforms lower the barrier to developing customized LLMs, they also introduce a new attack surface: instruction backdoor attacks, in which adversaries implant hidden malicious behaviors into customized instructions. However, existing attacks suffer from two key limitations. First, they ofte...
  </details>

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


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 7 papers

- **2026-08-06** — Hao Wang, Yuxuan Zhang, Wei Yang — [Universal Concept Disruption for SAM3 Image Segmentation](http://arxiv.org/abs/2608.05983v1)
  <details><summary>📄 Abstract</summary>
  SAM3 extends promptable segmentation from geometry-driven mask prediction to open-vocabulary concept segmentation, where a text-conditioned grounding model decides whether a concept is present and segments all matching instances. While this presence-gated design improves concept-level prediction, its adversarial robustness remains unexplored. In this paper, we introduce Universal Concept Disruption (UCD), the first universal cross-concept adversarial attack tailored to SAM3 image segmentation. U...
  </details>

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


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 33 papers

- **2026-08-06** — Zirui Chen, Shi Tang, Zhengchao Gao et al. — [Algebraic Cryptanalytic Extraction on Hard-Label Neural Networks](http://arxiv.org/abs/2608.05736v1)
  <details><summary>📄 Abstract</summary>
  Although the state-of-the-art neural network model extraction attack in the hard-label setting by Carlini et al. at EUROCRYPT 2025 has polynomial-time complexity in theory, its dual-point clustering relies on singular value decomposition (SVD) with a time complexity of $\mathcal{O}(n^2 \cdot (d^{(k)})^3)$, resulting in huge runtime in practice. To address this computational bottleneck, this work transforms Carlini et al.'s geometric-view hard-label attack into an algebraic framework, and propose...
  </details>

- **2026-08-06** — Omid Bazgir, Md Nasir, Jacob Hoffman et al. — [Improving the Realism of Synthetic Clinical Benchmarks Under Utility Constraints](http://arxiv.org/abs/2608.06265v1)
  <details><summary>📄 Abstract</summary>
  Synthetic clinical benchmarks for enterprise AI agents can pass existing utility checks and still remain structurally unrealistic, especially in privacy-sensitive healthcare settings where operational data are hard to access. We study how to improve such benchmarks without breaking the downstream utility checks already used in practice.   We formulate benchmark revision as utility-constrained realism improvement: dataset changes should increase realism while staying above an operational utility ...
  </details>

- **2026-08-06** — Manideep Dhar, Ritwik Singh, Sharat Chandra Kumar Manikonda — [From Siloed Algorithms to Compliance-First Agentic Platforms: A Multi-Layered Architecture for Hospital AI Systems](http://arxiv.org/abs/2608.06112v1)
  <details><summary>📄 Abstract</summary>
  Hospitals are rapidly adopting artificial intelligence for triage, imaging, scheduling etc., yet most deployments remain isolated point solutions locked inside departmental silos, resulting in duplicated effort, hidden risks, and unrealized enterprise value. Despite explosive growth of AI in healthcare market and accelerating investment, an estimated 70-80% of healthcare AI pilots fail to scale, largely due to governance gaps, fragmented data, and missing integration blueprints. This research pr...
  </details>

- **2026-08-06** — Kai Li, Conggai Li, Sarah Ali Siddiqui et al. — [When Agentic AI Meets Integrated Sensing and Communication](http://arxiv.org/abs/2608.05792v1)
  <details><summary>📄 Abstract</summary>
  Agentic artificial intelligence (AI) is transforming Integrated Sensing and Communication (ISAC) from a function-oriented physical-layer technology into a goal-driven, closed-loop intelligent system, a paradigm we term AISAC. Existing work on learning-based sensing, resource allocation, reconfigurable intelligent surfaces (RIS), edge intelligence, multi-agent coordination, and resilient networking has developed largely in isolation. This survey unifies the literature within a six-stage closed-lo...
  </details>

- **2026-08-06** — Jiarui Yang, Jiale Zhange, Jiawei Li et al. — [LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models](http://arxiv.org/abs/2608.05706v1)
  <details><summary>📄 Abstract</summary>
  World models enable agents to perform forward rollout and planning without real-world interaction. However, their application in open-world embodied intelligence remains limited by the high cost of action annotations and the heterogeneity of action spaces across platforms. Recently, latent action models (LAMs) have alleviated this bottleneck by learning action representations directly from unlabeled human videos in a self-supervised manner. Nevertheless, most existing LAMs rely on single-view in...
  </details>

- **2026-08-06** — J. de Curtò, Dayani Plasencia, Diego Sánchez et al. — [Visual Grounding in Zero-Shot Vision-Language Control](http://arxiv.org/abs/2608.06154v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used as zero-shot controllers, but successful trajectories do not necessarily show that decisions are grounded in visual input: simulator dynamics and conservative action priors can produce favourable scores without meaningful perception. We investigate this with an input-ablation battery: blind-image controls, repeated identical inputs, lane-axis reflection, non-visual baselines, and pipeline-integrity checks. Across nine direct-action models, six ...
  </details>

- **2026-08-06** — Weikai Xu, Yunren Feng, Haoxiang Lei et al. — [AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents](http://arxiv.org/abs/2608.05891v1)
  <details><summary>📄 Abstract</summary>
  Mobile GUI agents can operate apps through pixel perception and touch actions, making them a promising interface for collecting and improving long-horizon mobile interaction policies. However, real trajectories are difficult to obtain for sensitive apps and privacy-critical operations. At the same time, existing simulated environments are costly to scale up, and GUI world models still suffer from unstable generation, limited modality coverage, and inconsistent action-transition logic. To address...
  </details>

- **2026-08-06** — Songpan Gao, Yajie Zhang, Guanxing Chen et al. — [STAIL: Semantic Text-Anchored Incremental Learning for Medical Imaging via Large Language Models](http://arxiv.org/abs/2608.05808v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models applied to medical image analysis suffer from severe catastrophic forgetting when continually adapting to new clinical tasks in dynamic environments. Mainstream incremental learning methods typically mitigate this by rehearsing raw historical images. However, this pixel-level rehearsal incurs significant storage overhead, raises privacy concerns, and fails to adequately capture the true data distribution with sparse exemplars. Inspired by human cognitive mechanisms, we propo...
  </details>

- **2026-08-05** — Jiahao Zhang, Yongzhi Tong, Zelin Fu et al. — [LUNAR: Benchmarking Personalized Large Language Models on UNiversal User BehAvioR Logs](http://arxiv.org/abs/2608.05246v1)
  <details><summary>📄 Abstract</summary>
  Existing personalized LLM benchmarks primarily rely on textual personas or isolated behavioral signals, providing limited evaluation of cross-domain behavioral personalization, where responses must be grounded in heterogeneous daily-life activities. To address this gap, we introduce LUNAR, the first benchmark for evaluating how LLMs personalize responses from longitudinal app interaction histories across universal daily-life domains, including clothing, food, housing, and mobility. To support sc...
  </details>

- **2026-08-05** — Harvey Mannering, Yilin Zhang, Ziao Liu et al. — [A Foundational EDM2-Based Generative Model for High-Resolution Synthetic Fetal Ultrasound Imaging from Open Datasets](http://arxiv.org/abs/2608.05471v1)
  <details><summary>📄 Abstract</summary>
  Prenatal ultrasound imaging is key for assessing fetal health, but AI progress is limited by scarce, privacy-restricted, and hard-to-annotate datasets. We propose a high-resolution fetal ultrasound synthesis framework based on the EDM2 diffusion architecture, trained on multiple public datasets to generate 512x512 images across six anatomical classes. Our method achieved improved image quality with lower FID scores and enhanced downstream fetal plane classification, reaching 93.36% ensemble accu...
  </details>

- **2026-08-05** — Xinyue Zhang, Jixiang Li, Bin Shao et al. — [Fine-Tuning Small Language Models for Reliable VASP INCAR Generation](http://arxiv.org/abs/2608.05387v1)
  <details><summary>📄 Abstract</summary>
  Language models can prepare VASP INCAR files from natural-language requests, but so far only large proprietary cloud models come close to handling the tightly coupled, physics-sensitive settings reliably, a dependence that fits poorly with local, high-throughput materials workflows where privacy, cost, and offline deployment matter. We show that a small language model (SLM) can close this gap. The SLM is fine-tuned on reference VASP calculations and paired with VASPGuard, a deterministic post-pr...
  </details>

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


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 9 papers

- **2026-08-06** — Hongrui Bao, Yubing Ren, Yanan Cao et al. — [Once a Response, Always a Response: Detecting LLM-generated Text via Latent Prompt Restoration](http://arxiv.org/abs/2608.05741v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate fluent and convincing text at scale, creating growing risks for misinformation dissemination, educational misuse, and platform governance. These concerns make robust detection of machine-generated text increasingly necessary. Recent zero-shot detectors mainly exploit probability-based statistical discrepancies, but they do not explicitly account for the training process of LLMs, which leaves a distinct generation mechanism insufficiently modeled and limi...
  </details>

- **2026-08-06** — Shenyi Zhang, Keyan Guo, Zihao Wang et al. — [MMAligner: Safeguarding Multimodal Large Language Models through Representation Calibration](http://arxiv.org/abs/2608.05909v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) often refuse unsafe text prompts yet generate harmful responses to semantically equivalent multimodal inputs. Existing defenses either rely on external guardrails, which add inference overhead without repairing intrinsic flaws, or safety fine-tuning, which treats alignment as black-box optimization and may sacrifice utility or require large multimodal datasets. To identify the cause of this safety disparity, we analyze MLLM representations geometrically. ...
  </details>

- **2026-08-06** — Bohan Jiang, Dawei Li, Yasin Silva et al. — [Measuring and Detecting Harmful AI Sycophancy](http://arxiv.org/abs/2608.05624v1)
  <details><summary>📄 Abstract</summary>
  Sycophantic responses are becoming pervasive in large language models (LLMs), and prior work has pointed out that some of them could be harmful. This paper focuses on one harmful sycophancy: preference-induced stance reversal sycophancy (PSRS), where a model reverses an initial stance merely to align with a user's stated preference. While existing research mainly measures how sycophantic a model is, we go further and ask whether PSRS can also be detected automatically from a single response. To ...
  </details>

- **2026-08-06** — Linfang Shang, Ming Xu, Yiding Sun et al. — [When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents](http://arxiv.org/abs/2608.05810v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents accumulate capability by distilling reusable skills from their execution trajectories, but we find this process is not monotonic: past a critical pool size, newly added skills degrade performance instead of improving it. We formalize this capability-contamination phase transition and trace it to a structural cause: once a defective skill enters the decision context, it becomes reference material for distilling later skills, forming cross-round contamination chains. We furthe...
  </details>

- **2026-08-05** — Divyansh Singh — [Evidence Lock Before Commitment: A Frozen Interface Degrades LLM-as-Judge Evaluation](http://arxiv.org/abs/2608.05353v1)
  <details><summary>📄 Abstract</summary>
  LLM judges are often asked to extract criteria and evidence before choosing between candidate answers. This workflow assumes that the intermediate record preserves the information needed for a later verdict. For reasoning-capable models, visible field order does not reveal internal decision order, so we test an observable alternative: persist the evidence in one call and make it the exclusive input to the next. Across 24,000 judgments over HelpSteer3, FeedbackQA, and CoVal, we compare standard p...
  </details>

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

- **2026-08-06** — Nima Hatami, Karim Faez, Saeed Sharifian et al. — [CFGPNet: Cross-Attention-Based Fused Gradient Programmed Network Framework for Multispectral Object Detection](http://arxiv.org/abs/2608.06205v1)
  <details><summary>📄 Abstract</summary>
  RGB--T object detection exploits the complementary strengths of visible and infrared imagery, supporting robust perception in low-light, adverse-weather, and complex multi-scale environments. However, existing methods still suffer from insufficient cross-modal interaction, unstable fusion from modality distribution gaps, and the high computational cost of heavy attention-based architectures. To address these issues, CFGPNet is proposed, a Cross-Attention-Based Fused Gradient Programmed Network f...
  </details>

- **2026-08-06** — Omar Coser, Antonio Orvieto, Paolo Soda et al. — [Is Self-Pretraining really useful to improve diagnosis in medical Time Series?](http://arxiv.org/abs/2608.06122v1)
  <details><summary>📄 Abstract</summary>
  Inspired by recent evidence that transformer architectures benefit from Self-PreTraining (SPT) on long-context benchmarks, we investigate whether similar gains extend to multimodal, multivariate, and even simple univariate medical time series. Our objective is to assess the impact of SPT on the performance and scalability of transformer-based models across diverse medical applications, particularly under limited data conditions. We evaluate transformer architectures on three representative medic...
  </details>

- **2026-08-06** — Wenhao Mao, Chengbin Hou, Weixiao Wang et al. — [Training-Free Token-Level Steering for LLM Personalized Co-Writing](http://arxiv.org/abs/2608.06069v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) show great promise for personalization, they often lack specialized domain knowledge. Conventional solutions like fine-tuning struggle with high computational costs and rapid data updates, while Retrieval-Augmented Generation fails to provide fine-grained, token-level steering. Furthermore, chat-based interfaces remain dominant, whereas productive co-writing paradigms have not yet been well exploited beyond the coding domain. To this end, we introduce SteerWrit...
  </details>

- **2026-08-06** — Trond Vatten, Yuming Jiang — [ASGE-RR: Agentic Service Graph Embedding with Revisable Reservations for Dynamic AI-Agent Calls](http://arxiv.org/abs/2608.06033v1)
  <details><summary>📄 Abstract</summary>
  AI-agent workflows often involve remote calls to models, memory stores, and tools distributed across a network. As execution progresses, these dependency calls collectively form an agentic service graph (ASG). Unlike traditional service requests, many dependency calls are revealed only at runtime. Consequently, allocating resources to a currently visible call may consume capacity later needed by a call from a higher-value workflow. We formulate this challenge as Agentic Service Graph Embedding (...
  </details>

- **2026-08-06** — Zhuowen Liu, Bohan Cui, YinShang Guo et al. — [HERALD: Counterfactual Audits and Minimal Repairs for Proof-of-Retrieval Rewards](http://arxiv.org/abs/2608.06012v1)
  <details><summary>📄 Abstract</summary>
  Search-agent rewards mix answer quality, citation grounding, tool cost, and anti-hacking terms; a high score therefore need not imply that cited evidence was retrieved, and added penalties can cancel. We introduce HERALD, an offline audit that applies exact same-question interventions, separates candidate-visible from oracle information, and enumerates detector contracts before policy optimization. On four Qwen3-8B pools from HotpotQA, 2WikiMultiHopQA, and MuSiQue, $R_0$ rejects search deletion ...
  </details>

- **2026-08-06** — Majed Jaber, Abdul Qadir Khan, Ankush Meshram et al. — [Tool Demo: Topology analysis with GPML for detection of cyberattacks in Water Distribution Networks](http://arxiv.org/abs/2608.05902v1)
  <details><summary>📄 Abstract</summary>
  Water distribution networks depends on industrial control systems to integrate the physical process with communication network, making them vulnerable to cyberattacks that alter the traffic pattern and network behavior. Traditional detection approaches that rely on raw traffic or protocol information often oversee structural changes that are induced by such attacks. In this work, we presents a topology-driven approach for detection of cyberattacks in water distribution networks based on Graph Pr...
  </details>

- **2026-08-06** — Shayell Aharon Salomon Amir Shaked Matan Noga — [The Vulnerability With No CVE: Managing Persistent Gaps Between Mandate and Authority in AI Coding Agents](http://arxiv.org/abs/2608.05884v1)
  <details><summary>📄 Abstract</summary>
  Existing guidance identifies excessive agency, excessive permission, weak task-bound authorization, and inadequate agent controls as important risks. Control frameworks also describe capabilities for constraining, authorizing, observing, validating, and responding to agent activity. Yet security programs still need a way to manage persistent deployed instances that span components and outlive any one event.   We propose the agentic posture vulnerability (APV) as a task-conditioned vulnerability-...
  </details>

- **2026-08-06** — Dong Wang, Qiaoyu Han, Lin Yang et al. — [Agent-Based Test Assertion Generation via Diverse Perspective Aggregation](http://arxiv.org/abs/2608.05822v1)
  <details><summary>📄 Abstract</summary>
  Test assertions are critical elements of unit tests, serving as checkpoints to validate expected behavior and ensure software correctness. Numerous techniques have been proposed to automate assertion generation, with recent progress notably driven by large language models (LLMs). Despite the promise, existing approaches such as ChatAssert suffer from modest accuracy, heavy reliance on oversampling, and vulnerability to model randomness due to one-shot prompting. To address these limitations, we ...
  </details>

- **2026-08-06** — Mustafa Alfarhan, Matteo Ravasi, Fuqiang Chen et al. — [Foundation Model-Assisted Full Waveform Inversion](http://arxiv.org/abs/2608.05763v1)
  <details><summary>📄 Abstract</summary>
  Full waveform inversion (FWI) can recover high-resolution subsurface velocity models. Conventional waveform-difference objectives, however, are vulnerable to cycle skipping when the starting model is inaccurate. We introduce an FWI objective that compares features produced from modeled and observed seismic traces by SeisLM, a pretrained seismic foundation model. The SeisLM encoder remains frozen during inversion, and the feature discrepancy is differentiated with respect to the modeled traces to...
  </details>

- **2026-08-06** — Victor Gialis, Maxime Metz, David Esteve et al. — [Spectral Aliasing Pretext: A novel task for Self-Supervised fault diagnosis in rotating machinery](http://arxiv.org/abs/2608.05705v1)
  <details><summary>📄 Abstract</summary>
  Deep learning is a new way for machinery fault diagnosis but requires extensive labeled data, a scarce resource in industrial settings. We propose Spectral Aliasing Pretext (SAP), a self-supervised learning method that pretrains models on unlabeled vibration data by exploiting spectral aliasing. We deliberately undersample signals to create folded spectrum, then train a Transformer to reconstruct the original unfolded spectrum. This pretext task forces the model to learn frequency-domain invaria...
  </details>

- **2026-08-06** — Changshuo Liu, Yanzheng Jin, Shangfeng Cai et al. — [F$^2$Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading](http://arxiv.org/abs/2608.05668v1)
  <details><summary>📄 Abstract</summary>
  With increasingly diverse and heterogeneous information sources, effectively leveraging multimodal data is becoming pivotal for high-quality financial trading. Although recent advancements in Large Language Model (LLM)-based agents have enabled the ingestion of multimodal inputs, existing methods fail to capture nuanced cross-modal dependencies and remain vulnerable to market noise, due to limited multimodal modeling, ineffective fusion mechanisms, and inadequate robustness. To address these cha...
  </details>

- **2026-08-06** — Yu Gu, Zhi Zheng, Yunpeng Ba et al. — [Hyper-ES: Effective Evolution Strategies for LLM Reasoning via Descent Direction Merging](http://arxiv.org/abs/2608.05541v1)
  <details><summary>📄 Abstract</summary>
  Evolution Strategy (ES) is a promising alternative to gradient-based fine-tuning for resource-constrained Large Language Model (LLM) reasoning. However, directly applying ES to billion-parameter LLMs is highly ineffective. In such high-dimensional parameter spaces, most random perturbations are nearly orthogonal to useful update directions, leading to unstable optimization. We propose Hyper-ES, a subspace-based ES framework that avoids the weakness of ES in full-parameter search while exploiting...
  </details>

- **2026-08-05** — Marina Litvak, Ariel Perstin, Ilan Shtilman et al. — [Example-Guided Prompting for Document-Level Text Simplification](http://arxiv.org/abs/2608.05447v1)
  <details><summary>📄 Abstract</summary>
  Document-level text simplification requires large language models (LLMs) to rewrite complex documents while preserving meaning, readability, and discourse coherence. Although prompt-based LLMs have shown promising performance, they often produce inconsistent simplifications because textual instructions alone provide limited guidance for complex document-level transformations. We investigate whether retrieved document-simplification examples can improve document-level generation by augmenting pro...
  </details>

- **2026-08-05** — Xi Xiao, Xingjian Li, Cheng Han et al. — [Adapting Vision Foundation Models with Cascaded Semantics](http://arxiv.org/abs/2608.05393v1)
  <details><summary>📄 Abstract</summary>
  Prompt tuning, a leading parameter-efficient adaptation paradigm in NLP, has recently been extended to computer vision. Visual prompt tuning (VPT) adapts pre-trained vision transformers (ViTs) by updating a small set of additional prompt parameters. However, existing visual prompts are randomly initialized and do not exploit prior knowledge, such as instructions in NLP. We address this gap by injecting two complementary semantic priors into VPT. Fundamental image priors, including color, texture...
  </details>

- **2026-08-05** — Sangwoo Ha, Hyunwoo Seo, Yurim Jo et al. — [EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding](http://arxiv.org/abs/2608.05303v1)
  <details><summary>📄 Abstract</summary>
  On-device deployment of Large Language Models (LLMs) has become essential for personalized edge applications. A primary bottleneck is external memory access (EMA) in feed-forward network (FFN) layers. Speculative decoding and mixture-of-experts (MoE) are promising solutions. Speculative decoding reduces the number of decoding stages by generating multiple tokens per stage, and MoE minimizes per-stage cost through sparse expert activation. However, there is an incompatibility when combining these...
  </details>

- **2026-08-05** — Nick Oh, Fernand Gobet — [Small Foundation Models of Human Cognition and Behaviour](http://arxiv.org/abs/2608.05224v1)
  <details><summary>📄 Abstract</summary>
  Large language models fine-tuned on human behavioural data have emerged as general-purpose cognitive proxies, but the scale this requires, and whether these models process task structure or exploit statistical shortcuts, remain open questions. We train fourteen models from 135M to 14B parameters across four architecture families on Psych-101, a dataset of 10.7 million trial-level choices from 160 experiments. In-distribution, scale barely matters. The models fall within a narrow band, as though ...
  </details>

- **2026-08-05** — Anadi Goyal, Nandish Chattopadhyay, Anupam Chattopadhyay et al. — [A Survey of Adversarial Efficiency Degradation for Vision Transformer by Exploiting Input-adaptive Optimization](http://arxiv.org/abs/2608.05217v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) increasingly rely on input-adaptive inference, such as token pruning and early halting, to meet energy and latency budgets. This survey examines a recent class of adversarial efficiency degradation attacks that target these mechanisms to increase computation without necessarily degrading accuracy. We unify and compare two representative attacks, SlowFormer (a universal adversarial patch) and DeSparsify (per-image perturbations), across three popular token-pruning frame...
  </details>

- **2026-08-05** — Siyuan Li, Peng Shu, Churan Yu et al. — [ASTELD: A Six-Axis Classification Framework for Autonomous AI Agents - Design, Evaluation, and an OpenClaw Case Study](http://arxiv.org/abs/2608.05201v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agent platforms differ substantially in architecture, security, tool integration, execution, autonomy, and deployment, yet the field lacks a common classification scheme for comparing these design choices. We propose ASTELD, an operational six-axis classification framework for autonomous AI agents: Architecture pattern, Security posture, Tool integration model, Execution paradigm, Level of autonomy and human control, and Deployment topology. ASTELD is constructed by synthesizing pr...
  </details>

- **2026-08-05** — Hongbo Ma, Bangji Yang, Yunqian Selina Cheng et al. — [Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving](http://arxiv.org/abs/2608.05254v1)
  <details><summary>📄 Abstract</summary>
  Large language models can derive a plausible mathematical object yet still violate explicit requirements--for example, by omitting a modular reduction, returning a non-integer, or using the wrong encoded answer form. We introduce Constraint-First Reasoning (CFR), a training-free two-stage prompting protocol: Stage 1 extracts and summarizes constraints entailed by the problem, and Stage 2 solves while checking intermediate and final results against that summary. Routed-CFR activates the two-stage...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 58 papers

- **2026-08-06** — Jiacheng Wei, Zhaoxin Fan, Xin Wen et al. — [ChainClaw: A Layered Agent Framework for Reliable On-Chain Execution](http://arxiv.org/abs/2608.05790v1)
  <details><summary>📄 Abstract</summary>
  General-purpose large language model agents have achieved strong performance on tool-augmented tasks, yet they rely on assumptions break down in blockchain environments. On-chain execution is stateful, adversarial, and economically irreversible, exposing three fundamental gaps: Reactivity, Irreversibility, and Observability. We propose ChainClaw, a blockchain-native agent framework built on OpenClaw, that addresses all three gaps through a layered architecture comprising an event-driven orchestr...
  </details>

- **2026-08-06** — Aurosweta Mahapatra, Xiutian Zhao, Shreeram Suresh Chandra et al. — [AffectDF: The Most Comprehensive Benchmark for Speech Deepfake Detection against Emotionally Expressive Attacks](http://arxiv.org/abs/2608.05507v1)
  <details><summary>📄 Abstract</summary>
  Speech deepfake detection (SDD) systems achieve strong performance on conventional benchmarks; however, existing datasets provide limited coverage of emotionally expressive and recent large audio-language model (LALM)-based attacks. Existing emotional spoofing datasets are also limited in scale and attack diversity, typically covering only voice conversion (VC) or text-to-speech (TTS) attacks. We introduce AffectDF, the most comprehensive benchmark for emotionally expressive speech deepfakes, sp...
  </details>

- **2026-08-06** — Massi-Nissa Abboud, Aladin Djuhera, Elena Cabrio et al. — [Poli-Bias: Understanding and Measuring Large Language Model Biases in International Political Conflicts](http://arxiv.org/abs/2608.06123v1)
  <details><summary>📄 Abstract</summary>
  Measuring political bias in large language models (LLMs) remains challenging as it can manifest through subtle differences in framing, argumentation, and legal reasoning that are difficult to capture with a single metric. In this work, we introduce Poli-Bias, a counterfactual framework for measuring whether LLMs treat legally equivalent conflict scenarios differently depending on the countries involved. Poli-Bias compares responses to paired prompts in which country identities are systematically...
  </details>

- **2026-08-06** — R. P. Erickson — [A quantum framework for event graphs](http://arxiv.org/abs/2608.06058v1)
  <details><summary>📄 Abstract</summary>
  Graph representations of discrete events provide a natural foundation for machine-learning models of anomaly detection, yet they also suggest a deeper quantum description in which graph structure gives rise to interacting quantum degrees of freedom. We develop a quantum framework based on a directed participant graph whose edges represent events connecting pairs of source and destination vertices. A line-graph transformation maps each event to a node of a bidirectional event graph, whose edges i...
  </details>

- **2026-08-06** — Jiale Han, Xiang Li, Jing Qian et al. — [From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models](http://arxiv.org/abs/2608.06020v1)
  <details><summary>📄 Abstract</summary>
  Economic World Models (EWMs) are generative economic models that simulate how economies evolve from within by modeling heterogeneous agents, their beliefs and actions, and the market and institutional mechanisms through which their interactions produce aggregate outcomes. This paper develops an implementation roadmap for building economic world models as generative engines in which heterogeneous agents act, interact, adapt, and co-evolve with markets and institutions, thereby producing economic ...
  </details>

- **2026-08-06** — Mohammad Abboush, Hamza Ouarrad, Andreas Rausch — [Sensor-Level Fault Diagnosis for Automotive Software Validation Using Large Language Models](http://arxiv.org/abs/2608.05921v1)
  <details><summary>📄 Abstract</summary>
  The pre-series validation of automotive software on hardware-in-the-loop (HIL) platforms produces large volumes of multivariate sensor recordings whose assessment against functional safety requirements exceeds what manual review can sustain at campaign scale. Threshold-based tooling reports that a deviation has occurred but neither identifies its nature nor locates its source, while data-driven classifiers, although accurate, rely on large labelled datasets and return opaque decisions that sit u...
  </details>

- **2026-08-06** — Wenhao Lin, Chenyu Yu, Xingwei Lin et al. — [DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model](http://arxiv.org/abs/2608.05695v1)
  <details><summary>📄 Abstract</summary>
  As large language model (LLM) agents increasingly invoke external tools and interact with real-world systems, unsafe actions may cause irreversible consequences on external states, user data, and downstream services. Recent runtime guardrails mitigate such risks by checking proposed actions before execution, but many remain reactive: they primarily assess the apparent safety of the current action, lacking an explicit model of how risk evolves across the trajectory. This limitation creates a crit...
  </details>

- **2026-08-06** — Yanqi Wu, Runhe Lai, Xinhua Lu et al. — [TruthLens: Object Hallucination Detection via Self-Evaluating Truthfulness Scores in LVLMs](http://arxiv.org/abs/2608.05616v1)
  <details><summary>📄 Abstract</summary>
  Despite the remarkable progress of large vision language models (LVLMs), object hallucination remains a fundamental challenge that hinders their trustworthy deployment. A key finding motivates our work: real and hallucinated object tokens are clearly separable in hidden representations, yet this separability is largely lost at the language-modeling (LM) head. We propose TruthLens, a self-evaluation framework that teaches the LM head to expose a per-object truthfulness signal without any auxiliar...
  </details>

- **2026-08-06** — Nikhil Sreekumar, Abhishek Chandra — [Viveka: Context-Aware Sensing for Energy Efficiency in Smart Wearables](http://arxiv.org/abs/2608.05572v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of multi-sensor Internet of Things (IoT) systems, from Body Sensor Networks (BSNs) to industrial monitoring, is increasingly constrained by strict energy budgets and limited on-device storage. Continuous high-fidelity sensing leads to rapid battery depletion and data gaps that compromise application reliability. Existing strategies address this through sensor selection or adaptive sampling in isolation, or rely on computationally expensive agents for joint optimization. They la...
  </details>

- **2026-08-06** — Liyan Huang, Kaicheng Wang, Weihang Wang — [Reasoning from Traces: Divergence-Guided Agentic Repair of WebAssembly Discrepancies](http://arxiv.org/abs/2608.05521v1)
  <details><summary>📄 Abstract</summary>
  WebAssembly (Wasm) promises seamless reuse of C/C++ codebases as portable, fast, sandboxed binaries. In practice, however, this promise often falls short: recent studies show that cross-compiling the same C/C++ source to Wasm and native binaries frequently leads to runtime discrepancies, owing to library implementation differences or compiler bugs. Since the root causes lie in the platform-level runtime and are hidden beneath the source code, even state-of-the-art LLM-based repair agents often f...
  </details>

- **2026-08-06** — Aarohi Srivastava, David Chiang — [Different Perturbations, Different Mechanisms: Understanding Continued Pre-training for Zero-Shot Dialect Robustness](http://arxiv.org/abs/2608.05510v1)
  <details><summary>📄 Abstract</summary>
  Dialectal variation remains a major challenge for multilingual language models. Perturbation-based continued pre-training (CPT) has emerged as a promising approach to improving robustness, yet existing work largely evaluates individual perturbation strategies in isolation and provides limited insight into why they work. We present a systematic study of perturbation-based CPT for multilingual dialect robustness in LLMs, comparing six training conditions across nine German, Italian, and Arabic dia...
  </details>

- **2026-08-06** — Yunjia Qi, Zehua Yin, Xintong Shi et al. — [TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories](http://arxiv.org/abs/2608.06346v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agentic systems have shown remarkable capabilities in complex domains, while suffering from cascading errors and difficulty in debugging. Critical error detection aims to locate the earliest error step in a failed trajectory that is responsible for the final failure. However, progress faces two main challenges. First, long trajectories make it difficult to identify individual errors, since the evidence for judging a step may be scattered across distant instructions, observations, and p...
  </details>

- **2026-08-06** — Jonas Gann, Michael Gertz — [NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering](http://arxiv.org/abs/2608.06292v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely opaque: intermediate reasoning steps are difficult to verify and cannot be reliably attributed to specific evidence. Moreover, missing user-specific context is rarely detected systematically, often leading to incomplete or incorrect output.   We propose NeSy-RAG, a modular neuro-symbolic RAG framework...
  </details>

- **2026-08-06** — Dae-Jin Lee — [Learning Latent Memory States from Longitudinal Athlete Monitoring Data](http://arxiv.org/abs/2608.06290v1)
  <details><summary>📄 Abstract</summary>
  We propose a new unit of analysis for longitudinal data: the Latent Memory Table. The scientific contribution is not the encoder. It is that table, treated as a reusable statistical object on the same footing as a matrix of principal-component scores, a table of estimated random effects, or a table of predicted probabilities. We estimate a statistical table that summarizes recent longitudinal history and is intended to be stored, queried, analysed and reused throughout the statistical workflow. ...
  </details>

- **2026-08-06** — Fatemeh Behrad, Tinne Tuytelaars, Johan Wagemans — [Learning visual representations for compositional analysis of artworks and photographs](http://arxiv.org/abs/2608.06142v1)
  <details><summary>📄 Abstract</summary>
  Composition, the deliberate arrangement of visual elements, is central to how meaning, emotion, and aesthetic quality are conveyed in artwork, yet it remains among the least formalized dimensions of visual understanding. Prior work highlights a persistent gap in learning meaningful compositional representations, attributing it to semantic bias and suggesting that human-inspired approaches may be key. We compare two parallel paradigms for composition analysis: a human-inspired method grounded in ...
  </details>

- **2026-08-06** — Yufei Li, Yicheng Ruan, Long Tian et al. — [ConceptADapt: Concept-guided Adaptive Feature Reconstruction with Dynamic Attention for Few-Shot Industrial Anomaly Detection](http://arxiv.org/abs/2608.05743v1)
  <details><summary>📄 Abstract</summary>
  Few-shot industrial anomaly detection (FS-IAD) focuses on detecting and localizing visual defects in industrial inspection during the cold-start phase, where only a limited number of normal training samples are available per category. Recent advances in this field predominantly leverage visual features from foundation-model and have achieved promising performance. Despite the strong representational power of foundation-model features, the model generalization remains fragile due to the extreme s...
  </details>

- **2026-08-06** — Ahmed Hassoon, Mark Dredze — [Innovation-Residual Auditing of Autonomous Analysis Agents: Localization, Detection Limits, Error Control, and Identifiability](http://arxiv.org/abs/2608.05490v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents now carry out entire data analyses, selecting cohorts, joining tables, and fitting models with little step-by-step supervision. When such an analysis turns out to be wrong, someone must determine which operation caused it. A recent approach does this without any labelled mistakes, learning instead from analyses known to be sound and flagging operations that depart from what that model predicts; how reliable such audits are has not been studied. This paper supplies that analysis...
  </details>

- **2026-08-05** — Yidian Chen, Yingzi Gu, Natan Vidra et al. — [OrchestraBench: Evaluating Multi-Agent Orchestration Failure Modes, Recovery, and Decomposition Quality](http://arxiv.org/abs/2608.05263v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent orchestration frameworks are moving from demos to production, yet benchmarks typically report task accuracy without diagnosing why a pipeline failed, where a cascade began, or which routing decision caused the breakdown. OrchestraBench evaluates failure, recovery, and decomposition through a controlled, seed-reproducible failure-injection harness over templated enterprise workflows. It introduces cascade radius and per-failure-mode recovery as primary metrics and compares routing pol...
  </details>

- **2026-08-05** — Zhongzhi Li, Yucheng Shi, Zongxia Li et al. — [Recursive Synthesis for Long-Horizon Terminal Tasks](http://arxiv.org/abs/2608.05466v1)
  <details><summary>📄 Abstract</summary>
  High-quality long-horizon training data for terminal agents is expensive to produce, often costing hundreds to thousands of dollars per task, because each task must keep the instruction, environment, reference solution, and verifier mutually consistent. Human authoring does not scale, and direct generation with large language models (LLMs) often breaks these dependencies. We present Recursive Synthetic Terminal Tasks (RST), a recursive verified synthesis framework for constructing long-horizon t...
  </details>

- **2026-08-05** — I. de Medeiros Varzielas, A. Kunčinas — [GOOFy-compatible 3HDMs and beyond](http://arxiv.org/abs/2608.05304v1)
  <details><summary>📄 Abstract</summary>
  Beyond conventional Higgs-family and general CP transformations, one may also consider a broader class of non-standard "GOOFy" transformations, in which the scalar fields and their conjugates are assigned related but inequivalent transformations. Although these transformations are not symmetries of a full Lagrangian in the conventional sense, some nevertheless stabilise the scalar potential. Their impact on the quadratic sector has not yet been systematically classified. We develop a sign-orbit ...
  </details>

- **2026-08-05** — Jin Liu, Steffen Thoma, Achim Rettinger — [TriQua: Reconciling Granularity and Context in Factuality Evaluation](http://arxiv.org/abs/2608.05228v1)
  <details><summary>📄 Abstract</summary>
  The "decompose-then-verify" paradigm for LLM factuality evaluation faces a fundamental trade-off: atomic facts, i.e., one sentence conveying one unit of information, often omit essential context, while broader statements lack the granularity needed for precise assessment. To address this, we introduce TriQua, a framework that flexibly models facts based on their complexity. Simple claims are extracted as standard triples, while complex claims are represented as hyperrelational facts by attaching...
  </details>

- **2026-08-05** — Maximilian Posner, Martin Dazer, Daniela Lauer et al. — [A System for Train Condition Monitoring and Structural Health Assessment of Rail Vehicles](http://arxiv.org/abs/2608.05221v1)
  <details><summary>📄 Abstract</summary>
  The ongoing digitalization of rail systems and the increasing use of artificial intelligence (AI) are fundamentally transforming the design, operation, and maintenance of rail vehicles. While fully automated operation at Grade of Automation 4 (GoA4) is well established in metro systems, its deployment in mainline rail remains limited. This is primarily due to stringent safety requirements and the complexity of open operational environments. Current perception systems based on cameras, radar, and...
  </details>

- **2026-08-05** — Ye Leng, Junjie Chu, Yiting Qu et al. — [Innocent Panels, Hateful Stories: Evaluating and Detecting Hateful Intent in Multi-Turn Visual Story Generation](http://arxiv.org/abs/2608.05210v1)
  <details><summary>📄 Abstract</summary>
  Picture books and comics have long been used to disseminate hateful narratives because they are easily understood even by children, as exemplified by the notorious Nazi propaganda picture book \emph{Der Giftpilz}. Recently, frontier text-to-image (T2I) systems such as Gemini and GPT-Image have enabled conversational generation with consistent characters and scenes across turns, making hateful visual stories, namely ordered image groups that collectively convey hateful narratives, cheap and scala...
  </details>

- **2026-08-05** — Yuta Kobayashi, Pradyun Ramesh, Muhammad Ahmed Chaudhry et al. — [Positive-Unlabeled Preference Optimization For Chest X-ray Report Generation](http://arxiv.org/abs/2608.05341v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) for radiology report generation are typically trained on retrospective clinical reports, which suffer from omission noise: clinically present findings are left unreported due to the omission of subtle findings. For example, prior studies show that cardiomegaly may be omitted from ICU chest X-ray reports when the imaging request is focused on monitoring support device placement. As a result, models trained with standard approaches inherit these omissions, learning to...
  </details>

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

- **2026-08-04** — Zhenpeng Li — [Post-Hoc Trajectory-Risk Certification for Modular LLM-Based Security Agents](http://arxiv.org/abs/2608.05199v1)
  <details><summary>📄 Abstract</summary>
  Autonomous security agents operate as staged pipelines, such as classifying network traffic and then attributing attacks to a specific technique. Split conformal prediction gives each stage finite-sample coverage, but deployment requires a trajectory-level guarantee across the full chain. These guarantees do not compose automatically when stages are independently trained and calibrated. Bonferroni allocation is distribution-free but conservative under correlated errors. We show that a natural pa...
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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 67 papers

- **2026-08-06** — Tao Wang, Qihao Yang, Rongjiao Liang et al. — [Benchmarking and Enhancing LLMs for Rule-Intensive Review of National Standard Documents](http://arxiv.org/abs/2608.06312v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly support complex professional tasks, yet their capabilities in rule-intensive document review remain insufficiently evaluated. National standard documents, such as China GB/T standards, offer a representative testbed: they are lengthy, highly structured, and governed by explicit rules for scope, terminology, normative wording, and cross-section consistency. Existing benchmarks focus on domain knowledge and question answering, largely overlooking intrinsic...
  </details>

- **2026-08-06** — Fardin Afdideh, Fernando Seoane, Farhad Abtahi — [A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications in AI Governance](http://arxiv.org/abs/2608.06246v1)
  <details><summary>📄 Abstract</summary>
  Post-training adaptation has become central to modern machine learning practice and includes techniques such as retraining, fine-tuning, parameter-efficient adaptation, alignment, retrieval augmentation, model editing, unlearning, calibration, and Multimodal Instruction Tuning. However, the literature remains fragmented across technique families, model classes, and deployment contexts, making it difficult to compare methods or describe how a trained model has been modified. This survey synthesiz...
  </details>

- **2026-08-06** — Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng et al. — [EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation](http://arxiv.org/abs/2608.06231v1)
  <details><summary>📄 Abstract</summary>
  Emotion shapes how viewers interpret a scene, yet existing video generators entangle global atmosphere, affect-bearing semantic cues, and temporal progression within a single text condition. We present EmoWorld, a framework that decouples these factors within a frozen flow-matching video diffusion transformer (Video DiT). A one-time preparation stage extracts layer-specific affect directions and a reusable cue library from geometry-preserving neutral and emotion-edited panoramas. At inference, V...
  </details>

- **2026-08-06** — Hoda Fakharzadehjahromy, Emil Wiman, Andreas Bueff et al. — [SAGA: Score-Weighted Adaptive Generation Alignment for Low-Resource Nordic Language Models](http://arxiv.org/abs/2608.06179v1)
  <details><summary>📄 Abstract</summary>
  Preference optimisation has proven effective for improving large language models but typically relies on costly human preference annotations. Extending these methods to morphologically rich, low-resource languages remains challenging because such annotations are scarce. We present SAGA (Score-weighted Adaptive Generation Alignment), a parser-guided preference optimisation framework that replaces human labels with dependency-parser supervision. SAGA converts parser judgements into preference pair...
  </details>

- **2026-08-06** — Giorgio Tonetti, Laurent Kneip, Abel Gawel et al. — [Prior-SG: Task and Prior Driven Region Segmentation for Scene Graphs in Arbitrarily-Structured Environments](http://arxiv.org/abs/2608.06170v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical 3D scene graphs are a promising representation for high-level spatial reasoning in autonomous mobile platforms. However, existing extraction frameworks typically rely on purely local visual clustering or strict geometric heuristics, such as wall-separated rooms, which fail in open-plan or arbitrarily-structured environments. We propose Prior-SG, a task- and prior-driven framework that casts scene graph generation fundamentally as a probabilistic alignment problem. As the robot explo...
  </details>

- **2026-08-06** — Xingyu Guo, Wei Chen, Linlin Yang et al. — [Contextual Information Policy Optimization for Search Agents](http://arxiv.org/abs/2608.06128v1)
  <details><summary>📄 Abstract</summary>
  Search agents extend large language models beyond static parametric memory by enabling them to acquire and use ex ternal evidence during multi-step reasoning. For knowledge intensive tasks involving complex or evolving information, their reliability depends not only on retrieving relevant ev idence but also on using it to guide subsequent reasoning. However, existing methods primarily reward final-answer cor rectness or intermediate progress, without directly assessing whether post-retrieval act...
  </details>

- **2026-08-06** — Pranav Dahiya — [Mind the Gaps: Mixture-of-Minds for Human Simulation](http://arxiv.org/abs/2608.06115v1)
  <details><summary>📄 Abstract</summary>
  Predicting how a population will answer a new question is a long-standing goal. Statistical methods succeed at the level of the mass but falter at the level of the individual. Large language model simulators inherit this gap. They recover a population's central tendencies while flattening its heterogeneity, and they carry social biases and prompt brittleness that distort individual predictions. This paper introduces Anacreon, an audience simulation model that targets the individual level within ...
  </details>

- **2026-08-06** — He Kong, Zengjue Chen, Qi Wang et al. — [Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation](http://arxiv.org/abs/2608.05999v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have demonstrated remarkable capabilities in robotic manipulation by leveraging pretrained vision-language models. However, existing post-training methods predominantly optimize VLA models as flat policies, making it difficult to explicitly model task progression and perform robust long-horizon manipulation. Although hierarchical approaches introduce task decomposition, they mainly rely on supervised learning from offline demonstrations and cannot effectively ...
  </details>

- **2026-08-06** — Taolin Zhang, Weizi shao, Zijie Zhou et al. — [M$^3$Prune: Hierarchical Collaborative Pruning for Efficient Multi-Modal Multi-Agent Retrieval-Augmented Generation](http://arxiv.org/abs/2608.05967v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multi-modal retrieval-augmented generation (mRAG), which augments multi-modal large language models (MLLMs) with external knowledge, have shown that collective intelligence from multiple agents can outperform a single model through effective communication. Despite their strong performance, existing multi-agent systems incur substantial token overhead and computational cost, posing challenges for large-scale deployment. To address these issues, we propose a Multi-Modal Multi-ag...
  </details>

- **2026-08-06** — Maulik Chevli, Johannes Brandt, Rickmer Braren et al. — [Big, Bright, or Invisible: A Frozen-Feature Benchmark of 3D CT Foundation Models](http://arxiv.org/abs/2608.05960v1)
  <details><summary>📄 Abstract</summary>
  Routine CT interpretation is inherently comprehensive, capturing incidental findings across the entire scan volume. 3D CT foundation models could assist this process by providing generalizable representations of anatomy and pathology. To evaluate their diagnostic breadth, we benchmark ten frozen CT encoders across three cohorts of thoracic CT scans, including an unseen internal clinical dataset, using $k$-nearest neighbors, zero-shot prompting, and linear probing. We find no universal state-of-t...
  </details>

- **2026-08-06** — Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian — [CourseGraph: Finding overlaps and differences in Computer Science courses across universities](http://arxiv.org/abs/2608.05910v1)
  <details><summary>📄 Abstract</summary>
  Student mobility programs such as Erasmus+ enable students to take courses at other universities, broadening their academic and cultural horizons. However, this flexibility also leads to a practical challenge: ensuring that students do not take courses elsewhere that substantially overlap with courses in their home curriculum. In this work, we propose CourseGraph, a methodology that automates the evaluation of external courses based on insights obtained from the process followed by curriculum ad...
  </details>

- **2026-08-06** — Yushe Cao, Shikun Feng, Fei Shen et al. — [UniVVT: A Unified End-to-End Framework for High-Fidelity Video Virtual Try-on](http://arxiv.org/abs/2608.05745v1)
  <details><summary>📄 Abstract</summary>
  Video Virtual Try-On (VVT) synthesizes a video of a person wearing a target garment while preserving identity, motion, and scene dynamics. Dominant approaches cast VVT as mask-conditioned video inpainting and rely on separate modules for human parsing, pose estimation, and garment warping. This multi-stage design complicates deployment and, more critically, allows errors in explicit geometric priors to propagate irreversibly into the generated video. We present UniVVT, a unified end-to-end frame...
  </details>

- **2026-08-06** — Mehrshad Saadatinia, Parsa Razmara, Ardalan Aryashad et al. — [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](http://arxiv.org/abs/2608.05732v1)
  <details><summary>📄 Abstract</summary>
  Controlling the behavior of large language models (LLMs) remains a critical challenge for AI alignment. Existing steering methods, such as Contrastive Activation Addition (CAA), typically rely on fixed single-layer interventions derived from aggregate activation differences. These methods impose a single intervention across semantically diverse inputs and often fail to sustain consistent behavioral changes across layers, limiting the effectiveness of the steering. In this work, we introduce Circ...
  </details>

- **2026-08-06** — Yuma Asato, Kiyoaki Shirai, Natthawut Kertkeidkachorn — [Mitigating Scoring Bias in LLM-as-a-Judge via Random Number Generation](http://arxiv.org/abs/2608.05726v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are often used as evaluators of text quality, known as LLM-as-a-Judge, which can outperform conventional automatic evaluation metrics that rely on reference texts. However, LLM evaluators tend to generate particular scores regardless of the context of the evaluated text, which is known as scoring bias. This study proposes a novel method to mitigate this scoring bias. An LLM is instructed to randomly generate number tokens, and the latent numerical bias of the LLM is ...
  </details>

- **2026-08-06** — Yifan Shen, Jian Xu, Boyi Li et al. — [ChronoVision: Temporal Reasoning via Latent State Reconstruction](http://arxiv.org/abs/2608.05631v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models excel at passive perception but struggle with complex visual cognitive tasks requiring multi-step temporal reasoning. This degradation largely stems from the inherent ambiguity of language-based reasoning, which often fails to accurately articulate continuous visual transformations. To address this, we propose ChronoVision, a multimodal framework designed to align visual logic with latent imagery. During supervised fine-tuning, a Reconstructive Visual Head predic...
  </details>

- **2026-08-06** — Keane Zhang, Varshini Chinta, Raj Sanjay Shah et al. — [Human-Like Anaphor Resolution in Large Language Models](http://arxiv.org/abs/2608.05630v1)
  <details><summary>📄 Abstract</summary>
  Anaphors are expressions that refer to other expressions, called antecedents. The process of connecting the two is called resolution. Cognitive science has identified multiple factors that affect the speed and success of anaphor resolution, including discourse structure, situation-model properties, and semantic factors. Here, we investigate whether these factors also affect anaphor resolution in five Large Language Models (LLMs) with open weights: GPT-2-XL, Llama-3.1-8B, Pythia-12B, Mistral-7B, ...
  </details>

- **2026-08-06** — He Jiang, Jingtian Yan, Yulun Zhang et al. — [Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations](http://arxiv.org/abs/2608.05588v1)
  <details><summary>📄 Abstract</summary>
  Lifelong Multi-Agent Path Finding (LMAPF) requires repeatedly planning collision-free paths for agents that continuously receive new goals upon reaching their current ones. While many learning-based planners have been proposed for LMAPF, most rely on oversimplified kinematic assumptions that may overlook motion constraints critical to real-world performance. In this work, we study a more realistic LMAPF model derived from many real-world automated warehouse systems, termed LMAPF-R2, which incorp...
  </details>

- **2026-08-06** — Mohammad Asadi, Soheil Hor, Bardiya Akhbari et al. — [Align-RAG: Alignment Is All You Need for TSFM In-Context Learning](http://arxiv.org/abs/2608.05571v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented forecasting promises to adapt frozen Time Series Foundation Models (TSFMs) to new domains without fine-tuning, but recent methods typically rely on learned fusion modules, i.e., trained adapters that merge retrieved examples into the backbone's forecast, based on the assumption that frozen backbones cannot dynamically incorporate retrieved context on their own. We show this assumption is unnecessary. We introduce Align-RAG, a training-free method that applies a closed-form pe...
  </details>

- **2026-08-06** — Kefan Li, Hongyue Yu, Yuan Yuan — [Escaping the Self-Repair Trap: Improving Test Oracle Generation via Dual-Context Awareness](http://arxiv.org/abs/2608.05917v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown strong potential for regression-oracle completion, where a test prefix is given and the current program version is treated as expected behavior. Recent approaches increasingly rely on iterative self-repair and execution feedback, but optimizing execution success does not necessarily yield strong fault-revealing oracles. This objective, widely adopted in repair-based methods, serves only as a proxy and may be misaligned with the true goal of oracle generati...
  </details>

- **2026-08-05** — Takuro Kawada, Shunsuke Kitada, Hitoshi Iyatomi — [GenGA: Editable and Data-Grounded Graphical Abstract Generation for Academic Papers](http://arxiv.org/abs/2608.05478v1)
  <details><summary>📄 Abstract</summary>
  Graphical Abstracts (GAs) visually summarize the key findings of academic papers, playing a crucial role in facilitating the understanding of research content. Recently, advancements in vision-language models and image generation models have enabled the automatic generation of scientific figures based on paper content. However, most conventional methods output the generated results as raster graphics, making post-editing (e.g., text modification and layout changes) highly difficult. This poses a...
  </details>

- **2026-08-05** — Benjamin Barlog, Hudson Craig, Zedong Peng — [Evaluating and Improving Pedagogical Fit in LLM-Based AI Tutors with the Pedagogical Suitability Index](http://arxiv.org/abs/2608.05411v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as AI tutors, but a correct answer is not always a pedagogically appropriate one. In classroom learning, effective help depends not only on correctness, but also on whether a response matches the learner's current foundation, the course sequence, and the timing of concept introduction. Existing evaluations focus mainly on answer quality, leaving this instructional fit under-measured. We present the Pedagogical Suitability Index (PSI), a composit...
  </details>

- **2026-08-05** — Shiwen Chu, Shanglin Li, Motoaki Kawanabe et al. — [Rectifying Geometric Misalignment: Online Source-Free Adaptation for Class-Imbalanced EEG](http://arxiv.org/abs/2608.05315v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) based Brain-Computer Interfaces (BCIs) often require unsupervised domain adaptation (UDA) to generalize across subjects and sessions. While Riemannian alignment methods like the Riemannian Centering Transformation (RCT) are effective for handling covariate shifts, they implicitly assume balanced class priors. However, in realistic online BCI scenarios, the label distributions vary dynamically (label shift), causing standard alignment techniques to geometrically misal...
  </details>

- **2026-08-05** — Junlin Han, Shengbang Tong, David Fan et al. — [Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality Synergy, Early Unification, and Recipes](http://arxiv.org/abs/2608.05000v2)
  <details><summary>📄 Abstract</summary>
  Vision offers a critical axis for advancing foundation models, driving a shift towards natively unified multimodal pretraining. Despite this momentum, the design space and the fundamental mechanisms of how modalities interact during unified training remain underexplored. We provide empirical clarity through a systematic exploration of multimodal pretraining. Our controlled experiments on both synthetic and large-scale real-world datasets yield four key insights into the physics of multimodal pre...
  </details>

- **2026-08-05** — Xinran Feng, Yi Xie, Chao Zhang et al. — [Decoupling Perception from Description: Computation-Grounded Representation Alignment between Multivariate Time Series and Language](http://arxiv.org/abs/2608.05238v1)
  <details><summary>📄 Abstract</summary>
  Training multimodal models to align time series with language runs into a self-supervision trap. The usual recipe asks an LLM to read a series and write a description, so label quality is capped by the perceptual skill the model is supposed to learn. The data can never teach more than the labeler already knows. A second gap makes this worse: most datasets use a single variable, but the patterns that matter (cross-channel correlation, lead-lag structure, co-occurring anomalies) appear only with s...
  </details>

- **2026-08-05** — Yexing Du, Kaiyuan Liu, Youcheng Pan et al. — [Breaking the Curse of Multilinguality in Many-to-Many Speech-to-Text Translation via a Resource-Aware Mixture of Speech Encoders](http://arxiv.org/abs/2608.04586v2)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have achieved significant success in speech-to-text translation (S2TT). However, when processing multilingual speech inputs, a single speech encoder shared across all languages suffers from the curse of multilinguality: languages at different resource levels compete for limited representation capacity, leading to strong high-resource performance but substantial degradation on low-resource speech. To address this problem and improve multilingual consistenc...
  </details>

- **2026-08-05** — Gautam Neelakantan Memana — [A Counterexample to Fourier Alignment in Single-Neuron Modular Addition](http://arxiv.org/abs/2608.04451v2)
  <details><summary>📄 Abstract</summary>
  We give a negative solution to MAIS-O60. We first construct an example in which an initially active ReLU neuron becomes completely inactive in finite time and thereafter remains frozen at a limit whose Fourier energy is equally distributed among all nonzero real frequency classes. The counterexample holds on an open set of initial conditions and therefore occurs with positive probability under Gaussian initialization. An appendix prepared by GPT-5.6 Sol strengthens the counterexample by showing ...
  </details>

- **2026-08-05** — Yuexi Yang, Alyssa Wu, Ji Luo et al. — [RepoProbe: Benchmarking Architecture-Aware Repository Comprehension with Checklists](http://arxiv.org/abs/2608.04783v2)
  <details><summary>📄 Abstract</summary>
  The integration of Large Language Models (LLMs) into software engineering has shifted the focus from function-level generation to repository-scale assistance. However, existing benchmarks largely rely on bug reports from GitHub Issues, which often allow models to bypass genuine understanding via pattern matching on error logs. This misalignment under-measures Edit Bias, which refers to premature generation, where models prematurely propose code modifications instead of understanding the existing...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 66 papers

- **2026-08-06** — Zhiheng Wang, Bo Peng, Lai Wei et al. — [The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images](http://arxiv.org/abs/2608.06270v1)
  <details><summary>📄 Abstract</summary>
  The "thinking-with-images" paradigm equips multimodal LLMs with active visual operations such as crop-and-zoom. However, models using these operations often achieve only marginal or negative gains over direct inference at substantially higher token cost. They may also repeatedly crop irrelevant regions and fail on questions that direct inference answers correctly. We ask whether the returned visual evidence causally affects the answer. To answer this question, we formulate visual tool-use as a c...
  </details>

- **2026-08-06** — Ro Encarnación, Tina Behzad, Emma Lurie et al. — [What Current AI Benchmarks Leave Unmeasured: Modality, Search, Citations, and Implications (for Safety Evaluations)](http://arxiv.org/abs/2608.06202v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) benchmark evaluations are routinely used to support claims about model safety, reliability, and deployment readiness. Yet most evaluations rely on a single access modality (model APIs), perform a single run per prompt, and report accuracy as the primary outcome metric, without accounting for conditions such as web search that may have effects on model behavior in deployment. We audit these assumptions for one of the most widely-used LLMs, comparing two modalities, Chat...
  </details>

- **2026-08-06** — Xiaoqing Wu, Xingyu Fan, Feifei Li et al. — [When History Lies: Evaluating and Improving Tool Use under Misleading Multi-Turn Histories](http://arxiv.org/abs/2608.06057v1)
  <details><summary>📄 Abstract</summary>
  Tool-calling agents infer task state from accumulated dialogue and tool traces. In persistent interactions, however, historical traces may remain structurally valid and semantically plausible after they cease to be authoritative for the current request. We show that such history can hijack a policy the model already possesses: on Qwen3-1.7B, pollution flips 32.1% of decisions that are correct under the original trajectory and frequently induces reuse of corrupted entities or interface convention...
  </details>

- **2026-08-06** — Alexander Apartsin, Yehudit Aperstein — [Clinical Communication Processing with Models Trained on LLM-Generated Synthetic Data: A Structured Survey and Novel Application Case Studies](http://arxiv.org/abs/2608.05993v1)
  <details><summary>📄 Abstract</summary>
  Much clinical value is conveyed not through structured records but through communication: exchanges in which patients describe symptoms, clinicians reason and give instructions, ambulances hand over to emergency departments, and nurses pass on a shift. Such language differs from tabular data because meaning depends on speaker role, intent, causality, uncertainty, omission, and channel noise. Healthcare natural language processing must therefore interpret information as conveyed rather than coded...
  </details>

- **2026-08-06** — Yongjie Qian, Ke Gao, Zhibin Zhang et al. — [RepoOMP: Repository-Aware Hotspot OpenMP Parallelization via Dependency-Aware Context Reduction](http://arxiv.org/abs/2608.05855v1)
  <details><summary>📄 Abstract</summary>
  OpenMP parallelization of hotspots in mature repositories remains difficult because loop safety and optimization payoff often depend on non-local evidence. Rule-based tools under-parallelize when legality is not locally provable, while agent-based approaches become unstable when retrieval misses decisive dependencies or includes irrelevant code. We present RepoOMP, a hybrid framework that recovers parallelization-relevant evidence before generation. RepoOMP builds a Multi-granularity Attributes ...
  </details>

- **2026-08-06** — Gihoon Kim, Jeyoung Lee, Suhan Woo et al. — [Cautious Context Steering for Language Model Personalization](http://arxiv.org/abs/2608.05813v1)
  <details><summary>📄 Abstract</summary>
  Personalizing language models (LMs) to individual user preferences is essential for aligning responses with diverse goals and backgrounds. Existing methods typically train a separate adapter for each user or learn a reward model whose scores depend on the user. Despite explicitly optimizing for each user, these methods must learn from limited observations and therefore suffer from data sparsity and poor generalization to unseen users and domains. In-context learning (ICL) and Context Steering (C...
  </details>

- **2026-08-06** — Chenghao Gu, Hanyang Yu, Jingbo Zhang et al. — [GeniWorld: A Generalizable Interactive World Model for Robotic Manipulation via Visual Actions](http://arxiv.org/abs/2608.06332v1)
  <details><summary>📄 Abstract</summary>
  Generalist robot policies exhibit strong capabilities, but their robustness in complex and unseen environments remains limited. Scaling robot learning and evaluation in diverse real-world environments remains costly and challenging. Action-conditioned world models offer a promising alternative, but they often suffer from limited action controllability and poor generalization to out-of-distribution (OOD) scenarios. To this end, we present GeniWorld, an interactive world model for robots that gene...
  </details>

- **2026-08-06** — Xian Sun, Wei Chow, Yingshuo Wang et al. — [Learning When to Trust via Selective Context Preference Optimization](http://arxiv.org/abs/2608.06377v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly condition their answers on external signals, and a single misleading one can turn a correct answer wrong. The obvious remedy, training models to resist such signals, hides a failure mode: a model that ignores all context looks robust yet is useless when the context is worth trusting. We recast the problem as selective trust and introduce MIST, a human-annotated benchmark that renders each reasoning item under four matched conditions (clean, misleading, correct-contex...
  </details>

- **2026-08-06** — Ishan Patel, Sahil Sen, Elias Lumer et al. — [The Bitter Lesson of Tool Calling](http://arxiv.org/abs/2608.06370v1)
  <details><summary>📄 Abstract</summary>
  Tool use transforms LLMs into agents that act beyond their training data, and for code-capable models, programmatic tool calling extends this further by replacing rigid JSON calls with scripts that chain and parallelize naturally. However, a systematic evaluation of tools as code on an established benchmark across current and prior model generations under real-world task conditions has not been conducted. In this work, we empirically compare programmatic tool calling (PTC) to native JSON tool ca...
  </details>

- **2026-08-06** — Lev V. Utkin, Stanislav K. Kogan, Andrei V. Konstantinov — [Surv-IPTB: An Attention-Based Model for Estimating Individual Probability of Treatment Benefit with Survival Data](http://arxiv.org/abs/2608.06288v1)
  <details><summary>📄 Abstract</summary>
  This work presents a novel attention-based framework for estimating the Individual Probability of Treatment Benefit (IPTB) in survival analysis contexts. The proposed model, called Surv-IPTB, directly quantifies the probability that a specific patient will experience extended survival time under treatment versus control. We reformulate IPTB estimation as a binary classification problem, leveraging pairwise patient comparisons across treatment and control cohorts. The framework incorporates a pri...
  </details>

- **2026-08-06** — Yuntai Song, Zejun Liu, Zhencheng Wang et al. — [Approximate Quantum Error Correction at Chiral Topological Edges](http://arxiv.org/abs/2608.06258v1)
  <details><summary>📄 Abstract</summary>
  Topologically ordered phases naturally realize quantum error correction through nonlocal encoding of quantum information. More recently, conformal field theories have been shown to realize approximate quantum error-correcting codes, but such constructions generally require fine tuning to criticality. Here we introduce a family of approximate quantum error-correcting codes realized by the chiral edges of two-dimensional topologically ordered phases. The proposed encoding combines the robustness o...
  </details>

- **2026-08-06** — Yixiong Xiao, Congxi Xiao, Jingbo Zhou — [TS-RAG: Retrieval Augmented Generation for Time Series Forecasting](http://arxiv.org/abs/2608.06223v1)
  <details><summary>📄 Abstract</summary>
  While deep learning models, particularly transformer-based architectures, have shown impressive performance in time series forecasting, the application of retrieval-augmented generation (RAG) in this domain remains limited. Since RAG has proven effective in enhancing the capabilities of large language models by incorporating relevant external information, retrieving similar time series sequences as references might also improve accuracy in time series forecasting tasks. However, most time series...
  </details>

- **2026-08-06** — Yitong Li, Xinjiao Li, Dirk Kutscher — [MARS: Multipath Adaptive Reliable Service](http://arxiv.org/abs/2608.06101v1)
  <details><summary>📄 Abstract</summary>
  Multipath transport is increasingly important for Internet/WAN services that move large data volumes across heterogeneous paths, including geo-distributed analytics, content distribution, and cloud-service pipelines. Existing solutions, however, face a practical trade-off: end-to-end transports such as MPTCP and MPQUIC are deployable but limited by endpoint-visible paths and delayed congestion feedback, while routing-or forwarder-assisted approaches often require infrastructure support or lack s...
  </details>

- **2026-08-06** — Taehyeon Kong, Woojin Kim, Jemin Hwangbo — [TRACE: Learned Proprioceptive Odometry for Legged Robots under Unreliable Contact Conditions](http://arxiv.org/abs/2608.05975v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we present TRACE (Tokenized Robust Attention for Contact-Aware Estimation), an end-to-end learned proprioceptive odometry estimator for legged robots under unreliable contact conditions. The proposed estimator directly predicts relative displacement, relative rotation, and body-frame velocity from a recent history of onboard inertial and joint measurements. To improve robustness under unreliable contact conditions, we introduce a foot-aware cross-attention module that adaptively w...
  </details>

- **2026-08-06** — Yang Liu, Suwan Sun, Yueguang Zhou et al. — [Harnessing thermo-optic dynamics for frequency-agile soliton microcombs](http://arxiv.org/abs/2608.05932v1)
  <details><summary>📄 Abstract</summary>
  Dissipative Kerr soliton microcombs enable compact and scalable frequency comb sources for precision metrology, spectroscopy, communications and coherent LiDAR, where broad and reliable frequency tuning is essential. Thermo-optic response can support thermal locking during soliton operation, enabling resonance tracking and thereby extending the tuning range, albeit modestly. However, it also induces pronounced thermal instability during soliton initiation, hindering reliable access to this exten...
  </details>

- **2026-08-06** — Théo Danielou, Antoine Saporta, Léo Alberge et al. — [Curia-MAE: Multi-Modal Multi-Anatomy MAE Pre-Training for 3D Medical Image Segmentation](http://arxiv.org/abs/2608.05844v1)
  <details><summary>📄 Abstract</summary>
  Radiology foundation models learn transferable representations that can be adapted to new tasks by training only small layers on top of a frozen encoder. Dense prediction tasks such as 3D segmentation are, however, underrepresented in their evaluation, and, with the encoder kept frozen, pre-trained models still fall short of nnU-Net, the state-of-the-art reference trained from scratch. To close this gap we extend convolutional MAE pre-training with a robust reconstruction objective, a feature re...
  </details>

- **2026-08-06** — Xinshuang Liu, Runfa Blark Li, Shaoxiu Wei et al. — [Unified Agent: Managing Interactions across Devices](http://arxiv.org/abs/2608.05729v1)
  <details><summary>📄 Abstract</summary>
  As capabilities rapidly increase, AI agents can move from running inside one app to acting across a user's devices over time. Yet existing agent systems still fall short in this scenario. This is because observations are scattered across devices and moments, but mainstream systems are not designed around this fact: a single agent that treats devices as tools lacks effective state management for all devices across time, and multi-agent systems coordinate across agents but do not maintain the comp...
  </details>

- **2026-08-06** — Rasul Khanbayov, Hasan Kurban — [Consistency Has a Computable Blind Spot: A Commutation Theory of Label-Free Reliability for Vision-Language Figure Reading](http://arxiv.org/abs/2608.05675v1)
  <details><summary>📄 Abstract</summary>
  Label-free reliability for vision-language models rests on invariance: perturb the input and a faithful reader's answer should not change. This has a known blind spot, a systematic misreading survives the perturbation and gets certified wrong, which we show is computable, not just real: an error is invisible to an edit exactly when the two commute, so the errors a suite cannot reach form its joint centralizer, a set that shrinks as edits are added and can be written down rather than guessed at. ...
  </details>

- **2026-08-05** — Zhuo Xie, Haoze Ni — [Cross-platform epistemic verification for improving factual reliability in AI-generated news summarization](http://arxiv.org/abs/2608.05302v1)
  <details><summary>📄 Abstract</summary>
  This study proposes Multi-source Evidence Consen- sus Verification (MECV), a post-hoc hallucination cor- rection framework for AI-generated news summariza- tion. Instead of depending on a single retrieval channel, MECV aggregates evidence from multiple heterogeneous sources, including the source document, Wikipedia, and open-web retrieval. The framework further incorporates a multi-LLM jury mechanism that estimates factual reliabil- ity through contradiction-aware consensus scoring across verifi...
  </details>

- **2026-08-05** — Swapnanil Mukherjee, Agyeya Negi, Tanuja Ganu et al. — [C$^3$PO: Evaluating Cross-Modal Composition and Counterfactual Performance in Omnimodal Models](http://arxiv.org/abs/2608.05381v1)
  <details><summary>📄 Abstract</summary>
  Current Multimodal Large Language Models (MLLMs) can process diverse sensory inputs, yet their reasoning remains heavily biased toward a dominant modality, resulting in brittle cross-modal reasoning. We introduce C$^3$PO, a benchmark of 3,404 samples spanning video, audio, image, and text, evaluating two abilities: information composition (fusing dispersed evidence) and counterfactual conflict (resolving deliberate contradictions). C$^3$PO's paired IC/CC structure and four-tier design enable tar...
  </details>

- **2026-08-05** — Fangxin Wang, Ziyi Zhang, Diyi Zhuang et al. — [When Do Corrective Features Help? An Agent for Corrective Feature Discovery on Black-Box Forecasters](http://arxiv.org/abs/2608.05207v1)
  <details><summary>📄 Abstract</summary>
  Frozen pretrained forecasters often fail in structured, recurring ways that are costly to repair through fine-tuning. We study corrective feature discovery: mining interpretable features of a frozen forecaster's residual to drive a lightweight post-hoc corrector. Prior automated feature engineering models the data-generating process; corrective features instead model the model-failure process. We present CRAFTER (Corrective Residual Agent with Feature-based Temporal Exploration and Reasoning), w...
  </details>

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

- **2026-08-04** — Chenfei Yan, Zeyang Yue, Feifei Zhao et al. — [When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2608.03421v2)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems promise effective collaborative reasoning, but communication may amplify local errors into collective risks. Existing evaluations emphasize final outcomes, leaving the reliability and propagation dynamics of distributed information aggregation unclear. We introduce Hi-Agreement, a controlled evaluation framework that strictly pairs all-honest collaboration with controlled deception by a key evidence holder and analyzes the aggregation process through multi-stage vot...
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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 8 papers

- **2026-08-06** — Nuzhat Khan, Indrakshi Dey — [Certifying Collective Reasoning in Multi-Agent Systems via Koopman Spectral Analysis](http://arxiv.org/abs/2608.05956v1)
  <details><summary>📄 Abstract</summary>
  Orchestrated collectives of large language model (LLM) agents that debate and vote are an emerging form of computational intelligence: the intelligent behaviour resides in the \emph{interaction}, not in any single agent. They improve task accuracy, yet remain black boxes at the system level: there is no principled test of convergence, no bound on the rounds needed, and no faithful account of what drove a decision. This paper develops a novel framework based on Koopman operator theory and validat...
  </details>

- **2026-08-06** — Soorya Ram Shimgekar, Michelle Hu, Dorisa Shehi et al. — [Tracing the Heart: An Evidence-Linked Pipeline for Heart-Failure Feature Engineering](http://arxiv.org/abs/2608.06366v1)
  <details><summary>📄 Abstract</summary>
  Electronic health record (EHR) feature engineering is a major bottleneck in clinical research and AI, accounting for 39-45% of data scientists' workload. This is especially pronounced in heart failure, which affects an estimated 6.7 million U.S. adults and requires integrating fragmented EHR data with disease-specific, guideline-based clinical reasoning. Existing rule-based and large language model (LLM)-based approaches offer only partial automation with limited maintainability and evidence tra...
  </details>

- **2026-08-06** — Yuanhong Jiang, Jingjie Zou, Zhenghong Lin et al. — [Evaluating Investment Logic in Large Language Models: A Real-World Benchmark Towards Personalzied Financial Agents](http://arxiv.org/abs/2608.06108v1)
  <details><summary>📄 Abstract</summary>
  Investment competence is inherently personalized: the same market evidence can justify different actions for investors with different goals, horizons, portfolios, and risk boundaries. Yet financial LLMs are evaluated either by static question answering or by terminal profit and loss. The former omits agency; the latter cannot reveal whether a profitable action was grounded, profile-consistent, or merely lucky. We ask whether the community is using the wrong ruler for consequential agents.   We i...
  </details>

- **2026-08-06** — Rajatsubhra Chakraborty, Xujun Che, Ritabrata Chakraborty et al. — [MAVISEG: Manifold Propagation and Visual Prototypes for Zero-Shot Open-Vocabulary Segmentation in Diffusion Transformers](http://arxiv.org/abs/2608.05878v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion transformers learn about objects and scenes by learning to generate them, making them strong candidates for training-free zero-shot open-vocabulary semantic segmentation. State-of-the-art attribution methods score each pixel independently, comparing its features against a fixed text-derived class representation, whether as an output-space similarity or as a cross-attention weight. This discards structured signals the model itself exposes: the temporal structure of the gen...
  </details>

- **2026-08-05** — Zijie Zhuang, Changxin Lao, Pengbo Xu et al. — [From Trajectories to Evidence: Auditable Experimental Records for Industrial Research Agents](http://arxiv.org/abs/2608.05235v1)
  <details><summary>📄 Abstract</summary>
  Research agents increasingly conduct multi-round machine-learning experiments in industrial recommendation settings and retain the resulting trajectories to guide later decisions. Yet a completed trajectory is not automatically evidence: generated artifacts may be unsupported or incomplete, executed rounds may be invalid or confounded, and later modifications may obscure earlier findings. We study \textbf{trajectory-to-evidence conversion}, asking what a completed research process has actually e...
  </details>

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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-08-06** — Paweł Batorski, Przemysław Spurek, Paul Swoboda — [GROM: Gradient-Free Rapid One-Shot Machine Unlearning](http://arxiv.org/abs/2608.05783v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning has become a critical capability for safely removing specific, sensitive knowledge from large language models (LLMs). Current state-of-the-art approaches primarily rely on iterative, training-time unlearning via fine-tuning. However, even when utilizing parameter-efficient dimensionality reduction techniques like LoRA, gradient-based optimization remains computationally expensive and lacks explicit analytical formulations. It can also leave the targeted knowledge merely hidden...
  </details>

- **2026-08-05** — Yuhang Wang, Linlin Zhang, Haoxuan Ji et al. — [A Model Merging Approach for Continual MLLM Unlearning](http://arxiv.org/abs/2608.04548v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language model (MLLM) unlearning methods have been proposed to remove private, sensitive, or proprietary information from well-trained models. However, most existing MLLM unlearning methods are designed for one-shot requests and fail to adequately address continual scenarios, as repeatedly applying one-shot operations leads to cumulative utility degradation, unlearning rebound, and retention drift. We introduce Merging for Continual Unlearning (MCU), an approach that dynamically...
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
*综述与系统化 / Surveys & Systematization* — 6 papers

- **2026-08-06** — Jessica Y. Bo, Paula Akemi Aoyagui, Shalaleh Rismani et al. — [Studying People to Study AI: Expert Perspectives on the Epistemic Fit and Barriers of Human Research in AI Safety & Ethics](http://arxiv.org/abs/2608.05656v1)
  <details><summary>📄 Abstract</summary>
  Safety risks of AI are becoming increasingly evident in human interactions with AI technologies. The prominent approaches to evaluating these risks favor technical methods, such as model benchmarks and LLM simulations, often sidelining empirical research with human subjects. To examine this apparent gap in the acceptance of human research, we conduct an expert survey (n=93) and expert interviews (n=17) with AI Safety & Ethics (AISE) researchers from Technical, Sociotechnical, Governance, and Nor...
  </details>

- **2026-08-05** — Casey Wall, Longwei Wang, Rodrigue Rizk et al. — [Grad-CAM for Vision Transformers: A Systematic Taxonomy and Audit of Methodological Ambiguity in Explainable AI](http://arxiv.org/abs/2608.05258v1)
  <details><summary>📄 Abstract</summary>
  Gradient-weighted Class Activation Mapping (Grad-CAM) is widely used to visualize model decisions, but it was originally formulated for convolutional neural networks, where spatial feature maps and channel dimensions have clear architectural meanings. Vision Transformers (ViTs) do not provide the same structure, instead representing images through tokens, attention, residual streams, and multimodal interactions. This paper presents a systematic taxonomy and literature audit of how Grad-CAM and r...
  </details>

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


### 📂 other
*其他安全相关 / Other Security-Related* — 158 papers

- **2026-08-06** — Fanzhe Meng, Guoxin Chen, Jiale Zhao et al. — [CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks](http://arxiv.org/abs/2608.06352v1)
  <details><summary>📄 Abstract</summary>
  Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation establishes feasibility, yet does not reveal how a task behaves relative to a given solver setting. In this paper, we present CalibForge, an autonomous terminal-task synthesis system that uses verified solver behavior to revise candidate tasks through adversarial solver calibration. Multi-solver calibration targets disagreement within a...
  </details>

- **2026-08-06** — Germana Bertoli, Ilaria Amelia Caggiano, Francesca Lagioia et al. — [What out-of-the-box LLMs can(t) do in law? A Turing test in Italian exams for lawyers, judges and notaries](http://arxiv.org/abs/2608.06166v1)
  <details><summary>📄 Abstract</summary>
  The article reports on a blind Turing Test experiment, assessing the performance of out-of-the-box leading LLMs on three Italian legal professional exams: the Bar, Judges and Notary exams. Leading LLMs were asked to generate full written exam papers, which were made indistinguishable from human submissions and anonymously evaluated by expert examiners, using the same criteria applied in real examinations. Results reveal marked differences across both models and tasks. While some LLMs match or ex...
  </details>

- **2026-08-06** — Leo Sambrook, Sampo Sovio — [Hardware Keystores for AI Agent Signing Workflows: A Zero-Trust MCP Enforcement Architecture](http://arxiv.org/abs/2608.06130v1)
  <details><summary>📄 Abstract</summary>
  AI agents performing cryptographic operations (signing Git commits, authenticating API calls, issuing certificates) currently store private keys in software-accessible locations: plaintext files, environment variables, or container memory. Any process with sufficient read privileges can extract the raw key material. A recent production incident demonstrated the practical severity: private keys were exfiltrated from a widely deployed framework via email injection in under five minutes. We aim to ...
  </details>

- **2026-08-06** — Junfeng Li, Junjie He, Zhide Zhong et al. — [DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation](http://arxiv.org/abs/2608.06374v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have become a powerful paradigm for robot manipulation, but training a single generalist policy for heterogeneous robot embodiments remains an open problem. Existing methods have two main limitations. First, they underuse dynamics priors shared across diverse visual and interaction data, limiting cross-embodiment transfer. Second, they require extensive manual preprocessing to convert embodiment-specific actions into a common format. To overcome these limitati...
  </details>

- **2026-08-06** — Praphul Chandra, Sujit Gujar, Ganesh Ghalme — [Resourced Authority A Mechanism-Design Model for Participatory Governance of Deployed AI Agents](http://arxiv.org/abs/2608.06353v1)
  <details><summary>📄 Abstract</summary>
  We give a formal mechanism design model for the continuous participatory governance of a deployed AI agent. The mechanism is built on the principle that governance should control an AI agent through resource allocation so as to make authorization self enforcing via compute budgets. The mechanism seeks to establish the Safe AI paradigm that compute is an effective governance lever. We situate our work as a compliance or commons overlay on a deployer. One governance period is an extensive form gam...
  </details>

- **2026-08-06** — Alexandra Newcomb, Omar Ochoa — [Automatic Translation of Unstructured Requirements into Linear Temporal Logic through Large Language Models](http://arxiv.org/abs/2608.06287v1)
  <details><summary>📄 Abstract</summary>
  Automatically translating unstructured natural language requirements into formal specifications remains a challenge in requirements engineering and formal methods, particularly for safety- and mission-critical systems whose verification depends on mathematically precise specifications. This paper evaluates whether contemporary off-the-shelf Large Language Models (LLMs) can help bridge this gap by generating Linear Temporal Logic (LTL) formulas directly from unstructured requirements. The study e...
  </details>

- **2026-08-06** — Stefan Dziembowski, Grzegorz Fabiański, Daniele Micciancio et al. — [Game Hopping in Lean](http://arxiv.org/abs/2608.06261v1)
  <details><summary>📄 Abstract</summary>
  We present HOPSCOTCH, a Lean 4 framework for mechanizing computationally sound, game-based cryptographic proofs. Security definitions are expressed as indistinguishability between stateful probabilistic oracles, and proofs follow the standard game-hopping paradigm. HOPSCOTCH uses a shallow embedding: oracles and reductions are ordinary Lean definitions, enabling direct integration with the full Lean ecosystem, including general mathematical theories from Mathlib, such as finite-group theory. A g...
  </details>

- **2026-08-06** — Haris Riaz, Hyungji Kim, Mihai Surdeanu — [Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers](http://arxiv.org/abs/2608.06111v1)
  <details><summary>📄 Abstract</summary>
  Positional embeddings (PE) in Transformers encode token distance and order but are largely agnostic to \textit{syntactic structure}. We introduce \textbf{S}yntax-\textbf{i}nformed \textbf{P}ositional \textbf{E}mbeddings (\textbf{SiPE}), which learns a lightweight syntactic prior from dependency parses during pretraining and injects it across all three dominant PE families (absolute, relative, rotary), for both encoders and decoders, leaving self-attention and the rest of the architecture untouch...
  </details>

- **2026-08-06** — Zelong Sun, Jun Wang, Kaicheng Yang et al. — [Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval](http://arxiv.org/abs/2608.06060v1)
  <details><summary>📄 Abstract</summary>
  Unified multimodal retrieval aims to identify candidates that satisfy complex user intent expressed through heterogeneous inputs. Although Large Vision-Language Model (LVLM)-based retrievers are efficient and scalable, directly encoding raw multimodal inputs often misses fine-grained discriminative cues, leading to confusion among semantically similar candidates. Recent methods mitigate this limitation by generating Chain-of-Thought (CoT) rationales to enrich the query representation. However, s...
  </details>

- **2026-08-06** — Zirui Wang, Jiaqi Wang, Qinghan Wang et al. — [EpiBench: Can LLMs Understand Epitopes for Antibody Drug Discovery?](http://arxiv.org/abs/2608.06022v1)
  <details><summary>📄 Abstract</summary>
  Epitopes determine where antibodies bind antigens and shape downstream therapeutic properties such as functional blockade and escape resistance, making epitope understanding central to antibody drug discovery. Although large language models (LLMs) have shown strong biomedical reasoning ability, it remains unclear whether they can infer epitope information directly from antigen and antibody sequences. Existing epitope resources typically focus on isolated prediction tasks or rely on specialized s...
  </details>

- **2026-08-06** — Yuhan Zhou, Yuchu Luo, Hao Nie et al. — [TensorCast: The Missing Tensor Management Layer in Large Language Model Infrastructure](http://arxiv.org/abs/2608.06007v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM infrastructure increasingly manages tensors not only as computation data, but also as persistent states shared across distributed components. Existing systems optimize individual tensor management tasks, such as model weight loading, KV cache management, and checkpoint synchronization, by deeply integrating task-specific mechanisms with execution engines, networks, or storage backends. However, this specialization creates isolated silos that hinder the reuse and composition of tensor ...
  </details>

- **2026-08-06** — Paweł Batorski, Abtin Pourhadi, Akylgali Aitaza et al. — [MACRO: Markov Chain Routing of Transformer Layers](http://arxiv.org/abs/2608.05872v1)
  <details><summary>📄 Abstract</summary>
  Standard Large Language Models (LLMs) execute layers sequentially. Dynamic layer routing, i.e. search for a different execution path through layers involving layer repetitions, skips and other moves, can improve performance. Existing routing approaches often require updating model weights, running expensive search loops per test instance, or demand ground-truth labels during inference. In this work, we propose Markov Chain Routing of Transformer Layers (MACRO), a framework that learns task-speci...
  </details>

- **2026-08-06** — Hong Jiang, Junnan Zhu, Jingwang Huang et al. — [M$^3$R-Bench: A Unified Benchmark for Evidence-Grounded Multimodal Metaphor Understanding](http://arxiv.org/abs/2608.05817v1)
  <details><summary>📄 Abstract</summary>
  Metaphor enables the understanding of abstract concepts through cross-domain mappings while conveying affective attitudes. In multimodal scenarios, visual and textual information jointly construct Target--Source mappings, requiring both conceptual understanding and cross-modal reasoning. However, existing benchmarks mainly evaluate metaphor understanding through isolated subtasks and lack evidence-grounded explanations, making it difficult to assess whether models establish mappings grounded in ...
  </details>

- **2026-08-06** —  Vorch Team, Xiaoyu Chen, Yang Ding et al. — [Vorch-Omni: Multi-Task Orchestration of Sight and Sound](http://arxiv.org/abs/2608.05803v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative video modeling have enabled diverse generation, reference-based synthesis, extension, and editing, but existing approaches often rely on fragmented task-specific models. A general model must distinguish heterogeneous target, source, and reference signals to determine what to generate, preserve, or use as guidance, while reducing interference among tasks. Joint audio-visual generation further increases this challenge by introducing diverse conditioning and output con...
  </details>

- **2026-08-06** — Stefan Krsteski, Charlotte Meyer — [Predicting Task Difficulty Without Rollouts](http://arxiv.org/abs/2608.05797v1)
  <details><summary>📄 Abstract</summary>
  Task difficulty dictates an agent's likelihood of success, and estimating it without rollouts means forecasting this directly from a task description before executing costly simulations in stateful environments. Reliable estimates would therefore allow environment designers to calibrate evaluation benchmarks and construct progressive training curricula. This becomes increasingly important as agents move into long-horizon domains, where empirical trial-and-error is a severe computational bottlene...
  </details>

- **2026-08-06** — Lisai Zhang, Yidi Wu, Qi Liu et al. — [Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification](http://arxiv.org/abs/2608.05776v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive continuation provides a natural path toward minute-scale audio-visual generation by repeatedly extending a short-window generator conditioned on previously generated video and audio. However, models are trained on clean ground-truth histories, while inference relies on their own generated histories, where accumulated errors cause identity drift, over-smoothing, and audio-visual desynchronization. Recent methods reduce this mismatch by reusing prediction residuals as synthetic corr...
  </details>

- **2026-08-06** — Shuhao Yan, Changhao He, Xi Peng et al. — [RA-CAD: Learning Post-Execution Critique for State-Aware Text-to-CAD Generation](http://arxiv.org/abs/2608.05714v1)
  <details><summary>📄 Abstract</summary>
  Text-to-CAD generation translates natural-language design intent into editable and executable parametric computer-aided design (CAD) codes, reducing the expertise and effort required for manual modeling. Existing methods incorporate fixed, externally supplied, prompt-induced, or separately optimized critique mechanisms to optimize the generation process, but they do not necessarily optimize how feedback is interpreted and translated into effective corrective actions throughout the generation pro...
  </details>

- **2026-08-06** — Menglin Han, Yang Ding, Yulei Lu et al. — [Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](http://arxiv.org/abs/2608.05663v1)
  <details><summary>📄 Abstract</summary>
  Real-time long-form avatar audio--video generation requires causal, continuous synthesis while maintaining audiovisual synchronization and visual consistency. Adapting a pretrained bidirectional model to this setting presents two key dilemmas. First, autoregressively reusing generated blocks as context creates exposure bias, causing errors and visual drift to accumulate over long rollouts. Second, a global speech utterance does not indicates a causal generator which portion should be spoken next...
  </details>

- **2026-08-06** — Nimisha Karnatak, Max Van Kleek, Nigel Shadbolt — [Epistemic Trustworthiness in Generative AI: A Normative Framework for Warranted Reliance in High-Stakes Workflows](http://arxiv.org/abs/2608.05602v1)
  <details><summary>📄 Abstract</summary>
  Generative AI systems are increasingly deployed in high-stakes professional contexts, where their outputs shape what users believe, how they reason, and what they treat as settled. This raises a central question for responsible AI: under what conditions is reliance on generative AI outputs epistemically warranted rather than behaviourally induced? Existing frameworks largely ask whether AI outputs are accurate, fair, explainable, safe, or trusted by users. These questions remain necessary, and e...
  </details>

- **2026-08-06** — Haijie Li, Jiaxin Zhang, Dave Zhenyu Chen et al. — [CoordRefer: Coordinate-Aware 3D Visual Grounding from Multiview Images](http://arxiv.org/abs/2608.05569v1)
  <details><summary>📄 Abstract</summary>
  Multiview image-based 3D visual grounding predicts a coordinate frame to define a coordinate system and then regresses a 3D bounding box for localization. However, existing methods jointly optimize coordinate frame selection and box regression, leading to coordinate-relative box ambiguity and degraded grounding performance. This ambiguity arises because the same box admits different numerical representations across coordinate frames, creating multiple optimization targets and yielding invalid co...
  </details>

- **2026-08-06** — Yuyang Dai, Xueqing Peng, Yuxia Wang et al. — [Seeing Is Not Deciding: Can Multimodal LLMs Act as Effective CEOs?](http://arxiv.org/abs/2608.05864v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly applied as autonomous decision-making agents. However, in executive business decisions, existing benchmarks are limited to textonly settings. This makes it unclear whether models can perceive visual business evidence and effectively integrate it to improve decision quality. We introduce C-SUITEBENCH, a controlled multimodal benchmark that includes five decision tasks under paired text-only and multimodal conditions across 50 scenarios. We place nine frontie...
  </details>

- **2026-08-06** — Jiarui Yang, Wen Huang, Jiale Zhang et al. — [In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use](http://arxiv.org/abs/2608.05738v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have become the dominant recipe for generalist manipulation, yet they are almost universally trained by behavior cloning: a policy imitates expert action chunks conditioned on a static image and a fixed instruction. A natural remedy is to inject explicit reasoning through textual chain-of-thought (CoT). We show, both empirically and analytically, that free-form textual CoT degrades low-level control: the reasoning it produces is ungrounded, its latency breaks ...
  </details>

- **2026-08-06** — Daniia Zinniatullina, Iaroslav Kolomiets, Mikhail Konenkov et al. — [SpaceVLA: Spatially Grounded VLA for Robotic Manipulation with User-Authored Grasp and Place Anchors](http://arxiv.org/abs/2608.05730v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models follow language commands but often lack explicit spatial intent for manipulation. We present Visual Intent Anchors, an XR pipeline that lets users specify grasp and placement regions and renders them as image-space overlays for VLA control. We collect 200 Unity pick-and-place demonstrations and fine-tune OpenVLA-7B with LoRA on temporally subsampled annotated observations. The policy predicts tokenized 7-DoF incremental actions from marked RGB observations and...
  </details>

- **2026-08-06** — Hadi Hosseini, Samarth Khanna, Leona Pierce — [The Judgment-Consequence Gap: LLM Moral Reasoning in Healthcare Decisions](http://arxiv.org/abs/2608.05583v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) enter high-stakes domains such as healthcare, understanding their moral reasoning becomes essential. Decisions about scarce medical resources often hinge on judgments of responsibility, particularly when patients' own actions contribute to illness. We investigate how LLMs reason about responsibility and its consequences, tracing their judgments across successive levels, from the behavior, to the resulting illness, to the denial of care. We evaluate a wide range of...
  </details>

- **2026-08-06** — Mohammed Ali, Abdelrahman Abdallah, Adam Jatowt — [EXCISE: Query-Side Exclusion for Late-Interaction Retrieval](http://arxiv.org/abs/2608.05497v1)
  <details><summary>📄 Abstract</summary>
  Late-interaction retrievers handle exclusion queries poorly. When a user asks for X but not Z, the additive MaxSim score promotes documents covering Z, a problem we call exclusion inversion. We show that no readout of the frozen vectors recovers the constraint, because the difficulty lies in identifying the excluded topic, which depends on the query alone. EXCISE operates at query time and corrects the inversion while leaving the index frozen. Two query-side modules totalling 1.5M parameters ide...
  </details>

- **2026-08-06** — Andreas Chatziafratis, Claudio Giorgi, Alain Miranville et al. — [On generalised d'Alembert-type integral representations for damped wave equations on the quarter-plane](http://arxiv.org/abs/2608.06355v1)
  <details><summary>📄 Abstract</summary>
  We rigorously construct and verify a posteriori new closed-form solutions for the forced Maxwell-Cattaneo-Vernotte equation (also broadly known as the damped wave equation, hyperbolic heat, and telegrapher's equation on lossy transmission lines) posed on the spatiotemporal quarter-plane with general initial and boundary data in classical function spaces. For this purpose, the modern complex-analytic unified transform method of Fokas (originally developed for elliptic PDE and evolution equations ...
  </details>

- **2026-08-06** — Donna Hooshmand, Shubham Shahi, Cameron Barrie et al. — [Tytan: Interactive Neurosymbolic Construction of Analytic Semantic Schemas from Relational Data](http://arxiv.org/abs/2608.06331v1)
  <details><summary>📄 Abstract</summary>
  From natural-language query interfaces to automated report generation, data analysis tools need a description of the data: the real-world entities it contains, which columns function as measures or identifiers, and how tables connect into units of analysis. Today, this semantic layer is usually written by hand. This is a knowledge-acquisition bottleneck that limits the scalability of analytic systems, keeps non-technical users dependent on experts, and is itself error-prone. We present TYTAN, a ...
  </details>

- **2026-08-06** — Benjamin Cookson, Nisarg Shah, Paritosh Verma — [Fair and Efficient Balanced Allocations for Additive Valuations](http://arxiv.org/abs/2608.06325v1)
  <details><summary>📄 Abstract</summary>
  We study the existence of fair and efficient allocations of indivisible goods under the balancedness constraint, which requires that any two agents' bundles differ in size by at most one. Our main result establishes the existence of balanced allocations that satisfy envy-freeness up to one good (EF1) and fractional Pareto optimality (fPO) for arbitrary additive valuations. This generalizes a recent result of Kawase et al. (2026), which establishes existence only for personalized bivalued valuati...
  </details>

- **2026-08-06** — Arya Labroo, Mengjie Qian, Kate Knill — [Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors](http://arxiv.org/abs/2608.06300v1)
  <details><summary>📄 Abstract</summary>
  Automatic speaking assessment systems are increasingly deployed in high-stakes settings to mark second language (L2) learners' speaking tests, making it critical to show that their scores depend on speaking proficiency rather than irrelevant speaker attributes such as first language (L1) or age. Transformer-based foundation models have improved the accuracy of these L2 speaking graders, but their black-box representations make fairness and interpretability analysis more difficult. Building on pr...
  </details>

- **2026-08-06** — Yiting Zheng, Cheng Fang, Anthony Donofrio et al. — [RxnCLF: Contrastive Transformation-Aware Reaction Foundation Model for Improved Reactivity Prediction](http://arxiv.org/abs/2608.06259v1)
  <details><summary>📄 Abstract</summary>
  Reaction yield prediction remains challenging because labeled data are scarce and reaction space is both combinatorially large and sparsely populated, limiting the generalization of existing reaction representations. String-, fingerprint-, and graph-based reaction encodings only partially capture chemical transformations, making accurate prediction difficult for reactions with complex substrates. We propose reaction contrastive learning foundation (RxnCLF), a self-supervised contrastive framewor...
  </details>

- **2026-08-06** — Dohyun Ku, Min Gu Kwak, Francisco J. Pasquel et al. — [MetaboLLM: a metabolomics-specialized large language model for biochemical knowledge integration and predictive metabolite graph construction](http://arxiv.org/abs/2608.06253v1)
  <details><summary>📄 Abstract</summary>
  Metabolomics knowledge is distributed across heterogeneous resources and remains difficult to translate into predictive representations. We developed MetaboLLM, a metabolomics-specialized large language model adapted through continual pretraining, supervised fine-tuning, and structured retrieval, together with MetaboLLM-GIN, which converts generated biochemical descriptions into metabolite graphs for patient-level prediction using a graph isomorphism network. Across four backbone families, Metab...
  </details>

- **2026-08-06** — Ke-Xia Jiang — [Isomorphic Emergence of Lorentz and Gauge Symmetries--A Constructive Interpretation Based on Continuum Mechanics](http://arxiv.org/abs/2608.06244v1)
  <details><summary>📄 Abstract</summary>
  Lorentz symmetry and gauge symmetry constitute the mathematical cornerstones of modern physics, yet their ultimate physical origins remain elusive. From the standpoint of a constructive interpretation, this paper demonstrates that both symmetry structures can emerge isomorphically from a unified classical source: dynamical constraints on wave-packet excitations in a continuous elastic substrate medium (SM). Neither symmetry is posited as fundamental, nor does their emergence rely on quantization...
  </details>

- **2026-08-06** — Indivara Kolluru, Nathan Sportsman — [Comparative Approaches to Agent Retrieval over Large Skill Libraries](http://arxiv.org/abs/2608.06196v1)
  <details><summary>📄 Abstract</summary>
  Agents backed by large skill libraries must decide which skills to load and in what order. Loading the entire library into context is expensive and provides no structure for autonomous sequencing. We study two systems for this problem over a corpus of 690 skills: a hybrid ranker combining lexical and dense-embedding retrieval for sparse, on-demand loading, and a typed knowledge graph encoding workflow relations such as prerequisites, data flow, and ordering. On a set of 117 realistic, non-echoin...
  </details>

- **2026-08-06** — Aleks Bernhard, Arif Baran Yardimci — [Routing LLM Inference to the Cleanest Grid in Real Time](http://arxiv.org/abs/2608.06188v1)
  <details><summary>📄 Abstract</summary>
  Large-language-model inference is a fast-growing electricity load whose marginal carbon intensity varies by more than an order of magnitude across grid regions and across the day, making request placement an attractive lever: no retraining, no hardware change. We report a live validation of carbon-aware inference routing on multi-region GPU testbeds driven by marginal operating emissions rate (MOER) signals, with three properties uncommon in prior work: a blind baseline that is an actual product...
  </details>

- **2026-08-06** — Kevin Schott, Jan Lattenkamp, Daniel Hienert et al. — [Cleo: A Transparent and Controllable Chatbot for Conversational Commerce](http://arxiv.org/abs/2608.06068v1)
  <details><summary>📄 Abstract</summary>
  We demonstrate Cleo, a transparent and controllable conversational product advisor that addresses the challenges of opacity, unpredictability of LLMs, and the complexity of comparisons in conversational commerce. With our chatbot system, we make four contributions: First, we introduce transparency by prompting the LLM to reflect on interpreted user needs, while an auditable ranking mechanism reveals loss values per attribute, explaining ranking decisions. Second, we propose controllability throu...
  </details>

- **2026-08-06** — Jiahao Huang, Zheng Lian, Jingyi Zhang et al. — [OneEmo: A Unified Multimodal Reasoning Model for Emotion Perception, Understanding, and Interaction](http://arxiv.org/abs/2608.06013v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in emotional intelligence. However, prevailing research predominantly focuses on task-specific specialization, often neglecting inter-task synergy and leaving latent reasoning potential underexplored. To bridge this gap, we introduce OneEmo, a unified affective generalist capable of mastering emotion perception, comprehension, and interaction. For this purpose, we first construct EmoWorld-130K, a comprehensive dat...
  </details>

- **2026-08-06** — Patrick Krauss, Achim Schilling, Andreas Maier et al. — [Convergent Evolution in Neural Representation Space: Emergent Order in Deep Belief Networks](http://arxiv.org/abs/2608.05996v1)
  <details><summary>📄 Abstract</summary>
  Deep Belief Networks (DBNs) learn hierarchical generative models without class supervision. Here, we ask whether this purely unsupervised process nevertheless organizes internal representations according to the unknown data classes. We analyze successive layers of DBNs trained on MNIST, Fashion-MNIST, and KMNIST using the Generalized Discrimination Value (GDV), supervised probes applied only after training, a reconstruction-based measure of abstraction distance, effective dimensionality, and fre...
  </details>

- **2026-08-06** — Ning Xu, Xiang Zheng, Fuqiang Zhong et al. — [OPERA: Operator-residual feedback for reliable autonomous optical experiments with language-model agents](http://arxiv.org/abs/2608.05990v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents choose actions using scores that may not reflect experimental success. We developed OPERA, an operator-residual framework for optical experiments. It represents experimental actions as optical operators and evaluates their outcomes using physically interpretable residuals. Operators specify executable changes to measurement, control or reconstruction, while residuals report departures from specified physical conditions. The agent uses both to select, combine or generate operato...
  </details>

- **2026-08-06** — Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao et al. — [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](http://arxiv.org/abs/2608.05987v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, providing denser supervision, but it remains unclear how such local signals should represent sequential credit. We propose AgentOPSD, a critic-free, recursive method for turn-level credit assignment in ...
  </details>

- **2026-08-06** — Akanta Das, Tasinul Islam Ahon, Ahmed Mahir Sultan Rumi et al. — [ECG-LENS: Lead-Aware Clinical Context Enriched ECG Report Generation and Evaluation](http://arxiv.org/abs/2608.05893v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiography (ECG) is one of the most widely used non-invasive tools for diagnosing cardiovascular disease, but transforming multi-lead ECG recordings into reliable clinical reports remains challenging. Automating ECG report generation could reduce clinicians' interpretive workload, improve diagnostic efficiency, and expand access to cardiac assessment in underserved communities. Unlike image-based report-generation tasks, ECG interpretation requires the analysis of subtle temporal morpho...
  </details>

- **2026-08-06** — Przemysław Czuma — [The em-dash em-beds in Congress: A population-level rise in em-dash frequency in U.S. congressional press releases at the dawn of the large-language-model era, 2021-2025](http://arxiv.org/abs/2608.05889v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can leave small stylistic traces in text written with their help. The most discussed is the em-dash (U+2014), especially the unspaced form word---word, which is normal in typeset English prose but unusual in U.S. press writing, where AP style calls for spaced dashes. This study asks whether that trace is measurable in congressional press releases. In a preregistered design (OSF: 10.17605/OSF.IO/U5NEY), 146,239 scraper-sourced releases from 480 House and Senate office...
  </details>

- **2026-08-06** — Yaozi Zhong, Xingxing Yang, Shaohui Mei et al. — [Overcoming Attention Drift: Homogeneity-Heterogeneity Guided Feature Aggregation for Low-Light Remote Sensing Image Enhancement](http://arxiv.org/abs/2608.05843v1)
  <details><summary>📄 Abstract</summary>
  Restoring high-fidelity remote sensing imagery from extreme low-light degradation is indispensable for reliable Earth observation and downstream machine vision. However, under severe noise and illumination corruption, existing methods suffer from attention drift, erroneously aggregating features across distinct physical boundaries and causing severe structural blurring and color distortion. To address this, we propose HALO, a dual-prior-driven enhancement framework that formulates enhancement as...
  </details>

- **2026-08-06** — Jiafan Li, Mengxue Yang, Jiaqi Zhu et al. — [ViSR-KGC: Visual Subgraph Reasoning with Vision-Language Models for Multimodal Knowledge Graph Completion](http://arxiv.org/abs/2608.05833v1)
  <details><summary>📄 Abstract</summary>
  Knowledge graph completion (KGC) aims to infer missing entities or relations from incomplete graph structures, and has evolved into multimodal knowledge graph completion (MMKGC), where entities are associated with multiple modalities such as text and images. Traditional representation learning approaches follow the embedding-based paradigm and may struggle when relation-specific evidence is limited. Meanwhile, LLM-based reasoning methods typically linearize graph structures into textual prompts,...
  </details>

- **2026-08-06** — Ethan Hadley, Eren Gultepe — [Subliminal Learning is Non-Semantic Distillation](http://arxiv.org/abs/2608.05734v1)
  <details><summary>📄 Abstract</summary>
  Subliminal Learning (SL) is a surprising type of generalization displayed by modern language models. It allows the transfer of a bias or behavior from a teacher model to a student by distilling from seemingly unrelated or random synthetic data from the teacher. This presents challenges in ensuring AI systems remain predictable and are trained safely, as standard auditing of the input data would not catch the hidden subliminal signal. Here, we investigate several open questions as to the enabling...
  </details>

- **2026-08-06** — Kepeng Yang, Dongxuan Liu, Rongxin Gao et al. — [TAU-Bench: From Anomaly Instance Tracking to Fine-Grained Video Anomaly Understanding](http://arxiv.org/abs/2608.05699v1)
  <details><summary>📄 Abstract</summary>
  Humans understand anomalous events through a coherent perceptual process in which they identify the focal instance, follow its behavior as the event unfolds, and interpret why it violates the expectations of the surrounding scene. Video anomaly understanding (VAU) seeks to endow models with a similar capability, moving beyond deciding whether a video is anomalous toward explaining how the event develops and why it matters. Although recent vision--language models (VLMs) can generate detailed and ...
  </details>

- **2026-08-06** — Hamed Damirchi, Ignacio Meza De la Jara, Damith Ranasinghe et al. — [Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs](http://arxiv.org/abs/2608.05660v1)
  <details><summary>📄 Abstract</summary>
  As language models are increasingly used for tasks that require verifiable reasoning, reliably distinguishing sound reasoning from flawed reasoning has become an important practical problem. Recent trajectory-based methods seek this signal in layerwise residual-stream displacements, which capture how representations change while attenuating some stable, token-specific information. However, displacement omits the state from which an update originates, whereas restoring the full state risks reintr...
  </details>

- **2026-08-06** — Daniel Richard Levy — [Morphology of frozen labyrinths from irreversible threshold dynamics](http://arxiv.org/abs/2608.05496v1)
  <details><summary>📄 Abstract</summary>
  Majority threshold dynamics, in which each agent adopts the dominant state in a weighted neighborhood, relaxes a binary field toward consensus or stripes. We study what happens when this rule is made irreversible: each agent, interacting through a Gaussian kernel on a lattice, may flip out of its local weighted minority at most once. The reversible form is threshold dynamics of Merriman-Bence-Osher type, an exactly solvable calibration in which interfaces move by mean curvature with closed-form ...
  </details>

- **2026-08-05** — Truong Thanh Hung Nguyen, Hoang-Loc Cao, Phuc Ho et al. — [Adaptive Arena-based Contestable Argumentative Network-of-Experts for Open-Ended Care Plan Coordination](http://arxiv.org/abs/2608.05391v1)
  <details><summary>📄 Abstract</summary>
  Care plan coordination demands synthesizing heterogeneous clinical, functional, and psychosocial information across multiple professional disciplines, where monolithic LLM pipelines cannot perform in a transparent or safe manner. We present CANOE (Contestable Argumentative Network-of-Experts), a multi-agent neuro-symbolic framework that addresses these limitations through five modules: complexity assessment, adaptive team recruitment, role-based argumentative computation via an Arena-based Quant...
  </details>

- **2026-08-05** — Zhaowei Han, Xiang Zhang, Bing Han et al. — [KV-Skill: Forging Expertise in the Model's Native Language](http://arxiv.org/abs/2608.05475v1)
  <details><summary>📄 Abstract</summary>
  Task knowledge is commonly stored either as text in the prompt or as an update to model weights. Text is modular but must be interpreted on every use, while weight adaptation makes the resulting capability difficult to load, remove, or share independently. We introduce KV-Skill, a design space of external factorized operators that a frozen language model reads through a lightweight interface. KV-Skill supports two complementary paths. Registration converts an authored text skill into a text-deri...
  </details>

- **2026-08-05** — Jake Zhang — [A Costly-information Foundation for Psychometric Curves](http://arxiv.org/abs/2608.05444v1)
  <details><summary>📄 Abstract</summary>
  We study a binary choice problem in which an agent chooses between two actions whose payoff depends on a continuous state. The agent chooses how much effort to invest in learning about the state. Equivalently, we can think of the state as the strength of a stimulus, with the agent exerting costly effort to be more responsive to it. Taking as given the Fisher information cost introduced by Hebert and Woodford (2021), we analyze the optimal state-dependent choice rule using a variational approach....
  </details>

- **2026-08-05** — Mahyar Ghazanfari, Amin Tabrizian, Arsyi Aziz et al. — [A Paragraph is Worth a Thousand Captions: Rethinking Text Supervision for Vision-Language Retrieval](http://arxiv.org/abs/2608.05260v1)
  <details><summary>📄 Abstract</summary>
  Contrastive vision-language models such as CLIP and BLIP are typically trained on short image captions, limiting their ability to retrieve images from detailed textual descriptions. While methods such as Long-CLIP extend the token limit through positional embedding interpolation, we ask a simpler question: does training text granularity alone determine long-text retrieval performance? We present a systematic study of supervision ranging from single captions to multi-sentence paragraphs for contr...
  </details>

- **2026-08-05** — Tsz Ting Chung, Jiangnan Li, Jie Zhou et al. — [InsightEmb: Learning Action-Intent Embeddings for Agentic Insight Retrieval](http://arxiv.org/abs/2608.04761v2)
  <details><summary>📄 Abstract</summary>
  Self-improving agents accumulate reusable insights from prior trajectories, making retrieval increasingly important for turning accumulated experience into actionable guidance. At each decision step, retrieving the right insight can help the agent progress toward its goal, a setting we refer to as agentic insight retrieval. However, existing retrieval methods primarily model semantic similarity, while overlooking whether a retrieved insight resolves the agent's current decision bottleneck. We pr...
  </details>

- **2026-08-05** — Ziwei Zheng, Peiqiong Chen, Bang Wang — [Abstract Event Causal Rules: Induction and Application](http://arxiv.org/abs/2608.05205v1)
  <details><summary>📄 Abstract</summary>
  Event-centric intelligent analytical systems heavily depend on explicit causal event knowledge for risk early warning, decision-making support and narrative comprehension. Nevertheless, existing instance-level causal pairs suffer severe generalization deficits on low-frequency long-tail and unseen event combinations. To address this limitation, this work proposes Abstract Event Causal Rule (AECR), a novel relation-level causal abstraction paradigm that transforms concrete cause-effect pairs into...
  </details>

- **2026-08-05** — Mouxiao Bian, Zhi Chen, Ruiyao Chen et al. — [RESPClinBench: Benchmarking Multimodal Clinical Decision-Making and Longitudinal Disease Management in Respiratory Specialty Care](http://arxiv.org/abs/2608.04514v2)
  <details><summary>📄 Abstract</summary>
  Background: Respiratory specialty care requires multimodal interpretation, longitudinal risk assessment, guideline-concordant intervention, and whole-course management, which are poorly represented by examination-oriented medical benchmarks. Objective: To develop RESPClinBench, a real-world scenario-based benchmark for respiratory clinical decision-making, and evaluate seven contemporary large language models across AECOPD-PIM and PNBIM. Methods: RESPClinBench cases were adapted from de-identifi...
  </details>

- **2026-08-05** — Yuhao Pan, Haosong Peng, Zhengshen Zhang et al. — [World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation](http://arxiv.org/abs/2608.05369v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models often treat main-view and wrist-view observations as parallel visual inputs, overlooking their distinct roles in robot manipulation. Fine-grained manipulation, however, benefits from anticipating how wrist-local interactions may evolve under the global task context. To address this limitation, we present World-to-Wrist VLA (W2-VLA), a VLA model for fine-grained robot manipulation with task-conditioned future wrist modeling. Given current multi-view observation...
  </details>

- **2026-08-05** — Jihoon Oh, Kento Kawaharazuka, Kei Okada — [VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances](http://arxiv.org/abs/2608.05215v1)
  <details><summary>📄 Abstract</summary>
  Learning manipulation skills from human videos is promising for scalable robot learning. However, the embodiment mismatch between humans and robots makes this challenging. One promising solution is to learn object-centric actionable affordances that are embodiment-agnostic. In this work, we propose a framework that leverages egocentric human videos with state-of-the-art 3D Structure-from-Motion and hand mesh reconstruction to extract actionable affordances such as visual, grasp, and trajectory a...
  </details>

- **2026-08-05** — Zehua Fan, Junjie He, Wenxuan Song et al. — [MobileWAM: Bridging World Action Models to Mobile Manipulation with Chain-of-Foresight](http://arxiv.org/abs/2608.04657v2)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) built on video generation backbones are a rising recipe for robot learning, yet remain confined to tabletop manipulation. Mobile manipulation demands simultaneous locomotion and whole-body manipulation amid scene-scale dynamics, yet is still dominated by dynamics-blind visual encoders with hand-crafted coordination. We bridge this gap with MobileWAM, a mixture-of-transformers architecture that fuses a pretrained video diffusion transformer with a lightweight action exp...
  </details>

- **2026-08-05** — Zhen Zhang, Amr Alanwar — [Matrix Zonotopic Attention: A Context-Adaptive Value Projection for Set Transformers](http://arxiv.org/abs/2608.05472v1)
  <details><summary>📄 Abstract</summary>
  Multi-head attention combines an input-dependent softmax routing with an input-independent linear value projection, so the per-sample operator mapping aggregated values to outputs is the same for every input set. We study the consequences of this asymmetry for permutation-invariant set targets. We introduce the Transformation Degrees of Freedom (TDOF) of a target operator, a complexity measure counting the input-dependent directions an exact representation requires, and present a depth-separatio...
  </details>

- **2026-08-05** — Ruilin Wang, Bo-Hong Wang, Elizabeth Kourbatski et al. — [DoctorAgents: an agentic framework to iteratively refine AutoML pipeline for small clinical temporal data](http://arxiv.org/abs/2608.05375v1)
  <details><summary>📄 Abstract</summary>
  Clinical machine learning (ML) has the potential to support high-stakes medical decision-making, but reliable deployment is often constrained by scarce, heterogeneous, and temporal complexity. Developing effective ML pipelines for such data remains time-consuming and error-prone, while existing automated machine learning (AutoML) systems only partially address this challenge because they largely rely on brute-force search over predefined spaces and lack explicit reasoning and memory. We therefor...
  </details>

- **2026-08-05** — H. Betancourt-Infante, G. Ruano, F. Bonetto et al. — [Cooperative adsorption and diffusion trapping induced by AlF3 intercalation in graphite](http://arxiv.org/abs/2608.05305v1)
  <details><summary>📄 Abstract</summary>
  Graphite's structural and electronic response to molecular intercalation is central to its performance as a carbon-based electrode material, yet the microscopic coupling between subsurface intercalation and surface adsorption remains poorly understood. We present a first-principles investigation of AlF3 adsorption and intercalation in graphite to explain the microscopic origin of a recently observed two-step self-limiting sorption mechanism. Using density functional theory (DFT-D3), we show that...
  </details>

- **2026-08-05** — Haoze Sun, Jiequan Cui, Qingshan Xu et al. — [Disentangling 3D Modeling from Spatial Reasoning](http://arxiv.org/abs/2608.05242v1)
  <details><summary>📄 Abstract</summary>
  In this work, we explore an alternative paradigm for spatial reasoning by explicitly disentangling 3D perception from reasoning, rather than jointly acquiring implicit 3D perception and reasoning through large-scale training. Our key observation is that modern perception models excel at estimating continuous 3D geometry, whereas large language models (LLMs) are particularly effective at compositional and symbolic reasoning. Motivated by these complementary strengths, we propose the Disentangled ...
  </details>

- **2026-08-05** — Zhixiang Liang, Yifei Liu, Yidan Huang et al. — [SearchAuditor: Auditing and Attributing Failures in Long-Horizon Search Agents](http://arxiv.org/abs/2608.05212v1)
  <details><summary>📄 Abstract</summary>
  Deep search agents tackle challenging questions through long-horizon web interactions, a process that is both complex and fragile: small reasoning errors may propagate through long, noisy trajectories into fluent but incorrect answers. Diagnosing such failures is difficult, requiring the manual inspection of extremely long execution traces, which could be beyond human capacity. We therefore introduce SearchAuditBench, a benchmark that evaluates whether LLM auditors can localize, attribute, and r...
  </details>

- **2026-08-05** — Pau Arnal, Khaled Denfir, Danylo Smahliuk et al. — [EuroExec: Frontier Language Models Fall Short of Expert Judgment on European Executive Decision Tasks](http://arxiv.org/abs/2608.04549v2)
  <details><summary>📄 Abstract</summary>
  Frontier LLMs are increasingly put to use on open-ended complex questions, different in nature from the ones they are typically evaluated on. We dedicate more than 4,000 human expert hours to evaluate a selection of six frontier LLMs on a member of this class of problems: EuroExec, our introduced human expert-based benchmark composed of 413 open-ended long-form European executive tasks authored by 47 vetted domain experts, each question drawn from experience in a real case. Every response is man...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 566 |
| prompt-injection | 476 |
| memory-poisoning | 43 |
| tool-use-attack | 100 |
| backdoor | 408 |
| adversarial-attack | 549 |
| privacy-leakage | 3776 |
| steganography | 55 |
| misuse | 858 |
| red-teaming | 112 |
| vulnerability | 2587 |
| defense | 2273 |
| alignment | 2109 |
| robustness | 2061 |
| watermark | 243 |
| unlearning | 86 |
| agent-safety | 52 |
| benchmark | 55 |
| survey | 268 |
| other | 5986 |

---

📚 **全部 22663 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-08 12:36:21*