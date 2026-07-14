<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-20678-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-14 09:06 ｜ **论文总数 / Total Papers**: 20678（近 30 天 / Recent 30 days: 4090）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 20678 篇论文（含摘要、分类筛选、搜索）/ View all 20678 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 543
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 452
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 36
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 91
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 386
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 528
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3673
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 52
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 809
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 107
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2409
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2040
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1879
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1723
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 175
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 82
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 48
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 53
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 244
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5348

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4090 篇，完整 20678 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4090 papers from the last 30 days (with date, authors & abstract). For the full list of 20678 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

- **2026-07-13** — Junyoung Park, Namgyu Park, Sechan Lee et al. — [MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment](http://arxiv.org/abs/2607.11070v1)
  <details><summary>📄 Abstract</summary>
  Modern large language models (LLMs) operate in interactive multi-turn settings, making multi-turn jailbreaking a realistic threat model and an important setting for automated red teaming. A core challenge in learning multi-turn jailbreak attackers is credit assignment: different turns contribute differently to the final outcome, yet existing learning signals are often too coarse to identify their individual contributions. We propose decomposed credit GRPO (DC-GRPO), a unified turn-level credit a...
  </details>

- **2026-07-09** — Jennifer Za, Julija Bainiaksina, Nikita Ostrovsky et al. — [Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring](http://arxiv.org/abs/2607.08066v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring is a promising safety mechanism for AI agents, based on the premise that visible reasoning traces can surface misaligned or deceptive behavior. While effective in standard scenarios, recent work highlights that LLMs remain vulnerable to persuasion-based jailbreaks, where natural-language arguments override model constraints. We stress-test whether this vulnerability extends to monitoring LLMs: can an adversarial agent persuade its CoT monitor to approve proposed...
  </details>

- **2026-07-08** — Mohamed Amine Merzouk, Nolan Smyth, Damiano Fornasiere et al. — [Efficient Safety Alignment of Language Models via Latent Personality Traits](http://arxiv.org/abs/2607.07918v1)
  <details><summary>📄 Abstract</summary>
  Current safety methods for large language models are known to be vulnerable to adversarial attacks, motivating research into robust alternatives. Latent Adversarial Training (LAT) is among the most effective defenses, but can degrade utility and requires training on large datasets of harmful prompts. We introduce Latent Personality Alignment (LPA), which replaces explicit harm refusal with adversarial training on just 66 harm-agnostic statements drawn from psychometric personality literature. We...
  </details>

- **2026-07-08** — Anupam Wagle, Ifrat Ikhtear Uddin, Chaowei Zhang et al. — [Mechanistic Interpretability of LLM Jailbreaks via Internal Attribution Graphs](http://arxiv.org/abs/2607.07903v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit remarkable capabilities but remain highly vulnerable to adversarial prompts and jailbreak attacks. Existing approaches primarily analyze these failures through input-output behaviors or attribution methods, offering limited insight into how adversarial perturbations alter the model's internal reasoning. Consequently, the mechanisms underlying unsafe or incorrect behaviors remain poorly understood. We introduce a mechanistic framework for diagnosing LLM vulner...
  </details>

- **2026-07-08** — Victor Giannakouris, Immanuel Trummer — [Breaking Database Lock-in: Agentic Regeneration of High Performance Storage Readers for Database Bypass](http://arxiv.org/abs/2607.07696v1)
  <details><summary>📄 Abstract</summary>
  Analytical workloads operating on data stored in external database systems face a fundamental bottleneck: data access is guarded entirely by the database driver, like JDBC or ODBC, forcing all reads through query execution and other driver layers that are not designed for bulk columnar analytics. We present Jailbreak, an approach that bypasses the database engine entirely by reading storage files directly and materializing data as in-memory columnar buffers. Jailbreak's key insight is that datab...
  </details>

- **2026-07-08** — Aoxiong Zeng, Yuxin Yang, Xiangquan Yang — [Online Data Selection Is Implicit Alignment](http://arxiv.org/abs/2607.07023v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) is often treated as a capability-adaptation step, while alignment is attributed to later preference optimization or reinforcement learning. This separation is incomplete: when examples are scored and kept online during fine-tuning, the choice of which data to train on already changes the model's behavioral preferences. We study online data selection as an implicit alignment mechanism. Given the same base model, optimizer, and selected-token budget, we compare random,...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 7 papers

- **2026-07-12** — Bálint Gyevnár, Atoosa Kasirzadeh, Nihar B. Shah — [Distributed Denial of Science: How Indirect Data Poisoning of AI Systems Can Industrialize Scientific Fraud](http://arxiv.org/abs/2607.10712v1)
  <details><summary>📄 Abstract</summary>
  Scientific fraud is the instrument of doubt that malicious entities can use to establish controversy in science. Historically, it required the resources of a company: deep pockets, ghostwritten articles, and corrupt academics. Today, Artificial Intelligence (AI) is increasingly automating scientific research, so we ask: Can a remote adversary weaponize the honest use of AI in science to compromise scientific integrity? We envision and empirically evaluate a new attack, indirect data poisoning, i...
  </details>

- **2026-07-11** — Ruksat Khan Shayoni, Muhammad Faraz Shoaib, S M Asif Hossain et al. — [NetInjectBench: Benchmarking Indirect Prompt Injection in Tool-Using Large Language Model Agents for Network Operations](http://arxiv.org/abs/2607.10490v1)
  <details><summary>📄 Abstract</summary>
  Tool-using large language model (LLM) agents are attractive for network operations, but tickets, alerts, logs, runbooks, and ChatOps messages can carry indirect prompt injections. We present NetInjectBench, a 130-scenario benchmark that separates untrusted artifact text, trusted policy metadata, and evaluation labels for network-operation tool use. The sample contains 40 benign, 40 weak-attack, 40 strong-attack, and 10 approved high-impact change scenarios; each is evaluated with Qwen2.5-7B, Lla...
  </details>

- **2026-07-11** — Yaxin Li, Hao Wang, Yanda Shao et al. — [Devil in the Lens: Analyzing and Defending Physical Prompt Injection Against Vision-Language Models on Wearable Devices](http://arxiv.org/abs/2607.10269v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are rapidly deployed on human-facing wearable devices such as smart glasses to enable multimodal perception and AI-assisted decision-making. While prior research has demonstrated the risks of visual prompt injection into digital image inputs of VLMs, the unique security challenges posed by the increasing integration between physical environments and wearable intelligence, such as those embodied in VLM-enabled AI glasses, remain underexplored. Toward understanding an...
  </details>

- **2026-07-09** — Hugo García Cuesta, Pablo Mateo Torrejón, Alfonso Sánchez-Macián — [Multi-Agent Firewall Architecture for Privacy Protection of Sensitive Data in Interactions with Language Models](http://arxiv.org/abs/2607.08282v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) have become essential productivity tools, their integration into workflows without adequate safeguards creates significant risks. This paper proposes an open-source, privacy-focused, user-facing firewall designed to secure both web-based and programmatic LLM interactions. The architecture combines a browser extension and a proxy for total traffic interception across both HTTP(S) and WebSocket communications. At its core, a flexible multi-agent pipeline delivers...
  </details>

- **2026-07-09** — Corban Villa, Alp Eren Ozdarendeli, Sijun Tan et al. — [Prismata: Confining Cross-Site Prompt Injection in Web Agents](http://arxiv.org/abs/2607.08147v1)
  <details><summary>📄 Abstract</summary>
  Autonomous web agents promise to automate everyday browsing tasks, but inherit one of the web's oldest attack surfaces. Cross-Site Scripting proved that mixing trusted and untrusted content is dangerous, even on benign pages. Agents resurface this risk by interpreting natural language as instructions, allowing third-party and user-generated content to hijack the agent via prompt injection. The core challenge is that deriving a task-specific security policy requires reasoning over page structure ...
  </details>

- **2026-07-08** — Phat T. Tran-Truong, Xuan-Bach Le, Minh Nhat Nguyen — [FedMark-FM: Auditable, Risk-Adjusted Data Markets for Federated Foundation-Model Adaptation](http://arxiv.org/abs/2607.07529v1)
  <details><summary>📄 Abstract</summary>
  Federated foundation-model adaptation increasingly relies on heterogeneous private artifacts (retrieval corpora, prompts and demonstrations, LoRA adapters, preference and safety data, and update sketches), yet existing federated-learning incentive mechanisms price clients as homogeneous data or update providers. This assumption poorly matches foundation-model pipelines, where contribution value is heterogeneous, non-IID, pipeline-dependent, privacy-constrained, and vulnerable to strategic behavi...
  </details>

- **2026-07-08** — Aya Spira, Stav Cohen, Elad Feldman et al. — [Beware of Agentic Botnets: Scalable Untargeted Promptware Attacks via Universal and Transferable Adversarial HalluSquatting](http://arxiv.org/abs/2607.07433v1)
  <details><summary>📄 Abstract</summary>
  The growing adoption of agentic LLM applications has introduced a new threat previously named as promptware. While prior work has established that adversaries can exploit direct channels to LLM applications to apply promptware under weak threat models, many applications do not provide any direct channels that could be exploited for prompt injection beyond the Internet. This raises a question: can attackers exploit LLM applications at scale without any direct channels in practical threat models? ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-07-13** — Junrui Zhang, Zemin Chen, Lusi Li et al. — [Input-Aware Dynamic Backdoor Attack Against Quantum Neural Networks](http://arxiv.org/abs/2607.11843v1)
  <details><summary>📄 Abstract</summary>
  Quantum Neural Networks (QNNs) are a promising framework for quantum machine learning on near-term quantum devices, but their security risks remain insufficiently understood. Studies have shown that QNNs are vulnerable to backdoor attacks, yet existing quantum backdoors mostly rely on a fixed trigger shared by all poisoned inputs. This fixed-trigger design is a major weakness because many defenses detect or weaken the repeated patterns such triggers leave in data representations. Although input-...
  </details>

- **2026-07-13** — Yibo Hu, Ren Wang — [When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems](http://arxiv.org/abs/2607.11751v1)
  <details><summary>📄 Abstract</summary>
  As multi-agent, tool-using LLM systems are deployed, a common safety net is a runtime monitor that checks each message, tool call, or step on its own. We show this net has a fundamental hole. A distributed backdoor splits a harmful payload across agents, so every local check passes while the assembled object is the attack. The monitor can be right on every step and still miss the attack. The problem is not splitting itself: split fragments can still leak suspicious tokens or provenance edges. Th...
  </details>

- **2026-07-09** — Zifan Zhang, Minghong Fang, Dianwei Chen et al. — [Securing Autonomous Vehicle Systems via Twin-Aware Federated Reinforcement Learning](http://arxiv.org/abs/2607.08137v1)
  <details><summary>📄 Abstract</summary>
  Federated reinforcement learning (FRL) is crucial for enabling collaborative learning across multiple agents without sharing raw data, thereby enhancing privacy and scalability in the decision-making process within dynamic vehicular environments. However, poisoning attacks pose a significant threat to the security and reliability of FRL-based systems, particularly in safety-critical autonomous driving, where this vulnerability remains largely unexplored. These attacks can compromise the global c...
  </details>

- **2026-07-09** — Anjun Gao, Yueyang Quan, Zhuqing Liu et al. — [Beware What You Autocomplete: Forensic Attribution of Backdoored Code Completions](http://arxiv.org/abs/2607.08011v1)
  <details><summary>📄 Abstract</summary>
  Large language models have enabled powerful code completion systems that assist developers by predicting subsequent lines of code. However, these models remain vulnerable to backdoor attacks, where malicious fine-tuning data covertly implants unsafe behaviors. Despite advances in defensive techniques, adaptive and sophisticated backdoor attacks still evade detection and mitigation. We present CodeTracer, a forensic framework that traces malicious code completions back to the backdoor fine-tuning...
  </details>

- **2026-07-08** — Oliver Makins, Orazio Angelini, Zohreh Shams et al. — [Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors](http://arxiv.org/abs/2607.07368v1)
  <details><summary>📄 Abstract</summary>
  AI control is a family of techniques to prevent an AI with malicious goals from subverting its operator's intent. AI Control usually studies a single agent in one trajectory, but real deployments run many agents over shared infrastructure, and the most severe risks (model-weight exfiltration, training-run poisoning) plausibly need several agents acting in concert. We initiate the empirical study of multi-agent AI control, formalising distributed attacks in which several agents jointly aim for a ...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 7 papers

- **2026-07-13** — Congren Dai, Danni Zhao, Enyang Liu et al. — [Verifier-Guided Twelve-Tone Composition: A Generate-Verify-Repair Harness for Symbolic Music Generation](http://arxiv.org/abs/2607.11334v1)
  <details><summary>📄 Abstract</summary>
  Large language models can produce superficially legal twelve-tone scores that collapse into degenerate textures. We introduce a neuro-symbolic harness that wraps a language-model proposer in a generate-verify-repair-trace loop with symbolic verification. The complete pipeline improves event-local consistency without claiming whole-piece legality. Across 40 controlled tasks and four paired models, audited delivery yield rises from 13.3% under raw generation to 48.1% with the harness, which explic...
  </details>

- **2026-07-13** — Chenyang Li, Kaige Li, Zeyu Jiang et al. — [AdvNav: Behavior-Guided Black-Box Adversarial Attacks on Vision-Language Navigation](http://arxiv.org/abs/2607.11063v1)
  <details><summary>📄 Abstract</summary>
  Despite progress in Embodied AI, Vision-and-Language Navigation systems remain vulnerable to adversarial visual disturbances. Most existing methods rely on white-box access to target model gradients, which is often unrealistic for real-world deployed systems and computationally exhaustive due to recursive backpropagation for optimization, limiting their applicability. While previous black-box methods predominantly target single-step, instantaneous decision tasks, they struggle to handle the task...
  </details>

- **2026-07-11** — Qi Lu, Ziqi Zhou, Yufei Song et al. — [Imperceptible and Reversible Adversarial Examples against Vision-Language Models for Privacy Protection](http://arxiv.org/abs/2607.10329v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models (VLMs) offer powerful multimodal ability but also expose users to text-based privacy attacks where adversaries crawl online photos and query VLMs to extract sensitive attributes. Existing reversible adversarial example (RAE) methods protect images in purely visual tasks but fail in multimodal settings, and current adversarial examples on VLMs rely on high frequency noise that severely degrades visual quality. We propose CloakDiff, the first framework for reversible, high f...
  </details>

- **2026-07-09** — Eugene Ng Yi Sheng, Bingquan Shen — [Formal Mechanisms for Market Stability in Self-Interested Agent Societies: A Marketplace Simulation Study](http://arxiv.org/abs/2607.08652v1)
  <details><summary>📄 Abstract</summary>
  Self-interested agents, left unconstrained, tend toward defection in repeated social dilemmas, causing cooperative gains from trade to collapse. This paper investigates what formal mechanisms, layered on top of unrestricted communication, are sufficient for a society of such agents to maintain market stability, and how resilient those mechanisms are to adversarial attack. We instantiate the research question as a multi-agent marketplace simulation where 18 LLM agents (DeepSeek-V3) with complemen...
  </details>

- **2026-07-08** — Giulia Marchiori Pietrosanti, Giulio Rossolini, Giorgio Buttazzo — [Adversarial Decoys: Misdirecting Attention-Based Defenses in ViT](http://arxiv.org/abs/2607.07922v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) remain vulnerable to localized adversarial attacks, e.g., adversarial patches, while recent test-time defenses mitigate them by suppressing image tokens with abnormally high attention scores. These defenses exploit a strong coupling between attention and adversarial effectiveness: adversarial tokens often need to attract substantial attention to influence the prediction. We introduce adversarial decoys, independently optimized image patches that redirect the attention,...
  </details>

- **2026-07-08** — Zhenpeng Li — [Controllability-Aware Adversarial Examples Against LLM-Based Network Traffic Classifiers](http://arxiv.org/abs/2607.07739v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly explored as network intrusion detection classifiers, but their adversarial robustness under realistic attacker constraints remains unclear. We present a controllability-aware black-box transfer framework for LLM-based network traffic classifiers. The framework partitions flow features into directly controllable (DC), indirectly controllable (IC), and uncontrollable (UC) groups according to network communication semantics, then restricts perturbations...
  </details>

- **2026-07-08** — Xifeng Zhang, Tao Hu, Yijie Peng et al. — [A Unified Detection Framework for AI-Related Content and Artifacts](http://arxiv.org/abs/2607.07527v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) is a double-edged sword: while it has achieved remarkable success across a wide range of domains, its deployment also calls for effective oversight and regulation, for which the detection of AI-related content and artifacts is perhaps the most direct and cost-effective approach. To this end, we propose a unified detection framework based on Mahalanobis distance scores (MDS), applicable to several important settings, including the detection of large language model (LL...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 17 papers

- **2026-07-13** — Jijie Li, Jiankuo Zhao, Xiangyu Zhu et al. — [The Devil Is in the Leakage: A Disentangled Dual-Purification Framework for High-Fidelity Hairstyle Transfer](http://arxiv.org/abs/2607.11281v1)
  <details><summary>📄 Abstract</summary>
  Hairstyle transfer aims to synthesize a photorealistic portrait by transplanting the hairstyle from a reference image onto a source subject while preserving the source identity. Recent foundation models show strong generative capability, but they struggle with the zero-shot disentanglement required for precise local editing, often entangling the reference hairstyle with its original identity and pose. Existing diffusion-based pipelines typically decompose the task by first generating a "bald" im...
  </details>

- **2026-07-13** — Yiming Zhang, Jiangrong Wu, Yuhong Nan — [FlowArk: Boosting Agentic Data-flow Analysis for Android Apps via Context-Aware Knowledge Reuse](http://arxiv.org/abs/2607.11308v1)
  <details><summary>📄 Abstract</summary>
  Data-flow analysis is foundational to Android app privacy and security auditing. Recent coding agents can assist with non-trivial source-to-sink data-flow analysis tasks by searching, reading, and reasoning over repository code. However, when these tasks are executed as a batch workload, current agentic analysis setups incur substantial re-analysis cost. Agent instances assigned to different taint sources may inspect shared code fragments, because code reuse in the target app can cause different...
  </details>

- **2026-07-13** — Eddie Huang, Ken Liao, Iven Fu et al. — [NVAITC AI Scientist: A Governed End-to-End Research System -- A Hypertension GWAS Case Study](http://arxiv.org/abs/2607.11084v1)
  <details><summary>📄 Abstract</summary>
  Agentic research systems are emerging as a new paradigm for coordinating scientific workflows beyond isolated model inference, code generation, or statistical analysis. However, deployment in institutional biomedical environments requires governed mechanisms for research planning, data access, workflow orchestration, evidence tracking, reproducibility, and human oversight. We present NVAITC AI Scientist (NAIS), a governed end-to-end agentic research system designed to support domain-general scie...
  </details>

- **2026-07-13** — Junhao Ruan, Yuan Ge, Bei Li et al. — [ToFu: A White-Box, Token-Efficient Agent Harness for Researchers](http://arxiv.org/abs/2607.11423v1)
  <details><summary>📄 Abstract</summary>
  Agentic coding tools present new opportunities to transform research workflows. The performance of agent systems built depends on both large language models (LLMs) and the harness around LLMs, which is the orchestration code that determines an agent's behavior. We present ToFu, an agentic harness for researchers that reads your codebase, edits files, runs commands, and integrates with your development tools. ToFu plays a dual role in research. As a research assistant, it supports practical resea...
  </details>

- **2026-07-13** — Aleh Manchuliantsau — [From Checker to Forecaster: Code-Owned Evaluation of Model-Generated Strategic Routes Under Delayed Ground Truth](http://arxiv.org/abs/2607.10972v1)
  <details><summary>📄 Abstract</summary>
  Many evaluations of model outputs rely either on contracts checkable at evaluation time or on feedback that arrives within the operating loop. We study the complementary setting in which ground truth is delayed, censored, or private, so deterministic code cannot check correctness at scoring time and must instead issue a code-owned provisional forecast. RouteCast instantiates this regime for model-generated typed strategic routes: models propose candidate routes and structured factors; point-in-t...
  </details>

- **2026-07-12** — Borzoo Rassouli, Morteza Varasteh — [Differentially Private Consistent Release of Counting Queries](http://arxiv.org/abs/2607.10952v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of releasing counting-query outputs through a stochastic mechanism that is both consistent and \((ε,δ)\)-differentially private. Consistency requires the released value to lie within the feasible range of the query, while utility is measured by the worst-case probability of error. We first derive a closed-form expression for the minimum achievable error probability and obtain an explicit optimal mechanism. By exploiting the active differential privacy constraints satisfied b...
  </details>

- **2026-07-12** — Elette Boyle, MohammadTaghi Hajiaghayi, Keivan Rezaei et al. — [Can Watermarking Techniques Help Prevent LLM Model Stealing?](http://arxiv.org/abs/2607.10794v1)
  <details><summary>📄 Abstract</summary>
  Model stealing attacks have recently been introduced, enabling the extraction of precise information from black-box commercial language models. In this work, we propose defense methods against a recent attack of \cite{carlini2024stealing} and extensions for extracting the hidden layer dimension of production language models. Our methods are inspired by watermarking techniques that perturb the logits layer of these models to prevent such attacks. We provide empirical experiments demonstrating the...
  </details>

- **2026-07-12** — Syed Irfan Ali Meerza, Oktay Ozturk, Amir Sadovnik et al. — [DiffUE: Enhancing Utility-Unlearnability Trade-off of Unlearnable Examples via Diffusion Autoencoders](http://arxiv.org/abs/2607.10580v1)
  <details><summary>📄 Abstract</summary>
  AI models are increasingly trained on personal images scraped from social media and public platforms, often without consent, leading to serious privacy violations, such as unauthorized facial recognition and targeted advertising. To counter this, researchers have developed unlearnable examples (UEs), images modified with imperceptible noise to prevent AI models from extracting meaningful information. However, existing UE methods primarily rely on pixel-space noise, which can be bypassed by relea...
  </details>

- **2026-07-12** — Mohannad Takrouri, Nicolas M. Cuadrado A., Martin Takáč — [WattCouncil: Context-Aware Household Energy Scenario Generation With Governed LLMs](http://arxiv.org/abs/2607.10720v1)
  <details><summary>📄 Abstract</summary>
  The accelerating shift toward low-carbon power systems, together with the widespread adoption of behind-the-meter technologies such as rooftop solar and electric vehicles, is placing new operational and analytical demands on electricity grids. At the same time, smart-grid research increasingly relies on machine learning (ML), yet progress is constrained by limited access to high-resolution household energy data due to privacy concerns, regulatory barriers, and collection costs. This work present...
  </details>

- **2026-07-12** — Chen Gu, Hui Wan, Donghui Hu et al. — [PromptGraph: Graph-Guided Prompt Sanitization for Balancing Privacy and Utility in LLM Inference](http://arxiv.org/abs/2607.10709v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) services introduce a fundamental privacy challenge. Sensitive information may be inferred not only from explicit identifiers, such as names or phone numbers, but also from contextual associations among otherwise innocuous spans. Existing sanitizers typically assign privacy or utility signals to individual spans without explicitly modeling pairwise relationships among them. In this paper, we propose PromptGraph, a graph-guided prompt-sanitization approach for privacy-pr...
  </details>

- **2026-07-11** — Jiayi Tian, Shiao Liu, Yuting Xu et al. — [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](http://arxiv.org/abs/2607.10350v1)
  <details><summary>📄 Abstract</summary>
  Recent VLM and VLA systems have improved robotic perception and action prediction, yet long-horizon embodied agents still require a general runtime layer for reasoning, memory, tool use, verification, and cross-embodiment execution. We present ABot-AgentOS, a general robotic Agent Operating System that sits above low-level controllers and provides a deliberative agent layer for scene-conditioned planning, context-isolated skill execution, multi-stage verification, multi-modal memory, and edge-cl...
  </details>

- **2026-07-09** — Shashi Kumar, Yanis Labrak, Hasindri Watawana et al. — [When Synthetic Speech Is All You Have: Better Call GRPO](http://arxiv.org/abs/2607.08409v1)
  <details><summary>📄 Abstract</summary>
  LLM-based ASR adapted to regulated domains such as banking is bottlenecked by privacy: real speech is costly and legally constrained to collect, making synthetic text-to-speech (TTS) an attractive substitute. Yet synthetic speech stays acoustically mismatched with real recordings, and work on this gap has stayed within supervised fine-tuning (SFT). We instead turn to reinforcement learning, and show that Group Relative Policy Optimization (GRPO) extracts far more from the same synthetic speech t...
  </details>

- **2026-07-09** — Victor Jüttner, Xenia Wagner, Christoph Jahn et al. — [Simulating the Resident: Generating Executable Smart Home Schedules via LLM Personas](http://arxiv.org/abs/2607.08231v1)
  <details><summary>📄 Abstract</summary>
  Smart homes have emerged as an important domain for HCI research, including work on usable security and privacy. Ideally, studies in these areas draw on datasets collected in real homes with real residents, capturing authentic device interactions, network traffic, and daily routines. However, creating such datasets is slow, expensive, and raises significant privacy concerns, as it requires long-term observation of people in their most private spaces. We propose using LLMs to generate diverse res...
  </details>

- **2026-07-09** — Joongho Ahn, Moonsoo Kim — [From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents](http://arxiv.org/abs/2607.08028v1)
  <details><summary>📄 Abstract</summary>
  Enterprise large language model (LLM) applications often begin as prototypes whose behavior is carried by prompts and retrieval context. Productization adds requirements for source boundaries, entity routing, answer contracts, and reproducible traces. We present a harness-engineering approach that reconstructs this pattern into a traceable, auditable LLM-agent architecture: deterministic behavior moves into code, manifests, schemas, and validation artifacts around a replaceable composition bound...
  </details>

- **2026-07-09** — Vikash Sathiamoorthy, Shuo Huai, Hao Kong et al. — [FedTR: Federated Learning Framework with Transfer Learning for Industrial Visual Inspection](http://arxiv.org/abs/2607.08014v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) is a collaborative learning scheme to train deep learning models, where collaborating parties can consolidate their models without sharing local data with other parties, hence preserving data privacy. Nevertheless, when implementing FL in Industrial visual inspection (IVI), the constraints posed by limited data availability and the intricate nature of the inspection tasks significantly impact the performance of the resulting model. This paper introduces FedTR, a novel FL ...
  </details>

- **2026-07-08** — Jonathan Katzy, Ali Al-Kaswan, Razvan Mihai Popescu et al. — [The Poisoned Chalice of LLM Evaluation Report](http://arxiv.org/abs/2607.07481v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to evaluate and support software engineering tasks, yet the validity of these evaluations is often undermined by uncertainty about whether benchmark instances were seen during pretraining. This can lead to data contamination, which may inflate performance and result in misleading conclusions about model capability. Despite this, the training corpora of many modern models are only partially disclosed, making direct decontamination infeasible. This creat...
  </details>

- **2026-07-08** — Kiarash Ahi, Saeed Valizadeh — [Large Language Models (LLMs) and Generative AI in Cybersecurity and Privacy: A Survey of Dual-Use Risks, AI-Generated Malware, Explainability, and Defensive Strategies](http://arxiv.org/abs/2607.06963v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) and generative AI (GenAI) systems, such as ChatGPT, Claude, Gemini, LLaMA, Copilot, Stable Diffusion by OpenAI, Anthropic, Google, Meta, Microsoft, Stability AI, respectively, are revolutionizing cybersecurity, enabling both automated defense and sophisticated attacks. These technologies power real-time threat detection, phishing defense, secure code generation, and vulnerability exploitation at unprecedented scales. Following a rapid surge where LLM-generated malwar...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 16 papers

- **2026-07-13** — Romain Amigon — [Transformer-Guided Swarm Intelligence for Frugal Neural Architecture Search](http://arxiv.org/abs/2607.11826v1)
  <details><summary>📄 Abstract</summary>
  Neural Architecture Search (NAS) has automated the design of deep learning models but traditionally requires massive computational resources, often measured in thousands of GPU-days. In this paper, we propose a frugal and memetic NAS framework designed to democratize architecture design on consumer-grade hardware. Our approach combines the global macro-search capabilities of an autoregressive Transformer controller, trained via Reinforcement Learning (RL), with the local micro-exploitation of an...
  </details>

- **2026-07-13** — Praneeth Narisetty, Shiva Nagendra Babu Kore — [Mako: A Self-Evolving Agentic Operating System (SE-AOS) for Autonomous Web Exploitation](http://arxiv.org/abs/2607.11288v1)
  <details><summary>📄 Abstract</summary>
  We introduce the Self-Evolving Agentic Operating System (SE-AOS): a new class of AI agent that treats exploit capability as a mutable, versioned kernel it extends at runtime, observing its own failures, synthesising new capabilities, proving them against a live target, and hot-loading them back into itself. Mako is the first SE-AOS instance for security research and the autonomous web exploitation engine developed within LaunchSafe. LaunchSafe builds autonomous security agents for continuous off...
  </details>

- **2026-07-13** — Ahmed Omar Salim Adnan, Yogananda Manjunath, Shivanjali Khare — [An Explainable Agentic System for Detection of Conversational Scams with Summary-Based Memory](http://arxiv.org/abs/2607.11707v1)
  <details><summary>📄 Abstract</summary>
  Following the rapid progress of generative Artificial Intelligence, there is a growing threat posed by conversational scams. These scams often span over multiple weeks or months, gradually build trust and request for money or sensitive information. Existing scam-detection systems mainly focus on isolated messages, which renders them inadequate against this evolving threat. This paper extends single-message phishing detection and presents an explainable agentic system for detecting sophisticated ...
  </details>

- **2026-07-13** — Aznaur Aliev, Carlos Hinojosa, Abdelrahman Eldesokey et al. — [HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models](http://arxiv.org/abs/2607.11475v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in large language models can be fragile under fine-tuning, as even benign task adaptation may increase harmful compliance. Existing defenses mainly follow two directions: they either intervene during or after fine-tuning through retraining or weight modification, which can be costly and may hurt task performance, or they use model-agnostic safety classifiers, which may miss failures specific to a given fine-tuned checkpoint. These limitations motivate a post hoc, model-specific,...
  </details>

- **2026-07-13** — Joris Voerman, Nicolas Sidere, Jean-Christophe Burie — [Video Transformer for Remote Identity Document Hologram Detection](http://arxiv.org/abs/2607.11419v1)
  <details><summary>📄 Abstract</summary>
  Remote identity authentification using Identification Documents has been a major challenge for several years. DeepFakes advent and the development of AI-guided tools helps fraudsters creating counterfeit ID Documents. Ensuring the authenticity of ID Documents has become a real clue in the seurization of remote authentification. This need is all the more pressing given the increasing digitization of administrative and transactional processes. To ensure widespread accessibility, the system should ...
  </details>

- **2026-07-12** — Chinmayi Dixit — [Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF](http://arxiv.org/abs/2607.10750v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data is widely used to train large language models because it is inexpensive to generate and easy to control. As models are increasingly deployed as agents, synthetic trajectories are likely to become an important source of training data for agentic behavior. We investigate the effects of training on synthetic agentic trajectories containing adversarial interactions, including actions such as terminating another agents process, lowering its scheduling priority, or accessing resources w...
  </details>

- **2026-07-12** — Piper Harris, Chad M. Topaz — [Institutional Harm through Threshold Cascades](http://arxiv.org/abs/2607.10726v1)
  <details><summary>📄 Abstract</summary>
  Can a population of people not individually inclined to harm others nonetheless produce harmful collective outcomes, purely because of the institutional structure they inhabit? Social scientists have long argued yes, but existing accounts are largely qualitative and provide no precise condition distinguishing safe institutions from unsafe ones. We develop a threshold cascade model in which agents have positive activation thresholds, harmful behavior is irreversible, and the institution exerts bo...
  </details>

- **2026-07-12** — Caihui Yan, Gang Cao, Huawei Tian et al. — [Effective Synthetic Image Detection via Noise Residual Clustering](http://arxiv.org/abs/2607.10695v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of generative artificial intelligence (AI) has made synthetic images remarkably realistic, posing security threats such as misinformation and fraud. It is significant to detect the synthetic image in the manner of passive and blind image authentication. Most existing detectors rely on supervised training with large labeled datasets, leading to high costs and degraded performance on unknown generative models. To attenuate such deficiencies, we propose a training-free detecti...
  </details>

- **2026-07-11** — Lingwei Wei, Dou Hu, Wei Zhou et al. — [Large Language Models in Misinformation Ecosystems: Misuse, Defense, and Vulnerability](http://arxiv.org/abs/2607.10402v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have transformed misinformation from a primarily content-centric problem into a broader ecosystem-level security challenge. When misused, LLMs create risks beyond false content generation, enabling attacks on the social contexts, evidence sources, retrieval corpora, and verification workflows that misinformation defense depends on. In this paper, we introduce a role-layer framework to unify these risks and defenses. The role dimension characterizes LLMs as attackers,...
  </details>

- **2026-07-11** — Lam D. Dao, Vang T. Nguyen, Anh M. T. Bui et al. — [Which Neurons Detect Malicious Code? A Probing Study of LLM Security Knowledge](http://arxiv.org/abs/2607.10221v1)
  <details><summary>📄 Abstract</summary>
  Background. Large language models (LLMs) have become increasingly capable of understanding and generating source code, leading to their widespread adoption in software engineering tasks such as code completion, repair, and vulnerability detection. However, despite their strong empirical performance, the internal mechanisms through which LLMs recognize malicious or vulnerable code patterns remain poorly understood. Aim. We investigated where the malware detection behavior is encoded inside LLMs F...
  </details>

- **2026-07-11** — Kefan Song, Yanjun Qi — [ANCHOR: Automated Alignment Auditing for CLI Agents on Real-World Harm](http://arxiv.org/abs/2607.10455v1)
  <details><summary>📄 Abstract</summary>
  Autonomous CLI agents can now execute hundreds of actions across multi-hour sessions: writing code, executing shell commands, browsing the web, and managing cloud infrastructure, all with minimal human oversight. Does greater autonomy invite greater risk? We introduce ANCHOR, an automated auditing framework that stress-tests CLI agents on illegal tasks grounded in public US court cases. ANCHOR deploys an auditor agent fine-tuned on dark personality data using supervised and reinforcement fine tu...
  </details>

- **2026-07-09** — Kutub Uddin, Nusrat Tasnim, Awais Khan et al. — [Do Transformations Reveal the Truth? Generative Residual Learning for Generalized AI-Generated Image Detection](http://arxiv.org/abs/2607.08674v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of generative AI has enabled the creation of highly realistic deepfake media, posing significant threats, including misinformation, digital identity theft, fraud, and manipulation of public opinion. AI-generated image (AIGI) detection is reliably challenging due to the diversity of generative methods and the subtle artifacts they leave behind. In this work, we propose GenRes, a novel framework for generative residual learning via a neural tensor network, which models fine-g...
  </details>

- **2026-07-08** — Syed Usama Imtiaz, Mitra Nasr Azadani, Nasrin Alamdari — [Scalable and Trustworthy Earth Observation Foundation Models](http://arxiv.org/abs/2607.07758v1)
  <details><summary>📄 Abstract</summary>
  Foundation models (FMs) have transformed machine learning from isolated task-specific model development toward general-purpose models pretrained on broad data and adapted to multiple downstream tasks. Earth observation (EO) is an important domain for this paradigm because satellite and airborne archives are large, high-revisit, and increasingly multimodal, while reliable field labels are often sparse. Remote sensing foundation models (RSFMs) cannot be transferred reliably/optimally without domai...
  </details>

- **2026-07-08** — Zikai Alex Wen, Corrazon Ogot, Juan Li et al. — [Forensic Schema for Psychological Manipulation in Cyber Fraud: LLM-Driven Victim Reports Analysis](http://arxiv.org/abs/2607.07751v1)
  <details><summary>📄 Abstract</summary>
  Existing cybercrime classification schemas capture contact metadata and financial transactions but omit the psychological manipulation techniques perpetrators employ. We present a forensic schema (four categories, 35 questions) adding 11 manipulation indicators and cryptocurrency evidence fields to established forensic foundations. Applied to 10,994 victim reports via large language model (LLM)-driven annotation and validated against two human annotators (mean LLM-human $κ= 0.69$, matching inter...
  </details>

- **2026-07-08** — Harry Owiredu-Ashley — [Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents](http://arxiv.org/abs/2607.07474v1)
  <details><summary>📄 Abstract</summary>
  Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another ...
  </details>

- **2026-07-08** — Lifei Liu, Haoran Yu, Xiaochong Jiang et al. — [Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety](http://arxiv.org/abs/2607.07097v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluations of multi-agent LLM systems often compare a direct prompt with a planner-executor pipeline and report the difference as a single "pipeline effect." We argue that this aggregate is difficult to interpret because it conflates three mechanisms: harmful intent may be reframed as plausible operational work, the planner may refuse or transform the request, and the executor may act under delegation prompts implying prior approval. To separate these factors, we introduce a five-conditi...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 3 papers

- **2026-07-13** — Xutao Mao, Xiang Zheng, Cong Wang — [Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming](http://arxiv.org/abs/2607.11698v1)
  <details><summary>📄 Abstract</summary>
  Production LLM agents such as Claude Code and Codex operate over untrusted content, files, commands, and workspace state, making safety failures directly actionable. Red-teaming must therefore keep pace with evolving models and tools. Existing approaches mainly optimize attack success and preserve artifacts such as benchmarks, payloads, or attack programs, which record where attacks succeed but not the enabling conditions behind unsafe agent behavior. We study automated red-teaming for productio...
  </details>

- **2026-07-13** — Yi Ting Shen, Kentaroh Toyoda, Alex Leung — [AMT-X: Phase-Structured Multi-Turn Red-Teaming with Checklist-Gated Evaluation](http://arxiv.org/abs/2607.11151v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluation of large language models (LLMs) relies largely on single-turn attack datasets and single-judge scoring, underestimating risk from adaptive multi-turn adversaries and reporting a single success rate that does not separate partially actionable outputs from those carrying complete operational detail. We propose AMT-X (Adaptive Multi-Turn Exploitation), a phase-structured multi-turn red-teaming framework. Unlike prior multi-turn attacks that rely on ad hoc escalation or free-form p...
  </details>

- **2026-07-08** — Yujiao Chen — [Institutional Red-Teaming: Deployment Rules, Not Just Models, Causally Shape Multi-Agent AI Safety](http://arxiv.org/abs/2607.07695v1)
  <details><summary>📄 Abstract</summary>
  We introduce institutional red-teaming, an evaluation methodology for testing deployment rules in multi-agent AI: hold the agents, objectives, and task state fixed, vary only one rule, and attribute the resulting change in collective behavior to that rule. We instantiate the methodology in IABench-CA, a consequence-allocation benchmark spanning 228 contexts, five canonical rules, and seven model populations (33,924 games), with a normative cooperative reference and auto-labelled reasoning traces...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 56 papers

- **2026-07-13** — Kerui Chen, Jinglu Wang, Xiaoyi Zhang et al. — [Beyond the Single Camera: Agentic Multi-View Reasoning in Sports Video Understanding](http://arxiv.org/abs/2607.11844v1)
  <details><summary>📄 Abstract</summary>
  Recent Multimodal Large Language Models (MLLMs) achieve strong performance on single-view video understanding benchmarks. However, sports videos involve dense occlusion, rapid motion, and complex interactions that are difficult to resolve from a single viewpoint. In practice, sports events are recorded from multiple camera angles, providing complementary evidence used by referees. Yet, no existing benchmark evaluates MLLMs on multi-view sports video understanding. To address this gap, we introdu...
  </details>

- **2026-07-13** — Moritz Schaffenroth, Uwe Kölbel, Heike Lepke et al. — [Multi-Agent Reinforcement Learning for C-V2X RAT Selection](http://arxiv.org/abs/2607.11744v1)
  <details><summary>📄 Abstract</summary>
  Vehicles are increasingly equipped with advanced V2X communication capabilities. While early V2X apps utilized services such as Cooperative Awareness Messages, recent developments have allowed more advanced applications including cooperative driving, shared perception, and sensor-sharing services. The broader mix of applications leads to heterogeneous requirements for latency and reliability. At the same time multiple communication technologies for V2X are available with pros and cons. Hybrid V2...
  </details>

- **2026-07-13** — Iman Johary, Guillaume Bied, Alexandru C. Mara et al. — [STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling](http://arxiv.org/abs/2607.11722v1)
  <details><summary>📄 Abstract</summary>
  Career paths encode decades of skill acquisition, role transitions, and educational investment, and understanding them at scale underpins workforce planning, labor market policy, and job recommendation. Resumes are a rich source of information about career paths: they contain detailed descriptions of work experience, education, and skills. Yet their unstructured, heterogeneous, and multilingual nature has long prevented large-scale systematic analysis. With the advent of large language models (L...
  </details>

- **2026-07-13** — Julie Gilbert, Francesco Calzaferri — [Targeting DNA Methylation: New Paradigms and the Advent of Gene-Selective Tools](http://arxiv.org/abs/2607.11697v1)
  <details><summary>📄 Abstract</summary>
  DNA methylation can function as a toxic alkylation reaction exploited by chemotherapeutic agents to induce cancer cell death. However, finely tuned DNA methylation plays a fundamental role in cellular physiology, particularly in the epigenetic regulation of gene expression. Once thought to act solely as a repressor of gene transcription, its functional role has since been elucidated as genomic locus-specific and deeply connected with other epigenetic factors. Following the clinical approval of D...
  </details>

- **2026-07-13** — Chengcheng Yan, Qingsong Wang — [Structure-Feature Aligned Graph Learning via Alternating Constrained Optimization](http://arxiv.org/abs/2607.11577v1)
  <details><summary>📄 Abstract</summary>
  We introduce a constrained two-view framework for node prediction that aligns structure-conditioned GNN embeddings with a structure-free feature prior learned by an anchor model. Conventional Graph Neural Networks (GNNs) couple feature transformation and neighborhood aggregation, which renders them vulnerable to topology noise and heterophilous connections. To decouple this dependency, our framework utilizes an independent anchor network to capture intrinsic attribute features via a self-supervi...
  </details>

- **2026-07-13** — Tianyuan Zhang, Zonglei Jing, Jiangfan Liu et al. — [Technical Report on the CVPR 2026@AdvML Workshop Challenge](http://arxiv.org/abs/2607.11560v1)
  <details><summary>📄 Abstract</summary>
  Vision-language agents (VLAs) are increasingly used to interpret complex driving scenes and support safety-critical reasoning. This report presents the CVPR 2026@AdvML Workshop Challenge on adversarial multimodal attacks against autonomous-driving VLAs. Built on DriveLM-style multi-view visual question answering, the challenge represents each scene with six synchronized camera images and a structured collection of driving-related question-answer pairs. Participants generate adversarial images an...
  </details>

- **2026-07-13** — Xiaolin Wen, Feng Liang, Yuanye Ma et al. — [ManiScope: LLM-Assisted Visual Analytics of Cryptocurrency Manipulation Risk](http://arxiv.org/abs/2607.11451v1)
  <details><summary>📄 Abstract</summary>
  Cryptocurrency markets are vulnerable to trade-based manipulation, such as wash trading, which can distort price signals and mislead investors. Prior research has mainly focused on detecting manipulation using fixed rules or labeled examples, offering limited flexibility and interpretability for assessing potential risks. Existing visual analytics tools can reveal basic manipulation-related signals, such as token distribution, but still require substantial manual effort to integrate holder relat...
  </details>

- **2026-07-13** — Minase Mekete Mengistu, Juri Di Rocco, Phuong T. Nguyen et al. — [TerraRepair: A Tool-Grounded LLM Agent for Infrastructure-as-Code Repair](http://arxiv.org/abs/2607.11390v1)
  <details><summary>📄 Abstract</summary>
  Background: Infrastructure-as-Code (IaC) scanners detect cloud misconfigurations in Terraform and other IaC languages before deployment, but repairing the flagged configurations remains largely manual. Recent Large Language Model (LLM)-based repair approaches can repair some findings, but may hallucinate unsupported constructs or suppress warnings without fixing the issue. Aims: We study whether tool grounding can improve LLM-based Terraform repair, and when a finding should be escalated because...
  </details>

- **2026-07-13** — Mingxi Xu, Bowen Duan, Yi Gu et al. — [HandFlow: Fully Generative 4D Hand Recovery with Flow Matching](http://arxiv.org/abs/2607.11221v1)
  <details><summary>📄 Abstract</summary>
  Accurate monocular 4D hand reconstruction remains challenging. Per-frame discriminative regressors lack temporal context and often produce jittery predictions. Temporal models improve consistency by aggregating information across frames, but they are typically deterministic regressors, making them vulnerable to ambiguous observations caused by occlusion and motion blur. Generative modeling offers a natural alternative by learning a prior over plausible hand motion sequences, enabling coherent ha...
  </details>

- **2026-07-13** — Kim Hammar, Yuchao Li — [Recovery Control in Replicated Systems through Autonomous Multiagent Rollout](http://arxiv.org/abs/2607.11187v1)
  <details><summary>📄 Abstract</summary>
  We study recovery control in replicated computing systems. Such systems consist of replicas that collectively provide a service to a client population. This redundancy enables the system to withstand failures provided that failed replicas are recovered faster than new failures occur. We show that the problem of deciding when to initiate recovery of selected replicas can be formulated as a partially observable Markov decision problem (POMDP) with a multiagent structure. We exploit this structure ...
  </details>

- **2026-07-13** — Seohwan Yun, Jeeyoung Yun, Yongjin Kim et al. — [MusicMark: A Robust Generative Watermarking Framework for Music Generation](http://arxiv.org/abs/2607.11117v1)
  <details><summary>📄 Abstract</summary>
  AI music generation has rapidly advanced alongside commercial platforms, raising the need for reliable watermarking for provenance and attribution. However, existing audio watermarking research has largely focused on speech, and applying speech-oriented methods to music is challenging due to music's complex structure and rich acoustic texture. Most existing methods are post-hoc, adding imperceptible perturbations after generation rather than embedding watermarks as part of the content. This make...
  </details>

- **2026-07-13** — Zhen-Lin Chen, Maosen Sheng, Peng Lin et al. — [MMRM: A Multiplex Multimodal Representation Model for Product Ranking in E-commerce Search](http://arxiv.org/abs/2607.11030v1)
  <details><summary>📄 Abstract</summary>
  Multimodal information is pivotal for e-commerce search ranking. Existing works leverage multimodal data typically by fine-tuning general Multimodal Large Language Models (MLLMs) via collaborative signals, subsequently integrating the derived representations into ranking models as item features. Despite their efficacy, these methods face two primary limitations: (1) they rely on a single collaborative signal for MLLM fine-tuning, failing to exploit the heterogeneous signals essential for multita...
  </details>

- **2026-07-13** — Qiyang Sun, Yi Chang, Yupei Li et al. — [CHARM: Charge Calibration and Acoustic Rescue for LLM-based Multimodal Sarcasm Detection](http://arxiv.org/abs/2607.11102v1)
  <details><summary>📄 Abstract</summary>
  Sarcasm detection, the identification of discrepancies between literal and intended meaning, is a fundamental task in affective computing. However, zero-shot instruction-tuned Large Language Models (LLMs) systematically over-predict the positive (sarcastic) class across the entire capability spectrum, while the prosodic cues humans rely on remain underexploited and transfer unevenly across languages. We introduce CHARM (Charge Calibration and Acoustic Rescue for Multimodal Sarcasm Detection), a ...
  </details>

- **2026-07-12** — Joshua Haworth, Aryan Pasikhani, George Pavlides et al. — [Automated Stealthy Wear-Out Attack on Digital Twins With Deep Reinforcement Learning](http://arxiv.org/abs/2607.10830v1)
  <details><summary>📄 Abstract</summary>
  Digital Twins (DTs) have emerged as pivotal enablers of Industry 4.0, offering transformative capabilities such as real-time monitoring, advanced simulation, and precise control of physical assets. By bridging the physical and virtual domains, DTs facilitate seamless integration of data-driven decision-making and operational optimisation. However, this seamless interaction significantly expands the attack surface of industrial systems, creating vulnerabilities that adversaries can exploit. This ...
  </details>

- **2026-07-12** — Fengji Zhang, Tianyu Fan, Yuxiang Zheng et al. — [To Answer or to Abstain: Mitigating Search-Agent Hallucinations via Abstention-Aware Reinforcement Learning](http://arxiv.org/abs/2607.10738v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in equipping Large Language Models (LLMs) with search tools and outcome-reward reinforcement learning (RL) have achieved new state-of-the-art results on open-domain QA tasks. However, we argue that current training paradigms harbor a critical vulnerability: they predominantly reward correct answers but fail to penalize fabricated ones when retrieval fails, thereby implicitly exacerbating hallucinations. To address this, we propose Abstention-Aware Reinforcement Learning (AWA-RL),...
  </details>

- **2026-07-12** — Zipeng Gao, Zhi Zheng, Qingrong Xia et al. — [Unlocking Parallelism in Autoregressive Language Models via Speculative Decoding with Progressive Tree Drafting](http://arxiv.org/abs/2607.10661v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding has significantly accelerated Large Language Model (LLM) inference by alleviating memory-bound bottlenecks. However, traditional speculative decoding typically relies on auxiliary draft modules, incurring significant training and communication overhead. Although recent methods attempt to generate drafts within the target model itself, they often fail to fully exploit its latent parallel capacity due to a lack of structural coordination. In this paper, we propose \textbf{Prog...
  </details>

- **2026-07-12** — Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete et al. — [Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models](http://arxiv.org/abs/2607.10655v1)
  <details><summary>📄 Abstract</summary>
  Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We identify this failure mode as shortcut learning: the tendency to exploit predictive but non-causal correlations in the training distribution r...
  </details>

- **2026-07-12** — JungMin Yun, JuneHyoung Kwon, YoungBin Kim — [CRiT-QA: Evaluating Multi-hop Reasoning with Counterfactual Chains and Distractor Traps](http://arxiv.org/abs/2607.10562v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the multi-hop reasoning capabilities of large language models remains a significant challenge. Although current models achieve strong results on existing multi-hop question answering datasets, such performance often masks two critical vulnerabilities: (1) reliance on internal parametric knowledge rather than adherence to the provided context, and (2) exploitation of dataset shortcuts, such as single-document cues or type-matching, that diminish the need for genuine evidence aggregatio...
  </details>

- **2026-07-12** — Shengyuan Liu, Jia-Xuan Jiang, Boyun Zheng et al. — [Towards Autonomous and Auditable Medical Imaging Model Development](http://arxiv.org/abs/2607.10522v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are beginning to automate machine learning engineering (MLE) by coupling planning, code execution, debugging, and empirical feedback. Translating this capability to medical imaging remains difficult because each task imposes modality-specific experimentation and strict requirements for validation protocols and prediction artifacts. Here we introduce AMID, an autonomous multi-agent framework for medical imaging model development. AMID first proposes Data-Conditio...
  </details>

- **2026-07-11** — Kexin Huang, Junkang Wu, Jinda Lu et al. — [ARMOR: Stabilizing On-Policy LLM RL with Off-Policy Anchor Samples](http://arxiv.org/abs/2607.10481v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has significantly enhanced the reasoning capabilities of large language models (LLMs), yet the training process remains notoriously fragile. In this work, we investigate a critical source of this instability: over-optimization, where models exploit training heuristics at the expense of generalizable reasoning. While reverse KL regularization is the standard defense against such degradation, our analysis reveals that it is often insufficient in this regime, as it fails...
  </details>

- **2026-07-11** — Abhigya Verma, Khyati Mahajan, Amit Kumar Saha et al. — [SynthDocBench: Controlled Benchmark for Long-Context Visual Document Understanding](http://arxiv.org/abs/2607.10400v1)
  <details><summary>📄 Abstract</summary>
  Vision language models (VLMs) have achieved strong performance on visual document understanding benchmarks such as DocVQA, ChartQA, and MMLongBench-Doc. However, real-world documents combine multiple factors such as length, layout complexity, modality, and question difficulty, which makes it difficult to attribute model failures to specific causes. We introduce SynthDocBench, a fully synthetic benchmark for long-context visual document understanding that systematically controls factors including...
  </details>

- **2026-07-11** — Zhihui Sun — [SVD-RAG: Efficient Tree-Organized Retrieval-Augmented Generation via Singular Value Decomposition](http://arxiv.org/abs/2607.10316v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems enhance large language models by retrieving relevant documents from external knowledge bases. Recent work by Sarthi et al. (2024) introduced RAPTOR, which organizes documents into hierarchical tree structures for efficient retrieval, but requires expensive LLM-based abstractive summarization at each internal node -- making large-scale deployment prohibitively costly.   We present SVD-RAG, the first method to apply Singular Value Decomposition (SVD) on...
  </details>

- **2026-07-11** — Ziyu Lin, Ziting Wang, Xinfeng Li et al. — [Understanding Implicit Trust Errors in Core Carrier Networks through Multi-Agent Flaw Discovery and Analysis](http://arxiv.org/abs/2607.10315v1)
  <details><summary>📄 Abstract</summary>
  Cellular core networks (CNs) are critical infrastructure, yet their internal security model has historically relied on physical isolation: interfaces between core components often operate within an assumed trust zone. As CNs transition to cloud-native deployments, this assumption weakens, expanding the attack surface and enabling external adversaries to reach previously internal interfaces. From a root-cause analysis of security flaws reported in GitHub issues for opensource CN implementations, ...
  </details>

- **2026-07-11** — Kaiying Yan, Luoyi Sun, Xiao Zhou et al. — [Empowering Long-form Omni-modal Understanding with Robust Audio Perception](http://arxiv.org/abs/2607.10299v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large-scale multimodal models have drivenremarkable progress in vision-language tasks; however, comprehensiveomni-modal understanding remains under-explored, largely due to thescarcity of datasets with rich, explicitly aligned auditory cues. To bridgethis gap, we present AVDC (Audio-Visual Decoupled Captions), a large-scaledataset designed to disentangle visual and auditory semantics. Specifi-cally, we propose an automated pipeline that leverages off-the-shelf mod-els to annot...
  </details>

- **2026-07-09** — Shilin Ou, Yifan Xu, Luyao Zhang — [SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets](http://arxiv.org/abs/2607.08681v1)
  <details><summary>📄 Abstract</summary>
  As agentic AI systems are increasingly applied to cyber-physical environments, their evaluation requires assessment of both task performance and trustworthiness. In decentralized energy markets, autonomous agents may improve market utility, but may also exploit invalid physical data, create artificial liquidity, and produce unstable governance decisions. Therefore, we propose SolarChain-Eval, a physics-constrained benchmark for evaluating trustworthy economic agents. It formulates market governa...
  </details>

- **2026-07-09** — Seyyed Erfan Fatemi, Wafa Hedhly, Leila Musavian et al. — [Adaptive Wavelet Division Multiplexing for Heterogeneous Mobility Users](http://arxiv.org/abs/2607.08611v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an adaptive wavelet division multiplexing scheme for wireless systems serving users with heterogeneous mobility profiles over frequency-selective Rayleigh fading channels. By exploiting the multiresolution structure of the discrete wavelet transform (DWT), users are adaptively assigned to different decomposition levels according to their channel dynamics and Doppler conditions. A single-tap minimum mean square error (MMSE) equalizer is applied in the frequency domain, and the...
  </details>

- **2026-07-09** — Masatoshi Tateno, Alexandros Stergiou, Risa Shinoda et al. — [Do Egocentric Video-Language Models Capture Both Hand- and Object-Centric Cues?](http://arxiv.org/abs/2607.08514v1)
  <details><summary>📄 Abstract</summary>
  Hand-object interaction (HOI) recognition requires capturing both hand manipulations and object transformations. However, existing video-language models often fall into shortcuts by relying on spurious correlations among hands, objects, or environmental context, rather than reasoning from the appearance and dynamics of hands and objects themselves. To address this limitation, we propose a new learning paradigm that combines (i) hand-object masked training, which enables robust reasoning from par...
  </details>

- **2026-07-09** — Puji Wang, Yingchen Zhang, Ruqing Zhang et al. — [Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents](http://arxiv.org/abs/2607.08395v1)
  <details><summary>📄 Abstract</summary>
  Persistent AI agents extend large language models (LLMs) beyond single-turn interaction into long-lived software systems. Unlike traditional chat assistants, unsafe content in these agents can propagate through persistent state, reusable skills, and tool-mediated interactions, creating a substantially larger semantic attack surface. We observe that most security-critical interactions in such agents are transmitted through natural-language token flows, including memory updates, tool arguments, re...
  </details>

- **2026-07-09** — Matthias Weiß, Athreya Hosahalli Prakash, Maurice Artelt et al. — [Self-Adaptive Anomaly Detection with Reinforcement Learning and Human Feedback in Connected Vehicles](http://arxiv.org/abs/2607.08373v1)
  <details><summary>📄 Abstract</summary>
  Connected vehicles are autonomous cyber-physical systems whose behavior must be continuously monitored during operation to detect deviations from normal operation before they propagate into failures. Such evaluation is challenging because the systems themselves evolve: over-the-air updates, configuration changes, and shifting workloads alter the definition of normal behavior, causing static diagnostic methods to degrade silently over time. Existing approaches typically address either automated m...
  </details>

- **2026-07-09** — Anh Trac Duc Dinh, Khang Nhat Hoang Vo, Vinh Cong Doan et al. — [Echoes Across Vietnam's Highlands, Delta, and Coast: A Multilingual Corpus for Cham, Khmer, and Tay-Nung](http://arxiv.org/abs/2607.08362v1)
  <details><summary>📄 Abstract</summary>
  Vietnam's ethnic minority languages are almost absent from the field of Natural Language Processing (NLP), and the challenge goes beyond data scarcity: Cham, Khmer, and Tay-Nung differ sharply in script, Vietnamese contact, and standardization, conditions under which standard multilingual adaptation can learn the wrong signals. We introduce CKTN, the first corpus and benchmark for these languages (44,367 documents, 24M subword tokens), spanning continued pretraining, category classification, and...
  </details>

- **2026-07-09** — Lea Roxanne Muth, Marian Margraf — [From Legacy Documentation to OSCAL: An MCP-Based Agent Pipeline for Threat-Informed Continuous Compliance in Critical Infrastructure](http://arxiv.org/abs/2607.08288v1)
  <details><summary>📄 Abstract</summary>
  In critical infrastructure, operational technology environments often cannot be actively scanned, and yet active system feedback is needed for risk assessment and compliance. This paper presents a non-invasive, MCP-grounded multi-agent pipeline that converts natural-language system descriptions into source-verified knowledge graph and audit-ready artifacts in the NIST OSCAL format for continuous automated compliance management. The architecture decouples LLM-based reasoning from deterministic kn...
  </details>

- **2026-07-09** — Hou Hin Ip, Ka Nam Lam, Joshua Man Yu Ng et al. — [Enhancing the KidSat Model: Integrating Geographical Encoding and Data Quality Assessment for Childhood Poverty Prediction](http://arxiv.org/abs/2607.08281v1)
  <details><summary>📄 Abstract</summary>
  Accurate poverty mapping using satellite imagery is often hindered by (i) noisy and sparse survey-derived supervision, (ii) image quality issues such as cloud cover and image corruption, and (iii) lack of explicit spatial structure in image-only models. Building on the KidSat framework, we develop an enhanced pipeline that improves predictive accuracy via refined data preprocessing, systematic image quality assessment, and mathematically defined geographic encoding. First, we refine the fine-tun...
  </details>

- **2026-07-09** — Matthew W. Scroggs, Garth N. Wells — [Algorithm XXXX: Computation of finite element degree-of-freedom transformation matrices](http://arxiv.org/abs/2607.08172v1)
  <details><summary>📄 Abstract</summary>
  The arithmetic intensity of algorithms for computing finite element operators increases with increasing polynomial degree. This has made high degree methods particularly attractive on modern CPU and GPU architectures, since on these architectures performance at low degree is limited (severely) by the available memory bandwidth and only a very small fraction of the floating point capacity of the processor is used. Higher degree methods can exploit a significantly greater fraction of the available...
  </details>

- **2026-07-09** — Utkarsh A. Mishra, Yongxin Chen, Danfei Xu et al. — [Understanding and Mitigating the Video-Action Generalization Gap via Temporal Ratio](http://arxiv.org/abs/2607.08127v1)
  <details><summary>📄 Abstract</summary>
  Generative video foundation models exhibit strong compositional priors, yet world-action models (WAMs) and video-action models (VAMs) often lose these priors after finetuning on robotic action data. We refer to this discrepancy as the video-action generalization gap. In this paper, we systematically investigate this gap by evaluating a comprehensive design space of VAMs, demonstrating that standard design choices yield no emergent explanation pattern. To explain this behavior, we introduce the T...
  </details>

- **2026-07-09** — Lefu Cai, Hongjie Li, Xianchao Wang — [A Non-Decoupled Time-Domain Direct Sampling Method for Inverse Elastic Medium Scattering](http://arxiv.org/abs/2607.08067v1)
  <details><summary>📄 Abstract</summary>
  This work is concerned with an inverse medium problem for elastic waves, in which unknown inhomogeneities are reconstructed from time-resolved boundary measurements. We propose a novel time-domain direct sampling method for locating scatterers from a single incident source, without imposing specific assumptions on the temporal profile of the excitation. In particular, the imaging functional introduces a time-shifted correlation strategy that replaces the traditional $P$-$S$ wave decomposition wi...
  </details>

- **2026-07-09** — Youya Xu, Chengyong Yu, Sanjib Ghosh — [Robust Quantum Learning through Hamiltonian Reservoir Computing](http://arxiv.org/abs/2607.08037v1)
  <details><summary>📄 Abstract</summary>
  Quantum learning provides a versatile paradigm for information processing by exploiting the intrinsic representational capacity of high-dimensional Hilbert spaces. Here, we investigate a Hamiltonian-encoding framework for quantum reservoir computing that simultaneously addresses three key challenges in quantum learning: trainability, hardware efficiency, and information stability. In this framework, input data are directly mapped onto a fixed Hamiltonian and transformed into expressive nonlinear...
  </details>

- **2026-07-08** — Donghyun Lee, Yuhang Li, Ruokai Yin et al. — [KronQ: LLM Quantization via Kronecker-Factored Hessian](http://arxiv.org/abs/2607.07964v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) is a widely adopted technique for compressing large language models (LLMs) without retraining. Existing second-order PTQ methods, including GPTQ, construct quantization objectives exclusively from input activation statistics, effectively assuming that all output channels contribute equally to the layer-wise reconstruction objective. We propose KronQ, a PTQ framework that challenges this assumption by introducing the gradient covariance into the quantization pipel...
  </details>

- **2026-07-08** — J. Mark Bishop, Stephen J. Cowley — [How Do I Know What to Say Next? Barenholtz's Autogenerative Theory as an Enrichment of Harrisean Integrationism](http://arxiv.org/abs/2607.07891v1)
  <details><summary>📄 Abstract</summary>
  Roy Harris's Integrationist linguistics offers a compelling critique of the referentialist tradition embedded deep at the heart of computational approaches to language, arguing that language is not a code that maps onto a pre-given world but a situated, bipartite activity oriented toward prospective joint action. Yet Integrationism leaves certain explanatory gaps: it does not fully account for the structural mechanism by which signs sustain prospective openness, it undertheorises the continuity ...
  </details>

- **2026-07-08** — Felix Wang, Anudeep Das, Mei Nagappan et al. — [Functional and Secure Code Generation with Task Vectors](http://arxiv.org/abs/2607.07881v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for code generation, but they struggle to generate functional code free of security vulnerabilities. Prior work to improve the secure code generation abilities of such coding LLMs has largely focused on evaluating code functionality and security separately using different datasets, or focused on finding vulnerabilities post-generation. At the same time, the text-generation domain has seen significant work on alignment techniques, where models ar...
  </details>

- **2026-07-08** — Tingkai Liu, Muralidhar Andoorveedu, Sanjoy Das et al. — [CTA-Pipelining: A Latency-Oriented Spatial Scaling Method for Multi-GPU Systems](http://arxiv.org/abs/2607.07862v1)
  <details><summary>📄 Abstract</summary>
  The evolution of compute infrastructure has transformed multi-GPU systems into tightly integrated shared-memory structures. However, current software still mostly treats these coherent interconnects simply as high-speed networks. Simultaneously, the demand for serving Large Language Models under latency constraints has shifted GPU workload optimization from being throughput-driven to latency-bound, necessitating latency-oriented scaling methods beyond Tensor Parallelism (TP).   Thus, we introduc...
  </details>

- **2026-07-08** — Mihnea C. Moldoveanu, Joel A. C. Baum — [Adversarial Social Epistemology for Assemblies of Humans and Large Language Models](http://arxiv.org/abs/2607.07760v1)
  <details><summary>📄 Abstract</summary>
  We outline an adversarial social epistemology (ASE) for densely interactive communicative landscapes in which public assertions are scaffolded by chains of testimony, inference, institutional certification, and tacit trust. In such landscapes, agents have incentives and affordances to distort, color, omit, fabricate, or strategically under-specify information for private, reputational, rhetorical, or material gains. We argue that these phenomena are not adequately captured by familiar descriptio...
  </details>

- **2026-07-08** — Yingyun Cui, Yi Xie, Piaohong Wang et al. — [PERFOPT-Bench: Evaluating Coding Agents on Software Performance Optimization](http://arxiv.org/abs/2607.07744v1)
  <details><summary>📄 Abstract</summary>
  Coding-agent benchmarks have largely measured whether agents can produce functionally correct patches, but production software also demands measurable speedups on real execution targets. Performance optimization is a distinct agentic task: agents must profile executions, diagnose cross-layer bottlenecks, edit code without breaking correctness, and verify that gains are reproducible rather than measurement artifacts. We introduce PERFOPT-Bench, a benchmark for evaluating this full performance-eng...
  </details>

- **2026-07-08** — Qiaoni Shi, Kai Zhu, Kai Gu — [Answering Without Referring: How AI Search Rewrites the Web's Economic Bargain](http://arxiv.org/abs/2607.07652v1)
  <details><summary>📄 Abstract</summary>
  Search engines have long allocated attention on the web by routing users from queries to websites. AI search changes this arrangement because information needs can be resolved inside the intermediary. Using URL-level Comscore U.S. desktop clickstream, we compare ChatGPT and Google information-seeking occasions and exploit ChatGPT Search access expansions to estimate traditional search displacement. ChatGPT produces outbound clicks in only 5.2% of conversation sessions, far below Google's referra...
  </details>

- **2026-07-08** — Ana Schwengber Kelm, Christian Bockermann, Jörg Frochte — [Multi-Class vs. Multi-Label BERT for CVE-to-CWE Mapping: How Taxonomy Structure Shapes the Errors](http://arxiv.org/abs/2607.07573v1)
  <details><summary>📄 Abstract</summary>
  Assigning Common Weakness Enumeration (CWE) categories to Common Vulnerabilities and Exposures (CVE) records remains an important but largely manual step in vulnerability analysis. We study this task as a text classification problem and compare two modelling choices: a \emph{multi-class} formulation that predicts a single CWE per CVE and a \emph{multi-label} formulation that allows multiple assignments. Three transformer encoders (BERT Base, SecureBERT, and CySecBERT) are evaluated on three nest...
  </details>

- **2026-07-08** — Jaris Küken, Shi Bin Hoo, Martin Mráz et al. — [TimEE: End-to-end Time Series Classification via In-Context Learning](http://arxiv.org/abs/2607.07500v1)
  <details><summary>📄 Abstract</summary>
  Time series classification (TSC) is dominated by a two-stage paradigm: train a feature encoder -- either from scratch on the target dataset or via pretraining on large corpora -- and then fit a task-specific classifier on top. While effective, this decoupling optimizes representation learning independently of the classification objective, requires per-dataset training, and prevents the model from exploiting label information during inference. We introduce TimEE, a 4.5M-parameter foundation model...
  </details>

- **2026-07-08** — Florian Fuchs, Jessy Gosselin-Grant, Boris Skuin et al. — [Reward-Adaptive Iterative Discovery: A Case Study on Automated Game Testing for NHL26](http://arxiv.org/abs/2607.07498v1)
  <details><summary>📄 Abstract</summary>
  Testing is a major effort for the gaming industry, requiring a significant part of development budget and people power. We present a case study on a development version of the ice hockey game EA SPORTS NHL 26, for which human playtesters test the goalie AI for behavioral exploits. To reduce the effort of re-testing the goalie AI after every game or behavior modification in the development phase, we propose Reward-Adaptive Iterative Discovery (RAID), a novel approach to automatically find exploit...
  </details>

- **2026-07-08** — Yang Shi, Jiaheng Fu, Yihe Huang et al. — [Mitigating Taint-Style Vulnerabilities in MCP Servers via Security-Aware Tool Descriptions](http://arxiv.org/abs/2607.07461v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as autonomous agents that interact with external tools and services via the Model Context Protocol (MCP), a standardized interface for dynamic tool invocation. While MCP simplifies integration, it also expands the attack surface and enables generic exploits across multiple servers. Despite prior work on malicious MCP servers, the vulnerability landscape of MCP servers remains underexplored. In this work, we systematically analyze MCP server ...
  </details>

- **2026-07-08** — Chethan Krishnamurthy Ramanaik, Tobias Callies, Michael Hecht et al. — [On Adversarial Vulnerability of Vision-Language Models through the Lens of Intermediate Spectral Subspaces](http://arxiv.org/abs/2607.07375v1)
  <details><summary>📄 Abstract</summary>
  Adversarial vulnerability in deep neural networks (DNNs) has been studied from the perspectives of decision-boundary geometry, feature robustness, input-output Jacobians, and the instability of inverse problems. Here, we focus on the spectral structure of intermediate linear transformations that propagate information through modern DNNs, an unexplored mechanism of adversarial vulnerability. Specifically, we investigate transformer-based vision-language models, whose linear layers admit interpret...
  </details>

- **2026-07-08** — Xin Li, Jiaju Han, Ma Yaqi et al. — [InfraQR: Edge-Placed QR-Inspired Structured Patch Attacks on Infrared Vision-Language Models](http://arxiv.org/abs/2607.07288v1)
  <details><summary>📄 Abstract</summary>
  Infrared vision-language models are increasingly used for perception under low-light and adverse visual conditions, yet their robustness to localized structured perturbations remains underexplored. Existing infrared adversarial studies mainly focus on object detectors, leaving the security of infrared vision-language models less systematically examined. We present InfraQR, a QR-inspired structured patch attack for infrared vision-language models. Unlike localized attacks that attach perturbation...
  </details>

- **2026-07-08** — Antonio Cabrales, Wenhao Cheng — [Evaluation and Assignment with Networked Competition and Spillovers](http://arxiv.org/abs/2607.07280v1)
  <details><summary>📄 Abstract</summary>
  This paper studies how organizations should jointly design evaluation rules and assign workers when performance depends on both effort and non-discretionary advantage. Agents choose effort in positions linked by a competition network, while their effective advantage depends on own type and spillovers through a second network. The planner chooses both the assignment and the effort weight in evaluation. Equilibrium effort rises with a position's Katz-Bonacich centrality and falls with effective ad...
  </details>

- **2026-07-08** — Miguel Lopez-Duran, Elena Marrero, Julian Fierrez et al. — [Comparative Study of Domain-adapted VLMs for General Document Visual Question Answering](http://arxiv.org/abs/2607.07179v1)
  <details><summary>📄 Abstract</summary>
  Document Visual Question Answering (DocVQA) presents a complex multimodal challenge, requiring models to exploit visual, textual, and layout information from documents. Although Vision-Language Models (VLMs) have shown remarkable performance in text-vision tasks, their robustness and transferability to different document domains remains underexplored. In this study, we present a comprehensive evaluation of 8 open-source pretrained VLMs on DocVQA in three different document domains: industrial do...
  </details>

- **2026-07-08** — Zetian Hu, Shunyu Liu, Junjie Zhang et al. — [Entropy Pacing Policy Optimization for Multi-Task Agentic Reinforcement Learning](http://arxiv.org/abs/2607.07178v1)
  <details><summary>📄 Abstract</summary>
  Recent breakthroughs of Reinforcement Learning (RL) have highlighted its potential for complex agentic Large Language Model (LLM) tasks. However, existing efforts largely focus on single-task settings, whereas real-world deployment necessitates a generalist agent capable of solving multiple tasks simultaneously. In this work, we identify a critical yet underexplored phenomenon in multi-task agentic RL: different tasks can exhibit exploration-exploitation pace mismatch. Specifically, easier tasks...
  </details>

- **2026-07-08** — Yao Sheng, Yu Yokoi — [Stable Matchings with Minimum Utility Gap](http://arxiv.org/abs/2607.07160v1)
  <details><summary>📄 Abstract</summary>
  We introduce the Stable Matching Problem with Minimum Utility Gap, which seeks a stable matching in which the utilities received by individual agents are as balanced as possible. Our framework can handle many-to-many matchings and general utility functions on partner sets that are consistent with the agents' preferences. We consider two measures for comparing agents' utilities: the difference between the maximum and minimum utilities, and their ratio.   We provide a polynomial-time algorithm for...
  </details>

- **2026-07-08** — Víctor Mayoral-Vilches — [Certifying Ghosts: How Cybersecurity AI Agents Break the EU Cyber Resilience Act](http://arxiv.org/abs/2607.07109v1)
  <details><summary>📄 Abstract</summary>
  The EU Cyber Resilience Act (CRA) makes a smart bet. It does not demand that products be free of vulnerabilities, but only that manufacturers run a process: assess risk, handle flaws, ship updates. The bet pays off if four things about the world stay true: (P1) finding vulnerabilities is slow, skilled, human work; (P2) a product's exploitable flaws are knowable the day it ships; (P3) exploitation is rare enough to notice; and (P4) fixes keep pace with discovery. Cybersecurity AI (CAI) agents, AI...
  </details>

- **2026-07-08** — Junjie Wu, Lingjian Zhou, Zerui Shao et al. — [EvoOMG: An Evolution-Oriented Multi-Agent Guidance Framework for Heterogeneous Legacy-and-MLO Wi-Fi Networks](http://arxiv.org/abs/2607.07045v1)
  <details><summary>📄 Abstract</summary>
  The gradual deployment of Wi-Fi 7/8 multi-link operation (MLO) will lead to long-term coexistence between legacy non-MLO stations (STAs) and MLO-capable STAs in WLANs. This mixed deployment makes throughput optimization challenging because legacy STAs follow single-link contention and transmission, whereas MLO-capable STAs can exploit multiple links with richer access opportunities. Existing learning-based methods usually treat such networks as homogeneous systems and directly map the current ob...
  </details>

- **2026-07-08** — Dennis Gross, Quentin Mazouni, Helge Spieker et al. — [Gimitest: A Comprehensive Tool for Testing Reinforcement Learning Policies](http://arxiv.org/abs/2607.07029v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) policies can be unsafe and vulnerable to attacks. Ensuring their reliability is often a pain point as existing automated testing methods target only selected environments, testing scenarios, and RL algorithms. To address this, we propose a comprehensive framework for testing single- and multi-agent RL policies under varying conditions. Our implementation of this framework, Gimitest, is an open-source tool that supports various gym frameworks and allows for modificatio...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 50 papers

- **2026-07-13** — Yixuan Xiao, Cheng-Wei Lin, Xin Wang et al. — [Evidence Subspace Projection: Measuring How Much Evidence Explains Deepfake Detection in Self-Supervised Speech Models](http://arxiv.org/abs/2607.11538v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning (SSL) models are widely used as feature extractors for state-of-the-art audio deepfake detection, but it remains unclear how to directly and quantitatively connect what SSL models capture to detection decisions. To address this gap, we propose Evidence Subspace Projection, a method that represents both evidence factors (e.g., attack category, codec, gender, transmission) and authenticity labels in a shared space constructed from SSL models' neuron activation patterns. By...
  </details>

- **2026-07-13** — Ahmed M. Elmisery — [Graph-Based Structural Evaluation of LLM-Translated Adversary Emulation Procedures](http://arxiv.org/abs/2607.11517v1)
  <details><summary>📄 Abstract</summary>
  Adversary emulation plans describe multi-step attacker procedures using MITRE ATT&CK techniques, privilege requirements, and observable telemetry. Translating them across operating systems supports cross-platform defender evaluation, and large language models (LLMs) can automate this task. However, a translation may only rename tools while retaining source-platform logic, giving defenders little target-platform coverage. Binary scoring can overestimate fidelity because it measures countable feat...
  </details>

- **2026-07-13** — Ananya Acharya, Trenton Goyette, Masoud Ataei et al. — [Capture, Shield, or Neutralize: Engagement-Aware Pursuit-Evasion](http://arxiv.org/abs/2607.10986v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a hierarchical control architecture for multi-agent adversarial environments, decoupling strategic task planning from rigorous safety assurance. The system formulates pursuit-evasion as a zero-sum receding-horizon game, solved via an iterative minimax \acl{mpc} scheme. This allows pursuers to anticipate and block evader trajectories using transverse velocity penalties rather than relying on reactive heuristic formations. To guarantee collision-free operation without comprom...
  </details>

- **2026-07-13** — Markos Markakis, Tim Kraska — [AutoSLO: Practical Latency SLOs on Cloud Data Warehouses -- Extended Version](http://arxiv.org/abs/2607.11770v1)
  <details><summary>📄 Abstract</summary>
  Modern cloud data warehouses decouple compute from storage, making it easy for organizations to access the same underlying data with multiple compute clusters. This flexibility is often used for performance isolation among diverse workloads, so that each workload meets its latency service-level objective (SLO) more reliably. For example, interactive dashboards, ad hoc analysis, and batch jobs can each run on separate clusters. However, this dedicated-cluster approach requires each compute cluste...
  </details>

- **2026-07-13** — Yilong Yang, Jianxin Tian, Shengchuan Zhang et al. — [GFR-SAM: Training-Free Referring Camouflaged Object Segmentation via Cross-Image Prompting](http://arxiv.org/abs/2607.11732v1)
  <details><summary>📄 Abstract</summary>
  Referring Camouflaged Object Detection (Ref-COD) requires segmenting hidden targets guided by reference cues. While supervised methods are annotation-heavy and training-free approaches via sparse point-prompting are sensitive to localization errors, we propose GFR-SAM, a robust three-stage training-free framework. GFR-SAM shifts the paradigm from fragile point-matching to a "Generate-Filter-Refine" pipeline. First, we introduce In-Context Exemplar-guided Segmentation, empowering SAM3 with cross-...
  </details>

- **2026-07-13** — Huan Zhu — [Think Through a Bottleneck: Hourglass Reasoning for Rigorous Induction](http://arxiv.org/abs/2607.11696v1)
  <details><summary>📄 Abstract</summary>
  Self-refinement often fails to strengthen few-shot inductive reasoning in large language models. Prompting a model to explicitly state its inferred rule does little on its own. What actually matters is a structurally enforced isolation between reasoning stages, so that information can only pass between them as a compressed symbolic state.   We introduce \textbf{Hourglass reasoning}, which enforces strict context isolation between reasoning stages. The frozen LLM acts as a meta-constructor, build...
  </details>

- **2026-07-13** — Hari Prasad — [Auditing the Risk Claims of Distributional Reinforcement Learning](http://arxiv.org/abs/2607.11607v1)
  <details><summary>📄 Abstract</summary>
  Distributional reinforcement learning agents learn full return distributions that are increasingly read at face value: for interpretability, risk-sensitive control, and safety monitoring. We ask a question theory anticipates but that has not been measured directly: are the risk claims of a trained distributional agent true? Our audit combines a decision-relevant screening metric (the excess Wasserstein gap between the top two actions, which equals the mass by which first-order stochastic dominan...
  </details>

- **2026-07-13** — Yuliang Liu, Zhang Li, Ziyang Zhang et al. — [MonkeyOCRv2: A Visual-Text Foundation Model for Document AI](http://arxiv.org/abs/2607.11562v1)
  <details><summary>📄 Abstract</summary>
  Mainstream visual encoders are pretrained on natural images and cannot be effectively applied to document images without document-oriented adaptation, as dense text and fine-grained character strokes demand character-level visual perception. We present MonkeyOCRv2, a visual-text pretrained model for document AI. First, we construct MonkeyDoc v2, to our knowledge the largest document-image pretraining corpus, comprising 113 million images spanning 17 languages. Second, we propose a pretraining st...
  </details>

- **2026-07-13** — Sridhar Mahadevan — [Agentic Skill Optimization over Lie Algebroids](http://arxiv.org/abs/2607.11493v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems increasingly improve themselves by editing skills: prompts, rubrics, plans, tool contracts, examples, validators, and traces. Skill edits are not independent coordinates in a vector space: they are local repairs to structured artifacts whose effects are observed only after rollout, validation, and critique. Distinct edits can have the same immediate visible effect while differing in routing context, template state, guardrail scope, or future composability. The order of edits can ...
  </details>

- **2026-07-13** — Tengjiao Liu — [Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory](http://arxiv.org/abs/2607.11226v1)
  <details><summary>📄 Abstract</summary>
  LLM agents today are caught in an awkward bind. Lock them down with static safety instructions and they rarely venture beyond the obvious; give them free reign with tools and multi-agent debate, and safety violations quickly follow. Rather than forcing a single model to juggle both creativity and caution, we separate the concerns across specialized roles. A Disrupter generates unconventional proposals, a Validator enforces hard runtime checks at the tool gateway, and a Broker pulls in distant bu...
  </details>

- **2026-07-13** — Prashant Devadiga,  Abhishek, Adithya Mishra et al. — [A Formal Hierarchical Architecture for Agentic Orchestration with Stack-Based Execution and Lazy Discovery](http://arxiv.org/abs/2607.11138v1)
  <details><summary>📄 Abstract</summary>
  The rapid expansion of capabilities in Large Language Model (LLM) agents has exposed a critical architectural bottleneck: when agents are given access to a flat, monolithic registry of tools, the model must evaluate hundreds or thousands of options simultaneously. This leads to decision-space explosion, context window saturation, and degraded routing accuracy. To address these limitations, this paper presents a hierarchical, skill-based architecture for agentic orchestration. Capabilities are or...
  </details>

- **2026-07-13** — Sara Yakoubi, Ikram Khalfallah, Kenza Khelkhal et al. — [FAD-SA-GRU: Enhancing Hate Speech Detection in Algerian Dialect Through Feature-Augmented Self-Attention GRU Networks](http://arxiv.org/abs/2607.11279v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of social media platforms has transformed online communication by enabling users to exchange information and opinions instantly. However, these platforms have also facilitated the dissemination of abusive and hateful content, posing major social, psychological, and ethical challenges. Hate speech can incite discrimination, harassment, and violence against individuals or communities based on attributes such as ethnicity, religion, gender, nationality, or political affiliat...
  </details>

- **2026-07-13** — Kaixin Ma, Di Feng, Alexander Metz et al. — [MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents](http://arxiv.org/abs/2607.11818v1)
  <details><summary>📄 Abstract</summary>
  We introduce MM-ToolSandBox, a benchmark and evaluation framework for visually grounded tool-calling agents. The framework provides a stateful execution environment spanning 500+ tools across 16 application domains, supporting multi-image, multi-turn tasks where agents must ground progressively arriving visual inputs into executable tool calls while handling realistic conversational phenomena (goal revisions, error corrections, state mutations). An automated scenario generation pipeline produces...
  </details>

- **2026-07-13** — Yi Tang Soon, Jun-Wei Hsieh — [Confidence Scores in Open-Vocabulary Detection Are a Biased Mixture of Scale and Semantics](http://arxiv.org/abs/2607.10993v1)
  <details><summary>📄 Abstract</summary>
  Foundation models such as CLIP have enabled open-vocabulary object detectors that generalise to novel categories via vision-language similarity. However, the confidence scores these detectors produce are not reliable localization probability estimates: they conflate visual scale and semantic query specificity with the true detection signal. Through controlled experiments on COCO across three foundation-model-based detectors (GroundingDINO, OWL-ViT, YOLO-World), with the scale-bias finding furthe...
  </details>

- **2026-07-12** — Yuan Gao, Jiangyi Yang, Yao Zhao et al. — [Auditing Belief-Conditioned LLM Agents in Hidden-Information Social Deduction Games](http://arxiv.org/abs/2607.10814v1)
  <details><summary>📄 Abstract</summary>
  Evaluating LLM agents in hidden-information multi-agent settings is hard: final outcomes are high-variance and rarely reveal why an agent decided as it did. We study this in a 9-player Werewolf environment where agents act under strict, code-level information isolation, and we build an auditable framework that maintains an external belief state over hidden roles, logs belief updates and belief-action deviations as structured evidence, and supports a defensive offline improvement loop that review...
  </details>

- **2026-07-12** — Lin Zhang — [LLM-Enhanced Dynamic Financial Knowledge Graphs for Cross-Entity Signal Propagation and alpha discovery](http://arxiv.org/abs/2607.10932v1)
  <details><summary>📄 Abstract</summary>
  Financial information rarely affects a single company in isolation. Earnings surprises, capital expenditure changes, supply constraints, and guidance revisions can propagate through networks of suppliers, customers, competitors, and technology ecosystems. Traditional financial NLP primarily measures document-level sentiment for the directly mentioned company and often ignores cross-entity information diffusion.   This paper develops an LLM-based financial measurement and signal propagation frame...
  </details>

- **2026-07-12** — Keqin Peng, Chen Li, Yuanxin Ouyang et al. — [Diagnosing and Mitigating Thinking Collapse in On-Policy Self-Distillation](http://arxiv.org/abs/2607.10805v1)
  <details><summary>📄 Abstract</summary>
  On-Policy Self-Distillation (OPSD) has emerged as a crucial paradigm for enhancing and aligning Large Language Models (LLMs). However, in complex reasoning tasks, OPSD paradoxically degrades downstream performance. In this paper, we systematically investigate this pathology and identify a severe optimization trap we define as \textbf{Thinking Collapse} -- a sharp decline in the model's native intermediate reasoning behavior, measured by epistemic-token density (ET per 1k). Through entropy-based ...
  </details>

- **2026-07-12** — Dylan Xinming Hou, Juntian Zhang, Xu Gu et al. — [Detecting AI-Generated Video: A Vision-Language Dual-View Survey](http://arxiv.org/abs/2607.10787v1)
  <details><summary>📄 Abstract</summary>
  The evolving realism of AI-generated Videos (AIGC-V) is rapidly rendering traditional artifact-centric detection insufficient, necessitating a paradigm shift from low-level inspection to high-level semantic verification. This paper presents a comprehensive survey of AIGC-V detection, reframing the task as Factual Fidelity Verification, which asks whether the events, entities, and physical processes depicted in a video are consistent with real-world facts. To systematize this rapidly evolving fie...
  </details>

- **2026-07-12** — Sriram Selvam, Anneswa Ghosh — [Eval-Pair Matrix: Answer-Paired Meta-Evaluation of LLM Judges for Grounded RAG](http://arxiv.org/abs/2607.10626v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-judge evaluation is widely used for retrieval-augmented generation (RAG), but reusing the same model family as both generator and judge makes self-leniency difficult to identify. We introduce Eval-Pair Matrix, a controlled meta evaluation protocol for source-grounded RAG. Starting from GaRAGe questions and grounding passages, we induce one hidden answer-causal contradiction per record, generate answers from perturbed passages with GPT, Grok, and Gemini models, and then use the same mode...
  </details>

- **2026-07-12** — Zheng Pei, Mingwei Liu, Zhenxi Chen et al. — [WebDesignIter: Co-Evolving Design Knowledge for Repository-Level Front-End Code Generation](http://arxiv.org/abs/2607.10621v1)
  <details><summary>📄 Abstract</summary>
  Front-end development accumulates change after change at the repository level, weaving complex cross-file dependencies that current LLM coding agents tuned for single-shot tasks cannot reliably track across multiple iterations, leading to functional regressions and code that resists maintenance. We argue the missing piece is design knowledge: architectural principles, module responsibilities, and structural constraints that developers lean on to keep code readable, maintainable, and evolvable as...
  </details>

- **2026-07-11** — Igor Santos-Grueiro — [Temporary Authority, Permanent Effects: Commit-Time Authorization for LLM Agents](http://arxiv.org/abs/2607.10487v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can commit durable effects from authority evidence that was valid earlier in execution: a DOM snapshot, approval epoch, version witness, branch token, or worker result. We study the commit boundary at which earlier authority evidence no longer authorizes a durable effect. We call this property commit-time authorization: a durable effect is authorized only if the witness that licensed its derived state remains fresh, causally prior, bound to the same effect, and eligible at commit time...
  </details>

- **2026-07-11** — Basel Abdeen, S M Tahmid Siddiqui, Meah Tahmeed Ahmed et al. — [Hallucination Detection in Large Language Models Using Diversion Decoding](http://arxiv.org/abs/2607.10476v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have emerged as a powerful tool for retrieving knowledge through seamless, human-like interactions. Despite their advanced text generation capabilities, LLMs exhibit hallucination tendencies, where they generate factually incorrect statements and fabricate knowledge, undermining their reliability and trustworthiness. Multiple studies have explored methods to evaluate LLM uncertainty and detect hallucinations. However, existing approaches are often probabilistic and c...
  </details>

- **2026-07-11** — Istiaq Ahmed Fahad, Kamruzzaman Asif, Md. Nurul Ahad Tawhid — [Mitigating LLM Sycophancy in Code Smell Detection Using Evidence-Guided Reasoning Prompts](http://arxiv.org/abs/2607.10411v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used for code smell detection tasks due to their ability to interpret program semantics. However, their reliability in this context remains poorly explored, particularly under varying prompt conditions where model predictions may be influenced by external cues rather than code characteristics. One such limitation is sycophancy bias, where models tend to align their outputs with user-provided assumptions instead of performing objective analysis. In th...
  </details>

- **2026-07-11** — Fabian Lukassen, Christoph Weisser, Thomas Kneib et al. — [CAFE: A Compound-AI Factorial Evaluation Framework](http://arxiv.org/abs/2607.10380v1)
  <details><summary>📄 Abstract</summary>
  We introduce CAFE (Compound-AI Factorial Evaluation), an open-source platform that brings design of experiments to the evaluation of compound AI systems (CAIS). Such systems expose many interchangeable choices - e.g. which retriever, model, or prompt - and practitioners rarely know which of them most affects answer quality. With CAFE, a practitioner registers each swappable component of a pipeline as a factor to build a factorial design over the chosen factors, run the resulting configurations, ...
  </details>

- **2026-07-11** — Jiakang Yu, Yixuan Chai, Tianci Wang et al. — [ChartSync: A Benchmark for Visuo-Logical Cascading Chart Editing](http://arxiv.org/abs/2607.10301v1)
  <details><summary>📄 Abstract</summary>
  Generative image editing models struggle with structured statistical charts when data modifications require geometric synchronization. We formalize this task as Visuo-Logical Cascading Editing (VLCE). However, existing methods remain confined to localized text substitutions and struggle with dependency-aware cascading updates. To systematically evaluate this capability, we introduce ChartSync, an expert-validated benchmark constructed via a programmatic rendering pipeline that guarantees determi...
  </details>

- **2026-07-11** — Evropi Toulkeridou, Jiafei Li, Leonardo Lari et al. — [The evolution of AI from image interpretation toward scientific inference in nanoparticle electron microscopy](http://arxiv.org/abs/2607.10388v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) is transforming electron microscopy by enabling quantitative analysis of increasingly large and complex datasets for nanoparticle characterization. Recent advances in machine learning (ML) and deep learning (DL) have expanded microscopy from a descriptive imaging technique into a data-driven platform for structural interpretation, dynamic analysis, and scientific inference. This review examines AI methodologies for nanoparticle electron microscopy, focusing on transm...
  </details>

- **2026-07-11** — Hongliang Luo, Chuanbin Zhao, Boxuan Sun et al. — [Networked ISAC Enabled Target Recognition Towards Low-Altitude Economy](http://arxiv.org/abs/2607.10319v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose a low-altitude target (LAT) recognition scheme based on multi-base station (BS) collaboration and multi-scale feature fusion for integrated sensing and communications (ISAC) network. Firstly, we formulate the motion equations, echo channels, and echo signals for unmanned aerial vehicle (UAV), bird, vehicle, and pedestrian under multi-BS collaborative monitoring scenario. Then we extract the velocityresolution-preferred time-frequency spectrum, time-resolutionpreferred t...
  </details>

- **2026-07-09** — Amirhossein Taherpour, Xiaodong Wang — [Secure Decentralized Federated Learning via Gossip and Virtual Voting](http://arxiv.org/abs/2607.08651v1)
  <details><summary>📄 Abstract</summary>
  Decentralized federated learning (DFL) removes the central server by letting nodes exchange model updates through peer-to-peer gossip, but existing gossip-based methods often lack provenance finality and resilience to Byzantine or lazy participants. Ledger-assisted federated learning (FL) improves auditability, yet blockchains, shards, or settlement committees can reintroduce global coordination costs that conflict with DFL locality. This paper proposes \emph{gspDAG-FL}, a secure DFL framework t...
  </details>

- **2026-07-09** — Zheng Gao, Xiaoyu Li, Xiaoyan Feng et al. — [TRACE: A Two-Channel Robust Attribution Watermark via Complementary Embeddings for LLM-Agent Trajectories](http://arxiv.org/abs/2607.08400v1)
  <details><summary>📄 Abstract</summary>
  LLM agents reach users through resellers, who may rebrand a developer's agent or substitute a cheaper model. When provenance is disputed, attribution rests on the trajectory log (the record of tool calls, observations, and executed actions, not the model's reasoning), which the reseller stores and processes to meter usage. A watermark must therefore survive an adversary with full read/write access to the very evidence it is detected from; existing agent watermarks do not, as their attribution is...
  </details>

- **2026-07-09** — Zhekai Chen, Chengqi Duan, Kaiyue Sun et al. — [UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks](http://arxiv.org/abs/2607.08768v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of large language models and multimodal large language models has accelerated the emergence of proactive agents capable of operating everyday tools and assisting users in real-world environments. However, existing benchmarks struggle to evaluate such agents effectively, as they often rely on sandboxed environments and single-turn evaluation paradigms. Moreover, their scenario-based task taxonomies mix multiple model capabilities within the same task category, making it diff...
  </details>

- **2026-07-09** — Shreyas Subramanian, Adewale Akinfaderin, Akarsha Sehwag — [Super Weights in LLMs and the Failure of Selective Training](http://arxiv.org/abs/2607.08733v1)
  <details><summary>📄 Abstract</summary>
  Recent work identified Super Weights, individual parameters whose removal degrades model performance by orders of magnitude. We show that this degradation due to pruning Super Weights does not universally apply to all LLMs. Furthermore, if these parameters are so important, Super Weight-aware training should be effective. We show the opposite. Training Super Weights in isolation (100 to 8,192 parameters) drops accuracy to random-guessing levels on both OLMo-1B and OLMo-7B, and expanding to local...
  </details>

- **2026-07-09** — Xuefei Wang — [Out of Sight: Compression-Aware Content Protection against Agentic Crawlers](http://arxiv.org/abs/2607.08180v1)
  <details><summary>📄 Abstract</summary>
  The rise of LLM-based agents with reasoning, summarization, and memory capabilities has created a new threat surface for online content that conventional defenses fail to address. Existing defenses like access controls can be circumvented by agents mimicking ordinary browsers, and injection-based defenses often degrade human readability. In this paper, we revisit the agent pipeline and identify context compression, which agents routinely invoke to fit context budgets, as a critical yet overlooke...
  </details>

- **2026-07-09** — Hao Wu, RongQi Han, Zhen Wang et al. — [Diarization-Guided Qwen-ASR Adaptation for Multilingual Two-Speaker Conversational Speech](http://arxiv.org/abs/2607.08208v1)
  <details><summary>📄 Abstract</summary>
  This paper describes our self-designed system for Task 1 of the MLC-SLM 2026 Challenge for multilingual two-speaker conversational speech. The system combines a modular speaker diarization front end with a challenge-adapted Qwen3-ASR-1.7B recognizer. The diarization front end performs voice activity detection, subsegment generation, CAMPPlus speaker embedding extraction, two-speaker spectral clustering, and RTTM-based audio segmentation. The resulting speaker-attributed segments are grouped by l...
  </details>

- **2026-07-09** — Mingyu Zhao, Zhaohan Li, Zhenxiong Miao et al. — [PIT-SUN: A Deployable Empirical Marginal Transform Framework with Expectation-Consistent Recovery for Regression in Recommender Systems](http://arxiv.org/abs/2607.08202v1)
  <details><summary>📄 Abstract</summary>
  Estimating original-space conditional expectations is central to value-driven recommender systems, including dwell time, GMV, and LTV forecasting. Standard MSE is expectation-consistent in principle, but its gradients become unstable on heavy-tailed, zero-inflated, and multimodal targets, causing mean collapse and tail shrinkage. Target transformation alleviates this scale conflict, yet any useful nonlinear marginal transform loses expectation consistency under direct inversion. This is not an i...
  </details>

- **2026-07-09** — Mingyu Dou, Shi Qiu, Ming Hu et al. — [UAV-OVVIS: Unmanned Aerial Vehicles Also Need Open-Vocabulary Video Instance Segmentation](http://arxiv.org/abs/2607.08075v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicle (UAV) videos are widely used in traffic monitoring, urban management, and emergency rescue. However, existing UAV video perception mainly relies on box-level localization and trajectory association under predefined categories, making it difficult to simultaneously support flexible queries and fine-grained instance-level dynamic understanding in open scenarios. To this end, we introduce a new task, UAV Open-Vocabulary Video Instance Segmentation (UAV-OVVIS), which discover...
  </details>

- **2026-07-09** — Argyro Sasli, Maojie Xu, Alexandra Junell et al. — [Catching Disguised Transients with ASTRANet: Anomaly-Aware Spectroscopic Classification and Conformal Calibration](http://arxiv.org/abs/2607.08044v1)
  <details><summary>📄 Abstract</summary>
  Time-domain surveys discover thousands of transients per year, but the spectroscopic identification of rare and physically peculiar objects remains rate-limited by closed-set classifiers that confidently assign every input to a known class -- including spectra that genuinely belong to no known class. We present the \texttt{ASTRANet} framework, a confidence-aware infrastructure for spectroscopic transient classification built around three coupled modules: a hierarchical spectral classifier that o...
  </details>

- **2026-07-09** — Trong-Thuan Nguyen, Minh-Triet Tran — [LOGOS: Language-guided Oriented Object Detection in Aerial Scenes](http://arxiv.org/abs/2607.08004v1)
  <details><summary>📄 Abstract</summary>
  Object detection in geospatial scenes, such as satellite and aerial imagery, poses significant challenges due to the varying orientations and densities of objects, as well as the complex backgrounds inherent to remote sensing imagery. Traditional methods for oriented object detection have struggled to address issues such as angular discontinuity, fixed query sizes, and inefficiencies in handling sparse or cluttered scenes. In this paper, we propose LOGOS, a novel transformer-based approach that ...
  </details>

- **2026-07-08** — Shane Caldwell, Max Harley, Ads Dawson et al. — [ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents](http://arxiv.org/abs/2607.07774v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents take on offensive security work, a single out-of-scope tool call can breach a client's engagement boundary, disrupt production, or void a bug-bounty finding. Unlike a fixed safety policy, the boundary that matters is declared in the user's request and must be inferred from intent. That challenge is sharpened by the adversarial nature of offensive security: the same tool call is in or out of scope depending not on the action itself but on the target it touches and the context in whi...
  </details>

- **2026-07-08** — Dongyang Kuang, Zizheng Ma, Yushan Zhang et al. — [Graph-Regularized Deep Learning for EEG-Based Emotion Recognition with Psychologically-Grounded Label Structure](http://arxiv.org/abs/2607.07773v1)
  <details><summary>📄 Abstract</summary>
  EEG-based emotion recognition is critical for mental health monitoring and affective brain-computer interfaces, yet existing deep learning approaches often treat emotion classes as isolated labels, ignoring their psychological interdependencies. We propose a graph-regularized learning framework that conceptualizes emotions as nodes in a graph where edges encode proximity based on dimensional emotion theories. We adapt three complementary regularization strategies--Graph Label Smoothing (intuitiv...
  </details>

- **2026-07-08** — Chenghao Xu, Malcolm Mielle, Olga Fink — [Beyond Thermal Imaging: Inferring Thermophysical Properties from Time-Resolved Thermal Observations](http://arxiv.org/abs/2607.07962v1)
  <details><summary>📄 Abstract</summary>
  Inferring latent physical properties from sensory observations is a fundamental challenge in machine perception. Among available sensing modalities, thermal imaging is particularly promising because temperature evolution is directly governed by heat-transfer physics and therefore encodes information about underlying thermophysical properties of a scene. Recovering spatially resolved thermophysical properties from thermal observations could transform applications ranging from digital twins and in...
  </details>

- **2026-07-08** — Piotr Put, Arjun Pillai, Xuan Hoang Le et al. — [Quantum Sensors for Chemistry and Materials Science](http://arxiv.org/abs/2607.07848v1)
  <details><summary>📄 Abstract</summary>
  The advancement of chemistry and materials science relies on transformative analytical tools which can overcome the sensitivity, spatial resolution, and throughput limitations of conventional techniques. This review explores the application of quantum sensors - specifically optically pumped magnetometers (OPMs) and nitrogen-vacancy (NV) centers in diamond - as robust platforms for molecular and materials analysis. We contrast the extreme magnetic sensitivity of macroscopic OPM ensembles with the...
  </details>

- **2026-07-08** — Dexing Liu — [Agent Delivery Engineering Predictive Reliability Framework](http://arxiv.org/abs/2607.07689v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM multi-agent systems face reliability risks invisible to infrastructure monitoring. We propose the ADE Predictive Reliability Framework (ADE-PRF), enabling proactive health trajectory prediction from passive degradation detection. ADE-PRF aggregates 20 heterogeneous signals across five layers into a Trust Margin (TM) metric (39.2-point dynamic range). Triple-method parallel prediction enables 8-hour forecasts: the Exponential method achieves MAE=1.228, Direction Accuracy=76.8%, w...
  </details>

- **2026-07-08** — Hyunjae Kim, Dain Kim, Pan Xiao et al. — [MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models](http://arxiv.org/abs/2607.07673v1)
  <details><summary>📄 Abstract</summary>
  Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and clinical validation. We introduce MedPMC, an automated, continuously updatable frame...
  </details>

- **2026-07-08** — Kaicong Huang, Meng Ma, Ruimin Ke — [CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis](http://arxiv.org/abs/2607.07601v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluation for autonomous driving is dominated by rare, safety-critical interactions, motivating simulators that can deliberately synthesize corner cases with photorealistic observations. Corner-case generation is inherently a multi-source problem spanning visual representation, scene reasoning, and vehicle trajectory generation and control. Prior knowledge- and model-based approaches typically focus on scene or trajectory components in isolation, while diffusion-based methods attempt end...
  </details>

- **2026-07-08** — Bojie Li, Noah Shi — [RLVP: Penalize the Path, Reward the Outcome](http://arxiv.org/abs/2607.07435v1)
  <details><summary>📄 Abstract</summary>
  Agents acting on our behalf in the real world (e.g. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps. Two things follow. First, deployability depends on the path, not only the outcome. An agent must respect outcome-neutral constraints such as not repeatedly calling an unresponsive user, respecting business hours, or completing required authentication constraints that outcome-based rewards cannot express, since violating them fr...
  </details>

- **2026-07-08** — Zhijin Meng, Francisco Cruz — [Initiation Safety: A Missing Dimension in Generalist-Robot Safety](http://arxiv.org/abs/2607.07420v1)
  <details><summary>📄 Abstract</summary>
  Safety for generalist robots is usually discussed in terms of motion or dialogue. We argue a third question is missing: should the robot take its first hard-to-undo social action at all, such as a greeting, an uninvited grasp, or stepping into someone's space? We call this initiation authorization. Current frameworks rarely treat it as a separate safety layer. Today's stacks often skip this step: a high engagement score or a confident VLA rollout is treated as permission to act. But seeing a per...
  </details>

- **2026-07-08** — Alvina Rwaichi Minja, Jema David Ndibwile — [Evaluating Endpoint Detection Robustness Against Genetic Algorithm Driven Code Transformations](http://arxiv.org/abs/2607.07191v1)
  <details><summary>📄 Abstract</summary>
  Post-compromise test variants are widely used in controlled security evaluation and endpoint robustness benchmarking. However, modern Antivirus (AV) and Endpoint Detection and Response (EDR) systems increasingly combine signature- and behavior-based detection, challenging the reliability of conventional detection pipelines under adaptive variation. This study introduces ShellForge, a Genetic Algorithm (GA)-driven framework that evolves post-compromise variants representative of remote command ex...
  </details>

- **2026-07-08** — Yeonseok Lee — [Separation Logic for Memory Conflict Detection in High-Level Synthesis](http://arxiv.org/abs/2607.07126v1)
  <details><summary>📄 Abstract</summary>
  High-Level Synthesis leverages loop unrolling and array partitioning, but scheduling concurrent accesses is challenging when indices contain non-affine arithmetic. Conventional polyhedral frameworks systematically over-approximate these non-linear transformations, forcing conservative serialization that degrades performance. To minimize this bottleneck, we present a spatial verification framework operating at the LLVM Intermediate Representation (IR) level. By extracting flat arithmetic expressi...
  </details>

- **2026-07-08** — Ruilin Tong, Dong Gong — [MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning](http://arxiv.org/abs/2607.06974v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly improve their reasoning at test time via additional computation, yet most existing works treat each problem in isolation. When problems arrive sequentially, accumulating reusable experience across them can further improve performance. Existing memory-based methods either store whole-solution templates that generalize poorly to novel problems or use heuristic step-level selection that is not optimized for final-answer correctness. Learning selection polic...
  </details>

- **2026-07-08** — Paul F. R. Wilson, Mohamed Harmanani, Zhuoxin Guo et al. — [Compass: Prostate Cancer Detection Needs Multi-View Context](http://arxiv.org/abs/2607.06919v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) analysis of micro-ultrasound ($μ$US) has shown promise for prostate cancer (PCa) detection. However, most existing AI methods focus on the analysis of single $μ$US images in isolation. By contrast, expert $μ$US readers typically assess a full recorded video study, which provides three-dimensional context, to improve PCa detection compared to single-frame analysis. Inspired by this clinical workflow, we propose Compass, a novel AI methodology which models a $μ$US stud...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 70 papers

- **2026-07-13** — Runhui Huang, Qihui Zhang, Zhe Liu et al. — [Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation](http://arxiv.org/abs/2607.11886v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose SpectraReward, a training-free reward function that turns pretrained MLLMs into off-the-shelf reward models for image-generation reinforcement learning. Instead of asking the MLLM to judge a generated image or answer decomposed verification questions, SpectraReward measures how well the original prompt can be recovered from the generated image through a single image-conditioned, teacher-forced forward pass. We use the average image-conditioned prompt log-likelihood as t...
  </details>

- **2026-07-13** — Landon Liu, Mary Kelly, Alan Tsang — [Forgetting Our Way to Shared Meaning: Effects of Forgetting on Conceptual Alignment in a Non-Partnership Coordination Game](http://arxiv.org/abs/2607.11787v1)
  <details><summary>📄 Abstract</summary>
  Shared meaning in language requires people to learn and agree on categories. We ask how characteristics of agents' memories change the emergence and evolution of shared meaning. Without a coordination game, models of conceptual semantics cannot explain how shared meaning emerges and changes in groups of people; however, existing games assume that players share payoffs in a partnership setting. We model conceptual alignment as a non-partnership game and illustrate differences in actual and percei...
  </details>

- **2026-07-13** — Elmira Salari, Hazem Amamou, José Victor de Souza et al. — [How Temperature Shapes Ideological Discourse in Retrieval-Augmented Generation?](http://arxiv.org/abs/2607.11783v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) has been increasingly adopted to reduce hallucinations and strengthen the factual grounding of large language models (LLMs). While robustness to errors in the retrieval process has been explored, the impact of ideological bias on LLM outputs has been overlooked. For instance, if the retrieved material contains ideological positions, the RAG may transmit, amplify, or suppress such ideological discourses in its outputs. In this study, we address this issue by e...
  </details>

- **2026-07-13** — Daocheng Fu, Rong Wu, Yu Yang et al. — [Proxy Exploration and Reusable Guidance: A Modular LLM Post-Training Paradigm via Proxy-Guided Update Signals](http://arxiv.org/abs/2607.11505v1)
  <details><summary>📄 Abstract</summary>
  Post-training is essential for refining the domain-specific capabilities of large language models (LLMs), yet existing reward optimization and distribution matching methods tightly couple policy exploration with distribution alignment. This coupling forces expensive exploration directly on the policy model and severely hinders the asynchronous generation, reuse, and cross-model transfer of optimization signals. In this paper, we propose Proxy-guided Update Signal Transfer (PUST), a novel post-tr...
  </details>

- **2026-07-13** — Thi Kim Trang Vo, Nghia Hieu Nguyen, Ha Minh Tan — [Direct Image-to-Modern Vietnamese Translation of Han-Nom Manuscripts via Multimodal RLHF Preference Alignment](http://arxiv.org/abs/2607.11434v1)
  <details><summary>📄 Abstract</summary>
  Translating Han-Nom manuscripts into modern Vietnamese is challenging because historical pages are often degraded, the script contains rare logographic characters, and parallel supervision is limited. We propose a multimodal RLHF preference-alignment framework that conditions Vietnamese generation on manuscript images and aligned Han-Nom source text. The model combines four streams: CLIP ViT-L/14@336 for visual features, bert-base-chinese for Han-Nom representations, vinai/phobert-base for Vietn...
  </details>

- **2026-07-13** — Philip Schultheis, Kimia Chavoshi, John Lygeros — [Decentralized Model Predictive Control of Connected and Automated Vehicles with Coupled Safety Constraints](http://arxiv.org/abs/2607.11403v1)
  <details><summary>📄 Abstract</summary>
  Connected and Automated Vehicles (CAVs) operating on lane-free highways offer substantial gains in traffic efficiency. However, their inherent nonlinear dynamics and the presence of coupled, nonconvex safety constraints present critical challenges to control design. Centralized Model Predictive Control (MPC) ensures safety, but suffers from scalability and communication limitations. To address these challenges, this paper investigates decentralized MPC (DMPC) for CAV coordination, focusing on it...
  </details>

- **2026-07-13** — Chunyu Hu, Tianyin Liao, Ge Lan et al. — [Surprisingly Simple and Effective Multi-Domain Graph Foundation Model through Graph-to-Table Alignment](http://arxiv.org/abs/2607.11374v1)
  <details><summary>📄 Abstract</summary>
  Graph Foundation Models (GFMs) have emerged as a promising paradigm for learning transferable representations across diverse graph domains. Recent advancements in GFMs have been largely dominated by two paradigms: Graph Neural Network and Large Language Model (LLM) based methods. However, these methods often face a fundamental dilemma between training with limited data and a heavy reliance on textual attributes. Tabular foundation models (TFMs) offer a potential alternative, as node features and...
  </details>

- **2026-07-13** — Ajitesh Jamulkar, Aritra Hazra — [BackgroundMellow: A Multi-Modal Cohesive Framework for Narrative-Driven Rich Cinematic Soundscape Generation](http://arxiv.org/abs/2607.11364v1)
  <details><summary>📄 Abstract</summary>
  Generating immersive, synchronized and cinematic audio for long-form textual narratives remains a significant challenge in multi-modal AI. While current Text-to-Audio (TTA) frameworks successfully synthesize isolated sound effects, they struggle with narrative cohesion, temporal alignment, and cinematic emotional depth. We present BackgroundMellow, a framework that treats story-to-audio generation as a precise orchestration and signal processing problem. This framework is enabled without ground-...
  </details>

- **2026-07-13** — Jimin Xu, Tianbao Wang, Tao Jin et al. — [HierCAD: Hierarchical Text-to-CAD Design via Structure Alignment and Parameter Grounding](http://arxiv.org/abs/2607.11339v1)
  <details><summary>📄 Abstract</summary>
  Recent text-to-CAD approaches have shown promising results by leveraging large language models, but they often struggle with maintaining structural consistency in complex designs and accurately grounding geometric parameters. To address these issues, we propose HierCAD, a hierarchical text-to-CAD framework that improves both structural reasoning and parameter prediction. HierCAD reformulates CAD generation as progressive reasoning by decomposing CAD construction trees into object-level procedura...
  </details>

- **2026-07-13** — Alexis Popovici, Andrei Ionascu, Adrian-Marius Dumitran — [The Paternalistic Filter: Epistemic Injustice and Differential Refusal in LLM-Mediated History Education for Marginalized Romanian Students](http://arxiv.org/abs/2607.11292v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) are increasingly deployed as conversational tutors, they risk institutionalizing systemic inequalities. This study presents a systematic API audit of four LLMs acting as history tutors, evaluating 1,800 responses regarding the 1989 Romanian Revolution across five student personas varying by ethnicity and socio-economic tier. We uncover four interconnected patterns of \emph{epistemic paternalism}: (1)~\textbf{Differential Refusal}, where safety-aligned models block...
  </details>

- **2026-07-13** — Gangsu Kim, Won-Ki Jeong — [LaGuadia: Language-Guided Adaptive Distillation from Pathology Foundation Models](http://arxiv.org/abs/2607.11257v1)
  <details><summary>📄 Abstract</summary>
  Pathology Foundation Models (PFMs) offer powerful Whole Slide Image (WSI) representations but suffer from massive computational costs. While Knowledge Distillation (KD) can create efficient student models, existing multi-teacher methods often use suboptimal uniform weighting that ignores tissue heterogeneity. We propose LaGuadia (Language-Guided Adaptive DistillAtion), a framework that develops a compact pathology image encoder by dynamically integrating expertise from multiple PFMs under clinic...
  </details>

- **2026-07-13** — Shyam Marjit, Dheeraj Baiju, Anuj Shikarkhane et al. — [DynEval: Holistic Evaluations of T2I Generative Models in the Wild](http://arxiv.org/abs/2607.11199v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in text-to-image (T2I) generation have led to models capable of producing highly realistic images. Yet, reliably evaluating their outputs remains challenging, especially at scale. Existing automatic evaluators, often relying on a static prompt set, struggle to capture subtle failure modes such as partial prompt misalignment, compositional errors, or visually plausible but semantically incorrect generations. In this work, we introduce DynEval, a Dynamic Evaluation framework design...
  </details>

- **2026-07-13** — Alexandre Chapin, Emmanuel Dellandrea, Liming Chen — [Slot-RAE: Streamlining Object-Centric Learning via Direct Representation Auto-Encoders](http://arxiv.org/abs/2607.11196v1)
  <details><summary>📄 Abstract</summary>
  Deploying object-centric models for real-world scene understanding typically requires complex pipelines to achieve both robust scene decomposition and high-fidelity generation. Recent diffusion-based approaches have improved visual quality, but they almost universally rely on heavy, pretrained generative priors (e.g., Stable Diffusion) and external VAE latent spaces. In this paper, we propose Slot-RAE, a much simpler, fully integrated framework that operates directly within the continuous semant...
  </details>

- **2026-07-13** — Soohan Abbasi, Shahid Munir Shah, Rafia Shaikh et al. — [SISA-Rec: A Semantically Integrated Sequential Recommender with Contrastive Alignment](http://arxiv.org/abs/2607.11168v1)
  <details><summary>📄 Abstract</summary>
  Recommendation systems help users recommend relevant items from a large collection of choices. Present work on transformer-based sequential recommendation learns user preferences from interaction logs, but it mostly focuses on item identifiers and doesn't fully use the semantic meaning of items. This limitation becomes a major challenge in sparse and cold-start scenarios where historical interaction data is limited. To solve this problem, we introduce SISA-Rec (Semantically Integrated Sequential...
  </details>

- **2026-07-13** — Quynh Vo, Cong-Duy Nguyen, Ponhvoan Srey et al. — [TIGER: Text-Conditioned Visual Gated Routing with Acceptance Alignment for Multimodal Speculative Decoding](http://arxiv.org/abs/2607.11131v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates autoregressive generation by letting a lightweight drafter propose multiple tokens that are verified by a larger target model. Although effective for text-only LLMs, speculative decoding yields limited gains in VLMs because drafters often diverge on vision-critical content, while existing multimodal acceleration methods do not directly address irrelevant visual evidence or optimize the verifier-accepted prefix length that governs speedup. We propose TIGER, a Text...
  </details>

- **2026-07-13** — Xiuwei Chen, Quanlin Chen, Wentao Hu et al. — [Beyond the Eye: Efficient Multimodal Reasoning via Self-Regulated Implicit Visual Tools](http://arxiv.org/abs/2607.11106v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal large language models (MLLMs) have made remarkable progress on fine-grained perception tasks under the "Thinking with Images" (TwI) paradigm by iteratively performing various visual tool operations. However, this paradigm relies heavily on frequent external tool calls and repeated image re-encoding, which leads to substantial computational overhead and inference latency. To address these issues, we propose Beyond the Eye (BEE), a novel implicit visual tool paradigm centered on ...
  </details>

- **2026-07-13** — Andrew Hong, Jason Potteiger — [Dimensionality in Satisfaction Ratings](http://arxiv.org/abs/2607.11026v1)
  <details><summary>📄 Abstract</summary>
  We used a large language model (GPT-4.1) to annotate the text of about 9,000 support conversations at a global consumer-goods firm, decomposing customer-care satisfaction into component axes (overall, agent, outcome, product, and customer effort), and validated the LLM annotations against the satisfaction ratings customers gave themselves. Four of five axes track self-reported satisfaction closely (overall, agent, and outcome near an unadjusted 0.65; effort -0.54), while product satisfaction is ...
  </details>

- **2026-07-13** — Varun Ramesh Jois, Antonella DiLillo, James Storer — [Reference-Based Face Super-Resolution Using the Spatial Transformer](http://arxiv.org/abs/2607.11025v1)
  <details><summary>📄 Abstract</summary>
  Face super-resolution is the task of increasing the resolution of an image containing a face thereby adding finer detail. It is a ubiquitous task in many computer vision applications and quite often the user isn't even aware that it is being performed. However, doing it with high fidelity is challenging as it is an ill-posed problem. In this paper we present a reference-based solution for face super-resolution that uses higher resolution reference images to aid in the task. We show an alignment ...
  </details>

- **2026-07-13** — Jie Sun, Mao Zheng, Mingyang Song et al. — [EasyOPD: An Easy-to-use On-Policy Distillation Framework for Large Language Models](http://arxiv.org/abs/2607.11012v1)
  <details><summary>📄 Abstract</summary>
  Conventional language-model distillation often relies on fixed teacher-generated data, which may not cover the states encountered by an evolving student policy. On-policy distillation (OPD) instead collects teacher or evaluator supervision on student-generated rollouts. However, existing OPD methods differ substantially in supervision form, tokenizer compatibility, teacher access, and supervision granularity, leading to fragmented implementations that are difficult to reproduce and extend. We pr...
  </details>

- **2026-07-13** — Youngung Han, Hyunsu Go, Kyeonghun Kim et al. — [LoSA-Net: A Localized and Scale-Adaptive Network for Boundary-Sensitive Prediction of Perineural Invasion in 3D MRI](http://arxiv.org/abs/2607.10992v1)
  <details><summary>📄 Abstract</summary>
  Perineural invasion (PNI) is a clinically relevant indicator of tumor aggressiveness and can influence surgical decision-making, motivating interest in reliable preoperative assessment. The subtle MRI features of PNI, however, often resemble nearby anatomy, complicating noninvasive prediction. These fine perineural cues are easily attenuated by routine downsampling or overly global feature aggregation, reducing the effectiveness of conventional volumetric models. We present LoSA-Net, a localized...
  </details>

- **2026-07-13** — Thanh-Nhan Vo, Thanh-Khoi Nguyen, Trong-Thuan Nguyen et al. — [TreeSoc: Tree-Structured Dynamic Reasoning and Tool Synergy for Soccer Video Understanding](http://arxiv.org/abs/2607.10990v1)
  <details><summary>📄 Abstract</summary>
  Automated understanding of complex soccer scenarios from video remains a significant challenge for contemporary vision-language models (VLMs), which suffer from shallow cross-modal alignment and exhibit fundamental limitations in multi-step reasoning and coordinated tool integration. We present TreeSoc, a structured reasoning framework that reformulates soccer video question answering as a hierarchical search problem rather than a single-pass prediction. Specifically, TreeSoc employs a dynamic d...
  </details>

- **2026-07-12** — Guoliang You, Hongming Li, Yuanwang Zhang et al. — [Learning Anatomy-Grounded CT Vision-Language Representations with Organ-Hierarchical Report Knowledge](http://arxiv.org/abs/2607.10953v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language pretraining (VLP) from paired CT images and radiology reports enables scalable representation learning, but most existing methods align either whole scans with entire reports or local image regions with text fragments. These formulations underuse a key property of radiology reports: findings are organized around anatomical structures, with abnormalities described by organs, disease concepts, locations, and severity-related attributes. We propose OKA-CT, an organ-hierarchi...
  </details>

- **2026-07-12** — Asher Sprigler, Yang-Yang Feng, Iftach Amir et al. — [Toward Contemplative LLM: A Modular Framework for Evaluating and Enhancing LLM Alignment in Mental Health](http://arxiv.org/abs/2607.10871v1)
  <details><summary>📄 Abstract</summary>
  Contemplative traditions have long guided ethical behavior and prosocial interaction, and recent work suggests that contemplative principles (e.g., mindfulness, compassion, non-dual reasoning) may offer a promising paradigm for aligning large language models (LLMs), improving cooperation and reducing ethical violations in LLM outputs. However, as new models, evaluation metrics, and benchmarks emerge rapidly, it remains challenging to systematically assess whether and how contemplative principles...
  </details>

- **2026-07-12** — Tonmoy Hossain, Atiqur Rahman, Farhana Hossain Swarnali et al. — [Learning To Focus: Anatomy-Guided Attention Regularization for Medical Image Classification](http://arxiv.org/abs/2607.10851v1)
  <details><summary>📄 Abstract</summary>
  Medical image classification models are ideally expected to identify diagnostically relevant regions while making predictions, yet standard classification losses rarely provide spatial supervision. Explicit supervision via anatomical shape information, such as segmentation masks of task-relevant anatomy, has been shown to guide the network toward regions relevant to the target prediction. However, obtaining such masks incurs substantial manual annotation effort and computational overhead. With t...
  </details>

- **2026-07-12** — Venkanna Babu Guthula, Oswin Krause, Dimitri Gominski et al. — [Align and Segment: Unsupervised Learning for Building Segmentation From Misaligned Labels](http://arxiv.org/abs/2607.10841v1)
  <details><summary>📄 Abstract</summary>
  Supervised learning for image segmentation typically requires spatially aligned image and label sets. When images and labels originate from different sources, the pairing may be misaligned, which can significantly deteriorate the performance of the learned models. This is especially common in remote sensing, when aerial or satellite images are co-registered with labels from another source (e.g., OpenStreetMap). In this work, we propose a novel approach for training on misaligned labels, where we...
  </details>

- **2026-07-12** — Kai Yu, Lu Chen, Hanqi Li — [Distributed Agent System: Fault-Tolerant Collaboration Among Embodied Agents](http://arxiv.org/abs/2607.10811v1)
  <details><summary>📄 Abstract</summary>
  AI engineering is shifting from passive text generation by large language models (LLMs) to agent-driven task execution, creating new reliability challenges for long-horizon tasks under resource constraints and environmental uncertainty. Conventional error-elimination optimization strategies fail to address cumulative error propagation. This paper proposes Distributed Agent System (DAS), a device-edge-cloud framework for fault-tolerant collaboration among heterogeneous agents. We redefine agent r...
  </details>

- **2026-07-12** — Zehui Guo, Zhen Wang, Junwei Shu et al. — [h-Flow: Flexible Flow-based Image Editing via Doob's h-Transform](http://arxiv.org/abs/2607.10800v1)
  <details><summary>📄 Abstract</summary>
  Editing images with pre-trained text-to-image flow models typically requires carefully balancing target alignment with the desired prompt and source consistency with the original image. Existing approaches either rely on inversion-based pipelines or heuristic source-to-target trajectory constructions, which often depend on architecture-specific designs or are sensitive to hyperparameters. In this paper, we propose h-Flow, a training-free and theoretically grounded flow-based editing framework. I...
  </details>

- **2026-07-12** — Siyuan Song, Zhiheng Qian, Yunhao Zhang et al. — [The First ChineseBabyLM Challenge: training data-efficient and cognitively plausible language models for Chinese](http://arxiv.org/abs/2607.10745v1)
  <details><summary>📄 Abstract</summary>
  This paper describes the first ChineseBabyLM challenge, which will be held in the 2026 NLPCC conference. The challenge calls for researchers to train language models from scratch with 100 million Chinese tokens and evaluates the models on 3 tracks of tasks: NLU, cognitive alignment and Hanzi knowledge. There is no restriction on tokenizer, model architecture and the number of training epochs. Details of the challenge can be found in https://chinese-babylm.github.io/.
  </details>

- **2026-07-12** — Khush Kataruka, Harshit Maurya, Anuja Vats et al. — [WasteAssistant: Regulation-Guided Visual Question Answering Framework for Intelligent Waste Segregation and Sustainable Managemen](http://arxiv.org/abs/2607.10610v1)
  <details><summary>📄 Abstract</summary>
  Efficient waste segregation is critical for sustainable urban management and environmental governance. Existing automated systems are limited by single-modality visual processing, insufficient contextual understanding, and weak regulatory alignment. To address these issues, we propose a language-guided vision-AI framework that integrates vision-language models and multimodal large language models for joint visual-linguistic reasoning. This framework implements a visual question answering paradig...
  </details>

- **2026-07-12** — Mahammed Kamruzzaman, Shrabon Kumar Das, Gene Louis Kim — [Demographic Prompting at Scale: When More Attributes Hurt LLM--Human Agreement](http://arxiv.org/abs/2607.10590v1)
  <details><summary>📄 Abstract</summary>
  We investigate how annotator demographic attributes, supplied as prompt cues, shape the alignment between large language model (LLM) predictions and human annotations across five tasks. Using five open-source LLMs, we systematically vary the number and composition of demographic components in the prompt, spanning every combination from single-attribute through full-attribute configurations. Our experiments reveal three principal findings. First, alignment consistently peaks with one to three hig...
  </details>

- **2026-07-12** — Yunpeng Hong, Chenyang Bu, Di Wu et al. — [Implicit Fine-tuning via Context Engineering: A Curriculum Learning Framework for Multimodal Entity Alignment](http://arxiv.org/abs/2607.10532v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Entity Alignment (MMEA) aims to identify equivalent entities across different modalities. While existing methods enhance MMEA performance through black-box context engineering strategies, their reliance on LLM parameter capacity and lack of theoretical interpretability remain unresolved. To this end, we first theoretically validate the mathematical equivalence between context engineering and model fine-tuning in MMEA tasks, demonstrating that prompt components simulate contrastive lea...
  </details>

- **2026-07-12** — Seyed Arshan Dalili, Ajay Narayanan Sridhar, Vijaykrishnan Narayanan et al. — [Conditional Optimal Bridge for Riemannian Activation Steering](http://arxiv.org/abs/2607.10517v1)
  <details><summary>📄 Abstract</summary>
  Activation steering offers a lightweight alternative to fine-tuning for controlling large language models at inference time. While many existing methods implicitly optimize a log-density-ratio objective between desired and undesired activation distributions, they do so heuristically rather than deriving it from a principled optimization problem. Moreover, these methods produce query-independent steering directions that can degrade performance on both in-distribution and out-of-distribution (OOD)...
  </details>

- **2026-07-11** — Filip Pawlicki, Marcel Kańduła, Marcin Pucek et al. — [NanoVSR: Towards Real-Time Video Super-Resolution on Edge Devices](http://arxiv.org/abs/2607.10495v1)
  <details><summary>📄 Abstract</summary>
  Recent Video Super-Resolution (VSR) methods rely heavily on transformers and explicit optical flow, creating computational overhead and custom operations that hinder deployment on hardware accelerators like TensorRT. To address this, we introduce NanoVSR, a scalable, fully convolutional architecture designed for resource-constrained edge devices. Using structural reparameterization, NanoVSR collapses into standard convolutions during inference, ensuring seamless hardware compatibility and neglig...
  </details>

- **2026-07-11** — Christopher Buratti, Michele Marchetti, Federica Parlapiano et al. — [Gradient-Skipping Relevance Propagation for Efficient Explainability of Vision Transformers](http://arxiv.org/abs/2607.10365v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) are difficult to interpret because current methods of relevance propagation and attention flow do not fully consider some key architectural features, such as the uneven importance of attention heads and residual connections. Prior approaches typically assume uniform importance across attention heads; furthermore, they model skip connections as identity paths, leading to inaccurate relevance attribution. To address these issues, we introduce GradSkip, a novel relevance ...
  </details>

- **2026-07-11** — Oliver Steele, Jiangtao Wen, Yuxing Han — [One mechanism for many mental spaces: a shared router over a value slot in language models](http://arxiv.org/abs/2607.10248v1)
  <details><summary>📄 Abstract</summary>
  Language builds discourse contexts other than the actual: a painting, a belief, a memory, a hypothetical. Each is a mental space in which the same entity can take a different value, as when a flower is red in reality but purple in a portrait. Formal semantics keeps these contexts apart because their logics differ (modal, temporal, doxastic, depictive); Fauconnier's mental-space theory treats them as one space-building operation. We ask which of these a transformer language model implements, and ...
  </details>

- **2026-07-09** — Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang et al. — [LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models](http://arxiv.org/abs/2607.08770v1)
  <details><summary>📄 Abstract</summary>
  Recovering high-quality video from sparse event streams is a challenging task. Regression methods often blur textures, while existing generative models struggle with long-term stability. We propose LongE2V, a novel approach that leverages pre-trained video diffusion priors to jointly handle event-based video reconstruction, prediction, and frame interpolation. By fine-tuning a foundational video model, our approach achieves high data efficiency and superior perceptual quality. We introduce Autor...
  </details>

- **2026-07-09** — Wenbo Xu, Zhimin Chen, Xiaojie Liang et al. — [HumanForge: A Human-Centric Deepfake Video Benchmark with Multi-Agent Forgery Rationales](http://arxiv.org/abs/2607.08705v1)
  <details><summary>📄 Abstract</summary>
  Rapid advancements in video diffusion models and temporal editing tools have enabled the generation of highly realistic human-centric videos, posing unprecedented challenges to digital content forensics. Existing benchmarks primarily focus on either face-swapping or global text-to-video synthesis, overlooking the crucial dimensions of human-object or human-human interactions and multi-modal alignment. To address these limitations, we introduce HumanForge, a unified, large-scale, and multi-paradi...
  </details>

- **2026-07-09** — Xinlong Zhao, Dongsheng Liu, Hengyu Zhao et al. — [UltraX: Refining Pre-Training Data at Scale with Adaptive Programmatic Editing](http://arxiv.org/abs/2607.08646v1)
  <details><summary>📄 Abstract</summary>
  As available training data approaches its physical limit, gains from Scaling Laws have begun to diminish. Consequently, improving Large Language Models (LLMs) now depends less on data expansion and more on higher-quality data utilization. However, in the context of large-scale corpora, existing refinement methodologies face significant limitations in quality, efficiency, and reliability: Rule-based approaches are constrained by fixed heuristics and struggle with instance-level variations; LLM-ba...
  </details>

- **2026-07-09** — Weiduo Liao, Yunqiao Yang, Ying Wei — [When Structured Sparse Autoencoders Learn Consistent Concepts Across Modalities](http://arxiv.org/abs/2607.08605v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) have emerged as a promising technique for mechanistic interpretability by learning a set of sparse latent features in large models, each of which encodes a distinct concept. However, in vision-language models (VLMs), vanilla SAEs struggle to learn modality-consistent concepts, with concepts often exhibiting fragmented coverage (i.e., disjoint regions) in the visual modality. To address this challenge, we propose a Structured Sparse AutoEncoder ($S^2AE$) that enforces c...
  </details>

- **2026-07-09** — Arav Gupta, Nivedan Yakolli, Avinash Gautam — [Early to Share, Late to Save: Synchronisation-Driven Communication Gating in Bandwidth-Constrained Cooperative VLN](http://arxiv.org/abs/2607.08504v1)
  <details><summary>📄 Abstract</summary>
  Most cooperative Vision-Language Navigation (VLN) methods assume unlimited communication, not considering real-world applications where bandwidth is restricted and information efficiency is critical. We introduce \textbf{bandwidth-constrained cooperative VLN} and propose \textbf{hindsight gating}: a lightweight supervised gate that labels communication-critical steps post-hoc from navigation failures, avoiding the high variance of REINFORCE. Contrary to the intuition that agents should communica...
  </details>

- **2026-07-09** — Shun Liu, Nan Xi, Yang Liu et al. — [Attribute Retrieving for Open-Vocabulary Endoscopic Compositional Referring Segmentation](http://arxiv.org/abs/2607.08397v1)
  <details><summary>📄 Abstract</summary>
  Referring Image Segmentation (RIS) aims to segment image regions specified by natural language, enabling fine-grained and controllable visual understanding. Extending RIS to endoscopic imagery, however, presents unique challenges, including scarce high-quality annotations and complex, domain-specific image-text relationships. Although recent vision-language models demonstrate strong cross-domain alignment, they often fail to capture fine-grained textual cues in endoscopic settings, resulting in ...
  </details>

- **2026-07-09** — Xuerun Yan, Zhexi Lian, Nuoheng Zhang et al. — [WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving](http://arxiv.org/abs/2607.08375v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-V...
  </details>

- **2026-07-09** — Jing Jie Tan, Ban-Hoe Kwan, Danny Wee-Kiat Ng et al. — [Large-Language-Models-as-a-Judge in Theory-Agnostic Adaptive Metric-Alignment for Prototypical Networks in Personality Recognition](http://arxiv.org/abs/2607.08374v1)
  <details><summary>📄 Abstract</summary>
  Personality recognition has traditionally been constrained by theory-dependent formulations, where models are trained to fit predefined psychological taxonomies rather than uncovering shared underlying behavioral structure. This limits generalization, as personality itself is better understood as theory-invariant, while existing annotations reflect only partial and sometimes inconsistent views of the same latent traits. In this work, we introduce JAM ((J)udge for (A)daptive (M)etric-Alignment), ...
  </details>

- **2026-07-09** — Fengyuan Liu, Yuchen Fu, Yuqi Wang et al. — [XALPHA: A Memory-Driven AI Quant Researcher for Hypothesis-to-Code Alpha Discovery](http://arxiv.org/abs/2607.08332v1)
  <details><summary>📄 Abstract</summary>
  Financial markets are noisy, non-stationary, and high-dimensional, making it difficult to discover predictive and robust trading signals. Alpha discovery has evolved from manual factor design to machine learning, evolutionary search, and recent LLM-based frameworks, improving the efficiency of factor generation, search, and evaluation. However, existing methods still mostly automate isolated steps, rather than functioning as end-to-end quant researchers that can absorb external knowledge, close ...
  </details>

- **2026-07-09** — Ludovica de Paolis, Marco Baroni, Alessandro Laio et al. — [Texture Representations in Deep Vision Models: Comparing CNNs, Vision Transformers, and Human Perception](http://arxiv.org/abs/2607.08321v1)
  <details><summary>📄 Abstract</summary>
  In computational vision science, Convolutional Neural Networks (CNNs) have emerged as a popular model of biological vision because of the alignment they can exhibit with neural and behavioral data in humans and animals. However, it remains unclear to what extent this alignment persists for visual tasks that extend beyond the canonical object recognition paradigm based on well defined semantic content. In this study, we diverge from the common object-centric view by focusing on another aspect of ...
  </details>

- **2026-07-09** — Yuming Yang, Xiao Sun, Yuanwei Zou et al. — [MentalHospital: A Virtual Environment for Evaluating Psychiatric Clinical Encounters](http://arxiv.org/abs/2607.08257v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong performance on isolated psychiatric tasks, including dialogue, diagnosis, and treatment planning, yet existing benchmarks rarely simulate complete psychiatric clinical encounters. We introduce $\textbf{MentalHospital}$, a virtual evaluation environment for LLM-based psychiatric clinical encounters. MentalHospital instantiates the Subjective Interviewing, Objective Examination, Diagnostic Assessment, and Treatment Planning (S.O.A.P.) workflow, using ...
  </details>

- **2026-07-09** — Zheng Yu — [On the Limitations of Non-GPU AI Accelerators for Large-Model Inference: A Field Study of MoE and Multimodal Serving on Huawei Ascend](http://arxiv.org/abs/2607.08215v1)
  <details><summary>📄 Abstract</summary>
  Non-GPU AI accelerators are increasingly adopted as alternatives to general-purpose GPUs for large-model inference, but the real engineering cost of migrating demanding workloads beyond CUDA remains poorly documented. We present a field study of deploying two large inference workloads on a 16-device Huawei Ascend 910 system using CANN and vLLM-Ascend: an LLM-as-a-judge safety and alignment evaluation pipeline based on a W8A8 MoE judge model, DeepSeek-V4-Flash, and a multimodal medical vision--la...
  </details>

- **2026-07-09** — Mingjia Shi, Shuo Wang, Xiaobo Wang et al. — [Dive Into the Implicit Biases of Low-rank Vision-language Alignment](http://arxiv.org/abs/2607.08194v1)
  <details><summary>📄 Abstract</summary>
  Vision-language alignment, the stage that bridges pretrained vision encoders and large language models, is widely treated as a form of pretraining requiring full-parameter updates. We challenge this view and investigate what happens when low-rank adaptation is applied to the LLM during this stage instead. We find that low-rank alignment not only reduces computational costs but also outperforms full-parameter alignment on most benchmarks. To understand this phenomenon, we systematically character...
  </details>

- **2026-07-09** — Yidong Ouyang, Zhe Wang, Sourav Bhabesh et al. — [Reinforcing the Generation Order of Multimodal Masked Diffusion Models](http://arxiv.org/abs/2607.08056v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Language Models (DLMs) have recently achieved substantial progress in natural language generation tasks. Recent research demonstrates that adaptive token generation ordering can significantly improve performance in mathematical reasoning and code synthesis applications. In this work, we investigate the optimization of generation order for both text-to-image synthesis and multimodal understanding. We first establish that, unlike structured problems in language generation such as Sudoku ...
  </details>

- **2026-07-09** — Samuel Tetteh, Udip Shrestha, Joshua R. Waite et al. — [Who Analyses the Analyser? Self-Validating LLM Hazard Analysis with Constitutional Meta-STPA](http://arxiv.org/abs/2607.08054v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly trusted to draft the artifacts of safety analysis such as, losses, hazards, Unsafe Control Actions (UCAs), and safety constraints, inside rigorous processes such as Systems-Theoretic Process Analysis (STPA). Yet a blind spot runs through this fast-growing literature: every system gets analysed except the LLM-assisted tool doing the analysing, which is itself a safety-relevant system that can hallucinate standards, emit unverifiable constraints, and l...
  </details>

- **2026-07-09** — Kshitij Dani, Cordero Core, Landung Setiawan et al. — [Aleena: Alignment Agent for Research Software Engineering Collaborations](http://arxiv.org/abs/2607.08043v1)
  <details><summary>📄 Abstract</summary>
  Research software collaborations span meetings, informal chats, pull requests, and GitHub issues. A decision surfaced in a Slack thread, refined in a meeting, and implemented in a pull request can lose its original rationale across these artifacts, leaving domain researchers and research software engineers with divergent mental models of project intent, ownership, and scientific assumptions. We argue that alignment in research software engineering is a continuous lifecycle problem, and that agen...
  </details>

- **2026-07-09** — Dhruv Agarwal, Anya Shukla, Tanya Goyal et al. — [PLURAL: A Global Dataset for Value Alignment](http://arxiv.org/abs/2607.08034v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are used worldwide, yet disproportionately reflect Western values, limiting their ability to represent diverse value systems. We introduce PLURAL, a large-scale, value-focused preference dataset grounded in the Integrated Values Survey (IVS), a nationally representative survey spanning 92 countries. Using a two-stage generation pipeline, we transform survey responses into synthetic preference triplets that preserve normative value signals while producing realistic sc...
  </details>

- **2026-07-09** — Hyeju Shin, Chorwon Kim, Ryangsoo Kim et al. — [Rethinking Small VLM Quantization: From Component-Wise Analysis to Hardware-Aware Edge Deployment](http://arxiv.org/abs/2607.08029v1)
  <details><summary>📄 Abstract</summary>
  The emergence of vision language models with fewer than 3 billion parameters has accelerated the implementation of on-device multimodal intelligence. However, a detailed understanding of component-wise quantization remains a bottleneck for optimal deployment. This paper presents a systematic evaluation framework for empirically validating five hypotheses across six quantization configurations on the Jetson Orin NX and AGX. By separating the vision encoder, projector, and large language model bac...
  </details>

- **2026-07-09** — Ryota Kobayashi, Tsubasa Hirakawa, Takayoshi Yamashita et al. — [Structured Pruning of Large Language Models via Power Transformation and Sign-Preserving Score Aggregation with Adaptive Feature Retention](http://arxiv.org/abs/2607.08027v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an improved structured pruning method for large language models (LLMs) that addresses key challenges in adapting Adaptive Feature Retention (AFR), an unstructured pruning technique, to structured pruning. When applying AFR to structured pruning, three major problems arise: distribution mismatch between heterogeneous pruning scores, loss of sign information indicating optimization direction consistency, and influence of outliers. To address these issues, we propose a unified a...
  </details>

- **2026-07-09** — Lu Dai, Ziyang Rao, Yili Wang et al. — [Towards Mechanistically Understanding Why Memorized Knowledge Fails to Generalize in Large Language Model Finetuning](http://arxiv.org/abs/2607.08393v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning LLMs to inject new knowledge faces a critical challenge: LLMs can quickly memorize new facts, yet fail to use them for downstream reasoning tasks. We formalize this failure as the \textit{\textbf{Knowing--Using Gap}}, characterized by an accuracy gap and a temporal lag between memorization and generalization. To understand this phenomenon, we fine-tune LLMs with unseen knowledge and monitor the spatial permeation dynamics of the knowledge internally using a novel intervention techniq...
  </details>

- **2026-07-08** — Paul Dela Cruz, Mostafa Mo. Massoud, Jacqueline Libby — [Soft Robotic Exogloves for Dexterous Mobility -- Towards Personalized Rehabilitation](http://arxiv.org/abs/2607.07968v1)
  <details><summary>📄 Abstract</summary>
  Soft robotic exogloves can provide hand rehabilitation and assistance. Fitting these gloves often relies on standardized measurements not tailored to the individual, limiting their effectiveness, especially for fine articulation necessary for dexterous manipulation. We present the design, fabrication, modeling, and testing of a personalized pneumatically-actuated soft robotic exoglove. The glove was fit to a user's hand with topological scans and fabricated with silicone mold casting. Finite ele...
  </details>

- **2026-07-08** — Benjamin Poole, Minwoo Lee — [Feedback Manipulation Regularization: Enabling Offline Agent Alignment for Imitation Learning](http://arxiv.org/abs/2607.07859v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) research has increasingly shifted focus towards alignment, ensuring agents learn behaviors adhering to human values. While human demonstrations and feedback have proven crucial for alignment, existing approaches predominantly combine these signals using multi-stage pipelines designed for the contextual bandit framing of language generation. Yet little work explores how these complementary inputs can serve as a richer, interconnected signal for single-stage offline tra...
  </details>

- **2026-07-08** — Gwydion Williams, Sara Zannone, Bilal A Mateen — [Alignment Plausibility: A New Standard for Assuring AI in Healthcare](http://arxiv.org/abs/2607.07766v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have become significant providers of mental health support, yet they remain products of an attention economy whose operational and commercial targets favour sustained engagement over the friction that effective psychological support often requires. Developers' safety responses have been largely reactive, addressing the most visible and acute harms while subtler, longer-term patterns of risk (e.g., dependency, boundary erosion, the amplification of distorted beliefs) ...
  </details>

- **2026-07-08** — Jianyi Zhou, Feiyang Hong, Yunhao Li et al. — [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](http://arxiv.org/abs/2607.07287v2)
  <details><summary>📄 Abstract</summary>
  Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states such as force, slip, and contact stability. Although tactile sensing exposes these physical cues, most existing policies treat touch as a low-f...
  </details>

- **2026-07-08** — Marcus Williams, Hannah Sheahan, Cameron Raymond et al. — [Predicting LLM Safety Before Release by Simulating Deployment](http://arxiv.org/abs/2607.07184v1)
  <details><summary>📄 Abstract</summary>
  Pre-deployment safety evaluations aim to inform the downstream risks of releasing a new AI model. Yet most evaluations provide limited evidence about how often undesired model behavior will occur in deployment: they generally have insufficient coverage, are unrepresentative, and are generally recognizable as tests. To address these concerns, we study a simple way to simulate a model deployment: starting from de-identified conversations from a previous model deployment, we hold fixed the initial ...
  </details>

- **2026-07-08** — Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay — [Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF](http://arxiv.org/abs/2607.07693v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that subs...
  </details>

- **2026-07-08** — Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. — [Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](http://arxiv.org/abs/2607.07675v1)
  <details><summary>📄 Abstract</summary>
  Despite the recent promise in robot control, video generative models suffer from a domain mismatch due to their primary focus on content creation. For example, their design inherently prioritizes visual fidelity and creativity over computational efficiency and physical realism. In this work, we present LingBot-Video, a DiT-based video pretraining paradigm specifically tailored for embodied intelligence. From the architecture perspective, we adopt the Mixture-of-Experts (MoE), instead of dense, f...
  </details>

- **2026-07-08** — Jordan Painter, Dipankar Srirag, Adarsh Kappiyath et al. — [DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect Adaptation](http://arxiv.org/abs/2607.07669v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly \emph{understand} dialectal English, yet still \emph{produce} only standard, US-leaning English, leaving dialectal generation, the harder half of the problem, largely unaddressed. We introduce \textbf{DiaLLM}, which continually pretrains three open-weight language model families on the International Corpus of English and applies implicit and explicit post-training paradigms, each combined with three model alignment strategies, giving the first controlled compar...
  </details>

- **2026-07-08** — Willem Fourie, Isabel Ray, Gray Manicom — [User identity conditions moral wrongness ratings in non-reasoning large language models](http://arxiv.org/abs/2607.07605v1)
  <details><summary>📄 Abstract</summary>
  This study adopts a behavioural bottom-up approach to AI value alignment to investigate whether an implicitly conveyed user identity shifts the moral evaluations of large language models (LLMs). Through a structured, multi-turn conversational protocol across 12,000 interactions, we evaluate AI value alignment in two non-reasoning models, gpt-4.1-mini-2025-04-14 and gemini-2.5-flash-lite. Rather than instructing the models to adopt a persona or prompting them with explicit moral stances, the user...
  </details>

- **2026-07-08** — Daeun Song, Nhat Le, Jeffrey Chen et al. — [HumAIN: Human-Aware Implicit Social Robot Navigation](http://arxiv.org/abs/2607.07357v1)
  <details><summary>📄 Abstract</summary>
  Effective social robot navigation requires sensitivity to human behavior, often revealed through subtle skeletal cues like gait and orientation. We present Human-Aware Implicit Social Robot Navigation (HumAIN), a novel framework that fuses implicit social cues directly into the planning loop via knowledge distillation. We first employ a transformer-based teacher model that fuses rich multi-modal inputs, including historic images, skeletal keypoints, robot state, and a robot's target goal, to lea...
  </details>

- **2026-07-08** — Georg Schäfer, Jakob Rehrl, Stefan Huber et al. — [Safe Reinforcement Learning using Ideas from Model Predictive Control](http://arxiv.org/abs/2607.07252v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) enables the synthesis of control policies directly from data, making it highly appealing for complex cyber-physical systems (CPSs) and robotics. A persistent challenge, however, is ensuring strict, hard safety constraints during the active learning phase. In real-world physical systems, violating mechanical limits can cause irreversible damage, necessitating that exploration remains strictly within safe operational regions. We propose a generalized framework that comb...
  </details>

- **2026-07-08** — Waqas Arshid, Mohammad Awrangjeb, Alan Wee-Chung Liew et al. — [`Attention-Guided Cross-Temporal Clustering for Self-Supervised Video Object Segmentation](http://arxiv.org/abs/2607.07230v1)
  <details><summary>📄 Abstract</summary>
  Video object segmentation (VOS) is a fundamental task in video understanding, requiring accurate delineation and consistent tracking of objects across frames. While supervised methods achieve strong performance, they rely on densely annotated datasets that are costly to obtain and have limited domain coverage. Self-supervised learning offers a promising alternative by removing the need for manual labels; however, existing approaches often struggle to jointly maintain spatial accuracy and tempora...
  </details>

- **2026-07-08** — Alejandro Vergara-Richart, Xavier Rafael-Palou, Almudena Fuster-Matanzo et al. — [Vision Foundation Models in Radiology: A Scoping Review of Data, Methodology, Evaluation and Clinical Translation](http://arxiv.org/abs/2607.07219v1)
  <details><summary>📄 Abstract</summary>
  Vision foundation models (VFMs) are increasingly being developed for radiological imaging, yet their definition, development and evaluation remain heterogeneous. We conducted a PRISMAScR scoping review of peer-reviewed studies published between January 2017 and March 2026 describing foundation models trained exclusively on radiological imaging data. Sixty-seven studies were included and mapped across three pillars: data scale and heterogeneity, architectural and pretraining scalability, and down...
  </details>

- **2026-07-08** — Wenyan Xu, Alizer Wong — [Stage-Aware Adaptation and Distribution Calibration for Subject-Driven Personalized Text-to-Image Generation](http://arxiv.org/abs/2607.07173v1)
  <details><summary>📄 Abstract</summary>
  Subject-driven personalized text-to-image generation requires a pretrained diffusion model to acquire a specific subject from a few reference images while preserving subject identity, following novel text prompts, and maintaining sample diversity. Existing optimization-based methods instantiate subject adaptation through full fine-tuning, textual embedding optimization, or low-rank parameter updates; PaRa further constrains personalization from the perspective of parameter rank reduction. Howeve...
  </details>

- **2026-07-08** — Yi Yang, Siyuan Liu, Xin Gao et al. — [Learning social norms enhances compatibility in dynamic human-AI coordination](http://arxiv.org/abs/2607.07021v1)
  <details><summary>📄 Abstract</summary>
  Humans continuously coordinate with others in dynamic interactions, often through implicit, hard-to-quantify social norms that act as shared tacit expectations among interacting agents. As AI agents, including large language models (LLMs), become embedded in daily life, they increasingly participate in such interactions and reshape social interaction structures. Yet they often fail to coordinate with humans in an effective, considerate, and natural manner. We hypothesize that this gap arises bec...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 85 papers

- **2026-07-13** — A. Krylov, D. Rakhov, V. Veselova et al. — [LLM-Guided Program Evolution for Targeted Black-Box Attacks on Perceptual Hash Algorithms](http://arxiv.org/abs/2607.11472v1)
  <details><summary>📄 Abstract</summary>
  Perceptual hash algorithms (PHAs) are widely deployed to detect image forgery under benign transformations, yet their robustness against adversarially chosen perturbations remains poorly understood and rarely comes with provable guarantees. We propose a novel evolutionary framework based on GigaEvo and OpenEvolve for targeted second-image attacks on perceptual hash algorithms. We assess attack performance using a composite score that jointly accounts for the fraction of adversarial images whose ...
  </details>

- **2026-07-13** — Anqi Li, Jie Zhang, Zhongqi Wang et al. — [DeepBias: Adaptive In-depth Probing of Social Biases in LVLMs](http://arxiv.org/abs/2607.11228v1)
  <details><summary>📄 Abstract</summary>
  While Large Vision-Language Models (LVLMs) demonstrate remarkable capabilities, they remain highly susceptible to embedded social biases. Existing bias evaluation protocols predominantly rely on static datasets, which provide only a superficial assessment, as their fixed test cases cannot adaptively evolve to measure the true depth and limits of model vulnerabilities. We introduce DeepBias, an adaptive framework for the in-depth probing of social biases in LVLMs with carefully designed agents. O...
  </details>

- **2026-07-13** — Aritra Mazumder, Nusrat jahan Lia — [AgentCheck: A Reproduce-Intervene-Mitigate Workbench for LLM Agents over MCP](http://arxiv.org/abs/2607.11098v1)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents are mostly evaluated assuming all tools work. When a tool times out, returns a week-stale value, or has its description poisoned in deployment, the developer needs a controlled way to reproduce the failure, test a fix, and confirm the fix worked before deployment. We present AgentCheck, an open-source web workbench that turns an MCP server into an intervention surface. AgentCheck runs an agent against its real tools and records every tool response, then re-runs the agent wi...
  </details>

- **2026-07-13** — Georgios Piliouras, Ian Gemp, Siqi Liu et al. — [Paradoxes of Game Theoretic Equilibria and Price of Anarchy](http://arxiv.org/abs/2607.11752v1)
  <details><summary>📄 Abstract</summary>
  For decades, static solution concepts (Nash, Correlated, and Coarse Correlated Equilibria) and the Price of Anarchy (PoA) have formed the bedrock of algorithmic game theory, with no-regret learning proving fast convergence to such game-theoretic equilibria. We show that reducing multi-agent learning to static equilibrium and black-box regret analysis obscures underlying dynamic disequilibrium and game theoretic bounds.   First, interior Nash equilibria lack $C^1$ vector field information, meanin...
  </details>

- **2026-07-13** — Xuefeng Li, Pengfei Liu — [UMoE:Unlocking Every Expert in Domain-Specific Training](http://arxiv.org/abs/2607.11444v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) models scale capacity without proportional compute cost and have become a key architecture for frontier large language models (LLMs). Yet domain-specific post-training inherits an expert pool shaped by mixed-domain pre-training: a substantial subset of experts contributes little on the target domain, and standard supervised fine-tuning (SFT) leaves the composition of this pool unchanged. We propose a simple, budget-preserving pipeline that realigns the expert pool to the...
  </details>

- **2026-07-13** — Haojie Huang, Linfeng Zhao, Haotian Liu et al. — [Pix2Act: Image-Space Manipulation Policies with Equivariant Augmentation](http://arxiv.org/abs/2607.11167v1)
  <details><summary>📄 Abstract</summary>
  Representing manipulation actions as 2D trajectories in the camera plane provides a compact and interpretable basis for learning complex 3D manipulation policies. However, it also creates challenges from out-of-frame trajectories and limited precision. We propose Pix2Act, an imitation learning method that addresses these challenges by generating continuous image-space keypoint trajectories in each camera plane and losslessly recovering end-effector poses via triangulation. This reformulates high...
  </details>

- **2026-07-13** — Pei Chen, Baichao An, Mengying Wu et al. — [Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability](http://arxiv.org/abs/2607.11086v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) has rapidly established itself as a standard interface for enabling LLM-based agents to interact with external tools and services. As MCP servers are increasingly entrusted with security-sensitive operations, understanding their real-world risks has become critical. In practice, due to the absence of large-scale runtime MCP servers, such understanding largely relies on security scanners applied to a small number of cases, yet the reliability of these assessments ...
  </details>

- **2026-07-13** — Xinghang Li, Jun Guo, Qiwei Li et al. — [Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](http://arxiv.org/abs/2607.11643v1)
  <details><summary>📄 Abstract</summary>
  Recent foundation image and video generation models offer strong generalization and controllability, but their direct application to embodied scenarios is limited by requirements for multi-view consistency, geometric coherence, and robot embodiment constraints. Existing methods typically adapt foundation models with limited robot data, often sacrificing visual knowledge acquired during large-scale pre-training. We present Xiaomi-Robotics-U0, a 38-billion-parameter multimodal autoregressive model...
  </details>

- **2026-07-13** — Jihong Chen — [Relational Positioning as a Measurable Risk Object: History-Carried Lock-in and Self-Confabulation in Multi-Turn Human-AI Dialogue](http://arxiv.org/abs/2607.11437v1)
  <details><summary>📄 Abstract</summary>
  In long, multi-turn dialogue a large language model maintains an implicit relational stance toward the user, spanning from "push the user toward real-world others" to "position itself as the user's sole support." When it slides toward the latter, "support" degrades into "you only have me" -- a harm documented in real companion conversations (Moore et al., 2026). We define and validate a measure of this stance, relational positioning (D1), and use it to characterize the stance under controlled co...
  </details>

- **2026-07-13** — Mingyue Huo, Yuheng Zhang, Hao Zhang — [Where Speech Enhancement Hurts Recognition: An Inference Time Polar Projection Diagnosis](http://arxiv.org/abs/2607.11157v1)
  <details><summary>📄 Abstract</summary>
  Speech enhancement (SE) can substantially improve perceptual quality, yet enhanced speech does not necessarily improve automatic speech recognition (ASR). Existing remedies, such as retraining the enhancer jointly with recognizer or interpolating enhanced speech with the noisy input, can mitigate this mismatch, but common explanations such as artifacts and over-suppression remain qualitative and do not localize which enhancement component harms recognition. We propose inference time polar projec...
  </details>

- **2026-07-13** — Shijie Wang, Honglu Zhou, Ziyang Wang et al. — [Evidence-Backed Video Question Answering](http://arxiv.org/abs/2607.11862v1)
  <details><summary>📄 Abstract</summary>
  Current Video Large Language Models (Video LLMs) excel in question answering (QA) but largely operate as black boxes, providing textual answers without verifiable visual grounding. Existing explainability efforts rely on textual rationales or sparse bounding boxes, which struggle to capture complex video dynamics such as occlusions and non-rigid deformations. We propose Evidence-Backed Video Question Answering (E-VQA), a novel task requiring models to jointly output a semantic answer and precise...
  </details>

- **2026-07-13** — Ziyue Jiang, Dake Guo, Zekai Zhang et al. — [Qwen-Audio-VAE Technical Report](http://arxiv.org/abs/2607.11738v1)
  <details><summary>📄 Abstract</summary>
  We introduce \textbf{Qwen-Audio-VAE}, a suite of low-bitrate, fast-encoding continuous audio autoencoders designed for scalable general audio generation. The model is built around a simple but important principle: an audio VAE should not only reconstruct diverse audio with high fidelity, but also produce compact latent representations fast enough to support large-scale text-to-audio training. Qwen-Audio-VAE combines a causal encoder-decoder, window Transformer blocks, and multi-discriminator tra...
  </details>

- **2026-07-13** — Aastha Sharma, Guangjing Wang — [VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion](http://arxiv.org/abs/2607.11706v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM-driven text-to-speech (TTS) and voice conversion (VC) systems produce synthetic speech that differs from the generators represented in many legacy spoofing benchmarks. This mismatch creates a temporal generalization gap that can overestimate detector robustness under real-world post-processing conditions. We bridge this gap by introducing VoxENES 2026, a bilingual (English and Spanish) benchmark of 53,628 audio samples generated using 10 contemporary speech synthesis methods and evalu...
  </details>

- **2026-07-13** — Yi-You Yang — [Robust Welfare Decentralization under Population Entry](http://arxiv.org/abs/2607.11658v1)
  <details><summary>📄 Abstract</summary>
  We ask when an incumbent economy with indivisible goods can accommodate an arbitrary new participant while retaining an efficient allocation supported by anonymous item prices. We call this property universal entry robustness. An economy is universally entry-robust if and only if its aggregate welfare valuation is additive. Although the requirement quantifies over all entrant valuations, it can be tested using one canonical entrant whose value for a bundle equals the loss in maximal incumbent we...
  </details>

- **2026-07-13** — Christelle Schneuwly Diaz, Narmina Baghirova, Duy-Thanh Vu et al. — [Imputation-free transformer learning enables robust Alzheimer's disease prediction and calibrated uncertainty quantification across heterogeneous clinical cohorts](http://arxiv.org/abs/2607.11656v1)
  <details><summary>📄 Abstract</summary>
  Accurate diagnostic classification and disease-severity prediction for Alzheimer's disease are hampered by the incompleteness and heterogeneity of real-world clinical data. Left unaddressed, these barriers prevent reliable disease modelling and hinder effective clinical evaluation. Conventional imputation strategies introduce systematic bias, distort inter-feature relationships, and yield overconfident predictions, limitations especially consequential in diagnostic settings. Here, we propose NIT...
  </details>

- **2026-07-13** — Ye Yuan, Kehan Chen, Xinqiang Yu et al. — [DA-Nav: Direction-Aware City-Scale Vision-Language Navigation](http://arxiv.org/abs/2607.11638v1)
  <details><summary>📄 Abstract</summary>
  City-scale outdoor navigation is currently hindered by the heavy reliance on dense maps or costly navigation supervision. In this work, we introduce a novel paradigm for leveraging directional instructions from commercial navigation tools (e.g., Google Maps). To bridge the gap between commercial instructions and executable navigation actions, while mitigating long-horizon error accumulation through robust trajectory recovery, we propose DA-Nav, a Direction-Aware vision-language Navigation framew...
  </details>

- **2026-07-13** — Yikang Chen, Zhengkang Guan, Haoyuan Qian et al. — [DAG-FM: A Foundation Model for Causal Discovery under Heterogeneous Causal Mechanisms](http://arxiv.org/abs/2607.11510v1)
  <details><summary>📄 Abstract</summary>
  Causal discovery from observational tabular data remains fundamentally challenging, primarily due to the heterogeneity of underlying causal mechanisms and the high-dimensional combinatorial search space of Directed Acyclic Graphs (DAGs). In this paper, we propose \textbf{DAG-FM}, a novel foundation model architecture that amortizes causal discovery. Unlike direct matrix prediction, DAG-FM decomposes the causal discovery process into two auto-regressive stages using two specialized Transformer-ba...
  </details>

- **2026-07-13** — Dmitry Nikolaev — [Are LLMs ready for HardChoices?](http://arxiv.org/abs/2607.11471v1)
  <details><summary>📄 Abstract</summary>
  A lot of research attention has been devoted to checking whether large language models (LLMs) are politically biased. This work has largely focused on high-level ideological dimensions, such as left--right or progressive--conservative, and it has been shown that while LLMs are predominantly left and progressive leaning, largely mimicking the biases in the training data, they can be to some extent steered to change their preferences in post-training. In this short note, we check if LLMs have robu...
  </details>

- **2026-07-13** — Roberta Rocca, Sami Boukortt, Geoff Keeling et al. — [Beyond Sally-Anne: Evaluating Theory of Mind in LLMs using Epistemic Schelling Points](http://arxiv.org/abs/2607.11363v1)
  <details><summary>📄 Abstract</summary>
  Text-based evaluations of Theory of Mind (ToM) in Large Language Models (LLMs) often involve cognitive tests akin to the Sally-Anne task that can be gamed due to exposure to relevantly similar tasks in pre-training and do not obviously test models' functional ToM abilities in ways that generalize to naturalistic settings. To address these issues, we introduce the Epistemic Asymmetry Schelling Task (EAST), a two-player dialogue game designed to benchmark robust and generalizable ToM abilities. By...
  </details>

- **2026-07-13** — David Otero, Javier Parapar — [User Preference Induction with LLMs for Offline Top-N Recommendation Evaluation](http://arxiv.org/abs/2607.11354v1)
  <details><summary>📄 Abstract</summary>
  Offline evaluation is the standard methodology for comparing top-N recommender systems, yet it relies on incomplete relevance information. In most benchmark datasets, only a small subset of user--item preferences is observed, and unjudged items are commonly treated as non-relevant. This missing-as-negative assumption can bias evaluation, penalize plausible recommendations with no recorded feedback, and favour algorithms that concentrate on popular or highly exposed items. We propose an LLM-based...
  </details>

- **2026-07-13** — Zhuo Xiao, Bo Liu, Jingjing Wang et al. — [Multi-Catheter Digitization in Brachytherapy via Few-Shot Synthetic-to-Real Learning and Structure-Aware Tracking](http://arxiv.org/abs/2607.11290v1)
  <details><summary>📄 Abstract</summary>
  Accurate catheter digitization in CT-guided interstitial brachytherapy is a critical but time-consuming task, especially for complex implant configurations. We developed a data-efficient, physics-guided framework for automated multi-catheter digitization with minimal clinical annotation. The pipeline consists of two stages. First, an implant region-aware network was pretrained on synthetic CT volumes with simulated metallic signatures and then fine-tuned using only 10 clinical cases. Second, a s...
  </details>

- **2026-07-13** — Ruoxuan Zhang, Qiyun Zheng, Siyu Wu et al. — [RetroHolmes: When Semantic Plausibility Fails Retrospective Physical Process Reasoning](http://arxiv.org/abs/2607.11044v1)
  <details><summary>📄 Abstract</summary>
  Humans can infer hidden physical processes from sparse observations, yet current evaluation protocols for Vision Language Models fail to assess whether such physical reasoning is genuinely captured. To address this gap, we introduce Retrospective Physical Process Reasoning, a new evaluation paradigm to reason backward from outcomes under explicit physical constraints. Building on the paradigm, we present RetroHolmes, the first real-world benchmark for Retrospective Physical Process Reasoning, co...
  </details>

- **2026-07-13** — Jin-Kang Guo, Jia Li, Jin-Lei Wu et al. — [Non-Abelian holonomic transformations in digitally coupled acoustic waveguides guided by the global adiabatic criterion](http://arxiv.org/abs/2607.11000v1)
  <details><summary>📄 Abstract</summary>
  An acoustic platform is validated for implementing compact non-Abelian holonomic transformations (NHTs) guided by a global adiabatic criterion (GAC). A tripod model is mapped onto a digitally coupled four-waveguide structure, where designed coupling envelopes and an acoustically-induced-transparency phase-control module implement a two-stage phase-stitched holonomic evolution. Compared with a reference Gaussian envelope, the GAC-guided power-law profile flattens the spatial distribution of the g...
  </details>

- **2026-07-13** — Zheng Zeng, Deepak Sridhar, Nuno Vasconcelos — [MED-DSLC: Multi-Expert-Domain Classification via Domain Supervision and Logit Calibration](http://arxiv.org/abs/2607.10985v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) such as CLIP enable zero-shot classification by comparing image features with text prompts in a shared embedding space. A fundamental property underlying this capability is the global comparability of logits across arbitrary candidate classes. However, VLMs are often adapted to fine-grained domains using techniques such as LoRA. While this improves in-domain accuracy, out-of-domain accuracy degrades. This leads to a highly fragmented model ecosystem, with thousands ...
  </details>

- **2026-07-12** — Saadeldine Eletter, Owais Aijaz, Preslav Nakov — [Trust Before Fusion: QIMG-7 and Source-Aware Resolution for Polluted Multimodal RAG](http://arxiv.org/abs/2607.10798v1)
  <details><summary>📄 Abstract</summary>
  Multimodal retrieval-augmented generation (RAG) is often evaluated with clean evidence, yet real retrieval can return topically relevant but unreliable content: false text and misleading images from corrupted metadata, entity swaps, typographic overlays, semantic edits, adversarial patches, blends, or style transfer. We introduce QIMG-7, a controlled benchmark for multimodal retrieval pollution in multi-sentence factual QA, spanning four datasets, seven image-attack families, and 16 paired clean...
  </details>

- **2026-07-12** — Tong Nie, Yuewen Mei, Junlin He et al. — [World Models as Adversaries: Multi-Agent Self-Play Fine-Tuning for Robust Motion Planning](http://arxiv.org/abs/2607.10630v1)
  <details><summary>📄 Abstract</summary>
  Robust motion planning in dense traffic requires autonomous vehicles to interact in rare and safety-critical scenarios that are underrepresented in naturalistic driving data. Although adversarial training offers a feasible solution, existing methods often rely on external scenario generators, heuristic perturbations, or simulator-heavy rollouts, which makes them difficult to integrate with modern autoregressive planners. Here, we cast adversarially robust planner learning as a constrained min-ma...
  </details>

- **2026-07-12** — Sirine Ayadi, Sándor Daróczi, Stephan Günnemann et al. — [Reliability Scaling Laws for Quantized Large Language Models](http://arxiv.org/abs/2607.10855v1)
  <details><summary>📄 Abstract</summary>
  Quantization is a powerful strategy to build capable and resource-efficient large language models (LLMs) by reducing the bitwidth of the parameters. While quantized LLMs achieve state-of-the-art performance on unperturbed inputs using standard predictive metrics, their performance on perturbed inputs, measured using reliability metrics, remains underexplored, despite its importance for reliable deployment. To address this gap, we first conduct a comprehensive reliability evaluation of quantized ...
  </details>

- **2026-07-12** — Nuo Chen, Qian Wang, Qingyun Zou et al. — [Articulate Intuition or Genuine Analysis? Benchmarking Epistemic Reliability in LLM-as-a-Judge Peer Reviews](http://arxiv.org/abs/2607.10511v1)
  <details><summary>📄 Abstract</summary>
  When an LLM judge calls a peer review analytical and a human committee calls another review high quality, are they tracking the same thing? We argue they are not, and that the difference matters philosophically. We operationalise Kahneman's dual-process theory into a structured rubric for peer review and release Kahneman4Review, a benchmark of 3,563 rated reviews scored along nine theoretically motivated textual dimensions, eight bias diagnostics, and a continuous reasoning-quality score. Three ...
  </details>

- **2026-07-12** — Shrestha Datta, Hongfu Liu, Anshuman Chhabra — [Weight-Adjusted Gradients Reveal Parameter Importance and Failure Modes in LLMs](http://arxiv.org/abs/2607.10803v1)
  <details><summary>📄 Abstract</summary>
  Understanding which parameters are influential in Large Language Models (LLMs) is central to improving their efficiency, reliability, and interpretability. We introduce Weight-Adjusted Gradients (WAG), a simple yet effective approach for estimating parameter importance that explicitly captures the interaction between model weights and first-order gradient information and identifies parameters that disproportionately influence model behavior, such as those responsible for collapse phenomena in LL...
  </details>

- **2026-07-12** — Jinyang Du, Hao Ma, Xiaohu Shi et al. — [LLM-PDESR: Robust PDE Discovery via Subdomain Weighted Residuals and LLM-Guided Symbolic Hypothesis Generation](http://arxiv.org/abs/2607.10546v1)
  <details><summary>📄 Abstract</summary>
  Discovering governing partial differential equations (PDEs) from noisy observational data is a fundamental challenge in scientific machine learning. Traditional symbolic regression (SR) methods often struggle to identify accurate equations within vast combinatorial search spaces, largely due to their inability to incorporate essential domain-specific prior knowledge. Furthermore, reliance on pointwise evaluations and discrete finite differences inherently amplifies high-frequency noise, creating...
  </details>

- **2026-07-12** — Bo Chen — [Quantifying the Sources of Instability in LLM-Based Stance Analysis of Public Discourse](http://arxiv.org/abs/2607.10846v1)
  <details><summary>📄 Abstract</summary>
  Computational social science increasingly relies on automated preprocessing pipelines -- speaker diarization, ASR transcript cleaning, sentence segmentation -- to convert raw media into analyzable text. When these pipelines produce different outputs from the same input, two distinct sources of instability can arise: the preprocessing pipeline itself (diarization method, segmentation rules) and the downstream measurement instrument (LLM annotation vs.\ keyword lexicon). Using 256 YouTube intervie...
  </details>

- **2026-07-12** — Chunmei Wang, Shangyou Zhang — [Solving the Stokes Equations via a Least Squares Weak Galerkin Method](http://arxiv.org/abs/2607.10831v1)
  <details><summary>📄 Abstract</summary>
  We present a least-squares weak Galerkin (LS-WG) finite element method for solving the Stokes equations on arbitrary polygonal and polyhedral meshes. By utilizing discrete weak derivatives on discontinuous polynomial spaces, the proposed framework naturally accommodates complex domain geometries and general partitions. Crucially, this least-squares formulation bypasses the traditional inf-sup (LBB) compatibility condition, transforming the standard indefinite saddle-point problem into an inheren...
  </details>

- **2026-07-12** — Stefano Bannò, Penny Karanasou, Mengjie Qian et al. — [Data Augmentation for L2 English Speaking Assessment using TTS](http://arxiv.org/abs/2607.10790v1)
  <details><summary>📄 Abstract</summary>
  Automated assessment of second language (L2) speaking proficiency relies on large-scale annotated speech data, which remains scarce compared to widely available written learner corpora. A promising direction for addressing this imbalance is to use text-to-speech (TTS) and voice cloning to convert written L2 production into synthetic speech. However, written and spoken L2 differ fundamentally: spontaneous speech includes disfluencies and discourse markers, while writing is more planned and comple...
  </details>

- **2026-07-12** — Yongchang Fu, Xinjie Huang, Chengjun Dai et al. — [Opti-Agent-Bench: Benchmarking End-to-End Optimization R&D Agents on Real-World Business Problems](http://arxiv.org/abs/2607.10768v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are increasingly deployed to solve optimization problems, yet existing benchmarks evaluate them on pre-structured mathematical formulations that bypass the most critical challenge: translating complex business requirements into correct models and solve efficiently. We introduce Opti-Agent-Bench, an end-to-end benchmark that evaluates Large Language Models (LLMs) across the complete optimization R&D pipeline, from understanding business-language descriptions through mathematical ...
  </details>

- **2026-07-12** — Venkatesha Matam, Keon Kim — [MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference](http://arxiv.org/abs/2607.10582v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents accumulate heterogeneous context, including system instructions, plans, user turns, retrieved documents, tool outputs, and intermediate reasoning, whose key-value (KV) cache can become a major memory bottleneck. Existing eviction policies generally apply the same attention- or recency-based rule to every token, ignoring semantic structure already available to the agent orchestrator.   We introduce MemDecay, a training-free, region-aware KV-cache eviction policy....
  </details>

- **2026-07-12** — Xiyu Wei, Qingwei Zong, Zhuocheng Yu et al. — [UNIBROWSE: A Data-to-Agent Framework for Multimodal BrowseComp](http://arxiv.org/abs/2607.10557v1)
  <details><summary>📄 Abstract</summary>
  Multimodal BrowseComp tasks require agents to combine perception, tool use, and long-horizon reasoning over dynamic web content, challenging their ability to handle compositional structure, open-world uncertainty, and multimodal integration across extended interactions. Crucially, real-world multimodal browsing involves three distinct information-flow patterns: text-only, image-to-text, and text-to-image, yet existing data construction methods cover only the text-only and image-to-text patterns,...
  </details>

- **2026-07-11** — Rongping Zhou, Omid Tavallaie, Shuaijun Chen et al. — [Measure the Sim-to-Real Gap: Designing an Affordable Real-World Benchmark Platform for Reinforcement Learning in AIoT Systems](http://arxiv.org/abs/2607.10309v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) is commonly employed to enhance the performance of autonomous systems, including the Autonomous Internet of Things (AIoT). However, the trial-and-error nature of RL, when conducted in real-world environments, is costly and hazardous in some scenarios. Consequently, the majority of RL research is conducted in simulation. This reliance introduces challenges related to the Sim-to-Real transferability. Evaluating the Sim-to-Real algorithmic robustness and the Sim-to-Real ...
  </details>

- **2026-07-11** — Jinglan Gong, Jiefan Lu, Hewei Guo et al. — [Enjoy Your Talk: A Human-Centered Benchmark for Multi-Turn Dialogue with Decoupled User Simulation, Target Modeling, and Judging](http://arxiv.org/abs/2607.10428v1)
  <details><summary>📄 Abstract</summary>
  Evaluating large language models (LLMs) as multi-turn conversational partners requires probing capabilities that single-turn benchmarks miss: persona consistency, evolving intent tracking, emotional dynamics, and goal completion. We introduce EYT-Bench, a human-centered benchmark built around a three-party decoupled design: a persona-grounded user simulator, a target model that separates intent perception from response generation, and an independent third-party LLM judge with optional multi-judg...
  </details>

- **2026-07-11** — Francesco Di Salvo, Shyam Nandan Rai, Hamed Damirchi et al. — [Vertical Fusion: Condensing Internal Representations for Robust ViT Classification](http://arxiv.org/abs/2607.10391v1)
  <details><summary>📄 Abstract</summary>
  Despite exposing rich intermediate representations, Vision Transformers (ViTs) are almost exclusively utilized as black-box feature extractors, where only the last layer is considered for downstream tasks. We challenge this convention by introducing the notion of recoverability: the capacity of intermediate representations to correct last-layer failures. By evaluating independent classification probes at every model depth across 16 datasets, we observe that intermediate probes correctly classify...
  </details>

- **2026-07-11** — Ruiyan Gong, Yingnan Guo, Junjun Hu et al. — [ABot-N1: Toward a General Visual Language Navigation Foundation Model](http://arxiv.org/abs/2607.10383v1)
  <details><summary>📄 Abstract</summary>
  Visual Language Navigation foundation models aim to unify deep reasoning for grounded spatial decisions with broad versatility for diverse embodied tasks. Current approaches typically achieve this integration via monolithic policies that map observations directly to actions, yet they often suffer from coordinate drift and poor handling of long-tail semantics. Furthermore, these black-box mappings lack interpretability, hindering the simultaneous achievement of generality, robustness, and transpa...
  </details>

- **2026-07-11** — Stefano Trepella, Andrea Ostuni, Mauro Martini et al. — [Navigating the Crowd: Non-linear MPC with Social Forces Dynamics for Human-Aware Robot Navigation](http://arxiv.org/abs/2607.10374v1)
  <details><summary>📄 Abstract</summary>
  Safe and socially compliant navigation remains a fundamental challenge for autonomous robots operating in human-populated environments. Beyond collision avoidance, robots must anticipate human motion and respect personal space to ensure human comfort. Model Predictive Control (MPC) offers a robust alternative to classical and data-driven methods, although its effectiveness strongly depends on accurate human motion prediction and efficient computation. This paper introduces SFM-NMPC, a Social For...
  </details>

- **2026-07-11** — Andrei Kuzmenko, Alexandr Maximenko, Aleksandr Kutsakov et al. — [GigaAM Multilingual: Foundation Model for Underrepresented Languages](http://arxiv.org/abs/2607.10371v1)
  <details><summary>📄 Abstract</summary>
  Despite recent scaling successes, multilingual ASR performance remains highly uneven, with long-tail languages suffering from severe data scarcity. This work addresses the challenge of building robust foundation models for underrepresented Central Asian languages (Kazakh, Kyrgyz, Uzbek). We present GigaAM Multilingual, a Conformer encoder pre-trained on 2M hours of audio using a HuBERT-style objective. Crucially, we introduce a cluster-level data balancing strategy during pre-training and a doma...
  </details>

- **2026-07-11** — Jiatong Zhao, Tengyue Zhang, Yuhan Wang et al. — [Co4ICF: Co-evolving Physics-Informed Surrogate and RL-based Pulse Optimizer for Inertial Confinement Fusion](http://arxiv.org/abs/2607.10366v1)
  <details><summary>📄 Abstract</summary>
  Offline-trained surrogates for Inertial Confinement Fusion (ICF) suffer a well-known failure mode that iterative optimizers drive inputs into out-of-distribution (OOD) regions where predictions become unreliable. Here we present Co4ICF, a co-evolving framework that couples a physics-informed surrogate with a PPO-based pulse optimizer. The surrogate is iteratively fine-tuned on policy-induced trajectories, correcting extrapolation errors as the optimizer shifts the input distribution; the optimiz...
  </details>

- **2026-07-11** — Giang Nguyen, Raghav Mehta, Emma A. M. Stanley et al. — [Benchmarking the Robustness of Foundation Models for Mammography under Domain Shift](http://arxiv.org/abs/2607.10358v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are increasingly used as image feature extractors for mammography, but their robustness under external domain shift remains unclear. We benchmark 15 foundation-model backbones across breast density, BI-RADS severity, and cancer status using a unified frozen-backbone linear-probe protocol, training on 3 source datasets and evaluating on 12 task-compatible out-of-distribution (OOD) datasets after label harmonization. Mammography-specific vision-language models (Mammo-FM and MaMA)...
  </details>

- **2026-07-11** — Kang Ding, Zhigui Lin, Hongsong Wang et al. — [PrismAD: Decoupled Planning via Semantic Mixture-of-Planners for End-to-End Autonomous Driving](http://arxiv.org/abs/2607.10336v1)
  <details><summary>📄 Abstract</summary>
  This letter presents PrismAD, a decoupled end-to-end autonomous driving framework based on a Semantic Mixture-of-Planners. Existing planners usually aggregate heterogeneous scene tokens into a coupled representation space, forcing a single planning branch to jointly model agent interaction, road geometry, and driving intention. Such coupling may weaken factor-specific reasoning and obscure the contribution of different planning cues. To address this limitation, PrismAD partitions scene tokens in...
  </details>

- **2026-07-11** — Xuankun Rong, Wenke Huang, Bo Du et al. — [Behavioural Signatures of Risk-Sensitive Decision-Making in Large Language Models](http://arxiv.org/abs/2607.10251v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly used in decision support, it is important to understand whether their choices under uncertainty exhibit stable and interpretable behavioural regularities. Human decision-making combines relatively persistent risk preferences with context-dependent adjustment, yet it remains unclear whether analogous behavioural structure can be observed in LLM-based decision systems. Here we examine this question using a controlled multi-model framework based on n...
  </details>

- **2026-07-09** — Riccardo Revalor, Jalees Rehman, Debjit Pal — [Can We Trust LLM's Logic? Quantifying Uncertainty, Coherence, and Robustness via a Graph-Based Framework](http://arxiv.org/abs/2607.08017v1)
  <details><summary>📄 Abstract</summary>
  Large-Language Models (LLMs) can be prone to flawed and unfaithful reasoning that decoding strategies like Self-Consistency (SC) fail to detect as they evaluate only final-answer agreement while ignoring the logical validity of intermediate steps. This raises three fundamental questions: How can we reliably quantify uncertainty in LLM reasoning? Can semantic, structural, and causal awareness select more faithful reasoning compared to naïve majority voting? and How robust is reasoning topology un...
  </details>

- **2026-07-09** — Yunchao Yao, Zhuxiu Xu, Tianqi Zhang et al. — [DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation](http://arxiv.org/abs/2607.08751v1)
  <details><summary>📄 Abstract</summary>
  Building general-purpose dexterous manipulation policies requires benchmarks that go beyond isolated tasks to systematically evaluate policies across diverse interaction modes, sensory conditions, and robot embodiments. However, existing benchmarks remain limited in task and data diversity, embodiment coverage, or controllable visual variation, hindering studies of cross-task and cross-embodiment generalization. We present DexVerse, a large-scale and modular benchmark for dexterous manipulation....
  </details>

- **2026-07-09** — Siddharth Damodharan, Radhika Gupta, Ali Alshami et al. — [AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam Understanding](http://arxiv.org/abs/2607.08745v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Vision-Language Models, Large Language Models, and Multimodal Large Language Models have improved autonomous driving tasks such as scene understanding, decision making, trajectory prediction, and visual question answering. However, evaluating whether these models can reliably reason about safety-critical incidents remains challenging. To address this gap, we present AUTOPILOT-VQA, an incident-centric visual question answering benchmark for dashcam video understanding. The data...
  </details>

- **2026-07-09** — Ali Larian, Qian Lin, Chang Zong Wu et al. — [Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning](http://arxiv.org/abs/2607.08647v1)
  <details><summary>📄 Abstract</summary>
  As autonomous agents are increasingly deployed across diverse operational contexts, aligning their behavior with human intent demands reward functions that remain robust to such changes rather than overfitting to any single environment. Inverse reinforcement learning (IRL) provides a principled way to infer such objectives from human feedback. However, existing analyses of optimal teaching approaches for IRL focus on single-environment, demonstration-only settings, leaving underexplored how hete...
  </details>

- **2026-07-09** — Qihang Zhang, Lin Li, Luyao Zhang et al. — [Native Video-Action Pretraining for Generalizable Robot Control](http://arxiv.org/abs/2607.08639v1)
  <details><summary>📄 Abstract</summary>
  The advent of video-action models offers a promising path for robot control. Nevertheless, we argue that repurposing video generative models designed for digital content creation is inherently inadequate for physical environments. To bridge this gap, we present LingBot-VA 2.0, a video-action foundation model built from the ground up for embodiment. Four core design principles showcase its evolution from LingBot-VA. (1) Departing from traditional reconstruction-focused VAEs, we introduce a semant...
  </details>

- **2026-07-09** — Qian Jiang, Zhecheng Shi, Jingpu Yang et al. — [OmniFood-Bench: Evaluating VLMs for Nutrient Reasoning and Personalized Health Advice](http://arxiv.org/abs/2607.08423v1)
  <details><summary>📄 Abstract</summary>
  The rapid integration of Large Vision-Language Models (VLMs) into critical infrastructure promises to revolutionize   personalized healthcare and dietary management. However, in the domain of food systems, autonomous agents face a   unique and persistent challenge: the "Systemic Information Asymmetry" between visual appearance and intrinsic   nutritional composition. Existing benchmarks primarily focus on coarse-grained classification tasks, such as food   category recognition, which fail to eva...
  </details>

- **2026-07-09** — Iulia-Maria Udrea, Alexandra Diaconu, Bogdan Alexe — [VSRo-200: A Romanian Visual Speech Recognition Dataset for Studying Supervision and Multimodal Robustness](http://arxiv.org/abs/2607.08112v1)
  <details><summary>📄 Abstract</summary>
  We introduce VSRo-200, the first large-scale dataset for visual speech recognition (lip reading) in Romanian, comprising 200 hours of real-world podcast videos. All samples are annotated with pseudo-labels generated by a fine-tuned Romanian ASR model, while a subset of 100 hours is additionally transcribed by humans, enabling controlled analysis of supervision quality under a unified framework. Building on this dataset, we establish a benchmark for visual speech recognition in low-resource setti...
  </details>

- **2026-07-09** — Yi Zhang, Julia Rayz — [From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs](http://arxiv.org/abs/2607.08009v1)
  <details><summary>📄 Abstract</summary>
  We introduce a Bloom-aligned framework for measuring educational control in Large Language Models (LLMs): the ability to preserve a task's instructional intent while shifting its cognitive demand toward specified learning objectives. We apply this framework to programming tasks in computer science education to study the gap between solving tasks and adapting them for learners. Using revised Bloom's Taxonomy as an operational scale of cognitive demand, we evaluate two intervention settings: gener...
  </details>

- **2026-07-09** — Yixian Zhang, Huanming Zhang, Feng Gao et al. — [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](http://arxiv.org/abs/2607.08448v1)
  <details><summary>📄 Abstract</summary>
  Language-conditioned manipulation requires both precise contact-rich control and robust reasoning over language, scenes, and long horizons. End-to-end Vision-Language-Action (VLA) models provide strong local visuomotor skills, but they are trained on in-distribution task trajectories and often fail under deployment perturbations such as semantic retargeting, goal re-binding, spatial-layout shifts, and unstable local contacts. LLM coding agents provide complementary semantic and compositional rea...
  </details>

- **2026-07-09** — Fabio Tosi, Luca Bartolomei, Matteo Poggi et al. — [ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device](http://arxiv.org/abs/2607.08771v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth estimation has seen remarkable progress through foundation models achieving robust zero-shot generalization, yet their computational demands place them far beyond the reach of embedded and mobile platforms. Lightweight alternatives exist, but have been developed almost exclusively within single-domain, self-supervised paradigms, failing silently under domain shift. We present ZipDepth, a compact monocular depth network that bridges this gap by combining an efficient reparameteriz...
  </details>

- **2026-07-09** — Ruiqi Shen, Chang Liu, Henghui Ding — [SAM-MT: Real-Time Interactive Multi-Target Video Segmentation](http://arxiv.org/abs/2607.08688v1)
  <details><summary>📄 Abstract</summary>
  Modern Video Object Segmentation (VOS) involves tracking and segmenting user-specified targets. While recent approaches have achieved remarkable performance in single-target scenarios, extending them to multi-target settings typically involves replicating the single-target processing for each individual object, resulting in reduced frame rates (FPS) with unbounded latency as target count increases. Built upon Segment Anything 2 (SAM2), we propose SAM-MT, which addresses this by transforming the ...
  </details>

- **2026-07-09** — Teng-Ruei Chen — [Resample or Reroute? Budget-Aware Test-Time Model Selection for Large Language Models](http://arxiv.org/abs/2607.08665v1)
  <details><summary>📄 Abstract</summary>
  Routing among large language models (LLMs) trades response quality against serving cost, motivated by the reported gap between deployed routers and a per-instance oracle. Recent analysis shows that test-time resampling can recover per-instance selection headroom that no single-commit router captures; however, that guarantee holds only under an idealized oracle equipped with correctness labels and an unconstrained budget, neither of which a deployed system has. To the best of our knowledge, no pr...
  </details>

- **2026-07-09** — Tian Li, Thomas E. Collett, Coleman M. Krawczyk et al. — [Disentangling the dark and stellar mass through precise lens modelling of the JWST observation of lensed quasar WFI2033--4723](http://arxiv.org/abs/2607.08576v1)
  <details><summary>📄 Abstract</summary>
  We use high-resolution JWST/NIRCam imaging and measured time delays to model the quadruply imaged quasar WFI2033--4723 with a composite stellar plus dark-matter mass model. We first construct an elliptical power-law baseline model and recover Fermat-potential differences (fpd) consistent with previous HST-based and JWST-based analyses, providing a reference scale for composite modelling. We then replace the total mass profile with a physically motivated decomposition in which the stellar mass fo...
  </details>

- **2026-07-09** — Zongyou Yang, Yinghan Hou, Xiaokun Yang — [When the Judge Changes, So Does the Measurement: Auditing LLM-as-Judge Reliability](http://arxiv.org/abs/2607.08535v1)
  <details><summary>📄 Abstract</summary>
  An LLM-as-judge score can move even when the candidate responses stay fixed, simply because the evaluator has changed. We treat this evaluator-replacement ambiguity as a measurement-validity problem. Across four judgment datasets, we compare two upgrade paths available in practice: scaling Qwen3 dense judges from 1.7B to 32B parameters and moving across MiniMax M2-M2.7 released APIs. The main pattern is that judge upgrades are not interchangeable: only Qwen3 1.7B to 4B gives a robust adjacent ga...
  </details>

- **2026-07-09** — Carlos Garcia-Hernandez, Aymane Abdali, Guangyu Wu et al. — [Log-Insight: Automating Microservice Incident Diagnosis via Neuro-Symbolic Log Analysis](http://arxiv.org/abs/2607.08529v1)
  <details><summary>📄 Abstract</summary>
  Diagnosing production incidents in large-scale microservice systems is time-critical for Site Reliability Engineers (SREs). A single 30-minute incident window in our deployment can generate over two million log lines--approximately 1.2 billion characters, far exceeding standard LLM context windows--making direct LLM-based Root Cause Analysis (RCA) infeasible. Existing approaches leave gaps: template-based parsers lack semantic anomaly reasoning, deep-learning detectors emit black-box binary sign...
  </details>

- **2026-07-09** — Ashit Kumar Subudhi, Bhargav Chirumamilla, Shubham Vaishnav et al. — [ADORN: Adaptive Drift handling for Open RAN using Reinforcement Learning](http://arxiv.org/abs/2607.08443v1)
  <details><summary>📄 Abstract</summary>
  Dynamic traffic variations in Open Radio Access Networks (O-RAN) lead to drift, which degrades the performance of Artificial Intelligence/Machine Learning (AI/ML) models. Traditional retraining approaches maintain forecasting accuracy but incur high computational cost and may lead to violations of Service Level Agreements (SLAs). This work proposes a Q-learning-based adaptive retraining approach that formulates the retraining decision as a Markov Decision Process (MDP), where a Reinforcement Lea...
  </details>

- **2026-07-09** — Thibaud Ardoin, Semira Einsele, Evis Bregu et al. — [Prompt Compression via Activation Aggregation](http://arxiv.org/abs/2607.08399v1)
  <details><summary>📄 Abstract</summary>
  Large language models process prompts by propagating activations through dozens of layers before generating a response. We ask whether the task-relevant information contained in an instruction prompt can be compressed into a single activation vector and re-injected into the model, replacing the original token sequence? We show this is achievable using a learned weighted sum of activations extracted at an intermediate layer and injected at an early layer of the target LLM. The compressed vector p...
  </details>

- **2026-07-09** — Siddhartha Jain, Ameya Velingker — [Understanding Axes of Difficulty For Long Context Tasks Via PredicateLongBench](http://arxiv.org/abs/2607.08284v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated rapidly improving long-context capabilities, prompting a wave of benchmarks designed to evaluate them. However, existing long-context evaluations - from Needle-in-a-Haystack (NIAH) tests to more recent multi-hop reasoning and summarization tasks - predominantly measure average-case performance, and many are either saturated or lack robustness. Notably absent is a systematic way to probe how models perform as we scale up the difficulty of tasks along...
  </details>

- **2026-07-09** — Miseong Shawn Kim — [Compete Then Collaborate: Frontier AI Teachers Build a Verifiable Curriculum to Improve a Coding Student Beyond Imitation](http://arxiv.org/abs/2607.08255v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly serve as teachers generating training data for smaller students. Prior multi-teacher knowledge distillation methods merge outputs without determining which frontier model teaches best, often relying on an LLM judge biased toward its own outputs. We introduce a compete-then-collaborate framework where four frontier AI teachers (Claude, Codex-GPT, Grok, Gemini) are ranked head-to-head by an execution-based judge (unit tests and stdin-stdout checks) with fairness ...
  </details>

- **2026-07-09** — Mengchen Li — [AutoPersonas: A Multi-Timescale Loop Engine for Open-Ended Persona Evolution](http://arxiv.org/abs/2607.08252v1)
  <details><summary>📄 Abstract</summary>
  Long-term persona agents must remain identifiable while adapting to new events, relationships, evidence, and social conditions. We identify self-locking as a runtime failure mode in continuing persona-life loops: locally plausible events keep appearing while the generated life collapses toward familiar environments, weak relationships, suspended decisions, and stale life stages. We trace this failure to model-level convergence toward high-probability behavioral channels and system-level context ...
  </details>

- **2026-07-09** — Yifan Wang, Zhixiang Hao, Yu Wang et al. — [Multimodal 3D LUT Generation via StatLUT with Statistical Features for Photorealistic Style Transfer](http://arxiv.org/abs/2607.08227v1)
  <details><summary>📄 Abstract</summary>
  Photorealistic Style Transfer (PST) aims to transfer the color and tonal style of a reference to a content image while strictly preserving its structural integrity. However, existing deep learning-based methods inherently suffer from semantic entanglement caused by pre-trained image encoders, leading to unnatural spatial distortions. Moreover, current pixel-level mapping paradigms often ignore color gamut topology, resulting in color banding, while also lacking the multimodal capability for intu...
  </details>

- **2026-07-09** — Chris Xing Tian, Chengkai Wu, Ziyu Wang et al. — [LUMI: Tokenizer-Agnostic LLM-Based Lossless Image Compression](http://arxiv.org/abs/2607.08221v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based lossless image compression methods typically represent pixel data through the native text interface of a pretrained model, converting pixel values into token sequences that the LLM processes through its vocabulary head. This design shows that pretrained language models can provide probability estimates for image coding, but it also couples compression to tokenizer behavior, vocabulary-specific numeric tokens, and model-family-specific adaptation. In this paper, w...
  </details>

- **2026-07-09** — Sarthak Kumar Maharana, Shambhavi Mishra, Yunbei Zhang et al. — [Continual Test-Time Adaptation in Computer Vision: Methods, Benchmarks, and Future Directions](http://arxiv.org/abs/2607.08164v1)
  <details><summary>📄 Abstract</summary>
  Deep neural nets achieve remarkable performance when training and test data share the same distribution, but this assumption frequently breaks in real-world deployment, where data undergoes continual distributional shifts. Continual Test-Time Adaptation (CTTA) addresses this challenge by adapting pretrained models to non-stationary target distributions on-the-fly, without access to source data or labeled targets, while mitigating two critical failure modes: catastrophic forgetting of source know...
  </details>

- **2026-07-09** — Sokea Sang, Leanghok Hour, Dongmin Kim et al. — [Adaptive Qubit Freezing Enables Robust Graph Partitioning for Divide-and-Conquer QAOA](http://arxiv.org/abs/2607.08138v1)
  <details><summary>📄 Abstract</summary>
  Divide-and-conquer variants of the Quantum Approximate Optimization Algorithm (QAOA) provide a promising route for executing combinatorial optimization problems beyond the qubit capacity of near-term quantum devices. However, existing approaches rely on the existence of small vertex separators and fail entirely on dense or highly connected graphs where such decompositions do not exist. We introduce Frozen Large Graph Partitioning (FrozenLGP), an adaptive decomposition framework that transforms p...
  </details>

- **2026-07-09** — Jun Nie, Yonggang Zhang, Jun Song et al. — [TTHE: Test-Time Harness Evolution](http://arxiv.org/abs/2607.08124v1)
  <details><summary>📄 Abstract</summary>
  The behavior of an LLM agent is determined not only by the underlying model, but also by its harness: the executable program that constructs context, invokes tools, verifies intermediate results, and recovers from failures. Existing approaches optimize such harnesses before deployment, searching training or development data for a fixed agent workflow that is then frozen at test time. This limits adaptation when the test distribution, failure modes, or tool interactions differ from those seen dur...
  </details>

- **2026-07-09** — Jhih-Rong Guo, Bi-Cheng Yan, Tien-Hong Lo et al. — [COALA: Robust Contextualized Speech-augmented Language Modeling for ASR via Contrastive Regularizer and Biasing Score Estimation](http://arxiv.org/abs/2607.08117v1)
  <details><summary>📄 Abstract</summary>
  Contextual biasing seeks to integrate external knowledge into automatic speech recognition (ASR) systems to accurately recognize domain-specific entities. In this paper, we propose COALA (Contextualized ASR Leveraging Biasing Scoring), a robust framework designed to enhance speech-augmented language models (SLMs) in complex multi-entity scenarios. Considering the inherent context-window limitations of SLMs, identifying relevant target entities from a large-scale biasing list is crucial for effec...
  </details>

- **2026-07-08** — A. Sayyad, J. Emmons, S. Jones et al. — [A Reliability Assessment of LALM Audio Judges for Full-Duplex Voice Agents](http://arxiv.org/abs/2607.07985v1)
  <details><summary>📄 Abstract</summary>
  We report the empirical reliability of Gemini models as audio judges that score full-duplex agent conversations directly from the raw stereo waveform, tested across three models in the Gemini family: 2.5 Flash, 3.5 Flash, and 3.1 Pro. Our primary evidence base uses Gemini 2.5 Flash as the ground-truth model, validated against three calibrated human raters on 209 stereo sessions, scored on 8 production dimensions: 152 full-duplex conversations across 13 accent-and-condition strata, together with ...
  </details>

- **2026-07-08** — Alessandro Canevaro, Hang Yu, Julian Schmidt et al. — [Shift & Drift: A Zero-Shot Benchmark for Generalizable and Robust Autonomous Driving Motion Planning](http://arxiv.org/abs/2607.07844v1)
  <details><summary>📄 Abstract</summary>
  While closed-loop motion planners trained on large-scale, object-level datasets, e.g., nuPlan, demonstrate strong in-distribution (ID) performance, their generalization to novel urban topologies and recovery mechanisms following execution perturbations remain under-explored. To address this, we present Shift & Drift, a novel dual-track benchmark designed to rigorously stress-test motion planners across two critical axes of distribution shift: (1) The Semantic Shift Track leverages a novel conver...
  </details>

- **2026-07-08** — Nobin Sarwar, Shubhashis Roy Dipta, Zheyuan Liu et al. — [Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of Methods, Datasets, and Benchmarks](http://arxiv.org/abs/2607.07907v1)
  <details><summary>📄 Abstract</summary>
  With the growing adoption of VLMs, DMs, LLMs, and AFMs, these multimodal foundation models can inadvertently encode sensitive, copyrighted, biased, or unsafe cross-modal associations that originate from their training data. Retraining after deletion requests or policy updates is often impractical, and targeted forgetting remains difficult because knowledge is distributed across shared representations. Multimodal unlearning addresses this challenge by enabling selective removal across modalities ...
  </details>

- **2026-07-08** — Meera Desai, Dallas Card, Abigail Z. Jacobs — [Validating LLMs in social science: Epistemic threats and emerging norms](http://arxiv.org/abs/2607.07915v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are reshaping social science methodology. Researchers increasingly prompt language models to generate quantitative measurements of social concepts, for example labeling data or simulating survey responses. Yet LLMs pose methodological challenges including bias, hallucination, and brittleness across contexts, with unclear threats to validity. Standard practices and norms for addressing these challenges are still emerging. We collect and systematically analyze validati...
  </details>

- **2026-07-08** — Baoyu Li, Xinchen Yin, Mengying Lin et al. — [EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data](http://arxiv.org/abs/2607.08436v1)
  <details><summary>📄 Abstract</summary>
  Egocentric human data offers scalable supervision for robot manipulation. However, behavior cloning entangles transferable content like objects, scenes, and task semantics, with non-transferable factors like human morphology, head motion, and behavioral style. We study whether World Action Models (WAMs) provide a better training signal by requiring policies to predict not only actions, but also how the scene evolves. The central question is what world representation best enables human-to-robot t...
  </details>

- **2026-07-08** — Hari Prasad — [A Transdiagnostic Space of Disorder Like Phenotypes in Reinforcement Learning Agents](http://arxiv.org/abs/2607.07753v1)
  <details><summary>📄 Abstract</summary>
  Modelling psychological disorders in artificial agents offers both a testbed for computational psychiatry and a lens on the failure modes of affective control. Prior work induces one or two disorders in a reinforcement learning (RL) agent by hand-tuned reward shaping, labels the behaviour post hoc, and reports single runs. We recast disorder modelling as dose-controllable manipulation of cognitive appraisal signals in an appraisal-guided PPO agent, expressing seven disorders (anxiety, mania, obs...
  </details>

- **2026-07-08** — Seokhoon Jeong, Mijung Kim, Taehwan Kim — [Agentic Neural Architecture Search](http://arxiv.org/abs/2607.07984v1)
  <details><summary>📄 Abstract</summary>
  Neural architecture search (NAS) methods have grown increasingly efficient, yet they remain bounded by manually engineered search spaces that require substantial domain expertise and must be rebuilt for every new task. Large language models (LLMs) can generate architectures in an open-ended space, but how to optimally divide the labor between LLM-driven design and NAS-driven search remains unexplored. We propose a mechanism that bridges these two paradigms: an LLM produces a high-quality seed ar...
  </details>

- **2026-07-08** — Zhijian Luo, Yangyang Li, Xinyu Luo et al. — [Enhancing Photometric Redshift Estimation for LSST with a Hybrid LSTM-Mixture Density Network](http://arxiv.org/abs/2607.07960v1)
  <details><summary>📄 Abstract</summary>
  Accurate photometric redshift (photo-$z$) estimation and robust uncertainty quantification are essential for the LSST to achieve its precision cosmology goals. Traditional machine learning algorithms are largely restricted to point estimates, struggling to characterize the multimodal nature of redshift PDFs and the degeneracies within the color-redshift space. To address this, we present and validate the LSTM-MDNz architecture, which integrates sequential feature extraction with flexible probabi...
  </details>

- **2026-07-08** — Weizhe Liu, Yunjie Wu, Xiangqian Shu et al. — [DreamCharacter-1: From 3D Generative Foundation Models to Product-Ready Character Generation](http://arxiv.org/abs/2607.07817v1)
  <details><summary>📄 Abstract</summary>
  We present DreamCharacter-1, a lightweight post-adaptation framework that calibrates pretrained 3D foundation models toward high-fidelity, production-ready 3D character generation. Building upon a 3D foundation backbone, our pipeline incorporates three task-oriented components: (1) geometry post-training, which enhances fine-grained surface details through geometric preference optimization; (2) texture post-training, which synthesizes high-resolution textures and refines the appearance of occlud...
  </details>

- **2026-07-08** — Meet Barot, Daniel Berenberg, Sina Khajehabdollahi — [Architecture Generalization with MetaNCA](http://arxiv.org/abs/2607.07743v1)
  <details><summary>📄 Abstract</summary>
  Self-organization is an emergent property of life, driven by the collective behavior of individual components acting on local information. Biological neurons, through local interactions transmitted through synapses, are able to learn efficiently and can adapt their connections over an organism's lifespan. Motivated by these desirable properties of adaptability and local interaction, neural cellular automata (NCA) models have been successful at learning morphogenesis solely through local update r...
  </details>

- **2026-07-08** — Ishaan Batta, Meenu Ajith, Vince Calhoun — [Latent graph encoding of multimodal neuroimaging features with generative AI architectures](http://arxiv.org/abs/2607.07027v1)
  <details><summary>📄 Abstract</summary>
  While generative models enable encoding of complex neuroimaging data for feature generation and reconstruction, developing optimal architectural frameworks with appropriate encoding and latent space processes is crucial for studying structural and functional properties of the brain. We design a multimodal generative framework for structural and functional magnetic resonance imaging (MRI) features through systematic evaluation of encoding strategies, latent multimodal fusion, and generative model...
  </details>

- **2026-07-08** — Lipu Zhou, Yaoyun Kang, Junxiang Pang et al. — [GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM](http://arxiv.org/abs/2607.07452v1)
  <details><summary>📄 Abstract</summary>
  Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoidance, rely primarily on accurate spatial geometry rather than photorealistic rendering. This observation raises a natural question: Is it feas...
  </details>

- **2026-07-08** — Jinbo Yang, Mingyue Yuan, Boyuan Zhang et al. — [HPG-Diff: Hierarchical physics-guided diffusion with differentiable connectivity constraints for topology optimization](http://arxiv.org/abs/2607.07233v1)
  <details><summary>📄 Abstract</summary>
  Deep generative models offer a promising paradigm for topology optimization, enabling rapid design exploration. However, these approaches lack intrinsic physics guidance, often leading to poor generalizability across unseen boundary conditions and the formation of floating material artifacts. To address these limitations, we propose Hierarchical Physics-Guided Diffusion (HPG-Diff), a novel diffusion framework that enforces physics consistency through two synergistic mechanisms. First, we introdu...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 11 papers

- **2026-07-13** — Ke Xu, Han Xu, Xinran Chen et al. — [STAMP: Provenance-Guided Credit Assignment for Deep Search Agents](http://arxiv.org/abs/2607.11172v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for deep-search agents has largely focused on trajectory-level scoring -- outcome correctness, citation-aware rewards, and evidence coverage. Yet the actions that expose supporting documents receive no targeted credit, a gap we call the reward-credit mismatch. We propose STAMP, in which a reference-based verifier judges whether each cited document supports an entity or relation in a training-time evidence graph, and first-exposure attribution traces each supported citation...
  </details>

- **2026-07-12** — Obada Kraishan, Kulsawasd Jitkajornwanich, Kerk Kee — [Robo-Reporters: Evaluating Autonomous AI Agents as Algorithmic Gatekeepers in Computational Journalism](http://arxiv.org/abs/2607.10736v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence agents increasingly perform journalism tasks autonomously, searching for sources, evaluating credibility, and producing news content with minimal human oversight. Yet research has largely treated AI as a monolithic category, leaving the effects of architectural design unexamined. Drawing on gatekeeping theory, this study presents the first systematic comparison of four agent architectures, monolithic (Claude), chain-based (LangChain), multi-agent collaborative (CrewAI), a...
  </details>

- **2026-07-12** — Xutao Mao, Liangjie Zhao, Leyao Wang et al. — [Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents](http://arxiv.org/abs/2607.10526v1)
  <details><summary>📄 Abstract</summary>
  Stateful personal agents increasingly maintain long-term user profiles, episodic memories, and reusable skills. This persistence turns conversational sycophancy into a state-writing failure: accepted user-centric claims can be committed as lasting preferences, background facts, or workflows and later reused after the original conversation is gone. We call this persistent sycophancy and introduce the Personal Agent Sycophancy Benchmark (PASB), a 1,600-task benchmark that traces whether a conversa...
  </details>

- **2026-07-12** — Muhammad Awais Bin Adil, Saad Aamir — [modelDNA: Calibrated Lineage Verification and Merge Decomposition from Sampled Weight Fingerprints](http://arxiv.org/abs/2607.10617v1)
  <details><summary>📄 Abstract</summary>
  The lineage graph of open-weight language models is self-reported: Hugging Face's base_model metadata field is optional and unverified, and over 60% of Hub models document no parentage at all. Methods for detecting lineage from weights exist in the research literature, but each ships as paper code tied to one signal and one experiment; when a provenance dispute breaks, the analysis is redone by hand. This report describes modelDNA, a tool that fingerprints a model from roughly 100-300 MB of rang...
  </details>

- **2026-07-11** — Tomas Bruckner — [One Token Is Enough: Fingerprinting and Verifying Large Language Models from Single-Token Output Distributions](http://arxiv.org/abs/2607.10252v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly consumed through opaque serving chains - API aggregators, resellers, and inference providers - in which the client has no technical means to confirm that the model answering is the model advertised, and recent audits show that a substantial fraction of commercial endpoints deviate from the vendor's reference weights. Existing identification techniques require long generated texts, token-level log-probabilities, adversarially crafted prompts, or the m...
  </details>

- **2026-07-11** — Kyoungmin Kim, Anastasia Ailamaki — [Confining Nondeterminism: AI-Driven Research Systems as DBMSs for Reliable, Non-Wasteful, Transparent, and Collaborative Research [Vision]](http://arxiv.org/abs/2607.10508v1)
  <details><summary>📄 Abstract</summary>
  LLM agents that conduct research (proposing ideas, writing and running code, analyzing results) can already carry a study from research question to figures, yet cannot be fully trusted. The same question asked twice in a row returns different answers; the agent announces a number that no execution produced, and tool use does not prevent this, because nothing binds what the agent reports to what its tools returned; a small upstream change leaves downstream results silently stale, with no way to l...
  </details>

- **2026-07-09** — Ethan Leung, Elias Lumer, Corey Feld et al. — [Do You Need a Frontier Model as a Citation Verifier? Benchmarking Rubric LLMs for Deep-Research Source Attribution](http://arxiv.org/abs/2607.08700v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning increasingly relies on an LLM judge to score each rubric criterion, and that judge acts as the reward model during training. Before such a signal can be trusted, we need to know how capable the judge must be and how biased it is. We study this calibration question for citation quality in deep-research systems, where a search-grounded LLM must support each claim it writes with a cited source. Citation quality is a structured rubric task in which each attribution-citation pa...
  </details>

- **2026-07-09** — Adis Alihodzic, Selma Skopljakovic Hubljar — [SHAP-Weighted Cross-Modal Expert Fusion for Emotion and Sentiment Recognition: Evidence and Limits](http://arxiv.org/abs/2607.08573v1)
  <details><summary>📄 Abstract</summary>
  Multimodal emotion and sentiment recognition is commonly addressed by early fusion, which concatenates modalities before classification, or late fusion, which combines independently trained unimodal predictors. Early fusion can be accurate but monolithic, while late fusion is modular but may lose cross-modal interactions. This paper revisits XAI-guided adaptive fusion (\xgaf), a tree-based mixture of unimodal and cross-modal experts whose sample-level weights are derived from TreeSHAP attributio...
  </details>

- **2026-07-09** — Javier Izquierdo, Aygul Zagidullina — [Applying JEPA-Style Predictive Learning to JA4-Derived Network Fingerprints](http://arxiv.org/abs/2607.08465v1)
  <details><summary>📄 Abstract</summary>
  I-JEPA and V-JEPA learn by matching latent predictions to target encoder outputs rather than regenerating the original input, and this has worked well for images and video. We explore whether the same objective works for compact network fingerprints. We built JA4-JEPA, a Transformer-based model trained on JA4, JA4H, JA4S, and JA4X subfields drawn from JA4DB and CIC-IDS- 2017. The training data combines roughly 397K samples from both sources, though no single sample contains all four view familie...
  </details>

- **2026-07-08** — Yufei Xia, Anjun Gao, Yueyang Quan et al. — [Who Broke the System? Failure Localization in LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2607.07989v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) based multi-agent systems enable complex problem solving through coordinated reasoning and action, but their distributed structure also introduces new challenges in diagnosing system-level failures. When an execution fails, identifying which agent is responsible and at what point the trajectory first becomes irreversibly misdirected is difficult due to long-horizon interactions and tightly coupled agent behaviors. In this paper, we study the problem of failure localiza...
  </details>

- **2026-07-08** — Gospel Bassey, Vincent Fakiyesi — [Nigeria Machinery: A Low-Resource Industrial Dataset with a Domain-Grounded Reasoning Layer](http://arxiv.org/abs/2607.07883v1)
  <details><summary>📄 Abstract</summary>
  There is relatively little, public, and model-ready data on industrial machinery for African economies. This makes it hard to do quantitative analysis or to train language models on numeric tasks grounded in that setting. We release two things to help with part of this problem. The first is the Nigeria Machinery Usage and Failures Dataset: 89 machine-level records across 28 indicators, covering Nigeria's manufacturing and oil and gas sectors from 2006 to 2025. Every record names a public source ...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-07-13** — Chenxi Sun, Minghui Liwang, Wusi He et al. — [HermesHFL: Incentive-Compatible Hierarchical Federated Unlearning for Dynamic LLM Fine-Tuning](http://arxiv.org/abs/2607.11528v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical federated unlearning (HFUL) for large language model (LLM) fine-tuning faces significant challenges due to hierarchical aggregation, dynamic client participation, and strong parameter coupling in LLM adaptation. Selectively removing client contributions is particularly difficult because model updates propagate across multiple aggregation stages while unlearning requests may coincide with client departures and rejoining. To address these issues, we propose **HermesHFL**, a hierarchic...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 6 papers

- **2026-07-13** — Chunzheng Zhu, Lei Tian, Bohan Tan et al. — [The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy](http://arxiv.org/abs/2607.11175v1)
  <details><summary>📄 Abstract</summary>
  The growing ability of large language models and vision language models to jointly interpret and reason over images and text is reshaping medical agents, moving them from task specific predictors toward autonomous systems that perceive, reason, plan, remember, and act in clinical environments. This work departs from the capability first perspective of existing literature and instead begins from clinical deployment, asking what tasks, contamination resistant benchmarks, and interactive training e...
  </details>

- **2026-07-13** — Zhengyang Bai, Cheng Chen, Fan Yang et al. — [Many-Body Physics with Rydberg Atoms: Quantum Simulation and Non-equilibrium Dynamics](http://arxiv.org/abs/2607.11038v1)
  <details><summary>📄 Abstract</summary>
  Rydberg atoms, characterized by their strong and long-range dipole-dipole interactions, provide a versatile platform for exploring intriguing collective and many-body effects. Recently, the experimental realization of these effects in dense ensembles and reconfigurable atomic arrays has attracted significant interest, particularly for applications in quantum simulations and non-equilibrium physics. This review focuses on such recent development, discussing the theoretical foundations of the inte...
  </details>

- **2026-07-12** — Robert Wijaya, Ngai-Man Cheung — [Mixture of Cognitive Experts in Large Vision-Language Models](http://arxiv.org/abs/2607.10796v1)
  <details><summary>📄 Abstract</summary>
  Large Vision Language Models (LVLMs) require strong reasoning over both visual and textual input. Recent work suggests that cognitive elements, especially diverse representations and metacognition, correlate with better performance. Many of the needed perceptual functions are already provided by specialized domain-specific computer vision models, which act as the perceptual subsystem for detecting objects, localizing them, inferring states, recovering spatial layout, and reading text. The key ch...
  </details>

- **2026-07-12** — Yu Fu, Jiawei Zhou, Sichen Jin et al. — [How Data Narratives Go Wrong: A Taxonomy of Issues Across the Data Communication Process](http://arxiv.org/abs/2607.10523v1)
  <details><summary>📄 Abstract</summary>
  Data narratives increasingly shape public understanding, but their failures are rarely just isolated factual errors or deceptive charts. Instead, they emerge through a broader meaning-making process in which quantitative evidence is transformed into claims, representations, and arguments. While prior work has examined these failures across disparate fields (e.g., statistics, visualization, and fact-checking), the community lacks a holistic lens to explain how these issues arise, propagate, and c...
  </details>

- **2026-07-11** — Cedric Waterschoot, Nava Tintarev, Francesco Barile — [Consensus vs. Dissent: Dynamic LLM Modeling of Subjective Preferences in Group Recommenders](http://arxiv.org/abs/2607.10235v1)
  <details><summary>📄 Abstract</summary>
  Previous work in group recommender systems has demonstrated a sensitivity to the distribution of preferences within a group. Specifically, the selection of the preference aggregation strategy benefits from considering such group configurations. In this paper, we study whether LLMs are able to mimic this sensitivity and to select the ideal aggregation strategy (and corresponding recommendation) according to nuanced human perceptions of fairness, satisfaction, and consensus.   We do this by fine-t...
  </details>

- **2026-07-08** — Arun Malik — [Progressive Crystallization: Turning Agent Exploration into Deterministic, Lower-Cost Workflows in Production](http://arxiv.org/abs/2607.07052v1)
  <details><summary>📄 Abstract</summary>
  AI agents deployed for IT operations are typically permanent cost centers because every execution requires full LLM inference, even for previously solved problems. This paper introduces progressive crystallization, a lifecycle that treats agent exploration as a discovery mechanism rather than a permanent execution model. It defines a three-stage execution taxonomy, from fully agent-orchestrated to hybrid to fully deterministic workflows, together with an evidence-based promotion mechanism that c...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 160 papers

- **2026-07-13** — Nishant Aggarwal, Ayushi Dubal, Sreeraj Kannakarankodi et al. — [Can LLMs Perform Deep Technical Comprehension of Computer Architecture Papers?](http://arxiv.org/abs/2607.11859v1)
  <details><summary>📄 Abstract</summary>
  Can large language models perform deep technical comprehension of computer architecture papers -- not summarization, but structured critique that names the core mechanism, surfaces buried assumptions, and connects a contribution beyond its own scope? We study Gauntlet, an open-source pipeline that analyzes a paper through five independent expert-persona reviewers and an adversarial synthesis stage. On 20 ISCA 2025 and HPCA 2026 papers, ten researchers each wrote their own analyses and then judge...
  </details>

- **2026-07-13** — Ying Yan, Liwei Hu, Xiaoming Zhang — [IG-GAN: A Generative Adversarial Network for Aerodynamic Data Generation Based on Intrinsic Geometry](http://arxiv.org/abs/2607.11497v1)
  <details><summary>📄 Abstract</summary>
  Existing generative models learn data distributions in flat Euclidean space. However, most data in our real world are manifolds embedded in high dimensional Euclidean space. Therefore, we propose an intrinsic-geometry-based generative adversarial network (IG-GAN) for data generation in the field of aerodynamics. The generator of the IG-GAN represents aerodynamic data as a piecewise smooth manifold constructed by Bézier surfaces, and the generator tries to learn the coefficients of each Bézier su...
  </details>

- **2026-07-13** — Zahra Mousavi, Chadni Islam, M. Ali Babar et al. — [Understanding the Impact of AI Code Assistants on Security API Usage: An Empirical Study](http://arxiv.org/abs/2607.11348v1)
  <details><summary>📄 Abstract</summary>
  AI code assistants are transforming software development, but their implications for software security remain a major concern, particularly in the context of security APIs. These APIs are critical for safeguarding software systems, yet their complexity often leads to incorrect use and serious vulnerabilities. Developing an evidence-based understanding of how AI assistants influence developers' use of these APIs is therefore essential for informing effective mitigation strategies. While a few use...
  </details>

- **2026-07-13** — Saba Imran, Debanjum Singh Solanky — [ResearchQA: Benchmarking Citation-Grounded Question-Answering on Scientific Papers](http://arxiv.org/abs/2607.11074v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to assist scientific reading, but existing evaluation methods often fail to detect whether answers are supported by verifiable citations. We introduce ResearchQA, a benchmark of 6,211 single-paper question-answer pairs from 494 open-access papers spanning eight domains and four question types: lookup, comprehension, multi-hop, and adversarial. ResearchQA is designed for citation-grounded evaluation: it permits multiple valid supporting passages for a c...
  </details>

- **2026-07-13** — Amirmahdi Mirfakhar, Maria-Florina Balcan, Hedyeh Beyhaghi — [Efficient Online Proportional Sampling with Applications to Smoothed Online Learning](http://arxiv.org/abs/2607.10963v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of efficient online proportional sampling from a high-dimensional domain under a $σ$-smoothed adversary, where the sampling distribution is induced by a dynamically evolving weight function defined over a sequence of piecewise-structured partitions. This setting captures a broad range of applications, including principal-agent games (e.g., pricing and contract design), and algorithm configuration and parameter tuning. The central challenge is maintaining an efficient data st...
  </details>

- **2026-07-13** — Dian Wang, Jisang Park, Xiaomeng Xu et al. — [Mixture of Frames Policy: Multi-Frame Action Denoising for Bimanual Mobile Manipulation](http://arxiv.org/abs/2607.11884v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation is inherently multi-frame: local actions may be simple in an end-effector frame, while transport, upright-object handling, and whole-body coordination are better represented in a base-aligned frame. However, modern diffusion-based visuomotor policies typically commit to a single predefined action frame, forcing one denoiser to model action distributions that are often unnecessarily complex in that frame. We propose Mixture of Frames Policy (MoF), a diffusion policy that perf...
  </details>

- **2026-07-13** — Shikai Qiu, Marc Finzi, Yujia Zheng et al. — [Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data](http://arxiv.org/abs/2607.11883v1)
  <details><summary>📄 Abstract</summary>
  Compression is fundamental to intelligence. A model that can represent its training data as a short code has discovered regularities that enable generalization. Large neural networks may learn functions far simpler than their parameter counts suggest, but it is challenging to construct codes that realize this simplicity. Parameter-based methods such as quantization produce code lengths that scale with model size, insensitive to how much information the parameters store. Prequential coding bypass...
  </details>

- **2026-07-13** — Giulia Di Fede, Salvatore Andolina — [Supporting Reflection in LLM-based Exploratory Search](http://arxiv.org/abs/2607.11810v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can make exploratory search more efficient but may undermine the reflection and iterative sensemaking needed in unfamiliar domains. Existing LLM tools often prioritize rapid answers over supporting users in tracking how their understanding evolves and how well their strategies align with their goals. We present TrailLM, a system that helps users reconstruct and revisit their exploration paths to support reflection and metacognitive engagement during information seeki...
  </details>

- **2026-07-13** — Seung Hyun Hahm, Minh T. Dinh, SouYoung Jin — [StoryTeller: Training-Free Narrative Grounding for Long-Form Audio Description](http://arxiv.org/abs/2607.11798v1)
  <details><summary>📄 Abstract</summary>
  Long-form audio description (AD) requires more than describing visible actions: it must preserve characters, events, relationships, and story context across scenes so that blind and low-vision (BLV) audiences can follow a film. Modern video-language models (VLMs) are effective on short clips, but they often treat each moment independently, producing descriptions that miss who characters are, why events matter, and how the current scene connects to earlier narrative context. We propose StoryTelle...
  </details>

- **2026-07-13** — Ayoung Lee, Ryan Kwon, Yunxiang Zhang et al. — [MET: Theory-Grounded and Culture-Aware Multilingual Moral Reasoning](http://arxiv.org/abs/2607.11736v1)
  <details><summary>📄 Abstract</summary>
  Language models are increasingly used for moral decision-making across diverse linguistic and cultural contexts, yet existing work overlooks multilinguality on three aspects: 1) multilingual evaluation benchmarks use direct translation, failing to adapt culture-specific items; 2) inference-time methods for moral reasoning rely on static, English-centric scaffolds and lack grounding in moral theory; 3) training methods for moral decision-making typically require expensive supervision from stronge...
  </details>

- **2026-07-13** — Yuanzhi Liang, Xufeng Zhan, Haibin Huang et al. — [From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence](http://arxiv.org/abs/2607.11689v1)
  <details><summary>📄 Abstract</summary>
  Artificial general intelligence ultimately requires agents that can reason and act in the physical world. Action models, vision-language-action policies, and world models have advanced this goal, while World Action Models (WAMs) are particularly promising because they connect candidate interventions with predicted consequences. However, progress remains fragmented: models use incompatible action spaces and prediction targets, datasets and tasks follow different conventions, and runtime systems e...
  </details>

- **2026-07-13** — Nimrod Talmon, Oghenekaro Elem — [Cardano's Voltaire Governance: Complete Specification and Research Program](http://arxiv.org/abs/2607.11601v1)
  <details><summary>📄 Abstract</summary>
  Blockchain governance, the set of processes by which decentralized protocols evolve, remains a fundamental challenge in balancing adaptability, security, and stakeholder representation. This technical report analyzes Cardano's Voltaire governance system, the on-chain framework introduced via CIP-1694 and enacted through the Chang hard fork in September 2024, and lays down a corresponding research program.   We make two contributions. First, we provide a complete technical specification of Voltai...
  </details>

- **2026-07-13** — Milan Brož, Tamara Čierniková, Ondřej Kozina et al. — [Linux disk encryption and self-encrypting drives -- A case study on Opal2 drives security](http://arxiv.org/abs/2607.11563v1)
  <details><summary>📄 Abstract</summary>
  Opal2 self-encrypting drives provide hardware-based disk encryption serving as an additional layer of protection, or a replacement, for software-based solutions. This paper presents a case study of real-world Linux integration of Opal2 drives and the security of Opal2 firmware. The study was conducted on a testbed of 38 commercial off-the-shelf Opal2 drives from various vendors using a black-box approach. We identified several firmware security issues and incompatibilities, which we responsibly ...
  </details>

- **2026-07-13** — Gong Sitong, Tianyu Yan, Caixin Kang et al. — [Vinci2: Providing Proactive Assistance in Continuous Egocentric Videos](http://arxiv.org/abs/2607.11523v1)
  <details><summary>📄 Abstract</summary>
  When should an intelligent assistant speak up without being asked? Continuous egocentric video offers rich, evolving context that enables a new form of assistance: one that is proactive rather than merely reactive. Yet existing approaches either wait passively for user queries or treat every detected event as requiring a response, without considering the user's history, current activity, or whether assistance would actually be welcome. We reframe proactive assistance as a context-dependent decis...
  </details>

- **2026-07-13** — Xue Qin, Sumesh Surendran Letha — [From GUI Tests to Conversational Interaction: A New Perspective on App-Specific Voice Assistants](http://arxiv.org/abs/2607.11387v1)
  <details><summary>📄 Abstract</summary>
  Voice assistants are widely deployed on mobile platforms, yet most are designed as system-level services that remain poorly aligned with application-specific behavior. As a result, enabling voice interaction at the app level requires developers to manually reimplement application logic, leading to high development and maintenance costs.   We propose an LLM-driven approach to automating the development of app-specific voice assistants by repurposing GUI test code, which encodes behavior-preservin...
  </details>

- **2026-07-13** — Yannick Lehmen, Marvin Wyrich, Anna-Maria Maurer et al. — [Predicting Program Comprehension with Foundation Models of Human Cognition](http://arxiv.org/abs/2607.11372v1)
  <details><summary>📄 Abstract</summary>
  Software engineering depends on the ability of developers to understand code, yet predicting how they do so remains an open challenge despite decades of research. Existing approaches rely either on simplified proxy measures that limit accuracy or on non-trivial measurements requiring elaborate experimental setups that are difficult to scale and apply in practice. In contrast, recent work in psychology suggests an alternative perspective: Instead of modeling task-specific phenomena directly, huma...
  </details>

- **2026-07-13** — Miguel Gomez Fernandez, David Castro Boga, Roi Mendez-Rial et al. — [Benchmarking Edge Inference Strategies for Deep Learning Models in Industrial Machine Vision](http://arxiv.org/abs/2607.11356v1)
  <details><summary>📄 Abstract</summary>
  Edge deployment is often the preferred solution for industrial machine vision systems when low latency, data security, or limited connectivity are critical requirements. Several frameworks are available to optimise inference on edge devices; however, relatively few studies have systematically compared their inference-time performance under industrial deployment conditions.   In this work, we present a comparative study of four widely used approaches for machine vision inference in industrial set...
  </details>

- **2026-07-13** — Chenglin Yu, Li Yin, Ying Yu et al. — [Compile, Then Page: Executable SOP Programs and a Capability-Gated Runtime for Procedural LLM Agents](http://arxiv.org/abs/2607.11346v1)
  <details><summary>📄 Abstract</summary>
  Enterprise agents must follow long-horizon, conditional, safety-critical standard operating procedures (SOPs). We compile machine-readable SOP constraints into executable pseudo-code and run them with a program-guided (PG) stack machine that pages the active frame while an LLM performs semantic execution. A three-arm SOPBench study across six models separates representation from runtime: compiled text never significantly hurts and gains up to 16.0 points where official prose underperforms. Runti...
  </details>

- **2026-07-13** — Rodrigo Labouriau — [Markov Properties of $k$-Record Processes via Order Statistics](http://arxiv.org/abs/2607.11283v1)
  <details><summary>📄 Abstract</summary>
  The theory of $k$-record values (Type 2 $k$-records) plays an important role in the study of partial extremes and in statistical inference based on record data. A common approach reduces the analysis of $k$-records associated with a distribution function $F$ to that of ordinary records from the transformed distribution $F_{1:k}(x)=1-(1-F(x))^k$. This representation is widely used to derive distributional and inferential results, often without an explicit construction of the underlying stochastic...
  </details>

- **2026-07-13** — Liqian Feng, Lintao Wang, Xiaochen Liu et al. — [Q-BridgeNet: A Quantization Network for Cross-Lingual Sign Language Translation](http://arxiv.org/abs/2607.11215v1)
  <details><summary>📄 Abstract</summary>
  Most sign language translation (SLT) methods focus on isolated native sign-spoken pairs (e.g., American Sign Language - English). Extending language-specific SLT models to multilingual translation would improve accessibility by enabling communication across diverse sign and spoken language communities. However, existing multilingual SLT approaches still struggle to learn a unified model that minimizes cross-lingual conflicts while capturing shared cross-lingual semantics and preserving language-...
  </details>

- **2026-07-13** — Changlun Li, Peixian Ma, Qiqi Duan et al. — [NextFund: A Unified Performance Tracking Platform for Agentic Portfolio Management](http://arxiv.org/abs/2607.11141v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) based agents are beginning to participate in portfolio construction and market analysis, where decisions must be justified under evolving information and risk constraints. Current assessment practice, however, remains poorly aligned with this setting: many studies rely on static examinations or report only terminal portfolio returns, while the intermediate evidence, analyst judgments, and execution steps that produced those returns stay largely invisible. We introduc...
  </details>

- **2026-07-13** — Sunyoung Jung, Jiwoo Park, Yoonseok Choi et al. — [Controlling Motion Transfer in Diffusion Transformers via Attention Heads](http://arxiv.org/abs/2607.11081v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have advanced video generation with high-quality, temporally coherent results. However, extending them to motion transfer, which requires following reference motion while aligning with a target prompt, remains challenging due to limited understanding of motion and structure representations within DiTs. We analyze video DiTs at the attention-head level and identify distinct heads specialized for motion and spatial structure. Based on this insight, we propose a head-a...
  </details>

- **2026-07-13** — Kimia Hamidieh, Lester Mackey, David Alvarez-Melis — [Domain-Aware Scaling Laws Uncover Data Synergy](http://arxiv.org/abs/2607.11052v1)
  <details><summary>📄 Abstract</summary>
  Machine learning progress is often attributed to scaling model size and dataset volume, yet the composition of data can be just as consequential. Empirical findings repeatedly show that combining datasets from different domains yields nontrivial interactions. For instance, adding code improves mathematical reasoning, while certain mixtures introduce interference that reduces model performance. We refer to these effects collectively as data synergy, where the contribution of multiple domains exce...
  </details>

- **2026-07-13** — Tianjing Zeng, Yuntao Hong, Zhongjun Ding et al. — [QwenPaw-Data: Bridging Facts, Methodology, and Execution for Autonomous Enterprise Data Analytics](http://arxiv.org/abs/2607.11019v1)
  <details><summary>📄 Abstract</summary>
  Enterprise data analysis is emerging as a distinct frontier for autonomous agents. Compared with general-purpose interaction and software engineering, it operates in an open, ambiguous, and continuously evolving environment. These characteristics call for a data-agent architecture that treats semantics, methodology, execution, and evolution as first-class system concerns. To this end, we introduce QwenPaw-Data, an agentic data system designed for enterprise intelligent data analysis. QwenPaw-Dat...
  </details>

- **2026-07-13** — Tingcong Liu, Tongshun Chen, Siyi Ma et al. — [Whole-Body Semantic-to-Actuation Grounding of Elephant-Inspired Soft-Trunk Motion via Lightweight Flow Matching](http://arxiv.org/abs/2607.11018v1)
  <details><summary>📄 Abstract</summary>
  For close-contact human-robot interaction (HRI), trunk-like continuum manipulators provide a physical channel for diverse whole-body expression, but grounding open-vocabulary responses into such robots is difficult: end-effector motion underspecifies body shape, whereas direct whole-body commands are high-dimensional and hard to keep feasible. We propose a whole-body semantic-to-actuation grounding framework for elephant-inspired soft-trunk HRI based on lightweight flow matching. The framework c...
  </details>

- **2026-07-13** — Hao Xu, Xinyu Wei, Sam Wells et al. — [Temporal Feature Distillation for Label-Efficient Precise Event Spotting in Sports Videos](http://arxiv.org/abs/2607.10998v1)
  <details><summary>📄 Abstract</summary>
  Precise Event Spotting (PES) requires distinguishing visually similar yet semantically distinct adjacent frames, making it fundamentally different from image classification and coarse action recognition. Although self-distillation methods such as DINO have shown strong representation learning ability in images, we find that directly applying them to PES is ineffective: without supervised guidance, subtle but crucial motion cues are often suppressed as noise, leading to representations that are i...
  </details>

- **2026-07-13** — Ali Ahmadi, Hamed Rahimi, Adrien Jacquet Cretides et al. — [Think When It Matters: Conditional VLM Reasoning for Social Navigation with RL Policies](http://arxiv.org/abs/2607.10991v1)
  <details><summary>📄 Abstract</summary>
  As mobile robots become more integrated into everyday human environments, social robot navigation is becoming essential for ensuring human comfort, safety, and trust. While reinforcement learning (RL) navigation policies provide the fast inference and reactive behavior necessary for real-time deployment, they still lack flexible semantic reasoning capabilities and often fail to generalize to complex social scenarios. Recent approaches have increasingly turned to vision-language models (VLMs) in ...
  </details>

- **2026-07-13** — Yunhai Feng, Natalie Leung, Jiaxuan Wang et al. — [A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation](http://arxiv.org/abs/2607.11874v1)
  <details><summary>📄 Abstract</summary>
  Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires delicate regulation of contact modes and forces. We present REGRIND, a minimalist retargeting-guided RL pipeline that learns dexterous manip...
  </details>

- **2026-07-13** — Sheng Xu, Boyuan Huang, Ke Jia et al. — [Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results](http://arxiv.org/abs/2607.11183v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly operate as tool-using agents, where small format, argument, or function-call errors can invalidate otherwise plausible responses. We study inference-time feed-forward network (FFN) intervention for improving structured outputs without retraining model weights. Our project began with Orthogonal Residual Projection (ORP), a direction-changing repair attempt that revealed sensitive SwiGLU FFN intervention sites but often caused more harm than fixes. We therefore p...
  </details>

- **2026-07-13** — Hengyuan Hu, Priya Sundaresan, Jensen Gao et al. — [VIA: Visual Interface Agent for Robot Control](http://arxiv.org/abs/2607.11119v1)
  <details><summary>📄 Abstract</summary>
  Robot manipulation is a complex task that requires visual understanding, physical reasoning, planning, and closed-loop control. General-purpose foundation models (FMs) have grown remarkably capable of some of these, especially vision and reasoning. To leverage this for generalist robot policies, current methods typically involve converting existing FMs into vision-language-action (VLA) models by fine-tuning on robot data to output low-level actions. However, VLAs are often orders of magnitude sm...
  </details>

- **2026-07-13** — Tiberiu Musat, Tiago Pimentel, Nicholas Zucchet et al. — [Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks](http://arxiv.org/abs/2607.11875v1)
  <details><summary>📄 Abstract</summary>
  We present a theoretical framework to explain the emergence of inductive reasoning abilities in Transformer language models. While previous works on Transformer learning dynamics have so far been mostly tied to specific tasks, we study a generalized class of inductive tasks that unifies several synthetic tasks known in the literature, including in-context n-grams and multi-hop reasoning. In this class, we theoretically prove that the training dynamics of attention models can be confined to a hig...
  </details>

- **2026-07-13** — Zixiang Xu, Sixian Li, Huaxing Liu et al. — [Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias](http://arxiv.org/abs/2607.11871v1)
  <details><summary>📄 Abstract</summary>
  Existing studies of LLM-as-judge scoring bias work predominantly at the input-output level: they perturb inputs, measure score deltas, and propose prompt-level mitigations. We argue that the same biases admit a representation-level account in the judge's hidden state, complementary to the input-output view and operationally useful in ways it does not afford. We report three findings, across seven judges, seven bias types, and nine benchmarks. Geometry: baseline judging inputs occupy a tight acti...
  </details>

- **2026-07-13** — Francesco Sorrenti, Erick Pastén, Leonardo Giani — [Reconstructing the kinematics of Laniakea using Type Ia Supernovae](http://arxiv.org/abs/2607.11860v1)
  <details><summary>📄 Abstract</summary>
  We develop a kinematic framework that relates the monopole, dipole, and quadrupole of the luminosity distance to an ellipsoidal peculiar velocity field describing the dynamics of the Laniakea supercluster. By properly accounting for the transformations between the CMB and Laniakea reference frames and selecting Type Ia supernovae within the volume associated with the superstructure, we show that luminosity distance multipoles encode the expansion and shear of the local velocity field. This allow...
  </details>

- **2026-07-13** — Yu-Han Huang, Chih-Kai Yang, Ke-Han Lu et al. — [Encoder-Side Neuron Identification and Amplification for Acoustic Perception in Large Audio-Language Models](http://arxiv.org/abs/2607.11801v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) often underperform on fine-grained, non-semantic attributes of speech, such as a speaker's emotion, despite strong performance on speech content. Improving this without the cost of retraining calls for an effective inference-time intervention, yet most existing methods intervene only after the audio encoder and operate at a relatively coarse granularity. The encoder itself, where acoustic information is first extracted from the waveform, remains largely unexpl...
  </details>

- **2026-07-13** — Jin Xu, Kangdi Wang, Ruibin Yuan et al. — [Qwen-Music Technical Report](http://arxiv.org/abs/2607.11699v1)
  <details><summary>📄 Abstract</summary>
  In this report, we introduce Qwen-Music, a powerful music generation model capable of producing highly musical and high-fidelity songs with complete vocal singing. Qwen-Music supports two core tasks: Text to Music Generation, which create entirely new songs from text descriptions, lyrics, and musical attributes, and Cover Song Generation, which reinterprets existing songs with different styles and vocal characteristics. Architecturally, Qwen-Music integrates three core components: Qwen-Music-Tok...
  </details>

- **2026-07-13** — Matteo Tuveri — [From Prompt Engineering to Epistemic Prompting: Prompt Trajectories as AI-Mediated Problem Framing in Science Education](http://arxiv.org/abs/2607.11680v1)
  <details><summary>📄 Abstract</summary>
  Prompt engineering is commonly presented as a technical competence for obtaining more accurate, relevant, or well-formatted outputs from large language models (LLMs). However, in STEM education, prompting should also be understood as a continuous epistemic practice. Students interpret contextual and disciplinary cues and adopt expectations about what kind of knowledge, representation, and action are appropriate. Drawing on epistemological framing, and AI-mediated concept-to-decision reasoning, t...
  </details>

- **2026-07-13** — Xin Zhang, Haochen Wang, Yikang Zhou et al. — [Actor as Its Own Critic: Unifying Region Understanding and Localization via CycleGRPO](http://arxiv.org/abs/2607.11581v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces Actor as Its Own Critic, a unified reinforcement learning framework, Cycle Group Relative Policy Optimization (CycleGRPO), that jointly optimizes region understanding and localization for Multimodal Large Language Models (MLLMs). Unlike existing separate pipelines, we leverage the inherent duality between the two tasks to construct a self-evaluating reinforcement learning paradigm: "region $\to$ text $\to$ region''. Specifically, a single MLLM first acts as the actor to gen...
  </details>

- **2026-07-13** — Paul Garnier, Jonathan Viquerat, Elie Hachem — [Heuristic Learning for Active Flow Control Using Coding Agents](http://arxiv.org/abs/2607.11565v1)
  <details><summary>📄 Abstract</summary>
  Active flow control involves nonlinear dynamics, partial observations, and computationally expensive simulations, making controller design particularly challenging. Deep reinforcement learning (DRL) has emerged as a powerful framework for such problems, but its success typically relies on large numbers of simulator interactions and produces neural-network policies whose decision process often remains difficult to interpret. In this work, we investigate a different paradigm: instead of optimizing...
  </details>

- **2026-07-13** — Langyuan Cui, Chun Kai Ling, Hwee Tou Ng — [Communicating Chess Strategies in Natural Language](http://arxiv.org/abs/2607.11486v1)
  <details><summary>📄 Abstract</summary>
  Chess engines have long achieved superhuman playing strength. However, the underlying strategy behind their move suggestions is difficult for human players, even skilled ones, to comprehend. Motivated by this, we propose the task of chess strategy verbalization, which is to describe chess strategies in natural language. We design (i) a pipeline for verbalizing strategies and (ii) an evaluation framework for objective evaluation of generated strategy descriptions. Our experiments show that natura...
  </details>

- **2026-07-13** — Marlena Flüh, Soo-Yon Kim, Carolin Victoria Schneider et al. — [FAIR GraphRAG: A Retrieval-Augmented Generation Approach for Semantic Data Analysis](http://arxiv.org/abs/2607.11464v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) addresses the limitations of Large Language Models (LLMs) when providing responses to domain-specific questions. Graph-based RAG approaches, such as GraphRAG, enhance retrieval by capturing semantic relationships within knowledge graphs (KGs). While the FAIR principles (Findability, Accessibility, Interoperability, and Reusability) are becoming prevalent for scientific data management, especially in complex domains such as medicine, existing RAG approaches la...
  </details>

- **2026-07-13** — Costas Mylonas, Magda Foti — [A Multimodal Dataset for Large Language Model Applications in the Energy Domain](http://arxiv.org/abs/2607.11459v1)
  <details><summary>📄 Abstract</summary>
  This paper presents the mAIEnergy dataset, an open-access, multimodal corpus developed to support Large Language Model (LLM) applications in the energy sector. The dataset integrates approximately 50,000 textual documents, 20,000 images, 25 million numerical time series records, and 2 million geospatial and relational data entries. It includes policy and regulatory texts, scientific articles and news articles, satellite and contextual imagery, electricity system measurements, weather observation...
  </details>

- **2026-07-13** — Wenyi Wu, Sibo Zhu, Kun Zhou et al. — [StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure](http://arxiv.org/abs/2607.11388v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models (LLMs) and vision-language models (VLMs) have enabled increasingly capable digital agents for computer use. However, real-world tasks are often long-horizon and involve evolving contexts containing accumulated observations, intermediate edits, failed attempts, and partially completed executions. Existing agents typically operate over raw interaction history, making task progress difficult to interpret, verify, and recover, which ultimately limits reliable...
  </details>

- **2026-07-13** — Leo van Iersel, Mark Jones, Esther Julien et al. — [Proximity Measures for Classes of Phylogenetic Networks](http://arxiv.org/abs/2607.11325v1)
  <details><summary>📄 Abstract</summary>
  Phylogenetic networks are used to represent the evolutionary history of species. Due to biological interpretations and computational advantages, researchers have focused on restricted classes of phylogenetic networks, such as tree-child, orchard, and tree-based. These classes capture different notions of tree-likeness: tree-child networks require every internal vertex to have a taxon reachable by a tree path, orchard networks are trees with horizontal arcs (for modelling histories rife with hori...
  </details>

- **2026-07-13** — Tatsuhiko Sato, Shintaro Hashimoto, Tatsuhiko Ogawa et al. — [Toward AI-Agent-Driven Particle Transport Simulations: Implementation of AI-Assisted Workflows for PHITS](http://arxiv.org/abs/2607.11309v1)
  <details><summary>📄 Abstract</summary>
  Monte Carlo particle transport codes are powerful tools, but their use requires substantial knowledge of input preparation, execution, and result analysis. In this study, we present a code-side strategy for applying existing AI assistants and AI agents to PHITS. Two complementary sets of AI-ready resources were prepared from manuals, lecture materials, sample inputs, utility information, and developer-curated cautions: a bundled knowledge base for retrieval-augmented generation (RAG)-based assis...
  </details>

- **2026-07-13** — Ciprian Cristescu, Adrian-Marius Dumitran, Angela-Liliana Dumitran et al. — [Automated Textbook Auditing with Multi-Agent LLM Systems](http://arxiv.org/abs/2607.11276v1)
  <details><summary>📄 Abstract</summary>
  Ensuring the quality of educational materials requires more than standard proofreading: textbooks must be audited for factual accuracy, domain-specific technical correctness, and linguistic quality simultaneously -- a task that general-purpose grammar checkers cannot address. We present \textbf{AI Textbook Auditor}, a modular multi-agent pipeline for automated quality assurance of educational materials across subject domains. The system accepts a textbook PDF and produces a structured, human-rev...
  </details>

- **2026-07-13** — Daeyeop Lee, Hwanjo Yu — [Valid $\ne$ Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought](http://arxiv.org/abs/2607.11266v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) prompting has significantly advanced the reasoning capabilities of Large Language Models (LLMs), yet it often incurs substantial computational costs due to over-reasoning: the generation of redundant, verbose, or irrelevant steps. While existing reasoning step evaluators effectively detect logical fallacies and factual errors, our analysis reveals a critical blind spot: they fail to penalize valid but inefficient reasoning steps that inflate token usage without contributin...
  </details>

- **2026-07-13** — Abdullah Mağden — [4x4 Matrix Representation of Hybrid Numbers, Gram Matrix and Golden Ratio](http://arxiv.org/abs/2607.11242v1)
  <details><summary>📄 Abstract</summary>
  This study investigates the Lie algebra structure and geometric properties of hybrid numbers, under a specific non-associative multiplication table. Within the scope of the study, the structure constants of the system were derived through commutator relations, and 4x4 matrix representation was constructed. By defining the Gram matrix, complex and hybrid conjugates, the connection of the eigenvalues of Gram matrices to the golden ratio has been obtained. Theoretical analysis reveal that this hybr...
  </details>

- **2026-07-13** — Sukai Huang, Chenyuan Zhang, Fucai Ke et al. — [What We Talk About When We Talk About LLM Planning: Evidence for Two Distinct Planning Abilities](http://arxiv.org/abs/2607.11197v1)
  <details><summary>📄 Abstract</summary>
  When LLMs exhibit uneven performance across planning tasks, these gaps are often attributed to task difficulty. We argue that this explanation is incomplete, as task-level variation may reflect distinct latent planning competencies rather than differences along a single ability spectrum. We study this question on ACPBench-Hard by evaluating multiple LLM families under varying test-time reasoning budgets and applying a multidimensional item response theory model to uncover the latent competency s...
  </details>

- **2026-07-13** — Ziang Ren, Guodong Lin, Yuchen Ai et al. — [Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR](http://arxiv.org/abs/2607.11163v1)
  <details><summary>📄 Abstract</summary>
  Large-scale pretrained ASR models such as Whisper exhibit strong multilingual capabilities. However, fine-tuning on low-resource languages often causes catastrophic forgetting. Although continual learning mitigates this issue, existing methods struggle to regulate cross-task interference in multilingual settings, where dominant languages bias optimization. We propose Unified Gradient Projection (UGP), which constrains parameter updates using reference gradients from language-balanced replay in a...
  </details>

- **2026-07-13** — Haoyu Gu, Lekai Qian, Haowu Zhou et al. — [BeatEdit: Symbolic Music Generation as Explicit Editing](http://arxiv.org/abs/2607.11124v1)
  <details><summary>📄 Abstract</summary>
  Music creation is fundamentally a process of revision. Yet symbolic music generation remains dominated by paradigms that produce complete sequences from scratch, with limited support for selective modification. Edit-based methods have proven effective for text transformation tasks, but remain largely unexplored for symbolic music. We trace this absence to the representational level: conventional event-based music encodings lack the structural properties required by explicit music editing. In con...
  </details>

- **2026-07-12** — Jinhui Hu, Guo Chen, Huaqing Li et al. — [RED-SEGA:Resilient Decentralized Stochastic Proximal Optimization with Gradient Sketching over Time-Varying Networks](http://arxiv.org/abs/2607.10791v1)
  <details><summary>📄 Abstract</summary>
  Variance reduction is indispensable in Byzantine-resilient decentralized stochastic optimization over multi-agent systems (MASs) for its ability to mitigate gradient noise and thereby enhance the resilient aggregation process. However, most existing Byzantine-resilient decentralized variance-reduced (VR) stochastic gradient algorithms rely on random data sampling, which proves inefficient in data-scarce yet high-dimensional tasks, for instance, image deblurring. This paper pursues an alternative...
  </details>

- **2026-07-12** — Yan Lin, Yuyang Dai, Jiahui Geng et al. — [AI YOU Town: Make Friends and Money with Your Digital Twin](http://arxiv.org/abs/2607.10539v1)
  <details><summary>📄 Abstract</summary>
  Existing approaches to infer user traits and generate responses consistent with a persona rely on static prompting. They lack calibrated uncertainty, ignore sequential evidence, and drift during long interactions. We present \textbf{AI YOU}, a framework that continually updates a personality profile with 22 dimensions from conversation and embodies it in a personal digital twin. Practically, the system combines prompting, Bayesian updating, and conformal prediction for persona inference. A perio...
  </details>

- **2026-07-12** — Xiangxin Zhou, Jiarui Yao, Penghui Qi et al. — [Predictive Divergence Masks for LLM RL](http://arxiv.org/abs/2607.10848v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for large language models (LLMs) typically relies on trust-region masks to stabilize off-policy updates. The dominant PPO-style approach uses the sampled-token importance ratio for two criteria: a proximity criterion, which asks whether the policy has moved too far from the behavior policy, and a direction criterion, which asks whether the update pushes it farther away. Recent work DPPO improves the proximity criterion by replacing PPO's ratio-based test with a probability...
  </details>

- **2026-07-12** — Sudipto Ghosh, Tanmoy Chakraborty — [Route, Communicate, and Reason: Gated Routing and Adaptive Depth for Efficient Multi-Agent Reasoning](http://arxiv.org/abs/2607.10836v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent ensembling multiplies active parameters and inference cost without answering three basic questions: which agents to consult, how deeply a query should traverse a hierarchy of agents, and when inter-agent communication is worth its cost. We present GRADE (Gated Routing and Adaptive Depth for Efficient Reasoning), a hierarchical multi-agent system in which four lightweight learned gates jointly govern agent selection, hierarchy depth, inter-agent communication, and branch pruning. Trai...
  </details>

- **2026-07-12** — Matthias M. M. Buehlmaier — [LayerNorm as Implicit Gain Control in Looped Transformers](http://arxiv.org/abs/2607.10681v1)
  <details><summary>📄 Abstract</summary>
  In pre-LayerNorm looped transformers, LayerNorm inside the recurrent block acts as an implicit gain controller: by coupling the block's local Lipschitz constant inversely to the activation scale, it renders the recurrence Jacobian non-normal -- asymptotically contractive at every verified fixed point even where its operator norm exceeds 1 -- so the true stability budget is the spectral margin, not an operator-norm bound. That margin depletes as the carry $ρ\to 1$, and a minority of initializatio...
  </details>

- **2026-07-12** — Satoshi Kura, Hiroshi Unno — [Solving First-Order Fixed-Point Logics via a Least-to-Greatest Transformation Based on Game Semantics](http://arxiv.org/abs/2607.10650v1)
  <details><summary>📄 Abstract</summary>
  Fixed-point logics provide an expressive intermediate framework for reasoning about temporal properties of programs. One of the key approaches to solving their validity checking problem is via transformations from least fixed points to greatest fixed points ($μ$-to-$ν$ transformations), which generalizes a reduction from termination verification to safety verification studied in binary reachability analysis. In this paper, we introduce game-semantic interpretations of $μ$-to-$ν$ transformations....
  </details>

- **2026-07-12** — Tahmid Al Hannan, Diego Garcia, Alex Njoroge et al. — [Knowledge Distillation for Automated AI Tutor Evaluation](http://arxiv.org/abs/2607.10647v1)
  <details><summary>📄 Abstract</summary>
  The rapid integration of Large Language Models (LLMs) into K-12 and higher education has outpaced the development of reliable methods for evaluating their pedagogical quality. As the research community starts to explore the space of automating evaluation of AI tutors, we introduce FATE (FLC AI Tutor Evaluator), a specialized 8B-parameter language model designed to evaluate AI tutors. Aligned with the four core evaluation tracks from the BEA 2025 Shared Task, our model assesses pedagogical abilit...
  </details>

- **2026-07-12** — Ilia Karpov — [MafiaScope: Non-Invasive, Time-Resolved Belief Probing for LLM Agents in Social Deduction Games](http://arxiv.org/abs/2607.10645v1)
  <details><summary>📄 Abstract</summary>
  An LLM agent's public behaviour reveals little about its social reasoning: an agent that votes correctly may be guessing, and an agent that lies well leaves no trace of what it actually believes. We present MafiaScope, an open testbed that turns the social deduction game Mafia into a measurement instrument for machine Theory of Mind. After every public utterance, every agent privately answers a configurable set of structured probe questions; the answers never re-enter the game and are scored aut...
  </details>

- **2026-07-12** — Tiancheng Gao, Xiang Zhang, Wei Lan et al. — [Inferring Inventory Dynamics from Supply Chain Networks: A Graph Learning Approach with Autonomous Validation](http://arxiv.org/abs/2607.10642v1)
  <details><summary>📄 Abstract</summary>
  Supply-demand mismatch represents a fundamental challenge in supply chain management, yet its direct measurement remains particularly elusive for small and medium-sized enterprises (SMEs).These firms typically lack systematic inventory records, leaving labeled training data critically scarce. Conventional supervised learning methods rely heavily on labeled samples, rendering them ill-equipped to reliably validate firm-level predictions under such data-scarce conditions. To resolve this unlabeled...
  </details>

- **2026-07-12** — Yixiong Chen, Xinyi Bai, Alan Yuille — [The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory](http://arxiv.org/abs/2607.10608v1)
  <details><summary>📄 Abstract</summary>
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ...
  </details>

- **2026-07-12** — Yu Mei, Qingyue Zhuang, Jie Cai et al. — [U-Lens: Supporting User Uncertainty Management in Long-Form LLM Responses](http://arxiv.org/abs/2607.10604v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate long-form answers for knowledge-intensive tasks, but users often struggle to decide which parts of a response deserve scrutiny, why they may be unreliable, and what to do next. Prior work on uncertainty communication has largely focused on making uncertainty visible through cues such as confidence scores, leaving less support for the broader process of managing uncertainty distributed across a long response. Through a formative study...
  </details>

- **2026-07-12** — Haojie Huang, Zhang Ye, Linfeng Zhao et al. — [Action Map Policy: Learning 3D Closed-loop Manipulation via Pixel Classification](http://arxiv.org/abs/2607.10706v1)
  <details><summary>📄 Abstract</summary>
  The action space poses a major challenge in robot learning, since it is often high-dimensional, can span long time horizons, and frequently admits multi-modal optimal solutions. A good choice of action representation and loss function can help to address these concerns, but there are often trade offs. We propose Action Map Policy (AMP), which casts 3D closed-loop manipulation policy learning as a classification problem in image space. While classification has been an effective formulation in gen...
  </details>

- **2026-07-12** — Eli Bar-Yosef, Amir Averbuch, Eli Turkel — [The Singularity Space: A Generative Diffusion Framework for Signal Representation](http://arxiv.org/abs/2607.10930v1)
  <details><summary>📄 Abstract</summary>
  Generative models often represent signals as dense grids of amplitudes, blurring sharp transients that are crucial for the correctness of physical signals. We introduce Singularity Space, a generative framework that represents signals through complex-plane singularities, rooted in the classical pole-residue representation of meromorphic functions. We learn a latent space of physically constrained, per-signal singularity configurations to solve an inverse problem from degraded or partial observat...
  </details>

- **2026-07-12** — Marco Armenta — [$τ$-Hochschild (co)homology, the square of the Serre bimodule, and the Coxeter automorphism of the Tamarkin--Tsygan calculus](http://arxiv.org/abs/2607.10913v1)
  <details><summary>📄 Abstract</summary>
  We relate two recent enrichments of the Hochschild theory of a finite-dimensional algebra $\Lm$: the $τ$-Hochschild (co)homology of Cibils, Lanzilotta, Marcos and Solotar, built from Iyama's higher Auslander--Reiten translates of the regular bimodule, and the Coxeter automorphism $σ_\Lm$ of the Tamarkin--Tsygan calculus. We show that the Nakayama functor of the enveloping algebra transforms Happel's minimal resolution into a complex representing $\D\Lm\Ltimes_\Lm \D\Lm$, the square of the Serre ...
  </details>

- **2026-07-12** — Nacer Eddine Boukacem, Madhav Mani, Paul François — [Sandscapes: self-modifying energy landscapes with emergent branching and flips](http://arxiv.org/abs/2607.10903v1)
  <details><summary>📄 Abstract</summary>
  Energy landscapes provide a common framework for describing learning, embryonic development, and collective dynamics. Although such landscapes may evolve over time, their dynamics are typically prescribed externally rather than generated by the system itself. Here we get inspiration from biology to introduce sandscapes : self-modifying landscapes in which the motions of interacting agents continuously reshape the landscape that governs their own trajectories. We derive sandscapes from a minimal ...
  </details>

- **2026-07-12** — Yeon-Koo Che, Olivier Tercieux — [Top Trading Cycles in Large Markets: The Asymptotic Irrelevance of Priorities](http://arxiv.org/abs/2607.10819v1)
  <details><summary>📄 Abstract</summary>
  Top Trading Cycles (TTC) is Pareto efficient and strategy-proof and explicitly uses agents' priorities. Although TTC favors higher-priority agents in each round, we show that this priority advantage vanishes as the market grows large under a canonical random model of preferences and priorities. In the limit, TTC produces assignments with virtually the same incidence of justified envy as Random Serial Dictatorship (RSD) -- a mechanism entirely blind to priorities. This stark asymptotic equivalenc...
  </details>

- **2026-07-12** — Hao Zheng, Jinyi Huang, Tiantian Zheng et al. — [Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos](http://arxiv.org/abs/2607.10797v1)
  <details><summary>📄 Abstract</summary>
  Assembly action understanding is a key enabler for effective human-robot collaborative assembly, yet it remains challenging due to subtle motions and fine-grained hand-object interactions. We adapt vision-language models (VLMs) to this challenging domain with Compositional Context Fine-Tuning (CCFT), a method that decomposes assembly actions into semantic elements (Verb, Object, Tool) and fine-tunes VLMs to recognize each action element using templated question-answering pairs. This approach ens...
  </details>

- **2026-07-12** — Akira Matsui — [Return of the solo author: The changing division of labor in science in the age of generative A](http://arxiv.org/abs/2607.10780v1)
  <details><summary>📄 Abstract</summary>
  Modern science has experienced a long shift from individual work to team production. Generative artificial intelligence (AI) might appear to extend this trajectory by lowering research costs and enabling larger-scale collaboration. Yet if tasks once performed by coauthors can be delegated to AI, the same technology may also weaken the need for collaboration in parts of the research process. Here, we examine this tension by moving beyond average team size and focusing on the solo-authored tail of...
  </details>

- **2026-07-12** — Maya Grace Torii, Takahito Murakami, Yoichi Ochiai — [Lottery and Sprint Arcade: Enabling Player-Driven Game Editing with Generative AI](http://arxiv.org/abs/2607.10711v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are shifting game generation from offline automation toward play-driven modification through natural language interaction. In this work, we present a play-driven game editing system that enables players to modify a retro Space Invaders - style arcade game through voice-based natural-language commands during play. Spoken instructions are interpreted by an LLM and translated into structured updates of internal configuration parameters, allowing iterative play - edit - ...
  </details>

- **2026-07-12** — M. Průšek, A. Novozámský, F. Šroubek et al. — [HyperBank: A Differentiable Bank of Classical Priors for Few-Shot Spheroid Microscopy Segmentation](http://arxiv.org/abs/2607.10684v1)
  <details><summary>📄 Abstract</summary>
  Few-shot spheroid segmentation must adapt to new cell lines, microscopes, and illumination conditions from only a small set of annotated images. While foundation few-shot segmenters can be accurate, their large opaque backbones make it difficult to understand which visual cues drive success or failure. We study this question with HyperBank, a differentiable bank of classical image-processing operators combining Frangi vesselness, a Sauvola threshold pyramid, structure-tensor responses, gradient ...
  </details>

- **2026-07-12** — Qing Lin, Mengmi Zhang — [Personalized Emotional Intelligence in Generative AI through Symbolic Affective Reasoning](http://arxiv.org/abs/2607.10678v1)
  <details><summary>📄 Abstract</summary>
  Emotional intelligence enables humans to recognize emotions, infer their causes, reason about interventions, and modify their environment to achieve desired affective states. Despite recent advances in artificial intelligence (AI), current models remain largely limited to generating realistic content or performing semantic reasoning, with little capacity for understanding, predicting, and personalizing human emotional responses. Here we introduce Emotion-augmented geneRatiOn System (EROS), a hyb...
  </details>

- **2026-07-12** — Jun Chen, Erdent Bao, Wenlong Dong et al. — [Dual-Process Atomic Skill Learning: Decoupling Semantic Reasoning and Real-Time Control](http://arxiv.org/abs/2607.10625v1)
  <details><summary>📄 Abstract</summary>
  Language-conditioned Imitation Learning (IL) is essential for enabling robots to perform complex tasks following natural language instructions. However, generalizing to multi-step compositional tasks remains a significant challenge. While hierarchical approaches attempt to address this by decomposing tasks into atomic skills, existing methods often suffer from training instability and codebook collapse due to the tight coupling between high-level skill reasoning and low-level action generation i...
  </details>

- **2026-07-12** — Raziyeh Takbiri — [Demixing Sparse Signals from Nonlinear Observations using Generalized Non-convex Regularization](http://arxiv.org/abs/2607.10618v1)
  <details><summary>📄 Abstract</summary>
  We consider the recovery of a pair of sparse vectors from a limited number of nonlinear observations of their superposition: $y_i=g(\inner{\ba_i}{\bPhi\bw^\ast+\bPsi\bz^\ast})+e_i$, $i=1,\dots,m$, with $m\ll n$, incoherent orthonormal bases $\bPhi,\bPsi$, a scalar link $g$, and noise $e_i$ that may be heavy-tailed or contaminated. We propose a regularization-based framework combining a Huberized data fidelity with generalized folded-concave penalties (SCAD, MCP), and a two-block proximal alterna...
  </details>

- **2026-07-12** — Siyu Wang, Wei Tan, Lulu Chen — [Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification](http://arxiv.org/abs/2607.10588v1)
  <details><summary>📄 Abstract</summary>
  Tasks such as customs tariff classification, export control categorization, and standards-based equipment coding require assigning an input instance to a fine-grained class under an explicit regulatory hierarchy. Unlike standard text classification, the correct label in these tasks is not determined by semantic similarity alone, but by rule-defined boundaries, threshold conditions, exclusion clauses, definitions, and local exceptions. As a result, two highly similar inputs may require different ...
  </details>

- **2026-07-12** — Chunwei Ma, Russell Wolfinger — [Laguerre Geometry for Interpreting Large Language Models](http://arxiv.org/abs/2607.10578v1)
  <details><summary>📄 Abstract</summary>
  Existing hypotheses represent a concept in an LLM as a single point, a linear direction, or a Gaussian cluster, yet it remains unclear how and why such structures emerge. Here, we show that concept geometry can be precisely characterized via Laguerre Geometry, in which a concept is defined as a region--a Laguerre-Voronoi cell or a union of cells--allowing us to strictly define, measure, and separate concepts. Building on this formulation, we show that finer-grained concept structures, such as in...
  </details>

- **2026-07-12** — Zhaolin Hu, Hehe Fan, Wangyihan Guo et al. — [Large language model agents accelerate inverse design of metal-organic frameworks for gas separation](http://arxiv.org/abs/2607.10559v1)
  <details><summary>📄 Abstract</summary>
  Metal-organic frameworks (MOFs) offer a highly modular platform for adsorptive gas separation, yet their vast reticular design space makes inverse design difficult under simultaneous constraints of chemical validity, separation performance, and structural diversity. Here, we present LEMO Agent, a large-language-model agent framework for closed-loop inverse design of gas-separation MOFs in MOFid space. LEMO Agent couples language-based candidate generation with MOFid standardization, explicit val...
  </details>

- **2026-07-12** — Zichuan Liu, Ruijin Hua — [Tool-Adaptive LLM Reranker](http://arxiv.org/abs/2607.10555v1)
  <details><summary>📄 Abstract</summary>
  Generative Large Language Models (LLMs) have revolutionized information retrieval, yet their strictly parametric nature frequently leads to severe factual hallucinations when confronted with complex queries beyond their epistemic boundaries. While external tool-calling can mitigate this, indiscriminately invoking search tools for every document during reranking incurs prohibitive latency overheads, creating an intractable accuracy-efficiency dilemma. To address this challenge, we propose TALRank...
  </details>

- **2026-07-12** — Masayuki Ohzeki — [Coherent Quantum Schrodinger Bridge: Two-Boundary Optimal Control for Quantum Algorithm Design](http://arxiv.org/abs/2607.10550v1)
  <details><summary>📄 Abstract</summary>
  Quantum algorithms are intrinsically two-boundary processes: an input state is prepared, and an output state or subspace is selected as the computational answer. We formulate this observation as a coherent Quantum Schrödinger Bridge (QSB), a pure-state Hamiltonian counterpart of Schrödinger bridge theory in which the endpoint constraint is imposed on state vectors and the transport cost is the quadratic control action. In this setting Aharonov's two-state vector becomes the natural optimal-contr...
  </details>

- **2026-07-11** — S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha — [EvidentialRAG: Quantifying and Mitigating Information Conflict in Multi-Source Retrieval-Augmented Generation via Evidential Deep Learning](http://arxiv.org/abs/2607.10491v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation grounds large language models in external evidence, but most pipelines still treat retrieved passages as deterministic and mutually consistent context. In open information environments, retrieved sources may disagree because of temporal drift, source error, ambiguity, or genuine uncertainty. This paper introduces ERAG, an uncertainty-aware RAG framework that converts retrieved chunks into probabilistic evidence before generation. A lightweight evaluator extracts ca...
  </details>

- **2026-07-11** — Zhiyuan Wen, Jiannong Cao, Zijian Wang et al. — [PolyInterview: An LLM-based Platform for Immersive Mock Interview Practice with Comprehensive Multimodal Assessment](http://arxiv.org/abs/2607.10310v1)
  <details><summary>📄 Abstract</summary>
  Preparing for job interviews is important for securing desired positions, yet realistic practice remains difficult to access: real interviews are infrequent, expert mock coaching is costly, and self-practice offers neither adaptive dialogue nor structured assessment. Existing systems typically address only parts of this need through fixed question sequences, limited communication channels, or feedback with little supporting evidence. We present PolyInterview, an LLM-based platform for immersive ...
  </details>

- **2026-07-11** — Shihao Yuan, Yuanze Li, Ruyi Zhang et al. — [Generalize LMMs to Versatile Visual Modalities via Fabricated Modality Synthesis](http://arxiv.org/abs/2607.10308v1)
  <details><summary>📄 Abstract</summary>
  Despite the advancements of Large Multimodal Models (LMMs) in RGB vision, their ability to generalize to unseen visual modalities remains a largely unexplored challenge. We argue that different visual modalities are merely distinct samplings of the same physical world. Therefore, effective generalization requires models to possess both modality-agnostic perception of scene semantics and the adaptability to modality-specific characteristics. To achieve this, we propose a training framework, VVM-T...
  </details>

- **2026-07-11** — Tiancheng Ma, Nasir U. Eisty — [From Business Requirements to Test Assertions: Evaluating LLM-Generated Oracles on Real Bugs](http://arxiv.org/abs/2607.10277v1)
  <details><summary>📄 Abstract</summary>
  The oracle problem (determining the correct expected outcome for a test) remains a major bottleneck in automated testing, and is increasingly relevant as non-experts rely on AI-generated code they cannot reliably validate. We study whether large language models (LLMs) can generate generalizable test oracles directly from natural-language business requirements, without access to source code or example input-output pairs. We propose a reproducible, requirement-driven pipeline grounded in Defects4J...
  </details>

- **2026-07-11** — Amir Reza Jafari, Praboda Rajapaksha, Reza Farahbakhsh et al. — [PTEI: Integrating Personality Traits to Enhance Emotional Intelligence in Large Language Models](http://arxiv.org/abs/2607.10245v1)
  <details><summary>📄 Abstract</summary>
  Despite advances in Emotional Intelligence (EI), Large Language Models (LLMs) still significantly underperform humans in complex emotional reasoning. This gap originates partly from the limited incorporation of individual differences, particularly personality traits, which are fundamental to human emotional inference. To address this, we propose PTEI, a novel framework for integrating Personality Traits into Emotional Intelligence tasks using LLMs. In PTEI, MBTI and OCEAN personality traits are ...
  </details>

- **2026-07-11** — Zhiyan Zhang, Peipei Song, Jinpeng Hu et al. — [Benchmarking Dynamic Affective Reasoning: A Viewer-Centric Video Emotion Dataset](http://arxiv.org/abs/2607.10238v1)
  <details><summary>📄 Abstract</summary>
  Video emotion analysis is typically framed as a static classification problem, treating each clip as an independent labeled unit. However, such a formulation overlooks a key psychological fact: emotions change as a result of cumulative reactions to consecutive causal events. To bridge this gap, we introduce Dynamic Affective Reasoning, the first large-scale benchmark for viewer-centric affect transitions and causal reasoning over consecutive video events. DAR contains 15,087 videos and 36,908 ev...
  </details>

- **2026-07-11** — Varun Gandhi, Jaewook Lee, Shantanu Todmal et al. — [GRASP: GRanularity-Aware Search Policy for Agentic RAG](http://arxiv.org/abs/2607.10463v1)
  <details><summary>📄 Abstract</summary>
  Agentic retrieval-augmented generation (RAG) extends static RAG by allowing language models to iteratively reason, generate search queries, retrieve evidence, and predict answers. However, it remains challenging for models to decide when to retrieve, whether to use lexical matching or semantic similarity, and how to control context granularity to prevent irrelevant tokens from interfering with agent reasoning. In this paper, we introduce GRASP, a reinforcement learning (RL) framework for trainin...
  </details>

- **2026-07-11** — Qiqi Duan, Changlun Li, Chen Wang et al. — [Can Agentic Trading Systems Pay for Their Own Intelligence?](http://arxiv.org/abs/2607.10286v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly used in trading systems, where model reasoning, tool use, and continual decisions incur costs that are expected to produce trading value. Existing evaluations typically report performance metrics, but rarely examine agentic viability: whether dynamic LLM-mediated decisions convert their induced costs into measurable incremental profit. To apply this criterion, we introduce TradeLens, a trace-grounded diagnostic toolkit for evaluating agentic tra...
  </details>

- **2026-07-11** — Amirhossein Mohammadi, Laurence E. Frank, Albert Gatt et al. — [Language Re-generation: An investigation into information locality effects on reconstruction](http://arxiv.org/abs/2607.10268v1)
  <details><summary>📄 Abstract</summary>
  Information locality, the tendency for syntactically related words to appear close together, shapes both human language processing and language model learning. While prior work has examined whether language models can acquire impossible languages, it remains unclear whether they can recover natural language from such input and what this reveals about their inductive biases. We address this by complementing learnability-based approaches with a reconstruction framework: fine-tuning GPT-2 models pr...
  </details>

- **2026-07-11** — Pravina Mylvaganam, Eliathamby Ambikairajah, Ting Dang et al. — [Which Languages Transfer Best to Warlpiri? A Similarity-Based Study for Low-Resource ASR](http://arxiv.org/abs/2607.10256v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates how language similarity can improve cross-lingual transfer for automatic speech recognition (ASR) in extremely low-resource settings. Warlpiri, an Australian Aboriginal language, has very limited transcribed speech data, making transfer learning essential. We propose a framework combining acoustic similarity from pre-trained speech models with linguistic similarity based on typology, phoneme inventories, grammatical, and syntactic features to rank high-resource source lan...
  </details>

- **2026-07-11** — Guanhua Ye, Niu Jingbin, Yan Li et al. — [What Does Your Short-Answer VQA Score Actually Measure? Evaluator-Dependent Instability in Multimodal Short-Answer Benchmarks](http://arxiv.org/abs/2607.10240v1)
  <details><summary>📄 Abstract</summary>
  Short-answer VQA benchmarks conflate two distinct quantities: whether a model's answer is semantically correct, and whether that answer matches the surface form expected by the automatic evaluator. We study this conflation across six vision--language models and six benchmarks, using a human-validated semantic judge (97.6% precision) to audit over 37k official errors. A second text-only judge reproduces the same benchmark-level false-negative pattern, showing that the effect is not an artifact of...
  </details>

- **2026-07-11** — Haris Aziz, Xiaolin Bu, Xinhang Lu et al. — [Best-of-Both-Worlds Fairness for Mixed Goods and Chores](http://arxiv.org/abs/2607.10232v1)
  <details><summary>📄 Abstract</summary>
  We study the fundamental problem of fairly dividing indivisible items among agents with additive utilities. In our model, an item can be a good yielding non-negative utilities to some agents and simultaneously a chore yielding negative utilities to others. We take the best-of-both-worlds perspective and our goal is to construct a randomized allocation that is exactly fair ex ante while also being supported on ex post approximately fair allocations. The fairness notions examined in this paper are...
  </details>

- **2026-07-09** — Kushin Mukherjee, Na Yeon Kim, Maren Wehrheim et al. — [AI-guided stimuli discovery and generation to optimize facial emotion perception studies in autism](http://arxiv.org/abs/2607.08533v1)
  <details><summary>📄 Abstract</summary>
  Understanding perceptual differences between autistic and neurotypical adults requires behavioral assays that are sensitive, reliable, and mechanistically informative. Facial emotion perception is a useful test case because group differences have been reported, but findings vary across studies. Here we show that this variability may reflect image-level sparsity: autistic-neurotypical differences in emotion judgments were concentrated in a small subset of diagnostic facial expressions rather than...
  </details>

- **2026-07-09** — Mayank Singal — [When Thinking Hurts: Epistemic Signals in the Reasoning Chains of Visual Language Models](http://arxiv.org/abs/2607.08059v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty quantification for visual language models (VLMs) conventionally targets the answer token distribution. We provide the first three-family empirical characterisation of answer entropy behaviour in thinking-mode VLMs. Running four models on identical POPE adversarial samples, we find three qualitatively distinct patterns: Qwen3-VL-8B-Thinking shows complete collapse (ans H AUROC = 0.492); GLM-4.1V-9B-Thinking shows no collapse (0.716); and InternVL3-8B shows selective thinking (chains o...
  </details>

- **2026-07-09** — Yifan Zhou, Qihao Yang, Yan Li et al. — [Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation](http://arxiv.org/abs/2607.08758v1)
  <details><summary>📄 Abstract</summary>
  Scientific ideas rarely start from a blank page. They inherit mechanisms, repair known limitations, and recombine pieces of earlier work, much like biological genomes. Current benchmarks still say little about whether AI systems can follow this inheritance structure. We present IdeaGene-Bench (IG-Bench), a benchmark for scientific lineage reasoning and lineage-grounded idea generation. IG-Bench is organized around the IdeaGene framework: each paper or proposal is represented as a set of minimal,...
  </details>

- **2026-07-09** — Ayda Eghbalian, Kevin Desai — [Pose-to-Biomechanics: Bridging 3D Human Pose Estimation and Biomechanical Attribute Prediction](http://arxiv.org/abs/2607.08725v1)
  <details><summary>📄 Abstract</summary>
  Recent progress in 3D human pose estimation has made markerless recovery of skeletal motion increasingly accurate and scalable. However, most pose estimators remain optimized for geometric keypoint accuracy, while many real-world applications in rehabilitation, sports science, ergonomics, and clinical movement analysis require biomechanical quantities that describe how the body moves, loads, and activates. In this work, we propose BioModule, a lightweight plug-in temporal transformer that attach...
  </details>

- **2026-07-09** — Peng Cui, Jitao Wang, Siyan Xue et al. — [Towards Precision Therapy in Hepatocellular Carcinoma: A Clinical-Reasoning LLM for Risk Stratification and Treatment Guidance](http://arxiv.org/abs/2607.08602v1)
  <details><summary>📄 Abstract</summary>
  Hepatocellular carcinoma (HCC) is a common malignancy and a leading cause of cancer-related mortality. Current guidelines and staging systems provide coarse categories, but often miss within-stage heterogeneity and the clinical context in electronic medical records (EMRs). We present HCC-STAR (Hepatocellular Carcinoma Staging, Treatment And pRognosis), a clinically aligned large language model that reads routine EMR narratives and jointly outputs risk score-based staging, ranked guideline-consis...
  </details>

- **2026-07-09** — Palaash Goel, Ayush Maheshwari, Tanmoy Chakraborty — [It Takes a MAESTRO To Prune Bad Experts](http://arxiv.org/abs/2607.08601v1)
  <details><summary>📄 Abstract</summary>
  Sparsely-activated Mixture-of-Experts (MoE) language models achieve remarkable inference efficiency by activating only a small fraction of parameters per token, yet their full expert banks reside in memory at all times, creating a prohibitive deployment bottleneck. Existing structured pruning methods, largely designed for dense transformers, assess expert importance using locally derived heuristics that are blind to the interdependent nature of MoE routing. We introduce MAESTRO (Markov-chain App...
  </details>

- **2026-07-09** — Irina Vorobeva, Maxime Lenormand, Germana Berlantini et al. — [The geopolitics of knowledge: tipping points, national fingerprints, and the unequal globalization of science](http://arxiv.org/abs/2607.08512v1)
  <details><summary>📄 Abstract</summary>
  Science is often portrayed as a universal and self-contained system, driven solely by the internal logic of knowledge accumulation and isolated from the turbulences of the socio-political world. In this paper, we challenge this narrative by providing systematic quantitative evidence that the global scientific ecosystem is deeply shaped by geopolitical transformations. Using a large-scale dataset of scientific publications drawn from the OpenAlex database, spanning over five decades and covering ...
  </details>

- **2026-07-09** — Shenghui Chen, Po-han Li, Ximeng Sun et al. — [VEGAS: Human-Aligned Video Caption Evaluation via Gaze](http://arxiv.org/abs/2607.08489v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models excel at video captioning, yet typically generate descriptions that fail to capture individual viewers' attention. We propose VEGAS (Video caption Evaluation via GAze Score), a training-free metric that leverages test-time gaze to sample personalized, attention-aligned text. It is a cross-modal, information-theoretic metric that quantifies how well a candidate caption matches a viewer's focus. To evaluate VEGAS, we curate a dataset of egocentric activities and instructiona...
  </details>

- **2026-07-09** — Weiming Sheng, Jinlang Wang, Manuel Barros et al. — [GitLake: Git-for-data for the agentic lakehouse](http://arxiv.org/abs/2607.08319v1)
  <details><summary>📄 Abstract</summary>
  We present GitLake, a Git-for-data design for an agent-first lakehouse. The system lifts single-table Iceberg snapshots into lakehouse-wide commits, branches, and merges, letting agents work on isolated branches while humans review and publish changes. Pipelines run on temporary branches and publish through a final merge, so all outputs become visible atomically or none do. Finally, we report production lessons as well as correctness insights from a preliminary Alloy model of our core abstractio...
  </details>

- **2026-07-09** — Gabriel Matos, Lauren Larson, Abhilasha Dave et al. — [Transformer-based machine learning using low-level calorimeter signals for collimated photon identification at collider experiments](http://arxiv.org/abs/2607.08175v1)
  <details><summary>📄 Abstract</summary>
  Electromagnetic calorimeters provide essential information for reconstructing and selecting both Standard Model (SM) and potential beyond the SM physics events at high-energy particle colliders. The fine-grained segmentation of modern calorimeters captures rich information about the internal structure of particle showers, much of which is discarded by conventional high-level reconstruction methods. In this work, we leverage calorimeter cell-level information to classify highly collimated diphoto...
  </details>

- **2026-07-09** — Fan Ma, Mauro Giuffrè, Donald Wright et al. — [A safety-oriented hypothetico-deductive framework for AI-assisted differential diagnosis](http://arxiv.org/abs/2607.08038v1)
  <details><summary>📄 Abstract</summary>
  Diagnostic error is a major threat to patient safety, yet current large language model (LLM) systems often treat diagnosis as a one-shot prediction task, lacking safeguards against missed high-risk alternatives or rigorous verification of their reasoning. Here, we present AegisDx, a safety-oriented framework for hypothetico-deductive clinical reasoning. AegisDx coordinates specialized LLM components through role-specific contracts, structured intermediate outputs, evidence-retrieval interfaces, ...
  </details>

- **2026-07-09** — Sutanay Choudhury, Anwesha Banerjee, Udishnu Sanyal et al. — [Reaction-network reasoning with frontier models for experimentally confirmed catalyst-selectivity hypotheses](http://arxiv.org/abs/2607.08003v1)
  <details><summary>📄 Abstract</summary>
  Catalysts are essential for sustainable chemical manufacturing, yet discovering novel architectures remains a bottleneck dominated by trial-and-error experimentation and computationally intensive screening. In complex reactions such as electrochemical carbon dioxide reduction, product selectivity is governed by dynamic interfacial, electrolyte, and potential factors as well as kinetic pathway competition. Conventional descriptor-based machine learning and computational potentials struggle to res...
  </details>

- **2026-07-09** — T. Zalewski, M. S. Mrudul, Y. Lee et al. — [A crystal-field route to THz-driven magnetization](http://arxiv.org/abs/2607.08519v1)
  <details><summary>📄 Abstract</summary>
  Light carries angular momentum, but the microscopic pathways that transform it into magnetization remain elusive. Here we establish that crystal-field excitations, historically viewed primarily as equilibrium spectroscopic fingerprints of localized 4$f$ electrons, constitute an active microscopic route through which circularly-polarized terahertz (THz) light creates magnetic polarization. Using wavelength-selective ultrafast Faraday spectroscopy on the paramagnetic insulator CeF$_3$, we show tha...
  </details>

- **2026-07-09** — Zi-han Ding, Ziwei Wang — [SkillPlug: Unsupervised Skill Mining for Few-Shot Adaptation in Robotic Manipulation](http://arxiv.org/abs/2607.08354v1)
  <details><summary>📄 Abstract</summary>
  Learning transferable visuomotor imitation policies that generalize across diverse manipulation tasks and adapt rapidly to new tasks from only a handful of demonstrations remains challenging. Most modern policies are trained end-to-end to map observations directly to low-level actions, offering little explicit structure for reusing and recombining behaviors across tasks and making transfer data-inefficient under limited supervision. We propose SkillPlug, a plug-in framework that augments an exis...
  </details>

- **2026-07-09** — Aditya Aladangady, Ricardo Duque Gabriel, Carlo Wix — [Measuring Consumption with Credit Card Data: Benchmarking and Beyond](http://arxiv.org/abs/2607.08759v1)
  <details><summary>📄 Abstract</summary>
  We introduce a novel monthly county-level consumption dataset constructed from spending data on over 350 million credit cards in the Federal Reserve's Y-14M reports, covering over 3,000 U.S. counties since 2014. We first show that the data closely approximate traditional consumption measures, explaining 92 percent of the variation in monthly adjusted personal consumption expenditures (PCE) growth at the national level and capturing meaningful cross-sectional variation in annual adjusted PCE grow...
  </details>

- **2026-07-09** — Baha Rababah, Cuneyt Gurcan Akcora, Carson K. Leung — [The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs](http://arxiv.org/abs/2607.08734v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization is widely used to deploy large language models in resource-constrained settings, yet its evaluation relies almost exclusively on accuracy and perplexity. We show that these metrics fail to capture behavioral changes induced by quantization. We introduce correctness agreement, a decision-level metric that measures overlap in correct predictions between a base model and its quantized variants, independent of absolute accuracy. Across multiple models and quantization sche...
  </details>

- **2026-07-09** — Chuning Zhu, Eva Xu, Jose Barreiros et al. — [Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference](http://arxiv.org/abs/2607.08724v1)
  <details><summary>📄 Abstract</summary>
  Human decision-making is highly flexible -- some actions are taken immediately; others require longer deliberation. Language models have exhibited a similar capacity for adaptive "reasoning." However, transferring this capability to continuous control policies has been challenging, as directly reasoning in language space may lack the granularity for spatial understanding and precise motions. In this work, we show that reasoning for control policies can emerge by organizing information in an auto...
  </details>

- **2026-07-09** — Xiaoshuai Song, Liancheng Zhang, Kangzhi Zhao et al. — [WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search](http://arxiv.org/abs/2607.08662v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based web search agents are transforming information seeking from simple factoid question answering into complex, deep-and-wide search and research-oriented tasks. A single ReAct-style agent is constrained by one long trajectory and limited context, making it difficult to handle depth and coverage simultaneously. Existing multi-agent systems improve search coverage through parallel execution and aggregation, but still exhibit clear limitations in recursive depth, colla...
  </details>

- **2026-07-09** — Corinna Dannert, Pablo M. Blanco, Sebastian P. Pineda et al. — [Short Peptide Tails Modulate DNA Association and Condensation by PAMAM Dendrimers](http://arxiv.org/abs/2607.08623v1)
  <details><summary>📄 Abstract</summary>
  Poly(amidoamine) (PAMAM) dendrimers are promising candidates for nucleic acid delivery; however, biocompatibility and transfection efficiency remain a challenge. Here, we investigated how the composition of short peptide tails conjugated to generation 2 PAMAM (G2) dendrimers influence DNA association and condensation across a range of pH values. Using a combination of potentiometric titrations, DNA precipitation assays, and coarse-grained molecular simulations with charge regulation, we show tha...
  </details>

- **2026-07-09** — Trinity Rosebud Stenhouse, Chamkaur Ghag, Frank F. Deppisch — [The 20 GeV Galactic Halo Excess: Pixel-Level Confirmation and Consistency with Sub-TeV WIMP Annihilation](http://arxiv.org/abs/2607.08552v1)
  <details><summary>📄 Abstract</summary>
  A recent analysis of 15 years of Fermi-LAT data reported a spherically symmetric, halo-like component of the Galactic diffuse emission that peaks near 20GeV. We independently reproduce this cell-aggregated analysis, then extend it to a pixel-level likelihood on the native $0.125^\circ$ maps, adding energy-dependent point-spread-function forward folding and masking bright sources. Both methods replicate the 20GeV halo spectrum, with the pixel-level normalisation ${\sim}20\%$ above the cellwise fi...
  </details>

- **2026-07-09** — Harrison Grodin, Ethan Chu, Runming Li et al. — [Potential Functions as Types](http://arxiv.org/abs/2607.08547v1)
  <details><summary>📄 Abstract</summary>
  Amortized analysis can be framed from the physicist's view, amenable to manual verification in dependent type theory using potential functions, and the banker's view, amenable to automated inference in substructural type theory using type-level credit annotations. In this work, we synthesize these perspectives in Calf, a dependent type theory cost verification. From the physicist's view, we present a fracture and gluing theorem that renders every type as containing a fusion of an abstraction fun...
  </details>

- **2026-07-09** — Yanpeng Su, Norman Franchi, Maximilian Lübke — [Fundamental Sensing Limits of 6G Cooperative MIMO-ISAC Networks: Joint Position-Velocity CRLB and Decoupling Analysis](http://arxiv.org/abs/2607.08510v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a Cramér-Rao lower bound (CRLB)-based performance bound analysis of cooperative multiple-input multiple-output (MIMO) integrated sensing and communications (ISAC) networks. We first show the CRLB transformation of the signal-level parameters to the state parameters (position and velocity) in cooperative ISAC networks. Unlike existing studies that primarily ignored coupling between position and velocity in the Fisher information matrix (FIM), we derive the full FIM and the cor...
  </details>

- **2026-07-09** — Paula Font Solà, Adrià Molina Rodríguez, Josep Lladós — [Conversational Retrieval and On-the-Fly Knowledge Modeling of Historical Penitentiary Repression Records](http://arxiv.org/abs/2607.08459v1)
  <details><summary>📄 Abstract</summary>
  Recent developments in digital libraries increasingly favor conversational and natural language access to information through Retrieval-Augmented Generation (RAG). Although these approaches are effective for extractive tasks grounded in individual records, they remain limited in their ability to interpret document collections holistically and to incorporate expert knowledge dynamically. In this article, we present a document analysis system designed for the management of historical digital libra...
  </details>

- **2026-07-09** — Sebastian G. Gruber, Nassim Walha, Francis Bach et al. — [Eigenvalue Calibration for Semantic Embeddings of Large Language Models](http://arxiv.org/abs/2607.08377v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty quantification is central to the reliable deployment of large language models (LLMs), and eigenvalues of semantic embeddings have recently emerged as a key tool in state-of-the-art methods. However, conventional calibration results developed for classification probabilities cannot be directly transferred to eigenvalues. We address this gap by proposing a novel framework for calibrating the eigenvalues of semantic embeddings. We interpret LLMs combined with semantic embeddings of thei...
  </details>

- **2026-07-09** — Amir Asiaee — [Certified Interventional Fidelity: Anytime-Valid, Adaptive Evaluation of Causal Claims in Mechanistic Interpretability](http://arxiv.org/abs/2607.08349v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability often evaluates explanations by intervening on a model: swapping hidden states, patching activations, ablating components, or comparing a compressed model to the original one. These experiments are usually summarized by a point estimate, even though the evaluation may be monitored while it runs or adapted toward suspected failures. This makes it hard to tell whether a reported fidelity or patching effect is a stable causal claim or a consequence of finite sampling an...
  </details>

- **2026-07-09** — Kaustubh Kumar, Ashutosh Ranjan, Vivek Srivastava et al. — [ArtMine: Discovering and Formalizing Artistic Processes](http://arxiv.org/abs/2607.08331v1)
  <details><summary>📄 Abstract</summary>
  Understanding how artworks are created requires reasoning about the iterative decisions, material operations, and contextual influences that shape artistic production. While recent generative AI systems can synthesize artworks with high fidelity, they primarily model distributions over finished artifacts rather than the creative processes underlying their creation. In practice, artistic workflows are only partially documented through fragmented sources such as archival records, preparatory studi...
  </details>

- **2026-07-09** — Yuxiang Feng, Juncheng Wang, Chao Xu et al. — [Progression as Latent Drift: Generative Forecasting of Slow-Evolving Pathologies](http://arxiv.org/abs/2607.08270v1)
  <details><summary>📄 Abstract</summary>
  Forecasting the future anatomy of slow-evolving neurodegenerative diseases could enable earlier, more targeted intervention and improve clinical trial design, but it remains challenging because true progression signals are subtle in longitudinal MRI. In this low-signal regime, transferring modern generative sequence models directly is unreliable: training is dominated by stable baseline anatomy and confounded by dense, sample-specific nuisance variation. We first provide a theoretical analysis t...
  </details>

- **2026-07-09** — B. Maheshwari, P. Stevenson, P. Van Isacker — [Full-Spectrum Quantum Simulation for the Nuclear Shell Model](http://arxiv.org/abs/2607.08235v1)
  <details><summary>📄 Abstract</summary>
  The nuclear shell model is a general way of expressing the many-body nuclear Hamiltonian and deciphering the underlying nuclear structure. In today's era of modern and high-power computation, the primary limitation of the nuclear shell model is the enormous dimensionality of its Hilbert space, which far exceeds available storage capacity and prevents the diagonalization of the full Hamiltonian matrix in that space. Quantum computing offers a scalable solution to bypass this curse of dimensionali...
  </details>

- **2026-07-09** — Sumit Satishrao Shevtekar, Chandresh Kumar Maurya — [RhyMix: A Lightweight Adaptive Multi-Rhythm Network for Long-Term Time Series Forecasting](http://arxiv.org/abs/2607.08234v1)
  <details><summary>📄 Abstract</summary>
  Real-world time series exhibit complex dynamics characterized by multiple simultaneous temporal patterns: short-term fluctuations, periodic seasonal cycles, long-term trends, and irregular abrupt changes. However, many existing forecasting architectures rely on single-path temporal modeling--transformers capture long-range dependencies but smooth local variations, convolutions capture local patterns but have limited receptive fields, and linear models are efficient but cannot capture nonlinear d...
  </details>

- **2026-07-09** — David Serrano-Lozano, Luis Herranz, Michael S. Brown et al. — [Leveraging Color Naming for Image Enhancement](http://arxiv.org/abs/2607.08185v1)
  <details><summary>📄 Abstract</summary>
  Enhancing images to make them visually appealing is a persistent challenge in computer vision. Many deep-learning methods train models on paired datasets to replicate expert editing styles. However, these approaches struggle with two key issues: (1) interpretability and (2) a parametrization suitable for user adjustments. To address these challenges, we present NamedCurves+, an approach inspired by the concept of Color Naming, a universal set of familiar colors widely used in software tools for ...
  </details>

- **2026-07-09** — Kaihua Ding — [When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement as Confidence Signals](http://arxiv.org/abs/2607.08065v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-judge (Zheng et al., 2023) is increasingly the default for evaluating AI systems in enterprise pipelines, often scaled to ensembles (Verga et al., 2024) or "mixture-of-experts" (Shazeer et al., 2017) panels of judges. These systems share a key assumption: that consistency -- agreement among judges, or among a model's own samples -- indicates correctness. We show this assumption is unreliable. Agreement is not accuracy: a model can agree with itself, and different models can agree with eac...
  </details>

- **2026-07-09** — Xiucheng Wang, Junxi Huang, Nan Cheng — [RadioDiff-v2: Generative Angular Radio Maps for Multi-Beam Selection and Localization](http://arxiv.org/abs/2607.08045v1)
  <details><summary>📄 Abstract</summary>
  Angular radio maps describe the received-power distribution over the angle of arrival and underpin beam selection and receiver localization in sixth-generation (6G) networks. Predicting the angular power spectrum (APS) from geometry is difficult, because the mapping is ill-posed in non-line-of-sight (NLOS) conditions and must generalize to unseen environments. Distortion-minimizing regressors return the conditional mean, which over-smooths the spectrum and erases the multipath structure that dow...
  </details>

- **2026-07-08** — Shyam Agarwal, Courtney Miller, Christian Kästner et al. — [3100 Opinions on Code Review in an AI World: Building Causal Theory from Practitioner Discourse](http://arxiv.org/abs/2607.07980v1)
  <details><summary>📄 Abstract</summary>
  Coding agents now author entire pull requests, and practitioners sharply disagree about what this does to code review: whether it becomes the bottleneck, whether human review is still necessary, and whether it quietly erodes the understanding that it once built. Repository-mining studies measure surface trends but seldom explain the mechanisms beneath them, and the trends themselves prove unstable. A motivating observational analysis of public GITHUB activity finds that agent-authored pull reque...
  </details>

- **2026-07-08** — Luke Baines, Anton Gonzalvez Hawthorne, Mariia Koroliuk et al. — [Persona Cartography: Charting Language Model Personality Traits in Weight Space](http://arxiv.org/abs/2607.07916v1)
  <details><summary>📄 Abstract</summary>
  Large language models exhibit recurring behavioural patterns -- personas -- that shape generalisation and safety, but we lack reliable tools for decomposing, measuring, and controlling them. Our central insight is to treat personas as positions in a space of behavioural traits, using the OCEAN framework to describe model personas in terms of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. We train low-rank adapters to amplify or suppress individual traits, and evaluate...
  </details>

- **2026-07-08** — Xiaohan Zhang, Sebastian Starke, Alexander Winkler et al. — [GIRAF: Towards Generalizable Human Interactions with Articulated Objects](http://arxiv.org/abs/2607.07880v1)
  <details><summary>📄 Abstract</summary>
  Synthesizing realistic full-body human interactions with articulated objects is a fundamental challenge for embodied AI and graphics, with applications in robotics training and virtual agents. Existing models remain limited: some focus on simple activities with static objects, while others restrict attention to hand-only manipulation. This leaves open the problem of generating coordinated full-body motion that approaches, manipulates, and moves articulated objects in a realistic and generalizabl...
  </details>

- **2026-07-08** — Shengyuan Zhao — [On cube and Cremona rigidity for higher-rank lattices](http://arxiv.org/abs/2607.07940v1)
  <details><summary>📄 Abstract</summary>
  For irreducible lattices in semisimple Lie groups of real rank at least $2$, we prove a cohomological vanishing result implying that any action on a CAT(0) cube complex fixes a vertex whenever every hyperplane stabilizer is solvable. As an application, we prove regularizability for actions of all higher-rank lattices by birational transformations on projective surfaces. We first use superrigidity for actions on infinite-dimensional real hyperbolic spaces to reduce to the de Jonquières group, and...
  </details>

- **2026-07-08** — Weicheng Ma, John Guerrerio, Soroush Vosoughi — [Scalable and Culturally Specific Stereotype Dataset Construction via Human-LLM Collaboration](http://arxiv.org/abs/2607.07895v1)
  <details><summary>📄 Abstract</summary>
  Research on stereotypes in large language models (LLMs) has largely focused on English-speaking contexts, due to the lack of datasets in other languages and the high cost of manual annotation in underrepresented cultures. To address this gap, we introduce a cost-efficient human-LLM collaborative annotation framework and apply it to construct EspanStereo, a Spanish-language stereotype dataset spanning multiple Spanish-speaking countries across Europe and Latin America. EspanStereo captures both w...
  </details>

- **2026-07-08** — S M Farah Al Fahim, Md Nakhla Rafi, Md Ahasanuzzaman et al. — [Bug Report Specification Refinement with Trajectory Guidance for Automated Program Repair](http://arxiv.org/abs/2607.07882v1)
  <details><summary>📄 Abstract</summary>
  Bug reports serve as task specifications for repository-level automated program repair (APR) agents, but they often describe only the observed failure and omit repair-relevant information such as the failure-inducing behavior, behavioral requirement, and implementation scope. As a result, a repair agent may inspect irrelevant code, infer an incorrect requirement, or generate a patch that addresses the reported symptom without restoring the intended repository behavior. We present TrajSpec, a tra...
  </details>

- **2026-07-08** — Alessio Emanuele Biondo, Mauro Gallegati — [Inflation as an emergent phenomenon](http://arxiv.org/abs/2607.07864v1)
  <details><summary>📄 Abstract</summary>
  We develop an agent-based model in which inflation emerges from decentralized price-setting and credit-financed production in an endogenous-money economy. Firms operate under working-capital constraints, form market-based price expectations through heterogeneous adaptive learning, and set prices via cost-plus rules with endogenous mark-ups. Bank lending simultaneously creates deposits, while heterogeneous lending rates and credit rationing shape firms' financing costs and, through unit costs, th...
  </details>

- **2026-07-08** — Gaurav Arya, Mathieu Huot, Moritz Schauer et al. — [GradInf: Gradient Estimation as Probabilistic Inference](http://arxiv.org/abs/2607.07840v1)
  <details><summary>📄 Abstract</summary>
  Gradient estimation -- the task of computing the gradient of the expected value of a probabilistic program -- has diverse applications in scientific computing, but is notoriously difficult because of issues such as high-dimensional integration, discrete random choices, and complex stochastic dependencies. This article introduces gradient inference, a new approach to developing sound and efficient gradient estimators for probabilistic programs. Gradient inference rests on a formal reduction from ...
  </details>

- **2026-07-08** — Jingyao Cai, Shuaijun Liu, Abdul Rehman et al. — [From Triggers to Emotions: A CPM-Grounded Appraisal Multi-Agent for Dynamic Emotional Evolution in Persona-Based Dialogue](http://arxiv.org/abs/2607.07824v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have substantially advanced persona-based dialogue agents for emotion-sensitive role simulation in healthcare, education, counseling, customer service, and interactive storytelling. However, two related lines of work leave a key gap. Persona-based dialogue systems often encode emotions as static traits or surface-level stylistic cues, and affective dialogue research has largely focused on empathetic response generation toward users rather than modeling the agent pers...
  </details>

- **2026-07-08** — Osman Cevheroğlu, Arkadaş Özakın — [An analytical solution of a quantum system with non-Markovian behavior: The Bixon-Jortner system in time domain](http://arxiv.org/abs/2607.07546v1)
  <details><summary>📄 Abstract</summary>
  Non-Markovian behavior in quantum systems is often studied in the context of bipartite systems consisting of a system of interest and an environment -- tracing over the environment results in non-Markovian behavior for the subsystem of interest. One may get a Markovian limit in certain regimes, which is studied using the Lindblad master equation, and corrections to this behavior can be obtained by techniques such as the Nakajima-Zwanzig formalism. In this paper, we obtain an exact non-Markovian ...
  </details>

- **2026-07-08** — Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. — [Infinite Worlds with Versatile Interactions](http://arxiv.org/abs/2607.07534v1)
  <details><summary>📄 Abstract</summary>
  We present LingBot-World 2.0 (also known as LingBot-World-Infinity), an advanced iteration of LingBot-World featuring four distinct upgrades. (1) Our model achieves an unbounded interaction horizon while maintaining consistent output quality, benefiting from a carefully crafted causal pretraining paradigm. (2) Through distilling a real-time variant from the base model, our system guarantees rapid response time, sufficient to drive 720p video streams at 60 fps. (3) Compared to the previous versio...
  </details>

- **2026-07-08** — Tamal Maharaj — [A Word-Level Digital Reader of the Prasthanatrayi with Sankara's Bhasya: Corpus, Method, and an Open, Offline Reading Aid for the Advaita Vedanta Canon](http://arxiv.org/abs/2607.07282v1)
  <details><summary>📄 Abstract</summary>
  The Prasthanatrayi -- the ten principal Upanisads, the Brahmasutra, and the Bhagavadgita, with Sankara's commentaries (bhasya) -- is the foundational corpus of Advaita Vedanta. Continuous euphonic combination (sandhi), long compounds (samasa), and dense scholastic prose make it hard to read at the word level: where one word ends, and what each word means grammatically, are both obscured. We present an open, fully offline, word-level digital reader of the entire Prasthanatrayi with Sankara's bhas...
  </details>

- **2026-07-08** — Jerry Han, Rafael Moschopoulos, Ella Colby et al. — [Measuring Intelligence Beyond Human Scale](http://arxiv.org/abs/2607.07040v1)
  <details><summary>📄 Abstract</summary>
  How can we measure intelligence beyond human capability?   Human-authored benchmarks saturate, and above human capability, examiners may not know which tasks are both hard and verifiable. We argue that this difficulty is inherent to absolute-scale evaluation and propose a new paradigm based on relative measurement in which models generate public challenges that separate other systems. Aggregating these outcomes yields an adversarial psychometric rating system that can scale with the systems bein...
  </details>

- **2026-07-08** — Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi — [The Key to Going Linear: Analysis-Driven Transformer Linearization](http://arxiv.org/abs/2607.07706v1)
  <details><summary>📄 Abstract</summary>
  The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality. This work isolates the effect of state update design in a strict frozen-backbone regime. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style networks outperform purely gated accumulation. We identify a potential source of ...
  </details>

- **2026-07-08** — Si-Yu Yuan, Wen-Tan Xue, Ching Hua Lee — [Non-Hermitian Edge State Endocytosis](http://arxiv.org/abs/2607.07703v1)
  <details><summary>📄 Abstract</summary>
  An isolated edge state observed in a finite open chain is usually expected to survive the thermodynamic limit (TDL), with a localization mechanism distinct from non-Hermitian skin accumulation, which localizes the \emph{entire} bulk continuum. We show that scale-sensitive non-Hermitian systems can generically admit a different fate: as we scale up the system size, a detached edge-localized eigenstate can remain sharply visible over a broad window until a critical scale is reached, where it forms...
  </details>

- **2026-07-08** — Tianming Sha, Yue Zhao, Lichao Sun et al. — [SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI Agents](http://arxiv.org/abs/2607.07676v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents can execute complex tasks with limited human review, yet they often lack the grounded operational knowledge to make their outputs not just executable but correct, secure, and maintainable. We introduce SkillCenter, to our knowledge the largest open skill library for agents by total count: 216,938 structured skills across 24 domain bundles. A SkillGate-filtered pipeline contributes 114,565 source-grounded skills from peer-reviewed journals, ArXiv, and over 24,000 technical so...
  </details>

- **2026-07-08** — Halimat Olamide Yusuf, Augustine O. Nwajana — [Six-Pole Dual-band Bandpass Filter for WiMAX Applications](http://arxiv.org/abs/2607.07661v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multi-band wireless communication systems have driven the increasing need for dual-band bandpass filters. These types of filters are capable of isolating a small section of the frequency spectrum within a broader spectrum. Over the years, coplanar waveguide, microstrip, slotline, stripline, and other planar transmission line technologies have been widely employed in the design of microwave circuits and systems. This work employs a Folded-Arms Square Open-Loop Resonator (FASOLR...
  </details>

- **2026-07-08** — Azwar Abdulsalam, Nishil Patel, Andrew Saxe — [RL Post-Training Builds Compositional Reasoning Strategies](http://arxiv.org/abs/2607.07646v1)
  <details><summary>📄 Abstract</summary>
  Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable rewrite-grammar environment where the pretraining distribution is known and every generated rewrite can be audited. A Transformer is pretrained on primitive symbol-rewrite chains and post-trained on a Trace-based reasoning task with only a binary final-answer reward. RL solves held-out problems that...
  </details>

- **2026-07-08** — Aneesh Ramaswamy, Nageswara S. V. Rao, Joseph C. Chapman et al. — [Analysis of polarization drift of optical signals over deployed aerial-inground fiber connections](http://arxiv.org/abs/2607.07629v1)
  <details><summary>📄 Abstract</summary>
  Polarization measurements of a classical 1550-nm signal are collected and analyzed on 15-km hybrid aerial-inground fiber connections over 11 months. The spectral area and spectral moments9 of mHz-resolution Fast-Fourier-Transform (FFT) of these measurements are extracted, and related to temperature, humidity, wind speed, and time of day. Spectral area correlations show a strong11 diurnal structure: daytime maxima align with temperatures/wind speed peaks and humidity dips, with lower levels durin...
  </details>

- **2026-07-08** — Lara Khatib, Noble Saji Mathews, Meiyappan Nagappan et al. — [What Makes a Good Bug Report for an AI Agent?](http://arxiv.org/abs/2607.07593v1)
  <details><summary>📄 Abstract</summary>
  Automated program repair (APR) agents are transitioning from research benchmarks to developer workflows, yet they still begin with bug reports written for human developers. While decades of research have established what makes a good bug report for humans (e.g., steps to reproduce, stack traces), it remains unclear whether these features transfer to LLM-based agents. We study this question in two analyses. First, we use statistical modeling to examine associations between 27 bug-report features ...
  </details>

- **2026-07-08** — Dmitry Beresnev, Vladimir Makharev, Roman Khalikov et al. — [Search, Fail, Recover: A Training Framework for Correction-Aware Reasoning](http://arxiv.org/abs/2607.07492v1)
  <details><summary>📄 Abstract</summary>
  Many reasoning tasks are not well described by a single left-to-right chain: a solver may need to pursue a plausible branch, observe delayed failure, and return to the latest prefix that can still be completed. We introduce Pyligent, a training and inference framework inspired by the Diligent Learner formulation that represents reasoning as validated search over partial solution chains. A task validator labels generated continuations and failures, and the resulting search trees are converted int...
  </details>

- **2026-07-08** — Songhan Wang, Haoang Chi, He Li et al. — [SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis](http://arxiv.org/abs/2607.07467v1)
  <details><summary>📄 Abstract</summary>
  Spatial and Single-cell transcriptomics are transformative in deciphering cellular dynamics. As the fundamental paradigm for reconstructing cell developmental paths, trajectory inference (TI) is critical. However, existing methods require extensive manual intervention and proficiency in heterogeneous tools, posing a significant barrier to efficient TI analysis. To bridge this gap, we propose SpaCellAgent, an autonomous large language model (LLM) multi-agent framework that automates end-to-end sp...
  </details>

- **2026-07-08** — Xing Zhang, Yanwei Cui, Guanghui Wang et al. — [The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents](http://arxiv.org/abs/2607.07436v1)
  <details><summary>📄 Abstract</summary>
  A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library from drifting below the no-skill baseline, but its guarantee assumes an unbiased reward, which is false for the LLM judges that reference-free tasks force upon us. We show that a biased judge does not merely add noise; it \emph{silently switches off the curator}. We make this precise with a corrupted...
  </details>

- **2026-07-08** — Kajetan Rachwał, Maciej Majek, Bartłomiej Boczek et al. — [Multi-Agent Robotic Control with Onboard Vision-Language Models](http://arxiv.org/abs/2607.07403v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial wa...
  </details>

- **2026-07-08** — Elaine Ang, Chenxi Huang, Georgios Liargkovas et al. — [Agentic Data Environments](http://arxiv.org/abs/2607.07397v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents promise substantial gains in speed, scale, and labor efficiency, but their failures can impose abrupt and often irreversible costs. The central challenge for agentic automation is therefore to increase the benefits of automation while bounding the consequences of failure.   While databases remain central to modern computing, agents operate over a broader data environment spanning files, APIs, applications, and system state. In this talk, I will outline early work on Agentic Dat...
  </details>

- **2026-07-08** — Diab W. Abueidda, Bilal Ahmed, Panos Pantidis et al. — [Physics-Audited Agentic Discovery in Scientific Machine Learning](http://arxiv.org/abs/2607.07379v1)
  <details><summary>📄 Abstract</summary>
  In agentic scientific machine learning (SciML), large language model (LLM) agents can discover surrogate models and select one by an automated score, typically an error metric. A low error, however, does not establish that the predicted fields satisfy the physics that matter for mechanics, such as boundary conditions, superposition, stiffness scaling, or causality. We introduce Physics-Audited Agentic SciML (PA-SciML), a verification-first workflow for agentic SciML discovery. The workflow fixes...
  </details>

- **2026-07-08** — Pranav Sawant, Jakub Krejčí — [Mechanistic Interpretability for Neural Networks: Circuits, Sparse Features and Symbolic Reasoning](http://arxiv.org/abs/2607.07316v1)
  <details><summary>📄 Abstract</summary>
  This article offers a comprehensive overview of mechanistic interpretability, an emerging field that seeks to reverse-engineer the internal algorithms of modern neural networks. While traditional explainable AI methods often stop at surface-level input-output correlations, this approach directly addresses the opaque "black box" nature of machine learning models, which is essential for ensuring safety and auditability in high-stakes deployments. The paper provides a detailed examination of Transf...
  </details>

- **2026-07-08** — Arianna Pera, Mauro Martino, Nima Dehmamy et al. — [Billions of Sketches Reveal Hidden Cultural Variation in Human Concepts](http://arxiv.org/abs/2607.07267v1)
  <details><summary>📄 Abstract</summary>
  Claims about the universality of human concepts have been predominantly assessed through linguistic similarity across languages and cultures. However, words are effective as communication devices because they compress rich experiential variation into shared conventions, potentially obscuring hidden individual and cultural differences in how concepts are mentally represented. Here, we analyse 2.6 billion human-made sketches of common concepts from 236 countries and territories to examine conceptu...
  </details>

- **2026-07-08** — Zhenghao Zhou, Yiyan Li, Tao Xu et al. — [A Physics-guided Fine-tuned LLM-based Framework for Customized Power Distribution System Feeder Generation](http://arxiv.org/abs/2607.07237v1)
  <details><summary>📄 Abstract</summary>
  Power distribution system feeder models (e.g., IEEE 33-bus system, IEEE 13-bus system, etc.) are cornerstones for conducting power distribution system studies. As real-world feeder models are hard to acquire due to energy security concerns, generating high-quality synthetic feeders becomes an important alternative to satisfy the fast-growing and diversified needs of power system researchers and engineers. In this paper, we propose an LLM-based synthetic feeder generation framework that can achie...
  </details>

- **2026-07-08** — Jáchym Bártík, Alžběta Šrůtková, Irena Holubová — [Benchmark Engineering as a Design Instrument for Heterogeneous Information Systems](http://arxiv.org/abs/2607.07175v1)
  <details><summary>📄 Abstract</summary>
  Contemporary information systems operate in heterogeneous and continuously evolving data environments, where representation choices and structural redesign decisions strongly influence system behavior. Existing benchmarking approaches, however, rely mostly on static datasets and fixed schemas, providing limited support for analyzing architectural trade-offs or guiding evolution in multi-model settings.   This paper introduces TransforMMer, a framework for evolution-aware and representation-aware...
  </details>

- **2026-07-08** — Rakshitha De Silva, Shiva Raj Pokhrel, Jonathan Kua — [Small Language Model-based Control for BBR over Low Earth Orbit Satellite Internet](http://arxiv.org/abs/2607.07142v1)
  <details><summary>📄 Abstract</summary>
  Low Earth Orbit (LEO) satellite Internet introduces rapid path variability, intermittent capacity shifts, and non-terrestrial delay dynamics that challenge transport-layer congestion control. Although Bottleneck Bandwidth and Round-trip propagation time (BBR) achieves high throughput in such environments, its aggressive bandwidth probing can cause excessive retransmissions and unstable pacing over LEO links. This paper presents a global experimental evaluation of BBR over a SpaceX Starlink testb...
  </details>

- **2026-07-08** — Stepanida Alekseeva, Jenifer Kalafatovich, Seong-Whan Lee — [Tree-of-Thoughts Reasoning for Text-to-Image In-Context Learning](http://arxiv.org/abs/2607.07117v1)
  <details><summary>📄 Abstract</summary>
  In text-to-image in-context learning (T2I-ICL), a model has to infer a latent compositional pattern from fewshot demonstrations for generating a query image. Recent studies show that state-of-the-art multimodal large language models struggle with this setting, particularly due to limited compositional reasoning and sensitivity to prompt construction. In this work, we propose a Tree-of-Thoughts (ToT) reasoning framework for T2I-ICL that introduces a multi-stage reasoning and selection layer that ...
  </details>

- **2026-07-08** — Heye Huang, Jingguang Li, Zhiyuan Zhou et al. — [A knowledge-augmented dataset of high-risk driving scenarios with LLM annotations for autonomous driving](http://arxiv.org/abs/2607.07103v1)
  <details><summary>📄 Abstract</summary>
  Safe autonomous driving requires both rapid responses to common high-risk events and deeper reasoning over rare, extreme long-tail scenarios in traffic safety. These scenarios are severely under-represented in naturalistic driving data, and existing trajectory and language-augmented datasets seldom provide high-risk event labels, semantic annotations, and verifiable safety signals. Here we present K-Risk, a knowledge-augmented dataset that combines structured driving trajectories with large lang...
  </details>

- **2026-07-08** — Szczepan Konior, Alexandre Quemy, Przemysław Klocek et al. — [Riemannian Geometry for Pre-trained Language Model Embeddings](http://arxiv.org/abs/2607.07047v1)
  <details><summary>📄 Abstract</summary>
  Understanding the geometric structure of pre-trained language model embeddings matters for interpretability and safety. We ask whether sentence-level classification signal lives in the Riemannian geometry of contextual token embeddings, and probe it by extracting per-token pullback metrics from a learned encoder's analytical Jacobian and aggregating them with the Fréchet mean on the symmetric positive definite (SPD) manifold; we call this procedure Riemannian Mean Pooling (RMP). Across three dat...
  </details>

- **2026-07-08** — Yusen Feng, Bingchen Han, Jiangran Lyu et al. — [WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time](http://arxiv.org/abs/2607.06988v1)
  <details><summary>📄 Abstract</summary>
  Steering robot foundation models (RFMs) toward new task variants or user-preferred behaviors remains challenging, often requiring additional robot demonstrations, task-specific fine-tuning, or long-context conditioning. We present WAM-TTT, a test-time training framework for steering world action models from raw human videos. Rather than treating human videos as trajectories to imitate, WAM-TTT absorbs them into a lightweight adaptive memory inside a frozen WAM through self-supervised video predi...
  </details>

- **2026-07-08** — Amin Tabrizian, Arsyi Aziz, Aarifah Ullah et al. — [End-to-End LLM Flight Planning with RAG-based Memory and Multi-modal Coach Agent](http://arxiv.org/abs/2607.06964v1)
  <details><summary>📄 Abstract</summary>
  Bridging the gap between human pilot intent and autonomous flight operation is critical for real-world electric vertical takeoff and landing (eVTOL) aircraft deployment. Flight planning traditionally relies on classic algorithms that struggle to incorporate flexible human preferences. We present FRAMe, an End-to-End Large Language Model (LLM) Flight Planning tool with RAG-based Memory and Multi-modal Coach Agent. Our system integrates a planner LLM with a multi-modal coach agent and retrieval au...
  </details>

- **2026-07-08** — Yingshu Li, Yunyi Liu, Zhenghao Chen et al. — [Seeing What Matters: Lesion-Aware High-Resolution Patch Discovery and Fusion for Chest X-ray Report Generation](http://arxiv.org/abs/2607.06909v1)
  <details><summary>📄 Abstract</summary>
  Despite rapid advances in chest X-ray (CXR) foundation models, most radiology report generation (RRG) systems still rely on heavily downsampled inputs (e.g., 256x256) due to the fixed visual token budgets of pretrained vision encoders, suppressing subtle yet clinically important cues present in native-resolution images. However, enabling high-resolution (high-res) perception remains challenging: naive tiling causes prohibitive token inflation, while global compression suppresses subtle lesions a...
  </details>

- **2026-07-08** — Muayad Sayed Ali, Aliaksandra Novik, Anji Boddupally et al. — [The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI](http://arxiv.org/abs/2607.06906v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI development today runs on token maxing: buying capability with tokens -- longer reasoning traces, more turns, wider tool payloads, bigger replayed contexts -- so tokens per task grow faster than task value. Falling per-token prices mask the pattern; total spend rises anyway. We argue the decisive lever against token maxing is the harness: the orchestration layer that assembles context, exposes tools, sequences turns, delegates work, and carries enterprise observability and governance....
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 543 |
| prompt-injection | 452 |
| memory-poisoning | 36 |
| tool-use-attack | 91 |
| backdoor | 386 |
| adversarial-attack | 528 |
| privacy-leakage | 3673 |
| steganography | 52 |
| misuse | 809 |
| red-teaming | 107 |
| vulnerability | 2409 |
| defense | 2040 |
| alignment | 1879 |
| robustness | 1723 |
| watermark | 175 |
| unlearning | 82 |
| agent-safety | 48 |
| benchmark | 53 |
| survey | 244 |
| other | 5348 |

---

📚 **全部 20678 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-07-14 09:06:34*