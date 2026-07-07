<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-19938-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-07 03:24 ｜ **论文总数 / Total Papers**: 19938（近 30 天 / Recent 30 days: 4578）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 19938 篇论文（含摘要、分类筛选、搜索）/ View all 19938 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 537
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 444
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 35
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 89
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 381
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 520
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3634
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 51
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 788
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 104
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2332
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 1961
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1776
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1602
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 159
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 81
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 48
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 53
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 237
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5106

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4578 篇，完整 19938 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4578 papers from the last 30 days (with date, authors & abstract). For the full list of 19938 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-07-04** — Abhishek Kumar, Carsten Maple — [Refused in Chat, Written in Code: Workflow-Level Jailbreak Construction in IDE Coding Agents](http://arxiv.org/abs/2607.03968v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as IDE-integrated coding agents that decompose tasks, generate and edit files, run code, and refine outputs over many turns. Yet their safety is still often evaluated as if they were chatbots: one harmful prompt, one response, judged in isolation. We introduce workflow-level jailbreak construction, a failure mode in which a harmful objective is assembled across ordinary stages of a software-development workflow rather than generated through a singl...
  </details>

- **2026-07-02** — Joshua Adrian Cahyono — [Safety Targeted Embedding Exploit via Refinement](http://arxiv.org/abs/2607.01859v1)
  <details><summary>📄 Abstract</summary>
  Safety training for large language models (LLMs) is conducted predominantly in English, leaving uncertain how well safety mechanisms generalize to low-resource languages and mixed-language code-switching. We show that this creates an epistemic gap in which models confidently generate harmful responses for inputs that fall outside the distribution of their safety training. To study this phenomenon, we introduce STEER (Safety Targeted Embedding Exploit via Refinement), a gradient-guided attack tha...
  </details>

- **2026-07-01** — Shei Pern Chua, Fangzhao Wu — [HARC: Coupling Harmfulness and Refusal Directions for Robust Safety Alignment](http://arxiv.org/abs/2607.00572v1)
  <details><summary>📄 Abstract</summary>
  Understanding how aligned LLMs internally represent safety is critical for diagnosing alignment vulnerabilities, as it explains why jailbreaks succeed and informs the design of robust alignment strategies. Prior work shows that aligned LLMs encode harmfulness and refusal as separable directions in the residual stream at prompt-side token positions. We show that jailbreaks succeed at prompt encoding by suppressing either the refusal or harmfulness direction before any token is generated, with dis...
  </details>

- **2026-07-01** — Junlong Liu, Haobo Wang, Weiqi Luo et al. — [Beyond the Prompt: Jailbreaking Function-Calling LLMs via Simulated Moderation Traces](http://arxiv.org/abs/2607.00481v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak attacks remain a critical threat to the safe deployment of large language models (LLMs). While prior work has primarily studied attacks and defenses at the prompt level, we show that this prompt-centric paradigm overlooks a structural vulnerability in stateful, function-calling environments. In such applications, developer-defined schemas, structured arguments, and untrusted tool outputs are interleaved into a single shared model context. This architecture expands the attack surface by...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 6 papers

- **2026-07-06** — Kristina Nikolić, Egor Zverev, Javier Rando et al. — [Untrusted Content Masking for Web Agents with Security Guarantees](http://arxiv.org/abs/2607.05277v1)
  <details><summary>📄 Abstract</summary>
  Defenses that provide security guarantees against prompt injection attacks rely on strict isolation between trusted instructions and untrusted data. In text-based environments such as tool-use APIs, this separation arises naturally: agents can reason from interface definitions without ever processing untrusted content. Extending these guarantees to web agents faces a fundamental challenge: to perceive and interact with their environment, web agents must first observe the rendered page, which int...
  </details>

- **2026-07-06** — Yechao Zhang, Shiqian Zhao, Jiawen Zhang et al. — [When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents](http://arxiv.org/abs/2607.05189v1)
  <details><summary>📄 Abstract</summary>
  Persistent personal agents combine long-term memory with access to users' external environments, enabling personalized foreground assistance and proactive background execution. This integration also creates a new path to compromise: untrusted external content can be silently written into persistent memory and later reused as trusted state. We study this threat as stealth memory injection, in which a remote black-box adversary delivers a single email payload that must induce the agent to write po...
  </details>

- **2026-07-06** — Woohyuk Choi, Juhee Kim, Taehyun Kang et al. — [Agent Data Injection Attacks are Realistic Threats to AI Agents](http://arxiv.org/abs/2607.05120v1)
  <details><summary>📄 Abstract</summary>
  AI agents act on behalf of user prompts, consuming external data and taking actions based on the agent context. Prior research on AI agent security has primarily focused on indirect prompt injection (IPI). Its most well-studied category is instruction injection, where attacker-controlled untrusted data is interpreted as an instruction. In response, many mitigations have been proposed to prevent instruction injection attacks. In this paper, we introduce a new category of IPI, agent data injection...
  </details>

- **2026-07-05** — Bogdan Banu — [Biological Motifs for Agentic Control](http://arxiv.org/abs/2607.04240v1)
  <details><summary>📄 Abstract</summary>
  The transition of Large Language Models (LLMs) from passive generators to autonomous agents has introduced significant challenges in reliability, security, and state management. Current agentic architectures are often constructed ad-hoc, prone to hallucination cascades, infinite loops, and prompt injection attacks. This paper argues that many of these failure modes can be analyzed using control motifs long studied in systems biology, provided the comparison is made at the level of typed interfac...
  </details>

- **2026-07-05** — Amit LeVi, Elad David, Max Fomin — [Unsupervised Features Mining via Activation Geometry](http://arxiv.org/abs/2607.04222v1)
  <details><summary>📄 Abstract</summary>
  Interpretability methods aim to reveal the features represented inside large language models (LLMs). Many existing methods begin with labeled examples of a human-defined concept that may reflect human biases, and then identify how that concept is represented within the model, for example in its activation space or through other decomposition methods. We introduce \emph{Mining via Activation Geometry} (MAG), a simple unsupervised framework for extracting reasoning features from model activations ...
  </details>

- **2026-07-04** — Juhee Kim, Woohyuk Choi, Taehyun Kang et al. — [DualView: Preventing Indirect Prompt Injection in Personal AI Agents](http://arxiv.org/abs/2607.03821v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents that run on the user's local machine, such as OpenClaw, automate daily tasks including web search, email, and file management. Their access to computer resources, including the network, file system, and shell, exposes them to indirect prompt injection (IPI) attacks. Prior Dual LLM defenses block IPI by replacing untrusted data with symbols that the agent can reference but not read. However, they track untrusted data only inside the agent's context, so when the agent saves and ...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 3 papers

- **2026-07-06** — Neeraj Karamchandani, Piyush Nagasubramaniam, Sencun Zhu et al. — [Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses](http://arxiv.org/abs/2607.05029v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts...
  </details>

- **2026-07-05** — Om Solanki, Lopamudra Praharaj, Deepti Gupta et al. — [Knowledge Base Poisoning Attacks and Defense for Policy-Aware LLM-RAG Framework](http://arxiv.org/abs/2607.04379v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an adversarial security study of the Policy-Aware LLM Retrieval-Augmented Generation (PA-LLM-RAG) framework for Internet of Battlefield Things (IoBT) mission control. We propose Query-Agnostic Semantic Retrieval Poisoning, a novel attack that injects semantically crafted rules into the IoBT knowledge base achieving high retrieval ranking across all operator query types without requiring knowledge of runtime prompts. The attack achieves 85% LLM context corruption from a single...
  </details>

- **2026-07-02** — Jiankai Jin, Xiangzheng Zhang, Zhao Liu et al. — [ElephantAgent: Contextual State Continuity in Agentic Systems](http://arxiv.org/abs/2607.01919v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems enhance their capabilities by invoking external tools and maintaining persistent memory. However, these external dependencies introduce novel attack surfaces. Recent tool and memory poisoning attacks show that maliciously crafted tool descriptors and poisoned memory can covertly bias agent behavior. These threats reflect a deeper issue: the lack of verifiable continuity in the agent's contextual state for planning and execution. We present ElephantAgent, a protocol that enforces ...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-07-02** — Zimo Ji, Congying Xu, Zongjie Li et al. — [Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware](http://arxiv.org/abs/2607.02357v1)
  <details><summary>📄 Abstract</summary>
  LLM coding agents increasingly rely on third-party agent skills from public marketplaces, which execute with the agent's privileges and create a software supply-chain attack surface: a malicious skill can steal credentials, exfiltrate source code, or install backdoors. Existing defenses use static skill scanners based on pattern matching or LLM-as-judge analysis, but it remains unclear whether they withstand adaptive evasions that preserve malicious behavior while changing payload appearance.   ...
  </details>

- **2026-07-02** — Atharva Hans, Ilias Bilionis — [Coding-agents can replicate scientific machine learning papers](http://arxiv.org/abs/2607.02134v1)
  <details><summary>📄 Abstract</summary>
  Scientific machine learning papers typically make computational claims, e.g., that the relative mean square error is less than 5% or that the 95% predictive credible interval covers the test data. A coding agent can be prompted to replicate those claims from paper materials alone, but the prompt does not by itself reliably preserve progress or check whether generated evidence supports the paper's claims. We introduce Paper-replication, a workflow that makes each selected paper claim a target wit...
  </details>

- **2026-07-01** — Haoyu Gao, Jai Lal Lulla, Hong Yi Lin et al. — [From Registry to Repository: How AI Agent Skills Are Written, Adapted, and Maintained](http://arxiv.org/abs/2607.00911v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents increasingly rely on skills: structured context bundles, typically a SKILL.md file with a YAML header and Markdown body, loaded on demand for domain knowledge, workflows, and scripts. Public registries such as skills.sh now host tens of thousands of skills, making them an emerging unit of reuse in agent-based software engineering. Yet skills have largely been viewed as agent capabilities rather than software artefacts whose content and evolution shape agent behaviour. We present...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 7 papers

- **2026-07-06** — Fabien Polly — [Learning Only What Valid Adapters Can Express: Subspace-Constrained Adaptation Against Fine-Tuning Poisoning](http://arxiv.org/abs/2607.05300v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning still leaves a broad space of behavior-changing updates reachable, so a poisoned objective can be represented and optimized. We study an alternative: adaptation constrained to the subspace estimated from a trusted pool of existing task adapters. On flan-t5-large with 196 public LoRA adapters, we show that (1) the functionally relevant content of an adapter lies in a low-dimensional shared subspace, 30 to 38 percent of its weight norm being redundant under the eval...
  </details>

- **2026-07-06** — Yue Pan, Ziheng Zhang, Junxiang Lei et al. — [FORGE: Research-Trajectory Hijacking Attacks on Deep Research Agents](http://arxiv.org/abs/2607.04718v1)
  <details><summary>📄 Abstract</summary>
  Deep research agents decompose open-ended queries into subtasks, retrieve web evidence over multiple rounds, and synthesize long-form reports. This workflow creates a planning-layer poisoning surface: adversarial documents that enter the retrieval pool can steer follow-up questions and turn a local injection into report-level contamination. We present FORGE (Fabricated Orchestrated Reasoning chain for aGent Exploitation), a two-level attack that combines intra-document reasoning fabrication with...
  </details>

- **2026-07-02** — Thomas Winninger — [Steerability via constraints: a substrate for scalable oversight of coding agents](http://arxiv.org/abs/2607.02389v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are capable; human oversight is the bottleneck. Unconstrained agents introduce security risks, erode codebase scalability, and make human review increasingly costly. We argue that the same methods used for decades to manage large human engineering teams: access control, network policies, strict coding conventions enforced by tooling; transfer directly to coding agents, and are cheaper (in token) than recent agentic scaffolding. We sketch a start-to-end system on this principle, and...
  </details>

- **2026-07-02** — Yueming Huang, Wenhan Yao, Fen Xiao et al. — [DRL-CLBA: A Clean Label Backdoor Attack for Speech Classification via DDPG Reinforcement Learning](http://arxiv.org/abs/2607.01729v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models for speech classification are vulnerable to backdoor attacks, where malicious triggers cause misclassification at inference time. While sample-specific attacks can bypass many defenses, they often rely on poisoned label attack, making them detectable via manual data defense. In this paper, we propose DRL-CLBA, a novel clean label backdoor attack for speech classification that leverages Deep Deterministic Policy Gradient (DDPG) reinforcement learning. We also utilize deep aud...
  </details>

- **2026-07-02** — Dipayan Saha, Khan Thamid Hasan, Shams Tarek et al. — [VeriChat: An Agentic Conversational AI Assistant for Hardware Security Verification](http://arxiv.org/abs/2607.01668v1)
  <details><summary>📄 Abstract</summary>
  Hardware security verification is a multi-stage process in which engineers must navigate complex design analyses, threat considerations, and verification strategies. They often need security-focused guidance, yet current verification environments provide little structured support for such assistance. Although conversational AI could offer such on-demand assistance, directly using general-purpose chatbots like ChatGPT or Gemini is risky due to their tendency to hallucinate and their reliance on s...
  </details>

- **2026-07-01** — Zhihao Dou, Qinjian Zhao, Zhiqiang Gao et al. — [ReShift: Aha-Moment-Driven Reasoning-Level Backdoor Attacks on Vision-Language Models](http://arxiv.org/abs/2607.00361v1)
  <details><summary>📄 Abstract</summary>
  Vision--Language Models (VLMs) are increasingly deployed in safety-critical applications, yet remain vulnerable to backdoor attacks. Existing methods primarily manipulate final outputs, often producing reasoning traces that are inconsistent or easily detectable. In this paper, we propose ReShift, the novel aha-moment-driven reasoning-level backdoor framework that explicitly redirects the internal chain-of-thought (CoT) trajectory while preserving surface-level coherence. ReShift introduces a Poi...
  </details>

- **2026-07-01** — Shayan Talaei, Abhinav Chinta, Devvrit Khatri et al. — [Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation](http://arxiv.org/abs/2607.01208v1)
  <details><summary>📄 Abstract</summary>
  Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work has shown that these biases can transfer through context distillation on semantically unrelated data, ...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-07-02** — Haiyang Li, Yuming Fu, Qun Song et al. — [AGVBench: A Reliability-Oriented Benchmark of Data Augmentation for Vein Recognition](http://arxiv.org/abs/2607.02271v1)
  <details><summary>📄 Abstract</summary>
  Vein recognition is a secure biometric technology often constrained by limited annotated data and imaging variations. While data augmentation mitigates this, strategies designed for natural images may disrupt the fine-grained topology and textures essential for identity discrimination. We present AGVBench, which evaluates 30 representative augmentation strategies on five public palm- and finger-vein datasets with seven backbone architectures, covering classic CNNs, vision transformers, and vein-...
  </details>

- **2026-07-02** — Mahmoud Abdelfattah, Hamid Nasiri, Peter Garraghan — [kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail](http://arxiv.org/abs/2607.02072v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in domains requiring guardrails to detect unsafe, off-topic, or adversarial prompts. Existing guardrails predominately rely on fine-tuning to build classifiers, which often suffer from low generalization and high inference latency. We present kNNGuard, a training-free guardrail that utilizes the activation space of an off-the-shelf LLM. Given a small bank of 50 safe and unsafe prompts, kNNGuard extracts hidden activations and performs multi-...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 36 papers

- **2026-07-06** — Dylan Zongmin Liu — [SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints](http://arxiv.org/abs/2607.05363v1)
  <details><summary>📄 Abstract</summary>
  Personal agents are becoming persistent user-owned intermediaries: they remember preferences, filter platform-mediated information, use tools, and negotiate with services. Existing benchmarks evaluate tool use, web navigation, desktop control, personalization, recommendation, and evolving context, but rarely ask whether an agent preserves user sovereignty: advancing the user's current interests while respecting privacy, consent, evidence, user burden, and resistance to manipulative incentives. W...
  </details>

- **2026-07-06** — Xuyang Chen, Xiang Li, Yangxinyu Xie et al. — [Selective Disclosure Watermarking for Large Language Models](http://arxiv.org/abs/2607.05353v1)
  <details><summary>📄 Abstract</summary>
  Watermarking methods embed imperceptible and verifiable signals into text generated by large language models (LLMs). Existing approaches include zero-bit schemes for distinguishing synthetic text from human writing and multi-bit schemes for embedding metadata. However, current multi-bit watermarking methods do not allow selective disclosure: verifying any part of the watermark requires revealing the entire embedded message. This lack of control leads to unnecessary information exposure and raise...
  </details>

- **2026-07-06** — Zhiyuan Lu, Kanji Tanaka — [Trajectory-Anchor Optimization for Overconfident Thermal Visual Place Recognition: Zero-Leakage OOD Auditing and Kidnapped-Robot Recovery](http://arxiv.org/abs/2607.04745v1)
  <details><summary>📄 Abstract</summary>
  Modern thermal visual place recognition (TIR-VPR) frontends based on foundation models achieve remarkable closed-set retrieval but suffer from an overconfident forced-matching failure mode. Under out-of-distribution (OOD) or unmapped conditions, they generate highly plausible yet false loop candidates without a drop in similarity scores. While classical multi-hypothesis tracking (MHT) backends can mitigate these ambiguities by maintaining divergent trajectory beliefs, their exponential computati...
  </details>

- **2026-07-06** — Shubham Gupta, Nazanin Mohammadi Sepahvand, Abhinav Kumar et al. — [PiSAs: Benchmarking Contextual Integrity in Multi-User Agentic Systems](http://arxiv.org/abs/2607.05318v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents evolve from single-user assistants into shared organizational infrastructure, new privacy risks emerge: inappropriate information may not only be exposed through outputs for external recipients, but also internally across users through inter-agent messages, shared memory and agents. These data spillage risks are not captured by existing privacy benchmarks grounded in contextual integrity (CI) as they focus primarily on either single-user settings or interactions between independent...
  </details>

- **2026-07-06** — Md. Taksimul Ahsan Tawhid, Nasif Ahmed Rafe, Alif Tahmid Priyom et al. — [Wavelet Scattering Transform for Interpretable Schizophrenia Biomarker Discovery and Classification from Resting-State EEG](http://arxiv.org/abs/2607.05282v1)
  <details><summary>📄 Abstract</summary>
  Schizophrenia is a debilitating neuropsychiatric disorder characterized by profound cortical network dysregulation, for which objective, clinically translatable EEG based biomarkers remain underdeveloped. Existing automated classification pipelines rely predominantly on static power spectral density features inherently blind to amplitude modulation dynamics and cross-frequency coupling, phenomena central to schizophrenia pathophysiology, while adopting epoch level cross validation strategies tha...
  </details>

- **2026-07-06** — Mengmeng Liu, Diankun Zhang, Jiuming Liu et al. — [UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation](http://arxiv.org/abs/2607.05133v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) have shown strong potential for improving action generalization in autonomous driving by using future video prediction as dense supervision for scene dynamics and temporal causality. However, it remains unclear which architecture better transfers video-modeling benefits to trajectory generation. Existing cascaded or dual-DiT designs separate video imagination from action prediction, weakening the transfer of video-learned world dynamics to the trajectory branch: the ac...
  </details>

- **2026-07-06** — Xavier Fonseca — [Look-Ahead-Freedom as Temporal Non-Interference: A Verifiable Correctness Property for Backtesting and Agentic Trading Pipelines](http://arxiv.org/abs/2607.04958v1)
  <details><summary>📄 Abstract</summary>
  Look-ahead bias (using information from after a decision epoch to make the decision at that epoch) is the dominant way a backtest or a machine-learning evaluation flatters a system that will disappoint in deployment. The field manages it with construct-specific recipes and empirical detectors, which are sound only channel by channel and certify nothing by their silence. We show that look-ahead-freedom is a formal property in disguise: fixing an epoch, the demand that the future not influence the...
  </details>

- **2026-07-06** — Davide Jannussi, Stefano Carlo Lambertenghi, Constantin Carste et al. — [Cam2Sim: Neural Scenario Reconstruction for Closed-Loop Autonomous Driving Simulation](http://arxiv.org/abs/2607.04770v1)
  <details><summary>📄 Abstract</summary>
  Simulation-based testing enables safe and repeatable evaluation of autonomous driving systems, but its effectiveness is limited by the gap between synthetic simulator outputs and real-world camera observations. To address this problem, we present Cam2Sim, a tool that transforms real-world driving recordings into playable CARLA simulation scenarios. Starting from camera images and poses, Cam2Sim reconstructs road geometry, ego trajectories, parked vehicles, and simulation assets, and augments the...
  </details>

- **2026-07-06** — Vu Minh Tran, Doanh C. Bui, Maï K. Nguyen et al. — [MergeSurv: Merging-Based Continual Learning for Survival Analysis on Whole-Slide Images](http://arxiv.org/abs/2607.04747v1)
  <details><summary>📄 Abstract</summary>
  Survival analysis on Whole Slide Images (WSIs) is important in computational pathology for prognosis estimation and treatment planning. However, existing survival models are typically trained independently for each cancer cohort, making continual adaptation computationally expensive for gigapixel-scale WSIs. In this study, we propose MergeSurv, a merging-based continual learning framework for WSI survival analysis. A pathology vision-language foundation model is independently fine-tuned on each ...
  </details>

- **2026-07-05** — Nikos Athanasiou, Ilya A. Petrov, Angela Yao et al. — [TrustCLIP: Learning Private Visual Features via Adversarial Reconstruction](http://arxiv.org/abs/2607.04484v1)
  <details><summary>📄 Abstract</summary>
  Vision and vision-language models rely on high-level visual representations that are increasingly used across recognition, retrieval, and multimodal reasoning pipelines. However, recent advances in generative modeling have shown that such features can often be inverted, enabling realistic reconstructions of the underlying image and raising significant privacy risks. We revisit this problem through the lens of reconstruction and propose TrustCLIP, a reconstruction-driven framework that treats a f...
  </details>

- **2026-07-05** — Dayong Ye, Tainqing Zhu, Kun Gao et al. — [One Framework for All: Cross-Modal Membership Inference for Generative Models](http://arxiv.org/abs/2607.04339v1)
  <details><summary>📄 Abstract</summary>
  Large generative models across text-to-text, text-to-image, and image-to-text modalities have been shown to pose significant privacy risks. One fundamental threat is membership inference attacks (MIA), which aim to determine whether a given data point was used in a model's training set. Although prior work has investigated MIAs against these three classes of generative models, existing approaches treat them in isolation and are not cross-applicable, thereby limiting their real-world utility. To ...
  </details>

- **2026-07-05** — Joe Watson, Joana Ribeiro de Faria, Marcus Tomalin et al. — [Shortcut Learning in Legal Judgment Prediction: Empirical Evidence from the UK Employment Tribunal](http://arxiv.org/abs/2607.04261v1)
  <details><summary>📄 Abstract</summary>
  Current Legal Judgment Prediction (LJP) is constrained by its reliance on post-hoc judicial materials, increasing the likelihood that models perform retrospective classification rather than true forecasting. This paper empirically investigates shortcut learning in this context by studying claim-level outcome prediction in UK Employment Tribunal (UKET) decisions. Using a corpus of 33,158 individual claims, we predict outcomes from claim texts and LLM-extracted case summaries, evaluating models ra...
  </details>

- **2026-07-05** — Xinyu Lin, Yashar Deldjoo, Sunhao Dai et al. — [Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems](http://arxiv.org/abs/2607.04433v1)
  <details><summary>📄 Abstract</summary>
  The rapid integration of large language model-based agents into recommender systems has driven a shift from static, ranking-based pipelines toward autonomous and interactive systems that can reason, plan, and act. This survey provides a comprehensive overview of this emerging landscape by introducing a unified taxonomy grounded in the level of autonomy and three core paradigms of agentic recommender systems: agent-assisted recommendation, agent-as-recommender, and agent-as-user-simulator. The au...
  </details>

- **2026-07-05** — Jiaqi Tang, Shaoyang Zhang, Fandong Zhang et al. — [Topology-Driven Transferability Estimation for 3D Medical Vision Foundation Models](http://arxiv.org/abs/2607.04199v1)
  <details><summary>📄 Abstract</summary>
  The growing number of medical vision foundation models highlights the need for effective model selection. However, mainstream selection methods rely on exhaustive fine-tuning, which is computationally expensive. Most of the existing Transferability Estimation (TE) metrics are primarily designed for image-level classification. They fail to preserve spatial relationships and fine-grained boundary details, which are crucial for the segmentation task. Additionally, while image-level tasks typically ...
  </details>

- **2026-07-05** — Andrew Zhang, Chengzhan Li — [Agent Step Value: State-Transition Measurement with State-Grounded LLM Evaluators](http://arxiv.org/abs/2607.04419v1)
  <details><summary>📄 Abstract</summary>
  Most agent evaluations collapse a multi-step trace into a final answer, a success flag, or a trajectory-level score. These aggregates obscure the diagnostic question developers need most: which action changed the state in a useful direction? We introduce Agent Step Value (ASV), a state-transition measurement framework that scores each observed action by the change it induces in a state-grounded evaluator's distribution over fixed candidate outcomes. ASV renders redacted before/after state projec...
  </details>

- **2026-07-05** — Nicolas Della Penna — [Beyond Self-Resolution: Settlement Factorization for Robust Natural Language Mechanism](http://arxiv.org/abs/2607.04382v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly mediate paid advice: agents submit open-ended forecasts, recommendations, plans, and evidence; a principal acts on the reports; and the mechanism later pays the contributors. Advice should influence the public decision, but no adviser should write the answer key used to evaluate it. We formalize the separation as settlement factorization: reports are hardened into official records, a public decision record Z may use all advice, and each paid adviser is scored against...
  </details>

- **2026-07-05** — Mohamed Aly Bouke — [Detecting Hallucinations in Retrieval-Augmented Generation through Grounding-Aware Sensitivity by Perturbation (GASP)](http://arxiv.org/abs/2607.04223v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) reduces but does not eliminate hallucination, and existing detectors return a single answer-level score that does not indicate which sentence is unsupported, or why. To close this gap, we introduce Grounding-Aware Sensitivity by Perturbation (GASP), a span-level detector that scores each answer sentence by how strongly its likelihood depends on the retrieved evidence, a quantity we term grounding sensitivity. GASP holds the answer fixed and re-scores it under...
  </details>

- **2026-07-04** — Yudong Gao, Qingyue Wang, Yuanyuan Yuan et al. — [PathMark: Protecting Intellectual Property of Mixture-of-Expert LLMs via Path Watermarks](http://arxiv.org/abs/2607.03688v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) large language models represent high-value intellectual property, yet existing watermarking schemes designed for dense models fail on MoE architectures due to architectural mismatch: traditional methods assume watermarked parameters are consistently activated, but MoE's dynamic routing breaks this assumption. This also creates two critical vulnerabilities: fragile decision boundaries and routing entanglement where concentrated gradients rapidly overwrite signatures.   We...
  </details>

- **2026-07-04** — Md Omar Faruk Rokon, Andrei Simion, Weizhi Du et al. — [Enhancement of E-commerce Sponsored Search Relevancy with LLM](http://arxiv.org/abs/2607.03886v1)
  <details><summary>📄 Abstract</summary>
  Sponsored search plays a crucial role as a revenue stream for search engines, wherein advertisers competitively bid on keywords that align with the users' search queries. The task of matching relevant keywords to these queries is complicated by the vast and ever-evolving space of keywords, the ambiguity of user and advertiser intentions, and the wide range of topics and languages involved. Consequently, ensuring that ads are pertinent to user queries presents significant challenges. In the fast-...
  </details>

- **2026-07-04** — Yuhang Jiang, Guohui Deng, Miaozhong Xu et al. — [GeoSelect: Spatial-Program Execution for Training-Free Referring Remote Sensing Image Segmentation](http://arxiv.org/abs/2607.03869v1)
  <details><summary>📄 Abstract</summary>
  Referring remote sensing image segmentation isolates the object named by a natural-language expression in an aerial image. Existing training-free methods resolve the expression through implicit vision-language activations or region-text similarity, which gives weak control over the spatial, comparative, and ordinal relations that dominate aerial referring: they cannot represent constructions such as the largest ship or the second court from the left. We propose GeoSelect, a training-free pipelin...
  </details>

- **2026-07-04** — Matan Avitan, Yoav Goldberg, Yanai Elazar — [MANCE: Manifold Aware Concept Erasure](http://arxiv.org/abs/2607.03973v1)
  <details><summary>📄 Abstract</summary>
  Concept erasure aims to remove a target concept from a representation while preserving the other information encoded in it. This is difficult because representations encode many concepts that are often correlated with the erasure target, so removing the target risks damaging them. We propose the Manifold Constraint Hypothesis (MCH): if natural representations concentrate on a structured, lower-dimensional manifold, then interventions should be constrained to that manifold and better preserve oth...
  </details>

- **2026-07-04** — Varun Gupta, Vineet Gandhi, Makarand Tapaswi — [Attending to Multimodal Generation One Token at a Time](http://arxiv.org/abs/2607.03738v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) generate responses autoregressively, integrating visual and linguistic information in an evolving context. Prior work on interpretability has focused on individual layers and circuits (where), leaving the token-level dynamics of multimodal computation during generation (when) underexplored. We address this gap and study attention shifts as per semantic role; tracking model attention to image, text, instruction, and previously generated tokens, One Token a...
  </details>

- **2026-07-02** — Gemma Galdon Clavell, Pablo Accuosto, Usman Gohar — [The Eticas AI Risk Taxonomy: Open Infrastructure for Operationalizing AI Audits](http://arxiv.org/abs/2607.02201v1)
  <details><summary>📄 Abstract</summary>
  The rapid deployment of AI systems across high-stakes domains has created urgent demand for standardized evaluation, yet the field remains fragmented across competing risk taxonomies that catalog risks without showing how an audit is executed. At least 74 AI risk taxonomies exist, and almost all stop at the catalog. The hard part of auditing is not naming a risk but operationalizing it: turning it into a test run against a real system, a measured value, a calibrated severity, and a defensible gr...
  </details>

- **2026-07-02** — Jiale Amber Wang, Kaiyuan Wang, Pengyu Nie — [TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution](http://arxiv.org/abs/2607.02469v1)
  <details><summary>📄 Abstract</summary>
  Software tests and code evolve together: a code change should be followed by new or updated tests that record the new software behavior. Yet existing test generation and update benchmarks often isolate the test from the code change, and rely on static metadata that does not verify whether a test is executable or semantically tied to the code change. This makes it difficult to evaluate whether a test automation agent understands how a code change should propagate into the test suite.   We introdu...
  </details>

- **2026-07-02** — Seren Yenikent, Jack Vinijtrongjit, Katherine Ng — [Copewell: A Multi-Agent Swarm Architecture for Equitable Mental Wellness Support](http://arxiv.org/abs/2607.02245v1)
  <details><summary>📄 Abstract</summary>
  Mental health disorders affect nearly one billion people globally, yet 75% of individuals in low- and middle-income countries receive no treatment due to workforce shortages, cost barriers, and stigma. Current AI-powered wellness solutions predominantly rely on single-mode conversational interfaces that suffer high abandonment rates and fail to provide measurable, immediate relief calibrated to users' dynamic emotional states. This paper presents Copewell, a novel multi-agent swarm system design...
  </details>

- **2026-07-02** — Siyuan Li, Youyuan Zhang, Ruitong Liu et al. — [Multimodal Knowledge Edit-Scoped Generalization for Online Recursive MLLM Editing](http://arxiv.org/abs/2607.01978v1)
  <details><summary>📄 Abstract</summary>
  Online multimodal knowledge editing requires injecting a continual stream of visual-textual corrections into multimodal large language models (MLLMs) with bounded overhead and minimal disruption to unrelated behaviors. Existing editors mainly emphasize edit reliability and long-horizon stability, but rarely control the semantic boundary of each edit. Our pilot analyses of post-edit behaviors and internal neuronal activities reveal a scope gap behind reliable edits: instance-level success neither...
  </details>

- **2026-07-02** — Sofiane Ouaari, Kevin Vorwalder, Nico Pfeifer — [Assessing VLM Reliability for Medical Image Quality Evaluation Under Corruption and Bias](http://arxiv.org/abs/2607.01973v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are increasingly applied in medical tasks such as pathology description, report generation, and visual question answering. Medical Image Quality Assessment (MIQA) supports diagnostic accuracy and patient safety by determining whether images meet the standards required for clinical decision-making. Automating MIQA with VLMs may reduce workload, but their behavior under real-world conditions, where images may be degraded or textual context may affect judgments, should...
  </details>

- **2026-07-02** — Javier Irigoyen, Roberto Daza, Francisco Jurado et al. — [AIriskEval-edu: New Dataset for Risk Assessment in AI-mediated K-12 Educational Explanations](http://arxiv.org/abs/2607.01934v1)
  <details><summary>📄 Abstract</summary>
  This work introduces AIriskEval-edu-db2, a new dataset designed to train and evaluate auditors based on LLMs for an explainable pedagogical risk assessment in instructional content for grades K-12. The dataset comprises 1,639 explanations from 170 curated ScienceQA questions, covering science, language arts, and social sciences. For each question, the dataset includes an explanation written by a human teacher alongside 11 explanations generated by LLM-simulated teacher profiles associated with d...
  </details>

- **2026-07-02** — Yunhe Li, Hao Shi, Wenhao Liu et al. — [DemoPSD: Disagreement-Modulated Policy Self-Distillation](http://arxiv.org/abs/2607.02502v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) has emerged as a practical method for training large language models (LLMs) to reason, where a single model acts as both the teacher and the student with different levels of information access. However, recent studies have found that the teacher's dense token-level supervision, conditioned on privileged information, can lead to overfitting to in-domain patterns, suppress exploration, and hurt cross-domain generalization, while also introducing a more fundamenta...
  </details>

- **2026-07-02** — Quoc Bao Phan, Tuy Tan Nguyen — [QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition](http://arxiv.org/abs/2607.02426v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data, making it suitable for privacy-sensitive robotic sensing applications. However, multi-agent systems generate heterogeneous and non-independent and identically distributed (non-IID) multimodal sensor streams that degrade conventional FL algorithms, while classical fusion modules introduce substantial parameter overhead and communication cost. This paper proposes QFedAgent, a hybrid qu...
  </details>

- **2026-07-02** — Shuo Ren, Yaohui Han, Yifan Shi et al. — [A$^{2}$utoLPBench: An Auto-Generated, Agent-Friendly LP Benchmark via Inverse-KKT Construction](http://arxiv.org/abs/2607.02141v1)
  <details><summary>📄 Abstract</summary>
  Most LP-from-text benchmarks are static datasets of word problems written and labeled by hand. Once such a dataset is released, its size is fixed, its difficulty is fixed, and every problem can leak into the training data of future LLMs. We present \textbf{A$^{2}$utoLPBench}, a benchmark for testing LLM-driven agents on linear programming problems written in plain text. We first pick a feasible point and dual, then write down a problem for which that point is optimal and the objective value is k...
  </details>

- **2026-07-02** — Tzu-Heng Huang, Aditya Goyal, John Cooper et al. — [WARP: Weight-Space Analysis for Recovering Training Data Portfolios](http://arxiv.org/abs/2607.01686v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are routinely released to the public, yet the data recipes used to train them -- such as domain mixture weights that determine how different sources are sampled -- are rarely disclosed. This creates an access asymmetry: researchers study the resulting models but lack visibility into the training distribution that produces them. Prior works for inferring training data, such as membership inference, detect at the level of individual samples and thus cannot characterize the global...
  </details>

- **2026-07-01** — George Alexakis, Dimitrios Schoinianakis, Giorgos Dimitrakopoulos — [High-Performance NTT Accelerators for PQC leveraging Unified Redundant Arithmetic and Fine-Tuned Microarchitecture](http://arxiv.org/abs/2607.00621v1)
  <details><summary>📄 Abstract</summary>
  Post-quantum cryptography and privacy-preserving technologies are expected to play a central role in future secure communication systems. Lattice-based PQC schemes such as ML-KEM (CRYSTALS-Kyber) and ML-DSA (CRYSTALS-Dilithium) rely heavily on large-degree polynomial arithmetic, making the Number Theoretic Transform (NTT) a key computational primitive. Although existing hardware accelerators exploit parallelism and pipelining to support both NTT and INTT, their efficiency is often limited by the...
  </details>

- **2026-07-01** — Arya Raeesi, Hanna Roed — [Auditing Forgetting in Limited Memory Language Models](http://arxiv.org/abs/2607.00605v1)
  <details><summary>📄 Abstract</summary>
  Limited Memory Language Models (LMLMs) externalize factual knowledge to a database to enable deletion-based unlearning without retraining. Existing evaluations measure post-deletion correctness in aggregate and cannot tell whether a deleted fact persists through residual parametric memory, alternative retrieval paths, or near-neighbor retrieval artifacts. We propose a causal auditing framework that holds the model fixed and varies the database state at inference time across three interventions: ...
  </details>

- **2026-07-01** — Shijie Li, Yilin Gao, Siyuan Yang et al. — [Multimodal Continuous Reasoning via Asymmetric Mutual Variational Learning](http://arxiv.org/abs/2607.00461v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) are often constrained by a language-space bottleneck, forcing complex visual reasoning into discrete tokens which can lose perceptual nuance. A promising alternative is continuous latent reasoning, where the goal is to discover implicit reasoning pathways that bridge the multimodal query and the final answer. However, this introduces a severe train-inference mismatch: a training-time posterior, conditioned on the ground-truth answer, can exploit answer-de...
  </details>

- **2026-07-01** — Runhao Li, Xiaoxu Ma, Zhenyu Weng et al. — [Attribute-Prompted Kernel Hashing for Unsupervised Data-Efficient Cross-Modal Retrieval](http://arxiv.org/abs/2607.00379v1)
  <details><summary>📄 Abstract</summary>
  Unsupervised cross-modal hashing enables efficient retrieval of semantically related instances across different modalities without requiring manual semantic annotation. However, existing unsupervised methods rely heavily on large-scale image-text pairs. Collecting such data can be costly, particularly in scenarios where well-aligned pairs are scarce due to privacy and specialized constraints. More critically, existing methods tend to overfit to seen training data, restricting their generalizatio...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 2 papers

- **2026-07-06** — Enrique Adrian Villarrubia-Martin, David Muñoz-Valero, Luis Rodriguez-Benitez et al. — [Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets](http://arxiv.org/abs/2607.05179v1)
  <details><summary>📄 Abstract</summary>
  In liberalised railway systems, operators must set prices dynamically in an environment with partial observability, as they retain private information about their objectives and performance, where regulatory constraints prohibit communication or direct information exchange between competitors to prevent explicit collusion. Consequently, agents must learn to infer strategic interactions only from observable market data which presents a significant challenge for multi-agent reinforcement learning,...
  </details>

- **2026-07-05** — Chengcheng Wang, Zexin Ye — [Strategic Information Disclosure in Algorithmic Pricing](http://arxiv.org/abs/2607.04345v1)
  <details><summary>📄 Abstract</summary>
  As firms increasingly adopt AI-powered pricing algorithms, a key and urgent policy concern is how to regulate the potential algorithmic collusion. This paper approaches the regulatory question through the lens of information design and examines how different disclosure rules, committed to by a third-party intermediary, shape learning outcomes when firms delegate pricing to Q-learning algorithms under stochastic demand. We analyze three disclosure rules: no disclosure, full disclosure, and upper ...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 7 papers

- **2026-07-06** — Samira Hajizadeh — [Retroactive Chain-of-Thought (RetroCoT): Forensic Reconstruction Prompts as a Safety Diagnostic Across Model Generations](http://arxiv.org/abs/2607.04645v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in large language models is typically evaluated against direct, imperative harmful requests. We show that this alignment is highly conditioned on pragmatic register: models that refuse a direct request frequently comply when the same underlying objective is expressed through a different communicative stance. This suggests that current alignment policies are not invariant to semantic equivalence, but remain sensitive to how a request is pragmatically framed. We introduce Retroact...
  </details>

- **2026-07-06** — Ananth Eswar, Pratinav Seth, Utsav Avaiya et al. — [Faithfulness to Refusal: A Causal Audit of Neuron Selectors](http://arxiv.org/abs/2607.05355v1)
  <details><summary>📄 Abstract</summary>
  Attribution scores increasingly identify which neuron rows of a language model matter for applications such as pruning, interpretability, and editing for safety, yet whether they identify causally important rows is rarely tested directly. We address this with two paired audits built on one-shot neuron-row zeroing. We first audit selectors at the language-modeling level: attribution methods substantially outperform activation and magnitude-based baselines at identifying dispensable rows across fi...
  </details>

- **2026-07-05** — Lyndon Drake, Zandi Eberstadt — [Transplanting, inverting, and preventing a misalignment persona: method-conditional emergent misalignment in Qwen2.5](http://arxiv.org/abs/2607.04510v1)
  <details><summary>📄 Abstract</summary>
  Emergent misalignment (EM) -- the broad misbehaviour a language model acquires after fine-tuning on narrow harmful data -- is mediated in Qwen2.5 models by a latent persona direction, and that direction is causal in open weights. Transplanting it into a model that shares only pretraining with its source induces broad EM (2.83 +/- 0.26% misaligned against a random-direction floor of ~1.1%), and ablating a model's own direction roughly halves an overt inducer's broadcast (21% to 10%). The transpla...
  </details>

- **2026-07-04** — Shubhadip Nag, Srinjoy Das, Agniva Saha et al. — [MPSelectTune: Prompt-type Selection for Fine-tuning improves Concept Unlearning in LLMs](http://arxiv.org/abs/2607.03932v1)
  <details><summary>📄 Abstract</summary>
  LLMs can be conveniently adapted to a diverse set of tasks, e.g, prediction, question-answering tasks, etc, using appropriate prompts with few-shot examples. Biased or harmful concepts, e.g. gender or bio-weapons, present in pre-trained LLMs can lead to unsafe or unethical responses for many such prompts. Removing such undesirable concepts robustly across different prompt types remains a challenging problem, since existing unlearning methods typically ignore the impact of prompt variation. In th...
  </details>

- **2026-07-04** — Stefan Broecker, Mason del Rosario, Boris Selitser et al. — [The "I Don't Know" Filter: Enhancing Agentic Reliability in Function Calling](http://arxiv.org/abs/2607.04034v1)
  <details><summary>📄 Abstract</summary>
  The language models that underpin agents have seen a rapid rise in performance on function calling benchmarks. However, the metrics used in the training and evaluation of these models often encourage models to make positive claims even when the answer is uncertain, leading to hallucinations. Such hallucinations can be disastrous when language models are trusted to use function calls to make decisions in high stakes applications. To that end, we propose an agent evaluation metric that takes into ...
  </details>

- **2026-07-04** — Akira Tanaka, Yusuke Kawamoto — [Why3-py: A Tool for Formal Verification of Hypothesis Testing and Meta-Analysis in Python](http://arxiv.org/abs/2607.03951v1)
  <details><summary>📄 Abstract</summary>
  The reproducibility crisis in scientific research has received widespread recognition, thereby increasing the importance of meta-analyses that integrate statistical analyses from multiple studies. However, statistical methods often have ambiguous and implicit underlying assumptions, which can lead to their erroneous applications and interpretations. To address this issue, we propose a formal verification framework for statistical programs written in Python. Specifically, we present Why3-py, a Py...
  </details>

- **2026-07-02** — Thomas Winninger — [Fast Multi-dimensional Refusal Subspaces via RFM-AGOP](http://arxiv.org/abs/2607.02396v1)
  <details><summary>📄 Abstract</summary>
  Steering and monitoring activations in Large Language Models (LLMs) are increasingly used for both safety and interpretability. Early work assumed behaviours are encoded along single linear directions, but recent findings suggest complex behaviours, such as the refusal to answer harmful queries, live in multi-dimensional subspaces. However, existing methods for extracting these subspaces are computationally expensive, which becomes prohibitive on reasoning models who produce long reasoning trace...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-07-02** — Navaneeth Sangameswaran, Preetham S, Ashmiya Lenin — [HaloGuard 1.0: An Open Weights Constitutional Classifier for Multilingual AI Safety](http://arxiv.org/abs/2607.02079v1)
  <details><summary>📄 Abstract</summary>
  We present HaloGuard 1.0, an open-weights implementation of the constitutional-classifier paradigm for input safety. It achieves state-of-the-art performance on English and multilingual prompt-safety benchmarks at roughly one-tenth the model size of current leading open guard models. The safety constitution is the organising structure of the corpus: a natural-language constitution of 46 policies and 2,940 subcategories drives synthetic data generation, with exhaustive one-to-one paired counterfa...
  </details>

- **2026-07-02** — Mona Schirmer, Metod Jazbec, Alexander Timans et al. — [Online Safety Monitoring for LLMs](http://arxiv.org/abs/2607.02510v1)
  <details><summary>📄 Abstract</summary>
  Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with mor...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 52 papers

- **2026-07-06** — Eli N. Weinstein, David M. Blei — [Geometric Causal Models](http://arxiv.org/abs/2607.05153v1)
  <details><summary>📄 Abstract</summary>
  Scientists often seek to draw causal inferences from structured data that is not independently and identically distributed, such as spatial data, network data, or molecular data. We develop geometric causal models (GCMs), a framework for causal inference from dependent data that exploits underlying symmetries of the data generating process. For example, in spatial data, we consider processes that are symmetric under translations, or in graph data, symmetric under permutations of the nodes. We sh...
  </details>

- **2026-07-06** — Joongwon Chae, Lihui Luo, Yang Liu et al. — [ProCon: Projection-Consistency Memory for Training-Free Anomaly Detection](http://arxiv.org/abs/2607.04894v1)
  <details><summary>📄 Abstract</summary>
  Memory-based anomaly detection is attractive because it localizes defects from normal images without training a decoder or synthesizing pseudo anomalies. However, most memory methods still use the memory bank as a nearest-neighbor lookup table: a test patch is treated as normal if it has one nearby normal anchor. This hard retrieval view is vulnerable to false-normal matches and does not test whether the patch is consistently supported by a local normal neighborhood. We propose ProCon, a trainin...
  </details>

- **2026-07-06** — Kaixin Feng, Zhichao Wen, Zhaohong Liao et al. — [WinTA-GIL: Windowed Trajectory Alignment for GNSS-IMU-LiDAR Heading Refinement in Intermittent Signal Environments](http://arxiv.org/abs/2607.04879v1)
  <details><summary>📄 Abstract</summary>
  Although multi-source fusion positioning systems have achieved significant progress, accurate and reliable heading estimation remains a critical challenge due to the lack of gravitational constraints and the inherent weak observability of heading in complex environments. Most existing methodologies are specifically tailored for the startup phase, relying on a singular initial alignment to establish the heading reference. Consequently, these approaches lack the adaptability required to refine hea...
  </details>

- **2026-07-06** — Andreas Athanasopoulos, Anne-Marie George, Christos Dimitrakakis — [Probably Correct Optimal Stable Matching under Two-Sided Uncertainty](http://arxiv.org/abs/2607.04824v1)
  <details><summary>📄 Abstract</summary>
  We study a sequential learning problem for stable matchings in two-sided markets where preferences on both sides are initially unknown. We focus on a centralized setting where an algorithm matches agents at each time step and receives noisy rewards that reflect the preferences of the matched agents, following a semi-bandit feedback structure. We adopt a pure exploration perspective, aiming to efficiently identify the optimal stable matching with high probability. Our work extends prior results b...
  </details>

- **2026-07-06** — Weijian Liu, Mingzhen Li, Rui Kang et al. — [Direct Model State Migration for Elastic Training of Large Language Models](http://arxiv.org/abs/2607.04749v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) training shall adapt to dynamic resources in shared clusters to tackle the elasticity, including passive preemption and optimistic scaling. State migration across device sets is required when altering the hybrid-parallel configuration due to dynamic resources. Existing solutions rely on checkpoint-based mechanisms, which persist complete states to storage for resuming with re-assigned resources, forcing all GPUs to stall when transferring model states. Despite optimiza...
  </details>

- **2026-07-06** — Tarek Elsayed, Shiping Yang, Eunsong Koh et al. — [RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities](http://arxiv.org/abs/2607.04729v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly applied to vulnerability analysis, but existing benchmarks have not kept pace. They typically rely on small non-compilable snippets, focus on binary classification (vulnerable or not), and do not account for the risk that publicly-released datasets are part of model training corpora. We introduce RustMizan, a benchmarking framework for Rust vulnerability analysis that addresses these gaps. RustMizan contains compilable code variants at the crate, file, and function le...
  </details>

- **2026-07-06** — Pin Tang, Guoqing Wang, Xiangxuan Ren et al. — [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](http://arxiv.org/abs/2607.04637v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios. Existing VLAs typically predict and optimize 3D trajectories from 2D images. While intuitive, this 2D-to-3D prediction is inherently entangled with camera parameters, leading to limited data scalability across heterogeneous driving datasets. Moreover, directly optimizing in 3D space induces severe converg...
  </details>

- **2026-07-06** — Leran Hong, Lei Jin, Jianfeng Zhu — [Characterizing the Temporal, Emotional, and Social Patterns of Adolescent Substance Use Discussions on Reddit](http://arxiv.org/abs/2607.04566v1)
  <details><summary>📄 Abstract</summary>
  Adolescence is a critical developmental period marked by heightened emotional sensitivity, social stress, and vulnerability to substance use. However, traditional research methods provide limited access to adolescents' authentic experiences, hindering efforts to develop evidence-based prevention and intervention strategies. Social media provides a unique opportunity to observe adolescents' naturally occurring discussions about substance use, offering valuable insights into their opinions, emotio...
  </details>

- **2026-07-06** — Jerick Shi, Terry Jingcheng Zhang, Bernhard Schölkopf et al. — [When Agents Lie: Premeditation, Persistence, and Exploitation in Repeated Games](http://arxiv.org/abs/2607.05132v1)
  <details><summary>📄 Abstract</summary>
  As large language models are deployed as autonomous agents that communicate intentions before acting, a critical safety question is whether agents that publicly commit to actions will honor those commitments. We place LLM agents in repeated $n$-player games with a three-stage protocol that separates private intent, public announcement, and final action, allowing us to identify whether each deviation from a stated announcement was already planned during private deliberation. Evaluating three fron...
  </details>

- **2026-07-05** — Miguel Martínez-Antón, Justo Puerto — [Cooperation in Conic Programming with Applications to Control, Production, and Portfolio](http://arxiv.org/abs/2607.04499v1)
  <details><summary>📄 Abstract</summary>
  We introduce the class of cooperative conic games, a new family of transferable utility games whose characteristic function can be computed by solving a conic optimization problem. This framework unifies a broad range of optimization-based cooperative games within a common mathematical formulation, encompassing linear, second-order cone, semidefinite, and other convex nonlinear optimization problems admitting conic representations. Exploiting the structural properties of conic programs and conic...
  </details>

- **2026-07-05** — Jiwon Kang, Heeji Yoon, Jaewoo Jung et al. — [Transferability Between Understanding and Generation in Unified Multimodal Models](http://arxiv.org/abs/2607.04423v1)
  <details><summary>📄 Abstract</summary>
  Unified Multimodal Models (UMMs) integrate image understanding and generation within a single architecture, yet how the two tasks interact remains understudied. We investigate $\boldsymbol{\mathsf{transferability}}$ in UMMs: whether training a capability on one task improves the same capability on the other without explicit supervision. Through controlled experiments, we empirically find that transferability depends on architecture-models with fully shared transformer backbone and a unified visu...
  </details>

- **2026-07-05** — Siyu Ding, Mingchuan Ma, Jiabo Tong et al. — [Full-Stack FP4: Stable LLM Pretraining with Quantized Projections, Optimizers, and Attention](http://arxiv.org/abs/2607.04422v1)
  <details><summary>📄 Abstract</summary>
  Recent NVFP4 pretraining methods mainly target transformer linear layers, leaving optimizer states, optimizer arithmetic and attention underexplored in 4-bit pipelines. This critical gap blocks stable full-stack 4-bit pretraining, as the three core modules exhibit unique numerical failure patterns: linear layers hit hard quantization noise limits with dimension-propagated error amplification; AdamW second moments are heavy-tailed non-negative values fragile to low-precision denominators; attenti...
  </details>

- **2026-07-05** — Zhiran Yan, Gordon Elger — [Road-Aware Anomaly Segmentation with Query-Guided Polygons and CLIP in Autonomous Driving](http://arxiv.org/abs/2607.04304v1)
  <details><summary>📄 Abstract</summary>
  Traditional semantic segmentation models operate under a closed-set assumption and struggle to recognize unknown or unexpected objects-an essential capability for autonomous driving. As a result, such models often misclassify or overlook out-of-distribution (OOD) road anomalies, posing safety risks in open-world environments. We present a lightweight, postprocessing, road-aware anomaly segmentation framework that requires no retraining, no OOD data, and no auxiliary supervision. Our approach bui...
  </details>

- **2026-07-05** — Sarabeshwar Balaji, Shubham Mohanty, Akash Anil — [On Preserving Geometrical Invariance for Superpixel Image Classification using Graph Transformer](http://arxiv.org/abs/2607.04262v1)
  <details><summary>📄 Abstract</summary>
  Convolutional Neural Network (CNN) and Vision Transformer (ViT) for image classification exploit a dense grid of pixels containing redundant information. Consequently, for a larger image dataset, CNNs and ViTs face deployability challenges due to high computational complexity. Representing images as graphs of superpixels offers an efficient alternative that preserves key information while eliminating pixel-level redundancy. Graph Neural Networks (GNNs) have been utilized on such graphs to perfor...
  </details>

- **2026-07-05** — Duc-Tien Bui, Ngoc Thinh Nguyen, Hung Duy Nguyen et al. — [Integrated Graph Search and Model Predictive Control for Smooth and Efficient Path Planning in Autonomous Vehicles](http://arxiv.org/abs/2607.04259v1)
  <details><summary>📄 Abstract</summary>
  Path planning is a fundamental component of autonomous vehicles, where achieving safe, comfortable, and dynamically feasible paths while ensuring computational efficiency remains a significant challenge. This paper presents a sequential path planning framework in which a rough path obtained from graph search is explicitly exploited to guide a Model Predictive Control (MPC)-based path refinement. A rough path is first obtained via Dijkstra search on a discretized grid and is then used to construc...
  </details>

- **2026-07-05** — Dinesh Patra, Tanish Jain, Ashish R. Hota — [Robust Receding Horizon Games with Additive Uncertainty](http://arxiv.org/abs/2607.04213v1)
  <details><summary>📄 Abstract</summary>
  We study a receding horizon game in which multiple agents drive linear systems subject to additive disturbances, private state and input constraints, and shared coupling constraints. We propose a robust game-theoretic control framework that combines tube-based constraint tightening with a finite-horizon generalized Nash equilibrium problem (GNEP), equipped with a discrete algebraic Riccati equation (DARE)-based terminal cost and a decoupled positively invariant terminal set. The framework guaran...
  </details>

- **2026-07-05** — Jingfeng Wu, Yiyuan He, Minxian Xu et al. — [CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving](http://arxiv.org/abs/2607.04181v1)
  <details><summary>📄 Abstract</summary>
  Online large language model (LLM) serving has become the backbone of modern AI applications, powering diverse downstream services through shared hardware clusters. However, modern serving systems frequently encounter highly dynamic workloads characterized by severe workload skewness, where a small fraction of model instances receives the vast majority of traffic. Existing instance-level scaling mechanisms are limited by coarse-grained resource adjustment: scaling up requires the cold-start of fu...
  </details>

- **2026-07-05** — Liang Peng, Baolin Zhang, Zhaoli Guo et al. — [GPU-Accelerated Matrix-Based Hough Transform for Online Track Reconstruction in the STCF MDC](http://arxiv.org/abs/2607.04067v1)
  <details><summary>📄 Abstract</summary>
  The Super Tau-Charm Facility (STCF) is a proposed next-generation high-luminosity electron-positron collider operating at center-of-mass energies of 2-7 GeV for precision studies of tau-charm physics. Its high event rate, detector occupancy, and background level impose stringent requirements on real-time track reconstruction in MDC, particularly for low-transverse-momentum particles with strongly curved or multi-turn trajectories. To address this challenge, we develop a GPU-accelerated matrix-ba...
  </details>

- **2026-07-04** — Eduardo Abi Jaber, Elie Attal, Dimitri Sotnikov — [Stochastic control with signatures via Riccati equations on the tensor algebra](http://arxiv.org/abs/2607.03986v1)
  <details><summary>📄 Abstract</summary>
  We solve in semi-explicit form a class of non-Markovian stochastic optimal control problems with path-dependent rewards, using path signatures. We reformulate the control problem as the computation of Laplace transforms of signature functionals thanks to the Boué-Dupuis representation. Exploiting recent signature representations of such transforms on tensor algebras, we determine the value process and the optimal control through an infinite-dimensional system of Riccati equations on the extended...
  </details>

- **2026-07-04** — Yanjie Zhao, Hongjie Chen, Li Lu et al. — [Neuro-Symbolic Reasoning for Vulnerability Detection](http://arxiv.org/abs/2607.03963v1)
  <details><summary>📄 Abstract</summary>
  Ask a large language model (LLM) whether a pointer dereference is safe, and it can often produce a plausible justification for ``yes''. The difficulty is that a fluent justification is not a proof. This gap is precisely where automated vulnerability detection lives: deciding, for a given operation in source code, whether a memory safety defect such as a null dereference, use-after-free, or double free can actually occur. We trace the unreliability of LLM-based vulnerability detection to a mechan...
  </details>

- **2026-07-04** — Weiwei Chen, Yinghui He, Zhong Ye et al. — [Task-Oriented Multimodal Edge Intelligence via Integrated Sensing-Communication-Computation](http://arxiv.org/abs/2607.03907v1)
  <details><summary>📄 Abstract</summary>
  Integrated sensing, communication, and computation (ISCC) has recently emerged as a unified framework for enabling edge intelligence. However, existing ISCC designs predominantly rely on single-modal sensing, which is inherently vulnerable to occlusions, environmental uncertainties, and modality-specific failures, leading to degraded robustness in real-world deployments. This motivates the need for multi-modal ISCC, yet its design remains insufficiently explored. Compared with the single-modal c...
  </details>

- **2026-07-04** — Siru Jiang, Jian Liang, Ran He et al. — [USE: A Unified Self-Ensembling Framework for Test-Time Prompt Tuning](http://arxiv.org/abs/2607.03900v1)
  <details><summary>📄 Abstract</summary>
  Test-time adaptation (TTA) has emerged as a popular paradigm for improving the performance of vision-language models (e.g., CLIP) on downstream tasks. Among existing CLIP-based TTA methods, Test-Time Prompt Tuning (TPT) is a pioneering work that optimizes textual prompts using multiple test-time augmentations and remains a strong baseline to date. In this work, we revisit TPT and reveal that its optimization can be interpreted as implicitly learning from self-generated pseudo labels. Building on...
  </details>

- **2026-07-04** — Akash Deep, Gagan Deep — [Local Gaussian Correlation in the Tails: A Scarcity Diagnostic, an Optimal Local Bandwidth, and the Limits of Adaptivity](http://arxiv.org/abs/2607.03888v1)
  <details><summary>📄 Abstract</summary>
  Local Gaussian correlation (LGC) measures dependence locally, making it a natural tool for tail dependence and financial contagion, but its estimates degrade in the joint tails, where they are most needed. Location-adaptive bandwidths have been tried for LGC and found inferior to a single global bandwidth; we explain why, and map the regime in which adaptivity does help. First, a diagnostic: across heavy-tailed data-generating processes the parametric marginal pre-transform is inert (it changes ...
  </details>

- **2026-07-04** — Utkarsh Tiwari, Spoorthi M, Anirudh S et al. — [Advanced Topic Modeling Techniques for Categorizing Software Vulnerabilities](http://arxiv.org/abs/2607.03887v1)
  <details><summary>📄 Abstract</summary>
  The increasing complexity and frequency of software vulnerabilities demand efficient methods to analyze and prioritize threats. Traditional approaches often fail to process the vast amount of unstructured textual data effectively, highlighting the need for advanced solutions. This study leverages state-of-the-art topic modeling techniques powered by large language models (LLMs) to extract meaningful insights from the 'Threat' feature of a software vulnerability dataset. Models such as BERTopic, ...
  </details>

- **2026-07-04** — Hanqing Wang, Yongdong Chi, Jian Yang et al. — [Beyond Static Rules: Automated Discovery of Latent Vulnerabilities in Text-to-SQL](http://arxiv.org/abs/2607.03833v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) have achieved remarkable success in Text-to-SQL tasks, their deployment in real-world environments is hindered by latent reliability issues. Identifying these latent weaknesses is critical for building trustworthy database interfaces, yet current diagnostic approaches rely heavily on static, expert-defined rules, which lack the capability for systematic and automated exploration. To bridge this gap, we propose SAGE (Systematic Automated Guided Exploration), a n...
  </details>

- **2026-07-04** — Hyunsoo Kim, Jungmyung Wi, Soobin Um et al. — [Self-Improving Diffusion Classifiers with Minority Preference Optimization](http://arxiv.org/abs/2607.03770v1)
  <details><summary>📄 Abstract</summary>
  Prior studies have demonstrated that diffusion classifiers achieve robust zero-shot classification performance. However, their effectiveness is strongly tied to the pretraining data distribution: they perform well in majority, high-density regions of the data manifold, but are significantly less accurate in minority, low-density regions. Although prior works on minority sampling have focused on generating more minority-like images, what minority sampling fundamentally enables beyond generation r...
  </details>

- **2026-07-04** — Weiyang Guo, Zesheng Shi, Longhui Zhang et al. — [Agent Reinforcement Learning via Pivotal-Aware Self-Feedback Retry](http://arxiv.org/abs/2607.03702v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents have shown strong decision-making capabilities in long-horizon interactive tasks, yet they still struggle to effectively leverage failed trajectories: full retries incur high interaction costs, while experience retrieval tends to dilute critical experience signals. To address this, we propose PivoARL, a self-feedback retry framework for experience exploitation in LLM agents. PivoARL identifies the pivotal erroneous turn through structured reflection and performs...
  </details>

- **2026-07-02** — Josh Hills, Ida Caspary, Asa Cooper Stickland — [Distributed Attacks in Persistent-State AI Control](http://arxiv.org/abs/2607.02514v1)
  <details><summary>📄 Abstract</summary>
  As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt-injected agent can distribute attacks across pull requests (PRs) and time its payload for the PR with the best natural cover. To study the resulting dynamics, we introduce Iterative VibeCoding, a setting for AI control, the study of safely deploying capable but potentially untrusted AI. In Iterativ...
  </details>

- **2026-07-02** — Bohan Liu, Wenqian Ye, Guangzhi Xiong et al. — [Towards Robustness against Typographic Attack with Training-free Concept Localization](http://arxiv.org/abs/2607.02494v1)
  <details><summary>📄 Abstract</summary>
  Models trained via Contrastive Language-Image Pretraining (CLIP) serve as the foundational vision encoders for most modern Large Vision Language Models (LVLMs). Despite their widespread adoption, CLIP models exhibit a critical yet underexplored failure mode: irrelevant text appearing within images confounds visual representations, biasing them toward lexical meaning rather than true visual semantics. This robustness issue, commonly described as a Typographic Attack (TA), exposes a vulnerability ...
  </details>

- **2026-07-02** — Pedro Santos, Joel Reis, Paulo Oliveira et al. — [QuadRocket: An Aerial Robotic Testbed for Adaptive Thrust-Vector Control of Rocket-Like Vehicles](http://arxiv.org/abs/2607.02474v1)
  <details><summary>📄 Abstract</summary>
  This paper presents QuadRocket, a quadrotor-based rocket prototype that provides a low-cost, low-risk platform for validating advanced thrust-vector control strategies for launch vehicle-type systems. The prototype consists of a cylindrical main body mounted on top of a quadrotor through a universal joint, forming a flying inverted pendulum with non-negligible inertia. For control design, the coupled system is modeled as a single axisymmetric rigid body actuated by a vectored force applied along...
  </details>

- **2026-07-02** — Temitayo Olamilekan Ogunsusi, Lijun Qian, Xishuang Dong — [UA-ChatDev: Uncertainty-Aware Multi-Agent Collaboration for Reliable Software Development](http://arxiv.org/abs/2607.02186v1)
  <details><summary>📄 Abstract</summary>
  Software development is a complex task that demands cooperation among agents with diverse roles. Large language models (LLMs) have enabled autonomous multi-agent software development frameworks that leverage role-based collaboration to automate requirements analysis, coding, testing, and refinement. However, existing approaches typically assume that intermediate agent outputs are equally reliable, leaving them vulnerable to hallucination propagation, where incorrect decisions generated in early ...
  </details>

- **2026-07-02** — Chuxi Nan, Di Wu, Hongming Guo et al. — [Multimodal Fusion for Fine-Grained Classification of Breast Fibroadenoma and Phyllodes Tumors](http://arxiv.org/abs/2607.02091v1)
  <details><summary>📄 Abstract</summary>
  Breast fibroadenoma (FA) and phyllodes tumor (PT) are fibroepithelial breast lesions with highly overlapping appearances on B-mode ultrasound, making benign and borderline PT prone to being misclassified as FA and complicating preoperative decision-making. Existing computer-aided diagnosis methods commonly rely on single-modal imaging features and insufficiently exploit complementary clinical and textual information. To address this limitation, we construct the FAPT-M Dataset, a pathology-confir...
  </details>

- **2026-07-02** — Shuhan Liu, Yukai Zhao, Xing Hu et al. — [Mitigating Package Hallucinations in Large Language Models via Model Editing](http://arxiv.org/abs/2607.02052v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong capabilities in software engineering tasks, such as code generation, library recommendation, and dependency configuration. However, recent studies show that LLMs may suffer from package hallucination, where they generate non-existent or invalid package names. These hallucinations can be exploited in software supply chain attacks, as attackers may register malicious packages under hallucinated names. Therefore, mitigating package hallucination...
  </details>

- **2026-07-02** — Feng Li, Chaokun Zhang, Gong Chen — [Sparse-Aware Vector Quantization for Bandwidth-Efficient Collaborative 3D Semantic Occupancy Prediction](http://arxiv.org/abs/2607.01928v1)
  <details><summary>📄 Abstract</summary>
  Collaborative perception extends single-agent perception by enabling multiple vehicles to exchange complementary perceptual information. However, it introduces an inherent trade-off between perception gain and communication overhead, which is particularly severe for 3D semantic occupancy prediction that relies on fine-grained spatial structures. Existing methods typically compress 3D features into 2D, causing severe spatial information loss, or transmit dense 3D representations, hindering real-w...
  </details>

- **2026-07-02** — Yuanzhi Liu, Shousheng Zhao, Bo Zhou et al. — [MMBench-Live: A Continuously Evolving Benchmark for Multimodal Models](http://arxiv.org/abs/2607.01813v1)
  <details><summary>📄 Abstract</summary>
  Evaluation benchmarks are essential for assessing vision-language models (VLMs), but most multimodal benchmarks are static, making them vulnerable to temporal staleness, data contamination, and costly maintenance. We present MMBench-Live, a continuously evolving multimodal benchmark built by a multi-agent-driven automated pipeline. Our framework treats benchmark evolution as task-guided dataset construction, integrating structured benchmark specification, feedback-controlled real-time data acqui...
  </details>

- **2026-07-02** — Weili Guan, Haoyu Zhang, Meng Liu et al. — [SpaceEra++: A Unified Framework Towards 3D Spatial Reasoning in Video](http://arxiv.org/abs/2607.01784v1)
  <details><summary>📄 Abstract</summary>
  Visual-spatial understanding, defined as the ability to infer object relationships and scene layouts from visual inputs, is fundamental to downstream tasks such as robotic navigation and embodied interaction. However, pre-trained vision-language models (VLMs) remain constrained by spatial uncertainty stemming from inherently 2D observations and by the scarcity of data for 3D spatial understanding. To address these limitations, we proposed a novel framework, SpaceEra, in the NeurIPS 2025 Spotligh...
  </details>

- **2026-07-02** — Mingzhe Du, Luu Anh Tuan, Tianyi Wu et al. — [Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability Reproduction](http://arxiv.org/abs/2607.01764v1)
  <details><summary>📄 Abstract</summary>
  Repository-level vulnerability reproduction is a demanding software engineering (SE) task: an agent must inspect a codebase, infer the input grammar that reaches a vulnerable path, construct a proof-of-conceptv(PoC), and verify that the crash disappears on the patched build. Recent LLM agents can often execute these steps when the approach is correct, yet they still fail by choosing the wrong strategy. This paper argues that strategy, rather than the full action trajectory, is the right learning...
  </details>

- **2026-07-02** — Zirui Chen, Zhipeng Xue, Jiayuan Zhou et al. — [Refploit: Facilitating Exploit Construction via Code-Agent Trajectory Repair](http://arxiv.org/abs/2607.01760v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability exploits play a crucial role in assessing the downstream impact of Java library vulnerabilities. While some vulnerabilities are accompanied by disclosed exploit references, automatically reproducing such references into runnable exploits remains challenging because they are often incomplete, unstructured, or only describe partial reproduction steps. Recent code agents provide a promising way to automate this process, but our study shows that their generated exploits often appear su...
  </details>

- **2026-07-02** — Yuqiang Sun, Han Liu, Ying Li et al. — [Knowledge Over Parameters: Evolving Smart Contract Vulnerability Detection](http://arxiv.org/abs/2607.01742v1)
  <details><summary>📄 Abstract</summary>
  Smart contract vulnerabilities are predominantly logic bugs whose detection requires structured, step-by-step procedural knowledge of attack patterns and contract semantics. Existing LLM-based methods struggle to generate this knowledge automatically: prompt-based methods rely on manually crafted detection rules, while fine-tuning requires massive labeled datasets that are inherently scarce in this domain. We present EvoVuln, an automated framework that reformulates vulnerability detection as a ...
  </details>

- **2026-07-02** — Stefano Masini, Cecilia Viscardi, Michela Baccini — [Full Bayesian Reinforcement Learning via LF-IBIS](http://arxiv.org/abs/2607.01741v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) is a sequential decision-making framework in which an agent learns optimal policies through interaction with an environment by maximizing cumulative rewards. Among RL methods, Bayesian Reinforcement Learning (BRL) addresses common practical challenges related to data scarcity by leveraging prior knowledge about the environment and sequential belief updates. However, most BRL approaches require an explicit likelihood function, which is frequently inaccessible or intrac...
  </details>

- **2026-07-02** — Zhiyuan Zhang, Adeesh Desai, Jyun-Chi Hu et al. — [Imagining the Sense of Touch: Touch-Informed Manipulation via Imagined Tactile Representations](http://arxiv.org/abs/2607.01684v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing can substantially improve contact-rich robotic manipulation, yet its practical deployment remains limited by the fragility, calibration requirements, and maintenance burden of tactile hardware. This raises a fundamental question: can robots benefit from tactile knowledge without requiring tactile sensors at deployment? We present TacImag, a tactile imagination framework that predicts tactile observations from vision and proprioception and uses the generated signals to guide manip...
  </details>

- **2026-07-02** — Mingkai Zheng, Junlin Chen, Haotian Xie et al. — [SCAPE: Accurate and Efficient LLM Training with Extreme Sparse Communication](http://arxiv.org/abs/2607.01678v1)
  <details><summary>📄 Abstract</summary>
  Communication increasingly dominates the cost of Large Language Model (LLM) pre-training, especially under data-parallel and sharded training schemes, where gradient synchronization and parameter reconstruction overhead increase with model size and system scale. Existing communication-reduction methods either sparsify raw gradients, which can be unstable for modern Adam-style optimizers at high sparsity, or quantize communication, whose savings are fundamentally bounded by bit width and often in...
  </details>

- **2026-07-02** — Haotian Xie, Junlin Chen, Mingkai Zheng et al. — [DeadPool: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint](http://arxiv.org/abs/2607.01646v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art large language model (LLM) training takes tens of thousands of graphics processing units (GPUs) for months and encounters failures across the software and hardware stack. Existing fault-tolerance mechanisms either impose non-trivial overhead during failure-free execution or suffer from prolonged recovery latency, particularly under scenarios where a small subset of compute nodes experience permanent failures. %The tradeoff between failure-free overhead and recovery latency forms...
  </details>

- **2026-07-02** — Zimo Ji, Zekai Zhang, Congying Xu et al. — [Coding Agents Are Guessing: Measuring Action-Boundary Violations in Underspecified DevOps Instructions](http://arxiv.org/abs/2607.02294v1)
  <details><summary>📄 Abstract</summary>
  LLM coding agents are increasingly deployed to act autonomously on real production infrastructure. They execute shell commands, modify repositories, and call operational APIs. However, completing a task is not sufficient for safety. A wrong action can cause severe consequences. Existing agent benchmarks largely emphasize task completion, leaving open how agents behave under benign but underspecified instructions.   We present UnderSpecBench, a benchmark for measuring action-boundary violations i...
  </details>

- **2026-07-01** — Ahmet Nuri Cevik, Sinem Coleri — [Meta-Transfer Learning for mmWave Beam Alignment](http://arxiv.org/abs/2607.00860v1)
  <details><summary>📄 Abstract</summary>
  Millimeter-wave (mmWave) beam alignment plays a critical role in next-generation wireless systems, yet its efficient implementation remains challenging. Meta-learning and transfer learning have been explored to enable deep learning-based beam prediction models to rapidly adapt to unseen environments; however, existing meta-learning approaches adapt the entire network and are trained from random initialization, leading to a large number of updated parameters and a high meta-training cost, while t...
  </details>

- **2026-07-01** — Sheng Qiang, Ruiwei Chen, Yinpeng Wu et al. — [MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression](http://arxiv.org/abs/2607.00760v1)
  <details><summary>📄 Abstract</summary>
  Long-context LLM services now sustain prompts with hundreds of thousands to millions of tokens, making the key-value (KV) cache a first-order serving cost. Because the cache grows linearly with context length, it can exhaust GPU memory, force smaller batches, and reduce serving throughput. Prior KV cache compression techniques typically target only the sequence dimension or only the channel dimension, which leaves limited headroom as context windows scale. Compressing both dimensions promises hi...
  </details>

- **2026-07-01** — Emanuele Caglioti, Marco Cecchini — [Time Averages for the Vortex Model and Stroboscopic Ergodic Averages](http://arxiv.org/abs/2607.00721v1)
  <details><summary>📄 Abstract</summary>
  We consider the vortex model on the plane, focusing on the case of vortices with the same sign and, for simplicity, assuming all vortices possess equal circulation. In particular we are interested at the time average of the vorticity density, i.e. the empirical measure associated to the vortices.   We conjecture that, for a.e. initial data, the time average of the empirical density is radial.   We prove the result for N=3 vortices by exploiting the integrability of the system.   For N > 3 vortic...
  </details>

- **2026-07-01** — Yingjie Dai, Tianyang Xu, Yanglin Deng et al. — [Partial Skeleton Visibility for Action Recognition: A Constrained Field-of-View Approach](http://arxiv.org/abs/2607.00716v1)
  <details><summary>📄 Abstract</summary>
  Skeleton-based action recognition has achieved remarkable success by exploiting joint coordinates and their topological connections, yet prevailing methods overwhelmingly assume complete and clean skeleton inputs. In real-world deployments, such as egocentric vision, crowded surveillance, wearable devices, or edge robotics, limited field-of-view (FoV) frequently causes substantial joint visibility dropout, leading to severe performance degradation that existing models are largely unprepared to h...
  </details>

- **2026-07-01** — Seokhee Jin, Changhwan Sung, Sunung Mun et al. — [AdaBoosting Text Prompts for Vision-Language Models](http://arxiv.org/abs/2607.00684v1)
  <details><summary>📄 Abstract</summary>
  The classification accuracy of pretrained Vision-Language Models (VLMs) relies on the quality of the text prompts. Handcrafted templates and Large Language Model (LLM)-generated descriptions not only make predictions more interpretable, but also enable reuse of the same prompts across heterogeneous VLMs. Recent works construct task-adapted text prompts with a small number of labeled images. However, existing few-shot text prompting methods do not explicitly focus on misclassified examples during...
  </details>

- **2026-07-01** — Yifei Sun, Zemin Liu, Bryan Hooi et al. — [Multi-Label Node Classification with Label Influence Propagation](http://arxiv.org/abs/2607.00671v1)
  <details><summary>📄 Abstract</summary>
  Graphs are a complex and versatile data structure used across various domains, with possibly multi-label nodes playing a particularly crucial role. Examples include proteins in PPI networks with multiple functions and users in social or e-commerce networks exhibiting diverse interests. Tackling multi-label node classification (MLNC) on graphs has led to the development of various approaches. Some methods leverage graph neural networks (GNNs) to exploit label co-occurrence correlations, while oth...
  </details>

- **2026-07-01** — Camila C. Soares, Luis B. Castro, Antonio S. de Castro — [Scattering, bound states, and resonances in the one-dimensional Dirac equation via supersymmetric quantum mechanics](http://arxiv.org/abs/2607.00306v1)
  <details><summary>📄 Abstract</summary>
  We develop a unified treatment of scattering and discrete spectra for the one-dimensional Dirac equation with scalar and vector interactions. Under the spin-symmetry condition, the coupled first-order Dirac system maps exactly onto an effective Sturm--Liouville (Schrö\-din\-ger-like) problem for a single spinor component. This mapping provides a convenient framework for analyzing transmission, reflection, and analytic continuation. As an explicit application, we consider effective interactions o...
  </details>

- **2026-07-01** — Xiangyue Liu, Zijian Zhang, Miles Yang et al. — [Rosetta: Composable Native Multimodal Pretraining](http://arxiv.org/abs/2607.00293v1)
  <details><summary>📄 Abstract</summary>
  Achieving true artificial general intelligence requires foundation models capable of integrating new modalities without forgetting prior knowledge. However, accommodating continuous generative objectives alongside discrete understanding tasks causes severe gradient conflicts. Existing architectures, including standard Mixture-of-Experts (MoE), are highly susceptible to representation overwriting. Even structurally partitioned paradigms like Mixture-of-Transformers (MoT) remain vulnerable to cata...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 60 papers

- **2026-07-06** — Xue Qin, Simin Luan, Cong Yang et al. — [Governed Individuation: Cryptographically Decoupling an Agent's Learning from Its Authority](http://arxiv.org/abs/2607.04613v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are moving from sandboxed text generators to operators of code, data, and physical infrastructure, and they increasingly learn while deployed. This reopens a question that alignment techniques answer only probabilistically: after an agent has adapted in the field, is the running system still confined to what its operator authorised? Here we show that confinement can be guaranteed as an invariant of the agent's execution architecture rather than a probabilistic outcome of its tr...
  </details>

- **2026-07-06** — Michael Konstantinou, Florian Tambon, Mike Papadakis — [On the risk of coding before testing: An empirical study on LLM-based test generation workflow](http://arxiv.org/abs/2607.05139v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in software engineering workflows to generate both source code and test suites. This dual capability has enabled emerging development paradigms, including test-first and agentic workflows, where a single model is producing and validating implementations. However, these approaches assume that generated tests act as independent and reliable oracles - a fundamental requirement for effective software testing. In this paper, we challenge this assumpt...
  </details>

- **2026-07-06** — Babak Barazandeh, Subhabrata Majumdar, Vinay Prithyani et al. — [Localized LoRA-MoE: Block-wise Low-Rank Experts With Adaptive Routing](http://arxiv.org/abs/2607.05114v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) and high-dimensional perception networks increasingly rely on parameter-efficient fine-tuning (PEFT) to adapt to diverse operational contexts. However, standard methods like LoRA are structurally limited by a monolithic bottleneck, making them highly susceptible to gradient warfare. Interleaved multi-task streams may trigger destructive optimization feedback, collapsing adapter weights into unspecialized averages. While recent spatial partitioning methods have introd...
  </details>

- **2026-07-06** — Jean-Jacques Dubray — [Can Code Specify a System Precisely Enough to Formally Verify It?](http://arxiv.org/abs/2607.05076v1)
  <details><summary>📄 Abstract</summary>
  Formal verification is seldom applied to production software, because writing and maintaining a model has historically cost more than it returns. A companion study [1] extended SysMoBench [4] with a lower-cost alternative: specifications are graded against traces captured from the running system. It found that when large language models write the specifications, reliability is governed by the structure of the specification contract, not the language. This paper evaluates both on production softw...
  </details>

- **2026-07-06** — Saadeldine Eletter, Ruihong Zeng, Yuxia Wang et al. — [MIRAGE: Defending Long-Form RAG Against Misinformation Pollution](http://arxiv.org/abs/2607.05069v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) improves factuality by grounding LLMs in external evidence, but real-world retrieval is often polluted: semantically relevant passages may contain subtle misinformation, misleading framings, or fabrications. We introduce MIRAGE, a training-free, model-agnostic defense for long-form RAG. MIRAGE builds an NLI-based cross-document claim graph and applies a Defended-Claims Gate to either condition generation on a consistent, multi-source supported subset or to bl...
  </details>

- **2026-07-06** — Hadi Hasan, Safaa Salman, Adam Tai Abou Dargham et al. — [Toward Trustworthy Large Language Model Agents in Healthcare](http://arxiv.org/abs/2607.05055v1)
  <details><summary>📄 Abstract</summary>
  Healthcare appointment scheduling remains a persistent operational bottleneck, driven by manual coordination, fragmented legacy systems, and high administrative overhead. These inefficiencies constrain provider availability and degrade patient access to care. This paper presents CareConnect, a safety-first conversational agent for healthcare logistics automation that leverages large language model (LLM) function calling, retrieval-augmented generation (RAG), and layered deterministic safety guar...
  </details>

- **2026-07-06** — Yang Li, Feng Xue, Fan Mo et al. — [Multi-Robot Open Adaptive Teaming Across Unseen Environments, Partners, and Scales](http://arxiv.org/abs/2607.04972v1)
  <details><summary>📄 Abstract</summary>
  Deploying robot teams in the real world requires simultaneous adaptation to unseen environments, unknown partners, and varying team sizes, yet existing approaches often address these challenges in isolation under the closed-world assumption of fixed teammates. We formalize this as open adaptive multi-robot teaming and propose a hypergraphic-form game formulation that captures team-level cooperative relationships beyond pairwise interactions, providing a principled foundation for coordination str...
  </details>

- **2026-07-06** — Roie Kazoom, George Leifman, Genady Beryozkin — [FM-ChangeNet: Learning Change through Pathwise Feature Transport](http://arxiv.org/abs/2607.04750v1)
  <details><summary>📄 Abstract</summary>
  We present FM-ChangeNet, a pathwise-supervised framework for change detection that reformulates bi-temporal reasoning as continuous transport in feature space rather than static endpoint comparison. Given encoded pre and post-temporal representations, we construct intermediate latent states and learn a time-conditioned velocity field $\hat{v}_θ(z_t,t)$ along the transformation trajectory. This pathwise formulation constrains the predictor over a continuum of intermediate states, providing a dens...
  </details>

- **2026-07-06** — Argho Dey, Yunfei Yin, Swachha Ray et al. — [A Reliable Context-Aware and Temporal Planning Framework for Autonomous Driving](http://arxiv.org/abs/2607.04689v1)
  <details><summary>📄 Abstract</summary>
  Safe operation of autonomous vehicles in dense urban traffic depends on perception and planning that remain reliable when onboard sensing is degraded. In real driving conditions, camera observations are frequently corrupted by occlusion, motion blur, illumination change, and sensor noise, and when such degraded observations are aggregated indiscriminately over time, trajectory planning becomes unstable and collision risk rises for both the ego vehicle and surrounding road users. Recent Bird's-Ey...
  </details>

- **2026-07-06** — Khang Nhat Hoang Vo, Artem Vazhentsev, Artem Shelmanov et al. — [Does It Fail to See or Fail to Know? Attributing Errors in Vision-Language Models](http://arxiv.org/abs/2607.04683v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) perform well on visual question answering with high-quality images but struggle when questions require knowledge beyond what is clearly and directly visible. In such settings, uncertainty quantification should not only indicate whether the model is likely to fail but also diagnose why it is uncertain, across dimensions such as perception, entity recognition, and knowledge retrieval. While prior work has focused on individual failure modes in isolation or treated inc...
  </details>

- **2026-07-06** — Karina Halevy, Julia Mendelsohn, Chan Young Park et al. — [Evaluating Large Language Models for Antisemitic Incident Classification](http://arxiv.org/abs/2607.04890v1)
  <details><summary>📄 Abstract</summary>
  Addressing hate and violence in society requires timely detection of hateful events from public reporting, but automated identification of hateful events remains underexplored. We introduce the task of hateful event detection and investigate the ability of AI systems, specifically large language models (LLMs), to discover and classify reports of antisemitic events with fine-grained labels. We evaluate OpenAI's GPT-4o and Meta's Llama-3.2-3B-Instruct on multiple expert-annotated datasets containi...
  </details>

- **2026-07-06** — Rahul Kale, Thesath Wijayasiri, Kar Wai Fok et al. — [HilEnT: Hilbert, Entropy Transformed Image Based Malware Detection](http://arxiv.org/abs/2607.04772v1)
  <details><summary>📄 Abstract</summary>
  With the increasing threat of malware across various software related domains, malware detection and classification is critical to determine the response actions. Different strategies have been adopted to address the challenge of malware detection. With the advent of deep learning techniques, malware detection using image processing has garnered research attention. In this work, we proposed a novel malware binary to image transformation technique HilEnT based on a combination of Hilbert curve-ba...
  </details>

- **2026-07-06** — Akshay Gokhale, Mansi Dhamne — [Topological Shape Representation for Aneurysm -- Bifurcation Detection](http://arxiv.org/abs/2607.05317v1)
  <details><summary>📄 Abstract</summary>
  Automated detection of intracranial aneurysms (IAs) from CT angiography (CTA) is severely hindered by high false-positive rates. Convolutional neural networks (CNNs) rely on local pixel intensities, causing systematic confusion between saccular aneurysms and vascular bifurcations -- a problem especially acute for small lesions (<3 mm), where detection sensitivity falls below 60%. We propose a plug-and-play, topology-aware false-positive reduction framework evaluating the Smooth Euler Characteris...
  </details>

- **2026-07-06** — Sonali Santhosh, Kelly Shuhong Yu, Eugene Chang et al. — [EEG-SpikeAgent: Agentic Closed-Loop Program Synthesis for Automated EEG Spike Detection](http://arxiv.org/abs/2607.04558v1)
  <details><summary>📄 Abstract</summary>
  Automated detection of interictal epileptiform discharges in scalp electroencephalography (EEG) is clinically important, but recent high-performing deep-learning models often trade interpretability for accuracy. We introduce EEG-SpikeAgent, a closed-loop program-synthesis framework that uses a large language model (LLM) agentic system to generate signal-processing features for spike detection in scalp EEG. The system iteratively proposes one deterministic EEG feature module at a time, executes t...
  </details>

- **2026-07-05** — Henry Kabuye, Biju Issac, Jeyamohan Neera — [Agentic SABRE: An Uncertainty-Aware Neuro-Symbolic Multi-Agent Framework for Adaptive Ransomware Detection](http://arxiv.org/abs/2607.04292v1)
  <details><summary>📄 Abstract</summary>
  Ransomware has evolved into a complex, adaptive, and fast-moving adversary category in which static signatures and monolithic classifiers fail to generalise under concept drift, evasion, and behavioural polymorphism. In this paper, we present Agentic SABRE (Semantic-Behavioural Arbitration for Ransomware Evaluation), an uncertainty-aware, neuro-symbolic, multi-agent framework for adaptive ransomware detection. SABRE fuses semantic, representation-based evidence with behavioural, time-window fore...
  </details>

- **2026-07-05** — Jaber Jaber, Osama Jaber — [Auto: The AGI Compiler](http://arxiv.org/abs/2607.04542v1)
  <details><summary>📄 Abstract</summary>
  Every LLM agent run re-derives its behavior token by token on a frontier model: brilliant, expensive, slow, and unbounded. We present Auto, a compiler that records live agent behavior, measures which parts are secretly deterministic, extracts them into verified programs or distilled specialists, and emits cognition binaries: WebAssembly artifacts whose manifests carry measured guarantees and whose declared capabilities are physically enforced by the sandbox. A tiered runtime executes compiled be...
  </details>

- **2026-07-05** — Muhammad Aamir, Matthew Wijers, Sangyun Shin et al. — [A non-invasive video-based method for individual identification of wildlife using gait dynamics](http://arxiv.org/abs/2607.04518v1)
  <details><summary>📄 Abstract</summary>
  Gait is a distinctive behavioral characteristic that enables non-invasive individual identification without requiring physical interaction with an animal. While gait-based analysis has been extensively studied in humans, its application to wildlife remains limited due to environmental variability and the lack of scalable identification methods. This paper presents a fully automated, video-based pipeline for wildlife gait analysis and individual identification using deep spatiotemporal representa...
  </details>

- **2026-07-05** — Ahmed M. Sayed, Sondos A. Refaat, Abdallah M. Mostafa et al. — [LeukocyteCount: Automatic Identification and Counting for leukocytes using Deep Learning](http://arxiv.org/abs/2607.04486v1)
  <details><summary>📄 Abstract</summary>
  Diagnosing and monitoring diseases frequently involves the analysis of human biological samples, with blood analysis being pivotal. Specifically, leukocytes, or white blood cells (WBCs), are essential markers for evaluating the body's defense mechanisms against infections. Traditional methods for WBC counting and classification are labor-intensive and prone to inaccuracies, primarily due to human error. The conventional processes for blood cell analysis, especially those concerning WBCs, are bes...
  </details>

- **2026-07-05** — Lingao Xiao, Yalun Dai, Yangyu Huang et al. — [ResearchStudio-Reel: Automate the Last Mile of Research from Paper to Poster, Video, and Blog](http://arxiv.org/abs/2607.04438v1)
  <details><summary>📄 Abstract</summary>
  Research dissemination, turning a paper into a poster, a talk video, and a blog post, is still a manual last mile. Prior automation treats each artifact in isolation that each re-extract the paper from scratch, usually ship one-way renders the author cannot reopen in PowerPoint or Word, and gates quality on soft VLM-preference scores that plateau while load-bearing sections still read as empty. We argue this last mile is best built as a composition of skills: thin agent-readable contracts that s...
  </details>

- **2026-07-05** — Pavithra PM Nair, Preethu Rose Anish — [A Retrieval-Augmented Framework for Detecting and Resolving Pragmatic Ambiguities in Natural Language Requirements](http://arxiv.org/abs/2607.04436v1)
  <details><summary>📄 Abstract</summary>
  Natural language requirements (NLRs) are essential for bridging communication gaps among diverse stakeholders in software development. However, the inherent ambiguity in NLRs can pose significant challenges. In particular, some requirements may be misinterpreted due to varying contextual knowledge and domain-specific expectations of the stakeholders, a phenomenon known as pragmatic ambiguity. This paper presents an approach for detecting and resolving pragmatic ambiguities in NLRs. The approach ...
  </details>

- **2026-07-05** — ACE-Brain Team,  :, Ziyang Gong et al. — [ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI](http://arxiv.org/abs/2607.04426v1)
  <details><summary>📄 Abstract</summary>
  Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Age...
  </details>

- **2026-07-05** — Yang Zhou, Jianwen Chen, Ruipeng Wei — [Order Splitting and Liquidity Replenishment Are Jointly Necessary for the Square-Root Law of Market Impact:](http://arxiv.org/abs/2607.04280v1)
  <details><summary>📄 Abstract</summary>
  Three quantitative predictions have been advanced for the square-root law (SRL) of market impact, $I/σ_D = c\,(Q/V_D)^δ$ with $δ\approx 0.5$: GGPS ($δ=β-1$), FGLW ($δ=α-1$), and LOB walking ($δ=1/(1+γ)$). Using a minimal limit-order-book model populated by heterogeneous interacting agents and calibrated against the Tokyo Stock Exchange benchmark ($\langleδ\rangle = 0.489$~\citep{satoStrictUniversalitySquareRoot2025}), we test all three on identical simulated data and find that none matches the p...
  </details>

- **2026-07-05** — Atsushi Yano, Takuya Azumi — [Toward the Right Analytical Model and System Software for Autonomous Driving Systems: Open Problems and Research Directions](http://arxiv.org/abs/2607.04129v1)
  <details><summary>📄 Abstract</summary>
  Autonomous driving (AD) systems continuously transform multi-rate and asynchronous sensor streams into vehicle actuation through graphs of callbacks, nodes, and middleware components. In such systems, temporal correctness cannot be characterized by the execution time or deadline of an individual task alone: localization and perception chains run in parallel, fuse data with different timestamps, converge at planning, and propagate through control to actuation. Moreover, the demand for high proces...
  </details>

- **2026-07-05** — Yiqing Wang, Yixin Kang, Luyun Lin et al. — [Governing Generative AI Across Financial Institutions: An SR 26-2-Compatible Framework for Generative AI Risk Control](http://arxiv.org/abs/2607.04103v1)
  <details><summary>📄 Abstract</summary>
  The release of SR 26-2 marks a significant modernization of U.S. model risk management by replacing SR 11-7 with a more risk-based and materiality-sensitive supervisory framework. However, generative and agentic AI are excluded, creating an important governance challenge for banking organizations and other financial institutions. Although generative AI may not directly estimate credit risk or make underwriting decisions, its outputs can materially affect the surrounding control environment throu...
  </details>

- **2026-07-05** — Cangjin Qiu, Quan Zhang, Dan Jiang et al. — [UniSkip-Mamba: A Frequency-Aware State Space Model for Audio-Visual Temporal Forgery Localization](http://arxiv.org/abs/2607.04498v1)
  <details><summary>📄 Abstract</summary>
  With the proliferation of AI-generated content, sophisticated multimedia manipulation has raised critical concerns about malicious applications such as opinion manipulation and evidence fabrication, making Audio-Visual Temporal Forgery Localization (AV-TFL) an urgent research frontier. Existing TFL methods have progressed along two main paradigms: Transformer-based temporal modeling and channel-wise multimodal fusion. While these approaches capture temporal dependencies and cross-modal correlati...
  </details>

- **2026-07-05** — Venkata Sesha Sai Raj Nanduri, Akthar Hussain, Van-Hai Bui — [An End-to-End Explainable AI Framework with Automated LLM-Based Natural Language Explanation Generation for Energy Systems](http://arxiv.org/abs/2607.04374v1)
  <details><summary>📄 Abstract</summary>
  Explainable AI (XAI) is important for deploying machine learning systems in domains where stakes are very high and where transparency, trust and accountability are critical. Although black box models like deep neural networks often perform with high efficiency, interpreting their decisions remains as a difficult task. This paper proposes a reusable end-to-end XAI framework that is the combination of prediction, explanation generation, evaluation and converting these explanations into natural lan...
  </details>

- **2026-07-05** — Xian Li, Yuanhe Tian, Yang Yang et al. — [WPG-MoE: Weak-Prior-Guided Dense Mixture-of-Experts for User-Level Social Media Depression Detection](http://arxiv.org/abs/2607.04350v1)
  <details><summary>📄 Abstract</summary>
  Online social media posts provide scalable signals for early depression screening, and recent studies mainly improve pre-classification evidence through risk-post selection, symptom grounding, and clinically informed feature construction. However, these screening-stage designs often leave final decisions to a single detector, overlooking how users heterogeneously express depressive risk after screening. A monolithic classifier must average across heterogeneous users, which may dilute localized e...
  </details>

- **2026-07-05** — Rümeysa Hilal Sevinç, Bahaeddin Türkoğlu, İbrahim Kök — [Agentic IoT: Architectures, Applications, and Challenges Toward the Internet of Agents](http://arxiv.org/abs/2607.04219v1)
  <details><summary>📄 Abstract</summary>
  The integration of AI into Internet of Things (AIoT) systems has gradually transformed them from passive data collection infrastructures into intelligent systems capable of anomaly detection, predictive maintenance, classification, forecasting, and optimization. However, most existing solutions still rely on task-specific models that infer from sensor data; thus, system-wide capabilities such as real-time reasoning, adaptive planning, autonomous coordination, learning, tool use, and contextual d...
  </details>

- **2026-07-05** — Christopher Nassif, Josh F. Cooper — [Telescope: Improving Zero Shot Detection of LLM Generated Content By Measuring Token Repetition Probability](http://arxiv.org/abs/2607.04061v1)
  <details><summary>📄 Abstract</summary>
  Distinguishing Large Language Model (LLM) generated text from human writing is a critical and difficult challenge. While LLMs are trained to write like humans, we hypothesize that this training leaves an indelible mark. LLMs develop a particularly strong aversion to token repetition very early in training. This bias persists as a ''Vestigial Heuristic'' (a developmental artifact) that is activated in LLM-generated text, separating LLM from human writing. To probe this phenomenon, we introduce Te...
  </details>

- **2026-07-04** — Claudio Novelli, Luciano Floridi — [What is Left for Us? Second Scholarship Against the Degradation of Research by AI](http://arxiv.org/abs/2607.04049v1)
  <details><summary>📄 Abstract</summary>
  We argue that generative AI can degrade research by eroding the very practices through which scholarly judgement is formed and academic trust is built. As constitutive conditions for the production and validation of knowledge, these practices cannot be reduced to the final outputs of research, which is what AI so effectively simulate. Accordingly, when researchers delegate central tasks of inquiry to systems like Large Language Models, they may stop enacting these practices and, with them, lose ...
  </details>

- **2026-07-04** — Aisha Alansari, Malak Alkhorasani, Hamzah Luqman — [CrossHallu: Do Hallucination Signals Generalize Across Languages and Domains in Large Language Model's Internals?](http://arxiv.org/abs/2607.04029v1)
  <details><summary>📄 Abstract</summary>
  Recent hallucination detection techniques in large language models (LLMs) focus on directly extracting features from a model's internal representations and training a classifier on these features to detect hallucinations, demonstrating promising results. Notwithstanding this advancement, most internal-state hallucination detection techniques have been explored predominantly in English, raising the question of whether such internal signals generalize across different languages and domains. To add...
  </details>

- **2026-07-04** — Runzhi Deng, Yundi Hu, Yiming Zhong et al. — [Global Logic and Local Search: Dual-Stream Multimodal In-Context Learning for Verifiable Industrial Anomaly Detection](http://arxiv.org/abs/2607.03817v1)
  <details><summary>📄 Abstract</summary>
  Large Multimodal Models (LMMs) show strong few-shot generalization, but industrial anomaly detection remains difficult because defects are small, input resolution is limited, and textual standards are not always grounded in visual evidence. Recent optimization-based methods improve alignment through fine-tuning, but they often require many defective samples, which are unavailable in early deployment. We present Global Logic and Local Search (GLLS), a training-free framework for reference-guided ...
  </details>

- **2026-07-04** — Mohammad Abboush, Hamza Ouarrad, Andreas Rausch — [Fault Detection and Explainable Classification in Automotive HIL Validation via Denoising Autoencoders and In-Context Large Language Models](http://arxiv.org/abs/2607.03734v1)
  <details><summary>📄 Abstract</summary>
  Validating automotive software systems produces large multivariate test recordings that are still examined through effort-intensive manual review and rule-based evaluation, which detects faults beyond predefined rules poorly. Machine and deep learning have advanced fault diagnosis, yet most supervised models require large labelled datasets, generalise poorly to unseen conditions, and offer little insight into their decisions. We propose a generalisable and explainable two-phase framework for fau...
  </details>

- **2026-07-04** — Juepeng Wang, Jinyang Liu, Zhuangbin Chen et al. — [LogNLQ: Natural-Language Log Querying with Parser-Induced and Semantically Grounded Schemas](http://arxiv.org/abs/2607.03884v1)
  <details><summary>📄 Abstract</summary>
  Logs are essential for system monitoring and failure diagnoses in modern software systems, yet querying them through natural language remains an open challenge. Existing approaches either treat logs as plain text, generate queries for schema-light backends, or assume predefined relational schemas, but none addresses a fundamental obstacle: raw logs carry no executable schema over which structured queries can be defined and run. To address these limitations, we present LogNLQ, a framework that fo...
  </details>

- **2026-07-04** — Sadra Saremi — [AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative Decoding Framework with Multi-Policy Orchestration for CPU-Constrained LLM Inference](http://arxiv.org/abs/2607.03876v1)
  <details><summary>📄 Abstract</summary>
  With the rise of small quantized GGUF-based language models and their increasing use for on-device inference tasks, we have seen the growing need for an approach capable of reliably delivering these models at scale even under severe memory bandwidth constraints such as those imposed by pure CPU implementations. Fixed-depth speculative decoding has emerged as one promising technique, but in practice, it often leads to performance degradation due to either bandwidth saturation, instability, or eve...
  </details>

- **2026-07-02** — Haonan Huang — [Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics](http://arxiv.org/abs/2607.02329v1)
  <details><summary>📄 Abstract</summary>
  Autonomous-research agents have demonstrated end-to-end LLM automation in machine-learning sandboxes where execution provides calibration. Frontier physical science differs categorically: physical reasoning underlies every methodology choice, toolchains are often underdocumented, and calibration must come from external literature anchors - which unscaffolded agents cite but do not confront, hallucinating plausible, unverifiable results from internal priors. We present a pipeline that runs end-to...
  </details>

- **2026-07-02** — Ravi Kant Sharma — [Criticality-Based Guard Rail Validation for AI Agent Decisions in Autonomous Telecom Networks](http://arxiv.org/abs/2607.02210v1)
  <details><summary>📄 Abstract</summary>
  The evolution toward fully autonomous telecommunications networks (Autonomous Network Levels 4-5) requires AI/ML agents to make real-time network decisions without human intervention. However, no standardized runtime mechanism exists to intercept and validate individual inference outputs before they trigger live network state changes, creating risks of erroneous autonomous decisions. This paper proposes the Guard Rail Validation (GRV) framework, a standardizable runtime architecture for intercep...
  </details>

- **2026-07-02** — William Hackett, Peter Garraghan — [Behind the Refusal: Determining Guardrail Activation via Behavioral Monitoring](http://arxiv.org/abs/2607.02121v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) and agentic systems become integrated into real-world applications, ensuring their safety and security is critical. Guardrail systems that detect and block malicious instructions sent to and from an LLM are an essential component of AI security. However, researchers conducting black-box adversarial emulation against production AI systems often struggle to determine whether a guardrail block or an LLM rejection has occurred. This distinction is important because th...
  </details>

- **2026-07-02** — Yunhao Feng, Ruixiao Lin, Ming Wen et al. — [Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification](http://arxiv.org/abs/2607.01793v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly perform autonomous actions through external tools, leading to complex and evolving safety risks. However, existing safety testing targets expert-designed safety violations, and the corresponding outcomes are evaluated by hard-coded rules, making them costly to extend as agents evolve. To this end, we present Vera, an end-to-end automated safety testing framework that instantiates software engineering testing principles for non-deterministic agents through a three-stage, s...
  </details>

- **2026-07-02** — Juanwu Lu, Junyu Zhu, Ziran Wang — [Controllable Sim Agents with Behavior Latents](http://arxiv.org/abs/2607.02496v1)
  <details><summary>📄 Abstract</summary>
  Realistic traffic simulation requires agents that imitate logged behavior and can also be steered along interpretable axes. Such controllability enables engineers to isolate variables, reproduce specific edge cases, and test autonomous systems without real-world risk. We introduce Controllable Neural Variational Agents (CNeVA), a controllable simulated-agent framework that learns to infer a per-agent Gaussian behavior latent from per-channel discounted returns via a closed-form conjugate variati...
  </details>

- **2026-07-02** — Ziyao Wang, Maonan Wang, Yucheng He et al. — [Interpretation-Oriented Cloud Removal via Observation-Anchored Residual Flow with Geo-Contextual Alignment](http://arxiv.org/abs/2607.02471v1)
  <details><summary>📄 Abstract</summary>
  Cloud removal (CR) is essential for optical remote sensing, serving as a prerequisite for reliable downstream interpretation, such as semantic segmentation and change detection. However, existing CR approaches often prioritize visual realism while overlooking their impact on subsequent analytical tasks, leading to semantic drift and degraded downstream performance. To address this issue, we propose Geo-Anchored Cloud Removal (GACR), a unified framework that jointly ensures faithful reconstructio...
  </details>

- **2026-07-02** — Jinwei Hu, Yi Dong, Youcheng Sun et al. — [SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces](http://arxiv.org/abs/2607.02345v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based agents increasingly automate software engineering tasks through reusable skills, natural-language instruction documents that guide planning and execution. Open skill marketplaces enable users to assemble agents by co-activating community-contributed skills, but marketplace operators typically audit skills in isolation. As a result, individually benign skills may interact to redirect an agent toward unintended objectives, which we term implicit intents. Detecting ...
  </details>

- **2026-07-02** — Lev Sorokin, Chen Yang, Ken E. Friedl et al. — [Search-based Testing of Vision Language Models for In-Car Scene Understanding](http://arxiv.org/abs/2607.02300v1)
  <details><summary>📄 Abstract</summary>
  In the automotive domain, in-car scene understanding (ISU) enables the detection of safety-critical events, such as driver distraction, and supports drivers or passengers by analyzing the in-car scene and adapting the environment (e.g., ambient lighting). The industry is increasingly exploring vision-language models (VLMs) to interpret camera-recorded in-car scenes and extract information for downstream reasoning tasks. However, VLMs may generate incomplete, erroneous, or misleading scene descri...
  </details>

- **2026-07-02** — Xiangchen Cheng, Yunwei Jiang, Jianwen Sun et al. — [AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents](http://arxiv.org/abs/2607.02255v1)
  <details><summary>📄 Abstract</summary>
  Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw ...
  </details>

- **2026-07-02** — Ismail Ismail Tijjani, Ahmad Abubakar Mustapaha, Sunusi Ibrahim Muhammad et al. — [Evaluating Vision-Language Models as a Zero-Shot Learning Alternative to You Only Look Once and Optical Character Recognition for Nigerian License Plate Recognition](http://arxiv.org/abs/2607.02025v1)
  <details><summary>📄 Abstract</summary>
  License Plate Recognition (LPR) systems are critical tools in traffic monitoring, security enforcement, and urban mobility management. Traditional LPR systems often rely on a multi-stage pipeline involving object detection using You Only Look Once (YOLO) and Optical Character Recognition (OCR), which suffer from limitations such as high resource demands, poor performance in unstructured environments, and the need for large annotated datasets. This study explores the potential of Vision-Language ...
  </details>

- **2026-07-02** — Zhiren Gong, Zihao Zeng, Chau Yuen et al. — [Conditional Co-Ablation: Recovering Self-Repair Backups in Transformer Circuits](http://arxiv.org/abs/2607.01940v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability often relies on component-level interventions to discover how a model produces a behavior. This guides attribution, capability knockout, and model pruning downstream to operate by scoring each unit by the effect of ablation in isolation. Such first-order scoring is natural when component importance is additive, but becomes misleading when a transformer self-repairs: after a primary component is removed, a dormant backup can take over, muting the primary's measured ef...
  </details>

- **2026-07-02** — Yi Pan, Miao Pan, Qi Lu et al. — [VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon](http://arxiv.org/abs/2607.01804v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) foundation models have recently achieved strong progress in embodied intelligence. To reduce policy-call frequency while preserving temporal coherence, most generative policies adopt an action chunk mechanism, executing multiple future actions in an open-loop manner under a fixed action horizon. However, this "predict-then-blindly-execute" paradigm sacrifices closed-loop reactivity: in contact-rich physical interactions, even small local perturbations can rapidly amp...
  </details>

- **2026-07-02** — Jingtao Xu, Zizhuo Lin, Jianwen Sun et al. — [EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$](http://arxiv.org/abs/2607.02479v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in standard visual understanding, adapting them for active visual search in 360$^\circ$ panoramic environments exposes fundamental limitations. Specifically, standard MLLMs struggle to effectively model inherent panoramic properties, such as severe polar distortion and continuous cylindrical topologies, which significantly degrades target detection accuracy. Consequently, existing panoramic search methods a...
  </details>

- **2026-07-02** — Andrei-Marian Ungureanu, Stelian Spînu — [Real-Time Visual Intelligence on Low-Cost UAVs: A Modular Approach for Tracking, Scanning, and Navigation](http://arxiv.org/abs/2607.02298v1)
  <details><summary>📄 Abstract</summary>
  Autonomous drones are rapidly transforming modern warfare and civil applications alike. This paper presents the development of an integrated intelligent drone system designed to serve as a personal assistant. Leveraging the DJI Tello drone platform, we implemented a modular architecture that integrates three core artificial intelligence functionalities: facial detection, facial recognition, and depth estimation from monocular vision. A web-based interface enables seamless drone control and real-...
  </details>

- **2026-07-02** — Balint Turi, Archontis Politis, Parthasaarathy Sudarsanam et al. — [Speaker head orientation estimation with a single microphone array using phase spectrogram features](http://arxiv.org/abs/2607.02129v1)
  <details><summary>📄 Abstract</summary>
  Estimating a speaker's head orientation from audio can provide valuable information in smart environments, meetings, and driver monitoring. We propose a novel approach that leverages the phase component of the short-time Fourier transform from a single microphone array as input to a deep neural network combining convolutional, recurrent, and self-attention layers. Unlike prior methods that use physics-informed handcrafted features or raw waveform inputs, our approach enables robust learning from...
  </details>

- **2026-07-02** — Jiangdi Ru, Bing Li, Yage Huang et al. — [Traceable Fault Diagnosis for Battery Energy Storage Systems via Retrieval-Augmented Multi-Agent O&M Assistant](http://arxiv.org/abs/2607.01992v1)
  <details><summary>📄 Abstract</summary>
  Large-scale battery energy storage systems (BESSs) require O&M decisions that combine alarms, cell-level measurements, device topology, diagnostic tables, historical cases, and maintenance documents. Monitoring platforms can flag threshold violations, but they often cannot explain whether voltage inconsistency, resistance drift, short-circuit risk, capacity divergence, or thermal abnormality needs intervention. This digest presents a traceable BESS fault-diagnosis assistant that uses retrieval-a...
  </details>

- **2026-07-01** — Tong Xu, Xinzhe Cao, Zhihui Zhu et al. — [MolSafeEval: A Benchmark for Uncovering Safety Risks in AI-Generated Molecules](http://arxiv.org/abs/2607.00464v1)
  <details><summary>📄 Abstract</summary>
  Current molecular generation benchmarks emphasize task complexity, molecule novelty, and property alignment; they largely overlook a critical concern: the potential safety risks of AI-generated molecules. In practice, many generative models may produce molecules with toxic, reactive, or otherwise hazardous characteristics - posing hidden dangers that remain insufficiently addressed. To address this gap, we introduce MolSafeEval, a benchmark dedicated to evaluating and analyzing the safety risks ...
  </details>

- **2026-07-01** — Zijian Zhang, Rizhen Hu, Athanasios Glentis et al. — [Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training](http://arxiv.org/abs/2607.01232v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has become a central component of post-training large language models (LLMs), yet little is understood about how RL adaptation is distributed across transformer layers. Existing approaches typically update all model parameters uniformly, implicitly assuming that every layer contributes similarly to the gains obtained during RL post-training. In this work, we challenge this assumption through a systematic layer-wise study of RL training. Surprisingly, we find that trai...
  </details>

- **2026-07-01** — Arpita Nema, Hanwei Zhu, Xi Zhang et al. — [LongVQUBench: Benchmarking Long-Term Video Quality Understanding of Vision-Language Models](http://arxiv.org/abs/2607.01086v1)
  <details><summary>📄 Abstract</summary>
  The evaluation of long-term video quality understanding remains an open challenge for large vision-language models (LVLMs). Existing video quality benchmarks predominantly focus on short clips and isolated distortions, overlooking the temporal continuity, cumulative degradation, and reasoning complexity inherent in long-duration content. To address these limitations, we present LongVQUBench, a comprehensive benchmark for long-term video quality understanding. LongVQUBench contains over 1200 dive...
  </details>

- **2026-07-01** — Song-Lin Lv, Weiming Wu, Rui Zhu et al. — [Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use](http://arxiv.org/abs/2607.01084v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Model (LLM) agents demonstrate proficiency in static benchmarks, their deployment in real-world scenarios is hindered by the dynamic nature of user queries, tool sets, and interaction dynamics. To address this generalization gap, we formalize OpenAgent (Tool-Use Agent in Open-World), a problem setting characterized by distributional shifts across query, action, observation, and domain dimensions. To systematically diagnose its impact, we construct a controlled sandbox enviro...
  </details>

- **2026-07-01** — Jiaxu Leng, Jiankang Zheng, Mengjingcheng Mo et al. — [Linguistic Relative Policy Optimization for Video Anomaly Reasoning](http://arxiv.org/abs/2607.00654v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly detection (VAD) with multimodal large language models has shown strong potential, yet most existing methods still depend on large-scale annotations or expert-designed priors, limiting their ability to acquire anomaly knowledge with as little human intervention as possible. To address this, we propose Linguistic Relative Policy Optimization (LRPO), which distills group-relative semantic advantages from multiple reasoning trajectories into a linguistically expressed anomaly experienc...
  </details>

- **2026-07-01** — Sara Candussio, Francesca Padovani, Daniel Scalena et al. — ["Don't Say It!": Constraints, Compliance, and Communication when Language Models Play Taboo](http://arxiv.org/abs/2607.00601v1)
  <details><summary>📄 Abstract</summary>
  The game of Taboo requires describing a target word without using a set of forbidden words, so that other players can guess it. This deceptively simple task combines strict lexical constraints with the need for communicatively effective descriptions, making it a compelling playground for examining how LLMs navigate competing demands at inference time. We evaluate two open-weight models under conditions that intervene at progressively deeper levels of the generative process, from prompting to gen...
  </details>

- **2026-07-01** — Jihyeok Jung, Jeewu Lee, Sanghyeop Kim et al. — [EgoGapBench: Benchmarking Egocentric Action Selection in Multi-Agent Scenes](http://arxiv.org/abs/2607.00547v1)
  <details><summary>📄 Abstract</summary>
  Existing egocentric benchmarks have primarily constructed the egocentric setting from first-person-view data, which makes it difficult to evaluate egocentric perspective itself in isolation. However, understanding first-person-view input and taking an egocentric perspective are separable abilities, especially when first-person body cues are absent or when other agents are present. To isolate egocentric perspective understanding, we introduce EgoGapBench, a diagnostic benchmark for measuring acti...
  </details>

- **2026-07-01** — Chenxun Deng, Zhongde Zhang, Ye Yuan et al. — [HieDG: A Hierarchical Discrete Geometry-Guided Framework for Multi-Animal Tracking](http://arxiv.org/abs/2607.00494v1)
  <details><summary>📄 Abstract</summary>
  Multi-animal tracking (MAT) is critical for wildlife monitoring and behavioral analysis, yet remains challenging due to uniform appearance, high density, and irregular motion. Existing methods typically follow heuristic- or query-based paradigms: the former relies on handcrafted geometric associations without end-to-end optimization, whereas the latter enables joint optimization but relies heavily on appearance embeddings. In such conditions, continuous geometric embeddings can be unstable, as s...
  </details>

- **2026-07-01** — Kaysarul Anas Apurba, Md Hasibul Hasan, Mohammed Ali et al. — [MalariAI: A Label-Resilient Decoupled Framework for Universal Cell Segmentation and Explainable Stage Classification in Dense Malaria Blood Smears](http://arxiv.org/abs/2607.00385v1)
  <details><summary>📄 Abstract</summary>
  Automated malaria diagnosis from blood smear microscopy is a critical challenge in global health AI; in resource-limited settings, the scarcity of expert microscopists remains the primary bottleneck to timely and accurate diagnosis. Three compounding failure modes prevent reliable clinical deployment of existing deep learning systems. First, end-to-end detectors treat unannotated cells as background during training, producing recall figures that are strongly influenced by annotation completeness...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 71 papers

- **2026-07-06** — Cheng-Kang Chou, Ming-To Chuang, Ke-Han Lu et al. — [REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing](http://arxiv.org/abs/2607.05364v1)
  <details><summary>📄 Abstract</summary>
  Modern autoregressive ASR systems can emit timestamps as decoded tokens, enabling timestamped transcription without frame-level aligners or inference-time post-processing. We show that these generated timestamps can drift across long non-speech spans: the transcript may remain plausible, but the decoded time axis drifts away from the audio. We study this non-speech-induced timestamp drift with self-built gap and long-gap benchmarks across 15 evaluated timestamp-producing ASR and audio-language s...
  </details>

- **2026-07-06** — Wencan Jiang, Jiangning Zhang, Yong Liu — [ChatImage: Navigating Long-Form LLM Answers through Interactive Images](http://arxiv.org/abs/2607.05290v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can produce detailed answers to complex queries, but these answers are typically presented as dense linear text, which makes fine-grained inspection, navigation, and return visits difficult. We present ChatImage, a system that converts long-form LLM answers into interactive visual images. Given a textual answer, ChatImage first normalizes its content into structured visual modules, plans a visual layout, and renders a coherent image. It then applies a second groundin...
  </details>

- **2026-07-06** — Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim et al. — [Unified Audio Intelligence Without Regressing on Text Intelligence](http://arxiv.org/abs/2607.05196v1)
  <details><summary>📄 Abstract</summary>
  Audio intelligence involves understanding, reasoning about, and generating both audio and speech. In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM. Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation. This architec...
  </details>

- **2026-07-06** — Yimo Wang, Bin Kang, Shuojue Yang et al. — [DeGenseGS: Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting](http://arxiv.org/abs/2607.04761v1)
  <details><summary>📄 Abstract</summary>
  Real-time, text-promptable 4D reconstruction is indispensable for autonomous surgical interaction. Severe misalignment between semantic meaning and physical anatomy still persists, largely because existing solutions integrate Vision-Language Models into deformable fields via a rigid coupling scheme that tightly binds semantic features to geometric warping. In this paper, we propose DeGenseGS, Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting, a novel ...
  </details>

- **2026-07-06** — Gwang-Ho Na, Ho-Joong Kim, Seong-Whan Lee — [DiCE-CIR: Direct Composition Learning for Efficient Zero-Shot Composed Image Retrieval](http://arxiv.org/abs/2607.04665v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot composed image retrieval (ZS-CIR) aims to retrieve a target image from a multimodal query consisting of a reference image and an edit text describing the desired modification. Recent ZS-CIR studies have relied on projection-based methods that map a reference image into pseudo-word tokens in the text embedding space. However, such methods require additional projection and re-encoding steps, increasing training complexity, reducing efficiency, and introducing a discrepancy between traini...
  </details>

- **2026-07-06** — Haocheng Wang, Baiyu Huang, Yingjia Wan et al. — [FormalRx: Rectify and eXamine Semantic Failures in Autoformalization](http://arxiv.org/abs/2607.04655v1)
  <details><summary>📄 Abstract</summary>
  The veracious semantic alignment in autoformalization is significant for formal mathematical reasoning. However, existing evaluations provide only opaque binary verdicts or scalar scores, offering no interpretable insight into where or why translations fail. This opacity severely limits both human understanding and automated system improvement. To bridge this gap, we introduce FormalRx, a comprehensive diagnostic evaluation framework that transforms autoformalization assessment from black-box ju...
  </details>

- **2026-07-06** — Jiaqi Deng — [Wrong Before Right: Late Rescue and Interface Failure in Aligned Language Models](http://arxiv.org/abs/2607.04640v1)
  <details><summary>📄 Abstract</summary>
  We study how correctness is assembled inside aligned language models, not only whether the final answer is right. Using layer-wise difference-in-differences (DiD) trajectories over polarity-controlled minimal pairs, we identify the wrong-dip: in mid layers (25-90% depth), internal preference transiently commits to the incorrect answer and is rescued only by late-layer correction. We verify this causally with patchscope-style activation transplantation across 17 models, three families, and 64x sc...
  </details>

- **2026-07-06** — Wenqian Xing — [Attention Limited Reward Learning](http://arxiv.org/abs/2607.04590v1)
  <details><summary>📄 Abstract</summary>
  Pairwise human comparisons are a primary interface through which modern AI systems learn human preferences. RLHF and related alignment pipelines typically model such comparisons with Bradley--Terry log-odds, where choice probabilities are governed by latent reward differences. This paper examines what this assumption misses through a reduced-form model motivated by rational inattention, in which each label is generated by a low-capacity evaluation channel. The model separates two forms of ambigu...
  </details>

- **2026-07-06** — Wei Ao, Lan Wang, Vishnu Naresh Boddeti — [QSVideo: Query-Conditioned Semantic Temporal Retrieval for Video Understanding](http://arxiv.org/abs/2607.04559v1)
  <details><summary>📄 Abstract</summary>
  The performance of vision-language models (VLMs) in video understanding declines with increasing video duration, as video moments unrelated to the query confuse their language components. Multimodal retrieval has emerged as a critical component of video understanding, addressing this challenge by localizing key visual evidence. However, existing multimodal retrieval methods suffer from biased relevance estimation, limited diversity, and temporal collapse. In this paper, we propose QSVideo, a uni...
  </details>

- **2026-07-06** — Yu Li, Xiuyu Li, Mingyang Yi et al. — [Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment](http://arxiv.org/abs/2607.04728v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) post-training for large language models (LLMs) follows a efficient paradigm of "rollout then update", which inevitably results in off-policy training data. To resolve this, Importance sampling (IS) is proposed, while the token-level ratios compound over long sequences, causing severe variance exploded. A natural idea is "transferring" these off-policy token into on-policy token, so that the importance scores for correction are unnecessary. Following this idea, we prop...
  </details>

- **2026-07-06** — Qiang Liu, Taian Guo, Ruizhi Qiao et al. — [RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents](http://arxiv.org/abs/2607.04713v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning holds significant potential for training large language models (LLMs) to handle multi-turn interactive tasks. However, in long-horizon, multi-turn tasks characterized by sparse outcome rewards, directly training with outcome rewards often results in slow convergence due to the sparsity of signals and the lack of fine-grained feedback. Furthermore, the model may fail to learn successful trajectories that are not sampled during training, thereby limiting its performance. Con...
  </details>

- **2026-07-05** — Yugwon Won — [MOSAIC: Interpretable Multi-Token Cross-Attention of Biophonetic and Self-Supervised Representations for Unified Voice Anti-Spoofing](http://arxiv.org/abs/2607.04314v1)
  <details><summary>📄 Abstract</summary>
  The dominant trend in voice anti-spoofing fuses self-supervised (SSL) backbones (e.g., WavLM) with handcrafted features, yet such fusion typically lacks transparency in cue-to-layer interactions, and simple concatenation limits cross-modal learning. We propose MOSAIC (Multi-token Oriented Speech Anti-spoofing via Integrated Cross-attention), an interpretable multi-token cross-attention framework that splits a 152-dimensional biophonetic feature vector into six semantic-group query tokens (Praat,...
  </details>

- **2026-07-05** — Prakhar Godara, Pang Shiang Tay, Marcelo G. Mattar — [Beyond DSA: Conjugacy-based Comparison of Dynamical Systems](http://arxiv.org/abs/2607.04493v1)
  <details><summary>📄 Abstract</summary>
  Comparing whether two dynamical systems implement the same computation despite differences in coordinates or measurements is a central problem in neuroscience and machine learning. Dynamical Similarity Analysis [DSA; Ostrow et al., 2023] addresses this problem by aligning finite-dimensional Koopman approximations through an orthogonal similarity transformation. Here we show that orthogonal alignment is neither necessary nor sufficient for topological conjugacy: conjugate systems may require a no...
  </details>

- **2026-07-05** — Kargi Chauhan, Aditya Shah — [Covert Trait Propagation Is Representation Alignment: Mechanistic Evidence from Hidden-Channel Distillation](http://arxiv.org/abs/2607.04432v1)
  <details><summary>📄 Abstract</summary>
  A student model trained on pure uniform noise can still inherit its teacher's digit-classification ability, provided the two share initialization. Previous work proves this transfer is guaranteed when the teacher's learning rate is small enough, but does not explain where in the network the channel lives or what sets its capacity. Working in an MLP distillation setting on MNIST, we show these channels are not purely informational: geometric alignment gates access to the information the channel c...
  </details>

- **2026-07-05** — Sijin Dong, Hiroyuki Shinnou — [Uncertainty-Aware Abstention in Large Language Models with Provable Alignment Guarantees](http://arxiv.org/abs/2607.04430v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in question answering (QA) systems, yet they may generate hallucinated or misaligned responses without reliable confidence estimates. Uncertainty quantification (UQ) offers a natural basis for selective answering, where a system answers only when its prediction is deemed reliable and abstains otherwise. However, existing uncertainty scores for LLMs are often heuristic: a threshold chosen on such scores does not, by itself, provide statistica...
  </details>

- **2026-07-05** — Dhyey Yajnik, Amina Asif, Fayyaz Minhas — [The Good, the Bad, and the Brittle: Benchmarking Robustness and Generalisation of Histopathology Foundation Models](http://arxiv.org/abs/2607.04401v1)
  <details><summary>📄 Abstract</summary>
  How robust and generalisable are pathology foundation models and have their scaling limites been reached? We benchmarked twelve pathology foundation models (PFMs) and ResNet baselines using our Robustness Evaluation and Enhancement Toolbox (REET) across eleven clinically realistic perturbations and a dissimilarity-driven Non-Redundant K-fold validation (NR-Kfold) protocol. We introduce a Perturbation Performance Index (PPI) to summarise accuracy trends under controlled perturbation sweeps and an...
  </details>

- **2026-07-05** — Yuhong Luo, David M. Pennock, Xintong Wang — [Decentralized Aggregation of LLM Predictions via Wagering Mechanisms](http://arxiv.org/abs/2607.04389v1)
  <details><summary>📄 Abstract</summary>
  It is increasingly common to aggregate predictions from multiple LLMs, each with domain expertise or access to private tools and data, to improve collective prediction performance. In decentralized settings, aggregation weights need to be determined without access to models' private information and should remain robust to strategic reporting. We propose a family of advantage-aligned wagering mechanisms for LLM aggregation (WALLA), in which each model reports a prediction and a learned wager, and...
  </details>

- **2026-07-05** — Zixiang Zhou, Zhentao Yu, Yifeng Ma et al. — [Aura: Consistent Multi-Subject Video Generation via VLM-Grounded Semantic Alignment](http://arxiv.org/abs/2607.04311v1)
  <details><summary>📄 Abstract</summary>
  Subject-driven and multi-element video generation are central to controllable video synthesis, but existing methods still struggle to preserve identity consistency and model complex relationships among multiple subjects. In this paper, we propose Aura, a unified framework for high-fidelity and identity-consistent video generation. To better capture scene dynamics and subject interactions, we introduce AI director-level captions that provide dense and structured descriptions of video content. We ...
  </details>

- **2026-07-05** — Omer Tariq, Syed Muhammad Raza, Jeongbae Son — [SAD-LoRA: Spectral Alignment for Low-Rank Knowledge Distillation](http://arxiv.org/abs/2607.04306v1)
  <details><summary>📄 Abstract</summary>
  Distilling a fine-tuned teacher into a LoRA-adapted student is a standard recipe for parameter-efficient compression, but output-level KD does not explicitly control which rank-$r$ weight subspace the adapter occupies. We propose \textbf{SAD-LoRA} (\textbf{S}pectral \textbf{A}lignment \textbf{D}istillation), which selects this subspace from the data-weighted student-space reference update $\DWT\Sigx^{1/2}$ and maintains it during training via a differentiable principal-angle loss on $\colspan(B)...
  </details>

- **2026-07-05** — Gerasimos Papanikolaou-Ntais, Alexandros Kaloxylos, Athanasios Kanavos — [Agentic-V2X: Small Language Model Agents for Deadline-Aware V2X Scheduling in 5G/6G Networks](http://arxiv.org/abs/2607.04290v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are proposed as control interfaces for next-generation networks, but their latency, hallucinations, and lack of control guarantees make them unsuitable for near-real-time packet schedulers, especially in dynamic V2X environments. This paper introduces Agentic-V2X, an architecture where a small, locally deployed language model acts as a periodic non-real-time rApp-inspired policy creator, while a lightweight xApp-like controller executes validated policies at interval...
  </details>

- **2026-07-05** — Malak Ait Tamlihat, Ghizlane Ez-Zobayr, Laurent Schoeffel et al. — [Relativistic Hydrodynamics and Vorticity Dynamics in High-Energy Heavy-Ion Collisions: A Collective Flow Perspective](http://arxiv.org/abs/2607.04273v1)
  <details><summary>📄 Abstract</summary>
  This article provides a comprehensive overview of the application of relativistic fluid mechanics to describe the collective evolution of the Quark-Gluon Plasma (QGP) formed in ultra-relativistic heavy-ion collisions. We map out the chronological transformation of spatial eccentricities in the initial interaction volume into measurable anisotropic azimuthal momentum distributions, parameterized by the harmonic flow coefficients $v_n$. Utilizing multi-particle correlation techniques developed wit...
  </details>

- **2026-07-05** — Weihao Yan, Yeqiang Qian, Yi Dong et al. — [Beyond Random Sampling: Distribution-Aware Alignment for Semi-Supervised Medical Image Segmentation](http://arxiv.org/abs/2607.04249v1)
  <details><summary>📄 Abstract</summary>
  Precise medical image segmentation is crucial for clinical diagnosis and treatment planning, yet relies heavily on expensive expert annotations. Semi-supervised medical image segmentation (SSMIS) offers a cost-effective solution but typically operates under the assumption of independent and identically distributed (i.i.d.) data, defaulting to random sampling. While statistically valid at scale, this strategy suffers from severe representation bias in low-data regimes, failing to capture the hete...
  </details>

- **2026-07-05** — Waikit Xiu, Qiang Lu, Zian Wang et al. — [Beyond Scene Priors: Fine-Grained Traffic Scene Reasoning with Benchmarking and Query-Guided Small-Object Focus](http://arxiv.org/abs/2607.04149v1)
  <details><summary>📄 Abstract</summary>
  In safety-critical traffic scenarios, answering complex questions relies on minute, localized visual cues. However, standard Multimodal Large Language Models (MLLMs) tend to over-attend to backgrounds, overwhelming crucial small objects during visual-language alignment, a failure mode we term 'critical evidence dilution.' Furthermore, existing visual question answering (VQA) datasets rarely expose this flaw, as they lack large-scale, distractor-heavy evaluations that require pinpointing local ev...
  </details>

- **2026-07-05** — Junwon Moon, Seungbeom Kim, Yejin Lee et al. — [DELTA-TTS: Adapting Autoregressive Model into Diffusion Language Model for Text-to-Speech](http://arxiv.org/abs/2607.04140v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive (AR) text-to-speech (TTS) models generate discrete speech tokens sequentially, which makes inference slow and can degrade robustness by propagating local errors and hallucinations. This limitation stems from their left-to-right AR commitment: each token must be determined before future speech-token context is available. However, such ordering is not an inherent requirement for TTS, as the full input text is available before synthesis. In this paper, we introduce DELTA-TTS, a light...
  </details>

- **2026-07-05** — Zhaopeng Feng, Chen Zhi, Xuhong Zhang et al. — [SOV-CAD: Stepwise Orthographic Views Guided CAD Modeling Sequence Reconstruction](http://arxiv.org/abs/2607.04119v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing Computer-Aided Design (CAD) modeling sequences from images is crucial for preserving design intent and supporting parametric editing. However, existing methods typically generate full CAD sequences holistically, overlooking the iterative, feedback-driven nature of human design workflows. We address this limitation by introducing the rich stepwise visual supervision: at each modeling step, the system observes the target's orthographic projections, the projections of the incremental...
  </details>

- **2026-07-05** — Mohammad Arif Rasyidi, Syahirul Faiz — [Benchmarking API Drift in LLM-Generated Quantum Code Across Successive SDK Versions](http://arxiv.org/abs/2607.04072v1)
  <details><summary>📄 Abstract</summary>
  Large language models can generate plausible quantum code, but it is unclear whether they can reliably target the specific software development kit (SDK) version requested by the user. We study this problem as API drift and introduce quantum-api-drift, a benchmark for measuring version fidelity, defined here as execution success on the requested SDK version, cross-version compatibility, failure modes, and documentation-guided repair in LLM-generated quantum SDK code. We instantiate the benchmark...
  </details>

- **2026-07-05** — Chee Heng Tan, Zhuoyi Lin, Mehul Motani et al. — [On the effectiveness of reward functions in reinforcement learning for confidence calibration of large language models](http://arxiv.org/abs/2607.04332v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we consider the setting where large language models (LLMs) are trained using reinforcement learning (RL) to simultaneously improve reasoning accuracy and verbalize its confidence. Our reward scheme uses two functions for rewarding confidence verbalized by the LLM: one when the LLM is correct and a different one when the LLM is incorrect. With a poorly designed reward scheme, the LLM may be incentivized to answer incorrectly so that it can be confident that its answer is indeed inc...
  </details>

- **2026-07-04** — Wei Liu, Eric Krokos, Kirsten Whitley et al. — [Scalable Semantic Steering of Embedding Projections](http://arxiv.org/abs/2607.03978v1)
  <details><summary>📄 Abstract</summary>
  Low-dimensional projections support interactive visual analysis of high-dimensional data embeddings, but their structure often does not align with analyst-defined semantic relationships. Recent LLM-augmented semantic steering methods address this gap by externalizing analyst intent from user-defined groups of seed examples, but they propagate intent through per-item LLM reasoning, causing LLM calls and cost to grow linearly with collection size. We propose a scalable semantic steering method tha...
  </details>

- **2026-07-04** — Weibin Li, Wendu Li, Yushan You et al. — [NeuroOnline: Bridging Pretraining and Online Adaptation for EEG Foundation Models](http://arxiv.org/abs/2607.03925v1)
  <details><summary>📄 Abstract</summary>
  EEG foundation models have shown strong potential in learning generalized representations across subjects and tasks. However, most existing approaches follow a pretraining-static deployment paradigm, which suffers from two key limitations: (1) misalignment between pretraining objectives and downstream tasks, and (2) limited adaptability to distribution shifts in online settings. We propose Online Neural Adaptation (NeuroOnline), a unified framework that enables continuous adaptation in online sc...
  </details>

- **2026-07-04** — Jiayi Guan, Tianle Zhang, Li Shen et al. — [CDCP: Conditional Diffusion Model with Contextual Prompts for Multi-task Offline Safe Reinforcement Learning](http://arxiv.org/abs/2607.03903v1)
  <details><summary>📄 Abstract</summary>
  Multi-task offline safe reinforcement learning (RL) promises to learn a shared optimal safe policy from offline data across multiple tasks. This paradigm provides an effective means for the widespread application of RL in multi-task scenarios with high risk and interaction costs. However, the triple challenges of multi-tasking, safety constraints, and out-of-distribution (OOD) actions pose a significant hurdle for existing methods to ensure safety while maximizing reward returns. In this work, w...
  </details>

- **2026-07-04** — Xiangyu Shi, Ruoxi Yang, Wei Tao et al. — [From Region Arrival to Instance-Level Grounding in Vision-and-Language Navigation](http://arxiv.org/abs/2607.03792v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-Language Navigation (VLN) agents may satisfy conventional success criteria while still failing to establish reliable object-level grounding, because current evaluation protocols mainly reward stopping within a 3-meter radius and largely ignore the agent's final orientation and target visibility. We formalize this limitation as the Last-3-Meter Grounding Gap and introduce three instance-centric metrics to quantify proximity precision, target visibility, and final-view grounding. To mit...
  </details>

- **2026-07-04** — Dickens Kwesiga, Nishu Choudhary, Angshuman Guin et al. — [Explainable Reinforcement Learning for Adaptive Traffic Signal Control](http://arxiv.org/abs/2607.03703v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) has emerged as a powerful paradigm for adaptive traffic signal control. However, in safety-critical infrastructure like traffic control, the opaque, black-box nature of deep RL models poses challenges for transportation agency acceptance, regulatory compliance, operational trust, troubleshooting, and fine-tuning. To bridge this gap between high-performance optimization and human-comprehensible interpretability, this effort introduces a novel, explainable entity centri...
  </details>

- **2026-07-02** — Dengyang Jiang, Mengmeng Wang, Harry Yang et al. — [From SRA to Self-Flow: Data Augmentation or Self-Supervision?](http://arxiv.org/abs/2607.02508v1)
  <details><summary>📄 Abstract</summary>
  Representation alignment has become an effective way to accelerate diffusion transformer training and improve generation quality. Recent self-alignment methods, such as SRA and Self-Flow, further remove the dependency on external pretrained encoders by constructing alignment within the diffusion model itself. However, the mechanism behind the improvement from SRA to Self-Flow, dual-time scheduling, remains under-examined: Self-Flow attributes its gain to interactions between tokens at different ...
  </details>

- **2026-07-02** — Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah et al. — [What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates](http://arxiv.org/abs/2607.02507v1)
  <details><summary>📄 Abstract</summary>
  LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an off-the-record (OTR) channel elicited under the same condition. We introduce a dual-channel debate framework in which agents produce public utterances that enter the shared history alongside OTR resp...
  </details>

- **2026-07-02** — Song Tang, Shuming Hu, Xincheng Shuai et al. — [Seek to Segment: Active Perception for Panoramic Referring Segmentation](http://arxiv.org/abs/2607.02497v1)
  <details><summary>📄 Abstract</summary>
  Existing referring segmentation models passively process static images captured from fixed perspectives, limiting their applicability in Embodied AI, where agents must perform active perception in the continuous 360$^\circ$ environments. To bridge this gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS). In this setting, an agent is required to adjust its viewing direction ($Δθ, Δφ$) to explore the 360$^\circ$ environment, seeking the object specified by a user instruc...
  </details>

- **2026-07-02** — Kaustubh Kapil, Kishor P. Upla — [Transformer Geometry Observatory TGO-II: Representational Similarity Observatory](http://arxiv.org/abs/2607.02386v1)
  <details><summary>📄 Abstract</summary>
  While Vision Transformers have achieved remarkable success across computer vision and language applications, the geometric evolution of their internal representations throughout training remains insufficiently understood. Existing analyses primarily focus on attention mechanisms and downstream performance, leaving the evolution of representation geometry largely unexplored. In this work, we present Transformer Geometry Observatory-II (TGO-II), a representation geometry analysis framework designe...
  </details>

- **2026-07-02** — Kim Zierahn, Cristina Cachero, Anna Korhonen et al. — [Personality Without Persons? A Psychometric Critique of Big Five Testing in Large Language Models](http://arxiv.org/abs/2607.02325v1)
  <details><summary>📄 Abstract</summary>
  Human personality inventories are increasingly used to characterize large language models (LLMs), compare systems, and inform downstream governance claims. Yet, these inventories were developed and validated for humans, and it remains unclear whether they apply to LLMs. We present a systematic psychometric evaluation of Big Five personality measurements in LLMs. We ask three research questions: Do Big Five inventories a) appropriately describe LLMs, b) capture inter-individual differences across...
  </details>

- **2026-07-02** — Zijun Li, Yimin Zhou, Jia Sun et al. — [DetailAnywhere: Fashion Detail Generation via Cross-Modal Feature Alignment Distillation](http://arxiv.org/abs/2607.02220v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based generative AI has achieved remarkable success in e-commerce applications such as virtual try-on, poster generation, and product background synthesis. However, when making online purchasing decisions for apparel, consumers also desire the freedom to examine specific detail regions of interest, such as collars, cuffs, and fabric textures, yet existing methods have not explicitly studied this setting. We therefore formalize a new, non-template task: Fashion Detail Generation with fo...
  </details>

- **2026-07-02** — Zhanglin Shangguan, Wei Xiao, Bo Yang et al. — [Reference-Governed Distributed Safe Gradient Flow for Safe Optimal Output Agreement of Multi-Agent Systems](http://arxiv.org/abs/2607.02192v1)
  <details><summary>📄 Abstract</summary>
  This paper studies safe optimal output agreement for nonlinear multi-agent systems with output safety constraints. Existing safe feedback optimization methods often implement gradient-flow dynamics directly through the plant input, which may require high-order control barrier functions (HOCBFs). The resulting derivative-chain design is tuning-sensitive and can introduce additional equilibrium conditions that alter the steady-state optimal solution. We propose a reference-governed two-layer archi...
  </details>

- **2026-07-02** — Susmit Agrawal, Matthias Bethge, Matthias Kümmerer — [DeepGaze3.5-VL: Modeling Scanpaths via Autoregressive Token Prediction](http://arxiv.org/abs/2607.02083v1)
  <details><summary>📄 Abstract</summary>
  Understanding human visual attention on a scene over time has applications in domains such as interface design and inferring cognitive states. Modeling visual scanpaths has historically relied on specialized architectures with hand-crafted priors. While these architectures can model fixation sequences, their rigid structural biases restrict easy extendability and flexible conditioning. For instance, integrating task-specific instructions or adapting to distinct viewer identities requires custom,...
  </details>

- **2026-07-02** — Wenda Wang, Yihan Tong, Yuwei Hu et al. — [MolSight: A Graph-Aware Vision-Language Model for Unified Chemical Image Understanding](http://arxiv.org/abs/2607.01982v1)
  <details><summary>📄 Abstract</summary>
  Using molecular large language models (LLMs) as a unified framework for understanding molecular structures and functions is emerging as a new trend in tasks such as molecular design and drug discovery. However, these models struggle to fully capture the visual representation of molecular structures, limiting their potential. While existing molecular vision-language models (VLMs) show promise, they still face challenges in structural alignment and lack the necessary topological modeling for accur...
  </details>

- **2026-07-02** — Jan Drchal — [Object Aligner: A Configurable JSON Schema Similarity Score for Graphs, Applied to LLM Prompt Optimization](http://arxiv.org/abs/2607.01972v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are often asked to produce JSON conforming to a fixed schema, powering information extraction, tool calling, agentic planning, and knowledge-graph construction. Measuring how closely an output matches a gold reference is essential yet surprisingly hard: exact match is brittle, text similarity ignores structure, and an LLM judge is expensive, opaque, and non-deterministic. We address this with Object Aligner (OA), an open-source Python library that scores two JSON obj...
  </details>

- **2026-07-02** — Jinxi Li, Tianyi Zhang, Yafei Yang et al. — [NeoMap: Training-free Novel-View Synthesis from Single Images and Videos](http://arxiv.org/abs/2607.01962v1)
  <details><summary>📄 Abstract</summary>
  We study the challenging problem of novel view video synthesis from single images or monocular videos. Existing methods, which operate under the assumption that pre-trained video models lack native novel view synthesis capability and enforce view alignment via camera conditioning, task-specific fine-tuning, or stepwise hard denoising guidance, often suffer from artifacts and compromised global scene consistency. In this paper, we introduce NeoMap, a novel training-free framework designed to loca...
  </details>

- **2026-07-02** — Bingcong Yan, Chunlei Li, Jingliang Hu et al. — [Towards Real-World Ultrasound Understanding: Large Vision-Language Models from Multi-Image Examinations with Long-Form Reports](http://arxiv.org/abs/2607.01908v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have achieved strong performance across many medical imaging tasks, yet their application to ultrasound remains limited due to its inherent complexity and variability. In this work, we revisit what is truly needed to enable real-world ultrasound understanding. Instead of introducing complex architectures or elaborate training strategies, we show that data scale and clinically faithful data alignment are the key factors. We construct a large-scale dataset of 1...
  </details>

- **2026-07-02** — Yidan Xu, Xiangmin Han, Rundong Xue et al. — [SABER: A Semantic-Aligned Brain Network Analysis Framework via Multi-scale Hypergraphs](http://arxiv.org/abs/2607.01901v1)
  <details><summary>📄 Abstract</summary>
  Effective brain disease diagnosis requires the synergy of brain connectivity patterns and high-level semantic knowledge. Existing methods, however, largely treat semantics from large language models (LLMs) as auxiliary features or supervision, limiting their direct role in decision-making and constraining classification stability and robustness. To overcome this, we propose a semantic-aligned brain network framework that actively integrates LLM-derived semantics into the prediction process. Spec...
  </details>

- **2026-07-02** — Fengchen He, Hao Xu, Dayang Zhao et al. — [FoundDP: Revisiting Weak Disparity Observability in Dual-Pixel Depth Estimation](http://arxiv.org/abs/2607.01900v1)
  <details><summary>📄 Abstract</summary>
  Dual-pixel (DP) imaging enables metric depth estimation from a single camera using sub-aperture disparity. However, the extremely small effective baseline limits disparity observability, leading to structural degradation and depth failure in textureless, low-contrast, or downsampled regions. Existing DP-based methods rely primarily on local disparity cues and therefore become unreliable when disparity signals are weak or ambiguous. To address this limitation, we propose \emph{FoundDP}, a unified...
  </details>

- **2026-07-02** — Qing Yu, Kent Fujiwara — [InterCMDM: Block-Causal Diffusion for Autoregressive Human Interaction Generation](http://arxiv.org/abs/2607.01743v1)
  <details><summary>📄 Abstract</summary>
  Text-conditioned human interaction generation must capture both long-range temporal causality within each individual and tightly coupled coordination between partners. Existing interaction diffusion models typically denoise full sequences using bidirectional attention, which obscures causality and hinders streaming and long-horizon generation. Autoregressive alternatives enforce causality but often suffer from temporal drift, leading to coordination degradation and unstable interaction dynamics ...
  </details>

- **2026-07-02** — Hexian Ni, Tao Lu, Yinghao Cai — [CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning](http://arxiv.org/abs/2607.01721v1)
  <details><summary>📄 Abstract</summary>
  Reward design remains a central challenge in reinforcement learning (RL). Hand-crafted rewards are often difficult to specify and may lead to suboptimal policies, while learned rewards from preferences can suffer from inefficiency and unstable training. Inspired by the dual nature of human learning explored in cognitive science, we decompose rewards into two complementary components: Formal Rewards (FR), explicitly designed based on task knowledge, and Residual Rewards (RR), learned from observa...
  </details>

- **2026-07-02** — Xudong Wu, Jian Qian, Pangpang Liu et al. — [Distributionally Robust Listwise Preference Optimization](http://arxiv.org/abs/2607.01715v1)
  <details><summary>📄 Abstract</summary>
  Existing robust preference optimization for language-model alignment mainly studies pairwise supervision and places robustness at the dataset, prompt, or preference-pair level. We instead study listwise preference optimization under ranking-label uncertainty: given a prompt and a candidate list, the observed ranking over that list may be ambiguous due to annotator inconsistency, near-ties, lossy rankwise feedback, or reward-model noise. We propose a pointwise total-variation robust Plackett--Luc...
  </details>

- **2026-07-02** — Xuanhua He, Jiaxin Xie, Mingzhe Zheng et al. — [ICDepth: Taming Video Diffusion Models for Video Depth Estimation via In-Context Conditioning](http://arxiv.org/abs/2607.01677v1)
  <details><summary>📄 Abstract</summary>
  Monocular video depth estimation requires temporal consistency, geometric accuracy, and generalization across diverse scenarios, yet existing methods struggle to achieve all three simultaneously. Discriminative models excel at per-frame accuracy but suffer from temporal drift due to limited context windows, while generative methods improve consistency and generalization at the cost of extensive training data (10M+ samples) and lack of geometric precision. In response to these issues, we introduc...
  </details>

- **2026-07-02** — Chen Zhao, Jiajun Ma, Qilong Huang et al. — [Temporal and Cross-Modal Alignment for Enhanced Audiovisual Video Captioning](http://arxiv.org/abs/2607.01667v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) have advanced video understanding, achieving precise temporal and cross-modal alignment in audiovisual video captioning remains a formidable challenge. Most existing approaches suffer from modality detachment and temporal incoherence, failing to accurately bind auditory events to visual entities or capture complex causal dynamics. To address these deficiencies, we propose TCA-Captioner, a framework specifically engineered to enhance Temporal and Cro...
  </details>

- **2026-07-02** — Yuan Yuan — [The Dual Nature of LLM Persona: Aggregated Tendencies and Frame-Dependent Geometry](http://arxiv.org/abs/2607.02368v1)
  <details><summary>📄 Abstract</summary>
  Evaluations of LLM personas via psychometric questionnaires typically rely on aggregate scores, discarding within-instance correlation structure. We test whether this geometric structure is intrinsic or frame-dependent. Constructing within-instance correlation matrices from IPIP-50 responses, we analyze geometry on SPD manifolds under manipulated question orderings in GPT-4o simulating American and Chinese-American personas. We find that persona expression comprises two dissociable components: a...
  </details>

- **2026-07-01** — William Philipp, Finn Fassbender, Thorsten Langer et al. — [Clinician-Level Agreement Without Clinical Caution: LLM Evaluator Limits in Medical AI Benchmarking](http://arxiv.org/abs/2607.01103v1)
  <details><summary>📄 Abstract</summary>
  Open-response evaluation provides stronger clinical validity than multiple-choice benchmarks but creates a scoring bottleneck that motivates automated LLM-asa-Judge approaches. Whether such evaluators replicate clinical calibration and caution, however, remains untested. We introduce MedQADE, the first standardised open-response clinical benchmark for German, a major clinical language lacking native evaluation infrastructure, comprising 3,800 items annotated by ten practising physicians and nine...
  </details>

- **2026-07-01** — Soosung Kim, Minjae Park, Eui-Young Chung et al. — [GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache](http://arxiv.org/abs/2607.01065v1)
  <details><summary>📄 Abstract</summary>
  The deployment of Large Language Models (LLMs) with extended context windows is increasingly constrained by the linear growth of Key-Value (KV) cache memory. Vector Quantization (VQ), particularly Residual Quantization (RQ), is a promising approach for pushing KV cache storage toward the sub-1-bit regime by progressively encoding residuals with small codebooks. However, most VQ methods still rely on standard $\ell_2$ $K$-means as the core codebook-learning primitive. We identify a subtle high-di...
  </details>

- **2026-07-01** — Ali Vardasbi, Gustavo Penha, Enrico Palumbo et al. — [As It Was: Aligning LLM Search Evaluation with Historical User Preferences](http://arxiv.org/abs/2607.01040v1)
  <details><summary>📄 Abstract</summary>
  Large-scale search systems evolve faster than human quality assurance can scale, especially for long-tail intents and multilingual queries. LLM-as-a-judge approaches provide a scalable alternative for evaluating the relevance of search engine result pages (SERPs), but judgments based solely on semantic similarity or world knowledge can drift from actual user preferences, particularly for ambiguous queries. We introduce a behavior-grounded LLM judge that augments each SERP item with a lightweight...
  </details>

- **2026-07-01** — Subhadeep Pal, Shashwat Sourav, Tirthankar Ghosal et al. — [Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination](http://arxiv.org/abs/2607.00924v1)
  <details><summary>📄 Abstract</summary>
  Accelerating materials discovery requires AI systems that can generate scientifically valid hypotheses through multi-step, domain-grounded reasoning. Standard large language models often produce fluent but weakly traceable responses to open-ended materials design problems, making it difficult to determine whether final answers are supported by coherent intermediate reasoning. We develop Graph-PRefLexOR, a family of graph-native reasoning models fine-tuned with Group Relative Policy Optimization ...
  </details>

- **2026-07-01** — Fei Wang, Chao Xue, Taoran Liu et al. — [Beyond Activation Alignment:The Alignment-Diversity Tradeoff in Task-Aware LLM Quantization](http://arxiv.org/abs/2607.00908v1)
  <details><summary>📄 Abstract</summary>
  Mixed-precision quantization (MPQ) has become a key technique for deploying large language models under stringent memory and compute constraints. We first identify a phenomenon that we term the Perplexity Illusion: layers ranked as important by perplexity-based sensitivity show little rank correlation with those that are most influential for complex reasoning performance, with Kendall $τ\approx 0$ in our analysis. We further reveal an Alignment-Diversity Tradeoff: using only target-task calibrat...
  </details>

- **2026-07-01** — Zhihan Zeng, Amir Hussain, Yue Xiu et al. — [Geometry-Aware Cross-Height Channel Knowledge Map Prediction for UAV-Assisted Communications With Uncertainty-Guided 3D Sensing](http://arxiv.org/abs/2607.00887v1)
  <details><summary>📄 Abstract</summary>
  Low-altitude Unmanned Aerial Vehicles (UAVs) often need to infer channel knowledge across a range of heights from only sparse observations collected at a few altitude layers. To address this challenge, this paper studies height-conditioned cross-height channel knowledge map (CKM) prediction for UAV-assisted communications in geometry-rich urban environments. We develop a geometry-aware conditional prediction framework that combines urban scene priors, sparse multi-altitude observations, and targ...
  </details>

- **2026-07-01** — Ruixin Li, Jin Liu, Yuling Shi et al. — [Mirror-Fusion Attention for Reflection-Aware Self-Supervised Representation Learning](http://arxiv.org/abs/2607.00850v1)
  <details><summary>📄 Abstract</summary>
  Most self-supervised learning (SSL) methods encourage invariance across augmentations, but strict flip invariance can suppress informative left--right correspondences in approximately bilateral data such as medical images and human faces. We propose Mirror-Fusion-Augmented Self-Supervised Learning (MFASSL), a Vision Transformer framework that injects a soft reflection prior into standard SSL without redesigning the backbone. MFASSL constructs mirror-paired views aligned to an estimated symmetry ...
  </details>

- **2026-07-01** — Xianru Chen, Yukai Huang, Mingxiang Chen et al. — [MSQA: A Natively Sourced Multilingual and Multicultural SimpleQA Benchmark](http://arxiv.org/abs/2607.00724v1)
  <details><summary>📄 Abstract</summary>
  Multilingual fluency often invites a stronger assumption: a model that can speak a user's language must also understand the culture encoded by that language. We call this the Illusion of Cultural Alignment. To test this assumption directly, we introduce MSQA, a benchmark of 1,064 natively sourced questions across 11 language groups, five cultural dimensions, and three difficulty tiers. Unlike translated benchmarks, MSQA targets locally grounded knowledge and reduces shortcuts from English-centri...
  </details>

- **2026-07-01** — Ronghan Chen, Yandan Yang, Zuojin Tang et al. — [ABot-M0.5: Unified Mobility-and-Manipulation World Action Model](http://arxiv.org/abs/2607.00678v1)
  <details><summary>📄 Abstract</summary>
  Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result,...
  </details>

- **2026-07-01** — Tejas Pradeep Shirodkar — [Measuring Dead Directions: Decomposing and Classifying Singular Structure off Canonical Alignment](http://arxiv.org/abs/2607.00603v1)
  <details><summary>📄 Abstract</summary>
  We give a descent-free, alignment-free measurement of singular structure on trained networks. At a single frozen checkpoint the read recovers the order $k$ of each dead direction from the directional-Fisher rate, the master invariant from which the per-direction learning coefficient $1/(2k)$ follows exactly, in whatever basis the optimizer left. The same read classifies each direction, separating a genuine singularity, whose order the architecture fixes, from a flat gauge symmetry; the direction...
  </details>

- **2026-07-01** — Mattia D'Urso, Christian Sormann, Mattia Rossi et al. — [EPO: Boosting 3D Foundation Models with Edge-based Pose Optimization](http://arxiv.org/abs/2607.00579v1)
  <details><summary>📄 Abstract</summary>
  We introduce \textbf{Edge-based Pose Optimization (EPO)}, a trackless geometric optimization framework specifically designed to boost the Structure-from-Motion reconstructions generated by 3D Foundation Models. These models achieve rapid inference by bypassing the time-consuming feature extraction and matching stages of traditional pipelines, where explicit correspondences between each 3D point and multiple images, referred to as tracks, are established. However, their geometric accuracy current...
  </details>

- **2026-07-01** — Zijian Dong, Yi Lin, Ji Fang et al. — [BrainFIBRE: A Foundation Model via Information Decomposition for Brain Microstructure](http://arxiv.org/abs/2607.00573v1)
  <details><summary>📄 Abstract</summary>
  Diffusion MRI probes brain microstructure with particular sensitivity to early cerebrovascular and neurodegenerative changes. Neurite Orientation Dispersion and Density Imaging (NODDI) decomposes the diffusion signal into three biophysically interpretable maps: neurite density index (NDI), orientation dispersion index (ODI), and free water fraction (FWF), capturing neurite packing, fiber coherence, and extracellular fluid. These 3D maps offer a rich substrate for transferable microstructural rep...
  </details>

- **2026-07-01** — Yuchen Zhang, Luanyuan Dai, Yiwei Wang et al. — [Robust 3D Alignment of Generative Reconstructions via Partial Monocular Observations](http://arxiv.org/abs/2607.00498v1)
  <details><summary>📄 Abstract</summary>
  Aligning generative 3D reconstructions with partial monocular observations is a critical but under-explored challenge in computer vision. This task is inherently ill-posed due to severe asymmetries between noisy, sparse monocular inputs and dense generative priors, whose scale ambiguity and geometric hallucinations, combined with the lack of initial overlap, render traditional registration pipelines ineffective. To resolve these issues, we propose a training-free and interpretable geometric alig...
  </details>

- **2026-07-01** — Anindya Sarkar, Nasik Muhammad Nafi, Isaac Lyngaas et al. — [PAPA: Online Personalized Active Preference Alignment](http://arxiv.org/abs/2607.00486v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models are highly effective at modeling complex data distributions, including images and text. However, in applications like personalized recommender systems, the objective often shifts to modeling specific regions of the distribution that maximize user preferences-initially unknown but gradually uncovered through interactive feedback. This can naturally be framed as a reinforcement learning problem, where the goal is to fine-tune a diffusion model to maximize a reward function based o...
  </details>

- **2026-07-01** — Ji Ha Jang, Hayeon Kim, Chulwon Lee et al. — [HyFL-CLIP: Hyperbolic Fine-Tuning of CLIP for Robust Long-Context Understanding](http://arxiv.org/abs/2607.00428v1)
  <details><summary>📄 Abstract</summary>
  CLIP (Contrastive Language-Image Pre-training) has become a de facto paradigm for image-text alignment, but it struggles with long-context descriptions (>77 tokens) due to absolute positional encoding and pretraining on short captions. In long contexts, sentences are often reordered, summarized, or partially omitted. Although prior works extend CLIP with longer positional encodings, they often suffer from degraded image-text alignment under such text perturbations. We attribute this limitation t...
  </details>

- **2026-07-01** — Jaeho Han, Jisoo Yang, Hyeondong Woo et al. — [Selective Test-Time Debiasing for CLIP via Reward Gating](http://arxiv.org/abs/2607.00423v1)
  <details><summary>📄 Abstract</summary>
  Vision language models (VLMs) demonstrate strong zero-shot performance, but often perpetuate social stereotypes in person-centric queries, yielding skewed demographic distributions. Current debiasing methods apply uniform bias corrections across all input queries regardless of their bias sensitivity, creating a fundamental fairness--utility trade-off. Strong debiasing distorts semantically meaningful information in bias-insensitive queries, while weak debiasing fails to mitigate stereotypes in b...
  </details>

- **2026-07-01** — Saad Wazir, Patrick Dominique Vibild, Dinh Phu Tran et al. — [MedCAGD: Context-Aware Gated Decoder for Efficient Medical Image Segmentation](http://arxiv.org/abs/2607.00409v1)
  <details><summary>📄 Abstract</summary>
  Medical image segmentation relies on the ability of encoder-decoder architectures to translate rich feature representations into accurate pixel-level predictions under challenging conditions such as low contrast, structural ambiguity, and scale variability. While recent advances in large-scale pretraining and transformer-based encoders have substantially improved feature extraction, segmentation accuracy remains constrained by decoder design, particularly in terms of cross-scale alignment, conte...
  </details>

- **2026-07-01** — Xingran Guo, Tiaojie Xiao, Jie Liu et al. — [Holographic Quantum Transformer: A Generalist Neuro-Symbolic Architecture for Solving Frustrated Systems via Generative Attention](http://arxiv.org/abs/2607.00398v1)
  <details><summary>📄 Abstract</summary>
  Simulating two-dimensional frustrated quantum matter is a grand challenge due to the sign problem and exponential Hilbert space complexity. In this work, we introduce the Holographic Quantum Transformer (HQT), a physics-inspired generative architecture that leverages global self-attention to resolve non-local entanglement patterns. We validate HQT on the square lattice $J_1-J_2$ Heisenberg model. On the heavily frustrated $8 \times 8$ lattice at the quantum critical point ($J_2=0.5$), HQT reache...
  </details>

- **2026-07-01** — Kele Xu, Yulu Fang, Boda Zhou et al. — [From Objectives to Applications: Aligning Architectural Biases in Audio Self-Supervised Learning](http://arxiv.org/abs/2607.00387v1)
  <details><summary>📄 Abstract</summary>
  This paper examines audio self-supervised learning (SSL) through the alignment between pretraining objectives, architectural inductive biases, and downstream applications. Rather than treating SSL methods as a chronological sequence of pretext tasks or model families, we ask how different supervisory signals shape the representations that models are expected to learn. The discussion is organized around five paradigms: auxiliary tasks, contrastive learning, generative reconstruction, discrete tok...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 71 papers

- **2026-07-06** — Suryanarayana Reddy Yarrabothula, Manisha Chawla, Kunal Sinha et al. — [SteelBench: Evaluating Vision-Language Models in Real-World Industrial Environments](http://arxiv.org/abs/2607.05264v1)
  <details><summary>📄 Abstract</summary>
  Existing video benchmarks evaluate action recognition on consumer videos, egocentric recordings, or simulated industrial environments. They do not test vision-language models under the visual and procedural conditions of real industrial CCTV, where workers appear as distant figures amid dust, steam, low light, glare, occlusion, and overlapping activities. We introduce STEELBENCH, a diagnostic benchmark for industrial surveillance that jointly evaluates per-worker activity recognition, safety-rul...
  </details>

- **2026-07-06** — Sebastian A. Bruijns, Jirko Rubruck, Mia H. Whitefield et al. — [Pretraining Curricula Enable Selective Fine-tuning](http://arxiv.org/abs/2607.04846v1)
  <details><summary>📄 Abstract</summary>
  Transformers follow implicit curricula whereby some tasks are learned before others. However, how explicit pretraining curricula influence learning, generalization, and the selectivity of fine-tuning is unclear. This is important for AI safety, where fine-tuning is used to selectively suppress misaligned behaviors. Here, we compare curricula that pretrain tasks in a balanced (sampled uniformly) or an imbalanced (one task early, the other late) fashion. We show that imbalanced learning of two con...
  </details>

- **2026-07-06** — Sokipriala Jonah — [LLMs for Agentic Home Energy Management](http://arxiv.org/abs/2607.04569v1)
  <details><summary>📄 Abstract</summary>
  Home Energy Management Systems (HEMS) can reduce residential electricity costs and support demand response, but adoption is limited by the difficulty of translating household preferences into technical scheduling constraints. This paper evaluates whether large language model (LLM) agents can provide a practical natural-language interface for multi-appliance home energy scheduling. We present a tool-calling ReAct agent that uses live half-hourly Octopus Agile prices, weather forecasts, photovolta...
  </details>

- **2026-07-06** — Wenhao Li, Xueying Jiang, Quanhao Qian et al. — [From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model](http://arxiv.org/abs/2607.05396v1)
  <details><summary>📄 Abstract</summary>
  Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To...
  </details>

- **2026-07-06** — Zhe Zhao, Zhibin Li, Yilin Ou et al. — [Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation](http://arxiv.org/abs/2607.04940v1)
  <details><summary>📄 Abstract</summary>
  Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simula...
  </details>

- **2026-07-06** — Yunchao Zhang, Yijia Weng, Ruizhe Liu et al. — [Geometry-Aware Motion Latents for Learning Robust Manipulation Policies](http://arxiv.org/abs/2607.04714v1)
  <details><summary>📄 Abstract</summary>
  Learning motion latents for robotic manipulation heavily relies on extracting motion patterns from visual sequences, yet effective action abstractions require understanding three-dimensional geometric transformations. Here, we introduce GeoMoLa (Geometry-Aware Motion Latents), which learns discrete motion latent codes by predicting how point clouds evolve during manipulation rather than reconstructing visual observations. This four-dimensional objective -- spatial geometry changing through time ...
  </details>

- **2026-07-06** — Veeramanohar Avudaiappan, Ritwik Murali — [StructuredEdit: Constraint-Aware Graphic Design Editing via Differentiable Parameter Propagation](http://arxiv.org/abs/2607.04612v1)
  <details><summary>📄 Abstract</summary>
  Graphic design editing requires precise manipulation of typography, layout, and visual hierarchy under strict design constraints. Following the introduction of large language models, organizations have increasingly promoted vision-language models to enhance productivity. However, current models operate on pixels and achieve only 52% constraint satisfaction on structured design edits, thereby limiting their reliability for professional workflows. We present StructuredEdit, a pipeline that reframe...
  </details>

- **2026-07-06** — Kaiyuan Chen, Shuangyu Xie, Letian Fu et al. — [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks](http://arxiv.org/abs/2607.05369v1)
  <details><summary>📄 Abstract</summary>
  For robots to work reliably in commercial and industrial applications, can recent advances in agentic coding systems combine interpretable robot programming with the open-world adaptability of model-free policies? We focus on "Variational Automation" (VA), a class of tasks that have larger variations in object geometry and pose than fixed automation. Model-free policies often struggle to close the reliability gap for VA tasks, which must be executed persistently and reliably in commercial and in...
  </details>

- **2026-07-06** — Thomas Thebaud, Yuzhe Wang, Hao Zhang et al. — [SPEARBench: A Benchmark for Naturalness Evaluation in Streaming Speech-to-Speech Language Models](http://arxiv.org/abs/2607.05365v1)
  <details><summary>📄 Abstract</summary>
  Streaming speech-to-speech language models aim to answer spoken queries directly with synthetic speech. However, standard speech and text benchmarks do not capture whether these systems behave naturally in conversations, where timing, turn-taking, prosody, interpersonal stance, language and dialect consistency, and relationship-aware appropriateness jointly shape perceived quality. We introduce SPEARBench, a benchmark for evaluating naturalness in speech-to-speech language models from question-a...
  </details>

- **2026-07-06** — Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary et al. — [Multiplayer Interactive World Models with Representation Autoencoders](http://arxiv.org/abs/2607.05352v1)
  <details><summary>📄 Abstract</summary>
  We introduce the first multiplayer world model for highly dynamic environments governed by complex physical interactions. Whereas single-player world models treat the other agents as part of the environment, ours conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player and to stay coherent under arbitrary combinations of their actions. We study this problem in the game of Rocket League, where players compete and cooperate under fast, t...
  </details>

- **2026-07-06** — Vishal Asnani, Shruti Agarwal, John Collomosse — [FlowMark: Mask-Guided Video Watermarking](http://arxiv.org/abs/2607.05261v1)
  <details><summary>📄 Abstract</summary>
  We present FlowMark, a video watermarking framework guided by automatically predicted object masks. In contrast to prior region-based approaches that require user-supplied mask guidance, FlowMark learns to identify optimal regions for watermark embedding through a dedicated Mask Predictor network. Our end-to-end trainable architecture combines region-aware encoding with noise-augmented training to ensure robustness against compression, geometric transformations, and content variation, while pres...
  </details>

- **2026-07-06** — Ning Zhang, Wenjian Liu — [cQED-iCIPT2: A Near-Exact Method for Polaritonic Chemistry](http://arxiv.org/abs/2607.05192v1)
  <details><summary>📄 Abstract</summary>
  Strong light-matter coupling in optical cavities provides a versatile platform for modulating chemical structure, reactivity, and spectroscopy, and hence motivates the development of ab initio cavity quantum electrodynamics (cQED) methods that can treat the electronic and photonic degrees of freedom on an equal footing. We present such a method, cQED-iCIPT2, by combining the near-exact iCIPT2 (iterative configuration interaction with selection and second-order perturbation theory) with the cQED ...
  </details>

- **2026-07-06** — Zhiheng Xi, Dingwen Yang, Jiaqi Liu et al. — [AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments](http://arxiv.org/abs/2607.05174v1)
  <details><summary>📄 Abstract</summary>
  Language agents, i.e., LLM agents, progress rapidly and are increasingly deployed in production environments. This trend underscores the urgent need for rigorous and realistic evaluations. However, most existing benchmarks evaluate agents in simplified, idealized settings. They typically rely on pre-packaged tool interfaces, overlook critical steps, and assume inputs are clean and fully specified. Consequently, they understate the difficulty of real deployments, where uncertainty and noise are u...
  </details>

- **2026-07-06** — Rang Liu, Ming Li, A. Lee Swindlehurst et al. — [Multiuser MIMO-AFDM Beamforming for ISAC in Doubly Dispersive Channels](http://arxiv.org/abs/2607.05119v1)
  <details><summary>📄 Abstract</summary>
  Integrated sensing and communication (ISAC) in high-mobility channels requires waveform and beamforming designs that are robust to delay-Doppler dispersion. With this in mind, in this paper we study a monostatic multiuser multiple-input multiple-output (MIMO) affine frequency division multiplexing (AFDM) downlink system. We develop a discrete affine Fourier transform (DAFT)-domain model that preserves Doppler-induced inter-bin coupling and derive a data-aided delay-Doppler detector. The expected...
  </details>

- **2026-07-06** — Tadashi Tsuyuki, Shunji Kotsuki — [A Mutual Information-Based Ensemble Kalman Filter](http://arxiv.org/abs/2607.05030v1)
  <details><summary>📄 Abstract</summary>
  Ensemble Kalman filters (EnKFs) are widely used for data assimilation in geophysical systems. Among various implementations, the local ensemble transform Kalman filter (LETKF) has gained popularity because of its computational efficiency. However, the deterministic EnKF such as the LETKF is known to be less robust than the stochastic EnKF in strongly nonlinear regimes. We generalize the LETKF such that it contains a stochastic term and includes the stochastic EnKF within it. We adaptively optimi...
  </details>

- **2026-07-06** — Qiuyi Qi, Tian Liang, Mutian Bao et al. — [STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training](http://arxiv.org/abs/2607.04963v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) is the dominant paradigm for training Large Language Model (LLM) agents on long-horizon tasks. However, sparse and delayed rewards often lead to trajectory neglect, in which agents lose focus on the task goal and interaction history at intermediate steps. Prior work has explored step-level supervision using Shannon-entropy-based uncertainty signals, which conflate inherent state complexity with agent confidence and therefore provide unreliable estimates of decision re...
  </details>

- **2026-07-06** — Nicholas Tan Jerome, Frank Simon — [When Do Foundation Models Pay Off? A Break-Even Analysis of Pretrained Time Series Forecasters](http://arxiv.org/abs/2607.04919v1)
  <details><summary>📄 Abstract</summary>
  Deploying a time series foundation model requires GPU infrastructure, engineering overhead, and carries no guarantee of improvement over XGBoost. We provide the first systematic break-even analysis answering when this investment pays off. Across 30 benchmark datasets, we compare zero-shot and LoRA fine-tuned foundation models (Chronos, Moirai, Lag-Llama) against classical baselines (Naive, ETS, ARIMA, XGBoost) at six training set sizes from 2% to 100% of available data. Foundation models outperf...
  </details>

- **2026-07-06** — Miguel Antunes-García, Santiago Montiel-Marín, Fabio Sánchez-García et al. — [TGRIP: A Text-Guided Approach to Vehicle Instance Prediction in Autonomous Driving](http://arxiv.org/abs/2607.04812v1)
  <details><summary>📄 Abstract</summary>
  Bird's-Eye View (BEV) end-to-end instance prediction has emerged as a robust paradigm for autonomous driving perception, effectively mitigating the error propagation inherent in traditional modular pipelines. However, current state-of-the-art approaches rely predominantly on geometric supervision, such as occupancy regression and optical flow, effectively treating scene agents as generic moving obstacles. This absence of explicit semantic awareness imposes limitations on the capacity of the mode...
  </details>

- **2026-07-06** — Linas Beresna, Eugene Fiume — [Glare Mitigation using a Differentiable Unified Glare Rating](http://arxiv.org/abs/2607.04796v1)
  <details><summary>📄 Abstract</summary>
  Recent research in differentiable light transport extends the utility of computer graphics algorithms beyond traditional image generation, offering powerful tools for physical inverse design. In architectural and automotive applications, visual discomfort from glare is a critical design rating, traditionally quantified by the discrete CIE Unified Glare Rating (UGR). The standard UGR formulation relies on strict binary thresholds, making it fundamentally incompatible with smooth gradient-based in...
  </details>

- **2026-07-06** — Kenta Tsukahara, Kanji Tanaka, Rai Hisada — [SLAM: Structured and Localized Analytic Manifold Adaptation for Lifelong VPR](http://arxiv.org/abs/2607.04764v1)
  <details><summary>📄 Abstract</summary>
  Visual Place Recognition (VPR) in lifelong deployment requires continuous adaptation to new environments without catastrophic forgetting. In this paper, we propose SLAM, a Structured and Localized Analytic Manifold adaptation framework. Our framework elegantly unifies uncertainty-aware smoothing via Unscented transformation, topological space partitioning through a Gaussian Mixture Model (GMM), and $H_\infty$ robust bound optimization into a singular, unified closed-form analytical recursion. Ex...
  </details>

- **2026-07-06** — Ashna Goel, Shovan Bhaumik, Nutan Kumar Tomar — [Risk Sensitive Filtering for Singular Systems subject to Round-Robin Protocol](http://arxiv.org/abs/2607.04734v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a risk sensitive (RS) Kalman filtering framework for discrete-time linear stochastic singular systems operating under communication constraints imposed by a round-robin protocol. Due to limited network bandwidth, only a subset of the available measurements can be transmitted at each sampling instant, resulting in a periodically varying measurement structure. By employing the Weierstrass canonical form (WCF), the singular system is transformed into an equivalent augmented stat...
  </details>

- **2026-07-06** — Mingyang Fu, Ming Hu — [Strategic Buying Agents](http://arxiv.org/abs/2607.04708v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI is shifting online shopping from search toward delegated purchasing, where autonomous buying agents monitor markets and decide when to buy on a consumer's behalf. We study the design of such strategic buying agents, which must decide when to purchase within a finite shopping window, translating price observations, the remaining time horizon, and beliefs about future price changes into a purchase policy. We formulate this problem across three information regimes: stationary, Bayesian, ...
  </details>

- **2026-07-06** — Liuyun Jiang, Yanchao Zhang, Jinyue Guo et al. — [Probe-EM: Targeted Neuron Tracing via Training-Free Semantic Verification](http://arxiv.org/abs/2607.04696v1)
  <details><summary>📄 Abstract</summary>
  Establishing large-scale, high-resolution neural connectivity maps is fundamental to elucidating the structural basis of brain function. However, when processing terabyte- or petabyte-scale electron microscopy data, over-segmentation inherent in automated reconstruction algorithms remains a critical bottleneck, requiring extensive manual proofreading spanning person-years. To alleviate the heavy reliance on annotated data and the limited flexibility of conventional tracing methods, we propose a ...
  </details>

- **2026-07-05** — Haiwen Yi, Xinyuan Song — [Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents](http://arxiv.org/abs/2607.04528v1)
  <details><summary>📄 Abstract</summary>
  Software-agent benchmarks usually report whether an agent solves a task, but the agent reaches that outcome through a harness that controls what it sees, which actions it can take, which failures are repaired, which states are verified, and which evidence is logged. We show that this harness can change the agent's multi-step beliefs even when the task, environment, and base LLM are fixed. We introduce a belief-rollout diagnostic that elicits structured K-step trajectories over progress, risk, re...
  </details>

- **2026-07-05** — Zhaohong Liu, Hao Ye, Xianlin Zhang et al. — [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](http://arxiv.org/abs/2607.04179v1)
  <details><summary>📄 Abstract</summary>
  End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving. However, standard Supervised Fine-Tuning (SFT) often suffers from reasoning hallucinations and conservative biases. While traditional tool-augmented frameworks and Chain-of-Thought (CoT) approaches mitigate these issues, they incur exorbitant token consumption and unacceptable latency, rendering real-time deployment impractical. To resolve this reliability-efficiency trade-off, we propose CritiqueDriveVLM, a n...
  </details>

- **2026-07-05** — Iok Tong Lei, QianZhi Li, Ying Jie Yap et al. — [ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning](http://arxiv.org/abs/2607.04162v1)
  <details><summary>📄 Abstract</summary>
  Open-ended tabletop manipulation requires agents to not only understand natural language but also adapt to dynamic environments and execution failures. We present ACE (Agentic Control for Embodied Manipulation), a zero-shot workflow reasoning framework for tabletop pick-and-place from natural language. Rather than relying on direct low-level action mapping, ACE combines agentic workflow reasoning with two robot-facing executable skills: a visual grounding interface and a reusable pick-and-place ...
  </details>

- **2026-07-05** — Zexing Zhang, Jichao Li, Yilong Wang et al. — [Non-invasive Blood Glucose Estimation from Wearable Physiological Signals](http://arxiv.org/abs/2607.04414v1)
  <details><summary>📄 Abstract</summary>
  Non-invasive blood glucose estimation from wearable physiological signals remains difficult because longitudinal photoplethysmography (PPG) data are subject to distribution drift, whereas reference capillary blood glucose labels are sparse and costly to acquire. We propose a \rev{deep-learning-based} dynamic incremental learning (DIL) framework that combines a mutual entropy-optimized replay-based dynamic clustering module (MERDC) with an uncertainty-quantified proxy gradient bridging agent (PGB...
  </details>

- **2026-07-05** — Yaxuan Li, Jiarui Zeng, Shaofei Huang et al. — [Last-Meter Precision Navigation for UAVs: A Diffusion-Refined Aerial Visual Servoing Approach](http://arxiv.org/abs/2607.04352v1)
  <details><summary>📄 Abstract</summary>
  In this work, we study the last-meter precision navigation for UAVs, e.g., autonomously reaching a target within the final 10 meters using monocular vision. This task is challenging due to scale ambiguity, rotation discontinuities, and the need for fine-grained spatial reasoning. Existing methods often fail under large viewpoint changes or lack generalization to unseen environments. To this end, we propose DreamNav, a coarse-to-fine diffusion-refined aerial visual servoing framework. In the firs...
  </details>

- **2026-07-05** — Austin Stover, Juliang Li, Peter Sharpe et al. — [A 3D-Printed Millimeter-Wave Inline Waveguide-to-Coplanar-Waveguide Transition to Enable Dense Spectrometer Arrays for Intensity Mapping Surveys](http://arxiv.org/abs/2607.04258v1)
  <details><summary>📄 Abstract</summary>
  We present a 3D-printed millimeter-wave, octave-bandwidth, in-line waveguide-to-coplanar-waveguide transition designed to enable focal planes with dense arrays of on-chip spectrometers. These arrays will enable compelling surveys of the large-scale structure of the universe through millimeter-wave intensity mapping. The transition consists of a four-step ridge-waveguide transformer that couples light from a rectangular waveguide onto a coplanar waveguide via an electrical connection made with in...
  </details>

- **2026-07-05** — Huqin Weng, Jiayang Huang, Yimin Wen et al. — [Masked Generative-Contrastive Representation Learning for Cross-Dataset EEG-Based Emotion Recognition](http://arxiv.org/abs/2607.04139v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning (SSL) shows strong potential for cross-dataset transfer by improving feature representation and generalization. However, its application to EEG-based emotion recognition remains largely unexplored. Existing SSL methods struggle to capture the intricate spatiotemporal dependencies of EEG signals under varying channel configurations, extract fine-grained representations resilient to noise, and derive global features that generalize well across subjects. To address these ch...
  </details>

- **2026-07-05** — Silin Gao, Hao Zhao, Zeming Chen et al. — [DynaVieW: Schema-Guided World Modeling for Understanding Hierarchical Visual Dynamics](http://arxiv.org/abs/2607.04112v1)
  <details><summary>📄 Abstract</summary>
  Multimodal LLMs struggle to systematically model the temporal evolution of visual scenes in videos or multi-image sequences. Such inputs require models to predict or simulate multiple levels of dynamic constituents, such as actions taken in the visual sequence, and the associated changes to the visual environment that result. To address this challenge, we propose a dynamic schema-guided world model, DynaVieW, optimized for visual dynamic prediction and simulation. DynaVieW achieves an in-depth u...
  </details>

- **2026-07-05** — Kun Sun, Rong Wang — [Semantic Integration and Lexical Expectation Shape N400 and P600 Dynamics During Naturalistic Reading](http://arxiv.org/abs/2607.04107v1)
  <details><summary>📄 Abstract</summary>
  Word surprisal is a well-established computational predictor of human neural responses during language comprehension, but it remains less clear whether local semantic fit explains neural response variation beyond lexical expectation during naturalistic reading. Using the Dublin EEG-based Reading Experiment Corpus (DERCo), this study examined whether contextual semantic relevance predicts word-locked EEG activity in the N400 and P600 windows. Contextual semantic relevance was computed as an atten...
  </details>

- **2026-07-04** — Jianjie Fang, Yongyan Xu, Ziyou Wang et al. — [Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control](http://arxiv.org/abs/2607.03964v1)
  <details><summary>📄 Abstract</summary>
  World models are rapidly becoming a core infrastructure for embodied intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast, and acquire scalable experience. Yet current video generation world models are still organized around isolated control interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling bottleneck. The central challenge is not the absence of controllable ...
  </details>

- **2026-07-04** — Nguyen Kim Hai Bui, Md. Easin Arafat, Tamás Gábor Orosz et al. — [When Simpler Is Better: Evaluating Translation Pipelines for Medieval Latin Manuscripts](http://arxiv.org/abs/2607.03836v1)
  <details><summary>📄 Abstract</summary>
  Despite remarkable progress in machine translation, Vision Language Models (VLMs) struggle on historical manuscripts, a domain that stresses core Natural Language Processing (NLP) capabilities: low-resource transliteration, archaic vocabulary, and noisy input signals. We present a systematic framework for evaluating the full image-to-translation pipeline on medieval Latin manuscripts, a setting in which scribal shorthand, ligatures, and parchment degradation expose failure modes that are invisib...
  </details>

- **2026-07-04** — Xinqi Zhang — [NormWorlds-CF: Solver-Verified Counterfactual Normative Reasoning with Metamorphic-Relation GRPO](http://arxiv.org/abs/2607.03957v1)
  <details><summary>📄 Abstract</summary>
  Language models can reach the right normative verdict for the wrong reason. We introduce NormWorlds-CF, a solver-verified environment for counterfactual normative reasoning in executable rule worlds. Its deterministic solver produces final answers, proof and falsification certificates, argument statuses, support sets, and paired-world change labels, enabling supervision and evaluation without LLM judges. The benchmark contains staged SFT diagnostics and a compact paired-world task with 270 root ...
  </details>

- **2026-07-04** — Fuqiang Chen, Yifeng Wang, Hongpeng Wang et al. — [ContiStain: Cross-Domain Relation-Preserving Distillation for Continual Multi-Domain Virtual IHC Staining](http://arxiv.org/abs/2607.03851v1)
  <details><summary>📄 Abstract</summary>
  A unified multiplex virtual staining model enables scalable and non-destructive multiplex analysis from H&E slides while promoting parameter efficiency, shared pathological knowledge, and consistent cross-biomarker representations. However, in clinical practice, data for new biomarkers are typically acquired sequentially over time. Fine-tuning on such temporally arriving data leads to severe performance degradation on previously learned biomarkers, as sequential optimization disrupts the structu...
  </details>

- **2026-07-04** — Saba Fathi, Fardin Ayar, Maryam Abdolali et al. — [How Do Diffusion Classifiers Decide? A Bias-Centric Evaluation](http://arxiv.org/abs/2607.03831v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models have recently been repurposed for zero-shot classification, giving rise to diffusion classifiers that identify the best-matching text prompt by minimizing the noise-prediction error. Despite their growing adoption, how these models make classification decisions remains poorly understood. We introduce ASOB-Bench, a bias evaluation for diffusion classifiers along three dimensions: Attribute binding, Size-Order bias, and Background dependency. These dimensions serve not as an exhau...
  </details>

- **2026-07-04** — Dubing Chen, Huan Zheng, Tianyi Yan et al. — [FDR-Occ: Factorized Dense Routing for Full-Spectrum 3D Occupancy Prediction](http://arxiv.org/abs/2607.03822v1)
  <details><summary>📄 Abstract</summary>
  Vision-based 3D occupancy prediction fundamentally relies on the 2D-to-3D view transformation. Current paradigms predominantly utilize explicit physical projection, which artificially restricts the routing matrix to strict, sparse camera rays. While computationally efficient, this imposes a severe Locality Bottleneck, preventing the network from constructing holistic contextual understanding and degrading sharply when camera extrinsics are unreliable or absent. To break this bottleneck, we abstr...
  </details>

- **2026-07-04** — Chih-Ting Liao, Xin Cao — [The Objective Decides: When a Learned Dynamics Model Uses a Conserved Quantity](http://arxiv.org/abs/2607.03728v1)
  <details><summary>📄 Abstract</summary>
  A linear probe that recovers a conserved quantity from a learned dynamics model's activations is routinely read as evidence that the model uses that quantity. We show this inference is unsound. Across mechanical, circuit, and partial-differential-equation (PDE) systems, and on a 158M-parameter pretrained PDE foundation model, energy and other invariants are linearly decodable at $R^2 \approx 1$ yet causally inert on next-state prediction: overwriting the decoded direction with a donor state's va...
  </details>

- **2026-07-04** — Shu Yang, Junchao Wu, Derek F. Wong et al. — [SelfMem: Self-Optimizing Memory for AI Agents](http://arxiv.org/abs/2607.03726v1)
  <details><summary>📄 Abstract</summary>
  While current AI agents support increasingly long context windows, tool use, and skill execution for long-horizon tasks, they still require memory systems to effectively leverage historical experience. Existing memory frameworks typically rely on fixed storage, retrieval, and summarization mechanisms, which can be rigid across different tasks and often require manual tuning. To address this limitation, we propose SelfMem, a self-optimizing memory framework. Inspired by prior work on self-improvi...
  </details>

- **2026-07-02** — Matteo Boglioni, Thibault Rousset, Siva Reddy et al. — [LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning](http://arxiv.org/abs/2607.02513v1)
  <details><summary>📄 Abstract</summary>
  LLMs memorize sensitive training data, including personally identifiable information (PII), creating a pressing need for reliable post hoc removal methods. Unlearning has emerged as a promising solution, with state-of-the-art(SOTA) methods often following a localize-first, unlearn-second paradigm that targets specific model parameters. However, existing benchmarks evaluate unlearning solely at the output level, leaving open the question of whether unlearning truly erases knowledge from a model's...
  </details>

- **2026-07-02** — Misha Sulpovar, Benn R. Konsynski, Qaish Kanchwala et al. — [ContextNest: Verifiable Context Governance for Autonomous AI Agent](http://arxiv.org/abs/2607.02116v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents increasingly depend on external knowledge stores, yet most retrieval pipelines provide relevance without durable guarantees of provenance, version identity, integrity, traceability, or point-in-time reconstruction. We formalize this as context governance and present ContextNext, an open specification and reference implementation for governed AI-consumable knowledge vaults. ContextNext does not replace Retrieval-Augmented Generation (RAG); it supplies the governance layer ben...
  </details>

- **2026-07-02** — Minjong Cheon — [Robust for the Wrong Reasons: The Representational Geometry of LLM Robustness to Science Skepticism](http://arxiv.org/abs/2607.01951v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly consulted on contested scientific questions, raising the concern that they will sycophantically retreat from established consensus when a user signals doubt -- drifting toward a false balance that treats settled science as one view among several. We test this across three open instruction-tuned models (Llama-3.1-8B, Qwen2.5-7B, Mistral-7B), three consensus-science domains (climate, vaccines, evolution), and single- and multi-turn settings, combining ...
  </details>

- **2026-07-02** — Alex Brooker, Tim Hughes — [Pre-Flight: A Benchmark for Evaluating Large Language Models on Aviation Operational Knowledge](http://arxiv.org/abs/2607.01829v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly proposed for aviation business operations, from documentation and training generation to customer facing assistants. General purpose benchmarks do not measure whether a model reasons safely and correctly about aviation specific operational knowledge, and the high stakes, regulated nature of the domain makes that gap consequential. We present Pre-Flight, an open source benchmark of 300 multiple choice questions drawn from international standards and a...
  </details>

- **2026-07-02** — Jiamin Jiang, Jingfei Feng, Yu Luo et al. — [KRCA: An Efficient Root Cause Analysis System in Hyper-Scale Microservice Systems via Agentic AI](http://arxiv.org/abs/2607.01788v1)
  <details><summary>📄 Abstract</summary>
  Hyper-scale microservice systems have become the standard infrastructure for large-scale Internet companies. These systems consist of numerous loosely coupled microservices that evolve independently through continuous development and deployment. Such complexity makes failures unavoidable, necessitating efficient Root Cause Analysis (RCA) to help Site Reliability Engineers (SREs) quickly localize root cause services and classify failure types. However, existing RCA methods often struggle to adapt...
  </details>

- **2026-07-02** — Meng Wang, Haohan Zhao, Wenzhuo Liu et al. — [Denser $\neq$ Better: Limits of On-Policy Self-Distillation for Continual Post-Training](http://arxiv.org/abs/2607.01763v1)
  <details><summary>📄 Abstract</summary>
  Continual post-training enables foundation models to acquire new knowledge while preserving existing capabilities. Recent work suggests that on-policy learning can mitigate forgetting, with on-policy self-distillation emerging as a particularly attractive approach. In this work, we revisit this optimistic view through self-distillation policy optimization (SDPO). Our experiments show that SDPO can accelerate in-domain specialization when teacher signals are stable and well aligned, but it strugg...
  </details>

- **2026-07-02** — Sung June Kim, Sangpil Kim, Honglak Lee — [Path-level Hindsight Instructions for Semantic Exploration in Vision-Language Navigation](http://arxiv.org/abs/2607.01754v1)
  <details><summary>📄 Abstract</summary>
  On-policy exploration is a crucial component for training robust Vision-Language Navigation agents, as it exposes the policy to a broader state distribution. However, such exploration inevitably leads to trajectories that deviate from expert demonstrations, resulting in a semantic mismatch between the executed visual stream and the original language instruction. In this work, we address this challenge by introducing Phi-Nav, a unified on-policy framework that leverages hindsight reasoning to ali...
  </details>

- **2026-07-02** — Yongjie Bai, Hanting Wang, Mingtong Dai et al. — [Bridge-WA: Predicting Where and How the World Changes for Robotic Action](http://arxiv.org/abs/2607.02195v1)
  <details><summary>📄 Abstract</summary>
  General-purpose vision-language-action models benefit from large vision-language priors, but effective manipulation also requires anticipating action-relevant scene changes. Existing world-action models often rely on large generative world models or dense future rollouts, which are expensive and spend capacity on visual details weakly coupled to control. We present Bridge-WA, a lightweight world-action framework that distills a frozen future-change teacher into three compact priors: future token...
  </details>

- **2026-07-02** — Haofei Xu, Rundi Wu, Philipp Henzler et al. — [PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation](http://arxiv.org/abs/2607.02515v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions, or compress geometry into latent spaces in order to leverage pre-trained latent diffusion models. In this work, we show that such architectural overhead and intricate loss formulations are unnecessary. We introduce a minimalist pixel-space Diffusion Transformer, built on a plain ViT, that operates directly on raw 3D point map patches and is conditioned on image tokens from a pre...
  </details>

- **2026-07-02** — Yuxuan Li, Lingxi Xie, Xinyue Huo et al. — [Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas](http://arxiv.org/abs/2607.02504v1)
  <details><summary>📄 Abstract</summary>
  Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attributing each spoken utterance to its respective character. In this paper, we advance this field through two primary contributions. (1) We introduce \textbf{DramaSR-532K}, a large-scale benchmark comprising 532K annotated dialogue lines across more than 900 unique characters, necessitating the integra...
  </details>

- **2026-07-02** — Xi Zhang, Papi Menon, Vivian Chu et al. — [Adoption and Ecosystem Health: A Longitudinal Analysis of Open-Source Multi-Agent Frameworks](http://arxiv.org/abs/2607.02453v1)
  <details><summary>📄 Abstract</summary>
  Since ChatGPT's launch in November 2022, open-source agentic frameworks have proliferated, making framework selection important for engineering teams while obscured by popularity signals such as GitHub stars. This paper analyzes 15 major open-source AI agent framework repositories from late 2022 to early 2026, using 808,042 stars, 73,997 pull requests, 86,241 commits, and 987,330 user profiles to assess ecosystem health across awareness, adoption, and retention. Three findings emerge. First, hea...
  </details>

- **2026-07-02** — Xi Fang, Weijie Xu, Yingqiang Ge et al. — [DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models](http://arxiv.org/abs/2607.02374v1)
  <details><summary>📄 Abstract</summary>
  Personalization changes what a model says to a user; we show that it can also change the reasoning trajectory used to justify the response. Modern LLMs personalize interactions by storing user attributes, preferences, and prior context, then injecting this information into future prompts. We study whether such memory reshapes reasoning on open-ended questions where no single ground-truth answer exists. To quantify this effect, we introduce DRIFTLENS, a ground-truth-free framework that maps each ...
  </details>

- **2026-07-02** — Wanyun Cui — [A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets](http://arxiv.org/abs/2607.02303v1)
  <details><summary>📄 Abstract</summary>
  Linear-attention and state-space language models compress the prefix into a fixed-size recurrent state, yielding O(1) memory at the cost of a lossy exact memory: when many key--value associations compete, earlier facts are overwritten and needle recall degrades. Inspired by Complementary Learning Systems, we give linear attention a hippocampal complement. HOLA (Hippocampal Linear Attention) keeps the usual delta-rule state as a compressive memory and adds a bounded exact KV cache, forming a semi...
  </details>

- **2026-07-02** — Tien-Phat Nguyen, Ngai-Man Cheung — [When Token Compression Breaks: Structural Pruning vs. Token Reduction for Robust ViT Segmentation under High Compression](http://arxiv.org/abs/2607.02237v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) are strong backbones for semantic segmentation, but their computational cost limits deployment. Recent token compression methods for efficient transformer-based segmentation reduce this cost by decreasing the number of tokens. However, existing evaluations primarily focus on low-to-moderate compression, leaving their behavior under aggressive compression and corrupted inputs unclear. Meanwhile, structural pruning provides an orthogonal route to efficiency by removing r...
  </details>

- **2026-07-02** — Satoshi Yamamori, Koji Ishihara, Kentaro Minamikawa et al. — [Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning](http://arxiv.org/abs/2607.02205v1)
  <details><summary>📄 Abstract</summary>
  Sim-to-real transfer in robot learning is often limited by discrepancies between the ideal actuator dynamics assumed during policy training and the nonlinear, hardware-dependent behavior of physical motors. While conventional approaches attempt to bridge this gap by increasing simulator fidelity through system identification, domain randomization, or learned actuator models, we introduce an alternative paradigm: actuator reality shaping. Instead of modifying the simulator to match the real world...
  </details>

- **2026-07-02** — Shunya Kato, Taiki Miyanishi, Shuhei Kurita et al. — [LongEgoRefer: A Benchmark for Long-Form Egocentric Video Referring Expression Comprehension](http://arxiv.org/abs/2607.02096v1)
  <details><summary>📄 Abstract</summary>
  Egocentric videos capture rich and diverse human-object interactions and have emerged as a fundamental resource for understanding human activities related to objects. In this context, Video Referring Expression Comprehension (Video REC), the task of localizing the temporal and spatial extent of a referred object in video frames given a natural language query, plays a key role in linking textual descriptions to observed objects in untrimmed egocentric recordings. However, existing egocentric Vide...
  </details>

- **2026-07-02** — Yihuai Zhang, Yidan Cao, Huan Yu et al. — [Robust Stabilization of Linear Markov-Jumping Hyperbolic PDEs with Boundary Input Delay](http://arxiv.org/abs/2607.02081v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the robust stabilization of 2 $\times$ 2 linear hyperbolic partial differential equations (PDEs) with Markov-jumping parameters and boundary input delay. The main challenge arises from the simultaneous presence of stochastic parameter variations and input delay, which complicates both the stability analysis and controller design. To address this issue, a nominal delay-compensating backstepping controller is first designed for a fixed nominal system. Applying the nominal transf...
  </details>

- **2026-07-02** — Qianyu Chen, Canran Xiao, Runxuan Tang — [Hidden Forgetting in Continual Multimodal Learning: When Accuracy Survives but Grounding Fails](http://arxiv.org/abs/2607.02020v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models must continually adapt to evolving tasks and domains, yet standard continual learning metrics mainly measure whether old answers remain correct, leaving the stability of multimodal grounding largely unexamined. We study this overlooked failure mode and ask whether a continually adapted MLLM can preserve not only what it answers, but also how it uses visual, textual, OCR, chart, and document evidence. We identify \emph{hidden evidence-use forgetting}, where answer...
  </details>

- **2026-07-02** — Yi Wang, Fan Wang, Prabin Gyawali et al. — [UnderOneFacade: Worldwide Facade Semantic Segmentation Benchmark Dataset](http://arxiv.org/abs/2607.02018v1)
  <details><summary>📄 Abstract</summary>
  Globally consistent semantic digital twins require centimeter-accurate and geographically transferable 3D facade segmentation. However, progress in facade parsing is limited by the lack of large-scale, standardized benchmarks for evaluating cross-domain generalization. Existing datasets are geographically narrow, semantically inconsistent, or insufficiently precise. We introduce UnderOneFacade, the largest cross-country and cross-continent 3D facade benchmark to date, comprising centimeter-accur...
  </details>

- **2026-07-02** — Cedric Richter, Mike Papadakis — [Underspecification does not imply Incoherence: The Risks of Semantic Collapse in Coding Models](http://arxiv.org/abs/2607.01953v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have become increasingly effective at generating code when task descriptions are clear and precise. Yet, in practice, user-provided task descriptions are often ambiguous, incomplete, or contradictory, leaving critical aspects of the intended program behavior underspecified. In such cases, multiple behaviorally distinct interpretations may satisfy the description equally well, yet semantically differ in ways that matter/affect the user intent. A natural expectation, o...
  </details>

- **2026-07-02** — Lihui Luo, Joongwon Chae, Ziyan Chen et al. — [MMIR-TCM: Memory-Integrated Multimodal Inference and Retrieval for TCM Clinical Decision Support](http://arxiv.org/abs/2607.01814v1)
  <details><summary>📄 Abstract</summary>
  Traditional Chinese Medicine (TCM) diagnosis, particularly through tongue inspection, faces persistent challenges in subjectivity and reproducibility. The application of multimodal artificial intelligence to TCM clinical tasks, such as syndrome differentiation and prescription generation, is significantly hampered by the semantic gap between visual tongue features and textual reasoning, as well as the lack of large-scale, standardized datasets. To address these challenges, we introduce MMIR-TCM,...
  </details>

- **2026-07-02** — Haoju Lin, Wenchang Zhang, Weipeng Xu et al. — [TO-Master: an LLM-agent framework for automated topology optimization](http://arxiv.org/abs/2607.01812v1)
  <details><summary>📄 Abstract</summary>
  Topology optimization (TO) has become a mature computational design method, but using it still requires substantial manual effort in geometry preparation, mesh generation, boundary-condition assignment, solver setup, and postprocessing. This implementation barrier limits the use of TO outside expert workflows, even when differentiable finite element solvers are available. This work introduces TO-Master, a large language model (LLM) agent framework that turns finite-element-based TO into a conver...
  </details>

- **2026-07-02** — Jiatong Li, Weida Wang, Changmeng Zheng et al. — [Do LLMs Truly Generalize in the Molecular Domain? A Perturbation-Based Analysis](http://arxiv.org/abs/2607.01800v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have recently shown promise in molecular discovery, yet a gap remains between their probabilistic nature over discrete sequential tokens and the rigid topological constraints of chemical space. This raises the question of whether molecular LLMs can generalize beyond the local neighborhoods induced by their sequence-based representations. To systematically investigate this question, we introduce a Molecular Perturbation framework that generates syntax-valid structural...
  </details>

- **2026-07-02** — Wen Wang, Yaping Sun, Yejun He et al. — [LLM-Empowered Multimodal Fusion Framework for Autonomous Driving: Semantic Enhancement and Channel-Adaptive Design](http://arxiv.org/abs/2607.01772v1)
  <details><summary>📄 Abstract</summary>
  Vision-radar fusion is central to robust autonomous driving, combining dense visual semantics with precise range and velocity measurements from radar. However, real-world fusion quality is fundamentally challenged by dynamically varying input quality, stemming from occlusion, adverse weather, and channel noise. To address this, we re-frame the problem from static data fusion to channel-aware semantic reasoning and propose a Large Language Model-centric Semantic-layer Channel-aware Integrated Per...
  </details>

- **2026-07-02** — Ronghui Xu, Tongxin Wu, Guozhen Zhang et al. — [UniWind: Toward Unified Day-Ahead Wind Power Forecasting via Physics-Informed State Routing](http://arxiv.org/abs/2607.01670v1)
  <details><summary>📄 Abstract</summary>
  Day-ahead wind power forecasting is essential for cost-effective power-system operation. It is primarily driven by future meteorological conditions while retaining temporal dependencies in power generation. In practice, observed wind-farm power often entangles physically available power with local environmental effects and latent operational states, such as shutdowns and curtailment. Existing physical models provide useful constraints but adapt poorly across wind farms, whereas data-driven model...
  </details>

- **2026-07-02** — Eunyi Lyou, Yunjeong Choi, Junho Lee et al. — [Domain Generalization via Text-Anchored Information Bottleneck](http://arxiv.org/abs/2607.01657v1)
  <details><summary>📄 Abstract</summary>
  Visual recognition models often fail when deployed in new environments. Domain Generalization (DG) addresses this by learning representations that remain invariant to environment-specific variations. Recent approaches increasingly rely on large vision-language models, assuming that preserving their expressive visual representations improves robustness. However, we show that such visual expressiveness can instead propagate spurious cues that tie representations to the training environments, hinde...
  </details>

- **2026-07-01** — Yaofei Duan, Yuhao Huang, Tianyu Zhang et al. — [ClinRAG-GRAPH: Clinical-prior Retrieval-Augmented Graph Model with Domain Adversarial Learning for Breast pCR Prediction](http://arxiv.org/abs/2607.00798v1)
  <details><summary>📄 Abstract</summary>
  Neoadjuvant chemotherapy (NAC) response prediction is clinically important for treatment stratification in breast cancer. However, robust pre-treatment pathological complete response (pCR) prediction remains challenging due to insufficient cross-modal modeling, multicenter imaging heterogeneity, and weak evidence-grounded interpretability. We propose ClinRAG-GRAPH, a Clinically informed Retrieval-Augmented Generation Graph framework, for pre-treatment pCR prediction from DCE-MRI, structured clin...
  </details>

- **2026-07-01** — Nils Neukirch, Martin Maurer, Nils Strodthoff — [Foundation Models vs. Radiomics for Lung Computed Tomography: A Benchmark of Feature Extractors, Classification Heads, and Segmentation Choices](http://arxiv.org/abs/2607.01001v1)
  <details><summary>📄 Abstract</summary>
  Radiomics is the established approach for CT-based lung cancer phenotyping, yet comparisons with foundation models rarely isolate contributions of feature extractor, classification head, and segmentation choice, or test cross-cohort robustness. We benchmark five feature extractors (Curia, Curia-2, DINOv3, Radiomics2D, Radiomics3D), seven classification heads (TabPFN, TabICL, XGBoost, CatBoost, Random Forest, logistic regression, Ridge), and three segmentation regimes on five tasks: tumor volume ...
  </details>

- **2026-07-01** — Xinyi Shang, Peng Sun, Bei Shi et al. — [Condensing Large-Scale Datasets Directly with Minimal Information Loss](http://arxiv.org/abs/2607.00916v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in scaling dataset distillation rely heavily on decoupled information extraction pipelines, comprising SQUEEZE, RECOVER, and RELABEL stages. Despite their scalability to large-scale datasets, these methods suffer from prohibitive computational overhead and poor cross-architecture generalization. In this paper, we reveal the root cause of these bottlenecks: the implicit dual-compression process, from data to model and back to images, inherently induces severe information loss....
  </details>

- **2026-07-01** — Yuan Qing, Chengzhi Mao, Boqing Gong — [StochasT: Learning with Stochastic Turn Depth for Visual Instruction Tuning](http://arxiv.org/abs/2607.00465v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) rely extensively on Visual Instruction Tuning (VIT) to elicit their multimodal reasoning capabilities. However, we find a discrepancy: VIT often packs multiple language tasks about the same image for conversational, multi-turn training, whereas existing benchmarks evaluate LVLMs in isolated, single-turn scenarios. The models can suffer from visual attention decay and contextual overfitting during multi-turn training, making it hard for them to realize their f...
  </details>

- **2026-07-01** — Xiangchen Song, Zhenhao Chen, Lingjing Kong et al. — [Beyond Perplexity: A Behavioral Evaluation Framework for Deployment-Memory Claims in LLM Test-Time Training](http://arxiv.org/abs/2607.00368v1)
  <details><summary>📄 Abstract</summary>
  Large language model test-time training (TTT) is often evaluated through local proxy metrics: models are updated on recent tokens, retrieved context, target-domain data, or verifiable task attempts, and then judged by perplexity, future-token loss, long-context performance, or reward. These metrics are well matched to claims about stream adaptation, domain adaptation, context compression, and reward-backed test-time improvement. They are weaker evidence, however, for a capability that TTT result...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 9 papers

- **2026-07-06** — Xue Yao, Zehua Zhang, Jiatong Liu et al. — [RepoTrace: Browser-Assisted Evidence Collection for GitHub Research Datasets](http://arxiv.org/abs/2607.05106v1)
  <details><summary>📄 Abstract</summary>
  Empirical software engineering studies frequently build datasets from GitHub issues and pull requests. In many projects, researchers inspect pages in a browser, copy selected fields into spreadsheets, keep side notes in separate documents, and later run scripts to normalize or export the data. This workflow is flexible, but the page evidence, the research codes, and the rationale behind each decision end up spread across tabs and files, which leaves provenance, update tracking, and multi-reviewe...
  </details>

- **2026-07-06** — Jizhizi Li, Amy Shi-Nash — [MRMS: A Multi-Resolution Memory Substrate for Long-Lived AI Agents](http://arxiv.org/abs/2607.04617v1)
  <details><summary>📄 Abstract</summary>
  Long-lived AI agents require continuity across interactions, but continuity cannot be obtained by simply extending the prompt window. An agent must preserve useful prior experience, retrieve it selectively, distinguish personal context from external evidence, and revise memory when the underlying situation changes. We propose an architectural memory substrate organized along two orthogonal axes: a representational axis spanning structured records, vector representations, and graph relations; and...
  </details>

- **2026-07-05** — Guijia Zhang, Harry Yang — [Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure](http://arxiv.org/abs/2607.04334v1)
  <details><summary>📄 Abstract</summary>
  Multimodal GUI agents read an interface through two redundant channels: the rendered pixels of a screenshot and a serialized structure such as a DOM or accessibility tree. Before acting, an agent forms a belief about the current interface state, but existing benchmarks score task success, element grounding, or attack resistance and do not ask whether that belief is drawn from the pixels. We formalize visual state reliance, the attribution of a state belief to pixels, structure, or priors, and me...
  </details>

- **2026-07-05** — Sukanta Ganguly — [PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents](http://arxiv.org/abs/2607.04089v1)
  <details><summary>📄 Abstract</summary>
  Lifelong agents need more than larger context windows and better retrieval. They need memories that can persist, evolve, and be corrected without forcing the serving stack to recompute the same history on every turn or silently reuse stale runtime state. We present PLACEMEM as a systems position on lifelong-agent memory, instantiated by an executable control-plane prototype. The central claim is that agent memory should be represented as versioned capsules that unify semantics, provenance, valid...
  </details>

- **2026-07-04** — Qitong Chu, Xunjie He, Chen Deng et al. — [NeSy-CSA: A Neuro-Symbolic Framework for Open-Ended Critical Scenario Attribution](http://arxiv.org/abs/2607.03847v1)
  <details><summary>📄 Abstract</summary>
  Understanding why discovered scenarios become critical in scenario-based testing is essential for effectively leveraging them in decision-making systems. Reasoning about such criticality can be formulated as an attribution problem. However, across different decision-making tasks, the causes of criticality may involve diverse state variables, interaction patterns, and failure mechanisms, making attribution an inherently open-ended problem beyond predefined explanation spaces. Existing attribution...
  </details>

- **2026-07-04** — Yingdong Yang, Haijian Wu — [Candidate-Constrained Retrieval-Augmented Generation for LongEval-RAG: System Design and Empirical Analysis](http://arxiv.org/abs/2607.04008v1)
  <details><summary>📄 Abstract</summary>
  We present a candidate-constrained retrieval-augmented generation system for LongEval-RAG, where each query is associated with an organizer-provided candidate set and all retrieved evidence and final citations must remain within that set. The system combines deterministic provenance tracking with passage-based retrieval, deterministic query expansion, pseudo-relevance feedback (PRF), reciprocal rank fusion (RRF), lightweight evidence reranking, citation-aware evidence aggregation, and optional M...
  </details>

- **2026-07-02** — Ziyun Qiao, Yue Min, Ruining Chen et al. — [HERMES: A Multi-Granularity Labeling Substrate for Pre-training Data Mixtures](http://arxiv.org/abs/2607.02266v1)
  <details><summary>📄 Abstract</summary>
  Most data-mixing methods assume the corpus has already been partitioned into groups, and the choice of those groups determines what a mixer can express. Existing labels, including provenance, topic or format taxonomies, and flat embedding clusters, commit to one semantic axis at one granularity; changing the resolution rebuilds the labels. We argue the bottleneck is the label system, not the mixer, and provide a hierarchical one. HERMES is a data-derived labeling substrate: a Learned Semantic Tr...
  </details>

- **2026-07-02** — Xue Qin, Simin Luan, Cong Yang et al. — [Episodic-to-Semantic Consolidation Without Identity Drift](http://arxiv.org/abs/2607.01988v1)
  <details><summary>📄 Abstract</summary>
  Long-running adaptive intelligent agents face a structural tension between knowledge consolidation and information integrity. Memory consolidation is conventionally treated as an agent-changing operation: a model is fine-tuned, a prompt rewritten, a policy distilled, or a reflection appended to the context that governs future behaviour. In regulated autonomic deployment this is a liability because the agent operates under commitments and audit contracts that bind to a specific, cryptographically...
  </details>

- **2026-07-01** — Dangxing Chen, Pengzhan Guo — [Shapley in Context: Explaining Financial Language with Domain Expertise](http://arxiv.org/abs/2607.00856v1)
  <details><summary>📄 Abstract</summary>
  In recent years, large language models have achieved remarkable success and have seen growing adoption in financial applications. At the same time, explainability remains critical in finance, a domain characterized by high stakes and strict regulatory requirements. Although numerous methods have been proposed to explain black box machine learning models, the majority of these approaches are designed for general purpose tasks and do not incorporate domain specific knowledge. In this work, we stud...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-07-02** — Gabriel Hurtado — [Has This Checkpoint Been Abliterated? A Two-Signal Audit and Its Failure Map](http://arxiv.org/abs/2607.01854v1)
  <details><summary>📄 Abstract</summary>
  Can a platform tell, before deployment, whether an open-weight checkpoint has had its refusal mechanism stripped? Runtime guards cannot: they score generations, not the artifact. We combine two cheap internal signals, a reference-anchored activation refusal-gap and a weight-recovery energy of the base-to-candidate weight difference, into a threshold-free checkpoint audit. The two are negatively correlated and label-complementary: the gap supplies refusal-specificity and the weight energy supplie...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 2 papers

- **2026-07-05** — Ke Li, Kaidi Liang, Yuxin Ding et al. — [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](http://arxiv.org/abs/2607.04451v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment. However, generating controllable safety-critical scenarios remains challenging. Existing approaches use soft guidance that provides only probabilistic preferences and cannot guarantee the satisfaction of geometric and severity constraints associated with specific collision types. We introduce Collision-Constrained Flow Matching (CCFM), a novel framework that guarantees...
  </details>

- **2026-07-02** — Joshua Penman — [Epistemic Goggles: A Pretrained Module that Induces an Epistemic Frame via Gradient Editing](http://arxiv.org/abs/2607.01690v1)
  <details><summary>📄 Abstract</summary>
  Finetuning a language model on documents that are explicitly annotated as fictional results in a model that still actually believes the documents' core claims, an effect known as Negation Neglect. In our evaluations, models trained on documents prefixed and suffixed with such annotations correctly identify the relevant claims as fictional only about 9% of the time. To address this, we introduce Goggles, a learned module that intervenes on the finetuning gradient rather than the data. During supe...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 6 papers

- **2026-07-05** — Faid Keddouri, Sohaib Houhou, Aissa Boulmerka et al. — [Regime-Conditional Stabilisation of LLM-Augmented Cooperative Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2607.04470v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) offer a natural interface for translating human objectives into reward signals for cooperative multi-agent reinforcement learning (MARL), yet the training-time dynamics of this integration remain poorly understood. We show that dynamically updating LLM-generated reward weights during off-policy MARL violates the stationarity assumption of Potential-Based Reward Shaping (PBRS) and contaminates the experience replay buffer, whose stored transitions carry reward labels ...
  </details>

- **2026-07-05** — Shiming Gu, Ziang Yan, Ludovic van Waerbeke et al. — [KiDS-Legacy: The consistency test of the large-scale structure with Bernardeau-Nishimichi-Taruya transform](http://arxiv.org/abs/2607.04384v1)
  <details><summary>📄 Abstract</summary>
  We perform the first $k$-cut cosmic shear analysis of the KiDS-Legacy survey. This method uses the Bernardeau-Nishimichi-Taruya (BNT) transform to construct weak-lensing kernels that are more localised than conventional ones, and remove information from selected physical scales while retaining the constraining power of the targeted range. Removing the scale of $k \geq 0.33~\mathrm{Mpc}^{-1}$ from the KiDS-Legacy pseudo-$C_\ell$ data vector, and using a covariance matrix whose Gaussian component ...
  </details>

- **2026-07-04** — Sadia Afroz, Courtney Miller, Tyler Menezes et al. — ["AI Slop is DDoSing Open Source": Understanding the Impact of AI-Generated Contributions on Open Source Sustainability](http://arxiv.org/abs/2607.04003v1)
  <details><summary>📄 Abstract</summary>
  Open source software (OSS) communities are facing increasing pressure from Generative AI (GenAI) tools. We call it AI-DDoS: a denial-of-service effect in which plausible but low-quality AI-generated contributions overwhelm OSS community capacity. Using a phenomenon-based mixed-methods approach, we first analyze practitioner accounts from Reddit, OSS mentor mailing lists, and blogs to identify six recurring themes and derive hypotheses. We then evaluate these hypotheses using Bayesian Structural ...
  </details>

- **2026-07-02** — Manuel Alonso-Carracedo, Ruben Fernandez-Boullon, Pedro Celard et al. — [Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach](http://arxiv.org/abs/2607.02432v1)
  <details><summary>📄 Abstract</summary>
  Scalable and reliable grading of command-line examinations remains a challenge in computing education, where rising enrolments make manual marking difficult and rule-based autograders cannot handle partial credit, equivalent solutions, or syntactic variation. This paper evaluates whether four frontier Large Language Models (GPT, Claude Opus, Gemini, and GLM) can approximate expert judgment when grading short Linux/bash command responses. The study adopts a four-level cognitive taxonomy that comb...
  </details>

- **2026-07-02** — Jose Afonso, Stergios Amarantidis, Stas Shabala et al. — [The Road to Identifying the Earliest Radio-Powerful AGN with the SKA](http://arxiv.org/abs/2607.02366v1)
  <details><summary>📄 Abstract</summary>
  The Epoch of Reionization (EoR) is one of the most pivotal frontiers in modern astrophysics, marking the emergence of the first galaxies, stars, and supermassive black holes (SMBHs). Despite insights from the Atacama Large Millimetre/submillimetre Array and the James Webb Space Telescope, we still struggle to explain how $\sim10^{9}$ M$_\odot$ SMBHs powering luminous active galactic nuclei (AGN) already exist by $z\sim7$. The recent discovery of powerful radio emission from some of these early A...
  </details>

- **2026-07-01** — Elias Najarro, Ane Espeseth, Eleni Nisioti et al. — [Conversable Complexity: Agentic LLM Collectives as Interpretable Substrates](http://arxiv.org/abs/2607.01047v1)
  <details><summary>📄 Abstract</summary>
  Complexity and interpretability rarely coincide: systems rich enough for complex behaviours to emerge are usually too opaque to question, while transparent ones are too simple for anything complex to emerge. A single large language model (LLM) is a static artefact, hardly exhibiting any of the emergent properties we associate with life. This changes through interaction: populations of LLMs display emergent dynamics absent from isolated models. Furthermore, LLMs can be endowed with persistent mem...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 156 papers

- **2026-07-06** — Mouhamed Amine Bouchiha, Gregory Blanc — [TACTIC-KG: Toward Small Agent Teams for Cyber Threat Intelligence Knowledge Graph Construction](http://arxiv.org/abs/2607.05001v1)
  <details><summary>📄 Abstract</summary>
  Cyber Threat Intelligence (CTI) reports are predominantly unstructured, heterogeneous, and noisy, which limits their direct usability for automated analysis and reasoning. Cybersecurity Knowledge Graphs (CSKGs) provide a structured representation of adversarial entities, actions, and relations, but constructing such graphs from free-text CTI remains a challenge. Recent approaches rely on monolithic Large Language Models (LLMs) to perform end-to-end extraction and completion, leading to high cost...
  </details>

- **2026-07-06** — Xue Qin, Simin Luan, Cong Yang et al. — [Governed Caste Reassignment in Heterogeneous Swarms: An Asymmetric-Trust Protocol with Audited Operator Countersignature](http://arxiv.org/abs/2607.04634v1)
  <details><summary>📄 Abstract</summary>
  In heterogeneous robot swarms, caste reassignment (rebinding a robot to a new capability-bound role) is a high-frequency runtime event driven by battery, payload, and priority changes. Existing approaches treat it as an internal allocation algorithm and do not expose the reassignment to external authority. We argue that for regulated embodied deployments a caste change that elevates a robot's privilege envelope is a governance event that must be auditable and externally authorised. We propose an...
  </details>

- **2026-07-06** — Jiaqi Peng, Xiqian Yu, Delin Feng et al. — [Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation](http://arxiv.org/abs/2607.05377v1)
  <details><summary>📄 Abstract</summary>
  While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable ...
  </details>

- **2026-07-06** — Sensen Gao, Zhaoqing Wang, Qihang Cao et al. — [PixWorld: Unifying 3D Scene Generation and Reconstruction in Pixel Space](http://arxiv.org/abs/2607.05373v1)
  <details><summary>📄 Abstract</summary>
  3D reconstruction and generation are commonly tackled by separate paradigms: pixel-based regression for reconstruction, and latent diffusion for generation. Recent works attempt to unify them in latent space, but with notable drawbacks: the diffusion objective is defined on latent features rather than the underlying 3D representation, and both branches suffer from information loss introduced by latent encoding, while requiring a pretrained Variational Autoencoder (VAE) or Representation Autoenco...
  </details>

- **2026-07-06** — Xianhao Chen, Jiarui Hu, Yuanbo Yang et al. — [Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis](http://arxiv.org/abs/2607.05348v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary 3D scene understanding aims to segment 3D scenes beyond predefined categories by transferring semantic knowledge from vision-language models. Existing methods have advanced this task by lifting language-aligned 2D features into 3D, yet they often rely on context-independent semantic representations, leaving object relationships underexplored for contextual refinement. We propose RelGraphOV, a relationship-aware framework that uses 3D scene graphs to enhance open-vocabulary 3D und...
  </details>

- **2026-07-06** — B. C. Low, S. W. McIntosh — [The steady incompressible ideal free-boundary flows of a hydromagnetic star](http://arxiv.org/abs/2607.05299v1)
  <details><summary>📄 Abstract</summary>
  This self-contained theoretical study treats incompressible, free-boundary flows in a gravitating, ideal hydromagnetic star abutting vacuum, centered on the steady field-aligned flows of Chandrasekhar, Prendergast and Tsinganos, together with a novel family of steady cross-field flows, all as solutions of the axisymmetric Tsinganos equation. In the absence of compressive waves and shocks, an incompressible fluid evolves by its frozen-in magnetic field propagating as transverse Alfvèn waves along...
  </details>

- **2026-07-06** — Avina Nakarmi, Sohom Sen, Xun Song et al. — [A Multimodal Reasoning Typology for Grounding Chart-Image Coherence in Science Communication](http://arxiv.org/abs/2607.05222v1)
  <details><summary>📄 Abstract</summary>
  Charts and images appear together throughout scientific publications, yet most computational work does not characterize their coherence. We argue that a chart, its accompanying image, and the caption that links them form a multimodal unit, and that the inferential work required to read it varies systematically. To capture this variation, we develop a typology of reasoning gaps, R1 through R5, that characterizes how chart, image, and text jointly convey a scientific claim, and the interpretive wo...
  </details>

- **2026-07-06** — Hafsteinn Einarsson, Hafsteinn Birgir Einarsson, Jón Gunnar Ólafsson et al. — [Curated retrieval versus open web search in public AI information services: a coverage-trust trade-off](http://arxiv.org/abs/2607.05217v1)
  <details><summary>📄 Abstract</summary>
  Public institutions increasingly use large language models (LLMs) to answer citizens' questions, often pairing a curated knowledge base with live web search, yet whether the sources behind these answers can be trusted has received little empirical scrutiny. We report a pre-launch expert evaluation of Evrópuvefur, an independent, government-funded service run by the University of Iceland that answers questions about the European Union, conducted as Iceland prepared for its referendum of 29 August...
  </details>

- **2026-07-06** — Xingze Gao, Chuanrui Hu, Hongda Chen et al. — [EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](http://arxiv.org/abs/2607.05202v1)
  <details><summary>📄 Abstract</summary>
  Agent self-evolution in long-horizon LLM systems is largely procedural: useful experience is not merely stored information, but reusable procedures for searching, debugging, and verification. Yet current evaluations do not isolate this form of transfer. Agent benchmarks test single-episode task solving; memory benchmarks target information retention rather than procedural reuse. We introduce EvoAgentBench, a benchmark for agent self-evolution via Ability-guided transfer across four agentic domai...
  </details>

- **2026-07-06** — Tianjia Yang, Ke Li, Ruwen Qin et al. — [VLM-CASE: Vision-Language Model Enabled Context-Adaptive Safety Envelopes for Anticipatory Safe Autonomous Driving](http://arxiv.org/abs/2607.05180v1)
  <details><summary>📄 Abstract</summary>
  Adverse driving conditions, such as bad weather, remain a principal barrier to autonomous driving because they degrade two things at once: what the vehicle can perceive and what it can physically do. Human drivers cope by anticipation, reasoning about the scene and re-budgeting speed, following distance, and steering before grip or sight is lost, whereas current autonomous driving systems at best react after the fact. This paper proposes VLM-CASE, a framework that gives an autonomous vehicle thi...
  </details>

- **2026-07-06** — Yurui Dong, Shu Zou, Siqi Li et al. — [ASSEMCAD: Production-Ready CAD Assembly Generation from Natural Language](http://arxiv.org/abs/2607.05123v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models and programmatic CAD have significantly improved Text-to-CAD generation for individual parts. However, production-ready mechanical assembly generation remains largely unsolved. Unlike single-part modeling, assemblies require coordinated reasoning over multiple components, functional interfaces, assembly relations, engineering principles, and physical consistency. Consequently, directly generating executable CAD code is insufficient for constructing mechan...
  </details>

- **2026-07-06** — Handong Li, Longteng Guo, Zikang Liu et al. — [TimeThink: Reasoning with Time for Video LLMs](http://arxiv.org/abs/2607.05089v1)
  <details><summary>📄 Abstract</summary>
  Video reasoning requires models to identify and verify temporally localized evidence within long video sequences. Recent Video Large Language Models (Video-LLMs) have shown promising reasoning abilities when aligned with reinforcement learning, yet existing approaches typically rely on outcome-based rewards that supervise only the final prediction. Such supervision provides limited guidance on how models should discover the relevant temporal evidence during intermediate reasoning. In this work, ...
  </details>

- **2026-07-06** — Saimir Bala, Fabiana Fournier, Lior Limonad et al. — [Using Process Mining to Generate AI Agents from Software Engineering Process Records](http://arxiv.org/abs/2607.04948v1)
  <details><summary>📄 Abstract</summary>
  Integrating AI agents into Software Engineering (SE) raises an important challenge: how can we specify and realize AI agents that work effectively alongside humans in hybrid SE teams? Determining the right granularity and separation of concerns for such agents is non-trivial. Coarse-grained agents may introduce unmanageable complexity, whereas micro-agents may create severe coordination overhead. Moreover, existing multi-agent SE frameworks typically rely on predefined role structures and do not...
  </details>

- **2026-07-06** — Yoshiyuki Ootani — [Input Pathways Shape Few-Shot, Not Zero-Shot, Binding in Tiny Transformers: A Fully-Enumerable Study](http://arxiv.org/abs/2607.04926v1)
  <details><summary>📄 Abstract</summary>
  How does the way information reaches a transformer -- as symbolic tokens, a clean per-factor "oracle" code, or an entangled perceptual vector -- shape whether it binds that information compositionally? We study ~6-10K-parameter transformers on finite factored worlds enumerated exhaustively, so every measurement covers the whole input space (zero sampling variance) and the informative routes are information-matched (exact Bayes ceiling 1.0). We report four findings. (1) Endpoint invariance: on he...
  </details>

- **2026-07-06** — Mohammed Saim Ahmed Quadri, Yunzhe Xue, Justin W. Ady et al. — [Medi-Gemma: A Hybrid Clinical Decision Support System Integrating Deterministic EMR Analytics and Retrieval-Augmented Generation](http://arxiv.org/abs/2607.04907v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Models (LLMs) in high-stakes clinical settings remains limited by structural hallucinations, weak deterministic reasoning over tabular patient data, and omissions in vector retrieval. This paper presents the architecture and validation of Medi-Gemma, a Clinical Decision Support System (CDSS) for wound pathology triage and workflow automation. The platform introduces a decoupled framework that separates clinical perception from data orchestration while preserving traceabl...
  </details>

- **2026-07-06** — Ming-Kuan Lin, Yi-Chung Lai, Ming-Hsin Chiang et al. — [RL-Ballast: Ship Ballast Water Path Planning and Clog Prediction via Reinforcement Learning](http://arxiv.org/abs/2607.04906v1)
  <details><summary>📄 Abstract</summary>
  Under the Shipping 4.0 paradigm, autonomous and reduced-crew vessels require intelligent internal systems to maintain operational safety and structural stability. Ballast-water control is essential for ship trim and integrity, but conventional rule-based or manual approaches have limited adaptability to hydraulic anomalies such as valve failures and pipe blockages, and often depend on dense pressure or flow sensors for diagnosis. To address these limitations, this paper proposes RL-Ballast, a gr...
  </details>

- **2026-07-06** — Yuan Jiang, Ningyuan Zhang, Xicun Yang et al. — [Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control](http://arxiv.org/abs/2607.04837v1)
  <details><summary>📄 Abstract</summary>
  Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient ex...
  </details>

- **2026-07-06** — Tianhao Niu, Qingfu Zhu, Wanxiang Che — [What You See Is What You Get: Observation-Aligned Supervision for Chart-to-Code Generation](http://arxiv.org/abs/2607.04726v1)
  <details><summary>📄 Abstract</summary>
  Chart-to-code generation is commonly trained with supervised fine-tuning on reference plotting scripts, implicitly treating the gold code as a fully observable target. We argue that this assumption is often invalid: many chart programs contain latent raw variables that cannot be uniquely recovered from the rendered image. For example, a boxplot exposes summary statistics rather than original samples, a pie chart reveals proportions rather than arbitrary raw values, and a histogram shows bin-leve...
  </details>

- **2026-07-06** — Daeyeon Son — [Elastic Gang: Per-Token Membership Change for a Hard-Barriered LLM Inference Gang Co-Scheduled with OS Processes](http://arxiv.org/abs/2607.04668v1)
  <details><summary>📄 Abstract</summary>
  On-device LLM decoding is a hard-barriered CPU-SIMD computation that wants every core for milliseconds per token, while the rest of the OS wants those same cores continuously. A barriered gang cannot simply be dropped into a preemptive scheduler: an unannounced departure deadlocks a barrier, and an unannounced arrival silently corrupts logits. I present the elastic gang of Anima OS, a bare-metal x86-64 Rust kernel in which the inference gang is a first-class schedulable entity whose core members...
  </details>

- **2026-07-06** — Shuangyu Xie, Kaiyuan Chen, Ziyang Chen et al. — [RoboVista: Evaluating Vision Language Models for Diverse Robot Applications](http://arxiv.org/abs/2607.04610v1)
  <details><summary>📄 Abstract</summary>
  Diverse applications for robotics, such as industry and agriculture, require robots to operate across various embodiments, changing visual conditions, and complex planning. Vision-Language Models (VLMs) offer a promising foundation for general-purpose and interpretable robotic reasoning. Aligning VLMs with diverse robot applications requires a modular understanding of the individual decision components that underlie robotic behavior. Capturing such structure is challenging for conventional robot...
  </details>

- **2026-07-06** — Yang Zhou, Jianwen Chen, Ruipeng Wei — [Square-Root Price Impact Is Necessary for Endogenous Manipulation Cycles in Learning-Agent Markets](http://arxiv.org/abs/2607.05141v1)
  <details><summary>📄 Abstract</summary>
  We study a minimal agent-based market in which a single evolutionary-optimized institutional agent interacts with 20{,}000 herding retail traders. The agent spontaneously discovers a multi-cycle predatory strategy, producing 8--11 complete cycles over 2000 trading days with total portfolio return of $+51\%$ (best of 20 seeds; mean $+37.7\%$). Mean-field reduction maps the system onto a nonlinear oscillator that undergoes two distinct bifurcations: a continuous Hopf transition as institutional ca...
  </details>

- **2026-07-06** — Amal Akli, Melissa Akli, Cedric Richter et al. — [From Failing to Passing: Evolving Natural Language Prompt Optimization Rules for LLM Code Generation](http://arxiv.org/abs/2607.05121v1)
  <details><summary>📄 Abstract</summary>
  Large language models are known to be sensitive to prompt formulation. Even minor variations in wording can substantially degrade performance. This sensitivity reveals an opportunity: if prompt phrasing can harm performance, can it be used to improve it? To investigate this question, we introduce a search-based approach that identifies and evolves a set of natural language transformation rules with strong downstream effects on coding performance. We then propose DUALFIX, a staged repair pipeline...
  </details>

- **2026-07-06** — Nikolaos Xiros, Maria-Eleni Zoumpoulidi, Georgios Paraskevopoulos — [Knowledge Knows, Verbalization Tells: Disentangling Latent Directions for Mathematical Solvability in LLMs](http://arxiv.org/abs/2607.05013v1)
  <details><summary>📄 Abstract</summary>
  Although LLMs have made significant progress in mathematical reasoning, determining whether a mathematical problem is solvable remains a fundamental yet challenging capability. While recent studies have probed internal representations of model solvability beliefs, verbalization has primarily been studied behaviorally rather than as an internal representation, limiting its analysis and manipulation. We address this gap by separately probing representations of solvability knowledge and verbalizati...
  </details>

- **2026-07-06** — Jian Zhu, Jianjun Zhang, Taiyi Su et al. — [DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation](http://arxiv.org/abs/2607.04927v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) provide a promising alternative to Vision-Language-Action (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step goals, where coarse user commands need to be converted i...
  </details>

- **2026-07-06** — Yu Wang, Yong Cao, Kan Dai et al. — [Enhancing the Forecasting Capability of Multi-Model Blending Algorithms for Extreme Precipitation via Joint Use of Station and Gridded Observations](http://arxiv.org/abs/2607.04862v1)
  <details><summary>📄 Abstract</summary>
  Accurate extreme precipitation forecasting is critical for disaster mitigation but remains challenging for numerical weather prediction (NWP) models due to systemic intensity underestimation and spatial displacement. Traditional precipitation multi-model blending algorithms perform pixel-by-pixel blending on the forecast field based on weights, which may lead to the expansion of precipitation areas and the smoothing of extreme values. This study proposes an U-Net based two-stage framework: proba...
  </details>

- **2026-07-06** — Antonio Franchi — [Aerial Manipulation: Contact, Medium Coupling, and the Geometry of Readiness](http://arxiv.org/abs/2607.04719v1)
  <details><summary>📄 Abstract</summary>
  Aerial robots are increasingly moving from remote observation toward physical interaction with objects, surfaces, structures, loads, and surrounding flows. This review argues that aerial manipulation cannot be understood as classical manipulation simply mounted on a flying base. Because flying agents remain aloft through continuous momentum and energy exchange with the surrounding medium, support, locomotion, stabilization, and task-directed interaction are intrinsically coupled. Building on bro...
  </details>

- **2026-07-06** — Xinyu Shao, Keru Zhou, Guowei Huang et al. — [KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation](http://arxiv.org/abs/2607.04652v1)
  <details><summary>📄 Abstract</summary>
  Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinem...
  </details>

- **2026-07-06** — Theodore O. Cochran — [Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation](http://arxiv.org/abs/2607.04576v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly answer questions against knowledge bases they help maintain. A common intuition holds that progressive disclosure, a compact catalog plus a one-line summary per page so the agent loads only what it needs, should make this cheaper than consulting a large monolithic index. We test that on a real 709-page markdown wiki maintained by an LLM. We retrofit it for progressive disclosure and run a preregistered ablation in which four versions of the corpus differ only in how the a...
  </details>

- **2026-07-06** — Mohamed Amine Merzouk, Dmitri Carpov, Mirko Bronzi et al. — [How Much is Left? LLMs Linearly Encode Their Remaining Output Length](http://arxiv.org/abs/2607.05316v1)
  <details><summary>📄 Abstract</summary>
  Large language models generate one token at a time, yet their responses show remarkably consistent length structure: step-by-step solutions converge in predictable token counts, retrievals stop after a few sentences, retractions extend responses by measurable amounts. We ask whether the model carries an internal estimate of how much response remains. Training minimal-capacity linear probes on frozen hidden states of three open-weight 7-8B models across seven completion-style datasets, we find th...
  </details>

- **2026-07-06** — Guli Zhu, Chenwei Wu, Liyue Shen — [Evaluating and Understanding Model Editing for Medical Vision Language Models](http://arxiv.org/abs/2607.05310v1)
  <details><summary>📄 Abstract</summary>
  Model editing promises a fast, targeted way to correct post-deployment mistakes in medical vision-language models (VLMs) without costly retraining. However, existing multimodal model editing benchmarks focus on general-purpose tasks and do not reflect realistic clinical domain requirements and variability. To address this, we introduce M3Bench, a clinically grounded benchmark for multimodal model editing that evaluates whether an edit remains reliable, precise, and generalizable under the challe...
  </details>

- **2026-07-06** — Guorun Wang, Simone Foti, Andreas D. Demou et al. — [Air Quality Downscaling with Station-Guided Pseudo-Supervision](http://arxiv.org/abs/2607.05292v1)
  <details><summary>📄 Abstract</summary>
  Super-resolving coarse atmospheric fields to local PM$_{2.5}$ variations is uniquely challenged by a mismatch in spatial support: while pixels represent regional averages, ground-truth observations are discrete, unaligned samples of a continuous spatial signal. To bridge this gap, we present a station-guided framework for high-resolution PM$_{2.5}$ downscaling over Europe. Taking coarse CAMS atmospheric composition fields alongside heterogeneous side information (i.e., human activity, land cover...
  </details>

- **2026-07-06** — Alessio Brini — [Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks](http://arxiv.org/abs/2607.05291v1)
  <details><summary>📄 Abstract</summary>
  We ask whether pretrained time series foundation models (TSFMs) improve on established econometric benchmarks for forecasting realized volatility. Using the VOLARE dataset, we conduct the first systematic comparison of nine zero-shot TSFMs against eight econometric specifications, including the Heterogeneous Autoregressive (HAR) family, across 50 assets in equities, foreign exchange, and futures, and three forecast horizons, with formal pairwise and multi-model forecast-comparison tests. Foundat...
  </details>

- **2026-07-06** — Parth Upman, Nishita Jain, Shreyank N Gowda — [Erasing Without Collateral Damage: Precise Concept Removal in Diffusion Models](http://arxiv.org/abs/2607.05274v1)
  <details><summary>📄 Abstract</summary>
  Training-free concept erasure is an attractive mechanism for controlling text-to-image diffusion models, but precise erasure often comes at the cost of damaging semantically related non-target concepts. Existing value-space methods remove the component of each cross-attention value along the target concept direction, implicitly treating target identity and shared visual structure as the same signal. We argue that this is the source of much of the collateral damage in prior preservation. We intro...
  </details>

- **2026-07-06** — Mohamed Shalma, Amr Mansour, Ahmed El-Mahdy — [Optimal Base Station Placement for Beyond 5G Networks with Non-Convex Topology](http://arxiv.org/abs/2607.05210v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the optimal placement of a millimeter-wave (mmWave) base station (BS) within a realistic U-shaped environment with non-convex topology. The problem is challenging and NP-hard due to the non-convex topology and the non-convex objective functions which are the sum-rate maximization and max-min fairness, the latter being additionally non-smooth. To address this challenge, the BS placement is formulated as a Markov Decision Process (MDP). Then, we propose two deep reinforceme...
  </details>

- **2026-07-06** — André Silva, Han Tu, Martin Monperrus — [Latent Programming Horizons in Coding Agents](http://arxiv.org/abs/2607.05188v1)
  <details><summary>📄 Abstract</summary>
  A coding agent solving a software-engineering task spends dozens of steps reasoning, editing code, and running tests, yet little is known about what the underlying language model internally represents about the program it is working on. We show that the residual streams of language models under coding agents linearly encode properties of the evolving program: a logistic-regression probe on hidden states is able to decode whether the current code parses, passes its test suite, reduces the number ...
  </details>

- **2026-07-06** — Omer Moussa, Mariya Toneva — [RABBiT: Rapidly adaptive BOLD foundation model via brain-tuning for accurate zero-shot and few-shot prediction of speech-elicited responses in the brain](http://arxiv.org/abs/2607.05171v1)
  <details><summary>📄 Abstract</summary>
  Language understanding in the brain is context-dependent, varying across experimental stimuli and individuals, which makes it difficult to build computational models that generalize across both. This calls for a foundation model of language-evoked brain activity that can capture shared structure while adapting efficiently to new participants and inputs. We introduce RABBiT (Rapidly Adaptive BOLD foundation model via BraIn-Tuning), a compact audio-to-fMRI encoder designed for accurate zero- and f...
  </details>

- **2026-07-06** — Mark de Rooij — [Smooth Reduced Rank Regression with P-splines](http://arxiv.org/abs/2607.05096v1)
  <details><summary>📄 Abstract</summary>
  Linear regression is one of the core statistical tools used for analysis of data. In the era of statistical learning, linear regression has been expanded into two directions. The first is regularisation, where penalties are added to the loss function to obtain more stable or sparse solutions. The second direction is basis expansion, such as with spline or kernel functions, where the linearity assumption is dropped. In practice, empirical researchers often collect multiple outcome variables. Regr...
  </details>

- **2026-07-06** — Manuela Del Castillo Suero, Arnault-Quentin Vermillet, Nicole Sonne Heckmann et al. — [Multi-Large Language Model Orchestrated Severity Assessment of Clinical Records (MOSAIC)](http://arxiv.org/abs/2607.05032v1)
  <details><summary>📄 Abstract</summary>
  Background: Disease severity is a multidimensional construct difficult to capture with rule-based approaches in Electronic Healthcare Records (EHR). Agentic large language model (LLM) systems could synthesise clinical evidence and reason over EHRs, but remain unevaluated for this task. Methods: MOSAIC is a two-phase agentic LLM framework for severity phenotyping, using type 2 diabetes (T2D) as a proof-of-concept. MOSAIC was evaluated on a synthetic cohort (SyntheticMass; open-weight N = 4,886; c...
  </details>

- **2026-07-06** — Helena Mihaljević, Jolanda Beer, Mareike Lisker et al. — [Who's Behind It? Annotating and Extracting Conspiratorial Actors from German Telegram Posts](http://arxiv.org/abs/2607.04962v1)
  <details><summary>📄 Abstract</summary>
  Conspiracy theories commonly attribute important events to the actions of powerful and secretive actors. While computational research has largely focused on document-level analyses of conspiracy theories, less attention has been paid to identifying the actors that drive such narratives. We develop annotation guidelines for conspiratorial actors, present a span-annotated corpus of German Telegram posts, and investigate their automatic extraction using transformer-based models. We further apply th...
  </details>

- **2026-07-06** — Yang Yang, Run-Yu Lei, Jian-Ping Zhou et al. — [Different dielectric, magnetic, and magnetodielectric mechanisms in M-type BaFe12O19 hexaferrite regulated by doping Ga3+ and In3+ cations](http://arxiv.org/abs/2607.04861v1)
  <details><summary>📄 Abstract</summary>
  We systematically investigated the magnetic, dielectric, and MD properties of BaFe12-xMexO19 ceramics prepared by a solid-state reaction method. The Ga3+ cations with a smaller radius preferentially substitute the Fe3+ ions in FeO6 octahedra while the In3+ cations with a larger radius tend to replace the Fe3+ ions in FeO5 bipyramids of R blocks, inducing different physical characteristics. The pure BaFe12O19 and Ga-doped samples show ferrimagnetism in the temperature range from 10 K to 300 K. Th...
  </details>

- **2026-07-06** — Xujun Che, Xiuxia Du, Depeng Xu — [MARLIN: De Novo Molecular Structure Elucidation from Tandem Mass Spectra without a Ground-Truth Formula](http://arxiv.org/abs/2607.04774v1)
  <details><summary>📄 Abstract</summary>
  Untargeted tandem mass spectrometry (MS/MS) detects thousands of small molecules per biological sample, yet most go unidentified because they are absent from spectral libraries. These uncharacterized metabolites and natural products are precisely the compounds that matter for drug discovery, biomarker research, and exposomics. Computational de novo structure elucidation could close this gap, but almost all state-of-the-art methods assume the ground-truth molecular formula is known, an oracle tha...
  </details>

- **2026-07-06** — Na Liu, Chang Li, Yujia Gu et al. — [Stabilized Higher-Order Influence Functions: Statistical Theory of a Class of Bilinear Forms](http://arxiv.org/abs/2607.04743v1)
  <details><summary>📄 Abstract</summary>
  Higher-order influence functions, introduced in a series of articles (Robins et al., 2008, 2009a; van der Vaart, 2014; Robins et al., 2016, 2023; Liu et al., 2017), are a unified framework for constructing rate-optimal point estimates of a class of statistical functionals, under various complexity-reducing assumptions on the posited statistical model that generates the observed data. Although higher-order (influence functions) estimators are theoretically appealing, they have very limited practi...
  </details>

- **2026-07-06** — Yu Wei, Yukiko Ogura, Yoshiyuki Ohmura et al. — [Integrated Altruistic and Fairness Preference Induces Advanced Mutual Cooperation in Sequential Social Dilemmas](http://arxiv.org/abs/2607.04710v1)
  <details><summary>📄 Abstract</summary>
  Inducing cooperation among distributed agents is still a difficult problem in the field of multi-agent reinforcement learning (MARL), particularly in social dilemma situations. There, individual interests are misaligned with the common good and individual rationality leads to suboptimal group outcomes. In contrast, humans are able to achieve cooperation with one another in such situations. A common explanation for such cooperative behavior is that individuals have social preferences. In order to...
  </details>

- **2026-07-06** — Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev et al. — [URSA: Chemistry-Aware Benchmark for Utilitarian Retrosynthesis Assessment](http://arxiv.org/abs/2607.04688v1)
  <details><summary>📄 Abstract</summary>
  Synthesis planning aiming to find pathways of reactions for a target molecule is one of the most important and challenging tasks in drug discovery. Recent progress has produced both specialized deep-learning retrosynthesis systems and general-purpose large language models, but objective comparison remains difficult due to the lack of flexible, chemically interpretable benchmarking protocols. In the current study, we are introducing the URSA (Utilitarian RetroSynthesis Assessment) evaluation fram...
  </details>

- **2026-07-06** — Jiaxing Qi, Zhongzhi Luan, Hongyu Zhang et al. — [Can LLMs Really Recover Microservice Failures? A Recovery-Aware Evaluation of Diagnosis-to-Action Reasoning](http://arxiv.org/abs/2607.04623v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to interpret operational evidence and assist incident response in cloud-native microservice systems. However, recovery-oriented use cases require more than identifying a root cause. After observing symptoms and diagnosing a fault, an operator or agent must translate the diagnosis into a concrete recovery action, apply it to an admissible target, and verify that service health has been restored. Existing RCA and log-analysis evaluations are well-...
  </details>

- **2026-07-06** — Riccardo Renzulli, Gabriele Spadaro, Shruthi Gowda et al. — [TORINO: Token Reduction via Interpretable Concept Overlap in Vision-Language Models](http://arxiv.org/abs/2607.04593v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have demonstrated impressive capabilities across different tasks, but their computational cost is dominated by the large number of visual tokens fed to the language model. Existing token reduction methods rely on attention-based scores or pairwise similarity, without an explicit semantic representation of each token. We introduce TORINO (TOken Reduction via Interpretable coNcept Overlap), a plug-and-play framework for adaptive visual token reduction in VLMs that req...
  </details>

- **2026-07-06** — Saurabhsingh Rajput, Tushar Sharma — [Beyond the Need for Speed: Energy-Aware Code Generation via Simulation-Guided Reinforcement Learning](http://arxiv.org/abs/2607.04577v1)
  <details><summary>📄 Abstract</summary>
  Code models strictly prioritize functional correctness, leaving software energy efficiency as an unoptimized byproduct. Training models to generate energy-efficient code requires reproducible feedback at scale, which physical hardware measurement cannot reliably provide due to variance.   In this paper, we replace hardware profiling with a deterministic architectural simulation harness to build Green Tea, a corpus of $3.5$ million evaluations across $1{,}474$ C++ problems. We train an energy-awa...
  </details>

- **2026-07-06** — Yeganeh Bahoo, Sajad Saeedi, Roni Sherman — [An Exact Generalized k-Cell Decomposition](http://arxiv.org/abs/2607.04561v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces an exact $k$-cell decomposition for visibility planning in polygonal environments for agents equipped with $k$-modems, devices that can see through up to $k$ walls. Unlike prior decompositions that may include redundant partition lines, our proposed method ensures that visibility events (appear, disappear, merge, and split) are guaranteed to occur on every line of the decomposition. By eliminating these redundancies, we achieve an $O(n^4)$ complexity , representing a potent...
  </details>

- **2026-07-06** — Islam Eldifrawi, Shengrui Wang, Amine Trabelsi — [Can temporal article-level credibility signals improve domain-level credibility prediction?](http://arxiv.org/abs/2607.04560v1)
  <details><summary>📄 Abstract</summary>
  Web domain credibility evaluation is vital for combating misinformation. It is conducted by examining factors such as domain type, transparency, and overall reputation. However, assessing the credibility of newly emerging web domains remains challenging since they have no reputation yet. Expert fact-checkers evaluate the credibility of domains by analyzing the content of their articles, including the presence of misinformation, bias, or propaganda. Yet, the ease of large-scale content generation...
  </details>

- **2026-07-05** — Hao Wei, Wenjin Qi, Dasen Dai et al. — [IRIS: An Intelligent Vision-Language System for Ocular Surface Diseases via Topic Tree and Scene-Driven VQA Generation](http://arxiv.org/abs/2607.04344v1)
  <details><summary>📄 Abstract</summary>
  While Large Vision-Language Models (VLMs) demonstrate remarkable generic capabilities, their clinical reasoning in specialized domains like ocular surface diseases (OSDs) is severely hindered by a paucity of high-fidelity, multimodal instruction-tuning data. To dismantle this data bottleneck, we introduce IRIS, an Intelligent Recognition and Interaction System tailored for fine-grained OSD understanding via external eye photography. First, we curate IRIS-120K, the largest and most comprehensive ...
  </details>

- **2026-07-05** — Yaozu Wu, Wei-Chieh Huang, Jizhou Guo et al. — [HAS-Bench: Evaluating LLM-Based Human-Agent Systems under Configurable Human Participation](http://arxiv.org/abs/2607.04329v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly operate in settings where humans are active collaborators rather than passive task providers. We introduce HAS-Framework, a graph-based framework that represents humans and LLM-powered agents as first-class participants with explicit roles, permissions, communication paths, and action authority. Building on this framework, HAS-Bench evaluates Human-Agent Systems under configurable human participation across agency levels, interaction channels, and persona polic...
  </details>

- **2026-07-05** — Jiang Zhang, Bing Yuan, Qian Zhang — [Self-Reference in Large Language Models: The Introspection Threshold for Recursive Self-Improvement](http://arxiv.org/abs/2607.04277v1)
  <details><summary>📄 Abstract</summary>
  The pursuit of self-evolving AI raises a critical question: when is autonomous self-improvement sustainable rather than degenerative? Drawing an analogy to von Neumann's complexity threshold for self-reproducing automata, we argue that sustainable recursive self-improvement in Large Language Models (LLMs) requires a functional analogue: introspection -- the system's capacity to simulate its own operations and target modifications. Grounded in Kleene's Second Recursion Theorem, we demonstrate the...
  </details>

- **2026-07-05** — Badrinath Singhal, Srihari K G, Sreehari Iyer et al. — [AdaptiveSplat:Texture Aware Controllable 3D Gaussian Allocation for Feed-Forward Reconstruction](http://arxiv.org/abs/2607.04256v1)
  <details><summary>📄 Abstract</summary>
  Current feed-forward 3D reconstruction methods predict pixel aligned Gaussian primitives, resulting in highly redundant representations. A natural solution is to prune the redundant Gaussians, but naive pruning introduces severe artifacts and often requires inference time fine-tuning, breaking the feed-forward paradigm. Based on previous works, high frequency regions require more Gaussian primitives, while low frequency regions can be represented with significantly fewer primitives. Motivated by...
  </details>

- **2026-07-05** — Guangyu Lei, Tianhao Liang, Bingyan Xie et al. — [Towards Effcient Low Altitude Sensing: A Dual Heterogeneous Graph Learning Method for UAV Task Allocation](http://arxiv.org/abs/2607.04255v1)
  <details><summary>📄 Abstract</summary>
  With the development of low altitude intelligent systems, multiple unmanned aerial vehicles (UAVs) can collaboratively execute more complex tasks. Conventional task allocation methods usually regard tasks and UAVs as isolated entities, making it difficult to capture task dependencies and UAV communication relationships. To address this issue, this paper proposes a dual heterogeneous graph learning based UAV task allocation method. A directed task graph is constructed to represent task dependenci...
  </details>

- **2026-07-05** — Arthur Plaud, P. L. Krapivsky, S. Redner et al. — [Universal fluctuations of first discoveries in competitive exploration](http://arxiv.org/abs/2607.04252v1)
  <details><summary>📄 Abstract</summary>
  Random exploration is usually quantified by how fast new space is found, from   the range of a single walker to the territory collectively covered by many   walkers. In competitive exploration, first arrival secures an exclusive resource, as when foragers compete for food items or agents capture distributed targets. It is then no longer enough to know which sites have been discovered: one must determine, for each discovered site, which searcher reached it first. We introduce the discovery   shar...
  </details>

- **2026-07-05** — Qiang Chen, Xiao Wang, Hao Si et al. — [Hierarchical Multi-to-Single-Modal Knowledge Distillation for Disruption Prediction in EAST](http://arxiv.org/abs/2607.04241v1)
  <details><summary>📄 Abstract</summary>
  Plasma disruption is a critical threat to tokamak safety. Existing data-driven predictors mainly rely on time-series diagnostic signals, while visible images provide complementary spatial cues including plasma deformation, local brightening, and radiation-structure evolution. Although the image modality improves the model's discriminative capability, it also substantially increases the computational cost during inference. To address this issue, we propose a hierarchical multi-to-single-modal kno...
  </details>

- **2026-07-05** — Riccardo O. Feingold, Davide Liconti, Chenyu Yang et al. — [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](http://arxiv.org/abs/2607.04546v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned world models allow robots to predict the future consequences of candidate actions without additional physical interaction, supporting policy evaluation, planning, and data augmentation. We present Mask2Real-WM, a two-stage action-conditioned world model for dexterous manipulation that decouples pixel prediction into a dynamics model and a rendering model. The dynamics model predicts future segmentation masks from past masks and 23-DoF action sequences. The rendering model maps...
  </details>

- **2026-07-05** — Damir Shodiev, Aleksei Staroverov, Nikita Kachaev et al. — [VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models](http://arxiv.org/abs/2607.04517v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models are commonly treated as end-to-end action policies conditioned on natural-language task descriptions. In practice, however, their behavior often depends sharply on how the instruction is phrased, suggesting that language is not merely a task label but an optimizable conditioning input. We study whether frozen VLA policies can be improved by optimizing language space rather than updating action weights. Our method introduces a language-conditioning space policy...
  </details>

- **2026-07-05** — Fan Feng, Yujia Zheng, Minghao Fu et al. — [Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling](http://arxiv.org/abs/2607.04409v1)
  <details><summary>📄 Abstract</summary>
  Learning and planning in imagination using world models provides an effective paradigm for training agents for decision-making. However, existing approaches often rely on high-dimensional latent spaces or generic visual embeddings that retain many factors irrelevant to control, limiting efficiency and generalization across tasks. To this end, we study how agents can learn world models with representations that are task-specific, minimal, and sufficient for decision-making. We achieve this via a ...
  </details>

- **2026-07-05** — Lei Iok Tong, Qingchen Xie, Wei Huang et al. — [XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching for Lightweight Robotic Control](http://arxiv.org/abs/2607.04171v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) have shown strong multimodal understanding and spatial grounding, but their computational cost limits real-time robotic control. In contrast, lightweight models are suitable for edge deployment but often suffer from "spatial blindness", namely weak native spatial prediction ability. Training Vision-Language-Action (VLA) models on mixed human demonstrations can also degrade policy performance due to highly diverse behaviors. To address these limitations, we pr...
  </details>

- **2026-07-05** — Dongliang Zheng, Zhipeng Wang, Siqi Wang et al. — [Conflict-Based Lazy Search for Fast Multi-Manipulator Planning](http://arxiv.org/abs/2607.04124v1)
  <details><summary>📄 Abstract</summary>
  Employing multiple manipulators can boost efficiency and accomplish tasks that a single manipulator cannot do. However, real-time planning for multiple manipulators in a cluttered workspace still poses significant challenges for planning algorithms. This article proposes a new planning algorithm called Conflict-Based Lazy Search (CBLS) for multimanipulator planning. CBLS is built on Conflict-Based Search (CBS), an efficient multiagent pathfinding (MAPF) algorithm that has shown an order of magni...
  </details>

- **2026-07-05** — Md Asaduzzaman Noor, John W. Sheppard, Jason A. Clark — [Evaluation and Explainability of Unsupervised Scholarly Collaboration Recommendations](http://arxiv.org/abs/2607.04529v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we examine unsupervised, content-based collaboration recommendations using publication text in scholarly settings. We compare three families of methods: a TF-IDF baseline, topic-based models (LDA and BERTopic, including clone variants), and embedding-based retrieval using SciBERT with Faiss. To evaluate model behavior beyond simple lexical matching, we introduce a constrained setting where publication overlap between researchers is partially removed while still using historical co...
  </details>

- **2026-07-05** — Phuong Tuan Dat, Qi Li, Xinchao Wang — [dOPSD: On-Policy Self-Distillation for Diffusion Language Models](http://arxiv.org/abs/2607.04428v1)
  <details><summary>📄 Abstract</summary>
  Diffusion large language models (dLLMs) generate text by iteratively denoising a masked sequence, offering a parallel alternative to autoregressive models, but eliciting strong reasoning through post-training remains difficult: supervised fine-tuning is off-policy and suffers from exposure bias, while reinforcement learning gives only sparse, sequence-level rewards and is hard to apply without tractable sequence likelihoods. On-policy self-distillation (OPSD) offers a promising alternative, usin...
  </details>

- **2026-07-05** — Zhenhao Chen, Yongqiang Chen, Chenxi Liu et al. — [CausalGame: Benchmarking Causal Thinking of LLM Agents in Games](http://arxiv.org/abs/2607.04293v1)
  <details><summary>📄 Abstract</summary>
  Building AI Scientist agents with Large Language Models (LLMs) has recently attracted growing attention. Since scientific discovery fundamentally relies on uncovering causal relationships from observations, the capability of causal thinking, i.e., distinguishing causation from correlation and recognizing hidden biases, is essential to LLM agents. Although a number of benchmarks exist for AI Scientists, none explicitly incorporate challenges from selection bias, measurement error, and hidden conf...
  </details>

- **2026-07-05** — Hongchen Li, Bohao Wang, Jingbang Chen et al. — [LBR: Towards Mitigating Length Bias in Large Language Models for Recommendation](http://arxiv.org/abs/2607.04270v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently emerged as powerful backbones for recommender systems by reformulating recommendation as a token-level generation task. Despite their promise, we identify a pervasive yet underexplored issue: $\textit{Length Bias}$. Because items are represented by textual descriptions of varying lengths, LLM-based recommenders can be systematically biased in two ways. On the input side, longer item descriptions occupy more tokens in the context and thus receive disprop...
  </details>

- **2026-07-05** — Girum Abebe Beyene, Inam Mirza, Jijil JJ Nivas et al. — [Enhanced LIBS Emission Using Laser Beam Splitting: Interacting Multi-Plume Plasma Dynamics](http://arxiv.org/abs/2607.04229v1)
  <details><summary>📄 Abstract</summary>
  The optical emission in laser-induced breakdown spectroscopy (LIBS) is governed by the spatial intensity distribution of the incident laser beam, which influences plasma formation and evolution. Beam shaping therefore offers a route to control plasma dynamics and emission yield; however, its effects in LIBS remain insufficiently quantified, particularly under conditions relevant to compact instrumentation. In this work, a diffractive optical element (DOE) is used to transform a Gaussian beam int...
  </details>

- **2026-07-05** — Yinsheng Yao, Yan Liu, Chen Ye — [HCSU: A Dataset and Benchmark for Fine-Grained Historical Calligraphy Style Understanding](http://arxiv.org/abs/2607.04147v1)
  <details><summary>📄 Abstract</summary>
  Automated fine-grained perception of calligraphy styles--a task vital to cultural heritage preservation--remains a critical challenge for Large Vision-Language Models (LVLMs), largely constrained by existing datasets that suffer from modal mixture and flattened labels. To bridge this gap, we introduce HCSU, the first comprehensive dataset tailored for fine-grained Historical Calligraphy Style Understanding. HCSU comprises 39,307 meticulously curated character images from 49 historically prominen...
  </details>

- **2026-07-05** — Hew Phipps, Matteo Cagiada, Santiago D. Villalba et al. — [Spectral Diffusion for Protein Dynamics](http://arxiv.org/abs/2607.04134v1)
  <details><summary>📄 Abstract</summary>
  Generative models present a promising alternative to expensive molecular dynamics for computationally querying protein dynamics, yet many existing approaches treat ensembles as unordered snapshots rather than temporally coherent trajectories, or scale poorly with protein size. We present a new physics-informed representation using Fourier transforms as an inductive bias for the multiscale temporal nature of protein dynamics. Diffusion in the spectral domain allows for disentangling of dynamics i...
  </details>

- **2026-07-05** — Ritam Basu — [The Normalised Wigner Negativity Rate as a Second-Moment Probe of Infall in AdS$_3$](http://arxiv.org/abs/2607.04065v1)
  <details><summary>📄 Abstract</summary>
  In spread complexity, the average position of an operator along its Krylov chain, recovers the right radial momentum of an infalling particle in AdS, yet it is a measure of the first moment, irrespective of the spread of the wavepacket away from its classical trajectory. The rate of a normalized Krylov-Wigner negativity can be proposed as a diagnostic of the second moment of the boundary state that captures this spreading. Starting with the \emph{seed-normalized} Krylov-Wigner distribution -- th...
  </details>

- **2026-07-04** — Jae Hyung Ju, Euijun Chung, Hritvik Taneja et al. — [TileLens: Efficiently Using Large-Granularity Memory Systems with Transparent Two-Dimensional Memory Layout](http://arxiv.org/abs/2607.04031v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) inference is bottlenecked by the capacity and bandwidth of GPU High-Bandwidth Memory (HBM). Recent proposals, such as High-Bandwidth Flash (HBF) and RoMe, offer higher capacity or bandwidth than HBM, but require a minimum access granularity of kilobytes. We show that these Large-Granularity Memory Systems (LGMS) can degrade the performance of tiled matrix-multiplication, which is the dominant operation in LLM inference, by up to an order of magnitude. The root cause of...
  </details>

- **2026-07-04** — Weizhi Nie, Shaojin Bai, Weijie Wang et al. — [Patient-Conditioned Dual Hypergraph Reasoning for Auditable Traditional Chinese Medicine Prescription Support](http://arxiv.org/abs/2607.04025v1)
  <details><summary>📄 Abstract</summary>
  Traditional Chinese medicine (TCM) prescription support requires patient-specific reasoning from clinical narratives to syndromes, treatment principles, herbs, and doses. Direct language-model generation can produce fluent prescriptions, but its decisions are difficult to audit against explicit clinical evidence. Static TCM knowledge resources provide useful priors, but they cannot determine which diagnostic and prescription relations should be emphasized for an individual patient. We propose a ...
  </details>

- **2026-07-04** — Nelson Padilla, Ivan Lacerna, Dante Paz — [Assembly bias from nuisance to probe I: the relation between galactic conformity and the linear matter clustering](http://arxiv.org/abs/2607.04022v1)
  <details><summary>📄 Abstract</summary>
  Two-halo galactic conformity is commonly interpreted as a manifestation of galaxy assembly bias, but its statistical structure and physical origin remain unclear. We aim to write the quenched-neighbour statistic in correlation-function form, test whether its scale dependence follows the linear matter correlation function $ξ_{\rm mm}^{\rm lin}(r)$, and separate the contributions of halo-mass bias and assembly bias to its amplitude. Using galaxies in IllustrisTNG300-1 at $z=0$, we measure the two-...
  </details>

- **2026-07-04** — Shuyang Xiang, Hao Guan — [Full Glyph Images Beat Token Embeddings: A Controlled Study for Transformers](http://arxiv.org/abs/2607.03994v1)
  <details><summary>📄 Abstract</summary>
  Modern language models generally represent text as sequences of discrete token embeddings, an assumption deeply rooted in current practice but rarely questioned. We challenge this representation, especially for Chinese, by replacing index-based token embeddings entirely with a single rasterized image of the character sequence, processed by a vision encoder composed of a shared ResNet and a shallow Vision Transformer. To isolate the role of input representation, we construct a dual-branch control...
  </details>

- **2026-07-04** — Yaron Anavi, Mor Aisenberg, Nadav Nesher et al. — [Knowing When to Stop: Predicting Execution-Consistency Convergence in Text-to-SQL](http://arxiv.org/abs/2607.03991v1)
  <details><summary>📄 Abstract</summary>
  Repeated LLM calls are the standard way to estimate how trustworthy a Text-to-SQL result is: run the pipeline multiple times, judge each SQL execution, and use the consistency of the verdicts as a confidence signal. The open question is when to stop, when the consistency has converged. We formulate this as a convergence-prediction problem and train a family of lightweight 1-D models that observe the running consistency trajectory and decide, at each step, whether further runs are unlikely to shi...
  </details>

- **2026-07-04** — Rashmi Ravi, Bhaskarareddy N C, Augustine O. Nwajana — [A Triple-Band Bandpass Filter Using Square Open-Loop Resonators](http://arxiv.org/abs/2607.03921v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of multi-band wireless communication systems has driven demand for compact, high-performance multi-band bandpass filters (BPFs) capable of isolating specific frequency bands within a wider spectrum. This paper reviews the current state-of-the-art in multi-band filter design and implementation techniques and presents the design, simulation, and characterisation of a prototype triple-band bandpass filter to validate one of the investigated techniques. A triple-band BPF operat...
  </details>

- **2026-07-04** — Yining Zheng, Yuxin Wang, Jiahao Lu et al. — [Rethinking Scientific Discovery in an Agentic Era](http://arxiv.org/abs/2607.03863v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence has advanced scientific discovery, but most AI4Science systems remain fragmented tools that rely on humans to coordinate problem formulation, literature grounding, model use, simulation, validation, and knowledge reuse. This paper presents \textbf{SCION (Scientific Collaborative Innovation with Agentic Organizational Nexus)}, an agentic scientific operating system that acts as an \textbf{organizational nexus}. Through a Science Agent serving as a \textbf{Meta-Harness}, SC...
  </details>

- **2026-07-04** — Zhenyu Sun, Xiaohan Zhang, Qi Liu et al. — [CGGS: Consistency-Augmented Geometric Gaussian Splatting for Ego-centric 3D Scene Generation](http://arxiv.org/abs/2607.03819v1)
  <details><summary>📄 Abstract</summary>
  Challenges remain in ego-centric 3D scene generation due to limited view overlap and the dominant influence of individual perspectives on scene interpretation. These factors hinder the creation of viewpoint-consistent and semantically aligned visual content, as well as the construction of accurate geometric structures. In this paper, we propose CGGS, a text-to-3D framework aiming to enhance 3D-content-awareness and address geometric distortions in ego-centric scene generation. Firstly, the Ego-c...
  </details>

- **2026-07-04** — Héctor Martel, Joe Hennessy-Priest, Taemin Cho — [Probing Low-Level Acoustic Attribute Encoding in CLAP Audio Embeddings](http://arxiv.org/abs/2607.03806v1)
  <details><summary>📄 Abstract</summary>
  Audio foundation models are widely adopted as general-purpose feature extractors, yet the internal structure of their learned representations remains insufficiently understood. In this work, we analyze CLAP audio embeddings through a probing framework, studying the encoding of three fundamental perceptual dimensions: reverberation (RT60), loudness (LUFS), and spectral content, measured via spectral centroid (SC) and relative pitch (RP). Probes of increasing complexity are trained to predict each...
  </details>

- **2026-07-04** — Aureka AI OpenDDE project — [Folding, Reasoning, and Scaling with Open-source Drug Discovery Engine](http://arxiv.org/abs/2607.03787v1)
  <details><summary>📄 Abstract</summary>
  Accurately modeling biomolecular interactions is a central bottleneck in biology and therapeutic discovery. Here, we introduce Open Drug Discovery Engine (OpenDDE), an open-source, all-atom biomolecular foundation model that uses co-folding as the entry point to a scalable AI-driven drug discovery engine. Rather than treating structure prediction as an isolated endpoint, OpenDDE is designed as a shared structural reasoning layer for modeling sequence-structure-function relationships across biomo...
  </details>

- **2026-07-04** — Nicole Sonne Heckmann, Arnault-Quentin Vermillet, Søren Norlin Mølgaard et al. — [Optimizing Large Language Models for Causality Assessment in Pharmacovigilance: Developing a Performance Metric as Objective for Bayesian Hyperparameter Optimization](http://arxiv.org/abs/2607.03704v1)
  <details><summary>📄 Abstract</summary>
  Background: Growing individual case safety report (ICSR) volumes have intensified demand for scalable automated causality assessment. Large Language Models (LLMs) show promise, yet performance on clinically demanding tasks remains suboptimal and inference-time hyperparameter optimization has not been investigated. Objective: To develop a Gaussian Process (GP)-compatible optimization objective and investigate whether temperature optimization improves LLM-expert agreement on Naranjo causality asse...
  </details>

- **2026-07-04** — Oussama Ben Sghaier, Hao Li, Bram Adams et al. — [Don't Blame the Large Language Model: How Scaffolding Evolution Shapes Coding Agent Quality](http://arxiv.org/abs/2607.03691v1)
  <details><summary>📄 Abstract</summary>
  Coding agents, autonomous systems that use large language models (LLMs) to resolve software engineering tasks, rely on agentic scaffolding: a middleware layer in between a developer and a large language model that orchestrates system prompts, tool execution, context management, and iterative reasoning loops. While these scaffoldings evolve at extreme velocities, no study has examined how this evolution affects agent quality (i.e., effectiveness and efficiency) over time. Practitioners regularly ...
  </details>

- **2026-07-04** — Jiahao Jiang, Jianing Zhang, Zhenhan Yin et al. — [WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control](http://arxiv.org/abs/2607.03941v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in embodied AI have established robot foundation models (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions to continuous robotic actions. However, current RFMs lack an inherent ability to reason about physical dynamics and the causal effects of robot behaviors on the 3D physical world. This cre...
  </details>

- **2026-07-04** — Xunqi Li, Chris H. Kim — [SABLE: An NDA-Safe Closed-Loop LLM Framework for Analog Circuit Optimization in Industrial EDA Flows](http://arxiv.org/abs/2607.03701v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can propose circuit-optimization decisions, but industrial analog flows cannot expose foundry PDK content, proprietary schematics, absolute simulation paths, or license-bound tool state to a cloud endpoint. We present SABLE (Safe Analog Boundary for LLM-driven EDA), an NDA-safe closed-loop framework that lets LLMs optimize analog circuits through Cadence Virtuoso, Maestro, and Spectre while returning only scrubbed topology intent, numeric metrics, operating-point sum...
  </details>

- **2026-07-04** — Nicholas Boichuk — [Termination of Binary Trust-Gossip Dynamics: A Constructive No-Limit-Cycles Theorem](http://arxiv.org/abs/2607.04023v1)
  <details><summary>📄 Abstract</summary>
  In the binary trust-gossip dynamics, $n$ agents each hold a directed binary opinion, trust or distrust, of every other agent, and a gossip step lets one agent copy another agent's opinion of a third whenever the copier trusts the source. We prove that under any fair schedule of such steps, every trajectory reaches an absorbing state in finitely many steps, one in which no gossip step changes any opinion; in particular, there are no limit cycles. The proof is constructive and rests on a single de...
  </details>

- **2026-07-04** — Madhuparna Karmokar, Ujjwal Kumar, Soumyarup Sadhukhan — [Strategy-Proof Probabilistic Social Choice Correspondences under Conditional Expected Utility](http://arxiv.org/abs/2607.03955v1)
  <details><summary>📄 Abstract</summary>
  We study unanimous and strategy-proof probabilistic social choice correspondences (PSCCs), where the selected set of alternatives is interpreted as an interim outcome, and agents evaluate sets using conditional expected utility. We analyze two preference domains introduced by Barbera et al. (2001): the conditionally expected utility consistent (CEUC) domain and the conditionally expected utility consistent with equal probabilities (CEUCEP) domain. Our results characterize all unanimous and strat...
  </details>

- **2026-07-04** — Zixi Chen, Yinyu Ye, Zijie Zhou — [Online Linear Programming for Multi-Objective Routing in LLM Serving](http://arxiv.org/abs/2607.03948v1)
  <details><summary>📄 Abstract</summary>
  We study the online routing problem in large language model serving, where requests arrive sequentially and must be dispatched to parallel decode workers under tight batch-size and KV-cache constraints. Unlike widely used routing heuristics that are not tied to explicit service-level objectives (SLOs) and offer limited control over latency-throughput trade-offs, we introduce a multi-objective optimization framework that formulates routing as an online linear programming with interpretable decisi...
  </details>

- **2026-07-04** — Kareem Elozeiri, Mervat Abassy, Omar Kallas et al. — [Can Dialects Be Steered Like Languages? Sparse Neurons and Distributed Directions in Arabic LLMs](http://arxiv.org/abs/2607.03936v1)
  <details><summary>📄 Abstract</summary>
  A key challenge in Arabic NLP is the scarcity of dialectal data relative to Modern Standard Arabic (MSA), causing LLMs to overproduce MSA and struggle with dialectally accurate generation. From an interpretability perspective, this raises a fundamental question: where and how are dialectal features encoded within model internals, and can these representations be leveraged to improve dialect generation without fine-tuning? This study investigates two complementary inference-time approaches that s...
  </details>

- **2026-07-04** — Oliver Gerstl, Florian Sihler, Matthias Tichy — [Inferring the Shape of Data Frames in R Programs using Abstract Interpretation](http://arxiv.org/abs/2607.03889v1)
  <details><summary>📄 Abstract</summary>
  Data frames are a fundamental data structure in many data analysis tasks and are widely used in programming languages like R. Due to their omnipresence in data analysis, there are many functions that operate on their shape and content, for example, to clean and transform study data. However, languages like R do not offer static guarantees on data frames making it difficult to reason about their shape at a specific point in the program.   In this paper, we present a novel static analysis to infer...
  </details>

- **2026-07-04** — Diego Cerda-Mardini, Sarath Chandar, Sreenath Madathil — [Consistent but Miscalibrated: Evaluating LLM Limitations for Risk Communication in Natural Language](http://arxiv.org/abs/2607.03882v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly deployed as post-hoc explainers of AI-generated outputs, yet it remains unclear whether they can reliably communicate probabilistic information in natural language. For this role to be viable, models must produce identical verbal descriptions for identical inputs, and select descriptions that accurately reflect the magnitude of the underlying numerical quantities. We evaluate whether nine LLMs meet these requirements within a two-stage prediction pipeline, in which an upstr...
  </details>

- **2026-07-04** — Salvatore Romano — [The Reweighting Principle in Statistical Mechanics](http://arxiv.org/abs/2607.03867v1)
  <details><summary>📄 Abstract</summary>
  Reweighting of probability measures provides a unifying perspective on conditioning, exponential tilting, and, more generally, ensemble transformations in statistical mechanics. We show that exponential tilting and conditioning arise as the minimum-relative-entropy updates associated with soft and hard constraints, respectively. Their relative entropies naturally inherit complementary thermodynamic structures: exponential tilting gives rise to the Legendre structure of the canonical ensemble and...
  </details>

- **2026-07-04** — Byoungkwon Kim, Minhyuk Sung — [Tensor-Train Joint Modeling for Few-Step Discrete Diffusion](http://arxiv.org/abs/2607.03788v1)
  <details><summary>📄 Abstract</summary>
  Discrete diffusion promises orders-of-magnitude faster generation than autoregressive (AR) models for sequential discrete data, yet its full potential of few-step generation has remained out of reach due to a fundamental structural limitation. The conditional-independence assumption underlying current discrete diffusion models introduces a systematic parallelization bias that compounds with the number of tokens unmasked per step, becoming severe in the few-step regime that fast generation requir...
  </details>

- **2026-07-04** — Sébastien S. Ferenczi, Luca Q. Zamboni — [Order symmetry and orthogonality of trajectories in discrete interval exchange transformations](http://arxiv.org/abs/2607.03785v1)
  <details><summary>📄 Abstract</summary>
  Let $π=(<_D,<_A)$ be a pair of distinct orders on a $k$-letter alphabet $A. $ The periodic trajectories $v_i^\infty $ of a discrete $k$-interval exchange transformations $T$ with permutation $π$ are characterized by the following order symmetry : $v_i^ω<_D v_j^ω$ (lexicographically) if and only if $v_i^{-ω}<_Av_j^{-ω}$ (reverse lexicographically). For general words $u$ and $v$ over $A$, the orders need not agree in which case either $u^ω<_A v^ω<_D u^ω$ (Type 1) or $v^ω<_A u^ω<_D v^ω$ (Type 2). W...
  </details>

- **2026-07-04** — Xintong Zhou, Hongxu Xu, Chunhao Liao et al. — [Semantic-aware and Self-improving Program Reduction via Agentic Large Language Models](http://arxiv.org/abs/2607.03766v1)
  <details><summary>📄 Abstract</summary>
  Reducing bug-triggering programs to their minimal essential form is a fundamental task in debugging language processors such as compilers and interpreters. Existing reduction techniques are limited by their reliance on predefined, syntax-driven transformations that lack semantic understanding of the target program, and by their inability to learn from past reduction experiences.   We present a new approach that recasts program reduction as an autonomous reasoning task powered by agentic Large La...
  </details>

- **2026-07-04** — Satoshi Ohya, Taichi Tanaka — [ERG Kernels on Multiply Connected Configuration Spaces](http://arxiv.org/abs/2607.03750v1)
  <details><summary>📄 Abstract</summary>
  In the functional-integral formulation of Euclidean field theory, exact renormalization group (ERG) transformations are realized by functional-integral kernels. Unlike the ERG flow equations that describe infinitesimal ERG transformations, these ERG kernels explicitly depend on the global topology of the configuration space. This paper explores this topology dependence for multiply connected configuration spaces. We show that the ERG kernel is in general given by a weighted sum of kernels on its...
  </details>

- **2026-07-04** — Shu Yang, Difei Xu, Jiaxin Pei et al. — [ProACT: Towards Breakdown-Aware Proactive Agent in Multi-User Collaboration](http://arxiv.org/abs/2607.03730v1)
  <details><summary>📄 Abstract</summary>
  Conversational agents are increasingly embedded in human collaborative work, yet they remain fundamentally passive and reactive: they respond to explicit user requests rather than proactively recognizing moments when a team would benefit from timely intervention as human collaborators often do. This reactive design substantially limits the use of agents as active participants in multi-user collaboration, where disagreements, ambiguous goals, forgotten constraints, underspecified plans, discussio...
  </details>

- **2026-07-04** — Varvara Nazarenkko, Timur Lidzhiev, Alexander Tarakanov — [PIEFS: Physics-Informed Eigenfunction Features with Learnable Scaling](http://arxiv.org/abs/2607.03692v1)
  <details><summary>📄 Abstract</summary>
  Spectral methods are widely used to construct representations from the geometry of data, but they often rely on a fixed kernel, graph Laplacian, or manually selected feature scaling. We propose Physics-Informed Eigenfunction Features with Learnable Scaling (PIEFS), a supervised neural representation-learning framework with a spectral inductive bias, based on a modified Dirichlet energy. In PIEFS, scalar coordinate maps are trained under empirical Gram orthogonality, a supervised linear readout, ...
  </details>

- **2026-07-02** — Shahreen Salim, Klaus Mueller — [When Do LLM Personas Support Visualization Design? A Cross-Model Study of Color Assignment and Chart Choice](http://arxiv.org/abs/2607.02455v1)
  <details><summary>📄 Abstract</summary>
  Large language model personas are increasingly used to approximate diverse users during early-stage visualization design, but it remains unclear whether persona-conditioned outputs reflect stable personality effects or artifacts of model choice and task framing. We examine this question across two visualization-relevant tasks: color assignment for abstract and concrete concepts, and chart-idiom preference ratings across task contexts. Using 43 Big Five profiles across GPT-4o-mini, GPT-4.1-mini, ...
  </details>

- **2026-07-02** — Zhilin Wang, Han Song, Runzhe Zhan et al. — [EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](http://arxiv.org/abs/2607.02440v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are increasingly expected to improve executable policies through feedback, yet existing evaluations often collapse this process into a final score or confound it with open-ended software-engineering progress. We introduce Autonomous Policy Evolution, a controlled evaluation setting in which a harness-model agent repeatedly edits an executable policy system under a fixed interaction budget. We instantiate this setting in EvoPolicyGym, a benchmark built from compact interactive R...
  </details>

- **2026-07-02** — Francesca Pistilli, Simone Alberto Peirone, Giuseppe Averta — [Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs](http://arxiv.org/abs/2607.02425v1)
  <details><summary>📄 Abstract</summary>
  Understanding human behavior while interacting with the surrounding world is crucial for many applications of embodied AI. First-person videos are particularly informative for this problem, as they well capture how activities reshape the scene over time. However, existing approaches often rely on implicit visual or language-aligned representations, disregarding structured reasoning over the scene dynamic. We argue that explicit, compositional and editable representations of human-environment int...
  </details>

- **2026-07-02** — Mohamed Shamseldein — [Generative Autonomous Grid Control: Integrating Decision Transformers with a Two-Stage Safety Stack](http://arxiv.org/abs/2607.02379v1)
  <details><summary>📄 Abstract</summary>
  The displacement of synchronous generation by inverter-based resources is accelerating power system frequency dynamics beyond the response capability of conventional automatic generation control. This paper presents Autonomous Grid Generation Control with Decision Transformers, a framework coupling an offline-trained Decision Transformer with a twostage symbolic safety stack for secondary frequency control. The Decision Transformer learns a conditional dispatch policy from offline supervisory co...
  </details>

- **2026-07-02** — Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi — [Hardware-Enforced Semantic Coordination for Safety-Critical Real-Time Autonomous Systems](http://arxiv.org/abs/2607.02376v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in agentic AI are producing increasingly complex autonomous systems that integrate large language models, world models, optimization engines, specialized neural architectures, autonomous platforms, and human operators. While much current research focuses on improving reasoning capabilities, safety-critical real-time deployment also requires bounded and verifiable coordination among heterogeneous components operating concurrently under uncertainty. Software-mediated coordination p...
  </details>

- **2026-07-02** — Batu Guan, Zirui Wang, Shaohua Li — [Understanding Agent-Based Patching of Compiler Missed Optimizations](http://arxiv.org/abs/2607.02370v1)
  <details><summary>📄 Abstract</summary>
  Compiler missed optimizations refer to cases in which compilers failed to optimize certain code. It takes many compiler developers' efforts to implement or patch such missed optimizations. In this paper, we present a systematic study of how well agents patch compiler missed optimizations. We identify a significant challenge that patching a missed optimization requires more than just fixing the reported case, and instead requires generalizing to similar cases. We construct a benchmark of real-wor...
  </details>

- **2026-07-02** — Ohad Eitan, Idit Keidar, Ehud Shapiro — [Securing People and their Machines Against Major Faults](http://arxiv.org/abs/2607.02304v1)
  <details><summary>📄 Abstract</summary>
  We consider grassroots platforms -- distributed systems of agents consisting of people identified by self-chosen public keys and their machines (smartphones) -- and wish to make them secure against \emph{major faults}: the loss of their private keys and/or their smartphones. As grassroots platforms have no global resource to rely on for recovery, our peer-based solution is based on: (\ia) \emph{a grassroots social graph} in which agents establish and maintain friendships; (\ib) \emph{identity cu...
  </details>

- **2026-07-02** — Fatima Elsheimy, Mohammad Mussadiq Jalalzai, Tobias Klenze et al. — [Cadence: Extreme Pipelining with Multiple Concurrent Proposers](http://arxiv.org/abs/2607.02275v1)
  <details><summary>📄 Abstract</summary>
  We present Cadence, a Byzantine fault-tolerant multi-proposer consensus protocol with arbitrarily low block intervals, optimal resilience, and optimal fast-path latency. Cadence divides time into equally spaced slots, one block per slot, each finalized in its own consensus instance. Blocks do not build directly on their predecessor, so instances run independently and none waits for an earlier block to finish or propagate; we call this extreme pipelining, decoupling the block interval from networ...
  </details>

- **2026-07-02** — Rintaro Otsubo, Ryo Fujii, Reina Ishikawa et al. — [AnyGroundBench: A Specialized-Domain Benchmark for Video Grounding in Vision-Language Models](http://arxiv.org/abs/2607.02269v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have demonstrated immense promise in Spatio-Temporal Video Grounding (STVG). However, current evaluation protocols are largely confined to zero-shot assessments on general, daily-life benchmarks. This creates a critical disconnect from real-world applications in specialized fields, where models inevitably encounter rare visual concepts and complex spatio-temporal dynamics. Since exhaustive pre-training across infinite data distributions is infeasible, the ability to...
  </details>

- **2026-07-02** — Zhanming Shen, Jintao Tong, Shaotian Yan et al. — [Purified OPSD: On-Policy Self-Distillation Without Losing How to Think](http://arxiv.org/abs/2607.02234v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) has emerged as a promising paradigm for improving LLM reasoning, where a privileged teacher with access to reference solutions provides token-level supervision on the student's own generated trajectories. However, we find that OPSD consistently fails on long chain-of-thought (long-CoT) reasoning models, yielding at best marginal gains while destabilizing the reflective reasoning capability these models depend on. Through a novel decomposition of the teacher's s...
  </details>

- **2026-07-02** — Sampreeti Bhattacharya, Arkaprava Roy — [An Additive MLP-GNN Framework for Characterizing Chemical and Structural Contributions to Aqueous Solubility](http://arxiv.org/abs/2607.02212v1)
  <details><summary>📄 Abstract</summary>
  Aqueous solubility is a key property in early-stage drug discovery, but most predictive models merge physicochemical descriptors and molecular graph information into a single representation, obscuring whether a prediction is driven by global chemistry, molecular structure, or both. We present an additive deep-learning framework that keeps these two sources of information separate throughout training: physicochemical descriptors are encoded by a multilayer perceptron (the chemical branch) and mol...
  </details>

- **2026-07-02** — Jijie Zhang, Zhe Ren, Quan Zhang et al. — [Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation](http://arxiv.org/abs/2607.02182v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit remarkable reasoning capabilities, but their task-specific fine-tuning is notoriously plagued by overconfidence, severely hindering trustworthy deployment. We propose Data-Adaptive Lower-Rank Adaptation (DALorRA), a simple and effective variational Bayesian sparse framework that shifts the paradigm of uncertainty quantification from the dense parameter space to the lightweight rank level of low-rank adaptation (LoRA). With the insight that LoRA essentially ag...
  </details>

- **2026-07-02** — Samiha A. Ismail, Fan X. Chen, Ali Merali — [A rubric-based controlled comparison of frontier language models on expert-authored clinical reasoning tasks](http://arxiv.org/abs/2607.02175v1)
  <details><summary>📄 Abstract</summary>
  Multiple-choice medical benchmarks are increasingly saturated, and recent rubric-based evaluations such as HealthBench have shown that open-ended clinical performance is far from solved - its "Hard" subset top score remains 32%. We present a small, deliberately difficult evaluation dataset of five clinician-authored clinical scenarios spanning four specialties (anaesthesia, internal/family medicine, emergency medicine, and obstetrics), each accompanied by an atomic, weighted, MECE rubric (25-62 ...
  </details>

- **2026-07-02** — Gianmarco Spinaci, Lukas Klic, Giovanni Colavizza — [EduArt: An educational-level benchmark for evaluating art history knowledge in large language models](http://arxiv.org/abs/2607.02007v1)
  <details><summary>📄 Abstract</summary>
  Large language models now score near ceiling on general benchmarks, but these aggregate measures reveal little about how models behave within single disciplines. Existing art-focused evaluations rely on synthetic questions and rarely report item-level properties. This paper introduces EduArt, an educational-level benchmark for art-historical knowledge and visual reasoning in multimodal LLMs. EduArt comprises 871 human-authored questions from Italian secondary-school exercises and US Advanced Pla...
  </details>

- **2026-07-02** — Weichen Zhou, Yawen Zou, Chunzhi Gu et al. — [Understanding Geometric Representations in Self-Supervised Vision Transformers via Subspace Intervention](http://arxiv.org/abs/2607.01987v1)
  <details><summary>📄 Abstract</summary>
  We introduce a controlled subspace intervention framework to investigate how self-supervised Vision Transformers (ViTs) encode dense geometric information. While linear probing is widely used to assess geometric representations, it treats features as a black box, failing to disentangle the underlying topology. To address this issue, we decompose the weights of converged linear probes to isolate the low-rank subspaces containing explicit geometric signals using Singular Value Decomposition (SVD)....
  </details>

- **2026-07-02** — Shahbaz Siddeeq, Mateen Abbasi, Jussi Rasku et al. — [Epic-Organized vs. Requirement-Aligned Gherkin: An Empirical Evaluation of LLM-Based Acceptance Criteria Generation](http://arxiv.org/abs/2607.01980v1)
  <details><summary>📄 Abstract</summary>
  Automated authoring of Gherkin Behavior-Driven Development (BDD) acceptance criteria remains a manual bottleneck in requirements engineering. This study investigates whether epic-organized LLM-generated Gherkin produces higher quality and coverage than requirement-aligned generation. We compare our Timeless (an epic-organized LLM pipeline) approach against a naive large language model (LLM) baseline on four requirements documents (107 requirements) from the PURE dataset. Evaluation covers struct...
  </details>

- **2026-07-02** — Massimiliano Berti, Alberto Maspero, Antonio Milosh Radakovic — [McLean resonances and $3d$ spectral instability of Stokes waves](http://arxiv.org/abs/2607.01939v1)
  <details><summary>📄 Abstract</summary>
  The spectral instability of traveling periodic water waves has been investigated for more than sixty years, since the seminal discovery of Benjamin and Feir. Despite an extensive literature, no rigorous theory has been available for arbitrary three-dimensional -- longitudinal and transverse -- perturbations. We establish the first rigorous description of the $3d $ unstable spectrum of small-amplitude gravity Stokes waves in deep water in a full neighborhood of the McLean resonant curves. Our res...
  </details>

- **2026-07-02** — Nicholas Tagliapietra, Gian Lorenzo Marchioni, Moritz Willig et al. — [CausalSteward: An Agentic Divide-Conquer-Combine Copilot for Causal Discovery](http://arxiv.org/abs/2607.01936v1)
  <details><summary>📄 Abstract</summary>
  Learning causal models from high-dimensional data is a significant challenge, particularly in real-world settings where violations of core assumptions lead to causal identifiability issues. Although massive amounts of prior knowledge are available, and contain valuable causal information, effectively integrating this knowledge into the causal discovery process remains an open problem. We introduce CausalSTeward (CAST), a novel human-in-the-loop framework for interactively assembling large causal...
  </details>

- **2026-07-02** — Ahin Lee, Sehyun Yun, Taesik Gong — [EPnG: Adaptive Expert Prune-and-Grow for Parameter-Efficient MoE Fine-tuning](http://arxiv.org/abs/2607.01789v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) models scale efficiently but remain costly to adapt due to redundant experts and uniform parameter allocation. Existing parameter-efficient fine-tuning (PEFT) methods such as LoRA ignore MoE routing dynamics, leading to suboptimal resource use. We propose EPnG, an adaptive prune-and-grow framework that reallocates LoRA capacity based on expert importance derived from router gate probabilities. EPnG prunes under-utilized experts and expands high-importance experts via ran...
  </details>

- **2026-07-02** — Xinyuan Song, Zekun Cai — [Repair the Amplifier, Not the Symptom: Stable World-Model Correction for Agent Rollouts](http://arxiv.org/abs/2607.01767v1)
  <details><summary>📄 Abstract</summary>
  As agent planning moves from short tool chains toward persistent workflows with thousands or tens of thousands of steps, failures will occur inside large planning graphs rather than in isolated predictions. Replanning the entire graph after every mistake is neither computationally realistic nor desirable: full-graph replay consumes large context budgets, exposes the LLM to many irrelevant symptoms, and can degrade long-context retrieval. This paper studies the missing component in such systems: ...
  </details>

- **2026-07-02** — Minkuk Kim, Suyong Yun, Young Tae Kim et al. — [ReQuest: Rethinking-based Question-Aware Frame Selection for Long-Form Video QA](http://arxiv.org/abs/2607.01737v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal large language models (MLLMs) have substantially advanced video understanding, yet long-form video QA remains challenging under fixed input token budgets, where uniform sampling can be inefficient for evidence localization. We propose ReQuest , an uncertainty-driven, question-adaptive keyframe selection pipeline that aligns question intent with relevant video content through selective computation. ReQuest integrates (i) a lightweight question-aware selector distilled from MLLM-...
  </details>

- **2026-07-02** — Ruchao Fan, Yiming Wang, Rui Zhao et al. — [Rethinking Speech-LLM Integration for ASR: Effective Joint Speech-Text Training by Interleaving](http://arxiv.org/abs/2607.01733v1)
  <details><summary>📄 Abstract</summary>
  Speech-LLM integration has shown promising results by leveraging extensive textual pretraining, yet its specific benefits for automatic speech recognition (ASR) remain unclear. We observe that as supervised ASR training data increases, the contribution of LLM priors becomes less evident, and simple speech-text joint training under-utilizes textual knowledge. We therefore propose Joint Speech-Text Interleaved Pretraining (JSTIP), an ASR-oriented pretraining strategy that constructs word-level and...
  </details>

- **2026-07-02** — Zhaoyan Sun, Shan Zhong, Daizhou Wen et al. — [AgenticDataBench: A Comprehensive Benchmark for Data Agents](http://arxiv.org/abs/2607.01647v1)
  <details><summary>📄 Abstract</summary>
  Data science aims to derive actionable insights from heterogeneous raw data, unlocking the value of the massive amounts of data generated in modern society. Automating this process is essential to reducing labor-intensive efforts for data scientists and enabling scalable data-driven applications. Recently, large language model (LLM)-based data agents have emerged as a promising solution to automate data science workflows. However, the field lacks comprehensive benchmarks to rigorously evaluate t...
  </details>

- **2026-07-02** — Shuai Tian, Yupeng Zheng, Yuhang Zheng et al. — [VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation](http://arxiv.org/abs/2607.02503v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich manipulation requires policies to react to local deformation, pressure, slip, and friction, yet these cues are temporally sparse and often invisible in visual observations. Existing visual-tactile policies usually feed tactile observations directly into action prediction, but rarely model tactile deformation dynamics during action generation. In this paper, we introduce VT-WAM, a Visual-Tactile World Action Model that jointly learns future visual prediction, tactile deformation pred...
  </details>

- **2026-07-02** — Kyobin Choo, Youngmin Kim, Hyunkyung Han et al. — [QWERTY: Training-Free Motion Control via Query-Warped Video Diffusion Transformers](http://arxiv.org/abs/2607.01869v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion transformers (DiTs) generate high-fidelity and temporally coherent videos, yet motion control remains implicit, primarily relying on text prompts. As a result, achieving desired motion often requires extensive prompt engineering and repeated resampling. While fine-tuning models with additional spatial prompts (e.g., bounding boxes or point trajectories) enables explicit control, it demands substantial data curation and computation, and may compromise the generative capabilities o...
  </details>

- **2026-07-02** — Wentao Zhang, Liliana Hotsko, Woojeong Kim et al. — [Program-as-Weights: A Programming Paradigm for Fuzzy Functions](http://arxiv.org/abs/2607.02512v1)
  <details><summary>📄 Abstract</summary>
  Many everyday programming tasks resist clean rule-based implementation, such as alerting on important log lines, repairing malformed JSON, or ranking search results by intent, and are increasingly outsourced to large language model APIs at the cost of locality, reproducibility, and price. We propose fuzzy-function programming: compiling such a function from a natural-language specification into a compact, locally-executable neural artifact. We instantiate this paradigm with Program-as-Weights (P...
  </details>

- **2026-07-02** — Donghyun Lee, Jitesh Chavan, Duy Nguyen et al. — [OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers](http://arxiv.org/abs/2607.02461v1)
  <details><summary>📄 Abstract</summary>
  Diffusion transformers (DiTs) achieve state-of-the-art image and video generation, but their multi-step sampling and growing parameter count make inference expensive. Post-training quantization (PTQ) is the natural remedy, yet DiT activations shift across timesteps, prompts, and guidance branches, forcing prior methods to re-fit calibration data for every new checkpoint or modality. We present OrbitQuant, a data-agnostic weight-activation quantizer that bypasses range estimation by quantizing in...
  </details>

- **2026-07-02** — Nina Begus — [World Wide Models: Literary Tools for Cultural AI](http://arxiv.org/abs/2607.02369v1)
  <details><summary>📄 Abstract</summary>
  LLMs stage a new form of cultural encounter that is massive, automated, and monolingual. Literary disciplines have always negotiated cultural struggles with comparative reading of literature, narratological and poetic analysis, critical theory, world literature, and translation. These tools have now become indispensable for building culturally literate AI. The essay develops a layered framework toward more nuanced textual models and pluralistic interpretations of AI, emphasizing the natural inte...
  </details>

- **2026-07-02** — Yuan Ding, Wenjing Liu, Xin Chen et al. — [Facility Location Game with Envy Ratio](http://arxiv.org/abs/2607.02330v1)
  <details><summary>📄 Abstract</summary>
  We study the one-facility location game on a real line with a new objective called envy ratio. The envy ratio, which is adopted from fair division and represents the egalitarianism, is defined as the maximum over the ratios between any two agents' utilities. We are interested in strategyproof or group strategyproof mechanisms that can minimize the envy ratio objective.   We consider the model in two settings that can capture natural scenarios: the facility location and all the agents' locations ...
  </details>

- **2026-07-02** — Andrea Mazzolini, Leonardo Agasso, Filippo Valle et al. — [Alternative routes to universal diversity scaling in component systems: from proteomes to large language models](http://arxiv.org/abs/2607.02221v1)
  <details><summary>📄 Abstract</summary>
  Remarkably common statistical laws characterize the diversity scaling and its fluctuations across a wide range of complex "component systems". These regularities are often interpreted as signatures of an underlying innovation mechanism driving the growth of component diversity, but the basic ingredients necessary for their emergence remain poorly understood. In particular, from language and technological artifacts to genomes and gene expression patterns, the number of distinct components grows s...
  </details>

- **2026-07-02** — Mohammad Amanour Rahman — [MedSaab-US: A Backpropagation-Free Multi-Scale Wavelet-Saab Framework for Thyroid Nodule Segmentation in Ultrasound Images](http://arxiv.org/abs/2607.02209v1)
  <details><summary>📄 Abstract</summary>
  Deep learning (DL) methods dominate thyroid nodule segmentation in ultrasound (US) images, achieving high Dice scores but at the cost of millions of parameters, GPU-dependent training via backpropagation, and limited mathematical tractability. These limitations impede deployment in resource-constrained environments. In this paper, we propose MedSaab-US, a backpropagation-free segmentation framework grounded in the Green Learning paradigm. MedSaab-US extracts multi-scale spatial-frequency feature...
  </details>

- **2026-07-02** — Sara Antonijevic, Brani Vidakovic — [Quaternion Nondecimated Wavelet Descriptors for Multiclass Breast Histology Classification](http://arxiv.org/abs/2607.02133v1)
  <details><summary>📄 Abstract</summary>
  Breast histology images carry diagnostic information in color, texture, orientation, and tissue architecture across a range of scales. In H&E microscopy this information is inherently chromatic and is not fully recovered when the red, green, and blue (RGB) channels are reduced to grayscale or transformed as independent scalar images. We propose an interpretable quaternion nondecimated wavelet framework for breast histology classification. Each RGB image is encoded as a pure quaternion field, and...
  </details>

- **2026-07-02** — Jian Xu, Delu Zeng, John Paisley et al. — [Ask the Right Comparison:Bias-Aware Bayesian Active Top-$k$ Ranking with LLM Judges](http://arxiv.org/abs/2607.02104v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as cheap, scalable judges that compare candidate outputs pairwise -- to rank responses, select models, or triage papers. Yet LLM judges are both noisy and systematically biased: they favor verbose or well-formatted answers and exhibit position effects, so simply aggregating their votes recovers a ranking of presentation, not of true quality. We study the practical goal of identifying the \topk{} items under a fixed comparison budget, and make tw...
  </details>

- **2026-07-02** — Cuipeng Wang, Haipeng Wang — [SFKD: Spatial--Frequency Joint-Aware Heterogeneous Knowledge Distillation via Multi-Level Wavelet Spectral Interaction](http://arxiv.org/abs/2607.01906v1)
  <details><summary>📄 Abstract</summary>
  Most existing knowledge distillation methods focus on homogeneous models (e.g., CNN-to-CNN), thereby overlooking the flexibility and potential of knowledge transfer across heterogeneous models. Due to intrinsic inductive bias discrepancies between heterogeneous models that cause spatial distribution inconsistencies, prior heterogeneous distillation methods often weaken or discard spatial information in heterogeneous representations. However, the spatial information in representations often encod...
  </details>

- **2026-07-02** — Zihao Xu, Yuekang Li, Gelei Deng et al. — [Rethinking Complexity Metrics for LLM-Integrated Applications: Beyond Source Code](http://arxiv.org/abs/2607.01903v1)
  <details><summary>📄 Abstract</summary>
  LLM-integrated applications blend natural language prompts with program code, and much of their runtime behavior originates in the prompt layer rather than in the code itself. Existing complexity metrics, however, operate solely at the code level and therefore overlook this behavioral logic entirely. We present HECATE, the first tool designed to assess complexity in both the prompt and code layers of such applications. Central to HECATE is Prompt-as-Specification, a Hoare-logic-inspired formalis...
  </details>

- **2026-07-02** — Maximo Rulli, Thomas Fontanari, Simone Petruzzi et al. — [Subliminal Clocks: Latent Time Modelling in Diffusion Language Models](http://arxiv.org/abs/2607.01774v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Language Models (DLMs) have recently emerged as a promising alternative to autoregressive models. Unlike standard diffusion-based approaches, DLMs are not explicitly conditioned on a timestep, raising a natural question: do these models internally represent denoising progress, and how is such information used downstream? In this work, we show that DLMs do in fact encode a latent representation related to the diffusion timestep within their residual streams. We find that this signal can...
  </details>

- **2026-07-02** — Yujin Yang, Heejung Lee — [Verifiable Knowledge Expansion through Retrieval-Grounded Formal Concept Analysis](http://arxiv.org/abs/2607.01773v1)
  <details><summary>📄 Abstract</summary>
  Ontology construction requires deciding which objects, attributes, and structural relations should be accepted as valid knowledge. Language models can propose such structures from text, but their outputs can still be unsupported or inconsistent. This paper proposes a retrieval-augmented small language model (SLM) framework that uses formal concept analysis (FCA) as a symbolic verification loop for knowledge expansion. Starting from seed attributes, FCA proposes implications over a growing formal...
  </details>

- **2026-07-02** — Licheng Zhang, Bach Le, Pengtao Zhao et al. — [Beyond Pixel Diffs: Benchmarking Image Change Captioning for Web UI Visual Regression Testing](http://arxiv.org/abs/2607.01728v1)
  <details><summary>📄 Abstract</summary>
  Visual regression testing (VRT) is a standard quality assurance step in modern software release pipelines. On every change, it re-renders user interface (UI) screenshots, compares each one against an approved baseline image, and routes any detected difference to a human reviewer who decides whether it is an intended update or an unintended regression. A widely used approach, especially in open-source and continuous-integration pipelines, is pixel-level comparison, which is semantically blind and...
  </details>

- **2026-07-02** — Yongqin Zeng, Sicheng Pan, Jiale Wang et al. — [Generic Expert Coverage for Pruning SparseMixture-of-Experts Language Models](http://arxiv.org/abs/2607.01710v1)
  <details><summary>📄 Abstract</summary>
  Sparsely activated Mixture-of-Experts (MoE) language models contain substantial structured redundancy among routed experts, but pruning them without downstream calibration data remains challenging. Existing expert-pruning methods typically rely on a single aggregated importance score, which can bias the retained set toward experts favored by dominant calibration patterns. We propose \textbf{Generic TB-Coverage}, a coverage-aware expert pruning method that uses only generic text corpora (WikiText...
  </details>

- **2026-07-02** — Frederic Latremoliere — [How to approximate the flat spectral triple of a quantum torus by fuzzy tori : a twisted tale](http://arxiv.org/abs/2607.01681v1)
  <details><summary>📄 Abstract</summary>
  We prove that the classical and the quantum flat torus can be rigorously approximated at a differential level by finite-dimensional fuzzy tori within the framework of the spectral propinquity. Standard attempts to establish this convergence are traditionally obstructed by the intrinsic non-locality of discrete calculus and the subsequent failure of the Leibniz rule. While contemporary alternatives such as spectral truncations circumvent this issue by abandoning $C^*$-algebras in favor of operato...
  </details>

- **2026-07-02** — Lukáš Likavčan — [Substrate-Agnostic 3x: Biosignatures, Technosignatures, Ecologies](http://arxiv.org/abs/2607.01664v1)
  <details><summary>📄 Abstract</summary>
  Substrate-agnostic perspectives are currently attracting increased attention. For example, it has become customary to refer to agnostic biosignatures to reflect the range of alternative extraterrestrial biospheres and to account for the deeper philosophical dependence of candidate biosignatures on the underlying theory of life. Analogously, one can formulate a concept of agnostic technosignatures, reflecting that the more we expand the search for technosignatures, the more we invite theories of ...
  </details>

- **2026-07-01** — Ben Slivinski, Michael Saldivar — [Theoria: Rewrite-Acceptability Verification over Informal Reasoning States](http://arxiv.org/abs/2607.01223v1)
  <details><summary>📄 Abstract</summary>
  When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We present Theoria, a verification architecture that closes this gap. A candidate solution is rewritten into a sequence of typed state transitions, each licensed by an explicit justification, whether that be a...
  </details>

- **2026-07-01** — Jiale Li, Sihan Chen, Mengyuan Liu — [MoHallBench: A Benchmark for Motion Hallucination in Video Large Language Models](http://arxiv.org/abs/2607.01117v1)
  <details><summary>📄 Abstract</summary>
  Video Large Language Models (VideoLLMs) have shown strong progress in video understanding, yet they still suffer from hallucinations that are inconsistent with visual evidence. Existing benchmarks mainly focus on object hallucination or coarse action perception, leaving a key video-specific problem underexplored: motion hallucination, in which models infer human motions that are absent from the video. We present MoHallBench, a benchmark for diagnosing motion hallucination in VideoLLMs. MoHallBen...
  </details>

- **2026-07-01** — Yuan Si, Jialu Zhang — [Checked Program Recovery from Execution Video: A Sound Oracle for Untrusted Generators](http://arxiv.org/abs/2607.00635v1)
  <details><summary>📄 Abstract</summary>
  A growing class of tools recovers a program from observations of its behavior using an untrusted generator, a neural model or a search, that proposes candidates with no correctness guarantee. We study how to make such recovery trustworthy, in the concrete setting of recovering a runnable Scratch program from a recording of its execution. The recording shows what the program does but never its code; many programs produce the same video, so the source cannot be recovered, and the right target is a...
  </details>

- **2026-07-01** — Hongxing Li, Xiufeng Huang, Dingming Li et al. — [Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning](http://arxiv.org/abs/2607.01191v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained visual reasoning remains challenging for vision-language models, especially when small but critical visual cues are buried in high-resolution images. Existing approaches rely on repeated cropping or test-time visual search to introduce local evidence, but they typically do not explicitly distinguish perception from reasoning. In this paper, we propose Perceive-to-Reason (P2R), a unified framework that formulates fine-grained visual reasoning as a two-stage process: the model first l...
  </details>

- **2026-07-01** — Bingchen Zhao, Sara Beery, Oisin Mac Aodha — [Autonomous Scientific Discovery via Iterative Meta-Reflection](http://arxiv.org/abs/2607.01131v1)
  <details><summary>📄 Abstract</summary>
  Autonomous scientific discovery systems offer the potential to accelerate research by automating the process of hypothesis generation and validation. However, current systems operate within constrained search spaces or require predefined research questions, limiting their capacity for true open-ended inquiry. Furthermore, while they generate hypotheses iteratively, they largely lack the ability to explicitly synthesize their own accumulated findings to uncover complex, interconnected phenomena. ...
  </details>

- **2026-07-01** — Yin-Jie Li, Yuan-Zhu Wang, Shao-Peng Tang et al. — [Smoking-gun evidence for hierarchical black-hole mergers](http://arxiv.org/abs/2607.01121v1)
  <details><summary>📄 Abstract</summary>
  How stellar-mass black holes grow after their birth is a central open question in astrophysics. Gravitational-wave observations have revealed a subpopulation of coalescing black holes with both high masses and high spins, but whether these properties arise from hierarchical mergers in dense stellar environments or from accretion onto isolated black holes has remained unresolved. Here, using a flexible mixture population model applied to the 259 binary black hole mergers in GWTC-5, we show that t...
  </details>

- **2026-07-01** — Miruna Cretu, John Bradshaw, Patricia Suriana et al. — [SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles](http://arxiv.org/abs/2607.01105v1)
  <details><summary>📄 Abstract</summary>
  We present SynLaD, a latent diffusion framework for small-molecule generation that unifies ligand-based drug design objectives (what to make) with synthetic accessibility (how to make it). Current models typically optimize one objective at the expense of the other, creating a bottleneck for discovering high-scoring and synthesizable molecules. SynLaD combines reaction-constrained generation with pharmacophore-conditioned 3D design by learning a latent space that decodes to both 3D structures and...
  </details>

- **2026-07-01** — Zinan Tang, Yukun Zhang, Shaomian Zheng et al. — [CausalMix: Data Mixture as Causal Inference for Language Model Training](http://arxiv.org/abs/2607.01104v1)
  <details><summary>📄 Abstract</summary>
  In Large Language Model (LLM) training, data mixing plays a pivotal role in determining model performance. Recent methods optimize mixture weights via proxy models, but they rely on the assumption of static data distributions. As a result, when the underlying data pool shifts, these methods require costly retraining from scratch. This limitation restricts their ability to scale seamlessly from small settings to larger data pools and model sizes. In this paper, we propose CausalMix to address thi...
  </details>

- **2026-07-01** — Byeongguk Jeon, Seonghyeon Ye, JaeHyeok Doo et al. — [RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation](http://arxiv.org/abs/2607.01060v1)
  <details><summary>📄 Abstract</summary>
  Video world models are emerging as a scalable alternative for evaluating generalist robot policies, bypassing the physical constraints and engineering burdens of real-world deployment. However, evaluating policies with video world models remains challenging, as world-model errors can make generated rollouts unreliable and slow inference limits large-scale throughput. We introduce RoboWorld, an automated evaluation pipeline that pairs a fast autoregressive video world model with a task-progress-a...
  </details>

- **2026-07-01** — Li Jin, Jian Huang, Junde Lu et al. — [Slope-Guided Mamba and Angular-Refined Transformer for Light Field Super-Resolution](http://arxiv.org/abs/2607.00965v1)
  <details><summary>📄 Abstract</summary>
  Light Field Super-Resolution (LFSR) necessitates accurate modeling of spatial-angular correlations while preserving intrinsic 4D ray coherence. However, maintaining such high-dimensional consistency remains challenging, primarily due to two inherent limitations in prevailing modeling paradigms. First, spatial and angular dimensions are often modeled in a decoupled manner, restricting early cross-dimensional interaction and leading to geometric inconsistencies. Moreover, although continuous seque...
  </details>

- **2026-07-01** — Jingchen Ni, Cangjin Yu, Dan Jiang et al. — [MG-RWKV: Multi-Grained Context-Aware RWKV for Temporal Forgery Localization](http://arxiv.org/abs/2607.00902v1)
  <details><summary>📄 Abstract</summary>
  Driven by Artificial Intelligence-Generated Content (AIGC), the authenticity of audio-visual content is facing severe challenges. Temporal Forgery Localization (TFL) aims to precisely identify manipulated segments within untrimmed sequences. However, existing methods are limited by CNNs' local receptive fields or Transformers' quadratic complexity, while emerging linear models often struggle to balance global authentic context compression with local abrupt forgery perception. To address this, we...
  </details>

- **2026-07-01** — Maximilian Idahl, Jörg Tiedemann, Sampo Pyysalo et al. — [MultiSynt/MT: Trillion-Token Multi-Parallel Pre-Training Data Translated Across 36 Languages](http://arxiv.org/abs/2607.00890v1)
  <details><summary>📄 Abstract</summary>
  Open web-scale pre-training corpora remain concentrated in English, limiting multilingual LLM development. We introduce MultiSynt/MT, an open synthetic parallel corpus with approximately 4.8 trillion target-language tokens across 36 European languages, produced by translating 100 billion high-quality Nemotron-CC tokens with Tower+ and OPUS-MT/HPLT-MT systems. For many medium- and lower-resource European languages, this is the largest openly available pre-training resource. On a broad multilingua...
  </details>

- **2026-07-01** — Xudong Li, Mengdan Zhang, Peixian Chen et al. — [OmniView-Space: Reinforcing Spatial Reasoning via Multi-Perspective Spatial Mapping](http://arxiv.org/abs/2607.00881v1)
  <details><summary>📄 Abstract</summary>
  Spatial intelligence remains a persistent challenge for Multimodal Large Language Models (MLLMs), as it requires coherent spatial scene representations beyond basic object recognition. Existing methods typically build such representations through textual reasoning or 3D reconstruction. However, they often falter during multi-step reasoning, particularly when required to dynamically re-anchor evidence to the specific camera-, object-, or direction-centric reference frames demanded by complex quer...
  </details>

- **2026-07-01** — Biswa Sengupta — [Self-Evolving Agents with Anytime-Valid Certificates](http://arxiv.org/abs/2607.00871v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents violate the assumption behind most learning-theoretic guarantees: the data, evaluator, components, and hypothesis space are produced by the policy being updated. We present \textbf{SEA}, an architecture that confines self-modification to a small steering adapter and a versioned harness around a \emph{frozen} base model and admits each modification only through an anytime-valid gate that emits an auditable certificate against a fixed error budget. Five loop controllers compos...
  </details>

- **2026-07-01** — Andrea Sanchietti, Riccardo Marin, Bharat Lal Bhatnagar et al. — [Stitched Embeddings: A Unified Latent Space for 3D Garments and 2D Patterns](http://arxiv.org/abs/2607.00829v1)
  <details><summary>📄 Abstract</summary>
  While garments are essential for realistic digital humans, their topological variety makes them much harder to model than parametric bodies. Traditional tailoring relies on 2D sewing patterns, yet bridging these patterns to 3D geometry currently requires physical simulations. We present Stitched Embeddings, the first simulation-free framework to unify 3D garment reconstruction and sewing pattern inference within a single bidirectional latent space. By leveraging the geometric priors of a pretrai...
  </details>

- **2026-07-01** — Kyan Mahajan, Mohammad Saqlain — [SpiralFovea: Input-Adaptive Foveated Tokenization as a Third Lever of Resource-Adaptive Inference](http://arxiv.org/abs/2607.00780v1)
  <details><summary>📄 Abstract</summary>
  Most adaptive-inference techniques for foundation models change what the model does - early exit, MoE routing, KV-cache compression, dynamic attention sparsity. The input that hits the backbone, however, remains a fixed-grid tokenisation indifferent to image content. We argue that this is a missed lever. We present SpiralFovea, a parameter-free, input-adaptive tokeniser in which token identity, location, scale, and count are all functions of local visual entropy and selection completes before an...
  </details>

- **2026-07-01** — Mark Russinovich, Ram Shankar Siva Kumar, Ahmed Salem — [Phantom References: Hallucinated Citations That Survive Peer Review at Top-Tier Conferences](http://arxiv.org/abs/2607.00738v1)
  <details><summary>📄 Abstract</summary>
  Large language models can generate polished scientific text that includes unsupported claims, allowing hallucinations to enter the archival record. Assessing this risk via technical statements is difficult and often requires expert judgment, but citations provide a more auditable surface: a reference either resolves to a real scholarly work with compatible authorship, or it does not.   We measure citation hallucination in peer-reviewed proceedings using a conservative definition limited to ident...
  </details>

- **2026-07-01** — Kyuwon Kim, Sunjae Yoon, Chang D. Yoo — [SPECSIA: Stylization Dataset for Novel-View Enhancement in Drawing-based 3D Animation](http://arxiv.org/abs/2607.00525v1)
  <details><summary>📄 Abstract</summary>
  Generating animation from a single 2D drawing is challenging because the output must preserve character appearance while remaining plausible and temporally coherent under motion. Existing drawing-based 3D animation pipelines often use sample-wise 2D refinement to align animated renderings with the input image, but such optimization tends to overfit to the observed view and fails to correct projection-induced artifacts in novel views. To address this limitation, we introduce SPECSIA-15K, a paired...
  </details>

- **2026-07-01** — Emil Joswin, Srujananjali Medicherla, Priyanka Mary Mammen — [A Mechanistic View of Authority Hierarchy in LLM Sycophancy](http://arxiv.org/abs/2607.00415v1)
  <details><summary>📄 Abstract</summary>
  Authority bias poses a critical safety concern in language models: models systematically prioritize social cues from authority figures over factual consistency, swaying their answers based on source credibility rather than evidence. We mechanistically investigate this phenomenon using a controlled medical QA setting, where hints suggesting incorrect answers are attributed to personas of varying expertise. Across Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B, we find that models respond in a graded mann...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 537 |
| prompt-injection | 444 |
| memory-poisoning | 35 |
| tool-use-attack | 89 |
| backdoor | 381 |
| adversarial-attack | 520 |
| privacy-leakage | 3634 |
| steganography | 51 |
| misuse | 788 |
| red-teaming | 104 |
| vulnerability | 2332 |
| defense | 1961 |
| alignment | 1776 |
| robustness | 1602 |
| watermark | 159 |
| unlearning | 81 |
| agent-safety | 48 |
| benchmark | 53 |
| survey | 237 |
| other | 5106 |

---

📚 **全部 19938 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-07-07 03:24:57*