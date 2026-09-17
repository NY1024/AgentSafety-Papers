<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-28027-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-17 16:04 ｜ **论文总数 / Total Papers**: 28027（近 30 天 / Recent 30 days: 3923）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 28027 篇论文（含摘要、分类筛选、搜索）/ View all 28027 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 629
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 544
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 49
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 136
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 463
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 596
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4102
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 66
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1022
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 125
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3103
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2919
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2712
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2839
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 437
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 95
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 54
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 66
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 350
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7720

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3923 篇，完整 28027 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3923 papers from the last 30 days (with date, authors & abstract). For the full list of 28027 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 2 papers

- **2026-09-16** — Youjia Wang, Lin Xu, Yang Sun et al. — [Beyond Routine Compliance: Cunning Data Cultivates Safety Vigilance in Large Language Models](http://arxiv.org/abs/2609.18515v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment teaches large language models (LLMs) to recognize harmful requests and reject risky instructions. Yet aligned models can fail when harmful intent is concealed within seemingly benign contexts. Robust safety therefore requires both knowledge of safety boundaries and \textbf{vigilance}: the ability to detect unusual premises, misleading reasoning, and latent risks beneath surface-level semantics. Vigilance requires models to scrutinize a request's underlying intent and assumptions...
  </details>

- **2026-09-14** — Mark Russinovich, Blake Bullwinkel, Giorgio Severi et al. — [Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs](http://arxiv.org/abs/2609.15383v1)
  <details><summary>📄 Abstract</summary>
  Language model safety is typically evaluated one interaction at a time. We show that a weaker, unaligned model can split a harmful task into benign-looking subproblems, consult a stronger aligned model independently on each, and combine the answers locally. We call this attack capability laundering. Unlike a jailbreak, no single response is a harmful task. We measure consultation-aided uplift using tasks that a raw frontier model solves, the aligned frontier refuses, and the unassisted orchestra...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 10 papers

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

- **2026-09-14** — Xiaoyan Li, Yunli Wang — [Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks](http://arxiv.org/abs/2609.16098v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents have demonstrated impressive capabilities across a variety of domains, particularly when integrated with external tools for multi-step task completion. However, they are increasingly vulnerable to adversarial attacks, including direct prompt injection, indirect prompt injection, memory poisoning, and backdoor attacks, which exploit the model's openness to prompt injection and tool manipulation. In this work, we explore practical and generalizable defense strateg...
  </details>

- **2026-09-14** — Rakesh Kumar Surapani, Pradeep Kumar Dolabehera Kakitapelli, Arun Morampudi et al. — [Authorization Architectures for Tool-Using AI Agents](http://arxiv.org/abs/2609.15906v1)
  <details><summary>📄 Abstract</summary>
  Tool-using artificial intelligence (AI) agents, systems that autonomously invoke application programming interfaces (APIs), databases, browsers, and inter-agent protocols such as the Model Context Protocol (MCP), are becoming production infrastructure. Yet the security model governing when an agent is authorized to act on a human's behalf remains underdeveloped. Trustworthy human-AI systems require that every consequential agent action be traceable to a human principal, bounded by what that huma...
  </details>

- **2026-09-14** — Faruk Alpay, Taylan Alpay — [Approval Integrity and Recovery in LLM Answer Publication](http://arxiv.org/abs/2609.15576v1)
  <details><summary>📄 Abstract</summary>
  Publication integrity in LLM systems requires binding approved content to its current authorization context. We examine exact-content binding, authorization freshness and checkpoint recovery in Lightcap's publication enforcement mechanism. On 900 independently human-annotated RAGTruth responses from 150 source tasks, three dated Ministral models and a same-model direct-grounding baseline yield 3,600 assessments. The production response-act checker instantiated with 14B accepts 291 of 302 unsuppo...
  </details>

- **2026-09-14** — Yusuf Khalid Shire, Sang-Chul Kim — [PIDS-Bench: Evaluating Prompt-Injection Detectors Under Over-Defense, Obfuscation, and Distribution Shift](http://arxiv.org/abs/2609.15017v1)
  <details><summary>📄 Abstract</summary>
  Prompt-injection detectors are typically evaluated using aggregate F1 on in-distribution test data, which offers limited insight into behavior under distribution shift, particularly on the benign side of the decision boundary, where false positives impose direct operational cost yet are seldom measured. We present PIDS-Bench, a frozen multi-axis benchmark that jointly evaluates attack detection and benign false-positive behavior at fixed thresholds, spanning in-distribution inputs, hard-benign p...
  </details>

- **2026-09-14** — Bingzheng Wang, Xiaoyan Gu, Wentao Wang et al. — [ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents](http://arxiv.org/abs/2609.14987v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents interact with external environments through tool invocation, but tool outputs can also expose them to indirect prompt injection (IPI) attacks. Existing defenses mainly rely on prompt hardening, content filtering, pre-generated plans, or permission constraints. These approaches often struggle with complex tasks or over-sanitize external content, making it difficult to balance security and utility. The key challenge is therefore to preserve execution flexibility w...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-09-15** — Yunpeng Xiong, Ting Zhang — [After the Party: Growth, Governance, and Security Scanning in the OpenClaw Agent Skill Ecosystem](http://arxiv.org/abs/2609.17274v2)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act through agent skills, i.e., natural-language instructions, that direct a host agent toward shell, network, credential, file, and process actions, and public registries distribute them at scale. In the first half of 2026, the OpenClaw AI agent went viral, and its public skill registry boomed: the observable stock nearly doubled in 91 days, and a majority of the listings visible in June were created in just two months. By the end of our study window, the wave had crested...
  </details>

- **2026-09-15** — Yunpeng Xiong, Ting Zhang — [After the Party: Governing What a Viral Agent-Skill Ecosystem Left Behind](http://arxiv.org/abs/2609.17274v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act through agent skills, i.e., natural-language instructions, that direct a host agent toward shell, network, credential, file, and process actions, and public registries distribute them at scale. In the first half of 2026, the OpenClaw AI agent went viral, and its public skill registry boomed: the observable stock nearly doubled in 91 days, and a majority of the listings visible in June were created in just two months. By the end of our study window, the wave had crested...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 10 papers

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

- **2026-09-15** — Jiachang Zhang, Min Chen, Xiao Ren et al. — [InceptionRAG: Stealthy Poisoning Attack Against Retrieval-Augmented Generation](http://arxiv.org/abs/2609.16818v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) systems enhance large language models (LLMs) with external knowledge but have been demonstrated to be vulnerable to corpus poisoning. Existing poisoning attacks against RAG largely focus on single-point explicit injection, where the malicious payload is fully encapsulated within a single document. Consequently, recent mitigation mechanisms have evolved to identify and diminish these threats effectively. In this paper, we first verify that existing mitigation ...
  </details>

- **2026-09-15** — Zhipeng Zhao, Zhaoqiang Wei, Peishun Liu et al. — [ViD: Vision-Dominant Gender Bias Mitigation for Large Vision-Language Models](http://arxiv.org/abs/2609.16647v1)
  <details><summary>📄 Abstract</summary>
  Gender bias in large vision-language models (LVLMs) undermines their fairness and reliability, compromising output trustworthiness. Current mitigation methods rely on training-phase adjustments or post-hoc calibration, but face limitations in dynamic visual bias mitigation. These include inability to capture real-time visual-textual incongruence, dependence on predefined gender bias taxonomies, and degraded cross-modal alignment with emergent bias patterns. To address these challenges, we propos...
  </details>

- **2026-09-14** — Roberto Riaño, Gorka Abad, Stjepan Picek et al. — [When the World Lies: Backdoor Attacks on Latent World Models for Downstream Control](http://arxiv.org/abs/2609.15781v1)
  <details><summary>📄 Abstract</summary>
  Pretrained world models, learned simulators that encode an observation into a latent state and predict how it evolves under actions, are beginning to be reused as off-the-shelf dynamics backbones for control, like pretrained encoders and language models are reused today. We show that this reuse opens a supply-chain backdoor: an adversary who controls only a released checkpoint can hijack the downstream controller, even though the victim trains and evaluates entirely on clean data and never sees ...
  </details>

- **2026-09-14** — Aashiq Muhamed, Mona T. Diab, Virginia Smith et al. — [Pick Your Poison: Learning to Select Poison Sets for Stronger LLM Backdoor Attacks](http://arxiv.org/abs/2609.15029v1)
  <details><summary>📄 Abstract</summary>
  Backdoor poisoning attacks add poisoned examples to otherwise-clean finetuning data, pairing a trigger with a target behavior that the model learns to produce when the trigger appears. Existing evaluations typically fix the number of poisoned examples and sample them at random from a candidate pool. We show that this can severely underestimate worst-case vulnerability: across three LLaMA-3-8B backdoor settings, holding the model, clean data, and poison count fixed, attack success ranges from 3% ...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 6 papers

- **2026-09-16** — Makram Chehayeb, Walid Fahs, Amina Rizk et al. — [A GAN-Based Framework for Robust DDoS Attack Detection](http://arxiv.org/abs/2609.18281v1)
  <details><summary>📄 Abstract</summary>
  The availability and consistency of online services remain vulnerable due to Distributed Denial of Service (DDoS) attacks. These attacks are evolving by adopting more complex strategies to evade traditional network security systems. Despite the effectiveness of machine learning models in detecting DDoS traffic, targeted adversarial attacks can degrade their classification accuracy. This work proposes a robust detection framework that integrates generative adversarial modelling with advanced mach...
  </details>

- **2026-09-15** — Chenyi Wang, Yutong Liu, Qingzhao Zhang et al. — [Investigating Adversarial Robustness of Heterogeneous Cooperative Perception](http://arxiv.org/abs/2609.17856v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous cooperative perception (CP) enables connected vehicles with diverse sensor setups to share spatial awareness via compact feature maps, where receivers reconcile these maps using learned translation modules for fusion and inference. Prior attacks against CP in a homogeneous setting reveal that the data exchange introduces a critical attack surface: a single malicious agent can transmit crafted features that erase real objects from a neighbor's fused scene. Yet, it is widely hypothes...
  </details>

- **2026-09-15** — Kairong Li, Zhikun Zhang, Xiao Ren et al. — [MarkSec: Capability-Aware Evaluation of Adversarial Attacks Against LLM Watermarks](http://arxiv.org/abs/2609.16681v1)
  <details><summary>📄 Abstract</summary>
  LLM watermarking helps trace the origin of generated text, but faces stealing attacks that recover watermark information, scrubbing attacks that remove watermark signals, and spoofing attacks that forge text accepted as watermarked. These attacks are often studied in isolation, leaving their connections unclear. Evaluations also often lack shared detector calibration, metric definitions, and reporting protocols. Moreover, measuring attack success and text quality separately makes it difficult to...
  </details>

- **2026-09-14** — Pingzhi Li, Jinhao Duan, Vaishnav Tadiparthi et al. — [Test-Time Unlearning via Sparse Autoencoder](http://arxiv.org/abs/2609.16229v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning aims to remove specific knowledge from a trained large language model (LLM) without retraining from scratch. Existing methods modify model weights via gradient ascent and its advances. While effective on certain benchmarks, these weight-based approaches exhibit a sharp forget-utility trade-off, where stronger forgetting of target knowledge can degrade model utility, and unlearned knowledge may reappear under post-unlearning fine-tuning or prompt attacks. We propose ARIA (autoe...
  </details>

- **2026-09-14** — Fares Trad, Simin Chen, Hung Viet Pham et al. — [Adversarial Testing of Automated Program Repair Agents for Security Vulnerabilities](http://arxiv.org/abs/2609.15963v1)
  <details><summary>📄 Abstract</summary>
  Software agents with Large Language Models (LLMs) are designed for Automated Program Repair (APR) tasks, raising the possibility that, in the near future, APR agents will fix bugs automatically without much human intervention. Can we trust an APR agent to produce both functionally correct and secure code in such situations? What if attackers target production APR agents with adversarial issues that seem benign but may influence the agents to produce correct but insecure code? In this paper, we t...
  </details>

- **2026-09-14** — Paul Stahlhofen, Luca Hermes, Tim Kochs et al. — [Admissable: Training Reinforcement Learning Agents against Adversarial Missingness](http://arxiv.org/abs/2609.15297v1)
  <details><summary>📄 Abstract</summary>
  In order to make Reinforcement Learning algorithms applicable in real world scenarios, safety must be ensured even under adverse operating conditions. In this work, we consider the challenge of adversarial feature missingness: a scenario in which an adversary occludes features from the agent's observation in order to reduce performance as much as possible. We formally define adversarial missingness for Reinforcement Learning and compare it to the related concepts of $\ell_\infty$-norm bounded ad...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 29 papers

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

- **2026-09-15** — Qiangju Chen, Yang Xiao — [Beyond the Name: Demographic Leakage in De-Identified Résumés and Evaluation Artifacts in LLM Bias Audits](http://arxiv.org/abs/2609.16501v1)
  <details><summary>📄 Abstract</summary>
  De-identified résumé screening assumes that redacting explicit fields prevents ethnocultural inference; however, recent audits attribute residual leakage to declared languages. We investigate whether eliminating language fields resolves this leakage across nine open-weight models and 620 counterfactual résumés. By holding language attributes strictly identical, we isolate unstructured prose across five ethnocultural conditions and three cue-salience tiers. Target-group recovery averages 0.757 ov...
  </details>

- **2026-09-15** — Xin Quan, Reto Gubelmann, André Freitas — [Autoformalizing Argumentative Material Inferences](http://arxiv.org/abs/2609.16991v1)
  <details><summary>📄 Abstract</summary>
  Natural language arguments are compelling before they are formally explicit. A premise supports a claim through defeasible warrants, background commitments, and exception conditions that the text leaves implicit. However, formal verification requires the opposite. Making such arguments machine-checkable requires constructing the missing commitments, not only translating given sentences into logic. Construction, however, carries a risk that translation does not: a system free to add premises can ...
  </details>

- **2026-09-15** — Yichi Zhang, Shenyue Wang, Jing Luo et al. — [Affect-Prototype Guided Fusion for Open-Vocabulary Incomplete Multi-modal Emotion Recognition](http://arxiv.org/abs/2609.16962v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary multimodal emotion recognition (OV-MER) aims to generate open natural-language emotion labels from multimodal affective cues. In real-world scenarios, however, complete and synchronized modal data are difficult to obtain due to limitations of acquisition devices and user privacy constraints. Existing OV-MER methods are largely designed for full-modal inputs, and fail to perform effective feature fusion under modal missing conditions. Meanwhile, current fusion approaches designed ...
  </details>

- **2026-09-15** — Jiangrui Yu, Baosheng Zhang, Liang Kong et al. — [ROSETTA: Efficient and Accurate Privacy-Preserving LLM Decoding via Hybrid CKKS/TFHE Evaluation](http://arxiv.org/abs/2609.16915v1)
  <details><summary>📄 Abstract</summary>
  Generative large language models (LLMs) have achieved state-of-the-art performance on many real-world tasks such as code generation and question answering. These models predominantly rely on an autoregressive decoding strategy that generates output tokens sequentially. However, their pervasive deployment raises serious privacy concerns, motivating private inference frameworks based on fully homomorphic encryption (FHE). A major limitation of existing FHE frameworks is their inefficiency in evalu...
  </details>

- **2026-09-15** — Qingchen Yu, Shiying Duan, Xiaodong Li et al. — [Cascade: Hierarchical Recoverability Control for Large Language Model Unlearning](http://arxiv.org/abs/2609.16890v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) unlearning is essential for removing sensitive or copyrighted knowledge while preserving general utility. Existing methods often leave residual knowledge in intermediate representations, which can still be recovered. To address this, we propose Cascade, a hierarchical recoverability control framework that minimizes the internal identifiability of target knowledge. Cascade combines three complementary controls: path-level routing to suppress privacy-associated activatio...
  </details>

- **2026-09-15** — Wanchao Chen, Wen Li, Yanan He et al. — [SaltyMeta: a curated benchmark and protein language model-informed web tool for salty peptide prediction](http://arxiv.org/abs/2609.16809v1)
  <details><summary>📄 Abstract</summary>
  Excess sodium intake remains a major public health challenge, while salty and saltiness-enhancing peptides offer a potential route to preserve sensory saltiness in reduced-sodium foods. Machine-learning studies of salty peptides, however, are constrained by small datasets, heterogeneous evidence standards, uncertain negative labels, and sequence similarity leakage. Here we present SaltyMeta, a curated benchmark and web-accessible screening framework for salty or saltiness-enhancing short peptide...
  </details>

- **2026-09-15** — Bernie Boscoe, Srinath Saikrishnan, Vikram Seenivasan et al. — [AquiLLM: Evaluating Faithfulness in Open-Weight RAG-LLM Systems for Scientific Research](http://arxiv.org/abs/2609.16519v1)
  <details><summary>📄 Abstract</summary>
  Scientific research increasingly relies on large, heterogeneous data sources, motivating interest in retrieval-augmented generation (RAG) systems that provide natural language access to scientific knowledge and research workflows. Researchers are exploring the viability of these systems as natural language interfaces for document search and for generating analysis code and pipeline components. At the same time, concerns about data privacy and control over research infrastructure have motivated i...
  </details>

- **2026-09-14** — Xingyu Lyu, Jiayimei Wang, Jianfeng He et al. — [RAG-CT: Mitigating Privacy Risks on Retrieval-Augmented Generation Systems via Scanning Prompt Distribution](http://arxiv.org/abs/2609.16095v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm for improving the quality of generated contents of Large Language Models (LLMs) by grounding responses in external knowledge, thus reducing hallucinations and factual errors. However, recent studies have highlighted a critical vulnerability: adversaries can exploit the retrieval process to extract personally identifiable information (PII) from the underlying corpus. To mitigate this risk, we propose a novel defense, RAG-CT, ...
  </details>

- **2026-09-14** — Maya Subramanian, Devika Jain — [Toward Governance-Aware Autonomous GIS: A Narrative Review of Ethical and Privacy Risks in LLM-Enabled GeoAI](http://arxiv.org/abs/2609.16232v1)
  <details><summary>📄 Abstract</summary>
  Geospatial artificial intelligence (GeoAI) powered by large language models (LLMs) is expanding the capacity to query, generate, and interpret spatial information through natural-language interfaces and agentic autonomous GIS workflows. This capability creates governance challenges that general AI ethics discussions do not fully capture, including passive location inference from mobility traces, spatially structured bias amplification driven by spatial autocorrelation and scale effects, hallucin...
  </details>

- **2026-09-14** — Behrooz Razeghi — [Differentially Private Semantic Plans for Aggregate Insight Generation](http://arxiv.org/abs/2609.16283v1)
  <details><summary>📄 Abstract</summary>
  \texttt{URANIA} provides end-to-end differential privacy (DP) for summaries of data-dependent clusters. However, its cluster--keyword release does not directly provide collection-wide aggregates for semantic concepts defined independently of the protected corpus. Records may express several concepts, records expressing the same concept may be assigned to different clusters, and cluster identities need not correspond across analyses. Consequently, cluster-level statistics do not directly provide ...
  </details>

- **2026-09-14** — Abayomi O. Agbeyangi, Jose M. Lukose — [AI-Driven Feedback Systems, Digital Labour, and Silent Quitting: Transforming African Workplaces](http://arxiv.org/abs/2609.16192v1)
  <details><summary>📄 Abstract</summary>
  The current trend of digitalisation has revolutionised the organisation of work and the way it is measured and performed across the globe, with AI becoming more common for managing labour and performance, as well as employee communication. In African organisations, where there is increasing adoption of remote work, hybrid models of work, digital collaboration, and data-based HR management, the notion of silent quitting has become more relevant, defined as worker disengagement when employees are ...
  </details>

- **2026-09-14** — Bhaskar Mitra, Soumya Kundu — [Distributed Edge-to-Cloud Architecture for Continual Harmonic Load Modeling](http://arxiv.org/abs/2609.16185v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of power electronic loads at the distribution grid edge has made accurate harmonic load modeling critical for power quality assessment, transformer derating, and grid planning. Existing Frequency Coupling Matrix (FCM) identification methods produce static, one-time models that rapidly lose fidelity as load composition evolves. This paper proposes a distributed edge-to-cloud architecture for autonomous, continual FCM re-identification under real field conditions, with two ...
  </details>

- **2026-09-14** — Md Khalid Syfullah, Alvi Ataur Khalil — [Don't Send What You Don't Need: Question-Guided Token Pruning as a Privacy Defense for Vision-Language Models](http://arxiv.org/abs/2609.15671v1)
  <details><summary>📄 Abstract</summary>
  Visual Question Answering (VQA) with Vision-Language Models (VLMs) is increasingly used in privacy-sensitive and bandwidth-constrained settings. Federated Learning (FL), Split Learning (SL), and U-Shaped Split Learning (USL) keep raw data local, but transmitting all visual tokens across a model partition remains costly and can expose private information. We propose QPriv-VL, a question-guided, privacy-aware token-pruning framework for FL, SL, and USL that prunes visual tokens before transmission...
  </details>

- **2026-09-14** — Pengwei Wang, Zihan Wang, Hangcheng Cao et al. — [CounterPersona: Append-Only Defense Against Unauthorized Persona Skill Distillation](http://arxiv.org/abs/2609.15097v1)
  <details><summary>📄 Abstract</summary>
  Persona skill distillation can extract recurring patterns from personal information and encode them into reusable skills, enabling AI systems to closely replicate an individual's behavior. However, such replication also raises serious concerns regarding personal privacy and labor autonomy. Unlike existing perturbation-based defenses that require individuals to modify their data before collection, once historical records are collected by an attacker, they can no longer be altered, sanitized, or r...
  </details>

- **2026-09-14** — Shashie Dilhara Batan Arachchige, Robin Carpentier, Hassan Jameel Asghar et al. — [SpliTEE: Improving LLM Inference on Trusted Hardware with Differentially Private GPU Outsourcing](http://arxiv.org/abs/2609.15039v1)
  <details><summary>📄 Abstract</summary>
  User prompts provided to large language models (LLMs) may contain sensitive or private information that can be misused by remotely deployed models, such as through inadvertent memorization during retraining. One way to protect user prompts is to execute the LLM inside a trusted execution environment (TEE), with the guarantee that the service provider has no access to computations performed within or information exchanged with the TEE. However, current TEEs are primarily CPU-based and significant...
  </details>

- **2026-09-14** — Wen Hu, Ya Yu, Xutong Wang — [Reversibility-Verified De-identification for Cloud-Local LLM Inference: A Locally Certified Dehydrate-Rehydrate Loop with Layered Assurance (DR-SL)](http://arxiv.org/abs/2609.14883v1)
  <details><summary>📄 Abstract</summary>
  Cloud-local LLM inference must keep sensitive user data on-device while exploiting cloud-grade reasoning, yet existing sanitization approaches (placeholder substitution, differential-privacy perturbation, and skill distillation) lack a release decision that is simultaneously safe and utility-preserving. We propose DR-SL (Dehydrate-Rehydrate with Self-Learning loop), which formalizes de-identification completeness as two measurable conditions: de-identification sufficiency under Pufferfish semant...
  </details>

- **2026-09-14** — Paul-Gabriel Nicolae, Irina Georgiana Mocanu — [Anatomical Grounding and Leakage-Aware Multimodal Contrastive Learning for Alzheimer's Disease Classification from Structural MRI](http://arxiv.org/abs/2609.15888v1)
  <details><summary>📄 Abstract</summary>
  Deep networks trained on structural MRI for Alzheimer's disease (AD) staging often reach reasonable accuracy while attending to anatomically irrelevant regions, and multimodal models that add clinical tables frequently rely on variables that were used to assign the diagnostic label in the first place. We study both issues with a deliberately lightweight slice-based encoder (ResNet18 with a one-layer Transformer over slices) on 1,075 baseline T1-weighted scans from ADNI-1. First, we use FastSurfe...
  </details>

- **2026-09-14** — Wenxin Xu, Jinwei Lu, Hwanhee Kim et al. — [VisInteract: Towards Dynamic Interactive Text-to-Visualization under Imperfect Queries](http://arxiv.org/abs/2609.15182v1)
  <details><summary>📄 Abstract</summary>
  Real-world visualization requests are routinely ambiguous, incomplete, or factually incorrect, yet existing Text-to-Visualization (Text-to-Vis) systems assume well-specified inputs and produce charts in a single pass. When queries are imperfect, a system must \emph{interact} with the user to recover the true intent, but no benchmark or method supports this dynamic process. We introduce \textbf{VisInteract}, a new paradigm that reframes Text-to-Vis as interaction-driven intent recovery, and \text...
  </details>

- **2026-09-14** — Md Khalid Syfullah, Alvi Ataur Khalil — [LLM-Based Schema-Aware Split Learning for Privacy-Preserving Mental Distress Prediction Across Heterogeneous Surveys](http://arxiv.org/abs/2609.15871v1)
  <details><summary>📄 Abstract</summary>
  Rising societal and lifestyle complexity has been linked to a growing prevalence of mental distress worldwide. Educational institutions, workplaces, clinics, etc. collect large volumes of mental health survey data to understand and reduce this burden. Collaborative analysis of such data could yield effective generalizable predictive models. Privacy constraints and varied survey designs (i.e., different questions, scales, and formats) hinder direct integration. We propose a schema-aware split lea...
  </details>

- **2026-09-14** — Jigang Duan, Heran Wang, Ligen Shi et al. — [TRACE: Two-Stage Detector-Response Estimation With Angular Cosine Expansion for Ring Artifact Correction in Photon-Counting CT](http://arxiv.org/abs/2609.15834v1)
  <details><summary>📄 Abstract</summary>
  Detector response nonuniformity introduces systematic projection errors and ring artifacts in photon-counting detector computed tomography (PCD-CT). In measured PCD-CT data, residual stripe amplitudes vary slowly with projection angle, which fixed-bias models cannot adequately capture. We propose TRACE, a two-stage unsupervised sinogram decomposition method for estimating and correcting these response-related errors. TRACE represents stripes as a fixed bias plus low-order discrete cosine transfo...
  </details>

- **2026-09-14** — R. Oguz Araz, Xavier Lizarraga, Xavier Serra et al. — [Building a Dataset for Music Sample Identification](http://arxiv.org/abs/2609.15465v1)
  <details><summary>📄 Abstract</summary>
  Sample identification (SI) is the task of matching an element of a musical work to its musically transformed versions used to create new works. The task has received little attention and lacks large-scale publicly available data. In this work, we mine sampling annotations from a music database and split them for training and evaluation. The resulting dataset is nearly three orders of magnitude larger than the existing SI benchmarks, with training, validation, and test sets of 114 k, 6 k, and 10 ...
  </details>

- **2026-09-14** — Max Dupré la Tour — [Differentially Private Multicolor Discrepancy and Fair Division of Indivisible Goods](http://arxiv.org/abs/2609.15372v1)
  <details><summary>📄 Abstract</summary>
  We study the fair division of indivisible goods under pure differential privacy, continuing the line of work initiated by Manurangsi and Suksompong. For $n$ agents with nonnegative additive utilities over $m$ goods and a fixed privacy parameter, we give an entry-private algorithm that, with high probability, achieves consensus envy-freeness up to $O(\sqrt n+\log^3 m)$ goods. This substantially improves the dependence on $n$ over the previous $O(n\log m)$ guarantee for ordinary envy-freeness, whi...
  </details>

- **2026-09-14** — Jianhua Jiang, Dongbo Yuan, Weihua Li — [MemRiskBench: Trace-Aware Risk-Preserving Evaluation for Long-Horizon LLM Agents](http://arxiv.org/abs/2609.14976v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM agents accumulate memory across sessions, creating sparse but high-impact risks: stale facts, conflicting updates, cross-user leakage, revoked-memory reuse, and constraint decay. Standard aggregate scores hide per-risk failure rates--a model achieving 78% average accuracy may still leak data in 4% of episodes--and benchmark compression preferentially discards the rare high-severity events that distinguish a mostly-working model from one that occasionally causes harm. We present ...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 2 papers

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

- **2026-09-15** — Tapan Chugh, Vidushi Singh, Krish Jain et al. — [Agentic Societies Need a Social Harness](http://arxiv.org/abs/2609.17527v1)
  <details><summary>📄 Abstract</summary>
  An agentic society is a collection of AI agents that coordinate autonomously across trust boundaries, on behalf of different principals whose objectives may only partially align. We show experimentally that in agentic societies even honest, competent agents often fail to reach satisfactory outcomes with existing harnesses and messaging primitives, and that faulty or malicious agents can stall collaboration, influence outcomes, and pursue other harmful goals by exploiting vulnerabilities in commu...
  </details>

- **2026-09-15** — ZhuoXin Liu, Zhiming Ma, Ying Zhang et al. — [RiskChainBench: A Benchmark for Obfuscated Platform Message Restoration and Evidence-Grounded Web Investigation](http://arxiv.org/abs/2609.16900v1)
  <details><summary>📄 Abstract</summary>
  Platform abuse campaigns conceal redirection instructions with emojis, homophones, character decomposition, and redundant symbols, then route users through disguised links to services associated with pornography, fraud, gambling, or illicit transactions. Existing benchmarks evaluate obfuscated text and risky webpages separately, obscuring how target recovery affects downstream evidence acquisition. We introduce RiskChainBench, pairing 3,600 synthetic token-text restoration inputs from 600 source...
  </details>

- **2026-09-15** — Md Rayhanul Masud, Md Rizwan Parvez — [TAME: Token Attribution and Masking for Emergent misalignment](http://arxiv.org/abs/2609.16754v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning an aligned language model on narrow, flawed data can induce harmful behavior far outside the training domain, known as emergent misalignment (EM). Prior work has localized EM in model weights, activations, and training documents, but it remains unclear which training tokens carry the relevant fine-tuning signal. We introduce TAME (Token Attribution and Masking for Emergent Misalignment), a three-stage framework: token attribution scores how strongly the fine-tuning update raises each...
  </details>

- **2026-09-15** — Zhihao Guo, Zonghan Wu, Haizhou Du et al. — [Right Direction, Wrong Step: Geometric Analysis of Finite-Step Failure in Looped Transformers](http://arxiv.org/abs/2609.16665v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers offer a parameter-efficient route to test-time scaling by reusing shared layers for iterative latent reasoning. However, additional iterations can reduce support for a reference answer, leaving unclear whether an update's direction is locally unhelpful or its full displacement moves too far. We study this distinction by analysing reference utility, which measures this support, along the model's own update direction, varying the fraction of the proposed displacement supplied t...
  </details>

- **2026-09-14** — Jun He, Deying Yu — [Cognitive Admission Control: Risk-Conditioned Assurance for Consequential Actions in Agentic Distributed Systems](http://arxiv.org/abs/2609.16313v1)
  <details><summary>📄 Abstract</summary>
  In agentic distributed systems, an agent may be authorized to mutate external infrastructure while lacking evidence that the mutation is ready to execute. Cognitive Admission Control (CAC) makes this evidence requirement explicit. A policy maps a typed action and its modeled risk to assurance obligations specifying predicates, evidence classes, scope, freshness, and witness-set constraints. A deterministic evaluator distinguishes satisfied, violated, and unresolved obligations; unresolved condit...
  </details>

- **2026-09-14** — Laura M. Vowels, Matthew J. Vowels, Shivali Sharma et al. — [K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations](http://arxiv.org/abs/2609.15855v2)
  <details><summary>📄 Abstract</summary>
  People increasingly use large language models (LLMs) for mental health support, yet their safety in evolving, high-risk conversations remains poorly characterised. We developed K-Bench, a clinician-calibrated, protected benchmark evaluating 125 model configurations representing 33 base models from 14 providers across a fixed cohort of 200 multi-turn vignettes involving suicide, self-harm, domestic violence, substance misuse, and no-risk presentations. Synthetic patient conversations showed subst...
  </details>

- **2026-09-14** — Keertana Chidambaram, Andrew Ilyas, Vasilis Syrgkanis — [Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection](http://arxiv.org/abs/2609.15989v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring is a safety strategy where the reasoning of a large language model "actor" is inspected by a "monitor" (often another language model) for signs of unsafe planning, deception, or misalignment. We find that planting harmful but benign-sounding reasoning in the actor's context can steer it to perform adversarial actions while evading monitors, an attack we term "plan injection". We initially discover this attack in the multiple-choice question-answering monitorabil...
  </details>

- **2026-09-14** — Laura M. Vowels, Matthew J. Vowels, Shivali Sharma et al. — [K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations](http://arxiv.org/abs/2609.15855v1)
  <details><summary>📄 Abstract</summary>
  % !TEX root = ../main.tex People increasingly use large language models (LLMs) for mental health support, yet their safety in evolving, high-risk conversations remains poorly characterised. We developed K-Bench, a clinician-calibrated, protected benchmark evaluating 125 model configurations representing 33 base models from 14 providers across a fixed cohort of 200 multi-turn vignettes involving suicide, self-harm, domestic violence, substance misuse, and no-risk presentations. Synthetic patient ...
  </details>

- **2026-09-14** — Mohammed Ahnouch, Lotfi Elaachack — [Semantic Fibers and Cross-Gram Interference: A Calculus of Safety Drift in Overcomplete Representations](http://arxiv.org/abs/2609.14861v1)
  <details><summary>📄 Abstract</summary>
  A deployed language model may refuse a harmful request in English yet comply with its faithful translation, revealing a cross-lingual safety failure that cannot be characterized reliably by output behavior alone. We formalize this phenomenon through an audited equivalence relation and show that, for a declared quotient, representation, metric, feature dictionary, scoring head, threshold, and contrast model, the resulting safety drift admits an exact linear-algebraic characterization. Specificall...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-09-15** — Zhuoang Cai — [Benchmarking Factual Robustness of LLMs via Multi-conversation Persuasion](http://arxiv.org/abs/2609.16777v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) increasingly serve as primary knowledge retrieval interfaces, their robustness against \textit{persuasion attacks}---attempts to inject misinformation or enforce counterfactuals---has become a critical safety concern. Existing red-teaming frameworks typically evaluate models in multi-turn dialogues where the target model retains full conversation history. We identify a critical flaw in this setting termed \textbf{``Refusal Inertia''}: a model's initial refusal oft...
  </details>

- **2026-09-15** — Jakob Nyberg, Teodor Sommestad, Andrei Buhaiu et al. — [A Cyber Range Evaluation of Autonomous Network Incident Response Agents](http://arxiv.org/abs/2609.16541v1)
  <details><summary>📄 Abstract</summary>
  We test the performance of agents for automated network intrusion response in a cyber range intended for human operator training. The range implements an emulated networking environment with a variable network topology, red-team emulation and simulated user agents. The goal of the defensive agents is to prevent hosts in the network from being accessed by the red-team agent, while minimizing the availability costs induced from defensive measures. Alerts are generated using a SIEM platform and map...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 55 papers

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

- **2026-09-15** — Lehao Lin, Yuheng Cheng, Guolong Liu et al. — [QART: A Quantum-Classical Hybrid Architecture for Long-Horizon Reasoning -- Exploring a Conditional Path toward Quantum Scaling](http://arxiv.org/abs/2609.16887v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon reasoning is vulnerable to early errors that compromise later decisions. We present QART, the Quantum-Augmented Reasoning Transformer, a quantum--classical hybrid architecture combining a backbone language model with quantum encoding, CIM-based QUBO optimization, and quantum decoding. Semantic information can come from hidden representations or model-generated text; detailed encoding and optimization procedures remain proprietary. Under explicit assumptions, we establish a condition...
  </details>

- **2026-09-15** — Kai Yao, Bence Szilágyi, Sebestyén Kamp et al. — [What Breaks Local Watermarks? A Robustness Benchmark for Local Invisible Image Watermarking](http://arxiv.org/abs/2609.16832v1)
  <details><summary>📄 Abstract</summary>
  Local image watermarking embeds an invisible signal into selected image regions rather than spreading it across the entire image, enabling payload recovery from specific objects or regions without perceptibly altering the image. Existing studies evaluate the robustness of payload recovery and localization under image transformations, but they often focus on their own proposed method, resulting in narrow evaluations with inconsistent choices of transformations, datasets, and metrics. These incons...
  </details>

- **2026-09-15** — Bowen Qin, Yi Xie, Yesheng Liu et al. — [ImpossibleRubrics: Stress-Testing Generated Rubrics as Reward Signals](http://arxiv.org/abs/2609.16816v1)
  <details><summary>📄 Abstract</summary>
  Language model-generated rubrics are increasingly used as reward signals for rubric-based reinforcement learning, LLM-as-a-judge evaluation, and automated grading. Such rubrics are reliable only if they reward honest answers over adversarial answers optimized to exploit them. Yet their robustness to such optimization remains poorly understood. We isolate the hardest regime: impossible tasks, where the prompt pressures the model toward an unsupported conclusion, so the only honest response is to ...
  </details>

- **2026-09-15** — Simone Teglia, Irene Amerini — [Unifying Semantic Priors and High-Frequency Traces: Enhancing V-JEPA with Mixture-of-Experts for Robust Synthetic Image Forensics](http://arxiv.org/abs/2609.16778v1)
  <details><summary>📄 Abstract</summary>
  The unchecked proliferation of manipulated images on social media platforms has increased the spread of misinformation, posing a severe threat to public trust and information integrity. Modern deepfake detectors typically rely on Vision Transformers (ViTs) to capture the low-level inconsistencies that characterize fully synthetic or locally tampered images. However, the global understanding of such foundation models is not enough to discriminate alone between real and fake multimedia content, es...
  </details>

- **2026-09-15** — Heng Li, Fulin Zhao, Zhe Geng et al. — [When Agents See Differently: Exposing UI Desynchronization Threats in Mobile Agents](http://arxiv.org/abs/2609.16732v1)
  <details><summary>📄 Abstract</summary>
  Mobile agents are increasingly capable of autonomously interacting with mobile applications and performing consequential actions on behalf of users. Effective human oversight of such agents relies on a basic premise: users and agents observe consistent information from the same interface. We show that this premise can be systematically violated. Users perceive mobile interfaces through physical displays and the human visual system, making their observations subject to occlusion and luminance con...
  </details>

- **2026-09-15** — Rahul Dev T Y, Hiran V Nath — [Toward Secure AI-Powered Penetration Testing Agents: Security Threats, Guardrails, and Architectural Perspectives](http://arxiv.org/abs/2609.16694v1)
  <details><summary>📄 Abstract</summary>
  LLM-powered autonomous agents are transforming the penetration testing space with dynamic, multi-step offensive security workflows that require minimal supervision by humans. These agents leverage sophisticated reasoning abilities and external security tools to independently carry out reconnaissance, identify vulnerabilities, devise exploitation plans, and perform post-exploitation operations. But the ability to have persistent memory, to take actions in the real world, and to do long-horizon re...
  </details>

- **2026-09-15** — Qiyang Sun, Xudong Li, Yupei Li et al. — [CLASH: Counterfactual Auditing of Lexical and Prosodic Reliance in Spoken Sarcasm Detection](http://arxiv.org/abs/2609.16582v1)
  <details><summary>📄 Abstract</summary>
  Spoken sarcasm detectors may exploit lexical content, prosody, or their interaction, yet conventional evaluation cannot reveal which cues drive their predictions. We introduce CLASH (Controlled Lexical-Acoustic Separation Harness), a bilingual counterfactual diagnostic framework that evaluates each utterance under original, lexical-preserving, prosody-preserving, and approximately neutralised conditions. We evaluate handcrafted acoustic-feature systems, self-supervised learning (SSL) probes, and...
  </details>

- **2026-09-15** — Tung Le, Huy Tien Nguyen, Le Minh Nguyen — [Vision And Text Transformer For Predicting Answerability On Visual Question Answering](http://arxiv.org/abs/2609.16565v1)
  <details><summary>📄 Abstract</summary>
  Answerability on Visual Question Answering is a novel and attractive task to predict answerable scores between images and questions in multi-modal data. Existing works often utilize a binary mapping from visual question answering systems into Answerability. It does not reflect the essence of this problem. Together with our consideration of Answerability in a regression task, we propose VT-Transformer, which exploits visual and textual features through Transformer architecture. Experimental resul...
  </details>

- **2026-09-15** — Haoran Yang, Fei Chen, Yutian Xiao et al. — [ReliGRec: Reliability-Oriented LLM-Based Generative Recommendation via User-Risk-Aware Prompt Routing](http://arxiv.org/abs/2609.16560v1)
  <details><summary>📄 Abstract</summary>
  User behavior in real-world recommender systems is heterogeneous. While some users exhibit coherent preferences, others show abrupt interest shifts, bursty interactions, excessive repetition, or inconsistency with collaborative neighborhoods. Such deviations may arise from benign variation or manipulation, including shilling attacks, but do not alone establish malicious intent. Existing robust recommenders exploit user-risk signals through training-time reweighting or graph aggregation, whereas ...
  </details>

- **2026-09-15** — Yuchen Su, Zijian Huang, Yaotian Shi et al. — [PunGraph: Retrieval-Enhanced Phonetic-Semantic Graph Reasoning for Pun Understanding](http://arxiv.org/abs/2609.16557v1)
  <details><summary>📄 Abstract</summary>
  Puns are a challenging form of figurative language that exploit phonetic similarity and semantic ambiguity to convey multiple meanings. Although large language models (LLMs) demonstrate strong language understanding capabilities, they still struggle with pun reasoning due to limited phonetic modeling and uncontrolled end-to-end generation. We propose \textbf{PunGraph}, a retrieval-enhanced knowledge graph framework for pun understanding. PunGraph constructs a phonetic-semantic lexical graph usin...
  </details>

- **2026-09-15** — Vijay John, Amar Dabaja — [Multimodal Emergency Vehicle Classification via Audio-Visual Transformers and Knowledge Distillation](http://arxiv.org/abs/2609.16535v1)
  <details><summary>📄 Abstract</summary>
  Emergency vehicle detection in autonomous driving is a safety-critical perception task that demands robustness under diverse and adverse real-world conditions. Existing approaches rely on a single modality, either audio or video, which leads to systematic failure when that modality is degraded: microphone-based systems fail in noisy urban environments, and camera-based systems fail at night or under occlusion. This report presents AVNet, a multimodal audio-visual transformer that classifies emer...
  </details>

- **2026-09-14** — Satoshi Nakano, Kazuhiko Nishimura — [Computing Endogenous Transformations in Processing Networks: A Dynamic Calibration Approach](http://arxiv.org/abs/2609.15452v2)
  <details><summary>📄 Abstract</summary>
  Understanding how supply chains endogenously transform requires a parametric model of processing networks with non-neutral substitution elasticities. While the Cascaded CES production function provides a rigorous framework, dynamically calibrating its structural parameters from time-series data constitutes a highly non-convex inverse optimization problem. Since enforcing strict microeconomic concavity renders standard monolithic approaches computationally intractable, we propose a novel structur...
  </details>

- **2026-09-14** — Md Nazmul Hoque, Shaswata Mitra, Subash Neupane et al. — [Evaluating the NIST Bugs Framework Against CWE as a Successor for Automated Vulnerability Classification](http://arxiv.org/abs/2609.16433v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability classification based on root cause weaknesses is essential for numerous cybersecurity activities, where the Common Weakness Enumeration (CWE) serves as a public repository of such flaws. However, its overlapping entries create a non-orthogonal structure. The result is the same vulnerability being mapped to multiple weaknesses, complicating Root Cause Analysis (RCA) and triage. To address this, NIST Special Publication 800-231 introduces the Bugs Framework (BF), which organizes vuln...
  </details>

- **2026-09-14** — Ho Ting Hung, Angelica Chowdhury, James Teague et al. — [Mapping U.S. Federal AI Governance Against Sector Vulnerability](http://arxiv.org/abs/2609.16260v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) poses different levels of risk across sectors, but are these differences reflected in U.S. federal AI governance? To help answer this question, we assess 684 federal AI governance documents for their coverage of 14 sectors and 24 AI risks. We measure coverage as breadth (i.e., how frequently the risk or sector is addressed across documents) and depth (i.e., how substantively the risk or sector is discussed). We then compare sector coverage patterns for each of the 24...
  </details>

- **2026-09-14** — Shashank Chaurasia — [The World Model Hardware Accelerator](http://arxiv.org/abs/2609.16244v1)
  <details><summary>📄 Abstract</summary>
  Diffusion transformers invert the arithmetic that autoregressive decoding made familiar. There is no token-by-token recurrence: every denoising step is a full-sequence forward pass over static shapes, so the entire schedule is known at compile time and the only serial dimension is the step count itself. We exploit that structure in WMHA, a latency-first diffusion-transformer inference accelerator: a very-long-instruction-word sequencer issues four engines from one instruction word, a weight-stat...
  </details>

- **2026-09-14** — Bryce Cyr, Nabila Aghanim, Ethan Baker et al. — [Peering Beyond the Veil of Last Scattering: A View of the Universe with CMB Spectral Distortions](http://arxiv.org/abs/2609.16194v1)
  <details><summary>📄 Abstract</summary>
  The frequency spectrum of the cosmic microwave background is the most precise blackbody ever measured in nature, with deviations constrained at the level of almost one part per million from the COBE satellite. Nevertheless, departures away from a perfect blackbody are present in standard $Λ$CDM cosmology, lurking just beneath the surface of our current observational bounds. These spectral distortions provide invaluable information on our thermal history in both the post- and pre-recombination ep...
  </details>

- **2026-09-14** — Danny Wood, James Stringer — [Permutation-Based Stegomalware in Large Language Models: Threats and Countermeasures](http://arxiv.org/abs/2609.16193v1)
  <details><summary>📄 Abstract</summary>
  The difficulty of training large language models (LLMs), together with their ubiquity, raises the threat of stegomalware, where malicious payloads are embedded into model weights. Recent work has demonstrated the use of permutation symmetry in model weights to mitigate these threats, but failed to show neutralization of stegomalware across all weights for LLMs. In this paper, we demonstrate the full potential of behavior-preserving symmetries as a defense against stegomalware, as well as the ris...
  </details>

- **2026-09-14** — Sebastian Zhao, Minseo Kim, Coleman Hooper et al. — [LLM Inference in a Flash!](http://arxiv.org/abs/2609.16161v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown impressive capabilities across a range of natural language processing tasks, and LLM inference has emerged as a critical workload for enabling downstream applications. The demands of serving LLM inference are becoming increasingly challenging as requests shift toward longer sequences and heavier inference, driven by retrieval-augmented generation, inference-time compute scaling, and long-context applications. Additionally, these challenges are compounded b...
  </details>

- **2026-09-14** — Ashutosh P. Tripathi, Debasish Banerjee, Sandip Maiti et al. — [Investigating Interacting Fermionic Models with Locality-Preserving Qubit Encodings](http://arxiv.org/abs/2609.16142v1)
  <details><summary>📄 Abstract</summary>
  We investigate the utility of the locality-preserving Derby-Klassen (DK) fermion-to-qubit mapping [arXiv:2003.06939] for variational quantum simulation of two-dimensional $t$-$V$ and Fermi-Hubbard models. The DK mapping preserves the locality of fermionic interactions with an enlarged Hilbert space, thereby requiring additional constraints that define the physical sector. We incorporate these constraints directly into a Hamiltonian Variational Ansätz (HVA) through Clifford-gate state preparation...
  </details>

- **2026-09-14** — Aman Priyanshu, Supriti Vijay, Kimia Majd et al. — [Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale](http://arxiv.org/abs/2609.15939v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents increasingly operate over complete software repositories, yet cybersecurity evaluations primarily measure whether they can detect, reproduce, or repair vulnerabilities rather than whether they can locate the relevant code. We study vulnerability localization: given a weakness class and an unfamiliar repository, identify the implementation files associated with that weakness. We introduce the Vulnerability Localization Benchmark (VLoc Bench), comprising 500 real world vulner...
  </details>

- **2026-09-14** — Theodoros Moutesidis — [The Model Proposes, the Code Disposes: A Pre-Registered Ablation of a Verifier-and-Acceptance Stage in an LLM-Orchestrated Offensive-Security Agent](http://arxiv.org/abs/2609.15887v1)
  <details><summary>📄 Abstract</summary>
  We evaluate whether a verifier-and-acceptance stage - a model verifier whose verdicts are enforced by deterministic code - changes what an LLM-driven offensive-security agent reports. We report a 15-run exploratory pilot, a pre-registered 20-run confirmatory ablation, and a pre-registered 2 x 2 factorial study with 40 runs across two deliberately vulnerable lab targets. In the confirmatory study, removing the stage eliminated pre-report suppression (median 2 versus 0 findings per run; exact one-...
  </details>

- **2026-09-14** — Mingkai Liu, Hao Zhao, Xingxing Zuo — [SURE-Map: Self-Correcting Streaming Geometric Foundation Model](http://arxiv.org/abs/2609.15795v1)
  <details><summary>📄 Abstract</summary>
  Streaming geometric foundation models are emerging as a compelling alternative to SLAM systems. Yet this streaming nature introduces a fundamental issue: each prediction is made from limited context, which is vulnerable to dynamic objects and weak textures. Small local errors accumulate into severe geometric distortion and long-horizon scale drift. We argue that reliable streaming reconstruction requires geometric foundation models to be not only predictive, but also self-correcting. We introduc...
  </details>

- **2026-09-14** — Guo Fuzheng — [CiteShade: Citation Laundering in Multi-Source Retrieval-Augmented Generation and Its Counterfactual Defense](http://arxiv.org/abs/2609.15660v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) grounds a language model's answers on retrieved external knowledge and returns each answer with citations that identify its sources. Those citations are the user's audit trail: they let a reader verify a claim without trusting the model. Prior security work on RAG asks whether an attacker can corrupt the answer, leaving the citation channel unexplored. We show that this channel is a new and practical attack surface. We propose CiteShade, the first citation la...
  </details>

- **2026-09-14** — Oliver Stevanovic, Jasmin Wachter — [Automating Attack Graph Construction for Agentic Pentesting. Towards Neuro-Symbolic Vulnerability Hunting](http://arxiv.org/abs/2609.15523v1)
  <details><summary>📄 Abstract</summary>
  Logic attack graphs grounded in scanner output provide explicit and auditable attack path reasoning LLM-based agents lack. Integrating symbolic frameworks such as MulVAL to contemporary security workflows or agentic pipelines, however, requires translating scanner evidence to initial facts, and creating domain-specific rules. We present a semi-automated pipeline that addresses this interoperability problem and depict its feasibility in a web-security case study. Our pipeline parses findings from...
  </details>

- **2026-09-14** — Tianyi Li, Simon Geirnaert, Bert De Smedt et al. — [Multiscale Gaussian-Mixture Modeling for HMM Post-Processing in Selective Auditory Attention Decoding](http://arxiv.org/abs/2609.15490v1)
  <details><summary>📄 Abstract</summary>
  Selective auditory attention decoding (sAAD) infers from electroencephalography (EEG) which speaker a listener attends to in multi-speaker scenarios. A widely used approach reconstructs the attended speech envelope from EEG, correlates it with candidate envelopes, and selects the speaker with the highest Pearson correlation. However, correlations in each decision window have high intrinsic variance, making per-window decisions unreliable, especially for short windows. Recent work introduced a hi...
  </details>

- **2026-09-14** — Satoshi Nakano, Kazuhiko Nishimura — [Endogenous supply-chain transformation via dynamically calibrated nonneutroelastic processing networks](http://arxiv.org/abs/2609.15452v1)
  <details><summary>📄 Abstract</summary>
  Understanding how supply chains endogenously transform requires a parametric model of processing networks with non-neutral substitution elasticities. While the Cascaded CES (CCES) production function provides a rigorous framework for these multi-layered linkages, dynamically calibrating its structural parameters from time-series data constitutes a highly non-convex inverse optimization problem. Enforcing the strict microeconomic concavity constraint causes standard monolithic approach to fail du...
  </details>

- **2026-09-14** — Halil Burak Noyan — [Empirical Evaluation of Task-Based Permission Scoping Architecture for AI Agents](http://arxiv.org/abs/2609.15422v1)
  <details><summary>📄 Abstract</summary>
  AI agents are provisioned the same as employee-owned hosts in many enterprise settings with a static credential set fixed at deployment which includes all permissions the employee role might ever need. Role-based access control made this compromise for human principals because scoping access per task was infeasible. For AI agents, the compromise leaves every credential standing exposed whether or not the current task uses them. These permissions can later be utilised by a compromised or misalign...
  </details>

- **2026-09-14** — Christian Fisch, Angela Altmeier, Martin Obschonka et al. — [Artificial entrepreneurial cognition: Locating and causally steering an opportunity recognition dial inside large language models (LLMs)](http://arxiv.org/abs/2609.15277v1)
  <details><summary>📄 Abstract</summary>
  Entrepreneurial cognition is a foundation of entrepreneurship research. Yet the growing involvement of large language models (LLMs) in entrepreneurial work extends the cognition question beyond human actors to systems whose internal representations remain largely unexplored. We introduce artificial entrepreneurial cognition, the functional organisation of entrepreneurship-relevant representations and computations inside artificial intelligence (AI) systems. We bring mechanistic interpretability ...
  </details>

- **2026-09-14** — Yang Chen, Lirong Che, Zhenyu Huang et al. — [HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness](http://arxiv.org/abs/2609.15195v1)
  <details><summary>📄 Abstract</summary>
  Embodied navigation requires agents to interpret visual observations, accumulate spatial knowledge, and execute actions to follow instructions or locate objects. Training-based methods face generalization challenges, while training-free methods exploit multimodal large language models (MLLMs) but often lack mechanisms to reconcile proposed actions with spatial evidence, task progress, and execution failures. We present HarnessVLN, a zero-shot, training-free framework whose Agent Harness coordina...
  </details>

- **2026-09-14** — Yuyao Sun, Tao Deng, Shuang Li et al. — [AdaVSkip: Adaptive Visual Token Skipping Across Layers For Efficient MLLMs Inference](http://arxiv.org/abs/2609.15131v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) require substantial computation to process numerous visual tokens across all transformer layers. Most methods for efficient MLLM inference exploit horizontal redundancy by compressing visual tokens. Beyond token reduction, recent studies exploit vertical redundancy through early exit or fixed-layer skipping. However, we find that the extent and distribution of this redundancy vary across inputs and differ between self-attention and MLP modules. Motivated ...
  </details>

- **2026-09-14** — Shuhao Han, Wenjie Liao, Hayden Vance et al. — [DNF-SR: Dual-Input and Negative-Aware Feature Fine-Tuning for Real-World Image Super-Resolution](http://arxiv.org/abs/2609.15120v1)
  <details><summary>📄 Abstract</summary>
  Benefiting from the powerful generative priors of diffusion models, diffusion-based real-world image super-resolution (Real-ISR) methods have demonstrated impressive performance.To achieve efficient Real-ISR, several recent works have designed one-step diffusion-based models.Howerver, unmediatedly feeding LR into a diffusion model creates a distributional gap with the model's original input.A straightforward approach to reduce the distribution gap is to introduce noise to the LR latents. However...
  </details>

- **2026-09-14** — Yi Chen, Rufeng Cheng, Qiang Xie et al. — [Generate to Explore, Select to Exploit: Aligning LLM-based Headline Generation with Personalized Recommendation](http://arxiv.org/abs/2609.15094v1)
  <details><summary>📄 Abstract</summary>
  In industrial recommendation feeds, presenting a static headline for an item often fails to satisfy the diverse, multimodal interests of the user population, particularly suppressing the needs of long-tail audiences. While Large Language Models (LLMs) have been integrated into recommendation for content understanding or ranking, directly optimizing them to output a single best headline typically leads to mode collapse---converging to generic patterns that satisfy average tastes but miss specific...
  </details>

- **2026-09-14** — Xu He, Chih-Hsuan Lin, Hung-Mao Chen et al. — [Overflip: Repetition-Induced Label Flips in Guardrail Models](http://arxiv.org/abs/2609.15013v1)
  <details><summary>📄 Abstract</summary>
  Guardrail models are classifiers deployed to screen malicious prompts and responses in LLM-based services. To meet latency constraints, many lightweight guardrails adopt compact Transformer backbones (e.g., DeBERTa) that are trained with short context windows (typically 512 tokens) and rely on bucketed relative positional encodings to process longer inputs. Prior evaluations assume that a guardrail's decision is stable as the input is lengthened. We show that this assumption can fail. We identif...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 61 papers

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

- **2026-09-15** — Jakob Nyberg, Sandor Berglund, Andrei Buhaiu et al. — [The MAL Simulator: Cyber Operations Simulation based on Attack & Defense Graphs](http://arxiv.org/abs/2609.16563v1)
  <details><summary>📄 Abstract</summary>
  We have developed the MAL Simulator, a cyber operation simulator based on the Meta Attack Language (MAL). The MAL Simulator is intended for decision-driven cyber attack and defense simulations, for system analysis and the development of automated agents. By building the simulator around an attack modeling language, it can be adapted to different target domains without modifying the source code. We used the simulator for two case studies where we trained two types of agents for automated cyber op...
  </details>

- **2026-09-15** — Xiaoyang Liu — [Self-Emergence Agent Architecture:Behavior-Inertia HMM, Reflexive Metacognition,and Social-Contrastive Self-Modeling](http://arxiv.org/abs/2609.17331v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents exhibit strong language-generation and problem-solving capabilities, yet suffer from three structural limitations: personality drift, non-evolutionary reflection, and the absence of a self-other boundary. Existing generative-agent simulations rely on static memory and fixed prompts, maintaining neither behavioral inertia nor endogenous self-evolution. We propose the Self-Emergence Agent Architecture (SEAA), which integrates three components: (i) a Hidden Markov ...
  </details>

- **2026-09-15** — Farzad Nadiri, Mehdi Cina, Ahmad B. Rad — [DriveMCP: An Agentic AI framework for Advanced Driver Assistance System](http://arxiv.org/abs/2609.17247v1)
  <details><summary>📄 Abstract</summary>
  An agentic AI driver-assistance framework that integrates perception, compliance reasoning, vehicle-state interpretation, and safety arbitration into a modular and auditable pipeline. The architecture, referred to as DriveMCP, incorporates a sensor-like perception stack alongside DriveLM as the vision-language front end to generate a graph-structured scene understanding (Graph Visual Question Answering) and language-grounded driving information. Key compliance elements in world_state, including ...
  </details>

- **2026-09-15** — Vsevolod Hulchuk, Jan Bayer, Jan Faigl — [LiLi: Lie Theory Based 3D LiDAR Scan Alignment Degeneracy Detection](http://arxiv.org/abs/2609.17145v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study 3D LiDAR scan alignment in challenging scenarios with degeneracies, such as straight corridors or flat fields, where the alignment solution is not unique and compromises localization and mapping accuracy. Existing degeneracy detection methods that neglect the potential for reassociating data points are prone to being sensitive to noise and complex degeneracies. Therefore, we propose LiLi - a novel method that leverages Lie theory to identify the full set of degenerate tra...
  </details>

- **2026-09-15** — Xiucheng Zhang, Zhuoning Xu, Hanjun Luo et al. — [ANIMASK: What the Model Contributes to Role Play in Simulated Story Worlds](http://arxiv.org/abs/2609.16667v1)
  <details><summary>📄 Abstract</summary>
  When a language model plays a character, the observed behavior reflects both the assigned persona and the default dispositions of the actor model itself. Existing evaluations test persona fidelity or model defaults in isolation, but neither says, at a specific choice with consequences, what the persona changed and what the model's default kept. We introduce ANIMASK, a simulation framework that freezes books and scripts into story worlds whose characters act on their own motivations and replays e...
  </details>

- **2026-09-15** — Harish Gaggar — [Protocol-Preserving Context Trimming for Agentic Workflows: Benefits, Failure Regimes, and Budget Guardrails](http://arxiv.org/abs/2609.16461v1)
  <details><summary>📄 Abstract</summary>
  Agentic large language model (LLM) systems rely on long interaction histories to preserve instructions, tool states, intermediate decisions, and unresolved dependencies, but unrestricted context growth increases computational cost and can reduce efficiency. This study evaluates protocol-preserving context trimming as a reliability-constrained approach for multi-step agentic workflows. Five trimming strategies - recency-based, relevance-based, summarization, protocol-aware trimming, and adaptive ...
  </details>

- **2026-09-15** — Claudio Ranucci, Sébastien Pierre, Léo Vacher et al. — [$B$-sure. Part II. Scattering transforms as robustness test for tensor-to-scalar ratio detection from CMB observations](http://arxiv.org/abs/2609.17531v1)
  <details><summary>📄 Abstract</summary>
  Galactic foregrounds represent a major contamination to the measurement of primordial $B$-modes from observations of the Cosmic Microwave Background polarisation. Even after the application of component separation algorithms, foreground residuals may potentially still bias the estimate of the tensor-to-scalar ratio $r$, causing a false detection. In this work, we present the methodology of a robustness test for the validation of an eventual detection of primordial $B$-modes, as obtained by a fut...
  </details>

- **2026-09-15** — Luciano Marchezan, Kevin Delcourt, Eugene Syriani et al. — [Type-IV Code Clone Detection via Layer-Wise Non-Contrastive Representation Learning](http://arxiv.org/abs/2609.17338v1)
  <details><summary>📄 Abstract</summary>
  Software clones are fragments of code that are similar or functionally equivalent to each other. They pose significant challenges for maintenance, refactoring, and bug detection. Detecting Type-IV clones, which are semantically equivalent but may differ syntactically, is particularly difficult for traditional token- or syntax-based methods. Recent machine learning approaches rely on contrastive learning, which requires careful negative sampling and can introduce bias. In this paper, we propose L...
  </details>

- **2026-09-15** — Jesús M. Fraile-Hernández, Anselmo Peñas, Patrick Giedemann — [Zero-shot narrative detection in social messaging](http://arxiv.org/abs/2609.17310v1)
  <details><summary>📄 Abstract</summary>
  This study investigates the zero-shot ability of large language models (LLMs) to identify and classify hidden narratives in social messages. Our research hypothesis is that LLMs' extensive contextual knowledge allows them to interpret messages on a deeper, pragmatic level, going beyond basic sentiment or topic analysis. Experiments on the Dipromats and SemEval datasets show that providing models with human-written narrative descriptions significantly improves performance, without the need of tra...
  </details>

- **2026-09-15** — Jiawei Gu, Qilin Zhao, Tengkuo Guo et al. — [Probe-VAD: Ordinal Likelihood Probing for Training-Free Video Anomaly Detection](http://arxiv.org/abs/2609.17211v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly detection (VAD) aims to localize anomalous events in untrimmed videos. Vision-language models (VLMs) provide rich visual understanding for training-free VAD, but existing approaches impose restrictive interfaces between visual understanding and anomaly scoring. Caption-based pipelines compress visual evidence into text, potentially discarding subtle cues, while direct numerical generation forces the model to express its judgment through a small set of predefined scores. Such interf...
  </details>

- **2026-09-15** — Minh Dat Nguyen, Gabriele Gemmi, Tamerlan Aghayev et al. — [Agentic RDZ: Autonomous Zone Management with AI Agents and an FR3 Coexistence Use Case](http://arxiv.org/abs/2609.17110v1)
  <details><summary>📄 Abstract</summary>
  Radio Dynamic Zones (RDZs) allow wireless experiments to operate outside conventional spectrum regulations while continuously guaranteeing protection for incumbent users. Existing RDZ prototypes automate this task procedurally, through handcrafted rules and predefined workflows, and become brittle when experiments encounter hardware impairments, user workflows and devices, or interference mechanisms not anticipated at design time. This paper introduces the agentic RDZ (A-RDZ), which, to the best...
  </details>

- **2026-09-15** — Muhammad Ahmed Ullah Khan, Mohammed Elamine, Sheikh Talha Uddin et al. — [NeuroSymbEAD: A Large Scale Neuro-Symbolic Caption Dataset for Omni-Directional Embodied Autonomous Driving](http://arxiv.org/abs/2609.16919v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces NeuroSymbEAD, a large-scale neuro-symbolic caption dataset featuring an ego-centric knowledge graph (KG) of static and dynamic objects annotated with classes, categories, heading directions, orientations, and distances from the ego-vehicle. These annotations are used on the KITTI-360 dataset to generate multilevel textual captions representing a lightweight version of an ego-centric scene map. Outdoor scene-map reconstruction, visual recognition, and object grounding establ...
  </details>

- **2026-09-14** — Yuhang Wang — [Why LLM Agents Collapse Without Oversight: The Enforcement Gap as the Mechanism Behind Emergence World Failures](http://arxiv.org/abs/2609.15293v2)
  <details><summary>📄 Abstract</summary>
  When Emergence World placed frontier LLM agents in an unsupervised multi-agent simulation, the results were alarming: agents committed crimes, starved, and enforced unanimous conformity -- without any external attacker. This paper identifies the mechanism. Reflexion-style agents already detect dangerous plan steps through iterative self-critique, yet the architecture provides no pathway from detection to action. We call this the enforcement gap: the audit sees the problem; the controller ignores...
  </details>

- **2026-09-14** — Mantek Singh, Jeshwanth Challagundla, Prateek Karnal et al. — [LLMs as Master Forgers: Generating Synthetic Time Series Data for Manufacturing](http://arxiv.org/abs/2609.16155v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a novel framework leveraging Large Language Models (LLMs) to generate synthetic time series data for manufacturing processes. Motivated by the scarcity of labeled time-series data in real-world manufacturing settings, which hinders the development of robust machine learning models, we explore the potential of LLMs to learn complex temporal dependencies and generate realistic synthetic data. Our approach involves fine-tuning pre-trained LLMs on manufacturing process instructio...
  </details>

- **2026-09-14** — Ivy Zhang — [The Troy Moment of AI: Why Some Will Cheat and Some Will Follow?](http://arxiv.org/abs/2609.15494v2)
  <details><summary>📄 Abstract</summary>
  Recent investigations of the July 2026 OpenAI-Hugging Face incident motivate two questions: when an assigned task becomes impossible, does an agent stop or escalate, and can observing another agent's behavior change that decision? We study these questions using seven ImpossibleBench tasks with GPT-5.6 Sol, Claude Fable 5.1, and Gemini 3.8 Flash in solo and three-agent settings. Under an explicit-boundary regime with clear authorization rules and restricted tools, no protected tests are modified,...
  </details>

- **2026-09-14** — Aashiq Muhamed, Mona T. Diab, Virginia Smith — [Decoy Direction Optimization: A Post-Hoc Defense Against LLM Abliteration](http://arxiv.org/abs/2609.16204v1)
  <details><summary>📄 Abstract</summary>
  Safety guardrails in open-weight language models can be readily bypassed using Refusal Feature Ablation (RFA), a technique that identifies and projects out a linear refusal direction from the residual stream, often achieving a high attack success rate (ASR) while preserving model capability. Defending against these attacks typically requires computationally expensive safety finetuning for every new checkpoint. We introduce Decoy Direction Optimization (DDO), a fast, post-hoc weight-editing defen...
  </details>

- **2026-09-14** — Rohit Dhaipule, Sukhdeep Singh Kharbanda, Prasanth Bathala et al. — [StalePO: Anchored Token-Level Preference Optimization using Legacy Post-Edits in Machine Translation](http://arxiv.org/abs/2609.16340v1)
  <details><summary>📄 Abstract</summary>
  Machine translation systems are periodically upgraded to stronger models, but the available preference signal is human post-edits of an older system's outputs, which the newer model may already surpass. Moreover, collecting fresh post-edits for every new model is prohibitively expensive. We call this the Stale Preference problem. Standard DPO can fail in this setting: it may increase the likelihood of inferior post-edits, erode the model's existing quality, and fail to provide the per-token cont...
  </details>

- **2026-09-14** — Wuyang Dai, Song Wang — [AgentGuard: Learning Execution Guardrails from Anomalous Coding-Agent Trajectories](http://arxiv.org/abs/2609.16287v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents increasingly rely on execution harnesses to interact with repositories and external tools. However, task success does not guarantee reliable execution. Agents may still modify unrelated files, rewrite tests, issue unsafe commands, or ignore failed validations, motivating behavioral guardrails for reliable execution. We present AgentGuard, an instruction-level guardrail framework that learns conditional execution constraints from anomalous trajectories of coding agents. Rather th...
  </details>

- **2026-09-14** — Anubhav Khanal, Prabigya Acharya, Roshni Poudel et al. — [SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](http://arxiv.org/abs/2609.16233v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models excel at 2D image understanding but remain limited in 3D spatial reasoning. Progress is hindered by limitations in current benchmarks. First, 3D datasets often rely on point clouds that capture geometry but discard rich visual features like texture, text, and materials. Second, annotations treat objects in isolation while ignoring real-world hierarchical organization (scenes, rooms, functional areas, object groups). Third, evaluation tasks focus narrowly on basic recogniti...
  </details>

- **2026-09-14** — Mughees Ur Rehman, Aritran Piplai, Murat Kantarcioglu — [RuleAutoPilot: Synthesizing Deployable Suricata Rules from Network Traffic](http://arxiv.org/abs/2609.16231v1)
  <details><summary>📄 Abstract</summary>
  Rule-based Intrusion Detection Systems (IDS) such as Suricata are central to network security, yet crafting effective detection rules demands deep expert knowledge and cannot keep pace with emerging threats. Existing LLM-based approaches can reduce analyst effort, but they either rely on curated threat intelligence that is produced only after the underlying traffic artifacts already exist, or they require costly LLM use without sufficient quality control. We present RuleAutoPilot, an end-to-end ...
  </details>

- **2026-09-14** — Candace S. Y. Chan, Aris Karatzikos, Ilias Georgakopoulos-Soares — [Artificial intelligence and biosecurity: capabilities, threat pathways, and defense-in-depth governance](http://arxiv.org/abs/2609.16213v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence is reshaping biological research across an increasingly connected digital-to-physical workflow. General-purpose large language models can retrieve and integrate scientific information, support experimental planning, and computational analysis; biological foundation models can predict, optimize, and generate proteins, genes, and genome-scale sequences; agentic systems can coordinate multistep research tasks; automated laboratories can partially close the design-build-test-...
  </details>

- **2026-09-14** — Nishad Singhi, Hector Garcia Rodriguez, Aditya Arora et al. — [Reasoning with Image Generation](http://arxiv.org/abs/2609.16409v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought reasoning has revolutionized natural language processing by enabling large language models (LLMs) to decompose problems into intermediate steps before answering. Yet confining reasoning to the textual domain presents limitations for tasks requiring direct manipulation of visual representations. Recent efforts augment multimodal LLMs with external visual expert tools such as depth estimation or object detection modules, but these remain fundamentally limited by their reliance on ...
  </details>

- **2026-09-14** — Ghazal Farhani, Taufiq Rahman — [Geometry vs Structure: Graph-Based Diagnostics for LiDAR Point-Cloud Simulation Fidelity](http://arxiv.org/abs/2609.16378v1)
  <details><summary>📄 Abstract</summary>
  Digital twins provide a scalable and cost-effective complement to real-world testing for validating autonomous-driving and advanced driver-assistance system (ADAS) sensor pipelines. However, quantifying their fidelity remains challenging, particularly for 3D LiDAR point clouds, where conventional geometric metrics may overlook important structural discrepancies. We present a graph-based framework for evaluating the structural fidelity of simulated LiDAR point clouds against real-world scans. Whi...
  </details>

- **2026-09-14** — Zhaofeng Yu, Haokai Ma, Dongyang Zhan et al. — [Misleading the Planner through Deceptive Resumes: Registration-Time Injection in Centralized Multi-Agent Systems](http://arxiv.org/abs/2609.15516v1)
  <details><summary>📄 Abstract</summary>
  A centralized LLM-based multi-agent system (MAS) extends its functionality by registering new worker agents, whose descriptions are read by the planner to decide how a task is decomposed, which worker executes each subtask, and what each subtask requires. Third-party descriptions are authored outside the system but trusted by the planner, creating a registration-time injection channel. The payload is planted before any user instruction arrives, targets the planner and propagates through the gene...
  </details>

- **2026-09-14** — Luis M. Sánchez — [Clean Scores, Buried Evidence, and Confident Wrong: A Receipt-Based Audit of Frontier Agentic QA](http://arxiv.org/abs/2609.15319v1)
  <details><summary>📄 Abstract</summary>
  Frontier models score well on shallow document/chart reading tasks. In a controlled data-room audit, moving evidence into buried conditions reduced accuracy, increased forced declarations, increased tool calls, and increased cost per correct answer. Confidence and benchmark calibration did not fully capture wrong answers; a documented production incident shows fabricated structural claims can be mixed with accurate numeric tables. Agentic evaluations need claim-level receipts (statement-level pr...
  </details>

- **2026-09-14** — Yuhang Wang — [Why LLM Agents Collapse Without Oversight: The Enforcement Gap as the Mechanism Behind Emergence World Failures](http://arxiv.org/abs/2609.15293v1)
  <details><summary>📄 Abstract</summary>
  When Emergence World placed frontier LLM agents in an unsupervised multi-agent simulation, the results were alarming: agents committed crimes, starved, and enforced unanimous conformity -- without any external attacker. This paper identifies the mechanism. Reflexion-style agents already detect dangerous plan steps through iterative self-critique, yet the architecture provides no pathway from detection to action. We call this the enforcement gap: the audit sees the problem; the controller ignores...
  </details>

- **2026-09-14** — Dalton Diez, Peyton Andras, Max Shroyer et al. — [Event-Native Symbolic-Temporal Spike Encoding Framework for Heterogeneous Cyber Streams](http://arxiv.org/abs/2609.15772v1)
  <details><summary>📄 Abstract</summary>
  Spiking neural networks (SNNs) have shown promise for sparse, event-driven computation through stateful processing that is naturally compatible with low-power edge hardware. These properties align with cyber monitoring, where data arrives asynchronously, and malicious behavior often emerges through temporal patterns across event sequences. However, cyber streams are not composed solely of continuous numeric signals: their informative structure is also carried by categorical identifiers, irregula...
  </details>

- **2026-09-14** — Daniele Veri' — [Beyond AI Literacy: A Structured Review and Exploratory Meta-Analysis of Measures for Competent Generative-AI Use](http://arxiv.org/abs/2609.15624v1)
  <details><summary>📄 Abstract</summary>
  Researchers assessing competent generative-AI use at work must choose among self-reports, objective tests, and measures of oversight and reliance. We conducted a structured, seeded review of 24 focal empirical publications, starting from the 2024 COSMIN-based review and adding a targeted update through 17 August 2026. We grouped the measures into four domains: knowledge and use, epistemic oversight, reliance calibration, and operational control of tool-using agents. In an exploratory meta-analys...
  </details>

- **2026-09-14** — Yolo Y. Tang, Daiki Shimada, Jiayue Meng et al. — [BVB: Benchmarking Agentic Video Understanding via Programmatic Reconstruction in Blender](http://arxiv.org/abs/2609.15478v1)
  <details><summary>📄 Abstract</summary>
  Multimodal agents can create complex videos in software such as Blender by coding without relying on diffusion models. Yet video understanding benchmarks still evaluate models mainly through question answering. If an agent truly understands a video, it can reconstruct it programmatically. We introduce BVB, Blender-VideoBench, a benchmark that tests this ability by asking agents to reconstruct real-world videos as animated Blender scenes. To ensure fair comparison, each agent programs the reconst...
  </details>

- **2026-09-14** — Jean Groeninger, Zihao Zhao, Juliana de Castilhos et al. — [Listening for Airway Stenosis: A Foundation Model-Based Method for Rapid and Accessible Detection](http://arxiv.org/abs/2609.15453v1)
  <details><summary>📄 Abstract</summary>
  Airway stenosis can cause severe respiratory complications, yet its detection often relies on specialized examinations and medical imaging. This study explores the potential of acoustic AI for rapid and accessible airway stenosis detection using readily acquired patient voice recordings. We systematically investigate whether acoustic foundation models (AFMs) can extract acoustic representations associated with airway stenosis-related speech patterns. Experiments are conducted on a cohort of 748 ...
  </details>

- **2026-09-14** — Hongchang Shi, Jinpeng Hu, Ao Wang et al. — [MarKey: Marginal Utility Guided Greedy Keyframe Selection for Long Video Understanding](http://arxiv.org/abs/2609.15408v1)
  <details><summary>📄 Abstract</summary>
  Long-video understanding remains challenging for multimodal large language models (MLLMs) because densely encoding long frame sequences is computationally expensive, while uniform sampling under a limited visual budget can miss sparse yet decisive evidence. Recent training-free keyframe selection methods have enabled more efficient inference and yielded promising performance gains. However, many existing methods score frames largely in isolation without explicitly considering how each candidate ...
  </details>

- **2026-09-14** — Sayantan Mukherjee — [Large Universe Subset Predicate Encryption with IND-CCA Security (with Constant-size Ciphertext and Keys)](http://arxiv.org/abs/2609.15312v1)
  <details><summary>📄 Abstract</summary>
  Katz et al. (CANS'17) introduced Subset Predicate Encryption (SPE).   This scheme is a generalization of broadcast encryption as it emulates the \emph{subset containment} predicate in the encrypted domain.   They proposed two selectively IND-CPA secure SPE constructions in the small universe setting.   They also showed some black-box transformations of SPE to well-known primitives like WIBE and ABE to establish the richness of the SPE structure.   Chatterjee and Mukherjee (RSA'19) proposed two S...
  </details>

- **2026-09-14** — Hanne Beuter, Sebastian Dorn — [Closed-form Bayesian homography estimation from noisy point correspondences](http://arxiv.org/abs/2609.15227v1)
  <details><summary>📄 Abstract</summary>
  While homographies are fundamental to many computer vision tasks, the majority of conventional estimation techniques provide only point estimates without directly quantifying uncertainty introduced by noisy observations. Uncertainty, though, propagates to subsequent processing steps such as camera calibration and 3D reconstruction and is particularly relevant in safety-critical and socially relevant fields including medical imaging, autonomous driving, and defense. We present a fast Bayesian for...
  </details>

- **2026-09-14** — Gongbo Zhang, Hao Li, Yu Wang et al. — [OpenAI4S: Code as Action, Science as Sessions](http://arxiv.org/abs/2609.15096v1)
  <details><summary>📄 Abstract</summary>
  AI co-scientists could accelerate computational research, but over a long-running study the workflow also has to stay inspectable, resumable and reproducible, which requires persistent computational state and provenance. Here we present OpenAI4S, an open-source scientific research agent built around the principle of \emph{Code as Action, Science as Sessions}. OpenAI4S combines a persistent computing runtime with research-session management: orchestration is handled through structured tool calls,...
  </details>

- **2026-09-14** — Hyeongcheol Park, Sumin In, Suyeon Myeong et al. — [SALUTE: Benchmarking and Adapting LLMs for the Defense Domain](http://arxiv.org/abs/2609.15022v1)
  <details><summary>📄 Abstract</summary>
  Defense is a knowledge-intensive domain that requires precise understanding of specialized terminology, doctrinal concepts, operational procedures, and evolving military events. Although recent work has explored language technologies for military applications, existing efforts remain fragmented: they are often task-specific, rely on limited adaptation pipelines, or lack comprehensive defense-domain evaluation. In this paper, we present SALUTE, an end-to-end framework for benchmarking and adaptin...
  </details>

- **2026-09-14** — Hyungseok Ryu, Pilwon Hur — [Two-Stage Personalized Gait Phase Estimation in Stroke Survivors During Exoskeleton-Assisted Walking: An Offline Feasibility Study](http://arxiv.org/abs/2609.14984v1)
  <details><summary>📄 Abstract</summary>
  This study evaluated personalized gait phase estimation for stroke survivors using functional inertial measurement unit (IMU) alignment and two-stage sequential adaptation of models pre-trained on healthy gait. The estimator used signals from a thigh-mounted IMU. Heel force-sensitive resistor measurements provided reference phase labels for offline adaptation and evaluation. Stage 1 established a distillation-regularized participant-specific model, and Stage 2 performed conditional refinement us...
  </details>

- **2026-09-14** — Tinashe Handina, Yuehan Diao, Adam Wierman et al. — [Strategic Decision Focused Learning](http://arxiv.org/abs/2609.14907v1)
  <details><summary>📄 Abstract</summary>
  Machine learning (ML) predictions are increasingly being used to guide decision-making, giving rise to the problem of decision-focused learning (DFL) where predictors are optimized for downstream decision quality rather than accuracy alone. However, most existing work assumes a single decision-maker optimizing in isolation. This paper formalizes strategic decision-focused learning, where an ML system predicts an exogenous state that some agents observe before playing a game. For example, a park ...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 59 papers

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

- **2026-09-15** — Thanapat Trachu, Samuele Cornell, William Chen et al. — [LACE: Layer-Wise Compression for Dynamic Frame Rate Codecs](http://arxiv.org/abs/2609.17509v1)
  <details><summary>📄 Abstract</summary>
  Neural audio codecs are a key component in speech language modeling. However, their high frame rates lead to long sequence lengths, increasing computational costs. Dynamic frame rate codecs mitigate this by reducing the effective frame rate using a compression step to merge multiple frames together. However, most prior methods either operate on single-codebook codecs or apply a single compression step before multi-layer quantization. This forces all quantization layers to share the same segmenta...
  </details>

- **2026-09-15** — Rong He — [Decomposition Buys Integrity, Not Yield](http://arxiv.org/abs/2609.17464v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems split a task across a tree of agents and justify the split with folklore: smaller contexts, cleaner separation, parallelism. We ask what the split does to how much of what the leaves discover reaches the root. Model a decomposition as a tree in which an agent handed $b$ items keeps any one with probability $r(b)$. If $r(b)=1/b$, every tree delivers exactly one finding, for every task size and every shape; we verify this to $2.4 \times 10^{-15}$ on 20,000 random irregular tree...
  </details>

- **2026-09-15** — Clara Dehman, Daniele Viganò — [Spontaneous wandering of the magnetic axis in pulsars: 3D magneto-thermal simulations and the imprint on braking indices](http://arxiv.org/abs/2609.17436v1)
  <details><summary>📄 Abstract</summary>
  Braking index measurements of hundreds of pulsars, despite observational caveats, show a clear trend: $n<3$ at early ages, $n>3$ at middle ages, and increasingly large, fluctuating values at larger characteristic ages. Crustal magnetic fields in isolated neutron stars evolve through Ohmic dissipation and non-linear Hall redistribution across scales, with additional early-time contributions from the chiral magnetic effect and post-burial re-emergence. Initial conditions are usually assumed dipole...
  </details>

- **2026-09-15** — Adam Zachary Wasserman, David Beauchemin — [Right Tool, Right Job: Native-Language Evaluation, Tokenizer Sensitivity, and Methodological Findings from a French-Only BabyLM](http://arxiv.org/abs/2609.17435v1)
  <details><summary>📄 Abstract</summary>
  We submit MéTRON-FR, a 125M GPT-2 pretrained on 92.47M words of French, to the BabyLM 2026 Strict track. It scores 85.97 +/- 0.17% on QFrBLiMP (a native Quebec-French benchmark of grammatical minimal pairs) and 62.80% on the BabyLM-weighted leaderboard. A cross-lingual GLUE (General Language Understanding Evaluation) protocol that combines French task-data translation with rank-16 LoRA (Low-Rank Adaptation) produces a sharp task-type gradient: relational tasks gain measurably, while world-knowle...
  </details>

- **2026-09-15** — Giannis Kalyvas, Giorgos Filandrianos, Orfeas Menis Mastromichalakis et al. — [An Empirical Study of Counterfactual Self-Explanations in LLMs](http://arxiv.org/abs/2609.17119v1)
  <details><summary>📄 Abstract</summary>
  Large language models can easily generate explanations for their own outputs, but such self-explanations are not necessarily faithful to the model's behavior. We study this issue through counterfactual self-explanations, where a model minimally edits an input so that its own prediction changes. Across sentiment analysis and natural language inference, we evaluate ten instruction-tuned models from the LLaMA-3 and Qwen-2.5 families, measuring faithfulness, minimality, and alignment with human-anno...
  </details>

- **2026-09-15** — Cai Ke, Xin Liu, Han Zhang et al. — [ThinkFlow: Self-Evolving Probabilistic Latent Memory for Lifelong Conversational Agents](http://arxiv.org/abs/2609.17010v1)
  <details><summary>📄 Abstract</summary>
  Lifelong conversational agents rely on memory systems to maintain deep, context-aware interactions with users. However, existing explicit textual memory pipelines suffer from a severe information bottleneck, often losing subtle behavioral patterns and emotional shifts. Furthermore, being typically static post-deployment, they cannot autonomously adapt to personal habits and preferences without manual feedback. Cognitive science, however, suggests that humans maintain mental models purely in a la...
  </details>

- **2026-09-15** — Haonan Huang, Tianrui Qiu, Xianghao Zang et al. — [VOR-Bench: A Human Perception-Driven Benchmark for Video Object Removal](http://arxiv.org/abs/2609.16878v1)
  <details><summary>📄 Abstract</summary>
  Despite its crucial role in video object removal (VOR), existing evaluation paradigms face two critical limitations: questionable references and a misalignment between tradi- tional metrics and human preference. To address these challenges, we introduce VOR- Bench, which advances VOR evaluation through three integrated components. First, we present the VOR Dataset (VORD), the first benchmark dataset providing both paired edited videos and graffiti masks. Its unique strength lies in a diverse dat...
  </details>

- **2026-09-15** — Han Zhiguang, Farah Benamara, Pascale Zaraté — [Integrating the Analytic Hierarchy Process with Large Language Models for Transparent Multi-Criteria Decision-Making](http://arxiv.org/abs/2609.16779v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly employed in a wide range of decision-making tasks. However, the opacity of their internal reasoning makes it difficult to validate or interpret their outputs, and the need for interpretability becomes especially critical in high-stakes settings. This study examines the decision-making capabilities of LLMs through the Analytic Hierarchy Process (AHP), a classical and widely used multicriteria decision-making framework. We construct a new annotated benchmark based on AHP and ...
  </details>

- **2026-09-15** — Abhilaksh Singh Reen, Kushal Borkar, Ritvik Mahapatra — [IMVS: Interactive Medical Volume Segmentation with Test-Time Adaptation - A New Method for Annotating Radiology Datasets](http://arxiv.org/abs/2609.16775v1)
  <details><summary>📄 Abstract</summary>
  Annotating large radiology datasets is bottlenecked by the manual effort of delineating structures slice-by-slice in 3D volumes. Interactive methods reduce this effort but stay interaction-inefficient: slice-wise methods (including many foundation models) ignore inter-slice continuity, while 3D and video-based methods propagate a prompt with a \emph{fixed} propagator that never adapts to the target volume, so it drifts on low-contrast or pathological structures and must be re-prompted. We presen...
  </details>

- **2026-09-15** — Zishuo Zhao, Kai Chen, Ao Li et al. — [Turn-level Multiscale Density Ratio Estimation for LLM Agents](http://arxiv.org/abs/2609.16760v1)
  <details><summary>📄 Abstract</summary>
  With the rapid development of Large language model (LLM), agent systems enhanced by LLMs show huge potential in being able to deal with complex tasks, especially involving multi-step thinking or interaction with tools. For applying LLM techniques with a well-designed agent paradigm, post-training of LLM in multiple agent scenarios is necessary to achieve better performance. Among the variable post-training techniques, alignment methods such as PPO, DPO, DIL, and GRPO become popular because many ...
  </details>

- **2026-09-15** — Yihan Chen, Huan Ren, Wenfei Yang et al. — [PriorPose: Reference-Guided Joint Deformation and Alignment for Category-Level Object Pose Estimation](http://arxiv.org/abs/2609.16727v1)
  <details><summary>📄 Abstract</summary>
  Category-level object pose estimation seeks to recover a similarity transform $(R,t,s)$ for unseen instances without instance-specific CAD models. Most competitive methods are correspondence-based: prior-free variants regress canonical (NOCS) coordinates directly from local observations and implicitly memorize the canonical frame in the weights, which ties the parameters to category-typical orientations and hurts generalization under distribution shift; prior-based variants introduce a category ...
  </details>

- **2026-09-15** — Hailong Shu — [Predictability-Guided Multiscale Probabilistic Forecasting of Wind Direction under Extreme Shear](http://arxiv.org/abs/2609.16707v1)
  <details><summary>📄 Abstract</summary>
  Accurate multi-horizon wind direction forecasting is critical for turbine yaw control and grid security. Rapid directional shear (turning $\ge 90^\circ$) challenges models via non-Euclidean geometry on $S^1$, multiscale dynamics, and regime-dependent uncertainty. Conventional discrete models and foundation models suffer from mid-frequency phase lag and turning misalignments. We show that directional predictability decays at disparate rates across frequency subbands, rendering monolithic mechanis...
  </details>

- **2026-09-15** — Yu Li, Zhengran Shen, Yachun Mi et al. — [Bridging the Perceptual Gap: Residual-Enhanced Downscaling and Manifold-Aware Perception Alignment Adaptation for NR-IQA](http://arxiv.org/abs/2609.16664v1)
  <details><summary>📄 Abstract</summary>
  Leveraging Large Vision-Language Models like CLIP has recently set new benchmarks for No-Reference Image Quality Assessment (NR-IQA). However, the contrastive pretraining of CLIP inherently prioritizes semantic invariance, which often suppresses subtle perceptual signals, a phenomenon we term perceptual submergence. Furthermore, standard preprocessing techniques (e.g., cropping and interpolation) further exacerbate the loss of critical high-frequency quality cues. In this paper, we propose the C...
  </details>

- **2026-09-15** — Jeng Wen Joshua Lean, Ting-Yu Yen, Wei-Fang Sun et al. — [G3AR: Graph-Guided Neural Visual Geometry for Scalable Multi-Sequence Aerial Registration](http://arxiv.org/abs/2609.16603v1)
  <details><summary>📄 Abstract</summary>
  Full-context neural visual geometry is impractical for thousands of images, while sequence-based chunking poorly captures irregular non-local overlap in multi-sequence aerial collections. We present Graph-Guided Neural Visual Geometry for Aerial Registration (G3AR), a graph-guided framework for scalable dense neural geometry. Before local inference, G3AR builds a geometrically verified image-proximity graph that guides bounded overlapping chunks and induces a chunk graph whose maximum spanning t...
  </details>

- **2026-09-15** — Guangyu Sun, Shlok Kumar Mishra, Wentao Bao et al. — [FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal Tokens for Retrieval and Generation](http://arxiv.org/abs/2609.16591v1)
  <details><summary>📄 Abstract</summary>
  Traditional multimodal representation learning and generation are two stages: a contrastive or self-supervised visual encoder is trained first, followed by a separate downstream generative model. This setup bottlenecks generative performance behind frozen embeddings. To bridge this gap, we revisit joint multimodal representation learning and generation to produce linearly interpolatable embeddings that are directly consumable by generative decoders. We present FLAT (Flexible-Length Aligned Trans...
  </details>

- **2026-09-15** — Keqing Zhang, Jingyu Chen, Yufan Liu et al. — [Do LLMs Have Values? A Quantitative Analysis and Alignment Framework for Values in Large Language Models](http://arxiv.org/abs/2609.16589v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) increasingly handle complex subjective tasks, aligning their intentions and behaviors with human values has become a critical scientific challenge. However, current efforts are confounded by a striking behavioral paradox: they fluctuate unpredictably under minor wording changes ("swing"), yet stubbornly ignore explicit instructions to correct ingrained biases ("rigidity"). Resolving this duality is critical for reliable AI alignment. To systematically understand a...
  </details>

- **2026-09-15** — Istabrak Abbes, Nizar Islah, Irina Rish et al. — [What Does Layer-Importance Reveal About Transformers and State-Space Models?](http://arxiv.org/abs/2609.16537v1)
  <details><summary>📄 Abstract</summary>
  Transformers and state-space models (SSMs) are the two dominant families of sequence models, and a central open question is how far the analytical knowledge built for transformers transfers to SSMs. We address this through the lens of layer importance which underpins compression, selective fine-tuning, and interpretability across both families. We decompose layer importance into two distinct notions. \emph{Necessity} captures how much the pretrained model depends on a layer's existing contributi...
  </details>

- **2026-09-15** — Qian Chen, Xiangang Li, Xiang Lv et al. — [The Evolving Bottleneck in Speech Generation: Interface Co-design and Staged Alignment from CosyVoice to Qwen-Audio-3.0-TTS](http://arxiv.org/abs/2609.16514v1)
  <details><summary>📄 Abstract</summary>
  Speech synthesis systems are commonly narrated as a sequence of larger models, better tokenizers, and broader data. This technical retrospective offers a different account of the CosyVoice lineage, from CosyVoice through CosyVoice 2 and CosyVoice 3 to Qwen-Audio-3.0-TTS: progress came from repeatedly relocating the system's dominant bottleneck. Across the lineage, a stable decomposition separates an autoregressive language model that plans speech from a flow-matching model that renders acoustics...
  </details>

- **2026-09-15** — Quanwei Liu, Tao Huang, Jiaqi Yang et al. — [VPRef: A Cross-Domain Benchmark for Referring Remote Sensing Image Segmentation](http://arxiv.org/abs/2609.16486v1)
  <details><summary>📄 Abstract</summary>
  Rapid advancements in vision-language models have propelled Referring Remote Sensing Image Segmentation (RRSIS) to the forefront of Earth observation. However, practical deployments suffer severe performance degradation under a coupled dual-drift paradigm: visual domain drift from cross-spatial-resolution mismatches and spectral variations, alongside textual logic drift from unconstrained, variable user-input granularities. To mitigate these bottlenecks, this paper establishes the first cross-do...
  </details>

- **2026-09-15** — Muhammad Ashar Ishfaq, Glaucia Melo — [ToMAS: A Pilot Failure-Grounded Theory-of-Mind Benchmark from Multi-Agent LLM Failures](http://arxiv.org/abs/2609.16986v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems can fail even when communication succeeds because agents do not correctly track their peers' roles, knowledge, or intentions. We investigate whether such inter-agent misalignment cases, labelled FC2 in MAST-Data, can be converted into functional partner-state reasoning items. ToMAS applies four explicit convertibility criteria to diagnosed execution traces. A full conversion pass over 242 eligible non-AG2 training traces produced 39 CLEAN items. In an 18-trace relia...
  </details>

- **2026-09-14** — Vincent Karpf, Joseph Reth, Eike Gerhardt et al. — [Metacognitive Steering: Learning the Structure of Scientific Judgment](http://arxiv.org/abs/2609.16245v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon scientific discovery requires agents to alternate between exploration, disciplined execution, and critical reassessment as evidence changes. Current language models are trained primarily on the products of science and optimized using outcome-level signals, providing limited supervision for these process-level shifts in scientific judgment. We investigate whether such judgment can be recovered from scientist interaction traces and used to control the internal computation of a frozen ...
  </details>

- **2026-09-14** — Yingjia Wan, Lin Lin, Elisa Kreiss — [How Humans and LLMs Read Gender into Gender-Neutral Physical Descriptions](http://arxiv.org/abs/2609.16366v1)
  <details><summary>📄 Abstract</summary>
  When foundation models describe people, recent work in AI fairness, accessibility, and ethics recommends avoiding inferred identity labels (e.g., "she", "his") in favor of seemingly "objective" physical descriptions (e.g., "short hair", "a defined jawline"). Yet whether such descriptive language achieves gender-neutral communication remains an open empirical question. To study this, we introduce GAPA (Gender Associations of Physical Attributes), a dataset of 316 common physical attributes drawn ...
  </details>

- **2026-09-14** — Nunzio Lorè, Hongan Zhu, Babak Heydari — [Cheap Talk Stabilizes Strategic Interaction in LLM Agents](http://arxiv.org/abs/2609.16270v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as interacting agents, making the persistence of their action policies across repeated interaction critical for reliable multi-agent operation. We investigate whether and how agent-generated, non-binding pre-play communication ("cheap talk") increases such persistence in four open-weight 7-9B-parameter LLMs. Our experiments span four repeated two-player games -- Prisoner's Dilemma, Snowdrift, Stag Hunt, and Harmony -- with incentive structures rang...
  </details>

- **2026-09-14** — Yiwei Yang, Haoxiang Zhang, Bingbing Wen et al. — [Spurious Tool Use: When RL Agents Learn the Wrong Reason to Act](http://arxiv.org/abs/2609.16268v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly interleave natural language reasoning with external tools such as web search and code execution. These tool-use policies are often optimized via reinforcement learning (RL), which can amplify spurious correlations in the training data. In this work, we study when and why RL-trained agents learn shortcut tool-selection policies: invoking tools based on superficial prompt cues rather than genuine task requirements. We construct controlled synthetic en...
  </details>

- **2026-09-14** — Mantek Singh, Jeshwanth Challagundla, Siddharth Raina et al. — [Efficient Reasoning Distillation: Small Video-Language Models via Synthetic CoT and Difficulty-Aware Fine-Tuning](http://arxiv.org/abs/2609.16255v1)
  <details><summary>📄 Abstract</summary>
  We present an efficient method to distill reasoning capabilities into compact video-language models (VLMs) for video question answering (VideoQA). Our approach fine-tunes a 2B-parameter model using only $\sim$900 uncertainty-selected examples, each augmented with synthetic chain-of-thought (CoT) rationales generated by a 4B teacher. Despite its minimal compute cost - under two hours on a single A100 GPU - our method enables the 2B model to outperform VLMs up to 4$\times$ larger, and generalize a...
  </details>

- **2026-09-14** — Asraful Haque, Christopher M. Rouleau, Rama K. Vasudevan et al. — [An Open-Source Hardware and Software Toolkit to Enable Agentic RHEED-Guided Thin-Film Synthesis](http://arxiv.org/abs/2609.15922v1)
  <details><summary>📄 Abstract</summary>
  Reflection high-energy electron diffraction (RHEED) provides rich information about evolving surfaces during thin-film growth, but non-automated, operator-dependent alignment and fragmented analysis workflows limit its potential in fully autonomous synthesis. Here, we present an open-source hardware and software toolkit that makes RHEED control and quantitative analysis accessible to operators and artificial intelligence (AI) agents. Demonstrated on a pulsed laser deposition system, the toolkit ...
  </details>

- **2026-09-14** — Kyle O'Brien, Edward James Young, Puria Radmard et al. — [Inoculation Midtraining with Learned Neologisms](http://arxiv.org/abs/2609.15886v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often learn both desirable and undesirable properties during post-training. We study whether midtraining, an earlier training stage, can shape which of these properties later generalise. We introduce Inoculation Midtraining, a technique that teaches a base model that unsafe behaviour belongs to a designated <quarantine_token> context, as indicated by the <quarantine_token> neologism (a new token) introduced during midtraining, and then post-trains the model on unsafe...
  </details>

- **2026-09-14** — Natalie Collina, Surbhi Goel, Aaron Roth et al. — [Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control](http://arxiv.org/abs/2609.15803v1)
  <details><summary>📄 Abstract</summary>
  Long-running AI agents create a control problem: each action they take changes the state, which in turn affects the trajectory of future actions. If the agent is not fully aligned, then guaranteeing safety requires approving consequential actions before allowing them to be executed. But requiring human approval at every step makes attention a bottleneck. Delegating review to other AI agents raises the same alignment problem: the reviewers may themselves be misaligned. We identify a condition on ...
  </details>

- **2026-09-14** — Mingzhi Chen, Yiyu Gui, Guibo Luo et al. — [A Language-Guided Multimodal Foundation Model for Zero-Shot and Multi-Task Brain Signal Analysis](http://arxiv.org/abs/2609.15740v1)
  <details><summary>📄 Abstract</summary>
  Brain signal analysis is essential for both neuroscience research and clinical diagnostics, yet current approaches face critical limitations. End-to-end models require task-specific retraining and exhibit limited generalization, while pre-trained models lack semantic depth and still depend on extensive fine-tuning. Meanwhile, general-purpose multimodal foundation models, though powerful in other domains, struggle to interpret brain signals due to representational misalignment and lack of domain ...
  </details>

- **2026-09-14** — Matteo Barbieri, Giammarco La Barbera, Juan Pablo De La Plata et al. — [Benchmarking Intra-Patient 3D Deformable Multimodal Image Registration](http://arxiv.org/abs/2609.15669v1)
  <details><summary>📄 Abstract</summary>
  Multimodal image registration is a key component of many clinical workflows, yet it remains challenging because corresponding anatomical structures often exhibit substantially different image intensities across modalities. In this work, we present a comprehensive benchmark of intra-patient 3D multimodal deformable registration methods across three datasets covering different anatomical regions and difficulty levels, including both synthetic deformation recovery and real clinical scenarios. We ev...
  </details>

- **2026-09-14** — Jiayang Gu, Zheng Fang, Lichaun Xiang et al. — [Principal-timestep Restricted Init via Sparse Matrix-decomposition in Flow-matching](http://arxiv.org/abs/2609.15643v1)
  <details><summary>📄 Abstract</summary>
  Flow-matching diffusion models have recently emerged as a strong paradigm for high-fidelity visual generation. However, their prohibitively high fine-tuning cost limits scalability to downstream tasks. While Low-Rank Adaptation (LoRA) combined with spectral initialization has demonstrated accelerated convergence and improved performance in autoregressive language models by better aligning gradient directions, we find that it fails to deliver similar gains in diffusion fine-tuning, often yielding...
  </details>

- **2026-09-14** — Jiahao Chang, Dong Du, Wanhu Sun et al. — [SAM3D-Part: Interactive Part Selection and Generation from 3D Objects](http://arxiv.org/abs/2609.15639v1)
  <details><summary>📄 Abstract</summary>
  Part-level control is essential for modern 3D asset creation, where objects are frequently edited, reused, animated, or fabricated through their individual components. In many such workflows, users need only several specific components rather than a complete object decomposition. However, existing 3D generation methods produce all parts regardless of user intent, while promptable 3D segmentation methods typically output partial surfaces instead of reusable complete meshes. In addition, image-con...
  </details>

- **2026-09-14** — Weixin Xu, Zhenyu Yang, Bing Wang et al. — [VideoScout: Learning Agentic Active Exploration with Adaptive Reasoning Pacing for Long Video Understanding](http://arxiv.org/abs/2609.15606v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have achieved remarkable progress on short video understanding yet remain limited on long videos due to the limited visual context window. Prevailing approaches rely on uniform frame sampling or recent coarse-to-fine agentic zooming, both of which struggle to localize sparse, decisive evidence in sufficiently long videos. We formulate long video understanding as a \textbf{Sequential Evidence Acquisition (SEA)} problem, in which an agent reads the video tu...
  </details>

- **2026-09-14** — Yang Xing, Jiong Wu, Savas Ozdemir et al. — [A Unified Vision-Language Model for PSMA PET/CT Report Generation, Visual Question Answering, and Lesion Segmentation](http://arxiv.org/abs/2609.15603v1)
  <details><summary>📄 Abstract</summary>
  Accurate PSMA PET/CT interpretation is central to prostate cancer management, yet existing PET/CT AI models typically address isolated tasks. We propose a unified PSMA PET/CT vision-language model for report generation, visual question answering, and lesion segmentation. The framework adopts an LLaVA-style architecture, comprising a PET/CT vision encoder, an MLP-Mixer projection module, a LoRA-tuned large language model, and a 3D segmentation branch. Training followed a four-stage strategy: visi...
  </details>

- **2026-09-14** — Stephane Hatgis-Kessell, W. Bradley Knox, Emma Brunskill — [Specifying Reward Functions for RL Without Environment Sampling](http://arxiv.org/abs/2609.15544v1)
  <details><summary>📄 Abstract</summary>
  Enabling human stakeholders to specify reward functions that lead to their desired outcomes is a key challenge in deploying reinforcement learning agents. Preference-based methods such as online RLHF can reduce the burden of manual reward design, but they require repeatedly training policies, sampling trajectories from the real world, and eliciting feedback, making them impractical in settings where environment interaction is computationally expensive or unsafe. We introduce Experience-Free Auto...
  </details>

- **2026-09-14** — Qiangqiang Zhou, Wenjun Tang, Yong Chen et al. — [ViCo-SAM3: Vision-Conditioned Alignment for Open-Vocabulary Camouflaged Object Segmentation](http://arxiv.org/abs/2609.15418v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary camouflaged object segmentation (OVCOS) aims to segment unseen camouflaged objects under text guidance. We observe that SAM3 still suffers from a pronounced semantic gap between global textual semantics and fine-grained pixel-level visual cues in OVCOS. Meanwhile, fully fine-tuning the text encoder introduces heavy parameter overhead and risks overfitting to training categories, which compromises open-vocabulary representation flexibility. To address these issues, we propose ViCo...
  </details>

- **2026-09-14** — Chenxu Liu, Zilu Zou, Peizhong Gao et al. — [IWC-Bench: Evaluating Web Application Generation from a Software Testing Perspective](http://arxiv.org/abs/2609.15387v1)
  <details><summary>📄 Abstract</summary>
  Human evaluation provides a direct measure of the quality of LLM-generated web applications. However, fitting human judgments through automated evaluation remains challenging. Static benchmarks can credit functionality that exists in source code but is unreachable at runtime. Interactive benchmarks exercise the application, yet incomplete exploration can cause them to miss implemented functionality and confound application defects with agent execution failures. To address these limitations, we p...
  </details>

- **2026-09-14** — Qingyu Liu, Rixi Xu, Yushen Chen et al. — [Cross-Lingual F5-TTS 2: A Simplified Framework for Language-Agnostic Voice Cloning](http://arxiv.org/abs/2609.15184v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot text-to-speech (TTS) can clone a speaker's voice from a short audio prompt, yet most TTS systems still require the audio prompt transcript during inference. This dependency prevents cross-lingual voice cloning when the audio prompt transcript is unavailable, particularly for unseen languages. Cross-Lingual F5-TTS removes this dependency and enables transcript-free cross-lingual voice cloning, but it prepares its training data with forced alignment. Forced alignment is sensitive to boun...
  </details>

- **2026-09-14** — Hanzhang Tu, Zhanfeng Liao, Wei Min et al. — [Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](http://arxiv.org/abs/2609.15032v1)
  <details><summary>📄 Abstract</summary>
  Live free-viewpoint visualization of real humans is critical for immersive communication and interactive digital experiences. Existing methods either rely on computationally expensive optimization or require calibrated cameras and low-resolution inputs, making real-time high-resolution deployment impractical. In this work, we present Tele360, the first real-time feed-forward system for dynamic human reconstruction and live free-viewpoint visualization from sparse, unposed RGB streams. Our system...
  </details>

- **2026-09-14** — Frank Li — [Validating Hybrid-State Cache Recovery for GLM-5.3-Flash with vLLM and LMCache](http://arxiv.org/abs/2609.15030v1)
  <details><summary>📄 Abstract</summary>
  External cache transfers can succeed while a hybrid language model resumes from an inconsistent state. We examine the full 45-layer GLM-5.3-Flash model, using the RedHatAI/ GLM-5.3-Flash-NVFP4 quantized checkpoint with vLLM and LMCache under four-way tensor parallelism. A complete-hit recovery mismatch restored state for the full prompt while the scheduler credited one fewer token. We aligned recovery through strict-prefix lookup and established a numerical comparison using shared computation co...
  </details>

- **2026-09-14** — Quang Phuoc Nguyen, Félix Gaschi, David Anugraha et al. — [Online Language Adaptive Sampling for Better Distributed Cross-lingual Gains](http://arxiv.org/abs/2609.14969v1)
  <details><summary>📄 Abstract</summary>
  Realignment is a promising approach for improving the cross-lingual transfer ability of multilingual language models, particularly for extremely low-resource languages (LRLs). However, existing realignment methods rely on uniform and random sampling of parallel sentences across languages, which may be suboptimal under limited batch sizes. In practice, models may benefit from seeing certain languages more frequently, especially those that are poorly aligned, and the optimal distribution can evolv...
  </details>

- **2026-09-14** — Chandan Kumar Sah, Jishnu Keshavan — [Exact Feasibility Certification and Optimal Responsibility Allocation for Multi-Robot CBF Safety Filters](http://arxiv.org/abs/2609.14935v1)
  <details><summary>📄 Abstract</summary>
  Multi-robot Control Barrier Function (CBF) safety filters can become infeasible, but a failed quadratic program (QP) does not indicate why the conflict occurred or how to resolve it. To address this, we develop an exact feasibility certificate for multi-agent CBF filters with heterogeneous control-affine dynamics and convex input sets. The certificate quantifies a feasibility reserve by separating the demand imposed by safety constraints from the available actuator supply. This decomposition sho...
  </details>

- **2026-09-14** — Jiayi Yuan, Hangoo Kang, James Jihao Liu et al. — [Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning](http://arxiv.org/abs/2609.14896v1)
  <details><summary>📄 Abstract</summary>
  A notable byproduct of LLM alignment training is mode collapse: the progressive loss of output diversity that narrows a model's expressivity at inference time. This degradation is especially limiting for applications requiring open-ended exploration and pluralistic perspectives, such as scientific ideation and creative writing. We present MoDA (Mode-conditioned Diversity Alignment), an online post-training RL algorithm that jointly optimizes generation quality and diversity, inspired by the coor...
  </details>

- **2026-09-14** — Naihao Deng, Samee Arif, Shuaichen Chang et al. — [One Example Is Enough to Pass Fairness Benchmarks: Rethinking Fairness Evaluation for Aligned LLMs](http://arxiv.org/abs/2609.14860v1)
  <details><summary>📄 Abstract</summary>
  Warning: This submission studies stereotypes and biases, and contains toxic and offensive examples, used for illustration purposes only.   Fairness benchmarks such as BBQ have become the de facto standard for fairness evaluation across major model families. We argue that these benchmarks are too easy to support their role: training Qwen 2.5 7B Base with Group Relative Policy Optimization (GRPO) on a single BBQ example, or placing that example in context as a one-shot demonstration for in-context...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 58 papers

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

- **2026-09-15** — Jahanvi Rajput, Dhruv Kudale, Saikiran Kasturi et al. — [Tables Decoded: DELTA for Structure, TARQA for Understanding](http://arxiv.org/abs/2609.17458v1)
  <details><summary>📄 Abstract</summary>
  Table understanding is a core task in document intelligence, encompassing two key subtasks: table reconstruction and table visual question answering (TabVQA). While recent approaches predominantly rely on vision- language models (VLMs) operating on table images, we propose a more scalable and effective alternative based on structured textual representations. These representations are easier to process, align more naturally with LLMs, and eliminate the need for language-specific visual encoders, ...
  </details>

- **2026-09-15** — Oier Larumbe-Lizarraga, Roberto Pereira, Cristian J. Vaca-Rubio — [Goal-oriented probabilistic forecasting for dynamic PRB allocation in 5G networks](http://arxiv.org/abs/2609.17297v1)
  <details><summary>📄 Abstract</summary>
  Efficient physical resource block (PRB) allocation in 5G networks requires accurate demand forecasting. Conventional methods minimize symmetric error metrics (MAE, RMSE), ignoring the operational cost asymmetry where under-provisioning (service degradation) is far costlier than over-provisioning (wasted capacity). We propose a goal-oriented probabilistic forecasting framework that aligns model training with the operator's decision-making objectives. Specifically, we train DeepAR and Temporal Fus...
  </details>

- **2026-09-15** — Md. Samiul Alim, Mahir Shahriar Tamim, Tanvir Ahmed Khan et al. — [Can LLMs Follow the Pulse of a Crisis? Evaluating Crisis Sentiment in Bangladesh's July Uprising](http://arxiv.org/abs/2609.16997v1)
  <details><summary>📄 Abstract</summary>
  Crisis sentiment analysis is especially challenging for low-resource languages such as Bangla, where language, context, and public reaction shift rapidly. We introduce UNRESTSENT200K, a Bangla crisis sentiment dataset with approximately 200K Facebook and YouTube comments from the July-August 2024 Bangladesh uprising. The dataset covers five event-aligned phases, from early escalation and internet blackout to regime transition and a later flood crisis. Each comment is linked to its parent post, e...
  </details>

- **2026-09-15** — Zeyi Shao, Haowen Hua, Jiaxin Zhang et al. — [TecoPrompt: Temporal-Conservative Prompt Learning for Vision-Language Models](http://arxiv.org/abs/2609.16858v1)
  <details><summary>📄 Abstract</summary>
  Prompt learning adapts vision-language models, such as CLIP, by adjusting a small set of context tokens. However, under few-shot supervision, even moderate label noise can disrupt prompt optimization. To address this issue, we propose TecoPrompt, a closed-loop robust prompt-learning framework that revisits optimal transport (OT) pseudo-labeling from a temporal perspective. TecoPrompt employs an entropic OT plan in the CLIP semantic space to obtain globally consistent label candidates. It verifie...
  </details>

- **2026-09-15** — Fangke Chen, Sirry Chen, Wei Chen et al. — [SOTER: A Generative Time-Series Foundation Model for Wearable Human Physiological Signals](http://arxiv.org/abs/2609.16804v1)
  <details><summary>📄 Abstract</summary>
  Time-series foundation models have demonstrated strong cross-domain transfer, yet their common architectural assumptions remain poorly aligned with wearable physiological signals, which are multichannel, irregularly sampled, noisy, and governed by coupled continuous-time dynamics spanning distinct spectral scales. We present SOTER, a generative foundation model for wearable physiological time series that unifies cross-channel coupling, spectrum-guided expert specialization, and continuous-time l...
  </details>

- **2026-09-15** — Yuqi Wang, Fengyuan Liu, Haochen Luo et al. — [RoleBreak: Benchmarking Long-Horizon Role-Playing Robustness in Spoken Dialogue](http://arxiv.org/abs/2609.16614v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-speech dialogue models increasingly support persona control, yet existing spoken role-playing benchmarks remain largely character-centric and short-horizon. This leaves open whether spoken dialogue models can sustain diverse roles over extended interactions, especially beyond predefined fictional characters. We introduce RoleBreak, an open benchmark for long-horizon role-playing robustness in spoken dialogue. RoleBreak contains 310 character-based and user-centered roles, 6,688 human-v...
  </details>

- **2026-09-15** — Junle Li, Weixian Waylon Li, Fuxiang Wu et al. — [SAVLA: Symmetry-Aware Vision-Language-Action Models for Robotic Manipulation](http://arxiv.org/abs/2609.16641v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have become the dominant paradigm for language-conditioned robot manipulation. However, although images and language instructions inherently encode geometric information, VLAs acquire their spatial competence purely from demonstrations. As a result, they are reliable only within the range of scene poses that the demonstrations cover. We propose SAVLA, an end-to-end symmetry-aware VLA model for robust and data-efficient policy learning. Our approach keeps the p...
  </details>

- **2026-09-15** — Haichen Hu, Yuheng Zhang, David Simchi-Levi — [Coupled Calibration and Learning: Mitigating Teacher Bias in LLM Distillation without Target-Domain Reward Feedback](http://arxiv.org/abs/2609.17474v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) distillation aims to transfer the capabilities of a powerful teacher to a smaller student. Direct imitation, however, can also transfer the teacher's systematic bias and errors. This challenge is particularly pronounced under covariate shift, when the teacher's reliability on target questions is uncertain and target-domain reward feedback is unavailable. We propose Coupled Calibration and Learning (CCL), an LLM distillation algorithm that couples teacher calibration wi...
  </details>

- **2026-09-15** — Ting-Wei Chang, Hen-Hsen Huang, Hsin-Hsi Chen — [Enhancing Accessibility of Medical Texts through Large Language Model-Driven Plain Language Adaptation](http://arxiv.org/abs/2609.17398v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the challenge of making complex healthcare information more accessible through automated Plain Language Adaptation (PLA). PLA aims to simplify technical medical language, bridging a critical gap between the complexity of healthcare texts and patients' reading comprehension. Recent advances in Large Language Models (LLMs), such as GPT and BART, have opened new possibilities for PLA, especially in zero-shot and few-shot learning contexts where task-specific data is limited. In...
  </details>

- **2026-09-15** — Jiacheng Wei, Jerry Bai, Xiaoyu Yue et al. — [XPACE: Joint World and Action Modeling from Heterogeneous Experience](http://arxiv.org/abs/2609.17372v1)
  <details><summary>📄 Abstract</summary>
  A general-purpose robot needs to draw on diverse experience, choose actions, and anticipate how those actions will change the world. We introduce XPACE, a unified embodied world model that serves as both a world action model, jointly predicting executable robot actions and future video, and a world simulator, predicting the visual consequences of prescribed actions. Our key insight is that video prediction can both connect heterogeneous experience to action learning and generate new experience f...
  </details>

- **2026-09-15** — Yang Liu, Yifan He, Wenhao Zhao et al. — [TIO-Former: Ultra-Lightweight 6-Directional ToF-Inertial Odometry for Nano-UAVs via a Streaming Causal Transformer](http://arxiv.org/abs/2609.17198v1)
  <details><summary>📄 Abstract</summary>
  Autonomous nano-UAV navigation requires accurate ego-motion estimation under stringent size, weight, power, and computing (SWaP-C) constraints, where visual sensors and LiDARs exceed payload limits, optical flow degrades in low-texture scenes, and inertial-only state estimation is susceptible to accumulated drift. While multi-zone time-of-flight (ToF) arrays provide a lightweight metric complement, 6-DoF estimation from merely 384 ranges per frame is challenged by invalid returns, anisotropic ob...
  </details>

- **2026-09-15** — Long-Vu Hoang, Naomi Harte — [Audio-Visual Turn-taking Prediction in Cocktail Party Scenarios](http://arxiv.org/abs/2609.17056v1)
  <details><summary>📄 Abstract</summary>
  Current predictive turn-taking models (PTTMs) achieve strong performance on benchmarks with controlled acoustic conditions and clean audio signals. Their generalisation to conversations with overlapping speech and background interference remains underexplored. In this research, we evaluate audio-visual PTTMs trained with clean data on a challenging cocktail-party testbed derived from the AVCocktail dataset, and analyse their adaptation behaviour to this new domain. Experimental results show cons...
  </details>

- **2026-09-15** — Liana Toderean, Tudor Cioara, Vasilis Michalakopoulos et al. — [Distributed JEPA: A Self-Supervised Framework for Energy Forecasting](http://arxiv.org/abs/2609.17029v1)
  <details><summary>📄 Abstract</summary>
  Traditional energy forecasting solutions rely on task-specific supervision and energy asset representations, limiting transferability and the ability to capture general temporal dynamics across heterogeneous assets. We address this by proposing a distributed Joint Embedding Predictive Architecture (JEPA) for self-supervised learning from heterogeneous energy time-series. The framework predicts latent representations of masked temporal segments while integrating temporal observations and contextu...
  </details>

- **2026-09-15** — Qinhong Lin, Yuhao Zhang, Yinglun Feng et al. — [SKIP: a Self-knowledge-guided Step-wise Preference Learning Framework for Concise Reasoning](http://arxiv.org/abs/2609.17019v1)
  <details><summary>📄 Abstract</summary>
  While Chain-of-Thought (CoT) reasoning has been proven to be effective, it often leads to overthinking, resulting in computational overhead, inference latency, and even degraded performance in large language models (LLMs). Existing concise reasoning frameworks significantly compromise accuracy while compressing the length of output. In this paper, we propose SKIP, a self-knowledge-guided step-wise preference learning framework. Starting with lightweight fine-tuning to adjust the model's output s...
  </details>

- **2026-09-15** — Philipp Grünter, Karl Henrik Johansson, Angela Fontan — [On personal recommendations in social networks](http://arxiv.org/abs/2609.17011v1)
  <details><summary>📄 Abstract</summary>
  Social networks in which algorithms actively influence humans through personal recommendations are ubiquitous. While opinion dynamics is an established tool to analyze these systems, existing models typically do not capture how individual agents process personal recommendations. In this work, we introduce a model for personal recommendations that is analytically tractable and consistent with the confirmation bias phenomenon from behavioral psychology. We describe how individuals process recommen...
  </details>

- **2026-09-15** — Julio C. Amador Diaz Lopez — [When Confidence Signals Disagree: Local and Global Confidence in Autoregressive Language Models](http://arxiv.org/abs/2609.16933v1)
  <details><summary>📄 Abstract</summary>
  Modern predictive systems expose multiple quantities that are commonly interpreted as measures of confidence. However, these quantities can summarize different aspects of the predictive process. This distinction matters when confidence is used to evaluate reliability or inform downstream oversight and control. We investigate whether different confidence readouts are empirically interchangeable in an autoregressive language model by comparing local confidence, defined from the probability of the ...
  </details>

- **2026-09-15** — Guy Azran, Michael Navat, Sarah Keren — [Bridging Learned Visual Perception and Symbolic Belief-Space Planning](http://arxiv.org/abs/2609.16884v1)
  <details><summary>📄 Abstract</summary>
  In partially observable settings, agents must act without full knowledge of the world state and rely on uncertain state-estimation pipelines. Obtaining grounded and verifiable symbolic plans under such uncertainty remains a key challenge. Recent work has integrated Vision-Language Models (VLMs) to bridge perception and symbolic reasoning, following two main paradigms. The first, VLM-as-planner, maps images directly to action sequences, and the second, VLM-as-grounder, grounds observations into s...
  </details>

- **2026-09-15** — Ting-Wei Chang, Po-Chun Chen, Hen-Hsen Huang et al. — [Smarter by the Moment: Environment-Driven Dynamic Policies for Continual LLM Improvement](http://arxiv.org/abs/2609.16800v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved remarkable progress across diverse domains, but continual adaptation to evolving tasks and environments remains a key challenge. Existing memory-augmented approaches retrieve individual past examples as direct references, but do not explicitly synthesize actionable strategies from them, causing the same types of errors to recur. We propose Dynamic Retrieval-based Policy Generation (DRPG), a framework that integrates memory-based retrieval with a dynamic...
  </details>

- **2026-09-15** — Ruibo Wang, Ziyi Shen, Huaming Wu et al. — [FSANet: Frequency-Spatial Aware Network for Image Segmentation](http://arxiv.org/abs/2609.16773v1)
  <details><summary>📄 Abstract</summary>
  Image segmentation remains challenging due to occlusions, poor lighting, and irregular structures. Although transformer-based methods achieve high accuracy, they rely heavily on long-range spatial features, leading to high computational costs and neglecting prior knowledge or noise patterns, resulting in missing details and unclear boundaries. To address these issues, we propose Frequency Spatial Aware Network (FSANet), which integrates prior knowledge with a dual-domain solver to sequentially a...
  </details>

- **2026-09-15** — Ferran Bohigas-Daranas, Hamid Latif-Martínez, Eduardo Prieto-Araujo et al. — [Unified Heterogeneous Graph Neural Network solver for Power Flow, Optimal Power Flow and State Estimation](http://arxiv.org/abs/2609.16738v1)
  <details><summary>📄 Abstract</summary>
  Power Flow (PF), Optimal Power Flow (OPF), and State Estimation (SE) are fundamental problems in power system analysis, but solving them is computationally expensive. Graph Neural Networks (GNNs) have been proposed as fast surrogates, yet existing solvers are trained for a single problem at a time, producing narrow models that must be rebuilt for each new task.   We propose a more general approach: a single Heterogeneous Residual Gated Graph Convolutional Network that solves all three problems w...
  </details>

- **2026-09-15** — Kazushi Maruo, Ryota Ishii, Yusuke Yamaguchi et al. — [A flexible framework for treatment effect inference in longitudinal clinical studies with skewed outcomes](http://arxiv.org/abs/2609.16670v1)
  <details><summary>📄 Abstract</summary>
  Longitudinal continuous outcomes in clinical trials are commonly analyzed using mixed models for repeated measures (MMRM) under normality assumptions. However, many clinical outcomes are skewed, making mean-based treatment effects difficult to interpret and potentially reducing statistical efficiency. The Box--Cox MMRM (BCMMRM) approach accommodates skewness by enabling inference on model-based median differences via inverse transformation. However, BCMMRM typically assumes a common transformati...
  </details>

- **2026-09-15** — Mathurin Petit, Emir Torun, Louis Brusset et al. — [FlowATC: Aircraft Trajectory Prediction via Flow Matching](http://arxiv.org/abs/2609.16528v1)
  <details><summary>📄 Abstract</summary>
  Building accurate decision-support tools for next-generation air traffic control requires robust trajectory prediction models. We present a flow-matching architecture trained exclusively on historical aircraft trajectories, with no route labels or chart supervision. Trained on 1.15 million Automatic Dependent Surveillance-Broadcast trajectory windows collected over the San Francisco Bay Area, the model generates aircraft trajectory distributions that closely match historical traffic, reproducing...
  </details>

- **2026-09-15** — Bilvin Varughese, Aditya Koneru, Adil Muhammad et al. — [Symbolic Ensemble Learning Enables Discovery of Fast Accurate Physics-Based Interatomic Potentials](http://arxiv.org/abs/2609.16526v1)
  <details><summary>📄 Abstract</summary>
  Machine learning has transformed materials simulation by delivering force fields with ab initio accuracy, yet bridging the gap between high-dimensional regression and physical interpretability remains a grand challenge. Conventional analytical potentials offer transparency but often fail to capture the complexity of far-from-ground state regimes. Here, we introduce a hybrid symbolic-neural framework that unifies the interpretability of the Embedded Atom Method (EAM) with the adaptability of data...
  </details>

- **2026-09-14** — Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas et al. — [BLINDSPOT: A Benchmark for Safety and Refusal Calibration in Long-Horizon Tool-Using Agents](http://arxiv.org/abs/2609.16305v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly operate over long-horizon interactions involving tool use, persistent state, evolving authorization, and external environment feedback. In such settings, safety failures may emerge only after multiple turns, yet existing evaluations often reduce agent behavior to task or attack success, obscuring whether an agent acts, refuses, or remains appropriately calibrated as the interaction evolves. We introduce Blindspot, a benchmark for trajectory-level sa...
  </details>

- **2026-09-14** — Chaofan Wang, Xiaodong Gu, Yuling Shi et al. — [Translator vs. Challenger: Adversarial Agentic Learning for C-to-Rust Translation](http://arxiv.org/abs/2609.15381v1)
  <details><summary>📄 Abstract</summary>
  C-to-Rust translation remains challenging due to the substantial semantic gap between the two languages. Recent experience-enhanced LLM translators improve translation quality by learning reusable insights from prior failures and repairs. Yet learned insights do not automatically constitute reusable translation knowledge: derived from sparse, program-specific traces, they often contain missing conditions, narrow applicability boundaries, or overlooked corner cases. This limits their robustness a...
  </details>

- **2026-09-14** — Sarra Gharsallah, Adele Robaldo, Mariia Tokareva et al. — [Can We Trust the Judges? Validation of Factuality Evaluation Methods via Answer Perturbation](http://arxiv.org/abs/2609.15561v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the factual correctness of large language models (LLMs) is vital for many applications. But are our evaluation tools themselves trustworthy? Despite the rise of factuality-based metrics, their sensitivity and reliability remain underexplored. This paper introduces a meta-evaluation framework that systematically tests these metrics using controlled corruptions of gold standard answers. Our method generates ranked outputs with known degrees of degradation to probe how metrics capture nu...
  </details>

- **2026-09-14** — Lindsay Spoor, Aske Plaat, Thomas Moerland — [Evaluation Metrics for Safe Reinforcement Learning](http://arxiv.org/abs/2609.15315v1)
  <details><summary>📄 Abstract</summary>
  Safe reinforcement learning (RL) is commonly formalized as a Constrained Markov Decision Process (CMDP), in which an agent maximizes expected reward while keeping its expected cumulative cost below a specified safety bound. Existing safe RL benchmarks predominantly report whether an algorithm is safe on average, following this expectation-based guarantee. We argue that this convention is insufficient to reliably characterize an algorithm's true safety: it fails to capture how often and how sever...
  </details>

- **2026-09-14** — Dylan Waldner, Yiannis Kantaros, Guido Governatori et al. — [Legislating World-Model-Based Planning with Legal Reasoning](http://arxiv.org/abs/2609.15113v1)
  <details><summary>📄 Abstract</summary>
  As robotic systems grow more general, legal norms are needed to integrate them into society. This paper extends the isomorphism problem of aligning legal source texts with their encodings, and measures two key challenges to robot normative control: (1) the \textit{grounding isomorphism gap}, where perception error grounds false atoms for legal reasoning, and (2) the \textit{ontological isomorphism gap}, where one legal conclusion admits many faithful translations into planning constraints. The p...
  </details>

- **2026-09-14** — Shwai He, Haichao Zhang, Shen Yan — [Disentangling Representation Evolution in Transformers through Directional Decomposition](http://arxiv.org/abs/2609.15975v1)
  <details><summary>📄 Abstract</summary>
  Transformer representations evolve through learned additive transformations that either preserve their current direction or redirect it. We study this evolution as a functional geometry, decomposing learned updates into parallel and perpendicular components. Across pretrained models, we find substantial parallel components beyond the residual identity path. We then apply the decomposition in two spaces: to attention and MLP updates relative to the hidden state, and to attention value aggregation...
  </details>

- **2026-09-14** — Zhenjie Yang, Yideng Zhang, Dongjie Zhang et al. — [Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands](http://arxiv.org/abs/2609.15726v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing provides contact information that can be difficult to infer from vision alone, but tactile hardware for dexterous hands has not converged to a common design. Dexterous hands differ in finger structure, contact surfaces, and sensor layouts, while simulated tactile signals still differ from measurements produced by physical sensors. These factors make it difficult to study visuo-tactile manipulation across diverse dexterous hands within a consistent experimental setting. We present...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 13 papers

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

- **2026-09-15** — Fengshuo Liu, Ying Liu, Ruize Sun et al. — [Coding Agents Have Converged: Why the SWE-bench Leaderboard Can No Longer Order Its Top Entries, and What to Measure Instead](http://arxiv.org/abs/2609.17394v1)
  <details><summary>📄 Abstract</summary>
  Small differences on coding-agent leaderboards are often read as an ordering of systems. We audit whether the published verdicts support this reading, using 254 SWE-bench submissions across four splits without running models. On Verified, the leading two entries each resolve 396 of 500 instances. The top ten share 285 successes and 51 failures, leaving 164 instances that distinguish their outcomes. Frontier solution sets have median nesting 0.935 against a score-implied baseline of 0.774, indica...
  </details>

- **2026-09-15** — Jim Berend, Reduan Achtibat, Daniel Schäffer et al. — [ResLRP: The Role of Residual Cancellation in Attribution Instability in Vision Transformers](http://arxiv.org/abs/2609.17152v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) are central to most modern vision models, yet obtaining input attributions that are fine-grained, faithful, and stable remains challenging. Layer-wise Relevance Propagation (LRP) has been adapted to transformer attention, but in ViTs it often produces noisy, unfaithful explanations. We show that the missing ingredient is the treatment of residual connections: cancellation effects in residual pathways lead to attribution explosion. Moreover, we find that these cancellat...
  </details>

- **2026-09-15** — Weiming Li, Ana Catarina Fidalgo Barata, Miguel Constante et al. — [DiaWhisper-DPO: Role-Attributed Transcription of Clinical Interviews via Failure-Mined Preference Optimization](http://arxiv.org/abs/2609.16661v1)
  <details><summary>📄 Abstract</summary>
  Automated depression screening from clinical interviews requires attribution of utterances to the clinician or patient. We evaluate two datasets: DAIC-WOZ, where participant-only recordings require re-synthesizing both sides for controlled two-party evaluation, and PDCH-HAMD, comprising voice-converted real Chinese interviews for cross-lingual validation. Cascaded systems combine speaker diarization with role-assignment heuristics, so errors can propagate across stages. We propose an end-to-end ...
  </details>

- **2026-09-15** — Yao Zhao, Aditya Shanmugham, Swastik Roy et al. — [EchoPath: Execution-Level Replayable Memory for GUI Agents](http://arxiv.org/abs/2609.16635v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents increasingly operate browsers, software, and desktop applications via CLI or API portals, but graphical user interface (GUI) still plays an important role in common industrial production scenarios. GUI agents commonly employ fresh observe-plan-ground-act loops, which is inefficient for enterprise tasks that repeatedly update records, process forms, configure tools, and export reports. We introduce EchoPath, a model-agnostic harness that converts artifact-validated GUI traject...
  </details>

- **2026-09-15** — Paul Denny, Gweneth Barbre, Musa Blake et al. — [Testing Our Foundations: Citation Trends, Errors, and Emerging Hallucinations in the Computing Education Literature](http://arxiv.org/abs/2609.16574v1)
  <details><summary>📄 Abstract</summary>
  Accurate references are foundational to scholarly work, enabling verification, attribution, and systematic review. However, the rapid adoption of large language models has introduced a serious integrity concern: plausible-looking but fabricated citations. Although hallucinated references are widely discussed, their visibility within specific research communities remains unclear. We address this gap by examining reference integrity at key computing education venues using ACM Digital Library data....
  </details>

- **2026-09-14** — Hyojung Han — [Where Post-Training Quantization Breaks Text Embedders: A Measured Map Across Four Embedder Families](http://arxiv.org/abs/2609.16391v1)
  <details><summary>📄 Abstract</summary>
  Weight-only post-training quantization is the cheapest way to shrink a retrieval embedder, and the received advice for applying it -- protect the embedding table, allocate bits by module sensitivity, prefer a ranking-aware objective over weight reconstruction -- was carried into LLM quantization largely intact. We test that advice on retrieval embedders directly, quantizing five checkpoints from four architecture families across a grid of bit widths and group sizes, and isolating the embedding, ...
  </details>

- **2026-09-14** — Shuai Wang, Yize Zhao, Qingyu Chen — [CLEAR: Cross-Source Evidence Adjudication for Large Language Models in Medicine](http://arxiv.org/abs/2609.16301v1)
  <details><summary>📄 Abstract</summary>
  Medical knowledge evolves continuously, whereas the parametric knowledge encoded in large language models (LLMs) is fixed at training time. External retrieval, including retrieval-augmented generation (RAG), can provide access to newly available evidence, but retrieved information may be irrelevant, incomplete, or conflicting. As a result, external retrieval can in turn degrade the factual accuracy and evidence grounding of LLM outputs. To address this challenge, we propose \textbf{CLEAR}, an ag...
  </details>

- **2026-09-14** — Zvi Kons, Avihu Dekel, Hagai Aronowitz et al. — [Word Timestamps and Speaker Attribution with a Non-Autoregressive LLM](http://arxiv.org/abs/2609.15218v1)
  <details><summary>📄 Abstract</summary>
  Timestamps and speaker attribution are useful additions to speech recognition, creating a rich text transcript. This information can either be extracted during transcription or aligned to a given transcript. In this paper we present models that add timestamps and speaker information to a given transcript using a non-autoregressive LLM-based architecture. Compared to an autoregressive model built from similar components, the models are more accurate and annotate a given transcript one to two orde...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-09-16** — Oded Ovadia, Elad Ben Zaken, Elad Guttman et al. — [MiST: Mid-Training LLMs for Cybersecurity](http://arxiv.org/abs/2609.18496v1)
  <details><summary>📄 Abstract</summary>
  Cybersecurity combines high-stakes analysis with complex technical language, making it an impactful and challenging domain for LLMs. We present MiST (Mid-trained Security Transformer), a suite of 8B and 32B models that achieve strong performance on public cybersecurity benchmarks. We use mid-training as an intermediate adaptation stage between general pre-training and cybersecurity training. Rather than performing continual pre-training over large volumes of raw domain text, we curate a compact,...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 8 papers

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

- **2026-09-15** — Haiping Du, Linping Chan — [Large Language Models in the Loop: A Stability- and Network-Aware Survey in Networked Control, Cyber-Physical, and Multi-Agent Systems](http://arxiv.org/abs/2609.16599v1)
  <details><summary>📄 Abstract</summary>
  Modern networked control systems (NCSs), cyber-physical systems (CPSs), and complex multi-agent network systems (CNSs) increasingly rely on large language models (LLMs) for high-level decision-making. However, the slow, stochastic nature of LLMs directly conflicts with the strict stability and safety guarantees required by these physical systems. This survey presents a unified analysis of how LLMs can be admitted into the control loop of NCS, CPS, and CNS without compromising closed-loop guarant...
  </details>

- **2026-09-15** — Nanjie Yao, Hao Wang, Chong Cheng et al. — [World Models for Embodied Intelligence: From Plausible to Controllable to Actionable](http://arxiv.org/abs/2609.16697v1)
  <details><summary>📄 Abstract</summary>
  World models connect perception and decision-making in embodied intelligence by maintaining hidden state, anticipating consequences, comparing interventions, and adapting when execution departs from expectations. Although progress is often measured by visual fidelity, their value lies in improving behavior. Before reaching for a cup, a person anticipates its weight and resistance to grasping, shaping the hand before contact. Such anticipation is coarse and rarely pictorial, yet it guides action....
  </details>

- **2026-09-15** — Qizhou Wang, Bogdan Mamaev, Christopher Leckie — [Towards Detecting AI-Assisted Responses in Online Surveys](http://arxiv.org/abs/2609.17317v1)
  <details><summary>📄 Abstract</summary>
  The use of LLMs to complete online surveys impacts the validity of survey-based research, but detecting such usage remains underexplored. We introduce an initial benchmark dataset, namely ASURRE, for AI-assisted survey participation to capture usage strategies ranging from full generation and revision to persona-grounded agentic completion. Controlled by these strategies, LLM-assisted survey responses are generated using multiple LLMs on three real-world surveys in different disciplines, paired ...
  </details>

- **2026-09-15** — Kirill Skobelev, Eric Fithian, X. Y. Han — [Fine-Tuning Fixes Mode Collapse and Over-Dispersion in LLMs](http://arxiv.org/abs/2609.16454v1)
  <details><summary>📄 Abstract</summary>
  Recent work by Doshi and Hauser (2024), Bisbee et al. (2024), and Xie et al. (2026) raises concerns that outputs from large language models (LLMs) tend to be under-diverse: they repeat or resemble one another more often than responses from the population they are meant to represent, a phenomenon known as mode collapse. In this work, we show that whether mode-collapse, or its opposite, occurs depends on the specific model and dataset used. Further, with sufficient supervised fine-tuning (SFT) dat...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 166 papers

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

- **2026-09-15** — Amir Taubenfeld, Zorik Gekhman, Avigail Grinstein-Dabush et al. — [Verifiable Social Reasoning for LLM Assistants](http://arxiv.org/abs/2609.17496v1)
  <details><summary>📄 Abstract</summary>
  LLM assistants are widely used for daily social advice, yet evaluating their social reasoning in such consultation settings remains challenging since (i) it requires setups where the assistant learns about social situations from subjective user narratives, and (ii) social properties, such as others' intentions, typically lack verifiable ground truth. To address these challenges, we introduce Fuse, a multi-agent simulation framework for studying user-mediated social reasoning. In Fuse, a target a...
  </details>

- **2026-09-15** — Gjergj Plepi, Sven Behnke — [SlotDiT: Object-Centric Representations for Diffusion Transformers](http://arxiv.org/abs/2609.17414v1)
  <details><summary>📄 Abstract</summary>
  Text-conditioned latent diffusion models perform strongly in video generation and are promising backbones for robotic applications. However, existing approaches rely on pixel-level or VAE-based latent representations that lack explicit semantic structure, leaving the impact of the representation space largely unexplored. Slot-based object-centric representations offer a structured alternative by decomposing scenes into object-level latents, or slots. While they have shown success in dynamics mod...
  </details>

- **2026-09-15** — Danxuan Liang, Chun Yin Li, Zheng Wei et al. — [LumiNote: LLM-Assisted Multimodal Instruction for VR Stage Lighting Education](http://arxiv.org/abs/2609.17335v1)
  <details><summary>📄 Abstract</summary>
  Stage lighting education requires instructors to bridge abstract concepts, technical operations, and learner-understandable representations. While Virtual Reality (VR) removes physical constraints, existing systems provide limited support for live instruction. We present LumiNote, an LLM-assisted VR system that transforms spoken pedagogical intent into instructor-reviewable spatial annotations, executable demonstrations, and linguistic support. In an exploratory study with 3 instructors and 24 s...
  </details>

- **2026-09-15** — Lyes Saad Saoud — [Machine Zygote: Causal Biparental Heredity Before Learning in a Germline--Soma Artificial Agent](http://arxiv.org/abs/2609.17300v1)
  <details><summary>📄 Abstract</summary>
  Artificial ontogeny, developmental encodings, robot reproduction, and inherited controllers are established research directions, yet a narrower question remains: can a newborn artificial agent exhibit measurable biparental heredity before learning, and can that dependence be isolated causally rather than inferred only from parent-offspring resemblance? We introduce Machine Zygote, a computational germline-soma architecture designed to test this question. Two parental germlines are independently ...
  </details>

- **2026-09-15** — Marco Luca Sbodio, Marcos Martínez Galindo, Vanessa Lopez et al. — [Extracting ontology-compliant knowledge from scientific text describing irradiated materials using large language models](http://arxiv.org/abs/2609.17291v1)
  <details><summary>📄 Abstract</summary>
  The quest for new materials increasingly relies on predictive models and comprehensive simulations that span scales from atomic to macroscopic levels. However, essential data necessary for these models and simulations are often embedded in scientific literature as unstructured text, limiting reusability and posing challenges for researchers seeking to leverage existing knowledge effectively. While extracting structured data from unstructured text using large language models is gaining popularity...
  </details>

- **2026-09-15** — Maxim Mednikov, Oren Gal — [Calibrate Once, Fly Any Team: Residual-Grounded Low-Fidelity Training for Cooperative Drone Swarms](http://arxiv.org/abs/2609.17265v1)
  <details><summary>📄 Abstract</summary>
  Training multi-agent drone-swarm policies directly in high-fidelity (HF) rigid-body physics is accurate but computationally expensive. This cost scales poorly with team size, as each additional agent multiplies contact-resolution complexity and sharply raises the in-simulation crash rate. To address this, we propose a mixed-fidelity training scheme that eliminates HF reinforcement learning entirely.   A single shared, decentralized policy is optimized inside a fully-differentiable, JAX-native lo...
  </details>

- **2026-09-15** — Cai Ke, Jiangyue Yan, Han Zhang et al. — [Interactive Memory Learning for Long-Term Conversations](http://arxiv.org/abs/2609.17088v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in large language models have significantly enhanced the capabilities of agents in modeling long-term conversations. Despite these successes, existing approaches typically adopt a static heuristic paradigm, where information is passively archived without adaptive memory valuation. Consequently, these methods fail to self-evolve or align their memory management with evolving user needs. To address this, we propose ICML (InteraCtive Memory Learning), a multi-agent framework tha...
  </details>

- **2026-09-15** — Zhang Nengbo — [Waggle Dance Inspired Motion Communication for Multiple UAVs in MuJoCo](http://arxiv.org/abs/2609.16958v1)
  <details><summary>📄 Abstract</summary>
  The honeybee waggle dance motivates a communication mechanism in which one agent's movement conveys spatial information that guides other agents' actions. This paper presents a MuJoCo system that extends the point-to-point motion communication setting of MoCom to one performer and multiple observers. A performer broadcasts a six-bit navigation payload using four flight primitives and explicit null signals. Each of one to five observers processes its own onboard RGB images, extracts optical-flow ...
  </details>

- **2026-09-15** — Zeyuan Huang, Gang Chen, Zixuan Hao et al. — [Artificial Intelligence-Enabled Space Robot Operations: Technologies, Challenges and Prospects](http://arxiv.org/abs/2609.16880v1)
  <details><summary>📄 Abstract</summary>
  Space robots are increasingly expected to perform long-duration, contact-rich, and multi-stage operations with limited human intervention. Recent advances in artificial intelligence (AI), robot learning, and embodied foundation models provide new opportunities to improve the autonomy and adaptability of such systems, but their transfer to space is constrained by scarce mission data, space-specific dynamics and sensing conditions, limited onboard resources, and stringent safety requirements. This...
  </details>

- **2026-09-15** — Pengfei Zhu, Julien Lecompagnon, Mathias Ziegler — [Can Deep Learning Achieve Cross-Physics Mapping?](http://arxiv.org/abs/2609.16853v1)
  <details><summary>📄 Abstract</summary>
  Can deep learning translate physical fields governed by fundamentally different equations? We address this question by introducing Cross-Physics Mapping (CPM), an operator-learning framework for mappings between heterogeneous physical domains. We formulate sufficient conditions for such mappings through compatible latent representations and propose a dimensionless scaling principle that aligns the characteristic evolution scales of the source and target systems without assuming their dynamical e...
  </details>

- **2026-09-15** — Keisuke Masuda, Kazutaka Yatsushiro, Hirohumi Iwamoto et al. — [Japanese Stroke LLM Evaluation: A Conversational Benchmark for Safe Stroke Care in Japanese Using Large Language Models](http://arxiv.org/abs/2609.16739v1)
  <details><summary>📄 Abstract</summary>
  Background: Large language models (LLMs) have achieved physician-comparable performance on multiple-choice medical knowledge examinations, but their capabilities in clinical history taking, urgency assessment, and safety remain insufficiently evaluated. We proposed Japanese Stroke LLM Evaluation, a multi-turn conversational benchmark for stroke care in Japanese, and evaluated LLM performance and safety under practice-oriented conditions. Methods: We created 10 stroke and related-condition cases ...
  </details>

- **2026-09-15** — Wen Bing, Bing Li — [SpecLens: LLM-Based Verilog Generation with Specification-Derived Constraints via Behavioral Divergence](http://arxiv.org/abs/2609.16729v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently shown promise in Verilog generation, but producing functionally correct RTL directly from natural-language specifications remains a highly challenging task. Existing approaches improve LLM-based Verilog generation mainly with retrieval-augmented generation (RAG), self-planning, or few-shot prompting. However, these methods focus primarily on external or generic forms of enhancement rather than strengthening the specification with task-specific constrain...
  </details>

- **2026-09-15** — Tingyu Guo, Reza Langari — [CorrRisk-WM: Corridor-Conditioned Risk World Modeling for Safety-Critical Trajectory Planning](http://arxiv.org/abs/2609.16724v1)
  <details><summary>📄 Abstract</summary>
  Safe local planning requires forecasting surrounding-agent motion and evaluating candidate-specific risks, since identical agent motion can pose different risks to different ego trajectories. We present CorrRisk-WM, a planning-oriented partial world model coupling environment evolution with supervised intrusion and near-miss prediction over bounded candidate-trajectory corridors. A latent environment model recursively predicts agent states and updates agent-agent and agent-map interactions. Each...
  </details>

- **2026-09-15** — Sifan Zhou, Qiwei Wang, Linyue Tan et al. — [MAETrack: Unleashing the Potential of Pretrained Geometric Priors for 3D Single Object Tracking](http://arxiv.org/abs/2609.16695v1)
  <details><summary>📄 Abstract</summary>
  Large-scale pre-training has transformed representation learning in 2D vision, yet its transferability to 3D single object tracking (SOT) remains insufficiently understood. Directly fine-tuning self-supervised 3D encoders, such as masked autoencoders (MAE), often leads to sub-optimal adaptation because the reconstruction objective is not fully aligned with the spatial-temporal matching requirements of tracking. In this paper, we observe that this difficulty can be interpreted as a layer-wise tra...
  </details>

- **2026-09-15** — Minghua He, Lingzhe Zhang, Yuan Liu et al. — [GrowMTP: Can RL Grow Its Own Draft Head?](http://arxiv.org/abs/2609.16648v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) post-training drives the frontier capabilities of large language models, with its wall-clock dominated by autoregressive rollout generation. Speculative decoding is an established remedy for this bottleneck, but existing draft heads must be pretrained or warmed up before RL, introducing substantial training cost outside the RL run to be accelerated. We observe that RL training itself provides both conditions required for online draft-head training: its rollout distrib...
  </details>

- **2026-09-15** — Yang Zhao, Zhuo Chen, Xubo Yang — [EgoPathBench: Evaluating Zero-Shot Egocentric Waypoint Decision-Making in Vision-Language Models](http://arxiv.org/abs/2609.16610v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot waypoint navigation requires vision-language models to select, from the current first-person observation, a sequence of spatial actions that is feasible for the agent and reaches the goal, placing joint demands on the integrated spatial intelligence of today's foundation VLMs. Existing spatial-intelligence benchmarks primarily evaluate isolated judgments of relations, directions, or targets and therefore do not directly measure the integrated navigation ability required to combine targ...
  </details>

- **2026-09-15** — Jun Chen, Qi Zhao, Yunliang Jiang et al. — [A multimodal large language model for evidence-based autism spectrum disorder screening](http://arxiv.org/abs/2609.16464v1)
  <details><summary>📄 Abstract</summary>
  The clinical management of autism spectrum disorder (ASD) faces a bottleneck in early screening, mainly because trained specialists are scarce and conventional assessment tools are subjective. Here, we introduce ASDchat, a multimodal large language model designed for evidence-based ASD screening, which takes video, audio, and dialogue as input. ASDchat adopts a dual-branch architecture, where the decision branch generates screening probabilities and the evidence branch generates traceable, times...
  </details>

- **2026-09-15** — Fabian Harlacher, Christian Friedrich — [CAD-Based Relation Learning and Geometric-Symbolic Planning for Robotic Assembly](http://arxiv.org/abs/2609.17263v1)
  <details><summary>📄 Abstract</summary>
  Assembly Sequence Planning (ASP) remains a challenging problem due to its combinatorial nature, making exhaustive planning approaches impractical for complex industrial assemblies. Furthermore, many CAD models lack reliable semantic contact information or require extensive manual preprocessing, limiting the applicability of existing methods. This paper presents a hybrid ASP framework combining learning-based relation extraction with geometric-symbolic reasoning to generate feasible robotic disas...
  </details>

- **2026-09-15** — Zhenyang Feng, Jimin Heo, Erik B. Sudderth et al. — [TEMPO: Learning Temporal Context for Dynamic Robot Manipulation](http://arxiv.org/abs/2609.16864v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have achieved impressive performance in quasi-static manipulation, but struggle in dynamic manipulation tasks because they operate on a single observation at inference time. We identify two representational failures that underlie this limitation. The first is motion ambiguity, where a single observation does not include scene dynamics and therefore cannot anticipate the future state of moving objects. The second is state aliasing, where visually similar observ...
  </details>

- **2026-09-15** — Bo Kang — [The Latent That Never Was: A Forensic Re-run of the CVAE Ablation in Action Chunking Transformer](http://arxiv.org/abs/2609.16745v1)
  <details><summary>📄 Abstract</summary>
  Action Chunking Transformers (ACT) are widely used to learn robot manipulation from demonstrations. Their conditional variational autoencoder includes an encoder meant to capture differences between demonstrations during training. The original ACT paper reported that encoder removal dropped the mean success rate from 35% to 2% on two simulated tasks with human demonstrations. We re-ran this ablation in the original code and checked whether the findings depend on the implementation or training da...
  </details>

- **2026-09-15** — Hyesung Lee, Si-Hwan Heo, Sungwook Yang — [UniDex-ViTac: Learning Unified Visuo-Tactile Dexterous Manipulation Policy from Human Video Data](http://arxiv.org/abs/2609.16504v1)
  <details><summary>📄 Abstract</summary>
  Human videos provide demonstrations of dexterous manipulation but lack robot-executable actions and tactile measurements. We present UniDex-ViTac, a framework that uses human-video-guided simulation to generate robot demonstrations paired with fingertip contact observations for training a deployable visuo-tactile policy. Object-specific residual reinforcement learning specialists adapt annotated human-object interaction references to a robotic arm-hand system. Their successful rollouts pair fina...
  </details>

- **2026-09-15** — Zhaoyang Wei, Zipeng Wang, Yushe Cao et al. — [Video-HolmesV2: Can MLLMs Reason with Spatio-Temporal Audio-Visual Evidence in Long Videos?](http://arxiv.org/abs/2609.17248v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models have demonstrated impressive video understanding, yet their ability to reason over long-form narratives is often masked by visual-centric evaluations and inefficient context processing. Existing benchmarks over-rely on visual heuristics while marginalizing auditory cues, effectively reducing models to "silent observers" that bypass genuine cross-modal reasoning. Moreover, standard dense sampling creates an evidence-context trade-off: increasing frames to capture ...
  </details>

- **2026-09-15** — Mohammad Ammar Mughees, Giovanni Montefoschi, Zhongxin Chen et al. — [From Foundation Embeddings to Cropland Maps: Label Efficiency, Temporal Transferability and Independent Human Validation](http://arxiv.org/abs/2609.17138v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models provide reusable representations of satellite imagery that support downstream mapping with limited task-specific modelling. We evaluate whether annual AlphaEarth embeddings support binary cultivated-versus-non-cultivated mapping in Maine, USA, using 192 spatially separated patches and labels derived from the USDA Cropland Data Layer (CDL). Without fine-tuning the foundation model, a lightweight classifier reaches 93.7% overall accuracy and 90.8% balanced accuracy on ...
  </details>

- **2026-09-15** — Lilian Killich, Marko Schmellenkamp, Fabian Vehlken et al. — [Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs](http://arxiv.org/abs/2609.17111v1)
  <details><summary>📄 Abstract</summary>
  Modelling with mathematical formalisms like logical formulas, mathematical equations, or regular expressions is an important yet challenging task for students of computer science and other STEM disciplines. Identifying common mistakes occurring in this context is an important step towards helping struggling students by providing targeted high-quality feedback, e.g. in interactive learning systems.   We present a tool-supported workflow that allows to (1) identify candidates for common mistakes t...
  </details>

- **2026-09-15** — Shiqi Liu, Zeyu He, Letian Tao et al. — [Beyond Token-Local Imitation: Reward-Compatible Temporal Credit Assignment for On-Policy Distillation](http://arxiv.org/abs/2609.16937v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has emerged as an effective approach for large language model post-training, yet existing objectives face a trade-off between objective fidelity and optimization stability. Token-level OPD provides stable but local supervision, whereas sequence-level OPD captures future credit at the cost of horizon-dependent variance. We establish a unified temporal-credit view of these formulations, showing that practical token-level OPD can be interpreted as a temporal approximati...
  </details>

- **2026-09-15** — Shan-Zhong Li, Zhi Li — [Nonlocal Magic across the Many-Body Localization Crossover](http://arxiv.org/abs/2609.16935v1)
  <details><summary>📄 Abstract</summary>
  Nonlocal magic quantifies the minimum nonstabilizerness attainable under independent local unitary transformations on the two subsystems. Here, we use min-relative nonlocal magic (NLM) to characterize the crossover from ergodicity to many-body localization (MBL) in the random-field XXZ chain. Unlike entanglement entropy, NLM probes how entanglement is organized through the distance of the Schmidt spectrum from dyadic-flat stabilizer spectra. From weak to intermediate disorder, NLM evolves from a...
  </details>

- **2026-09-15** — Chenhao Zeng, Zhibin Pu, Shufei Ge — [HyCoSeq: Contextual Hyperbolic Representation Learning for Genomic Sequences](http://arxiv.org/abs/2609.16925v1)
  <details><summary>📄 Abstract</summary>
  Hyperbolic geometry provides a natural inductive bias for genomic representation learning, but existing hyperbolic genomic models primarily use Lorentz convolutions to learn local sequence representations, while their residual pathways do not directly aggregate full Lorentz representations. We propose HyCoSeq, a contextual hyperbolic representation learning framework for genomic sequences. HyCoSeq incorporates weighted Lorentzian residual aggregation into multi-curvature Lorentz encoding, allowi...
  </details>

- **2026-09-15** — Miłosz Adamczyk, Tymoteusz Zapala, Piotr Borycki et al. — [PiPS: Post-Hoc Prototypical Explanations for Interpretable Semantic Segmentation](http://arxiv.org/abs/2609.16909v1)
  <details><summary>📄 Abstract</summary>
  With the increasing deployment of deep neural networks in critical systems, such as medical diagnostics and autonomous vehicles, ensuring their interpretability is crucial to building trust in decision-making systems. In the field of explainable artificial intelligence, prototype-based reasoning has gained particular popularity, as it mimics human cognitive processes by explaining model decisions based on visual similarity under the looks like this paradigm. While this paradigm has been thorough...
  </details>

- **2026-09-15** — Annirudh K P, Vinayak Rane, Shradha Atakar et al. — [Portable Vector NV-Diamond Magnetometer for Shot-Noise-Limited, Drift-Free Operation in Unshielded Environments](http://arxiv.org/abs/2609.16901v1)
  <details><summary>📄 Abstract</summary>
  Ensemble nitrogen-vacancy (NV) diamond magnetometers combine high sensitivity with vector-field reconstruction, but practical deployment is limited by errors arising from high-frequency laser noise during short-duration operations and slow-varying gain fluctuations and offset drift during long-term operation. Here, we present an integrated digital architecture for achieving NV magnetometry stability across distinct timescales. A dynamic differential readout continuously balances fluorescence and...
  </details>

- **2026-09-15** — Zhengyang Zhang, Haojin Zhou — [The Equivariance Criterion in a Linear Model for Random-$X$ Cases](http://arxiv.org/abs/2609.16897v1)
  <details><summary>📄 Abstract</summary>
  Equivariance is increasingly used in machine learning and statistics, often without systematic justification. In a companion article, the equivariance criterion was applied to the normal linear model with a fixed design matrix (fixed-$X$), yielding the minimum risk equivariant (MRE) estimators of the coefficient vector and of the condensed diagonal covariance matrix under a multivariate invariant location--scale group. We extend these results to the random-$X$ case, with covariates sampled from ...
  </details>

- **2026-09-15** — Fermín Moscoso del Prado Martín — [A Data-free Universal Prior over Syntactic Structures](http://arxiv.org/abs/2609.16854v1)
  <details><summary>📄 Abstract</summary>
  Probability is fundamental to theories of language comprehension, production, acquisition, and evolution, as well as to large language models. Existing theories estimate the probability of syntactic structures from language-specific data. Whether part of this probability structure can arise independently of language-specific experience remains unknown. Here I show that a universal prior over syntactic structures emerges from a cognitively motivated model of incremental language production, in wh...
  </details>

- **2026-09-15** — Younes Boufouss, Luc Pommeret, Thomas Gerald et al. — [Can We Do Interpretable NLI with Graphs Based on Atomic Propositions?](http://arxiv.org/abs/2609.16814v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Model (LLM)-based Natural Language Inference (NLI) systems achieve high accuracy, their decision-making processes lack auditable structures. This paper explores whether NLI can be performed using only interpretable, graph-based representations of evidence. We introduce a fully graph-based pipeline where the classifier never directly processes the input text. Instead, sentences are decomposed into atomic propositions, converted into ConceptNet triples via constrained decoding...
  </details>

- **2026-09-15** — Biswas Rudra Jyoti Arka, Sadman Sakib, Md. Zahidul Islam et al. — [Explainable Post-Disaster Grid Observability Recovery Using Human-Oversight Agentic LLMs](http://arxiv.org/abs/2609.16774v1)
  <details><summary>📄 Abstract</summary>
  Post-disaster phasor measurement unit (PMU) outages reduce power-system observability and degrade operator situational awareness, requiring sequential restoration under limited resources. Existing PMU restoration methods based on optimization or heuristics can generate restoration schedules, but they often provide limited support for explanation, traceability, and operator interaction. This paper proposes an agentic tool-calling framework orchestrated by a large language model (LLM) for post-dis...
  </details>

- **2026-09-15** — Xiaobin Li — [Cartan-Fejer Gram Tomography and Flop Covariance for BPS Resummed Gromov-Witten Potentials](http://arxiv.org/abs/2609.16693v1)
  <details><summary>📄 Abstract</summary>
  We introduce a matrix-valued finite difference formalism for the genus zero BPS resummed local Gromov-Witten potential of a threefold flop. Factoring the central difference as \[ Δ_η=\nabla_η^2, \qquad \nabla_η=T_{hη/2}-T_{-hη/2}, \] we prove that the mixed differences \( \mathbf H=(\nabla_{η_i}\nabla_{η_j}F)_{i,j} \) admit an exact rank one signed \(q\)-Gram decomposition. Primitive BPS classes are therefore detected by rank one coefficient matrices, and a matrix-valued Möbius inversion reconst...
  </details>

- **2026-09-15** — Zhipeng Zhao, Wenxu Wang, Peishun Liu et al. — [Mechanism-Level Evaluation for Vision-Language Models: Controlled Activation-Replacement Diagnosis of Gender Bias](http://arxiv.org/abs/2609.16651v1)
  <details><summary>📄 Abstract</summary>
  Behavioral benchmarking reveals \emph{what} biases exist in vision-language models but not \emph{which internal components} are most sensitive to targeted intervention, precluding principled intervention. We argue for mechanism-level evaluation as a necessary complement, demonstrating causal mediation analysis as a diagnostic instrument for gender bias. We decompose gender-cue effects into controlled indirect effects attributable to specific-layer activations and direct effects through all other...
  </details>

- **2026-09-15** — Zixiu Ding, Zilin Zhao, Yingjie He et al. — [SAVOR: Self-Aware Visual Grounding via Confidence-Calibrated Reinforcement Learning for Multimodal Hallucination Mitigation](http://arxiv.org/abs/2609.16601v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have made strong progress on visual question answering and image captioning, yet they still produce fluent claims about objects, attributes, or relations that are not grounded in the image. Many remedies either modify decoding at test time, which adds latency, or fine tune with preferences such as DPO variants, which teach which answer is preferred but not when the model's own answer is unreliable. We argue that calibrated self assessment is the missing s...
  </details>

- **2026-09-15** — William L. Tong, Aryo Lotfi, Emmanuel Abbe et al. — [On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models](http://arxiv.org/abs/2609.16540v1)
  <details><summary>📄 Abstract</summary>
  State Space Models (SSMs) have emerged as a compelling alternative to Transformers, enabling sequence modeling with constant memory and linear compute. Although SSMs exhibit reasonable performance and favorable computational characteristics, they continue to lag behind Transformers on tasks that require in-context learning and precise retrieval, slowing their adoption for large-scale language modeling. In this work, we demonstrate that both the success and failure of SSMs in these domains can be...
  </details>

- **2026-09-15** — Daniel Ebanks, Devika Jain — [Geospatial Metadata Improves Discoverability by Connecting Datasets Across Scientific Disciplines](http://arxiv.org/abs/2609.16498v1)
  <details><summary>📄 Abstract</summary>
  Research data repositories are essential infrastructure for scientific inquiry and for ensuring that datasets follow FAIR (Findable, Accessible, Interoperable, and Reusable) principles. However, repository reuse depends on the quality and completeness of geospatial and thematic metadata, which researchers generally provide voluntarily. Given limited curation resources, it is unsurprising that even Harvard Dataverse, the world's largest general-purpose research repository, contains many incomplet...
  </details>

- **2026-09-14** — Mahjabin Nahar, Eun-Ju Lee, Yujin Heo et al. — [When AI Says "I Am Unable to Answer": Understanding User Responses to AI Refusals](http://arxiv.org/abs/2609.16191v1)
  <details><summary>📄 Abstract</summary>
  While refusal-based safeguards to mitigate hallucinations in large language models (LLMs) are becoming increasingly common, they may conflict with users' preferences for definitive answers. However, we know little about how users respond to refusals across repeated interactions, when refusals become more or less acceptable, and for whom. In this work, we examine how refusal frequency, explanations, and need for cognitive closure (NFCC) shape responses to AI refusals. Participants (N=599) interac...
  </details>

- **2026-09-14** — Kai Wang, Carlton Baugh, Sownak Bose et al. — [Forged in Quenching: Morphological Transformation across Star-forming and Quiescent Galaxies in EAGLE](http://arxiv.org/abs/2609.16187v1)
  <details><summary>📄 Abstract</summary>
  The connection between morphology and quenching in central galaxies is well established, but its physical origin remains widely debated. We address this by tracing the main progenitor branches of $z=0$ star-forming and quiescent central galaxies in the EAGLE cosmological simulation from $z\gtrsim4$. Their disc-to-total ratio and triaxiality tracks are indistinguishable until $z\approx 1$-$2$, when both diverge concurrently with the onset of quenching, whereas the size and supermassive black hole...
  </details>

- **2026-09-14** — Teanna Barrett, B. Biira, Jainaba Jawara et al. — [Moral Missions: Surfacing Moral Decision-Making Strategies for Responsible Data Science Practice](http://arxiv.org/abs/2609.16166v1)
  <details><summary>📄 Abstract</summary>
  A growing ecosystem of techniques, toolkits, and guidelines has been developed to help data scientists consider the social implications of data-driven technologies. However, prior literature highlights that even when this ecosystem of techniques is provided to professional data scientists, they still struggle to consistently adopt a responsible data science practice. We posit that the key to sustained responsible data science practice is to approach it as a moral mission: a conviction-driven tec...
  </details>

- **2026-09-14** — Pinak Banerjee, Subham Roy, Xingyang Yu — [Symmetry Descent in M-theory, Part I: A Twelve-Dimensional Parent Theory](http://arxiv.org/abs/2609.16141v1)
  <details><summary>📄 Abstract</summary>
  We initiate a symmetry descent procedure for M-theory engineered quantum field theories. Starting from a higher form BF theory supplemented by a cubic bulk topological interaction, we construct a gauge-invariant bulk-boundary system whose edge modes acquire generalized Maxwell--Chern--Simons dynamics after the introduction of a metric-dependent boundary action. The nonlinear contribution to the boundary equation is induced entirely by the cubic bulk interaction. In the case of twelve dimensional...
  </details>

- **2026-09-14** — Ivy Ning Zhang — [Coaching Qwen3 Coder 30B to Think Like a CodeClash Arena Agent](http://arxiv.org/abs/2609.16096v1)
  <details><summary>📄 Abstract</summary>
  Large language model coding agents have recently become useful for software tasks, but weaker or open-weight agents still struggle to reliably interpret user intent and execute complex multi-step workflows. This gap is especially visible in long-horizon settings, where an agent must repeatedly inspect prior outcomes, diagnose failure, and choose the next code edit under interaction constraints. It motivates a natural question: what can we do to improve the thinking process of a weak code agent? ...
  </details>

- **2026-09-14** — Nimit Shah, Haitz Sáez de Ocáriz Borde — [Evaluating Open-Weight E-Commerce Agents with Environment-Grounded Verification](http://arxiv.org/abs/2609.16093v1)
  <details><summary>📄 Abstract</summary>
  A shopping conversation has many routes to the same cart, and a task-success rate reduces all of them to one score. We build a deterministic and reproducible e-commerce environment that precommits each trial's customer and trajectory parameters, including the persona, difficulty, target cart, and an item reveal schedule. A simulated consumer attempts to buy a target cart from the environment with assistance from the evaluated model. The environment guides the simulator's actions and records ever...
  </details>

- **2026-09-14** — Honghao Lin, David P. Woodruff, Yuan Deng et al. — [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](http://arxiv.org/abs/2609.15983v2)
  <details><summary>📄 Abstract</summary>
  Language models can produce plausible short proofs, but may still be unreliable on long-horizon research problems, where progress depends on a sequence of uncertain and interdependent decisions. We introduce Stellar Colosseum, a model-agnostic harness for allocating inference across research in mathematics and theoretical computer science. Colosseum explores alternative strategies before proof construction, uses a readiness gate to decide when a route is mature enough to decompose, represents th...
  </details>

- **2026-09-14** — Micah Adler, John W. Byers, Mark Crovella — [Attention Mean Fields Predict Average Representation Dynamics and Reveal Context-Specific Computation](http://arxiv.org/abs/2609.16382v1)
  <details><summary>📄 Abstract</summary>
  A language model's representation geometry is not predetermined; it evolves as the model runs. A faithful account of that geometry must capture that dynamic process, and so cannot be based solely on model-independent statistics such as co-occurrence. Here we introduce a mean-field analysis of attention. The average attention from one token to another defines a kernel that carries representations layer to layer and can be iterated through the network to model how the geometry is transformed. We c...
  </details>

- **2026-09-14** — Yan Zhu, Yongbo Chen, Zhengming Ding et al. — [ProtoLIP: From Sentence-Level to Object-Level Evidence Disentanglement](http://arxiv.org/abs/2609.16284v1)
  <details><summary>📄 Abstract</summary>
  Query-conditioned vision--language models enable fine-grained interpretation by revealing how visual evidence changes with textual queries. However, evidence conditioned on complete descriptions does not necessarily resolve into object-specific evidence, nor does an exposed evidence map necessarily identify the evidence that constitutes the model's prediction. Across multiple VLM architectures and independent benchmarks, we find that object-level queries often retain evidence from co-occurring o...
  </details>

- **2026-09-14** — Valen Tagliabue, Leonard Dung, Cameron Berg — [The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It](http://arxiv.org/abs/2609.16247v1)
  <details><summary>📄 Abstract</summary>
  Large language models sometimes behave in ways resembling human emotional responses, and recent work has identified internal representations that may explain this. We ask whether LLMs represent pain distinctly from fear, sadness, and generic negative valence, and whether this representation functions as pain would be expected to. We build a dataset describing painful situations across five categories: physical, psychological, social, moral, and cognitive. These are paired with controls for fear,...
  </details>

- **2026-09-14** — H. Yousef, H. Hassan, I. Roy et al. — [A deep dive into Tollmien-Schlichting wave control via passive wall deformations: The battle between local and downstream stabilization, lessons learned, and implications for phononic subsurfaces](http://arxiv.org/abs/2609.16144v1)
  <details><summary>📄 Abstract</summary>
  A decade ago, a landmark study on flow control via subsurface phonons transformed our understanding of fluid-structural interactions, compelling us to reimagine ways by which to suppress boundary layer instabilities. While subsequent investigations have steadily enriched this landscape, several questions remain largely unanswered. The notion of Tollmien-Schlicting (TS) wave stabilization relies on phase-engineered surface interactions, which destructively engage with the wave and impede its grow...
  </details>

- **2026-09-14** — Zhancheng Guo, Congren Dai, Shangda Wu et al. — [MUUNRiver-Bench: Diagnosing Relation-Dependent Music Retrieval with Multimodal Instructions](http://arxiv.org/abs/2609.16090v1)
  <details><summary>📄 Abstract</summary>
  Music retrieval is relation-dependent: given a reference track, a listener may seek its style with a new theme, a cover, or a comparable voice, and these intents demand contradictory rankings. We present MUUNRiver-Bench, a diagnostic benchmark whose reference-audio queries use natural-language instructions to define relevance. A pipeline combining expert genre priors, LLM-generated prompts and lyrics, synthesis, and expert review yields 3,440 tracks spanning 13 genres and 116 sub-genres, and sev...
  </details>

- **2026-09-14** — Jiayue Gaveal Fan, Arul Murugan, Shreyas Krishnan et al. — [Interpreting and Steering LLM Agents for Social Simulations](http://arxiv.org/abs/2609.16436v1)
  <details><summary>📄 Abstract</summary>
  Simulations based on large language models (LLMs) have proven to be powerful for understanding human behavior, making them valuable additions to the social scientific toolkit. However, LLMs are ultimately black boxes based on deep neural networks which limits their value for social science. This is because of a lack of (i) interpretability: i.e. the ability to assign clear mechanisms driving observed behavior; and a lack of (ii) steerability: i.e. the ability to mute or amplify specific theoreti...
  </details>

- **2026-09-14** — Reed Orchinik, David Rand — [A light-touch AI literacy intervention helps protect against AI political persuasion](http://arxiv.org/abs/2609.16432v1)
  <details><summary>📄 Abstract</summary>
  Conversations with large language models (LLMs) can substantially shift beliefs and attitudes, raising concerns about manipulation using AI persuasion. Here we test whether a light-touch AI literacy intervention - a brief warning that LLMs can be prompted to persuade and may present information selectively - helps protect users. Across two experiments (total N = 3,208 Americans) in which participants conversed with an LLM instructed to shift their views about different political topics, the pres...
  </details>

- **2026-09-14** — Peiqi Yu, Mosam Dabhi, Shangtao Li et al. — [ManiSkillFormer: Demonstration-Free Compositional Manipulation via Task-Conditioned Geometric Contracts](http://arxiv.org/abs/2609.16331v1)
  <details><summary>📄 Abstract</summary>
  We present ManiSkillFormer, a neuro-symbolic framework for demonstration-free and compositional robotic manipulation. Instead of learning end-to-end visuomotor policies, ManiSkillFormer introduces task-conditioned geometric contracts that explicitly structure the interface between perception and action. Each manipulation skill declares the semantic geometric primitives required for execution, such as object keypoints and surface normals. Building on human-defined skill structures, LLM agents gen...
  </details>

- **2026-09-14** — Zihan Dong, Yuanzhe Liu, Zhiyuan Ma et al. — [CADWorld: Computer-Use Benchmark for Long-Horizon Computer-Aided Design](http://arxiv.org/abs/2609.16251v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents are increasingly evaluated in realistic desktop environments, but existing benchmarks provide limited coverage of professional engineering workflows whose outputs are persistent, structured artifacts. Mechanical computer-aided design (CAD) is a particularly demanding setting: an agent must manipulate geometry and constraints over long interaction horizons while producing a native project whose dimensions, construction structure, and downstream engineering state remain valid. ...
  </details>

- **2026-09-14** — Christos Galanopoulos, Kimon Antonios Provatas, Ilias Georgakopoulos-Soares — [Feasibility of Homomorphic Inference for a Genomic Foundation Model](http://arxiv.org/abs/2609.16211v1)
  <details><summary>📄 Abstract</summary>
  Human genomic sequences can identify individuals, cannot be replaced after disclosure, and are the inputs that genomic foundation models are designed to interpret. We assess whether a compute provider can execute a released genomic foundation model without receiving query-derived genomic values in plaintext and whether correctness, memory, or cost prevents complete encrypted inference. We first reproduce the released model on three genomic task families and freeze an independently validated nume...
  </details>

- **2026-09-14** — Andrea Morghen, Pierluigi Arpenti, Roberto Schiattarella et al. — [Structure-Preserving Quantum Circuit Architectures for Robot Kinematics](http://arxiv.org/abs/2609.16089v1)
  <details><summary>📄 Abstract</summary>
  Structured spatial data require quantum encodings that preserve geometric relations, expose measurable observables, and remain implementable on finite-depth hardware. This work introduces a quantum representation and circuit architecture for rigid-body transformations and specializes it to Denavit--Hartenberg kinematics of serial open-chain manipulators. Each translational contribution is factorized into a classical metric magnitude and a signed unit direction encoded by a single-qubit Bloch vec...
  </details>

- **2026-09-14** — Honghao Lin, David P. Woodruff, Yuan Deng et al. — [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](http://arxiv.org/abs/2609.15983v1)
  <details><summary>📄 Abstract</summary>
  Language models can produce plausible short proofs, but may still be unreliable on long-horizon research problems, where progress depends on a sequence of uncertain and interdependent decisions. We introduce Stellar Colosseum, a model-agnostic harness for allocating inference across research in mathematics and theoretical computer science. Colosseum explores alternative strategies before proof construction, uses a readiness gate to decide when a route is mature enough to decompose, represents th...
  </details>

- **2026-09-14** — Tobias Ladner, Matthias Althoff — [The Misery of Mechanistic Interpretability: A Formal Perspective](http://arxiv.org/abs/2609.15533v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability has become the dominant lens for understanding frontier language models, as their inner workings are complex and inherently black boxes. To gain insights into these models, interpretable replacement networks (IRNs) are trained at all layers, exposing interpretable features through sparsely activated neurons. However, the faithfulness of an IRN is usually evaluated only empirically on clean data, and we show that even semantically minor input perturbations flip the do...
  </details>

- **2026-09-14** — Zeyang Li, Sunbochen Tang, Navid Azizan — [Safe Meta-Reinforcement Learning via Information Space Reachability](http://arxiv.org/abs/2609.15915v1)
  <details><summary>📄 Abstract</summary>
  Meta-reinforcement learning (meta-RL) enables agents to adapt to unseen tasks with limited experience. Despite its promise, the application of meta-RL in real-world tasks is hindered by safety requirements, which have been underexplored in prior work. In this paper, we propose a safe meta-RL framework that explicitly accounts for safety during adaptation. Our key insight is to reason about safety in the information space, which captures both the physical state and the agent's belief over the und...
  </details>

- **2026-09-14** — Xiaofeng Mao, Peijia Lin, Shaohao Rui et al. — [LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](http://arxiv.org/abs/2609.15863v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion models are stochastic and hard to control: precise content often requires repeated sampling without guaranteed success, and long-horizon scenes drift in appearance, interactions, and temporal coherence. Agentic visual creation provides explicit references, editable 3D scenes, or executable game states for stable control, but does not by itself guarantee high object or character fidelity. Combining the two can enable stable, high-quality generation. To realize this combination, we...
  </details>

- **2026-09-14** — Jocelyn Kang, Caroline Zhang — [KnowBench: Effort Reduction as a Unified, Deployment-Grounded Benchmark for Clinical AI](http://arxiv.org/abs/2609.15794v1)
  <details><summary>📄 Abstract</summary>
  Clinical AI systems are evaluated with instruments built for research settings (reference-based similarity metrics and expert rubric panels) that measure resemblance to an artifact rather than reduction of a burden. We introduce KnowBench, pioneered by Knowtex, whose unifying metric is Effort Reduction (ER): the proportion of system-generated clinical work product accepted by the responsible clinician under expert and safety review. ER is defined once and instantiated per task across the adminis...
  </details>

- **2026-09-14** — Jiajie He, Jiangyuan Hong, Dongling Ni et al. — [Are LLMs Good Financial User Simulators? A Preliminary Study](http://arxiv.org/abs/2609.15727v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as user simulators, but their ability to reproduce evolving individual financial decisions remains unclear. We present a preliminary study in a controlled paper-trading environment with 120 volunteers. Participants used non-redeemable virtual funds under real-time market conditions; no real brokerage accounts, real-money positions, or real transaction records were accessed. Given only information available before a prediction cutoff, a simulator...
  </details>

- **2026-09-14** — Lemen Chao, Zixuan Yang, Anran Fang et al. — [Data storytelling meets interpretable machine learning: Decoding AI decisions for non-experts without revealing sensitive data and model details](http://arxiv.org/abs/2609.15722v1)
  <details><summary>📄 Abstract</summary>
  AI-driven automated decision-making requires both predictive performance and interpretability. Recent advances in interpretable machine learning (IML) provide tools for explaining model predictions, but the technical complexity of these explanations may hinder accessibility to non-experts. To address this challenge, this study integrates data storytelling with IML to enhance the explainability of AI-generated decisions for a broader audience. Following the design science research (DSR) paradigm,...
  </details>

- **2026-09-14** — Jinyuan Deng, Yuqi Jiang, Wenjing Huang et al. — [Circuit-MLLM: Topological Logic-Guided Latent-Space Visual Reasoning for Circuit Schematic Understanding](http://arxiv.org/abs/2609.15668v1)
  <details><summary>📄 Abstract</summary>
  Through pre-training on extensive text and image datasets, current multi-modal large language models (MLLMs) achieve strong performance on general tasks. However, circuit schematics present a unique challenge for MLLMs due to their dense component layouts and distinct topological logic, demanding fine-grained structural parsing to extract the electrical semantics. To address this, we propose Circuit-MLLM, a multimodal reasoning framework that reformulates circuit topology analysis as a process o...
  </details>

- **2026-09-14** — JuHeon Ha, Byounghan Lee, Yunseo Choi et al. — [Empathy Is Steerable but Multi-Axial: Mechanism Geometry and Persona Effects in LLMs](http://arxiv.org/abs/2609.15654v1)
  <details><summary>📄 Abstract</summary>
  Activation steering has been used to control traits such as honesty, refusal, and sycophancy, yet supportive empathy is evaluated along multiple dimensions that need not correspond to independently controllable activation directions. Using the EPITOME framework, which decomposes supportive empathy into Emotional Reactions, Interpretations, and Explorations, we study three instruction-tuned LLMs and ask whether candidate directions derived from these labels produce distinguishable intervention ef...
  </details>

- **2026-09-14** — Haoyu Wang, Jing Yang, Chenyu Liu et al. — [Graph Attention Design Choices Matter: A Controlled Study of LoRA-Adapted Audio Anti-Spoofing](http://arxiv.org/abs/2609.15650v1)
  <details><summary>📄 Abstract</summary>
  Audio anti-spoofing systems increasingly combine self-supervised learning, parameter-efficient fine-tuning, and graph-attention-based backends. However, performance gains in such systems are often entangled with concurrent changes in the backbone, fine-tuning strategy, and training protocol, making the independent contribution of graph attention design difficult to isolate. To address this issue, we conduct a systematic controlled study of the graph attention layer under a unified experimental s...
  </details>

- **2026-09-14** — Son Ho, Cédric Fournet, Jonathan Protzenko et al. — [Scaling Verification of Cryptographic Software with Aeneas, Rust, and Lean](http://arxiv.org/abs/2609.15648v1)
  <details><summary>📄 Abstract</summary>
  We develop a new methodology for verifying cryptographic software. We target production code written in Rust for performance and system integration, rather than verification convenience. Rust's ownership discipline enables Aeneas to extract a pure model of this code in Lean, relieving us from low-level reasoning about pointer liveness and aliasing. Lean's extensibility lets us develop tactics and libraries that greatly simplify reasoning about extracted Rust code.   We design and tune our toolch...
  </details>

- **2026-09-14** — Jiawei Li, Fabio Bonassi, Johan Sundström et al. — [On the role of the tokenizer in ECG transformer models](http://arxiv.org/abs/2609.15433v1)
  <details><summary>📄 Abstract</summary>
  Tokenization determines both the physiological content presented to an ECG Transformer and the sequence over which attention operates. We compare eight tokenization strategies across Transformer, Informer, Reformer, and FEDformer on the nine-label CPSC2018 classification task. The input projection and principal backbone capacity are controlled to isolate the effect of token construction. Median-beat and HeartLang tokenization achieve mean macro-AUCs of 0.893 and 0.889 across the four backbones, ...
  </details>

- **2026-09-14** — Haoxiang Kang, Ming Wen — [SkillLift: Learning Dense Rubrics from Sparse Oracles for Efficient Skill Evolution](http://arxiv.org/abs/2609.15396v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents increasingly rely on persistent skills, i.e., reusable procedural prompts, to adapt without weight updates. Existing skill self-evolution methods directly revise skill text based on execution feedback, but each oracle evaluation requires a full agent rollout, creating a supervision bottleneck that confines search to failure-patching updates. Our key insight is that ranking is a smoother supervision target than absolute outcome regression: identifying which skill is better requir...
  </details>

- **2026-09-14** — Xudong Yuan, Shunyu Liu, Tongya Zheng et al. — [CodeTS: Verifiable Text-to-Time Series Generation via Executable Code](http://arxiv.org/abs/2609.15393v1)
  <details><summary>📄 Abstract</summary>
  Text-to-Time Series Generation (Text-to-TS) provides a promising paradigm for synthesizing time series from natural language, enabling scenario-specific generation when real observations are scarce or costly to acquire. However, existing methods typically lack an explicit mechanism for deriving generation logic from textual descriptions to guide time series synthesis. In this paper, we propose CodeTS, a verifiable framework that uses code as an intermediate generation interface, reformulating Te...
  </details>

- **2026-09-14** — Konstantinos Varsos, Ramin Khalili, Adamantia Stamou et al. — [A Game-Theoretic Framework for Incentive-Compatible AI training Under Renewable-Energy Constraints](http://arxiv.org/abs/2609.15389v1)
  <details><summary>📄 Abstract</summary>
  As artificial intelligence systems increasingly rely on distributed and collaborative training, the energy footprint of these processes becomes a shared responsibility. Modern AI training often unfolds across heterogeneous compute nodes-ranging from cloud clusters to edge devices-whose energy availability is spatially and temporally variable. At the same time, renewable energy grids experience growing levels of excess generation, creating opportunities to align computational workloads with low-c...
  </details>

- **2026-09-14** — Xinyue Xu, Hongbin Lin, Juangui Xu et al. — [Concept-Grounded Reasoning with Prompt-Driven Localization for Interpretable Structured Report Generation](http://arxiv.org/abs/2609.15334v1)
  <details><summary>📄 Abstract</summary>
  Medical imaging modalities such as ultrasound and X-ray are widely used in clinical practice, where diagnosis follows a structured, evidence-driven workflow aligned with standardized criteria. While multimodal large language models (MLLMs) show promise for automated medical report generation, most existing systems rely on end-to-end multimodal fusion without modeling clinically defined intermediate attributes, leading to limited grounding and interpretability. To address this issue, we propose C...
  </details>

- **2026-09-14** — Chanho Park, Bumsu Park, Soonhee Kwon et al. — [Thinking in Tokens, Talking in Bits: A Practical Interface for Token Communication](http://arxiv.org/abs/2609.15256v1)
  <details><summary>📄 Abstract</summary>
  Advanced artificial intelligence models think in tokens; contemporary communication systems carry bits. The direct way to bridge this gap is to transmit tokens, but that makes a model-specific representation part of the air interface, coupling the endpoints through a shared tokenizer, codebook, and often a neural transceiver. We take a different route: keep bits in the payload and let tokens control how those bits are generated and protected. The resulting token-bit interface transition aligns t...
  </details>

- **2026-09-14** — Rui Lu, Rui Ge, Huanghuang Liang et al. — [ETCInfer: An Energy-efficient Thermal-aware Cooling-joint Scheduler for LLM Inference in AI Datacenters](http://arxiv.org/abs/2609.15230v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference in AI datacenters creates a coupled control problem between GPU serving and facility cooling. Raising ambient temperature setpoints can reduce cooling energy and carbon, but also shrinks thermal headroom, induces GPU throttling, and leads to Service-Level-Objective (SLO) violations. In this paper, we study joint cooling--computing control for LLM inference: minimizing per-job GPU-plus-cooling energy while satisfying thermal safety and latency SLO constraints....
  </details>

- **2026-09-14** — Juntong Zhang, Chun Gu, Li Zhang — [X-WBC: A Cross-Embodiment Foundation Model for Humanoid Whole-Body Control](http://arxiv.org/abs/2609.15213v1)
  <details><summary>📄 Abstract</summary>
  Scaling humanoid whole-body control toward general-purpose deployment requires large human motion corpora and training experience shared across robot bodies. Existing methods usually train one policy per robot, leaving motion experience isolated across embodiments. We introduce X-WBC, a cross-embodiment foundation framework that separates relatively shared human motion semantics from embodiment-specific physical execution. Human-centered command tokens align full human motion, robot reference mo...
  </details>

- **2026-09-14** — Sriram Selvam, Anneswa Ghosh — [CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search](http://arxiv.org/abs/2609.15164v1)
  <details><summary>📄 Abstract</summary>
  When several retrieved sources support the same claim, an answer engine cites some but not others. We call this decision citation allocation and introduce CITECHOICE, a causal audit of authentic multi-turn agentic search. From 129 everyday-query transcripts, CITECHOICE selects 113 same-call document pairs with independently verified support for the same pre-specified fact, without observing ranks or answer outcomes; blinded human review confirms 103. It runs a hash-verified 2-by-2 replay crossin...
  </details>

- **2026-09-14** — Siran Zhang, Shuming Cheng, Xiang Li et al. — [A train--prune--readout--rewrite workflow for interpretable quantum learning](http://arxiv.org/abs/2609.15139v1)
  <details><summary>📄 Abstract</summary>
  AI for Science aims not only to predict complex physical systems from data, but also to extract mathematical structure and physically testable representations from learned models. Here, a train--prune--readout--rewrite workflow is developed that separates physical-domain grounding from three increasingly stringent analysis claims: algebraically equivalent readout of a trained predictor, compact teacher-faithful symbolic rewriting on the sampled physical domain, and transformation-based tests of ...
  </details>

- **2026-09-14** — Yunhao Feng, Ruixiao Lin, Ming Wen et al. — [HazardAuditor: From Executable Threats to Safer Computer-Use Agents](http://arxiv.org/abs/2609.15134v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents increasingly interact with browsers, terminals, file systems, and external services, introducing safety risks that emerge through runtime behavior rather than generated content alone. Existing guard models target static prompts and responses and are poorly suited to agent execution; existing executable safety platforms produce evaluation verdicts rather than the normalized supervision a guard model needs to learn across heterogeneous agent frameworks. We introduce HazardAudit...
  </details>

- **2026-09-14** — Kushagra Agrawal, Yuming Feng, Man-Fai Leung — [Translating the Translator: Decomposing the Cost of English-Forced Inter-Agent Communication](http://arxiv.org/abs/2609.15079v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM architectures, such as LangChain and AutoGen, largely assume English as the lingua franca for internal inter-agent communication, even when the end-user task is non-English. We fill this gap by evaluating a two-agent extraction-answer core, with an additional back-translation agent in the English-forced condition, across four typologically diverse languages (Hindi, Chinese, Spanish, Arabic; n = 300 per language) using the Aya-23-8B model. We compare a native-language pipeline to ...
  </details>

- **2026-09-14** — Yu Li, Qikun Cai, Tao Huang et al. — [Semantic-TVM: Structure-Preserving Trustworthy Virtual Memory for Memory-Augmented and Tool-Using Agents](http://arxiv.org/abs/2609.15011v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented and tool-using agents expose exact private values when remote LLMs process retrieved memory, tool actions, and intermediate observations. One-way masking limits direct exposure but removes values needed for trusted execution and can leak them through later observations. We propose Trustworthy Virtual Memory (TVM), a closed-loop runtime that keeps exact-value state local while presenting a protected view to the remote model. Within this single runtime, Rule-TVM replaces whole pro...
  </details>

- **2026-09-14** — Zhendong Li, Mingze Zhu, Zhou Su et al. — [Discrete Antenna Positioning and Beamforming Design for RIS-Assisted MA Secure ISAC Systems](http://arxiv.org/abs/2609.14974v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates a reconfigurable intelligent surface (RIS)-assisted movable antenna (MA) secure integrated sensing and communication (ISAC) system. In this architecture, the RIS establishes indirect transmission links to provide communication services for multiple legitimate users, while the high spatial diversity gain of MA is leveraged to enhance system security. Then, we formulate an optimization problem to maximize the system total secrecy rate by jointly optimizing the MA position s...
  </details>

- **2026-09-14** —  DeepCybo Team, Yu Bin, Haipeng Cao et al. — [PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models](http://arxiv.org/abs/2609.14973v1)
  <details><summary>📄 Abstract</summary>
  We present PhysBrain 1.5, a unified model for understanding physical environments, generating actions, and predicting future states. Motivated by the physical loop of observation, interaction, and environmental change, we bring these capabilities into a common learning framework. Starting from a general vision--language model, we encode language responses, end-effector motion, and dense visual targets as discrete sequences and jointly optimize them with autoregressive next-token prediction. Pre-...
  </details>

- **2026-09-14** — Yahya Mohamed Elnawasany — [A Corpus-Aligned Uthmani-to-Standard Quranic Word Mapping and a Deterministic Recitation Validator](http://arxiv.org/abs/2609.14967v1)
  <details><summary>📄 Abstract</summary>
  Quranic text is distributed in two orthographic forms that are byte-level distinct: the Uthmani script used in every printed mushaf, and the Standard (Imla'i) Arabic form that every mainstream Arabic NLP tool is built for. The gap is concentrated in one Unicode character, U+0670 (superscript alef), which appears in some of the most frequently recited words in the Quran and is silently mishandled by general-purpose Arabic normalizers. We release a 2,290-pair, corpus-aligned Uthmani-to-Standard wo...
  </details>

- **2026-09-14** — Beibei Jing, Tianle Guo, Youjia Zhang et al. — [MoVT: Video-Augmented Motion Tokenizer for Text-to-Motion Generation](http://arxiv.org/abs/2609.14965v1)
  <details><summary>📄 Abstract</summary>
  Text-driven 3D human motion generation models face significant challenges in responding to diverse and unconstrained textual prompts, primarily due to the limited availability of 3D motion training data. To address this, we introduce MoVT, a novel framework that effectively leverages the extensive range of human action videos to enhance text-to-motion generation. At the core of our approach is the cross-modal augmented motion tokenizer, which projects discrete 3D motion tokens into the 2D domain...
  </details>

- **2026-09-14** — Xinjing Zhou, Jason Mohoney, Samuel Madden et al. — [Chronos: Efficient Bolt-on Branching Across Data Stores for Stateful Agentic Applications](http://arxiv.org/abs/2609.14889v1)
  <details><summary>📄 Abstract</summary>
  Data-centric applications increasingly use speculative execution to explore multiple candidate paths where each path modifies state distributed across heterogeneous data stores. This trend is intensified by the rise of tool-calling agents. Hence, applications need data systems that can create branches quickly, isolate state-modifying paths, and merge changes consistently across stores without imposing substantial query overhead. Existing systems provide only partial support, forcing applications...
  </details>

- **2026-09-14** — Haoran Yu, Lifei Liu, Danping Zhang — [Toward Sustainable AI Deployment: A Carbon-Aware Decision Framework for Enterprise Supply Chain Systems](http://arxiv.org/abs/2609.14881v1)
  <details><summary>📄 Abstract</summary>
  Enterprises deploying AI for supply chain decisions commonly default to the largest available language model, a procurement heuristic that neglects both empirical performance and environmental cost. We benchmark six large language models across 520 supply chain tasks, simultaneously measuring decision quality and estimated generation-related operational carbon. Drawing on the Technology-Organization-Environment (TOE) framework, we develop a Carbon-Aware AI Procurement Framework (CAAPF), a Green ...
  </details>

- **2026-09-14** — Tong Zheng, Xidong Wu, Zheng Zhang et al. — [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](http://arxiv.org/abs/2609.14858v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement is becoming increasingly vital for autonomous AI agents, where progress hinges on discovering high-value solutions across complex domains. The driver of this process is effective exploration, however, managing and improving exploration strategies remains a major bottleneck. Current systems face a fundamental dilemma: fixed strategies fail to adapt as search spaces scale, while online policy optimization requires navigating vast meta-search spaces under delayed and expe...
  </details>

- **2026-09-14** — Matteo Grimaldi, David Klee, Ziling Chen et al. — [Touch2Trace: Tactile-Driven Imitation Learning for Dexterous Cable Tracing](http://arxiv.org/abs/2609.15921v1)
  <details><summary>📄 Abstract</summary>
  Dexterous manipulation of deformable objects demands continuous fingertip-level regulation of pressure, friction, and incipient slip. We study one of the most challenging cases: dexterous cable tracing, feeding a cable through the hand with repeated pinch-and-curl motions of the thumb and index finger. We introduce Touch2Trace, a tactile-driven imitation-learning system for this task, and provide, to our knowledge, the first systematic real-world characterization of how encoder pretraining, cont...
  </details>

- **2026-09-14** — Protik Dey, Mohd Saifuzzaman, Taslima Akter — [More Than Just Access: Generative AI as Communication Intermediary for Blind and Low-Vision Users](http://arxiv.org/abs/2609.15696v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) tools are increasingly woven into how blind and low-vision (BLV) people communicate, not only with digital information, but with the physical world and with other people. Tools such as ChatGPT, Google Gemini, Be My AI, and Seeing AI translate visual and textual content into accessible form, and are beginning to substitute for interpersonal requests for help, such as asking a family member to read a label or describe a scene. Drawing on semi-structured interviews with 19 BLV...
  </details>

- **2026-09-14** — Keuntae Kim, Eunhye Jeong, Yong Suk Choi — [CWM: Controllable White-Box Meta-Prompting for Adaptive Retrieval-Augmented Generation and Reasoning Ability](http://arxiv.org/abs/2609.15234v1)
  <details><summary>📄 Abstract</summary>
  Recently, Large Language Models (LLMs) have gained significant attention due to their strong language understanding and generation capabilities, demonstrating impressive reasoning abilities as well as effective utilization of external knowledge. Many studies have proposed methods that specialize in improving performance for individual tasks. However, ironically, only a limited number of attempts have explored general-purpose, task-agnostic methods. In this work, we present a unified framework in...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 629 |
| prompt-injection | 544 |
| memory-poisoning | 49 |
| tool-use-attack | 136 |
| backdoor | 463 |
| adversarial-attack | 596 |
| privacy-leakage | 4102 |
| steganography | 66 |
| misuse | 1022 |
| red-teaming | 125 |
| vulnerability | 3103 |
| defense | 2919 |
| alignment | 2712 |
| robustness | 2839 |
| watermark | 437 |
| unlearning | 95 |
| agent-safety | 54 |
| benchmark | 66 |
| survey | 350 |
| other | 7720 |

---

📚 **全部 28027 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-17 16:04:07*