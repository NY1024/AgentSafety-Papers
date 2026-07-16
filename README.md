<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-20868-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-16 02:42 ｜ **论文总数 / Total Papers**: 20868（近 30 天 / Recent 30 days: 3947）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 20868 篇论文（含摘要、分类筛选、搜索）/ View all 20868 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 545
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 453
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 36
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 91
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 386
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 530
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3682
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 52
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 812
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 108
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2427
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2064
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1890
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1778
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 181
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 82
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 48
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 53
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 244
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5406

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3947 篇，完整 20868 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3947 papers from the last 30 days (with date, authors & abstract). For the full list of 20868 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-07-14** — Roman Prosvirnin, Victor Minchenkov, Alexey Soldatov et al. — [Silent Alarm: A J-Space Protocol for Comparing Danger Recognition Across Models and Quantization Levels](http://arxiv.org/abs/2607.12792v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak-robustness research typically evaluates safety through generated responses using an LLM-as-judge approach. Such evaluations, however, are sensitive to the benchmark's grading procedure and capture only observed behavior on a given set of attacks, without directly revealing the hidden fragility of the underlying safety mechanisms. This work proposes JADR (Jacobian Assessment of Danger Recognition), a protocol that measures a model's internal representation through Jacobian space (J-spac...
  </details>

- **2026-07-13** — Ren-Yi Huang, Mingchen Li, Dumindu Samaraweera et al. — [Securing LLMs in the Wild: Privacy and Security Challenges at the Edge](http://arxiv.org/abs/2607.13088v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are rapidly moving from research settings into the wild, deployed on enterprise infrastructure, personal devices, and edge platforms. While cloud deployments offer scalable compute, concerns over data sovereignty, compliance, latency, and third-party dependence are driving organizations toward edge and on-premise LLMs. This shift introduces new security and privacy challenges: limited compute and memory force aggressive optimizations, including quantization, pruning,...
  </details>

- **2026-07-13** — Junyoung Park, Namgyu Park, Sechan Lee et al. — [MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment](http://arxiv.org/abs/2607.11070v1)
  <details><summary>📄 Abstract</summary>
  Modern large language models (LLMs) operate in interactive multi-turn settings, making multi-turn jailbreaking a realistic threat model and an important setting for automated red teaming. A core challenge in learning multi-turn jailbreak attackers is credit assignment: different turns contribute differently to the final outcome, yet existing learning signals are often too coarse to identify their individual contributions. We propose decomposed credit GRPO (DC-GRPO), a unified turn-level credit a...
  </details>

- **2026-07-09** — Jennifer Za, Julija Bainiaksina, Nikita Ostrovsky et al. — [Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring](http://arxiv.org/abs/2607.08066v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring is a promising safety mechanism for AI agents, based on the premise that visible reasoning traces can surface misaligned or deceptive behavior. While effective in standard scenarios, recent work highlights that LLMs remain vulnerable to persuasion-based jailbreaks, where natural-language arguments override model constraints. We stress-test whether this vulnerability extends to monitoring LLMs: can an adversarial agent persuade its CoT monitor to approve proposed...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 6 papers

- **2026-07-14** — Huihao Jing, Wenbin Hu, Shaojin Chen et al. — [Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions](http://arxiv.org/abs/2607.12406v1)
  <details><summary>📄 Abstract</summary>
  The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model. Consequently, safety is no longer only about input--output content alignment. It also concerns system behavior and real-world execution outcomes. However, the current literature is fragmented across attack types, applications, and benchmarks. This makes it hard to explain why failures such as prompt injection, tool misuse, and memory poisoning often share t...
  </details>

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


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 4 papers

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


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 6 papers

- **2026-07-15** — Michal Štefánik, Philipp Mondorf, Andreas Waldis et al. — [AIMO Interpretability Challenge](http://arxiv.org/abs/2607.13899v1)
  <details><summary>📄 Abstract</summary>
  We propose the AIMO Interpretability Challenge, a competition on distinguishing robust from spurious reasoning in frontier mathematical language models based on the models' internal mechanisms. The challenge is motivated by a central limitation of standard reasoning benchmarks: strong final-answer accuracy does not reveal whether a model relies on stable reasoning mechanisms or exploits brittle reasoning shortcuts. Building on AI Mathematical Olympiad (AIMO) problems and submissions, together wi...
  </details>

- **2026-07-14** — Yuxin Huang, Ziming Hong, Mingming Gong et al. — [Delving into the Temporal Challenges of Unified Video Protection Against Image-to-Video and Fine-Tuning-based Customization](http://arxiv.org/abs/2607.13336v1)
  <details><summary>📄 Abstract</summary>
  Recent diffusion-based video generation models have enabled high-quality personalized video customization through both tuning-based pipelines, which fine-tune a video diffusion model, and reference-based pipelines such as image-to-video generation. However, these capabilities raise serious concerns about personal privacy, identity ownership and intellectual property protection. Existing anti-customization works focus on protecting images, while protection for videos against both reference- and t...
  </details>

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


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 21 papers

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

- **2026-07-13** — Jing Liu, Chenxuanyin Zou, Jiayang Ren et al. — [Continual Learning with Elastic Regularization and Synthetic Replay for Federated MLLM Fine-Tuning](http://arxiv.org/abs/2607.12112v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning of Multimodal Large Language Models (MLLMs) across distributed networks enables privacy-sensitive adaptation to evolving data streams, yet a fundamental obstacle prevents robust deployment in dynamic environments: catastrophic forgetting, wherein sequential task updates erase previously acquired knowledge across visual, linguistic, and cross-modal representations. Addressing this challenge is especially critical for autonomous networked AI operating in safety-sensitive doma...
  </details>

- **2026-07-13** — Kartik Ghanshyambhai Pansuriya, Ehsan Ghorbani, Deepak Singh et al. — [Predicting Acceptance and Review Effort in Human and Agent Pull Requests](http://arxiv.org/abs/2607.12057v1)
  <details><summary>📄 Abstract</summary>
  Pull requests (PRs) are a central mechanism for reviewing and integrating code changes in modern software repositories. As AI coding agents begin to submit more code changes alongside human developers, maintainers face a new challenge: deciding which PRs are likely to be accepted and which ones may require substantial review effort. This paper studies whether such outcomes can be estimated at the time a PR is opened, before reviewer discussion, CI feedback, or merge decisions are available. Usin...
  </details>

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


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 14 papers

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


### 📂 red-teaming
*红队测试 / Red Teaming* — 3 papers

- **2026-07-14** — Yakov Pyotr Shkolnikov — [Composable Trust for Language Models: A proven boundary and a measured defense](http://arxiv.org/abs/2607.13149v1)
  <details><summary>📄 Abstract</summary>
  In a language model, instructions and data share one token stream, so nothing inside the model's generation can keep untrusted text from steering it. We develop a trust model that places the authority to act outside the model, in code: a source's standing, not its content, decides which operation runs and whether it acts. A lower-trust source may inform an answer but not override a higher one. An unmodified model runs inside a deterministic pipeline that ranks inputs by source integrity, and a f...
  </details>

- **2026-07-13** — Xutao Mao, Xiang Zheng, Cong Wang — [Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming](http://arxiv.org/abs/2607.11698v1)
  <details><summary>📄 Abstract</summary>
  Production LLM agents such as Claude Code and Codex operate over untrusted content, files, commands, and workspace state, making safety failures directly actionable. Red-teaming must therefore keep pace with evolving models and tools. Existing approaches mainly optimize attack success and preserve artifacts such as benchmarks, payloads, or attack programs, which record where attacks succeed but not the enabling conditions behind unsafe agent behavior. We study automated red-teaming for productio...
  </details>

- **2026-07-13** — Yi Ting Shen, Kentaroh Toyoda, Alex Leung — [AMT-X: Phase-Structured Multi-Turn Red-Teaming with Checklist-Gated Evaluation](http://arxiv.org/abs/2607.11151v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluation of large language models (LLMs) relies largely on single-turn attack datasets and single-judge scoring, underestimating risk from adaptive multi-turn adversaries and reporting a single success rate that does not separate partially actionable outputs from those carrying complete operational detail. We propose AMT-X (Adaptive Multi-Turn Exploitation), a phase-structured multi-turn red-teaming framework. Unlike prior multi-turn attacks that rely on ad hoc escalation or free-form p...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 54 papers

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

- **2026-07-13** — Lukas Rapp, Jiewei Feng, Muriel Médard et al. — [Generalized Segmented GRAND for Guesswork Reduction in Turbo Product Decoding](http://arxiv.org/abs/2607.12147v1)
  <details><summary>📄 Abstract</summary>
  Guessing random additive noise decoding (GRAND) can efficiently decode any moderately redundant code with near maximum likelihood (ML) performance via noise effect guessing. For binary linear codes, Rowshan and Yuan's Segmented GRAND was the first to show that constrained guessing can reduce guesswork. Although powerful, their approach requires a specific parity-check matrix structure that limits the number of constraints that can be exploited as well as the class of applicable codes. Here we in...
  </details>

- **2026-07-13** — Zeyan Liang, Graham McDonald, Iadh Ounis — [Explaining When PRF Fails: Participatory Auditing for Selective Query Expansion](http://arxiv.org/abs/2607.12098v1)
  <details><summary>📄 Abstract</summary>
  Pseudo-Relevance Feedback (PRF) improves retrieval effectiveness on average, but harms a substantial fraction of queries through query drift, an asymmetry hidden by aggregate offline metrics. Existing Selective PRF (sPRF) approaches typically rely on Query Performance Prediction (QPP) methods derived from the same ranking statistics, and therefore inherit, rather than resolve, this opacity. We argue that this is a core explainability problem in IR, and propose a two-stage audit-then-automate fra...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 55 papers

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

- **2026-07-13** — Boda Xiao, Xiran Xu, Songyi Li et al. — [Beyond Parallel Tracking: Interactive Multi-Feature Fusion Drives Semantic Reconstruction from Non-invasive Brain Recordings](http://arxiv.org/abs/2607.12071v1)
  <details><summary>📄 Abstract</summary>
  Continuous semantic reconstruction from non-invasive neural recordings remains limited by the representational mismatch between semantic feature spaces and neural coding patterns, which severely impedes cross-modal alignment between high-noise neural signals and target semantic features. Prior semantic decoders have predominantly relied on static lexical representations or dynamic contextualized representations in isolation. This single-dimension approach inevitably leads to severe information l...
  </details>

- **2026-07-13** — Sam Cheng-Tse Huang, Matthew R. Buckley, Justin I. Read et al. — [A Universal Distribution of Dark Matter in Milky Way-like galaxies and How to Infer It](http://arxiv.org/abs/2607.12008v1)
  <details><summary>📄 Abstract</summary>
  The phase-space density of dark matter within the Milky Way is a key quantity that encodes information about the nature of the dark sector. The local phase-space density is also required to properly interpret the results of dark matter direct detection experiments. However, there are at present few observational constraints. In this paper, we show that a simple coordinate transformation reveals a near-universal DM phase-space distribution function among three independent suites of cosmological s...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 51 papers

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

- **2026-07-13** — Niranjan Kumar M, Balaji Nagarajan, Karthik Nair et al. — [Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking](http://arxiv.org/abs/2607.12085v1)
  <details><summary>📄 Abstract</summary>
  Evaluating retail conversational agents requires methods beyond lexical-overlap metrics to assess intent alignment, factuality, helpfulness, clarity, tone, and overall response quality. Although LLM-as-a-judge methods provide scalable alternatives to human evaluation, production deployment introduces challenges in governance, reproducibility, cost, schema consistency, traceability, and reliability. We present GenAI Evaluation, a governed, configuration-driven pipeline for large-scale evaluation ...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 107 papers

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

- **2026-07-13** — Samer Saab, Chaouki Abdallah — [Graph Feedback Controls Consensus and Clique Formation in Open-Weight Language-Model Populations](http://arxiv.org/abs/2607.12077v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent language-model systems increasingly route local interactions, yet the runtime interaction graph is often treated as an implementation detail. We study convention formation in open-weight LM populations spanning 1.1B-32B parameters with a naming-game protocol. Restricted first-token scores over tokenizer-safe labels let us measure prompt-conditioned score-state distributions, construct state-similarity graphs, and separate sampled-label agreement from latent state-space consensus. Acr...
  </details>

- **2026-07-13** — Fangxia An, Fatemeh S. Tabatabaei, Nick Seymour et al. — [Tracing cosmic star formation history through radio continuum spectral energy distribution and non-thermal emission](http://arxiv.org/abs/2607.12073v1)
  <details><summary>📄 Abstract</summary>
  As a tracer of massive star formation unaffected by dust, the radio continuum emission provides a unique window into the formation of the first stars and galaxies in the Universe. Recent observations show that the integrated rest-frame mid-radio (~1-10 GHz) luminosity of galaxies serves as one of the most robust tracers of the star formation rate (SFR). These studies further demonstrate that the synchrotron spectral index and the shape of the radio spectral energy distribution (SED) evolves with...
  </details>

- **2026-07-13** — Said Elnaffar, Farzad Rashidi — [Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability](http://arxiv.org/abs/2607.12056v1)
  <details><summary>📄 Abstract</summary>
  Online shopping is increasingly shifting toward a model in which AI agents independently search for products, compare options, evaluate constraints, and carry out parts of the purchasing process for users. Website design must now support both human and agent-mediated interaction. This paper introduces the agent-ready website, a design framework for enhancing the readability, interpretability, verifiability, and actionability of e-commerce platforms for AI agents. Existing web design, SEO, and ge...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 13 papers

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

- **2026-07-13** — Vincent Giap, Eric Wang, Cris Nguyen — [Measuring the Re-executability of Published Molecular Docking Claims](http://arxiv.org/abs/2607.12117v1)
  <details><summary>📄 Abstract</summary>
  Published molecular docking scores depend on the receptor, ligand, software, search box, seed, and preparation choices; a paper reporting only the score has published a number with unknowable provenance. We ask whether such claims can be re-executed from their own published records. We introduce MERS-Dock, a 16-field Minimum Executable Reporting Set, and a deterministic E0-E4 executability ladder over audited field states. In 236 open-access SARS-CoV-2 main-protease docking papers, only 8.1% met...
  </details>

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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-07-13** — Chenxi Sun, Minghui Liwang, Wusi He et al. — [HermesHFL: Incentive-Compatible Hierarchical Federated Unlearning for Dynamic LLM Fine-Tuning](http://arxiv.org/abs/2607.11528v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical federated unlearning (HFUL) for large language model (LLM) fine-tuning faces significant challenges due to hierarchical aggregation, dynamic client participation, and strong parameter coupling in LLM adaptation. Selectively removing client contributions is particularly difficult because model updates propagate across multiple aggregation stages while unlearning requests may coincide with client departures and rejoining. To address these issues, we propose **HermesHFL**, a hierarchic...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 5 papers

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


### 📂 other
*其他安全相关 / Other Security-Related* — 156 papers

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

- **2026-07-13** — Pradyumna Elavarthi, Arun J. Bhattacharjee, Harrison Lisabeth et al. — [From Reconstruction to Interpretation: Zero-Setup Multi-Phase Segmentation of X-ray Tomography Data](http://arxiv.org/abs/2607.12175v1)
  <details><summary>📄 Abstract</summary>
  X-ray tomography enables nondestructive characterization of material microstructures, while advances in micro-CT imaging have accelerated volumetric data acquisition and reconstruction. However, rapid interpretation remains limited by image segmentation, which often requires manual thresholding, user prompting, or material-specific model training. We present a zero-setup framework for multi-phase segmentation of synchrotron X-ray tomography data that generates interpretable masks for previously ...
  </details>

- **2026-07-13** — Sarel Weinberger, Amir Hozez — [Token Reduction Is Not Cost Reduction](http://arxiv.org/abs/2607.12161v2)
  <details><summary>📄 Abstract</summary>
  Context-reduction layers for API-based coding agents, including command-output compressors, retrieval rankers, and API-boundary proxies, are commonly evaluated by how much context or tool output they remove. We ask a different question: which interventions actually reduce end-to-end billed cost while preserving task success?   Our primary evidence is a pre-specified, hash-frozen, paired campaign of 2,908 provider-billed Claude Code runs, of which 2,848 were analyzed, covering 103 tasks, seven re...
  </details>

- **2026-07-13** — Leonardo Modesto — [Superconductive or superfluid condensation in curved spacetime](http://arxiv.org/abs/2607.12133v1)
  <details><summary>📄 Abstract</summary>
  We provide a proof of unitarity for quantum field theory in a general spacetime. Our argument expresses the Bogoliubov transformations in terms of a unitary squeezing operator relating the initial and final Hilbert spaces. The $S$-matrix in curved spacetime is thus the product of the squeezing operator and the $S$-matrix in the out-Hilbert space (typically Minkowski). Since both factors are unitary, their product is unitary. It follows that the Bogoliubov in-vacuum is described by a BCS-like sta...
  </details>

- **2026-07-13** — Tiberiu Musat, Tiago Pimentel, Nicolas Zucchet et al. — [Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks](http://arxiv.org/abs/2607.11875v2)
  <details><summary>📄 Abstract</summary>
  We present a theoretical framework to explain the emergence of inductive reasoning abilities in Transformer language models. While previous works on Transformer learning dynamics have so far been mostly tied to specific tasks, we study a generalized class of inductive tasks that unifies several synthetic tasks known in the literature, including in-context n-grams and multi-hop reasoning. In this class, we theoretically prove that the training dynamics of attention models can be confined to a hig...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 545 |
| prompt-injection | 453 |
| memory-poisoning | 36 |
| tool-use-attack | 91 |
| backdoor | 386 |
| adversarial-attack | 530 |
| privacy-leakage | 3682 |
| steganography | 52 |
| misuse | 812 |
| red-teaming | 108 |
| vulnerability | 2427 |
| defense | 2064 |
| alignment | 1890 |
| robustness | 1778 |
| watermark | 181 |
| unlearning | 82 |
| agent-safety | 48 |
| benchmark | 53 |
| survey | 244 |
| other | 5406 |

---

📚 **全部 20868 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-07-16 02:42:45*