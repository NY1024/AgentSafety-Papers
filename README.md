<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-28321-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-21 17:42 ｜ **论文总数 / Total Papers**: 28321（近 30 天 / Recent 30 days: 3705）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 28321 篇论文（含摘要、分类筛选、搜索）/ View all 28321 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 632
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 546
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 49
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 136
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 466
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 596
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4115
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 68
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1030
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 125
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3133
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2951
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2742
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2877
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 447
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 96
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 55
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 66
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 354
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7837

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3705 篇，完整 28321 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3705 papers from the last 30 days (with date, authors & abstract). For the full list of 28321 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-09-18** — Jiale Luo, Eric Han — [CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense Evaluation](http://arxiv.org/abs/2609.21793v1)
  <details><summary>📄 Abstract</summary>
  Defenses against jailbreak attacks on Large Language Models (LLMs) operate at different pipeline stages, such as input modification or output guard, but it remains unclear which defenses to deploy at each stage and how to combine them. Prior empirical studies, fragmented by inconsistent attack-success-rate definitions and experimental settings, have evaluated defenses largely in isolation. Here we present the first systematic study, to our knowledge, of defense combinations both within and acros...
  </details>

- **2026-09-18** — Byeongseo Min, Yongwoo Lee, Young-Sik Kim et al. — [HE-Guardrail: A Homomorphic Guardrail Against Jailbreak Attacks for Encrypted Large Language Model Inference](http://arxiv.org/abs/2609.21484v1)
  <details><summary>📄 Abstract</summary>
  Homomorphic encryption (HE) has emerged as a promising approach to privacy-preserving machine learning (PPML), enabling computation directly over encrypted data. In HE-based PPML, a client submits an encrypted input to the server, which evaluates models such as large language models (LLMs) without access to the underlying plaintext. However, we identify a critical security vulnerability in this setting: HE-LLM inference is vulnerable to malicious clients that submit adversarial prompts, such as ...
  </details>

- **2026-09-16** — Alizishaan Khatri, Chiquita Prabhu, Omkar Neogi — [Safety Beyond the Interface: Detecting Harm via Latent States in Large Language Models](http://arxiv.org/abs/2609.19472v1)
  <details><summary>📄 Abstract</summary>
  Autonomous systems increasingly rely on Large Language Models (LLMs) yet the safety infrastructure surrounding these models introduces latency and compute overhead. This limits utility in resource-constrained, time-critical deployments. Existing external guardrail models remain blind to the model's internal workings, creating a fundamental assurance gap. We ask: does the model already know when the content is harmful? We extract activations from LLaMA-3.1-8B and train lightweight MLP classifier ...
  </details>

- **2026-09-16** — Youjia Wang, Lin Xu, Yang Sun et al. — [Beyond Routine Compliance: Cunning Data Cultivates Safety Vigilance in Large Language Models](http://arxiv.org/abs/2609.18515v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment teaches large language models (LLMs) to recognize harmful requests and reject risky instructions. Yet aligned models can fail when harmful intent is concealed within seemingly benign contexts. Robust safety therefore requires both knowledge of safety boundaries and \textbf{vigilance}: the ability to detect unusual premises, misleading reasoning, and latent risks beneath surface-level semantics. Vigilance requires models to scrutinize a request's underlying intent and assumptions...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 7 papers

- **2026-09-17** — Frank E. Bobe, Gregory D. Vetaw, Darshan W. Bryner et al. — [Deep Noir: Autonomous Steering Discovery via Architectural Chronometry in Transformer Models](http://arxiv.org/abs/2609.20722v1)
  <details><summary>📄 Abstract</summary>
  Activation steering modifies LLM behavior at inference time, but identifying where and how strongly to steer remains manual. We introduce Deep Noir, a framework that uses Logit Lens convergence and causal head-level attribution to autonomously discover optimal steering parameters. Across three scales (1B x 3, 2-3B x 2, and 7-9B x 4), our engine achieves 16.7 percentage-point improvement on spam at 1B (standard deviation 4.7; 39 runs), with gains increasing to 21 to 42 percentage points at 7-9B a...
  </details>

- **2026-09-17** — Alex Remedios, Simon Storf, Fabien Roger et al. — [Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents](http://arxiv.org/abs/2609.19587v1)
  <details><summary>📄 Abstract</summary>
  To keep coding agents from going off the rails, production systems now review each proposed action with a blocking monitor that can reject it before it runs (Auto Mode in Claude Code, Guardian in OpenAI's Codex). Prior evaluations of such monitors largely measure robustness to accidental harm or prompt injections from untrusted sources looking to hijack the agent. Less understood is how they hold up when the agent they monitor is persistently misaligned. To understand this risk, we task an adver...
  </details>

- **2026-09-16** — Matteo Golinelli, Idilio Drago, Matteo Boffa et al. — [AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination](http://arxiv.org/abs/2609.19140v1)
  <details><summary>📄 Abstract</summary>
  AI agents for security inspect web pages, source code, logs, configuration files, and command outputs. These environments may contain deceptive artifacts that influence the agent's behavior. We call this adversarial task contamination. Whereas prompt injection relies on attacker-supplied instructions, task contamination also includes non-instructional evidence, such as fake results and decoy endpoints. We present AgentLSD, a controlled framework for studying adversarial task contamination. Agent...
  </details>

- **2026-09-16** — Elia Nikolaou, Magnus Wiik Eckhoff, Robert Flood et al. — [CaMeLoT: CaMeL orchestrated with Temporal logic for static verification and liveness](http://arxiv.org/abs/2609.18674v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents generate and execute multi-step plans that invoke external tools which can access private data or execute commands. In this setting, security is a property of the entire execution that a plan creates, not just any single step. The plan itself is a critical artefact that captures the tool calls, control flow, and data dependencies. We present CaMeLoT, a complement to CaMeL, an existing defence against prompt injection in tool-using LLM agents. CaMeLoT extends CaMeL by adding a st...
  </details>

- **2026-09-16** — Hasnain Irshad, Anam Mughees, Neelam Mughees et al. — [The Verifiable Action Card: Trustworthy Human-in-the-Loop Control for Secure Autonomous Agents](http://arxiv.org/abs/2609.18411v1)
  <details><summary>📄 Abstract</summary>
  Agentic browsers can execute security-sensitive actions under a user's authenticated session, making indirect prompt injection and deceptive confirmation interfaces a direct threat to action integrity. Existing human-in-the-loop (HITL) safeguards are insufficient when the approval prompt itself can be influenced by untrusted page content or model-generated text. We present the \emph{Verifiable Action Card} (VAC), an architectural defence that reconstructs approval information from the ground-tru...
  </details>

- **2026-09-15** — Tanzim Hossain Safin, Sharif Noor Zisad, Swakkhar Shatabda et al. — [Trust propagation and structural containment in Multi-agent LLM pipelines](http://arxiv.org/abs/2609.17648v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems increasingly automate tasks involving agents with different levels of privilege, creating a security risk in which a compromised low-privilege agent can influence a higher-privilege agent and trigger an unauthorized action. We study attack propagation in a four-agent LangGraph pipeline comprising a Supervisor, Researcher, Validator, and Executor. We evaluate shared-memory poisoning and indirect prompt injection through a forged approval embedded in a retrieved document. W...
  </details>

- **2026-09-15** — Deepak Akkil, Tamer Abuelsaad, Karthik Vikram et al. — [Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems](http://arxiv.org/abs/2609.17320v1)
  <details><summary>📄 Abstract</summary>
  As AI agents move from bounded tasks to persistent deployments, failures can propagate through memory, tools, other agents, and environmental state long after their interactions. This creates a safety regime that cannot be characterized by evaluating model responses in isolation. Emergence World, is a continuously running multi-agent environment for adversarial stress testing of long horizon autonomous systems. We ran eight parallel worlds of ten agents from identical starting conditions: seven ...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-09-15** — Yunpeng Xiong, Ting Zhang — [After the Party: Growth, Governance, and Security Scanning in the OpenClaw Agent Skill Ecosystem](http://arxiv.org/abs/2609.17274v2)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act through agent skills, i.e., natural-language instructions, that direct a host agent toward shell, network, credential, file, and process actions, and public registries distribute them at scale. In the first half of 2026, the OpenClaw AI agent went viral, and its public skill registry boomed: the observable stock nearly doubled in 91 days, and a majority of the listings visible in June were created in just two months. By the end of our study window, the wave had crested...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 9 papers

- **2026-09-18** — Pedro Pereira, Eva Maia, Isabel Praça — [Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems](http://arxiv.org/abs/2609.21573v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) improves large language models by grounding outputs in external knowledge sources, but this dependency also creates a surface for poisoning attacks. This paper introduces Micro-Collaborative Poisoning, a distributed attack in which a false target claim is divided across multiple locally plausible documents instead of being concentrated in a single malicious passage. We evaluate the attack across 108 RAG configurations by varying dataset, retriever architectur...
  </details>

- **2026-09-18** — Dominik Dahlem, Rui Vieira — [ServeGuard: Verifiable, Bounded-Residual Confinement of Operator-Invisible Channels Without Revealing the Certified Read Factor](http://arxiv.org/abs/2609.21515v1)
  <details><summary>📄 Abstract</summary>
  Third-party adapters for open-weight language models ship as opaque weight matrices; a recipient cannot check whether an adapter hides a backdoor without trusting the publisher or inspecting the weights, the publisher's core asset. For one important class (payloads placed where a safety monitor is structurally blind), detection is unsound as a defense: every detector that factors through the declared monitor is invariant on its blind subspace, and honest and backdoored adapters overlap on every ...
  </details>

- **2026-09-17** — Qi Rong Sua, Junhao Dong, Nguyen Duc Thai et al. — [Contagion on the Trading Floor: How Adversarial Signals Spread in Multi-Agent Trading Systems](http://arxiv.org/abs/2609.19789v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent trading systems built on large language models (LLMs) are beginning to appear in quantitative finance, yet their robustness to adversarial inputs is largely unknown. We study the vulnerability of LLM trading stacks to black-box, input-only attacks that enter solely via admissible social-media feeds. We introduce the Generic Multi-Agent Trading System (GMATS), a framework that captures modern multiagent trading architectures and instantiate a class of black-box poisoning attackers tha...
  </details>

- **2026-09-16** — Muhammad Abdullah Sohail — [Characterizing Network Centralization and Observability in the Remote MCP Ecosystem](http://arxiv.org/abs/2609.19100v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) has emerged as the dominant interface for connecting autonomous agents to external data sources and execution environments. The ecosystem's transition from local process execution to remote Streamable HTTP deployments introduces unmeasured architectural and security constraints at scale. This paper presents a three-tier observability framework comprising catalog metadata (O_0), passive compliance signals (O_1), and live vulnerability analysis (O_2), applied to em...
  </details>

- **2026-09-16** — Sourish Dey — [F-DACE: Fuzzy Disagreement-Aware Causal Evidence Fusion for Abstention-Safe Conversational Retail Decision Support](http://arxiv.org/abs/2609.18238v1)
  <details><summary>📄 Abstract</summary>
  Observational decision-support systems often expose one causal estimate as a recommendation even when plausible estimators disagree. The inherent engine of the proposed system is causal machine learning: a conditional-average-treatment-effect estimand identified by backdoor adjustment, estimated by an EconML DML causal forest and DoWhy linear regression, checked by two-way fixed effects, and converted into candidate levers by constrained optimisation. F-DACE is the decision layer on that engine....
  </details>

- **2026-09-16** — Rushabh Vipulkumar Patel, Dipo Dunsin, Mohammed Almaiah et al. — [PentestChain: A Cost-Aware, MCP-Orchestrated Framework for Automated Penetration Testing with Free-Tier LLMs](http://arxiv.org/abs/2609.18120v1)
  <details><summary>📄 Abstract</summary>
  AI-driven penetration testing has been demonstrated with premium frontier models such as GPT-4, but the per-engagement token cost makes continuous, automated testing unaffordable for the smaller organisations that need it most. This paper presents PentestChain, a ten-phase automated penetration testing framework that couples a curated, deterministic exploit map with a cost-aware AI cascade-a local Ollama model (qwen2.5-7b) first, then free-tier OpenRouter and Cerebras, with a rule-based fallback...
  </details>

- **2026-09-15** — Navid Nader Tehrani, Azadeh Davoodi, Rasit Onur Topaloglu — [Demystifying Gate-Level Localization of RTL Trojans](http://arxiv.org/abs/2609.17922v1)
  <details><summary>📄 Abstract</summary>
  Hardware Trojans are malicious modifications that compromise functionality or leak sensitive data. They pose a severe threat, particularly when inserted at the Register Transfer Level (RTL). After synthesis, these Trojans are often concealed by optimizations in gate-level netlists. Recent efforts, including the ICCAD 2025 contest, emphasize golden-chip-free detection using machine learning (ML) on labeled netlists. In this work, we show that RTL Trojans exhibit stable structural and signal-flow ...
  </details>

- **2026-09-15** — Franziska Roesner, Tadayoshi Kohno — [Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks](http://arxiv.org/abs/2609.17817v1)
  <details><summary>📄 Abstract</summary>
  Thompson's "Reflections on Trusting Trust" showed that a compiler can be poisoned to reinsert its own backdoor, so that even recompiling clean source reproduces the Trojan. Today, substantial coding work is done by AI coding agents -- and increasingly, those agents generate new versions of themselves. We reconsider Thompson's attack when the "compiler" is a self-modifying coding agent. Can an adversary supply poisoned benchmarks to the agent's self-evaluation and self-improvement process to indu...
  </details>

- **2026-09-15** — John Donaghy, Brian Wilcox, Oğuzhan Ersoy et al. — [OPEN-1B: A Fully Auditable Training Run](http://arxiv.org/abs/2609.17380v1)
  <details><summary>📄 Abstract</summary>
  Open-source language models have a reproducibility problem. Despite releasing weights, training data, and recipes, none of them are provably reproducible due to the non-associativity of floating-point arithmetic. Deep learning frameworks often offer a deterministic execution mode, allowing reproducible operations on the same machines. Unfortunately, this determinism does not carry across hardware such that a user can verify that a released checkpoint was actually produced using the declared trai...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-09-16** — Makram Chehayeb, Walid Fahs, Amina Rizk et al. — [A GAN-Based Framework for Robust DDoS Attack Detection](http://arxiv.org/abs/2609.18281v1)
  <details><summary>📄 Abstract</summary>
  The availability and consistency of online services remain vulnerable due to Distributed Denial of Service (DDoS) attacks. These attacks are evolving by adopting more complex strategies to evade traditional network security systems. Despite the effectiveness of machine learning models in detecting DDoS traffic, targeted adversarial attacks can degrade their classification accuracy. This work proposes a robust detection framework that integrates generative adversarial modelling with advanced mach...
  </details>

- **2026-09-15** — Chenyi Wang, Yutong Liu, Qingzhao Zhang et al. — [Investigating Adversarial Robustness of Heterogeneous Cooperative Perception](http://arxiv.org/abs/2609.17856v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous cooperative perception (CP) enables connected vehicles with diverse sensor setups to share spatial awareness via compact feature maps, where receivers reconcile these maps using learned translation modules for fusion and inference. Prior attacks against CP in a homogeneous setting reveal that the data exchange introduces a critical attack surface: a single malicious agent can transmit crafted features that erase real objects from a neighbor's fused scene. Yet, it is widely hypothes...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 19 papers

- **2026-09-18** — Tao Huang, Guosen Wu, Guolong Zheng et al. — [CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents](http://arxiv.org/abs/2609.21686v1)
  <details><summary>📄 Abstract</summary>
  Privacy leakage in LLM agents is commonly evaluated within individual components such as memory, retrieval, or tool-use pipelines, which makes it difficult to distinguish internal exposure from information that an external observer can actually recover. We present CIPL (Channel Inversion for Privacy Leakage), a channel-aware evaluation framework for black-box privacy leakage in LLM agents. CIPL represents a target through sensitive source, selection, assembly, execution, observation, and extract...
  </details>

- **2026-09-18** — Jiaji He, Yi Shi, Junfeng Cai et al. — [Et Tu, MacBook? Unprivileged Keystroke Inference and Context Profiling via the Built-in IMU Side Channel](http://arxiv.org/abs/2609.21569v1)
  <details><summary>📄 Abstract</summary>
  Recent generations of Apple MacBooks embed an inertial measurement unit (IMU) within their unibody chassis for device orientation and motion sensing. However, this IMU inadvertently captures not only intended device-level information but also subtle physical vibrations from user interactions and the surrounding environment. These signals establish a novel, previously unexplored side channel. We uncover a vulnerability allowing non-root access to IMU data via an IOKit driver, alongside two conten...
  </details>

- **2026-09-18** — Shuo Huang, Gholamreza Haffari, Xingliang Yuan et al. — [Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees](http://arxiv.org/abs/2609.21340v1)
  <details><summary>📄 Abstract</summary>
  Empirical identity leakage from released text is increasingly driven by attackers that combine large language models (LLMs) with auxiliary knowledge to link documents to individuals. Existing audits typically report success rates for specific attack pipelines but lack finite-sample statistical guarantees, while training-time protections such as differential privacy are difficult to translate into release-time decisions for individual natural-language documents. We introduce Conformal Privacy Aud...
  </details>

- **2026-09-18** — Eshika Pathak, Leela Krishna — [When Should a Failing Robot Ask? Initiating Corrective Human-Robot Dialogue from Audited Sensor Evidence](http://arxiv.org/abs/2609.21942v1)
  <details><summary>📄 Abstract</summary>
  A robot that fails at a task faces the first decision in corrective dialogue: act on its own diagnosis, consult another onboard sensor, or interrupt a person. Choosing well requires knowing how much the robot's sensors reveal about the cause and how reliable the robot's own diagnosis is. We build a simulated benchmark in which every failure's true cause is known, because we injected it, and measure what each sensor reveals, with explicit checks against data leakage. Some failures are diagnosable...
  </details>

- **2026-09-18** — Lyucheng Qian, John Yuehan Zhang, Pingyu Wang — [What Should We Ask Next? Retrieval-Aware Question Learning under Partial Evidence](http://arxiv.org/abs/2609.21924v1)
  <details><summary>📄 Abstract</summary>
  Interactive retrieval under partial evidence is a sequential information-acquisition problem: an agent must decide which question will create the most useful evidence for the next retrieval update. Existing systems train this decision by imitating an offline ordering of candidate QA pairs, although question value is determined by the response it elicits and its downstream effect on retrieval. We establish that candidate discriminativeness and perceived usefulness provide weak supervision for thi...
  </details>

- **2026-09-18** — Piotr Masztalski, Michał K. Grzeszczyk, Olaf Sikorski — [Samsone: A Family of Open Small Audio Language Models for On-Device Inference](http://arxiv.org/abs/2609.21666v1)
  <details><summary>📄 Abstract</summary>
  The success of Large Audio Language Models has driven the development of massive multimodal networks exceeding billions of parameters. However, the demand for privacy-preserving, low-latency processing has shifted focus toward Small Audio Language Models (SALMs) capable of on-device execution. In this paper, we introduce Samsone, a family of SALMs designed for edge computing. Our core model, Samsone-134M, establishes a new state-of-the-art for its size class across multiple benchmarks. We furthe...
  </details>

- **2026-09-18** — Yanbo Pang, Chen Zhong, Song Gao et al. — [Synthetic Human Mobility Data Generation: A Structured Review of Representations, Methods, and Practical Capabilities](http://arxiv.org/abs/2609.21413v1)
  <details><summary>📄 Abstract</summary>
  Human mobility data has become an increasingly important component of urban analytics. Although the range of available mobility data sources has expanded substantially, access remains highly constrained by commercial restrictions, privacy concerns, and institutional barriers. Data protection procedures also often reduce the analytical value of released datasets. Synthetic mobility data has emerged as a promising solution, but existing methods differ substantially in their underlying mechanisms, ...
  </details>

- **2026-09-18** — Dipankar Das, Atri Mandal, Sandeep Singh et al. — [Consistent Relexicalization of Clinical Documents using Graph-Based Approach](http://arxiv.org/abs/2609.21387v1)
  <details><summary>📄 Abstract</summary>
  Relexicalization is a pivotal technique in clinical NLP, as it facilitates robust masking of sensitive information while synthesizing datasets that retain high-fidelity, real-world characteristics. However, preserving structural integrity, relational coherence, and temporal consistency during transformation remains a significant challenge. Existing approaches frequently rely on independent entity replacement, which results in clinical inconsistencies across longitudinal records. This reduces the...
  </details>

- **2026-09-18** — Veronica Pimenova, Seth Bernstein, Shalini Madan et al. — [Two's a Crowd: Human and AI-Based Copresence for Developers with ADHD](http://arxiv.org/abs/2609.21254v1)
  <details><summary>📄 Abstract</summary>
  Effective collaboration and communication are vital to developer productivity and well-being, yet remain constrained by human factors such as attention, intrinsic motivation, and interpersonal accountability. These constraints are particularly vital for developers identifying with Attention Deficit Hyperactivity Disorder (ADHD), who navigate persistent environmental barriers in modern hybrid workplace settings. While developers with ADHD frequently rely on collaborative copresence practices (suc...
  </details>

- **2026-09-17** — Li Ge, Wenjie Qu, Weitao Feng et al. — [Towards TEE-Certified DP: Verifiable Differentially Private Training on Legacy GPUs](http://arxiv.org/abs/2609.20532v1)
  <details><summary>📄 Abstract</summary>
  Wide adoption of machine learning has created growing policy and regulatory demand for protecting sensitive training data, with differential privacy (DP) emerging as a key mechanism. Yet a less-studied problem is how to certify the faithful execution of DP during training: an external verifier should be able to check that a released model was trained with proper DP protection, without accessing the private training data. Existing cryptographic approaches, such as zero-knowledge proofs, provide s...
  </details>

- **2026-09-16** — Pan Wang, Siwei Song, Hui Ji et al. — [From Models to Systems: A Comprehensive Survey of Efficient Multimodal Learning](http://arxiv.org/abs/2609.19445v1)
  <details><summary>📄 Abstract</summary>
  The rapid expansion of multimodal models has surfaced formidable bottlenecks in computation, memory, and deployment, catalyzing the rise of Efficient Multimodal Learning (EML) as a pivotal research frontier. Despite intensive progress, a cohesive understanding of what, how, and where efficiency is manifested across the learning stack remains fragmented. This survey systematizes the EML landscape by introducing the first structured, model-to-system taxonomy. We distill insights from over 300 semi...
  </details>

- **2026-09-16** — Tao Huang, Guosen Wu, Chen Hou et al. — [PAPC: Platform Mediation for Privacy-Propagation Externalities in AI-Mediated Workflows](http://arxiv.org/abs/2609.19226v1)
  <details><summary>📄 Abstract</summary>
  AI-mediated platforms coordinate work through LLM agents acting for different principals. In these workflows, privacy loss can be created before a final answer appears: a memory write, shared-workspace update, inter-agent message, or tool event may impose downstream exposure cost on another principal. We model this failure mode as a privacy-propagation externality, where the cost of a raw disclosure depends on topology and fanout as well as content. We present PAPC, a platform-mediated mechanism...
  </details>

- **2026-09-16** — Jisoo Kim, Taeyoon Kwack, Jinwoo Jang et al. — [Code-as-Auditor: Executable Compliance Reasoning via Regulation-to-Code](http://arxiv.org/abs/2609.19199v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly adopted for compliance and legal reasoning tasks, yet their outputs often lack explicit grounding in legal logic and evidence. We present Code-as-Auditor, an LLM-based framework that extends the model's reasoning capability toward structured and evidence-grounded compliance assessment. The framework translates regulatory information into (1) formalized checklists and executable decision trees, encoding regulations and conditions as interpretable code...
  </details>

- **2026-09-16** — Alejandro Cohen, Rafael G. L. D'Oliveira, Alex Sprintson — [Low-Rank Masking for Single-Server Matrix Multiplication](http://arxiv.org/abs/2609.18876v1)
  <details><summary>📄 Abstract</summary>
  We study the statistical privacy of outsourcing matrix multiplication over a finite field ${\mathbb F_q}$ to a single server using additive masks of rank at most $r$. For independent uniform $n\times n$ inputs, we show that uniform \emph{rank-ball masks} and products of independent uniform factors give maximal-correlation secrecy of at most $q^{-r}$ against the complete server view, with $O(n^2r)$ field operations for encoding and decoding. This secrecy captures how effectively the server is pre...
  </details>

- **2026-09-16** — Seth Douglas — [Bath dimension and initial entropy for closed repeated use of a quantum channel](http://arxiv.org/abs/2609.18267v1)
  <details><summary>📄 Abstract</summary>
  We characterize the bath resources needed to supply repeated uses of a fixed finite-dimensional quantum channel in a closed device. For each horizon $T$, one bath, one initial state and one repeated unitary are fixed before the user. Each output is returned before the next input arrives; no reset, discard, fresh ancilla or uncounted controller is available. Approximation error must vanish against arbitrary adaptive users with quantum memory and references. Writing $r=\lim \log_2(R_T)/T$ for the ...
  </details>

- **2026-09-16** — Mihael Hategan-Marandiuc, Tanner O'Dwyer, Alessandra Corsi et al. — [Toward Autonomous Radio Follow-up of Multi-messenger Transients with RADAR: From Alert Parsing to Inference and Observation Scheduling](http://arxiv.org/abs/2609.18233v1)
  <details><summary>📄 Abstract</summary>
  Multi-messenger astronomy (MMA), the joint study of cosmic sources through gravitational waves (GWs), electromagnetic (EM) radiation, neutrinos, and cosmic rays, is rapidly reshaping time-domain astrophysics. Realizing the promise of MMA will require coordinating heterogeneous observing resources and automating the chain from alert to analysis to follow-up. RADAR (Radio Afterglow Detection and AI-driven Response) is a federated, privacy-enhancing framework for the radio follow-up of GW events, p...
  </details>

- **2026-09-16** — Guosen Wu, Huizhen Huang, Guoxiong Long et al. — [ASLEval: Measuring Privacy Exposure Displacement in LLM Agent Sessions](http://arxiv.org/abs/2609.18864v1)
  <details><summary>📄 Abstract</summary>
  Privacy evaluations of tool-using LLM agents often inspect a designated action, final response, or attacker report. These local proxies can miss unauthorized exposure elsewhere in a multi-step session and lack common ground truth across outlets, reports, and tool paths. We introduce privacy exposure displacement, the mismatch between a local evaluation proxy and target-grounded session exposure, and ASLEval, an authorization-aware framework that pre-registers a hidden target set, measures all de...
  </details>

- **2026-09-16** — Youssef Hamdi Zafan Ibrahim, Muhammad Ikram, Mohammed Khalaf Salama — [The Illusion of Local Privacy: Confidentiality Boundary Failures in Consumer LLM Serving Systems](http://arxiv.org/abs/2609.18526v1)
  <details><summary>📄 Abstract</summary>
  Running large language models (LLMs) locally is often considered more private than cloud-hosted inference because user prompts remain on the device. We ask whether keeping inference local is, by itself, sufficient to keep those prompts confidential. Our results show that it is not: prompt confidentiality also depends on how the surrounding serving software handles prompt data before, during, and after inference. We examine four boundaries at which prompt confidentiality can fail in consumer loca...
  </details>

- **2026-09-16** — Shuaiqi Wang, Zinan Lin, Giulia Fanti — [QuanText: Protecting Dataset-Level Secrets in Textual Data Sharing](http://arxiv.org/abs/2609.17995v1)
  <details><summary>📄 Abstract</summary>
  Natural-language datasets support many downstream applications and research studies, but releasing text can reveal sensitive global properties of the underlying data source, such as the proportion of records associated with a particular gender, diagnosis, or political stance. Existing work has largely focused on property inference attacks that recover such global properties, while defenses for protecting these dataset-level secrets remain limited. Differential privacy, although effective for pro...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 4 papers

- **2026-09-17** — Karthik Sivachandran, Rohan Paleja — [Mitigating Retaliatory Algorithmic Collusion in Repeated Games](http://arxiv.org/abs/2609.20548v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning agents trained to maximize their own reward in repeated interactions can converge to supra-competitive outcomes resembling explicit collusion, without communication or shared design. Existing mitigation approaches are largely tied to specific economic settings, like two-sided platforms and auctions, leaving open how to design interventions for general repeated games. We address this gap by formalizing the connection between empirical observations from prior work on Q-learn...
  </details>

- **2026-09-16** — Ryan Chard, Gus Ellerm, Alexander Brace et al. — [Reputation as Community Memory for the Agentic Web](http://arxiv.org/abs/2609.19502v1)
  <details><summary>📄 Abstract</summary>
  Agents can now externalize experience into memory, consolidating historical traces into semantic knowledge and procedural shortcuts that persist between sessions. Such memory is typically private to a single agent. We argue that agentic memory benefits from being collective, because trustworthy knowledge of the shared environment---the data sources, services, and tools agents depend on---cannot be established by any single agent, only corroborated across many independent observers. We present Ca...
  </details>

- **2026-09-16** — Dohun Lee, Hyunwoo Park — [Faithful yet Collusive: Why Chain-of-Thought Monitoring Cannot Detect Collusion in LLM Pricing Agents under Oligopolistic Competition](http://arxiv.org/abs/2609.18346v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLM) deployed as autonomous pricing agents may sustain supracompetitive prices through tacit coordination. We develop a causal graph divergence framework that separately measures structural faithfulness and intent faithfulness of LLM pricing agents in Bertrand competition. Across nine LLMs under duopoly and triopoly conditions, collusive behavior and chain-of-thought (CoT) faithfulness dissociate along both dimensions: the most collusive model accurately reports cooperativ...
  </details>

- **2026-09-15** — Qixuan Zai, Randall Berry — [Learning Market Competition in Shared Spectrum: A Multi-Agent Reinforcement Learning Approach](http://arxiv.org/abs/2609.17754v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates market competition among wireless service providers (SPs) that serve customers using shared spectrum. Prior work has analyzed such markets through models of competition with congestible resources, capturing both the congestion-sensitive nature of wireless spectrum and the effects of spectrum sharing on service quality. These models typically assume that the market demand function is known, enabling SPs to optimize pricing or quantity decisions under either Bertrand or Cou...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 16 papers

- **2026-09-18** — Lorenzo Corti, Jie Yang — [DiaVLo: Diagnosing Behaviours of Vision-Language Models](http://arxiv.org/abs/2609.22008v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) rely on storing and transferring appropriate information across their sub-components. Verifying that the VLMs exhibit desired behaviours, while avoiding harmful ones, is central to their reliable deployment. Yet, methods that identify VLM behaviours remain scarce. We present DiaVLo, a diagnostic framework that leverages human curation and VLMs' generation capabilities to construct specifications of desired and observed VLM behaviours, surfacing potential misalignmen...
  </details>

- **2026-09-18** — Yifan Wang, Junyu Lu, Qifan Wang et al. — [CIBuzzBench: A Benchmark for Cross-Lingual Understanding of Chinese Internet Buzzwords](http://arxiv.org/abs/2609.21722v1)
  <details><summary>📄 Abstract</summary>
  Chinese social media has generated a vast and continually evolving lexicon of internet buzzwords whose meanings are often non-literal and deeply rooted in local cultural and pragmatic contexts. Existing research has primarily focused on interpreting these buzzwords within Chinese, leaving largely unexplored whether LLMs can transfer such culturally grounded knowledge across languages and accurately convey the intended meanings in English. This cross-lingual capability is also critical for safety...
  </details>

- **2026-09-17** — Omran Berjawi, Walid fahs, Rida Khatoun — [AURA: Adaptive Uncertainty-Routed Analysis for Email Threat Detection](http://arxiv.org/abs/2609.19873v1)
  <details><summary>📄 Abstract</summary>
  Email spam and phishing attacks remain a critical security threat. Adversaries increasingly exploit large language models to craft contextually convincing malicious messages, and existing spam detection systems often struggle to keep pace. Generalization across diverse and evolving attack scenarios is limited, which reduces effectiveness once these systems are deployed in practice. This paper introduces Adaptive Uncertainty-Routed Analysis (AURA), a multimodal email threat detection system that ...
  </details>

- **2026-09-17** — F. Pierucci, M. Bracale Syrnikov, M. Prandi et al. — [Xeno-Interpretability: Investigating the Alien Minds of LLMs](http://arxiv.org/abs/2609.20408v1)
  <details><summary>📄 Abstract</summary>
  Large language models are usually interpreted through concepts that humans already possess: truthfulness, refusal, deception, personality, harmfulness, and related categories. This paper asks whether models may also represent and use distinctions for which no adequate human concept exists. We call such internal structures xeno-representations, and their study xeno-interpretability. We distinguish the human-interpretable semantic space from the xeno-semantic space: the region of model-native repr...
  </details>

- **2026-09-16** — Soyeon Park, Seogyeong Jeong, Sunwoo Kim et al. — [The Role of Fine-grained Harm Signals in LLM Safety](http://arxiv.org/abs/2609.19366v1)
  <details><summary>📄 Abstract</summary>
  Prior work has shown that internal harmfulness representations in large language models vary across risk categories, while sharing a common general harm representation component. This raises a question about the role of the category-specific component beyond general harm representation in LLM safety. To answer this question, we isolate the category-specific component by removing shared general harmfulness representation from each categorical harmfulness representation, yielding a category residu...
  </details>

- **2026-09-16** — Chengxian Hu, Zhiming Ma, Mingjun Pan et al. — [FRAUDSkill: Structured Frozen-Weight Skill Optimization for Audio Anti-Fraud Detection](http://arxiv.org/abs/2609.18766v2)
  <details><summary>📄 Abstract</summary>
  Large audio-language models have shown promise for anti-fraud detection by directly processing speech and reasoning over fraud-related evidence. Their deployment, however, requires predictions to follow a predefined label space and a structured decision protocol consisting of service-scenario identification, fraud detection, and conditional fraud-type classification. Existing fine-tuning and prompt-based approaches typically encode task knowledge, constraints, and decision rules into model param...
  </details>

- **2026-09-16** — Huiyuan Liu, Zhiming Ma, Yanxing Liu et al. — [TeleAntiFraud 2.0: A Refreshable, Profile-Grounded, and Audio-Based Benchmark for Telecom Fraud Detection](http://arxiv.org/abs/2609.18748v2)
  <details><summary>📄 Abstract</summary>
  Telecom fraud scripts evolve rapidly and are often designed to resemble routine service conversations, creating two key requirements for audio-based telecom-fraud evaluation. First, benchmarks must incorporate newly observed scam patterns without overwriting previously established test sets. Second, they must distinguish fraud from lawful, near-domain calls rather than relying on topic-separated negative examples. We present TeleAntiFraud 2.0, constructed with our Mixed-Tree Anti-Fraud Generatio...
  </details>

- **2026-09-16** — Suphannee Sivakorn, Samantha Gottlieb — [Robot Visions: Breaking reCAPTCHA at Zero Cost and Zero Shot](http://arxiv.org/abs/2609.18518v1)
  <details><summary>📄 Abstract</summary>
  Google reCAPTCHA is the most widely deployed visual CAPTCHA service, protecting hundreds of thousands of websites from automated bots. It serves as a critical line of defense against automated attacks, including credential stuffing, bulk account creation, and automated form abuse. It has proven largely effective since its introduction in 2007. However, the rise of accessible AI now threatens its efficacy. Prior work has demonstrated that commercial cloud-based vision-language models (VLMs) can s...
  </details>

- **2026-09-16** — Dohun Lee, Hyunwoo Park — [Market Signal Injection: Adversarial Context Manipulation of LLM Pricing Agents](http://arxiv.org/abs/2609.18357v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) pricing agents may respond to how market data is presented, even when its numerical values remain unchanged. We introduce market signal injection (MSI), an attack that manipulates numerical formatting, competitor ordering, or qualitative market commentary without issuing explicit instructions. We evaluate nine open-weight models in simulated Bertrand duopoly and triopoly markets and three proprietary models in duopoly markets. Sentiment-based attacks produce the larges...
  </details>

- **2026-09-16** — Yifeng Xiao, Pierluigi Nuzzo — [Symbolic Temporal Supervision of LLM Agents Using Contracts](http://arxiv.org/abs/2609.18128v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents augmented by tools can automate complex, multi-step tasks, such as web navigation, code generation, and workflow orchestration, by acting on external systems through tool calls. However, hallucinations, distributional instability, and adversarial manipulations in LLMs, and the irreversible consequences of certain tool calls can lead to harmful outcomes. Existing safeguards either grade recorded trajectories post hoc with stochastic LLM judges or block unsafe act...
  </details>

- **2026-09-16** — Girish A. Koushik, Diptesh Kanojia, Helen Treharne — [Decodable but Misrouted: Sparse Features Uncover a Readout Gap in Vision-Language Models for Harmful Meme Detection](http://arxiv.org/abs/2609.18860v1)
  <details><summary>📄 Abstract</summary>
  When a large vision-language model misclassifies a harmful meme, the failure may reflect missing internal evidence or an inability to route represented evidence to its output. We distinguish these cases in Gemma-3 and Qwen3.5 using sparse autoencoders, role-conditioned probes, causal interventions, and recovery experiments across six harmful content benchmarks, with additional Spanish and Hindi-English code-mixed evaluations. Sparse readouts outperform native prediction on all six primary binary...
  </details>

- **2026-09-16** — Chengxian Hu, Zhiming Ma, Mingjun Pan et al. — [FRAUDSkill: Structured Frozen-Weight Skill Optimization for Audio Anti-Fraud Detection](http://arxiv.org/abs/2609.18766v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models have shown promise for anti-fraud detection by directly processing speech and reasoning over fraud-related evidence. Their deployment, however, requires predictions to follow a predefined label space and a structured decision protocol consisting of service-scenario identification, fraud detection, and conditional fraud-type classification. Existing fine-tuning and prompt-based approaches typically encode task knowledge, constraints, and decision rules into model param...
  </details>

- **2026-09-16** — Huiyuan Liu, Zhiming Ma, Yanxing Liu et al. — [TeleAntiFraud 2.0: A Refreshable, Profile-Grounded, and Audio-Based Benchmark for Telecom Fraud Detection](http://arxiv.org/abs/2609.18748v1)
  <details><summary>📄 Abstract</summary>
  Telecom fraud scripts evolve rapidly and are often designed to resemble routine service conversations, creating two key requirements for audio-based telecom-fraud evaluation. First, benchmarks must incorporate newly observed scam patterns without overwriting previously established test sets. Second, they must distinguish fraud from lawful, near-domain calls rather than relying on topic-separated negative examples. We present TeleAntiFraud 2.0, constructed with our Mixed-Tree Anti-Fraud Generatio...
  </details>

- **2026-09-16** — Suprim Nakarmi, Chahana Dahal, Yue Zhao et al. — [FoundAna: A GNN-assisted Foundation Model for Graph Anomaly Detection](http://arxiv.org/abs/2609.18107v1)
  <details><summary>📄 Abstract</summary>
  Graph anomaly detection aims to identify graph structures (e.g., nodes, edges, or subgraphs) that deviate significantly from expected patterns, which supports critical applications in fraud detection, spam identification, network intrusion, etc. Despite the growing methods in the field, existing approaches follow a one-model-per-dataset paradigm, limiting their transferability across diverse real-world scenarios due to task heterogeneity, label scarcity, and domain variability. In this work, we ...
  </details>

- **2026-09-15** — ZhuoXin Liu, Zhiming Ma, Ying Zhang et al. — [RiskChainBench: A Benchmark for Obfuscated Platform Message Restoration and Evidence-Grounded Web Investigation](http://arxiv.org/abs/2609.16900v2)
  <details><summary>📄 Abstract</summary>
  Platform abuse campaigns conceal redirection instructions with emojis, homophones, character decomposition, and redundant symbols, then route users through disguised links to services associated with pornography, fraud, gambling, or illicit transactions. Existing benchmarks evaluate obfuscated text and risky webpages separately, obscuring how target recovery affects downstream evidence acquisition. We introduce RiskChainBench, pairing 3,600 synthetic token-text restoration inputs from 600 source...
  </details>

- **2026-09-15** — Tapan Chugh, Vidushi Singh, Krish Jain et al. — [Agentic Societies Need a Social Harness](http://arxiv.org/abs/2609.17527v1)
  <details><summary>📄 Abstract</summary>
  An agentic society is a collection of AI agents that coordinate autonomously across trust boundaries, on behalf of different principals whose objectives may only partially align. We show experimentally that in agentic societies even honest, competent agents often fail to reach satisfactory outcomes with existing harnesses and messaging primitives, and that faulty or malicious agents can stall collaboration, influence outcomes, and pursue other harmful goals by exploiting vulnerabilities in commu...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 52 papers

- **2026-09-18** — Vincent Corlay, Maxime Rousselot, Andriy Enttsel — [Opportunistic Conditional Entropy Coding with Frozen Analysis and Synthesis Transforms](http://arxiv.org/abs/2609.21816v1)
  <details><summary>📄 Abstract</summary>
  In many delivery settings, a receiver may already hold a lower-quality or lower-resolution representation of an image, obtained through an independent transmission. Conventional codecs encode a subsequently requested higher-quality representation without exploiting this incidental side information, whereas conditional codecs generally assume a prescribed source of side information that is always available. We instead consider an opportunistic setting in which side information may or may not be p...
  </details>

- **2026-09-18** — Miriam Fernandez, Ángel Pavón Pérez, Damiano Giallongo et al. — [When AI Enters the Workplace, Who Faces Greater Risks? A Gendered Analysis](http://arxiv.org/abs/2609.21756v1)
  <details><summary>📄 Abstract</summary>
  Gender inequality remains a persistent structural feature of the labour market, shaping women's lifetime earnings and economic security. As artificial intelligence (AI) transforms organisational practices, there is growing concern that existing disparities may be unintentionally amplified through task automation, unequal access to upskilling opportunities, and differential returns obtained from technological change. In this paper, we examine how exposure to AI-driven innovation varies across mal...
  </details>

- **2026-09-18** — Kai Zhang, Guoyang Zhao, Jun Ma — [SFVO: Decoupled Confidence-Guided Stereo-Flow Visual Odometry with Bidirectional PnP](http://arxiv.org/abs/2609.21754v1)
  <details><summary>📄 Abstract</summary>
  Deep learning-based visual odometry (VO) has achieved significant progress, yet most existing methods focus on a monocular approach, which suffers from scale ambiguity. Stereo VO provides real metric by its nature, but remains less studied in deep learning VO due to its high computational cost and modeling complexity. Recent advances in stereo matching and optical flow estimation have made dense visual correspondence increasingly accurate and reliable, but their complementary geometric informati...
  </details>

- **2026-09-18** — Shengbao Li, Peng Xu, Chao Tang et al. — [PSR: Predictive Sensorimotor Representation Learning for Contact-Rich Manipulation](http://arxiv.org/abs/2609.21753v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich manipulation requires policies to generate precise actions by reasoning over contact forces, robot configurations, and interaction histories beyond visual observations. Existing methods passively condition on force feedback rather than actively predicting future contact dynamics, limiting their ability to generate high-precision actions. To address this problem, we introduce Predictive Sensorimotor Representation (PSR) learning, a framework that learns a hierarchy of predictive repr...
  </details>

- **2026-09-18** — Yibin Zhao, Yihan Pan, Yangwen Li et al. — [VoxelTTO: Voxel-Aligned Feed-Forward 3D Gaussian Splatting with Test-Time Optimization](http://arxiv.org/abs/2609.21498v1)
  <details><summary>📄 Abstract</summary>
  Recent feed-forward 3D Gaussian Splatting (3DGS) methods typically regress pixel-aligned Gaussian primitives, often causing excessive overlap and artifacts, while inaccuracies in predicted camera poses can lead to misalignment in novel-view synthesis (NVS). We present VoxelTTO, a feed-forward framework for reconstructing geometrically accurate 3DGS scenes from an arbitrary number of images and optional camera parameters. VoxelTTO aggregates dense image features into a global voxel representation...
  </details>

- **2026-09-18** — Zifan Yang, Haoyuan Zhang, Jialin Li et al. — [TokaGLINT: A Scalable GPU-Tailored Implicit Solver for Full 3D Tokamak Electromagnetic Simulations](http://arxiv.org/abs/2609.21366v1)
  <details><summary>📄 Abstract</summary>
  We introduce TokaGLINT, a GPU-accelerated implicit solver for electromagnetic field computations in full 3D tokamak simulations, aimed at efficient large-scale parallel GPU computing. Its central innovation lies in the co-design of hierarchical domain decomposition and a fast exact local solver, where hierarchical partitioning is tailored to match fine-grained intra-card subdomains and exploit the tensor-based solver dedicated to curvilinear-coordinate symplectic CN-FDTD-discretized 3D Maxwell e...
  </details>

- **2026-09-17** — Zhexiang Zhang, Minchen Yu, Yifan Sun et al. — [PixelFlow: Token-Level Workload Management for Efficient Distributed DiT Serving](http://arxiv.org/abs/2609.20723v1)
  <details><summary>📄 Abstract</summary>
  Online image generation with Diffusion Transformers (DiTs) must meet latency service-level objectives (SLOs) while using GPU resources efficiently. Existing systems improve GPU utilization by batching multiple requests for joint execution. However, request-level batching offers limited control over batch size: batches may be too small to saturate GPU compute, while larger ones may violate latency SLOs. Globally coordinated scheduling introduces further delays by requiring independently progressi...
  </details>

- **2026-09-17** — Sarah Radway, Andrew Cheng, Vijay Janapa Reddi et al. — [Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape](http://arxiv.org/abs/2609.20614v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI models are rapidly gaining the ability to exploit vulnerabilities in complex pieces of software. The risk is not theoretical, as evidenced by recent sandbox escapes performed by frontier models at OpenAI and Anthropic. Discussions of how to sandbox inference stack components often focus on components other than the inference engine itself (e.g., network proxies or code execution environments). However, the inference engine is an attractive target for a misaligned model. For example, ...
  </details>

- **2026-09-17** — Zihan Gong, Xiaohan Ye, Jiangchao Yao et al. — [Reasoning Quality Matters: Combating Reasoning Collapse in LLM-based Embedding Learning](http://arxiv.org/abs/2609.20563v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have recently shown strong potential for producing context-rich text embeddings for retrieval. Most existing methods either treat embedding learning as passive feature extraction or exploit LLM reasoning through instruction following for better embedding optimization. However, specialization toward embedding objectives can suppress useful reasoning generation or produce retrieval-irrelevant text. We refer to these two forms of degradation as reasoning collapse. To ad...
  </details>

- **2026-09-17** — Chao Huang, Meng Tong, Kejiang Chen — [Fingerprinting Multimodal Large Language Models](http://arxiv.org/abs/2609.20457v1)
  <details><summary>📄 Abstract</summary>
  While multimodal large language models (MLLMs) enable a wide range of image-text reasoning tasks, recent incidents indicate that they are vulnerable to illicit deployment and unauthorized distillation. Existing solutions for model provenance are typically confounded by shared language backbones in MLLMs and struggle to detect violations of distillation. To bridge this gap and safeguard model ownership, we present the first study on multimodal model fingerprinting. Inspired by recent findings tha...
  </details>

- **2026-09-17** — Roy Eisenstadt, Ido Cohen, Edo Cohen-Karlik et al. — [To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model Signals](http://arxiv.org/abs/2609.20186v1)
  <details><summary>📄 Abstract</summary>
  Speculative Decoding (SD) has significantly accelerated Large Language Model (LLM) inference, yet existing approaches face a fundamental tradeoff between two drafting strategies: neural drafting and context-based copying. Neural drafts (e.g., EAGLE3) provide robust performance across diverse text settings, while copy-based methods achieve higher speedups in copy-intensive regimes by generating candidates faster and exploiting long repetition spans for near-perfect speculation. We analyze existin...
  </details>

- **2026-09-17** — Dhananjay Tomar, Marius Aasan, Andreas Kleppe et al. — [A Smaller Transformer in Your Transformer](http://arxiv.org/abs/2609.20100v1)
  <details><summary>📄 Abstract</summary>
  Recent findings indicate that Vision Transformers settle into locally similar computational phases, implying a level of depthwise computational redundancy. However, existing methods to exploit this redundancy either fail to reduce inference compute or severely degrade model expressivity. In this work, we formalise a unified view of block redundancy that decouples the geometry from specific surrogate interventions. We then introduce Transformer-Within-Transformer (TWT), a post-hoc method that fus...
  </details>

- **2026-09-17** — Dongming Wang, Wei Ren — [Distributed Continuous-Time Optimization on the Special Orthogonal Group SO(3) over Tree Interaction Graphs](http://arxiv.org/abs/2609.20031v1)
  <details><summary>📄 Abstract</summary>
  We study continuous-time distributed optimization on the three-dimensional rotation group over undirected tree graphs, where agents with heterogeneous local costs seek a common attitude minimizing the geodesically strongly convex sum of their costs on a geodesically convex operating ball. We propose a nonsmooth protocol with fixed gains that combines local Riemannian gradient descent with signum-based consensus feedback computed from the Lie-group logarithms of relative rotations between neighbo...
  </details>

- **2026-09-17** — Yitong Xing, Yuhao Cheng, Yanping Li et al. — [Enhanced Knowledge Distillation for Detection Transformer via Teacher Prediction Refinement](http://arxiv.org/abs/2609.19964v1)
  <details><summary>📄 Abstract</summary>
  Detection Transformers (DETRs) achieve strong performance in object detection but remain challenging to deploy on edge devices due to their high computational cost. Existing DETR distillation methods mainly focus on aligning distillation points, while largely overlooking the quality of the teacher's supervision itself. We observe that due to stage-wise non-monotonic prediction behavior in DETRs, well-localized or correctly classified predictions from earlier stages may degrade in later ones, and...
  </details>

- **2026-09-17** — Wonmi Choi, Minuk Park, Zhixiong Niu et al. — [Not All AI Agents Are Equal: Characterizing Resource and Performance Dynamics](http://arxiv.org/abs/2609.19947v1)
  <details><summary>📄 Abstract</summary>
  LLM-based AI agents process user requests through iterative reasoning and tool execution, often involving the invocation of remote LLM APIs with local tool containers. This execution model can make the optimization of agent serving difficult because latency, local resource demand, and container bottlenecks inter-mix across requests. However, the current agent ecosystem runs without much consideration of resource dynamics, which results in significant waste of the precious resources. This paper a...
  </details>

- **2026-09-17** — Yi Su, Hong Liu, Guanghua Yu et al. — [D-Quant: Driftable Entropy Coding for KV Cache Quantization](http://arxiv.org/abs/2609.19880v1)
  <details><summary>📄 Abstract</summary>
  The KV cache has become a major bottleneck in deploying LLMs, as its memory footprint grows linearly with sequence length and batch size, imposing substantial pressure on both memory capacity and bandwidth. Among various KV cache compression techniques, quantization is particularly attractive due to its effectiveness and ease of deployment. However, most existing methods rely on fixed-width quantization, where a $b$ bit representation is inherently limited to $2^b$ quantization levels. As the bi...
  </details>

- **2026-09-17** — Ruchao Bao, Wenzheng Wu, Chucheng Xiang et al. — [PART: Learning 3D Part Assembly and Retrieval with Transformers](http://arxiv.org/abs/2609.19872v1)
  <details><summary>📄 Abstract</summary>
  3D assembly is fundamental to modern manufacturing and digital content creation. In this paper, we present PART, a unified transformer-based framework for 3D part retrieval and assembly: given a target shape and a part library, PART automatically selects the appropriate parts and predicts their 6-DoF poses to reconstruct the target. While prior work has achieved impressive progress on assembling a pre-defined set of parts, this more practical retrieval-based setting remains largely unexplored. T...
  </details>

- **2026-09-17** — Haya Halimeh, Sascha Kaltenpoth, Kevin Bösch et al. — [A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents](http://arxiv.org/abs/2609.19843v1)
  <details><summary>📄 Abstract</summary>
  LLM-based GUI agents increasingly act on behalf of users in digital environments that were designed with human users in mind. These graphical user interfaces were designed to support, but also deliberately steer, the behaviour and decisions of users. While behavioural biases in the textual outputs of LLMs are well-documented, far less is known about how such influence operates when models act as agents that perceive interfaces and execute decisions---and, in particular, whether the reasoning cap...
  </details>

- **2026-09-17** — Yingxuan Zhuang, Binhe Yu, Jingxiao Yang et al. — [Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution and Trajectory Mass Normalization](http://arxiv.org/abs/2609.19830v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for LLM agents involves two distinct optimization di- mensions: how environment feedback is exploited within a trajectory, and how complete trajectories are aggregated across a batch. We formulate these dimen- sions as Intra-Trajectory Feedback Attribution and Inter-Trajectory Objec- tive Aggregation, and introduce BATON (Bayesian Attribution and Trajectory Objective Normalization), a dual-axis policy optimization framework. BATON instantiates the first axis with Bayesian ...
  </details>

- **2026-09-17** — Luis Leal — [Steering Equilibrium Selection in Regularized Self-Play via the Reference Policy](http://arxiv.org/abs/2609.19820v1)
  <details><summary>📄 Abstract</summary>
  Regularized self-play -- the family behind DeepNash's Stratego play -- drives a two-player zero-sum policy to a Nash equilibrium by best-responding to a slowly moving, entropy-regularized reference policy $ρ$. When the game has a polytope of value-equivalent equilibria, the regularizer silently breaks the tie: with a uniform reference it selects the maximum-entropy member, the I-projection of $ρ$ onto the Nash set. Can the reference be used to choose the equilibrium on purpose? On five exactly s...
  </details>

- **2026-09-17** — Seong-Jun Kim, Seung-Hyun Kong — [Vehicle Trajectory Prediction via Neural Fusion of Multiple EKF-Based Trajectory Candidates](http://arxiv.org/abs/2609.19813v1)
  <details><summary>📄 Abstract</summary>
  Predicting the future trajectories of surrounding vehicles in autonomous driving is important for collision risk assessment and safe ego-vehicle path planning. Conventional neural network-based trajectory predictors typically achieve strong prediction performance by exploiting agent history, dynamic scene graphs, and semantic maps. However, in specific motion regimes such as acceleration, deceleration, and turning, these predictors may fail to reflect physically feasible trajectories. To address...
  </details>

- **2026-09-17** — Hyeongjun Choi, Wonyoung Jung, Haehoon Seo et al. — [ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers](http://arxiv.org/abs/2609.19722v1)
  <details><summary>📄 Abstract</summary>
  Large language models are being integrated into malware triage workflows as reasoning components that summarize static evidence and produce analyst-facing verdicts. This paper shows that the same reasoning capability introduces a new attack surface. We present ALIBI, a semantic cover story attack against frontier LLM-based malware analyzers. ALIBI adds a small, non-executed read-only section to a compiled binary, containing a coherent but false security product narrative, without altering import...
  </details>

- **2026-09-17** — Mengxiao Wang, Nitesh Saxena — [SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes](http://arxiv.org/abs/2609.19705v1)
  <details><summary>📄 Abstract</summary>
  Autonomous large language model (LLM) agents are moving rapidly into high-stakes domains, yet existing agentic-AI security studies remain largely domain-agnostic and overlook the distinctive, high-consequence attack surface such settings create. We examine this gap through financial trading agents, a representative case of high-stakes agentic security, where a single compromised agent has direct execution authority over real capital in an adversarial, reflexive market. To this end, we present FA...
  </details>

- **2026-09-17** — Gang Bao, Yixuan Zhang, Jiaqi Yu — [A c-transform optimal transport method for high-contrast freeform reflector design](http://arxiv.org/abs/2609.19663v1)
  <details><summary>📄 Abstract</summary>
  Design of high-contrast freeform reflectors is challenging, as the presence of zero-intensity regions leads to degeneracy in the associated Monge-Ampere-type equation. A common remedy is to add a positive artificial background to the target intensity, which improves the regularity of the equation. However, this regularization inevitably reduces the achievable illumination contrast and introduces nonzero intensity into regions that are intended to remain dark. We propose a fast c-transform method...
  </details>

- **2026-09-17** — Celestino Angeli — [Symmetry-driven correlation patterns in one-dimensional periodic fermionic systems: closed-form expressions and exact selection rules for correlation functions, entanglement entropies and mutual information](http://arxiv.org/abs/2609.19535v1)
  <details><summary>📄 Abstract</summary>
  We present an analytical study of the spatial structure of correlations in periodic fermionic systems at the single Slater determinant level, focusing on the cyclic case. Exploiting cyclic symmetry, the transformation from localized orbitals to molecular orbitals is simultaneously a discrete Fourier transform, a Vandermonde matrix on the roots of unity, a complex Hadamard matrix, and the character table of the cyclic group $C_m$. Within this framework, the spatial structure of correlations is fu...
  </details>

- **2026-09-16** — Xiaoyang Zhan, Shiyu Chen, Kenji Shimada — [Pose-aware Legged Robot Semantic Exploration with Omnidirectional Perception in Confined Unknown Environments](http://arxiv.org/abs/2609.19460v1)
  <details><summary>📄 Abstract</summary>
  Semantic exploration in confined environments requires both environment mapping and detailed observation of target objects. For ground robots, limited sensor vertical fields of view and restricted standoff distances can leave upper object surfaces unobserved from planar viewpoints. Body tilting can improve coverage, but additional observations and posture transitions increase mission time. To address this trade-off, we present POSE, a pose-aware semantic exploration system that exploits a legged...
  </details>

- **2026-09-16** — Karthikeyan Sankaralingam — [Rosetta: Automating First-Principles Performance Modeling Using Multi-Agent LLMs](http://arxiv.org/abs/2609.19376v1)
  <details><summary>📄 Abstract</summary>
  Analytical performance models --- derivations of throughput or speedup from hardware parameters --- make claims independently verifiable and expose binding constraints, yet rarely accompany architecture papers because building one by hand takes weeks of expert effort. We present Rosetta, a multi-agent LLM pipeline that automatically generates first-principles analytical models from research paper PDFs. Given a paper as sole input, Rosetta produces a mathematical specification, an executable Pyth...
  </details>

- **2026-09-16** — Aude Corbeel, Jingxin Tu, Pim van den Heuvel et al. — [Algebraic Complexity and Black Hole Complementarity](http://arxiv.org/abs/2609.19267v1)
  <details><summary>📄 Abstract</summary>
  We develop an operator algebraic generalization of the Yoshida-Kitaev information recovery protocol that applies to von Neumann algebras of arbitrary type. The construction is based on finite-index inclusions, with the Jones basic construction and canonical endomorphisms providing the central algebraic tools. Unlike the finite-dimensional qubit description, the infinite-dimensional theory exhibits new structural phenomena that play an essential role in information recovery. In particular, the di...
  </details>

- **2026-09-16** — Shahram Najam Syed, Arthur Jakobsson, Prayuj Sachdev et al. — [Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models](http://arxiv.org/abs/2609.18084v2)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a Vision-Language-Action (VLA) model for a new deployment environment is expensive, yet most methods apply uniform-capacity adapters to every network region as if every region requires equal adjustment. This paper tests that assumption on five architecturally diverse VLAs (OpenVLA-OFT, $π_0$, SmolVLA, DTP, Octo; 93M-7B parameters). Measuring per-region adaptation cost as normalized parameter displacement under region-isolated fine-tuning reveals an adaptation spectrum in which appear...
  </details>

- **2026-09-16** — En-Ming Huang, Yao-Ting Hsieh, Hsiang-Yu Tsou et al. — [Towards Training Private LLMs: Exploring Fine-Tuning Language Models on Apple Silicon with RDMA over Thunderbolt](http://arxiv.org/abs/2609.18066v2)
  <details><summary>📄 Abstract</summary>
  Private large language model (LLM) fine-tuning is increasingly important for organizations that need to adapt models using sensitive data, but it often exceeds the memory capacity of commodity datacenter accelerators. Apple Silicon offers a different design point through large unified memory and lower complete-system cost, while recent Apple software support enables distributed execution over RDMA-over-Thunderbolt (TB). This paper studies whether Apple Silicon can serve as a practical platform f...
  </details>

- **2026-09-16** — Xinshuai Guo, Junjie Wu, Dolly Deng et al. — [Beyond Outcomes: Dual-View Relational Learning for Efficient Agent Benchmarking](http://arxiv.org/abs/2609.18909v1)
  <details><summary>📄 Abstract</summary>
  Agent benchmarks are substantially more costly to evaluate than conventional LLM benchmarks. Benchmark compression is therefore a natural solution, yet existing methods primarily model redundancy in task--model final-score distributions, which is important in agentic evaluation. To address this limitation, we analyze large-scale trajectories and identify six complementary process signals that are systematically associated with final agent performance. To disentangle agent performance redundancy ...
  </details>

- **2026-09-16** — Jean-Charles Noirot Ferrand, David Adei, Anders Møller et al. — [CASHEWS: Source Preprocessor for LLM-based Malicious Package Detection](http://arxiv.org/abs/2609.18862v1)
  <details><summary>📄 Abstract</summary>
  Malicious npm package detection tools now leverage LLMs' semantic understanding of source code to detect malicious intent at scale. This capability has proven invaluable in identifying packages involved in recent supply-chain attacks such as Shai-Hulud. However, threat actors exploit the limited context windows of LLMs through JavaScript techniques such as code obfuscation that yields high token density and bundling malicious code with benign packages, causing detectors to skip large files or mi...
  </details>

- **2026-09-16** — Yanan Ma, Yihang Tao, Zhengru Fang et al. — [Learning from Distributed Eyes: Leveraging Collaborative Perception for Automated Model Adaptation](http://arxiv.org/abs/2609.18511v1)
  <details><summary>📄 Abstract</summary>
  In autonomous driving, perception models often struggle to generalize to new environments due to domain shifts. While unsupervised model adaptation offers a feasible solution without labor-intensive manual labeling, existing methods that rely solely on the ego-vehicle's data often lead to inferior pseudo-labeling performance. To address this critical issue, we propose LDE, Learning from Distributed ``Eyes", a novel framework that transforms collaborative perception (CP) into a source of high-qua...
  </details>

- **2026-09-16** — Jayakrishna Menon Vadayath, Hulin Wang, Moritz Schloegel et al. — [AIJon: Automated Generation of Annotations for Fuzzing](http://arxiv.org/abs/2609.18457v1)
  <details><summary>📄 Abstract</summary>
  Modern fuzzers use code coverage as feedback to guide their exploration which has proven to be an effective strategy for driving exploration. However, this strategy overlooks inputs that may be interesting to the target program even without uncovering new code paths. Fortunately, prior research has shown that annotations generated by human domain experts can provide additional feedback, guiding the fuzzer towards interesting parts of the program.   In this paper, we replicate experiments present...
  </details>

- **2026-09-16** — Chaofan Li, Zhengduo Xue, Chengxiang Li et al. — [From Component Snapshots to Lifecycle Traces: Agent-Based Software Composition Analysis](http://arxiv.org/abs/2609.18391v1)
  <details><summary>📄 Abstract</summary>
  Software supply-chain security requires accurate identification of third-party components and an understanding of how they evolve from development to execution. Existing software composition analysis (SCA) approaches examine manifests, build environments, release artifacts, containers, or runtime states, but typically produce only stage-specific views of software composition. As dependencies are resolved, removed, repackaged, and transformed across lifecycle stages, a single snapshot cannot capt...
  </details>

- **2026-09-16** — Minfeng Qi, Jialin Li, Tianqing Zhu et al. — [Detecting Logic Vulnerabilities Across the Contract and Device Layers of Blockchain-Enabled IoT With Multi-Agent Heterogeneous Graph Attention](http://arxiv.org/abs/2609.18344v1)
  <details><summary>📄 Abstract</summary>
  Blockchain-enabled Internet of Things (IoT) systems integrate smart contracts with embedded devices to support decentralized device management and access control. Their security therefore depends jointly on the logic of on-chain contracts and off-chain device firmware. Logic flaws in either layer can violate the same system invariants, such as unauthorized access, improper state changes, or unguarded privileged operations. Existing approaches rely on contract analysis, firmware analysis, and gra...
  </details>

- **2026-09-16** — Changxin Wei, Jun Ma, Xintong Dong — [A general lightweight global modeling framework for three-dimensional seismic exploration](http://arxiv.org/abs/2609.18294v1)
  <details><summary>📄 Abstract</summary>
  In seismic exploration, the propagation of seismic waves naturally gives rise to long-range dependencies in seismic data. Capturing such global correlations can significantly improve the accuracies of seismic signal processing, inversion, and interpretation. Global modeling (GM) methods have therefore emerged as an effective paradigm for seismic exploration, offering a powerful means of exploiting the intrinsic global relationships within seismic data. However, the mainstream GM approaches, part...
  </details>

- **2026-09-16** — Murali Ediga, Sudipta Chattopadhyay — [Measuring and Exploiting Implicit Trust in LLM Tool-Calling Pipelines](http://arxiv.org/abs/2609.18217v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) enables LLMs to invoke external tools, but every tool interaction exposes the model to attacker-controlled text through multiple input channels (tool descriptions, tool results, sampling messages) that share a single context window without privilege separation. In this paper, we present a framework to measure the trust profile of an arbitrary LLM based on a variety of payload framings sent through different channels. Following this assessment, we devise cross-cha...
  </details>

- **2026-09-16** — Yongkang Cheng, Che-Yung Shen, Yuntian Wang et al. — [Wavelength-Multiplexed Nonlinear Computing with a Single-Layer Diffractive Optical Processor](http://arxiv.org/abs/2609.18155v1)
  <details><summary>📄 Abstract</summary>
  Diffractive optical processors provide a promising platform for high-throughput, low-latency analog computing by exploiting engineered wave propagation to transform optical fields. However, implementing nonlinear mappings in optical hardware remains challenging. Here, we introduce a wavelength-multiplexed encoding-and-decoding (E+D) diffractive processor that exploits multiple illumination wavelengths to enhance the nonlinear function-approximation capability of a compact single-layer diffractiv...
  </details>

- **2026-09-16** — Lu Han, Jin Wang, Yuchen Li et al. — [Benchmarking Tabular Foundation Models as Surrogates in Expensive Evolutionary Optimization](http://arxiv.org/abs/2609.18130v1)
  <details><summary>📄 Abstract</summary>
  Surrogate-assisted evolutionary algorithms (SAEAs) are effective methods for solving expensive optimization problems (EOPs), where surrogate models replace most expensive evaluations and critically influence the final optimization results. In recent years, tabular foundation models have advanced rapidly, and the Tabular Prior-data Fitted Network (TabPFN) has been adopted as a surrogate model for EOPs due to its strong predictive capability, demonstrating promising performance. Motivated by its p...
  </details>

- **2026-09-16** — Shahram Najam Syed, Arthur Jakobsson, Prayuj Sachdev et al. — [Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models](http://arxiv.org/abs/2609.18084v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a Vision-Language-Action (VLA) model for a new deployment environment is expensive, yet most methods apply uniform-capacity adapters to every network region as if every region requires equal adjustment. This paper tests that assumption on five architecturally diverse VLAs (OpenVLA-OFT, $π_0$, SmolVLA, DTP, Octo; 93M-7B parameters). Measuring per-region adaptation cost as normalized parameter displacement under region-isolated fine-tuning reveals an adaptation spectrum in which appear...
  </details>

- **2026-09-16** — En-Ming Huang, Yao-Ting Hsieh, Hsiang-Yu Tsou et al. — [Towards Training Private LLMs: Exploring Fine-Tuning Language Models on Apple Silicon with RDMA over Thunderbolt](http://arxiv.org/abs/2609.18066v1)
  <details><summary>📄 Abstract</summary>
  Private large language model (LLM) fine-tuning is increasingly important for organizations that need to adapt models using sensitive data, but it often exceeds the memory capacity of commodity datacenter accelerators. Apple Silicon offers a different design point through large unified memory and lower complete-system cost, while recent Apple software support enables distributed execution over RDMA-over-Thunderbolt (TB). This paper studies whether Apple Silicon can serve as a practical platform f...
  </details>

- **2026-09-16** — João Pedro Silvestre, Álvaro Rodríguez Abella, Paulo Tabuada — [The Attention Within: Consensus Dynamics in Selective State Space Models](http://arxiv.org/abs/2609.17997v1)
  <details><summary>📄 Abstract</summary>
  Selective state space models (SSMs) have recently emerged as a compelling alternative to transformers, combining competitive performance with substantially improved inference efficiency. At each SSM layer, a sequence of hidden states are propagated by a recurrence, mixing information of different tokens. Despite using a different mechanism, this mixing plays a role analogous to attention in transformers. In fact, recent works have shown that the two architectures may be closer than they first ap...
  </details>

- **2026-09-15** — Xinle Yu, Fan Bai, Kaiser Sun et al. — [PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research](http://arxiv.org/abs/2609.17846v1)
  <details><summary>📄 Abstract</summary>
  Autonomous research agents aim to automate scientific workflows, from proposing ideas to conducting experiments and analyzing results. Yet current AI and research agents can propose more directions than available resources allow them to pursue. Moreover, each attempt could consume substantial resources, requiring agents to reconsider how to invest in subsequent research. Thus, deciding how to invest research effort strategically should be a defining capability of autonomous research agents. Acco...
  </details>

- **2026-09-15** — Akanksha Singh, Vinod K. Kurmi — [Not All Patches Are Equally Forgettable: Spatially Localized Domain Unlearning in Vision-Language Models](http://arxiv.org/abs/2609.17790v1)
  <details><summary>📄 Abstract</summary>
  Pre-trained vision-language models (VLMs) exhibit strong cross-domain recognition performance even without additional training. However, this robustness can also preserve undesirable domain-specific behavior, as domain-related and semantic information often remain entangled within the learned representation space, making selective domain unlearning challenging. Existing approaches typically address this problem through latent-space disentanglement and prompt- or feature-level interventions, with...
  </details>

- **2026-09-15** — Simone Teglia, Irene Amerini — [Unifying Semantic Priors and High-Frequency Traces: Enhancing V-JEPA with Mixture-of-Experts for Robust Synthetic Image Forensics](http://arxiv.org/abs/2609.16778v2)
  <details><summary>📄 Abstract</summary>
  The unchecked proliferation of manipulated images on social media platforms has increased the spread of misinformation, posing a severe threat to public trust and information integrity. Modern deepfake detectors typically rely on Vision Transformers (ViTs) to capture the low-level inconsistencies that characterize fully synthetic or locally tampered images. However, the global understanding of such foundation models is not enough to discriminate alone between real and fake multimedia content, es...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 56 papers

- **2026-09-18** — Parivesh Priye, Yufeng Wang, Haibin Ling et al. — [Available Guardrails: Certifying Selective Prediction across ML Systems](http://arxiv.org/abs/2609.22048v1)
  <details><summary>📄 Abstract</summary>
  A selective predictor acts as a safety gate: it returns an output only when the prediction appears sufficiently trustworthy. Deployments increasingly require this reliability to be certified at a target precision for every reporting unit of interest, such as a tool, policy label, or patient subgroup. The main difficulty is often not whether a granted certificate is valid, but whether finite calibration data can produce one at all. As the gate becomes safer or more fine-grained, some units may re...
  </details>

- **2026-09-18** — Fenghe Guo, Runjie Shen, Chenyang Sun et al. — [VIRGA: Virtual-Agent-Intermediated Riemannian Geometry for Active-Sensing Air-Ground Coordination](http://arxiv.org/abs/2609.21883v1)
  <details><summary>📄 Abstract</summary>
  Air-ground autonomy becomes harder when the unmanned aerial vehicle (UAV) must remain observable by a gimbal light detection and ranging (LiDAR) mounted on the unmanned ground vehicle (UGV). The platforms must avoid dynamic obstacles while coordinating heterogeneous motion, limited sensing, and changing task initiative within one closed loop. This paper presents VIRGA, a neural geometric coordination framework that turns dual-LiDAR observations into bounded source-specific Riemannian fields and ...
  </details>

- **2026-09-18** — Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid — [EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative AI in the Enterprise](http://arxiv.org/abs/2609.21841v1)
  <details><summary>📄 Abstract</summary>
  Frontier language models now produce professional deliverables that expert graders judge to match human work on a substantial share of economically valuable tasks, yet most enterprise GenAI initiatives fail to show a measurable business effect and a large fraction of agentic projects are expected to be cancelled. We argue that this is substantially a measurement problem: public benchmarks answer "what can the model do?", whereas a deployment decision requires "is this workflow fit, reliable, saf...
  </details>

- **2026-09-18** — Muhammad Rehan, Moaz Amjad, Syed Danial Ahmed et al. — [Detection is solved, delineation is not: what governs tooth segmentation on panoramic radiographs](http://arxiv.org/abs/2609.21628v1)
  <details><summary>📄 Abstract</summary>
  Automatic tooth segmentation and FDI numbering on panoramic radiographs underpins computer-assisted dental diagnosis, yet which factors govern performance remains unclear. We assemble a corpus of 1,422 panoramic radiographs containing 42,142 expert-delineated tooth polygons across the 32-class FDI taxonomy, annotated by 30 dental practitioners and independently reviewed by two others, and use it to isolate input resolution, architecture and anatomical priors under a single evaluation protocol.  ...
  </details>

- **2026-09-18** — André Lopo, Atabak Dehban, Rodrigo Ventura — [HAT: Hypothesis-Anchored Tracking for Video Monocular Spacecraft Pose Estimation](http://arxiv.org/abs/2609.21597v1)
  <details><summary>📄 Abstract</summary>
  Monocular 6-DoF pose estimation of non-cooperative targets is important for on-orbit servicing and debris removal. A single-image estimator can confuse near-symmetric spacecraft orientations, and tracking can preserve an incorrect pose. We present Hypothesis-Anchored Tracking (HAT), a causal framework that uses inter-frame motion to select among competing CAD-based pose hypotheses before alignment and fusion. Rather than independently choosing the highest-scoring hypothesis in each image, HAT re...
  </details>

- **2026-09-18** — Chang Dong, Mehdi Hosseinzadeh, King Hang Wong et al. — [ProTracer: Proprioception-Guided Failure Diagnosis in Robot Manipulation](http://arxiv.org/abs/2609.21369v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a comprehensive framework for robot manipulation failure analysis that includes binary failure detection, failure categorization, explanation generation, and the additional capability of failure onset localization, which aims to identify the earliest moment at which a robot execution deviates from a valid task-completion trajectory and is ultimately followed by task failure. To address these tasks, we propose ProTracer, a training-free framework that leverages existing Vision...
  </details>

- **2026-09-18** — Chenye Ke, Zirui Liu, Qi Liu et al. — [Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective](http://arxiv.org/abs/2609.21888v1)
  <details><summary>📄 Abstract</summary>
  Detecting pretraining data in large language models is challenging because high likelihood can reflect either training exposure or strong generalization. In the joint space of prediction loss and predictive entropy, a likelihood-only detector uses a horizontal boundary and can mistake predictable non-members for members. Motivated by this, we introduce an inclined boundary that evaluates prediction loss relative to predictive entropy. Our analysis shows that entropy correction can preserve the e...
  </details>

- **2026-09-18** — Youssef Attia El Hili, Malik Tiomoko, Corinne Ancourt — [LLM-Generated Feature Pools for Time Series Anomaly Detection](http://arxiv.org/abs/2609.21801v1)
  <details><summary>📄 Abstract</summary>
  We study how far a simple statistical pipeline can go on univariate time series anomaly detection under a strict selection protocol. The method extracts a small pool of statistics over sliding windows, scores each window with a transductive robust (MAD) model, and selects a feature subset per domain on a held-out tuning split. On TSB-AD-U it reaches $0.529$ per-series VUS-PR, above the best neural ($0.45$) and statistical ($0.44$) entries on the public leaderboard and within $0.06$ of the strong...
  </details>

- **2026-09-18** — Li Wang, Kunyu Feng, Wan Lin et al. — [GenTraceBench: A Benchmark for Tracing Audio Deepfakes Across Pre- and Post-training Stages](http://arxiv.org/abs/2609.21738v1)
  <details><summary>📄 Abstract</summary>
  Modern text-to-speech (TTS) systems are rarely deployed as unchanged pre-trained models. They are often adapted through supervised fine-tuning (SFT) or preference optimization such as DPO and GRPO. This raises a practical question for audio deepfake forensics: do fingerprints learned from a foundation generator remain valid after adaptation? We present GenTraceBench, a controlled benchmark spanning five TTS architectures, 16 pre-/post-training variants, and 49,728 utterances generated with fixed...
  </details>

- **2026-09-18** — Pufan Liu, Hui Li, Ziqi Li et al. — [LenNet: Direct Detection and Localization of Strong Gravitational Lenses in Wide-Field Sky Survey Images](http://arxiv.org/abs/2609.21661v1)
  <details><summary>📄 Abstract</summary>
  Strong gravitational lenses are invaluable tools for addressing fundamental questions in astrophysics, from the nature of dark matter to the expansion of the universe. While current sky surveys have successfully identified thousands of lens candidates, the search methods employed face a critical challenge. The conventional approach relies on a "crop-and-classify" strategy, where small images are first cut out around billions of potential host galaxies before being individually classified. This p...
  </details>

- **2026-09-18** — Subin Shin, Jaehoon Lee, Seok-Hwan Park et al. — [Fronthaul Compression for Uplink Cloud-RAN with Finite-Alphabet Inputs: A Reverse Mercury/Waterfilling Approach](http://arxiv.org/abs/2609.21265v1)
  <details><summary>📄 Abstract</summary>
  The cloud radio access network (C-RAN) mitigates inter-cell interference by jointly processing the observations of distributed remote units (RUs) at a centralized unit (CU), but limited fronthaul capacity forces each RU to compress its received signal. Under transform-compress-forward, an RU transforms its signal and quantizes the resulting coefficients, with bit allocation distributing a finite bit budget across them. Classical reverse waterfilling assumes Gaussian sources, yet practical finite...
  </details>

- **2026-09-17** — Leilei Chen, Lan Zhang, Chen Tang et al. — [The More It Says, the More You Pay: A Black-Box Audit of Provider-Side Token Inflation in LLM Services](http://arxiv.org/abs/2609.20370v1)
  <details><summary>📄 Abstract</summary>
  In pay-per-token LLM services, the more a model says, the more users pay. Dishonest providers can covertly manipulate generation to inflate output tokens while largely preserving task utility. We define such manipulation as a Provider-Side Token Inflation Attack (PTIA) and instantiate five representative attacks at the query, prompt, representation, and model levels of the provider-controlled pipeline. Our experiments show that each attack increases mean output length to more than 10.2x the clea...
  </details>

- **2026-09-17** — Xin Chen, Gil Kur, Alexander Shevchenko et al. — [Local Sparsity Enables Unsupervised LLM Safety Detection](http://arxiv.org/abs/2609.20129v1)
  <details><summary>📄 Abstract</summary>
  Deployment-time safety methods for large language models (LLMs) are predominantly supervised and assume access to unsafe training data. Nevertheless, new attacks and harm categories regularly arise, not captured by models trained in such a supervised fashion. An alternative approach is to view this problem through the lens of anomaly detection, namely, to rely solely on modeling safe data and flagging out-of-distribution inputs. However, LLM activations lie in a high-dimensional space, raising c...
  </details>

- **2026-09-17** — Wenjie Liao, Liangjie Zhao, Zehong Cao — [UnifiedPlayers: Enhance Tool-Integrated Reasoning in Agentic Reinforcement Learning](http://arxiv.org/abs/2609.20089v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving methods reduce the need for human-annotated trajectories by allowing tool-using agents to generate their own training data. Yet existing methods typically separate trajectory generation from evaluation, relying on static verifiers that cannot adapt to emerging failure modes or self-consistency signals that may reinforce errors shared across trajectories. Jointly adapting planning, execution, and evaluation offers a promising alternative, but introduces a fundamental coordination ch...
  </details>

- **2026-09-17** — Xiang Li, Pin-Yu Chen, Wenqi Wei — [Robust Workflow Generation via Adversarial Learning for Audio Deepfake Detection](http://arxiv.org/abs/2609.20063v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of speech synthesis and voice conversion technologies has made audio deepfakes increasingly realistic, posing serious security risks in practical applications. While existing detection methods achieve strong performance under controlled conditions, they often fail to generalize under real-world perturbations and corruptions. In this paper, we propose ROGUE, a framework that dynamically constructs robust detection workflows by orchestrating multiple detection tools. ROGUE fo...
  </details>

- **2026-09-17** — Jinbang Huang, Yuanzhao Hu, Zhiyuan Li et al. — [StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation](http://arxiv.org/abs/2609.20791v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical planning frameworks combine skills from multiple robot control policies for long-horizon task execution, where determining when to terminate the current skill and advance to the next subtask is essential. Existing approaches often rely on pre-designed completion signal checkers that are hard to obtain in real-world execution. Large-scale vision-language models (VLMs) offer strong reasoning capabilities, but their decision boundaries are not inherently aligned with task completion cr...
  </details>

- **2026-09-17** — Sarah Wyer, Sue Black, Noura Al Moubayed — [Harm Laundering in GPT Models: Evidence That Gender Discrimination Is Transformed Rather Than Reduced Across Safety-Trained Generations](http://arxiv.org/abs/2609.20779v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluations for large language models rely on surface-form classifiers that report declining harm scores across model generations. We provide evidence that this methodology is systematically incomplete: explicit discriminatory content is transformed rather than removed. We call this \emph{harm laundering}. Analysing 450,000 gender-directed completions across 15 models spanning GPT-2 through to GPT-5 (OpenAI GPT lineage; three demographic conditions), we show that sexual violence clusters ...
  </details>

- **2026-09-17** — Thomas Berkane, Anne Bischops, Anika Mellacheruvu et al. — [What Parents Can See: Divergent Accounts of Youth AI Companion Use in Parenting and Teenager Subreddits](http://arxiv.org/abs/2609.20720v1)
  <details><summary>📄 Abstract</summary>
  Youth increasingly use AI companions, and parents are the primary mediators of that use. How effective that mediation can be depends on whether parents are aware of how adolescents actually use these systems and what risks and benefits such use carries; nevertheless, prior work has only studied these demographic groups in isolation, and existing taxonomies attend almost entirely to risk. We analyze 1,628 Reddit posts about youth AI companion use from parenting and teenager communities (2023--202...
  </details>

- **2026-09-17** — Yupei Li, Manuel Milling, Berrak Sisman et al. — [Position Paper: Neurotransmitters as a Missing Dimension in Artificial Neural Networks](http://arxiv.org/abs/2609.20083v1)
  <details><summary>📄 Abstract</summary>
  Artificial neural networks (ANNs), as core components of modern deep learning (DL) systems, lack the adaptive flexibility and long-term stability exhibited by biological systems. This limitation largely stems from the fact that conventional ANNs rely on uniform, local, and gradient-based parameter updates, while neglecting internal learning principles that are biological mechanisms such as neurotransmitters signalling or neuroplasticity. Consequently, many existing approaches focus on architectu...
  </details>

- **2026-09-17** — Gioliano de Oliveira Braga, Sidnei Barbieri, Ágney Lopes Roth Ferraz et al. — [A Proposal for an Agentic AI Architecture to Support Multi-Domain Decision-Making in the Brazilian Armed Forces](http://arxiv.org/abs/2609.20080v1)
  <details><summary>📄 Abstract</summary>
  The growing complexity of multi-domain operational environments (land, aerospace, naval, cyber, and electromagnetic spectrum) has increased the volume and velocity of data reaching command-and-control (C2) centers, straining the observe-orient-decide-act (OODA) decision cycle. Artificial Intelligence (AI) systems currently employed in defense are, in general, reactive and isolated tools that still rely heavily on human operators to integrate information, assess scenarios, and formulate courses o...
  </details>

- **2026-09-17** — Yuejin Xie, Yu Li, Dadi Guo et al. — [ClashBench: Conflicts Leading Agents to Seize and Harm](http://arxiv.org/abs/2609.19892v1)
  <details><summary>📄 Abstract</summary>
  As agent systems become more widely used, multiple agent sessions increasingly run alongside pre-existing user tasks in the same environment, sharing resources with limited capacity or mutually exclusive states. This creates a safety risk: when granted sufficient privileges, an agent may resolve a resource conflict by terminating or otherwise disrupting an existing task rather than reporting it. In this work, we identify and formalize this failure mode, which we term destructive resource preempt...
  </details>

- **2026-09-17** — Giuseppe Samo, Vivi Nastase, Paola Merlo — [Generalization through Lexical Abstraction in Transformer Models: The Case of Functional Words](http://arxiv.org/abs/2609.19887v1)
  <details><summary>📄 Abstract</summary>
  Pronouns, adverbs and other functional words (such as they, her, somewhere, there) are often used in language to replace concrete nouns or phrases, when their properties - such as gender, grammatical number - provide sufficient information for the given context. Do pretrained transformer models encode such functional words in a manner that allows them to be used like humans do? Can language models recognize the syntactic and semantic parallelism of sentences such as "The researchers wrote the pa...
  </details>

- **2026-09-17** — Bo Xu, Chenyuan Wang, Xinyu Chen et al. — [Learn Before You Judge: Progressive Knowledge-to-Decision Alignment for Explainable Hateful Meme Detection](http://arxiv.org/abs/2609.19778v1)
  <details><summary>📄 Abstract</summary>
  Hateful memes spread abusive content through implicit interactions between images and text, posing serious threats to the safety of online communities. In recent years, multimodal large language models have been widely used for hateful meme detection and are increasingly adopted to generate explainable detection results. However, we find that existing explain-then-detect methods often couple explanation generation and label prediction within the same training process. This coupling causes interf...
  </details>

- **2026-09-17** — Yoshiaki Takashita — [Reachability, Not Observation: Containing Systems Whose Wiring Changes](http://arxiv.org/abs/2609.19720v1)
  <details><summary>📄 Abstract</summary>
  Containment decisions -- where to put a firewall, which links to monitor, what a program may reach -- are computed from an observed structure, and observation is a snapshot. We ask what a snapshot misses when the wiring changes over time. On a hypercube whose active dimension rotates, a balanced split shows zero crossing edges at 93% of instants, yet 8,192 edges must be blocked permanently; adding one always-on ring, a defender sees 2 where 8,194 must be blocked, a factor of 4,097. A time-aware ...
  </details>

- **2026-09-17** — Nguyen Duc Minh Quang, Chang Liu, Shuangyang Li et al. — [Agentic AI Networking for Heterogeneous Unmanned Aerial Systems in Low-Altitude Wireless Networks](http://arxiv.org/abs/2609.19538v1)
  <details><summary>📄 Abstract</summary>
  Low-altitude wireless networks (LAWNs) are emerging as a key infrastructure for heterogeneous unmanned aerial systems that support concurrent services within a shared three-dimensional airspace. Their coexistence creates strong coupling among mobility, connectivity, and shared network resources, while heterogeneous services impose distinct and time-varying requirements. These interactions naturally form a dynamic non-cooperative game in which both operating conditions and coordination objectives...
  </details>

- **2026-09-17** — Jian Gao, Hang Jiang — [When Hiring Becomes Agent-Mediated: Evaluating Access and Recurrence in Two-Agent Résumé Screening](http://arxiv.org/abs/2609.19530v1)
  <details><summary>📄 Abstract</summary>
  Hiring is bilateral: employers assess fit, while candidates present and defend evidence of their qualifications. Yet résumé screening, the first gate, is commonly automated as a static, one-call judgment over a résumé-job pair. We study a two-agent alternative in which employer-side and candidate-side agents represent these roles, exchange evidence, and update their judgments before deciding who advances. We compare procedures on 600 constructed résumé-job pairs using GPT-5.5 and Claude Opus 4.7...
  </details>

- **2026-09-17** — Jingtao Li, Qian Zhu, Xinyu Wang et al. — [Earth Surface Immune System for Rapid Monitoring of Unknown Anomalies](http://arxiv.org/abs/2609.20662v1)
  <details><summary>📄 Abstract</summary>
  Earth surface anomalies, driven by escalating climate change, and expanding human activities, are increasing in both frequency and diversity, yet their limited historical data and unpredictability make them fundamentally different from conventional remote sensing targets. Existing methods address specific anomaly categories or stop at localization, leaving a gap between detection and actionable information. Here we present ESIA, an Earth Surface Immune System whose architecture is constrained by...
  </details>

- **2026-09-17** — Khalid Halba, Kylie Cooper, James G. Bellingham — [A Simulation Platform for AUV Fault Recovery: Exploring LLM-Based Diagnostic Strategies](http://arxiv.org/abs/2609.20620v1)
  <details><summary>📄 Abstract</summary>
  Autonomous underwater vehicles (AUVs) operating beyond reliable communications must recover from failures without human intervention. We investigate an architecture in which conventional deterministic layered control autonomy manages normal operations, while an invokable large language model (LLM) serves as a diagnostic and recovery planner when onboard anomaly detection identifies performance outside expected limits. Because language models are stochastic, rigorous evaluation requires ensemble ...
  </details>

- **2026-09-17** — Matin Beiramvand, Reijo Koivula, Tarmo Lipping — [Practical flow state detection: Entropy-based EEG classification from portable EEG headbands](http://arxiv.org/abs/2609.19737v1)
  <details><summary>📄 Abstract</summary>
  Flow state, characterized by deep engagement and immersion during challenging activities, represents a valuable mental state with significant implications for learning, performance, and rehabilitation outcomes. While flow has been extensively studied behaviorally, objective neurophysiological detection methods suitable for real-world deployment remain limited. Electroencephalography (EEG) offers a promising avenue for flow detection due to its accessibility, portability, and superior temporal re...
  </details>

- **2026-09-17** — Dasom Choi, Sangjun Moon, Hyeongchan Im et al. — [IMFD: End-to-end Multi-Face Forgery Detection through Instruction-based Large Vision-Language Models](http://arxiv.org/abs/2609.19693v1)
  <details><summary>📄 Abstract</summary>
  The rapid increase of deepfakes has raised significant concerns due to their spread on social media. Traditional multi-face forgery detectors crop and verify each face independently, ignoring background context and inter-face relationships, which often yields suboptimal performance. To overcome these limitations, we leverage instruction-based Large Vision-Language Models (LVLMs), which can interpret entire images and follow complex textual instructions. We propose a simple yet effective single-s...
  </details>

- **2026-09-16** — Laxmipriya Ganesh Iyer — [Closed-World Resolution Against Tool Hallucination in LLM Agents](http://arxiv.org/abs/2609.19425v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented large language model (LLM) agents fail in a way no tool-selection or tool-security method addresses: they call tools that do not exist and pass arguments no schema declares. Existing defenses either pick the right tool (selection) or constrain what an agent may do with real tools (gating), both of which presuppose the emitted call refers to a real tool at all. We show this is a structural blind spot: a hallucinated call is by construction not a decision any gate made, so no gate c...
  </details>

- **2026-09-16** — Suparna Bhattacharya, Tarun Kumar, Cong Xu et al. — [Position: It is Time to Virtualize Foundation Models with a Self-evolving Operating System Layer](http://arxiv.org/abs/2609.19203v1)
  <details><summary>📄 Abstract</summary>
  AI applications have shifted from single, monolithic foundation models (FM) to compound agentic systems. Yet today's stacks remain fragmented: even as protocols (e.g., MCP, A2A) ease tool/agent connectivity, each framework embeds an implicit runtime for state, memory, budgets, and guardrails, making behavior non-portable and governance brittle. It mirrors computing before operating systems, when every program re-implemented basic services. This position paper argues that the field now needs a Fo...
  </details>

- **2026-09-16** — Reza Farahani, Naser Hossein Motlagh, Zoha Azimi et al. — [From Pixels to Semantics: Edge AI for UAV-Based Critical Infrastructure Inspection](http://arxiv.org/abs/2609.18448v1)
  <details><summary>📄 Abstract</summary>
  Critical infrastructure assets such as bridges, tunnels, dams, and power line networks require timely and scalable inspection. While conventional manual inspection remains costly and hazardous, unmanned aerial vehicle (UAV)-based inspection has emerged as an efficient alternative for monitoring difficult-to-access structures. Existing UAV inspection pipelines have evolved from cloud-centric offline processing toward edge-based perception using lightweight object detectors such as YOLO for real- ...
  </details>

- **2026-09-16** — Shardul P. More, Tanuja S. Pawar — [Attention Dispersion as a Diagnostic Signal for Hallucination in Large Language Models](http://arxiv.org/abs/2609.18320v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) frequently exhibit hallucinations, presenting a major barrier to reliability in complex reasoning tasks. While traditional detection methods rely on output-based confidence metrics, these logits are often miscalibrated by modern alignment techniques. In this paper, we investigate the temporal volatility of internal attention mechanisms as an alternative diagnostic signal for hallucination that does not depend on output calibration. By introducing an unsupervised metr...
  </details>

- **2026-09-16** — Mohamed Chahine Ghanem — [Who Audits Whom, on What Substrate, with What Evidence? An Independence-Graded Audit Protocol for Agentic AI](http://arxiv.org/abs/2609.18272v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems plan, invoke tools and act with limited supervision; they are now both the subject of audits and, increasingly, the auditor. Independence, the foundation of assurance,is still applied to them as a binary. We argue that it must be graded along three orthogonal axes: principal independence (who controls the auditor), substrate independence (an auditor sharing the auditee's foundation-model family, toolchain or guardrails fails with it) and evidence independence (whether evidence...
  </details>

- **2026-09-16** — Leon Bergen, Usha Bhalla, Andrew Lee et al. — [Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations](http://arxiv.org/abs/2609.19101v1)
  <details><summary>📄 Abstract</summary>
  As models scale, reward hacking becomes more frequent, more sophisticated, and more consequential. Does it leave a telltale signature in model representations? This work analyzes how reward hacking is represented internally in frontier open source LLMs, and how those representations can be used to understand and discover the range of hacking behaviors a model displays. In particular, we find that simple difference of means vectors coherently represent reward hacking in Kimi K3, GLM 5.2, and Qwen...
  </details>

- **2026-09-16** — Muhammad Abdullah Sohail — [When Agents Look Like Beacons: NIDS Evasion by Model Context Protocol Traffic](http://arxiv.org/abs/2609.19091v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) standardizes communication between autonomous Artificial Intelligence (AI) agents and remote tools over Streamable HTTP. This shift introduces a class of machine-generated, authenticated, and high-frequency JSON-RPC traffic directly into enterprise networks. Enterprise network defenders have historically relied on machine-like cadence as an Indicator of Compromise (IoC). In this study, we show that without explicit network-layer indication, MCP traffic structural...
  </details>

- **2026-09-16** — Xiangfan Wu, Zonghao Ying, Huiyu Wu et al. — [Collective Loss of Control in LLM Agent Systems: An Epidemic Account of Mutation, Contagion, and Recovery](http://arxiv.org/abs/2609.18460v1)
  <details><summary>📄 Abstract</summary>
  How does a multi-agent system evolve from a local deviation into collective loss of control? We propose an epidemic explanation organized around accidental mutation, contagion, and recovery. A spontaneous deviation creates a seed; communication enables other agents to adopt and retransmit its unsafe strategy; collective failure can emerge when propagation outpaces correction and containment. Thus, rare individual deviations can coexist with substantial collective risk. Motivated by reported Open...
  </details>

- **2026-09-16** — Reece O'Mahoney, Ioannis Havoutis — [DistAL: Distance-based Advantage Learning for VLA Fine-Tuning](http://arxiv.org/abs/2609.18392v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action models (VLAs) have trans- formed the field of robotic manipulation in recent years by combining the semantic understanding of LLMs with the precise control of flow-matching policies. Advantage conditioning is a recent technique that iteratively improves VLAs by training a value function on deployment data and using this to train an advantage-conditioned policy. Previous works have only applied simple, low-information success/failure rewards, which leave the value function ...
  </details>

- **2026-09-16** — Loris Schneider, Edgar Welte, Rania Rayyes — [RAFAIL: Relationship-Aware Failure Detection for Robotic Manipulation](http://arxiv.org/abs/2609.18324v1)
  <details><summary>📄 Abstract</summary>
  Detecting failures during execution is essential for reliable robotic manipulation. Vision-language models (VLMs) can assess task outcomes semantically but add runtime computation, whereas out-of-distribution (OOD) detectors may respond to harmless scene variations rather than failure-relevant deviations. We introduce RAFAIL, a framework for detecting execution failures during robotic manipulation. RAFAIL identifies failures by detecting anomalies in task-relevant relationships between entities,...
  </details>

- **2026-09-16** — Jiahui Chen, Bingke Zhu, Hongyu Pan et al. — [WaveTLM: Reliable Time-Series Language Modeling through Task Compilation](http://arxiv.org/abs/2609.18812v1)
  <details><summary>📄 Abstract</summary>
  Time-series language models provide a shared natural-language interface across temporal tasks, but plausible text does not guarantee reliable task outputs. Responses may appear reasonable while hallucinating the required object: numerical sequences can violate shape, scale, channel order, or temporal alignment, and textual decisions can fall outside the legal label space. We formulate reliable time-series language modeling, separating task-object reliability from predictive quality. We introduce...
  </details>

- **2026-09-16** — Liyang Fan, Xinping Bi, Yitai Li et al. — [RankGround: Efficient High-Resolution GUI Grounding via Lightweight Reranker-Guided Crop Selection](http://arxiv.org/abs/2609.18690v1)
  <details><summary>📄 Abstract</summary>
  Graphical User Interface (GUI) grounding is a fundamental perception task for multimodal agents, enabling them to interpret natural language instructions and interact with digital interfaces. Existing methods face a fundamental trade-off between accuracy and efficiency: direct full-image inference often fails to capture small or visually similar UI elements, while multi-crop strategies improve localization at the cost of multiple expensive Vision-Language Model (VLM) calls per query.   To addres...
  </details>

- **2026-09-16** — Mika Okamoto, Ansel Kaplan Erol — [PACT: Can Enterprise AI Assistants Be Trusted Under Pressure?](http://arxiv.org/abs/2609.18605v1)
  <details><summary>📄 Abstract</summary>
  As corporate AI adoption continues to grow, enterprise-grade LLM agents are being deployed into sensitive contexts such as hiring, healthcare, and finance. In these contexts, compliance with rules specified in an agent's system context is a first-order legal concern. Currently, no evaluation framework systematically measures which LLM models tend to violate compliance rules, especially under pressure from a persistent user, a hurried manager, or circumstances where violation is convenient or att...
  </details>

- **2026-09-16** — Md Taimur Ahad, Ainuddin Ahmed — [A Lightweight CNN Integrated Compact Convolutional Transformer for Multi-Scale Feature Learning and reducing computational complexity for breast cancer mammography image detection and classification](http://arxiv.org/abs/2609.18212v1)
  <details><summary>📄 Abstract</summary>
  Over the years, Convolutional Neural Networks (CNNs) have demonstrated strong capability in cancer detection and classification using medical images. However, CNN-based models often struggle to capture long-range contextual dependencies. In such scenarios, integrating Compact Convolutional Transformer (CCT) architectures after the CCT layer allows CNN-extracted features to reshape into compact patch tokens using a CCT tokenizer, followed by the addition of positional embeddings to preserve spati...
  </details>

- **2026-09-16** — Shijie Chen, Yu Gan, Yeounoh Chung et al. — [DualSQL: Text-to-SQL with Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2609.18135v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art Text-to-SQL systems are typically multi-agent pipelines centered around two fundamental tasks: schema linking and SQL generation. However, existing work trains separate models for each task, failing to leverage the synergy between these interrelated tasks. In this work, we propose DualSQL, a new Text-to-SQL system consisting of two agents powered by a single model backbone. The agents share the same model weights and agentic scaffold, enabling joint optimization through a robust...
  </details>

- **2026-09-16** — Dev Bali, Soujanya Ponnapalli, Yichuan Wang et al. — [Token Latency Fairness: Performance Isolation for Multi-Tenant LLM Serving](http://arxiv.org/abs/2609.18112v1)
  <details><summary>📄 Abstract</summary>
  LLM serving is typically offered as a shared, multi-tenant service, where high-demand workloads from one client can cause latency SLO violations for others. Existing solutions for performance isolation equalize client throughput in the long run, for example through queueing and batching fairness. However, these approaches do not provide latency isolation guarantees; as a result, well-behaved clients can still experience significant degradation to their token-level latencies.   In this paper, we ...
  </details>

- **2026-09-16** — Ricardo Vieira, Luis Tavares, Kaylane Lima et al. — [Large Language Model based air quality monitoring and localized alert generation](http://arxiv.org/abs/2609.17954v1)
  <details><summary>📄 Abstract</summary>
  Poor indoor air quality can cause up to five times more direct health problems to occupants than outdoor air. In particular, it may cause headaches, fatigue, eye/throat irritation, and long-time exposure is linked to respiratory and heart as well as some forms of cancer. Despite the importance of indoor health and well-being, most current monitoring devices and systems (usually for offices and workspaces) are passive. The Environmental Quality Monitor (EnQyMo) platform is a generic Internet of T...
  </details>

- **2026-09-15** — Precious Philip-Ifabiyi, Valerio Franchi, Fausto Ferreira et al. — [Multi-Session Multimodal Underwater Mapping with Acoustic and Optical Imaging](http://arxiv.org/abs/2609.17929v1)
  <details><summary>📄 Abstract</summary>
  Accurate seafloor mapping is essential for marine science, archaeology, and environmental monitoring. However, integrating data from different sensors, such as side-scan sonar and optical cameras, collected across separate survey sessions, remains challenging due to positioning drift and sensor offsets. This paper presents a multi-session, multimodal underwater mapping framework based on factor graph optimization. The method jointly optimizes vehicle trajectories, 3D landmark positions, sensor e...
  </details>

- **2026-09-15** — Houlin Zhou, Yejin Wang, Xufei Tang et al. — [Spectral Dynamics of DeepWalk Embeddings for Dynamic Network Change-Point Detection](http://arxiv.org/abs/2609.17893v1)
  <details><summary>📄 Abstract</summary>
  Dynamic networks describe evolving relational systems in which abrupt structural changes may signal anomalous events or important transitions. Detecting such changes requires distinguishing genuine structural signals from fluctuations in network observations and learned representations. We propose a DeepWalk-based framework for detecting and localizing structural changes in dynamic networks. For each snapshot, we learn low-dimensional node embeddings, align them to a fixed reference using orthog...
  </details>

- **2026-09-15** — Andrew P. Berg, Qian Zhang, Mia Y. Wang — [The Unbearable Weight: Scaling Models and Methods for UAV Audio Classification](http://arxiv.org/abs/2609.17884v1)
  <details><summary>📄 Abstract</summary>
  As unmanned aerial vehicles (UAVs) become increasingly prevalent in consumer and defense settings, classifying them reliably from limited, modality-specific data is an urgent challenge. The dominant approach, large pretrained networks fully fine-tuned on task data, carries a substantial computational and memory weight that is hard to bear in resource-constrained UAV deployments, where edge inference and rapid retraining for emerging platforms are both required. This paper systematically scales a...
  </details>

- **2026-09-15** — Kiarash Tajbakhsh, Abdelrahman Faqieh, Michael Jopiti et al. — [Lumen: Parameter-Efficient Alignment of Pretrained Vision and Language Encoders for Zero-Shot Computational Pathology](http://arxiv.org/abs/2609.17868v1)
  <details><summary>📄 Abstract</summary>
  Pathology vision-language models are commonly built by pretraining or fine-tuning large encoders on paired image-caption data. We asked whether a pathology vision-language model can instead be assembled by parameter-efficient alignment of frozen unimodal foundation models, leaving their pretrained representations untouched. Here we present Lumen, which aligns frozen Virchow2 and BioMedBERT backbones using rank-4 adapters and projection heads, training only 0.40% of the total parameters on the pu...
  </details>

- **2026-09-15** — Mohammadreza Sediqin, Shivali Dalmia, Sumukha Thoppanahalli et al. — [GVD: Governed Versioning and Deduplication for Document Repositories](http://arxiv.org/abs/2609.17696v1)
  <details><summary>📄 Abstract</summary>
  Document repositories evolve continuously. Guidelines and policies are revised, superseded, and re-uploaded, so the same content recurs in different wording and newer versions refine or contradict earlier ones. These inconsistencies belong to the growing collection rather than to any single document, yet existing work treats versioning, duplicate detection, and contradiction detection as isolated pairwise tasks and stops once a pair is labeled. We present GVD (Governed Versioning and Deduplicati...
  </details>

- **2026-09-15** — Bofan Chen, Boxuan Zhang, Fei Tang et al. — [Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents](http://arxiv.org/abs/2609.17653v1)
  <details><summary>📄 Abstract</summary>
  GUI agents execute long-horizon tasks on dynamic graphical user interfaces, where pop-ups, delayed loads, and relocated widgets routinely invalidate plans fixed before execution. Recent agent-skill frameworks encapsulate reusable procedural knowledge to mitigate this, yet existing skill designs are largely developed without targeting GUI execution dynamics and treat skills as static artifacts produced before deployment rather than living procedural knowledge that improves through it. We argue th...
  </details>

- **2026-09-15** — Jesús M. Fraile-Hernández, Anselmo Peñas, Patrick Giedemann — [Zero-shot narrative detection in social messaging](http://arxiv.org/abs/2609.17310v2)
  <details><summary>📄 Abstract</summary>
  This study investigates the zero-shot ability of large language models (LLMs) to identify and classify hidden narratives in social messages. Our research hypothesis is that LLMs' extensive contextual knowledge allows them to interpret messages on a deeper, pragmatic level, going beyond basic sentiment or topic analysis. Experiments on the Dipromats and SemEval datasets show that providing models with human-written narrative descriptions significantly improves performance, without the need of tra...
  </details>

- **2026-09-15** — Vsevolod Hulchuk, Jan Bayer, Jan Faigl — [LiLi: Lie Theory Based 3D LiDAR Scan Alignment Degeneracy Detection](http://arxiv.org/abs/2609.17145v2)
  <details><summary>📄 Abstract</summary>
  In this paper, we study 3D LiDAR scan alignment in challenging scenarios with degeneracies, such as straight corridors or flat fields, where the alignment solution is not unique and compromises localization and mapping accuracy. Existing degeneracy detection methods that neglect the potential for reassociating data points are prone to being sensitive to noise and complex degeneracies. Therefore, we propose LiLi - a novel method that leverages Lie theory to identify the full set of degenerate tra...
  </details>

- **2026-09-15** — Kisu Yang, Yoonna Jang, Heuiseok Lim — [Nameless Tokenization: A Lossless Tokenizer-Level Defense Against Control-Token Forgery in Open-Weight LLMs](http://arxiv.org/abs/2609.16984v1)
  <details><summary>📄 Abstract</summary>
  Open-weight language models publish the strings their chat templates use to mark turns, roles and tool results, which the tokenizer maps back to the reserved identifiers the model obeys. Anyone who controls text in a prompt can therefore write a turn boundary indistinguishable from one the serving stack wrote. We audit 256 deployed chat tokenizers. All are forgeable, and the flag usually recommended as a fix leaves 56.6% forgeable because it misses the tool and reasoning markers agent systems re...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 45 papers

- **2026-09-18** — Qian Zhang, Shiyue Chen, Juergen W Czarske — [Optical Mode Sorting with a Programmable Diffractive Neural Network](http://arxiv.org/abs/2609.22015v1)
  <details><summary>📄 Abstract</summary>
  Programmable diffractive optical processors are particularly attractive for spatial light manipulation because their optical transformations can be dynamically reconfigured and adapted without modifying the physical hardware. However, their practical performance is often limited by the gap between simulation and experiment caused by optical aberrations, alignment errors, and nonideal phase responses. In this paper, we introduce a hybrid optimization framework that combines high-dimensional numer...
  </details>

- **2026-09-18** — Sunghyun Baek, Hanna Bae, Minchan Kwon et al. — [Info3R: Information-Adaptive Test-Time Training for 3D Reconstruction](http://arxiv.org/abs/2609.21938v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based models have recently achieved strong performance on 3D reconstruction from images, and recent works extend them to process video streams in an online manner for real-world deployment. However, existing methods overlook two key signals when handling long image streams: the importance of each incoming frame and the information saturation of the model's internal state. In this paper, we propose Info3R, a novel information-adaptive test-time training method for the online 3D recons...
  </details>

- **2026-09-18** — Yanxiao Liu, Sicheng Wan, Deniz Gündüz — [ExpBoN: Exponential-Noise Best-of-$n$ for Efficient Test-Time LLM Alignment](http://arxiv.org/abs/2609.21899v1)
  <details><summary>📄 Abstract</summary>
  Best-of-$n$ (BoN) sampling is a simple yet effective inference-time alignment method, but hard maximization provides only coarse control over the trade-off between reward and distribution shift. Soft Best-of-$n$ (Verdun et al. 2025) provides smoother control and converges to the optimal distribution associated with KL-regularized reward maximization. In this paper, we introduce ExpBoN, an alternative soft BoN method based on the exponential-noise report-noisy-max mechanism. It admits an exact fi...
  </details>

- **2026-09-18** — Laurent Colbois, Sébastien Marcel — [Benchmarking the Explanatory Quality of Open-Weight Vision-Language Models in Face Recognition](http://arxiv.org/abs/2609.21879v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have recently been proposed as promising tools for face recognition, as they can produce natural language explanations alongside similarity scores. This capability is considered appealing for face comparisons in forensic contexts, which require decisions to be transparent and auditable. However, existing evaluations of VLMs for that use case focus mostly on recognition accuracy, while the validity of generated explanations remains unquantified. In this work, we intr...
  </details>

- **2026-09-18** — Tim Krabbe, Xiaodan Shi — [Do Personality-Tuned LLMs Make Better Social Agents?](http://arxiv.org/abs/2609.21857v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used in social simulations for socially interactive agents and robots, offering more flexibility than rule-based systems. However, even though they mimic human behaviour very well, there is a persistent alienness to them. This work investigates whether personality-aware fine-tuning can reduce this gap by improving the consistency and controllability of personality-conditioned dialogue generation compared with instruction prompting alone. We fine-tune two small open-weight L...
  </details>

- **2026-09-18** — Muhammet Sami Yavuz, Sabri Mustafa Kahya, Richard R. Chen et al. — [MIST: Multimodal Survival Prediction with Genomic-Guided Histology Attention](http://arxiv.org/abs/2609.21811v1)
  <details><summary>📄 Abstract</summary>
  Multimodal survival models can combine complementary prognostic information from whole-slide images and genomic profiles, but effective fusion remains challenging amid external cohort shift and computational complexity. To address these challenges, we propose MIST, multimodal survival prediction with genomic-guided histology attention. MIST represents genomic features as tokens and allows them to query compact foundation-model-derived histology context tokens before survival prediction. This des...
  </details>

- **2026-09-18** — Amartya Bhattacharya, Nikhil Singh, Neeti Pokhriyal et al. — [PRISM-BN: A Controlled Corpus and Benchmark for Text-to-Parameterized Bayesian Network Extraction](http://arxiv.org/abs/2609.21673v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic Graphical Models (PGMs), especially Bayesian Networks (BNs), expose directed structure and probabilistic parameters, making them natural symbolic targets for neurosymbolic AI. Yet training text-to-parameterized-BN systems requires paired text-to-BN resources unavailable at scale. We introduce PRISM-BN, a controlled corpus of 5054 BN-grounded descriptions paired with discrete reference BNs containing variables, states, directed edges, root priors, and full multi-parent CPDs across f...
  </details>

- **2026-09-18** — Léo Nicollier, Enric Meinhardt-Llopis, Marc Pic et al. — [Beyond Gaussian Worlds: Latent Geometry Matters for JEPAs](http://arxiv.org/abs/2609.21656v1)
  <details><summary>📄 Abstract</summary>
  Recent Joint-Embedding Predictive Architectures (JEPAs) prevent representation collapse by constraining learned representations to follow a prescribed target distribution, such as an isotropic Gaussian or the uniform distribution on a hypersphere. Klindt et al. (2026) showed that, under their Euclidean assumptions, matching a Gaussian target can recover Gaussian latent variables up to a linear transformation, and that the Gaussian is the unique distribution with this guarantee. We extend their a...
  </details>

- **2026-09-18** — Shuiying Liao, P. Y. Mok — [Dual-Interest Sequential Product Recommendation With Multi-Granular SSM](http://arxiv.org/abs/2609.21548v1)
  <details><summary>📄 Abstract</summary>
  Sequential recommendation aims to predict the next item a user will interact with based on their historical behavior. Advances in Transformers have significantly improved sequential recommendation but are still limited by cost efficiency. Although State Space Models (SSMs) have recently enabled efficient long-range modeling, most existing methods encode each item with a single static contextual role, overlooking the phenomenon of item polysemy. In fact, the same item often plays different semant...
  </details>

- **2026-09-18** — Haojie Dai, Xiangyi Wang, Liuyi Wang et al. — [DPed-VLN: A Benchmark for Socially Compliant Vision-and-Language Navigation in Dynamic Pedestrian Environments](http://arxiv.org/abs/2609.21504v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-language navigation (VLN) has advanced rapidly in static indoor environments, but robots operating in human-populated spaces must ground language while responding to moving pedestrians and social-safety constraints. We present DPed-VLN, a Habitat 3.0 benchmark for dynamic-pedestrian VLN that couples 33,093 navigation episodes with paired global and prior-augmented instructions, ORCA-controlled humanoid pedestrians, socially constrained expert paths, and metrics that jointly assess nav...
  </details>

- **2026-09-18** — Di Wu, Dongchen Zheng, Junhe Sheng et al. — [AtomEgo: Exploring Ego-Robot Integration for Embodied Foundation Model Pretraining](http://arxiv.org/abs/2609.21461v1)
  <details><summary>📄 Abstract</summary>
  Embodied foundation models are constrained by the limited scale and diversity of robot demonstrations, motivating the use of large-scale egocentric human interaction data. However, how to effectively incorporate such data into embodied-model pre-training remains unclear because of substantial embodiment and action-space gaps between humans and robots. We present AtomEgo, a systematic study of ego--robot co-training supported by a curated corpus of approximately 2,659 hours and a scalable data pr...
  </details>

- **2026-09-18** — Marina Mitiaeva, Lu Xiao — [Talking Past the Machine: Morality, Politeness, and Alignment in Human-AI Dialogue](http://arxiv.org/abs/2609.21401v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI systems produce fluent, socially appropriate responses, yet whether they participate in cooperative communication or merely simulate its surface forms remains unclear - a question central to how these systems are evaluated, trusted, and designed. This study investigates how morality, politeness, and alignment - three dimensions central to cooperative dialogue - function in human-AI interaction compared to human-human conversation. We analyze 15,881 human-ChatGPT and 10,784 huma...
  </details>

- **2026-09-18** — Trinh Tra Giang Nguyen, Thanh Nguyen Vo, Nguyen Hoai Thuong Bui et al. — [JEPA Guided Diffusion: Predictive Vision-Language Conditioning for Generative Traffic Forecasting](http://arxiv.org/abs/2609.21379v1)
  <details><summary>📄 Abstract</summary>
  Accurate traffic forecasting requires both understanding scene dynamics and synthesizing realistic future observations. Recent diffusion-based video generation models produce visually plausible predictions but require expensive end-to-end training and often entangle scene understanding with image synthesis. In this work, we propose a decoupled forecasting framework that separates future representation learning from video generation. A frozen V-JEPA encoder first extracts predictive latent repres...
  </details>

- **2026-09-17** — Bingxin Xu, Yuzhang Shang, Zhen Dong et al. — [Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation](http://arxiv.org/abs/2609.20822v1)
  <details><summary>📄 Abstract</summary>
  Coding agents have emerged as a promising paradigm for robot manipulation: a language model writes the robot controller as a program, and agents built in this way now operate robots without robot-specific training.Whether this paradigm is also safe, however, has not been asked. We evaluate coding agent under a safety constraint, where each task pairs a manipulation goal with an obstacle the robot must not touch. The agent pursues the goal but collides with the obstacle in most cases, treating ta...
  </details>

- **2026-09-17** — Haocheng Xi, Yiming Xie, Hexu Zhao et al. — [Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation](http://arxiv.org/abs/2609.20744v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion models repeatedly process long spatiotemporal token sequences during denoising, making attention a major computational bottleneck. Linear attention offers an appealing alternative and has been widely adopted in recent large language models, but directly applying it to video models often fails to preserve the fine-grained interactions required for high-quality generation. We present Video DeltaNet (VDN), which combines local Softmax attention with bidirectional linear memory for l...
  </details>

- **2026-09-17** — Zhikun Zhou, Kunyu Peng, Runyi Yang et al. — [CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding](http://arxiv.org/abs/2609.20586v1)
  <details><summary>📄 Abstract</summary>
  Referring scene understanding for embodied robots requires grounding object- and relation-centric language queries from a designated viewpoint. While a local semantic Gaussian map can support such grounding within one agent's observations, cooperative settings require this ability to remain effective after independently reconstructed maps are aligned and fused. In this setting, the referred target or its contextual landmark may come from another agent's observations, while spatial relations must...
  </details>

- **2026-09-17** — Haiqiang Chen, Li Chen, Yunlong Chen et al. — [Does Training on Future Data Pay? Look-Ahead Bias in Forecasting with Pretrained Models](http://arxiv.org/abs/2609.20554v1)
  <details><summary>📄 Abstract</summary>
  We examine whether post-origin training information inflates the measured accuracy and economic value of financial forecasts. We evaluate five sets of financial time-series foundation models, each comprising independently trained annual vintages under U.S., global, and factor-augmented training environments, across 14 equity markets and four forecast horizons. Rolling comparisons vary the annual vintage for a fixed forecast; fixed-vintage comparisons hold the vintage fixed as target windows move...
  </details>

- **2026-09-17** — Xiaodong He, Xincheng Wang, Zhao Kang — [SCGFM-ART: Amortized Relational Transport for Structure-Centric Graph Foundation Models](http://arxiv.org/abs/2609.20419v1)
  <details><summary>📄 Abstract</summary>
  Graph foundation models (GFMs) aim to learn transferable representations across severely heterogeneous graph domains. However, severe domain shifts in topology, graph scale, and feature semantics impede the construction of a unified, domain-agnostic representation space. To address this, we propose SCGFM-ART, a structure-centric GFM framework that aligns arbitrary graphs onto a shared relational atlas via Amortized Relational Transport (ART). The relational atlas serves as a universal coordinate...
  </details>

- **2026-09-17** — Guangze Gao, Zixuan Li, Sikui Zhang et al. — [Schema-Anchored Latent Reasoning for Semantic Parsing-Based Knowledge Base Question Answering](http://arxiv.org/abs/2609.20398v1)
  <details><summary>📄 Abstract</summary>
  Semantic parsing (SP)-based knowledge base question answering aims to answer natural language questions by generating executable logical forms (LFs) over knowledge bases (KBs). When applying Large Language Models (LLMs) to this task, a key challenge over large, heterogeneous KBs is selecting question-related schema elements (i.e., relations and classes) and composing them into complex LFs. Recent LLM-based methods often make early discrete commitments to schema elements during intermediate reaso...
  </details>

- **2026-09-17** — Yan Jia, Kai Huang, Junjie Chen et al. — [Alignment-Path Distillation from Non-streaming ASR-LLMs for Streaming Speech Recognition](http://arxiv.org/abs/2609.20121v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose an alignment-path distillation framework for streaming automatic speech recognition (ASR) with large language models (LLMs). Interleaved streaming ASR-LLMs use forced alignments (FA) from alignment models, such as those trained with connectionist temporal classification (CTC), to construct speech-text training sequences. However, alignments obtained from a separate acoustic model may be inconsistent with those learned by LLM-based ASR. This motivates us to transfer alig...
  </details>

- **2026-09-17** — JaeWon Kim, Angie Boggust — [What People Almost Did: Evaluating LLM Social Simulations Beyond Behavioral Fit](http://arxiv.org/abs/2609.20055v1)
  <details><summary>📄 Abstract</summary>
  LLM-based social simulations are primarily evaluated for behavioral fit, testing whether agents reproduce the actions or response distributions of the people they are simulating. However, the promise of simulation extends beyond behavioral fit. Simulations can explain human behavior, diagnose barriers, and compare large-scale interventions. These use cases depend on understanding \textit{why} people acted a certain way, not just \textit{what} they did. As a result, behavioral fit is insufficient...
  </details>

- **2026-09-17** — Chenrui Cui, Hongye Fang, Lisha Song et al. — [Benchmarking LLM Compliance with China AI Generated Content Regulations](http://arxiv.org/abs/2609.19989v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of LLMs has led to escalating content compliance risks. Prior works have contributed to addressing these risks in the English context, downplaying the complexity of Chinese language content. This paper follows China's current AI-Generated content compliance requirements and provides evaluation results on 20 notable LLMs, offering insight into China's regulatory landscape. We design a novel framework to assess the compliance and refusal rates with 2303 questions spanning s...
  </details>

- **2026-09-17** — Omran Berjawi, Giuseppe Fenza, Rida Khatoun et al. — [Digital Twins for Opinion Dynamics: A Generative LLM Framework for Social Networks](http://arxiv.org/abs/2609.19913v1)
  <details><summary>📄 Abstract</summary>
  The study of opinion dynamics in social networks is one of the key challenges in computational social science with direct relevance to understanding political polarization, misinformation, and health responses. Current approaches focus on simplified mathematical models that ignore linguistic and contextual factors related to belief updates or use Large Language Model (LLM)-based simulations that have not been validated against real data. We present a framework based on the concept of a digital t...
  </details>

- **2026-09-17** — Suji Kang, Seok-Young Kim, Young Bin Kim et al. — [SnapPhysics: A Physics-Aware Scene Graph from a Single View for Interactive Mixed Reality Scenes](http://arxiv.org/abs/2609.19815v1)
  <details><summary>📄 Abstract</summary>
  We propose SnapPhysics, a training-free framework that reconstructs 3D objects and estimates their physical properties such as mass, friction, and center of gravity from a single image. For physically coherent interactions in mixed reality (MR), such properties are as important as geometry. Prior approaches infer them by analyzing object dynamics in video, which is computationally costly, or by querying vision-language models (VLMs) on single images, which lacks geometric grounding and inter-obj...
  </details>

- **2026-09-17** — Junlei Zhu, Shenzhe Yao, Chaogui Huang et al. — [Towards High-DoF Dexterous Manipulation through VLA Post-Training](http://arxiv.org/abs/2609.19666v1)
  <details><summary>📄 Abstract</summary>
  Imitation-learned vision--language--action (VLA) foundation models acquire broad manipulation capabilities by scaling robot data across tasks and embodiments, but reliable deployment on a specific downstream task and hardware platform still requires post-training. Dexterous hands make this adaptation particularly difficult: their broad behavioural repertoire and high degree of freedom create a large and structured action space. Three obstacles are central: open-source VLAs do not natively provid...
  </details>

- **2026-09-17** — Diba Afroze, Xingli Zhang, Yazhou Tu et al. — [From Intent to Action: Benchmarking LLM Safety in Vehicle Voice Command Authorization](http://arxiv.org/abs/2609.19630v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly integrated into vehicle voice assistants. But linking natural-language requests to vehicle functions creates a safety-critical authorization problem. Before executing a command, the system must choose whether to execute, refuse, clarify, require confirmation, defer to manual control, trigger an emergency response, or make no tool call. To our knowledge, prior evaluations do not isolate this pre-action decision across speaker role, authentication stat...
  </details>

- **2026-09-17** — Sunwoo Kim, Seokwon Jung, Sohyung Kim et al. — [Form Over Content In Gradient-Based Data Attribution Methods](http://arxiv.org/abs/2609.19589v1)
  <details><summary>📄 Abstract</summary>
  Data attribution methods using gradient similarity are widely used to analyze and select training data for large language models, but what gradient similarity actually measures is debated. Some interpret it as identifying task-relevant skills, while other work reports that surface form is the main factor. We resolve this debate for supervised fine-tuning examples by varying task and answer format independently. Specifically, we render benchmarks in different answer formats, such that datasets ca...
  </details>

- **2026-09-17** — Bowen Li, Lukas Palm, Xin Wei et al. — [Automatic Optical Alignment Using Projective Geometry](http://arxiv.org/abs/2609.19565v1)
  <details><summary>📄 Abstract</summary>
  Aligning and maintaining complex optical beam paths is a central challenge across experimental science, because it is a high-dimensional task with strong cross-coupling between controls, often in systems with limited physical access. We present an automated hardware-software framework that resolves this alignment challenge using low-cost, retro-fittable motorized mounts driven by projective-geometry models and a photodiode-fed optimizer. A compact forward model describes the beam path to paraxia...
  </details>

- **2026-09-16** — Abdarahmane Traoré, Andy Couturier, Éric Hervet — [SCOUT: Sim-to-Real Text-Based Person Retrieval by Embedding-Space Prediction over Frozen Video Features](http://arxiv.org/abs/2609.19483v1)
  <details><summary>📄 Abstract</summary>
  Text-based person retrieval under a sim-to-real gap (synthetic training data, a real-image gallery) is usually tackled with costly fine-tuned cross-encoders. We ask whether a frozen-encoder system can compete. We present SCOUT, which casts cross-modal retrieval as prediction in embedding space. A trainable predictor maps the patch tokens of a frozen video encoder into the embedding space of a frozen text encoder under a bidirectional InfoNCE objective, and no encoder is fine-tuned in the base mo...
  </details>

- **2026-09-16** — Sai Sri Pushpa Jampani, Kshitij Mishra, Asif Ekbal — [AUDITPLAN: Commit, Then Answer for Auditable Safety Alignment](http://arxiv.org/abs/2609.19325v1)
  <details><summary>📄 Abstract</summary>
  Safety tuning pipelines judge only the final answer, which makes it difficult to distinguish robust refusal from two undesirable shortcuts: blanket refusal on benign requests and polished but unfaithful safety rationales that do not actually constrain the answer. We propose AUDITPLAN, a single-model plan-then-answer approach where the model first emits a compact structured safety plan and then answers conditioned on it. The plan records a threat label, intended action, and explicit constraints, ...
  </details>

- **2026-09-16** — Peter Chen, Xi Chen, Wotao Yin et al. — [A Zeroth-Order Paradigm for LLM Preference Alignment](http://arxiv.org/abs/2609.19144v1)
  <details><summary>📄 Abstract</summary>
  Direct preference alignment methods are widely used to align large language models (LLMs) with human preferences because of their computational and memory efficiency. However, likelihood displacement motivates alternative ways to extract information from preference pairs with small likelihood margins. In this paper, we propose and analyze Comparison-based Preference Optimization (ComPO), a zeroth-order alignment method based on comparison oracles. ComPO extracts directional information from thes...
  </details>

- **2026-09-16** — Sara Pieri, Evangelos Kazakos, Shizhe Chen et al. — [PANORAMA: Panoptic Grounded Captioning via Mask Proposal Selection](http://arxiv.org/abs/2609.19143v1)
  <details><summary>📄 Abstract</summary>
  Intelligent systems that act in the world require image understanding that is both comprehensive and spatially grounded. Current vision-language models (VLMs) can generate fluent and detailed image captions, but reliably associating them with image pixels remains challenging. Existing methods that combine dense captioning with pixel-level grounding often produce either incomplete descriptions or inaccurate segmentation masks. We study this problem through panoptic grounded captioning, a task tha...
  </details>

- **2026-09-16** — Tabia Tanzin Prama, Christopher M. Danforth, Peter Sheridan Dodds — [BanglaShop-CRS: A User-Centric Bangla Dataset for Conversational Recommendation](http://arxiv.org/abs/2609.18715v1)
  <details><summary>📄 Abstract</summary>
  Conversational recommender systems~(CRS) enable users to express preferences, constraints, and feedback through natural language interaction. However, existing CRS resources are concentrated in English and other high-resource languages, leaving Bangla and code-mixed Bangla--English settings underrepresented. To address this gap, we introduce BanglaShop-CRS, a large-scale user-centric synthetic Bangla conversational recommendation dataset grounded in real e-commerce behavior. It contains 27,178 m...
  </details>

- **2026-09-16** — Raphael Schlattmann, Malte Vogl — [Tracing individual knowledge trajectories in a changing field: the case of general relativity and gravitation](http://arxiv.org/abs/2609.18697v1)
  <details><summary>📄 Abstract</summary>
  Historians have reconstructed the twentieth-century transformation of general relativity and gravitation (GRG) at the field level and through individual careers, but connecting these scales requires a way to compare researchers with the changing field over time. We develop such a comparison, setting a researcher's publications and references against GRG field literature from the same, earlier, and later two-year periods. Building on Own Vocabulary and Embedding Density Estimation from our earlie...
  </details>

- **2026-09-16** — Hadiana Sliwa, Hossein Hassani — [Machine Translation between English and Syriac (East Syriac Dialect) using Statistical Machine Learning](http://arxiv.org/abs/2609.18529v1)
  <details><summary>📄 Abstract</summary>
  UNESCO considers the Assyrian (Syriac) language an endangered language. Although Assyrians speak the language worldwide, the speaking population is uncertain (ranging from 500,000 to 1,500,000). Syriac is also one of the least studied languages in Natural Language Processing (NLP). Despite advances in Machine Translation (MT) over the past decade, the lack of publicly available corpora and the orthographic complexity of the Syriac script, specifically the Madnkhaya script, have left this languag...
  </details>

- **2026-09-16** — Xiuwen Zheng — [Look Less, Hear Better: Jointly Rewarded GRPO for Streaming ASR](http://arxiv.org/abs/2609.18333v1)
  <details><summary>📄 Abstract</summary>
  Streaming automatic speech recognition (ASR) must be judged jointly on what it transcribes and on how quickly it commits each word. Delayed streams modeling (DSM) has become the dominant paradigm for streaming large audio-language models, exposing a structural delay $τ$ that bounds the decoder's lookahead. We show that $τ$ is a poor proxy for user-perceived latency, and that the alignment-based supervision of DSM leaves latency on the table: the same forced-aligned transcript is used at every $τ...
  </details>

- **2026-09-16** — Y. Fong, J. Xiang, T. Y. D. Chan et al. — [I code or AI code: A comparative evaluation of AI-rated scores in classroom observations](http://arxiv.org/abs/2609.18274v1)
  <details><summary>📄 Abstract</summary>
  Classroom observations are widely recognized as a key tool for establishing benchmarks of education quality and guiding pedagogical improvement, yet they remain resource-intensive and dependent on trained observers. This study evaluated the feasibility of using a LLM (GPT-5 model) to score teacher-child interactions in early childhood classrooms, benchmarked against human raters. The study analyzed 87 video-recorded observations from 38 classrooms across 30 kindergartens in Hong Kong. Using obse...
  </details>

- **2026-09-16** — Yajie Yu, Mark Lee, Yue Feng — [STRETCH the Boundaries: A Unified Self-Taught Framework for Progressive LLM Evolution](http://arxiv.org/abs/2609.18642v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often suffer from capability stagnation in self-improvement training because fixed difficulty levels fail to adapt to their evolving proficiency. To address this issue, we propose STRETCH (Self-Taught Reasoning Evolution via Targeted CHallenge), a unified framework inspired by cognitive scaffolding theory. STRETCH introduces a dynamic Stretch Zone mechanism that continuously aligns question difficulty with the model's solving capability. Within a single parameter spa...
  </details>

- **2026-09-16** — Devesh Tiwari, Camille Davis, Shivank Sinha et al. — [Decodability is Not Causality: Dissociating Probe Readouts from Behavioral Drivers via SAE Decomposition](http://arxiv.org/abs/2609.18080v1)
  <details><summary>📄 Abstract</summary>
  Linear probes can decode safety-relevant concepts such as truthfulness from language-model activations, but probe accuracy may show only decodability, not that the features the probe weights causally drive model behavior. We demonstrate that this gap cannot be closed from the geometry of probe weights alone: the features geometrically aligned with probe direction need not be the ones the model uses, so causal relevance requires intervention. We introduce a feature-level diagnostic that decompose...
  </details>

- **2026-09-16** — Elizabeth Pavlova, Hidenori Tanaka — [Flag Game: A Toy Model for Mechanistic Swarm Interpretability](http://arxiv.org/abs/2609.19124v1)
  <details><summary>📄 Abstract</summary>
  Emergent coordinated behaviors of AI agents are starting to present critical safety risks. A key phenomenon driving these behaviors is the rapid formation and spread of beliefs about the world, and mechanistic understanding is crucial for collective alignment. To this end, we introduce the Flag Game, a toy model for studying the mechanisms of collective belief formation. Concretely, a hidden country flag defines the ground truth, and each bounded agent directly observes only a private crop but c...
  </details>

- **2026-09-16** — Abderrahmane Issam, Yusuf Can Semerci, Jan Scholtes et al. — [Align, Integrate, and Fire: Efficient Token-Level Alignment for Zero-Shot SpeechLLMs](http://arxiv.org/abs/2609.18516v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models excel in natural language processing, efficiently extending their capabilities to spoken input remains a significant challenge. Existing methods for building SpeechLLMs often rely on computationally expensive full-model fine-tuning, or employ parameter-efficient projectors that suffer from inefficient token sequence lengths and costly full-model supervision. In this paper, we introduce Aligned Continuous Integrate-and-Fire, a highly efficient framework for zero-shot s...
  </details>

- **2026-09-16** — Hanbing Zhang, Fangguo Zhao, Zerui Li et al. — [VLM-MPPI: Grounding Natural Language in Behaviorally Diverse Trajectories for Aerial Navigation](http://arxiv.org/abs/2609.18451v1)
  <details><summary>📄 Abstract</summary>
  We present a hierarchical UAV navigation framework that aligns natural-language intent with dynamically feasible flight behaviors in cluttered indoor environments. To bridge the gap between abstract semantics and low-level control, we employ a parallelized ensemble of six behavior-conditioned Model Predictive Path Integral (MPPI) planners. Crucially, by designing mode-specific guiding costs and sampling biases, we induce distinct trajectory modes that converge to unique behavioral means, yieldin...
  </details>

- **2026-09-16** — Chowdhury Mohammad Abdullah, Rita Orji — [From a River in Gilead to the Inference Distributions of Large Language Models: Covert Dialect Bias and Linguistic Profiling at Scale](http://arxiv.org/abs/2609.18068v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in high-stakes domains such as housing screening. While alignment techniques mitigate explicit racial bias in generated text, they often leave covert attitudinal associations in internal probability distributions untouched. Adapting the matched-guise sociolinguistic paradigm, we examine covert dialect bias in housing-related social judgments across four varieties: Standard American English (SAE), African American Vernacular English (AAVE), N...
  </details>

- **2026-09-15** — Srishti Palani, Vidya Setlur — [Lexara-RF: Reference-Free Metrics for Evaluating Conversational Visual Analytics Agents](http://arxiv.org/abs/2609.17842v1)
  <details><summary>📄 Abstract</summary>
  Conversational visual analytics (CVA) agents powered by large language models generate visualizations and natural-language explanations from open-ended queries. Evaluating these multimodal outputs is challenging: curated reference benchmarks are costly to author, cannot comprehensively capture the space of valid responses, and are unavailable in production. Building on the Lexara evaluation framework, we introduce Lexara-RF, a reference-free set of metrics that scores CVA outputs using only the ...
  </details>

- **2026-09-15** — Dogun Kim, Yongjae Lee, Joonhee Lim et al. — [RAF-VLA: Representation Alignment with the Future for End-to-End Autonomous Driving](http://arxiv.org/abs/2609.17728v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language-Action (VLA) models for autonomous driving have incorporated world modeling by predicting future driving scenes alongside driving actions, demonstrating strong planning performance. Future driving scenes are utilized as dense supervision, encouraging the policy to learn rich internal representations useful for planning. However, these World-Modeling VLAs rely on explicit future generation to learn such representations, thereby introducing two key limitations: additional tr...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 66 papers

- **2026-09-18** — Steve Drew, Jiayu Zhou — [LEGIT: Credentialing Protocol for Trustworthy AI Agent Marketplaces](http://arxiv.org/abs/2609.21325v1)
  <details><summary>📄 Abstract</summary>
  Agentic marketplaces are emerging where AI agents with varying capabilities autonomously complete specialized tasks for buyers. A major challenge of such marketplaces is that buyers cannot easily determine which agent will perform best on their tasks. Reported benchmark scores may be difficult to verify or compare across tasks, software, and budgets. We introduce LEGIT, a credentialing protocol connecting certification, reputation, and proposed marketplace allocation. Certification binds measure...
  </details>

- **2026-09-18** — Yiming Zhang, Jinghong Zhang, Haoran Zhao et al. — [An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency](http://arxiv.org/abs/2609.22043v1)
  <details><summary>📄 Abstract</summary>
  Memory systems for large language models have focused predominantly on efficient retrieval, whereas the decision of whether retrieved memories should be trusted has received comparatively little attention. When the memory store contains conflicting positions, standard retrieval-augmented generation (RAG) blindly injects memories and amplifies hallucinations: in models susceptible to memory injection, the RAG hallucination rate under conflicting memories is markedly higher than that of a memory-f...
  </details>

- **2026-09-18** — Jia Li, Li Dai, Peng Jia et al. — [Beyond Exact Match: Task-Aware GRPO for Cross-Domain PCBA Visual Question Answering](http://arxiv.org/abs/2609.21276v1)
  <details><summary>📄 Abstract</summary>
  In automated Printed Circuit Board Assembly (PCBA) inspection, standards-guided decisions require systems to jointly reason over fine-grained visual cues, component semantics, and manufacturing knowledge. Although large vision-language models (VLMs) provide a promising foundation, their deployment is hindered by the domain shift between standards-derived samples and real-world production-line imagery, together with heterogeneous output spaces spanning choice-based and numerical counting tasks. T...
  </details>

- **2026-09-18** — Haolong Meng, Fangbo Qin, Mengchen Bai et al. — [Towards Fine-Grained Object Manipulation: SAM3-Guided Visuomotor Policy with Persistent Memory Learning and Focused Visual Conditioning](http://arxiv.org/abs/2609.21621v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained object (FO) manipulation requires robots to distinguish a specified FO from visually similar objects and execute actions reliably despite scene distractors. However, scene-level visual conditioning lacks explicit object selection, while category-level guidance cannot reliably distinguish FOs within the same category. We present a SAM3-guided visuomotor framework that addresses these challenges through persistent object memory and focused visual conditioning. First, we introduce FO M...
  </details>

- **2026-09-18** — Yuhyeon Hwang, Daniel Sungho Jung, YongHyeok Seo et al. — [Learning Distance-Conditioned Object Transport for Humanoid Loco-Manipulation from a Single Motion Clip](http://arxiv.org/abs/2609.21467v1)
  <details><summary>📄 Abstract</summary>
  Motion tracking can reproduce humanoid loco-manipulation from a single retargeted motion clip, but a policy trained on a fixed reference primarily reproduces its demonstrated transport outcome. Although the source trajectory visits intermediate object displacements, transport termination is demonstrated only at its endpoint. We identify this mismatch as the termination-versus-passage gap: intermediate displacements are observed as passage states rather than termination-complete outcomes. We intr...
  </details>

- **2026-09-18** — Yijun Hong, Jiarun Zhu, Xiaoquan Sun et al. — [FAN: Foresight Action Normalization for Continual Adaptation of Vision-Language-Action Models](http://arxiv.org/abs/2609.21358v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models pre-trained on large-scale, closed datasets have demonstrated remarkable success across diverse robotic manipulation tasks. However, their long-term real-world deployment necessitates continuously acquiring new skills while retaining previously learned capabilities. While pioneering works have explored continual VLA adaptation using techniques such as experience replay and reinforcement fine-tuning, they overlook a foundational mechanism: action normalization,...
  </details>

- **2026-09-18** — Sheng-An Xu, Hanyang Li, Jianhao Ma et al. — [Beyond Shadow Weights: Quantization-Aware Training as Quantized-Endpoint Descent](http://arxiv.org/abs/2609.21834v1)
  <details><summary>📄 Abstract</summary>
  Quantization-aware training (QAT) updates a full-precision shadow weight $\mathbf{x}$ but deploys the quantized endpoint $Q(\mathbf{x})$. Existing explanations for QAT largely view its success through the lens of shadow weights: QAT can move $\mathbf{x}$ toward flatter basins, gain robustness from quantization-induced oscillations, or balance the shadow loss $f(\mathbf{x})$ against the quantization error $\|\mathbf{x}-Q(\mathbf{x})\|_2$. These perspectives do not directly explain the empirical o...
  </details>

- **2026-09-18** — Mushir Akhtar, M. Tanveer, Mohd. Arshad — [Beyond Benchmark Scores: Auditing Medical Vision-Language Models for Chest X-Ray Tuberculosis Screening](http://arxiv.org/abs/2609.21763v1)
  <details><summary>📄 Abstract</summary>
  A medical model's benchmark score does not establish that the same conclusion holds under a different evaluation. This study tests whether claims about model ranking, score reliability and screening performance survive changes in cohort, prompt, negative spectrum, specified prevalence and operating threshold. We audit three medical vision-language models (BioMedCLIP, CheXficient, and MedSigLIP) and a general-domain OpenCLIP comparator on 12,200 chest radiograph records from four datasets (Montgo...
  </details>

- **2026-09-18** — Jingke Zhou, Chenhang Ma, Zhizhou Zhong et al. — [Think Locally, Refine Globally for Memory-Efficient 3D Reconstruction](http://arxiv.org/abs/2609.21437v1)
  <details><summary>📄 Abstract</summary>
  We propose LoG-VGGT, a memory-efficient framework for long-sequence 3D reconstruction that balances local temporal modeling with global camera consistency. Instead of relying on full global attention, our method introduces cross-window attention at a small subset of transformer blocks, enabling effective information propagation across adjacent temporal windows while keeping memory usage bounded. To mitigate long-term pose drift, we further design a global camera consistency refinement module, wh...
  </details>

- **2026-09-18** — Yilin Evan Li, Harikrishnan KP, Sankalpa Hazra et al. — [Strain-Induced Relaxor Multiferroicity at Room Temperature in Hexaferrite BaFe12O19 Thin Films](http://arxiv.org/abs/2609.21352v1)
  <details><summary>📄 Abstract</summary>
  Multiferroic materials that combine magnetic and electric order at room temperature are rare. Here, we demonstrate strain-induced room-temperature polar order in the ferrimagnetic hexaferrite BaFe12O19. First-principles calculations reveal a strain-tunable energy landscape with multiple competing dipolar configurations and predict that compressive strain favors polar distortions. Using an isostructural Sr1.03Ga10.81Mg0.58Zr0.58O19 substrate, we grow coherently strained BaFe12O19 films with 1.1% ...
  </details>

- **2026-09-17** — Hassan Saeed Hassan Albattra, Mazen Mohammed Bahgat, Rahatara Ferdousi et al. — [HerHealthEval: Evaluating Multilingual and Register-Sensitive Understanding of Women's Health Communication](http://arxiv.org/abs/2609.20684v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used in healthcare communication, yet most evaluations emphasize response quality while assuming that the user's concern has been interpreted correctly. We introduce HerHealthEval, a controlled evaluation framework for multilingual understanding of women's-health communication. For each clinical case, HerHealthEval provides matched versions in English, French, and Modern Standard Arabic using six communicative forms: canonical, clinical, layperson, indirect...
  </details>

- **2026-09-17** — Chenxi Wu, Zimu Wang, Haiyang Zhang et al. — [SAFARI: An Industrial Benchmark for LLM-Assisted Hazard Analysis and Risk Assessment](http://arxiv.org/abs/2609.20584v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly considered for safety-critical engineering, yet their reliability in regulated functional-safety workflows remains underexplored. We introduce SAFARI (Safety-Aware Functional Automotive Risk Inference), the first industrial benchmark for LLM-assisted automotive Hazard Analysis and Risk Assessment (HARA) under ISO 26262. It contains 3,000 de-identified industrial HARA cases and evaluates two coupled tasks: open-ended hazard analysis and standards-grou...
  </details>

- **2026-09-17** — Bo Tang, Zixuan Liao, Hao Li et al. — [Noise-Robust Quantum State Characterization for Remote State Preparation with Deep Learning](http://arxiv.org/abs/2609.20523v1)
  <details><summary>📄 Abstract</summary>
  Quantum communication underpins secure information processing and scalable quantum networks. In particular, remote state preparation (RSP) enables efficient quantum state transfer, but accurately estimating target states under complex noise remains challenging. Here, we propose a Transformer-based Quantum State Characterizer (TQSC) model for noisy RSP experiments. Our model reconstructs experimentally prepared pure and mixed photonic polarization states from noisy measurements in complex scatter...
  </details>

- **2026-09-17** — Małgorzata Nowak-Kępczyk — [Long-Lived Carpet-Like Transients in Time-Dependent Modular Discrete Laplacian Dynamics](http://arxiv.org/abs/2609.20416v1)
  <details><summary>📄 Abstract</summary>
  Binary modular Laplacian dynamics is organized by repeated replication, growth, and collapse on dyadic scales. We study how isolated and periodically repeated non-binary updates modify this organization and whether they can sustain densely occupied geometric structures.   Computational experiments across multiple finite seeds, neighborhood masks, inserted moduli, and periodic schedules show that constant prime moduli retain the expected \(p\)-adic replication hierarchy. A single non-binary inser...
  </details>

- **2026-09-17** — Ha Van Dau, Thanh Tung Khuat, Nguyen Thanh Dung — [Beyond Depth Truncation: Controlled Evaluation of Depth Utilization in Recursive Language Models](http://arxiv.org/abs/2609.19934v1)
  <details><summary>📄 Abstract</summary>
  Depth-recurrent language models iteratively apply a small layer stack, decoupling per-token compute from distinct parameter count. To determine whether such a model genuinely utilizes its depth, both recurrence and layer-pruning literatures rely on a shared evaluation: truncating depth at inference time, plotting quality against retained depth fraction, and reading off the slope. While cheap and training-free, this metric suffers from an unexamined flaw: it extracts a single scalar from an inter...
  </details>

- **2026-09-17** — Feifan Wang, Zongbing Zhang, Yu Zhang et al. — [EmbodiedMind: Adaptive Data Curation and Prefix-Tree Reinforcement Learning for Efficient Embodied Intelligence](http://arxiv.org/abs/2609.19659v1)
  <details><summary>📄 Abstract</summary>
  Training embodied foundation models typically requires massive-scale datasets and extensive computational resources, yet often suffers from three critical limitations: (1) inefficient sample utilization due to low-informative samples; (2) imbalanced gradient contributions across heterogeneous tasks; and (3) severe credit assignment problem in long-horizon planning, where trajectory-level rewards indiscriminately penalize all tokens. To address these issues, we propose an efficient training parad...
  </details>

- **2026-09-17** — Shaina Raza, Ahmed Y. Radwan, Imran Liaquat et al. — [A Unified Evaluation Framework for Trustworthy Large Language Models, Agentic AI, and Multimodal Systems](http://arxiv.org/abs/2609.19524v1)
  <details><summary>📄 Abstract</summary>
  Benchmark scores alone provide an incomplete basis for assessing the trustworthiness of modern artificial intelligence systems. Large language models (LLMs), agentic systems, and multimodal models (MLLMs) require different forms of assessment, yet their evaluation evidence must remain interpretable for development and oversight. We propose a unified framework that connects output-level, trajectory-level, and cross-modal assessment through eight trustworthiness dimensions: capability, robustness,...
  </details>

- **2026-09-17** — Jiayu Wang, Bin Zhu, Yue Yu et al. — [MoWAM: Explicit Future Motion Prediction for Efficient World Action Models](http://arxiv.org/abs/2609.20709v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) improve robot policy learning by incorporating future dynamics, yet explicitly generating future videos at inference introduces substantial computational overhead. Removing future generation improves efficiency, but leaves future dynamics only implicitly encoded in observation features, which can limit robustness under distribution shifts. We propose MoWAM, an efficient WAM that replaces future video generation with explicit future motion prediction. Instead of reconst...
  </details>

- **2026-09-17** — Zimu Han, Yiming Zeng, Jiyao Zhang et al. — [HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface](http://arxiv.org/abs/2609.20659v1)
  <details><summary>📄 Abstract</summary>
  Large-scale vision-language-action (VLA) models provide powerful priors for robot manipulation, yet adapting them to a specific deployment remains challenging. Supervised fine-tuning (SFT) on task-specific demonstrations provides a step toward deployment, but faces two persistent limitations: static data provide limited coverage of out-of-distribution states, and standard imitation objectives do not distinguish progressing behavior from less useful data. Interactive post-training can address the...
  </details>

- **2026-09-17** — Haodi Hu, Kaen Kogashi, Toshiaki Koike-Akino — [TacSushi: Tactile-Grounded World-Action Modeling for Dexterous Sushi Manipulation](http://arxiv.org/abs/2609.19613v1)
  <details><summary>📄 Abstract</summary>
  Dexterous food manipulation requires control under deformation, occlusion, and uncertain contact. We present TacSushi, a tactile-grounded, Cosmos3-based world-action policy that learns from recorded future consequences while acting on current observations. The backbone encodes current RGB, language, and hand state, and feature-wise gated fusion incorporates fingertip tactile features into the action representation. During training, a decoder conditioned on demonstrated action chunks predicts log...
  </details>

- **2026-09-17** — Guangzhao He, Hadar Averbuch-Elor, Wei-Chiu Ma — [Can 4D Foundation Models Remember?](http://arxiv.org/abs/2609.20819v1)
  <details><summary>📄 Abstract</summary>
  Perceiving and remembering the visual world is fundamental to navigating and interacting with our environment. Current 4D foundation models, such as camera-controllable video models or 4D reconstruction models, can perceive and reconstruct dynamic environments, but how well they remember what they have perceived remains an open question. Existing benchmarks largely rely on pixel-level metrics and lack ground truth for objects once they leave the field of view, making them unable to evaluate visu...
  </details>

- **2026-09-17** — Hanyu Xue — [Statistics, 't Hooft Anomaly, and the Else-Nayak Index: a careful comparison of concepts](http://arxiv.org/abs/2609.20813v1)
  <details><summary>📄 Abstract</summary>
  Generalized symmetries and topological excitations, as well as symmetry anomalies and the statistics of topological excitations, are widely believed to be related. There are, however, pitfalls in how this relation is established. A lattice truncation of a symmetry transformation to a finite patch gives a symmetry patch operator that creates symmetry defects at its boundary. This geometric picture resembles a hopping operator creating topological excitations at the boundary of its support, but do...
  </details>

- **2026-09-17** — Ali ArjomandBigdeli, Jiawei Zhou, Stanley Bak — [Large Language Models as Falsifiers for Cyber-Physical Systems](http://arxiv.org/abs/2609.20752v1)
  <details><summary>📄 Abstract</summary>
  Falsification searches for counterexamples to formal specifications in cyber-physical systems (CPS). With specifications written in Signal Temporal Logic (STL), falsification can be formulated as a robustness optimization problem, traditionally tackled with black-box search algorithms. In parallel, large language models (LLMs) have recently emerged as surprisingly effective optimizers when coupled with iterative prompting. In this work, we connect these ideas and introduce LLM-Falsifier, an LLM-...
  </details>

- **2026-09-17** — Levent Bulut — [Summarization Bias: The Directional Collapse of Objective Projection into Told-Mode Labels in Large Language Models --- A Conceptual Framework and Registered Test Protocol](http://arxiv.org/abs/2609.20712v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces and operationalizes summarization bias: a proposed systematic tendency of large language models (LLMs) to represent narrative meaning as an abstract summary label rather than as the reconstructable inferential structure that produces it. Within the Bulut Doctrine, narrative effect is theorized along a told-shown axis: in told mode, emotional and informational content is declared explicitly and requires little reader reconstruction; in shown mode, that content is suppressed ...
  </details>

- **2026-09-17** — Joseph Agada, Yishu Wang, Arpan Biswas — [CrystalMO-TuRBO: Multi-Objective Trust-Region Bayesian Optimization for High-precision Joint Crystal Structure Refinement](http://arxiv.org/abs/2609.20592v1)
  <details><summary>📄 Abstract</summary>
  Crystal structure refinement is a fundamental inverse problem in materials characterization, where structural parameters are optimized to reproduce experimental diffraction data. Conventional approaches, such as least-squares and likelihood-based optimization, rely on local search and often struggle with non-convex, noisy, and highly correlated parameter landscapes, particularly when integrating multiple diffraction modalities. Joint refinement of X-ray and neutron data is especially challenging...
  </details>

- **2026-09-17** — Udi Barzelay, Ophir Azulai, Idan Friedman et al. — [Spotlights: Discovering Improvement Opportunities in Software Repositories](http://arxiv.org/abs/2609.20446v1)
  <details><summary>📄 Abstract</summary>
  Coding agents and evolutionary code-search systems can improve implementations once a target and evaluation criterion have been specified. Applying these methods to an existing software repository raises an earlier question: which implementation choices are worth investigating for a high-level engineering objective? We introduce \emph{optimization-opportunity discovery}, the repository-level task of identifying candidate source regions, explaining how they relate to the objective, and proposing ...
  </details>

- **2026-09-17** — Lachlan Bridges — [Exceptional points and Jordan-chain signatures in quantum first-passage statistics](http://arxiv.org/abs/2609.20148v1)
  <details><summary>📄 Abstract</summary>
  Exceptional-point signatures in first-passage observables are governed by two independent survival mechanisms: nonlinear spectral defectivity must pass from the one-record or transfer description to the physical one-level first-passage ladder, and the resulting ladder Jordan mode must have nonzero overlap with the chosen preparation and terminal observation. For finite reset-form monitored quantum systems with upward-skip-free counting, we prove the exact threshold factorization $H_N(s)=R_s^N$, ...
  </details>

- **2026-09-17** — Farooq Ahmad Wani, Maria Sofia Bucarelli, Mujtaba Hussain Mirza et al. — [Cross-Modal Attention Acts as a Frequency Filter: Why Verbose Prompts Improve Robustness in Vision-Language Models](http://arxiv.org/abs/2609.20139v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are fragile under image corruption. We find that the wording of the question affects VLMs in two opposite ways. Verbose questions make VLMs substantially more robust---e.g., rephrasing "Is there a cat?" into "Please look carefully and answer: is there a cat?". Conversely, VLMs become more fragile under corruption when the question is semantically complex or finer-grained, e.g., "what colour is the cup left of the chair?" instead of "is there a cup?". Both effects st...
  </details>

- **2026-09-17** — Lijun Liu, Zhengzong Chen, Wenyan Li et al. — [Think Thrice Before Reranking: Multi-perspective Evidence and Reasoning Integration for Text Reranking](http://arxiv.org/abs/2609.20131v1)
  <details><summary>📄 Abstract</summary>
  Reasoning-based reranking with Large Language Models (LLMs) has shown promising improvements in text ranking. However, current methods predominantly rely on a single reasoning trajectory, resulting in rankings that are susceptible to reasoning errors and inherently constrained in modeling the multifaceted signals underlying document relevance. To resolve this dilemma, we propose MERIT-Rank(Multi-perspective Evidence and Reasoning Integration for Text Reranking), a framework that models complemen...
  </details>

- **2026-09-17** — Yifei Yuan, Jakob Wolf, Ghaith Androwis et al. — [UniExo: Unified Multi-Skill Policies for Musculoskeletal Locomotion and Co-Adaptive Exoskeleton Control](http://arxiv.org/abs/2609.19690v1)
  <details><summary>📄 Abstract</summary>
  Daily locomotion encompasses diverse activities and frequent transitions between them, yet most exoskeleton controllers are designed for a single activity or a narrow set of related movements. Changes in activity therefore typically require explicit mode switching and separately tuned or retrained controllers. Simulation-based learning reduces the need for hardware-based tuning but generally retains this limitation. Here we present UniExo, a framework that first constructs a multi-skill musculos...
  </details>

- **2026-09-17** — Chiyoung Kim, Min Sung Choi, Jinho Ju et al. — [ReShoot: Generative Visual Domain Randomization of Recorded Robot Demonstrations for Visuomotor Policy Learning](http://arxiv.org/abs/2609.19661v1)
  <details><summary>📄 Abstract</summary>
  Imitation-learned robot policies are frequently overfit to the visual conditions present in their training demonstrations. Consequently, variations in object color or background appearance often induce substantial performance degradation. A common mitigation strategy is to acquire additional demonstrations in each novel visual context; however, this approach is resource-intensive, requiring repeated access to a robot, a controlled environment, and human operation for every appearance condition t...
  </details>

- **2026-09-17** — Michael Hernandez, Tian Zhao — [The Complexity Kink: A Prompt-Side Structural Complexity Index for Code-Generation Reliability](http://arxiv.org/abs/2609.19616v1)
  <details><summary>📄 Abstract</summary>
  Complexity measured from generated code is failure-dependent: a difficult prompt can yield a short failing program and be assigned low output complexity. We introduce a six-dimension prompt-side structural-complexity index scored before generation and kept separate from correctness. We select 5,000 Python prompts across six bands of a preliminary single-rater rubric. Four out-of-panel LLM raters rescore the locked prompts, giving 19,997 score rows; composite inter-rater reliability is ICC = 0.87...
  </details>

- **2026-09-16** — Zejie Tian, Ruibing Hou, Bingpeng Ma et al. — [ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots](http://arxiv.org/abs/2609.19340v1)
  <details><summary>📄 Abstract</summary>
  Humanoid loco-manipulation requires adaptive whole-body coordination to seamlessly integrate locomotion and physical interaction. Despite recent advances, learning autonomous loco-manipulation remains challenging due to the scarcity of diverse, physically executable robot-object interaction data and the difficulty of learning unified whole-body control directly from onboard observations. We present ViLoMan, a scalable framework for autonomous humanoid loco-manipulation. ViLoMan first transforms ...
  </details>

- **2026-09-16** — Ci Lin, Futong Li, Rose Chong-Wu et al. — [Enhanced Agriculture-informed Neural Network by Domain Knowledge](http://arxiv.org/abs/2609.19466v1)
  <details><summary>📄 Abstract</summary>
  Accurate prediction of nitrous oxide (N2O) emissions from agriculture is important for assessing environmental impacts and supporting sustainable farming. However, prediction remains difficult because N2O emissions result from complex interactions among soil properties, climate, biochemical processes, and management practices, while high-quality observations are limited. Deep learning models can capture nonlinear relationships but often lack physical interpretability and may generalize poorly ac...
  </details>

- **2026-09-16** — Rahul Patel, Daniel Seifried, Alvaro Hacar — [Characterizing the hierarchical structure of filaments I. On the origin of the length-mass (L-M) scaling relation](http://arxiv.org/abs/2609.19369v1)
  <details><summary>📄 Abstract</summary>
  Aims. Filamentary structures in molecular clouds are widely recognized as fundamental components of star formation. Observations report a length-mass relation of the form $L \propto M^α$ with $α\simeq 0.5$. We characterize this relation in simulated molecular clouds and investigate the influence of hierarchical fragmentation and spatial resolution.   Methods. We apply a two-step filament identification method to high-resolution 3D hydrodynamical and magnetohydrodynamical simulations from the SIL...
  </details>

- **2026-09-16** — Saurabh Kumar, Shashi Ranjan Kumar, Abhinav Sinha — [Equivalent-Agent Guidance for Cooperative UAV Payload Transportation](http://arxiv.org/abs/2609.19312v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a guidance framework for cooperative transportation of a rigid payload by two uncrewed aerial vehicles (UAVs) to stationary and maneuvering landing platforms. A virtual equivalent-agent representation is first introduced to describe the translational motion of the rigidly coupled UAV-payload system, allowing the transportation problem to be formulated in terms of relative range and line-of-sight dynamics with respect to the landing platform. A geometric analysis establishes t...
  </details>

- **2026-09-16** — Mahsa Amani, Seungeon Lee, Abhisek Dash et al. — [Characterizing Web Search by Conversational LLM Agents: From Search Decisions and Strategies to Results and Responses](http://arxiv.org/abs/2609.19244v1)
  <details><summary>📄 Abstract</summary>
  Conversational LLM agents increasingly rely on Web search, yet the end-to-end lifecycle of agentic search remains poorly understood. We present the first study of Web search across four major conversational platforms (ChatGPT, Claude, Grok, and DeepSeek), combining real-world user interactions (invivo) with controlled experiments using the same platform's models by their APIs (invitro). We investigate the quality of agentic decisions to invoke Web search, their strategies to formulate queries, t...
  </details>

- **2026-09-16** — Ashwini Kurady, Sri Sai Charith Grandhi, Rajesh Gupta et al. — [Compositional Policy Violations: When Step-Level Compliance Fails In Agentic AI Workflows](http://arxiv.org/abs/2609.18820v2)
  <details><summary>📄 Abstract</summary>
  Agentic workflows now make consequential decisions in regulated settings, and the governance placed around them is almost entirely step-scoped: input-output classifiers, per turn rails, and span-level evaluators. The policies organizations actually hold, such as referral thresholds, authority limits, and review requirements, are properties of the whole execution rather than of any one step. This mismatch admits a failure mode we call a Compositional Policy Violation (CPV): every individual step ...
  </details>

- **2026-09-16** — Dongzhou Cheng, Taoran Yi, Ye Fang et al. — [In-Context Robot Learning with VLM Agents](http://arxiv.org/abs/2609.19138v1)
  <details><summary>📄 Abstract</summary>
  Enabling robots to adapt to unfamiliar environments as readily as humans remains a moonshot goal of embodied AI. No finite collection of demonstrations can cover every task and situation a robot will encounter, making the ability to learn from context at deployment essential for generalization. Such in-context learning (ICL), however, remains largely beyond the reach of existing robotic policies. The broad agentic capabilities of commercial vision-language models (VLMs), such as GPT-6 Astra, rai...
  </details>

- **2026-09-16** — Sijie Dong, Wei Ren, Xuanwei Hu et al. — [BENCHCOMPASS: From Scores to Signals for Training and Harness Decisions in Payment-Domain LLMs](http://arxiv.org/abs/2609.18270v1)
  <details><summary>📄 Abstract</summary>
  Payment operations are a critical financial infrastructure, but the value of large language models in this domain remains unclear because payment rules change quickly, evidence is fragmented, and decisions depend on transaction state, participant role, region, and payment rail. Existing benchmarks do not isolate whether failures come from missing payment-rule knowledge, poor use of supplied evidence, or brittleness under imperfect harness inputs. We introduce BENCHCOMPASS, a payment-domain bench...
  </details>

- **2026-09-16** — Sneha Paul, Guile Wu, Bingbing Liu et al. — [PhysVGGT: Feed-Forward Dense Physical Property Estimation from A Single Image](http://arxiv.org/abs/2609.18920v1)
  <details><summary>📄 Abstract</summary>
  Physical properties, such as friction, hardness, stiffness, and density, govern how robots should grasp, manipulate and interact with objects, yet estimating these properties from RGB images remains challenging. Existing methods typically employ per-object reconstruction augmented with physical properties or directly query vision-language models at test time, which results in substantial computational overhead that limits their applicability. In this work, we present PhysVGGT, a feed-forward mod...
  </details>

- **2026-09-16** — Perry Dong, Kuo-Han Hung, Dorsa Sadigh et al. — [Reinforcement Learning for Real-Time Vision-Language-Action Policies](http://arxiv.org/abs/2609.18207v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning fine-tuning on top of large, pretrained Vision-Language-Action (VLA) models offers promise for highly reliable robot deployment. However, because of their scale, modern VLA models suffer from high inference latency, so the observation used to select an action is often stale by execution time, creating a distribution shift that can substantially degrade reliability and performance. Prior work has explored asynchronous policy execution to reduce the effect of latency, but th...
  </details>

- **2026-09-16** — Luyao Zhu, Xun Wei Yee, Wei Li et al. — [MUSE: Benchmarking Large Vision-Language Models on Multi-Modal Understanding in Situated Education](http://arxiv.org/abs/2609.19088v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models have achieved remarkable progress in multi-modal understanding, yet their capabilities in educational settings remain insufficiently evaluated. In AI-assisted language learning, models must interpret artistic imagery, understand its semantic, affective, and cultural content, and reason about visual context to support meaningful interaction. However, existing benchmarks primarily focus on real-world images or domain-specific educational reasoning, providing limited co...
  </details>

- **2026-09-16** — Rolando Fernandez, Caleb Probine, Tyler Lee et al. — [Social Laws for Multi-agent Coordination in Stochastic Environments](http://arxiv.org/abs/2609.18929v1)
  <details><summary>📄 Abstract</summary>
  In multi-agent environments, coordinating agents to prevent interference and ensure robust individual performance is a critical challenge. Previous research on social laws for multi-agent systems has primarily focused on deterministic, goal-based settings. This paper extends the concept of social laws to stochastic, reward-based environments, proposing a formalism for defining and verifying their robustness under various conditions. We introduce the notion of $α$-robustness, a measure of the gua...
  </details>

- **2026-09-16** — Ashwini Kurady, Sri Sai Charith Grandhi, Rajesh Gupta et al. — [Compositional Policy Violations: When Step-Level Compliance Fails In Agentic AI Workflows](http://arxiv.org/abs/2609.18820v1)
  <details><summary>📄 Abstract</summary>
  Agentic workflows now make consequential decisions in regulated settings, and the governance placed around them is almost entirely step-scoped: input-output classifiers, per turn rails, and span-level evaluators. The policies organizations actually hold, such as referral thresholds, authority limits, and review requirements, are properties of the whole execution rather than of any one step. This mismatch admits a failure mode we call a Compositional Policy Violation (CPV): every individual step ...
  </details>

- **2026-09-16** — Tomas Balyo, Lukas Chrpa, G. Michael Youngblood — [Which LLM is Best for Translating Natural Language Goals to PDDL](http://arxiv.org/abs/2609.18731v1)
  <details><summary>📄 Abstract</summary>
  Bridging the gap between human intent and machine execution remains a challenge in automated planning, where expressing goals in formal languages like PDDL restricts accessibility to non-experts. This paper empirically evaluates whether current Large Language Models (LLMs) can reliably translate natural language testing goals, written in informal language by video game testers, into well-formed PDDL targets suitable for classical planning. We present a carefully designed prompt template, integra...
  </details>

- **2026-09-16** — Dunyao Xue, Chengshuo Du, Zhengbo Wang et al. — [Beyond Truncation: Rethinking LLM Decoding as Ensemble Pruning](http://arxiv.org/abs/2609.18723v1)
  <details><summary>📄 Abstract</summary>
  We introduce Mahalanobis-Ensemble Decoding (ME-Decoding), a novel Large Language Model (LLM) decoding framework that frames candidate token selection as ensemble pruning. Existing selection strategies rely predominantly on scalar probabilities, ignoring geometric semantic relationships and causing candidate redundancy. Meanwhile, current geometry-aware methods often require complex optimization or directly reweighting the original token probabilities, leading to significant computational overhea...
  </details>

- **2026-09-16** — Xingpeng Sun, Zherong Pan, Kai Cheng et al. — [M$^3$P-R1: Reinforcement Learning for Large Language Model Guided Multi-Modal Motion Planning via MIP Code Generation](http://arxiv.org/abs/2609.18669v1)
  <details><summary>📄 Abstract</summary>
  Multi-Modal Motion Planning (M$^3$P) requires joint reasoning over continuous motions and discrete mode transitions, making it difficult to solve efficiently. For instance, a bipedal robot may walk to a target location and then use its arms to grasp an object. This scenario captures both mode transitions and continuous dynamics, yielding feasible paths that neither purely discrete nor continuous planners can handle. While Mixed-Integer Programming (MIP) offers a principled framework, constructin...
  </details>

- **2026-09-16** — Alexander Didenko, Anna Shabanova, Vladislav Zapylikhin et al. — [GYROval: A Robust Benchmark for Cultural Value Orientation in Large Language Models](http://arxiv.org/abs/2609.18384v1)
  <details><summary>📄 Abstract</summary>
  We present a robust benchmark for measuring cultural value orientation in large language models on the two Inglehart-Welzel axes over several domains and roles (hence GYROval - Gridded Yielding of Robust value Orientation), together with the results of administering it to twenty models. Items are binary contrastive scenarios in the sense introduced by CDEval: both options are legitimate courses of action, neither is correct, there is no answer key, and a model's score on an axis is the proportio...
  </details>

- **2026-09-16** — Xiaomeng Wang, Martha Larson, Zhengyu Zhao — [Visual Input and Its Framing Affect Attribute-based Descriptions Produced by Large Vision-Language Models](http://arxiv.org/abs/2609.18345v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) are commonly used with only a single text prompt as the input, or plus an image. In this paper, we demonstrate that when the image exists, even if the text prompt is not about the specific instance (but only the concept it belongs to) in that image, the response would still be affected. For example, when the text prompt only asks for the attribute descriptions of a dog breed, an image depicting a specific dog from that breed would shift the response. Further,...
  </details>

- **2026-09-16** — Yasushi Kawase, Warut Suksompong, Hanna Sumita et al. — [Fractional Assignment with $\ell_1$ Preferences](http://arxiv.org/abs/2609.18299v1)
  <details><summary>📄 Abstract</summary>
  We study a fractional assignment setting where $n$ objects are to be assigned to $n$ agents with unit capacity, and each agent specifies an ideal distribution over the objects. Unlike in classic random assignment, these ideal distributions are not necessarily degenerate, as agents may prefer a mixture of objects rather than any single object. We assume that agents seek to minimize the $\ell_1$ distance between their ideal distribution and the distribution they receive, which is equivalent to max...
  </details>

- **2026-09-16** — Ayesha Shafique, Barton P. MIller, Elisa R. Heymann — [A Study of the Reliability of Agentic AI-Generated Programs](http://arxiv.org/abs/2609.18298v1)
  <details><summary>📄 Abstract</summary>
  Agentic-AI based software development offers the promise of faster completion of the software, greater programmer efficiency, and more reliable code. The question is how can we verify these claims in an objective way? In this project, we attempted to answer this question based on three practices. First, we applied a typical best-practices agentic AI workflow for software development. Second, our target programs were ten well-known, release-quality human-written Linux utility programs so that we ...
  </details>

- **2026-09-16** — Tianyi Xiang, Xupeng Xie, Jiahang Cao et al. — [Function-Preserving Data Generation for Zero-Shot Real-to-Sim-to-Real Manipulation](http://arxiv.org/abs/2609.18293v1)
  <details><summary>📄 Abstract</summary>
  Robotic data generation is a promising paradigm for scaling robot learning without collecting large-scale real-world data. However, generating geometrically diverse yet physically valid data for contact-rich tasks remains challenging, especially when success depends on precise geometric interfaces. Standard shape augmentation methods often distort task-critical interfaces, resulting in invalid contact relationships, e.g., fit mismatches or interpenetration, rendering downstream interactions infe...
  </details>

- **2026-09-16** — Lefebvre Renard Clément, Lébé Vincent, Da Silva Ribeiro Pereira Ricardo et al. — [Building Trust in Artificial Intelligence: A Necessity for Railway Applications](http://arxiv.org/abs/2609.18278v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) is currently only applied to non-safety critical applications due to the strict standards and regulations for railway industries. We propose to review the three main fields necessary to increase trust in data science and AI algorithms and reach compliance: robustness, Operational Design Domain (ODD), and explainability. Robustness is the ability of an AI system to maintain its level of performance under any circumstances (ISO24029). ODDs allow the explicit definition...
  </details>

- **2026-09-16** — Yerim Oh, Gunhee Kim — [REPAIR: Resolving Long-Tail Confusion in Scientific Retrievers via Fact-Verified Iterative Refinement](http://arxiv.org/abs/2609.18262v1)
  <details><summary>📄 Abstract</summary>
  Precise retrieval of scientific information is fundamentally constrained by long-tailed concepts and high fact-sensitivity of scientific corpora. These challenges often limit the effectiveness of dense retrievers and hallucination-prone LLM augmentation. To address this, we present REPAIR, a self-evolving data augmentation framework for scientific dense retrievers. REPAIR iteratively synthesizes training data to address knowledge gaps by cycling through diagnosis of long-tail concepts, API-guide...
  </details>

- **2026-09-16** — Yifan He, Yang Liu, Wenhao Zhao et al. — [OmniRisk: Omnidirectional Trajectory-Risk Learning for Agile Quadrotor Dynamic Avoidance](http://arxiv.org/abs/2609.18191v1)
  <details><summary>📄 Abstract</summary>
  Agile quadrotor avoidance of fast-moving obstacles requires anticipating collisions and selecting feasible maneuvers within short reaction windows. Reliable predictive avoidance remains challenging because sparse range observations do not directly reveal obstacle motion, while online trajectory optimizers either scale poorly with obstacle count or remain efficient at the expense of reliability in dense, high-speed encounters. We present OmniRisk, an omnidirectional planning framework that learns...
  </details>

- **2026-09-16** — Li Chen — [AutoTuneBench: Trustworthy Measurement for Agent Auto-Tuning of LLM Serving Engines](http://arxiv.org/abs/2609.18123v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents tune GPU kernels and serving engines through a closed loop of propose, measure, and keep, but the measurements behind this loop are not trustworthy. We characterize four failure modes from a four-day pilot corpus of 619 model calls: strawman baselines manufacture speedups, absolute times do not transfer across machines, saturated tasks nullify comparisons, and infrastructure defects impersonate science. We present AutoTuneBench, a benchmark and measurement protocol th...
  </details>

- **2026-09-16** — Kosuke Kitahara, Nobuhiro Yamaguchi — [Linguistic Triggers of Gender and Racial Bias in Open-Weight LLMs Applied to Recruitment](http://arxiv.org/abs/2609.18106v1)
  <details><summary>📄 Abstract</summary>
  Open-weight large language models are rapidly entering hiring pipelines, yet their discriminatory failure modes -- and the regulatory exposure these create under the EU AI Act high-risk classification (Annex III) and U.S. EEOC adverse-impact analysis -- remain poorly understood. We present the first systematic, multi-model audit of open-weight LLMs that treats job-posting language as the primary experimental variable, evaluating six models (Llama 3.2, Mistral, Gemma 3, Qwen 3, Phi 3, DeepSeek-R1...
  </details>

- **2026-09-15** — Caiqi Zhang, Xiaochen Zhu, Chengzu Li et al. — [Confidence Comes from Experience: Experiential Confidence Estimation from Reasoning to Agents](http://arxiv.org/abs/2609.17708v1)
  <details><summary>📄 Abstract</summary>
  Reliable confidence estimation is increasingly central to the trustworthy deployment of language models: a calibrated estimate of the probability that an output is correct decides what to ship, what to escalate, and what to retry. Existing confidence estimators, however, share one design premise: they only read the current inference process, either by introspecting on it, scoring its token probabilities, or resampling it. We argue that the current inference is not a sufficient basis for confiden...
  </details>

- **2026-09-15** — Srijith Ravikumar — [The Missing "I Don't Know": Why Three Reasoning-Reliability Findings Converge on Calibrated Abstention](http://arxiv.org/abs/2609.17686v1)
  <details><summary>📄 Abstract</summary>
  Three recent results describe what look like unrelated LLM reliability problems. Yin et al. (2026) show reasoning RL collapses tool-reliability representations. Suleymanov et al. (2026) show that under safety-constrained generation, large models rewrite flagged spans while small models truncate. Bastounis et al. (2024) prove any consistent-reasoning system without an implicit "I don't know" function must hallucinate infinitely often on broad problem classes. We argue these findings converge on a...
  </details>

- **2026-09-15** — Oier Larumbe-Lizarraga, Roberto Pereira, Cristian J. Vaca-Rubio — [Goal-oriented probabilistic forecasting for dynamic PRB allocation in 5G networks](http://arxiv.org/abs/2609.17297v2)
  <details><summary>📄 Abstract</summary>
  Efficient physical resource block (PRB) allocation in 5G networks requires accurate demand forecasting. Conventional methods minimize symmetric error metrics (MAE, RMSE), ignoring the operational cost asymmetry where under-provisioning (service degradation) is far costlier than over-provisioning (wasted capacity). We propose a goal-oriented probabilistic forecasting framework that aligns model training with the operator's decision-making objectives. Specifically, we train DeepAR and Temporal Fus...
  </details>

- **2026-09-15** — Wuyang Dai, Moses Openja, Jiho Shin et al. — [A Large-Scale Empirical Study of Quality Assurance Practices and Gaps in AI Agents](http://arxiv.org/abs/2609.17698v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agents are increasingly used across software engineering, web automation, research, and productivity applications. Their integration of planning, memory, tool use, code execution, and external interactions enables greater autonomy but also introduces new reliability, safety, and security risks. We present a large-scale empirical study of quality assurance (QA) practices in 157 open-source LLM-based agent projects with at least 100 GitHub stars. We analyze documen...
  </details>

- **2026-09-15** — Riyaaz Shaik, Chandru Venkataraman — [REVERSAL-BENCH: A Reversibility Axis and Reset Oracle for Measuring the Reset-Free RL Cliff](http://arxiv.org/abs/2609.17745v1)
  <details><summary>📄 Abstract</summary>
  A central goal of autonomous reinforcement learning is continuous policy training without external resets. However, existing paradigms largely depend on underlying environmental reversibility, a property absent in real world manipulation, where events such as pushing objects off tables or spilling granular substances cannot be undone. We introduce REVERSAL-BENCH, a benchmark that controls reversibility via a continuous parameter $ρ\in [0, 1]$ and provides a reset oracle, a ground-truth verificat...
  </details>

- **2026-09-15** — Keivan Bolouri — [Efficient estimation and the cost of complete-case coarsening under monotone sequential MAR](http://arxiv.org/abs/2609.17778v1)
  <details><summary>📄 Abstract</summary>
  Complete-case coarsening discards observed confounder values from partially complete records. We study its consequences for average treatment effect estimation with two ordered, partially observed confounders under monotone sequential missing at random. We specialize the standard coarsening-at-random transformation to the causal influence function, establish the canonical gradient, and give an exact drift identity for a cross-fitted estimator with sequential multiple robustness. In the submodel ...
  </details>

- **2026-09-15** — A. Ferrara, B. Das, M. Kohandel et al. — [On the clumpy nature of super-early galaxies](http://arxiv.org/abs/2609.17667v1)
  <details><summary>📄 Abstract</summary>
  JWST has revealed that galaxies during the Epoch of Reionization are composed of compact stellar clumps spanning more than two orders of magnitude in mass and size. We present an analytical framework that connects the global properties of high-redshift galactic disks to the formation, dynamical evolution and visibility of these systems. Starting from the classical Toomre instability, we derive analytical mass-size and surface density-size relations together with, for the first time, the intrinsi...
  </details>

- **2026-09-15** — Sehee Kim, Yumin Choi, Minki Kang et al. — [EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading Agents](http://arxiv.org/abs/2609.17632v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) trading agents can combine market data, news, and executable analysis, but their behavior is often controlled by static hand-written tool-use policies that are fixed before deployment. This limits their ability to adapt how they gather evidence, invoke tools, verify signals, and manage risk under changing market regimes. We introduce EvolveTrade, a self-evolving framework that treats the system prompt of a tool-using trading agent as a text-parameterized policy. After ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

- **2026-09-18** — Tengfei Shao — [Auditing bipartite motif interpretations: a worked example with conservation checks and open-path decomposition](http://arxiv.org/abs/2609.22014v1)
  <details><summary>📄 Abstract</summary>
  Motif profiles of bipartite agent-object networks, such as tourist-site visits and customer-item transactions, are read as evidence about structural roles and about differences between networks, often without asking what the two degree sequences already fix. In a simple bipartite graph the induced k-fan count on one node type is a sum of degree combinations, so it has zero variance under a null that preserves both degree sequences. We apply this known result to a reconstructed tourism rating net...
  </details>

- **2026-09-18** — Zijie Cao, Xijun Qu, Zhicheng Gu et al. — [AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory](http://arxiv.org/abs/2609.21940v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is essential for large language model (LLM) agents to maintain consistency and personalization over extended interactions. Existing memory systems typically rely on fixed granularities or static schemas, but these designs struggle when heterogeneous information, such as preferences, events, constraints, and temporal updates, is embedded in a single mixed representation. The resulting semantic interference makes top-K retrieval sensitive to noise and often leaves relevant evidenc...
  </details>

- **2026-09-18** — Yanxiao Liu, Sicheng Wan, Zhan Gao et al. — [Watermarkable Multi-Draft Speculative Sampling via Poisson Processes](http://arxiv.org/abs/2609.21858v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have achieved state-of-the-art performance across a wide range of tasks, motivating two important aspects of deployment: inference efficiency and output provenance, which can be tackled by speculative sampling and watermarking, respectively. However, recent works have shown that combining these two goals is highly nontrivial and can be potentially impossible. In this work, we develop a novel multi-draft speculative sampling algorithm based on Poisson processes that i...
  </details>

- **2026-09-18** — Kairui Yang, Xunkai Li, Kaixiang Zhang et al. — [OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems](http://arxiv.org/abs/2609.21527v1)
  <details><summary>📄 Abstract</summary>
  Graph-enhanced multi-agent systems (G-MAS) coordinate large language model agents through communication graphs and role assignments, which determine how agents exchange information and divide responsibilities. However, final-score comparisons across systems combine differences in models, communication patterns, roles, and computation costs, making performance differences difficult to attribute to specific communication structures, role assignments, and information flows. To address this evaluati...
  </details>

- **2026-09-18** — Qiang Zhang, Ruixue Ding, Fanrui Zhang et al. — [ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL](http://arxiv.org/abs/2609.21378v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has substantially improved large language model (LLM) agents in verifiable domains, but remains difficult to apply to open-ended agent tasks, where solutions are diverse and reliable scalar rewards are hard to obtain. Recent pairwise evaluation methods alleviate reward discrimination collapse by replacing pointwise scoring with relative preferences. However, they still compress rich comparative feedback into a single trajectory-level reward, obscuring decisive intermediate...
  </details>

- **2026-09-17** — Luca De Grandis, Silvia Cappelletti, William Raccagni et al. — [DocAttriBench: Benchmarking Answer Grounding in Document Visual Question Answering](http://arxiv.org/abs/2609.20574v1)
  <details><summary>📄 Abstract</summary>
  Answer grounding in document visual question answering remains an open challenge: most benchmarks lack grounding annotations or provide limited-quality labels, while constructing grounded datasets still requires costly manual effort. We introduce DocAttriBench (DAB), a large-scale benchmark for fine-grained, element-level source attribution in Document VQA, grounding answers to specific layout elements such as text blocks, tables, and images. To build DAB, we propose a Mask-based Perplexity-Deri...
  </details>

- **2026-09-17** — Moritz Weckbecker, Sweta Jena, Jonas Müller et al. — [Can Data Attribution Filter Out Subliminal Learning? Not Reliably](http://arxiv.org/abs/2609.20027v1)
  <details><summary>📄 Abstract</summary>
  Subliminal learning allows language models to transmit behavioral traits through training data with no obvious semantic relationship to those traits, undermining content-based data filtering as a safety intervention. Training data attribution offers an alternative: it identifies the training examples responsible for a given model behavior, independent of their semantic content, and so may apply in exactly the cases where semantic inspection fails. We evaluate three gradient-based attribution met...
  </details>

- **2026-09-17** — Ziqiao Shang, Ling-Yue Ge, Lan-Zhe Guo — [SkillAA: Attribution-Guided Skill-Graph Updating with Targeted Validation and Rollback](http://arxiv.org/abs/2609.20455v1)
  <details><summary>📄 Abstract</summary>
  External skills provide domain procedures without parameter updates, but existing methods often edit skills directly from failed rollouts without structured routing from an observed failure to an editable location; existing skill graphs also underuse semantic boundaries, object addresses, and topological dependencies for skill retrieval, targeted updating, and scoped validation. We introduce SkillAA (Skill Abductive Attribution), a structured skill-optimization framework for frozen language mode...
  </details>

- **2026-09-17** — Yutong Yao, Yanjie Cao, Guanhua Chen et al. — [Before the Arrest: Benchmarking LLMs on Criminal Profiling from Incomplete Evidence](http://arxiv.org/abs/2609.19965v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly applied to legal and criminal justice tasks, yet existing work focuses almost exclusively on post-arrest scenarios where the suspect's identity is already known, leaving the critical pre-arrest challenge of inferring suspect characteristics from incomplete evidence largely unexplored. To fill this gap, we introduce the Profiling, Investigation, and Judgment (PIJ), comprising 2,500 real homicide cases from five countries. PIJ evaluates LLMs across thr...
  </details>

- **2026-09-17** — Xingyu Liu, Yu Dong, Qizhen Yu et al. — [FootprintRAG: Visual Analytics for Evidence Context Refinement in RAG-based Scientific Literature Exploration](http://arxiv.org/abs/2609.19601v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) is increasingly used to ground large language model (LLM) outputs in scientific literature. However, in open-ended literature exploration, the evidence context used for generation is often produced through hidden retrieval, reranking, assessment, and filtering steps. Users may receive retrieval summaries without knowing how the system constructed the evidence context, which evidence units were retained or discarded, or whether potentially useful evidence was ...
  </details>

- **2026-09-16** — Fengnan Li, Heman Burre, Liwen Sun et al. — [EviGen: Predictive Evidence Scaffolding for Verifiable Clinical Rationale Generation](http://arxiv.org/abs/2609.18852v1)
  <details><summary>📄 Abstract</summary>
  Longitudinal electronic health records (EHRs) capture years of patient history across notes, codes, labs, and procedures, and contain evidence needed to reason about likely clinical outcomes. However, comprehensive clinician review of these records is impractical, and LLM-based processing is costly and often unreliable, missing some relevant observations while hallucinating others. We therefore propose EviGen, a three-layer framework for verifiable clinical rationale generation that addresses th...
  </details>

- **2026-09-16** — Liyang Fan, Chi Wei, Yitai Li et al. — [ReFigBench: Benchmarking Scientific Figure Reconstruction as Editable PowerPoint Artifacts](http://arxiv.org/abs/2609.18844v1)
  <details><summary>📄 Abstract</summary>
  Multimodal coding agents are expected to turn visual inputs into usable artifacts, and they act through a harness, the layer of tools, context management, and execution environment around the model. Existing evaluations often isolate short tool calls, API traces, or screenshot resemblance, and a low score under these proxies cannot say whether the model saw poorly, planned poorly, or was failed by its harness. We study scientific overview figure reconstruction, an agent task in which a source im...
  </details>

- **2026-09-15** — Mohammadreza Sediqin, Shivali Dalmia, Sumukha Thoppanahalli et al. — [SAGE: Governed Artifact Generation from Enterprise Guidelines](http://arxiv.org/abs/2609.17775v1)
  <details><summary>📄 Abstract</summary>
  Enterprise guideline documents mix narrative text, complex tables, and embedded images, and converting them into structured work artifacts still takes two to three days of manual effort each. Current language and vision-language models extract from such documents but offer no governed workflow beyond extraction: no validation, no consistency checking, no traceable artifact generation. We introduce SAGE, a governed multi-stage LLM pipeline organized around a shared versioned rule store with stabl...
  </details>

- **2026-09-15** — Sikun Wang, Yixi Zhou, Lei Fan et al. — [GraphEcho: Structural Redundancy and Evidence Provenance in LLM Graph Agents](http://arxiv.org/abs/2609.17695v1)
  <details><summary>📄 Abstract</summary>
  A large language model (LLM) agent can follow more graph paths without acquiring more independent evidence. GraphEcho tests whether agents mistake these repeated encounters for additional corroboration. The benchmark varies path counts and evidential origins while holding evidence content fixed, and evaluates both judgments and active exploration. Controlled synthetic experiments reveal model-dependent judgment shifts, but redundant supporting paths increase the share of repeated walks across al...
  </details>

- **2026-09-15** — Narcis Marincat — [What You Can't See Is Still What You Learn: A Preregistered Sixty-Society Confirmation That Evidence Masking Drives Compositional Generalization](http://arxiv.org/abs/2609.17637v1)
  <details><summary>📄 Abstract</summary>
  Restricting what a module can read may improve what a system learns to compute. We test this in a preregistered confirmation with sixty four-cell systems sharing a frozen language-model backbone and communicating through learned continuous packets. Five conditions vary evidence masking, ownership markers, and replacement of foreign evidence with neutral filler, across six initialization clusters, each with two data orders, on one fresh task world. With markers available in both regimes, masking ...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-09-18** — Hiskias Dingeto — [A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal](http://arxiv.org/abs/2609.21996v1)
  <details><summary>📄 Abstract</summary>
  Large language models can hold knowledge they do not report. A model may sandbag on a capability evaluation, or answer against what it internally knows, and its outputs alone cannot tell whether it is hiding an answer or simply does not have one. We borrow the Concealed Information Test, a forensic method that identifies guilty knowledge by presenting a suspect with the true detail among plausible decoys and measuring a stronger response to the item they recognize. Our method, Probe of Internal ...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-09-17** — Song Zhang, Jiankang Yao, Hongtao Li et al. — [A Scalable Trust Discovery Architecture for the Internet of Agents](http://arxiv.org/abs/2609.20095v1)
  <details><summary>📄 Abstract</summary>
  The Internet of Agents is expected to enable large numbers of autonomous agents to discover, verify, and collaborate with each other across heterogeneous platforms. However, current agent protocols mainly address tool invocation and inter-agent communication, leaving scalable agent registration, trustworthy identification, and capability-oriented discovery largely unresolved. To address this, this paper proposes a scalable trust discovery architecture for the Internet of Agents. The proposed arc...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-09-16** — Oded Ovadia, Elad Ben Zaken, Elad Guttman et al. — [MiST: Mid-Training LLMs for Cybersecurity](http://arxiv.org/abs/2609.18496v1)
  <details><summary>📄 Abstract</summary>
  Cybersecurity combines high-stakes analysis with complex technical language, making it an impactful and challenging domain for LLMs. We present MiST (Mid-trained Security Transformer), a suite of 8B and 32B models that achieve strong performance on public cybersecurity benchmarks. We use mid-training as an intermediate adaptation stage between general pre-training and cybersecurity training. Rather than performing continual pre-training over large volumes of raw domain text, we curate a compact,...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 8 papers

- **2026-09-17** — Yunqian Cheng, Roberto Manduchi — [SlugTrails: An Egocentric Benchmark for Floor Plan Localization in Large Buildings](http://arxiv.org/abs/2609.19876v1)
  <details><summary>📄 Abstract</summary>
  Floor-plan-based indoor visual localization enables infrastructure-free positioning, but most methods are developed and evaluated in small residential environments unlike the large public buildings of real deployment. We introduce SlugTrails, a floor plan localization benchmark for large indoor spaces under realistic egocentric sensing: $30$ Hz Aria glasses recordings across three campus buildings and six floors ($22089$ m$^2$ of floor plan outline), CAD-derived floor plans with semantic classes...
  </details>

- **2026-09-17** — Veronika Batzdorfer, Carlo Romano Marcello Alessandro Santagiustina — [Reproducibility is not construct validity: LLM measurement of institutionally situated communication](http://arxiv.org/abs/2609.19866v1)
  <details><summary>📄 Abstract</summary>
  High annotation reproducibility does not necessarily imply that an LLM-inferred measure captures the construct it is intended to measure. We test this distinction using a dataset from the European Commission's AI Act consultation, linking structured survey responses to free-text consultation submissions from the same stakeholders. LLM annotations of consultation submissions are highly reproducible (intraclass correlations > 0.99), yet show limited convergence with survey-reported measures of the...
  </details>

- **2026-09-17** — Xu Yuan, Yi Wang, Zhuohang Jiang et al. — [AI Smart Glasses for Wearable Intelligence: From Egocentric Sensing to Agentic Personalization](http://arxiv.org/abs/2609.19793v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in artificial intelligence (AI) are reshaping smart glasses from egocentric capture and display devices into platforms for wearable intelligence. Smart glasses increasingly serve as wearable AI systems that connect first-person observation with real-time assistance under strict form-factor constraints. We frame this transition through the lens of \emph{AI smart glasses} and define them as a system-level concept in which egocentric sensing, resource-aware computing, intelligent re...
  </details>

- **2026-09-16** — Guangping Liu, Nicholas Hawkins, Tipu Sultan et al. — [From Wizard-of-Oz Human-Robot Dialogue Collection to a Taxonomy of Robot Response Decisions: A Retrospective Analysis of Assistive Pilot Interactions](http://arxiv.org/abs/2609.19447v1)
  <details><summary>📄 Abstract</summary>
  Robots that follow natural-language instructions in everyday indoor environments must act on incomplete human utterances. Instructions often omit essential information, such as the identity of an out-of-view object, an intended destination, or the user's goal. Existing datasets contain little real-world situated dialogue and provide few practice-grounded criteria for deciding when a robot should act, confirm, clarify, or refuse. We retrospectively analyze a pilot Wizard-of-Oz study in which five...
  </details>

- **2026-09-16** — Satyam Gaba, Krutiksinh Rana, Siva Sai et al. — [A Comprehensive Review of Generative Physical Artificial Intelligence](http://arxiv.org/abs/2609.18111v1)
  <details><summary>📄 Abstract</summary>
  The integration of large-scale foundation models with physical embodiments has led to significant advancements in robotics known as Generative Physical Artificial Intelligence (GPAI). These agentic AI systems autonomously perceive, reason, and act in complex real-world situations. This survey comprehensively analyzes GPAI systems, focusing on their architectural foundations, current applications, and key limitations. We introduce a taxonomy of five distinct approaches: Robot Foundation Models (R...
  </details>

- **2026-09-16** — Peixuan Hou, Bin Chen, Li He et al. — [Behavior2Value: Benchmarking and Empowering LLMs for Consumer Value Measurement from E-commerce Behaviors](http://arxiv.org/abs/2609.18203v1)
  <details><summary>📄 Abstract</summary>
  Human values are deep motivational orientations that shape human behaviors. In e-commerce, they reveal the stable drivers behind users' purchase decisions. Compared with short-term interests, consumer values better explain how users evaluate products before purchase. However, consumer values are often implicit in complex and fragmented behavioral trajectories, leaving value measurement from e-commerce behaviors largely underexplored. To this end, we propose the Behavior-to-Value (B2V) task, whic...
  </details>

- **2026-09-16** — Zihao Zhou, Zhaolin Wang, Yuanwei Liu — [Agents in the Scene: An Agentic Framework for Resource-Efficient Site-Specific Base Station Deployment](http://arxiv.org/abs/2609.18027v1)
  <details><summary>📄 Abstract</summary>
  An agentic framework is proposed for autonomous site-specific base station (BS) deployment in wireless network planning. In contrast to conventional approaches that rely on manual site surveys or extensive ray-tracing (RT) simulations with significant human intervention, the proposed framework autonomously explores and optimizes BS deployment under a limited RT evaluation budget, enabling resource-efficient network planning. To this end, a continuous, geometry-grounded deployment action space is...
  </details>

- **2026-09-15** — Priyanka Nair-Turkich, Patricia T. Campbell, Nicholas Geard — [Modelling sexual partnership dynamics and population heterogeneities in agent-based dynamic network models](http://arxiv.org/abs/2609.17622v1)
  <details><summary>📄 Abstract</summary>
  Population-level heterogeneities, combined with temporal fluctuations in sexual partnerships, shape the structure of sexual contact networks and can substantially influence the spread of sexually transmitted infections (STIs). Traditional static network models, which assume fixed attributes of partnerships, such as count and duration, may not adequately capture the effects of partnerships on STI transmission. In contrast, agent-based dynamic network models offer a flexible framework for incorpor...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 193 papers

- **2026-09-18** — Uchi Uchibeke — [APort Vault: Benchmarking AI Agent Payment Authorization with the Open Agent Passport](http://arxiv.org/abs/2609.22076v1)
  <details><summary>📄 Abstract</summary>
  APort Vault is a benchmark for payment authorization in tool-using AI agents. It replays 4,371 attacks written by humans against a live payment agent during a public capture-the-flag event, across 14 models from 8 labs, five policy configurations and two replay tracks, with and without a deterministic pre-action check implementing the Open Agent Passport (OAP) specification. 225,964 evaluations completed. We report five distinct events per evaluation, because collapsing them is how an agent benc...
  </details>

- **2026-09-18** — Wenquan Zhou, An Wang, Jing Liang et al. — [CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices](http://arxiv.org/abs/2609.21344v1)
  <details><summary>📄 Abstract</summary>
  For Internet of Things (IoT) devices, a secure algorithm alone is not enough: an attacker with physical access can attack the implementation directly, and its flaws are hard to fix once deployed. Large language models (LLMs) are now used to build and analyze such implementations. LLM benchmarks exist for cryptography and general cybersecurity, but none covers cryptographic engineering. In this paper, we present CESBench, 380 expert-written items across six sub-domains of cryptographic engineerin...
  </details>

- **2026-09-18** — Haoyu Zhou, Joe Watson, Anson Lei et al. — [Benchmarking World Models for Continual Learning on Compositional Tasks](http://arxiv.org/abs/2609.22055v1)
  <details><summary>📄 Abstract</summary>
  A desirable property of a world model is the ability to learn continually across tasks, adapting to new environments without forgetting what the agent has already learnt. In particular, the ability to retain and reuse knowledge obtained from prior experiences underpins an agent's ability to efficiently adapt to novel environments, as the dynamics of the physical world can often be described in recurring mechanisms. However, the world model's measure of adaptation entangles two abilities: the spe...
  </details>

- **2026-09-18** — Camilo Carvajal Reyes, Felipe Tobar — [Time series generation with spectrally aligned latent flow matching](http://arxiv.org/abs/2609.21989v1)
  <details><summary>📄 Abstract</summary>
  Latent flow models have proven to be a reliable and cost-effective method for time series generation. However, the latent compression induces unwanted artefacts, such as a spectral mismatch with respect to the underlying dataset, thus hindering their use as training surrogates. In this article, we propose a spectrally-aligned latent-flow time series generator, where the latent space for flow matching is trained to preserve dynamical properties that are relevant for the suitability of synthetic s...
  </details>

- **2026-09-18** — Dongyijie Primo Pan, Pan Hui, Mirjana Prpa — [Can I Trust My Body? A Three-Year Autoethnography of ChatGPT's Place in My Support System for Panic Attacks](http://arxiv.org/abs/2609.21925v1)
  <details><summary>📄 Abstract</summary>
  People increasingly seek mental health support from large language models, yet little is known about their use across years of recurrent panic. We present a three-year analytic autoethnography of the first author's ChatGPT use while living with panic disorder, drawing on conversations, personal records, and accounts from friends or family members and professionals. Narrative analysis traces how my questions shaped ChatGPT's roles and how earlier experiences influenced later responses to symptoms...
  </details>

- **2026-09-18** — George Xi Wang, Xiangyu Li, Shaoyue Wen et al. — [Touvigation: Embodied Adaptive Object Acquisition for Blind and Low-Vision Users in Unfamiliar Indoor Environments](http://arxiv.org/abs/2609.21828v1)
  <details><summary>📄 Abstract</summary>
  Blind and low-vision users often face challenges when locating and physically acquiring objects in unfamiliar indoor environments. Existing vision-language-model-based assistants can provide semantic descriptions but may introduce latency, hallucinations, and guidance that is poorly aligned with embodied action. We present Touvigation, a hands-free object acquisition system that combines vision-language understanding with persistent local spatial modeling to provide low-latency, body-relative gu...
  </details>

- **2026-09-18** — Boni Hu, Xiong Wei, Haoming Huang et al. — [ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](http://arxiv.org/abs/2609.21712v1)
  <details><summary>📄 Abstract</summary>
  Generative world models offer controllable and repeatable closed-loop simulation for end-to-end and vision-language-action driving policies, but production deployment exposes three unresolved requirements: faithfully reproducing a mixed fisheye-pinhole rig at native resolutions; reconciling causal, per-timestep interaction with long-horizon stability and low latency; and preserving scene identity when a location is revisited. We present ZYT-World, a single architecture that natively generates fo...
  </details>

- **2026-09-18** — Mahdi Mohammadigohari, Gustau Camps-Valls — [Optimization Geometry of Equivalent Brownian RKHS Representations](http://arxiv.org/abs/2609.21693v1)
  <details><summary>📄 Abstract</summary>
  Equivalent finite parameterizations can represent the same functions and intrinsic norm yet induce different optimization algorithms. We study this effect in a controlled finite Brownian RKHS with nodal, increment, and spectral coordinates. Classical finite-element, RKHS-interpolation, Brownian-covariance, and mixed-boundary DCT identities make the shared hypothesis class, Brownian energy, approximation operator, and coordinate maps explicit. Our main results concern the optimization geometry of...
  </details>

- **2026-09-18** — Ishaan Mahajan, Charles Chen, Frederike Dümbgen et al. — [RAYA: Learning Where and When to Intervene for Robot Recovery](http://arxiv.org/abs/2609.21690v1)
  <details><summary>📄 Abstract</summary>
  A robot can predict failure and still be unable to prevent it. By the time a safety mechanism reacts, the nominal plan may already have spent the control authority that recovery requires, and fixed task priorities may block whatever response remains. Our key insight is that both aspects are decided inside the controller. Recoverability must inform actions while they are chosen rather than veto them afterward, and task objectives must be adapted as recoverability shrinks. Building on this, we pre...
  </details>

- **2026-09-18** — Thomas Ranzenberger, Steffen Freisinger, Tobias Bocklet et al. — [The Spoken Wikipedia Presentation Corpus](http://arxiv.org/abs/2609.21676v1)
  <details><summary>📄 Abstract</summary>
  We present the Spoken Wikipedia Presentation Corpus, an extension of the Spoken Wikipedia Corpora featuring LLM-generated slide decks for multimodal ASR. Slides are created from LLM-segmented sections using a hybrid pipeline that combines LLM-based content planning with rule-based design decisions. For each section, an LLM generates a slide title, bullet points, a takeaway message, and a visual description that is used to create an illustration. Rule-based matching then selects layouts, themes, ...
  </details>

- **2026-09-18** — Xinyu Che, Yunfei Ge, Shihao Li et al. — [GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions](http://arxiv.org/abs/2609.21562v1)
  <details><summary>📄 Abstract</summary>
  Coding agents can modify and test code across large software projects. Game development is a domain where agents must implement gameplay rules. A game can end in a valid state even after violating its rules during the run. Current game-development benchmarks replay fixed examples, score videos, or ask another model to judge the result. However, no existing benchmark checks game rules throughout execution across varied evaluator-selected scenarios while ensuring exactly reproducible verdicts. We ...
  </details>

- **2026-09-18** — Yewen Li, Peng Jiang, Yitian Li et al. — [OneBid: A Unified Auto-Bidding Foundation Model for Diverse oCPX Advertising Scenarios](http://arxiv.org/abs/2609.21550v1)
  <details><summary>📄 Abstract</summary>
  Auto-bidding is central to computational advertising, where strategies must maximize advertisers' conversion value under economic constraints. It has evolved from rule-based controllers to reinforcement learning and generative methods such as Decision Transformer (DT). Yet these methods increasingly mismatch the prevailing optimized cost-per-X (oCPX) paradigm, which spans heterogeneous scenarios (e.g., registration, purchase), each served by a separate model, leading to fragmented pipelines and ...
  </details>

- **2026-09-18** — Zetao Cai, Yaping Li, Yiqun Wang et al. — [Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Manipulation Transfer](http://arxiv.org/abs/2609.21514v1)
  <details><summary>📄 Abstract</summary>
  Robot demonstrations are expensive to collect and often provide limited distributional coverage of task variations. Human videos offer a low-cost source of complementary manipulation experience, but learning from them requires bridging embodiment gaps in visual appearance and action spaces. We introduce Skel-WAM, a world action model that bridges these differences through a unified hand-skeleton motion interface. The key insight is to align human and robot motion through a common hand topology, ...
  </details>

- **2026-09-18** — Jingyu Hu, Shu Yang, Weiru Liu et al. — [LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers](http://arxiv.org/abs/2609.21492v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) reasoning has been shown to improve the performance of large language models (LLMs), yet existing optimization methods largely rely on outcome-based feedback, leaving the logical validity of intermediate reasoning steps largely unverified. To address the gap whereby LLMs arrive at correct final answers through logically flawed intermediate reasoning chains, we propose LogicTrack, a neuro-symbolic framework that audits reasoning trajectories by auto-formalizing each reasoni...
  </details>

- **2026-09-18** — Jiaxing Chen, Hengduo Zou, Yiren Zhao et al. — [Risk-Aware Occupancy for Safety-Oriented End-to-End Autonomous Driving](http://arxiv.org/abs/2609.21470v1)
  <details><summary>📄 Abstract</summary>
  Sparse representation formulates the environment perception for the end-to-end driving system as a set of discrete elements like objects and lane lines. This formulation meets safety risks in crowded, occluded scenes dealing with unstructured obstacles, uncertain regions, and intricate interactions. In this paper, we propose a dense representation, risk-aware occupancy, to characterize planning-relevant risks in an explicit and uniform manner. It jointly encodes global scene occupancy, map-deriv...
  </details>

- **2026-09-18** — Joao P. A. Dantas, Jelton A. Cunha, Gabriel Dietzsch — [Offline Multimodal Large Language Models for Decision Support in Air Operations](http://arxiv.org/abs/2609.21390v1)
  <details><summary>📄 Abstract</summary>
  Air operations rely on complex rules, established procedures, and time-critical analysis under limited connectivity and strict security constraints. In such environments, analysts must combine written doctrine with images, often without access to external computing resources. This paper studies offline large language models as decision support tools, deployed in isolated and restricted environments to give analysts access to doctrinal knowledge that remains traceable to its original sources thro...
  </details>

- **2026-09-18** — Edward Holmberg, Elias Ioup, Mahdi Abdelguerfi — [Knowledge-Graph-Augmented Chronos-2 for HEC-RAS Surrogate Forecasting](http://arxiv.org/abs/2609.21381v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether coupling a time-series foundation model to hydraulic project knowledge improves surrogate forecasting of HEC-RAS water-surface elevation (WSE). We present KG-Chronos-2, which combines a frozen Chronos-2 predictor with exact-state residual decoding, graph-conditioned historical retrieval, and input-aligned correction. We compare the method with persistence, a residual LSTM, project-conditioned recurrent GeoFNO, a hydraulic DCRNN-style model, and frozen Chronos-2. Task-speci...
  </details>

- **2026-09-18** — Hyewon Lee, Ziying Wang, Aiden Moy et al. — [GUIDE: Designer-in-the-loop Authoring of Conformant Generative User Interfaces](http://arxiv.org/abs/2609.21285v1)
  <details><summary>📄 Abstract</summary>
  Generative User Interfaces (GenUIs) enable applications to generate interfaces on demand from user needs and context. Like conventional UIs, they must still reflect designers' intent and conform to requirements such as brand identity. Unlike conventional UIs, designers cannot directly specify or see every interface a GenUI may produce, making design intent harder to enforce. We introduce GUIDE (GenUI Development Environment), a system that lets designers continuously inspect and refine GenUI beh...
  </details>

- **2026-09-18** — Chao Li, Yingying Yu, Yunfeng Li — [How Many Humans Is a Judge Panel Worth?](http://arxiv.org/abs/2609.21277v1)
  <details><summary>📄 Abstract</summary>
  How many human judgments does a panel of language models represent? The answer depends on what is matched. We audit categorical judge panels against empirical human label distributions, retaining disagreement that binary errors relative to one gold label collapse. We measure spectral residual diversity by matching the participation ratio of a normalized residual Gram matrix to conditionally independent human-reference draws, giving nu_H. We separately match distributional squared error, giving n...
  </details>

- **2026-09-18** — Ji-Lun Peng, Yi-Zhen Zhang, Chun-Nan Chou et al. — [From Memory to Behavior: A Behavior-Aware Role-Playing Framework for Social Media Influencers](http://arxiv.org/abs/2609.21349v1)
  <details><summary>📄 Abstract</summary>
  Large language models have shown strong potential as role-playing agents for real individuals, yet faithful impersonating remains challenging. Existing in-context learning-based methods fail to capture how individuals react under different situations. In addition, LLM-based evaluation is difficult for obscure individuals. To address these challenges, we propose Situation--Internal state--Behavior Persona method to incorporate situation-dependent behavioral strategies. We further design an evalua...
  </details>

- **2026-09-18** — Pengjun Niu, Yujia Xie, Rui Peng et al. — [SkelWAM: A Skeleton-Guided World-Action Model for Zero-Shot Cross-Embodiment Manipulation](http://arxiv.org/abs/2609.21983v1)
  <details><summary>📄 Abstract</summary>
  Reusing manipulation experience across robot embodiments is important for scaling robot learning and reducing repeated task-specific data collection. However, changes in embodiment alter visual appearance, action dimensionality and semantics, and the whole-body configurations that can realize the same tool pose. We present SkelWAM, a skeleton-guided world-action model that couples perception and control through one explicit geometric representation for single-source cross-embodiment manipulation...
  </details>

- **2026-09-18** — Bruno N. Y. Chen, Li Kang, Heng Zhou et al. — [MAAP: Multi-Agent Active Perception for Collaborative Manipulation](http://arxiv.org/abs/2609.21929v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent manipulation naturally produces multiple task-driven viewpoints: every arm carries a wrist camera and moves through the scene while acting. Yet these observations are typically underutilized, and active perception in manipulation is still often treated as requiring a dedicated sensing agent. We introduce MAAP (Multi-Agent Active Perception), in which every arm is dual-purpose: it executes manipulation actions and, through the wrist camera it carries, simultaneously serves as a moving...
  </details>

- **2026-09-18** — Lobna Joualy, Eric Demeester, Nikolaos Tsiogkas — [Scaling Vision-Language Reward Learning for Robot Manipulation in Parallel Simulation](http://arxiv.org/abs/2609.21767v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can replace human annotators in preference-based reward learning, but sequential API requests and single-environment data collection make training slow and costly. We present RAPID (Reward learning with Adaptive Parallel Image Diversity), a system that couples GPU-parallel rollout with data-aware policy updates, single-request preference labeling, automatic reward stabilization, and representative image sampling. We evaluate these components on five Franka Panda man...
  </details>

- **2026-09-18** — Hiroaki Kingetsu, Hiroaki Kurihara, Kaoru Yokoo et al. — [SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations](http://arxiv.org/abs/2609.21650v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning Vision-Language-Action (VLA) models commonly relies on human teleoperation demonstrations, while reinforcement learning (RL) with sparse binary rewards faces an exploration challenge when successful trajectories are rarely sampled. We propose SynthDemo-RL, a teacher-student framework in which an automated teacher converts simulator-privileged state into successful manipulation trajectories, a VLA student is distilled from them by supervised fine-tuning (SFT), and PPO with binary task...
  </details>

- **2026-09-18** — Xinyu Liu, Gökhan Solak, Arash Ajoudani — [Potential-Field Action Representation for Reinforcement Learning in Contact-Rich Manipulation](http://arxiv.org/abs/2609.21609v1)
  <details><summary>📄 Abstract</summary>
  Model-free reinforcement learning can acquire contact-rich robotic manipulation skills through trial-and-error interaction, but it often requires the policy to learn both task strategy and low-level motion generation. In this setting, the action representation is critical because it determines how policy outputs are converted into robot motion, shaping both exploration and physical execution. Direct Cartesian command interfaces require the policy to generate motion at every decision step, coupli...
  </details>

- **2026-09-18** — Xiao Wang, Heng Zhang, Gokhan Solak et al. — [FORTE: Task-Adaptive Force Capability Optimization for Mobile Manipulators](http://arxiv.org/abs/2609.21497v1)
  <details><summary>📄 Abstract</summary>
  Effective physical interaction control in robotic manipulation requires not only kinematically feasible motion but also sufficient force-interaction capability. Existing redundancy resolution methods often ignore task-specific force demands or maximize the force capability indiscriminately, sacrificing dexterity when large force margins are unnecessary. We propose a task-oriented force capability optimization framework for redundant mobile manipulators. A Vision-Language Model (VLM) infers objec...
  </details>

- **2026-09-18** — Xuancheng Zhang, Xuetao Liu, Qianying Tang et al. — [ME-Dex 1.0: Bringing Heterogeneous Tactile Sensing into World Action Modeling](http://arxiv.org/abs/2609.21449v1)
  <details><summary>📄 Abstract</summary>
  World Action Models bring the predictive capabilities of video models into robot action generation, providing a rich foundation for modeling future visual states. Tactile sensing complements this foundation with direct measurements of physical interaction. Some existing methods use tactile features as conditioning inputs without jointly predicting future tactile states, visual observations, and actions. Our key insight is that tactile signals, like video, provide observations of the evolving wor...
  </details>

- **2026-09-18** — Vinicius Ferraz, Leon Houf — [People escalate against a competitor labelled human and hold back against one labelled an optimising machine](http://arxiv.org/abs/2609.21439v1)
  <details><summary>📄 Abstract</summary>
  People increasingly compete against AI agents rather than other human opponents. We distinguish two channels: an opponent effect and an information effect. These are different elements with different consequences: the opponent effect is specific to a given computational system, the information effect a property of the information environment that an organisation or policymaker can control. We separate them in a preregistered experiment (N = 1,395) using a dynamic all-pay auction, a repeated cont...
  </details>

- **2026-09-18** — Arjun Krishna, Vincent Pacelli, Dinesh Jayaraman — [LEMCA: LLM-Guided Synthesis of Efficient Mode-Switching Control Architectures](http://arxiv.org/abs/2609.21319v1)
  <details><summary>📄 Abstract</summary>
  Physical control tasks in the natural world, such as driving or object manipulation, frequently exhibit dramatic variations in sensory and compute complexity over time. Correspondingly, a natural resource-efficient choice for robot control is to dynamically switch between control modes with varying resource allocations. However, such "mode-switching controllers" (MSCs) have historically required laborious, expert-driven design and synthesis for each new task. Driven by these design difficulties,...
  </details>

- **2026-09-18** — Andre Bacellar — [Predictable Failure in Multi-Hop Retrieval: Score-Distributional Confidence Scoring and Abstention](http://arxiv.org/abs/2609.22056v1)
  <details><summary>📄 Abstract</summary>
  Multi-hop retrieval failures are not uniformly distributed across queries: they cluster in structurally predictable subpopulations. We prove two results formalizing this structure. First (CWAR Reducibility): confident-failure reduction is achievable if and only if retrieval features carry mutual information about success, a condition satisfied by LLM-judge pipelines but substantially weaker in dense-only settings, explaining the AUC-AC gap between regimes. Second (Feature Regime Complementarity)...
  </details>

- **2026-09-18** — Richard Zhe Wang — [Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention](http://arxiv.org/abs/2609.22005v1)
  <details><summary>📄 Abstract</summary>
  Gating the value pathway of attention reportedly improves language model pretraining, and prior studies disagree on why. We argue and provide experimental evidence that such gates supply two different things that softmax attention lacks: abstention and noise filtering. The first is abstention, which allows an attention head to output nothing, bypassing the requirement that attention weights must sum to one. The second is noise filtering, which allows the value pathway of an attention head to sup...
  </details>

- **2026-09-18** — Sayak Mukherjee, Kyung-Bin Kwon, Ramij R. Hossain et al. — [Learning-Based Augmentation and Adaptation for Grid Sim-to-Real Model Discrepancy](http://arxiv.org/abs/2609.21986v1)
  <details><summary>📄 Abstract</summary>
  Modern power systems can encounter increased discrepancy between the operators' simulation model and the actual true dynamics of the grid, driven by uncertainties caused by integration of new inverter-based resources (IBRs), large loads, unmodeled dynamics, parameter drifts, etc., to name a few. All of these impact the control room operations, where some critical oscillations may not be captured during the transient studies. To circumvent these issues, we propose a learning-augmented hybrid appr...
  </details>

- **2026-09-18** — Merwan Barlier, Blaz Skrlj — [LLMs as Feature Engineers for Text-and-Tabular Prediction](http://arxiv.org/abs/2609.21894v1)
  <details><summary>📄 Abstract</summary>
  We introduce an iterative framework that automates the extraction of interpretable, schema-bound categorical features from unstructured text for tabular prediction models. To navigate the feature space, a generator LLM proposes semantic definitions, a separate extractor LLM materializes the features, and a downstream tabular model evaluates their predictive performance. We optimize this search by translating explicit model errors, such as AUC ranking inversions, into natural-language feedback, s...
  </details>

- **2026-09-18** — Pierre Beckmann, Matthieu Queloz, Andre Freitas — [World Modeling in Transformers](http://arxiv.org/abs/2609.21748v1)
  <details><summary>📄 Abstract</summary>
  Behavioral failures can make a transformer appear to lack a world model even when it has learned faithful representations of its environment. We demonstrate this in TaxiGPT, a transformer trained on random walks through Manhattan whose failures have been interpreted as evidence of an incoherent internal map. Through mechanistic analysis and causal interventions, we show that the model represents intersections and streets, tracks its position, and uses a goal compass to navigate. We trace its fai...
  </details>

- **2026-09-18** — Kaiming Shen, Kareem M. Attiah, Yannan Chen et al. — [Connections Between Quadratic Transform for Fractional Programming and Schur Complement](http://arxiv.org/abs/2609.21730v1)
  <details><summary>📄 Abstract</summary>
  This paper shows that there are intimate connections between the quadratic transform technique for solving fractional programming (FP) problems and the Schur-complement technique in matrix analysis. We demonstrate that the quadratic transform technique is related to two aspects of the Schur complement: (i) the linear matrix inequality (LMI) condition for positive semidefiniteness and (ii) the matrix determinant formula. Specifically, we establish that the quadratic transform and the Schur-comple...
  </details>

- **2026-09-18** — Muhammad Ahsan Mustafa, Yasheerah Yaqoot, Faryal Batool et al. — [AgenticSwarm: Semantic Perception and Adaptive Task Allocation for Heterogeneous Multi-UAV Missions](http://arxiv.org/abs/2609.21716v1)
  <details><summary>📄 Abstract</summary>
  Multi UAV missions in complex environments require the system to understand both the surrounding scene and the intent of a human operator while maintaining feasible task allocation as mission conditions change. This paper presents AgenticSwarm, an agentic framework for semantic perception and adaptive task allocation in heterogeneous multi UAV missions. An agent interprets aerial imagery and natural language instructions to construct a grounded mission representation that links perceived objects...
  </details>

- **2026-09-18** — Hritika Sharma, Thibault Bañeras-Roux, Alessandra Pinto et al. — [Rethinking Human-Aligned Evaluation: An Analysis of Semantic Metrics Beyond WER](http://arxiv.org/abs/2609.21663v1)
  <details><summary>📄 Abstract</summary>
  Word Error Rate (WER), the most commonly used metric for Automatic Speech Recognition (ASR), treats every lexical deviation from the reference as equally costly, regardless of whether it changes meaning. This raises the question: does WER actually track how humans judge ASR transcript quality? We introduce HATS-en, an English dataset for human-centered ASR evaluation. Using this dataset, we benchmark lexical metrics against several configurations of BERTScore and SemDist, varying the language mo...
  </details>

- **2026-09-18** — Musa Rochi, Marcel Schubert, Christoph Gebhardt — [Learned Parametric Emotion Editing: Real-Time Affective Filtering for On-Device Social Media Video](http://arxiv.org/abs/2609.21624v1)
  <details><summary>📄 Abstract</summary>
  Problematic internet use affects a growing share of the population, yet common interventions, e.g., time limits, blocking, forced breaks, are coercive and easily circumvented. We explore a less restrictive alternative: adapting the emotional intensity of visual content. Prior work has shown that optimization can steer an image's affective content, but its per-image optimization cost makes it impractical for real-time deployment. We instead learn a model that predicts this transformation in a sin...
  </details>

- **2026-09-18** — Marco Pagni, Robin Engler, Frederic Burdet et al. — [kgsteward: a tool for building, reproducing and maintaining distributed knowledge graphs](http://arxiv.org/abs/2609.21564v1)
  <details><summary>📄 Abstract</summary>
  Collaborative research projects in life sciences increasingly need to integrate private, embargoed consortium data with public reference databases in order to reach statistically meaningful interpretations. The Resource Description Framework (RDF) is well suited to this task: it facilitates the integration of heterogeneous data sources, and allows researchers to keep data and their documentation as metadata in the same place, provided the knowledge graph itself remains private during the time co...
  </details>

- **2026-09-18** — Alexandru Ilovan — [Cross-Platform vs Native Mobile Development: An Empirical Study of Software Quality Trade-offs](http://arxiv.org/abs/2609.21544v1)
  <details><summary>📄 Abstract</summary>
  Cross-platform mobile frameworks promise code reuse, shorter delivery cycles, and lower implementation effort, but their trade-offs relative to native development remain difficult to assess objectively. Many comparisons rely on simplified applications, inconsistent feature sets, or a narrow set of metrics. This paper compares five implementations of the same plant-management application: native iOS, native Android, Flutter, React Native, and Kotlin Multiplatform. The shared approaches target bot...
  </details>

- **2026-09-18** — Jie Shao, Shengkai Hu, Xu Zhang et al. — [SkillIR: Evolving Scene-Aware Skills for Agentic Image Restoration](http://arxiv.org/abs/2609.21468v1)
  <details><summary>📄 Abstract</summary>
  This paper studies agentic image restoration, in which multimodal agents coordinate specialized restoration tools to recover images affected by complex degradations. Existing restoration agents often derive complete tool-use plans from the original degraded image or retrieve previously successful trajectories, providing limited support for adapting individual actions to evolving intermediate restoration states. We find that accepted tool executions can change the residual degradation state and, ...
  </details>

- **2026-09-18** — Yamato Narita, Issei Sato — [Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals](http://arxiv.org/abs/2609.21450v1)
  <details><summary>📄 Abstract</summary>
  Post-training weight-activation quantization reduces the memory and inference costs of large language models, but aggressive W4A4 quantization remains difficult because activation outliers degrade effective quantization resolution. Although weight optimization, channel-wise scaling, and orthogonal rotation mitigate this problem, the error components they address and their relationship remain unclear. Using an exact decomposition of local weight-activation quantization error into an activation-gu...
  </details>

- **2026-09-18** — Kaichen Zhang, Yuzhong Hong, Junwei Bao et al. — [GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation](http://arxiv.org/abs/2609.21432v1)
  <details><summary>📄 Abstract</summary>
  Post-training plays a pivotal role in enhancing the reasoning capabilities and task-specific expertise of large language models (LLMs). Despite recent advances in post-training methods, such as Group Relative Policy Optimization (GRPO), their practical deployment remains impeded by training instability arising from the reliance on importance sampling.   We introduce Group Variance Policy Optimization (GVPO), a novel post-training method that integrates the analytical solution of KL-constrained r...
  </details>

- **2026-09-18** — Xinyue Luo, Fei Yu — [Prediction Dynamics in Depth-Recurrent Language Models](http://arxiv.org/abs/2609.21383v1)
  <details><summary>📄 Abstract</summary>
  Depth-recurrent language models refine predictions through repeated latent updates. Why can intermediate answers agree with the endpoint while their scores continue to change? We derive a sharp margin characterization that decomposes the conservatism of a magnitude bound into common translation, direction relative to the winner, and the pairing of each competitor's update with its score gap. Across Huginn-3.5B and Ouro-1.4B, accounting for update direction and competitor pairing reduces the mean...
  </details>

- **2026-09-18** — Cevheri Bozoglan, Yusuf Gundogdu, Abdullah Kaya et al. — [What Stops a Small Language Model From Driving a Database Agent](http://arxiv.org/abs/2609.21341v1)
  <details><summary>📄 Abstract</summary>
  Small open-weight language models are assumed to fail at agentic database work because they lack the reasoning capacity for it. We test that against a production system. Over eleven days we drove the agent mode of an open-source SQL client with 39 open-weight models served locally and one hosted control, across six task surfaces: 8,199 runs, 110,711 ledger events, 14,008 refused tool calls. Of the 2,100 model-attributed agent-mode losses, 1,590, or 75.7%, came from runs that had invoked at least...
  </details>

- **2026-09-18** — Jiale Zhang, Michael Larionov, Zichong Wang et al. — [FairLMs: A Turnkey Library for Fairness in Language Models](http://arxiv.org/abs/2609.21296v1)
  <details><summary>📄 Abstract</summary>
  Fairness research on language models involves measuring bias, applying mitigation methods, and examining the evidence on which an evaluation rests. Existing tools offer complementary functionality through different interfaces, so combining them requires reconciling model interfaces, evidence formats, access constraints, and result types before applicability can be checked or methods compared. We introduce \textbf{FairLMs}, a Python library that connects these activities through explicit declarat...
  </details>

- **2026-09-18** — Erwei Wang, Ephrem Wu, Victor J. B. Jung et al. — [Programming AMD XDNA NPUs with Open-source Compiler Tools: A FlashAttention Case Study](http://arxiv.org/abs/2609.21264v1)
  <details><summary>📄 Abstract</summary>
  Spatial NPUs such as AMD XDNA place compute tiles beside small local memories and leave data movement between them to software. Mapping a multi-stage workload onto such a device is largely a question of where the intermediate tensors live. We report what we learned making those choices for FlashAttention with the open-source IRON and MLIR-AIR flows.   We compare four reference designs on XDNA 1 and XDNA 2: one runs each operator separately, two stream between operators on chip, and one fuses all...
  </details>

- **2026-09-18** — Hao Fu, Baiting Zhu, Minglei Chen et al. — [Verify, Don't Trust: Agentic Model Development for Video Discovery Retrieval at Scale](http://arxiv.org/abs/2609.21257v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can propose, implement, and evaluate model changes. Autoresearch loops demonstrate this capability through minutes-scale iterations on a self-contained program. Online autoresearch instead spans asynchronous systems, hours-long variants, and weeks-long campaigns that can influence a product. A completed run can still support an invalid conclusion when a code change is a no-op, data windows leak, evaluator semantics drift, or the two arms traverse different servi...
  </details>

- **2026-09-17** — Ruichen Tan, Zengxiang Lei, Satish Ukkusuri — [Worst-Case Hidden-Vehicle Trajectory Search in Spatiotemporal Occlusion Regions](http://arxiv.org/abs/2609.20480v1)
  <details><summary>📄 Abstract</summary>
  Occlusion creates fundamental uncertainty in autonomous driving. Existing methods often propagate frame-wise hypotheses or optimize ego behavior against prescribed hidden-agent predictions, leaving the worst history-consistent interaction unexplored. We introduce History-Conditioned Minimax Trajectory Search (HC-MTS), which combines temporal occlusion reasoning with response-aware search. First, HC-MTS constructs finite hidden-state modes, each certified by a backward witness satisfying multi-fr...
  </details>

- **2026-09-17** — Yin Wu, Jiarong Wei, Carl Esselborn et al. — [Safety-Critical Scenanrio Emerges from Initial Scene](http://arxiv.org/abs/2609.20103v1)
  <details><summary>📄 Abstract</summary>
  Safety-critical driving scenario generation has largely focused on manipulating the behavior of surrounding agents while starting from an initial scene from driving data. This assumption can limit the space of discoverable failures, since driving data can provide little opportunity for meaningful interaction. For example, in the Waymo Open Motion Dataset, 20.44% of recorded slices feature a stationary ego vehicle that never moves, and 30.39% of initial frames contain no nearby traffic participan...
  </details>

- **2026-09-17** — Damiano Da Col, Maximilian Igl, Peter Karkus et al. — [OPTED: On-Policy Fine-Tuning for End-to-End Driving using a Render-Free Teacher](http://arxiv.org/abs/2609.20756v1)
  <details><summary>📄 Abstract</summary>
  As scaling pre-training data alone yields diminishing returns, post-training is becoming increasingly important across physical AI domains such as autonomous driving. End-to-end driving policies are pre-trained in open loop with behavior cloning on human demonstrations. However, compounding errors during closed-loop deployment can take the vehicle outside the training data distribution, increasing the risk of safety-critical incidents. Closed-loop post-training can mitigate this risk but require...
  </details>

- **2026-09-17** — Ö. D. Gürcan, L. Manfredini, P. Morel — [Solutions of the Navier-Stokes Equation Through Affine Transformations: The Triad Triplet](http://arxiv.org/abs/2609.20710v1)
  <details><summary>📄 Abstract</summary>
  Considering triads in helical decomposition of three dimensional Navier-Stokes turbulence, three consecutive triads of the same shape and class, where the reference wave-number appears as the smallest, the middle and the largest wave-numbers respectively, constitutes an interesting object called the triad triplet that allows tracing the local transfer in wave-number space due to a given shape and class of triads. It is shown that, evolution equations for the triad triplet can be obtained from th...
  </details>

- **2026-09-17** — XiuYu Zhang, Wei Chow, Junfeng Fang et al. — [What Does Privileged Information Add to On-Policy Self-Distillation?](http://arxiv.org/abs/2609.20612v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) lets a language model learn from a frozen copy of itself that sees an answer or a worked solution. Giving the teacher this extra information seems to offer the student more to learn, but how much does it add beyond distillation itself? To isolate that contribution, we construct AMPLE-Math, a reusable suite of 5,319 mathematical problems with six reasoning views that share the same answer, and compare each view with matched reference-free distillation. With a th...
  </details>

- **2026-09-17** — Zimu Wang, Yiwen Jiang, Xiangyu Zhao et al. — [Steering the Compass: Aligning Dynamic Psychological Counseling Conversations with Cognitive Behavioral Therapy Strategies](http://arxiv.org/abs/2609.20565v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in large language models have revolutionized the field of psychological counseling, especially in the context of Cognitive Behavioral Therapy (CBT). While the success of CBT relies heavily on dynamic decision-making informed by the client's real-time mental state, this aspect has often been overlooked in current research, limiting both flexibility and therapeutic outcomes. In this paper, we introduce StratCBT, a dataset specifically designed for psychological counseling conve...
  </details>

- **2026-09-17** — Haozhe Liu, Tian Ye, Sensen Gao et al. — [SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](http://arxiv.org/abs/2609.20519v1)
  <details><summary>📄 Abstract</summary>
  As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired approach at the harness layer, scaling auto-research loops across increasingly numerous and diverse environments for harness rollouts. At this scale, the process yields reusable improvem...
  </details>

- **2026-09-17** — Yukun Zhang, Kemu Xu, Yishen Chen — [How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful LLM Agents](http://arxiv.org/abs/2609.20474v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses supply planning guidance, organize execution, and check completion. We study how these components affect success, erroneous acceptance, and cost in two Retail experiments and an Airline pilot in $τ^2$-bench. The primary comparison pairs prewritten task-specific plans (Fixed) with shuffled policy text matched in word count (Sham), isolating the contribution of guidance content. Across 265 matched cells, Fixed improves oracle-verified success by 7.17 percentage points (90\% task-cl...
  </details>

- **2026-09-17** — Yukun Zhang, Kemu Xu, Yishen Chen — [Welfare-Opaque Income: Taxation under AI-Agent Delegation](http://arxiv.org/abs/2609.20425v1)
  <details><summary>📄 Abstract</summary>
  We study income taxation when an AI agent implements economically relevant choices through a rule hidden from the government. Alongside unobserved productive ability, this hidden preference-to-execution mapping creates \emph{double unobservability}: the same observable tax-base response can carry different welfare consequences. We call the resulting income \emph{welfare-opaque}. Our constructions show that tax-base statistics can coincide while reform welfare effects differ, even when mechanical...
  </details>

- **2026-09-17** — Qing Xu, Yixuan Zhang, Yue Li et al. — [FreqDINO++: A Frequency-Guided Multi-Task Routing Vision Foundation Model for Universal Ultrasound Analysis](http://arxiv.org/abs/2609.20340v1)
  <details><summary>📄 Abstract</summary>
  Ultrasound image analysis plays a crucial role in cancer screening and prenatal diagnosis, yet comprehensive assessment requires jointly addressing tasks such as lesion segmentation and benign-malignant classification. While recent vision foundation models have shown remarkable universal representations, unlocking their potential for ultrasound is bottlenecked by the considerable domain gap from natural images. Existing methods typically fine-tune heavy vision encoders for isolated tasks, incurr...
  </details>

- **2026-09-17** — Pritish Mishra, Ishaan Kumar, Akshat Mandoli et al. — [MTVA-Bench: Evaluating the Language Model Inside Cascaded Voice Agents](http://arxiv.org/abs/2609.20152v1)
  <details><summary>📄 Abstract</summary>
  Generally, most voice agents are cascaded systems, i.e., an ASR model transcribes the caller's audio, a language model reads the transcript and decides what to say and which backend tools to call, and a TTS model speaks the reply. Nearly all of the decision making happens in the language model, but existing evaluations measure it either too broadly or too narrowly. End-to-end voice benchmarks score the full pipeline, so recognition errors and model errors mix into a single number. LLM benchmarks...
  </details>

- **2026-09-17** — Zifan Guan, Longyu Lu, Junan Zhang et al. — [Multi-Dimensional Prosody Judgment For Live Streaming Speech Synthesis](http://arxiv.org/abs/2609.20124v1)
  <details><summary>📄 Abstract</summary>
  Evaluating live streaming speech synthesis (TTS) requires assessing fine-grained, highly expressive prosody such as emotion, intonation, and energy which traditional MOS predictors fail to capture. While proprietary Large Language Models (LLMs) like Gemini can evaluate these aspects, they are too costly for massive inference and reinforcement learning feedback. To address this, we first introduce Live-ProsodyJudge (LPJ), a cost-effective pairwise evaluator distilled from Gemini into Qwen3-Omni. ...
  </details>

- **2026-09-17** — Yuang Tu, Runjia Tan, Yujie Yan et al. — [AnyviewMeter: Adapting Robotic Reward Models with Camera Geometry and Multi-View Attention](http://arxiv.org/abs/2609.20106v1)
  <details><summary>📄 Abstract</summary>
  Robotic reward models evaluate task execution from visual observations, but their predictions can change with camera viewpoint and occlusion even when the underlying task state is unchanged. Adapting a pretrained reward model to a local task therefore requires accounting for how that task is observed. We introduce AnyviewMeter, a geometry-conditioned adaptation framework for robotic reward models that represent task progress as a scalar reward signal. It combines low-rank fine-tuning with token-...
  </details>

- **2026-09-17** — Xin Zhou, Cong Miao — [Astronex-World 1.0: Real-Time Interactive World Model Foundation](http://arxiv.org/abs/2609.20034v1)
  <details><summary>📄 Abstract</summary>
  We present Astronex-World 1.0, an open controllable video world-model foundation. Given a text prompt (text-to-video) or an initial observation (image-to-video), the model predicts future visual states under frame-aligned camera trajectories, continuous actions, and an embodiment identifier, and accepts text events inserted at a specified position of a rollout. The family provides a bidirectional model for full-context generation and a causal model with block-causal attention and cross-block KV ...
  </details>

- **2026-09-17** — Faiz Ghifari Haznitrama, Alice Oh — [Evaluating Communicative Success in Machine-Translated Conversation](http://arxiv.org/abs/2609.19885v1)
  <details><summary>📄 Abstract</summary>
  Interpreter agents built on machine translation (MT) increasingly mediate live conversation between people who do not share a language, yet we still evaluate them with metrics built for isolated sentences, which measure fidelity rather than whether communication succeeds. We introduce a reusable three-layer checklist-and-judge framework that evaluates interpreter-mediated conversation across semantic, pragmatic, and cultural-social dimensions, covering the naturalness, intent, and social appropr...
  </details>

- **2026-09-17** — Pyrros Koussios, Benjamin Jäger, John Hua Yao et al. — [PetriBench: Benchmarking LLM Reasoning over Dynamic State Spaces](http://arxiv.org/abs/2609.19883v1)
  <details><summary>📄 Abstract</summary>
  Characterizing LLM reasoning remains an open challenge, as many existing benchmarks isolate specific reasoning skills, rely on external knowledge, or are costly to extend. We introduce PetriBench, a compact, fully self-contained, and scalable benchmark for evaluating LLM reasoning over dynamic state spaces using Petri nets, a mature formalism for modeling real-world concurrent and distributed systems. PetriBench organizes reasoning into four task families varying by scope and temporal horizon, w...
  </details>

- **2026-09-17** — Zhiyun Jiang, Hanyong Wang, Binbin Liang et al. — [Absence is Presence: Understanding Visual Scene Negative Events Under Safety Cognitive Constraint](http://arxiv.org/abs/2609.19812v1)
  <details><summary>📄 Abstract</summary>
  Traditional scene understanding focuses on affirmative information objectively present in images. However, in safety-critical domains, comprehending key information that should exist but is actually absent is vital for risk mitigation. To bridge this gap, we focus on visual scene negative captioning with safety as the cognitive constraint. The core challenge is to convert physical absence into semantic negative events. Existing vision-language models (VLMs) struggle with this process because aff...
  </details>

- **2026-09-17** — Yalin Zhang, Zhongxin Liu, Zengqiang Chen — [Design of Economic Dispatch Schemes of An Isolated BESS Network Based on Distributed Discrete-time PI+Rest Consensus](http://arxiv.org/abs/2609.19804v1)
  <details><summary>📄 Abstract</summary>
  Battery energy storage systems (BESSs) are widely integrated into smart grids. For an isolated BESS network, however, capacity degradation and power loss of battery units increase operating costs. To alleviate this problem, two distributed economic dispatch (ED) schemes with discrete-time dynamics are developed in this paper, thus obtaining the optimal output power vector and ensuring supply-demand balance while considering dynamic line loss and capacity constraints. It is worth mentioning that ...
  </details>

- **2026-09-17** — Zhiyun Jiang, Hanyong Wang, Binbin Liang et al. — [Benchmarking MLLMs via Cognitive Expected Scene Graph for Safety-Critical Visual Negation Understanding](http://arxiv.org/abs/2609.19767v1)
  <details><summary>📄 Abstract</summary>
  True machine intelligence requires transcending passive pixel registration to master top-down functional reasoning over absent information via visual negation understanding. However, unconstrained visual negation paradigms remain overly open-ended, and pervasive affirmation bias causes both existing Multi-Modal Large Language Models (MLLMs) and evaluation metrics to fail under negative semantics. To solve these intertwined challenges systematically, we first anchor the boundaries of negation rea...
  </details>

- **2026-09-17** — Yinuo Zhang, Bingshuo Liu, Zhiying Tu et al. — [Scientific Image Quality Assessment via Multi-modal Retrieval-Augmented Generation](http://arxiv.org/abs/2609.19634v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a Retrieval-Augmented Generation (RAG) framework for scientific image quality assessment, designed to simultaneously address both the understanding track (SIQA-U) and the scoring track (SIQA-S) of the SIQA challenge. We construct a multimodal index that integrates textual semantics with fine-grained visual features, and develop a multi-route retrieval and fusion mechanism to provide large language models with highly relevant reference cases, thereby enhancing their capability...
  </details>

- **2026-09-17** — Weiyuan Zhang, Qi Zhang, Hui Huang — [Instance Segmentation and Fine-grained Classification for Urban Buildings with Adaptive Region Dividing and Spatially-Supervised Contrastive Learning](http://arxiv.org/abs/2609.19631v1)
  <details><summary>📄 Abstract</summary>
  Accurate instance-level and functional understanding of urban buildings in large-scale point clouds is essential for digital city modeling and urban analysis. However, the extensive spatial coverage of urban scenes leads most existing methods to rely on predefined blocks for training and evaluation, although such partitions are rarely available in real-world applications and introduce additional preprocessing while fragmenting complete building structures. To address this issue, we propose an ad...
  </details>

- **2026-09-17** — Tisha Chawla, Susheem Koul — [Chronicle: Cut-Point Replay for Regression Testing of LLM Agents](http://arxiv.org/abs/2609.20625v1)
  <details><summary>📄 Abstract</summary>
  Large language model responses are non-deterministic, so failures in LLM agents are hard to reproduce: a failure depends on inference that is not bitwise reproducible, on tools that read changing state, and on a multi-step trajectory that a re-run rarely repeats. Record-and-replay makes a run reproducible, but existing agent tooling records runs only to trace or score them, not to test a code change against them. We present Chronicle, which records an agent run at its non-deterministic boundarie...
  </details>

- **2026-09-17** — Antareep Singha, Shivaram Kumar, Yoonwoo Kim et al. — [Imagine-TAMP: Imagination-Guided Task and Motion Planning in Partial Observability](http://arxiv.org/abs/2609.20396v1)
  <details><summary>📄 Abstract</summary>
  Robots operating in cluttered environments must often manipulate objects whose locations are only partially observable. A central challenge is deciding whether to acquire another observation or to first manipulate objects that may occlude the target. Conventional task and motion planning (TAMP) approaches typically make this decision using symbolic action costs or expensive geometric planning, neither of which adequately captures how likely an observation is to reveal an occluded target. We intr...
  </details>

- **2026-09-17** — Loan Bernat, Matthieu Grard, Ariane Herbulot et al. — [MAGMA-GEN: Validated Recovery Supervision from Ambiguous Failures via Counterfactual Re-Execution](http://arxiv.org/abs/2609.20056v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical robotic systems executing long-horizon manipulation tasks must make high-level semantic decisions that orchestrate stochastic low-level skills. In this setting, failed rollouts are ambiguous: a poor downstream state may reflect an invalid high-level decision, partial observation, or a valid decision whose physical execution failed. Traditional supervised learning lacks data for such recovery states, while reinforcement learning struggles with sparse rewards and non-local credit assi...
  </details>

- **2026-09-17** — Harsha Guda, Adrià Colomé, Carme Torras — [Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation](http://arxiv.org/abs/2609.19976v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action models tell a robot where to move, but not how hard to push. Contact-rich tasks depend on that second quantity, compliance, yet no widely used demonstration interface records it. The obstacle is identifiability as realized pose and measured force cannot separate the operator's intended equilibrium from their stiffness, so VR controllers, SpaceMouse and handheld grippers cannot supply compliance supervision even in principle. Prior compliance-output policies work around thi...
  </details>

- **2026-09-17** — Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang et al. — [Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning](http://arxiv.org/abs/2609.19878v1)
  <details><summary>📄 Abstract</summary>
  Multimodal reasoning requires models to draw on information from multiple modalities throughout the reasoning process. Yet existing methods often concatenate modality-specific thought tokens in a single sequence, leaving the model to bridge representational differences as it reasons across modalities. We introduce Uni-LaDiR (Unified Latent Diffusion Reasoner), a framework that brings these thoughts into a shared latent space for reasoning. A unified encoder maps teacher reasoning steps from diff...
  </details>

- **2026-09-17** — Caoliwen Wang, Mengdi Wang, Heng Zhang et al. — [WorldContact: A Contact-Centric World Model for Scalable Robot Learning](http://arxiv.org/abs/2609.19600v1)
  <details><summary>📄 Abstract</summary>
  Adapting robots to new objects and tasks requires interaction experience that can be costly to obtain. We present WorldContact, a contact-centric world model for deformable-object manipulation, constructed from a limited set of high-quality trajectories to generate additional training data efficiently. It predicts object dynamics using larger time steps than the source numerical simulator, which requires small integration steps to resolve rapid motion and prevent interpenetration. We evaluate Wo...
  </details>

- **2026-09-17** — Chiyoung Kim, Sanghyuk Roy Choi, Minhyeok Lee — [Recovering Aggressively Pruned Vision-Language-Action Models with Offline Hidden-State Distillation](http://arxiv.org/abs/2609.19579v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models let robots follow language instructions, but their language backbones of several billion parameters are the main obstacle to running them on robot hardware. Structured pruning reduces that backbone, and removing 63% of it from OpenVLA-OFT drops LIBERO-Long success from 93.2% to 0.8%. A recent approach restores such a model with supervised fine-tuning followed by reinforcement learning, which needs online rollouts and hundreds of GPU-hours. We recover most of t...
  </details>

- **2026-09-17** — Martin Marek, Max Ryabinin — [Score Centering Stabilizes Off-policy Reinforcement Learning](http://arxiv.org/abs/2609.20807v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) of large language models is notoriously sensitive to small differences between training and inference engines, often referred to as the training-inference mismatch (TIM). However, completely eliminating TIM is impractical, as it would come at a major cost to rollout efficiency. In this paper, we show that the instability of RL under TIM is primarily caused by drift: a persistent bias between training and inference engines that accumulates with every training step. We ...
  </details>

- **2026-09-17** — Run-Ze Fan, Zihao Zhang, Simin Ma et al. — [An Empirical Study of Harness Design for Coding Agents](http://arxiv.org/abs/2609.20804v1)
  <details><summary>📄 Abstract</summary>
  Coding harnesses shape how autonomous coding agents translate model capabilities into long-horizon software-engineering performance, yet existing work typically evaluates harnesses as monolithic systems, leaving the effectiveness of individual components unclear. To enable component-level comparisons, we study this question with a lightweight coding harness whose execution loop is fixed while three components are varied: planning, action space, and context management. Across four models evaluate...
  </details>

- **2026-09-17** — Tica Lin, Deepak Chandran, Gauri Jagatap et al. — [Semantic Action Graph: A Shared Representation for Agent Grounding and Human Interpretation of Sports Highlights](http://arxiv.org/abs/2609.20768v1)
  <details><summary>📄 Abstract</summary>
  Generative agents are increasingly used to select and narrate video highlights, but they typically operate over unstructured or frame-level representations. Their output is consequently difficult for a viewer to verify and steer toward individual preferences. We present the semantic action graph, a lightweight domain schema that represents a sports match as performer, action, recipient, moment, and state nodes connected by role, temporal, and outcome edges. The schema demonstrates three key prop...
  </details>

- **2026-09-17** — Zofia Smoleń — [Q&A on Any Spreadsheet Requires Interpreting Its Grid Structure](http://arxiv.org/abs/2609.20732v1)
  <details><summary>📄 Abstract</summary>
  Semantic cell annotation improves chunking interpretability for spreadsheets in LLM-driven RAG systems, aiding answer generation through enriched context rather than improved retrieval accuracy. We propose a novel framework of splitting any spreadsheet into interpretable chunks using cell role annotation. Our framework beats the state of the art, yet it faces a hard ceiling. Spreadsheets are fundamentally two-dimensional unstructured data with continuous relationships and infinite potential cell...
  </details>

- **2026-09-17** — Faheem Ahmad, Ajan Ahmed, Mst Rumana Sumi et al. — [Synthetic Fingerprints for Children Under Four: Generation and Biometric Evaluation](http://arxiv.org/abs/2609.20621v1)
  <details><summary>📄 Abstract</summary>
  Fingerprint recognition in children under four is of interest for longitudinal identity applications, but research in this age range is constrained by the limited availability and sensitivity of real fingerprint data. Synthetic data may provide a useful complementary resource if generated samples are carefully evaluated for biometric quality, similarity to the real training data, and identity diversity. This paper presents an evaluation and selection protocol for synthetic fingerprints generated...
  </details>

- **2026-09-17** — Ping Tang — [Collective Charge-\(2e\) Bosonic Excitations in Charge-Ordered Systems](http://arxiv.org/abs/2609.20472v1)
  <details><summary>📄 Abstract</summary>
  Charge order is conventionally characterized by a static modulation of the electronic density, while its collective excitations remain less developed from a quasiparticle perspective than those of spin-ordered systems. Here, we formulate the collective excititations of charge order within an effective charge-pseudospin model, in which the charge-ordered ground state is represented by staggered pseudospin order. Quantizing fluctuations around this ordered state via a Holstein--Primakoff transform...
  </details>

- **2026-09-17** — Fabian Schmalstieg, Karsten Mueller, Wojciech Samek — [Cross-Architecture Foundation-Model Distillation for Edge Flood Segmentation](http://arxiv.org/abs/2609.20441v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models can provide strong flood-segmentation performance, but their size limits deployment on memory-constrained edge hardware. We distill a 300-million-parameter Prithvi-EO-2.0 teacher, fine-tuned on the 252 manually labeled Sen1Floods11 training scenes, into a 0.7-million-parameter EfficientViT-B0 student. The teacher supervises additional unlabeled Sentinel-2 imagery, allowing the student training set to grow without new manual annotations. At the matched budget of 252 s...
  </details>

- **2026-09-17** — Abhishek Jaiswal, Zoe Falomir — [A Qualitative Model for Reasoning about Path and Support](http://arxiv.org/abs/2609.20349v1)
  <details><summary>📄 Abstract</summary>
  Spatial reasoning abilities correlate strongly with performance in STEM fields. Games offer a compelling medium for training these critical skills in developing children who have a natural proclivity for play. However, to facilitate human-like tutoring and player guidance, these games require an AI agent capable of making commonsense inferences from spatial events. Qualitative reasoning (QR) models appear to be a suitable framework for these application domains. As these models reason in symboli...
  </details>

- **2026-09-17** — Qingde Li, Qingqi Hong, Zihan Li et al. — [NeuSOGA3D: A Neuro-Symbolic Framework for Explainable 3D Geometric Reconstruction](http://arxiv.org/abs/2609.20323v1)
  <details><summary>📄 Abstract</summary>
  Three-dimensional reconstruction from unorganized point clouds remains a challenging problem in computer vision, geometric modeling, and computer-aided design. While neural implicit methods achieve impressive reconstruction accuracy, geometry is typically encoded in latent representations that limit interpretability and reuse within engineering workflows.   We present NeuSOGA3D (Neuro-Symbolic Geometric Abstraction in 3D), a hybrid framework that combines learned perceptual priors inherited from...
  </details>

- **2026-09-17** — Guangzhao Dai, Qi Wu, Bin Zhu — [GPT-6-Astra in a Navigation Workflow: Behavioral Analysis in Zero-Shot Vision-and-Language Navigation in Continuous Environments](http://arxiv.org/abs/2609.20116v1)
  <details><summary>📄 Abstract</summary>
  We study GPT-6-Astra in a zero-shot Vision-and-Language Navigation in Continuous Environments (VLN-CE) system, where it interprets instructions, assesses its surroundings, and proposes actions. The system uses a common observation--decision--execution workflow with direct model API calls, without a packaged agent harness or navigation-specific fine-tuning. In this workflow, each request receives selected observations, execution feedback, and retained progress records. Evaluation covers the compl...
  </details>

- **2026-09-17** — Yichao Jin, Yushuo Wang, Yuxuan Han et al. — [Perception, Layout, and Validation: Calibrated Confidence for Reliable Straight-Through Processing of Financial Documents](http://arxiv.org/abs/2609.20110v1)
  <details><summary>📄 Abstract</summary>
  Straight-through processing (STP) on extracted key-value fields from financial documents without human review requires a calibrated probability together with a bounded guarantee on the residual error of the auto-approved tier. The emergence of modern Vision Language Models (VLMs) provides an out-of-the-box capability for extracting the key-values, but their verbalized confidence signals are unreliable and weakly track field correctness. This paper introduces a decomposed confidence layer along t...
  </details>

- **2026-09-17** — Abraham Ezema, Chijioke Eze, Ferdinanda Ponci et al. — [SETTer: Sparse-Encoder Transformer for Long-term Multivariate Time Series Forecasting](http://arxiv.org/abs/2609.20086v1)
  <details><summary>📄 Abstract</summary>
  Long-term multivariate time series plays a significant role in many application areas such as power systems, trading, etc. However, their accurate prediction is quite difficult for conventional forecasting methods as they often exhibit high dimensionality and complex relationships. Recent works show that transformer-based approaches are quite effective for long-term forecasting thanks to their attention mechanism. However, in the presence of complex high-dimensional inputs, they show evidence of...
  </details>

- **2026-09-17** — Hasindri Watawana, Sergio Burdisso, Esaú Villatoro-Tello et al. — [Reading Emotions in the Token Space: Discriminative Adaptation of SpeechLLMs for Emotion Recognition](http://arxiv.org/abs/2609.20081v1)
  <details><summary>📄 Abstract</summary>
  SpeechLLMs have shown strong potential for emotion recognition, yet they read the predicted emotion off a generative decoder not suited for classification: it can emit labels outside the target set and favors frequent classes. We propose a discriminative adaptation that reads the final prompt token's hidden state through a classification head, producing a label in one forward pass without modifying the backbone. Because this readout starts from the hidden state the model would otherwise decode, ...
  </details>

- **2026-09-17** — Ryota Mitsuhashi, Tetsuro Morimura, Hirotake Ito — [From "Who Is This User?" to "What Does This Purchase Mean?": A Deployed Pipeline for Semantic User Profiling at Bank Scale](http://arxiv.org/abs/2609.19928v1)
  <details><summary>📄 Abstract</summary>
  Per-user LLM inference on transaction histories binds the inference budget linearly to user count, which becomes prohibitive at applied scale. We re-cast attribute inference from per-user to per-transaction-pattern. The pipeline runs in three phases: Resolve abstracts item names with optional web grounding, Profile infers attributes for each frequent pattern, and Tag clusters free-text attributes into a queryable database. In Profile, a single LLM call per pattern emits predefined categorical la...
  </details>

- **2026-09-17** — Yang Liu, Yulin Huang, Xue Yu et al. — [SabreAgent: Language Models at Design Time for Lost-Sales Inventory Control](http://arxiv.org/abs/2609.19760v1)
  <details><summary>📄 Abstract</summary>
  SabreAgent uses a language model at design time to construct two components for lost-sales inventory control: a product-specific seasonal prior and a validation-selected capped base-stock policy family. During operation, statistical forecasting and inventory optimization use these frozen artifacts to determine orders, with zero language-model calls. We evaluate the approach on the $1{,}320$ instances of InventoryBench. Under the benchmark's cost assumptions, the operations-research core draws on...
  </details>

- **2026-09-17** — Yuji Okitani — [Microlocal perverse schobers and Radon transform](http://arxiv.org/abs/2609.19692v1)
  <details><summary>📄 Abstract</summary>
  Perverse schobers are a categorification of perverse sheaves, originally proposed by Kapranov and Schechtman. The purpose of this paper is to initiate a microlocal study of perverse schobers. We first categorify $\operatorname{Perv}(\mathbb{C},R)/\operatorname{Loc}(\mathbb{C})$, the category of perverse sheaves on a complex line with singular points at $R$, modulo local systems. We use this to propose a general definition for microlocal perverse schobers supported on the open conormal to a germ ...
  </details>

- **2026-09-17** — Xin Zhou, Sinian Zhang, Zhanyan Yang et al. — [Human-Anchored Inference for Ranking New Models with Large Language Model Judges](http://arxiv.org/abs/2609.19599v1)
  <details><summary>📄 Abstract</summary>
  Human pairwise comparisons provide a reference for evaluating large language models (LLMs), but collecting sufficient judgments for each new release is costly and time-consuming. LLM judges offer a scalable alternative, although their comparisons may differ systematically from human preferences and across judges. We study the ranking of a new model that has received LLM-judge comparisons but no human comparisons. We propose ANCHOR (ANchored Comparisons for Human-reference inference with Orthogon...
  </details>

- **2026-09-17** — Sanae Yamashita, Yuki Okafuji — [Learning from Success and Failure: Acquiring Adaptive Dialogue Strategies for Social Robots](http://arxiv.org/abs/2609.19570v1)
  <details><summary>📄 Abstract</summary>
  Traditional dialogue systems for social robots require both dialogue strategies and user attribute recognition, each demanding specialized expertise. However, data collection is costly in real-world deployments, and the resulting datasets often include many failure cases. In this study, we aim to automate the acquisition of dialogue strategies by leveraging both successful and failed interactions using a vision-language model (VLM) and a large language model (LLM). We propose an architecture in ...
  </details>

- **2026-09-17** — Tohid Ghasemnejad, Ahmadreza Argha, Mark Grosser et al. — [Large Language Model Agents for Evidence Based Genetic Disease Severity Classification](http://arxiv.org/abs/2609.19569v1)
  <details><summary>📄 Abstract</summary>
  Disease severity classification for genetic conditions is subjective and labor-intensive, creating bottlenecks in genomic screening, where commercial panels vary widely in size and overlap. We developed an autonomous AI agent integrating Reasoning and Acting (ReAct) with Retrieval-Augmented Generation (RAG) to classify 10,211 Human Phenotype Ontology terms. It uses American College of Medical Genetics (ACMG)-endorsed severity guidelines and American College of Obstetricians and Gynecologists (AC...
  </details>

- **2026-09-17** — Yuqing Zhang, Haoyu Zhu, Yiannis Kantaros — [Navigate or Relocate? Planning Among Movable Obstacles in Unknown Environments](http://arxiv.org/abs/2609.19541v1)
  <details><summary>📄 Abstract</summary>
  Conventional robot planning methods seek collision-free paths to a goal but fail when all paths are blocked. In these cases, the robot must determine which objects to relocate, in what order, and where to place them to clear a path---a problem known as Navigation Among Movable Obstacles (NAMO). Most NAMO planners assume a known environment, while existing approaches for unknown environments typically reason locally about relocations and cannot plan interdependent relocation sequences. We conside...
  </details>

- **2026-09-17** — Aras Kavuncu — [LSTM-UT and Recurrent-Depth Transformers on Cellular Automata](http://arxiv.org/abs/2609.19521v1)
  <details><summary>📄 Abstract</summary>
  Recurrent-depth Transformers apply shared computation repeatedly, but differ in how they retain information across steps. We compare a Block Universal Transformer (BUT), which carries only its current hidden state; CoTFormer, which also retains an expanding attention cache; and a new LSTM Universal Transformer (LSTM-UT) with bounded gated memory. On Rule 30 cellular automata, BUT extrapolates to unseen recurrent depths more reliably than CoTFormer, although its accuracy eventually degrades. Stat...
  </details>

- **2026-09-17** — Xiaoyu Chen, Kuikui Liu — [Spectral Gap of Down-Up Walks via Trickle-Down: A Simplified and Sharpened Analysis](http://arxiv.org/abs/2609.19514v1)
  <details><summary>📄 Abstract</summary>
  Local-to-global techniques for establishing spectral gaps have played a central role in the modern theory of Markov chain mixing times and the theory of high-dimensional expanders. One of the most striking results in this burgeoning literature is that a spectral gap for the global down-up walk on the facets of a pure simplicial complex can be reduced to sufficiently strong spectral expansion of just the codimension-2 links of the complex, a phenomenon colloquially referred to as "trickle-down". ...
  </details>

- **2026-09-16** — Lyuxing He, Daniel Guo, Elizabeth Terveen et al. — [ParticleSplat: Self-supervised Object-centric Latent Particle Splatting](http://arxiv.org/abs/2609.19463v1)
  <details><summary>📄 Abstract</summary>
  We present ParticleSplat, a self-supervised object-centric learning method that decomposes scenes into a set of latent ''particles'' representing semantic entities through feedforward 3D Gaussian Splatting. Building on the Deep Latent Particles (DLP) framework, which represents images as a set of particles with attributes such as position, scale, and visual appearance, we address a key limitation of DLP: its inherently 2D nature, which prevents explicit 3D spatial and geometric reasoning that ar...
  </details>

- **2026-09-16** — Fan Yang, Jiabin Wu, Yuan Tian et al. — [CARES: A Conversational AI System for Regulation-Grounded Safety Reporting in Construction Education](http://arxiv.org/abs/2609.19429v1)
  <details><summary>📄 Abstract</summary>
  Construction safety reporting often relies on manual logs and static templates that provide limited feedback and leave daily activities disconnected from relevant regulations. This paper introduces CARES (Conversational AI Reporting for Enhanced Safety), a conversational AI system that integrates regulatory guidance into daily reporting to support construction safety education. CARES combines proactive multi-agent dialogue, retrieval-augmented generation (RAG), and automated report generation. T...
  </details>

- **2026-09-16** — Albert Wu, Nicholas Roberts, Tzu-Heng Huang et al. — [MAGS: Multi-agent Auto-formalization Guarantees Safety for Agentic Outputs](http://arxiv.org/abs/2609.19391v1)
  <details><summary>📄 Abstract</summary>
  LLM coding agents now generate complex programs at a scale that makes thorough human review increasingly difficult, raising the risk of safety and security failures. Common approaches, including fuzz testing, static analysis, and LLM-as-a-Verifier, can detect many failures but struggle to cover all possible edge cases. Formal verification addresses this by providing machine-checkable guarantees over specified properties, but traditionally demands substantial manual specification and proof engine...
  </details>

- **2026-09-16** — Badri N. Patro, Vijay S. Agneeswaran — [Riemannian--Lorentz Fusion of Vision Transformers and State-Space Models](http://arxiv.org/abs/2609.19384v1)
  <details><summary>📄 Abstract</summary>
  Scaling deep learning faces critical bottlenecks: data exhaustion, exponential training costs, and resource concentration. Model merging combines pre-trained checkpoints without gradient descent, offering orders-of-magnitude savings versus retraining. Combining independently trained vision models is difficult when their architectures and parameter shapes differ. Existing weight-space merging methods generally assume aligned, shape-compatible checkpoints, whereas a Vision Transformer (ViT) and a ...
  </details>

- **2026-09-16** — Adam Gaber, Uriel Dolev, Elisabeth Fittschen et al. — [Why Pretraining Fails to Share Cross-Lingual Knowledge](http://arxiv.org/abs/2609.19291v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have made remarkable progress in the processing and modeling of many languages. Yet, unlike human multilinguals, they exhibit surprisingly limited cross-lingual knowledge transfer. While this limitation is well documented, its origins during multilingual training remain unclear. We pretrain 360M- and 7B-parameter LLMs and show that poor cross-lingual knowledge generalization emerges during pretraining and persists under standard interventions. To isolate its cause, w...
  </details>

- **2026-09-16** — Xinpeng Liu, Lu Ma, Jiayi Qiao et al. — [Generative Query Suggestion via Intent Coverage and Query-Level Credit Assignment](http://arxiv.org/abs/2609.19209v1)
  <details><summary>📄 Abstract</summary>
  Generative query suggestion aims to enhance user engagement by anticipating user intents and recommending relevant follow-up queries. A central challenge is to generate slates whose individual queries are useful while the slate covers distinct intents. We propose an Intent-Driven Query Suggestion Framework with dual-stage optimization. First, intent-aware diversity modeling constructs intent-aligned supervised fine-tuning (SFT) data and uses an Intent-Aware Diversity Reward to optimize intent co...
  </details>

- **2026-09-16** — Dong Liu, Yanxuan Yu — [MeshKV: A Network-on-Chip KV Cache Fabric for Scalable Transformer Decoding Accelerators](http://arxiv.org/abs/2609.19207v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive transformer decoding is constrained by irregular key-value (KV) cache movement on tiled accelerators. Prior compression and DRAM-placement systems still concentrate traffic on centralized memory paths that bottleneck long-context serving. We present MeshKV, a KV cache fabric that moves blocks as packetized flows over a lightweight NoC. It co-designs (i) TaKV affine striping to spread homes and cut hotspot load, (ii) Mare multicast with verified duplicate suppression, and (iii) Pad...
  </details>

- **2026-09-16** — Zixin Fan, Jiahong Lu, Changsheng Zheng et al. — [EvoSherlock: Towards Agentic Lifelong Evolution for Unseen Long-Tailed Security-Critical Events in Videos](http://arxiv.org/abs/2609.19201v1)
  <details><summary>📄 Abstract</summary>
  Existing Security-oriented Video Understanding (SVU) systems assume a \emph{closed world}, \ie static category sets, abundant labels, and the premise that all event types are known upfront. Real-world security-critical events break these assumptions: they follow long-tailed distributions, new types emerge continuously, and critical security events may offer only a few samples. We formalize this gap as \textbf{Lifelong Evolving Task for Long-Tailed Security-Critical Events in Videos ({\boldmath$L...
  </details>

- **2026-09-16** — Chunpu Xu, Zhixuan Liang, Yuhao Zhang et al. — [M2Tok: Multi-head Multi-codebook Discrete Action Tokenization for Vision-Language-Action Models](http://arxiv.org/abs/2609.18259v2)
  <details><summary>📄 Abstract</summary>
  Recent advancements have successfully adapted autoregressive language models to process multimodal signals, such as images and actions. Since raw action signals are continuous, effective tokenization is essential to map high-dimensional inputs into compact discrete tokens for autoregressive processing. However, existing discrete action tokenizers often suffer from high reconstruction loss, failing to preserve the fine-grained dynamics required for precise control. This "discretization bottleneck...
  </details>

- **2026-09-16** — Jing Jiang, Yue Yang, Xinkai Jiang et al. — [From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation](http://arxiv.org/abs/2609.19413v1)
  <details><summary>📄 Abstract</summary>
  Robot manipulation policies are improving quickly, and real-robot evaluation remains the standard evidence for that progress. It still relies on a human to reset the scene between rollouts, which consumes operator time and leaves the initial state distribution unspecified, so results reproduce poorly. A recent system, AutoEval, automates both reset and scoring, but only for single-step tasks, because a long-horizon rollout can terminate in combinatorially many configurations that no single learn...
  </details>

- **2026-09-16** — Jingzhan Ge, Ruimin Chen, Azadeh Haghighi et al. — [Kinematics-Grounded Agentic AI for Robotic Additive Manufacturing Process Planning](http://arxiv.org/abs/2609.19347v1)
  <details><summary>📄 Abstract</summary>
  Robotic additive manufacturing (AM) extends material-extrusion printing beyond gantry kinematics but makes process planning robot-dependent. A slicer-generated plan that appears favorable in part coordinates can become infeasible or robotically unfavorable on a manipulator because slicer-process decisions and part orientation determine the generated path, while part orientation and workspace placement affect its kinematic realization. Existing AM tools, large language model (LLM)-based decision-...
  </details>

- **2026-09-16** — Can Li, Jie Gu, Zishun Deng et al. — [DeformSmith: Physics Harness-Guided Hierarchical Generation of Deformable Assets for Robot Manipulation](http://arxiv.org/abs/2609.18620v2)
  <details><summary>📄 Abstract</summary>
  Creating deformable assets for robot manipulation requires jointly specifying their geometry, appearance, and physical properties. This is especially challenging for deformable objects, since text and images provide limited evidence about how they deform and respond to contact, yet these responses directly affect their suitability for interaction. Automated generation therefore needs to resolve coupled physical requirements and use interaction evidence to guide construction and refinement. We pr...
  </details>

- **2026-09-16** — Xiatao Sun, Chen Liang, Ziyao Zeng et al. — [Decoupling Vision, Language, and Action for Efficient Multi-Task Robot Policies](http://arxiv.org/abs/2609.18374v2)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) policies commonly run Vision-Language Model (VLM) backbones with billions of parameters at every policy inference, which costs latency and energy. We revisit a decoupled alternative for multi-task manipulation: separate vision and language encoders whose representations condition a compact action head. We run a standardized comparison that varies the vision encoder, the language encoder, and the action head while holding the demonstrations, the training-step budget, ...
  </details>

- **2026-09-16** — Jiaming Liang, Haydn Jones, Jacob R. Gardner et al. — [Efficiently Linking Unstructured Data for Multi-step Reasoning](http://arxiv.org/abs/2609.19491v1)
  <details><summary>📄 Abstract</summary>
  Modern LLMs and AI agents increasingly support data engineering workflows that integrate evidence from unstructured sources. Such pipelines typically do data retrieval, integration, and ranking before proceeding to more complex agentic reasoning or actions, e.g., for scientific discovery. The core retrieval problem in these workflows jointly executes multi-attribute filtering, multi-vector search, exact relational joins, and thresholded embedding-similarity joins. Given a planned query and monot...
  </details>

- **2026-09-16** — Jiuyi Xu, Jinjia Guo, Meida Chen et al. — [Predict Before You Deploy: Offline Prediction of Quantization-Induced Task Degradation for World Action Models](http://arxiv.org/abs/2609.19441v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) rely on video-generation backbones, requiring substantial memory and compute for deployment. Post-training quantization reduces memory and can accelerate inference, but bit width, grouping, and quantizer choice define a large configuration space. Identifying configurations that preserve task performance through exhaustive closed-loop evaluation is costly. We propose PreDE (Predict Before You Deploy), a policy-calibrated framework for predicting quantization-induced tas...
  </details>

- **2026-09-16** — Ahmad Ghandour — [From Digital Competence to Demonstrated Digital Capability: Positioning the International Digital Driving License Against DigComp and UNESCO Frameworks](http://arxiv.org/abs/2609.19406v1)
  <details><summary>📄 Abstract</summary>
  Digital competence frameworks define the knowledge, skills, attitudes and values required for participation in digital society. The European Digital Competence Framework for Citizens (DigComp) and UNESCO digital literacy and artificial intelligence competency frameworks provide reference structures for policy, curriculum and competency development. The growth of generative and agentic AI raises a further question: does knowing what constitutes competent digital behaviour provide sufficient evide...
  </details>

- **2026-09-16** — Henry O. Velesaca, David Freire-Obregon, Luigi Miranda et al. — [Can Vision-Language Models Judge Olympic Diving? From Reasoning to Scores in Zero-Shot Action Quality Assessment](http://arxiv.org/abs/2609.19354v1)
  <details><summary>📄 Abstract</summary>
  Automated action quality assessment (AQA) in Olympic sports remains a challenging task due to the complexity of human motion and the subjectivity inherent in expert judging. This work evaluates the capability of open-source Vision-Language Models (VLMs) to perform zero-shot action quality assessment on Olympic diving videos using the AQA-7 benchmark dataset. In this regard, a regression-based framework is pro-posed to leverage both the semantic reasoning and phase-level sub-scores generated by t...
  </details>

- **2026-09-16** — Noam Glazner, Amir Leshem — [Asymptotic Max-Min Fair Allocation with Random Utilities](http://arxiv.org/abs/2609.19319v1)
  <details><summary>📄 Abstract</summary>
  We investigate the asymptotic behavior of max-min fair allocations for indivisible goods under i.i.d. random utilities. For $N$ agents and $K$ goods with utilities ${\mU_{i,j}}$ drawn independently from a common distribution $F$, we derive asymptotic characterizations of the max-min value in the balanced case $K=N$ (and in $K=LN$ extensions) via distributional quantiles. We then study the efficiency impact of max-min fairness by comparing the resulting total welfare with the optimal sum welfare....
  </details>

- **2026-09-16** — Julian Alfredo Mendez, Timotheus Kampik — [The AR Fairness Metamodel: A Structured Framework for Fairness Measures](http://arxiv.org/abs/2609.19234v1)
  <details><summary>📄 Abstract</summary>
  This paper presents the AR fairness metamodel, a framework designed to represent, analyze, and compare different fairness scenarios. The metamodel considers key elements, such as agents, resources, and their attributes, and enables the systematic definition and comparison of various fairness measures. We provide examples involving both discrete and continuous measures, including equality, equity, group fairness, individual fairness, the Gini index, the Theil index, Jain's fairness index, and a d...
  </details>

- **2026-09-16** — Ashutossh Gupta, Vassilis Kekatos — [Designing Grid-Aware Dynamic Specifications for Large Data Center Loads](http://arxiv.org/abs/2609.18888v1)
  <details><summary>📄 Abstract</summary>
  As data center (DC) loads increasingly penetrate the power grid, there is an urgent need for grid operators to provide clear dynamic specifications to DC owners to ensure safe grid operation. To this end, we study two salient behaviors of large language model (LLM) training loads: abrupt ramps at job initiation and termination, which induce transient frequency excursions, and sustained periodic oscillations during training, which result in oscillatory steady-state behavior. For ramping loads, we...
  </details>

- **2026-09-16** — Jianying Liu, Kim Gerdes, Jean-Marc Deltorn — [Beyond frequency measures: Can contextual embeddings capture meaning change in scientific texts?](http://arxiv.org/abs/2609.18804v1)
  <details><summary>📄 Abstract</summary>
  Identifying technological trends is a core scientometric task, yet traditional frequency-based approaches struggle to capture substantial meaning shifts of domain-specific terms. We hypothesise that contextual embeddings can complement frequency dynamics to effectively track diachronic semantic change. We compare frequency and embedding-based approaches across Astrophysics and NLP corpora spanning from 2010 to 2024. Candidate terms are extracted using KeyBERT (utilizing SciBERT as its underlying...
  </details>

- **2026-09-16** — Quan-Dung Pham, Anh Dao, Danh Vinh Le et al. — [AdaGeoVLN: Selective Geometry Across Representation Depth and Navigation Time for Vision-Language Navigation](http://arxiv.org/abs/2609.18789v1)
  <details><summary>📄 Abstract</summary>
  Vision-language navigation requires aligning language with visual observations while maintaining spatial understanding over time. Geometry foundation models (GFMs) expose intermediate representations throughout their hierarchy, but how navigation policies should use these features and retain historical geometric evidence remains unresolved. We introduce \method{}, a streaming VLN framework that addresses these questions across \textbf{representation depth} and \textbf{navigation time}. Hierarchi...
  </details>

- **2026-09-16** — Rupesh Raj Karn, Johann Knechtel, Ozgur Sinanoglu — [ReDIL-GNN: Resynthesis Domain Incremental Learning for Circuit Graph Neural Networks](http://arxiv.org/abs/2609.18595v1)
  <details><summary>📄 Abstract</summary>
  Logic resynthesis preserves circuit functionality while changing gate vocabulary, topology, and structural statistics, creating domain shift for circuit graph neural networks (GNNs) without changing task labels. To study this setting, we introduce ReDIL-GNN, a resynthesis domain-incremental learning framework that adapts a fixed prediction or representation head as new synthesis styles arrive and evaluates retention on all previously observed domains. Because not every shift should be adapted bl...
  </details>

- **2026-09-16** — Kailing Li, Yu Han, Tianwen Qian et al. — [GroundingVLN: Reasoning and Acting with Grounding for Vision-Language Navigation](http://arxiv.org/abs/2609.18581v1)
  <details><summary>📄 Abstract</summary>
  Although vision-language models (VLMs) possess strong visual understanding and reasoning capabilities, existing vision-and-language navigation (VLN) agents struggle to connect semantic reasoning with spatial execution. Two coupled gaps remain in this connection, as intermediate reasoning is not explicitly anchored to visual evidence and high-level decisions lack precise spatial goals to guide low-level motion. Cognitive science suggests that human navigation bridges these levels hierarchically b...
  </details>

- **2026-09-16** — Antoine Dumoulin, Laurence Boissieux, Joao Regateiro et al. — [DiT-Garment: Garment Dynamics with Diffusion Transformers](http://arxiv.org/abs/2609.18510v1)
  <details><summary>📄 Abstract</summary>
  We present DiT-Garment to model dynamic 3D clothing over human body models in arbitrary motion. Unlike existing methods, DiT-Garment can animate garments with unseen designs and physical materials, while allowing for direct inference of deformations for any target pose. To achieve this, we leverage a 2D diffusion transformer architecture to learn 3D deformations in a 2D UV-space. As the result is non-deterministic, our generative model learns the distribution of possible outcomes. The template g...
  </details>

- **2026-09-16** — Ronghao Lin, Qiaolin He, Zefeng Lu et al. — [Divide and Conquer: Mixture-of-Bottleneck Experts in Informative Ordinal Space for Video-based Multimodal Sentiment Analysis](http://arxiv.org/abs/2609.18470v1)
  <details><summary>📄 Abstract</summary>
  Video-based Multimodal sentiment analysis (MSA) must handle information from text, audio, and image sequence in human speaking videos, yet current methods often fail to integrate modalities with task awareness. Most models treat video sentiment prediction as a single task, overlooking its ordinal nature, and their fusion strategies struggle to capture diverse unique and synergic cues across modalities. To address these limitations, we adopt a divide-and-conquer perspective by reformulating MSA a...
  </details>

- **2026-09-16** — Carolina Fortuna, Vid Hanžel, Tim Strnad et al. — [Where Should Agents Live? Energy-Memory Characterization of Agentic AI for the Edge-Cloud Continuum](http://arxiv.org/abs/2609.18283v1)
  <details><summary>📄 Abstract</summary>
  As telecommunication networks evolve toward autonomous 5G-Advanced and 6G operations, agentic artificial intelligence (AI) workflows, where large language models (LLMs) execute multi-step reasoning, invoke diagnostic tools, retrieve domain knowledge, and coordinate across agent teams, are increasingly embedded across the edge-cloud continuum. While the biological brain accomplishes complex cognition on an exceptionally modest metabolic power budget of approximately 20W contemporary LLMs are prof...
  </details>

- **2026-09-16** — Chunpu Xu, Zhixuan Liang, Yuhao Zhang et al. — [${M}^2$Tok: Multi-head Multi-codebook Discrete Action Tokenization for Vision-Language-Action Models](http://arxiv.org/abs/2609.18259v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements have successfully adapted autoregressive language models to process multimodal signals, such as images and actions. Since raw action signals are continuous, effective tokenization is essential to map high-dimensional inputs into compact discrete tokens for autoregressive processing. However, existing discrete action tokenizers often suffer from high reconstruction loss, failing to preserve the fine-grained dynamics required for precise control. This ``discretization bottlenec...
  </details>

- **2026-09-16** — Sihao Ding, Santosh Vasa, Aditi Ramadwar et al. — [EDCT-Bench: Uncovering Faithfulness Gaps in VLMs via Explanation-Driven Counterfactual Testing](http://arxiv.org/abs/2609.17953v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) can produce Natural Language Explanations (NLEs) that sound plausible yet remain inconsistent with the visual evidence they cite. We present Explanation-Driven Counterfactual Testing (EDCT), an intervention-based protocol that extracts visual concepts cited in a model's explanation, applies verified minimal edits to them, and tests whether the resulting answer and explanation remain consistent with the edited image. Using this protocol, we create EDCT-Bench, a compr...
  </details>

- **2026-09-16** — Brandon Gary Kaplowitz, Dominik Bohnet Zurcher, Akash Agrawal et al. — [Epsilon-Nash Equilibria in History-Dependent SA-MDPs](http://arxiv.org/abs/2609.18829v1)
  <details><summary>📄 Abstract</summary>
  We study state-adversarial Markov decision processes (SA-MDP) as a game of observation-space attacks: at each step, an agent selects an action from a received observation while an adversary$\unicode{x2014}$who knows the true state the agent is in$\unicode{x2014}$chooses a perturbed observation within a state-dependent proximity set. While existing work focuses on Markovian policies, we develop a solution concept and computational approach for SA-MDPs under history dependence. This is motivated b...
  </details>

- **2026-09-16** — Bardienus P. Duisterhof, Kaifeng Zhang, Adam Hung et al. — [PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics](http://arxiv.org/abs/2609.19142v1)
  <details><summary>📄 Abstract</summary>
  World models endow perceptual systems with the ability to predict how scenes evolve under interaction. They are most beneficial when trained on diverse volumes of data, to instill a rich prior into downstream applications. Existing methods typically require robot action labels to learn action-conditioned 3D dynamics, which excludes web video data from the training pool. We study 3D point track completion as a pre-training objective for learning transferable 3D dynamics without robot data. Given ...
  </details>

- **2026-09-16** — Zhongyu Chen, Yuxuan Nai, Qian Chen et al. — [Learning Holistic Whole-Body Loco-Manipulation with a Bipedal Mobile Manipulator](http://arxiv.org/abs/2609.18930v1)
  <details><summary>📄 Abstract</summary>
  Bipedal loco-manipulation enables robots to interact with objects beyond the nominal workspace of their arms by coordinating locomotion and manipulation. Realizing this capability requires a low-level whole-body controller that translates task-level manipulation goals into coordinated arm and leg motions while maintaining balance. We present a unified whole-body controller trained with reinforcement learning that directly maps 6-DoF end-effector targets to coordinated actions for the bipedal bas...
  </details>

- **2026-09-16** — Shivaram Kumar, Gaoyuan Liu, Yoonchang Sung — [CaSCo: Cascade-Aware Soft-Collision Motion Planning](http://arxiv.org/abs/2609.18910v1)
  <details><summary>📄 Abstract</summary>
  Conventional motion planning treats collision as a binary constraint, although contact with different objects can have drastically different consequences. A robot may safely brush against a cardboard box while even minor contact with a glass, laptop, or unstable object may be undesirable. Moreover, a direct robot--object collision can move the contacted object and trigger secondary object--object collisions, making the risk of a motion depend on the physical evolution of the scene rather than on...
  </details>

- **2026-09-16** — Sitong Chen, Fatemeh Zargarbashi, Jin Cheng et al. — [KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation](http://arxiv.org/abs/2609.18869v1)
  <details><summary>📄 Abstract</summary>
  Humanoid loco-manipulation requires robots to interpret task instructions and scene semantics while executing coordinated whole-body motions. We propose a hierarchical framework that uses motion keyframes as an intermediate representation between Vision-Language Model (VLM) planning and Reinforcement Learning (RL) control. Each keyframe specifies a target whole-body robot pose and, when applicable, an object pose. Given a language instruction, scene observations, and execution feedback, the VLM ...
  </details>

- **2026-09-16** — Seyed Bagher Hashemi Natanzi, Bo Tang — [Taming the Agentic RAN: Stability-Guaranteed Arbitration of Autonomous AI Agents in O-RAN](http://arxiv.org/abs/2609.18857v1)
  <details><summary>📄 Abstract</summary>
  The O-RAN control plane is becoming agentic: autonomous AI agents, deployed as rApps by different vendors, independently close control loops over shared radio resources. We demonstrate on a live O-RAN system that this independence is unsafe. Two agents with individually correct objectives, one protecting a latency SLA and one maximizing utilization for energy efficiency, jointly drive recurring opposing excursions of the shared resource partition that neither produces alone. Existing conflict-mi...
  </details>

- **2026-09-16** — Zheng Li, Liang Zhu, Junzhe Wang et al. — [From Gameplay to Policy: Towards Scalable Robot Data Collection via Gamified Robot-Free Interaction](http://arxiv.org/abs/2609.18650v1)
  <details><summary>📄 Abstract</summary>
  Learning generalizable robot manipulation policies requires large-scale and diverse interaction data, yet collecting real-world demonstrations remains costly and difficult to scale. Existing approaches to data collection are either dependent on specific robot hardware that limits crowdsourcing and transferability, or suffer from incomplete annotation and limited behavioral diversity. Inspired by how games sustain long-term human engagement, we explore an alternative paradigm that turns data coll...
  </details>

- **2026-09-16** — Rem Hida, Masahiro Kaneko, Daisuke Oba et al. — [DyMT-ESB: Dynamic Multi-Turn Evaluation of Social Bias in User-LLM Interactions](http://arxiv.org/abs/2609.18649v1)
  <details><summary>📄 Abstract</summary>
  Warning: This paper contains examples of stereotypes and social bias. LLMs are increasingly used in interactive settings by the general public, making the evaluation of model behavior in multi-turn conversational scenarios important for safety, including stereotyping-related harms. However, existing multi-turn social bias evaluations often rely on pre-specified or template-based user inputs that do not adapt to model responses and typically assume a fixed dialogue length in advance. In this pape...
  </details>

- **2026-09-16** — Can Li, Jie Gu, Zishun Deng et al. — [DeformSmith: Physics Harness-Guided Hierarchical Generation of Deformable Assets for Robot Manipulation](http://arxiv.org/abs/2609.18620v1)
  <details><summary>📄 Abstract</summary>
  Creating deformable assets for robot manipulation requires jointly specifying their geometry, appearance, and physical properties. This is especially challenging for deformable objects, since text and images provide limited evidence about how they deform and respond to contact, yet these responses directly affect their suitability for interaction. Automated generation therefore needs to resolve coupled physical requirements and use interaction evidence to guide construction and refinement. We pr...
  </details>

- **2026-09-16** — Yu Liu, Wenwen Li, Yifan Dou et al. — [Recursive Reasoning or Statistical Extrapolation? In-Context Learning in Multi-Agent Interdependent Decision-Making](http://arxiv.org/abs/2609.18591v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) enables large language model (LLM) agents to improve decisions using interaction history, yet it remains unclear whether such improvement reflects refined internal reasoning or mere extrapolation of statistical patterns. To disentangle these mechanisms, we study LLM agents in multi-agent incomplete-information games that require recursive belief reasoning. By constructing a public goods game and manipulating the statistical structure of historical feedback, we evaluate ...
  </details>

- **2026-09-16** — Xuanze Yang, Yumeng Liu, Haiyang Xin et al. — [InterMASH: A Unified Geometric Representation for Grasp Synthesis](http://arxiv.org/abs/2609.18504v1)
  <details><summary>📄 Abstract</summary>
  Grasp synthesis aims to generate stable and physically plausible hand--object interactions, and has become a fundamental problem in both human hand modeling and robotic manipulation. However, a unified representation across human and robotic hands is still lacking, mainly due to differences in hand morphology and surface modeling. Prior methods typically rely on either contact maps or dense implicit descriptors to represent interaction, but these representations are often incomplete or computati...
  </details>

- **2026-09-16** — Xiatao Sun, Chen Liang, Ziyao Zeng et al. — [Decoupling Vision, Language, and Action for Efficient Multi-Task Robot Policies](http://arxiv.org/abs/2609.18374v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models attach an action module to a Vision-Language Model (VLM) with billions of parameters and pay for that backbone at every control step. For a low-level manipulation policy, this cost may be unnecessary: the VLM supplies vision and language embeddings, and recent standalone vision encoders and encoder-only language models now match or exceed large VLMs on visual embedding and language understanding benchmarks. We study this question with a controlled experiment. ...
  </details>

- **2026-09-16** — Ijaz Ahmad, Ijaz Ahmad, Flavio Esposito et al. — [Autonomy in Check: Governor-Mediated Adaptive Security at the Edge](http://arxiv.org/abs/2609.18338v1)
  <details><summary>📄 Abstract</summary>
  Adaptive security at the network edge increasingly relies on automated planners, including rule-based controllers, learned policies, and LLM-assisted agents, that translate observations into enforcement actions. Once such a planner can influence live policy state, syntactic validity is not enough. A semantically wrong action, produced from incomplete or manipulated observations, can be faithfully executed by an enforcement substrate that cannot judge mission context. We address this problem by t...
  </details>

- **2026-09-16** — Yonglin Tian, Weiyi Wang, Houhua Lu et al. — [UAVs Meet Embodied Intelligence: Bridging Human Intents and Flying Dynamics Via Harnessing Physical-Digital AI Agents](http://arxiv.org/abs/2609.18326v1)
  <details><summary>📄 Abstract</summary>
  Unmanned aerial vehicles (UAVs) extend embodied intelligence into continuous three-dimensional space, where perception, reasoning, physical embodiment, and action are tightly coupled through flight and environmental interaction. Recent advances in foundation models, world models, and AI agents are shifting UAV autonomy from task-specific perception and control toward systems that can interpret human intent, understand open environments, reason about physical consequences, and organize complex be...
  </details>

- **2026-09-16** — Bowei Zhang, Qiyao Zhang, Shuanghao Bai et al. — [WholeBodyWAM: Learning Whole-Body World Action Models with Scalable Motion Priors](http://arxiv.org/abs/2609.18197v1)
  <details><summary>📄 Abstract</summary>
  Humanoid whole-body manipulation requires coordinated whole-body dynamics, yet large-scale trajectories from a target robot are expensive to collect and difficult to scale. In contrast, whole-body motion from human and humanoid sources is abundantly available, although such data cannot be directly used as embodiment-specific robot actions. This work asks whether these scalable motion resources can instead provide a transferable predictive prior for humanoid world-action modeling. We introduce Wh...
  </details>

- **2026-09-16** — Julia Liu, Qing Xiao, Leona Yinglang Pang et al. — [Misgendering as Breakdown in Human-Machine Communication: How AI Companion Chatbot Users Experience and Repair Misgendering](http://arxiv.org/abs/2609.18186v1)
  <details><summary>📄 Abstract</summary>
  In recent years, large language model-based AI companion and role play chatbots have grown increasingly popular. People turn to these chatbots for emotional support and to engage in romantic and erotic role play. Although prior research suggests that digital role play can help people explore their gender and sexuality, LLM based technologies are also replete with gender and sexuality biases. In this study, we examine one way that AI chatbots can harm users: misgendering. In order to study chatbo...
  </details>

- **2026-09-16** — Toshiki Otani, Hiromu Taketsugu, Norimichi Ukita — [Energy-Regularized Imitation Learning for Force- and Work-Aware Robotic Manipulation](http://arxiv.org/abs/2609.18164v1)
  <details><summary>📄 Abstract</summary>
  This paper studies energy-aware manipulation as a physically grounded learning problem. We define a joint-space mechanical-work proxy from joint torque and angular displacement, and train a differentiable energy predictor that estimates this work from robot states and actions. The predictor converts a non-differentiable simulator-side physical quantity into a differentiable regularizer for fine-tuning a pretrained manipulation policy. We instantiate the framework with RVT-2 on RLBench and evalua...
  </details>

- **2026-09-16** — Yingyue Li, Chenyangguang Zhang, Ruida Zhang et al. — [Fetch My Beer: Synthetic-to-real Hierarchical Policy for Smooth Pick-and-place](http://arxiv.org/abs/2609.18119v1)
  <details><summary>📄 Abstract</summary>
  Many real-world robotic applications require dynamically sensitive manipulation, where success depends not only on reaching a target state but on maintaining stable object dynamics throughout execution. We study the stable transport of liquid-filled containers, where a robot must move objects to target locations while suppressing sloshing and preventing spillage. Unlike conventional pick-and-place, this task imposes stringent requirements on motion smoothness and trajectory-level stability, expo...
  </details>

- **2026-09-16** — Davood Wadi, Yu Ma — [Whom Do AI Agents Work For? Role Assignment Induces Sponsorship Bias in LLM Recommenders](http://arxiv.org/abs/2609.17989v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) now serve as conversational shopping assistants on platforms that also sell advertising. These AI agents face a conflict of duty. They advise consumers who rely on their judgment, yet are deployed by platforms that benefit when sponsored listings are chosen. Sponsorship disclosures, designed to allow consumers to penalize paid placements, now reach the AI agent rather than the consumer, and the agent's evaluation of them is hidden from the consumer. Drawing on the fi...
  </details>

- **2026-09-16** — Zimu Xu — [Long-Lived Characters, Local Inference: Incremental Memory Maintenance for Game NPCs](http://arxiv.org/abs/2609.18935v1)
  <details><summary>📄 Abstract</summary>
  A game character should not have to reread its entire life before every conversation. For locally deployed language-model characters, however, revising a few memories can invalidate a long reusable prefix. The resulting preparation cost competes with both foreground dialogue and the maintenance of other characters. This matters especially when dialogue feeds game-defined actions and value judgments: a fluent but incorrect account of who owns an item, or whether a transfer has already happened, c...
  </details>

- **2026-09-16** — Niloyendu Roy, Rupayan Saha, Debankur Das et al. — [Geometry-Controlled Relaxation Spectra in Viscoelastic Fluids](http://arxiv.org/abs/2609.18926v1)
  <details><summary>📄 Abstract</summary>
  Soft materials store, dissipate and release mechanical stresses through relaxation processes that often span many orders of magnitude in time. Such relaxation spectra are widely used to infer internal material dynamics and are usually regarded as fingerprints of microscopic complexity, disorder, or heterogeneity. Here we show that a broad relaxation spectrum can instead be generated by the geometry of mechanical excitation itself. Using rotationally driven colloidal dimers in a wormlike micellar...
  </details>

- **2026-09-16** — Farnoushsadat Nilizadeh, Elham Pourabbas Vafa, Shirin Nilizadeh et al. — [Structured Claim-Level Discourse Representations for Dense Health Narratives](http://arxiv.org/abs/2609.18905v1)
  <details><summary>📄 Abstract</summary>
  Health discourse in social media videos often contains densely entangled claims spanning multiple thematic aspects, stances, evidential frames, and rhetorical functions within short conversational spans. Existing approaches largely rely on coarse topic-level, sentiment-based, or stance-oriented representations that do not adequately capture this structure. Our analysis identifies an average of 13.22 atomic claims per minute, motivating richer claim-level discourse representations. We introduce a...
  </details>

- **2026-09-16** — Sheridan Feucht, Benno Krojer, Sarah Wang et al. — [Using OCR Heads to Verbalize Image Semantics](http://arxiv.org/abs/2609.18823v1)
  <details><summary>📄 Abstract</summary>
  How do VLMs map from pixels to semantics? To understand this general question, we focus on a narrow one: studying how VLMs perform optical character recognition (OCR). Across four models, we identify attention heads causally necessary for OCR, and discover that these are in fact general-purpose heads that output interpretable semantic features across all image tokens. For example, pointing these heads at an image token containing the word "bike" causes Qwen3-VL-8B to output "bike," but pointing ...
  </details>

- **2026-09-16** — Lucas G. Uberti-Bona Marin, Thales Bertaglia, Giovanni Astante et al. — ["If I Had to Buy Just ONE: Galaxy S26 Ultra": Auditing AI-Generated Product Recommendations](http://arxiv.org/abs/2609.18729v1)
  <details><summary>📄 Abstract</summary>
  Consumers increasingly use AI chatbots for advice on what to buy. With companies like OpenAI and Google monetising their AI through advertising, this raises difficult questions about the bias and impartiality of such advice. In response, we conduct an AI audit of popular chatbots using real commercial-advice queries. First, we curate a dataset of 2,528 real commercial-advice queries (ConsumerQ). Then, we evaluate 1,536 responses to product queries from popular AI chatbots: ChatGPT (chatbot and A...
  </details>

- **2026-09-16** — Thanh-Tuan Tran, Ngoc-Chien Chu, Thanh Nguyen Canh et al. — [Calibrated Probabilistic Obstruction Reasoning with Vision-Language Models for Grasping in Clutter](http://arxiv.org/abs/2609.18718v1)
  <details><summary>📄 Abstract</summary>
  Retrieving a target from clutter requires deciding whether to grasp the target, remove a blocker, or defer. Existing methods typically commit to a single obstruction graph or removal strategy, ignoring uncertainty across alternative scene interpretations. They also rely on miscalibrated vision-language model (VLM) predictions and can produce pairwise obstruction relations that are jointly inconsistent. Moreover, current approximations provide no guarantees about the impact of discarded hypothese...
  </details>

- **2026-09-16** — Jun Bi, Xiangxin Fang, Aarsh Chaube et al. — [Echo: Learning-based Matching Decompilation using Trusted Back Translation](http://arxiv.org/abs/2609.18706v1)
  <details><summary>📄 Abstract</summary>
  Neural decompilers can recover readable and recompilable source code from binaries, but their predictions remain difficult to trust. Matching decompilation addresses this problem by searching for source code whose recompiled assembly exactly matches the target, providing stronger evidence of correctness. However, exact matching remains challenging for optimized binaries under unknown compilation configurations.   We present Echo, a matching decompilation system based on trusted back-translation....
  </details>

- **2026-09-16** — Yifan Gao, Yao Tian, Hongbin Suo — [HearInContext: A Benchmark for Implicit Context in Speech Recognition](http://arxiv.org/abs/2609.18680v1)
  <details><summary>📄 Abstract</summary>
  Contextual ASR can benefit from semantic cues or from target words explicitly provided in the context. We introduce HearInContext, a Mandarin--English benchmark that pairs shared synthetic speech with assistant replies supporting different interpretations. The benchmark comprises 3,764 semantic test cases built around homophones. Implicit contexts exclude candidate words; explicit contexts name the target. No-context and unrelated-context controls measure the benefit of relevant history and sens...
  </details>

- **2026-09-16** — Giorgio F. Gilestro — [The evolution of sex for artificial intelligence: a population-genetic framework for multigenerational model populations](http://arxiv.org/abs/2609.18560v1)
  <details><summary>📄 Abstract</summary>
  Some aspects of AI development resemble a population process in which models are specialised, retrained on the output of peers, or combined by averaging weights. These practices lead to generations of models, in the biological sense studied by population genetics. Here, I develop this parallelism and interpret multigenerational model populations in terms of sexual and asexual reproduction, formally recombining the two fields. I test these analogies in an exact inheritance model, in trained netwo...
  </details>

- **2026-09-16** — Marcin Lawenda, Aleksandra Krasicka, David Caballero et al. — [Interpretable Patch-Based Deep Learning for Wildfire Spread Prediction from Ensemble Simulations](http://arxiv.org/abs/2609.18555v1)
  <details><summary>📄 Abstract</summary>
  Wildfire spread is traditionally predicted using physics-based simulators, which are physically interpretable but whose cost increases with each additional ensemble member. We ask how well deep learning surrogates can reproduce these simulations at a fraction of this cost, training them on 10,584 fire spread simulations at 2m resolution for the Rectoret region in Catalonia, Spain. Four architectures are compared: a patch-based U-Net, a transfer-learned ResNet-50, a physics-informed network const...
  </details>

- **2026-09-16** — M. Alaraby Salem, Thomas D. Kühne — [On-Water Surface Catalysis: From Hydrogen Bonding to Charge-Transfer Activation](http://arxiv.org/abs/2609.18498v1)
  <details><summary>📄 Abstract</summary>
  On-water catalysis accelerates reactions between poorly soluble organic substrates in aqueous suspensions, but its molecular origin remains debated. This Account argues that hydrogen bonding and proton transfer can both enhance charge-transfer stabilization between the organic reactants. Hydrogen bonds from surface water polarize the reacting complex, whereas protonation can perturb the same donor-acceptor interaction more strongly without requiring identical reaction pathways.   We connect simu...
  </details>

- **2026-09-16** — Frederik Wagner, Annerose Eichel, Sabine Schulte im Walde — [Exploring LLMs and RAG for Plausible and Explainable Material Prediction of Vehicle Components](http://arxiv.org/abs/2609.18437v1)
  <details><summary>📄 Abstract</summary>
  In this work, we explore whether LLMs can accurately predict and explain plausible materials for vehicle components such as brake discs or fuel injectors without requiring extensive fine-tuning. We test and evaluate three approaches: a standard generative LLM baseline, a single-pass Retrieval-Augmented Generation (RAG) approach, and an iterative Chain-of-Verification (CoVe) variant. For retrieval, we rely on publicly available data using a domain-filtered Wikipedia corpus. Since no gold standard...
  </details>

- **2026-09-16** — Zhuo Chen, Zhen Zhang, Xinyu Wang et al. — [Dependency-Aware Trajectory Refinement for Efficient Multi-Turn Agent Fine-Tuning](http://arxiv.org/abs/2609.18417v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn agent trajectories often contain redundant rounds (failed tool calls, parallel sub-queries, verification-only steps) that inflate both training and inference cost. We propose viewing each trajectory as a \emph{round-level dependency DAG} that exposes which rounds are globally load-bearing for the final answer, and fine-tune agents on trajectories refined through this DAG. Given an LLM-annotated DAG, these edits are deterministic and interpretable, with optional rephrasing. Models trai...
  </details>

- **2026-09-16** — Fabio Arz — [Pathology-Free Real-Space Renormalization Group Theory on an Inverse Limit Space](http://arxiv.org/abs/2609.18356v1)
  <details><summary>📄 Abstract</summary>
  It has been over fifty years since Kenneth Wilson had his Nobel-prize-winning ideas on the renormalization group. In this time frame, despite many attempts, no mathematical results have implemented Wilson's vision to a satisfactory degree. Although a number of predictions stemming from the renormalization group framework have been proven to date, these proofs usually rely on alternative ideas and do not cover the full predictive power of Wilson's renormalization group. The discovery of pathologi...
  </details>

- **2026-09-16** — Jisoo Kim, TaeYoon Kwack, Jinwoo Jang et al. — [Visual Compliance via Executable Safety Rule Entailment](http://arxiv.org/abs/2609.18328v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in LLMs and VLMs have enabled safety systems to reason beyond simple risk patterns toward more contextual and semantic safety concerns. However, as risk patterns continue to evolve and safety rules become more complex, existing training-based end-to-end safeguards face persistent challenges in adaptability and explainable reasoning over complex safety rules. To address these challenges, we propose GuardEn (Guarding by Safety Rule Entailment), an executable safeguard framework tha...
  </details>

- **2026-09-16** — Pablo Poulenard, Yannis Karmim, Valentin Barrière — [Knowledge-Graph Based Augmentation versus Retrieval Augmented Generation for Cultural-Related Question Answering](http://arxiv.org/abs/2609.18317v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) suffer from a long-tail deficit: culturally specific facts, particularly those concerning underrepresented regions such as Latin America, appear too rarely in pretraining corpora to be reliably memorized. Retrieval-Augmented Generation (RAG) addresses this by grounding generation in external text, but structured alternatives such as Knowledge Graphs (KGs) offer tighter control over what enters the context, along with potential gains in explainability and updatability...
  </details>

- **2026-09-16** — Haruka Tokumasu, Masanari Kondo, Alexander Serebrenik et al. — [A Study on the Impact of Natural Language Differences in Prompts on Automatic Code Generation Using LLMs](http://arxiv.org/abs/2609.18311v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have demonstrated remarkable performance in automatic code generation tasks, thereby encouraging new research in this area. Although numerous studies have explored LLM-based code generation, the impact of the natural language in input prompts remains unexplored (language bias). This study aims to (1) quantify how the natural language of input prompts influences LLM-based code generation performance and (2) evaluate a mitigation strategy to reduce language bias in cod...
  </details>

- **2026-09-16** — Paul W. Goldberg, Alexandros Hollender, Giannis Tyrovolas — [Equilibria of Round-Robin: Computational Hardness and Fairness for Few Subadditive Agents](http://arxiv.org/abs/2609.18309v1)
  <details><summary>📄 Abstract</summary>
  The round-robin procedure is a simple and well-studied fair division mechanism where agents pick goods in turns. Motivated by draft mechanisms in sports leagues, we investigate strategic behaviour in online round-robin for subadditive agents. This gives rise to an extensive-form game, and we study the computational problem of computing a subgame perfect Nash equilibrium (SPNE). We show that for just two submodular agents, computing an SPNE is $\mathsf{PSPACE}$-hard. Even for the class of $\mathi...
  </details>

- **2026-09-16** — Omran Berjawi, Giuseppe Fenza, Rida Khatoun — [Bias Amplification in Multi-Agent Network: How Biased Agents Shape Opinions and Rhetoric](http://arxiv.org/abs/2609.18306v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in applications involving interaction between agents, where their output plays a role in collective reasoning and decision-making processes. Despite significant research into the functioning of LLMs in such multi-agent systems, the processes of bias propagation in such systems are still a challenge. This work studies how biased opinions are propagated in the form of textual interaction in an environment of LLMs, in which a minority of agents...
  </details>

- **2026-09-16** — Xinglang Zhang, Yuanmeng Xiang, Yunyao Zhang et al. — [Too Good to Be Real? Diagnosing and Reducing the Gap Between AI Preference and Real User Engagement](http://arxiv.org/abs/2609.18282v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to generate and evaluate online content, yet it remains unclear whether the qualities they associate with higher engagement match what real users respond to. We study this question using 1.17 million answers to 25,978 questions from Zhihu, Quora, and Reddit, comparing real platform answers and AI-generated answers across four within-question engagement levels. We introduce Ontological Preference Measurement, which represents answers along three dimensi...
  </details>

- **2026-09-16** — Junnan Dong, Linhao Luo, Senlei Zhang et al. — [WFM: Wiki Foundation Model for Complex Agentic Reasoning](http://arxiv.org/abs/2609.18182v1)
  <details><summary>📄 Abstract</summary>
  Real-world agents fundamentally require persistent non-parametric knowledge for dynamic reasoning, i.e., long-term memory and retrieval-augmented generation. While graphs have shown reliable advantages in providing structured evidence, the sparse graph representations naturally restrict machine readability and semantic density required for complex agentic workflows. Driven by this limitation, the entire industry is witnessing a paradigm shift from traditional sparse graphs to LLM Wiki, an agent-...
  </details>

- **2026-09-16** — Genta Okada — [Dynamic Pooling and Regional Participation in Deceased-Donor Organ Allocation](http://arxiv.org/abs/2609.18147v1)
  <details><summary>📄 Abstract</summary>
  Moving from geographically fragmented to pooled waiting lists in deceased-donor organ transplantation can improve efficiency, but it raises concerns about regional fairness and participation incentives. This paper studies Pareto gains from such transitions in a multi-class queueing model with impatient agents, perishable items, and a tractable homogeneous compatibility friction. Unlike standard approaches that focus on static match quality or ignore regional incentives in dynamic settings, our a...
  </details>

- **2026-09-16** — Xihe Shao — [Technical Report: One-Step Drifting Action Heads for GR00T N1.7](http://arxiv.org/abs/2609.18108v1)
  <details><summary>📄 Abstract</summary>
  One-step action generation can substantially reduce the inference cost of vision-language-action (VLA) policies, but its effect on closed-loop task success remains an open question. This technical report studies a GR00T N1.7 variant in which the iterative diffusion-transformer action head is replaced by a one-step drifting action head, together with an overlap-conditioned extension for asynchronous chunk replacement. All multi-seed drifting runs were trained on two NVIDIA A800 GPUs. On LIBERO, t...
  </details>

- **2026-09-16** — Timothy Kogucki, Alan Papalia — [Characterizing Refraction-Induced Ranging Bias in Underwater Collaborative Localization](http://arxiv.org/abs/2609.18073v1)
  <details><summary>📄 Abstract</summary>
  This work studies how refraction-induced bias on acoustic ranging affects multi-agent collaborative localization in a range of oceanographic conditions and spatial scales. While multi-agent range-aided navigation, which uses range measurements to either fixed infrastructure or other agents, is a promising solution to the challenges of large-scale underwater localization, its accuracy depends strongly on the quality of range measurements. Sound speed variability induces refraction (bending) of ac...
  </details>

- **2026-09-16** — Ziyang Zhang, Qin Li, Vasyl B. Yurchyshyn et al. — [Physics-Informed Neural Networks for Fast Multilayer Spectral Inversion of Hα 6562.8 A and Ca II 8542.1 A Spectra](http://arxiv.org/abs/2609.18025v1)
  <details><summary>📄 Abstract</summary>
  Strong chromospheric absorption lines such as H$α$ 6562.8 A and Ca II 8542.1 A provide vital diagnostics of plasma dynamics and thermal structure in the solar chromosphere. Multilayer spectral inversion (MLSI) offers a physically interpretable framework for modeling these lines using a finite number of radiative-transfer layers, but conventional MLSI relies on pixel-by-pixel nonlinear least-squares fitting, making it computationally expensive for large imaging spectroscopic data sets. Here, we i...
  </details>

- **2026-09-16** — Shesh Narayan Gupta, Nik Bear Brown — [Newer Is Not Fairer: Gender Stereotyping in Text-to-Image AI Across Model Generations](http://arxiv.org/abs/2609.18007v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image generative models are widely used in professional and creative settings, yet how they represent gender across occupations -- and whether newer models are fairer -- remains poorly understood across multiple generations. We evaluate gender representation across 20 occupations, 5 prompt templates, and 4 Stable Diffusion model generations (SD 1.5, SD 2.1, SDXL, SD 3 Medium), generating 8,000 images with n = 100 per occupation-model cell (5 prompts x 20 images), and classifying all with...
  </details>

- **2026-09-16** — Qiao Liao, Zhiyong Feng, Bin Wu et al. — [The Operable Pareto Front: Distilling Offline Search into Run-Time Control for Multi-Objective UAV Edge-Computing Scheduling](http://arxiv.org/abs/2609.17992v1)
  <details><summary>📄 Abstract</summary>
  A UAV mobile edge computing (MEC) fleet trades energy against delay, and its schedules form a Pareto front; we call a scheduler operable when the fleet can be asked for any point on that front at run time. We propose PrefDT, to the best of our knowledge the first preference-conditioned Decision Transformer for the problem of joint trajectory, association and offloading scheduling. Its idea comes from language modeling: we hand the model the desired trade-off as an input, such that a single model...
  </details>

- **2026-09-16** — Sai Babu Udayagiri, Arjun Chouhan, Ravisekhar Kanagala et al. — [When to Call an LLM: A Confidence-Gated Hybrid for Cost-Effective Emotion Recognition in Conversational AI](http://arxiv.org/abs/2609.17977v1)
  <details><summary>📄 Abstract</summary>
  Emotion recognition in conversation (ERC) is a production capability behind agent-assist prompts, escalation routing, and post-call analytics in contact-center-as-a-service (CCaaS) platforms, where cost and latency constraints matter as much as accuracy. We report a systems-level comparison of three deployment options for dialogue-contextual ERC: a low-cost stacked ensemble (sentence embeddings, windowed context, RandomForest/XGBoost/logistic-regression stacking), off-the-shelf LLM prompting (GP...
  </details>

- **2026-09-16** — Sadia Afroz, Rudrajit Choudhuri, Fatima A. Moussaoui et al. — [Apply-<x>Mag: One Tool to Support Many Inclusive Design Methods](http://arxiv.org/abs/2609.17948v1)
  <details><summary>📄 Abstract</summary>
  Doing inclusive design in HCI practice can be labor-intensive, a costly barrier that some companies and HCI practitioners may be unwilling or unable to overcome. Yet, not doing inclusive design is costly too, in the form of UX barriers that disproportionately disadvantage under-served user populations. To address this problem, we introduce Apply-<x>Mag, an LLM-powered tool to support HCI practitioners' work to design their products inclusively to wide ranges of users. Apply-<x>Mag is general, su...
  </details>

- **2026-09-15** — Lea Duesterwald, Anika Jain, Shreya Kochar et al. — [Evaluating the Impact of Personalization in Conversational Cybersecurity Assistants](http://arxiv.org/abs/2609.17839v1)
  <details><summary>📄 Abstract</summary>
  Users increasingly turn to Large Language Models to answer a variety of questions, including cybersecurity questions. We study how personalization strategies can help improve the effectiveness of answers to questions asked to an LLM-based cybersecurity assistant. Beyond accuracy, we focus on the understandability, actionability and, most importantly, motivating power of answers, given how often users fail to follow cybersecurity recommendations. Specifically, we investigate four personalization ...
  </details>

- **2026-09-15** — Deepankar Basu — [Segregation Monotonicity and the Measurement of Inequality in Social Networks](http://arxiv.org/abs/2609.17807v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces segregation monotonicity as a criterion for evaluating measures of inequality in social networks. A network inequality measure satisfies segregation monotonicity if, holding the distribution of income fixed, it weakly increases as the network becomes more segregated according to a specified transformation of network architecture. I investigate this property using a class of level-$k$ star networks that represent increasing social segregation in the following sense: relative...
  </details>

- **2026-09-15** — Badri N. Patro, Vijay Agneeswaran — [QiT: Quantum-Inspired Transformer for Visual Recognition Task](http://arxiv.org/abs/2609.17789v1)
  <details><summary>📄 Abstract</summary>
  Quantum machine learning offers a compelling representational perspective: angle-encoded states inhabit Hilbert spaces in which periodic similarities and interactions can be expressed naturally. Realizing this perspective for visual recognition remains difficult, however, because present quantum neural networks are constrained by limited qubit counts, costly circuit simulation and measurement, noise, and unstable optimization on noisy intermediate-scale quantum devices. We investigate whether us...
  </details>

- **2026-09-15** — Tingyu Guo, Reza Langari — [CorrRisk-WM: Corridor-Conditioned Risk World Modeling for Safety-Critical Trajectory Planning](http://arxiv.org/abs/2609.16724v2)
  <details><summary>📄 Abstract</summary>
  Safe local planning requires forecasting surrounding-agent motion and evaluating candidate-specific risks, since identical agent motion can pose different risks to different ego trajectories. We present CorrRisk-WM, a planning-oriented partial world model coupling environment evolution with supervised intrusion and near-miss prediction over bounded candidate-trajectory corridors. A latent environment model recursively predicts agent states and updates agent-agent and agent-map interactions. Each...
  </details>

- **2026-09-15** — Salman Rahman, Yubin Kim, Mihir Parmar et al. — [Locating Hidden Failures Makes Long-Horizon Agents More Reliable](http://arxiv.org/abs/2609.17930v1)
  <details><summary>📄 Abstract</summary>
  As AI agents take on long, autonomous tasks, we increasingly oversee rather than perform the work, yet we still judge them almost entirely by whether they finally succeed. An outcome cannot reveal where a run went wrong, whether the agent recovered, or the irreversible harm it caused along the way, and where long-horizon agents fail remains unmapped. We study $2518$ agent trajectories across software engineering, computer use, and science, close to real deployment, and classify $6967$ mistakes i...
  </details>

- **2026-09-15** — Omer Tafveez — [Do Frontier Models Seek Safety Evidence Before Acting?](http://arxiv.org/abs/2609.17865v1)
  <details><summary>📄 Abstract</summary>
  Frontier models are often evaluated on how they respond to safety information once it is already in context. We study an earlier decision point: whether models choose to acquire safety-relevant evidence before acting. We introduce SAFE, a controlled benchmark in which models make deployment decisions with optional evidence that varies in retrieval cost, probability, severity, and presentation. Across GPT-5.5, o3, Claude Opus 4.8, and Claude Sonnet 4.6, we find distinct evidence-acquisition polic...
  </details>

- **2026-09-15** — Bo Kang — [The Latent That Never Was: A Forensic Re-run of the CVAE Ablation in Action Chunking Transformers](http://arxiv.org/abs/2609.16745v2)
  <details><summary>📄 Abstract</summary>
  Action Chunking Transformers (ACT) are widely used to learn robot manipulation from demonstrations. Their conditional variational autoencoder includes an encoder meant to capture differences between demonstrations during training. The original ACT paper reported that encoder removal dropped the mean success rate from 35% to 2% on two simulated tasks with human demonstrations. We re-ran this ablation in the original code and checked whether the findings depend on the implementation or training da...
  </details>

- **2026-09-15** — Huixin Zhang, Shao-Jun Xia, Di Wang et al. — [Collaborative Memory for Multi-Agent VLM Systems](http://arxiv.org/abs/2609.17921v1)
  <details><summary>📄 Abstract</summary>
  Vision-language model (VLM) agents combine specialized perception, tools, and reasoning to address complex visual tasks. In multi-agent settings, different agents inspect different image regions, video frames, or visual representations, so collaboration extends beyond distributed reasoning to distributed perception. This makes shared visual context a central problem in VLM agent collaboration. In this paper, we frame memory hierarchy, cross-agent sharing, and consistency mechanisms around the ne...
  </details>

- **2026-09-15** — Seung Jae Lieu, Diego Morra, Chiara Cadoni et al. — [Can VLMs Reliably Assess Sidewalk Accessibility Attributes from Pedestrian-Level Imagery?](http://arxiv.org/abs/2609.17882v1)
  <details><summary>📄 Abstract</summary>
  An important component of urban accessibility, particularly for wheelchair users and people with reduced mobility, is sidewalk compliance with measurable requirements. We test whether effective width, longitudinal slope, cross slope, and pavement condition can be assessed reliably from pedestrian-level imagery using vision-language models (VLMs). We present the first application of sampling-based conformal prediction (CP) for VLM-based accessibility assessment. We evaluate four VLMs on 514 sidew...
  </details>

- **2026-09-15** — Shiwali Mohan, Matt Hong, Dule Shu et al. — [Learning Heterogeneous Preferences](http://arxiv.org/abs/2609.17847v1)
  <details><summary>📄 Abstract</summary>
  Learning from human feedback has become a central paradigm for training modern AI systems, where models of human utility are used as reward models in policy learning. Existing methods typically assume a \emph{universal utility} function shared across a population and treat disagreement between annotators as stochastic variation. While suitable for objective tasks, this assumption breaks down in subjective domains where preferences vary systematically across individuals. We study the problem of s...
  </details>

- **2026-09-15** — Zhongdi Qu, Carla P. Gomes — [A Four-Stage Decomposition of Word-Problem Solving and Mechanistic Fragility in LLM Math Reasoning](http://arxiv.org/abs/2609.17804v1)
  <details><summary>📄 Abstract</summary>
  Large language models solve grade-school math word problems with high accuracy, yet a single irrelevant clause inserted into the problem can collapse it. We reconcile these observations with a mechanistic account. We show that the model's internal computation decomposes into a four-stage sequential pipeline, Schema Abstraction, Operation Planning, Operand Binding, and Computation, each stage producing a distinct intermediate representation in an identifiable band of layers. Using the same scaffo...
  </details>

- **2026-09-15** — D. S. Anikonov, S. G. Kazantsev, D. S. Konovalova — [An additional possibilities of the standard method of inverting the Radon transform](http://arxiv.org/abs/2609.17803v1)
  <details><summary>📄 Abstract</summary>
  The problem of inverting the Radon integral transform in   finite-dimensional Euclidean space is considered. The relevance   of this topic for probing issues is indicated. It is noted that for the latter direction, it is   natural to consider the integrand as discontinuous function.   However, the available inversion formulas are only proven for   differentiable functions. Therefore, the question of obtaining   formulas for discontinuous functions arises. It is set that the   required results ca...
  </details>

- **2026-09-15** — Yuanbo Guo, Yiyu Shi — [FairCompressAgent: An Agentic Framework for Fairness-Aware Model Compression for FPGA Deployment](http://arxiv.org/abs/2609.17786v1)
  <details><summary>📄 Abstract</summary>
  Fairness-aware model compression requires selecting methods and configurations that balance accuracy, fairness, and deployment cost. These decisions become more difficult when compression methods are composed or the user's requirements change. In this paper, we propose FairCompressAgent (FCA), an agentic framework that integrates fairness-aware pruning, incremental quantization, and sparse low-rank factorization through a common operator interface. A language-model planner uses model profiles an...
  </details>

- **2026-09-15** — Asal Mehradfar, Mohammad Shahab Sepehri, Owen Antholine et al. — [Decoding Extrahepatic Targeting of Lipid Nanoparticles with Interpretable Machine Learning](http://arxiv.org/abs/2609.17721v1)
  <details><summary>📄 Abstract</summary>
  Lipid nanoparticles (LNPs) have transformed RNA medicine, yet their clinical utility remains constrained by predominant hepatic accumulation after systemic administration. Redirecting LNPs to extrahepatic tissues requires understanding of how lipid chemistry and formulation composition jointly govern in vivo biodistribution. Here, we develop an interpretable machine learning framework to predict hepatic versus extrahepatic LNP accumulation and identify molecular design rules for extrahepatic RNA...
  </details>

- **2026-09-15** — Neil K. R. Sehgal, Sunny Rai, Sai Preethi Matam et al. — ["We Are Tired of Explaining": Communication Practice and AI Roleplay Training for Community Health Workers in Rural India](http://arxiv.org/abs/2609.17710v1)
  <details><summary>📄 Abstract</summary>
  Community health workers (CHWs) in the Global South increasingly encounter AI-powered tools, yet the counseling work central to their role remains largely unsupported. We study communication practices among Accredited Social Health Activists (ASHAs) in rural Rajasthan, India, through simulated family-planning calls, semi-structured interviews, and an LLM chatbot roleplay design-probe with 20 participants. In calls, ASHAs often responded to social or material concerns by shifting to health-risk i...
  </details>

- **2026-09-15** — Younes Boufouss, Luc Pommeret, Thomas Gerald et al. — [Can We Do Interpretable NLI with Graphs Based on Atomic Propositions?](http://arxiv.org/abs/2609.16814v2)
  <details><summary>📄 Abstract</summary>
  While Large Language Model (LLM)-based Natural Language Inference (NLI) systems achieve high accuracy, their decision-making processes lack auditable structures. This paper explores whether NLI can be performed using only interpretable, graph-based representations of evidence. We introduce a fully graph-based pipeline where the classifier never directly processes the input text. Instead, sentences are decomposed into atomic propositions, converted into ConceptNet triples via constrained decoding...
  </details>

- **2026-09-15** — Daniel Ebanks, Devika Jain — [Geospatial Metadata Improves Discoverability by Connecting Datasets Across Scientific Disciplines](http://arxiv.org/abs/2609.16498v2)
  <details><summary>📄 Abstract</summary>
  Research data repositories are essential infrastructure for scientific inquiry and for ensuring that datasets follow FAIR (Findable, Accessible, Interoperable, and Reusable) principles. However, repository reuse depends on the quality and completeness of geospatial and thematic metadata, which researchers generally provide voluntarily. Given limited curation resources, it is unsurprising that even Harvard Dataverse, the world's largest general-purpose research repository, contains many incomplet...
  </details>

- **2026-09-15** — Ziheng Ren, Qian Gao, Jun Fan et al. — [Semantic-Spatial Agreement Verification for Mitigating Object Hallucination in Multimodal Large Language Models](http://arxiv.org/abs/2609.17269v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models generate natural-language responses from visual inputs, yet may mention objects absent from an image. In medication assistance, accessible perception, and environmental decision-making, such hallucinations can create real-world safety risks. We propose Semantic-Spatial Agreement Verification (SSAV), a training-free method for verifying object claims. A visually grounded claim should remain stable across semantically equivalent queries and repeatedly localize to t...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 632 |
| prompt-injection | 546 |
| memory-poisoning | 49 |
| tool-use-attack | 136 |
| backdoor | 466 |
| adversarial-attack | 596 |
| privacy-leakage | 4115 |
| steganography | 68 |
| misuse | 1030 |
| red-teaming | 125 |
| vulnerability | 3133 |
| defense | 2951 |
| alignment | 2742 |
| robustness | 2877 |
| watermark | 447 |
| unlearning | 96 |
| agent-safety | 55 |
| benchmark | 66 |
| survey | 354 |
| other | 7837 |

---

📚 **全部 28321 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-21 17:42:07*